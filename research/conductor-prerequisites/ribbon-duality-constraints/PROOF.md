# A seven-dimensional bound for the double-conic connecting image

## Statement

Use the fixed ribbon E=2C in W=P², where C≅P¹ is a conic. Plane twists are explicitly marked; all degrees on C are P¹ degrees. Let F be the ambient normalized HM bundle restricted to E, B=End₀(F), and G=B⊗O_E(−2 plane). The established splitting is

    B_C≅O⊕O(d)⊕O(−d),  d∈{0,2,…,20}.

Write J=I_{C/E}=O_C(−4). In the canonical ribbon sequence

    0→B_C(−8)→G→B_C(−4)→0,

let ε denote the connecting map on H⁰ and let ρ=rank ε. Put A=max(d−7,0) and T=max(d−3,0). Then

    ρ≤min(T,7).                                             (1)

In particular the previous exact dimension formulas sharpen to

    A+max(T−7,0) ≤ h⁰(G)=A+T−ρ ≤ A+T,
    30+A+max(T−7,0) ≤ h¹(G) ≤ 30+A+T,
    dim ker[H¹(G)→H¹(B_C(−4))]
        ≥21+A−min(T,7).                                    (2)

The lower bound in the last line, for d=0,2,…,20, is respectively

    21, 21, 20, 18, 17, 17, 19, 21, 23, 25, 27.

Thus the universal minimum remains seventeen, but the large-splitting cases have strictly stronger bounds. For d≥10 the lower bounds are h⁰(G)≥2d−17, h¹(G)≥2d+13, and reduction-kernel dimension ≥d+7. These are conditional formulas, not a determination of the actual HM splitting.

For d>0 the positive-degree summand P⊂B_C is intrinsic. The reduction kernel admits a natural surjection

    ker[H¹(G)→H¹(B_C(−4))] → H¹(P∨(−8)),             (3)

whose target has dimension d+7. This assertion is before any component-image quotient.

The same nonsplit ribbon supports determinant-correct rank-two bundles with this splitting and ε=0. Consequently nonsplitness, trace self-duality, and the rank-two endomorphism structure alone cannot force ρ>0.

## 1. Compare orthogonal bundles on the same ribbon

The trace form q(x,y)=tr(xy) is a nondegenerate symmetric form on End₀(F) in characteristic zero. Under a splitting of F_C, the decomposition of B_C consists of a diagonal line and two root lines; q pairs the root lines perfectly, makes each root line isotropic, and is nondegenerate on the diagonal line.

Because d is even, the orthogonal reference bundle

    B⁰=O_E ⊕ O_E(d/2 plane) ⊕ O_E(−d/2 plane)

exists on E itself, with the same constant diagonal and hyperbolic trace form. Fix an isometry B⁰_C≅B_C. This construction does not use or provide a retraction E→C.

On a sufficiently fine affine cover, the isometry on C lifts to local isometries between B⁰ and B. To see this directly, first lift the underlying bundle isomorphism; its discrepancy in the Gram matrix has coefficients in J. Since J²=0 and 2 is invertible, a first-order change by minus one half of that discrepancy corrects the form. On overlaps the two lifted isometries differ by 1+a_ij, where

    a_ij∈J⊗so(B_C,q),
    q(a_ij x,y)+q(x,a_ij y)=0.

The a_ij form a Čech cocycle: products of two J-valued discrepancies vanish. Thus the first-order comparison is controlled by a class in H¹(J⊗so(B_C,q)). No splitting of O_E as O_C-algebras has been made.

## 2. The reference connecting map vanishes

Set G⁰=B⁰⊗O_E(−2 plane). For d≤2, H⁰(B_C(−4))=0. For d≥4, its only nonzero summand is H⁰(O_C(d−4)). Put n=d/2−2≥0. The ordinary conic sequence on P² is

    0→O_P²(n−2)→O_P²(n)→O_C(2n)→0.

Because H¹(P²,O(m))=0 for every integer m, every section of O_C(d−4) lifts to a plane section of O_P²(n), hence to a section of O_E(n) and of G⁰. Therefore the connecting map for G⁰ is zero for every allowed d.

Given a section s of B_C(−4), choose such a global reference lift. Transporting it through the local isometries above gives local lifts for G whose overlap differences are, up to the fixed Čech sign convention, a_ij s. Consequently ε(s) is represented by this cup-product cocycle. The sign has no bearing on the containment or dimension claims below.

## 3. Skew-adjointness excludes the negative root

Assume d>0 and let P=O_C(d) be the positive root line. It is the unique maximal-degree line subbundle of B_C, hence intrinsic. Every section in the domain of ε lies in P(−4). For a local generator e of P, skew-adjointness gives

    2q(a_ij e,e)=0.

Thus a_ij e lies in P-perpendicular. The component along the opposite root is zero. This proves

    im ε ⊂ im[H¹(P-perpendicular(−8))→H¹(B_C(−8))].   (4)

Using the displayed splitting,

    P-perpendicular(−8)≅O_C(d−8)⊕O_C(−8).

For d≥8 the first summand has H¹=0. Therefore the entire connecting image is contained in a seven-dimensional subspace, H¹(O_C(−8)). For d≤6, its domain dimension T is at most three, so ρ≤T≤7 directly. For d=0 the domain is zero. Together these statements prove (1).

It is important not to claim that the positive-root component always vanishes. For d=4 or 6, a Cartan-valued deformation can contribute to H¹(O_C(d−8)); these cases are handled by the small domain bound, not by the d≥8 vanishing argument.

The exact sequence of the orthogonal filtration identifies

    B_C/P-perpendicular≅P∨.

After twisting by −8 its H¹ quotient map is surjective, since H² of a coherent sheaf on C is zero. By (4) this quotient kills im ε. The ribbon long exact sequence identifies the reduction kernel with coker ε, so the quotient factors through it and proves (3). No choice of splitting is needed for this formulation.

## 4. Dimensions

The previously established line-bundle computation gives

    h⁰(B_C(−8))=A,     h¹(B_C(−8))=21+A,
    h⁰(B_C(−4))=T,     h¹(B_C(−4))=9+T.

The ribbon long exact sequence gives h⁰(G)=A+T−ρ, h¹(G)=30+A+T−ρ, and reduction-kernel dimension 21+A−ρ. Substituting (1) proves (2). For d≥10, A=d−7 and T=d−3≥7, giving the simplified formulas. Formula (3) also directly explains the d+7 reduction-kernel bound in that range.

These statements do not assert that the indicated quotient survives modulo the images of H¹ on N and W. Nor do they assert any nonzero image of an ambient obstruction or retained source.

## 5. A determinant-correct zero-boundary countermodel

Here is a bundle construction on this same nonsplit E showing why no positive lower bound on ρ follows from the ribbon-local package.

The square-zero units sequence is

    1→1+J→O_E*→O_C*→1,

with 1+J identified additively with J. Constants lift, and H²(C,J)=0. Hence

    0→H¹(C,J)→Pic(E)→Pic(C)→0.

The kernel is a complex vector group. In particular, any line bundle on E whose restriction has even degree has a square root: lift a line bundle of half the restriction degree and correct its square by a half of the residual kernel class.

Let L=O_E(d/2 plane), and let D=O_E(−2 plane), the required determinant of the normalized ambient rank-two bundle on E. The restriction degree of L⊗D is d−4, which is even. Choose A₀ with A₀²≅L⊗D, and set

    F⁰=A₀ ⊕ (D⊗A₀⁻¹).

Then det F⁰=D, and

    End₀(F⁰)≅O_E⊕L⊕L⁻¹=B⁰

with its trace form. Its restricted rank-two splitting degrees are (d−4)/2 and (−d−4)/2, exactly the required pair. Section 2 proves that its connecting map ε is zero.

This is a countermodel only to deductions from the fixed ribbon, the stated splitting, determinant, and trace/End₀ structure. It is not asserted to extend to a bundle on W or Y with the HM Chern classes or monad, and is not a proposed actual HM restriction. Any exclusion of this countermodel would need additional global or HM-specific input.

## Scope

This proof uses only the established conductor ribbon, parity and splitting bounds, trace algebra, infinitesimal isometries, exact sheaf sequences, and line-bundle cohomology. It computes no selected HM map, source, obstruction value, polynomial instance, or actual connecting rank.  The dimension table is substitution into the proved universal inequality.

Dependencies: https://github.com/Akilleez-QA/read-em-and-weep/blob/21b252420c0011b2cbc119cab2983a6d4ad2e966/research/conductor-normalization/conductor-double-conic-intersection/PROOF.md and AUDIT.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/f3f85ffc04213778c8c4fbd60e1e7e04b56cfd65/research/conductor-normalization/conductor-cohomology-bounds/PROOF.md.
