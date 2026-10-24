# 148. The ordered rank-four reverse-adjacent plateau is excluded

**Craig Ward · 24 October 2026 UTC · A fourth coarse rank-four stratum removed**

## Exact new reduction

The [reverse-adjacent theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/ce63dba8623675e6fa5760917873b29e39a62ce3/research/hm/rankfour-reverse-adjacent/PROOF.md) excludes generic SF rank four with ordered maximal plateau lengths (k,l)=(3,2), under its retained actual-geometric and physical-marking hypotheses.

Relative to [chapter147](147-rankfour-adjacent-euler-exclusion.md), **24 necessary bad coarse bins become 23**, and the rank-four group decreases from six to five. The groups at ranks five through twelve remain 6,4,2,2,1,1,1,1. The optional source-labeled refinement decreases from 96 to 92, since the baseline necessary overlist assigns all four source labels to this l=2 container; these are not four additional coarse exclusions.

The theorem is not obtained by exchanging the two directions in the earlier (2,3) proof. The actual E has rank17, while Q* has rank13 and a different presentation. Forward length two does not force source Z, and no Z splitting is assumed. The exclusion covers the whole ordered stratum without a source-specific restriction.

The remaining rank-four bins are (1,1), (1,2), (2,1), (2,2), (3,1). These necessary containers are not asserted realized or equally difficult. Generic SF≥4 remains the lower bound: SF≥5, positive-square surjectivity, full-adjoint invertibility and the original repair are not proved. Chapter147's forward bound l≤2 still holds, with no unsupported global backward bound.

## Two endpoint alternatives

The hypothetical actual saturated chain has ranks 5,9,13,17,21,25, with E=F₃. Its reversed annihilator chain has Q*=D₂; the two rank-five endpoints F₀ and D₀=F₅⊥ are not identified.

Persistence, including the endpoint containments, bounds every endpoint degree by -5. Center-even determinants and perfectness sharpen the total endpoint bounds to a=deg F₀≤-26 and b=deg D₀=deg F₅≤-26.

The four regular adjacent rank-four derivative maps have effective determinant defects δ_i≥0. Eliminating the first quotient degree gives

    2a+3b=-150+2δ₁+4δ₂+6δ₃+3δ₄.

Writing a=-26-2u and b=-26-2v yields

    4u+6v+2δ₁+4δ₂+6δ₃+3δ₄=20.

Every nonzero invariant effective divisor on the physical parameter line has degree at least twelve. The smallest nonzero weighted defect would cost twenty-four, exceeding twenty. All defects therefore vanish. The only possibilities are:

| Case | Endpoint degrees (a,b) | Five quotient degrees |
| --- | --- | --- |
| I | (-36,-26) | (-14,-6,2,10,18) |
| II | (-30,-30) | (-16,-8,0,8,16) |

Set B=L₃. The derivative-induced graded isomorphisms give (L₁,…,L₅)=(B(-4),B(-2),B,B(2),B(4)). They do not split the actual filtration or connection.

## Eliminate B exactly, without enumerating it

The actual lower and upper sequences give in equivariant K-theory

    [E]-[F₀]=[B(-4)]+[B(-2)]+[B],
    [Q]-[D₀*]=[B(2)]+[B(4)].

Twist the second identity by -6 and subtract. The quotient is eliminated exactly:

    [B]=[E]-[F₀]-[Q(-6)]+[D₀*(-6)].

The plus sign, twist -6, dual on D₀ and use of Q rather than Q* are essential. This follows from actual exact sequences, not from checking a few scalar dimensions.

For each possible endpoint pair define the forced Euler function

    C(t)=χ_G(E(t))-χ_G(F₀(t))-χ_G(Q(t-6))+χ_G(D₀*(t-6)).

An actual pair must have C(t)=χ_G(B(t)). Substitution into the upper sequence requires

    C(t+2)+C(t+4)+χ_G(D₀*(t))-χ_G(Q(t))=0.

Testing t=0 and t=1 supplies necessary conditions only. The proof does not claim those two evaluations characterize K-theory classes, construct B, or realize a flag.

## The endpoint domain is finite and exhaustive

Each endpoint has rank five, degree d and top slope at most -5. Any one ordinary degree e must satisfy d+20≤e≤-5, because the other four degrees sum to at most -20. Correct central parity and rank/degree constraints then give:

| Degree | Forced slope window | Abstract endpoint splittings |
| ---: | --- | ---: |
| -36 | [-16,-5] | 44 |
| -30 | [-10,-5] | 15 |
| -26 | [-6,-5] | 4 |

Case I consequently has 176 endpoint pairs, and case II has 225, for 401 altogether. These are newly derived abstract endpoint data, not actual instances or historical source records. No rank-four quotient splitting or quotient slope window is enumerated.

The two necessary Euler identities leave four pairs in case I and ten in case II. The proof records every survivor explicitly, rather than treating fourteen as a sufficient certificate by itself.

## Persistence positivity rejects all fourteen

The actual exact sequences

    0→F₂→E→B→0,
    0→D₁→Q*→B*(-2)→0

combine with H⁰(F₂(2))=0 and H⁰(D₁(3))=0 to force two genuine cohomology characters:

    C_pr=C(2)-χ_G(E(2))=H¹(F₂(2)),
    C_du=-C(-3)-χ_G(Q*(3))=H¹(D₁(3)).

The second expression uses equivariant Serre duality, χ_G(B*(1))=-χ_G(B(-3)); the negative twist is -3. No H¹ term is discarded and Q* is not replaced by E.

In case I, the lower endpoint is either O(-10)+O(-8)+V O(-6) or W O(-9)+V O(-6). Each can pair with either O(-6)+(W+W′)O(-5) or O(-6)+S₄O(-5). For all four pairs the dual character is

    C_du=2W+T₆-W′,

which has negative W′ multiplicity. All four are impossible.

In case II, the lower endpoint is either O(-10)+S₄O(-5) or D O(-6). Each has five possible upper annihilators. For the upper choice O(-10)+(W+W′)O(-5), the dual character is W+S₄+T₆-W′, again impossible. For each of the other four upper choices the primal character is

    C_pr=-1+D+2P+V,

with negative trivial multiplicity. This excludes the other eight pairs, hence all ten.

The forced cohomology dimensions are positive: 17 and 8 in case I, and 15 and 10 in case II. Ordinary numerical cohomology therefore does not reveal the contradiction. The obstruction is the negative irreducible multiplicity in a representation that must be genuine.

## Verification and boundary

The frozen proof SHA256 is `6e9a8770e4d418e6ba22a3ebaa2b1523605a178ac0522d7f4ab72507d536106a`. The final independent whole-proof review accepts the conditional mathematical argument and independently derives the endpoint lists, both Euler identities, all fourteen survivors and their two character columns. Its exact conjugacy-class calculation imports neither the author code nor a McKay graph.

The final author certificate reports 10,951 controls and 54 mutation rejections. The final independent review SHA256 is `fd358312450ff6a2dedc9becb7b56ebbab9860618304f93d0bd2d952fb253a01`, with 470 checks and nine executed mutation controls. Ordinary and optimized runs reproduce the frozen outputs. Controls explicitly test the unequal E/Q* presentations, Serre twist, signs, endpoint parity, physical marking and omitted H¹ corrections. They support the written argument, not proof-assistant certification of the actual geometry or all transitive sources.

No actual HM coefficients, parameter values, jets, matrices or instance ranks are evaluated. No historical enumeration or stopped experiment is rerun. Prior chapters and the delivered v0.3 PDF remain unchanged.
