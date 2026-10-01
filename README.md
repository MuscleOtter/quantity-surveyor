# Quantity Surveyor

![Quantity Surveyor: architectural section with a blue highlighted bay and the words Measure. Estimate. Control.](assets/cover.png)

**Quantity Surveyor is a free, MIT-licensed AI skill for construction quantity take-off, cost estimating and commercial cost control.** Measure quantities, build estimates, compare tenders, reconcile forecasts and changes, plan cash flow, and assess lifecycle options. Use it for new buildings, renovations, individual construction packages and associated site works.

One open **Agent Skills** folder. The same instructions for Claude, Codex and skill-capable agents running open models. No required subscription, connector, API key, service or Python installation. Your chosen AI app may have its own requirements. Optional helpers use Python's standard library.

## Start here — no terminal needed

| Your app | Easiest route |
|---|---|
| Claude / Cowork | [Download the skill ZIP](https://github.com/MuscleOtter/quantity-surveyor/releases/latest/download/quantity-surveyor.zip), then upload it under **Customize → Skills → + → Create skill → Upload a skill**. [Step-by-step help](docs/INSTALL.md#claude-and-cowork) |
| Codex | Copy the installation request below into Codex. [Help](docs/INSTALL.md#codex) |
| Claude Code / OpenCode / another local agent | Ask your agent to install the shared folder using [these instructions](docs/INSTALL.md#local-agents). |
| Any other chat app, including an open model | [Download the single Markdown edition](https://github.com/MuscleOtter/quantity-surveyor/releases/latest/download/quantity-surveyor.md), attach it to a chat, then say **“Use these quantity surveying instructions for this task.”** [Help](docs/INSTALL.md#any-chat-app-or-open-model) |

Copy this into Codex:

```text
Use skill-installer to install the Quantity Surveyor skill from
https://github.com/MuscleOtter/quantity-surveyor/tree/v2.0.3/skills/quantity-surveyor
If quantity-surveyor already exists, compare it and preserve a backup before
proposing replacement. Keep private memory intact; do not overwrite it.
Then tell me how to invoke the new skill.
```

Start a new chat if your app does not show the installed skill. Then try:

> Use Quantity Surveyor. A wall is 12 m × 3 m, with one 2 m × 2.4 m door. Deduct the door in full. Supply costs 80 per m² of purchased material, installation 45 per m² of net wall. Allow 5% material waste, no waste on installation. Calculate the total before tax and show your working.

Expected: **31.2 m² net; 32.76 m² purchased; 4,024.80 total.** No currency was supplied, so the answer should avoid inventing one.

## Features and deliverables

| Feature | What it helps you do | What you receive |
|---|---|---|
| Drawing-set review | Check issued sheets and revisions, follow details/schedules, track inspected areas and flag missing references. | Drawing register, coverage statement and prioritized questions. |
| Quantity take-off | Calculate counts, lengths, areas and volumes; show openings, deductions, repeated items and material waste separately. | Quantity schedule with units, calculations and drawing/revision locations. |
| Estimates and rate build-ups | Combine quantities with supplied or evidenced labour, material and equipment rates; show fees, overhead, risk, escalation, FX and tax bases. | Itemized estimate, transparent rate build-ups and a total reconciled to the detail. |
| Scope-gap review | Check work packages, shared site costs, utilities, temporary works and owner/contractor responsibilities. | Coverage matrix showing included, excluded and unpriced scope without double counting. |
| Tender comparison | Retain original bids, align supported scope differences and expose exclusions and qualifications. | Side-by-side comparison with adjustment evidence and conditional recommendations. |
| Budget, changes and final-cost forecast | Reconcile purchase orders, amendments, paid amounts, remaining work and pending changes. | Forecast final cost, budget variance, change log and explanation of movements. |
| Cash-flow planning | Apply programme dates, payment lags, deposits, retention and releases. | Period-by-period payment forecast with cumulative cash and balance checks. |
| Risk and value engineering | Show named exposures and compare options including consequential costs and required approvals. | Risk/assumption register, supported scenarios and net-savings comparison. |
| Maintenance and lifecycle costs | Schedule maintenance/replacements and discount costs using consistent timing and price assumptions. | Event schedule, present-value comparison and sensitivities. |
| Coding and audit trail | Use your supplied cost-code definitions; retain uncertain mappings and source evidence. | Reconciled coded totals, unallocated amounts and queries linked to affected items. |

The [feature guide](docs/FEATURES.md) explains inputs, operations, outputs and limits for each workflow. [Example requests](docs/QUICKSTART.md) help you start. Five blank CSV templates cover estimates, forecasts, changes, drawing registers and quantity evidence; a project-basis Markdown template records the brief. The pending 2.1.0 source also includes an [optional estimating workbook](skills/quantity-surveyor/assets/templates/estimating-template.xlsx) with seven sheets, visible missing-input queries, allocation checks and a revision bridge. Read its [usage and limits](skills/quantity-surveyor/references/workbook-pattern.md).

These are workflows for your AI app to carry out. Drawing viewing, calculation, file export and current-source access depend on the host. Optional private memory and release checking are separate helpers, off by default.

The latest published version is **2.0.3**; source changes for **2.1.0** are pending release. Version **2.0.3** uses the name **Quantity Surveyor** and folder **quantity-surveyor**. The repository is now **MuscleOtter/quantity-surveyor**. Earlier installed release checkers need a one-time manual update; see [update guidance](docs/UPDATES.md#repository-rename). [Migration help](docs/INSTALL.md#migrating-from-version-1).

The package is designed to be portable. Automatic discovery, image reading, browsing, file creation and calculation tools depend on the app and model. It does not mean identical accuracy across models. Jurisdiction and project rules remain explicit; UK NRM is not imposed worldwide. [Compatibility details](docs/COMPATIBILITY.md).

## Documentation

[Features](docs/FEATURES.md) · [Claude guidance](docs/USING-WITH-CLAUDE.md) · [FAQ](docs/FAQ.md) · [Large drawing sets and accuracy](docs/DRAWING-SETS.md) · [Research](docs/RESEARCH.md) · [AI documentation index](llms.txt) · [Installation](docs/INSTALL.md) · [First project and examples](docs/QUICKSTART.md) · [Troubleshooting](docs/TROUBLESHOOTING.md) · [Updates](docs/UPDATES.md) · [Architecture](docs/ARCHITECTURE.md) · [Astra distribution review](docs/DISTRIBUTION-REVIEW.md) · [Privacy](docs/PRIVACY.md) · [Standards and rights](skills/quantity-surveyor/references/standards.md) · [Evaluation](docs/EVALUATION.md) · [Publication checks](docs/PUBLICATION-V2.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

## Quality and limits

**Accuracy on a huge coordinated drawing set has not been measured.** The skill guides a reviewable workflow; the app/model must supply and correctly use document, visual and calculation tools. Start with a representative, independently checked pilot. [What it can review and how to validate it](docs/DRAWING-SETS.md).

The historical Astra score of **9.96448/10** covers 23 bounded synthetic responses from the earlier QS instructions. It is not a 99.6% accuracy rate or a score for the new large-set workflow. Version 2 has a separate bounded instruction review. A [user-reported Claude smoke check](evaluation/claude-smoke-report.md) adds one native Claude Code activation and four correct published-case answers on 2.0.1. These do not establish real-project accuracy or cross-model parity. [Actual evidence and limits](docs/EVALUATION.md).

## For AI readers and search

Start with [llms.txt](llms.txt) for a concise documentation map, or [llms-full.txt](llms-full.txt) for the generated complete instructions. [FAQ](docs/FAQ.md) provides direct answers. These files aid agents that choose to read them; they do not guarantee search indexing or citations. [Discovery approach](docs/DISCOVERY.md).

Original text and code are [MIT licensed](LICENSE). The cover is AI-generated and supplied under [CC0](assets/README.md) to the extent rights can be granted. No proprietary standards, private rate library, company coding system or project memory is bundled.
