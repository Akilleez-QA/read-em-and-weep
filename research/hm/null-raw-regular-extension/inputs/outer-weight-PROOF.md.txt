# Literal outer partition and standard Čech transport lowering

## Result and exact scope

The frozen `detector-realization/program.py` implements the stated first-hit partition, carrier54/legal29 weights, and signed staircase weighted sum. Its literal coefficient ranges and exponents agree with the pinned finite-formula source. No discrepancy was found in these formulas. This is a conditional denotation/lowering result: the regular extension of the actual whole coefficients and the actual source/HPL/frame denotations are imported premises, not conclusions of the binomial identities below. No actual detector value or ID0 vanishing follows.

The inspected program has SHA256 `87816979ce914f30629ba5187bc15d68ff6a3a34fd934672aaaf4e8fbb17a99b`, Git blob `745beade7f111b4648d5da36a962c787f1a29d72`. A read-only GitHub fetch at [e93cf712](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-realization/program.py) was byte-compared to the frozen local source. `pins.json` records all inspected input hashes; inert text copies are under `sources/`; historical reviews are labeled excerpts. See REVIEW.md for provenance limits. No production module was imported or executed.

The mathematical sources are:

1. [Outer finite formulas at 10810ee](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-support-certificates/outer_partition_source_binding.py), `PartitionChart.formulas` and `definitions`: literal B/Cbar/Dbar/legal quotient formulas, exact full-owner cancellation, 54/29/5251, and target-tag conditions. This is a source-definition specification, explicitly not executable lowering. Its SHA256 is `e99e4a8c8a3736a7ef583d66f8de21680fae7dca5fe253bff7483426c513fa00`.
2. [Regular cover transport at 10810ee](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-proof-foundations/hm-regular-cover-transport.md), §§2,5–8: unit identity, first-hit and two-carrier partition, legal line partition, Pi, prism and signed staircase. SHA256 `98a10d3da934ef5b6dfe1e2cf6af4ac46fcf6347e0e6081a8c0cbd58b2f7f02d`.
3. [JC domain application at e93cf712](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/full-lift-domain/PROOF.md), §§4–6, and its [independent conditional acceptance](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/full-lift-domain/review-independent.md): whole-source homogeneous owned-pole argument and regular extension, including all prism/restriction suffixes and J3 closure.
4. [Transport-binding review at e93cf712](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/transport-binding/review-independent.md): accepts only conditional metadata/template consistency. It explicitly does not supply an actual source binding, coefficient realization, or execution release. We do not upgrade that review to any stronger acceptance. `transport-binding/PROOF.md` is absent (read returned 404); the actual mathematical theorem is the linked regular-cover/scalar-family theorem, as that review itself explains.

The old generic transport note derives a conservative common power62 and permits sharper separately proved bounds. The selected powers54/29 here come from JC's refined actual whole-source domain theorem. They are not deduced by changing62 to54 in the older ledger. Standard bound5251 is retained throughout, even though it does not appear as a numerical exponent in `outer_weight`.

Review-provenance qualification: the current pinned JC proof is SHA256 `0fed4ce72868ffa43f9c8e042055396f441873cca208d40e943b1b60b35f0443`, Git blob `7fdf8d04485681cd9760615cf1994597bc242261` (also verified by a fresh read-only fetch). The JC review's historical handoff table records proof SHA256 `27747cbfbcdcd7a40407cfbf5e4943632de7a72faa125ccf25bb81e0427ecd10`, not this current file. Its prose directly states the domain implication used here, but this bridge does not certify that every later JC source revision received an independent implementation review. Current-definition acceptance remains an explicit external premise. The program itself, unlike that historical-review correspondence, was directly authenticated against e93cf.

## 1. Chart dictionary and the unit relation

For standard tag e, set e_i=(tag>>(3-i))&1 and s=sum e_i. Legal masks use the different convention m_i=(mask>>i)&1. Lines40–50 construct z_i=x_i when e_i=0 and z_i=x_i^-1=t_i when e_i=1, and

    v_j = sum_{|A|=j} product_{i in A,e_i=0} x_i product_{i not in A,e_i=1} t_i.

Thus v_j is the coefficient of u^j in F(u)=product_finite(1+x_i u) product_infinity(t_i+u). The local carrier equations are h_j=v_j^5-product_{a=0}^4 v_a and a=v_0 v_1 v_3 v_4, so v_j^5=h_j+v_2 a.

Lines51–59 construct H_k as the complete homogeneous polynomial in the finite x variables: every nonnegative tuple of total k occurs once. Induction on the number of parts proves `compositions`: select the first part from0..k, then uniquely select the remainder. For no finite variables the code handles the empty tuple separately, giving H_0=1 and H_k=0 for k>0; it never calls `compositions(k,0)`.

Taking coefficient u^s after formal division by product_finite(1+x_i u) gives

    sum_{j=0}^s c_j v_j=1,   c_j=(-1)^(s-j)H_(s-j).

Only coefficients through s are needed; the identity is finite algebra, not an analytic series argument. This proves exactly the `cs` list, including its signs.

## 2. First hit and integer coefficients

Put N=54, M=2N-1=107, T=5M=535, d=s+1 and L=d(T-1)+1. For a nonnegative tuple nu=(nu_0,...,nu_s) of total L, define j(nu)=min{i:nu_i>=T}. It exists because if all nu_i<=T-1 their sum is at most d(T-1)=L-1.

The tests at lines23–24 retain exactly nu_j>=T and nu_i<T for i<j. No condition is imposed on later components. Hence the first-hit sets are disjoint and exhaustive. The literal output is

    B_j = sum_{j(nu)=j} [product_{i=0}^s binom(L-sum_{a<i}nu_a,nu_i)]
                         product_i c_i^nu_i product_i v_i^(nu_i-T*[i=j]).

Every exponent is nonnegative. The chained binomial product telescopes in integers to L!/product nu_i!, i.e. the ordinary multinomial coefficient. The code computes each binomial by exact integer recurrence; at step q it is binom(n,q), so the floor division is exact and does not perform inversion in the coefficient ring. This remains an integral polynomial identity under any permitted base change.

Multiplication by v_j^T restores the assigned multinomial terms. Therefore

    sum_j v_j^T B_j = (sum_i c_i v_i)^L = 1.

This is a universal proof of the partition identity, not a physical high-degree expansion. `first_hit` remains hard gated at the production parameters; the proof describes its body conditional on hypothetical admission and exact operations.

## 3. Carrier split: the exact quotient exponents

For each j the pinned definitions are

    Cbar_j = sum_{k=N}^M binom(M,k) h_j^(k-N) v_2^(M-k) a^(M-k),
    Dbar_j = sum_{k=0}^{N-1} binom(M,k) h_j^k v_2^(M-k) a^(M-k-N).

These are exactly lines66–70. The primary branch is `range(N,M+1)`, including both N and M. The auxiliary branch is `range(N)`, including0 and N-1. For that second branch M-k-N>=0 because M=2N-1. The code never invents a primary h_5: carrier5 selects `aux`.

Multiplying Cbar_j by h_j^N and Dbar_j by a^N gives respectively the upper and lower ranges of the binomial expansion of (h_j+v_2 a)^M=v_j^T. Thus the program returns carrier factors

    R_b=h_b^N B_b Cbar_b                   (0<=b<=s),
    R_b=0                                (s<b<=4),
    R_5=a^N sum_{j=0}^s B_j Dbar_j.

The program's outer multiplication by the selected carrier power is after its j-sum, exactly as needed. Consequently sum_{b=0}^5 R_b=1, h_b^N divides each primary R_b, and a^N divides R_5. No v_j is inverted.

When s=4 there are no finite variables. Then c_0,...,c_3=0, c_4=1 and v_4=1. For j<4 every assigned summand contains c_j^nu_j with nu_j>=T>0, so B_j=0. Only primary4 and auxiliary5 survive. More strongly B_4=1: the only surviving tuple has all its mass at4. This justifies the special `[4,5]` alphabet without any actual polynomial computation.

## 4. Legal-line split and support

Set n=29 and m=2n-1=57. For an infinity coordinate t, the code multiplies the following quotient by its indicated clearing factor:

    Q_0=sum_{k=n}^m binom(m,k)t^(2k-n)(1-t^2)^(m-k),       ell_0^n=t^n;
    Q_1=sum_{k=0}^{n-1} binom(m,k)t^(2k)(1-t^2)^(m-k-n),   ell_1^n=(1-t^2)^n.

These are the exact `range(n,ml+1)` and `range(n)` branches at lines80–84. Each exponent is nonnegative. Their products L_0,L_1 split (t^2+(1-t^2))^m=1. L_0 is actually divisible by t^(2n), but the required certified factor is only t^n; we do not alter n. On a finite coordinate the code returns zero for legal bit1 and uses factor1 for bit0.

The complete return is

    rho_(e,b,m)=R_b product_i L_(i,m_i).

It is polynomial on its OWN standard chart, sums to1 over b,m, and has precisely the matching carrier and legal divisibility. Scalars have twist zero. The t=1/x substitutions restrict this scalar function once; there is no extra tau or deck multiplier in `outer_weight`.

The omitted fibers have identically zero weights by the preceding proofs: primary b>s, finite-coordinate mask1, and primaries0..3 at s=4. `potential_owners` retains every other carrier/mask combination and preserves `(30, occurrence, carrier, legal_mask, standard_tag)`. No physical-label merging or nonzero-support inference is used. Pure index cardinalities at s=0,1,2,3,4 are2,6,16,40,32; their product is245760 per staircase and24 times that is5898240. These are algebraic cardinalities only, not enumerated owner tuples, polynomial multiplication counts, or a resource certificate.

## 5. Alternation, fixed weights, and staircase sum

Write k(o)=(-1 if carrier5 else carrier, legal_mask, standard_tag). `sorted_source` sorts the ENTIRE five-owner tuple by k and multiplies by the parity of that sorting permutation. `weighted_assignment` sends the resulting tuple to `source_and_lift(...,stage=2)`, applies L(X)=X13[5,0]+X02[1,3]+X02[4,2], multiplies by that parity, and then multiplies by rho on each ORIGINAL owner in `owners`. It never substitutes the sorted position's standard tag for the original tag and never recomputes a weight on a source face.

This realizes alternating extension of the already fixed increasing-tuple J2 construction, conditional on that construction's denotation. Sorting is not a proof that a nonlinear raw source evaluated in some different historical order gives the same cochain. Such historical identification remains outside scope.

Important boundary: the inspected `interfaces.sorted_source` does not return zero for repeated equal source keys; its parity is always +/-1. Accordingly `if not parity` in this program does not itself enforce general alternating degeneracy. For THIS `_actual_body` path the five staircase tags are strictly increasing and distinct, and standard_tag is part of the key. Therefore all five keys are distinct regardless of repeated physical `(carrier,mask)` labels. No repeated-key branch is needed on this domain. This result must not be advertised as a correct arbitrary repeated-common-vertex evaluator.

`compiler.staircase_records` starts at tag0, sets bit(3-d) in permutation order and records the inversion sign of the permutation of four coordinates. It therefore gives the24 signed top-dimensional paths from0000 to1111, with the convention of regular-cover §2.2. All tags increase. Each target path intersection is the full tensor fourfold overlap.

Let C be the already denoted original-frame J2 cochain and let p_o be the sorting permutation. The scalar accumulated before extraction is exactly

    T = sum_{sigma in S4} sign(sigma)
          sum_{o_j over retained fibers of e_sigma^j}
            [product_{j=0}^4 rho_(e_sigma^j,b_j,m_j)]
            sign(p_o) L(C_(o_{p_o(0)},...,o_{p_o(4)})).

The omitted weights are zero, so this is L(S Pi_rho C) on the top tensor cell. L is constant linear and can pass through these finite scalar sums. There is no additional staircase sign beyond sign(sigma), and no extra J2 minus: its minus belongs inside the accepted HPL recursion.

`_actual_body` completes both sums before `dict(total.terms).get(15,...)`, then calls Laurent coefficient extraction on the resulting whole rational-x expression. No mask projection or Laurent coefficient is requested in the summand. Full-sign extraction is a linear operation, but this code does not use that fact to admit local rational coefficients or discard branches early. Its frozen route30 exponent is(-1,-1,-1,-1); an ID0 terminal weighting change is a separate adapter obligation and does not change this outer sum theorem.

## 6. Regular extension and suffix ownership remain genuine premises

The partition identities alone prove neither actual pole bounds nor regularity of the weighted source. JC's conditional theorem applies only to the SAME complete homogeneous source and accepted frame/contraction/derivative semantics. Its owned bounds for J0,J1,J2,J3 are respectively carrier36/42/48/54, legal20/23/26/29, standard5251. The common powers stay54/29 even though terminal J2 has the smaller48/26 bounds: J3 remains necessary for closure and the comparison.

For each actual occurrence v the clearing is

    D_v=H_v^54 product_i ell_vi^29 Z_(r(v),i)^5251.

The imported whole-source theorem proves a homogeneous cleared numerator with no codimension-one poles; smooth normal (P1)^4 then gives regular extension. This requires complete combined scalar numerators before complementary differentiation, the actual transported current cancellation, homogeneous physical frames, and the classification of all owned poles. A universal binomial identity or a declared numeric bound cannot manufacture these hypotheses.

In Pi every sampled owner receives its OWN rho. Its H/ell clearing cancels against the proved polynomial quotient for the identical full occurrence. Its Z factors are not cancelled by rho; they remain units because the target intersection contains that owner's original standard tag. Equal polynomial values from different owners never license a transfer of denominators or cancellation charges.

In the prism H_rho only inserted prefix owners are weighted. Original suffix owners keep their carrier/legal denominators and tags in the common-cover domain. The assertion of full-standard extension is about the appropriately CLEARED WHOLE prism coefficient, not its uncleared value. A homotopy owner used before a later face deletion remains charged. The proof is stable under restrictions and Čech/End differentials; it is not a license to admit raw Leibniz pieces independently. This program does not compute the prism, so suffix correctness remains the imported JC/regular-cover premise rather than a new executable prism result here.

Together with closed J0–J3 and the constant selector's L d_End=0, the accepted comparison r*A S Pi J-J=D(-H_rho J-r*K Pi J) gives the desired scalar cohomology comparison. The actual source, HPL, selector and field denotations, all required implementation acceptances, and independent arithmetic/live-storage admission are still required. Neither transport metadata acceptance nor this literal partition proof gives permission to run the body.

## Controls and reproducibility

Run `python -B check.py` and `python -BO check.py`. They hash inputs, verify the remote program blob match, parse source ASTs without executing them, check44 literal coefficient/wiring fragments, and reject8 in-memory semantic mutations (range endpoint, overlap, auxiliary exponent, two line exponents, weight-owner loop, mask and first-hit threshold). Separate finite-index checks cover exponent nonnegativity and reconstruction at powers1,2 and54/29. One tiny invented two-letter first-hit example has threshold2,total3 and verifies the four binomial monomials. It has no geometric variables or actual owner objects.

These checks support the displayed source inspection and universal proofs. Fragment checks are not a general Python verifier, and an input hash by itself proves no mathematics. Source bodies and proofs above supply the remaining meaning. No production import, actual owner enumeration, physical model/source/matrix/jet execution, actual polynomial multiplication, production patch application, external write or admission change occurred. Only this local deliverable directory was written.


## Independent public-package qualification

The archived JC review authenticates the historical proof hash 27747cbf..., not the later 0fed4ce7... proof. The two-paragraph difference is included as inert text and independently inspected here; see REVIEW.md. No latest implementation acceptance is inferred. The offline checker recomputes actual Git blob digests, pins the whole manifest, and uses inert source text only. No network authentication occurs during replay.
