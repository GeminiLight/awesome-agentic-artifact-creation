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
    "section",
    "group",
    "publisher",
    "year",
    "type",
    "entry_kind",
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


def load_taxonomy(path: Path = TAXONOMY_PATH) -> list[dict[str, object]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    sections = payload.get("sections")
    if not isinstance(sections, list) or not sections:
        raise CatalogValidationError("taxonomy must contain a non-empty sections list")

    names: set[str] = set()
    pairs: set[tuple[str, str]] = set()
    for section in sections:
        name = section.get("name")
        groups = section.get("groups")
        if not isinstance(name, str) or not name.strip():
            raise CatalogValidationError("each taxonomy section needs a name")
        if name in names:
            raise CatalogValidationError(f"duplicate taxonomy section: {name}")
        if not isinstance(groups, list) or not groups:
            raise CatalogValidationError(f"taxonomy section has no groups: {name}")
        names.add(name)
        for group in groups:
            if not isinstance(group, str) or not group.strip():
                raise CatalogValidationError(f"invalid group in taxonomy section: {name}")
            pair = (name, group)
            if pair in pairs:
                raise CatalogValidationError(f"duplicate taxonomy group: {name} / {group}")
            pairs.add(pair)
    return sections


def _duplicate_values(rows: list[dict[str, str]], field: str) -> list[str]:
    counts = Counter(row[field].casefold() for row in rows if row[field])
    return sorted(value for value, count in counts.items() if count > 1)


def load_papers(
    path: Path = PAPERS_PATH,
    taxonomy: list[dict[str, object]] | None = None,
) -> list[dict[str, str]]:
    taxonomy = taxonomy or load_taxonomy()
    valid_pairs = {
        (section["name"], group)
        for section in taxonomy
        for group in section["groups"]
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
        rows = [
            {column: (row.get(column) or "").strip() for column in REQUIRED_COLUMNS}
            for row in reader
        ]

    if not rows:
        raise CatalogValidationError("paper catalog is empty")

    for line_number, row in enumerate(rows, start=2):
        required_values = [
            "section",
            "group",
            "publisher",
            "year",
            "type",
            "entry_kind",
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
        if (row["section"], row["group"]) not in valid_pairs:
            raise CatalogValidationError(
                f"row {line_number} uses an unknown taxonomy path: "
                f"{row['section']} / {row['group']}"
            )
        if not re.fullmatch(r"\d{4}", row["year"]):
            raise CatalogValidationError(f"row {line_number} has an invalid year")
        if row["type"] not in ALLOWED_TYPES:
            raise CatalogValidationError(f"row {line_number} has an invalid type")
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
    papers: list[dict[str, str]], taxonomy: list[dict[str, object]]
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
            f"- **{len(taxonomy)} artifact families** and "
            f"**{sum(len(section['groups']) for section in taxonomy)} artifact subtypes**.",
            "",
            "*Sources: `data/audit.csv` and generated `data/papers.csv`.*",
        ]
    )


def render_readme(
    papers: list[dict[str, str]],
    taxonomy: list[dict[str, object]],
    header_path: Path = HEADER_PATH,
) -> str:
    header = header_path.read_text(encoding="utf-8")
    if header.count(STATS_MARKER) != 1:
        raise CatalogValidationError(
            f"expected exactly one {STATS_MARKER!r} marker in {header_path}"
        )
    header = header.replace(STATS_MARKER, render_statistics(papers, taxonomy)).rstrip()

    papers_by_path: dict[tuple[str, str], list[dict[str, str]]] = {}
    for paper in papers:
        papers_by_path.setdefault((paper["section"], paper["group"]), []).append(paper)
    for rows in papers_by_path.values():
        rows.sort(
            key=lambda paper: (
                -int(paper["year"]),
                paper["publisher"].casefold(),
                paper["title"].casefold(),
            )
        )

    lines = [header, "", '<table>', '<tr><th colspan="2">Artifact-centered catalog</th></tr>']
    for section_index, section in enumerate(taxonomy, start=1):
        section_name = section["name"]
        populated_groups = [
            group
            for group in section["groups"]
            if papers_by_path.get((section_name, group))
        ]
        if not populated_groups:
            continue
        lines.append(
            f'<tr><td colspan="2"><strong><a href="#{heading_anchor(section_name)}">'
            f"{section_index}. {section_name}</a></strong></td></tr>"
        )
        for offset in range(0, len(populated_groups), 2):
            lines.append("<tr>")
            for group in populated_groups[offset : offset + 2]:
                group_index = section["groups"].index(group) + 1
                lines.append(
                    f'<td>&emsp;<a href="#{heading_anchor(group)}">'
                    f"{section_index}.{group_index}. {group}</a></td>"
                )
            if offset + 1 >= len(populated_groups):
                lines.append("<td></td>")
            lines.append("</tr>")
    lines.extend(["</table>", ""])

    for section in taxonomy:
        section_name = section["name"]
        if not any(papers_by_path.get((section_name, group)) for group in section["groups"]):
            continue
        lines.extend([f"## [{section_name}](#content)", ""])
        for group in section["groups"]:
            group_rows = papers_by_path.get((section_name, group), [])
            if not group_rows:
                continue
            lines.extend([f"### [{group}](#content)", ""])
            for paper_index, paper in enumerate(group_rows, start=1):
                lines.extend(
                    [
                        f"{paper_index}. **{markdown_text(paper['title'])}**",
                        "",
                        f"    *{markdown_text(paper['authors'])}*",
                        "",
                        f"    {markdown_text(paper['publisher'])}, {paper['year']}. "
                        f"[`{paper['type']}`]({paper['link']}) · `{paper['entry_kind']}`"
                        + (f", [`code`]({paper['code']})" if paper["code"] else ""),
                        "",
                    ]
                )
        lines.append("")
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
