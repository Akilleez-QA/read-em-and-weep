# Actual corrected HM generator a=(12)

## Result

This implements the actual ordered-model map `T_a = P rho((12)) I` in the pinned full-sign finite HM complex, over Q using exact BigInt integer arithmetic. It does not use an ambient polynomial, construct an obstruction, or identify any input with a geometric class.

The full-sign finite dimensions in degrees 0 through 4 are `(0,2560,6560,4080,354)`. The non-harmonic pieces are:

| Degree | Correction shape, rows × columns | Nonzero columns | Nonzero entries | Coefficients |
|---|---|---|---|---|
| 2 | 80 × 6480 | 272 | 568 | ±1 |
| 3 | 160 × 3920 | 1128 | 1664 | ±1 |

The three permitted terms are explicitly evaluated. In degree 2 only `(u,v)=(1,3)` survives; in degree 3 only `(u,v)=(2,2)` survives. The vanishings are exhaustive and have the algebraic explanation in `ALGEBRA.md`.

`verify-generator.js` checks `dT_a=T_a d` on every source basis vector in degrees 1, 2, and 3: respectively 2,560, 6,560, and 4,080 columns. It also checks `d²=0` on all degree-1/2 columns and verifies the harmonic and correction blocks of `T_a²=1`. This strict involution is a verified fact for this generator only; no relations involving other generators or a strict D8 projector are asserted.

The exhaustive verifier and pinned oracle self-test were rerun successfully with Node v24.19.0 before publication. The self-test compares every entry of the initial differential and all ten higher-kernel columns with the original PR5 verifier. Runtime is recorded in the regenerated certificate and is not part of the mathematical claim.

## Run and use

No installation or network access is needed.

```
cd research/hm/d8-small-certificates/generator
node verify-generator.js
node full-sign-boundary-oracle.js --self-test
node generator-action.js --apply sample-basis-column.input.json
```

The last command accepts the existing oracle's rational input schema (`basis`, `source_commit`, and sparse `entries`, or dense `negative`/`positive` arrays) and writes a rational degree-two vector in the same schema. It can therefore be passed directly to the existing boundary oracle. This does not certify that the supplied vector is an authenticated obstruction.

Programmatic API: `applyDegree2({negative,positive})` accepts BigInt vectors of lengths 6480 and 80. `applyDegree3` accepts lengths 3920 and 160. `correctionTerms` returns the three correction vectors in increasing v order: `(3,1),(2,2),(1,3)`. Both APIs compute the map from the HPL operators, rather than trusting the saved matrix file.

The example input is a basis vector divided by 7, not a cocycle or obstruction claim. Its negative key is `(2,0,0,0,-3,-2,-2,-3)`. Its image has negative key `(2,0,0,0,-2,-3,-2,-3)` with coefficient -1/7 and positive key `(0,2,5,0,0,0,0,0)` with coefficient -1/7. This gives an explicit nonzero correction missing from the naive harmonic permutation.

## Basis and signs

Basis ID: `hm-pr5-full-sign-harmonic-v1`. Each key is `(u,v,a,b,e1,e2,e3,e4)` with the same ordering as the oracle's `--basis` output. The negative degree-two summand has `(r,p)=(-2,4)`, the positive summand `(2,0)`. Degree three has `(-1,4)` and `(3,0)`.

The elementary symmetric substitutions, internal differential, endomorphism commutator sign, ordered h, and exponent pruning are taken directly from the pinned oracle. The new signed transposition swaps the first two exponent coordinates and B/C mask bits, multiplying by -1 exactly when both swapped factors have Čech degree 1. Multiplicity coefficients are fixed and the ordinary `y1 y2 y3 y4` generator has no extra sign. The harmonic negative blocks have the transposition sign; positive blocks are ordinary exponent permutations. Degree-two positive exponents are all zero, so that block is identity.

## Files

- `generator-action.js`: executable corrected action, pin checking, rational input adapter
- `verify-generator.js`: exhaustive finite matrix certificate
- `certificate.json`: exact counts, scope, source pins, runtime, and matrix digest
- `ALGEBRA.md`: mathematical justification and independent-review targets
- `sample-basis-column.*.json`: rational CLI regression input/output
- `full-sign-boundary-oracle.js`, `pinned-verify-hm-ext.js`: unchanged source dependencies

The `matrices_sha256` field hashes compact `JSON.stringify` serialization of the matrix object, not the pretty-printed file bytes. Its value is `b8a43d22da0b0e14a66c88b6e3d3653e94dfa31f7a1c739487a4cbe7267d1bf3`. The optional `generator-a-matrices.json` is not committed: running `verify-generator.js` regenerates it with the two correction matrices as `[target_row,source_column,integer_string]` triples and also rewrites `certificate.json` with the current runtime.

## Provenance

Original model: [PR5 verifier at add03476d9055aa00e1e00778eea6332cf8e01cc](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/verify-hm-ext.js). SHA-256 `1fe4608ed77f3767691e7ef4de375fc55b052ccf26159a4aae3ec6d35fe96414`, matching the previously independently reviewed source pin.

Boundary oracle: [exact source at a100f4e0be453d6e182320b792359f8a04e32b4d](https://github.com/Akilleez-QA/read-em-and-weep/blob/a100f4e0be453d6e182320b792359f8a04e32b4d/research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js). Git blob `8f534fd7a074e333fa031a6d8c51b864faf76d42` was recomputed and matched exactly; SHA-256 `29bbe778ed43ce91b52390d27fd78678879bb39c877982afb8063676b3fe1558`.

The action loader does not edit either dependency. It appends a local CommonJS export adapter at evaluation time to expose the already-defined operators. Both original files are SHA-256 checked before execution.

## Scope and handoff

The matrix identities are integral, so their reductions are valid over F3 as well. No characteristic-zero dimension or obstruction-identification statement is transferred to F3. No ambient obstruction, full D8 action/projector, detector completeness calculation, or new boundary decision has been attempted.

Independent reviewers should check the P-rho-I expansion order and signs, the discarded-A argument, the swap sign, the symmetric pruning window, and the basis indexing in the exhaustive chain checks. The exact executable output is ready for handoff to the finite-model owners.
