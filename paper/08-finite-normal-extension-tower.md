# 8. Exactly two marked formal extensions of the actual cone bundle

## 8.1 Fixed scope and theorem

Work over C with the binary icosahedral group G. Let Q = Q₀ be the actual invariant rank-three quadric, let Q_n = (q₀ⁿ = 0), and retain B = End₀(F). Fix the determinant inherited from F and a marked identification of the reduction on Q with the actual F|Q. All extensions in this section are G-equivariant, with these fixed data.

**Theorem.** There are exactly two marked G-equivariant fixed-determinant formal-extension isomorphism classes of the actual cone bundle. Both are restrictions of ambient bundles F_r and F_(−r), where r = a/b is the nonzero monad channel ratio. The first-normal torsor is an affine line; exactly two points extend to Q₃. Each has a unique formal continuation, and both scalar gates to Q₄ and Q₅ vanish on both points. All transitions from Q₅ onward are uniquely liftable and unobstructed. [Finite upper bound][T]; [exact-two theorem][N2].

This classifies the specified marked formal extensions, not all global bundles. No general algebraization theorem is invoked: the two formal objects are explicitly supplied by ambient bundles. The positive cubic Bockstein is a distinct problem, now resolved as zero in [Section 15](15-third-vanishing-and-fourth-frontier.md).

## 8.2 Why the first scalar has a nonzero derivative

Use the actual restriction F|Q₂ as origin on the first-normal extension torsor. Its tangent space is

    H¹(B_Q(−2))ᴳ = C.

The obstruction to extending to Q₃ lies in H²(B_Q(−4))ᴳ. Its derivative at the actual point is the composite

    H¹(B_Q(−2))ᴳ → H²(B(−4))ᴳ → H²(B_Q(−4))ᴳ.

This is a comparison of actual sheaf extensions. The normal sequence is

    0 → B_Q(−4) → B|Q₂(−2) → B_Q(−2) → 0.

Its connecting map is the derivative obtained by varying transition functions. Naturality compares it with the ambient restriction sequence, so the ambient connecting class is not identified with the normal derivative before applying restriction. The first arrow is the established invariant isomorphism; the second is injective because H²(B(−6)) = H²(B(1))* = 0. The independently calculated character H¹(B(1))ᴳ = 0 also makes the invariant target one-dimensional. Thus the derivative is nonzero. [Derivative theorem][D].

In an affine coordinate s with the actual point at zero, the exact obstruction is

    ob(s) = cs + ds²,   c ≠ 0.

The degree bound comes from determinant-one transition corrections modulo q₀³: products of three first-normal factors vanish, while the quadratic determinant correction and gauge terms are retained. The origin is reduced. If d = 0 it is the sole zero; if d ≠ 0 there are exactly two distinct first-normal zeros. The geometric argument in Section 8.8 now proves d ≠ 0 and shows both zeros extend through all orders.

## 8.3 Uniqueness after first normal order and eventual vanishing

The fixed-determinant obstruction, lift-class, and infinitesimal-automorphism groups for Q_n → Q_(n+1) are, respectively,

    H²(B_Q(−2n)), H¹(B_Q(−2n)), H⁰(B_Q(−2n)),

with G-invariants for the equivariant problem. The controlling ambient bounds are

    H³(B(t)) = 0 for t ≥ −1,
    H²(B(t)) = 0 for t ≥ 1,
    H¹(B(t)) = 0 for t ≥ 6.

The tower proof derives these from the actual section resolution and primary-image theorem, including the twist-one endpoint. Restriction and Serre duality then give H¹(B_Q(−2n)) = H⁰(B_Q(−2n)) = 0 for n ≥ 2. Thus every lift that exists is unique up to a unique determinant-preserving isomorphism inducing identity on the preceding thickening.

Although Q is singular, it is a Gorenstein hypersurface with dualizing sheaf O_Q(−3). Hence

    H²(B_Q(−2n)) = H¹(B_Q(2n−3))*.

For n ≥ 5, the right group lies between vanishing ambient H¹(B(2n−3)) and H²(B(2n−5)). Every obstruction group therefore vanishes from Q₅ onward, even before taking invariants. Finite-group averaging in characteristic zero introduces no further equivariant descent obstruction. [Tower proof, Sections 1–2][T].

## 8.4 The actual invariant multiplication is zero

Write M_t = H¹(B(t)) here, without a parity restriction. The invariant spaces M₃ᴳ and M₅ᴳ are each one-dimensional, but dimensions alone do not determine multiplication. The actual theorem is

    q₀:M₃ᴳ → M₅ᴳ is zero.

The primary-image injection is a graded module map

    H⁰(F(3)) ⊗ H¹(F(t−2)) → H¹(B(t)).

Here H⁰(F(3)) = P4, H¹(F(1)) = P4 ⊕ W ⊕ S4, and H¹(F(3)) = W. At twist three, the primary source contains exactly one invariant, from P4 ⊗ P4, and injects it onto the unique invariant line of M₃. At twist five, the primary source P4 ⊗ W has no invariant. Multiplication compatibility sends the first primary submodule into the second. Since q₀ is invariant, it must kill the invariant line. This proves zero for the actual map, not for a freely chosen representation channel. [Tower proof, Sections 3–4][T]; [primary-image theorem][P].

## 8.5 The three scalar obstruction targets

The character and restriction calculations yield

    H²(B_Q(−4))ᴳ = C,
    H²(B_Q(−6))ᴳ = C,
    H²(B_Q(−8))ᴳ = C.

The first uses the derivative comparison and H¹(B(1))ᴳ = 0. By quadric duality, the latter two are computed from H¹(B_Q(3))ᴳ and H¹(B_Q(5))ᴳ. The final dimension uses the actual zero map of Section 8.4; merely knowing its source and target have dimension one would not suffice.

Consequently the entire formal extension problem has three potentially nonzero scalar gates: to Q₃, Q₄ and Q₅. The first has at most two roots, every subsequent lift is unique when it exists, and no later obstruction remains. This is the finite determination result. Section 8.8 resolves these actual values: d ≠ 0, and the later gates vanish on both resulting branches. [Tower proof, Section 5][T].

## 8.6 Why this does not solve the positive cubic gate

The normal derivative has target H²(B_Q(−4))ᴳ. The positive cubic Bockstein instead has a quotient of H¹(B_Q(4))₊ as target. These differ in degree and twist. Ordinary multiplication by a³h has degree eight and sends the normal derivative to H²(B_Q(4))₊ = 0; it does not lower cohomological degree. Therefore the nonzero normal derivative cannot simply be substituted into the cubic gate. A genuine secondary comparison would require its own construction and choice-independence proof. [Derivative theorem, Section 4][D].

No algebraization, new positive Bockstein nonvanishing, generic four-section conclusion, source recovery, or Weil-class algebraicity follows from this chapter. The main result remains four or five sections.

## 8.7 The quadratic coefficient has one universal scalar

The family premise is now pinned to the standalone [three-channel theorem][M3], with its [independent review][M3R]. The historical coefficient and Serre-residue notes name UNIVERSAL-THREE-CHANNEL-MONAD-ISOTROPY.md, which is missing at their cited public source. PR643 supplies a verified replacement for that dependency. Its proof uses the actual monad and its end exactness at PR455, together with the pinned coefficient representations and contraction conventions; the coordination comment alone is not evidence for the theorem.

Write H = V ⊕ W for coordinate functions, N = A ⊕ W′, K = Ω²(2), and Δ = det(H). The actual self-dual monad is

    N O(−1) → W′K → N*Δ.

Since H⁰(K(1)) = Λ³H = 1 ⊕ T6 ⊕ V, the coefficient Hom space has exactly three channels: a and b on the W′ source, through Λ³V and V ⊗ Λ²W respectively, and c on the A source, through Λ²V ⊗ W. Every subbundle arrow has abc ≠ 0. Setting c = 0 kills the A source; setting b = 0 kills the W′ source along P(W*). If a = 0, contraction on P(V*) identifies the b-channel with the isomorphism V* → sl(W′). Its determinant conic contains singular operators, each killing a nonzero W′ source vector; the c-channel cannot repair this source kernel.

Source gauges act by (a,b,c) ↦ (sa,sb,rc), and block coordinate pullbacks act by

    (a,b,c) ↦ (λ³a, λμ²b, λ²μc).

These actions are transitive on (C*)³: set λ = 1, choose μ² = (b′/a′)/(b/a), then take s = a′/a and r = c′/(μc). The known actual monad supplies one subbundle point, so all nonzero triples are genuine subbundle monads. Isotropy then extends to every triple by polynomial density, but injectivity does not extend to the boundary. The determinant-valued pairing is retained throughout. Transitivity includes coordinate pullback; it does not identify the bundles over the identity of projective space. [Three-channel theorem, Sections 1–5][M3].

Let (a,b,c) now denote these universal monad parameters on abc ≠ 0. They are not the negative quadratic direction a of Section 4. Normalize β ∈ H²(B(−4))ᴳ by its leftmost symmetric-monad cohomology line, and normalize η by δ_q₀(η) = β. After fixing channel identifications and generators, the normal quadratic cup coefficient satisfies

    [η,η]/2 = d(a,b,c) β|Q,
    d(a,b,c) = κb²

for one universal constant κ. The weight theorem alone does not determine its vanishing. The separate geometric theorem in Section 8.8 now proves **κ ≠ 0**, without assigning it a numerical value. [Universal coefficient theorem][U]; [geometric nonvanishing][N2].

The determinant character is essential to the proof. The natural symplectic pairing takes values in ΔO(−1), so the adjoint complex retains its Δ⁻¹ factor. Its canonical invariant β line has determinant weight Δ⁻²; the η line also retains the equation line generated by q₀. Source gauges and block coordinate changes therefore give

    d(sa,sb,rc) = s²d(a,b,c),
    d(λ³a, λμ²b, λ²μc) = λ²μ⁴d(a,b,c).

The function b² has exactly these weights. Since the established source-gauge and coordinate transformations act transitively on abc ≠ 0, their invariant ratio d/b² is constant. Dropping the determinant character would fail even the consistency check for scalar coordinate changes. This is a naturality and weight argument, not a selected coefficient evaluation.

Consequently the quadratic coefficient vanishes throughout this subbundle family or nowhere on it. There is no parameter-specific cancellation locus involving a or c inside abc ≠ 0. The geometric theorem rules out universal cancellation and constructs ambient representatives for both roots. Thus both later gates vanish as well. This additional conclusion uses the actual scheme and Serre-residue geometry, not the weight calculation alone. The positive cubic obstruction vanishes by the separate proof in [Section 15](15-third-vanishing-and-fourth-frontier.md), not by this formal-extension classification.

The [companion verifier][UV] checks the integral weight system and that b² is its unique monomial solution. It does not determine κ or establish the geometric inputs by computation.

## 8.8 A Serre-residue double cover realizes both branches

The weighted-stack zero scheme Z of the actual regular spinor section consists of a reduced conic and a nonreduced vertex component. The proof first establishes homogeneity of the **actual ideal**, not merely its support or associated graded module. In the known three-layer vertex module, every equivariant generator-surjection is conjugate by a module automorphism to the homogeneous one. The coarse affine projection recovers its kernel; on stack charts, the regular odd generators recover the whole ideal from its odd part. The homogeneous vertex generators have degrees three and five. This does not split the global quintic-generator extension.

The Koszul and ambient spinor sequences give H⁰(O_Z) = 2·1 ⊕ V and H¹(O_Z) = 0. The V summand is nilpotent and has no invariants; consequently all invariant units are precisely one nonzero scalar on each of the two components. The intrinsic Serre residue line is det(N_(Z/X)) ⊗ O_Z(−2). Its nowhere-zero invariant residues classify locally free extensions, modulo a common scalar, by a ratio ρ ∈ C*. There are no additional ideal automorphisms or invariant nilpotent parameters.

Let φ_μ fix the positive coordinates and scale the negative coordinates by μ. It preserves Z as a scheme. Retaining both the normal determinant and physical line-bundle factors, its residue weights on the conic and vertex are μ⁻² and μ². Thus

    ρ ↦ μ⁴ρ.

When μ² = −1 both residues acquire the same scalar. The cone bundle is therefore unchanged up to a G-equivariant isomorphism, which can be rescaled to preserve its determinant framing. But the ambient monad ratio transforms as r = a/b ↦ −r.

These ambient bundles are genuinely nonisomorphic. The strong exceptional monad triple makes bundle isomorphisms lift to degreewise chain isomorphisms; equivariant source gauges preserve a/b. Hence r and −r distinguish them. Stability and the perfectness of G rule out an additional nonequivariant isomorphism.

Formal restriction also distinguishes them. If their restrictions were formally isomorphic, an isomorphism on a sufficiently high Q_n would lift to an ambient homomorphism by Serre duality and Serre vanishing for Hom(F_r,F_(−r))(−2n). Its determinant is a nonzero global constant, forcing a global isomorphism, a contradiction. The uniqueness of every lift after first normal order then places these two ambient bundles at distinct first-normal points.

The exact obstruction cs + ds² with c ≠ 0 already allowed at most two such points. Since two distinct points now lift to every order, d ≠ 0; the roots are 0 and −c/d. Both later scalar gates vanish on both roots, and there are exactly two marked formal-extension isomorphism classes. With d = κb² and b ≠ 0 this also proves κ ≠ 0. [Full geometric proof][N2].

The [companion verifier][N2V] checks universal module automorphisms, representation invariants, residue weights, and the double-cover identity. It does not replace the scheme, Serre-extension, or formal-restriction arguments, and it evaluates no actual-instance coefficients or ranks. None of these conclusions computes the positive cubic Bockstein.

## 8.9 The midpoint has a square-zero adjoint, but cannot extend to Q₃

The involution exchanges the two roots 0 and s_* = −c/d and fixes their midpoint m = −c/(2d). At this midpoint, the invariant nilpotent N ∈ H⁰(B_Q(2))ᴳ has a unique invariant trace-free lift Ñ to the adjoint of the bundle on Q₂, and Ñ² = 0. The actual bracket [η,N] from the first-normal tangent line to H¹(B_Q)ᴳ is nonzero. [Midpoint theorem][MP].

The boundary δ_e(N) depends affinely on the extension e. The Serre comparison gives N character −1, while the invariant orbit-tangent Atiyah line H¹(B_Q)ᴳ has character +1. Naturality makes the boundary odd under reflection about m, so it vanishes at m. The vanishing H⁰(B_Q)ᴳ = 0 gives uniqueness. Its two nonzero, opposite endpoint values force its derivative [η,N] to be nonzero.

The determinant of the lifted adjoint restricts to zero on Q and lies in q₀H⁰(O_Q(2))ᴳ. This group is zero: the only ambient invariant quadratic is q₀ itself, which vanishes in the coordinate ring of Q. Trace zero and Cayley–Hamilton therefore prove Ñ² = 0 even on the nonreduced Q₂.

Nevertheless the midpoint obstruction is

    ob(m) = −c²/(4d) ≠ 0.

It does not extend to Q₃. In particular no flatness of ker Ñ or im Ñ, no spinor-line lift, and no ambient realization of the midpoint is inferred. The [companion check][MPV] concerns the displayed affine and determinant-character arithmetic. This supplies a useful reference point, not an evaluation of the constant cubic in Section 4.11.

## Pinned sources

[T]: https://github.com/Akilleez-QA/read-em-and-weep/blob/4a08fceeba54e81f909f53ae7579732067a7607e/research/hm/order-four-quadratic-load/FINITE-NORMAL-TOWER-AND-THREE-SCALAR-GATES.md
[D]: https://github.com/Akilleez-QA/read-em-and-weep/blob/768092ad96bb1eb355e19c151da22fdcb43cc62c/research/hm/order-four-quadratic-load/ACTUAL-SECOND-NORMAL-OBSTRUCTION-DERIVATIVE-IS-INJECTIVE.md
[P]: https://github.com/Akilleez-QA/read-em-and-weep/blob/d5d9bd997145b0ecf7d7bd659a19fb7845afb75f/research/hm/actual-primary-image-extension/PROOF.md

The twist-one endpoints are pinned in [PR455](https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md), and the higher-twist section resolution in [PR167](https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md). The source proofs record their further dependencies. Their mathematical arguments and universal checks are not proof-assistant certificates.

[U]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b15a545e5630f3ae886968e673bdf511f73f1454/research/hm/order-four-quadratic-load/NORMAL-QUADRATIC-COEFFICIENT-UNIVERSAL-B-SQUARE.md
[UV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9cfa648e923711d7d95ea5aa15b1447bdee901eb/research/hm/order-four-quadratic-load/verify_normal_quadratic_b_square.py

[N2]: https://github.com/Akilleez-QA/read-em-and-weep/blob/a0ccfe44a4d2b528622d591888b8cc1cddb47792/research/hm/order-four-quadratic-load/NORMAL-QUADRATIC-NONZERO-BY-SERRE-RESIDUE-DOUBLE-COVER.md
[N2V]: https://github.com/Akilleez-QA/read-em-and-weep/blob/0a93b2a6413ec612b935c299086a07a37de00dcb/research/hm/order-four-quadratic-load/verify_normal_serre_residue_double_cover.py

[MP]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b7010f3a25097aa6c9489ff802b44f5b149f9a66/research/hm/order-four-quadratic-load/MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md
[MPV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/0fdb493ec11b0f51e0a2d61841c24c067cec9ef5/research/hm/order-four-quadratic-load/verify_midpoint_nilpotent_lift.py

[M3]: https://github.com/Akilleez-QA/read-em-and-weep/blob/356a3b8d2da36f5b3e2034cc5c6adf82757a33cc/research/hm/three-channel-monad-family/PROOF.md
[M3R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/356a3b8d2da36f5b3e2034cc5c6adf82757a33cc/research/hm/three-channel-monad-family/REVIEW.md
