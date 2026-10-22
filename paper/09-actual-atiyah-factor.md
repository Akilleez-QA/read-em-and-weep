# 9. The actual Atiyah input and its six exceptional directions

## 9.1 What has been resolved

The lower map feeding the positive third obstruction is now determined geometrically. This is a statement about the actual bundle, not merely a list of representation-theoretically allowed maps. It is still distinct from the higher secondary operation applied afterward.

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

The next multiplication by a annihilates the positive Serre nine-space. Its action on the remaining twenty-one-space is now also determined: C⁻ = ε H⁰(Q4(4)), with canonical 9 → 21 → 12 quotient. On the full C it has rank four for every nonzero negative quadratic and an eighteen-dimensional common kernel. This is distinct from the five-to-nine Atiyah map and its six exceptional directions above. See [Section 10.8](10-midpoint-operator-residue.md#108-the-whole-lower-multiplication-has-uniform-rank-four).

A canonical quartic scalar adjustment realizes the corresponding corrected differential operator on the cone. [Cone correction][C]. Its specified multiplied operator now has an exact first-normal obstruction description: Ψ = δ(r), with r in H⁰(ω_(2Z)(5))₊ and kernel equal to the image of global H⁰(G(4))₊. See [Section 10.1](10-midpoint-operator-residue.md#101-the-actual-third-value-has-a-global-boundary-description).

The local tangent discrepancy modulo conjugation is intrinsically M = ω_(2Z)(1), where 2Z is the ordinary square of the regular Serre ideal, not the ambient double quadric. [Global defect][M]. The first-normal twist M(-2) is invariantly acyclic. Together with complete determinant, coordinate, generator and stabilizer comparisons, this now matches the corrected Hessian symbol with the actual midpoint nilpotent. It does not license the bare formula without its unique generator primitive or transfer vanishing to M(4). [Actual-symbol matching](10-midpoint-operator-residue.md#103-the-corrected-hessian-symbol-matches-the-actual-midpoint).

The conic-supported operator boundary is zero. The degree-eight vertex part now has the exact 32 → 36 → P4 quotient and explicit split bundle M₈; its two square-boundary channels are nonzero. These quotient results alone do not evaluate the particular actual corrected residue or its second-symbol quotient. See [Section 10.6](10-midpoint-operator-residue.md#106-the-exact-degree-eight-quotient-and-double-cubic-bundle). The complementary global restriction route identifies the same remaining problem through a 35/31 quotient and its canonical deepest-quintic slice, without evaluating the actual remainder. See [Section 10.9](10-midpoint-operator-residue.md#109-a-complementary-global-restriction-and-canonical-last-jet-route). Thus uniform injectivity of K_(ℓ²), surjectivity onto the nine-space, the explicit family cokernel, and uniform rank four of the subsequent multiplication do **not** imply nonvanishing of the composite third Bockstein. The actual leading cochain is now explicit, and its upper connection and family coefficient reductions are described in [Section 12](12-harmonic-cochain-and-family-gate.md). The final third class is now zero by [Section 15](15-third-vanishing-and-fourth-frontier.md). This does not identify every lower or unquotiented class with zero. Fourth and later obstructions, the generic four-versus-five alternative, and the original repair remain open. [Remaining quotient](10-midpoint-operator-residue.md#105-the-conic-contributes-zero-to-the-boundary).

## Evidence

Each linked proof has a companion verifier for the universal character, polynomial, or degree identities it uses. The geometric arguments are authored proofs with independent mathematical checks, not Lean certificates. No selected actual coefficients, matrix-rank evaluations, or parameter scans are used.

[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eea50ed4146ae071de5df5ae0ff2888b05d080c8/research/hm/order-four-quadratic-load/ACTUAL-LOWER-COHOMOLOGY-SERRE-INVOLUTION-SPLITTING.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b2500656b997a0a846477fdd527fc821fa681f7f/research/hm/order-four-quadratic-load/ACTUAL-POSITIVE-ATIYAH-MULTIPLICATION-SURJECTS-ONTO-NINE-SPACE.md
[D]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b30db22c6f4e5a972e43aca4262937753f3c4ba9/research/hm/order-four-quadratic-load/POSITIVE-ATIYAH-SIX-AXIS-LOCUS-AND-UNIFORM-SQUARE-INJECTIVITY.md
[Q]: https://github.com/Akilleez-QA/read-em-and-weep/blob/07aaf979da71c71847ee5e13c2a3b53c6030d8d6/research/hm/order-four-quadratic-load/ACTUAL-SQUARE-ATIYAH-SEQUENCE-IS-COMPLETE-QUINTIC-EVALUATION.md
[E]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2b54a6e599531232dbf4ca10faec277c8a0081cd/research/hm/order-four-quadratic-load/ACTUAL-ATIYAH-FAMILY-COKERNEL-IS-SIX-POINT-ELEMENTARY-TRANSFORM.md
[C]: https://github.com/Akilleez-QA/read-em-and-weep/blob/e4f799e1f48e08d61850d055b2d107b8eeddc2d6/research/hm/order-four-quadratic-load/POSITIVE-SERRE-RESIDUE-AND-CANONICAL-CONE-OPERATOR-CORRECTION.md
[M]: https://github.com/Akilleez-QA/read-em-and-weep/blob/6118f6711df979073aa55b2811b801cd69bd0c14/research/hm/order-four-quadratic-load/GLOBAL-NORMAL-ADJOINT-DEFECT-DUALIZING-TWIST.md
