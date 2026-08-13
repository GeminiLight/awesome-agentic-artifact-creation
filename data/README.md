# Catalog data

`audit.csv` is the decision ledger. `papers.csv` is derived from its two
inclusion verdicts for venues currently marked `include` and is the source
rendered into the root `README.md`. `survey_membership.csv` is derived from
`papers.csv` and records which public view or views contain each entry.
`venues.csv` is the controlled registry for publication and source names used
by these files.

The candidate snapshot combines the 156 entries in
`reference/survey-core-papers.csv` with 50 Chapter 5-only supporting works from
`reference/survey-papers.csv` of the
[Agentic Artifact Creation survey](https://github.com/GeminiLight/agentic-creation-survey).
The original 206 records, 39 additional ICLR, ICML, and NeurIPS candidates,
18 additional KDD, The Web Conference, and SIGIR candidates, 16 additional
ACM Multimedia candidates, and later proceedings and arXiv updates are retained
in the 303-row decision ledger. The
public catalog requires both an `include_system` or `include_benchmark` verdict
and an `include` venue status; importing a supporting work does not guarantee
its inclusion.

## Audit columns

- `artifact_family` and optional `artifact_type` / `artifact_subtype` record
  what is constructed using the artifact-centered landscape hierarchy. A
  family-level record leaves both finer fields empty when the manuscript does
  not define a mature profile for that output.
- `application_domain` and optional `application_subdomain` independently
  record where the work is used. Classification fields are empty when that
  axis does not apply or has not been established; use empty CSV values rather
  than `N/A`.
- `venue_id`: stable identifier registered in `venues.csv`. Store the year only
  in `year`; do not create year-specific venue names.
- `original_role`: legacy import provenance (`system`, `benchmark`, or
  `supporting`) retained only for audit traceability. It is not a current
  catalog classification and is not copied into `papers.csv`.
- `audit_verdict`: `include_system`, `include_benchmark`,
  `pending_full_text`, or `exclude`.
- `confidence`: calibrated decision confidence.
- `evidence_basis`: `abstract` or `full_text`; titles are not evidence.
- `criterion` and `note`: the operational reason for the verdict.
- `name`: author-assigned system, benchmark, or primary-method name evidenced
  by the abstract or full text. Use `N/A` when the work does not explicitly
  name one; do not invent a name from the paper title or `bib_key`. It is a
  display field and need not be unique; use `bib_key` as the stable identifier.

See [`../AUDIT.md`](../AUDIT.md) for the inclusion rule and limitations.

## Generated catalog columns

- `artifact_family`: one of the six top-level artifact families.
- `artifact_type`: an optional artifact profile within the selected family.
- `artifact_subtype`: an optional finer artifact class.
- `application_domain`: an optional application cluster from the survey.
- `application_subdomain`: reserved for a controlled finer application class;
  it remains empty until that taxonomy is defined.
- `venue_id`: stable key for the publication venue, track, preprint server, or
  repository defined in `venues.csv`.
- `venue_display_name`, `venue_full_name`, `venue_kind`, and
  `parent_venue_id`: generated venue metadata copied from `venues.csv`. Do not
  edit these fields directly; regenerate `papers.csv` after changing the venue
  registry.
- `year`: four-digit publication year.
- `type`: `preprint`, `published`, or `project`.
- `link`: use the archival conference or journal record for formally published
  work. Use arXiv only when no formal version has been established.
- `entry_kind`: `system` or `benchmark`.
- `name`: evidenced system, benchmark, or primary-method name, or `N/A`.
- `title`, `link`, `authors`: bibliographic display fields.
- `code`: optional implementation URL.
- `bib_key`: stable key inherited from the survey bibliography.

## Survey membership columns

`survey_membership.csv` contains one row for every public `papers.csv` entry:

- `bib_key`: stable key joining the membership row to `papers.csv`.
- `artifact_view`: `true` when the entry has an artifact classification and
  therefore appears in the Artifact-centered View.
- `application_view`: `true` when the entry has an application classification
  and therefore appears in the Application-centered View.

Both view fields may be `true`. This file does not define a `core` versus
`supporting` hierarchy.

`taxonomy.json` is the controlled vocabulary for both classification axes.
`venues.csv` provides the canonical README label, full name, venue kind,
optional parent venue, and `catalog_status` for each `venue_id`. Use `include`
for sources eligible for `papers.csv` and `hold` for sources retained in the
audit ledger but temporarily omitted from the public catalog. Artifact-only,
application-only, and jointly classified rows are valid, but at least one axis
must be populated.

After editing the CSV, run:

```bash
python3 scripts/build_catalog.py
python3 scripts/generate_readme.py
python3 -m unittest discover -s tests
```

The README generator also refreshes the deterministic Catalog Analysis charts
in `visualization/`.

The generated README combines the hand-maintained `header.md` and `footer.md`
with the two catalog views derived from `papers.csv`.
