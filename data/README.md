# Catalog data

`audit.csv` is the decision ledger. `papers.csv` is derived from its two
inclusion verdicts and is the source rendered into the root `README.md`.

The candidate snapshot combines the 156 entries in
`reference/survey-core-papers.csv` with 50 Chapter 5-only supporting works from
`reference/survey-papers.csv` of the
[Agentic Artifact Creation survey](https://github.com/GeminiLight/agentic-creation-survey).
All 206 records are retained in the decision ledger. The public catalog is
still derived only from `include_system` and `include_benchmark`; importing a
supporting work does not guarantee its inclusion.

## Audit columns

- `artifact_family`, `artifact_type`, and optional `artifact_subtype` record
  what is constructed using the artifact-centered landscape hierarchy.
- `application_domain` and optional `application_subdomain` independently
  record where the work is used. Classification fields are empty when that
  axis does not apply or has not been established; use empty CSV values rather
  than `N/A`.
- `original_role`: `system`, `benchmark`, or `supporting` in the imported
  survey corpus.
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
- `artifact_type`: the artifact profile within the selected family.
- `artifact_subtype`: an optional finer artifact class.
- `application_domain`: an optional application cluster from the survey.
- `application_subdomain`: reserved for a controlled finer application class;
  it remains empty until that taxonomy is defined.
- `publisher`: publication venue or preprint source.
- `year`: four-digit publication year.
- `type`: `preprint`, `published`, or `project`.
- `link`: use the archival conference or journal record for formally published
  work. Use arXiv only when no formal version has been established.
- `entry_kind`: `system` or `benchmark`.
- `name`: evidenced system, benchmark, or primary-method name, or `N/A`.
- `title`, `link`, `authors`: bibliographic display fields.
- `code`: optional implementation URL.
- `bib_key`: stable key inherited from the survey bibliography.

`taxonomy.json` is the controlled vocabulary for both classification axes.
Artifact-only, application-only, and jointly classified rows are valid, but at
least one axis must be populated.

After editing the CSV, run:

```bash
python3 scripts/build_catalog.py
python3 scripts/generate_readme.py
python3 -m unittest discover -s tests
```
