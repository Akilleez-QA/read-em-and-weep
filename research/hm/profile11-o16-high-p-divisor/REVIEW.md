# Independent exact-version review: the divisor-twelve high-P branch

## Verdict and version boundary

**PASS for the stated partial exclusion. No mathematical defect was found.**

This review applies exactly to:

- `PROOF.md`, SHA256 `0477e228a7253400fc80c58e484157a23cbadce559dcf252758155191f490f5f`;
- `verify.py`, SHA256 `65a72b3756889575649bf922a86709ae5e5e0fc4ee6d1fd235133bd0e818cca2`.

The conclusion is only that the high-only map `P O(-2) -> O(16)` has no common divisor in the four displayed source127 tuples. In particular, the degree-twelve common-divisor branch is impossible. **The basepoint-free branch remains open in all four edges.** This review licenses no whole-source exclusion, whole-label exclusion, compatible-pair decrement, current frontier count, or global theorem completion.

The written proof was checked independently before inspecting the supplied verifier. The verifier was then inspected and run against the seven exact local input files; it passed. A separate bounded McKay recurrence, not importing the verifier, checked the small symmetric-power identities. These calculations used only fixed abstract characters and original catalog data. No selected actual HM/source coefficients, parameters, points, derivatives, matrices, ranks, models, or large computation were used. This is not proof-assistant certification.

## 1. Source identity and assumptions

The original catalog's zero-based entry127 is exactly

    A = O(-8) + O(2) + O(16),
    B = O(-18) + O(-4) + O(6),
    defect = 0.

The stable-label record for `G3.11.cce6e3ba4eeb` has `source_index=127`, this same A, and `original_defect=0`. All four asserted tuples occur in that entry's necessary compatible-source list. Decoding them by the pinned actual-bundle formulas gives exactly the four splittings in the proof, each of rank17 and degree-54. The catalog is a necessary overlist, not a realization theorem; the new proof uses it in that limited sense.

The proof's geometric assumptions are the actual saturated inclusion `E -> H O`, the standard constant connection, the original zero-defect identification of the Gauss quotient with a saturated subbundle of `(H O/E)(-2)`, and `H0(E^-(2))=0`. These are precisely the relevant pinned inputs. It does not import the profile-(1,2) interior equality or an assertion that `H0(E^+)=0`.

For every one of these four source types, the canonical top block is `(P+D) O(-2)`. Its P-isotypic summand F is saturated in E and hence in the ambient constant bundle. Its component to `O(-8)` vanishes by degree; its component to `O(2)` vanishes because `Hom_G(P,Sym4 W)=Hom_G(P,D)=0`. Thus the actual external derivative of F is genuinely high-only. Strict-top gives injectivity on its four global sections after twist2, not fiberwise injectivity of a rank-four bundle into a line.

## 2. Common divisor and exact residual kernel

A common divisor of degree d leaves four independent sections of `O(18-d)`, so `d<=15`. It is invariant. The projective A5 orbit lower bound gives `d>=12` if nonempty. Perfectness of G removes any semi-invariant character ambiguity in its defining section. Odd degrees13 and15 have no invariant because of the center, while

    Sym14 W = A + V + P + D

has no trivial constituent. Hence only d=12 remains. The independent McKay calculation also gave

    Sym6 W = V + P,
    Sym7 W = Wp + T,
    Sym18 W = A + V + 2P + D,
    V W = T,  Wp W = P.

Removing the full common divisor, rather than a proper part of it, gives an everywhere-surjective residual morphism

    p0: P O(-2) -> O(4).

Its kernel K0 has rank3, degree-12, no sections after twist2, and `H1(K0(2))=V`. The proof's short splitting argument is exhaustive: a block `R O(-j)`, j>=4, contributes `R Sym(j-4) W` to this sole three-dimensional H1 budget. At j4 only R=V works; at j5 the smallest allowed odd coefficient already contributes dimension4; at j6 only the scalar can fit, and it contributes A rather than V; j>=7 exceeds the dimension budget. Thus `V O(-4)` is forced, and its full rank3 leaves no room for degree-minus-three blocks. There is no hidden alternative splitting or extra equivariant line character.

## 3. The raw sheaf argument, before saturation

This is the main point audited. Put

    B_F = (H O/F)(-2),
    N = (E/F)(-2).

The actual second fundamental form is an O-linear morphism `beta_F:F -> B_F`, and its composition with `B_F -> (H O/E)(-2)` is the external derivative p. The kernel of p is exactly K0, unchanged by factoring off the common divisor. On K0 the derivative lies in N.

In the four cases, N has the displayed `D O(-4)` summand and only strictly lower-degree summands otherwise. Every morphism `V O(-4) -> N` is zero: the sole equal-degree channel has inequivalent coefficients V and D. Therefore `beta_F(K0)=0`, as a sheaf morphism, not merely at generic points.

It follows that beta_F factors through the actual quotient `F/K0=O(4)`. The induced map from this quotient to the external `O(16)` is multiplication by the nonzero degree-twelve divisor section and is injective as a sheaf morphism. Hence the induced map `O(4) -> B_F` is also injective, and its image I is **isomorphic to O(4)**. This proves the assertion about the raw image; it neither asserts nor needs that the external `O(4)` image is saturated in `O(16)`.

Taking the inverse image of `I(2)` under `H O -> H O/F` now gives an exact sequence of the actual raw first-osculation sheaf:

    0 -> P O(-2) -> Mraw -> O(6) -> 0.

This is exact before any saturation. The inverse-image construction is the sheaf generated locally by F and its first derivatives. Its quotient by F is the raw image I(2), so no torsion was silently discarded. It is locally free on the smooth curve, has rank5, and has degree-2. Applying an already-saturated image lemma at this point would be unjustified, but the reviewed proof explicitly avoids that mistake.

## 4. Saturation defect and the profile-free contradiction

Let M be the saturation of Mraw in `H O`. The quotient `M/Mraw` is torsion, of nonnegative length delta, and

    deg M = -2 + delta.

Since M is a subbundle of a constant bundle, all its splitting degrees are nonpositive, so `delta<=2`. Both the raw sheaf and its saturation are G-invariant. Consequently the torsion lengths at points are constant on projective G-orbits, and their effective determinant divisor is invariant. If nonempty, it has degree at least12. Thus delta=0. This argument does not confuse the external common divisor with the possible osculation saturation defect; they are different quotients.

The exact saturated quotient is therefore `F^+/F=O(6)`, with generic Gauss rank one. The quadratic gap applies with r=4 and b=6, which violates both alternatives `b=2r` and `b<=r-1`.

I also checked the underlying gap directly. Quadratic values and their first two derivatives span the full constant coefficient space C, so `F^{++}=C O`. The derivative of F^+ kills F and factors through its line quotient. Hence `dim C` is 5 or6. Dimension5 would make F^+ constant, contradicting its degree-2. Dimension6 makes `C O/F^+=O(2)`, so the nonzero next derivative would induce a nonzero map

    O(6) -> O(2)(-2) = O,

which is impossible. This uses the original constant connection and no maximal-plateau hypothesis.

## 5. Independent polar/constant-projection check

First-polar generation gives the actual epimorphism `P W O(-1) -> M`. Together with saturation in the constant ambient bundle, it restricts the splitting degrees of M to 0 and-1. Rank5 and degree-2 give three constant dimensions and two linear dimensions. The exact equivariant Euler characters give

    chi_G(M) = -P + Sym6 W = V,
    chi_G(M(1)) = Sym7 W = Wp + T.

Using `V W=T`, this forces `M=V O+Wp O(-1)`. Here the constant V is the actual subspace `H0(M)` in H, not an abstract complement with an invented connection.

Projection by this constant subspace leaves the saturated subbundle `L=Wp O(-1)` of the projected constant ambient bundle. The projected F-to-L morphism cannot vanish, since a rank-four bundle cannot lie in a rank-three constant subspace. Its equivariant Hom space is one-dimensional because `Wp W=P`; hence it is a nonzero multiple of the tensor-Wp Euler map and is everywhere onto.

Derivatives of projected sections of F lie in L. Every local section of L has a local lift through the epimorphism from F, so L is preserved by the projected constant connection. Its Grassmannian map has zero differential and is constant in characteristic zero. That contradicts `deg L=-2`. This independently checks the final contradiction rather than relying only on the numerical gap.

## 6. Verifier and immutable public anchors

The supplied verifier passed. Its role is properly limited to exact character identities, the short rank/degree and Hom budgets, input integrity, and the four exact catalog decodings. The coherent-sheaf, saturation, and connection arguments are written mathematics checked above, not consequences of the script's arithmetic assertions alone.

For each of the following, I independently queried the immutable GitHub file and obtained its Git blob SHA, then checked the same hash directly from the local bytes using the Git blob header. All seven matched the manifest:

- [Actual splitting and Gauss persistence](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md): `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- [Strict-top theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md): `d7506dae49b4be43230450c4132bd5db91f137ef`.
- [Original necessary pairs](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json): `fe0afa410d89340d3082dc814277f89fbb582c19`.
- [Stable-label frontier](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json): `8b5971092f9ef762584912609fd5e9301c4e271d`.
- [PR802 polar principle and identities](https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md): `98a1bd6123e148476da0b997d879aecbf885ec97`.
- [PR796 quadratic Gauss-gap lemma, Section8](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md): `46a0de762000f21182f6d3168f3ecfd63adaf75f`.
- [Additional PR828 input](https://github.com/Akilleez-QA/read-em-and-weep/blob/ae077cbe42d65cde27d65ce88923dc35851b6952/research/hm/profile11-horizontal-quotient-exclusion/HORIZONTAL-CONSTANT-QUOTIENT-EXCLUSION.md): `6b43295c16eda2abd79e9d3c774d4d57139e1ff7`. This file is integrity-checked by the reproduction bundle but is not needed for the reviewed theorem.

I additionally read the pinned [endpoint-safe quotient and defect construction](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md), Git blob `dcacf0bcdef8377c1ed7654e5b82659ea409456e`. It supplies the original meaning of the quotient pairs and determinant defect, and records the projective orbit sizes12,20,30,60. No change in current frontier accounting was inferred from its historical counts.

No corrective change to the frozen proof is required. The precise contribution is a rigorously removed divisor branch and a reusable invariant-saturation-budget argument, not a removed source edge.
