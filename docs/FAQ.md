# Quantity Surveyor: questions and answers

## What is Quantity Surveyor?

Quantity Surveyor is a free, MIT-licensed AI agent skill for construction quantity take-off, cost estimating and commercial cost control. It covers complete buildings and luxury retail interiors/facades. It is published by MuscleOtter and is not affiliated with a professional institution or model provider.

## Does it work with Claude, Codex and open-source models?

The instructions are model-neutral Markdown in the Agent Skills folder format. Skill-capable hosts can load the folder; other chat apps can use the complete Markdown attachment. Tools, context capacity and instruction following differ, so portable instructions do not imply equivalent accuracy. Cross-model performance and every native installation path have not been tested. See [compatibility](COMPATIBILITY.md).

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

## Why does the GitHub address still include “universal”?

The skill's name and install folder are now **Quantity Surveyor / quantity-surveyor**. The original repository address is retained so existing links and version 1 update checks continue to work. It remains designed for different models and hosts.

## Can I install it over a skill already named quantity-surveyor?

Do not replace an existing personalized skill blindly. Have your agent compare the packages and preserve your current skill/customizations and private memory before choosing how to install. Version 2 changes the package name; see [migration](INSTALL.md#migrating-from-version-1).
