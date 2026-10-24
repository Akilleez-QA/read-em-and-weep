# 149. A strict dual-cubic image bound inside the backward rank-four plateau

**Craig Ward · 24 October 2026 UTC · Partial reduction within (3,1), not a coarse exclusion**

## Exact new information

Under the retained actual-geometric and fixed physical-marking hypotheses, the [backward dual-cubic theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/64ff42030e91a3a8e8b713d0ef8cef952511dccc/research/hm/rankfour-backward-cubic-image/PROOF.md) treats generic SF rank four with ordered maximal plateau (k,l)=(3,1). For every chosen equivariant inclusion T₆→H⁰(Q*(3)), the actual composite

    ψ: T₆ O→Q*(3)→E*(1)

has nonzero image of rank one, two or three, never four. If the image has rank one, it is O(9), and the necessary source label is D. Neither existence of a rank-one image nor realization of source D is asserted.

A T₆ copy exists because χ_G(Q*(3))=T₆−2W−S₄ has positive T₆ coefficient. There need not be a unique copy, and its evaluation need not be injective or saturated. The theorem applies separately to every chosen copy. The actual derivative kernel D₀ has H⁰(D₀(3))=0, so the composite is injective on that T₆ space of global sections and is nonzero.

This does not close the (3,1) plateau. At this image-bound checkpoint, the [chapter148](148-rankfour-reverse-adjacent-exclusion.md) count remained **23 necessary bad coarse bins**, including five rank-four bins (1,1), (1,2), (2,1), (2,2), (3,1). The later [chapter150](150-rankfour-diagonal-torsion-exclusion.md) supplies a separate coarse exclusion; it is not a consequence of this image theorem. Generic SF≥4 and square rank≥28 remain the bounds. No SF≥5, positive-square surjectivity, full-adjoint invertibility or original repair follows.

## Positive ramification remains in the general ledger

The ordered actual chain has ranks 5,9,13,17,21, with E=F₃ and Q*=D₁ in the reversed annihilator chain. The bundles E and Q* have unequal ranks and different presentations. Forward length one does not force source Z; all four necessary source types D/P/V/Z are retained.

Persistence bounds the endpoint degrees a=deg F₀≤−20 and b=deg D₀=deg F₄≤−36. For four rank-four quotients L_i and their three regular derivative maps,

    c_(i+1)=c_i+8+δ_i,   δ_i∈⟨12,20,30⟩,
    a+3b=−168+δ₁+2δ₂+3δ₃.

Writing a=−20−2u and b=−36−2v gives

    2u+6v+δ₁+2δ₂+3δ₃=40,
    c₁=(−78−a−2δ₁−δ₂)/3∈2ℤ.

The complete necessary ledger has 31 rows: seven unramified and **24 with positive defects**. These are numerical necessities, not actual configurations. The theorem does not discard the ramified rows or claim a blanket zero-defect conclusion.

## Four full-rank images, then none

Let J=im ψ. It is a globally generated, center-odd image sheaf inside E*(1). The four actual source types bound its ordinary degrees by nine. Source-generation and target-Hom tests on irreducible blocks R O(e), with 0≤e≤9 and correct parity, give fourteen necessary blocks and twenty-four rank-four multisets.

Suppose J has rank four. Its saturation is J̄=(E/F₂)*(1). Set B=E/F₂ and d̄=deg J̄. The regular backward derivative maps and H⁰(F₀(3))=0 give

    deg J−6≤d̄−6≤h⁰(J*(2))+h⁰(J*).

Only four shapes survive:

| J | Degree | Upper bound for d̄ |
| --- | ---: | ---: |
| P O(1) | 4 | 14 |
| S₄ O(2) | 8 | 10 |
| V O(1)+O(9) | 12 | 12 |
| 2W′ O(2) | 8 | 10 |

Each possible saturation length is less than twelve. Invariance therefore forces J=J̄. This is a statement about the cubic image's saturation, not about all plateau defects. In each case H⁰(B(−1))=0, so H⁰(F₁(3))=0 and H⁰(F₂(3)) embeds in H⁰(B(1)).

Three shapes fail directly:

- For S₄ O(2), χ_G(F₂(3))=W′+T₆−W−S₄ forces W′ and T₆ into H⁰(F₂(3)), which cannot embed in S₄. Genuine H¹ cannot remove the positive Euler constituents.
- For 2W′ O(2), the relevant intertwiner space is one-dimensional. Every map from T₆ O factors through one diagonal W′ O(2), so cannot have rank four.
- For V O(1)+O(9), the section injection and χ_G(F₂(3))=T₆ force H¹(F₂(3))=0. All F₂ slopes are consequently at least −4. Its derivative to V O(−2)+O(−10) has zero scalar component by degree and hence rank at most three, contrary to the hypothetical full derivative rank four.

## The last image forces an endpoint contradiction

Only under the remaining hypothesis J=P O(1) does the proof force all plateau defects to vanish. Here B=P O and

    a=−30+δ₁+2δ₂≤−20,
    b=−46+δ₃≤−36.

Each available gap is ten, below the first positive invariant defect twelve. Thus a=−30, b=−46 and (L₁,L₂,L₃,L₄)=(P O(−4),P O(−2),P O,P O(2)). These are associated-graded isomorphisms induced by the derivative, not a horizontal splitting.

The rank-five endpoint F₀ has degree −30 and slopes in the proved window [−14,−4]. Its 46 abstract equivariant splittings are tested against the necessary identities

    χ_G(F₀(3))=−S₄−T₆,
    χ_G(F₀(4))=V−A−D.

Exactly two remain: V O(−4)+O(−8)+O(−10), and V O(−4)+W O(−9). In both cases every equivariant endpoint derivative F₀→P O(−6) is zero. The V component vanishes by degree; the other components vanish because [1:P Sym²W]=[1:P Sym⁴W]=[W:P Sym³W]=0.

A subbundle of a constant bundle with zero second fundamental form has constant Grassmannian classifying map in characteristic zero. It would have degree zero, contradicting deg F₀=−30. This excludes the last rank-four image, without excluding the remaining image ranks one through three.

## Evidence and scope

The frozen proof SHA256 is `0e291e31481530df3163ed6abc3d433a4e402c98e9258d3a329b05b51a2ea507`. The final independent review SHA256 is `7f4cc562718242c1808b69ce70a8180f8d5cf67bfb1a17ac4a5d76bf8bfbd173`. The author certificate has 12,643 checks; the independent calculation has 603 checks and thirteen executed mutation controls. Normal and optimized outputs match. Complete domains, not just their sizes, were compared. Five complete pinned original sources are authenticated, with their transitive actual-geometric prerequisites retained.

The exact-character calculations support the written proof; they are not proof-assistant certification of the original geometry. The rank-one conclusion is a necessary source-conditioned refinement, not a constructed example. The 31-row defect ledger is not the 23-bin coarse frontier and must not replace its denominator. No actual coefficients, parameters, jets, matrices, instance ranks or historical enumeration are evaluated. Earlier chapters and the delivered PDF remain frozen.
