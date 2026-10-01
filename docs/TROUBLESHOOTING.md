# Troubleshooting

| Problem | What to do |
|---|---|
| Claude rejects the ZIP | Download the **skill ZIP** from Releases. Do not use the whole-repository ZIP or add an extra enclosing folder. The folder and frontmatter name must both be `quantity-surveyor`. |
| No Skills upload option | Check Claude's code-execution capability and organization policy; use the single Markdown edition if native installation is unavailable. |
| Local agent cannot find the skill | Ask it to confirm its supported skill directory and that `SKILL.md` is directly inside the named folder. Restart or refresh discovery. |
| Agent says it cannot open references | Preserve the complete folder; in plain chat use the combined Markdown edition. Ask it to name what it actually read. |
| An open model ignores instructions | Give a smaller task, load just the relevant reference, and verify calculations externally. A different host/model may be needed for complex work. |
| Drawing has no usable dimensions | Supply a dimension or calibrated scale. Do not ask the model to guess image scale. |
| Prices are missing | Ask for quantities, scope gaps and a rate-evidence request. Supply lawful current quotes before treating costs as a project estimate. |
| Update check says unavailable | The release API may be offline/rate-limited or restricted. Open Releases manually; continue the current QS task. |
| Optional helper is unavailable | Continue without memory/update helper. It needs Python 3.10+ but the core instructions do not. |
| Memory primary file is missing but backup exists | Stop writes. Use the documented explicit recovery process; inspect the backup and expect loss of records newer than that backup. Do not start a new store over it. |
| Two versions seem active | Ask the host to show loaded skill paths/versions, then disable the duplicate through its normal UI. Preserve private memory and customizations. |

If you need help, [open an issue](https://github.com/MuscleOtter/universal-quantity-surveyor/issues) with your app, skill version, synthetic input and observed behavior. Do not upload private project data.
