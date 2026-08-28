# Corpus audit

This repository does not treat the survey's original count as an inclusion
guarantee. The initial candidate corpus was re-audited before publication so
that every catalog row is tied to an explicit, reproducible decision.

## Operational inclusion rule

A system is included only when both conditions hold:

1. The artifact is material, persistent construction state rather than a
   disposable model response.
2. At least one intermediate observation can change a later action, branch,
   revision, or stopping decision. Qualifying observations include rendered or
   executed output, critic or verifier feedback, user actions, peer or
   environment state, and persistent memory.

A fixed pipeline does not qualify merely because it contains multiple agents,
models, or stages. Benchmarks are assessed separately and never counted as
systems.

## Evidence and verdicts

The audit uses an evidence ladder:

- `full_text`: the decision was checked against method or system-description
  passages in the paper.
- `abstract`: the abstract contains enough operational detail for a scoped
  decision.

Titles alone are insufficient. When an abstract does not establish
observation-conditioned construction, the item is left as `pending_full_text`
instead of being inferred into the catalog.

Each row in [`data/audit.csv`](data/audit.csv) has one verdict:

- `include_system`: passes the operational system rule.
- `include_benchmark`: primarily evaluates artifact construction.
- `pending_full_text`: plausible, but available evidence is insufficient.
- `exclude`: does not meet the rule or is outside the catalog's scope.

`data/papers.csv` is generated from the two inclusion verdicts for venues whose
`catalog_status` is `include` in `data/venues.csv`. A venue may be placed on
`hold` without changing a paper's technical audit decision. Artifact and
application classifications are independent: a row may carry either axis or
both, while unknown or inapplicable classification cells remain empty. Pending
and excluded records remain visible in the audit ledger so that count changes
are reviewable rather than silent.

## Current audit result

| Verdict | Count |
|---|---:|
| Included systems | 253 |
| Included benchmarks | 33 |
| Pending full-text review | 19 |
| Excluded | 17 |
| Audited candidates | 322 |

Two entries originally labeled as systems are published as benchmarks in this
catalog. The initial audit replaced the provisional “144 systems + 9
benchmarks” description with “130 systems + 11 benchmarks.” A subsequent
family-gap audit added three full-text-verified produced-audio systems. The
Chapter 5 import then audited 50 application-specific supporting works, adding
29 systems and 4 benchmarks. A subsequent 2023--2026 ICLR, ICML, and NeurIPS
review added 31 systems and 8 benchmarks from formal conference records. A
subsequent KDD, The Web Conference, and SIGIR review added 10 systems and 4
benchmarks from formal venue records and retained four plausible candidates
for full-text review. A conservative ACM Multimedia review then added 11
systems from the 2023--2025 proceedings and retained five plausible candidates
for full-text review. A subsequent recency sync reviewed 24 citation-only
works: 20 previously unaudited candidates were added, while four existing
exclusions were reclassified using full-text construction-loop evidence. This
added 19 systems and five benchmarks to the public catalog, bringing the
ledger to 299 decisions. A subsequent corpus-alignment review added DRACO as
a benchmark of structured long-form report construction, bringing the ledger
to 300 decisions. A targeted ICCC, SemEval, and audio-scene review then added
three observation-conditioned construction systems, bringing the ledger to
303 decisions. The August 19 main-track refresh added 16 systems from CVPR,
ICCV, ECCV, ACL, EMNLP, NAACL, and CHI, and added RPGAgent as a pending
full-text case. It also normalized VISTA to CVPR 2026 and corrected archival
track metadata for DeepPresenter, SCMAPR, and DocAgent, bringing the ledger to
320 decisions. The subsequent AutoDesign full-text review added one core
paper-to-poster system with nested artifact-revision and harness-update loops,
bringing the ledger to 321 decisions.

The August 20 Nature refresh upgraded The AI Scientist from its arXiv record
to the 2026 Nature article and added Robin as an application-only scientific
discovery system, bringing the ledger to 322 decisions.

The ICCC, SemEval, Digital Discovery, ACL/EMNLP Findings, and ACL/EMNLP System
Demonstrations venue records remain in the audit ledger but are held from the
generated public catalog. After applying those venue controls, the public
catalog contains 256 entries.

## Synchronization with the survey corpus

This repository and the parent survey use `bib_key` as their stable join key.
They intentionally retain separate authorities: this audit ledger and venue
registry determine public-catalog eligibility, while the parent
`reference/survey-canonical-corpus.csv` determines survey membership and
coding. A publication update may change venue, year, title, or archival link
without renaming its stable key.

A synchronized change updates the bibliography, both source ledgers, and any
new venue record before running `scripts/build_catalog.py`,
`scripts/generate_readme.py`, the parent `build_survey_paper_csv.py`, and their
checks. Derived catalog files and survey views are regenerated; they are not
used to overwrite either source ledger. Any held-venue citation or membership
disagreement must be resolved explicitly.

## Limitations

This is a structured first-pass audit, not an independent dual-review study.
Most decisions rely on abstracts, and publication metadata can change. A
reclassification should cite the relevant method evidence in a pull request,
update `data/audit.csv`, rebuild the public catalog, and pass the repository
checks.
