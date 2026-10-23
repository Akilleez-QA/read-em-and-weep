# Four distinct geometric coefficient lines

**Craig Ward · 23 October 2026 · PR1036**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/bb22e239e9423b54487236dba8c4f70f9e6b738f/research/hm/source2-pure-v-lift-jet-placement/PROOF.md).

## 1. Exact placement in the pinned lift basis

In the universal basis R=αR₁+βR₂, with R₁=ρ_D L* and R₂=L*ρ_P, the four previously intrinsic lines have these distinct coordinates:

| Geometric condition | Equation | Projective coefficient |
|---|---|---|
| Order-five jet line ℓ₅ | 2α−β=0 | [1:2] |
| Order-three jet line ℓ₃ | 2α+β=0 | [1:−2] |
| Square-conic base line ℓ_Δ | β=0 | [1:0] |
| Exceptional generic-rank-three lift | α+β=0 | [1:−1] |

![Exact coefficient ratios of the four distinguished universal lines, with the separate projective point at infinity](figures/pure-v-coefficient-pencil.svg)

These equations use the pinned bilinear-adjoint normalization. They identify universal lines, not actual source coefficients or an actual nonzero gate.

## 2. Whole-orbit certificates, not selected jets

Let N be the signed maximal-minor row of the original second-channel representative B_a(h)=Π(a²h). Torsion-freeness identifies its cokernel with the relevant rank-one ideal-sheaf image. The gate's two nonic rows are therefore F₁=NLR₁ and F₂=NLR₂, up to a common nonzero target normalization. They are not substitute systems chosen solely by characters.

On the symbolic chart p=1, the known reduced axis ideals I₅ and I₃ have quotient lengths 6 and 10, so the chart contains their full orbits. Ordinary powers of these radical zero-dimensional ideals impose the respective jets at every point. Exact polynomial remainders give

    rem_(I₅³)(F₂)=−½ rem_(I₅³)(F₁),
    rem_(I₃²)(F₂)=+½ rem_(I₃²)(F₁),

with both displayed F₁ remainders nonzero. Hence the two jet-kernel equations are exactly 2α−β=0 and 2α+β=0. All direction variables remain indeterminate.

For the conic line, substitute the entire symbolic square family (p,q,t)=(u²,2uv,v²). Full homogeneous divisibility by f₁₂ holds for F₁ and fails for F₂, establishing β=0. Degree recovery and the explicit square-factor/zero-point identity retain the homogeneous boundary; no actual square or orbit representative is evaluated.

## 3. Consequences for distinct objects

The rank-three lift line is off both jet lines, so its nonic base ideals at all sixteen prescribed axes equal the old Z ideals. This does not by itself exclude additional off-axis basepoints. Both jet lines have generic **lift** rank four. Each of these three lines misses the conic-base line and therefore has no conic basepoints.

Together with [PR1035](75-pure-v-finite-support.md), each jet line has support exactly the sixteen axes, because it admits neither additional off-conic support nor conic points. The four-line theorem itself retains only the older exceptional length lower bounds; it does not compute their exact local ideals or lengths.

Matrix rank of R, nonic component-ideal jets and the original fourth quotient map are different invariants. The coordinate placement does not select any actual alternative or infer that fourth's rank from the lift. The packet reports independent full-proof and homogeneous-boundary review, with 40 ordinary/optimized checks and five authenticated input files. Four necessary source-dual pairs across three labels remain.

The subsequent [PR1037 exact-local theorem](78-pure-v-exact-jet-lengths.md) closes this jet-line length gap: ℓ₅ has m³ at six axes and m at ten, total 46; ℓ₃ has the six prescribed length-four ideals and m² at ten, total 54. No actual coefficient is selected.
