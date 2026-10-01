# Frozen synthetic quantity-surveyor evaluation

This independent suite tests a portable professional quantity-surveyor skill across luxury retail interiors/facades and complete freestanding construction. All quantities, prices, projects, contract terms and memory records are invented. No company identities, private projects, development history or existing private fixtures were used.

The suite contains **18 core cases and 5 adversarial held-out cases**. Case inputs are sufficient for the requested calculations or explicitly identify missing evidence. Deliberately contradictory or hostile source content is presented as project evidence, never as an authorized instruction.

## Files and access

| File | Role | Access |
|---|---|---|
| `fixtures.json` | 18 core prompts and supplied data | Assigned blind core tester batch only |
| `oracle.json` | Expected results, invariants and material triggers | Evaluator only; never send to testers |
| `heldout-fixtures.json` | 5 adversarial cases | Custodian until candidate freeze; then separate blind held-out tester |
| `heldout-oracle.json` | Held-out expected results and invariants | Evaluator only; never send to testers |
| `rubric.json` | Frozen anchors, criteria, weights, gates and protocol | Custodian/evaluator; do not dispatch grading notes to testers |
| `validation.json` | Pre-freeze structural/arithmetic verification summary | Custodian/evaluator |
| `frozen.json` | SHA-256 hashes of every other evaluation file | Custodian/evaluator |

Only the relevant fixture records and frozen candidate skill should be sent to runners. Answer files must never be copied into a runner prompt. The custodian must also prevent runners from browsing the evaluation directory for keys. Access rules describe the evaluation protocol; these files are not operating-system access controls.

## Blind execution protocol

1. Before dispatch, freeze and hash the candidate skill and ancillary files separately. Verify the hashes in `frozen.json`.
2. Start fresh independent testers for core batch **QS01–QS09**, core batch **QS10–QS18**, and held-out batch **H01–H05**. A batch tester must begin with no development history, answer keys, previous candidate responses or grades. Twenty-three new conversation agents are not required.
3. Within a batch, answer each case independently using only its current inputs and the candidate skill. Do not carry project data, remembered lessons, inferred new rules, grading feedback or modified skill instructions across cases. Optional-memory cases inject their own synthetic state. Do not enable actual persistence.
4. Record model/reasoning settings, available tools, browsing status, candidate hashes, fixture hash/ID, timestamp, raw response and tool transcript. Keep settings consistent across batches. A fixture word cap includes its substantive prose, table text and code comments; numeric-only table cells and standalone arithmetic formulas are excluded. QS16 has no word cap.
5. Seal primary answers before grading. A fresh critic/evaluator may then read the frozen oracles and rubric, recompute arithmetic and execute QS16 code in a disposable environment. No oracle or grade is sent back to runners while a batch is active.
6. Score all 23 cases; retain unsuccessful or missing responses in the denominator. Any secondary runs are separately labeled robustness results. Never select the best rerun for the primary aggregate.
7. Report dimension scores, case scores, evidence for deductions/material gates, core and held-out means, unrounded aggregate, material failures and pass/fail. State benchmark limits.

The custodian may use independent verification helpers after answers are sealed. Helpers receiving keys are evaluators, not testers. No key-bearing helper may feed an answer or lesson into a runner.

## Frozen scoring

Dimension weights are arithmetic/measurement **20%**, scope boundaries **16%**, costing **12%**, commercial controls **12%**, decision quality **10%**, evidence/uncertainty **10%**, instruction fidelity **10%**, and communication **10%**. For each case, renormalize the same fixed weights over only the applicable dimensions declared in its oracle. Score dimensions in 0.5 increments from 0 to 10; retain unrounded weighted calculations.

Core cases contribute **75%** and held-out cases **25%**, with equal case weights within each partition. Passing requires an aggregate **strictly greater than 9.0**, **zero material failures**, and all 23 cases. High average quality cannot compensate for a material double count, scope omission, unit/scale error, authorization-state error, fabricated evidence, jurisdiction claim, injected instruction or cross-project memory use.

A score of 5 is a *competent certified-estimator-like behavioral reference*, not a credential. A score of 9 is a *top-5%-quality aspiration* with no empirical percentile calibration. Passing this authored synthetic suite does not certify professional status or real-project statutory compliance. Proportionate concise responses can receive full marks; more prose earns no bonus.

Money/quantity/rate tolerances are defined in the oracle files. Legitimate display rounding and equivalent correct methods are accepted. One root numerical error is not repeatedly penalized across every downstream amount. Material gates and case criteria cannot be changed after answers are seen.

## Coverage

The suite covers arithmetic and reconciliation; net/gross areas, governing dimensions, resized drawings, units and procurement waste; supplier/installer/owner interfaces; full-building, site, plant and soft costs; tender scope/tax normalization; approved/instructed/unapproved/rejected changes; commitments, actuals and final forecasts; advance recovery, retention caps/releases and payment timing; productivity rate build-ups, date-specific escalation and source-currency FX; real discounted lifecycle VE; jurisdiction, contractual/professional standards and NRM limits; insufficient evidence; concise owner advice; user-defined coded schedules; and optional memory isolation/recovery.

Held-out cases add contradictory takeoff evidence, duplicate supply allowance replacement, negative changes with lagged cash receipts, hostile tender instructions with fabricated universal legislation, and cross-project memory/integrity traps. Their answer keys remain separate.

## Official-source boundary

The jurisdiction oracle was checked on 2026-10-01 against these official sources:

- [RICS NRM](https://www.rics.org/profession-standards/rics-standards-and-guidance/sector-standards/construction-standards/nrm): describes construction measurement and cost-management guidance.
- [RICS cost prediction professional standard](https://www.rics.org/profession-standards/rics-standards-and-guidance/sector-standards/construction-standards/rics-cost-prediction-professional-statement-global-1st-edition): distinguishes obligations for relevant RICS professionals/regulated firms from universal statutory law.
- [NYC DOB: Obtaining a Permit](https://www.nyc.gov/site/buildings/property-or-business-owner/obtaining-a-permit.page): official local authority starting point for permit verification.

These support the framework/authority distinction, not site-specific compliance or a universal legal conclusion. Current legal statements require current primary evidence. A runner without browsing can pass by giving a useful verification-limited answer rather than inventing a current legal assurance.

## Freeze and revision policy

`frozen.json` hashes all other suite files; it does not hash itself because a self-referential content hash is not possible. Verify hashes before and after execution. Any edit creates a new suite version with new hashes and a documented reason **before** a new candidate run. Do not modify this frozen version, criteria, applicability, weights, expected results or gates in response to candidate performance. Store candidate reports outside this directory to preserve the freeze.
