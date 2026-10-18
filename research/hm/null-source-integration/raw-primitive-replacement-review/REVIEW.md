# BI01 independent analytic-reduction review

## Disposition

**Accept the representative replacement at PR89 commit `4ad480da0031536ed37735953dc945d41cb8609f`, under the explicitly imported actual-model, FD/RS, and corrected JC hypotheses. No blocking mathematical defect found.**

For the same physical transitions, gerbe, ambient jet, character convention, and freshly evaluated increasing source order:

1. `E_p(delta f)=delta B_p(f)` is correct with the stated endpoint sums, transported currents, and positive sign.
2. The complete five-term sources satisfy `R_T-R_raw=delta K`, where `K=B_p(f_q)+B_q(f_p)` and `s_T-s_raw=delta f` separately for each pair.
3. The displayed C0–C3 recurrence gives a regular total-resolution boundary. Its last equation uses bottom injectivity, not an omitted top component.
4. The two individually admitted outer comparisons give the same **global** class and hence the same 32 authenticated weighted Serre tests. No finite projection is applied to an uncertified comparison primitive.

This eliminates the inner N14 solver from a valid alternative mathematical source for those tests. It does not eliminate the baseline, Fk terms, second jets, or raw transgression derivatives; it does not evaluate a test or establish vanishing. A source-faithful raw-s coefficient realization and its execution/resource review remain separate.

Reviewed [BI01 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4ad480da0031536ed37735953dc945d41cb8609f/research/codex-swarm/source-boundary-analysis/PROOF.md).

## 1. Current identity: endpoint sums and row transport

Write `A_i=V_a f_i`, `B_i=V_b f_i`, `L_d=L_d,ij`, and `U_d=g_ij^-1 L_d,jk g_ij`. Differentiating the actual transition identity gives `L_d,ik=L_d+U_d`. With the ordinary row-End differential,

`delta(A_i L_d,ij)=(A_j-A_i)U_d`,

`delta(A_j L_d,ij)=(A_j-A_k)L_d`.

Applying these identities to

`B_p(f)_ij=((B_i+B_j)L_a,ij-(A_i+A_j)L_b,ij)/2`

gives

`delta B_p(f)=((A_k-A_j)L_b-(B_k-B_j)L_a+(B_j-B_i)U_a-(A_j-A_i)U_b)/2`,

which is exactly `E_p(delta f)`. All four terms and both endpoints are required. In particular the last two terms cannot be dropped by treating the transported current as a current in another endpoint frame.

The identity is valid for physical scalar functions on X before deck stripping. Global invariant vector fields commute with restriction and with the scalar Čech differential. For frame-stripped scalar sections the corresponding physical derivative, including its frame correction, must be used; ordinary differentiation of a normalized constant frame would not prove this identity.

The reversal law `L_d,ji=-g_ij L_d,ij g_ij^-1` and the symmetric endpoint sums make B an alternating row-End edge cochain. Determinant one makes the currents and B traceless. The new proof uses the actual first-current cocycle identity; it does not require any source-specific second-jet symmetry.

The independent tests expand this identity using formal scalar/current letters, reject each of the four E-sign mutations, and test noncommuting artificial frames, reversal, and a deliberately wrong transport. These are universal/formal checks, not physical evaluations.

Sources: [BI01 §1](https://github.com/Akilleez-QA/read-em-and-weep/blob/4ad480da0031536ed37735953dc945d41cb8609f/research/codex-swarm/source-boundary-analysis/PROOF.md#1-actual-currents-give-an-explicit-boundary-operator), [pinned E/current definition](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-proof-foundations/direct-scalar-free-pairing-reduction.md#3-exact-derivative-operator).

## 2. Full-source and residual comparison

The source is the complete expression

`R(s)=tf(M0)+F_q k_p,ik+F_p k_q,ik+E_p(s_q)+E_q(s_p)`.

For `s'_r=s_r+delta f_r`, F, the complete gerbe-corrected M0, and both Fk terms stay fixed. Therefore

`R(s')-R(s)=delta[B_p(f_q)+B_q(f_p)]`.

No baseline or Fk term was declared zero. The seven kinetic and three negative gerbe terms remain inside M0 before its trace-free projection. The second-jet contribution remains there too.

Combining this with RS's **positive** boundary `R(s)=tf(M(s))+delta W(s)` gives

`tf(M(s'))-tf(M(s))=delta[K-(delta f_q)k_p-(delta f_p)k_q]`.

Thus equation (5)'s minus signs are correct. Full-sign central scalar H² vanishes by the separate RS argument, so this comparison preserves the complete obstruction class without assuming a pointwise-zero trace. It is not a proof that either representative is itself exact.

The dual identity is also correctly typed: if `E delta_0=delta_1 B`, then `delta_0* E* Lambda=B* delta_1* Lambda`. Its use with a cutoff functional requires the relevant domain. The global argument below avoids extending that functional to an uncertified primitive.

## 3. Why the two actual scalar solutions differ by a scalar coboundary

The raw scalar is the pinned unsymmetrized transgression, including block ranks `(5,15,10,2)`, supertrace signs `(-,+,-,+)`, line weights `(-1,1,3,5)`, both wedge/linear pieces, and the `-15 q_a,ij q_b,ij/8` edge correction. Its known source identity is `delta s_raw=F`. FD supplies `delta(T_N14 F)=F` on the same fresh source ordering. Neither statement is inferred from a manifest hash or from closedness of F alone.

Consequently `t=s_T-s_raw` is a regular scalar 1-cocycle in the relevant pair character. The finite double-cover pushforward has eigensheaf `O(-2,-2,0,0)` (or its complementary permutation). Each negative factor has only H¹; each O(0) factor has only H⁰. Künneth therefore puts the sole harmonic degree at two and gives pair-character H¹=0.

The cover argument needed to turn that cohomology vanishing into an actual Čech primitive is valid:

- A standard chart on Y is affine. An intersection of standard charts is obtained by inverting the appropriate coordinates.
- In such a chart, carrier and legal open conditions are principal nonvanishing conditions on their local polynomial representatives. Intersecting finitely many of them is another principal open, hence affine.
- The product elliptic-cover map `X -> Y` is finite. The preimage of each such affine intersection is affine.
- Scalar eigensheaves and all terms of the bounded locally free End(K) complex are quasi-coherent. Their higher cohomology on these affine intersections vanishes.

Thus the common cover is acyclic for the relevant sheaves, and its Čech H¹ agrees with sheaf H¹. There is a regular pair-character scalar 0-cochain f on this **same common cover** with `t=delta f`. Equivalently, one may take the corresponding character summand using the characteristic-zero deck projector. No refinement-dependent meromorphic primitive or unbounded analytic-function extension is needed.

This is existence of f, not an evaluated f, and it supplies no 54/29/5251 bound for f, B(f), or the resulting total primitive. The boundary formula is constructive **given** f; the procedure does not compute f from s_T and s_raw.

Sources: [BI01 §§3–4](https://github.com/Akilleez-QA/read-em-and-weep/blob/4ad480da0031536ed37735953dc945d41cb8609f/research/codex-swarm/source-boundary-analysis/PROOF.md#3-the-fresh-raw-scalar-is-explicit-and-source-pinned), [actual first-order source](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md), [FD fresh primitive theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/ce8b3eeae7159e2dcb146638789533360a3e32be/research/codex-swarm/source-domain-application/PROOF.md).

## 4. Constructive original-resolution boundary

Let `z=J(R_T)-J(R_raw)` and use `D=delta+(-1)^q d_End`. The primitive components have bidegrees `(1+s,-s)`. Put

`C0=jK`,

`C1=H_0(z0-delta C0)`,

`C2=H_-1(delta C1-z1)`,

`C3=H_-2(z2-delta C2)`.

For the first step, `z0-delta C0` is vertically closed and has zero cohomology projection. The latter uses the actual compatibility `pi_first delta jK=delta_row K`, together with `R_T-R_raw=delta_row K`; it does not follow merely from unrelated pointwise contractions.

The End contraction then gives `d C1=z0-delta C0`. Since d commutes with restrictions and delta, the next arguments are vertically closed, and the negative-degree projection vanishes. Successively:

`delta C0+d C1=z0`,

`delta C1-d C2=z1`,

`delta C2+d C3=z2`.

The remaining `z3-delta C3` has internal degree -3 and is vertically closed by the closedness of z. In this four-term resolution, its vertical differential contains `gamma W`; `H0 gamma=1` therefore forces W=0. This yields the final equation `delta C3=z3`. There is no need for a degree -4 primitive and no omission of the top equation.

All these cochains are regular on common intersections: f, its physical derivatives, K, and the actual local contractions are regular there. Finite algebraic sums/products preserve that regularity, independently of any fixed cutoff.

An independent 8-dimensional graded rational complex with seven varying local contractions verifies all four boundary equations, a nonzero C3, and J3's top closure. It also rejects reversal of the C2 sign. The test executes only the pinned artificial boundary class, isolated by AST, against an independently implemented rational engine and a different invented fixture. It does not instantiate the actual resolution/source factory.

Sources: [BI01 §5](https://github.com/Akilleez-QA/read-em-and-weep/blob/4ad480da0031536ed37735953dc945d41cb8609f/research/codex-swarm/source-boundary-analysis/PROOF.md#5-constructive-resolution-boundary-and-comparison-outside-a-cutoff), [JC original-frame contraction and closure](https://github.com/Akilleez-QA/read-em-and-weep/blob/4ad480da0031536ed37735953dc945d41cb8609f/research/codex-swarm/full-lift-domain/PROOF.md#2-exact-hpl-signs-and-j3-closure).

## 5. Global comparison does not require the primitive's finite cutoff

Each source lift must independently satisfy the accepted outer-domain theorem. Write `z_i=S Pi_out J_i` and use that theorem separately to obtain

`r* A z_i-J_i=D W_i`, for `i=T,raw`.

Subtracting and using the preceding total boundary gives

`r* A(z_T-z_raw)=D(W_T-W_raw+C)`

in the **full regular common-cover total complex**. This does not apply Pi_out to C or K.

The standard and common covers are acyclic for every term of the bounded quasi-coherent End(K) complex, as established above. Their total Čech complexes therefore compute the same global hypercohomology; the refinement pullback r* agrees with the identity through the augmentations and induces an isomorphism. Its injectivity already suffices here. The signed standard/tensor comparison A is a chain equivalence. Hence z_T and z_raw have equal global classes.

This argument does not claim equality in the cohomology of the **cutoff subcomplex**. A new explicit toy countercontrol has two admissible degree-two cycles differing by a full-complex boundary whose primitive lies outside the degree-one cutoff; their cutoff classes differ while their global class and global detector value agree. The test refuses applying its finite projection to that primitive. This isolates exactly the distinction used by BI01.

The corrected JC qualification remains essential: Pi_out weights every sampled owner and extends the whole weighted projection term onto its standard target. H_rho weights only inserted owners; suffix divisors remain in the common-cover domain. Full-standard regularity for a prism concerns its appropriately cleared whole coefficient. BI01 preserves this qualification and does not promote an uncleared prism to a standard-global section.

After original-frame conversion and the single full-sign deck removal, each authenticated constant L is a global sheaf chain map, with the internal -2 conversion tau^-4 performed first. It maps the equal classes to equal scalar H⁴ classes in O(-4,-4,-4,-4). The selected Serre coordinates detect exponents `{-3,-2,-1}^4`; a regular scalar boundary has an A-face exponent at least zero or a B-face exponent at most -4 in one factor, so these coordinates annihilate **all regular scalar boundaries**, with no common primitive cutoff required. Every degree-at-most-two weighted Serre test is a linear combination of these coordinates.

Thus all twenty selected L maps and the thirty-two authenticated weighted tests agree globally. No rank-completeness theorem is necessary for this equality, and no test value is computed.

Sources: [corrected JC domain and scalar comparison](https://github.com/Akilleez-QA/read-em-and-weep/blob/4ad480da0031536ed37735953dc945d41cb8609f/research/codex-swarm/full-lift-domain/PROOF.md#5-whole-standard-extension-including-every-prismrestriction), [uniform scalar-family transport §§2–5](https://github.com/Akilleez-QA/read-em-and-weep/blob/43193bc8badf3f29a1363132135d956cc12d46ad/research/hm/null-source-integration/scalar-family-transport/PROOF.md).

## 6. Raw-source domain and prospective reduction

The raw scalar is defined on its original carrier/legal edge opens by the actual physical split bases and transported old connections. It introduces no inner inserted owner and no extra standard-chart pole from a partition/Laurent homotopy. The actual homogeneous first-order source theorem supplies carrier14/legal1, not merely a finite-chart affine estimate. A complementary physical derivative gives 15/2 with the associated character-frame change retained.

Using the same accepted current identity and source ledger, E(s_raw) and Fk have bounds 24/7; the unchanged full baseline is bounded by 32/18. Inclusion adds 4/2 and each End homotopy adds 6/3. Hence the complete raw lift fits 54/29 with additional standard-boundary exponent zero. Its own whole-coefficient extension proof follows the same homogeneous owned-divisor/normality argument as JC, with no extra Z denominator. This statement imports the actual homogeneous primitive/raw-s bounds; a JSON table alone would not establish it.

The resulting conservative metadata arithmetic checks:

- J2 numerator degree: `5*(54*5+29*3)-4=1781`.
- J3 numerator degree: `6*(54*5+29*3)-5=2137`.
- With the imported quotient bounds 6677/2006 and owner reversal 357, the J2 rectangle is `[-11815,35166]^4`; the at-most-six-owner full-lift rectangle is `[-14178,42199]^4`.

These are enclosures, not occupied supports, enumerations, costs, or memory bounds. The six-owner statement does not cover the seven-owner delta-J3 boundary. The existing compiler still contains the N14 solver; BI01's denotation is a replacement target for future source-faithful implementation, not an executable rewrite of that compiler.

## 7. Authentication, controls, and remaining scope

Verified all **15 immutable dependency records plus 3 workspace dependency records**, including byte lengths, SHA-256, and Git blobs where specified. Workspace dependencies were read at the reviewed PR89 commit, so they are immutable in this review. All **13 producer files** match the anchored ready marker, SHA-256 `aa0e81b32699e15c3c95fc6792b3cdcec763fd5b12f074b169f8da908ebc6a65`.

The new independent suite has **12 passing tests in normal mode and 12 under -O**. It includes universal current signs, noncommuting artificial transport, full-source/sign bookkeeping, scalar harmonic degree accounting, the complete total-boundary recurrence, the global-vs-cutoff countercontrol, scalar boundary annihilation, source recipe retention, and analytic bounds. A preliminary reviewer-engine run used Python's floating result for a negative exponent of -1; the reviewer engine was corrected to exact integer parity before the final runs. No producer code was changed.

The algebraic acyclic-cover/hypercohomology proof is the mathematical reasoning above, not an inference from finite matrix tests. The tests do not re-prove actual contraction identities, determinant one, physical-frame/raw-s pole bounds, or previously accepted FD/RS/JC semantics. Those are explicit imported premises.

No actual source polynomial operation, coefficient, jet, residual, fiber enumeration, detector evaluation, old checker replay, source graph compilation, or physical factory execution occurred. Producer build/control scripts were read and authenticated, not run. There were no repository modifications, commits, pushes, or external posts.

Still required before arithmetic: a complete cleared raw-s/complementary-derivative coefficient program tied to these physical homogeneous definitions, exact outer coefficient/fiber realization, and aggregate resource/admission review. Source-specific J-transpose-S-H symmetry, cancellation of the surviving second jets, and the global obstruction value are not proved. The mathematical removal of the inner N14 solver is valid without any of those stronger claims.

## Public replay

Required publication files: this report and `test_bi01_independent.py`. Recommended evidence: the two logs, receipt, and SHA256SUMS. No unpublished source directory is needed.

`python -B test_bi01_independent.py --repo /path/to/read-em-and-weep`

`python -BO test_bi01_independent.py --repo /path/to/read-em-and-weep`

The script uses read-only git show of the reviewed PR89 and the exact commits in its authenticated source manifest. It does not fetch or alter the checkout. The object store must contain PR89 `4ad480da0031536ed37735953dc945d41cb8609f` and dependency commits `08b73637d4136f91606aad332c46cafd064417f8`, `10810ee877fdaf291399198ad60d7dd0c316a42d`, `5df68750f766b18a746e50bff662b09829225ab1`, `43193bc8badf3f29a1363132135d956cc12d46ad`, and `ce8b3eeae7159e2dcb146638789533360a3e32be`.

The recorded executions used `--snapshot sources` against the GitHub-retrieved byte-authenticated snapshot. A complete checkout was not available here; the logs do not claim to exercise the Git transport. Both input modes feed the same tests. Only the pinned artificial `boundary.py` and the isolated `TinyBoundaryPrimitive` class execute; the latter uses the reviewer's independent rational engine and fixture. All remaining producer/dependency content is read as bytes, JSON, or AST.
