# Catalog data

`audit.csv` is the decision ledger. `papers.csv` is derived from its two
inclusion verdicts and is the source rendered into the root `README.md`.

The initial snapshot was derived from the 153 core entries in
`reference/survey-papers.csv` of the
[Agentic Artifact Creation survey](https://github.com/GeminiLight/agentic-creation-survey).
The audit includes 130 systems and 11 benchmarks, leaves 7 candidates pending
full-text review, and excludes 5. Supporting and boundary-evidence papers from
outside the candidate set remain in the survey repository and are not silently
mixed into this catalog.

## Audit columns

- Bibliographic and taxonomy fields identify the candidate.
- `original_role`: `system` or `benchmark` in the imported candidate set.
- `audit_verdict`: `include_system`, `include_benchmark`,
  `pending_full_text`, or `exclude`.
- `confidence`: calibrated decision confidence.
- `evidence_basis`: `abstract` or `full_text`; titles are not evidence.
- `criterion` and `note`: the operational reason for the verdict.

See [`../AUDIT.md`](../AUDIT.md) for the inclusion rule and limitations.

## Generated catalog columns

- `section`: one of the six top-level artifact families in `taxonomy.json`.
- `group`: an artifact subtype belonging to the selected family.
- `publisher`: publication venue or preprint source.
- `year`: four-digit publication year.
- `type`: `preprint`, `published`, or `project`.
- `entry_kind`: `system` or `benchmark`.
- `title`, `link`, `authors`: bibliographic display fields.
- `code`: optional implementation URL.
- `bib_key`: stable key inherited from the survey bibliography.

After editing the CSV, run:

```bash
python3 scripts/build_catalog.py
python3 scripts/generate_readme.py
python3 -m unittest discover -s tests
```
