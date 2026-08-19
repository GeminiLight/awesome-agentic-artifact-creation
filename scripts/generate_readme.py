#!/usr/bin/env python3
"""Validate the paper catalog and generate the root README deterministically."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

from catalog_analysis import build_chart_outputs, compute_analysis
from venue_registry import load_venues, venue_assignment_error


ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "data" / "papers.csv"
TAXONOMY_PATH = ROOT / "data" / "taxonomy.json"
HEADER_PATH = ROOT / "data" / "header.md"
FOOTER_PATH = ROOT / "data" / "footer.md"
README_PATH = ROOT / "README.md"
STATS_MARKER = "<!-- catalog-stats -->"
BADGES_MARKER = "<!-- catalog-badges -->"

REQUIRED_COLUMNS = (
    "artifact_family",
    "artifact_type",
    "artifact_subtype",
    "application_domain",
    "application_subdomain",
    "venue_id",
    "venue_display_name",
    "venue_full_name",
    "venue_kind",
    "parent_venue_id",
    "year",
    "type",
    "entry_kind",
    "name",
    "title",
    "link",
    "authors",
    "code",
    "bib_key",
)
ALLOWED_TYPES = {"preprint", "published", "project"}
ALLOWED_ENTRY_KINDS = {"system", "benchmark"}


class CatalogValidationError(ValueError):
    """Raised when catalog data cannot be rendered safely."""


def heading_anchor(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def markdown_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("*", "\\*")


def paper_sort_key(paper: dict[str, str]) -> tuple[int, str, str]:
    return (
        -int(paper["year"]),
        paper["venue_display_name"].casefold(),
        paper["title"].casefold(),
    )


def load_taxonomy(path: Path = TAXONOMY_PATH) -> dict[str, list[dict[str, object]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    families = payload.get("artifact_families")
    domains = payload.get("application_domains")
    if not isinstance(families, list) or not families:
        raise CatalogValidationError(
            "taxonomy must contain a non-empty artifact_families list"
        )
    if not isinstance(domains, list) or not domains:
        raise CatalogValidationError(
            "taxonomy must contain a non-empty application_domains list"
        )

    family_names: set[str] = set()
    artifact_paths: set[tuple[str, str, str]] = set()
    for family in families:
        family_name = family.get("name")
        artifact_types = family.get("types")
        if not isinstance(family_name, str) or not family_name.strip():
            raise CatalogValidationError("each artifact family needs a name")
        if family_name in family_names:
            raise CatalogValidationError(f"duplicate artifact family: {family_name}")
        if not isinstance(artifact_types, list) or not artifact_types:
            raise CatalogValidationError(
                f"artifact family has no types: {family_name}"
            )
        family_names.add(family_name)
        type_names: set[str] = set()
        for artifact_type in artifact_types:
            type_name = artifact_type.get("name")
            subtypes = artifact_type.get("subtypes")
            if not isinstance(type_name, str) or not type_name.strip():
                raise CatalogValidationError(
                    f"invalid artifact type in family: {family_name}"
                )
            if type_name in type_names:
                raise CatalogValidationError(
                    f"duplicate artifact type: {family_name} / {type_name}"
                )
            if not isinstance(subtypes, list):
                raise CatalogValidationError(
                    f"artifact type needs a subtypes list: {family_name} / {type_name}"
                )
            type_names.add(type_name)
            artifact_paths.add((family_name, type_name, ""))
            for subtype in subtypes:
                if not isinstance(subtype, str) or not subtype.strip():
                    raise CatalogValidationError(
                        f"invalid artifact subtype: {family_name} / {type_name}"
                    )
                path_key = (family_name, type_name, subtype)
                if path_key in artifact_paths:
                    raise CatalogValidationError(
                        "duplicate artifact taxonomy path: " + " / ".join(path_key)
                    )
                artifact_paths.add(path_key)

    domain_names: set[str] = set()
    for domain in domains:
        domain_name = domain.get("name")
        subdomains = domain.get("subdomains")
        if not isinstance(domain_name, str) or not domain_name.strip():
            raise CatalogValidationError("each application domain needs a name")
        if domain_name in domain_names:
            raise CatalogValidationError(
                f"duplicate application domain: {domain_name}"
            )
        if not isinstance(subdomains, list):
            raise CatalogValidationError(
                f"application domain needs a subdomains list: {domain_name}"
            )
        domain_names.add(domain_name)
        for subdomain in subdomains:
            if not isinstance(subdomain, str) or not subdomain.strip():
                raise CatalogValidationError(
                    f"invalid application subdomain: {domain_name}"
                )
    return {"artifact_families": families, "application_domains": domains}


def _duplicate_values(rows: list[dict[str, str]], field: str) -> list[str]:
    counts = Counter(row[field].casefold() for row in rows if row[field])
    return sorted(value for value, count in counts.items() if count > 1)


def load_papers(
    path: Path = PAPERS_PATH,
    taxonomy: dict[str, list[dict[str, object]]] | None = None,
    venues: dict[str, dict[str, str]] | None = None,
) -> list[dict[str, str]]:
    taxonomy = taxonomy or load_taxonomy()
    venues = venues or load_venues()
    valid_artifact_paths = {
        (family["name"], artifact_type["name"], subtype)
        for family in taxonomy["artifact_families"]
        for artifact_type in family["types"]
        for subtype in ["", *artifact_type["subtypes"]]
    }
    valid_artifact_paths.update(
        (family["name"], "", "") for family in taxonomy["artifact_families"]
    )
    valid_application_paths = {
        (domain["name"], subdomain)
        for domain in taxonomy["application_domains"]
        for subdomain in ["", *domain["subdomains"]]
    }

    with path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        missing_columns = [
            column for column in REQUIRED_COLUMNS if column not in (reader.fieldnames or [])
        ]
        if missing_columns:
            raise CatalogValidationError(
                "missing required columns: " + ", ".join(missing_columns)
            )
        unexpected_columns = [
            column
            for column in (reader.fieldnames or [])
            if column not in REQUIRED_COLUMNS
        ]
        if unexpected_columns:
            raise CatalogValidationError(
                "unexpected catalog columns: " + ", ".join(unexpected_columns)
            )
        rows = [
            {column: (row.get(column) or "").strip() for column in REQUIRED_COLUMNS}
            for row in reader
        ]

    if not rows:
        raise CatalogValidationError("paper catalog is empty")

    for line_number, row in enumerate(rows, start=2):
        required_values = [
            "venue_id",
            "venue_display_name",
            "venue_full_name",
            "venue_kind",
            "year",
            "type",
            "entry_kind",
            "name",
            "title",
            "link",
            "authors",
            "bib_key",
        ]
        blank = [field for field in required_values if not row[field]]
        if blank:
            raise CatalogValidationError(
                f"row {line_number} has blank required fields: {', '.join(blank)}"
            )
        artifact_path = (
            row["artifact_family"],
            row["artifact_type"],
            row["artifact_subtype"],
        )
        application_path = (
            row["application_domain"],
            row["application_subdomain"],
        )
        if not row["artifact_family"] and (
            row["artifact_type"] or row["artifact_subtype"]
        ):
            raise CatalogValidationError(
                f"row {line_number} has artifact fields without an artifact_family"
            )
        if row["artifact_family"] and artifact_path not in valid_artifact_paths:
            raise CatalogValidationError(
                f"row {line_number} uses an unknown artifact taxonomy path: "
                + " / ".join(artifact_path)
            )
        if not row["application_domain"] and row["application_subdomain"]:
            raise CatalogValidationError(
                f"row {line_number} has an application_subdomain without a domain"
            )
        if row["application_domain"] and application_path not in valid_application_paths:
            raise CatalogValidationError(
                f"row {line_number} uses an unknown application taxonomy path: "
                + " / ".join(application_path)
            )
        if not row["artifact_family"] and not row["application_domain"]:
            raise CatalogValidationError(
                f"row {line_number} has no artifact or application classification"
            )
        if not re.fullmatch(r"\d{4}", row["year"]):
            raise CatalogValidationError(f"row {line_number} has an invalid year")
        if row["type"] not in ALLOWED_TYPES:
            raise CatalogValidationError(f"row {line_number} has an invalid type")
        venue_error = venue_assignment_error(row["venue_id"], row["type"], venues)
        if venue_error:
            raise CatalogValidationError(f"row {line_number} has {venue_error}")
        venue = venues[row["venue_id"]]
        venue_fields = {
            "venue_display_name": "display_name",
            "venue_full_name": "full_name",
            "venue_kind": "venue_kind",
            "parent_venue_id": "parent_venue_id",
        }
        mismatched = [
            field
            for field, venue_field in venue_fields.items()
            if row[field] != venue[venue_field]
        ]
        if mismatched:
            raise CatalogValidationError(
                f"row {line_number} has stale derived venue fields: "
                + ", ".join(mismatched)
            )
        if row["type"] == "published" and "arxiv.org" in row["link"].casefold():
            raise CatalogValidationError(
                f"row {line_number} is published but still uses an arXiv link"
            )
        if row["entry_kind"] not in ALLOWED_ENTRY_KINDS:
            raise CatalogValidationError(f"row {line_number} has an invalid entry_kind")
        for field in ("link", "code"):
            if row[field] and not row[field].startswith("https://"):
                raise CatalogValidationError(
                    f"row {line_number} field {field} must use https://"
                )

    for field in ("title", "link", "bib_key"):
        duplicates = _duplicate_values(rows, field)
        if duplicates:
            raise CatalogValidationError(
                f"duplicate {field} values: " + ", ".join(duplicates)
            )
    return rows


def render_statistics(
    papers: list[dict[str, str]],
    taxonomy: dict[str, list[dict[str, object]]],
) -> str:
    analysis = compute_analysis(papers, taxonomy)
    kinds = Counter(paper["entry_kind"] for paper in papers)
    largest_family_index = max(
        range(len(analysis.family_counts)),
        key=analysis.family_counts.__getitem__,
    )
    largest_application_index = max(
        range(len(analysis.application_counts)),
        key=analysis.application_counts.__getitem__,
    )
    top_pairs = ", ".join(
        f"{family} × {application} — **{count}**"
        for family, application, count in analysis.top_pairs[:3]
    )
    return "\n".join(
        [
            "## Catalog Analysis",
            "",
            '<p align="center">',
            (
                '  <img src="visualization/artifact-taxonomy-composition.svg" '
                'alt="Two-level donut chart showing artifact families and '
                'their artifact types" width="100%">'
            ),
            "</p>",
            "",
            '<p align="center">',
            (
                '  <img src="visualization/family-trends.svg" '
                'alt="Stacked bar chart showing yearly paper counts across '
                'the six artifact families" width="100%">'
            ),
            "</p>",
            "",
            '<p align="center">',
            (
                '  <img src="visualization/artifact-application-matrix.svg" '
                'alt="Heatmap of paper counts across artifact families and '
                'application contexts" width="100%">'
            ),
            "</p>",
            "",
            f"- **Catalog coverage:** {analysis.total} papers spanning "
            f"**{analysis.earliest_year}–{analysis.latest_year}**, from "
            f"**{analysis.source_count} publication sources**; "
            f"{kinds['system']} systems and {kinds['benchmark']} benchmarks.",
            f"- **Dual-axis coverage:** {analysis.dual_classified} papers "
            f"(**{analysis.dual_classified / analysis.total:.1%}**) carry both "
            f"artifact and application labels; {analysis.artifact_only} are "
            f"artifact-only and {analysis.application_only} application-only.",
            f"- **Largest artifact family:** "
            f"{analysis.family_names[largest_family_index]} — "
            f"**{analysis.family_counts[largest_family_index]} papers "
            f"({analysis.family_counts[largest_family_index] / analysis.total:.1%})**.",
            f"- **Largest application context:** "
            f"{analysis.application_names[largest_application_index]} — "
            f"**{analysis.application_counts[largest_application_index]} papers "
            f"({analysis.application_counts[largest_application_index] / analysis.total:.1%})**.",
            f"- **Strongest cross-axis concentrations:** {top_pairs}.",
            f"- **System-name coverage:** {analysis.named_systems} of "
            f"{analysis.system_count} systems "
            f"(**{analysis.named_systems / analysis.system_count:.1%}**) have a "
            "verified name.",
        ]
    )


def render_badges(papers: list[dict[str, str]]) -> str:
    venue_count = len({paper["venue_id"] for paper in papers})
    kinds = Counter(paper["entry_kind"] for paper in papers)
    return "\n".join(
        [
            "  <p>",
            (
                '    <a href="https://agentic-creation.github.io/"><img '
                'alt="Website — Explore the catalog" '
                'src="assets/badge-website.svg" height="56"></a>&nbsp;&nbsp;'
            ),
            (
                '    <a href="https://github.com/GeminiLight/'
                'agentic-creation-survey"><img alt="Survey paper — Coming soon" '
                'src="assets/badge-paper.svg" height="56"></a>'
            ),
            "  </p>",
            "  <p>",
            (
                f'    <a href="#catalog-analysis"><img alt="Papers: {len(papers)}" '
                f'src="https://img.shields.io/badge/Papers-{len(papers)}-4C9D96'
                '?style=flat-square"></a>'
            ),
            (
                f'    <a href="#catalog-analysis"><img alt="Systems: {kinds["system"]}" '
                f'src="https://img.shields.io/badge/Systems-{kinds["system"]}-55A2D5'
                '?style=flat-square"></a>'
            ),
            (
                f'    <a href="#catalog-analysis"><img alt="Benchmarks: '
                f'{kinds["benchmark"]}" src="https://img.shields.io/badge/'
                f'Benchmarks-{kinds["benchmark"]}-957CC3?style=flat-square"></a>'
            ),
            (
                f'    <a href="#survey-scope"><img alt="Venues: {venue_count}" '
                f'src="https://img.shields.io/badge/Venues-{venue_count}-D58B68'
                '?style=flat-square"></a>'
            ),
            (
                '    <a href="https://github.com/GeminiLight/'
                'awesome-agentic-artifact-creation/commits/main"><img '
                'alt="Last Updated" '
                'src="https://img.shields.io/github/last-commit/GeminiLight/'
                'awesome-agentic-artifact-creation/main?style=flat-square'
                '&amp;label=Updated&amp;color=718DCA"></a>'
            ),
            "  </p>",
        ]
    )


def render_readme(
    papers: list[dict[str, str]],
    taxonomy: dict[str, list[dict[str, object]]],
    header_path: Path = HEADER_PATH,
    footer_path: Path = FOOTER_PATH,
) -> str:
    header = header_path.read_text(encoding="utf-8")
    footer = footer_path.read_text(encoding="utf-8").strip()
    if not footer:
        raise CatalogValidationError(f"footer must not be empty: {footer_path}")
    if header.count(BADGES_MARKER) != 1:
        raise CatalogValidationError(
            f"expected exactly one {BADGES_MARKER!r} marker in {header_path}"
        )
    if header.count(STATS_MARKER) != 1:
        raise CatalogValidationError(
            f"expected exactly one {STATS_MARKER!r} marker in {header_path}"
        )
    header = header.replace(BADGES_MARKER, render_badges(papers))
    header = header.replace(STATS_MARKER, render_statistics(papers, taxonomy)).rstrip()

    papers_by_path: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    for paper in papers:
        if paper["artifact_family"]:
            path = (
                paper["artifact_family"],
                paper["artifact_type"],
                paper["artifact_subtype"],
            )
            papers_by_path.setdefault(path, []).append(paper)
    for rows in papers_by_path.values():
        rows.sort(key=paper_sort_key)

    papers_by_application = {
        domain["name"]: sorted(
            (
                paper
                for paper in papers
                if paper["application_domain"] == domain["name"]
            ),
            key=paper_sort_key,
        )
        for domain in taxonomy["application_domains"]
    }

    lines = [
        header,
        "",
        "<table>",
        '<tr><th colspan="3"><a href="#artifact-centered-view">'
        "📦 Artifact-centered View</a></th></tr>",
    ]
    families = taxonomy["artifact_families"]
    for family_index, family in enumerate(families, start=1):
        family_name = family["name"]
        family_rows = papers_by_path.get((family_name, "", ""), [])
        populated_types = [
            artifact_type
            for artifact_type in family["types"]
            if any(
                papers_by_path.get((family_name, artifact_type["name"], subtype))
                for subtype in ["", *artifact_type["subtypes"]]
            )
        ]
        if not family_rows and not populated_types:
            continue
        lines.append(
            f'<tr><td colspan="3"><strong><a href="#{heading_anchor(family_name)}">'
            f"{family_index}. {family_name}</a></strong></td></tr>"
        )
        for offset in range(0, len(populated_types), 3):
            type_batch = populated_types[offset : offset + 3]
            lines.append("<tr>")
            for artifact_type in type_batch:
                type_name = artifact_type["name"]
                type_index = family["types"].index(artifact_type) + 1
                lines.append(
                    f'<td>&emsp;<a href="#{heading_anchor(type_name)}">'
                    f"{family_index}.{type_index}. {type_name}</a></td>"
                )
            for _ in range(3 - len(type_batch)):
                lines.append("<td></td>")
            lines.append("</tr>")

    lines.append(
        '<tr><th colspan="3"><a href="#application-centered-view">'
        "🎯 Application-centered View</a></th></tr>"
    )
    application_domains = taxonomy["application_domains"]
    for offset in range(0, len(application_domains), 3):
        domain_batch = application_domains[offset : offset + 3]
        lines.append("<tr>")
        for domain_index, domain in enumerate(
            domain_batch, start=offset + 1
        ):
            domain_name = domain["name"]
            lines.append(
                f'<td>&emsp;<a href="#{heading_anchor(domain_name)}">'
                f"A.{domain_index}. {domain_name}</a></td>"
            )
        for _ in range(3 - len(domain_batch)):
            lines.append("<td></td>")
        lines.append("</tr>")
    lines.extend(
        [
            "</table>",
            "",
            '<a id="artifact-centered-view"></a>',
            "",
            "## [📦 Artifact-centered View](#content)",
            "",
            "This primary view organizes papers by the artifact they construct.",
            "",
        ]
    )

    def append_papers(rows: list[dict[str, str]]) -> None:
        for paper_index, paper in enumerate(rows, start=1):
            metadata = [
                f"[{paper['type'].title()}]({paper['link']})",
            ]
            if paper["code"]:
                metadata.append(f"[Code]({paper['code']})")
            metadata.append(f"`{paper['entry_kind'].title()}`")
            if paper["artifact_family"]:
                metadata.append(
                    f"`📦 {markdown_text(paper['artifact_family'])}`"
                )
            if paper["application_domain"]:
                application = markdown_text(paper["application_domain"])
                if paper["application_subdomain"]:
                    application += (
                        f" / {markdown_text(paper['application_subdomain'])}"
                    )
                metadata.append(f"`🎯 {application}`")
            lines.extend(
                [
                    f"{paper_index}. **{markdown_text(paper['title'])}**",
                    "",
                    f"    *{markdown_text(paper['authors'])}*",
                    "",
                    f"    {markdown_text(paper['venue_display_name'])}, "
                    f"{paper['year']}. "
                    + " · ".join(metadata),
                    "",
                ]
            )

    for family in families:
        family_name = family["name"]
        family_rows = papers_by_path.get((family_name, "", ""), [])
        if not family_rows and not any(
            papers_by_path.get((family_name, artifact_type["name"], subtype))
            for artifact_type in family["types"]
            for subtype in ["", *artifact_type["subtypes"]]
        ):
            continue
        lines.extend([f"### [{family_name}](#content)", ""])
        append_papers(family_rows)
        for artifact_type in family["types"]:
            type_name = artifact_type["name"]
            type_rows = papers_by_path.get((family_name, type_name, ""), [])
            subtype_rows = {
                subtype: papers_by_path.get((family_name, type_name, subtype), [])
                for subtype in artifact_type["subtypes"]
            }
            if not type_rows and not any(subtype_rows.values()):
                continue
            lines.extend([f"#### [{type_name}](#content)", ""])
            append_papers(type_rows)
            for subtype, rows in subtype_rows.items():
                if not rows:
                    continue
                lines.extend([f"##### [{subtype}](#content)", ""])
                append_papers(rows)
        lines.append("")

    lines.extend(
        [
            '<a id="application-centered-view"></a>',
            "",
            "## [🎯 Application-centered View](#content)",
            "",
            "This alternate view re-indexes application-classified papers by their "
            "use context. Papers classified on both axes therefore appear in both "
            "views.",
            "",
        ]
    )
    for domain in application_domains:
        domain_rows = papers_by_application[domain["name"]]
        if not domain_rows:
            continue
        lines.extend([f"### [{domain['name']}](#content)", ""])
        append_papers(domain_rows)
    lines.extend(["", footer])
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if README.md or charts do not match the generated catalog",
    )
    args = parser.parse_args()

    taxonomy = load_taxonomy()
    venues = load_venues()
    papers = load_papers(taxonomy=taxonomy, venues=venues)
    rendered = render_readme(papers, taxonomy)
    chart_outputs = build_chart_outputs(papers, taxonomy)
    if args.check:
        stale_paths: list[Path] = []
        current = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""
        if current != rendered:
            stale_paths.append(README_PATH)
        for path, expected in chart_outputs.items():
            current_chart = path.read_text(encoding="utf-8") if path.exists() else ""
            if current_chart != expected:
                stale_paths.append(path)
        if stale_paths:
            stale = ", ".join(str(path.relative_to(ROOT)) for path in stale_paths)
            print(
                f"generated catalog outputs are out of date: {stale}; "
                "run scripts/generate_readme.py",
                file=sys.stderr,
            )
            return 1
        return 0

    README_PATH.write_text(rendered, encoding="utf-8")
    for path, content in chart_outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(
        f"wrote README.md and {len(chart_outputs)} charts from "
        f"{len(papers)} catalog entries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
