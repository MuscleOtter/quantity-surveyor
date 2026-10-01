# Astra independent review — v2 drawing workflow

## Scope and result

Reviewed the frozen `skills/quantity-surveyor/references/large-drawing-sets.md` against the main skill, relevant evidence and measurement references, both new CSV templates and six frozen workflow probes. All manifest hashes matched at review time. No external services or earlier benchmark answers were consulted. This is a document and text-probe review, not a visual drawing-set benchmark.

**No release-blocking material error, unsupported accuracy claim or required proprietary dependency found.** The reference explicitly distinguishes extracted text from visual review, supplied coverage from expected-set coverage, candidate matches from physical instances, and arithmetic reconciliation from scope completeness. Its issue control, per-view calibration, crop deduplication, rejected-candidate review and dependent-cache invalidation controls address the main failure modes represented in these probes. Capability limits and coordinate uncertainty have usable fallbacks. Simple arithmetic is explicitly exempted from the full workflow.

## Non-blocking refinements

1. **Clarify review stage versus unresolved disposition.** In “Establish the set,” inventoried/text-indexed/visually inspected/reconciled sit beside unresolved/excluded as “states,” while the register supplies one `review_state` field. A sheet can be visually inspected and still contain unresolved scope. The separate unresolved-query and view-locator fields mitigate this, so it is not a blocker. A short instruction to preserve completed review stage alongside open disposition, or to use separate view-level rows, would prevent a later editor from overwriting useful coverage history with a single “unresolved” value.

2. **Qualify the pilot reference take-off.** The final paragraph usefully requires an independent human take-off and does not claim full-set accuracy. Calling that result “ground truth” could nevertheless encourage treating a single human pass as infallible. Define the comparison reference as an adjudicated take-off with disputed items retained and reconciled, and choose pilot coverage that includes difficult/rare relevant cases as well as routine sheets. This would strengthen future empirical evaluation without expanding the everyday workflow.

## Complexity and portability

The controls are substantial but justified for large coordinated sets. Optional tables, optional hashes and explicit text-only fallbacks make the workflow portable. Reviewing rejected candidates and independently sweeping relevant regions can be expensive; that cost is a necessary limitation to disclose when claiming completeness, rather than a reason to substitute detector confidence. The existing proportionality and pilot language prevents this from becoming a universal requirement for every minor calculation.

The new reference is ready as workflow guidance subject to those optional refinements. It supplies no evidence of measured drawing-detection accuracy, scalable throughput or performance on real projects; the text probes must remain labelled accordingly.

## Follow-up — 2026-10-01

Verified the final candidate against `frozen.json`: every listed file matches its SHA-256 hash. Comparing `frozen-initial.json` with the final manifest shows changes only to `references/large-drawing-sets.md` and `templates/drawing-register.csv` within the skill. Reversing the two reviewed paragraph edits and the register header change reproduces the initial hashes, confirming the bounded delta described in `changes-after-review.md`; all other frozen sources and the six cases remain unchanged.

Both optional findings are resolved. Review stage and open/resolved/excluded disposition are now explicitly separate, with matching register columns and view/scope-level guidance. The pilot now requires an independently prepared, adjudicated reference, includes difficult and rare relevant cases, and retains disputed reference items for reconciliation. No new blocker or material regression found. The refinements do not alter the six probe conclusions, so a full rerun is unnecessary. The initial review and retained responses are preserved; this follow-up remains a text-only instruction review and supplies no visual accuracy evidence.
