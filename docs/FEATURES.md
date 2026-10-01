# Quantity Surveyor features

Quantity Surveyor helps an AI work through construction quantities, estimates and commercial cost records for new buildings, renovations, individual packages and associated site works. Choose the deliverable you need and supply the relevant evidence. The skill should perform supported work, show its basis and identify material gaps.

These are instructed workflows, not guaranteed automated functions. The host supplies document access, visual reading, calculation and export tools. A text-only chat can work from supplied dimensions and tables; a drawing take-off needs appropriate visual tools. [Compatibility](COMPATIBILITY.md) explains those requirements.

## 1. Drawing-set review and revision tracking

**Supply:** the issued drawings, drawing index/transmittal, relevant specifications and schedules, and the trade/building/floor to review.

**Work:** reconcile listed sheets with actual files; identify missing, duplicate and superseded sheets; establish the applicable issue; follow plan/detail/schedule references; calibrate each measured viewport using a known dimension and an independent check, with tolerance selected before verification; record inspected and unresolved areas. For revisions, recheck affected quantities and linked documents while retaining the previous evidence.

**Receive:** a drawing register, review coverage statement, unresolved-reference list and, when supported, a revision comparison with additions, removals and net changes. Large sets can be reviewed in batches with saved progress.

**Boundary:** uploading or extracting text is not proof that drawings were visually inspected. Huge-set accuracy is unmeasured. [Drawing-set workflow and validation plan](DRAWING-SETS.md).

## 2. Quantity take-off and bills of quantities

**Supply:** readable drawings or explicit dimensions, units, the measurement convention and relevant descriptions/specifications.

**Work:** calculate counts, lengths, areas and volumes; separate repeated locations; apply the supplied deduction rules; distinguish net installed, billed and purchased quantities; show waste and procurement rounding on their own bases. Trace quantities to dimensions, locations and revisions.

**Receive:** a take-off or bill schedule with item IDs, descriptions, calculation strings, quantities, units and source locators, plus unresolved measurement questions. Without prices, the quantity schedule is still useful.

**Boundary:** no guessed image scale or invented dimensions. Formal measurement compliance requires the adopted rule and edition, not just a familiar standard name.

## 3. Estimates, cost plans and rate build-ups

**Supply:** quantities or defined project scope, rates/quotes or permitted evidence sources, location, currency, price date, tax basis and inclusions.

**Work:** extend quantity × rate; build rates from labour, crew output, materials, waste, equipment and other supplied costs; show preliminaries, overhead/profit, fees, owner costs, risk, escalation, currency conversion and tax with explicit bases. Compare estimate revisions by quantity, rate, scope and other stated movements.

**Receive:** an itemized estimate or cost plan, rate calculations, assumptions and exclusions, an unpriced-scope list and a detail-to-total reconciliation.

**Boundary:** no bundled live rate database, automatic contingency percentage or invented productivity. An all-in quote must be checked before adding costs that it may already include.

## 4. Scope coverage and package responsibility

**Supply:** project brief, site boundary, package scopes, inclusions/exclusions and responsibility information.

**Work:** check enabling works, structure, envelope, finishes, building services, site works/utilities, temporary works, access, testing, commissioning and owner costs as relevant. Separate shared costs from individual buildings or packages; assign each inclusion once.

**Receive:** a coverage matrix showing the responsible package, evidence, included/excluded/unpriced status and unresolved interfaces. It makes missing scope visible without pretending every gap has a price.

Trade-specific prompts cover [partitions/ceilings](../skills/quantity-surveyor/references/trade-partitions-ceilings.md), [stone/specialist finishes](../skills/quantity-surveyor/references/trade-finishes.md), [millwork/FF&E](../skills/quantity-surveyor/references/trade-millwork-ffe.md), [facades/glazing](../skills/quantity-surveyor/references/trade-facades-glazing.md) and [services interfaces](../skills/quantity-surveyor/references/trade-services.md). Load only the relevant prompt, and apply the chosen project measurement convention.

## 5. Tender comparison

**Supply:** original bids, qualifications, exclusions, alternatives, commercial terms and the common comparison scope.

**Work:** preserve each submitted total; reconcile supported additions and deductions; align relevant units, currencies, taxes and price dates; distinguish contractor-confirmed changes from client allowances and unpriced exposures. Check requirements before ranking options.

**Receive:** a comparison schedule showing submitted price → evidenced adjustments → comparable amount, qualifications, conditional recommendations and prioritized clarifications.

**Boundary:** an allowance is not a revised contractor offer. Comparing bids does not authorize an award or establish legal entitlement.

## 6. Budget, commitment and final-cost forecasting

**Supply:** approved budget, purchase orders and amendments, paid/accrued records, remaining work, pending changes, cut-off date and definitions of each financial state.

**Work:** distinguish replacement PO totals from incremental amendments; avoid adding payments again to commitments that already contain them; locate changes and risk once in the forecast. Reconcile current forecast to budget and to the previous forecast.

**Receive:** forecast final cost, budget variance with an explicit sign convention, commitment/remaining-work reconciliation and an explanation of movements and unresolved differences.

## 7. Change control

**Supply:** change IDs, source instructions, descriptions, quantities/rates, approval status, associated commitments and current forecast treatment.

**Work:** record each change's pricing basis, revised-total or incremental treatment, responsibility and inclusion in commitments/remaining costs. Keep approval status separate from forecast exposure.

**Receive:** a change log with net forecast effect and queries tied to affected records. Pending exposure remains visible without being represented as approved expenditure.

## 8. Cash-flow planning

**Supply:** programme, work values or milestones, payment terms, deposits/advances, payment lag, retention and release dates.

**Work:** distinguish work value, amounts due and actual payment timing; apply advance recovery and retention movements; extend the forecast for delayed payments and releases.

**Receive:** a period-by-period cash schedule with cumulative totals, remaining retention/advances and reconciliation to the final payment basis.

**Boundary:** it does not silently impose an S-curve or infer contract terms. Owner payments and contractor receipts need an explicit perspective.

## 9. Risk, contingency and value engineering

**Supply:** named risks and supporting assumptions, baseline/options, performance constraints, consequential costs, programme and approval dependencies.

**Work:** separate design gaps, provisional sums, inflation and named risks; show supported scenarios or expected-value calculations when justified. Compare alternatives at equivalent installed scope, including redesign, testing, logistics, programme and maintenance consequences.

**Receive:** a risk/assumption register, transparent scenario allowances, net-savings comparison and decision dependencies.

**Boundary:** a simple range is not a P80 forecast. A cheaper option must still meet the applicable requirements; design equivalence requires evidence.

## 10. Maintenance, renewal and lifecycle costing

**Supply:** asset quantities, tasks/frequencies, service-life evidence, event costs, analysis period, discount/inflation basis and residual/disposal assumptions.

**Work:** schedule maintenance and replacement events; distinguish real and nominal money; apply the selected discount/timing convention; include residual credits and check study-period boundaries. Test sensitivities that could change the choice.

**Receive:** an event schedule, capital/maintenance/renewal subtotals, present-value comparison and sensitivities.

**Boundary:** a reference life is not a surveyed remaining life. Lower cost does not establish lower carbon; carbon needs its own data and units.

## 11. Cost coding and evidence trails

**Supply:** your company code definitions, approved version and any authorized crosswalks. Private configuration and original import paths stay outside the skill.

**Work:** distinguish measurement classifications, procurement packages and financial codes. Preserve confirmed, provisional and unallocated amounts, including credits, while checking that mappings retain the total. Keep assumptions and queries tied to affected items.

**Receive:** coded schedules, unresolved mappings, source/revision references and a reconciliation. Matching labels or number suffixes alone do not establish a valid mapping.

## Templates and file formats

| Supplied template | Purpose |
|---|---|
| [estimate.csv](../skills/quantity-surveyor/templates/estimate.csv) | Quantities, rates, extensions, price evidence, inclusions and coding status. |
| [forecast.csv](../skills/quantity-surveyor/templates/forecast.csv) | Budget, commitments, paid portion, remaining work, changes/risk and variance. |
| [changes.csv](../skills/quantity-surveyor/templates/changes.csv) | Change basis, approval state, commitment link and net forecast effect. |
| [drawing-register.csv](../skills/quantity-surveyor/templates/drawing-register.csv) | File/sheet identity, revision, review stage, disposition and dependencies. |
| [quantity-evidence.csv](../skills/quantity-surveyor/templates/quantity-evidence.csv) | Physical scope/instance, location, method, quantity and evidence status. |
| [project-basis.md](../skills/quantity-surveyor/templates/project-basis.md) | Scope, programme, measurement and pricing assumptions. |
| [estimating-template.xlsx](../skills/quantity-surveyor/assets/templates/estimating-template.xlsx) | Seven linked sheets for basis, drawing evidence, quantities, rates, queries, code allocations and revision checks. [Usage](ESTIMATING-WORKBOOK.md). |

The templates are blank starting points. Your app can populate them, adapt your existing format or return pasteable tables. A formatted XLSX estimating template is supplied. Populating it, recalculating formulas and exporting other spreadsheets or documents depend on your app; verify the saved file before issue. Other schedules above are generated as needed from the task instructions.

## Optional helpers

**Private memory:** record scoped project lessons and corrections in a location you choose; retain provenance and a previous-copy recovery path. Verify that the chosen location survives and is accessible in a later session before promising persistence. Temporary writes are session-only. Memory is off by default and is not encrypted storage or a project database. [Privacy](PRIVACY.md).

**Release checking:** read public GitHub release metadata on request, show whether a newer stable version exists and ask before installation. Optional check-on-use requires the host to retain your explicit preference. No background updater is installed. [Updates](UPDATES.md).

Use [Quickstart](QUICKSTART.md) for example requests and [Evaluation](EVALUATION.md) for the actual testing boundaries.
