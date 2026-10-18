# BI01: replace the inner scalar solver by the fresh raw primitive

## Result and exact scope

For the SAME actual physical transitions, ambient two-jet, gerbe and fresh source order, the full five-term representative formed with the N14 scalar solution has the same GLOBAL obstruction class as the representative formed with the pinned local transgression scalar. This replacement removes the inner N14 partitions/fibers/standard h from the mathematical source definition needed for a future detector realization. It does not remove any of the five terms, any of the seven kinetic/three gerbe baseline terms, or the second-jet contribution. It computes no physical source value and proves no obstruction vanishing.

The new constructive identity is an explicit source-current primitive for `E_p(delta f)`. The comparison is global sheaf cohomology; it does not pretend that this primitive has the original finite cutoff bound. Both source representatives individually satisfy the admitted outer-domain hypotheses.

## 1. Actual currents give an explicit boundary operator

Use physical derivations V_d, row transitions `g_ik=g_jk g_ij`, and the fixed source-first alternating extension. For p=(a,b) let

    L_d,ij=g_ij^-1 V_d(g_ij),
    U_d,ijk=g_ij^-1 L_d,jk g_ij.

Differentiating the actual transition identity gives

    L_d,ik=L_d,ij+U_d,ijk.

The source operator, including both endpoint terms, is

    E_p(t)_ijk=1/2[(V_a t_jk)L_b,ij-(V_b t_jk)L_a,ij
                         +(V_b t_ij)U_a,ijk-(V_a t_ij)U_b,ijk].

For a scalar vertex0-cochain f define the row-End EDGE cochain

    B_p(f)_ij=1/2[(V_b f_i+V_b f_j)L_a,ij
                          -(V_a f_i+V_a f_j)L_b,ij].                 (1)

Then the exact identity is

    E_p(delta f)=delta B_p(f).                                     (2)

Proof. Put A_i=V_a f_i and B_i=V_b f_i in this paragraph only. For either actual current L_d, its cocycle identity gives

    delta(A_i L_d,ij)=(A_j-A_i)U_d,ijk,
    delta(A_j L_d,ij)=(A_j-A_k)L_d,ij.

Substitute these two identities into(1). The result is

    1/2[(A_k-A_j)L_b-(B_k-B_j)L_a
                     +(B_j-B_i)U_a-(A_j-A_i)U_b],

which is exactly E_p(delta f). There is no commutation of matrix factors or replacement of a physical derivative by a frozen-frame derivative. Scalars commute with the matrices, but U is still transported to the first row frame. Formula(1) is alternating with that row transport. Since the actual determinant-one currents are traceless, B_p(f) is traceless.

The physical E and current definitions are pinned by `direct-scalar-free-pairing-reduction.md` section3 and the current/transition source. Equation(2) therefore applies to this actual source, beyond an abstract unconstrained second-jet ansatz. It uses only the actual first-current cocycle identity, not any unproved J^t S H symmetry.

## 2. Explicit comparison of the COMPLETE source

For scalar solutions s_p,s_q, retain exactly

    R(s)=M0^0+F_q k_p,ik+F_p k_q,ik+E_p(s_q)+E_q(s_p).              (3)

Suppose s'_p=s_p+delta f_p and s'_q=s_q+delta f_q, with F unchanged. The baseline and both Fk terms are unchanged. By(2),

    R(s')-R(s)=delta K,
    K=B_p(f_q)+B_q(f_p).                                         (4)

This is an explicit boundary identity for the full representative. It is not the false assertion that solving the first-order scalar equation makes R exact. The accepted RS identity is

    R(s)=M(s)^0+delta W(s),   W(s)=s_q k_p+s_p k_q.

Consequently the complete tracefree residuals also obey the constructive comparison

    M(s')^0-M(s)^0
       =delta[K-(delta f_q)k_p-(delta f_p)k_q].                   (5)

The sign in(5) follows from RS's POSITIVE boundary sign. Full-sign central scalar H2 vanishes as in RS, so passing to the tracefree representative preserves the complete obstruction class. This is not a pointwise trace-zero assertion. The baseline's three negative gerbe terms were retained before tracefree projection in(3); no new baseline cancellation is used.

For a globally boundary-annihilating detector Lambda, or one whose domain contains B_p(f), equation(2) has the dual consequence

    delta_0^* E_p^* Lambda=B_p^* delta_1^* Lambda=0.                (6)

One cannot use(6) as a direct cutoff computation if B_p(f) is outside that cutoff. The global argument below avoids that unsupported domain promotion.

## 3. The fresh raw scalar is explicit and source pinned

The actual old/split connection construction in `first-order-source.md` at08b73637d4136f91606aad332c46cafd064417f8 supplies the RAW scalar, not an assumed primitive. Its block ranks are(5,15,10,2), supertrace signs(-,+,-,+), and line weights k=(-1,1,3,5). With the SAME physical moving split bases U_i,

    B_i=-(d U_i)U_i^-1-diag(k gamma_i),
    theta_a=q_a,ij/2.

For pair(a,b), the edge scalar is precisely

    s_raw,ij = (1/4) sum_blocks supertrace_sign * [
          tr(B_i,a B_j,b-B_i,b B_j,a)
          +k(theta_a tr(B_i,b+B_j,b)-theta_b tr(B_i,a+B_j,a))]
          -(15/8)q_a,ij q_b,ij.                                 (7)

This is section4's `scalar=sum/4-15*q_a*q_b/8`, derived from its unsymmetrized transgression in sections2–3. Both mixed terms, ordinary-wedge square coefficient-30, the exact edge gerbe representative correction, and row/column trace sign are essential. It gives

    delta s_raw=(15/4)q_a cup q_b-tr(C_p)/2=F_p.                 (8)

All derivatives in(7) are physical moving-frame derivatives; paired deck factors are removed only with the correct character conversion. Old connections are transported at infinity, never reset to zero. `actual-raw-s-denotation.json` records this recipe and its source pins without evaluating a source matrix.

The universal raw identity is evaluated on NEW increasing edges/triples and then extended alternatingly, as established in FD. It is not equality with a historically constructed nonlinear cochain after reordering. Each pair is treated directly. No historical scalar, mask table, old78 detector output or carrier merger value is imported.

The same first-order source and transition-only proof give s_raw owned carrier14/legal1 in homogeneous physical frames, without the EXTRA standard-boundary5250 introduced by the N14 comparison solver. This includes the raw scalar's differential and all restrictions. Thus its complementary derivative has owned15/2. These are actual formula/domain theorems, not inferred from the degree of an arbitrary affine expression.

## 4. H1 vanishing supplies the comparison without evaluating f

Let s_T=T_N14 F be the accepted complete N14 solution and set t=s_T-s_raw for either pair. By FD and(8), delta t=0. Under finite pushforward to Y=(P1)^4, this scalar character is O(-2,-2,0,0), or its complementary permutation. Each O(-2) has only H1, so Kunneth puts its only cohomology in total degree2. In particular H1=0.

The standard/common covers and all finite intersections are affine: a common intersection is a standard product affine chart with the corresponding carrier/legal/coordinate functions inverted. Finite pullback to X preserves affineness. Therefore these Cech complexes compute the scalar sheaf cohomology. There exists a regular scalar0-cochain f on the common cover with

    s_T-s_raw=delta f.

This is an existence proof; no f, partition, fiber, coefficient or jet is evaluated. Applying(4) yields `[R_T]=[R_raw]` in global H2(End E) for the specified fresh ambient problem. It does not imply that either class is zero.

## 5. Constructive resolution boundary and comparison outside a cutoff

The row boundary in(4) also gives an explicit total-resolution comparison, using the SAME local contractions and total differential `D=delta+(-1)^q d_End`. Write DeltaJ=J(R_T)-J(R_raw), and put

    C0=jK,
    C1=H_0(DeltaJ0-delta C0),
    C2=H_-1(delta C1-DeltaJ1),
    C3=H_-2(DeltaJ2-delta C2).                                  (9)

C_s has bidegree(1+s,-s). The contraction identities successively give DC=DeltaJ through internal degree-2. The remaining internal-3 error is vertically closed; bottom injectivity `H0 gamma=1` forces it to vanish. Thus(9) is a regular TOTAL boundary on the full common cover. There is no need to assert that K or C has the original54/29/5251 cutoff bound.

Each representative's lift separately satisfies the JC common domain: J_T by the accepted full inner/whole-source theorem; J_raw by the SAME source-operation ledger using s_raw14/1 and V(s_raw)15/2. Both have the complete baseline and actual homogeneous frames. Raw scalar terms require no inner inserted owners. The resulting raw R has32/18, inclusion adds4/2, and each End H adds6/3, giving J_raw through54/29. Its standard-boundary order is0 beyond those owned divisors, so it may harmlessly be padded to the existing5251 domain for comparison.

Let Pi_out be the same fixed54/29 outer partition. For i=T,raw, the regular comparison gives `r* A S Pi_out J_i-J_i=D W_i`. Pi_out weights ALL sampled owners, so its WHOLE weighted value extends on the full standard target. In H_rho, weights cancel only INSERTED owners; the suffix denominators remain in the common-cover domain and full-standard regularity concerns its appropriately CLEARED WHOLE coefficient. This is the JC clarification, not an assertion that the uncleared prism has global standard regularity.

Subtract these identities and use(9). The pulled-back standard representatives differ by a boundary in the FULL common-cover total complex. Since standard and common acyclic covers compute the SAME global hypercohomology, the pullback r* is an isomorphism on it. Therefore the two standard/tensor representatives have identical global classes, even if the comparison primitive is outside the chosen cutoff. This is not the invalid step 'apply finite Pi to an out-of-domain primitive'.

Applying any authenticated scalar chain map L, AFTER original-frame/deck/tau^-4 conversion, gives equal scalar cohomology classes. Consequently all20 selected maps and all32 weighted Serre tests have the same values on R_T and R_raw. The proof requires no rank-completeness assertion; it proves class equality before the scalar tests. Their common value remains unknown.

## 6. Prospective reduction in the source and exponent enclosures

The raw source is again local to its three actual source owners: s_raw uses the two edge owners in(7). In(3), Fk and both E(s_raw) use only the same triple's actual jets; there are no inner N14 weights, inserted fibers or standard h operations. This is a new realization target, not reuse of an old historical table. The4-block raw scalar and its complementary derivatives still need a source-faithful complete cleared-numerator program before any arithmetic. There is no claim that the raw transgression is free or that its materialization fits a budget.

With no additional standard-boundary factors, the existing outer54/29 theorem gives the conservative J2 cleared degree

    54*25+29*15-4=1781

instead of28036 with5251 per owner. J3 degree is at most `54*30+29*18-5=2137`. Reusing the SAME imported outer quotient bounds6677 finite/2006 infinity and max owned reversal54*5+29*3=357 gives the conservative J2 exponent rectangle[-11815,35166]^4; the at-most6-owner full-lift rectangle is[-14178,42199]^4. Neither rectangle is occupied support or permission to enumerate a box; no six-owner rectangle is asserted for the seven-owner delta J3 boundary. These are analytic metadata bounds only, not operation counts, memory bounds, storage forecasts or execution release.

## 7. What this does not settle

The actual distinct-carrier identities making J^t S H symmetric remain unproved. The second-jet bracket stays in M0^0, and E(s_raw) has actual source-specific second derivatives as well. Eliminating the inner solver does not eliminate those terms or certify their cancellation. The pinned survivor and degeneracy proofs rule out the tempting determinant-one/edgewise-commutativity/universal two-jet-boundary shortcuts, but do not establish an actual HM obstruction value.

The explicit tiny countercomplex in the controls shows why first-order scalar exactness alone does not force a second-order global class to vanish. It is a logical countercontrol, not an actual HM specialization. The useful result here is the proved representative replacement and explicit boundary, with all source/gerbe/frame and global-vs-cutoff distinctions retained.
