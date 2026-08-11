# Contributing

Thank you for helping maintain Awesome Agentic Artifact Creation.

## Inclusion criteria

A system belongs in the main catalog only when the artifact is persistent
construction state and an intermediate observation can change a later action,
branch, revision, or stopping decision. A fixed multi-agent pipeline is not
agentic under this rule merely because it contains multiple agents or stages.
Benchmarks are assessed separately and are never counted as systems.

Classify artifact and application context as independent axes. Do not use
workflow stage, agent organization, or evaluation method as a peer artifact
taxonomy.

## Add a paper

1. Add one row to `data/audit.csv` using controlled values from
   `data/taxonomy.json`.
2. Populate `artifact_family`, `artifact_type`, and `artifact_subtype` when a
   primary constructed artifact can be assigned. Populate `application_domain`
   and `application_subdomain` independently when the application context is
   established. Leave unknown or inapplicable classification cells empty; do
   not write `N/A`.
3. Prefer a stable publisher or arXiv abstract URL and use HTTPS.
4. Set `name` to the author-assigned system, benchmark, or primary-method name
   stated in the abstract or full text. Use `N/A` if the work does not name
   one; do not derive a label from the title or `bib_key`.
5. Record the evidence basis, criterion, calibrated confidence, and a concise
   operational note. A title is not sufficient evidence.
6. Choose an audit verdict; use `pending_full_text` when the available evidence
   does not establish observation-conditioned construction.
7. Add an official implementation URL in `code` when one is known.
8. Regenerate and validate the catalog:

   ```bash
   python3 scripts/build_catalog.py
   python3 scripts/generate_readme.py
   python3 -m unittest discover -s tests
   ```

Please keep unrelated formatting changes out of catalog updates. For
reclassification proposals, explain why the new artifact family or subtype
better reflects the paper's primary constructed output.
