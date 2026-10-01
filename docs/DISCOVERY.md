# AI and search discovery

The public name is **Quantity Surveyor** and the canonical source is the [GitHub repository](https://github.com/MuscleOtter/universal-quantity-surveyor). The README explains the purpose, install routes, supported tasks, limitations, license and evidence in accessible text. Dedicated FAQ and drawing-set pages answer specific questions directly and link to supporting sources.

The repository provides [llms.txt](../llms.txt), a concise machine-readable documentation index following the [llms.txt proposal](https://llmstxt.org/), and [llms-full.txt](../llms-full.txt), a generated complete instruction edition. These are conveniences for agents that choose to read them. They do not install a skill, set crawler permissions or guarantee discovery.

**Google explicitly says it ignores llms.txt for ranking.** Its [AI optimization guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) recommends clear, useful, accessible content and ordinary search fundamentals. There is no special AEO file that guarantees inclusion, citations, rankings or traffic.

This repository uses descriptive headings, direct answers, stable public URLs, links between relevant pages, meaningful image alt text and precise evidence boundaries. It makes no fabricated review, accreditation or cross-model performance claims. We have not verified search-engine indexing or AI citations. A separate documentation website can be added if publishing volume warrants it; no website framework or backend is required to use this skill.

Maintainers regenerate llms-full.txt from the canonical skill with `python3 tools/build_release.py --sync-discovery`. The validator rejects drift. Edit the original instructions rather than maintaining a second AI edition. Keep the curated llms.txt links in sync when documentation moves.
