#!/usr/bin/env python3
"""Load and validate the controlled publication-venue registry."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VENUES_PATH = ROOT / "data" / "venues.csv"
VENUE_COLUMNS = (
    "venue_id",
    "display_name",
    "full_name",
    "venue_kind",
    "parent_venue_id",
    "catalog_status",
)
ALLOWED_VENUE_KINDS = {
    "conference",
    "journal",
    "workshop",
    "track",
    "preprint_server",
    "repository",
}
ALLOWED_CATALOG_STATUSES = {"include", "hold"}
ALLOWED_KINDS_BY_PUBLICATION_TYPE = {
    "published": {"conference", "journal", "workshop", "track"},
    "preprint": {"preprint_server"},
    "project": {"repository"},
}


class VenueValidationError(ValueError):
    """Raised when the venue registry is malformed or inconsistent."""


def load_venues(path: Path = VENUES_PATH) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if tuple(reader.fieldnames or ()) != VENUE_COLUMNS:
            raise VenueValidationError(
                "venue columns must be exactly: " + ", ".join(VENUE_COLUMNS)
            )
        rows = [
            {column: (row.get(column) or "").strip() for column in VENUE_COLUMNS}
            for row in reader
        ]

    if not rows:
        raise VenueValidationError("venue registry is empty")

    venues: dict[str, dict[str, str]] = {}
    display_names: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        required = [
            "venue_id",
            "display_name",
            "full_name",
            "venue_kind",
            "catalog_status",
        ]
        blank = [field for field in required if not row[field]]
        if blank:
            raise VenueValidationError(
                f"venue row {line_number} has blank required fields: "
                + ", ".join(blank)
            )
        venue_id = row["venue_id"]
        if not re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)*", venue_id):
            raise VenueValidationError(
                f"venue row {line_number} has an invalid venue_id: {venue_id}"
            )
        if venue_id in venues:
            raise VenueValidationError(f"duplicate venue_id: {venue_id}")
        display_key = row["display_name"].casefold()
        if display_key in display_names:
            raise VenueValidationError(
                f"duplicate venue display_name: {row['display_name']}"
            )
        if row["venue_kind"] not in ALLOWED_VENUE_KINDS:
            raise VenueValidationError(
                f"venue row {line_number} has an invalid venue_kind"
            )
        if row["catalog_status"] not in ALLOWED_CATALOG_STATUSES:
            raise VenueValidationError(
                f"venue row {line_number} has an invalid catalog_status"
            )
        venues[venue_id] = row
        display_names.add(display_key)

    for venue_id, venue in venues.items():
        parent_id = venue["parent_venue_id"]
        if parent_id and parent_id not in venues:
            raise VenueValidationError(
                f"venue {venue_id} has an unknown parent_venue_id: {parent_id}"
            )
        if parent_id == venue_id:
            raise VenueValidationError(f"venue {venue_id} cannot parent itself")

    for venue_id in venues:
        trail: set[str] = set()
        current_id = venue_id
        while current_id:
            if current_id in trail:
                raise VenueValidationError(
                    f"venue parent cycle detected at: {current_id}"
                )
            trail.add(current_id)
            current_id = venues[current_id]["parent_venue_id"]

    return venues


def venue_assignment_error(
    venue_id: str,
    publication_type: str,
    venues: dict[str, dict[str, str]],
) -> str | None:
    venue = venues.get(venue_id)
    if venue is None:
        return f"unknown venue_id: {venue_id}"
    allowed_kinds = ALLOWED_KINDS_BY_PUBLICATION_TYPE.get(publication_type)
    if allowed_kinds is None:
        return None
    if venue["venue_kind"] not in allowed_kinds:
        return (
            f"venue_id {venue_id} has kind {venue['venue_kind']}, which is "
            f"incompatible with publication type {publication_type}"
        )
    return None
