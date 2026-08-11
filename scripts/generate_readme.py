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


ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "data" / "papers.csv"
AUDIT_PATH = ROOT / "data" / "audit.csv"
TAXONOMY_PATH = ROOT / "data" / "taxonomy.json"
HEADER_PATH = ROOT / "data" / "header.md"
README_PATH = ROOT / "README.md"
STATS_MARKER = "<!-- catalog-stats -->"

REQUIRED_COLUMNS = (
    "artifact_family",
    "artifact_type",
    "artifact_subtype",
    "application_domain",
    "application_subdomain",
    "publisher",
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
) -> list[dict[str, str]]:
    taxonomy = taxonomy or load_taxonomy()
    valid_artifact_paths = {
        (family["name"], artifact_type["name"], subtype)
        for family in taxonomy["artifact_families"]
        for artifact_type in family["types"]
        for subtype in ["", *artifact_type["subtypes"]]
    }
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
            "publisher",
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
    years = [int(paper["year"]) for paper in papers]
    kinds = Counter(paper["entry_kind"] for paper in papers)
    with AUDIT_PATH.open(encoding="utf-8-sig", newline="") as source:
        audit_rows = list(csv.DictReader(source))
    verdicts = Counter((row.get("audit_verdict") or "").strip() for row in audit_rows)
    return "\n".join(
        [
            "## Catalog at a glance",
            "",
            f"- **{len(papers)} included papers** spanning **{min(years)}–{max(years)}**.",
            f"- **{kinds['system']} artifact systems** and "
            f"**{kinds['benchmark']} artifact benchmarks**.",
            f"- **{len(audit_rows)} audited candidates**: "
            f"{verdicts['pending_full_text']} pending full-text review and "
            f"{verdicts['exclude']} excluded.",
            f"- **{len(taxonomy['artifact_families'])} artifact families**, "
            f"**{sum(len(family['types']) for family in taxonomy['artifact_families'])} "
            "artifact types**, and "
            f"**{len(taxonomy['application_domains'])} application domains**.",
            f"- **{sum(bool(paper['application_domain']) for paper in papers)} included "
            "papers** currently carry an application classification.",
            "",
            "*Sources: `data/audit.csv` and generated `data/papers.csv`.*",
        ]
    )


def render_readme(
    papers: list[dict[str, str]],
    taxonomy: dict[str, list[dict[str, object]]],
    header_path: Path = HEADER_PATH,
) -> str:
    header = header_path.read_text(encoding="utf-8")
    if header.count(STATS_MARKER) != 1:
        raise CatalogValidationError(
            f"expected exactly one {STATS_MARKER!r} marker in {header_path}"
        )
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
        rows.sort(
            key=lambda paper: (
                -int(paper["year"]),
                paper["publisher"].casefold(),
                paper["title"].casefold(),
            )
        )

    lines = [header, "", '<table>', '<tr><th colspan="2">Artifact-centered catalog</th></tr>']
    families = taxonomy["artifact_families"]
    for family_index, family in enumerate(families, start=1):
        family_name = family["name"]
        populated_types = [
            artifact_type
            for artifact_type in family["types"]
            if any(
                papers_by_path.get((family_name, artifact_type["name"], subtype))
                for subtype in ["", *artifact_type["subtypes"]]
            )
        ]
        if not populated_types:
            continue
        lines.append(
            f'<tr><td colspan="2"><strong><a href="#{heading_anchor(family_name)}">'
            f"{family_index}. {family_name}</a></strong></td></tr>"
        )
        for offset in range(0, len(populated_types), 2):
            lines.append("<tr>")
            for artifact_type in populated_types[offset : offset + 2]:
                type_name = artifact_type["name"]
                type_index = family["types"].index(artifact_type) + 1
                lines.append(
                    f'<td>&emsp;<a href="#{heading_anchor(type_name)}">'
                    f"{family_index}.{type_index}. {type_name}</a></td>"
                )
            if offset + 1 >= len(populated_types):
                lines.append("<td></td>")
            lines.append("</tr>")
    lines.extend(["</table>", ""])

    def append_papers(rows: list[dict[str, str]]) -> None:
        for paper_index, paper in enumerate(rows, start=1):
            application = ""
            if paper["application_domain"]:
                application = (
                    f" · application: `{markdown_text(paper['application_domain'])}`"
                    + (
                        f" / `{markdown_text(paper['application_subdomain'])}`"
                        if paper["application_subdomain"]
                        else ""
                    )
                )
            lines.extend(
                [
                    f"{paper_index}. **{markdown_text(paper['title'])}**",
                    "",
                    f"    *{markdown_text(paper['authors'])}*",
                    "",
                    f"    {markdown_text(paper['publisher'])}, {paper['year']}. "
                    f"[`{paper['type']}`]({paper['link']}) · `{paper['entry_kind']}`"
                    + application
                    + (f", [`code`]({paper['code']})" if paper["code"] else ""),
                    "",
                ]
            )

    for family in families:
        family_name = family["name"]
        if not any(
            papers_by_path.get((family_name, artifact_type["name"], subtype))
            for artifact_type in family["types"]
            for subtype in ["", *artifact_type["subtypes"]]
        ):
            continue
        lines.extend([f"## [{family_name}](#content)", ""])
        for artifact_type in family["types"]:
            type_name = artifact_type["name"]
            type_rows = papers_by_path.get((family_name, type_name, ""), [])
            subtype_rows = {
                subtype: papers_by_path.get((family_name, type_name, subtype), [])
                for subtype in artifact_type["subtypes"]
            }
            if not type_rows and not any(subtype_rows.values()):
                continue
            lines.extend([f"### [{type_name}](#content)", ""])
            append_papers(type_rows)
            for subtype, rows in subtype_rows.items():
                if not rows:
                    continue
                lines.extend([f"#### [{subtype}](#content)", ""])
                append_papers(rows)
        lines.append("")

    application_only = [paper for paper in papers if not paper["artifact_family"]]
    if application_only:
        lines.extend(["## [Application-only and Cross-artifact Work](#content)", ""])
        for domain in taxonomy["application_domains"]:
            domain_rows = [
                paper
                for paper in application_only
                if paper["application_domain"] == domain["name"]
            ]
            if not domain_rows:
                continue
            lines.extend([f"### [{domain['name']}](#content)", ""])
            append_papers(domain_rows)
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if README.md does not match the generated catalog",
    )
    args = parser.parse_args()

    taxonomy = load_taxonomy()
    papers = load_papers(taxonomy=taxonomy)
    rendered = render_readme(papers, taxonomy)
    if args.check:
        current = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""
        if current != rendered:
            print("README.md is out of date; run scripts/generate_readme.py", file=sys.stderr)
            return 1
        return 0

    README_PATH.write_text(rendered, encoding="utf-8")
    print(f"wrote {README_PATH.relative_to(ROOT)} from {len(papers)} catalog entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
