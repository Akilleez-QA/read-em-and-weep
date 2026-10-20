# Independent rank-two centrality and first-order sign audit

## Verdict

The proposed rank-two argument is valid for the **whole End(E)-valued cohomology class**, not merely its trace. In the actual PR16 conventions it gives

A² = −15 θ² id_E,
ev_E(π) = (1/2) ι_π A² = −15 Π id_E,
[b] = −15 Π,
[o₁] = ev_E(π) − [b] id_E = 0.

Here Π = (1/2)ι_π(θ²), B = 15Π, and the algebroid unit is exp(hb). In particular b is **minus** the HKR gerbe component B. This is a cohomological first-order cancellation, not a pointwise identity between the raw transition defect and b. It supplies no second-order vanishing claim.

## 1. Why centrality is genuinely End-valued

The bundle is holomorphic of rank two, with holomorphically trivial determinant. Choose a nonzero global holomorphic determinant section. Rescale any Hermitian metric by a positive scalar function so that the determinant section has constant norm. The induced determinant Chern connection is then flat, and the Chern curvature F of E has tr(F)=0 pointwise. Normalize F consistently with the Chern-normalized Atiyah class A and ch(E)=tr(exp A).

Locally write F=[[a,b],[c,−a]], with a,b,c complex differential forms of type (1,1). Their total degree is two, so the scalar form coefficients commute under wedge product. Therefore direct matrix multiplication, or Cayley–Hamilton over the even-form ring, gives

F² = (a²+bc) id_E = (tr(F²)/2) id_E.

This identity is gauge invariant and hence global. It is valid before taking trace or passing to cohomology. The Chern connection has (1,1) curvature and its curvature is Dolbeault closed by the Bianchi identity. Passing to Dolbeault cohomology identifies the square with the wedge-composition square of the Atiyah class in H²(Ω² ⊗ End E). Chern–Weil gives

tr(A²)=c₁(E)²−2c₂(E)=−30θ².

Thus A²=−15θ² id_E. Contracting by the global holomorphic bivector π is a cohomology operation and yields the full stated End-valued equality. Holomorphic triviality of det(E), rather than an unsupported inference from the trace alone, supplies the convenient trace-zero representative.

There is no claim that the arbitrary Ext algebra is commutative. Only the scalar differential forms underlying this curvature representative commute. Nor is there a claim that the square on an arbitrary Čech representative is pointwise scalar; such a representative may have a trace-free coboundary.

## 2. Čech–Dolbeault and HKR signs

PR16 §1 uses the total Čech–forms multiplication with sign (−1)^(form_degree × next_Čech_degree). Its Atiyah and polarization cocycles have bidegree (1,1). Their total squares are therefore minus their ordinary coefficient-wedge Alexander–Whitney squares. Both A² and θ² must be totalized together; changing the convention on only one square produces a spurious sign.

The curvature argument is in the ordinary differential-form algebra, i.e. the total-degree realization. The Čech-to-Dolbeault multiplicative comparison uses the corresponding Koszul convention. Consequently the same centrality identity transfers to PR16's total squares. Even a simultaneous alternate square convention cannot change their proportionality coefficient −15. The remaining contraction sign is fixed by PR16's explicit definition of Π and its line-bundle calibration, not guessed from a trace formula.

Specifically, PR16 uses ι_(V_i∧V_j)=ι_(V_j)ι_(V_i), μ₁(f,g)=π(df,dg)/2, and θ_i represented by q_i ω_i/2. Write Q_ij=q_i cup q_j. Totalization gives the precise Alexander–Whitney representative

Π_AW = −(Q_12−Q_21+Q_34−Q_43)/8.

In cohomology Q_ji=−Q_ij, so

Π = −[Q_12+Q_34]/4,
16Π = −4[Q_12+Q_34].

This is the actual normalization of PR16 §§1,4,7. It is not a new normalization imposed on the source.

## 3. The actual compensator and its representative correction

PR16 §4 defines the first-order module obstruction as ev_E(π)−[b]id_E. The scalar unit exp(hb) appears on the right side of the row-transition equation, so its contribution to the normalized defect is −b. To encode ξ=π+B with B=15Π, its actual gerbe is b=−B, represented by

b = (15/4)(Q_12+Q_34).

For r_ij=q_(1,ij)q_(2,ij)+q_(3,ij)q_(4,ij), the ordinary Čech differential gives

δr=−(Q_12+Q_21+Q_34+Q_43).

Hence the exact, not merely cohomological, representative conversion is

−15Π_AW = b + (15/8)δr.

One must retain this correction when constructing a primitive on an ordinary nerve. Independent odd factors may anticommute strictly in a tensor model, but ordinary Alexander–Whitney cochains do not do so strictly.

For N and N⁻¹, the bivector characteristic term is Π since (±θ)²=θ². The same b therefore gives compensated residual Π−(−15Π)=16Π. This reproduces PR16's mandatory first-order line calibration and independently fixes the compensating sign.

## 4. What newer explicit source establishes

The newer pinned `first-order-source.md` supplies more than abstract cohomological cancellation. In its §§2–3, let C=g_ik⁻¹ μ₁(g_jk,g_ij) and K(g)=μ₁(g⁻¹,g). Its formal transgression produces a scalar one-cochain s with

δs = b − tr(C)/2,
δK = 2C − tr(C) id_E.

Thus x=s id_E−K/2 satisfies δx=b id_E−C and u=gx solves the actual first-order transition equation. The scalar primitive includes the correction −15r/8. The raw trace-free defect is a boundary rather than necessarily zero. This agrees with the curvature centrality argument and avoids claiming that the old PR16 implementation-status paragraph is the latest state of the formal construction.

The second identity is special to traceless two-by-two logarithmic derivatives; it does not license s=0. Likewise centrality alone does not prove tr(C)=2b as cochains, does not give a resource bound for an executed comparison, and does not certify any second-order obstruction value.

## 5. Immutable sources and review scope

- [Actual carrier](https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md), blob fc0b0c7cf512d93c7a4ea976f986b7332b926f51.
- [Second-order algebroid, §§1,4,5,7](https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md), blob a58834ab61e18a5dedd8a7bf20bec7121bfa9165.
- [Existing first-order construction, §§2–3](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md), blob 5f4e56252cd9a8a6eb218aceb911c95a1c330ebc.

The independent review covers the curvature proof, total-product and HKR signs, and formal first-order transgression identities. It is not a fresh physical matrix evaluation, rank computation or verification of executed primitive coefficients. The formula x=sI−K/2 belongs to the cited existing source, not to this proof's novelty claim.
