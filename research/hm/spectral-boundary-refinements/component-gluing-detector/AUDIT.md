# Independent audit: component and double-conic detector filtration

## Verdict

The proof passes independent review, including the added equations (2.7)–(2.8). No mathematical correction is required. The quotient of actual ambient detector images in (3.8), the dual ribbon identification, all four cochain tests and their signs, and the dimension formulas are correct. In particular the proof does not confuse the full ribbon detector spaces with the images of their maps on the ambient ten-dimensional space.

Read directly: this directory's PROOF.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/21b252420c0011b2cbc119cab2983a6d4ad2e966/research/conductor-normalization/conductor-double-conic-intersection/PROOF.md and AUDIT.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/21b252420c0011b2cbc119cab2983a6d4ad2e966/research/conductor-normalization/simple-pole-cofactor-comparison/PROOF.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/f3f85ffc04213778c8c4fbd60e1e7e04b56cfd65/research/conductor-normalization/normalization-gysin-factorization/PROOF.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/9a7637be2a384cfb784b7e97d6655f1c65a83ef9/research/conductor-normalization/nullcone-normalization/PROOF.md; and https://github.com/Akilleez-QA/read-em-and-weep/blob/f3f85ffc04213778c8c4fbd60e1e7e04b56cfd65/research/conductor-normalization/conductor-cohomology-bounds/PROOF.md. The numerical HM inputs are imported from the stated local dependencies rather than independently rederived here.

## 1. Ribbon quotient and component relations

The previously established geometry gives E=2C as a Cartier plane quartic in W=P², I_{C/E}=O_C(−4), and G|C=B_C(−4), with degrees on C measured on P¹. Consequently the exact sequence (1.1) has the correct end terms L=B_C(−8) and M=B_C(−4). No retraction of E onto C or O_C-module splitting of G_E is required.

Since H²(L)=0, the ribbon long exact sequence makes π_*:H¹(G_E)→H¹(M) surjective and identifies U with H¹(L)/im ε. For I=im v_1, the induced quotient map H¹(G_E)/I→H¹(M)/π_*(I) is surjective with kernel (U+I)/I. This proves (1.2)–(1.3), including

    D_nil=U/(U∩I)=H¹(L)/ι_*^{-1}(I).

The inverse image in the last denominator automatically contains ker ι_*=im ε. Further, a component class maps into U exactly when it belongs to P_1^0=ker(π_*v_1), so v_1(P_1^0)=I∩U. Equation (1.4) and the component relations retained in it are exact. Quotienting only by im ε would generally be insufficient.

## 2. Ambient and Hilbert–Burch filtrations

Mayer–Vietoris is exact for the scheme union and its scheme-theoretic intersection. Tensoring by G preserves it because G is locally free. H²(G_E)=0 gives exactly (2.1), including surjectivity onto the sum of component H² groups.

The inverse of the connecting injection on its image therefore defines β_E on A_1=ker r_comp without a choice. The quotient D_E→D_red defines β_red, and its kernel A_2 is precisely the domain on which β_E lands in D_nil. The resulting β_nil has kernel ker r. Thus A_3=ker r, and the imported surjective Hilbert–Burch invariant identifies A_3/J with V_Z. All inclusions and quotient identifications in (2.3)–(2.4) follow. No direct-sum decomposition is being assumed.

Counting these successive quotients proves both the ten-dimensional budget (0.2) and rank r=c+g+n. Since rank α*=rank α, one has

    dim V_Z=10−rank α−c−g−n.

Subtracting this from dim W_Z proves the exact equality in (2.6); the stated lower bound follows immediately from the imported lower bound on dim W_Z. All rank terms remain symbolic.

The new global-section layer is also correct. Mayer–Vietoris gives 0→D_0→H¹(G_Z)→K_1→0. Applying λ=h a to lifts of K_1 defines λbar modulo precisely R_0=λ(D_0). Hence im λbar=R/R_0 and V_Z=(W_Z/R_0)/im λbar, as in (2.7). The bound dim R_0≤h⁰(G_E)≤30, subtracted from (2.6), proves (2.8). Replacing 30 by dim R_0 gives the sharper estimate directly, and using its upper bound dim D_0 also gives a valid estimate. This retains both global-section and compatible-component lift ambiguity.

## 3. Dual ribbon and the two full detector spaces

Adjunction for the degree-four plane divisor gives ω_E=O_E(1) in plane twists. Because O_Y(1)|W=O_W(2), G_E=B_E⊗O_E(−2). Trace self-duality thus yields H_E=B_E⊗O_E(3). The Gorenstein curve Serre pairing identifies H¹(G_E)^∨ with H⁰(H_E), so the annihilator definition T_E=ker v_1^∨ is exactly D_E^∨.

The component duals in (3.3) have the correct twists: N is the (2,3) complete intersection with ω_N=O_N, while ω_W=O_W(−3). Surface duality applied to G_N=B_N(−1) and G_W=B_W⊗O_W(−2) gives the stated H¹ groups.

The canonical dual of (1.1) is (3.4), with end terms

    M^∨ω_C=B_C(2),    L^∨ω_C=B_C(6).

One can check this intrinsically by duality for the finite closed immersion C→E: Hom_E(i_*L,ω_E)=i_*(L^∨ω_C), and likewise for M. The end terms are maximal Cohen–Macaulay modules on the Gorenstein curve E, so the relevant positive sheaf Ext into ω_E vanishes. Equivalently, the ribbon ideal sequence for H_E has kernel I_{C/E}H_E=B_C(2) and quotient H_E|C=B_C(6). These two constructions agree; they do not identify H_E with a direct sum of its end terms.

Under the natural Serre pairings, q is the transpose of ι_* and the inclusion of H⁰(B_C(2)) is the transpose of π_*. Therefore T_red=T_E∩H⁰(B_C(2)) is D_red^∨. Restricting functionals annihilating I from H¹(G_E) to U gives all functionals on U annihilating I∩U: a functional on U/(I∩U) first extends to (U+I)/I and then to H¹(G_E)/I. Its ambiguity is the dual of D_red. This proves T_nil=q(T_E)=D_nil^∨ and (3.6).

In particular extension across the ribbon and annihilation of the component H¹ image are both necessary. Neither all sections of B_C(6) nor all sections extending to H_E can replace T_nil in general.

## 4. Actual ambient detector image quotient (3.8)

For a direct linear-algebra verification, put f=β_E:A_1→D_E and p:D_E→D_red. Then A_2=ker(pf). Restriction A_1^∨→A_2^∨ takes im f^∨ onto im β_nil^∨: a σ∈T_E restricts to the functional defined by qσ∈T_nil, and q:T_E→T_nil is surjective.

Its kernel on im f^∨ is exactly im β_red^∨. Indeed every β_red-functional vanishes on A_2. Conversely, if f^∨σ vanishes on A_2, then σ restricted to im f vanishes on

    f(A_2)=im f∩D_nil.

It therefore factors through p(im f)=im β_red. Extend that functional from im β_red to D_red; its pullback gives exactly f^∨σ on A_1. This proves both exactness in the middle and surjectivity on the right of (3.8). The argument concerns the actual images, even if T_E, T_red, or T_nil contain functionals annihilating every ambient class.

Finally Q^∨=ker α by the stated transpose identification. Taking annihilators of the filtration of Q gives the four dual successive pieces in the stated reverse order. There is no preferred extension of a functional on A_1 or A_2 to all of A.

## 5. Cochain signs, choices, and sufficiency

An affine cover of separated Y and its closed restrictions has affine intersections. Coherent sheaf exact sequences are sectionwise exact there, so all asserted cochain lifts exist.

- Step 1: d(p_N|E−p_W|E)=0. The lift of t_E through the difference map is (p_N,p_W), whose differential is the diagonal restriction of x. With the prescribed positive convention, ∂[t_E]=r(η), with no minus sign. Changing component primitives adds exactly a component H¹ relation.
- Step 2: subtracting vz and de_E makes the E cocycle lie in ker π=im ι. Its unique L preimage is closed. All choices change its cohomology class by ι_*^{-1}(I), including the ε ambiguity. Functorial Serre duality gives (4.4); the component correction pairs to zero with T_E, and extension ambiguity T_red pairs to zero on A_2.
- Step 3: after choosing [vz′]=[t_E], lifting the zero-cochain f_E through v and replacing p by p−z′−df kills the difference on E without changing the differentials. The adjusted component primitives therefore glue on Z. This proves the converse as well as necessity of the full two-stage gluing test.
- Step 4: θ=x−dp is closed and GI_Z-valued. If A^T w=du, injectivity gives dw=0. Changing p_Z by a closed z_Z changes [θ] by −a[z_Z] and [w] by −h a[z_Z], so the sign used to cancel [w] in R is correct. Once its class is zero, w=dv and u−A^T v is closed while still lifting θ. Thus x=j^T u+dp, proving membership in im α*. Conversely that expression supplies all four tests directly.

Adding an ambient coboundary dR to x and adding the restrictions of R to the primitives leaves the ribbon difference and final θ unchanged, as asserted. The algorithm is therefore necessary and sufficient and independent of the original cocycle and every intervening lift.

## 6. Dimensions and stopping criteria

For B_C=O⊕O(d)⊕O(−d), line-bundle cohomology gives

    h¹(L)=21+a_d,    h¹(M)=9+t_d.

Subtracting ρ=rank ε gives dim U=21+a_d−ρ and h¹(G_E)=30+a_d+t_d−ρ. Since ρ≤t_d and a_d−t_d≥−4, dim U≥17. The permitted d≤20 gives h¹(G_E)≤60. Rank-nullity for P_1^0→U and P_1→H¹(M) gives exactly (5.1).

These bounds do not force a nonzero D_nil or a nonzero actual ambient gluing map. The four ambient layers share the single ten-dimensional budget. Finally the claimed invertibility criterion is valid because t:A_3→V_Z is surjective: vanishing of the three successive restriction/gluing maps and of V_Z is equivalent to J=A. For one specified η only its successive obstruction values must vanish, not the entire space V_Z.

## Scope

This audit used local mathematical dependencies, exact sequences, duality, cochain algebra, and symbolic dimension checks only. It evaluated no source, HM or cofactor matrix, selected splitting type, actual rank, or obstruction pairing.

## Status of this record

This is a historical mathematical audit, not a new formal verification or a new execution of tests.
