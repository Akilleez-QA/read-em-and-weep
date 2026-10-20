# Implication audit: mixed lift is not yet the full second-order lift

> Historical scope audit: the distinction between mixed, diagonal, and full two-parameter lifting remains valid. The suggestion below that second-ambient freedom might affect character zero is superseded for this actual carrier by the subsequent [characteristic-map theorem](pure-square-next.md) and [audit](pure-ambient-audit.md). The pure obstruction itself remains unevaluated.

## Finding

The thirty retained tests were the remaining tests of the original **mixed/full-sign component**, not demonstrably the last tests of the full second-order module obstruction. The new D5 argument proves an original-upstairs module lift over C[s,t]/(s²,t²), with the already established source-comparison premises. It does **not** yet prove a module lift over C[s,t]/(s,t)³ or over C[h]/h³ for the literal diagonal PR16 two-jet.

This is a positive distinction, not evidence that the remaining pure classes are nonzero. No inspected later source supplies their vanishing. The pinned full source explicitly warns that its full-sign comparison proves neither equality of all weight components nor vanishing of the full Ext² obstruction.

## Exact decomposition and missing equations

The authenticated two-parameter ambient has

μ=m0[1+(sD_P+tD_Q)/2+(sD_P+tD_Q)²/8],
F=id+s²T_P+t²T_Q,
A=1+β+β²/2, β=sb_P+tb_Q.

It specializes to the literal one-parameter PR16 ambient by s=t=h **before** taking the mixed quotient. For the actual equivariant first lift g+s u_P+t u_Q, the normalized quadratic defect decomposes as

C₂=s² C_PP+st C_PQ+t² C_QQ.

The deck characters are 0, χ1234, 0 respectively. The known first-order characteristic cancellation supplies u_P and u_Q; the vanishing H1 in pair characters makes their equivariant gauge classes unique. It does not solve second-order pure equations.

For either pair p=P,Q, specializing PR16 §5 gives the complete pure numerator

R_pp = u_p,jk u_p,ij
 + μ_p(u_p,jk,g_ij)+μ_p(g_jk,u_p,ij)
 + μ_pp(g_jk,g_ij)+T_p,ij(g_jk)g_ij
 − b_p,ijk u_p,ik − (b_p,ijk²/2)g_ik
 − μ_p(b_p,ijk,g_ik),

where μ_pp=m0 D_p²/8 and C_pp=g_ik⁻¹R_pp. All terms have trivial deck character. The last same-pair derivative term and T_p term are among the terms eliminated by the mixed projection, not by a proof that their pure classes vanish.

The exact missing equations for the fixed two-parameter ambient and boundary are δx_PP=−C_PP and δx_QQ=−C_QQ. After the mixed primitive is supplied, the diagonal obstruction for that same boundary is [C_PP+C_QQ]; its vanishing is a weaker requirement than the separate two-parameter vanishings, but neither is proved by the mixed result. Factor exchange relates C_PP and C_QQ by transport, not an established negative sign, so cancellation cannot be assumed.

There is no ring substitution s=t=h from C[s,t]/(s²,t²) to C[h]/h³: it would impose h²=0. Thus a mixed-quotient lift cannot itself be specialized into a full second-order diagonal lift.

## Strongest justified positive result

With the D5 proof and the existing constant-component result, the canonical corrected mixed class is zero. The established actual root/Morita/source comparison identifies the raw mixed class with j(C). If D_raw=j(c)+δq and δH_model=c, the original mixed transition correction is x=−j(H_model)−q. Hence the original, already chosen first-order boundary extends over the actual mixed quotient. This is stronger than merely saying an abstract thirty-vector is zero, but weaker than full second-order existence.

The independence from arbitrary first-order choices established for the full-sign projection does not extend automatically to the remaining character-zero obstruction. Likewise, changing a new ambient coefficient can affect character zero through the characteristic map, unlike the full-sign sector. The problem must specify whether the literal two-jet is held fixed before invoking that freedom.

## Next gap, before higher order

The next justified mathematical target is the pure-square residual above, including its noncentral same-pair terms, or a valid theorem annihilating its class for the chosen boundary and fixed ambient. Only after a full quadratic module jet is constructed is a third-order module obstruction defined for that jet. At degree three the equivariant parameter monomials s³,s²t,st²,t³ have pair characters P,Q,P,Q; the mixed D5 proof supplies no general vanishing in those sectors. Previously proved ambient formal extension controls ambient coherence, not module obstructions. Higher module obstructions can depend on earlier module and ambient choices.

## Exact sources checked

1. Full literal residual, projection distinction, and full second-order stopping criterion: PR16 source at c8aec970fd65a105f39f4e8aeb8a17f0f0053f89, Sections 5, 8, 9:
https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

2. Actual first-lift characters and explicit scope limitation, Sections 2, 4, 5, at 08b73637d4136f91606aad332c46cafd064417f8, blob 946f96670ecb8152eaae16195329f9eb1243b7ae:
https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md

3. Authenticated two-parameter ambient, literal diagonal specialization, and distinction between ambient and module lifting:
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259871686

4. Mixed quotient explicitly discards pure-square transition corrections; pure-square characters are zero:
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6263865869

5. Actual source comparison [D_raw]=j(C), including pure-boundary matching:
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6274541018

6. Mixed representative reconstruction and correction signs:
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6279132359

7. Explicit cubic ambient construction, expressly not a module lift:
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260064519

Formal source audit; no obstruction coordinates were evaluated.
