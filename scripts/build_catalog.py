#!/usr/bin/env python3
"""Validate the audit ledger and derive the public paper catalog."""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

from venue_registry import load_venues, venue_assignment_error


ROOT = Path(__file__).resolve().parent.parent
AUDIT_PATH = ROOT / "data" / "audit.csv"
PAPERS_PATH = ROOT / "data" / "papers.csv"
SURVEY_MEMBERSHIP_PATH = ROOT / "data" / "survey_membership.csv"
TAXONOMY_PATH = ROOT / "data" / "taxonomy.json"

AUDIT_COLUMNS = (
    "artifact_family",
    "artifact_type",
    "artifact_subtype",
    "application_domain",
    "application_subdomain",
    "venue_id",
    "year",
    "type",
    "original_role",
    "audit_verdict",
    "confidence",
    "evidence_basis",
    "criterion",
    "note",
    "name",
    "title",
    "link",
    "authors",
    "code",
    "bib_key",
)
PAPER_COLUMNS = (
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
SURVEY_MEMBERSHIP_COLUMNS = (
    "bib_key",
    "artifact_view",
    "application_view",
)
ALLOWED_VERDICTS = {
    "include_system",
    "include_benchmark",
    "pending_full_text",
    "exclude",
}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
ALLOWED_EVIDENCE = {"abstract", "full_text"}
ALLOWED_ORIGINAL_ROLES = {"system", "benchmark", "supporting"}
ALLOWED_TYPES = {"preprint", "published", "project"}
ALLOWED_CRITERIA = {
    "render_execute_feedback",
    "critic_verifier_revision",
    "persistent_state_conditioning",
    "human_or_conversational_feedback",
    "environment_or_peer_observation",
    "benchmark_of_artifact_construction",
    "insufficient_observation_conditioning_evidence",
    "non_agentic_generation_or_evaluation",
    "role_reclassified_to_benchmark",
}


class AuditValidationError(ValueError):
    """Raised when the audit ledger is incomplete or inconsistent."""


def load_taxonomy_paths() -> tuple[set[tuple[str, str, str]], set[tuple[str, str]]]:
    taxonomy = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))
    artifact_paths = {
        (family["name"], artifact_type["name"], subtype)
        for family in taxonomy["artifact_families"]
        for artifact_type in family["types"]
        for subtype in artifact_type["subtypes"]
    }
    artifact_paths.update(
        (family["name"], artifact_type["name"], "")
        for family in taxonomy["artifact_families"]
        for artifact_type in family["types"]
    )
    artifact_paths.update(
        (family["name"], "", "") for family in taxonomy["artifact_families"]
    )
    application_paths = {
        (domain["name"], subdomain)
        for domain in taxonomy["application_domains"]
        for subdomain in domain["subdomains"]
    }
    application_paths.update(
        (domain["name"], "") for domain in taxonomy["application_domains"]
    )
    return artifact_paths, application_paths


def load_audit(
    path: Path = AUDIT_PATH,
    venues: dict[str, dict[str, str]] | None = None,
) -> list[dict[str, str]]:
    valid_artifact_paths, valid_application_paths = load_taxonomy_paths()
    venues = venues or load_venues()
    with path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        missing = [column for column in AUDIT_COLUMNS if column not in (reader.fieldnames or [])]
        if missing:
            raise AuditValidationError("missing audit columns: " + ", ".join(missing))
        unexpected = [
            column for column in (reader.fieldnames or []) if column not in AUDIT_COLUMNS
        ]
        if unexpected:
            raise AuditValidationError(
                "unexpected audit columns: " + ", ".join(unexpected)
            )
        rows = [
            {column: (row.get(column) or "").strip() for column in AUDIT_COLUMNS}
            for row in reader
        ]

    if not rows:
        raise AuditValidationError("audit ledger is empty")

    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        required = [
            column
            for column in AUDIT_COLUMNS
            if column
            not in {
                "artifact_family",
                "artifact_type",
                "artifact_subtype",
                "application_domain",
                "application_subdomain",
                "code",
            }
        ]
        blank = [field for field in required if not row[field]]
        if blank:
            raise AuditValidationError(
                f"row {line_number} has blank required fields: {', '.join(blank)}"
            )
        key = row["bib_key"].casefold()
        if key in seen:
            raise AuditValidationError(f"row {line_number} duplicates bib_key {row['bib_key']}")
        seen.add(key)
        if row["original_role"] not in ALLOWED_ORIGINAL_ROLES:
            raise AuditValidationError(f"row {line_number} has an invalid original_role")
        if row["audit_verdict"] not in ALLOWED_VERDICTS:
            raise AuditValidationError(f"row {line_number} has an invalid audit_verdict")
        if row["confidence"] not in ALLOWED_CONFIDENCE:
            raise AuditValidationError(f"row {line_number} has an invalid confidence")
        if row["evidence_basis"] not in ALLOWED_EVIDENCE:
            raise AuditValidationError(f"row {line_number} has an invalid evidence_basis")
        if row["criterion"] not in ALLOWED_CRITERIA:
            raise AuditValidationError(f"row {line_number} has an invalid criterion")
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
            raise AuditValidationError(
                f"row {line_number} has artifact fields without an artifact_family"
            )
        if row["artifact_family"] and artifact_path not in valid_artifact_paths:
            raise AuditValidationError(
                f"row {line_number} has an invalid artifact taxonomy path"
            )
        if not row["application_domain"] and row["application_subdomain"]:
            raise AuditValidationError(
                f"row {line_number} has an application_subdomain without a domain"
            )
        if row["application_domain"] and application_path not in valid_application_paths:
            raise AuditValidationError(
                f"row {line_number} has an invalid application taxonomy path"
            )
        if not row["artifact_family"] and not row["application_domain"]:
            raise AuditValidationError(
                f"row {line_number} must have an artifact or application classification"
            )
        if not re.fullmatch(r"\d{4}", row["year"]):
            raise AuditValidationError(f"row {line_number} has an invalid year")
        if row["type"] not in ALLOWED_TYPES:
            raise AuditValidationError(f"row {line_number} has an invalid type")
        venue_error = venue_assignment_error(row["venue_id"], row["type"], venues)
        if venue_error:
            raise AuditValidationError(f"row {line_number} has {venue_error}")
        if row["type"] == "published" and "arxiv.org" in row["link"].casefold():
            raise AuditValidationError(
                f"row {line_number} is published but still uses an arXiv link"
            )
        for field in ("link", "code"):
            if row[field] and not row[field].startswith("https://"):
                raise AuditValidationError(
                    f"row {line_number} field {field} must use https://"
                )
        if row["original_role"] == "benchmark" and row["audit_verdict"] == "include_system":
            raise AuditValidationError(
                f"row {line_number} promotes a benchmark to system without a role audit"
            )
        if row["audit_verdict"] == "pending_full_text" and row["confidence"] != "low":
            raise AuditValidationError(
                f"row {line_number} pending_full_text must use low confidence"
            )

    return rows


def derive_papers(
    rows: list[dict[str, str]],
    venues: dict[str, dict[str, str]] | None = None,
) -> list[dict[str, str]]:
    venues = venues or load_venues()
    included = []
    for row in rows:
        verdict = row["audit_verdict"]
        if verdict not in {"include_system", "include_benchmark"}:
            continue
        venue = venues[row["venue_id"]]
        if venue["catalog_status"] != "include":
            continue
        included.append(
            {
                "artifact_family": row["artifact_family"],
                "artifact_type": row["artifact_type"],
                "artifact_subtype": row["artifact_subtype"],
                "application_domain": row["application_domain"],
                "application_subdomain": row["application_subdomain"],
                "venue_id": row["venue_id"],
                "venue_display_name": venue["display_name"],
                "venue_full_name": venue["full_name"],
                "venue_kind": venue["venue_kind"],
                "parent_venue_id": venue["parent_venue_id"],
                "year": row["year"],
                "type": row["type"],
                "entry_kind": "system" if verdict == "include_system" else "benchmark",
                "name": row["name"],
                "title": row["title"],
                "link": row["link"],
                "authors": row["authors"],
                "code": row["code"],
                "bib_key": row["bib_key"],
            }
        )
    return included


def render_papers(rows: list[dict[str, str]]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=PAPER_COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def derive_survey_membership(
    papers: list[dict[str, str]],
) -> list[dict[str, str]]:
    return [
        {
            "bib_key": paper["bib_key"],
            "artifact_view": str(bool(paper["artifact_family"])).lower(),
            "application_view": str(bool(paper["application_domain"])).lower(),
        }
        for paper in papers
    ]


def render_survey_membership(rows: list[dict[str, str]]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=SURVEY_MEMBERSHIP_COLUMNS,
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if generated catalog CSVs do not match the audited records",
    )
    args = parser.parse_args()

    venues = load_venues()
    audit = load_audit(venues=venues)
    papers = derive_papers(audit, venues)
    rendered_papers = render_papers(papers)
    membership = derive_survey_membership(papers)
    rendered_membership = render_survey_membership(membership)
    if args.check:
        stale_paths = []
        for path, expected in (
            (PAPERS_PATH, rendered_papers),
            (SURVEY_MEMBERSHIP_PATH, rendered_membership),
        ):
            current = path.read_text(encoding="utf-8") if path.exists() else ""
            if current != expected:
                stale_paths.append(path.relative_to(ROOT))
        if stale_paths:
            stale = ", ".join(str(path) for path in stale_paths)
            print(
                f"generated catalog CSVs are out of date: {stale}; "
                "run scripts/build_catalog.py",
                file=sys.stderr,
            )
            return 1
        return 0

    PAPERS_PATH.write_text(rendered_papers, encoding="utf-8")
    SURVEY_MEMBERSHIP_PATH.write_text(rendered_membership, encoding="utf-8")
    verdicts = Counter(row["audit_verdict"] for row in audit)
    print(
        f"wrote {PAPERS_PATH.relative_to(ROOT)} with {len(papers)} entries "
        f"and {SURVEY_MEMBERSHIP_PATH.relative_to(ROOT)} from "
        f"{len(audit)} audited candidates ({dict(verdicts)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
