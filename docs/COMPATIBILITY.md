# Compatibility

The package follows the [open Agent Skills specification](https://agentskills.io/specification): one named folder, `SKILL.md` with name/description, relative Markdown references, optional scripts and templates. No provider-specific tool names, agent manifest, hooks or model forks are needed.

| Capability | Minimum requirement | If unavailable |
|---|---|---|
| Advice, estimates from supplied quantities/rates | Model can read instructions and task inputs | Use the single Markdown edition in chat |
| Accurate arithmetic | Calculator, code runner or spreadsheet recommended | Identify arithmetic that could not be independently checked |
| Drawing-set inspection and take-off | Access to relevant pages/views, legible rendering, explicit dimensions or calibrated scale, and retained review records | Produce only the supported inventory/dimension-based work and identify uninspected scope |
| Live market/standards verification | Authorized current authoritative sources | Mark the specific claim unverified; use supplied evidence or a conditional scenario |
| Estimates, registers and schedule files | File access/export; spreadsheet tools for formatted workbooks or executed formulas | Return pasteable tables/CSV and disclose unexecuted calculation checks |
| Persistent memory | Optional Python 3.10+, explicitly scoped private storage and verified survival/access across sessions | Label temporary storage session-only; offer an export rather than promise persistence |
| Release checks | Optional network/browser access or Python 3.10+ | Open Releases manually or skip |

Claude and Codex support native skill workflows; OpenCode documents discovery of Agent Skills folders. An open model can follow the same text through a compatible host or a sufficiently capable chat app. The model alone does not determine installation paths or grant tools. Provider support documented here is format/discovery compatibility, not an executed cross-provider accuracy claim.

Evaluation used Codex desktop local agents reading the references directly. Native routing, Claude execution, open-model execution and real-project performance were not tested. Your host's instruction hierarchy and permissions still govern every task. Small models may need a narrower task, shorter reference selection and external calculation checks.

The [feature guide](FEATURES.md) separates supplied inputs, instructed work and expected deliverables. Tables, scope checks and calculations do not require a particular provider. Automated PDF parsing, CAD interrogation, symbol detection and financial-system connections are not installed by this skill.

[Claude-specific guidance](CLAUDE.md) distinguishes documented structure from executed testing. The package description is 191 characters to stay within the stricter upload guidance checked for this release. Native automatic selection and task performance still need a real Claude session.
