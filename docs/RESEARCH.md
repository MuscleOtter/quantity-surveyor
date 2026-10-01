# Research: reading large construction drawing sets

Reviewed on 1 October 2026. This is a source-level comparison of useful public approaches, not a ranking, security certification, installation recommendation or reproduced performance benchmark. No third-party runtime was installed or executed. Quantity Surveyor's new guidance is original; no third-party skill code or restricted-license instruction text is bundled.

## Public projects inspected

| Project and pinned source | Useful approach | Limits and adoption decision |
|---|---|---|
| [AutoConst Drawing Takeoff](https://github.com/hamzaabduljabbar/autoConst-drawing-takeoff-claude/tree/3f0c8be1cb2064e1cf01a7dce4a80acf31c9e787) | Index vector text, metadata and schedules once; query a persistent drawing index before repeatedly opening a large PDF. | Text extraction is not visual validation, and tags/schedule rows are not automatically installed quantities. SQLite/Python and Claude-oriented workflow. Custom source-available license restricts resale/rebranding; no code or text copied. We adopted the general principle of indexed navigation with source validation, without a required database. |
| [Takeoff Lens](https://github.com/anekhirun/Takeoff-Lens-Plugin/tree/8f3cdbbd317f35b6919a6138046d6711bd583506) | Project legend interpretation, candidate crops, accepted/rejected/uncertain review, stale-result checks and sweeps for detector misses. | MIT; dedicated MCP/tool stack focused on Electrical/ELV. Its published small regression is not proof of general building or huge-set accuracy. We adopted an evidence/review contract in plain instructions, not the detector. |
| [Claude Code Construction](https://github.com/dleerdefi/claude-code-construction/tree/0732956d1a3f77146c40566dbb7f53b16db8811c) | Separate viewports and scales; reconcile vision with text anchors; track physical instances and repeated depictions. | MIT; many operations depend on AgentCM data/APIs. The tag take-off has a flat-file mode but is count-focused. Simplified rules such as one plan tag equalling one instance need project-specific checks. We adopted viewport-level evidence and explicit instance reconciliation without host-specific APIs. |
| [BuildSense CAD Reader](https://github.com/buildsense-ai/cad-reader-skill/tree/e7d54eb6cca5b607a340853969d8ab5724ce7ac3) | Inspect native CAD structure, layouts/layers/blocks and missing or unsupported objects before drawing conclusions. | Apache-2.0; requires a remote CAD service, authentication and appropriate transfer permission. Not a complete priced bill-of-quantities engine. Keep CAD inspection as an optional host capability; do not imply it is installed here. |
| [AEC-Bench](https://github.com/nomic-ai/aec-bench/tree/3f50ae80516422138ea643236cf145f978245cbb) | Separate tasks within a sheet, across a drawing set and across a project; test navigation and reference resolution as well as local interpretation. | Apache-2.0 benchmark, not a QS skill. Its 196 tasks across nine families offer evaluation design ideas, not a performance score for Quantity Surveyor. We have not executed this benchmark. |

We also inspected the archived [Construction Drawing Analyzer](https://github.com/hamzaabduljabbar/construction-drawing-analyzer/tree/f0e798532643dc7f008f28b6994ae7feabed47cc). Its successor above is a more relevant reference. Repository stars, author-reported efficiency gains and results on a single example do not establish “best of breed” accuracy.

## Professional-tool references

[Bluebeam's viewport guidance](https://support.bluebeam.com/user-manual/menus/window/create-manage-viewports.html) supports treating different scaled areas on a page separately. [Bluebeam's calibration guidance](https://support.bluebeam.com/revu/how-to/set-the-page-scale-on-drawing.html) explains scale setup from a known measurement. [Autodesk's sheet comparison guidance](https://help.autodesk.com/cloudhelp/ENU/Takeoff-Files/files/Compare_Sheets.html) illustrates revision comparison and alignment. These inform the per-view calibration and revision controls; neither vendor has validated this skill.

The [AEC-Bench authors' research overview](https://www.nomic.ai/news/aec-bench-a-multimodal-benchmark-for-agentic-systems-in-architecture-engineering-and-construction) identifies navigation, spatial grounding and project-wide context as distinct challenges. It is vendor-authored research; its agent results do not transfer to this package or to newer model versions.

## What changed here

Version 2 adds issued-set selection, actual-versus-index coverage, per-view scale checks, cross-reference tracking, resumable batches, an evidence ledger, false-negative review and revision invalidation. It retains one portable instruction folder and optional helpers. No parser, vision detector, drawing database or CAD service is bundled.

The [drawing-set guide](DRAWING-SETS.md) proposes a representative, independently checked pilot and larger held-out evaluation before claiming full-set accuracy. That evaluation remains to be run on actual drawing sets.
