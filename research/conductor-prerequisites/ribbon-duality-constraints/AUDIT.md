> Historical mathematical review retained with the source. This is not a new independent review or a formal verification certificate.

# Independent audit: double-conic orthogonal connecting-map bound

## Verdict

The proof passes independent review. The bound

    rank ε ≤ min(max(d−3,0),7)

holds under the stated assumptions. The intrinsic quotient of the reduction kernel and the determinant-correct zero-boundary countermodel are also valid. The argument accounts for the nonsplit base ribbon by comparing two bundles on that same ribbon, rather than replacing it by a split thickening. It does not evaluate the actual HM splitting or connecting rank.

Read directly: this directory's PROOF.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/21b252420c0011b2cbc119cab2983a6d4ad2e966/research/conductor-normalization/conductor-double-conic-intersection/PROOF.md and AUDIT.md; and https://github.com/Akilleez-QA/read-em-and-weep/blob/f3f85ffc04213778c8c4fbd60e1e7e04b56cfd65/research/conductor-normalization/conductor-cohomology-bounds/PROOF.md.

## 1. Geometry, twists, and the orthogonal reference

The imported intersection is E=2C inside the plane W, with C a smooth conic and square-zero ideal J=O_P¹(−4). A plane twist restricts to twice that degree on C. Therefore G=B⊗O_E(−2 plane) has the ribbon filtration with quotient B_C(−4) and kernel B_C(−8). This agrees with the earlier conductor proof.

For rank-two F in characteristic zero the trace pairing on End₀(F) is nondegenerate and symmetric. In a splitting of F_C, the two off-diagonal endomorphism lines pair perfectly, each is isotropic, and the diagonal tracefree line has nonzero self-pairing. Thus the plane-split reference B⁰, with weights 0 and ±d/2 in plane degrees, is genuinely isometric to B_C after restriction. The evenness of d is necessary for this particular plane reference and is supplied by the earlier splitting result.

## 2. Infinitesimal comparison on a nonsplit ribbon

The comparison of the actual orthogonal bundle and the reference is valid without a retraction E→C. On affine opens, a fixed isometry of their reductions lifts first to an underlying module isomorphism. If the resulting form discrepancy is the symmetric J-valued matrix Δ relative to the reference Gram matrix Q, composition with 1−(1/2)Q⁻¹Δ removes it: the quadratic error is zero because J²=0. The lifted map is invertible because its reduction is invertible.

The differences between these local isometries are 1+a_ij. Their reductions are the identity, and their infinitesimal parts are skew-adjoint elements of J⊗so(B_C,q). Composition is addition in this kernel; the reference transition functions supply exactly the usual gluing of that sheaf. Consequently the differences form an additive Čech cocycle.

With a fixed reduction identification, the isomorphism classes of orthogonal lifts form a torsor for H¹(J⊗so(B_C,q)), once a reference lift exists. Automorphisms of the reduction would have to be quotiented out for an unframed classification. The proof needs only the cocycle comparison and correctly avoids making a stronger unframed classification claim. There is no omitted base-ribbon deformation term: both bundles and all local comparisons live over the same fixed E.

## 3. Reference boundary and change of boundary

For d≤2 the section domain vanishes. For d≥4 its only contribution is H⁰(O_C(d−4)). The ordinary conic restriction sequence with plane twist n=d/2−2 has H¹(O_P²(n−2))=0, so every such section extends to P² and hence to E. This proves that the boundary for the reference bundle vanishes, despite the fact that E has no retraction onto C.

Transporting one global reference lift through the local isometries produces actual local lifts. Their differences are a_ij applied to the reduced section; nilpotence removes dependence on the chosen first-order part of the section. Thus the stated cup-product expression for ε is correct up to a harmless uniform Čech sign. The use of a reference with zero boundary is essential and has been justified.

## 4. Image constraint and rank bound

For d>0 the line P=O_C(d) is intrinsic: any map from O_C(d) to either lower-degree summand vanishes, so the maximal-degree line is unique. Every domain section belongs to P(−4).

For any local generator e of P, skew-adjointness and characteristic zero give q(a_ij e,e)=0. This excludes the component in the opposite root line. Equivalently, the cup-product cocycle lies in P-perpendicular⊗O_C(−8). In sl₂ language, a bracket with a positive root vector has only positive-root and Cartan components; it cannot have a negative-root component.

The splitting gives P-perpendicular(−8)=O_C(d−8)⊕O_C(−8). When d≥8 the first summand has no H¹, while the second has H¹ of dimension seven. Therefore rank ε≤7 in this range. For d=4 and 6 the domain has dimension one and three respectively; its small dimension suffices. The proof explicitly retains the possible positive-root contribution in these two cases. For d=0 and 2 the domain is zero. Combining these cases with the domain dimension gives precisely the claimed bound.

No vanishing of a Cartan-valued deformation is assumed. In particular, applying a Cartan infinitesimal automorphism to a positive-root section can indeed contribute to the positive-root target for d=4 or 6.

## 5. Canonical quotient and dimensions

The trace form identifies B_C/P-perpendicular with P∨. Its twisted H¹ quotient map is surjective because H² on C vanishes. The cup-product image is killed by this quotient. The ribbon long exact sequence canonically identifies the reduction kernel with coker ε, so it has the asserted natural surjection onto H¹(P∨(−8)), of dimension d+7. This is intrinsic even though a displayed Cartan complement is a choice.

The imported dimensions are h⁰(L)=A, h¹(L)=21+A, h⁰(M)=T, and h¹(M)=9+T. Exactness gives the stated h⁰, h¹, and reduction-kernel formulas. Substitution of the new rank bound gives the table

    21,21,20,18,17,17,19,21,23,25,27

for d=0,2,…,20. For d≥10, the simplified lower bounds 2d−17, 2d+13, and d+7 are correct. The unconditional minimum remains seventeen. These are bounds before the component-image quotient, and the proof correctly avoids transferring them to an actual ambient obstruction or source image.

## 6. Determinant-correct countermodel, including odd summands

The units sequence identifies 1+J with J additively. Global units on C are constants and lift to E, while H²(C,J)=0. Hence Pic(E)→Pic(C) is surjective and its kernel is H¹(C,J), with no extra quotient by nonlifting global units.

Multiplication by two is bijective on that complex vector group. Any line bundle on E whose restriction degree is even consequently has a square root: lift the half-degree line from C and correct the square by half the residual kernel element. This remains valid for the nonsplit ribbon. In particular it does not require the desired root to extend to the plane.

For L=O_E(d/2 plane) and D=O_E(−2 plane), the restriction degree of LD is d−4. Choosing A₀²=LD yields F⁰=A₀⊕DA₀⁻¹ with determinant D. Its off-diagonal line is A₀²D⁻¹=L, so End₀(F⁰) is exactly the reference orthogonal bundle. The restricted degrees are (d−4)/2 and (−d−4)/2. This includes odd restricted degrees, which could not be obtained merely by restricting plane line bundles. Its connecting map is zero by the reference lifting argument.

This countermodel proves only that the fixed ribbon, splitting, determinant, and tracefree rank-two endomorphism structure do not force positive boundary rank. No extension to W or Y, global HM Chern class realization, or compatibility with the HM monad is established or required for that limited conclusion.

## Scope

This audit uses exact sequences, local square-zero algebra, trace linear algebra, and line-bundle cohomology. It determines no selected HM matrix, actual rank, source value, or obstruction pairing.
