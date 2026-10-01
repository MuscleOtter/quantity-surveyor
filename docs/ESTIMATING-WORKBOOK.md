# Use the estimating workbook

[Download estimating-template.xlsx](https://github.com/MuscleOtter/quantity-surveyor/releases/latest/download/estimating-template.xlsx). It is also included in the skill ZIP under `assets/templates/`. Save a project copy before editing. You can use the workbook without installing the skill or running Python.

The workbook starts without project quantities, rates, codes or percentage allowances. Use your required company format when supplied; a simple calculation can still use one concise schedule. Verify that formulas recalculate in your chosen spreadsheet app, especially after importing or converting the file.

## Start with the basis

Complete Summary with the project/scope, country or locality, currency, rate base date, measurement standard/edition and drawing issue/exclusions. Currency must agree with the linked rates. Record the selected project convention; a standard name does not establish compliance.

Inputs use amber basis cells and blue detail text. Grey detail cells contain calculations. Preserve formulas when entering or pasting inputs.

## Enter evidence and prices

1. **Drawings:** record each drawing/revision/page/viewport, actual visual-review status, scope coverage and calibration evidence. For graphical measurement use a reliable known dimension, an independent check and a tolerance chosen beforehand. A listed drawing is not automatically a reviewed drawing.
2. **Rates:** give each supplied/evidenced rate a unique ID, numeric value, unit, currency, geography, base date and source/locator. State included/excluded scope and choose Supported or Scenario. Missing values stay unresolved; the template does not invent market prices.
3. **Takeoff:** give every scope/location a unique line ID, source/revision, dimension calculation, numeric quantity, unit and quantity basis. Link the Rate ID. Unit and currency must agree before the amount calculates. Repeated descriptions are allowed; repeated IDs are queried.
4. **Queries:** retain missing dimensions, specifications, prices and scope decisions under stable query IDs. Keep an unpriced item in the scope schedule; do not replace an unknown quantity/rate with zero.

A supported explicit zero rate remains valid. A blank or text value such as TBD is unresolved. The Input query columns explain missing data, duplicate IDs and unit/currency differences. Fix the underlying evidence rather than overwriting the calculated amount.

## Read the subtotal honestly

Summary separates measured quantities with supported prices from provisional quantities and scenario prices. The included-cost subtotal excludes unpriced/unmeasured lines. It is a partial cost basis when material scope remains unresolved; it does not approve a budget or establish a forecast final cost.

Add supported preliminaries, fees, risk, inflation or tax as separate item lines with explicit cost bases only where required. Confirm they are outside existing rate inclusions. No default percentage is supplied.

## Optional company coding

Use Codes only when company reporting is needed. Supply the literal code, selected version and complete definition evidence; private mappings/configuration belong outside the skill. Assign Confirmed, Provisional or Unallocated status. Supported split allocations must total 100% for each priced line.

Summary shows code-state subtotals and priced cost without a valid allocation. Reconcile those amounts to the included-cost subtotal. Coding uncertainty does not remove the cost from the estimate; the workbook cannot approve a code, budget transfer or transaction.

## Optional revision bridge

Enter independently established prior and new totals on Revision. Match scope using stable IDs and retain the old/new drawing basis. Quantity effect is (new quantity − prior quantity) × prior rate; rate effect is new quantity × (new rate − prior rate). Record added/removed scope or other evidenced signed movements separately, without double counting.

The unexplained residual compares the independent total movement with the bridge. Investigate a difference instead of forcing both baselines from the same summed result. Missing cause/revision evidence, quantity units or change inputs remain queries. Unpriced scope stays outside the priced bridge.

## Capacity and issue checks

Each detail sheet reserves **100 rows, rows 7–106**. An extra row is not automatically included. Extend every dependent formula, validation, lookup, summary and check range together, or use a suitable larger model.

Before issue, change representative inputs and verify recalculation, query messages, rate inclusions, units/currency, repeated scope, detail-to-summary totals, allocations and revision residuals. Inspect the saved file as well as its appearance. Keep measurement evidence and outstanding queries with it.

The seven-sheet file has no macros or external workbook links. Thirty authoring-run input-state checks and saved-file checks are recorded in the [evaluation evidence](../evaluation/trade-workbook-refresh/README.md). Those checks do not prove identical recalculation across Excel, Google Sheets, LibreOffice or every host application.

## Controlled example

For supplied dimensions of 10 m × 6 m and an installation rate of 50 currency units/m² including ordinary bedding, net installation is 60 m² and its extension is 3,000. Record the supplied exercise rate and basis honestly. If owner-supplied stone has no purchase rate or fabrication yield, retain that purchase as unpriced scope and label 3,000 an installation-only subtotal. Do not add ordinary bedding again as levelling or call the subtotal the complete project cost. This example does not establish a market rate or formal measurement rule.
