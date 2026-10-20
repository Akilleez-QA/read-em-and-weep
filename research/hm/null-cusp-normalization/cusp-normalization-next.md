# Exact normalization reduction of the actual cusp obstruction

20 October 2026. Formal mathematical record; no obstruction coordinates were evaluated.

## Result

The remaining vector v=Q(1,0,0) is detected faithfully after normalizing the cuspidal carrier. Moreover its full differential algebroid, including b and T, becomes explicitly equivalent modulo h³ to a globally split commuting-vector-field Moyal algebra on (P¹)^4. This is an exact reduction of the actual prescribed-boundary obstruction, not merely a comparison of coefficient dimensions or an affine trivialization argument.

Consequently the accepted six-condition problem is equivalent to the invariant obstruction of a specific transported first-order deformation of

    E~= (ρ∘d⁴)*H ⊗ O(1,1,1,1),   d:P¹_t→P¹_x, x=t²,

over that global Moyal algebra. The transport of the first boundary is essential. This deduction does not show the six coordinates vanish.

## 1. Normalization intertwines the actual differential operators

At the cusp C:y²=x³, let ν:P¹_t→C be x=t²,y=t³. On the infinity chart u=1/t the normalization is regular, and the infinity point is unchanged. The actual root N∞=O_C(P∞) pulls back to O_P¹(1), not to a formal half-line.

The actual derivation has the unique indicated extension

    V~= (t²/2)∂t = −(1/2)∂u.

Indeed V~(t²)=t³ and V~(t³)=3t⁴/2, agreeing with Vx=y and Vy=3x²/2. It is globally regular; in the t chart it vanishes twice at t=0. For every regular local cusp function a, V~ν*(a)=ν*(Va). The same is therefore true for every iterated derivative entering μ₁,μ₂ and every actual unary correction. Products and the explicitly specified b,T pull back as well. Thus ν gives an actual morphism of the truncated differential algebroid presentations, not only a Poisson map on a smooth open set.

Pulling back locally free module transitions and their first-order boundary is legitimate without flatness of ν: this uses the transition equations directly. Their complete obstruction numerator pulls back term by term, including T(g)g and −μ₁(b,g).

## 2. Faithful detection on invariant obstruction cohomology

Write B=(P¹_x)^4, M=ρ*End(H), X=C⁴, X~=(P¹_t)^4 and G=(Z/2)^4. Both maps X→B and X~→B are finite flat double-cover products. Their one-factor algebras are respectively

    O ⊕ O(−2),       O ⊕ O(−1).

The normalization inclusion is the identity on the invariant O summand. The root line cancels canonically in End, so finite pushforward and exact G-invariants give, for every k,

    H^k(X,End E)^G = H^k(B,M)
                      = H^k(X~,End E~)^G,

and the actual pullback map is the identity under these identifications. In particular it is an isomorphism, not just injective, in degree two. This is compatible with permutations of factors and hence with the accepted compact target and its coefficient projections.

The map need not be an isomorphism on the other deck characters: the twists −2 have become −1. No uniqueness theorem for arbitrary first-order lifts on X~ is inferred from the cusp pair-character Ext¹ vanishing.

For the prescribed first-order cusp lift, functoriality of the complete residual identifies ν*v with its normalized obstruction. Therefore v=0 if and only if that normalized invariant obstruction vanishes. Combined with the accepted injectivity v↦v+Rv, this detects exactly the original six remaining diagonal conditions.

## 3. Explicit global removal of the full b,T descent

Use the pulled-back standard two-chart cover on each P¹_t. With Čech convention δf=f∞−f0, set

    f=(−t,0),   q=δf=t,
    a=V~f=(−t²/2,0),   δa=V~q.

These are regular zero-cochains on their own charts. The fact that q is now a coboundary is explicit, not only a consequence of H¹(O_P¹)=0.

Retain exactly the coefficient convention of [branch-boundary-extension.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-boundary-extension.md) §2:

    b=Σ_rs β_rs q_r∪q_s,
    s_k=Σ_rs β_rs(δ_kr a_r∪q_s−δ_ks q_r∪a_s),
    T=Σ_kl π^{kl}s_k V~_l.

For the actual diagonal, β selects λ(q₁∪q₂+q₃∪q₄), λ=15/4. The same construction can be coefficientwise two-parameter. Define

    c=Σ_rs β_rs f_r∪q_s,
    D=−Σ_rsl β_rs π^{sl} f_r a_s V~_l.

The Čech product rule gives δc=b. Differentiating c, using a_k=V~_k f_k, gives the stronger identity

    s_k−V~_k c=−δ(Σ_rs β_rs δ_ks f_r a_s),

and consequently

    T−{c,−}=δD.

Here the Poisson bracket is the one in the source identity δT={b,−}. These formulas use all the supplied PR16 data rather than replacing T by zero by fiat.

Now change overlap equivalences by scalar star-units exp(−hc). Their inner conjugations change T by the corresponding Hamiltonian derivation, leaving T−{c,−}. The triple unit exp(hb) is killed modulo h³ because δc=b. Products of exp(hc) agree with the ordinary exponential multiplication through h²: the noncommutative correction from two h-linear terms first appears in order h³. The first overlap maps themselves differ from the identity only in order h², so their action on h c likewise contributes first in order h³.

The remaining unary overlap correction is δD and is removed by chart changes id±h²D, with the sign chosen according to transport direction. Each D is an ordinary derivation, so these are algebra automorphisms modulo h³ of the same Moyal product. They do not introduce a new second-order local multiplication. Triple units are already one and remain one. Thus the resulting global algebra is precisely

    O_X~[h]/(h³),   a⋆b=ab+hμ₁(a,b)+h²μ₂(a,b),

with μ₁,μ₂ the original commuting-derivation exponential operators using V~_i. No residual global bivector correction or scalar gerbe is being suppressed.

This explicit computation also explains the more abstract global check: H²(X~,O)=0 and H¹(X~,T_X~)=0. Those vanishings alone would require tracking the induced unary cocycle; the displayed c,D do that tracking explicitly.

## 4. The exact remaining global Moyal obstruction

Let g denote the pulled-back classical transitions and u the pulled-back stipulated first boundary. In the convention δ_g u=b g−μ₁(g,g), the scalar overlap change gives

    u_hat,ij = u_ij−c_ij g_ij.

More explicitly, write a possible second transition as G=g+h u+h²w. In the row convention F_ij(G_jk)⋆G_ij=A_ijk⋆G_ik, put B_ij=exp⋆(−h c_ij). Then the exact compatible transport is

    F′_ij=Ad⋆(B_ij)F_ij,
    G′_ij=B_ij⋆G_ij,
    A′_ijk=B_ij⋆F_ij(B_jk)⋆A_ijk⋆B_ik^(−1).

In particular the induced second transition is

    w′ = w−c u+(c²/2)g−μ₁(c,g).

The last term is essential: removing the scalar gerbe does not license omission of the noncentral differential correction. The order-h² chart correction D does not change u_hat but does contribute to the transported second-order transition. It cannot simply be omitted when comparing raw representatives. Since the full transport is an algebroid equivalence, these induced contributions change the obstruction representative only by the prescribed comparison boundary.

The remaining obstruction is thus represented on an acyclic trivializing refinement by the ordinary global-star numerator

    R_split,ijk = u_hat,jk u_hat,ij
      + μ₁(u_hat,jk,g_ij)+μ₁(g_jk,u_hat,ij)
      + μ₂(g_jk,g_ij),
    C_split,ijk = g_ik^(-1) R_split,ijk.

Its invariant cohomology class is exactly ν*v for the diagonal pure problem. In the two-parameter presentation the statement applies coefficientwise to the pure s² and t² coefficients, whose sum is v; mixed terms are transported too, not silently erased. The pre-existing accepted mixed vanishing is a separate premise.

The class can be computed using any refinement of the global product cover that trivializes E~. No assertion that the bundle itself is trivial on the entire product chart is required.

## 5. Limits and why normalization does not already force vanishing

1. The target survives unchanged. The invariant H² is H²(B,M), not H²(O_X~). Rationality of X~ therefore does not annihilate the End-valued obstruction.
2. A globally split star algebra need not admit a deformation of every given vector bundle with a prescribed first boundary. Affine charts individually having free lifts does not solve their global gluing equations.
3. The normalized bundle is not known to carry a lift of the additive actions generated by V~_i. Its defining map x=t² does not turn t-translation into a fixed PGL₂ action on x, and an HM equivariance statement cannot be invented from this normalization. Likewise a full exceptional collection on (P¹)^4 is not an equivariant quantization of this particular pulled-back HM bundle.
4. The normalized pair-character Ext¹ groups have not been computed here; their coefficient sheaves contain O_i(−1)O_j(−1), rather than the cusp O_i(−2)O_j(−2). Since noninvariant Ext¹ groups change under normalization, substituting a convenient different first lift would require an additional proof that it has the same invariant quadratic obstruction. The theorem above deliberately fixes the transported actual lift.
5. No coordinate of C_split was evaluated and no second-order primitive was constructed. The six-dimensional eigenspace restriction and its two-plus-four compact decomposition remain the accepted previously audited result, not a new dimension computation here.

The concrete next target is now a global-star transition problem for E~ with V~_i=−½∂u_i on the infinity affine chart, retaining the explicitly transported u_hat and algebraic gluing at u_i=∞. This is strictly smaller than a noncentral algebroid problem on the singular fourfold, while preserving every remaining obstruction coordinate.

## Sources and dependency pins

Direct inputs read: [branch-boundary-extension.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-boundary-extension.md), especially §§1–3,5,8–9; [branch-boundary-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-boundary-audit.md), especially §§2–6 and the cusp interpretation; [pure-target-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-target-next.md) §§1–4; [pure-square-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-square-next.md) §§1–4. Accepted premises: actual first-order cancellation and its family extension; pair-character uniqueness on the cusp; the complete PR16 two-jet and residual; target representations and Q(F0)=v+Rv. The normalization and explicit c,D construction above are new formal deductions from those inputs.

Pinned underlying source references, inherited from the cited audits (not independently fetched again for this record):

- PR16 full algebroid and residual, commit c8aec970fd65a105f39f4e8aeb8a17f0f0053f89, blob a58834ab61e18a5dedd8a7bf20bec7121bfa9165:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md
- Actual carrier/root, commit 3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f, blob fc0b0c7cf512d93c7a4ea976f986b7332b926f51:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md
- Target/HM stabilizer source used by the accepted audit:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/86251374e9c62528b9b9dbb35ef883bdfac30ad8/research/hm-smooth-family.md


