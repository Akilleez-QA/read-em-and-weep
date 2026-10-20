# Normalized first-boundary ambiguity: exact Ext¹ and a symmetry-preserving replacement theorem

20 October 2026. Formal mathematical record; no obstruction coordinates were evaluated.

## Results

Let Y=(P¹_x)^4, X̃=(P¹_t)^4, d⁴:X̃→Y be x_i=t_i², ρ:Y→P⁴ the symmetric-product map, and

    Ẽ=(ρd⁴)*H ⊗ O(1,1,1,1).

Work over C. Let χ12 be the deck character odd in t₁,t₂ and even in t₃,t₄, and set a=(12), b=(34).

1. The normalized pair-character group is **not zero**:

       Ext¹(Ẽ,Ẽ)_χ12 ≅ H¹(P⁴,End H(-1)) ⊗ C⁴,
       dim Ext¹(Ẽ,Ẽ)_χ12 = 20.

   The same dimension holds for every two-element deck character. The displayed isomorphism is an ordinary vector-space decomposition; no unspecified canonical basis is claimed.

2. Its canonical internal-swap decomposition is

       (a,b) parity:    (+,+)   (+,-)   (-,+)   (-,-)
       dimension:        15      5       0       0.

   In particular every χ12 Ext¹ class is a-even. For χ34, every class is b-even; the dimensions in the same parity order are 15,0,5,0.

3. Consequently the first-order boundary **is still unique up to reduction-preserving gauge in the actual compensated-symmetry sector**. In the split global Moyal presentation, any s-boundary with deck character χ12 and internal-swap signs (a,b)=(-,+) is gauge-equivalent to the transported actual s-boundary. Any t-boundary with character χ34 and signs (+,-) satisfies the analogous statement. A convenient lift respecting these signs can replace the transported boundary, with its induced second-order gauge terms retained. This preserves the whole obstruction class, not just the six retained coordinates.

4. Without the symmetry condition, a genuine 20-dimensional ambiguity remains for each pair. The exact general obstruction-comparison criterion is the vanishing of the explicit linear-plus-Yoneda-square class in §5. Neither ordinary smoothness on the original elliptic carrier nor first-order uniqueness there is silently transferred to X̃.

These statements do not construct a convenient lift or prove any of the six remaining coordinates vanish. They remove an important ambiguity in what a valid normalized replacement would have to establish.

## 1. Reduce Ext¹ to a fixed coefficient bundle

The root cancels in End, and finite pushforward for d⁴ gives

    Ext^k(Ẽ,Ẽ)_χ12
      = H^k(Y, ρ*End H ⊗ L),
    L=O_Y(-1,-1,0,0).

The line L has its natural permutation linearization: its local odd generator t₁t₂ is **even** under a. There is no extra differential-form or alternating sign. This is the point on which the parity conclusion depends.

The quotient ρ is finite of degree 24. Its domain and target are smooth of dimension four; finite equidimensionality and the Cohen–Macaulay/regular local flatness criterion imply it is flat. Thus ρ_*L is a rank-24 vector bundle. Projection formula applies to the actual bundle End H.

For every integer k,

    H^r(P⁴,ρ_*L(k))
      = H^r((P¹)^4,O(k-1,k-1,k,k)).

For k≥1 only H⁰ can survive; for k=0 or -1 an O(-1) factor kills every cohomology group; for k≤-2 only H⁴ can survive. Therefore ρ_*L has no intermediate cohomology in any twist, and Horrocks splitting applies over C. Its Hilbert polynomial is k²(k+1)². Equivalently its graded generator degrees are determined by

    Σ_{k≥0} k²(k+1)² z^k = (4z+16z²+4z³)/(1-z)^5.

It follows that

    ρ_*L ≅ 4O(-1) ⊕ 16O(-2) ⊕ 4O(-3).                 (1)

This is a formal sheaf calculation, not a fresh HM matrix computation.

The accepted characteristic-zero HM cohomology inputs are

    h¹ End H(-1)=5,
    h¹ End H(-2)=h¹ End H(-3)=0.                       (2)

They are the previously audited small-certificate ranks. The twist -3 statement also follows from Serre duality and H³ End H(-2)=0. Applying (2) to (1) proves the dimension 20.

## 2. Resolve the internal-swap signs, not just the total dimension

Factor ρ as

    Y --p--> Z=P²×P² --m--> P⁴,

where p symmetrizes each pair separately and m multiplies binary quadratics. The double-cover quotient P¹×P¹→P² has

    q_*O = O_(+) ⊕ O(-1)_(-).

Its branch divisor is the discriminant conic. The anti-invariant generator is the alternating difference of the two roots, fixing the sign convention. Since O(-1,-1)=q*O_P²(-1) with the symmetric tensor-product linearization, the four (a,b)-summands of p_*L are

    (++): O_Z(-1,0),      (-+): O_Z(-2,0),
    (+-): O_Z(-1,-1),     (--): O_Z(-2,-1).             (3)

The map m is finite flat of degree six by the same smooth/Cohen–Macaulay argument. For a,b among the indices in (3),

    H^r(P⁴,m_*O_Z(-a,-b)(k))
      = H^r(Z,O_Z(k-a,k-b)).

Because |a-b|≤2, a nonzero H² tensor factor cannot coexist with H⁰ on the other P² factor: that would require |a-b|≥3. H¹ and H³ also vanish. Hence all four pushforwards are ACM and split. Their Hilbert series or successive H⁰ dimensions give

    m_*O(-1,0)  ≅ 3O(-1) ⊕ 3O(-2),
    m_*O(-2,0)  ≅ 6O(-2),
    m_*O(-1,-1) ≅ O(-1) ⊕ 4O(-2) ⊕ O(-3),
    m_*O(-2,-1) ≅ 3O(-2) ⊕ 3O(-3).                  (4)

For example the first has h⁰(k)=binom(k+1,2)binom(k+2,2), and the second has h⁰(k)=binom(k,2)binom(k+2,2) for k≥2. The last two also follow by twisting m_*O and m_*O(-1,0), respectively. Their sum agrees with (1).

Tensor (4) with End H and use (2). This proves the parity dimensions in the results. In particular

    Ext¹(Ẽ,Ẽ)_(χ12,a=-1)=0,
    Ext¹(Ẽ,Ẽ)_(χ34,b=-1)=0.                         (5)

These are canonical parity vanishings, even though the line-bundle splittings inside individual parity summands need not be canonically chosen.

## 3. The actual transported boundary admits the required signs

This step is essential: a vanishing subgroup is useful only if the actual boundary lies in its affine sector.

Use the two-parameter presentation, with π_P=Ṽ₁∧Ṽ₂ and π_Q=Ṽ₃∧Ṽ₄. The globally split Moyal algebra has the canonical compensated actions

    a:(s,t)↦(-s,t),      b:(s,t)↦(s,-t).

The classical bundle Ẽ has its canonical factor-permutation structure. On a group-stable affine trivializing refinement, use the functorial Čech nerve (or an equivariantly identified refinement), so pullback and the canonical bundle identifications define an action on transition cochains commuting with δ. This avoids an untracked reordering sign in an ordered-nerve implementation. Thus the s-source -μ_P(g,g) is χ12 with signs (-,+), and the t-source is χ34 with signs (+,-).

One must not merely average the already transported boundary and assume that doing so preserves its class. Instead justify the symmetry *before* normalization, where the imported pair-character Ext¹ vanishing is available:

(a) Replace the cusp scalar first-order cocycle b_P, if necessary, by its (-,+) internal-swap projection. Its cohomology class already has those signs: exchanging the two degree-one Čech factors negates their cup product. The difference is a scalar Čech coboundary, and its primitive can be chosen in the pair deck character by deck averaging. Use that scalar arrow equivalence, including the module-boundary transport, to identify the first-order presentations. The same applies to b_Q. This is valid on the cusp without any singular HKR claim.

(b) In this symmetrized presentation, average a first-order module solution into the prescribed deck and internal-swap sector. The first-order equation is linear and its source is in that sector, so the average is still a solution. The difference from the actual solution is a pair-character End-valued cocycle. The accepted cusp pair-character Ext¹ vanishing makes it a gauge coboundary. Thus the averaged solution is genuinely equivalent to the actual first lift, not an arbitrary substitute.

(c) After normalization, choose scalar splitting primitives c_P,c_Q in those same signs. This is possible because b_P,b_Q are scalar coboundaries on X̃, and the finite-group projection commutes with δ. Hence

    û_P=u_P-c_P g,      û_Q=u_Q-c_Q g

have exactly the desired signs. The order-two derivation-chart gauge does not alter these first-order boundaries.

(d) This equivariant splitting produces the same first-order module gauge class as the explicit splitting in [cusp-normalization-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/2420001144ab274e51e32d60fb88f492e178115f/research/hm/null-cusp-normalization/cusp-normalization-next.md). Compose its scalar arrow primitive with the scalar presentation change in (a), so that both primitives kill the same original b. Their difference is a scalar Čech one-cocycle on X̃. Since H¹(X̃,O)=0, it is a scalar coboundary, and its effect on û is an ordinary first-order module gauge. There is also no new second-order ambient structure hidden here. If the composite primitive is c+δr and the explicit primitive satisfies T−{c,−}=δD, then T−{c+δr,−}=δ(D−{r,−}). The chart correction remains an ordinary derivation and removes the overlap correction inside the same Moyal product modulo h³. All induced module terms are transported as in the audited full algebroid equivalence; none is discarded.

This argument needs neither vanishing of normalized pair-character Ext¹ nor an unproved lift of additive group actions on Ẽ. It uses the accepted cusp uniqueness, explicit scalar splitting, finite-group averaging, and H¹(O_(P¹)^4)=0.

## 4. Symmetry-preserving replacement theorem

Let û_P be the actual transported boundary, represented in the sector from §3, and let v_P be any other first-order solution for the **same** global Moyal algebra and same classical Ẽ, satisfying the same deck and internal-swap equivariance. Then

    w_P=v_P-û_P,
    z_P,ij=g_ij^(-1) w_P,ij

is an End-valued Čech one-cocycle in (χ12,a=-,b=+). By (5), [z_P]=0. A zero-cochain r_P therefore gives the required reduction-preserving first-order change of module frames. Use the actual star-invertible frame change 1+s r_P (with its formal inverse) modulo total parameter degree three. It carries the second-order residual by an End-valued Čech boundary; the h² terms induced by star multiplication must be kept.

The same proof applies to v_Q in (χ34,a=+,b=-). Combining the frame changes to first order gives one two-parameter reduction-preserving gauge, with its mixed second-order terms included. Therefore the **entire** second-order obstruction class agrees coefficientwise. In particular the pure s² and t² classes, their sum, and all the accepted compact-target projections agree.

If the actual boundary is retained in the nonsymmetric explicit gauge from the normalization note, first apply its gauge identification from §3(d). This is a comparison of boundary classes, not an assertion that the original raw cochains already have strict parity.

The theorem's hypotheses are concrete and checkable: same algebra, same classical bundle, a genuine first-order solution, and the stated compensated equivariance. An arbitrary convenient pair-character lift without those signs does not meet the criterion.

## 5. Exact criterion when the replacement is not symmetry-preserving

Let u denote a fixed first solution in the split global star algebra, and let u+w be another. Define z_ij=g_ij^(-1)w_ij; the difference equation says δz=0. The split residual is

    R(u)=u_jk u_ij + μ₁(u_jk,g_ij)+μ₁(g_jk,u_ij)+μ₂(g_jk,g_ij).

Direct subtraction, in the actual row convention, gives

    R(u+w)-R(u)
      = w_jk u_ij + u_jk w_ij
        + μ₁(w_jk,g_ij)+μ₁(g_jk,w_ij)
        + w_jk w_ij.                                  (6)

Both normalized residuals are cocycles, and the quadratic term alone is the ordinary Yoneda-square cocycle in this row convention. Consequently the linear term defines a cohomology class ℓ_u([z]), and

    o(u+w)-o(u)=ℓ_u([z])+[z]².                         (7)

Here [z]² is represented explicitly by g_ik^(-1)w_jk w_ij; this fixes any potential cup-order convention. Well-definedness under z↦z+δr follows from the genuine first-order star-frame gauge and its induced second-order coefficient. Linearity of ℓ_u follows directly from (6), after the quadratic cocycle is removed.

Thus equality of full obstruction classes is equivalent to

    ℓ_u([z])+[z]²=0 in Ext²(Ẽ,Ẽ).                   (8)

Equality only in the invariant target is equivalent to the invariant projection of (8). If the replacement is not in the symmetry sector, its invariant obstruction need not lie in the same six-dimensional compact subspace; one cannot discard extra components by definition.

For a χ12-only replacement in a pure P problem, z ranges over the actual 20-dimensional group computed above. The linear term has deck character χ12²=1 and can affect the invariant obstruction; deck-character bookkeeping alone no longer kills it. Its active-swap sign is odd because u_P and μ_P are a-odd while every z is a-even, whereas z² is a-even. Hence, for this single-pair problem,

    o(v_P)=o(û_P) iff ℓ_(û_P)([z])=0 and [z]²=0,   (9)

with the two conditions separated by the a parity in invariant Ext². This refinement is a formal consequence of the newly computed parity, not a smoothness assertion. In particular an obstruction-free replacement would force the actual even obstruction to be -[z]²; it would not by itself prove the actual obstruction zero.

No evaluation of ℓ_u or the Yoneda square on the 20-dimensional ambiguity space is made here. The symmetry-preserving theorem avoids both evaluations because its admissible [z] is zero.

## 6. Inputs, provenance, and limits

Reviewed source documents:

- [cusp-normalization-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/2420001144ab274e51e32d60fb88f492e178115f/research/hm/null-cusp-normalization/cusp-normalization-next.md) and [cusp-normalization-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/2420001144ab274e51e32d60fb88f492e178115f/research/hm/null-cusp-normalization/cusp-normalization-audit.md);
- [pure-square-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-square-next.md), [pure-target-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-target-next.md), [branch-boundary-extension.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-boundary-extension.md);
- [dihedral-character-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/43194f29b0f1b01dac1ef1cc92742359da5e6e34/research/hm/null-dihedral-mixed-vanishing/CHARACTER-AUDIT.md), especially its independently audited cohomology inputs;
- [pinned full algebroid source](https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md), especially the actual row differential and complete residual;
- [pinned small-rank source](https://github.com/Akilleez-QA/read-em-and-weep/blob/f968b53943ba2312f09fbc3e8f9d462e86bcaa34/research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md) and [classical Ext model](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md).

Pinned source lineage (inherited from the cited source copies and audits; not a new remote-byte authentication):

- Actual carrier and normalized HM model: commit 3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f, research/hm-carrier-and-atlas.md.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md
- Classical line-complex and deck-character source: commit add03476d9055aa00e1e00778eea6332cf8e01cc, research/hm/ext-model.md.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md
- Previously audited small-rank statement: commit f968b53943ba2312f09fbc3e8f9d462e86bcaa34, research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/f968b53943ba2312f09fbc3e8f9d462e86bcaa34/research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md
- Full PR16 algebroid/residual: commit c8aec970fd65a105f39f4e8aeb8a17f0f0053f89, blob a58834ab61e18a5dedd8a7bf20bec7121bfa9165, research/hm/second-order-algebroid.md.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

The ranks (2), actual first-order cancellation, cusp pair-character uniqueness, and identification of the transported actual source remain explicit imported premises. New deductions are (1), the parity refinement (3)–(5), and the symmetry-preserving comparison theorem. The residual-difference criterion is derived directly from the pinned row formula.

No conclusion about mixed vanishing is newly established; that remains conditional on the imported certificates. No obstruction coordinate is evaluated. No second-order primitive or unrestricted normalized smoothness theorem is constructed. No public action is authorized by this report.

## Independent review

The independent review in [normalized-boundary-symmetry-audit.md](normalized-boundary-symmetry-audit.md) accepts the Ext¹ splitting, swap parity, constructive cusp-to-normalized symmetry bridge, and residual-comparison criterion, under the explicitly imported rank and source premises. Its suggested explicit pair-character choice of scalar presentation primitive has been incorporated in §3(a).
