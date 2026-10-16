# AC binding-followup independent review

Disposition: **AC transitive replay-binding repair accepted narrowly; no blocker.**
The previously accepted mathematical envelope and exponent-height repair are not
reopened. Physical route remains BLOCKED_ROUTE with no admission capability.

Frozen producer marker before and after all controls: `b4ab5a47e4b3a64d11e674ce7a163ff959b16f0c3ad22216541e43a23a8e9b6b`.
Whole-envelope implementation SHA256: `bbe9ffd7154bcb1017e56834a1ffe24326b288d289299bc0bdcd67f4ba6f3e1c`.
New test SHA256: `6440c2a8c69b1539fbfd10c1184790416ff1794c493df32525cbcde808a2654c`.
Current historical independent-test adapter SHA256: `2f8d8e9485420879bf080d62744b19b39025ca5363a1e6c0ece8ca7a5f1331ce`.
Reviewed Wave7 runner SHA256: `b9dff82e5255dc2e614755657f85a88c9b208af59c000da5558c11759739cde0`.
The runner is root-owned; a later runner edit requires its own frozen-byte check.

The producer's five changed files are the whole-envelope verifier, producer
control file, README, PROOF and handoff marker. Source pins, whole-route envelope
JSON and blocked-route JSON retain the prior reviewed mathematical contents.
The fix verifies all13 SR-owned payload hashes, then parses the thereby frozen
source-pins manifest and verifies each of its10 declared local dependency bytes
BEFORE reading/parsing caller AST metadata. It imports or executes none of those
physical helper files. The immutable SR marker authenticates the manifest's
schema, paths and hash records themselves; editing those declarations without
an authorized new release is rejected at the preceding own-file hash check.
This is the complete **declared ten-file local closure**, not an assertion of an
unbounded recursive dependency scanner. The Wave7 runner additionally authenticates
the exact union with AC workspace inputs and its three declared immutable inputs.

## Reproduction and evidence

Direct entry point:

```sh
python -B research/codex-swarm/detector-admission/test_binding_followup.py
python -B -O research/codex-swarm/detector-admission/test_binding_followup.py
```

**12 tests passed per mode**, child unittest times0.095s/0.093s, supervised
wall0.150s/0.147s. Each child had RLIMIT_AS805306368 bytes, CPU59 seconds and
parent wall timeout60 seconds. No expected failures. An earlier preliminary
11-case pass was followed by the final12-case pass adding the real local-union
byte authentication control; only the final test hash above is the handoff.
The tests independently freeze-check every AC producer payload before and after.

The controls perform:

- A clean isolated, byte-only replay exactly matches the existing envelope JSON.
- The literal interface parity `sign=(-1)**sum(...)` is changed to
  `sign=(+1)**sum(...)`. AST node counts remain identical. The repaired build
  rejects the byte change before ast.parse; the route-certificate composition
  rejects it too, despite AC's own direct pins historically omitting that file.
- Corruption and removal are checked separately for EVERY one of the10 declared
  local dependencies. ast.parse is poisoned, so a failure after AST work cannot
  pass this control. Missing files may raise FileNotFoundError; changed bytes
  raise ValueError. Both are fail-closed and produce no envelope.
- SR marker drift, an owned program change and source-manifest drift are refused.
  Five malformed manifest cases cover schema, absent collection, unsafe path,
  invalid digest and duplicate-count change. They fail at the frozen own-file
  authentication, before altered declarations or ASTs can be trusted. No forged
  replacement producer anchor is introduced to bypass that protection.
- actual_route_certificate reaches the SAME dependency check through build;
  clean output equals blocked-route.json, and actual_admission still refuses.
- Runner tests use a wholly synthetic temporary repository and mocked immutable
  BYTE transport. They check the exact declared union, omitted/extra records,
  conflicting declarations, changed/missing bytes, invalid digests, traversal,
  absolute/noncanonical paths, symlink escape, and missing immutable records.
  The real union's local bytes are independently hash-checked, including
  interfaces.py and the RS/PH proof dependencies. No Git subprocess is invoked.

Only metadata modules whole_envelope, certifier and run_controls are loaded;
certifier reuses its generic schedule validator. Copied source/field/frame files
are read/hashed/AST-parsed as data and never imported. No actual source formula,
model polynomial, physical helper, owner generator, fiber, jet or coefficient is
executed. No large envelope integer is materialized and no physical budget is
created. These controls authenticate replay inputs; they do not prove layout,
cap-unit reconciliation or a current all-worker ledger.

## Historical preservation

review-independent.md and review-height-followup.md were left untouched. The
only changes to existing test_independent.py are its frozen MARKER anchor and
footer producer-count11→12. Its13 mathematical controls were not rewritten or
rerun by this narrow follow-up; the final bounded Wave7 runner owns aggregate
replay timing. New evidence lives in this report and test_binding_followup.py.

## Dispatch-only runner addendum

Accepted the root/cohomology runner's single-line dispatch correction. New runner
SHA256: `8f73ec1682aa997acbc78f92451811d3684c97c7b2e1ad024b32cbeebbf21309`. The earlier reviewed `b9dff82e5255dc2e614755657f85a88c9b208af59c000da5558c11759739cde0` hash above remains historical. Exact byte comparison
finds only line153 changed, with line count unchanged: the existing
independent-test --child predicate is parenthesized and ORed with the exact
`detector-admission/test_height_followup.py` lane/file pair. All authentication,
dependency, limits and execution-body logic is unchanged. The height follow-up's
--child branch runs its six tests once rather than recursively supervising both
Python modes. The top-level runner still supplies normal/-O independently.
No controls were rerun for this dispatch-only review; root's final bounded
replay must confirm six height cases per mode. This does not change the AC
mathematical acceptance or physical BLOCKED_ROUTE status.
