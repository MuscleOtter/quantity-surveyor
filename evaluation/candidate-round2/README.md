# Quantity Surveyor — portable edition

A shareable skill for hands-on construction cost work: luxury retail interiors/facades and complete freestanding building projects. It supports take-offs, bills, early/elemental estimates, resource rates, scope checks, tender comparison, forecasts/changes, payment cash flow, value engineering and lifecycle costing. It also gives proportionate process advice.

## Use it

Use the folder as a skill in a harness that supports Markdown skills, according to that harness's documented installation process. Keep the folder name and `SKILL.md` together with its relative references. The name is `quantity-surveyor-portable`, so it can coexist with another quantity-surveyor skill. This package has not been installed into anyone's existing configuration.

For a harness without skill discovery, provide `SKILL.md` as task instructions and allow access to the relevant linked references; alternatively paste those references into the task context. A Markdown file cannot enable unavailable tools or guarantee automatic routing. The host's instruction hierarchy, tool permissions, context capacity and model ability still apply. Do not claim that a host loaded a reference unless it did.

No connector, external service, specific model or agent harness is required. Readable project inputs and ordinary calculation capabilities support most tasks. Drawing take-offs need visual reading and calibrated scale; live rates/current legal facts need current authoritative sources. Original CSV templates are optional and can be opened by common spreadsheet tools. The only executable helper uses Python 3.10+ standard library and is optional; no package installation is needed for it.

## Practical requests

- “Take off this interior finish schedule from revisions A3/E2 using the supplied project deduction convention. Separate measured installed quantities from purchase quantities and waste. Price with these quoted rates; flag facade interfaces not covered.”
- “Build a cost plan for this freestanding building, including shared site utilities and owner costs. Use our area convention and supplied package rates; show missing scope instead of inventing prices.”
- “Compare these facade tenders. Preserve submitted totals and distinguish confirmed scope adjustments, scenario allowances and unpriced qualifications.”
- “Reconcile this approved budget, revised purchase orders, payments and pending changes to forecast final cost. Check amendment semantics and duplicate inclusion.”
- “Compare these two compliant options over 20 years at the supplied real discount rate; show event timing, maintenance, replacements and residual credits.”

Supply only the inputs relevant to the request: scope/drawings and revisions, units/convention, location/currency/date/taxes, programme, rates and their inclusions, contract/payment definitions or chosen codes where needed. [Project basis](templates/project-basis.md) is an optional prompt. Missing prices still permit a quantity schedule; inaccessible rule evidence permits a labelled project convention without claiming standards compliance.

## Standards and references

[Standards guidance](references/standards.md) distinguishes work measurement, reporting, area and lifecycle methods. NRM is UK-origin practice information, not mandatory worldwide. ICMS supports international high-level reporting; local law, appointment and adopted project rules determine actual requirements. Current-status research is dated 1 October 2026 and must be refreshed when it matters.

The package includes original guidance and links, not proprietary RICS/ISO/CSI or local library files. User-supplied references need appropriate rights for the intended reading/AI use, not just download access. Exact standard rules require actual authorised clause evidence. Use [the evidence register](references/evidence-and-interfaces.md).

## Optional memory and adapters

Memory is off by default. Explicitly choose a dedicated root, user and project before using [memory guidance](references/memory-and-review.md). The helper stores provenance-backed tentative/verified records, corrections and a previous-copy backup. It never discovers existing personal memory, shares between scopes or writes to a default home/harness directory. Scope filtering is accidental-isolation protection, not authentication or encryption. Keep stores private and outside the shareable package.

Jev or another semantic checker is an optional adapter. Exact checks and ordinary reasoning work without it. An adapter cannot supply missing code authority, approval or arithmetic verification; private/restricted inputs require authority before external transmission.

## Portability and validation

The original package is plain Markdown/CSV plus an optional Python helper. See the accompanying evaluation report for actual behavioral cases, executed helper tests, defects/corrections and environment evidence. No broad cross-model, cross-harness, real-project or certified-human comparison is implied. Skill syntax validation alone does not establish estimating competence. Visual drawing take-off and independent local market-rate calibration require further project evidence.

The original content is under [MIT](LICENSE); third-party references retain their own rights. This package does not confer professional credentials, statutory sign-off authority or publisher endorsement.
