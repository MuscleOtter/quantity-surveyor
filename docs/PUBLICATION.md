# Publication verification

Version **1.0.0** is published in the public [MuscleOtter/universal-quantity-surveyor repository](https://github.com/MuscleOtter/universal-quantity-surveyor), on the `main` branch with source tag `v1.0.0`. The [release](https://github.com/MuscleOtter/universal-quantity-surveyor/releases/tag/v1.0.0) includes the skill ZIP, complete chat Markdown edition and checksums.

On 1 October 2026, unauthenticated public downloads of all three assets returned HTTP 200 and were byte-for-byte identical to the separately reviewed local artifacts. The ZIP contains 16 files under the matching skill folder; extraction/version-manifest checks passed. The public cover URL returned HTTP 200 and image/png. [Machine-readable evidence](../evaluation/publication-verification.json) records hashes and sizes.

The real optional checker returned **current** for installed version 1.0.0. A separately labelled simulated older local version 0.9.0 returned **update_available** against the real release and supplied the correct release URL and ask-before-installation action. Neither check replaced files. Nine deterministic updater tests also cover malformed metadata, stable numeric comparisons, offline behavior, credentials/data boundaries, network failure and interrupted reads.

[GitHub CI for the published source](https://github.com/MuscleOtter/universal-quantity-surveyor/actions/runs/36901819887) completed successfully on Linux with Python 3.10 and 3.12. Both jobs ran package/evidence validation, update tests, both optional-memory suites and a release build. Local verification also ran on macOS arm64/Python 3.12.6.

This is publication, download and executable-package evidence. No Claude-account installation, native automatic skill routing, open-model behavioral execution or real-project validation was performed. The documented wall calculation is a setup smoke example, not an independently executed cross-provider test. The personalized original source was preserved; private memory was not accessed or migrated.

This document was added after the immutable v1.0.0 source tag to record the actual publication results. It changes no installed skill files or release assets. See [Astra's earlier distribution review](DISTRIBUTION-REVIEW.md) for the separately reviewed build.
