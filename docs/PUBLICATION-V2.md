# Version 2 publication verification

Verified 1 October 2026 after publication of [Quantity Surveyor 2.0.0](https://github.com/MuscleOtter/universal-quantity-surveyor/releases/tag/v2.0.0). Release source: `c0da4a6d31b7ff0db33cdd58ca8f17125f5c6d57`. This later documentation record does not change the release tag or installed package.

- [GitHub validation](https://github.com/MuscleOtter/universal-quantity-surveyor/actions/runs/36903490009) passed every check on Python 3.10 and 3.12: package/source/link/discovery validation, nine update tests, both memory suites and release build.
- All five published assets downloaded without authentication and matched local bytes: new ZIP/Markdown, legacy-named aliases and checksums. The ZIP contains 19 files under one `quantity-surveyor` folder.
- All 13 raw documentation/instruction links in llms.txt returned HTTP 200 and matched the committed local content at verification. The cover URL also returned HTTP 200.
- The unchanged version 1 checker reports `update_available` for 2.0.0. The version 2 checker reports `current`. The repository address is preserved; no automatic installation occurred.
- Local skill-format validation, the same updater/memory checks, preserved historical evidence hashes and final v2 source hashes passed.

[Machine-readable publication results](../evaluation/v2-drawing-workflow/publication-verification.json) contain checksums and public URLs only. The cover was copied unchanged from the user's selected latest image; its SHA-256 is `6ba6469fba58fbbc516fd3eee0d34419c844676310759dddd4af26043c98b85e`.

These checks establish publication integrity and the tested helper/package behavior. They do not establish drawing-set accuracy, every host's native installation behavior, search indexing or AI citations. [Evaluation boundaries](EVALUATION.md), [drawing-set validation plan](DRAWING-SETS.md), [historical version 1 publication](PUBLICATION.md).
