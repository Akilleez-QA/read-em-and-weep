# Independent audit of the cusp normalization reduction

20 October 2026. Formal mathematical record; no obstruction coordinates were evaluated.

## Verdict

Accepted under the explicitly imported source premises. The normalization faithfully detects the actual invariant cusp obstruction, and the displayed scalar-arrow and derivation-chart gauges turn its full differential algebroid into the unchanged global commuting-vector-field Moyal algebra modulo h³. The induced first-order module boundary must be retained. This proves an equivalence of vanishing tests, not vanishing itself or automatic quantizability of the normalized bundle.

I directly reviewed [cusp-normalization-next.md](cusp-normalization-next.md) together with [branch-boundary-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-boundary-audit.md), [pure-ambient-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-ambient-audit.md), and [pure-square-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-square-next.md). Identification of the displayed b,T and complete residual with pinned PR16 remains an accepted source premise, not a newly fetched source verification.

## 1. Geometry, signs, and root degree

For Vx=y and Vy=3x²/2, the normalization x=t²,y=t³ intertwines V with V~=t²∂t/2. With u=1/t this is exactly −∂u/2. Thus the field is globally regular, with a double zero at the cusp preimage t=0, not a pole at infinity. Every iterated derivative in the stipulated product intertwines, as do multiplication and the displayed unary operators.

The infinity point is smooth on the projective cusp curve and normalization is an isomorphism near it. Consequently ν*O_C(P∞)=O_P¹(∞)=O(1). Its square is O(2), exactly the pullback of O_P¹_x(1) along x=t². There is no lost factor of two or reversal of root degree.

## 2. Nonflatness is accounted for

Normalization need not be flat. One must not infer exact pullback of arbitrary sheaves or extension sequences. The argument instead pulls back locally free transition matrices, their formal corrections, and the complete identities between them along an actual differential algebra map. Classical inverses remain inverses, and formal matrices with invertible reduction remain invertible. This suffices for functoriality of the obstruction cocycle and its coboundaries.

For locally free E, Ext²(E,E)=H²(End E), and pullback here is the natural map of the latter cohomology groups. No singular HKR statement and no unjustified flat-base-change assertion is needed.

## 3. Exact invariant cohomology map

Over the common base B=(P¹_x)^4, the cusp and normalized finite cover algebras have factors O⊕O(−2) and O⊕O(−1), respectively. The odd algebra summands are not identified, but the invariant summand maps by the identity O→O. Since End(E)=π*M and End(E~)=π~*M for M=ρ*End(H), the projection formula, exact finite pushforward, and exact finite-group invariants in characteristic zero identify both invariant H^k groups with H^k(B,M). The actual pullback map is the identity in these identifications.

This proves the claimed degree-two isomorphism, with no unspecified scalar. Cancellation of the root line is valid for this target calculation, although it would not by itself identify module quantization problems. The transition-level differential map supplies that latter identification. Nothing here identifies noninvariant Ext¹ or licenses replacing the transported first lift.

## 4. Explicit noncentral gauge calculation

Take δf=f∞−f0, f=(−t,0), q=δf=t, and a=V~f=(−t²/2,0). For the exact supplied coefficients β_rs, including λ=15/4, put

c=Σ β_rs f_r∪q_s,
D=−Σ β_rs π^{sl} f_r a_s V~_l.

Then δc=b. The Čech product rule gives

s_k−V~_k c=−δ(Σ β_rs δ_ks f_r a_s),

so T−{c,−}=δD. There is no division by λ or additional factor of one-half. The bracket here must be the actual commutator bracket μ₁(a,b)−μ₁(b,a), consistently with the source identity δT={b,−}.

Here are precise conventions that remove the draft's harmless ± chart notation. For the row equation

F_ij(G_jk)⋆G_ij=A_ijk⋆G_ik,

let B_ij=exp⋆(−h c_ij). The compatible arrow transformation is

F′_ij=Ad⋆(B_ij)∘F_ij,
G′_ij=B_ij⋆G_ij,
A′_ijk=B_ij⋆F_ij(B_jk)⋆A_ijk⋆B_ik^(−1).

It gives F′=id+h²(T−{c,−}). Because the exponents are h-linear, their mutual star corrections start at h³, not h². Also F_ij(B_jk)−B_jk starts at h³. Therefore A′=exp(h(b−δc))=1 modulo h³, including its quadratic scalar coefficient. This argument treats B as noncentral: its conjugation effect on ordinary functions occurs at h² and is precisely the retained Hamiltonian correction.

Set φ_i=id+h²D_i. With F″_ij=φ_i∘F′_ij∘φ_j^(−1), the correction becomes δD+D_i−D_j=0. Since D_i is an ordinary derivation, φ_i is an automorphism of the unchanged star product modulo h³: its Hochschild differential on ordinary multiplication vanishes, and its interaction with hμ₁ starts at h³. The triple unit remains one. Thus no residual scalar correction is needed for this explicit primitive; the abstract H²(O)=0 fallback is unnecessary.

## 5. Transport of the actual boundary and second coefficient

Write G=g+h u+h² w. The preceding arrow transformation gives exactly

u′=u−cg,
w′=w−cu+(c²/2)g−μ₁(c,g).

The chart change G″_ij=φ_i(G′_ij) adds D_i(g_ij) to w′ and does not change u′. These are the induced terms that would be lost by treating c as central or discarding the second-order transport. The original first boundary need not be a Čech cocycle; the transformed u′ solves the global-star first-order equation by the full transformed descent identity.

After transport, the second-order source is the ordinary global-star expression stated in the draft. Naturality and reduction-identity gauge equivalence identify its class with the pullback of the complete old source, including T(g)g, −μ₁(b,g), and b²g/2. The induced w terms above account for the change of representatives by the appropriate Čech boundary. This is not permission to substitute an unrelated first lift.

## 6. Equivariance and strongest conclusion

The normalization commutes with the deck involutions (t↦−t over x), so the invariant cohomology comparison is genuinely equivariant. The explicit f,q,a and gauges have the inherited source characters. More generally any chosen reduction-identity gauge acts trivially on the classical End target, so it cannot change the identified pure class. The argument does not require an unsupported equivalence of all noninvariant source cohomology.

Let u_hat denote the actual transported first boundary on E~=(ρ∘d⁴)*H⊗O(1,1,1,1). Then

v=0 if and only if the invariant global-Moyal obstruction for (E~,u_hat) is zero.

Under the prior accepted six-condition reduction this is exactly the same remaining test as before. Rationality gives H²(O_X~)=0, not H²(End E~)=0; global splitting of the ambient does not supply module descent. No coordinate has been evaluated, no second-order module primitive constructed, and no vanishing or automatic module-quantization claim follows.
