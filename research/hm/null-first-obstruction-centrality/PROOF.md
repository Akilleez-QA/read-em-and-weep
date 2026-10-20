# First-obstruction premise: independent proof and pinned-source review

20 October 2026. Formal proof and pinned-source review; the imported physical source and ranks are not newly evaluated here.

## Verdict

The premise used in PR16 is provable from the actual carrier and its rank-two, holomorphically determinant-trivial structure:

**ev_E(π) = −15 Π id_E.**

This is an equality in Ext²(E,E), not merely an equality after trace. The crucial extra argument is rank-two centrality of the square of the Atiyah class. Trace alone would not establish it for a general bundle. Consequently the compensated first-order obstruction really vanishes, separately for each specified bivector pair. This establishes the first-existence premise, subject to the actual carrier and the explicitly stated standard HKR/Atiyah convention.

It does not remove the pair-character Ext¹ premise P2, prove any second-order coordinate vanishes, or supply a newly executed physical first primitive. Later pinned first-order source actually contains authored explicit primitive formulas; that historical distinction is explained below.

## 1. Actual carrier, not a Chern-data replacement

Directly fetched carrier source:

https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md

Returned blob: fc0b0c7cf512d93c7a4ea976f986b7332b926f51.

It specifies E=f*H⊗N, where H is the normalized rank-two Horrocks–Mumford bundle on P⁴, c1(H)=−h, c2(H)=4h², and f*O(1)=N². This is a genuine geometric construction, including monad and atlas, not an assertion that any bundle with a prescribed Chern character can substitute for E.

Since Pic(P⁴)=Z[O(1)], det H=O(−1). Hence det E=f*O(−1)⊗N²=O holomorphically. Writing θ=c1(N), f*h=2θ. The rank-two twist formula gives

c2(E)=f*c2(H)+c1(f*H)θ+θ²
      =16θ²−2θ²+θ²=15θ².

Only the stated classical geometry and standard Chern formulas are used; no matrix entries or physical cohomology ranks need evaluation.

## 2. Why the Atiyah square is genuinely scalar

Let E be any holomorphic rank-two bundle with a holomorphic trivialization of det E. Choose a smooth Hermitian metric inducing constant norm one on that determinant trivialization. One obtains this from any Hermitian metric by a positive scalar rescaling. The induced determinant Chern connection is flat, so the Chern curvature F has tr F=0 pointwise.

Use the Dolbeault representative of At(E) given by this curvature, with the common normalization/sign fixed by At(L)=c1(L) in the source's convention. Its entries are scalar forms of bidegree (1,1), hence even total degree. They commute under the total exterior product. In a local frame its matrix therefore has the form

A = [[a,b],[c,−a]],

with ab=ba, ac=ca, and bc=cb. Direct multiplication, not a cohomological trace inference, gives

A²=(a²+bc)I=(1/2)tr(A²)I.

This identity is gauge invariant and global, and descends to the Atiyah-class identity

At(E)² = (1/2)tr(At(E)²) id_E

in H²(X,Ω²_X⊗End E), with the exterior product on the Ω factors. Chern–Weil/Atiyah normalization gives ch2(E)=(1/2)tr At(E)²=(c1(E)²−2c2(E))/2. Since c1(E)=0,

**At(E)²=−c2(E) id_E.**

This argument does not incorrectly apply ordinary Cayley–Hamilton to arbitrary Ext-valued matrices or to an ordinary Alexander–Whitney cochain ring. The Dolbeault resolution supplies an actual commutative even scalar-form algebra before matrix multiplication. The analytic proof yields the algebraic coherent-cohomology identity here by GAGA, since X=C⁴ is smooth projective over C. There is no singular-HKR claim or claim about an actual root at the origin of the branch-parameter space.

The determinant hypothesis is holomorphic triviality, not merely vanishing of a topological first Chern number. The carrier supplies precisely that stronger hypothesis. No stability or Hermitian–Einstein connection is needed.

## 3. HKR factor and PR16's gerbe sign

Directly fetched PR16:

https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

Returned blob: a58834ab61e18a5dedd8a7bf20bec7121bfa9165.

Its product is μ1(f,g)=π(df,dg)/2, and its total Čech–forms product has sign (−1)^(q p′). Its row-module line calibration explicitly identifies the bivector characteristic contribution as

ev_E(π)=(1/2)ι_π At(E)².

The factor 1/2 is essential. Applying the identity above and the source definition Π=(1/2)ι_π θ² gives

ev_E(π)=−(1/2)ι_π(15θ²) id_E=−15Π id_E.

For a direct scalar check, θ_i is represented by α_i=(q_i/2)ω_i in Čech degree one and holomorphic form degree one. For the pair i<j, the total product introduces a minus sign:

ι_(Vi∧Vj) θ²=−(1/4)(q_i cup q_j−q_j cup q_i).

Thus

Π_AW=−(1/8)(Q12−Q21+Q34−Q43).

Graded commutativity in H*(O_X) gives [Qji]=−[Qij], so [Π]=−(1/4)[Q12+Q34]. This is a cohomology statement unless using a tensor Čech model with strict anticommutation.

PR16's row equation has first obstruction o1=ev_E(π)−[b]id. Therefore b=−15Π, not +15Π, cancels it. In the shorter representative b=(15/4)(Q12+Q34). The exact ordinary-nerve representative correction is present in the later source below; omitting it at cochain level is not justified.

Linearity gives this result for π12 and π34 individually, and hence vanishing in both corresponding deck characters. For the fixed algebraic first-order algebroid, zero class means the normalized first residual has an algebraic Čech primitive on an acyclic affine refinement. Character projection/averaging selects a primitive in the requested pair characters. Its existence does not depend on Ext¹ vanishing; Ext¹ vanishing is a separate uniqueness/comparison input.

## 4. Later pinned first-order source corroboration

Directly fetched:

https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md

Returned blob: 5f4e56252cd9a8a6eb218aceb911c95a1c330ebc.

This later source is stronger than the historical PR16 statement that its first-order lift remains to be instantiated. Sections 2–3 give authored scalar transgression and rank-two matrix formulas, and Section 4 gives their dictionary to a pinned generator. This review reads and checks their formal algebra but does not rerun that generator or independently verify its physical split matrices/determinants.

In its notation C=g_ik^−1 μ1(g_jk,g_ij), determinant-one row transitions yield logarithmic derivatives P_r and Q_r, each traceless. Put K(g)=μ1(g^−1,g)=−(1/2)π^{rs}P_rP_s. The product transition has logarithmic derivative P+Q. Therefore direct expansion in the twisted Čech differential gives

δK=(1/2)π^{rs}(P_rQ_s+Q_rP_s)
   =(1/2)π^{rs}[Q_r,P_s].

For ordinary traceless two-by-two matrices, [Q,P]=2QP−tr(QP)I. Since C=(1/2)π^{rs}Q_rP_s, this proves

δK=2C−tr(C)I.

Thus the trace-free part of the first Moyal defect is explicitly a boundary. This is an independent algebraic/cochain manifestation of the centrality proof above. It does not claim the raw defect itself is pointwise scalar.

The source's unsymmetrized total-product transgression T has

δT=str(A wedge A−A′ wedge A′),
str(A wedge A)=−30 θ0 wedge θ0,
str(A′ wedge A′)=tr(AE wedge AE).

Here wedge is deliberately ordinary coefficient wedge, not the total product. Its scalar cochain is s=−(1/4)ιπ^ord T−(15/8)r, with r_ij=q1,ij q2,ij+q3,ij q4,ij. Since δr=−(Q12+Q21+Q34+Q43), its exact conversion is

−15Π_AW=b+(15/8)δr.

The row/column transposition trace identity is tr C=−(1/2)ιπ^ord tr(AE wedge AE). Substituting the displayed equations gives exactly

δs=b−(1/2)tr C.

Combining the scalar and trace-free identities yields

x=sI−K/2,  u=gx,  δx=bI−C.

All factors/signs agree with PR16's equation. In particular the scalar projection contributes 1/2 because rank is two, independently of the HKR factor 1/2. Confusing these two factors can produce a wrong coefficient. The unsymmetrized transgression must retain both BA and AB; ordinary Čech cochains do not support a cyclic-trace shortcut.

## 5. Consequence and remaining boundary

PR16 itself invoked ev_E(π)=−15ΠI. But that equality is not an unresolved geometric hypothesis: rank two plus actual trivial determinant proves centrality, and the actual carrier's c2 and calibrated HKR convention fix its value.

A stronger present statement is therefore justified: the compensated first-order algebraic module exists, and the later pinned source already provides explicit authored lift formulas. No fresh physical evaluation is needed to prove the existence theorem. It would be misleading to say this review has instantiated or executed the source's physical comparison, or that it freshly validated all its claimed matrix identities.

Remaining independent premises include pair-character Ext¹ vanishing, HM/dihedral symmetry and target representation inputs, and whichever mixed-vanishing theorem is used. The six pure obstruction coordinates remain unevaluated. Centrality of At² gives no general second-order vanishing: the full second residual involves the chosen first lift, noncentral algebroid corrections, and nonlinear products, not merely the Chern character.
