# Optional memory helper and portability tests

13/13 test groups passed; 0 failed.

These tests run the actual packaged script in separate processes with `-I -S`, synthetic records and isolated temporary storage. No private installed skill or memory was accessed. Package files were not modified.

Reproduce with Python 3.10+ (uses `sys.stdlib_module_names`):

```text
python3 test_memory_helper.py --package /absolute/path/quantity-surveyor-portable --work /temporary/work --output /results/helper
```

Actual commands, exit codes, standard output and standard error are captured in `process-transcript.json`. `results.json` maps each group to the transcript event numbers. The transcript includes synthetic test content only.

| Test group | Outcome | Observed result |
|---|---|---|
| explicit configuration required | PASS | All required and whitespace-only configuration failures returned exit 2; no store created. |
| provenance requirements | PASS | Missing, empty, unstructured and incomplete provenance all refused before state creation. |
| same-root user and project isolation | PASS | Three scopes at the same root hold disjoint records; a fourth sees none. |
| tentative versus verified and identity protection | PASS | Default listing returns verified records, tentative suggestions stay separate, identity injection is discarded and tentative correction leaves verified bytes intact. |
| correction history and duplicate refusal | PASS | Two successive corrections preserve all three rows and bidirectional links; duplicate and unknown corrections refused without changes. |
| invalid JSON refusal without data loss | PASS | Invalid incoming JSON preserves current and previous copies; corrupt stored JSON refuses reads/writes and preserves exact damaged bytes. |
| wrong-scope envelope refusal | PASS | Wrong-scope current envelope and previous copy both refused; no mutation or recovery archive produced. |
| confirmed previous-copy recovery and preservation | PASS | Recovery requires confirmation, restores validated previous snapshot, preserves damaged bytes in a mode-0600 archive, and visibly rolls back the latest addition. |
| unresolved lock refusal | PASS | Writes and recovery refuse a preexisting lock, leave lock and state intact; snapshot reader continues to work as documented. |
| concurrent subprocess writers | PASS | {"attempts": 32, "successful_writes": 12, "safely_refused": 20, "surviving_records": 12, "lost_successful_records": 0} |
| human-scope collisions and traversal-like IDs | PASS | Traversal-like IDs, slash-colliding pairs, Unicode and composed/decomposed Unicode remain distinct hashed scope names in the chosen root. |
| relocation and isolated standard-library execution | PASS | {"cwd_outside_package": true, "relocated_path": "<workspace>/work/helper-regression/run-1790875665500144000/relocated package with spaces", "interpreter_flags": ["-I", "-S"], "imports": ["argparse", "contextlib", "datetime", "hashlib", "json", "os", "pathlib", "sys", "tempfile", "uuid"], "external_dependencies": []} |
| blank original templates and optional core tools | PASS | {"changes.csv": "header-only CSV; no filled rows", "estimate.csv": "header-only CSV; no filled rows", "forecast.csv": "header-only CSV; no filled rows", "project-basis.md": "empty prompts; no filled values", "core": "Explicitly requires no service, connector, model or proprietary library; memory optional. No hardcoded private user paths or installed-memory lookup."} |

## Limits and material findings

No material defect found in the requested memory-helper behavior. The helper validates evidence fields but cannot establish factual truth; `verified` is a user-supplied state. Exact Unicode scope identifiers remain separate: composed/decomposed forms and trailing whitespace can create distinct scopes, so callers must consistently reuse their chosen identifiers. This is documented exact-scope behavior, not a collision.

Concurrency means successful writes serialize while contenders may fail with an explicit lock error. The test compares every successful writer ID with the final store and checks that no successful record was lost. It does not establish power-loss durability, network filesystem safety, distributed transaction support, encryption or resistance to hostile filesystem access.

Core portability is checked by inspecting the package core and blank templates and executing the optional helper after copying the package to a path with spaces from a working directory outside the package. No independent model/harness execution of the surveying workflows is implied. The standards reference is being authored separately and was excluded from missing-file findings.

All fixture and copied-package state is under the work directory reported in `results.json`; original package files remain untouched.
