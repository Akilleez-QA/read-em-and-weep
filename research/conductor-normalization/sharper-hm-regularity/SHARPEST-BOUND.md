# Supporting regularity theorem

This existing result is included as a prerequisite for the selected pole, detector and socle manuscripts. The older intermediate bounds are preserved as history; SHARPEST-BOUND.md records the stronger proved bounds under its precise hypotheses. No source membership is inferred.

# Tensoring the primary section resolution: the strongest verified bounds

## Results

For the normalized Horrocks–Mumford bundle F on complex P⁴ and B₀=End₀(F),

    reg(F)=5,
    H¹(B₀(t))=0 for t≥7,
    H²(B₀(t))=0 for t≥2.

The last two thresholds improve the consequences of tensor regularity alone and of the short tensor-monad argument. They imply the following sufficient bounds under the imported geometry and transport hypotheses:

- Each of the two weighted coordinates has universal discriminant pole bound one.
- The first-weight ideal coefficient H² vanishes for collision order k≥8.
- The second-weight ideal coefficient H² vanishes for collision order k≥9.
- A common UNWEIGHTED regular source representative of ideal order seven suffices to annihilate both weighted coordinates.
- A common downstairs coordinate-detection thickening is N₆, of transverse length five and degree thirty.

These are sufficient bounds, not claims of optimality or actual source membership. Collision-ideal order is not deformation order.

## 1. Primary section-module resolution

Source: Wolfram Decker, *Monads and cohomology modules of rank 2 vector bundles*, Compositio Math. 76 (1990), 7–17:

https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf

The rendered printed pages 14–16 were checked directly. Page 14 defines a minimal resolution 0→F₃→F₂→F₁→F₀→H⁰F(*)→0. Page 15 identifies the successive terms of the H¹-module resolution as F₃, F₂, F₁⊕2S(−3), F₀⊕10S(−2), 15S(−1), 5S. Comparing with the explicit shifts on page 16 gives

    0→2S(−8)→20S(−6)→35S(−5)
      →15S(−4)⊕4S(−3)→H⁰F(*)→0.

Sheafification is exact and recovers F. Thus

    0→2O(−8)→20O(−6)→35O(−5)
      →15O(−4)⊕4O(−3)→F→0.                 (R)

The primary H¹-module calculation in PROOF.md gives H¹F(s)=0 for s<0 or s≥4, and H²F(s)=0 except s=−2. Also F∨=F(1), so H³F(s)=H¹F(−s−4)* and H⁴F(s)=H⁰F(−s−4)*. The section resolution itself gives H⁰F(s)=0 for s<3.

## 2. Tensor the resolution and use diagonal vanishings

Tensor (R) by F∨(t). This remains exact because F∨ is locally free. The resulting resolution of End(F)(t) has terms, indexed from the right by homological degree j,

    E₀(t)=15F(t−3)⊕4F(t−2),
    E₁(t)=35F(t−4),
    E₂(t)=20F(t−5),
    E₃(t)=2F(t−7).

For an exact length-three resolution E₃→E₂→E₁→E₀→G, the vanishings H^(i+j)(E_j)=0 for j=0,1,2,3 imply Hⁱ(G)=0. This follows by splitting into short exact kernel sequences; groups in degree greater than four vanish automatically. No claim of global-section surjectivity is involved.

For i=1 and t≥7:

    H¹E₀(t)=15H¹F(t−3)⊕4H¹F(t−2)=0;
    H²E₁(t)=35H²F(t−4)=0;
    H³E₂(t)=20H¹F(1−t)*=0;
    H⁴E₃(t)=2H⁰F(3−t)*=0.

Thus H¹End(F)(t)=0 for t≥7.

For i=2 and t≥2:

    H²E₀(t)=15H²F(t−3)⊕4H²F(t−2)=0;
    H³E₁(t)=35H¹F(−t)*=0;
    H⁴E₂(t)=20H⁰F(1−t)*=0;
    H⁵E₃(t)=0.

Thus H²End(F)(t)=0 for t≥2. The trace splitting End(F)=O⊕B₀ gives both conclusions for B₀. No differential, matrix rank, or source instance is evaluated.

## 3. Discriminant pole consequence

The discriminant has degree six. The first and second weighted target coefficients are B₀(−4) and B₀(−3). After one discriminant twist these become B₀(2) and B₀(3), whose H² groups vanish by Section 2. In the exact divisor-boundary/localization construction already established in the discriminant-pole work, every class in either weighted H² target therefore lies in the corresponding one-pole boundary image.

This is a universal existence bound for a pole presentation, not an assertion that any particular source has a chosen presentation or that the representing meromorphic cochain is unique. The divisor exact sequence and localization hypotheses are those of the imported discriminant-pole theorem.

## 4. Collision coefficient and common source orders

Retain the exact geometry and regular source-transport premises of prerequisite full-target-collision-criterion, document PROOF.md. (see the unit INPUTS.md) For r=0,1,2 and n=k−3,

    (q_*(I^k EA^r))_sign=B₀(r−5)K_n.

The adjacent-generator resolution has dᵢ≥n and eᵢ≥n+3. After tensoring, the outer groups controlling H² of the coefficient dualize to H²B₀(dᵢ−r) and H¹B₀(eᵢ−r). When n≥r+4,

    dᵢ−r≥4≥2,     eᵢ−r≥7,

so both vanish. Therefore

    H²(Y,(q_*(I^k EA^r))_sign)=0 for k≥r+7.

The respective sufficient coefficient orders for r=0,1,2 are 7,8,9. A common closed regular UNWEIGHTED R∈I⁷E gives e_sign(σR)∈I⁸EA and e_sign(τR)∈I⁹EA² because σ∈IA and τ∈I²A². Both weighted classes vanish. With the stipulated regular class comparison and injective constant inclusions, both retained traces vanish. The r=0 case also kills the constant coordinate if its corresponding transport is included.

The same sufficient premise may be imposed on the H-sign projection R_H of a raw source, rather than all of that raw source. Closure, global regularity, the correct coefficient identification, ideal membership, and [R_H]=j₀([C]) remain separate hypotheses. No such lift or membership is constructed here.

## 5. Common degree-thirty collision detector support

Individual downstairs neighborhoods N₄,N₅,N₆ suffice for r=0,1,2. A common choice for restrictions of the already-defined coordinate classes is T=N₆=V(K₆), with

    K₆=(u³,u²v,v²),    deg u=2, deg v=3.

The generator degrees are (6,7,6), and adjacent least-common-multiple degrees are (9,10). The exact resolution is

    0→O(−9)⊕O(−10)→O(−6)²⊕O(−7)→O→O_T→0.

The five surviving weighted monomials are 1,u,u²,v,uv. The imported flatness argument gives generic transverse length five, degree(T)=5 degree(N)=30, and a Cohen–Macaulay surface thickening. This is not a set of thirty sample points. Dualizing by O(−5) gives

    0→O(−5)→O(1)²⊕O(2)→O(4)⊕O(5)→ω_T→0.

The coordinate restrictions

    H²(Y,B₀(r−5))→H²(T,B₀(r−5)|T), r=0,1,2,

are injective. Their dual detector maps are surjective:

    H⁰(T,B₀(5−r)|T⊗ω_T)↠H²(Y,B₀(−r)).

These yield complete families of detector representatives, not canonical bases or evaluated detector values. The ambient coordinate dimensions 2,10,20 are imported unchanged.

The natural upstairs order-seven neighborhood gives chain quotient targets modulo K₄,K₅,K₆ respectively. It does not automatically give the stronger common K₆ quotient for the first two components. The common-N₆ theorem restricts already-defined global coordinate classes, compatibly with restriction from N₆ to N₄ and N₅.

## Scope and status

This proof supersedes the weaker numerical consequences in PROOF.md, DETECTOR-COROLLARY.md and MONAD-H2-IMPROVEMENT.md; their statements remain valid. It does not decide twists below the stated H¹/H² thresholds, a minimum sufficient collision order, actual source membership, or an actual physical obstruction. No publishing, external source-app writes, large computation or selected instance evaluation occurred.

## Bounded endpoint uncertainty

The same resolution chase gives useful bounds, without determining the endpoint groups. At t=1 the higher controlling diagonal groups H³E₁ and H⁴E₂ vanish, so H²End(F)(1) is a quotient of H²E₀(1)=15H²F(−2), of dimension thirty. At t=6 the groups H²E₁,H³E₂,H⁴E₃ vanish, so H¹End(F)(6) is a quotient of H¹E₀(6)=15H¹F(3), also of dimension thirty. Therefore

    h²B₀(1)≤30,    h¹B₀(6)≤30.

No equality or vanishing of these endpoint groups is asserted; their incoming maps are not evaluated.
