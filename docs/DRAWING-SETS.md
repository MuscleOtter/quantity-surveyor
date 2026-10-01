# How well can Quantity Surveyor review a huge drawing set?

**Full-set accuracy is not measured yet.** Quantity Surveyor can guide an AI through drawing inventories, quantities, scope checks, revisions and cross-sheet reconciliation. It is suitable as an assistant to a reviewed take-off. We do not have evidence that handing it hundreds of drawings produces a dependable complete estimate without review.

The skill supplies a method. Your app supplies document access, image viewing, OCR/CAD tools, calculation and working storage. The model must actually use those tools and follow the method. Large context capacity alone does not establish that it found all relevant details.

## What makes the task difficult?

| Failure | Control in version 2 |
|---|---|
| Missing or superseded sheets | Compare actual title blocks with the expected index/transmittal; record applicable issue and gaps. |
| Different scales on one sheet | Identify and calibrate each relevant view; do not scale NTS or unresolved views. |
| Relevant information on another sheet | Follow plans, sections, details, schedules, specifications and matchlines; record unresolved dependencies. |
| Double counts or missed items | Distinguish physical instances from repeated depictions; reconcile schedules and sweep for missed candidates. |
| Losing progress across a large set | Work in bounded batches and keep a resumable evidence/coverage register. |
| Reusing stale findings after a revision | Invalidate affected records and linked quantities; preserve prior evidence and show deltas. |
| Correct arithmetic on incomplete scope | Report completeness separately from calculation checks. |

The [full workflow](../skills/quantity-surveyor/references/large-drawing-sets.md) includes two blank spreadsheet templates. No new parser, detector, remote service or database is installed.

## What can it grade?

It can review evidence supporting quantities and costs: coverage, inconsistent dimensions, missing references, schedule/plan disagreements, duplicated scope and unpriced obligations. It can flag design questions. It cannot certify engineering adequacy, regulatory compliance, constructability or a drawing set's completeness merely by issuing a score. Those conclusions need the relevant professional and evidence.

## What the existing tests mean

The earlier 9.96448/10 result grades 23 bounded synthetic responses from the pre-version-2 QS instructions. Two small synthetic visual cases also checked drawing interpretation. Neither is a percentage accuracy figure, an evaluation of a huge coordinated set, or a score for the new large-set workflow. There is no verified Claude/open-model accuracy parity. [Evaluation evidence](EVALUATION.md).

## A practical validation plan

1. Select a representative pilot, for example 30–50 sheets across the requested trades, including dense details, schedules, mixed scales, a scan and a revised issue. This size is a proposed starting point, not a validated threshold.
2. Have an independent quantity surveyor prepare and adjudicate the reference using the same issued set and measurement rules. Keep answers hidden from the tested agent.
3. Freeze files, task scope, model/version, host tools and skill release. Run the workflow and retain source locators, outputs, failures and human corrections.
4. Measure sheet/reference retrieval, scope omissions, duplicate counts, detection precision and recall, and absolute/relative quantity error by trade and unit. For a zero reference use absolute error. If comparing cost, hold rates constant. Do not net positive errors against missing scope.
5. Report review time and corrective effort as well as quantities. Separate confirmed work from unresolved coverage. Set acceptable tolerances with the project owner/QS before testing; there is no universal safe percentage.
6. Repeat on a substantially larger unseen set and a revision before drawing a scale-up conclusion. Compare a baseline run with and without the skill under equivalent conditions.

[Research notes](RESEARCH.md) describe the public projects we inspected and what we did—and did not—adopt.

## A useful first request

> Use Quantity Surveyor to inventory this drawing set for a door take-off. Establish the applicable issue, reconcile the drawing index to the actual files, identify relevant plans/schedules/details and report missing dependencies. Then review a representative batch with source evidence before continuing across the set. Keep quantities, coverage and unresolved scope separate.
