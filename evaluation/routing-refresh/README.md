# Routing clarification — version 2.0.3

The user reported successful Claude smoke checks on 2.0.1 together with four usability issues. This patch clarifies instruction selection and exposes existing templates; it does not add new estimating formulas or helper behavior.

`changes.json` records the exact substitutions applied after the 2.0.2 editorial changes. The validator verifies the preserved version 2 sources, cumulative allowed changes, template links, documentation links and generated distributions. Earlier frozen cases and answers are unchanged.

## Static routing review

These are intended routes checked by reading the revised instructions, not observed new model responses:

| Example request | Intended reference selection | Expected output boundary |
|---|---|---|
| Calculate a wall from supplied dimensions and stated deduction/waste rules | Measurement and estimating | Direct calculation; standards and large-set references unnecessary. |
| Take off one self-contained drawing view | Measurement and estimating | Verify relevant dimensions/scale and evidence without requiring a whole-set register. |
| Coordinate plans with schedules/details across a revised set | Large drawing sets plus measurement when quantities are requested | Issued-set control, dependency/coverage review and evidenced quantities. |
| Apply a named measurement standard or choose its edition | Standards plus the relevant task reference | Verify the applicable rule, or state the unresolved rule and calculation convention. |
| Advise at an early stage with insufficient pricing information | Measurement and estimating; add commercial control only for procurement/decision/process advice | Supported subtotal if possible; otherwise unpriced scope, missing inputs and next actions without invented rates. |
| Produce an estimate, forecast, change log, drawing register, evidence ledger or project basis | Task reference plus the directly linked relevant template if useful | Preserve a supplied user format; no mandatory template for a short calculation. |

The core now links all six templates. The public Claude guide uses `USING-WITH-CLAUDE.md`, avoiding the reserved instruction filename. The [reported Claude check](../claude-smoke-report.md) remains explicitly tied to the supplied report and the known tested version. No new Claude rerun or numeric score is claimed for 2.0.3.
