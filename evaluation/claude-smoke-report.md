# User-reported Claude smoke check

Report received: **1 October 2026**. Source: the user's report in the repository-maintenance conversation. This document records that report; the maintainer agent did not independently execute or replay these Claude runs.

| Observation | Reported result | Scope known from the report |
|---|---|---|
| Native activation | One successful trigger in Claude Code | Exact prompt, model/build and installed version for that trigger were not supplied. |
| Task answers | Four cases run on skill version 2.0.1; all four reported correct | The inputs were cases from this repository's published evaluation suite. Case IDs and full answers were not supplied here. |
| Usability | No wrong answers attributed to the reported friction | Overlapping take-off routes, apparently mandatory standards loading, missing early-stage advice routing and incomplete template links. |

The tester described the four-case run as blind. Because the cases are already public and the execution record is not available here, this project treats the result as a **smoke/regression check**, not fresh held-out evidence or a numeric competence score. It is encouraging but too small to support an accuracy percentage or cross-model equivalence.

The report does not establish claude.ai/Cowork upload behavior, persistent storage across sessions, large-drawing-set accuracy or execution of releases 2.0.2/2.0.3. Version 2.0.3 changes routing in response to the usability feedback; those changes need their own Claude follow-up. Prior scoring records are unchanged.

A more reproducible follow-up would retain skill version/hash, model/build, host, exact prompts, loaded references, case IDs and full outputs, with fresh unpublished cases when making a new blind-performance claim. Unknown fields remain unknown rather than being reconstructed from expected answers.
