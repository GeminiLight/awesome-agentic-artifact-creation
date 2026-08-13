#!/usr/bin/env python3
"""Build the zero-dependency GitHub Pages site from the audited catalog."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from collections import Counter
from pathlib import Path

from catalog_analysis import FAMILY_COLORS, compute_analysis
from generate_readme import load_papers, load_taxonomy, paper_sort_key
from venue_registry import load_venues


ROOT = Path(__file__).resolve().parent.parent
SITE_SOURCE = ROOT / "site"
DEFAULT_OUTPUT = ROOT / "_site"


def _count(rows: list[dict[str, str]], field: str, value: str) -> int:
    return sum(row[field] == value for row in rows)


def build_payload() -> dict[str, object]:
    taxonomy = load_taxonomy()
    papers = sorted(load_papers(), key=paper_sort_key)
    venue_registry = load_venues()
    analysis = compute_analysis(papers, taxonomy)
    family_colors = dict(zip(analysis.family_names, FAMILY_COLORS))

    families = []
    for family in taxonomy["artifact_families"]:
        family_name = str(family["name"])
        families.append(
            {
                "name": family_name,
                "count": _count(papers, "artifact_family", family_name),
                "color": family_colors[family_name],
                "types": [
                    {
                        "name": artifact_type["name"],
                        "count": _count(
                            papers, "artifact_type", str(artifact_type["name"])
                        ),
                    }
                    for artifact_type in family["types"]
                ],
            }
        )

    applications = [
        {
            "name": domain["name"],
            "count": _count(papers, "application_domain", str(domain["name"])),
        }
        for domain in taxonomy["application_domains"]
    ]

    years = Counter(paper["year"] for paper in papers)
    venues = Counter(paper["venue_display_name"] for paper in papers)
    publication_venues: Counter[str] = Counter()
    publication_venue_kinds: dict[str, str] = {}
    publication_venue_domains: dict[str, str] = {}
    for paper in papers:
        if paper["type"] != "published":
            continue
        venue_id = paper["parent_venue_id"] or paper["venue_id"]
        venue = venue_registry.get(venue_id)
        venue_name = venue["display_name"] if venue else paper["venue_display_name"]
        publication_venues[venue_name] += 1
        publication_venue_kinds[venue_name] = (
            venue["venue_kind"] if venue else paper["venue_kind"]
        )
        publication_venue_domains[venue_name] = (
            venue["venue_domain"]
            if venue
            else "Interdisciplinary & General Science"
        )
    named_systems = sum(
        paper["entry_kind"] == "system"
        and paper["name"].strip().casefold() not in {"", "n/a", "na", "none"}
        for paper in papers
    )
    public_fields = (
        "artifact_family",
        "artifact_type",
        "artifact_subtype",
        "application_domain",
        "application_subdomain",
        "venue_display_name",
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

    return {
        "summary": {
            "total": analysis.total,
            "systems": analysis.system_count,
            "named_systems": named_systems,
            "benchmarks": analysis.total - analysis.system_count,
            "published": sum(paper["type"] == "published" for paper in papers),
            "dual_classified": analysis.dual_classified,
            "years": len(years),
            "earliest_year": analysis.earliest_year,
            "latest_year": analysis.latest_year,
            "venues": len(venues),
        },
        "families": families,
        "applications": applications,
        "years": [
            {"year": year, "count": years[year]}
            for year in sorted(years, reverse=True)
        ],
        "publication_venues": [
            {
                "name": name,
                "count": count,
                "kind": publication_venue_kinds[name],
                "domain": publication_venue_domains[name],
            }
            for name, count in sorted(
                publication_venues.items(),
                key=lambda item: (-item[1], item[0].casefold()),
            )
        ],
        "papers": [
            {field: paper[field] for field in public_fields} for paper in papers
        ],
    }


def build_site(output: Path = DEFAULT_OUTPUT) -> Path:
    if not SITE_SOURCE.is_dir():
        raise FileNotFoundError(f"site source is missing: {SITE_SOURCE}")

    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(SITE_SOURCE, output)

    data_dir = output / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    (data_dir / "catalog.json").write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    index_path = output / "index.html"
    index = index_path.read_text(encoding="utf-8")
    versioned_assets = (
        "assets/styles.css",
        "assets/app.js",
        "assets/charts.js",
        "data/catalog.json",
    )
    for relative_path in versioned_assets:
        digest = hashlib.sha256((output / relative_path).read_bytes()).hexdigest()[:12]
        index = index.replace(
            f'"{relative_path}"', f'"{relative_path}?v={digest}"'
        )
    index_path.write_text(index, encoding="utf-8")

    (output / ".nojekyll").touch()
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="directory to build (default: _site)",
    )
    args = parser.parse_args()
    output = build_site(args.output.resolve())
    print(f"Built GitHub Pages site at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
