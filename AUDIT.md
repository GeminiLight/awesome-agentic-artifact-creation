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

`data/papers.csv` is generated from the two inclusion verdicts. Artifact and
application classifications are independent: a row may carry either axis or
both, while unknown or inapplicable classification cells remain empty. Pending
and excluded records remain visible in the audit ledger so that count changes
are reviewable rather than silent.

## Current audit result

| Verdict | Count |
|---|---:|
| Included systems | 162 |
| Included benchmarks | 15 |
| Pending full-text review | 9 |
| Excluded | 20 |
| Audited candidates | 206 |

Two entries originally labeled as systems are published as benchmarks in this
catalog. The initial audit replaced the provisional “144 systems + 9
benchmarks” description with “130 systems + 11 benchmarks.” A subsequent
family-gap audit added three full-text-verified produced-audio systems. The
Chapter 5 import then audited 50 application-specific supporting works, adding
29 systems and 4 benchmarks to the public catalog while retaining all 206
decisions in the ledger.

## Limitations

This is a structured first-pass audit, not an independent dual-review study.
Most decisions rely on abstracts, and publication metadata can change. A
reclassification should cite the relevant method evidence in a pull request,
update `data/audit.csv`, rebuild the public catalog, and pass the repository
checks.
