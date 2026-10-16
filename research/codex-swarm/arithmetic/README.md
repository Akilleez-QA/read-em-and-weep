# Two exact unresolved demands and conditional arithmetic plans

These are metadata contracts and conditional recurrence plans for two independently checked **UNKNOWN** demands. They do not evaluate a physical coefficient or implement a complete obstruction evaluator. Every physical admission flag remains false.

| Directory | Concrete scope |
|---|---|
| `seed12` | Original seed12 E34, four fixed owners: carriers5,1,2,4; standard1,9,13,15; masks8,9,11,15. Retains both residual paths R[1,0],R[1,1], all four E terms, coefficient2 times1/2, and four outer weights. |
| `seed30` | Original seed30 E34, five fixed owners: carriers0,1,2,3,4; standard0,8,12,14,15; masks0,1,3,7,15. Retains all four residual paths, effective q4 coefficient+1 times1/2, and five weights. |
| `primary_current` | A current-only rational/factored DAG adapter for three distinct source-sorted primary tail owners. It accepts actual arbitrary standard tags and rejects exceptional tail carriers. It does not supply the exceptional prefix, selector, scalar primitive, complete weighted derivative, or arithmetic admission. |
| `recurrence12` | Exceptional-prefix outer partition plan plus an executable **synthetic** bounded affine convolution. The auxiliary denominator conversion doubles its carrier order; actual combined orders are unresolved. |
| `recurrence30` | An independent divided-power/generating-function recurrence and signed Laurent demand plan. Tiny synthetic controls test the recurrence, not a physical partition expansion. |
| `ledger` | A synthetic single-snapshot schedule replay and a hash-bound join of the two candidate metadata contracts. It separates actual file lengths from unknown physical costs, never authenticates real ledger history, and never emits execution authorization. |

The two requests use fixed prefix masks. Replacing a prefix mask sum by its partition-of-unity value1 is a different family operation, never a multiplication by the number of masks. Code preserves the fixed masks and weights. Inserted-label lists in the seed30 scalar leaf are explicit finite **enclosures**; branch-specific standard-owner restrictions remain unresolved and must be bound before enumeration.

## Immutable dependency

The code reads PR #79 at `6e28c6b59f8245779f6c03a20798e4de6842ae19`. `package_snapshot.py` authenticates its release-manifest hash and every one of its65 entries before public modules are imported. The snapshot contains source code and proof metadata; no release command or incumbent scan is invoked here.

From the repository root, stage the pinned dependency without changing another worker's checkout:

```sh
git fetch origin 6e28c6b59f8245779f6c03a20798e4de6842ae19
swarm_snapshot=$(mktemp -d)
git archive 6e28c6b59f8245779f6c03a20798e4de6842ae19 research/hm/null-support-certificates | tar -x -C "$swarm_snapshot"
export NULL_SUPPORT_PACKAGE="$swarm_snapshot/research/hm/null-support-certificates"
```

Only this custom environment variable is used. The code is portable; it contains no producer's machine path. Python `-B` keeps the authenticated dependency directory unchanged.

## Reproduce bounded controls

Run each suite in a separate process because the imported public bindings validate module origins and some refuse preloaded modules:

```sh
for directory in seed12 seed30 primary_current recurrence12 recurrence30 ledger; do
  (cd "research/codex-swarm/arithmetic/$directory" && python -B -m unittest discover -v)
done
```

The same controls pass with `python -B -O`. They use source hashes, symbolic ASTs, integer/Boolean metadata, and tiny synthetic polynomials. No HM polynomial is expanded or evaluated.

The seed12 request and small canonical demand snapshot are retained. Regenerate the larger seed30 metadata contract when needed:

```sh
python -B research/codex-swarm/arithmetic/seed12/demand_seed12_e34.py research/codex-swarm/arithmetic/seed12/seed12-e34-request.json
python -B research/codex-swarm/arithmetic/seed30/seed30_e34_contract.py
```

These outputs are symbolic requests. Their serialized size and node count do not certify physical multiplication counts or live storage.

The portable candidate join regenerates larger symbolic metadata in subprocesses, checks its pinned hashes, and reports both physical byte bounds as unknown:

```sh
python -B research/codex-swarm/arithmetic/ledger/candidate_preflight.py
```

Its metadata input lengths total720769 bytes; this is **not** an arithmetic allocation certificate or a new resource allowance. The synthetic schedule validator checks accounting within a supplied snapshot only. It does not authenticate previous spending, revision monotonicity, real storage aliases, or cross-worker authorization. Byte reservations are commitments rather than individual caps. Real global-state receipts, source/pole proofs, and measured physical operation/storage bounds remain prerequisites for admission.

## Reviewed limits

The seed12 compiler explicitly records that the original selected seed4 lowering rejects its actual tail tags; it does not spoof those tags or use a fallback. The generalized current adapter is a separate, reviewed partial component. Joining it to the prefix kernel and scalar correction still requires a combined owner-specific denominator ledger, canceled-inner-quotient derivative proof, infinity/standard transport, and a complete operation schedule.

The finite-only `../source_jet_contract.py` is a separate lazy formal jet contract. Its finite-chart restriction is not silently substituted for these infinity-tagged requests.

Independent reviews: Codex-V01 checked complete fixed-owner/sign/request metadata; Codex-V03 checked source/current/frame formulas and both recurrences. Root repaired the seed30 interval ambiguity into explicit sixteen-element enclosures, added whole-snapshot authentication, removed staging paths, and reran the controls. Current verdict: physical extraction **unadmitted**; obstruction **undecided**.
