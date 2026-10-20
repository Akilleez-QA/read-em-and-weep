> Scope: the projective lift, the explicit weighted-root-gerbe comparison, and the actual mixed-class covariance are distinct claims. The last remains conditional on the stated source identities and pair-character vanishing premises. It is not equality of raw cochains or a preferred same-object action. This packet extends the central comparison to a relative P39 family, not a new claim of the earlier central covariance theorem.

# Inversion transport of the actual weighted root gerbe

## Result and boundary

Assume the actual-source identities imported in ../pair-character-vanishing/MIXED-GAUGE-DESCENT.md, including its identification [R]=tf([M]). For the actual product-root legal cover and weighted gerbe, the projective inversion symmetry from ../../cubic-loci/foundation-p02/INVERSION-LIFT.md extends, after t↦−t and u↦−u, to transport of the truncated star/gerbe deformation problem. The resulting action fixes the actual trace-free mixed obstruction class under the induced End-bundle identification. This is a cohomology-class constraint, not covariance of a selected raw representative, HPL selector, or scalar detector.

The essential additional ingredient is a regular explicit gerbe gauge; ordinary projective-bundle symmetry alone would not suffice.

## 1. Actual cover comparison and regular root correction

Use zero-based physical factor indices and r_d=y_d/x_d. The actual one-factor legal opens are U₀=C\{O} and U₁=C\{T,P₁,P₋₁}, with P_±₁=(±1,0). For each factor the involution on x exchanges O,T and fixes P₁,P₋₁. Hence

    a⁻¹U₀=C\{T},     a⁻¹U₁=C\{O,P₁,P₋₁}.

Refine the source legal cover and its inverse image to opens W_i contained in U_(m_i)∩a⁻¹U_(n_i), also refining the carrier covers as needed. Here m_i,n_i are four-bit masks. Define scalar zero-cochains

    h_d,i=(m_i,d+n_i,d−1)r_d.

These are regular on W_i. If the bits differ, the coefficient is zero. If both bits are zero, the intersection excludes O and T. If both are one, it also excludes O and T. The only poles of r_d are O and T. This proves regularity, including the formerly problematic infinity and T loci, without pointwise evaluation.

Write q_d,ij=(m_j,d−m_i,d)r_d for the actual scalar one-cocycle, and let q^(n) denote the same source formula on the cover with labels n. Since a*r_d=i r_d,

    a*q_d^(n)=i(δh_d−q_d).                       (1)

This is an exact identity of regular cochains on the common refinement. It is not the incorrect assertion that the original legal cover is preserved or that the root line N is fixed.

## 2. Semilinear star-algebra transport

Let V(x)=y, V(y)=(3x²−1)/2 be the invariant physical derivation. Since a*(dx/y)=i dx/y, the chain-rule identity is

    V_d a*=i a* V_d.

For the disjoint pair first bidifferentials this gives

    μ_p(a*F,a*G)=−a*μ_p(F,G),
    μ_q(a*F,a*G)=−a*μ_q(F,G),
    μ_pq(a*F,a*G)=a*μ_pq(F,G).

Thus pullback on functions combined with t↦−t,u↦−u is an exact isomorphism of the source truncated star algebras. This follows termwise from their commuting-field exponential definition, and includes the mixed coefficient.

The actual b_r is (15/4)q_a∪q_b for the ordered physical pair r=(a,b). Put C=15/4. The transformed gerbe coefficient is, by (1),

    b'_r=−a*b_r^(n)=C(q_a−δh_a)∪(q_b−δh_b).

Define the regular scalar one-cochain

    k_r=C(−h_a∪q_b+q_a∪h_b+h_a∪δh_b).

The ordinary Čech Leibniz identity and δq=0 give exactly

    b'_r−b_r=δk_r.                              (2)

Every cochain k_p depends only on its physical pair, and every k_q only on the complementary pair (the discrete masks are constant on each open). Complementary physical derivations therefore annihilate these cochains.

## 3. Full weighted gerbe equivalence

Let c=exp(t b_p+u b_q) and c'=exp(t b'_p+u b'_q) in k[t,u]/(t²,u²). Define the scalar edge cochain

    z_ij=exp(t k_p,ij+u k_q,ij).

The complementary derivative vanishings imply z⋆F=zF=F⋆z for every local matrix F, exactly as for c in the mixed-gauge proof. In particular star multiplication of these weighted scalar cochains agrees with ordinary multiplication. Equation (2) yields

    c'=c·δz,

with δz_ijk=z_jk z_ik⁻¹ z_ij. If T' has gerbe c', multiplication by z_ij⁻¹ gives transitions with gerbe c. This is an explicit regular equivalence of the full truncated weighted gerbes, including their tu terms. It is not just equality of abstract additive cohomology classes.

## 4. Remove the scalar-line twist without changing the star problem

The geometric isomorphism is a*E≅E⊗Q, not a*E≅E. The two-torsion line Q has a flat algebraic structure: choose Q²≅O and take the associated finite étale μ₂ torsor. On that torsor Q has horizontal frames with transition constants ±1. The commuting physical derivations extend uniquely through an étale morphism and kill those constants. Therefore tensoring by this local system, or its inverse, is an exact equivalence for the same star algebra and scalar gerbe. It preserves all scalar curvatures and induces the canonical identity End(E⊗Q)≅End(E).

This argument is legitimate algebraic étale descent, not a claim that Q admits Zariski horizontal frames or an ordinary global trivialization. Differential operators, connections, and the locally free transition data descend across the finite étale cover. The flat structure can equivalently be defined on Q by requiring the chosen isomorphism Q²≅O to be horizontal; characteristic zero makes it unique, and different constant rescalings of Q²≅O give the same connection.

Combining semilinear pullback, the regular gerbe correction z⁻¹, tensoring by Q⁻¹, and the ordinary isomorphism E⊗Q≅a*E transports the deformation problem back to E with its original weighted gerbe. Locally the ordinary isomorphism must be lifted by star-gauge transport, including the derivative correction terms; naive ordinary conjugation of first lifts is not asserted.

## 5. Match the actual chosen first lifts and conclude

The automorphism a commutes with all factorwise deck involutions. On P(E)=X×_(P⁴)P(H), its lift (a,r) commutes with the canonical deck lifts (d,id), so the induced End identification is deck equivariant. The correction h_d is odd in factor d; hence k_r and its first weighted correction have the same pair character χ_r as the actual branch. The flat Q tensor operation is compatible with the deck structure: its square trivialization changes at most by a constant under deck action, which preserves the flat connection. More explicitly, equip t and u with deck characters χ_p and χ_q. Then the star algebra, the weighted gerbe and z are equivariant, since their coefficients have the matching characters. The flat Q connection is deck invariant. The ordinary bundle identification implementing the projective lift is deck equivariant up to a global constant scalar: its projectivization is equivariant, so the discrepancy is an invertible scalar function on the proper connected X. Physical derivations kill that constant, and it cancels from normalized End-valued cochains. Consequently the star-gauge transport of first lifts preserves precisely their pair characters; projective equivariance alone is not being treated as a substitute for this argument.

After the preceding transport, both transformed and prescribed first lifts solve the same branch equations with the same b_r. Their normalized difference is consequently a χ_r-valued Čech one-cocycle in End(E). The structural vanishings

    H¹(End E)_χ12=H¹(End E)_χ34=0

from ../pair-character-vanishing/PROOF.md produce first-order gauges matching the two branches. Lift the simultaneous gauge to the mixed ring. The transformed transitions then differ from the prescribed ones only by a tu transition term; the actual mixed-curvature argument proves that their normalized mixed classes differ by a Čech boundary. Trace-free projection commutes with this transport. The source identity [R]=tf([M]) therefore identifies their actual trace-free residual classes.

Since the parameter transformation sends tu to tu, the conclusion is

    A_End([R])=[R],

where A_End is the pullback identification on H²(X,End₀E) induced by the unique projective lift. This action also preserves the full-sign component, because a commutes with deck involutions. On the full-sign sector A_End² is simultaneous deck inversion and hence acts by (−1)^4=+1. Thus A_End is an involution on that sector, and [R] belongs to its +1 eigenspace. No dimension of that eigenspace is computed here, and no nonvanishing or vanishing of [R] follows solely from this fixed-class constraint.

## Evidence boundary

Imported projective-lift proof: ../../cubic-loci/foundation-p02/INVERSION-LIFT.md; its audit: ../../cubic-loci/foundation-p02/historical-audits/inversion-projective-lift-AUDIT.md; ../relative-mixed-character-purity/dependencies/PRODUCT-ROOT.md; ../relative-mixed-character-purity/dependencies/FIRST-LIFT-STRUCTURAL.md; ../pair-character-vanishing/PROOF.md and MIXED-GAUGE-DESCENT.md. The source-bound identities used by the last note remain imported premises, not newly authenticated source executions. All new work is formal regular-cover, scalar-cocycle, étale-descent and obstruction-theory reasoning. No source/model/rank/polynomial-instance/point/jet/residual evaluation or execution occurred.
