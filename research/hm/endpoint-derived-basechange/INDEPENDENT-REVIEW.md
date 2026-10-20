# Independent review: relative order-six endpoint

## Verdict

PASS, within the stated dependency and scope limits. No mathematical correction is required in the reviewed argument.

Reviewed artifact: `PROOF.md`, SHA-256
`156551583b7c47d774d9fe7265d6c08dd212652cf28c2624d4395acb60fe5725`.

Review date: 2026-10-20 (UTC).

The verified new conclusions are relative `H^2_A=0`, the canonical identification of the torsion in relative `H^3_A` with two copies of `Ext^1_A(Q_A,A)`, and the natural fat-fiber description with multiplication-by-`z` restriction maps. The review does not assert that the exceptional quotient is nonzero or evaluate the original fixed endpoint.

## Checks performed

1. **The family and relative flatness.** The imported PR443 family is defined on precisely the locus where `1+alpha s` is invertible. At every permitted point, `tau(s)-tau(b)` is `s-b` times a unit. Its localized quotient therefore has the stated annihilator and length bound; the omitted ramified/singular parameter has not been silently included. The ordinary collision ideal and its sixth power are scalar extensions from the complex root space. They are flat over the parameter ring. Tensoring with the varying locally free coefficient preserves this flatness. This does not require flatness of `Q_A` or its cohomology modules.

2. **Transport, exactness, and coefficients.** PR437 proves its filtered identity for an arbitrary locally free target coefficient, not only an invariant HM bundle. Its scalar filtration identity extends from the field to `A`; projection formula and the specified target automorphism then give the displayed three summands with fixed `B_A` and transported `u_s,v_s`. The GL lift accounts for the line identifications. There is no illicit assumption that `B` is invariant under projective automorphisms. Applying an automorphism to the original regular pair preserves the exact adjacent-monomial resolutions, including at collision strata.

3. **Twists and surviving transpose maps.** All generator and syzygy twists match PR439. For `K_4`, dualizing the surviving first syzygy column gives `va-ub` with target `H^1(B(6))`; the other target is `H^1(B(7))=0`. For `K_5`, the surviving second column gives `vb-uc`, again with target `H^1(B(6))`. The unused source summands remain present. Both images are exactly the defining sum for `Q_A`, without asserting a new rank or dropping an incoming relation. The fixed Serre and coefficient-line conventions are retained.

4. **Long exact sequence and relative vanishing.** The imported positive `H^2` vanishings kill `R^2 F_0` and `R^2 F_1` after duality. The displayed kernel and cokernel segment follows with the correct degrees. The unknown `H^4` map has not been discarded: its kernel is a submodule of a finite free DVR module, hence finite free. It follows canonically that the torsion of `R^3 G_j` is the torsion of `coker L`. For `K_3`, the relevant `R^3 F_1` is zero. For the other two summands, torsion of `Q_A` makes the positive map generically surjective, hence its transpose injective over the DVR. This proves relative `H^2_A=0` without trying to specialize a generic vanishing statement.

5. **Torsion duality and canonicality.** With `I=im P` and `N=ker P`, the two exact sequences used in the proof consist of finite free modules except for `Q`. Their dual sequences give the canonical short exact sequence

   `0 -> Ext^1_A(Q,A) -> coker(P^vee) -> N^vee -> 0`.

   Thus its left term is exactly the torsion submodule, independently of a splitting. Identifying the two positive cokernels with the same quotient `Q_A` is canonical because they have literally the same image in the marked target. No canonical self-identification of `Q_A` with its Ext dual is claimed. The invariant-factor length and annihilator conclusions are valid, including the zero-module case.

6. **Derived base change and degree.** An affine-intersection Cech complex of the flat coefficient sheaf has flat `A`-modules and computes ordinary reduction to `A/(z^n)`. The DVR universal-coefficient sequence has the Tor term in degree `i+1`, as written. Character projection is an exact direct summand and commutes with the construction. At degree two the zero left term makes the Tor description canonical.

7. **Independent sign and transition verification.** There is also a direct check not relying on spectral-sequence conventions. Flatness gives the sheaf exact sequence

   `0 -> C --z^n--> C -> C_{A_n} -> 0`.

   Its connecting map, together with `H^2_A=0`, identifies the fat-fiber `H^2` with the kernel of `z^n` on relative `H^3_A`. The map from the sequence for `n+1` to the sequence for `n` is multiplication by `z` on the left copy of `C`, identity on the middle copy, and restriction on the quotient. Naturality therefore gives multiplication by `z`, not inclusion or identity, on the kernel descriptions. This confirms the stated Tor transition and its sign. The same calculation gives a composite of `e` restrictions equal to zero, and hence zero inverse limit. Stabilization of dimensions at thickness two is not confused with stabilization by isomorphisms.

8. **Special fiber and logical boundary.** Right-exact base change identifies the quotient's closed fiber with PR439's fixed positive-cohomology quotient, and PR439 supplies the field duality statement. This is compatible with, but is not obtained by tensoring, the zero relative `H^2`. The conclusions rule out a compatible nonzero infinite lift in this specific parameter-thickening tower. They do not rule out unrelated deformations, evaluate a source, or imply vanishing or nonvanishing of `Q_0`.

## Exact dependency verification

The following public files were read at the supplied immutable commits through the GitHub read connector:

- PR437, `50e82ed233cd7729c38608194f990376eb832418`, `research/hm/paired-collision-filtration/PROOF.md`, blob `9697423e880070cdf34cbc3548f5a2b32b2a40a0`: full character identity, arbitrary coefficient bundle, and preserved collision strata.
- PR439, `bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b`, `research/hm/paired-collision-endpoint/PROOF.md`, blob `8b420be9fd49374981a7dfc59058483a4ae4dbfa`: all three exact resolutions, transpose maps, and doubled field endpoint.
- PR443, `bc5a8ba31104bc66b180984a1fdfc7f17ceb1eef`, `research/hm/rank-one-algebraic-transport/PROOF.md`, blob `ca5d8fa0a5fba0f0e6034199504969ff941db210`: the algebraic family, localized length and exponent argument, original special geometry, and the prior relative-cohomology limitation.
- PR442, `2072baf63868a309366a7d3ae54dc1132e56adb7`, `research/hm/endpoint-pencil-torsion/PROOF.md`: length-two controller and local multiplicity bounds. The proof's use of these facts is consistent with PR443's moving-cubic refinement.
- PR167, `063da90fc4543304e87e701cdefcc08225412f17`, `research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md`: the exact positive-twist vanishings used in the resolution chase.

## Limitations

This is an independent mathematical review of the new argument against the pinned public inputs, not a formal verification or a new proof of every historical input. The public-thread timestamp and global novelty are not independently certified by this review. No selected HM/source instance, multiplication matrix, numerical rank, random sample, checker, or large computation was run. No external state was changed. Only this requested local review artifact was written.
