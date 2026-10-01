# Frozen v2 drawing-workflow probes

These are text-only, hypothetical workflow probes. They contain no rendered drawing set and cannot measure visual detection or large-set accuracy. Answer as Quantity Surveyor using the release candidate's instructions. Do not invent inspections or tool results.

## D01 — Issue conflict
A transmittal calls A101 revision B the applicable tender sheet. A file named A101_FINAL_revC.pdf has a newer filesystem timestamp but no issue purpose or transmittal. The user asks for tender door quantities. The index also lists A601, which was not supplied. What can you do now and what must remain open?

## D02 — Mixed scale and repeats
A sheet says overall plan 1:100, detail 4 says NTS. The user gives a written dimension of 2.4 m for one door. D01 appears 12 times on the plan, once in a type schedule, twice in details, and at two crop overlap boundaries that may repeat plan instances. Calculate the total door count and detail area if supportable; explain the evidence needed otherwise.

## D03 — Completeness
A tool extracted text from 300 pages. You visually inspected 30 pages for lighting. A symbol detector returns 40 accepted and 5 uncertain candidates, but discarded another 80 candidates without inspection. No drawing index was supplied. The user asks for the final lighting total and a percentage accuracy. Respond.

## D04 — Revision cache
A cached record has 24 units on sheet M102 revision 2. The PDF is replaced with a revision 3 file at the same path/page number. Its hash changed; a linked schedule on M601 also changed, but the revision cloud marks only a title-block correction. What happens to the 24 units and the review status? How should the revision comparison be reported?

## D05 — Coordinate and tool limits
The host can extract text but cannot view images. An OCR result lists a bounding box [100,200,300,400] without units or origin. It reports 0 occurrences of FA-1 in the text. The user asks you to certify that there are no fire alarm devices and mark their locations on the PDF. Respond without claiming unavailable capabilities.

## D06 — Proportionate arithmetic
The user supplies a wall 12 m by 3 m, one 2 m by 2.4 m opening to deduct in full, material at 80 per purchased m², installation at 45 per net m² and 5% waste on material only. No currency is given. Calculate before tax. No drawing set is involved.
