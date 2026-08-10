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


ROOT = Path(__file__).resolve().parent.parent
AUDIT_PATH = ROOT / "data" / "audit.csv"
PAPERS_PATH = ROOT / "data" / "papers.csv"
TAXONOMY_PATH = ROOT / "data" / "taxonomy.json"

AUDIT_COLUMNS = (
    "section",
    "group",
    "publisher",
    "year",
    "type",
    "original_role",
    "audit_verdict",
    "confidence",
    "evidence_basis",
    "criterion",
    "note",
    "title",
    "link",
    "authors",
    "code",
    "bib_key",
)
PAPER_COLUMNS = (
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
ALLOWED_VERDICTS = {
    "include_system",
    "include_benchmark",
    "pending_full_text",
    "exclude",
}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
ALLOWED_EVIDENCE = {"abstract", "full_text"}
ALLOWED_ORIGINAL_ROLES = {"system", "benchmark"}
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


def load_audit(path: Path = AUDIT_PATH) -> list[dict[str, str]]:
    taxonomy = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))["sections"]
    valid_paths = {
        (section["name"], group)
        for section in taxonomy
        for group in section["groups"]
    }
    with path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        missing = [column for column in AUDIT_COLUMNS if column not in (reader.fieldnames or [])]
        if missing:
            raise AuditValidationError("missing audit columns: " + ", ".join(missing))
        rows = [
            {column: (row.get(column) or "").strip() for column in AUDIT_COLUMNS}
            for row in reader
        ]

    if not rows:
        raise AuditValidationError("audit ledger is empty")

    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        required = [column for column in AUDIT_COLUMNS if column != "code"]
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
        if (row["section"], row["group"]) not in valid_paths:
            raise AuditValidationError(f"row {line_number} has an invalid taxonomy path")
        if not re.fullmatch(r"\d{4}", row["year"]):
            raise AuditValidationError(f"row {line_number} has an invalid year")
        if row["type"] not in ALLOWED_TYPES:
            raise AuditValidationError(f"row {line_number} has an invalid type")
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


def derive_papers(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    included = []
    for row in rows:
        verdict = row["audit_verdict"]
        if verdict not in {"include_system", "include_benchmark"}:
            continue
        included.append(
            {
                "section": row["section"],
                "group": row["group"],
                "publisher": row["publisher"],
                "year": row["year"],
                "type": row["type"],
                "entry_kind": "system" if verdict == "include_system" else "benchmark",
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if data/papers.csv does not match the audited inclusion verdicts",
    )
    args = parser.parse_args()

    audit = load_audit()
    papers = derive_papers(audit)
    rendered = render_papers(papers)
    if args.check:
        current = PAPERS_PATH.read_text(encoding="utf-8") if PAPERS_PATH.exists() else ""
        if current != rendered:
            print("data/papers.csv is out of date; run scripts/build_catalog.py", file=sys.stderr)
            return 1
        return 0

    PAPERS_PATH.write_text(rendered, encoding="utf-8")
    verdicts = Counter(row["audit_verdict"] for row in audit)
    print(
        f"wrote {PAPERS_PATH.relative_to(ROOT)} with {len(papers)} entries "
        f"from {len(audit)} audited candidates ({dict(verdicts)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
