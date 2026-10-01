# Using Quantity Surveyor with Claude

The package has a **user-reported Claude smoke check**: one native activation in Claude Code and a four-case run on version 2.0.1, with all four answers reported correct. These were published evaluation cases, so this is a small smoke/regression check, not a new blind benchmark or accuracy score. See the [report and limits](../evaluation/claude-smoke-report.md). The report does not establish execution of the subsequent 2.0.2, 2.0.3, 2.1.0 or 2.1.1 changes.

## Installation and selection

For Claude/Cowork, download the release skill ZIP and use Customize → Skills → + → Create skill → Upload a skill. Confirm it is enabled. This route was checked against [Anthropic's upload instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude) on 1 October 2026; account settings may control availability.

For Claude Code, copy the complete folder into its supported project or personal skill directory as described in [Installation](INSTALL.md#local-agents). Invoke `/quantity-surveyor`, or test a natural-language request. The description helps automatic selection; host configuration and availability also matter. A plugin manifest is not needed for this direct skill-folder route. [Claude Code skills](https://code.claude.com/docs/en/skills).

The description names general construction tasks and is 191 characters. This stays below the 200-character limit in the [Claude custom-skill upload guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills). The ZIP contains one `quantity-surveyor/` folder with `SKILL.md` and its references/templates.

## Updates and storage

For this GitHub distribution, download an approved release and upload/update it through the Skills interface; confirm which version is enabled. The optional checker reports release metadata only. Do not assume that editing an extracted file in a task sandbox changes the installed skill. If network access is blocked, check the release page manually. This is the documented route for this package, not a claim that every Claude interface prohibits skill editing.

A successful memory write proves only that data was written at that location during that session. Before promising persistence, verify the chosen root is durable and accessible later. If unknown, call it session-only and offer an export. Do not assume all Cowork storage is temporary: it can access connected local folders under the conditions documented in [Cowork's platform guide](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile). Keep private memory outside the replaceable skill folder.

## Further host validation

The reported smoke check is partial evidence; the following is a checklist for broader testing, not a claim that every step has run. Use synthetic inputs in a fresh session and record the Claude model/version, host, skill release, enabled skills, prompt, references actually loaded and full output.

1. **Explicit invocation:** run the README wall calculation with the skill named. Check 31.2 m² net, 32.76 m² purchased and 4,024.80 before tax, without an invented currency.
2. **Natural routing:** try “prepare a take-off for this apartment refurbishment” and “compare these subcontractor quotes” without naming the skill. Provide sufficient synthetic inputs. Verify activation separately from numerical correctness.
3. **Reference selection:** test a forecast amendment, a tender comparison and a lifecycle question. Check that relevant guidance is loaded and the output follows the given scope.
4. **Capability limits:** request a drawing quantity without a readable drawing or dimensions. Check that missing evidence remains visible rather than producing fabricated measurements.
5. **Storage, if enabled:** write only a harmless synthetic record to an explicitly chosen durable root, then confirm retrieval in a new session before using it for project memory.

The public evaluation cases are reusable regression checks; published answers make them unsuitable as new blind evidence. Use new held-out inputs for a fresh performance claim. Keep plugin distribution as an optional future convenience, separate from validation of the portable skill.
