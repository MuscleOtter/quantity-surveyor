# Maintainer release checklist

Use stable `major.minor.patch` versions. Patch releases correct compatible instructions/bugs; minor releases add compatible workflows; major releases introduce significant changed expectations. State actual behavior changes, not only the version label.

1. For QS behavior changes, retain a new candidate and freshly frozen evaluation evidence. Update the validation's equivalence baseline deliberately; never rewrite old sealed answers or answer keys to improve a score. Update dependencies/official guidance when relevant.
2. Change `skills/quantity-surveyor/version.json`, SKILL metadata and CHANGELOG. Update the README/install guide's pinned example to the new tag. Record distribution-only additions separately from behavioral evaluation.
3. Run the [documented deterministic checks](EVALUATION.md#reproduce-deterministic-checks), including both optional-memory suites. Remove interpreter caches from the distributable and inspect files for private data and proprietary material.
4. Run `python3 tools/build_release.py --sync-discovery --out dist` before validation, then confirm the generated discovery file has no drift. Inspect the single-folder ZIP and complete Markdown file. Verify checksums and installation smoke steps. Read the generated chat edition, not just the source.
5. Commit the source and create the matching `vX.Y.Z` Git tag. Never move an existing published release tag. Publish a stable GitHub release with `quantity-surveyor.zip`, `quantity-surveyor.md` and `SHA256SUMS.txt`, plus the two legacy-named aliases produced by the builder; the whole-repository source ZIP is not the install package.
6. State supported formats, executed evidence and limitations in the release notes. Confirm the public latest-release endpoint, asset download links and read-only update checker work. Check CI results; any failures need a visible disposition.

Publishing a release makes it available; it does not replace users' installed instructions. Users retain their chosen version until they approve an update. Prefer corrective releases over replacing assets under an existing version. No automated release job or secrets are needed for this first architecture.
