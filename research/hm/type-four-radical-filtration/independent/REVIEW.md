# Independent review: conditional type IV doubled Euler filtration

Verdict: PASS, conditional on PR1127 and its dependencies. This written-proof and exact-code review is not proof-assistant verification and makes no actual-source claim.

## Immutable reviewed packet

The companion packet `type-four-radical-filtration` has these SHA256 hashes:

- `PROOF.md`: `b8c82e49d9501437941054599c78b8dbc5f4b2f365abff6580a1f734ca714629`
- `verify.py`: `c54332e3748f42668606c80d6b0e25a9c03b0d95654e28679258e3a42e34d481`
- `RESULT.json`: `8bf9d0da1ffa33c5382d8eb8a54769d5a72d22803f046292e84f6e1de857f475`
- `INPUTS.json`: `55293661f9ad680ca876f7bd253ad421e43563ff4618e12cc91773eb066e8719`
- `README.md`: `32c9c3db4013eecbf9581fa0c59b218ce8587f8ca073c48a079d60ede6ebddd8`
- `inputs/PR1127-PROOF.md`: `3101157347802226a3b2638e76375854944d7a41d503b75b1591bc3eb66b1577`

The complete pinned input was read: https://github.com/Akilleez-QA/read-em-and-weep/blob/60dda5a940d5ba7ee081a86cd1b1a783a5952a39/research/hm/primary-quotient-composition/PROOF.md .

## Verified mathematical scope

For K=2T O(-3)+V O(-4), PR1127 identifies the two-dimensional radical as the two independent tautological channels from the bottom V into the two T copies. Their products vanish by block support. The isolated doublet L adds neither radical image nor extra operator constraints on K.

The sum of the two image sheaves is 2V O(-4), of rank6 and degree-24. The common kernel is all 2T O(-3), of rank12 and degree-36: already one tautological channel is injective on the bottom V, and there are no constraints on the T copies. Thus, unlike type III, image and common annihilator differ.

The doubled Euler sequence gives A/S=2V O(-2), rank6 and degree-12; K/A=V O(-4), rank3 and degree-12. Both inclusions and their composite are saturated. The verifier's local homotopies establish these facts over each full coordinate chart, not only generically. Its 15-dimensional and 17-dimensional stacked/concatenated factorizations correctly certify common kernels and images. In E, Ann_E(J)=L+A has rank14, degree-42, and quotient V O(-4).

The constructions are intrinsic because the Jacobson radical is intrinsic. Image and annihilator are preserved by every global equivariant bundle endomorphism via its two-sided ideal property. This does not assert stability under additional operators.

The middle sequence 0→S→A→A/S→0 is nonsplit even ordinarily: its twist by O(2) has h0 middle=0 but h0 of the hypothetical split sum=6. The distinct outer sequence 0→A→K→K/A→0 does split noncanonically. The proof correctly keeps these claims separate.

## Independent controls and execution

`python verify.py` and `python -O verify.py` reproduce the reviewed `RESULT.json` byte-for-byte, with109 checks, including68 clearly labeled inherited controls and41 type IV checks.

The independent relocatable standard-library `check_euler_overlap.py` and its optimized execution reproduce `REVIEW-RESULT.json` byte-for-byte, with51 controls. It computes in the x chart t=y/x that the difference of Euler right inverses is a(-t^-1). The class of -t^-1 survives in C[t,t^-1]/(C[t]+t^-2 C[t^-1]); doubling and tensoring with V gives the invertible coefficient matrix -Id_6. The determinant and cohomology dimensions are checked exactly. The bounded monomial controls supplement, rather than replace, the universal support proof of nontriviality.

No defect found. This neither selects nor eliminates an actual bundle type and does not establish positive/Q/Gauss compatibility, source occurrence, geometric coverage, full-adjoint invertibility, algebraicity, or a complete original repair.
