# Review: six source-edge exclusions for the retained O(16) labels

## Verdict and exact binding

**PASS for the six source-edge exclusions, with exactly the stated scope.**

This review applies to these exact file contents:

- `PROOF.md`, SHA-256 `e1c5bdad0cfe1f989ba1d325d35cd80d69dafc961da7710691a173c235b0af9a`.
- `verify.py`, SHA-256 `b37855cd689f595ade7d82449ecefad8c562fd7c4db8d729587a27ec4aee9bf8`.

The review checks the mathematics as well as the bounded verifier. It is not proof-assistant certification. Its verdict does not extend automatically to a modified proof or verifier, another source edge, or any separate subsequent argument.

## 1. Pinned dependencies and catalog audit

The five original dependencies are at commit `db51525015bb7c5e825833d550d08dedf6f6ea96` under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

Their immutable path-to-blob identities and the exact local audit-input contents were checked:

| File | Git blob SHA |
|---|---|
| ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 |
| NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md | d7506dae49b4be43230450c4132bd5db91f137ef |
| ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md | dcacf0bcdef8377c1ed7654e5b82659ea409456e |
| one-one-endpoint-necessary-pairs.json | fe0afa410d89340d3082dc814277f89fbb582c19 |
| rank-three-quotient-frontier-144.json | 8b5971092f9ef762584912609fd5e9301c4e271d |

The two additional proof dependencies were also fetched and their immutable path-to-blob identities checked:

- [PR796 proof at d2b43060c83328dd5118aee6b9288fcfa0c873ac](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md), blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`.
- [PR802 proof at e484640a6565c278321bf6557860262c1ac1b7df](https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md), blob `98a1bd6123e148476da0b997d879aecbf885ec97`.

Only the actual internal/external derivative-image lemma, the profile-free quadratic rank-one gap, and first-polar generation are needed from these later proofs. In particular the profile-(1,2) section-free interior condition is not imported.

The three stable labels, original indices, A_q and B_q splittings, and zero determinant defects agree with both original catalogs. Independently of the verifier's length-and-membership assertions, the entire source lists were compared with Section 1: the lists at indices113 and125 are exactly the ten tuples described by its formula, and the list at index127 is exactly its thirteen displayed tuples, without duplicates. All six edges belong to those lists. Applying the original eight-parameter decoding formula gives exactly the bundles used in Sections 3-6.

The catalogs remain necessary overlists. Their completeness as necessary inputs does not assert realizability of any member, nor supply a current frontier count.

## 2. Common high-line interface and complete kernels

For each selected F, the actual strict-top vanishing gives the required injection on H0(F(2)); this is not an unsupported inference of fiberwise injectivity into a line. The absence of a component to the lower positive quotient is separately justified by its equivariant Hom, or, in the index125 ee case, by the intrinsic kernel construction.

An invariant common divisor of the O(18) section system would have degree at least12 and leave at most seven independent sections. This contradicts the established eight or eleven independent sections. Therefore p is onto everywhere. Original determinant defect zero makes the external O(16) a saturated subbundle of Q(-2).

The cohomology budgets and Euler characters in (1) follow from the exact line-system sequence. Central parity and the dimension bound exhaust the nine displayed atoms with j>=4. The degree-minus-three coefficient contributes only to H0 at twist3. The negative W multiplicity forces O(-6) or W O(-7), each consuming the unique A budget; the remaining S requirement and V budget then give exactly the two kernels for each m. There is no omitted high-degree kernel atom or cancellation between genuine H1 constituents.

## 3. Internal images and saturation

All atomic internal Hom spaces for both kernels and all five target forms were checked. For the complementary-D cases the sole possible nonzero map in either kernel branch is respectively

    W O(-7) -> D O(-4), or O(-8) -> D O(-4).

Both Hom spaces have dimension one. Their nonzero maps are the universal multiplication W tensor l^3 -> Sym4 W and the tautological l^4 line. Their ranks are respectively two and one at every line l. Thus their images are saturated; there is no scalar-zero, rank-drop, divisor, or mixed-image branch left unexamined.

For the be, ce and ee cases every internal component vanishes. In every case the internal image and external line are saturated. The actual quotient by the full raw derivative image is an extension of locally free quotients, so the exact sequences (6) indeed describe the actual saturated first forward transform. No numerical degree calculation is being applied to a merely generic image.

## 4. Complementary-D obstruction

The zero internal image gives degree2 for a subbundle of a constant bundle and is impossible.

For internal image O(-8), first-polar generation and saturation force all degrees of M to be0 or-1. Its constant coefficient is A+V, while its prospective linear coefficient is Wp+T-S. The negative S multiplicity is an actual representation-theoretic contradiction, not just a numerical rank mismatch.

For internal image W O(-7), the same reasoning forces

    M = V O + (Wp+T) O(-1).

The V here is the actual constant space H0(M) in H. Quotienting by that constant space preserves the constant connection and gives a saturated inclusion of L0=(Wp+T) O(-1). The derivative of the projected F stays inside L0.

There are exactly two multiplicity-one channels from P O(-2), with linear rows lambda and mu on the two-dimensional P multiplicity space. If the rows are dependent, their common kernel contains an entire rank-four P block whose original inclusion would land in the rank-three constant V. If independent, ker(mu) has nonzero lambda, whose tensor-Wp Euler map is onto the entire Wp O(-1) summand.

The latter case is also impossible: local sections of that summand lift through the image of the projected F, so their derivatives remain in L0. The first span of an embedded pure degree-minus-one block is its nonzero constant coefficient space. This would put a constant subbundle in L0, contrary to H0(L0)=0. This argument requires neither saturation of the projected F nor a horizontal splitting of M; it uses the actual constant projection and local lifts. It therefore exhausts both row cases without an implicit connection assumption.

## 5. The other three edge arguments

- **index113 be:** both exact kernels have zero internal image in T O(-5)+Wp O(-7)+O(-12). The resulting first-span degree2 is impossible.
- **index113 ce:** both exact kernels have zero internal image, giving F^+/F=O(18) with rank F=11. The profile-free quadratic rank-one gap requires b=22 or b<=10. Neither holds. Its quadratic second-span proof does not assume an interior plateau, H0(E^+)=0, or any maximal-profile endpoint condition.
- **index125 ee:** strict-top injects 3P into H0(O(6)+O(18)), whose P multiplicity is exactly three. Hence the map on P multiplicity spaces is an isomorphism, its O(6) projection is nonzero, and that projection has a two-dimensional constant multiplicity kernel. The resulting F=2P O(-2) is saturated and maps injectively on sections to O(18). Both exact kernels then have zero internal image in P O(-4)+2Wp O(-7)+O(-12), again forcing first-span degree2. The construction of F is intrinsic linear algebra, not selection or evaluation of an actual source instance.

## 6. Exact six-edge coverage

| Original index and stable label | Tuple | Excluding argument |
|---|---|---|
| 113, G3.11.ad509d55173f | (0,0,0,0,1,1,0,1) | Section 3, complementary D |
| 113, G3.11.ad509d55173f | (0,0,1,0,1,0,0,1) | Section 5, ce quadratic gap |
| 113, G3.11.ad509d55173f | (0,1,0,0,1,0,0,1) | Section 4, be zero internal image |
| 125, G3.11.ea6bced3bddf | (0,0,0,0,2,0,0,1) | Section 6, ee forced kernel subblock |
| 127, G3.11.cce6e3ba4eeb | (0,0,0,0,1,1,0,1) | Section 3, complementary D |
| 127, G3.11.cce6e3ba4eeb | (0,0,0,0,1,0,1,0) | Section 3, complementary D |

Each conclusion covers the whole stated source stratum. Basepoint-free behavior and image saturation were proved, not imposed as extra branch assumptions.

## 7. Verifier and boundary

Running `python verify.py` with the exact pinned JSON inputs returned:

    PASS: nine declared kernel atoms; four exact kernels; 80 fixed atomic Hom checks; polar characters; all six original source-edge identities.
    No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.

The code uses exact Q(sqrt(5)) character arithmetic, verifies orthogonality of the nine irreducibles, and checks the declared finite identities. Its kernel checks confirm the proposed kernels; their completeness additionally depends on the mathematical budget argument reviewed above. Similarly, the code does not replace the saturation, constant-connection, or row-surjectivity proofs.

No selected actual HM/source coefficients, parameters, points, derivative values, matrices, instance ranks, models, or large computations were used. The exact tuple reads and abstract universal representation checks are within the declared scope.

No whole-label exclusion, current necessary-pair count, source2 conclusion, O26 conclusion, low-positive conclusion, or original global rank conclusion follows from this review. No mathematical gap was found in the six stated exclusions.
