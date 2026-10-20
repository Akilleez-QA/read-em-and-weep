# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent audit of the Čech primitives

## Verdict: PASS

The formulas in `PROOF.md` are correct with its explicitly declared totalization, source orientation, and transgression convention. No correction is required. This audit checked the proof and the two cited proof documents by static reading and formal graded algebra only. The imported geometric/cohomological theorems are dependencies, not newly proved or evaluated here.

## 1. Grading and total multiplication

Write a bidegree as `(r,p)` (internal degree, Čech degree). The differentials commute before totalization. Therefore `δ=∂+(−1)^r c` squares to zero. For the Alexander–Whitney product multiplied by `(−1)^(p r′)`, the internal and Čech Leibniz identities combine into the Leibniz rule with sign `(−1)^(r+p)`. This verifies the product convention used later. In particular a global degree-one left factor contributes no cup-product sign, while its total differential still has the usual odd Leibniz sign.

The graded adjoint operators `T_i` anticommute because their graded commutator is the adjoint action of `D_iD_j+D_jD_i`, which vanishes. Their squares vanish as well. These assertions also hold on all intermediate internal degrees in the bounded Hom complex; maps outside the allowed range are zero.

The additional convention-comparison paragraph also passes. Conjugation on bidegree `(r,p)` by `(−1)^(rp)` changes the internal differential sign to `(−1)^p` and cancels the sign on the Čech differential, giving `c+(−1)^p∂`. Transporting the product by the same conjugation changes its sign to `(−1)^(r p′)`. On total degree one, `r=1−p`, so `rp=p−p²` is even and the entire staircase `h` is unchanged. On total degree zero, `r=−p`, so the factor is `(−1)^p`; this gives exactly the claimed componentwise conversion of `b`. Global constants are unchanged.

For the component `q_p`, the internal degree is `1−p`. At twist `−2` its line degree is `(1−p)−2=−1−p`, precisely the degree of the reciprocal of its `p+1` denominator coordinates. Its total degree is one. Every denominator coordinate is invertible on the relevant Čech intersection, so these are regular local sections.

## 2. Staircase signs

Let `E(J)=Σ_{j∈J}j+3m−m(m−1)/2`, where `m=4−p`. If `i` occupies position `s` in the increasing set `I`, then there are `i−s` elements of `J` below `i`. Hence moving `T_i` into its increasing position contributes `(−1)^(i−s)`.

Adding `i` to `J` changes `E` by `i+3−m=i+p−1`. Thus the term obtained by deleting index `i` in `c q_{p−1}` has coefficient

    (−1)^s a(I\{i}) = (−1)^(s+i+p−1) a(I),

whereas the corresponding term of `∂q_p` has coefficient `(−1)^(i−s)a(I)`. Their ratio is `(−1)^(p−1)`. This proves exactly the claimed staircase identity, including its sign. Contributions with `i∈J` vanish by `T_i²=0` and anticommutation.

The Čech differential of `q_{p−1}` enters `δh` with sign `(−1)^(2−p)`. Its sum with `∂q_p` is zero. The top cochain has coefficient one and is the stipulated source generator times `φ`. For `p=0`, the exponent defining `a({i})` is `16−i`, giving `(q_0)_i=(−1)^i T_{[0,4]\{i}}φ/v_i`. Its differential is `T_0T_1T_2T_3T_4φ` on every chart. There is no Čech term above the top degree. Consequently `δhφ=Fφ` with the stated positive sign.

This identifies `d₅` in the declared staircase convention. A different independent convention for spectral-sequence signs might rename this differential by an overall sign; there is no ambiguity within this proof, which fixes its convention before using the inverse.

## 3. Multiplication homotopy and regularity

The alternating insertion operator satisfies `cs_l+s_lc=1` in positive Čech degree. In degree zero its unaugmented form is `(s_l c a)_i=a_i−a_l`. Both formulas remain valid with repeated indices set to zero. Insertion and the internal differential commute after restriction to common intersections.

For an inserted term of `v_l q_p`, if `l` already belongs to the output index set the alternating term is zero. Otherwise its denominator contains `v_l` exactly once and that factor cancels. The resulting denominator uses only output indices. Thus every summand of `b_lφ` extends regularly, without requiring invertibility of `v_l` on the output intersection. Its bidegree is `(1−p,p−1)`, total degree zero, and its line degree at twist `−1` is `−p`, agreeing with its remaining denominator.

At output Čech degree `t≥1`, the internal contribution to `δb_lφ` has coefficient `(−1)^t` and is `s_l∂(v_lq_{t+1})`; the Čech contribution is `cs_l(v_lq_t)`. The staircase gives `∂q_{t+1}=(−1)^t c q_t`, so their sum is `v_lq_t`. At the top degree the missing internal contribution is replaced by zero, consistently with `c q_4=0`. At degree zero the contribution is `s_l c(v_lq_0)`, which is `v_l(q_0)_i−v_l(q_0)_l`. The last term is the constant global map `H_lφ`.

This proves the actual cochain identity

    δb_lφ = v_lhφ−H_lφ.

The localization check is legitimate because the coefficient sheaves are direct sums of line bundles on integral projective space, so restriction into the common localization is injective. Also `∂H_lφ=v_lFφ`: only the `T_l` term survives, and its ordering sign cancels the prefactor `(−1)^l`. Hence the claimed removal of a possible residual cohomology class is justified by explicit exactness, not merely by closedness.

## 4. Massey defining system and surviving representative

The derivative-relations proof supplies injectivity of `d₅` and identifies its image with the derivative-wedge relations. With the source generator fixed, the inverse notation `φ_ab` is therefore meaningful and unique. The current proof does not need to evaluate it.

The cochains `α=v_lD_k`, `β=D_i`, and `γ=D_j` are closed of total degree one and weights zero, one, and one. The proposed primitives satisfy the ordered defining-system equations exactly:

    δhφ_ij = βγ,
    δH_lφ_ki = αβ.

Thus `αhφ_ij+H_lφ_kiγ` is the cocycle with the plus sign stipulated in the imported definition. Substituting the multiplication homotopy gives the additional term `D_kδb_lφ_ij`. Since `δD_k=0` and `D_k` has odd total degree, this term is `−δ(D_kb_lφ_ij)`, verifying the sign of the displayed exact correction.

The remaining two terms have internal degree two, Čech degree zero, and twist `−2`; they are constant global maps. Their differentials are respectively `−v_lD_kD_iD_j` and `+v_lD_kD_iD_j`, so the sum is closed. The derivative-relations theorem identifies its hypercohomology class with its class modulo the span of the derivative products. The weight-two Massey theorem supplies independence from defining-system choices. These inputs establish precisely the claimed formula on the indicated inputs, without asserting that those weight-zero inputs span all of `U_0`.

## 5. Scope check

No actual inverse transgression, Massey value, nonvanishing claim, image dimension, or residual class was evaluated. The audit used no concrete matrix operation, instance evaluation, point, jet, rank calculation, or external write. The only new output is this local audit document. The proof's stated boundary is respected.
