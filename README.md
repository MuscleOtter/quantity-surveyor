# Quantity Surveyor

![Quantity Surveyor: architectural section with a blue highlighted bay and the words Measure. Estimate. Control.](assets/cover.png)

**Quantity Surveyor is a free, MIT-licensed AI skill for construction quantity take-off, cost estimating and commercial cost control.** Measure quantities, build estimates, compare tenders, reconcile forecasts and changes, plan cash flow, and assess lifecycle options. Covers complete buildings and luxury retail interiors and facades.

One open **Agent Skills** folder. The same instructions for Claude, Codex and skill-capable agents running open models. No required subscription, connector, API key, service or Python installation. Your chosen AI app may have its own requirements. Optional helpers use Python's standard library.

## Start here — no terminal needed

| Your app | Easiest route |
|---|---|
| Claude / Cowork | [Download the skill ZIP](https://github.com/MuscleOtter/universal-quantity-surveyor/releases/latest/download/quantity-surveyor.zip), then upload it under **Customize → Skills → + → Create skill → Upload a skill**. [Step-by-step help](docs/INSTALL.md#claude-and-cowork) |
| Codex | Copy the installation request below into Codex. [Help](docs/INSTALL.md#codex) |
| Claude Code / OpenCode / another local agent | Ask your agent to install the shared folder using [these instructions](docs/INSTALL.md#local-agents). |
| Any other chat app, including an open model | [Download the single Markdown edition](https://github.com/MuscleOtter/universal-quantity-surveyor/releases/latest/download/quantity-surveyor.md), attach it to a chat, then say **“Use these quantity surveying instructions for this task.”** [Help](docs/INSTALL.md#any-chat-app-or-open-model) |

Copy this into Codex:

```text
Use skill-installer to install the Quantity Surveyor skill from
https://github.com/MuscleOtter/universal-quantity-surveyor/tree/v2.0.0/skills/quantity-surveyor
If quantity-surveyor already exists, compare it and preserve a backup before
proposing replacement. Keep private memory intact; do not overwrite it.
Then tell me how to invoke the new skill.
```

Start a new chat if your app does not show the installed skill. Then try:

> Use Quantity Surveyor. A wall is 12 m × 3 m, with one 2 m × 2.4 m door. Deduct the door in full. Supply costs 80 per m² of purchased material, installation 45 per m² of net wall. Allow 5% material waste, no waste on installation. Calculate the total before tax and show your working.

Expected: **31.2 m² net; 32.76 m² purchased; 4,024.80 total.** No currency was supplied, so the answer should avoid inventing one.

## What you get

- Large drawing-set review: issued-sheet inventory, per-view scales, cross-references, resumable coverage and quantity evidence.
- Evidence-led take-offs and estimates with visible scope gaps, units, revisions and pricing boundaries.
- Whole-building scope checks, including site infrastructure, utilities, contractor additions and owner costs.
- Tender bridges, commitments, revised orders, payments, pending changes and forecast reconciliations.
- Practical risk, value engineering, cash flow and lifecycle analysis.
- Optional private project memory with provenance, corrections and explicit recovery.
- CSV templates you can open in a spreadsheet.

Version **2.0.0** uses the name **Quantity Surveyor** and folder **quantity-surveyor**. The original repository address is retained for existing links and update checks. [Migration help](docs/INSTALL.md#migrating-from-version-1).

The package is designed to be portable. Automatic discovery, image reading, browsing, file creation and calculation tools depend on the app and model. It does not mean identical accuracy across models. Jurisdiction and project rules remain explicit; UK NRM is not imposed worldwide. [Compatibility details](docs/COMPATIBILITY.md).

## Documentation

[FAQ](docs/FAQ.md) · [Large drawing sets and accuracy](docs/DRAWING-SETS.md) · [Research](docs/RESEARCH.md) · [AI documentation index](llms.txt) · [Installation](docs/INSTALL.md) · [First project and examples](docs/QUICKSTART.md) · [Troubleshooting](docs/TROUBLESHOOTING.md) · [Updates](docs/UPDATES.md) · [Architecture](docs/ARCHITECTURE.md) · [Astra distribution review](docs/DISTRIBUTION-REVIEW.md) · [Privacy](docs/PRIVACY.md) · [Standards and rights](skills/quantity-surveyor/references/standards.md) · [Evaluation](docs/EVALUATION.md) · [Publication checks](docs/PUBLICATION.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

## Quality and limits

**Accuracy on a huge coordinated drawing set has not been measured.** The skill guides a reviewable workflow; the app/model must supply and correctly use document, visual and calculation tools. Start with a representative, independently checked pilot. [What it can review and how to validate it](docs/DRAWING-SETS.md).

The historical Astra score of **9.96448/10** covers 23 bounded synthetic responses from the earlier QS instructions. It is not a 99.6% accuracy rate or a score for the new large-set workflow. Version 2 has a separate bounded instruction review; neither establishes real-project or cross-model performance. [Actual evidence and limits](docs/EVALUATION.md).

## For AI readers and search

Start with [llms.txt](llms.txt) for a concise documentation map, or [llms-full.txt](llms-full.txt) for the generated complete instructions. [FAQ](docs/FAQ.md) provides direct answers. These files aid agents that choose to read them; they do not guarantee search indexing or citations. [Discovery approach](docs/DISCOVERY.md).

Original text and code are [MIT licensed](LICENSE). The cover is AI-generated and supplied under [CC0](assets/README.md) to the extent rights can be granted. No proprietary standards, private rate library, company coding system or project memory is bundled.
