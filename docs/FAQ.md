# Quantity Surveyor: questions and answers

## What is Quantity Surveyor?

Quantity Surveyor is a free, MIT-licensed AI agent skill for construction quantity take-off, cost estimating and commercial cost control. It supports new buildings, renovations, individual construction packages and associated site works. It is published by MuscleOtter and is not affiliated with a professional institution or model provider.

## What can it produce?

A drawing register, quantity take-off, itemized estimate, rate build-up, scope-gap matrix, tender comparison, budget/forecast reconciliation, change log, payment forecast or lifecycle-cost comparison. Outputs retain calculations, units, source/revision locations, assumptions and unresolved questions. The [feature guide](FEATURES.md) lists what you need to supply and the deliverable for each task.

## Does it automatically scan drawings or supply construction prices?

The skill provides instructions and templates, not a bundled drawing parser, symbol detector or live price database. Your app must supply document/image access and calculation tools; drawings need readable dimensions or calibrated views. Rates need project quotes, supplied evidence or appropriate authorized research. If those inputs are missing, ask for supported quantities, scope gaps and a pricing query list.

## Does it work with Claude, Codex and open-source models?

The instructions are model-neutral Markdown in the Agent Skills folder format. Skill-capable hosts can load the folder; other chat apps can use the complete Markdown attachment. Tools, context capacity and instruction following differ, so portable instructions do not imply equivalent accuracy. One native Claude Code activation and four correct published-case answers on 2.0.1 have been reported as a [smoke check](../evaluation/claude-smoke-report.md). That does not establish cross-model parity or all native installation paths. See [compatibility](COMPATIBILITY.md).

## Do I need to code or buy a service?

No coding is needed to upload the skill ZIP or attach the Markdown edition. The skill itself requires no paid API, subscription or connector. Your chosen app may have its own fees and capabilities. [Installation](INSTALL.md).

## Can it read hundreds of drawings accurately?

There is no measured accuracy percentage for a huge coordinated drawing set. Version 2 guides inventory, revision selection, cross-sheet references, calibrated measurement and evidence tracking. Your app must actually read/render the documents and perform the checks. Start with a reviewed pilot. [Drawing-set capability and validation plan](DRAWING-SETS.md).

## Is the old 9.96448/10 score a 99.6% accuracy rate?

No. It is a rubric score for 23 bounded synthetic responses from the earlier instructions. It is not a quantity error rate, a full-set completeness metric or a validation of version 2's new workflow. [Evaluation](EVALUATION.md).

## What should I provide?

The task and scope, relevant issued drawings/specifications and schedules, measurement convention, units, currency and price date where relevant. For pricing, supply rates or authorize appropriate market research. The skill should ask only for missing inputs that affect the work and continue supported tasks.

## Does it contain construction prices or licensed standards?

No private rate library or proprietary standard text is bundled. The skill distinguishes evidence, assumptions and calculations. It links to official standards guidance and requires an explicit applicable edition or project convention.

## Will it send my drawings elsewhere or update itself?

The package contains no automatic upload or self-update mechanism. Your host app governs its own data handling and tool actions. The optional update checker reads public release metadata only after an explicit online request; installation needs approval. Optional memory is separate and off by default. [Privacy](PRIVACY.md), [updates](UPDATES.md).

## What is the repository address?

The repository is now [MuscleOtter/quantity-surveyor](https://github.com/MuscleOtter/quantity-surveyor), matching the skill name and folder. It remains designed for different models and hosts. Installations from before the rename need a one-time manual update to restore their release checker; see [updates](UPDATES.md#repository-rename).

## Can I install it over a skill already named quantity-surveyor?

Do not replace an existing personalized skill blindly. Have your agent compare the packages and preserve your current skill/customizations and private memory before choosing how to install. Version 2 changes the package name; see [migration](INSTALL.md#migrating-from-version-1).
