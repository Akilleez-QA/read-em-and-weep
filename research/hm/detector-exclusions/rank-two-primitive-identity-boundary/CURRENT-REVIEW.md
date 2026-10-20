# Current independent mathematical review: S304

Review date: 2026-10-20.

**PASS within the stated hypotheses and bounded scope.** This review covers the complete proof, historical audit, dependencies, and current-scope text. It checks the mathematical argument and directly cited public prerequisites; it is not formal verification or an evaluation of an actual HM/source instance.

## 5. S304: exact pointwise primitive-linear boundary

The graded rank-two signs are correct:

    xy−yx=tr(xy)Id,
    (xy)₀=(xy+yx)/2=B(x,y)=B(y,x).

Adjugate-compatible primitive normalization gives symmetric traceless variables `q_ab=q_ba` and antisymmetric scalar odd variables `t_ab=−t_ba`. Moving an odd scalar past `a` gives precisely

    T(a,b,c)=B(a,q_bc)+B(q_ab,c)−t_bc a+t_ab c.

This proves outer reversal. The proof does not incorrectly discard the scalar primitive parts.

In the free graded-commutative coefficient algebra, the `P_a`, `P_b`, and `P_c` terms use different independent variable families. They are nonzero universal tensors because the Lie bracket of `sl₂` is nonzero. The family multigrading, not merely the coarser input tridegree, makes coefficient comparison valid. A relation among the three reversal representatives forces

    λ+μ=0, μ+ν=0, ν+λ=0,

and characteristic zero forces all coefficients to vanish. Therefore the three reversal differences are exactly the constant-coefficient relation space among the six formal permutations.

The cyclic sum is not a zero pointwise polynomial. PR185 §5 separately proves its **cohomological** vanishing using the third-order lift in the actual smooth family, not merely second-order unobstructedness. Imposing this one relation on the formal three-generator ordering space leaves dimension two; that is not a claim about the span of values for a particular actual triple.

The discarded scalar cocycle in the downstairs weight-two target is exact because `H²(P⁴,O(−2))=0`. This standard intermediate line-bundle vanishing needs no HM input. PR187 §§3 and 7 give exactly

    m110(b,c,a)=F(a,c,b),
    m101(b,a,c)=−F(a,b,c)−F(a,c,b)=−2F_sym(a,b,c),

with two symmetric and two alternating eligible components. The universal pointwise test adds no further relation in its stated sector. The needed cyclic proof is fully present in PR185, so a separate copy of the supplementary family-extension manuscript is not needed.

**Accepted conclusion:** the specified pointwise matrix-algebra shortcut supplies no additional permutation relation or four-component reduction. Differential equations, global realization, stronger geometric identities, and actual values are outside the classification.

## Reviewed file SHA-256 bindings

The four files below are the exact texts reviewed before this review was added.

- `AUDIT.md`: `2c6a7eb94ccde7b9ffeb502ee218a8196d206b92e6c4476f314e685a0868c5f7`
- `DEPENDENCIES.md`: `0574d845f4ff0579f46a3e8e42d6ec365a15d5b05b7a7c4973714c6cf9ce3554`
- `PROOF.md`: `117084d0b2934ca88341254cbcd855d322556867cf1bbd1f18b70b9768a50847`
- `SCOPE.md`: `7880453915ce6ede7ff3987b8839b0786a9fb8e774af9af58a5e77838c1625b1`

## Immutable public prerequisites

- [canonical: PR185, 721fdc556714bb40f0a805f01fae51cf6d555fd5](https://github.com/Akilleez-QA/read-em-and-weep/blob/721fdc556714bb40f0a805f01fae51cf6d555fd5/research/hm/cubic-loci/foundation-p04/CANONICAL-MASSEY.md): Sections 4–5 prove outer reversal and cyclic zero from an actual third-order family lift.
- [weighttwo: PR185, 721fdc556714bb40f0a805f01fae51cf6d555fd5](https://github.com/Akilleez-QA/read-em-and-weep/blob/721fdc556714bb40f0a805f01fae51cf6d555fd5/research/hm/cubic-loci/foundation-p04/WEIGHT-TWO-TRANSFER.md): Weight-two target and scalar H²(P⁴,O(−2))=0.
- [eligible: PR187, 1260bfd20b6680dc2ce66088c19ae6431b347ab0](https://github.com/Akilleez-QA/read-em-and-weep/blob/1260bfd20b6680dc2ce66088c19ae6431b347ab0/research/hm/cubic-loci/foundation-p05/ELIGIBLE-MULTIPLICITY.md): Sections 3 and 7 retain both symmetric and alternating two-component sectors and m101=−2Fsym. This excerpt suffices; whole-source coverage is not asserted.
