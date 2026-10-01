# Install in your app

You do not need to write code. Choose one route below. The skill name is **universal-quantity-surveyor**. Keep the complete folder together so the AI can open its references.

## Claude and Cowork

1. [Download universal-quantity-surveyor.zip](https://github.com/MuscleOtter/universal-quantity-surveyor/releases/latest/download/universal-quantity-surveyor.zip). Keep it zipped.
2. In Claude, open **Customize → Skills**. Select **+ → + Create skill → Upload a skill**.
3. Choose the downloaded ZIP and turn the skill on.
4. Ask: “Use Universal Quantity Surveyor to check this estimate.” Attach the relevant project inputs.

If Skills is missing, enable code execution/file creation in Settings → Capabilities where available; an organization administrator may control access. Cowork uses skills enabled for your Claude account. See [Claude's official instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

Use the release **skill ZIP**, not GitHub's “Download ZIP” source archive. The install ZIP has exactly one top-level folder with `SKILL.md` inside, following [Claude's packaging guidance](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

## Codex

Paste this into Codex:

```text
Use skill-installer to install this skill:
https://github.com/MuscleOtter/universal-quantity-surveyor/tree/v1.0.0/skills/universal-quantity-surveyor
Preserve existing skills and private memory. Show me the installed location
and how to select universal-quantity-surveyor.
```

If your app has no installer, download and unzip the skill ZIP, then ask the agent to copy its folder into the supported personal or project skill directory. Current Codex documentation lists personal `~/.agents/skills/` and project `.agents/skills/`. Older installations may use a different configured location: let the installed app/installer determine it. In Codex CLI/IDE, use `$universal-quantity-surveyor`; desktop selection can use its skill picker. Restart if discovery does not refresh. [Official Codex skill guide](https://learn.chatgpt.com/docs/build-skills).

## Local agents

Download and unzip the skill ZIP. Ask your local agent:

```text
Install the downloaded universal-quantity-surveyor folder using your documented
skill directory. Copy the complete folder with its references and templates.
Preserve existing skills and private memory; if the destination already exists,
show me the difference before replacing it. Confirm that you can load SKILL.md
and references/measurement-and-estimating.md. Do not enable memory or update
checks automatically.
```

For someone helping with a manual copy:

| Host | Project folder | Personal folder |
|---|---|---|
| Claude Code | `.claude/skills/universal-quantity-surveyor/` | `~/.claude/skills/universal-quantity-surveyor/` |
| Codex | `.agents/skills/universal-quantity-surveyor/` | `~/.agents/skills/universal-quantity-surveyor/` |
| OpenCode | `.agents/skills/universal-quantity-surveyor/` | `~/.agents/skills/universal-quantity-surveyor/` |

These paths are for the host, not a specific model. OpenCode also supports its own `.opencode/skills` directories. [Claude Code documentation](https://code.claude.com/docs/en/skills), [OpenCode documentation](https://opencode.ai/docs/skills/). Windows users can ask their agent to resolve the matching user/project folder; do not type a literal `~` into File Explorer.

## Any chat app or open model

1. [Download universal-quantity-surveyor.md](https://github.com/MuscleOtter/universal-quantity-surveyor/releases/latest/download/universal-quantity-surveyor.md).
2. Attach it to your chat, or open it in a text editor and paste it if attachments are unsupported.
3. Say: “Read the attached quantity surveying instructions and apply them to this task. Tell me if any part is outside your capabilities.” Then provide the task and relevant project inputs.

The file includes all core guidance, references and template content. It needs enough context space; if your model cannot fit it, provide `SKILL.md` and only the task's needed references from the source folder. Chat attachment alone does not install an automatically invoked skill. Plain chat cannot run optional Python helpers without execution tools.

## Confirm installation

Run the wall calculation in the [README](../README.md). The answer should show 31.2 m² installed, 32.76 m² purchased and 4,024.80 before tax. A correct answer is a useful setup check, not a full accuracy benchmark. Also ask the app to identify the skill and reference it actually loaded.

## Uninstall

Claude: switch the skill off or delete it in Customize → Skills. Local agents: remove only the installed `universal-quantity-surveyor` folder using your app's documented process. Chat-only: remove the attachment/instructions or start a new chat. Private memory is stored separately and is never deleted by this package.

Installation guidance was checked against official documentation on 1 October 2026. Interfaces can change; the linked official guides are the fallback.
