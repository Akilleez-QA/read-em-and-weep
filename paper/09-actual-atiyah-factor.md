# 9. The actual Atiyah input and its six exceptional directions

## 9.1 What has been resolved

The lower map feeding the open positive obstruction is now determined geometrically. This is a statement about the actual bundle, not merely a list of representation-theoretically allowed maps. It is still distinct from the higher secondary operation applied afterward.

Let C = H¹(B_Q₀(2))₊. The Serre involution φ gives

    C^{φ+} = P4 ⊕ D5,                dimension 9,
    C^{φ−} = V ⊕ 2P4 ⊕ 2D5,        dimension 21.

These φ-eigenspaces subdivide the physical-positive space; φ must not be confused with physical inversion. The nine-space is annihilated by multiplication by A. The [actual splitting proof][S] retains the determinant character in its equivariant Euler calculation.

The actual multiplication

    D5 ⊗ A → C^{φ+},     h ⊗ a ↦ h At_F(D_a)|_Q₀

is onto. The key point is the [Serre residue comparison][R]: it identifies this particular geometric map with the infinitesimal action on the relative complete-intersection residue pairing. The connection term is included, and a compact Casimir argument forces both irreducible target components. Nonzero permitted channels alone would not have established this conclusion.

## 9.2 Exactly six exceptional directions

For a fixed nonzero a in A, write K_a(h) = h At_F(D_a)|_Q₀. Then

    rank K_a = 5 outside six C5-axis directions,
    rank K_a = 4 on those six directions.

The exceptional scheme is six reduced points in P(A), all disjoint from the discriminant conic of squares. In particular K_(ℓ²) is injective for every nonzero square ℓ². The proof uses the universal projection V⊗A → P4, a low-degree equivariant-kernel exclusion, and a Hilbert–Burch length calculation. It does not evaluate a chosen actual matrix. [Six-axis theorem][D].

There is an independent explanation on the square conic P(W): the actual map factors as the complete-quintic evaluation syzygy sequence

    0 → D5 O(-2) → T6 O(-1) → O(4) → 0.

Its full cokernel in the trivial nine-space is equivariantly O(4) ⊕ V O(2). The factor morphism lies in a one-dimensional equivariant Hom space and is nonzero, so comparison with complete-quintic evaluation proves injectivity everywhere on that conic. [Square sequence][Q].

## 9.3 The entire parameter-plane cokernel

The family over P(A) contains more information than its individual ranks. Put

    E = coker[D5 O(-1) → C^{φ+} O],

and let D denote the six reduced exceptional points. There are exact sequences

    0 → I_D(2) → E → V O(1) → 0,
    0 → E → O(2) ⊕ V O(1) → O_D(2) → 0.

The first is the unique nonzero equivariant extension up to scalar automorphisms of its end terms. The actual class is nonzero because H⁰(E(-1)) vanishes, whereas a split extension would have a V-space of sections. The second describes a length-six modification of the split double-dual bundle. E has rank four, first Chern class 5, and second Chern class 15; at an exceptional point it is locally a maximal ideal plus three free summands. It is therefore not itself the split double-dual bundle. [Actual family cokernel][E].

## 9.4 What still has to be computed

The next multiplication by a annihilates the nine-space. A canonical quartic scalar adjustment realizes the corresponding corrected differential operator on the cone, but its extension through the actual first-normal bundle remains a separate question. [Cone correction][C].

The local tangent discrepancy modulo conjugation has an intrinsic global description: for the ordinary square thickening 2Z of the regular Serre zero scheme, it is ω_(2Z)(1); first-normal corrections shift it to ω_(2Z)(-1). This retains the determinant and normal-equation line factors. It does not assert that every local discrepancy is a commutator or that the correction glues. [Global defect][M].

Thus uniform injectivity of K_(ℓ²), surjectivity onto the nine-space, and the explicit family cokernel do **not** imply nonvanishing of the composite third Bockstein. The absolute secondary value, the generic four-versus-five alternative, and the original repair remain open.

## Evidence

Each linked proof has a companion verifier for the universal character, polynomial, or degree identities it uses. The geometric arguments are authored proofs with independent mathematical checks, not Lean certificates. No selected actual coefficients, matrix-rank evaluations, or parameter scans are used.

[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eea50ed4146ae071de5df5ae0ff2888b05d080c8/research/hm/order-four-quadratic-load/ACTUAL-LOWER-COHOMOLOGY-SERRE-INVOLUTION-SPLITTING.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b2500656b997a0a846477fdd527fc821fa681f7f/research/hm/order-four-quadratic-load/ACTUAL-POSITIVE-ATIYAH-MULTIPLICATION-SURJECTS-ONTO-NINE-SPACE.md
[D]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b30db22c6f4e5a972e43aca4262937753f3c4ba9/research/hm/order-four-quadratic-load/POSITIVE-ATIYAH-SIX-AXIS-LOCUS-AND-UNIFORM-SQUARE-INJECTIVITY.md
[Q]: https://github.com/Akilleez-QA/read-em-and-weep/blob/07aaf979da71c71847ee5e13c2a3b53c6030d8d6/research/hm/order-four-quadratic-load/ACTUAL-SQUARE-ATIYAH-SEQUENCE-IS-COMPLETE-QUINTIC-EVALUATION.md
[E]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2b54a6e599531232dbf4ca10faec277c8a0081cd/research/hm/order-four-quadratic-load/ACTUAL-ATIYAH-FAMILY-COKERNEL-IS-SIX-POINT-ELEMENTARY-TRANSFORM.md
[C]: https://github.com/Akilleez-QA/read-em-and-weep/blob/e4f799e1f48e08d61850d055b2d107b8eeddc2d6/research/hm/order-four-quadratic-load/POSITIVE-SERRE-RESIDUE-AND-CANONICAL-CONE-OPERATOR-CORRECTION.md
[M]: https://github.com/Akilleez-QA/read-em-and-weep/blob/6118f6711df979073aa55b2811b801cd69bd0c14/research/hm/order-four-quadratic-load/GLOBAL-NORMAL-ADJOINT-DEFECT-DUALIZING-TWIST.md
