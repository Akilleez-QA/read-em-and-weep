# Independent review: complete rank-one Gauss flag exclusions

Verdict: PASS for the exact frozen proof and stated scope. No correction required.

## Bound artifacts

Author packet: .. (the parent directory of this review).

- PROOF.md SHA256 a75ab590e7f7e2ecdf4e89661f54c5edb38e9e0fe9a60c061321b048ec5d180e
- verify.py SHA256 43d2c07e50e97164d46976608f05b587359e86b11806ef198cccb4994151f841
- RESULT.json SHA256 f0f2aeb5180c393159d7e3f476ad59ea3e93ea8477a5e1ba7ab5b74d03ef97e7
- INPUTS.json SHA256 b2496b4522aecb03668082e42820b6c0139a5c02ceaa37b38b2e71435bba8e39

Independent verifier: independent_check.py, SHA256 631a60c89902531552449a6ba18ff9063e82528f0990aae7d55547089eb26eff.
Independent output: RESULT.json, SHA256 bc4f7d4fc6d0ca37080550a31592ac2be572ce59659f73e7b87d85045833c292.

The complete frozen proof was read, including all-source reduction, predecessor dependence, termination at F14=0, orbit-degree arithmetic, all seven exact Euler contradictions, and the separate early r5 envelope. Detailed independent reasoning is in GEOMETRIC-REVIEW.md.

## Evidence

Eleven complete public source files were freshly downloaded through the connected GitHub reader. The ten antecedent originals match their byte counts, SHA256 and Git blob identities; the newly public PR1158 full proof at bfbb3fe3dd0659e69b6b818ec86038a62ebd2675 matches the frozen scalar-endpoint lemma SHA256 d76c66aac6cf179ae06a03d311edffe819834db6aa6dee1f39d59cd76ed7d2af. Exact downloaded bytes and source metadata are retained in authenticated/ and AUTHENTICATION.json.

Author commands python3 verify.py and python3 -O verify.py both passed 1003 explicit checks plus 81 character-module checks; both outputs match the frozen RESULT.json byte for byte.

Independent commands python3 independent_check.py and python3 -O independent_check.py both passed 509 explicit checks and produced identical output. This evaluator uses the closed binomial formula for SU2 symmetric-power characters at the nine conjugacy classes and exact Q(sqrt5) inner products, rather than importing the author's production recurrence. It checks orthogonality of the complete irreducible table, enumerates the full necessary orbit-degree semigroup directly, finds the five plus two complete deficit patterns, computes their signed Euler residuals, verifies the common cubic-zero obstruction and missing degree14 invariant, and independently computes the r5 early-envelope obstruction. All seven degree-list/residual pairs also match the author's output in an order-independent comparison.

## Geometric points checked

1. A cubic-zero V multiplicity -1 excludes V/Z sources; D's forced O2 image is impossible because both the negative-doublet degree and the scalar Sym14 invariant condition fail. This legitimately reduces all four actual sources to P.
2. PR1158 is used only to force the initial coherent image O14 at k=1. It did not already exclude either target, and the current proof does not misattribute the new exclusion to it.
3. Each backward derivative kernel is saturated in the constant ambient. Negative nonzero bundles cannot be horizontal. The preceding rank-one quotient bounds every next derivative by one, hence it is exactly one until fourteen lines exhaust rank14. There is no unsupported rank-three continuation or horizontal splitting.
4. The induced injections Q(j+1)->Qj(-2) include the terminal quotient. Perfectness removes line-character ambiguity; their invariant divisors have degrees in the orbit semigroup. The weighted equation correctly uses thirteen deficits with weights13 through1.
5. Exact equivariant Euler additivity, not virtual genuineness, is the decisive full-flag condition. All seven residuals are nonzero despite zero ordinary dimension. In particular A_std and V remain distinct irreducibles.
6. The F7/F8 indexing and twist10 early envelope are correct. Its r3 value is genuine and is not incorrectly used to exclude r3; the full-flag argument supplies that exclusion.

## Scope of approval

Both shapes W'O(-3)+O16 and W'O(-5)+O16 are excluded for every actual primary source under maximal lower plateau length k=1, including profile-(1,1) occurrences. No conclusion of whole-profile closure, live count, full-adjoint invertibility, original theorem repair or proof-assistant verification is approved. No actual instance coefficient, point, jet, matrix, rank experiment or historical enumeration was run. No external write was performed by this reviewer. This review is supporting verification, not an independently claimed new proof-repair contribution.
