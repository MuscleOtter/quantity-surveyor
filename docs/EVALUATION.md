# Evaluation and release review

The historical pre-version-2 independent Astra critic graded **all 23 sealed round-2 task outputs at 9.964479813664596/10 (exact 51337/5152), passing the frozen strictly-greater-than-9 rule, with zero material failures**. Core mean 9.952639751552795; held-out mean 10.0. Configured reviewer: **gpt-6-astra, high**; exact tool-exposed model revision unavailable. Read the [actual critic report](../evaluation/round2/astra-critic.md), [all dimension scores](../evaluation/round2/astra-critic.json) and [executed verification](../evaluation/round2/astra-verification.json).

## Version 2: a different evidence boundary

The original version 2 release preserved the assessed six QS references, original templates and memory helper, but added a large-drawing-set reference, two templates and core routing guidance. The old behavioral score does **not** grade those additions or the complete version 2 package.

A separate Astra session (`gpt-6-astra`, high; exact model revision not exposed) answered six frozen text-only probes and reviewed the new workflow. The [cases](../evaluation/v2-drawing-workflow/cases.md), [source hashes](../evaluation/v2-drawing-workflow/frozen.json), [actual answers](../evaluation/v2-drawing-workflow/astra-responses.md) and [review](../evaluation/v2-drawing-workflow/astra-review.md) are retained. The initial reviewed source and subsequent two refinements are distinguished in the [change record](../evaluation/v2-drawing-workflow/changes-after-review.md); the critic verified the final delta separately. Cases cover issue conflicts, mixed scales/repeated depictions, incomplete detection, revision caches, unavailable visual tools and a proportionate simple calculation. The same session answers and then critiques, so this is a bounded instruction check, not independent grading of an unseen test run. No new numeric competence score is assigned.

There were no real drawing PDFs in these probes. Those probes did not evaluate full-set visual accuracy, practical review effort, native host routing or Claude/open-model performance. The later reported Claude smoke check is documented separately below. See the proposed [real-set validation plan](DRAWING-SETS.md).

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

## Historical version 1 distribution

The public release renames only the skill identity/heading, adds license/version/repository metadata, removes the generic in-folder README in favor of root documentation, and adds an optional update section, reference, checker and version manifest. **All six assessed QS references, templates and the memory helper are byte-for-byte unchanged.** The distribution change is recorded in `evaluation/distribution-delta.json`. The score applies to the recorded candidate and outputs; it is not a new behavioral score for the update mechanism or a universal model claim. Packaging, source equivalence, offline/online update policy and release build are verified separately with executable checks. The same configured Astra reviewer also completed a separately labelled [distribution/architecture review](DISTRIBUTION-REVIEW.md), found and independently verified correction of an interrupted HTTP-read defect, and retained the reviewed asset hashes.

The source snapshot is [candidate-round2](../evaluation/candidate-round2/) and its [manifest](../evaluation/candidate-round2-hashes.json). Scored answers/code and hashes are preserved under both rounds. Incidental absolute machine paths in public logs were sanitized; [redaction manifest](../evaluation/public-redactions.json) records before/after hashes. Frozen suite files and scored responses were not redacted. Full original network/tool-response archives were not retained; concise tester provenance and the critic's fresh source verification are available. No private project data, installed private skill memory or proprietary publisher library is distributed.

## Reproduce deterministic checks

From the repository folder, with Python 3.10+:

```text
python3 tools/validate.py
python3 -m unittest discover -s tests -p 'test_updates.py'
python3 tests/test_memory_helper.py --package skills/quantity-surveyor --work work/memory --output work/memory-results
python3 tests/test_missing_primary.py --package skills/quantity-surveyor --work work/recovery --output work/recovery-results
python3 tools/build_release.py --out dist
```

Helpers use only the standard library; tests write synthetic state under the explicitly chosen work folders. Model behavior cannot be reproduced by deterministic scripts alone. A new behavioral evaluation needs fresh appropriately blind cases/testers, retained actual outputs, frozen criteria and independent grading.

## Limits of the evidence

No professional credential, certified-estimator equivalence, human top-5% percentile, real-project validation, market-rate calibration or universal correctness is established. The 5/9 rubric anchors are aspirations/behavioral anchors, not measured human comparisons. The original scored evaluation did not exercise native automatic routing, Claude or open models. The subsequent user-reported Claude smoke check adds limited evidence, not cross-model accuracy parity. Local environment was macOS arm64/Python 3.12.6/Codex desktop; CI results are reported separately when available. The instructions need real evidence, competent models and the tools appropriate to the task.

## Repository rename patch (2.0.1)

Only repository addresses, the checker User-Agent and release metadata change in the installed package. QS instructions, the drawing workflow and templates retain their version 2 content. The four affected version 2 source files are preserved under `evaluation/v2-drawing-workflow/released-candidate/`; validation verifies the original frozen hashes and the exact allowed rename/version delta. Old scored answers are untouched. Update tests verify the new fixed repository boundary, including rejection of legacy or unrelated release URLs. This patch does not assign a new behavioral score.

## Documentation refresh (2.0.2)

Current wording describes construction projects and work packages without the earlier sector specialization. The core description/opening and affected references have bounded wording changes; the [change record](../evaluation/documentation-refresh/README.md) and exact substitutions retain their relationship to the frozen sources. Feature pages explain existing workflows rather than adding a parser, estimating engine or new accuracy claim. Optional-memory instructions clarify storage durability, and update guidance clarifies Claude ZIP installation; helper code is unchanged. Historical cases and their descriptions remain evidence of what was actually tested, not current market positioning.

## Reported Claude smoke check and routing follow-up (2.0.3)

On 1 October 2026 the user reported one native activation in Claude Code and a four-case run on version 2.0.1, all answers correct. The cases came from the published suite. This is smoke/regression evidence, not a new blind benchmark, numeric score or validation of later releases. [Report, provenance and unknowns](../evaluation/claude-smoke-report.md).

Version 2.0.3 addresses the reported friction by separating simple take-off from coordinated drawing review, making standards loading conditional, routing early-stage pricing advice, and linking all six templates directly from SKILL.md. The [routing change record](../evaluation/routing-refresh/README.md) documents the intended selections and exact instruction delta. These changes have not been rerun on Claude in the evidence supplied here.

## Trade/workbook transfer (2.1.0)

The [new evidence record](../evaluation/trade-workbook-refresh/README.md) preserves the prior public package, an explicit additive delta and a newly frozen three-case drawing exercise with a blind evaluator and separate critic. All three fresh drawing cases passed independent mandatory checks. The optional workbook has 30 recorded input-state checks and structural/export checks; its formulas still need verification in the user's spreadsheet application. Historical scores do not apply to these additions; this bounded exercise cannot establish full-set accuracy or general skill lift.
