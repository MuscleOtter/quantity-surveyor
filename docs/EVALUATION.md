# Evaluation and release review

The latest independent Astra critic graded **all 23 sealed round-2 task outputs at 9.964479813664596/10 (exact 51337/5152), passing the frozen strictly-greater-than-9 rule, with zero material failures**. Core mean 9.952639751552795; held-out mean 10.0. Configured reviewer: **gpt-6-astra, high**; exact tool-exposed model revision unavailable. Read the [actual critic report](../evaluation/round2/astra-critic.md), [all dimension scores](../evaluation/round2/astra-critic.json) and [executed verification](../evaluation/round2/astra-verification.json).

## What was evaluated

The original tool-neutral quantity-surveyor-portable candidate was frozen before dispatch. Fresh core-A/core-B testers each answered nine cases; a separate fresh tester answered five held-out cases. Each used independent case inputs with no cross-case memory; batches were not separate new conversations per case. Testers read instructions/references directly and received no evaluator answer keys. The fresh Astra critic saw the actual outputs, frozen fixtures/oracles/rubric and relevant verification evidence, without prior scores or development history. The original inherited tester model identity/reasoning settings were not exposed to the evaluator. The explicitly configured Astra review is a separate reviewer role, not a test of Astra as the estimating model.

The [suite protocol](../evaluation/README.md) fixes applicability/weights and material gates before outputs. The [frozen manifest](../evaluation/frozen.json) protects seven suite files. Eighteen core cases and five held-out cases cover measurement/rate arithmetic, whole-building omissions, bids, amendments/forecast/payment states, escalation/FX, lifecycle timing, jurisdiction, sparse evidence, practical advice, scoped memory and executable normalization. Equal cases within partitions; aggregate = 75% core mean + 25% held-out mean. Applicable dimension weights are normalized per case; dimension increments are 0.5. The suite is narrow and synthetic. Public answer keys are excluded from the installed skill and now make these cases regressions rather than future blind evidence.

## Remaining deductions

- QS04: the scope matrix was complete but longer than the concise brief needed.
- QS13: the distinction between obligations on relevant RICS professionals/firms and universal statutory duties was implied rather than explicit.
- QS16: generated test-answer code raises decimal.InvalidOperation for Decimal NaN instead of its promised ValueError. It rejects the invalid data. All six frozen invalid examples pass; the critic retained the extra edge-case deduction. This normalization function is an evaluated answer, not an executable helper distributed inside the skill.

All 101 independently recomputed consequential numerical comparisons matched; all explicit word caps and frozen/candidate/response hashes passed. These deductions remain in the sealed record; no best-answer substitution was used.

## Defects and improvements

The first output run passed at 9.97373188405797 under a different fresh critic. A separate release audit still found a material optional-memory defect: when the primary disappeared but its previous-copy backup survived, an add could overwrite the backup with an empty store. It was reproduced, fixed and independently tested. Whole-building and utility-verification prompts were also narrowed in response to actual omissions. The complete fresh second output run used the same frozen rubric/oracles. Different critics can give different scores; a higher earlier score is not substituted for the latest result. [Retained defects/corrections](../evaluation/defects-and-corrections.md), [before/after reproduction](../evaluation/reproductions/).

The final independent memory suite passed 13/13 groups (108 subprocess calls), plus the missing-primary regression passed (20 calls), **128 executed CLI calls**. It covers scope isolation, validation, provenance/corrections, restore confirmation, corruption, safe locking and relocated no-package-dependency execution. Astra independently reran both. All successful concurrent writes were retained; competing lock refusals were safe. These are not extra scored QS cases and do not prove exhaustive power-loss or hostile-filesystem security. The current memory helper is unchanged from the assessed hash. [Helper final evidence](../evaluation/helper-final/final-regression-report.md).

Two additional original synthetic image cases were actually viewed by a fresh tester and critic. They cover facade installed/purchased quantities and a civil subset. All 27 independent visual recomputations passed. These add visual-reading evidence, with no primary-score bonus. [Visual review](../evaluation/visual/review.md).

## Published universal distribution

The public release renames only the skill identity/heading, adds license/version/repository metadata, removes the generic in-folder README in favor of root documentation, and adds an optional update section, reference, checker and version manifest. **All six assessed QS references, templates and the memory helper are byte-for-byte unchanged.** The distribution change is recorded in `evaluation/distribution-delta.json`. The score applies to the recorded candidate and outputs; it is not a new behavioral score for the update mechanism or a universal model claim. Packaging, source equivalence, offline/online update policy and release build are verified separately with executable checks. The same configured Astra reviewer also completed a separately labelled [distribution/architecture review](DISTRIBUTION-REVIEW.md), found and independently verified correction of an interrupted HTTP-read defect, and retained the reviewed asset hashes.

The source snapshot is [candidate-round2](../evaluation/candidate-round2/) and its [manifest](../evaluation/candidate-round2-hashes.json). Scored answers/code and hashes are preserved under both rounds. Incidental absolute machine paths in public logs were sanitized; [redaction manifest](../evaluation/public-redactions.json) records before/after hashes. Frozen suite files and scored responses were not redacted. Full original network/tool-response archives were not retained; concise tester provenance and the critic's fresh source verification are available. No private project data, installed private skill memory or proprietary publisher library is distributed.

## Reproduce deterministic checks

From the repository folder, with Python 3.10+:

```text
python3 tools/validate.py
python3 -m unittest discover -s tests -p 'test_updates.py'
python3 tests/test_memory_helper.py --package skills/universal-quantity-surveyor --work work/memory --output work/memory-results
python3 tests/test_missing_primary.py --package skills/universal-quantity-surveyor --work work/recovery --output work/recovery-results
python3 tools/build_release.py --out dist
```

Helpers use only the standard library; tests write synthetic state under the explicitly chosen work folders. Model behavior cannot be reproduced by deterministic scripts alone. A new behavioral evaluation needs fresh appropriately blind cases/testers, retained actual outputs, frozen criteria and independent grading.

## Limits of the evidence

No professional credential, certified-estimator equivalence, human top-5% percentile, real-project validation, market-rate calibration or universal correctness is established. The 5/9 rubric anchors are aspirations/behavioral anchors, not measured human comparisons. No native automatic routing, Claude execution, open-model execution or cross-harness behavior was tested. Local environment was macOS arm64/Python 3.12.6/Codex desktop; CI results are reported separately when available. The instructions need real evidence, competent models and the tools appropriate to the task.
