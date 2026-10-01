# Final independent helper regression verification

Missing-primary regression: **PASS** across 20 subprocess invocations. Existing suite: **13/13 groups passed** across 108 subprocess invocations.

Candidate helper SHA-256: `9e7eb6bbd3906a120a9567d57a2da273809f1e2ff63154975be5e07fff5962d4`. It remained unchanged before and after both tests. Tested with Python 3.12.6 using isolated subprocesses (`-I -S`) and synthetic scoped memory.

This is explicit regression verification of a disclosed fault path and rerunning established tests; no blind new-case testing is claimed. The tester independently constructed and executed the missing-primary scenario without reading another test's regression, prior critic/grades/oracles, private installed memory or estimating keys. No package edits were made.

A populated previous snapshot was created by two normal additions. The main JSON was preserved in scratch storage then deleted to create the fault. `list`, `check`, `add`, and `correct` each returned exit 2 with the missing-primary/previous-copy error. Following every refusal, the main file remained absent, no lock was left, and the surviving previous copy was byte-for-byte unchanged. `recover` without confirmation likewise refused without changing that copy.

`recover --confirm` restored the previous copy byte-for-byte and kept the available backup unchanged. With no main file to archive, `preserved_current` correctly returned null. Recovery restored the earlier record, not the latest unavailable record. A subsequent addition retained the original record and safely updated the store; a subsequent verified correction preserved linked history. The recovered scope ended with three valid records. A separate genuinely new scope listed empty, reported `exists: false`, accepted its first addition, and left the recovered scope's files unchanged.

The 13-group rerun covered required explicit configuration, provenance, user/project isolation at one root, tentative/verified state, correction history and duplicate refusal, malformed JSON, wrong scope, damaged-current recovery, unresolved locks, concurrent writers, traversal/Unicode identifiers, relocation with spaces from an external working directory, standard-library-only operation, and blank templates/core optional tools. Concurrent writer result: 13 successful writes, 19 safe lock refusals from 32 attempts; all 13 successful records survived.

No material remaining defect was observed in these exercised helper behaviors. These local tests do not establish power-loss durability, distributed filesystem safety, hostile-access protection, truth of supplied provenance or surveying workflow compatibility across every model/harness.

Reproduce from this evidence directory:

```text
python3 test_missing_primary.py --package /absolute/package --work /temporary/work --output /results/helper-final
python3 test_memory_helper.py --package /absolute/package --work /temporary/work --output /results/helper-final
```

`missing-primary-results.json` contains the candidate hashes and storage snapshots; `missing-primary-transcript.json` contains all targeted commands, exit codes and actual output. `results.json`, `process-transcript.json` and `report.md` contain the established suite's results and actual output. Each test runner is included here.
