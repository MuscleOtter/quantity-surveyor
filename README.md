# Universal Quantity Surveyor

![Universal Quantity Surveyor: an exploded architectural model flowing from a blueprint](assets/cover.png)

**Give your AI a practical construction cost workflow.** Measure quantities, build estimates, compare tenders, reconcile forecasts and changes, plan cash flow, and assess lifecycle options. Covers complete buildings and luxury retail interiors and facades.

One open **Agent Skills** folder. The same instructions for Claude, Codex and skill-capable agents running open models. No required subscription, connector, API key, service or Python installation. Your chosen AI app may have its own requirements. Optional helpers use Python's standard library.

## Start here — no terminal needed

| Your app | Easiest route |
|---|---|
| Claude / Cowork | [Download the skill ZIP](https://github.com/MuscleOtter/universal-quantity-surveyor/releases/latest/download/universal-quantity-surveyor.zip), then upload it under **Customize → Skills → + → Create skill → Upload a skill**. [Step-by-step help](docs/INSTALL.md#claude-and-cowork) |
| Codex | Copy the installation request below into Codex. [Help](docs/INSTALL.md#codex) |
| Claude Code / OpenCode / another local agent | Ask your agent to install the shared folder using [these instructions](docs/INSTALL.md#local-agents). |
| Any other chat app, including an open model | [Download the single Markdown edition](https://github.com/MuscleOtter/universal-quantity-surveyor/releases/latest/download/universal-quantity-surveyor.md), attach it to a chat, then say **“Use these quantity surveying instructions for this task.”** [Help](docs/INSTALL.md#any-chat-app-or-open-model) |

Copy this into Codex:

```text
Use skill-installer to install the Universal Quantity Surveyor skill from
https://github.com/MuscleOtter/universal-quantity-surveyor/tree/v1.0.0/skills/universal-quantity-surveyor
Keep any existing quantity-surveyor skills and private memory intact.
Then tell me how to invoke the new skill.
```

Start a new chat if your app does not show the installed skill. Then try:

> Use Universal Quantity Surveyor. A wall is 12 m × 3 m, with one 2 m × 2.4 m door. Deduct the door in full. Supply costs 80 per m² of purchased material, installation 45 per m² of net wall. Allow 5% material waste, no waste on installation. Calculate the total before tax and show your working.

Expected: **31.2 m² net; 32.76 m² purchased; 4,024.80 total.** No currency was supplied, so the answer should avoid inventing one.

## What you get

- Evidence-led take-offs and estimates with visible scope gaps, units, revisions and pricing boundaries.
- Whole-building scope checks, including site infrastructure, utilities, contractor additions and owner costs.
- Tender bridges, commitments, revised orders, payments, pending changes and forecast reconciliations.
- Practical risk, value engineering, cash flow and lifecycle analysis.
- Optional private project memory with provenance, corrections and explicit recovery.
- CSV templates you can open in a spreadsheet.

“Universal” describes the portable package. Automatic discovery, image reading, browsing, file creation and calculation tools depend on the app and model. It does not mean identical accuracy across models. Jurisdiction and project rules remain explicit; UK NRM is not imposed worldwide. [Compatibility details](docs/COMPATIBILITY.md).

## Documentation

[Installation](docs/INSTALL.md) · [First project and examples](docs/QUICKSTART.md) · [Troubleshooting](docs/TROUBLESHOOTING.md) · [Updates](docs/UPDATES.md) · [Architecture](docs/ARCHITECTURE.md) · [Astra distribution review](docs/DISTRIBUTION-REVIEW.md) · [Privacy](docs/PRIVACY.md) · [Standards and rights](skills/universal-quantity-surveyor/references/standards.md) · [Evaluation](docs/EVALUATION.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

## Quality and limits

The independent Astra critic scored all 23 sealed synthetic round-2 outputs **9.96448/10 with zero material failures**. The public evaluation records also cover visual drawing cases and executed memory-helper checks. The Astra review and its deductions are published with the actual scored answers. This is not professional certification, a human percentile benchmark or evidence of testing every model. Review consequential project results against actual drawings, rates and applicable requirements.

Original text and code are [MIT licensed](LICENSE). The cover is AI-generated and supplied under [CC0](assets/README.md) to the extent rights can be granted. No proprietary standards, private rate library, company coding system or project memory is bundled.
