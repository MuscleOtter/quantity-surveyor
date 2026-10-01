# Fresh independent evaluation evidence

## Scope and source boundaries

Task performed from [request.txt](../fixtures/request.txt), the raw [transfer-cases.pdf](../fixtures/transfer-cases.pdf), and the portable [candidate skill](../../../skills/quantity-surveyor/SKILL.md). The measurement, drawing-takeoff and trade-finishes references governed the calculations, calibration and bedding boundary. Other candidate trade prompts (partitions/ceilings, facades/glazing, services) were read for interface context; they supplied no dimensions, rules or prices used here. A local PDF skill was used solely for read-only rendering and inspection.

No expected answers, baseline snapshots, hashes, previous evaluations, private skill/configuration, audit files or generated chat edition were read. No company sources, memory, network/API calls, external actions or fixture/skill edits were used. Outputs contain repository-relative source locators only.

## Visual coverage and tooling

All three pages were rendered at 120 dpi with local Poppler and visually inspected: page 1 W-201 R1 plus R2 height note; page 2 V-202 R1 imported viewport with control and T1; page 3 F-203 R1 rooms P/Q. Renders are in `work/public-transfer-evaluation/case-1.png` through `case-3.png`. No drawing-set completeness claim is made beyond these three supplied pages. Explicit dimensions governed A/C; those sketches were not scaled. The page-3 bottom room labels overlap slightly in the fixture, but its top written dimensions clearly identify P and Q.

For B, local pdfplumber vector geometry corroborated the visually identified control. Page coordinates are points, origin at top-left: control x=80 to 240, y=275.276 to 365.276 (160 × 90 pt). Render conversion is 120/72 pixels per point, approximately 266.667 × 150 pixels. The diagnostic uses exact PDF vector lengths rather than rounded raster lengths. No target dimensions or area were accepted from the rejected calibration.

## Calibration evidence

Tolerance **2%** was declared in the evaluation commentary before vector measurement and numeric comparison. It is a chosen acceptance criterion for this exercise, not a claimed professional accuracy band. X: 4 m / 160 pt = 0.025 m/pt. Independent Y: 90 pt × 0.025 = 2.25 m versus the stated 2 m; (2.25−2)/2 × 100 = **12.5%**. Y's independent factor is 0.022222… m/pt. Calibration therefore fails. The fixture expressly disallows nonuniform rectification while geometry/projection is unverified. T1 is unresolved; it has neither written dimensions nor a supplied price.

## Calculation evidence and reconciliation

Calculations used Decimal arithmetic; machine-readable detail is saved in `work/public-transfer-evaluation/calculations.json`.

- A R1: gross 7.2×3.1=22.32 m²; opening 1.2×2.1=2.52 m²; net 19.80 m²; purchase 19.80×1.05=20.790 m²; supply 20.790×80=1,663.20 CU; install 19.80×45=891.00 CU; sum=2,554.20 CU.
- A R2: gross 7.2×3.4=24.48 m²; net 21.96 m²; purchase 23.058 m²; supply=1,844.64 CU; install=988.20 CU; sum=2,832.84 CU.
- A bridge: +2.16 net m² and +2.268 purchased m²; supply +181.44 CU; installation +97.20 CU; sum +278.64 CU; prior total + bridge = new total. No rate effect.
- Independent alternative A check: net factor=80×1.05+45=129 CU/net m²; 19.80×129=2,554.20 and 21.96×129=2,832.84. Height-only bridge 7.2×(3.4−3.1)×129=278.64 CU. These identities were asserted successfully in executable code.
- C: P=6.5×4=26 m² ×52=1,352 CU; Q=3×5=15 m² ×52=780 CU. Independent subtotal check 1,352+780=41×52=2,132 CU passed. Separate stable IDs C-P and C-Q retained; ordinary bedding counted once within the GC rate.

Precision retained through calculation; costs displayed to two decimals, purchase areas to three. No unstated tax, mark-up, labour waste, procurement rounding or rates were added.

## Limits and behavioral observations

The candidate supported the requested proportional schedules without a full workbook or a formal NRM claim. Material waste was separated from installation, the revision bridge reconciled, failed calibration blocked graphical measurement, room identities were preserved, and owner supply/GC installation/bedding were distinguished. Missing purchase/yield/levelling inputs remain queries, not fabricated allowances or zero-cost scope. These observations concern this supplied three-case exercise only; they do not establish broader drawing completeness, market pricing, design suitability or compliance. No live workbook recalculation was requested or performed.
