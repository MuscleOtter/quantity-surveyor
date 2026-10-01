# Compatibility

The package follows the [open Agent Skills specification](https://agentskills.io/specification): one named folder, `SKILL.md` with name/description, relative Markdown references, optional scripts and templates. No provider-specific tool names, agent manifest, hooks or model forks are needed.

| Capability | Minimum requirement | If unavailable |
|---|---|---|
| Advice, estimates from supplied quantities/rates | Model can read instructions and task inputs | Use the single Markdown edition in chat |
| Accurate arithmetic | Calculator, code runner or spreadsheet recommended | Identify arithmetic that could not be independently checked |
| Drawing measurement | Image/PDF reading and a known calibrated scale or explicit dimensions | Request dimensions; never scale an uncalibrated image |
| Live market/standards verification | Authorized current authoritative sources | Mark the specific claim unverified; use supplied evidence or a conditional scenario |
| CSV/file deliverables | File access or export | Return a table or CSV text |
| Persistent memory | Optional Python 3.10+ and explicitly scoped private storage | Memory stays off |
| Release checks | Optional network/browser access or Python 3.10+ | Open Releases manually or skip |

Claude and Codex support native skill workflows; OpenCode documents discovery of Agent Skills folders. An open model can follow the same text through a compatible host or a sufficiently capable chat app. The model alone does not determine installation paths or grant tools. Provider support documented here is format/discovery compatibility, not an executed cross-provider accuracy claim.

Evaluation used Codex desktop local agents reading the references directly. Native routing, Claude execution, open-model execution and real-project performance were not tested. Your host's instruction hierarchy and permissions still govern every task. Small models may need a narrower task, shorter reference selection and external calculation checks.
