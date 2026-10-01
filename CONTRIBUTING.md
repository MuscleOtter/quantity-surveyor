# Contributing

Improvements should make a real QS decision clearer or reduce a demonstrated failure. Keep the instructions portable and proportional. Do not add mandatory vendor tools, model-specific forks, unsupported prices, professional credential claims or proprietary standard excerpts.

1. Describe the concrete problem with a synthetic example.
2. Make the smallest justified change to the canonical skill folder.
3. Run `python3 tools/validate.py` and `python3 -m unittest discover -s tests -p 'test_updates.py'`.
4. For memory changes, run both subprocess suites (see `docs/EVALUATION.md`).
5. For behavioral changes, freeze a new suite/candidate before fresh blind outputs and independent grading. Retain failures and deductions. Existing evaluation answers are now public, so they are regression cases rather than future held-out evidence.
6. Update the changelog/version and build assets with `python3 tools/build_release.py --out dist`. Do not hand-edit the combined Markdown edition.

You retain responsibility for contributed material's rights. Never commit private projects, rate libraries, memory stores, credentials, licensed PDFs or copied publisher corpora. Use synthetic fixtures and original examples. The pull request should explain the changed behavior, validation and limitations. Release publication remains an explicit maintainer action.
