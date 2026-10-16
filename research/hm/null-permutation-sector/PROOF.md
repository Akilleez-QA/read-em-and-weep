# Rational permutation-sector split after the nonzero Omega certificate

## Result and scope

Over Q, the authenticated 32-dimensional D8 permutation-sign sector splits under the full alternating projector into a 2-dimensional image and a 30-dimensional kernel. The 2-dimensional image is the full S4 sign-isotypic part. The 30-dimensional kernel consists of the D8-sign lines in thirty copies of the S4 representation (2,2). The D8 sector itself is not S4-stable, so this is a projector decomposition of that sector, not a claim that its 30-dimensional kernel is an S4 subrepresentation.

The highest mixed-second-jet symbol Omega cancels pointwise in the full alternating combination of the three pair partitions. This does not make the complete obstruction's alternating projection zero: terms linear in second jets, other lower terms, scalar terms and gerbe terms still require comparison. It supplies a sharper division of the remaining global work after actual pointwise Omega=0 was refuted.

## 1. Published premises

Use the pinned complex on P4, B=End(L), the genuine factor-permutation action, finite-flat rho:(P1)^4 -> P4, and the characteristic-independent small twist ranks from:

https://github.com/Akilleez-QA/read-em-and-weep/blob/f968b53943ba2312f09fbc3e8f9d462e86bcaa34/research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md

The input dimensions are h2(B)=2, h2(B(-1))=10, h2(B(-2))=20, h2(B(-3))=20. The finite direct image has graded free-generator dimensions (1,11,11,1). Over Q the same graded splitting can be chosen S4-equivariant by averaging over all24 elements; this argument is not asserted in characteristic3. The coefficient complex on P4 is permutation-trivial because its variables are elementary-symmetric coefficients.

The full-sign deck line uses the ordinary product linearization, whereas the canonical bundle adds the sign from wedging four differentials. Therefore the genuine full-sign H2 representation is the dual of H2(Y,rho*B), tensored with S4 sign. These premises are exactly the published geometric action, not a naive action on an ordered/pruned finite-model basis.

## 2. Recover the full S4 representation by integer characters

For g in S4 with c cycles, the actual monomial permutation basis in degree n has trace (n+1)^c. Since the five polynomial generators on P4 are S4-trivial, the graded free-generator characters are the coefficients of (1-t)^5 times this Hilbert-character series. In degrees0 through3 they are

    W0: 1,
    W1: 2^c-5,
    W2: 3^c-5*2^c+10,
    W3: 4^c-5*3^c+10*2^c-10.

Write V for the usual 3-dimensional standard representation and U for the 2-dimensional representation indexed by (2,2). Direct character comparison on the five conjugacy classes gives

    W0=1, W1=3V+U, W2=3(V tensor sign)+U, W3=sign.

Projection formula and the four h2 inputs yield

    H2(Y,rho*B)=2*1+30V+30U+60(V tensor sign)+20sign.

Duality and the canonical sign then give

    H2(full-sign End)=20*1+60V+30U+30(V tensor sign)+2sign.  (1)

Its character on classes (1^4),(2,1,1),(2,2),(3,1),(4) is

    (352,48,-8,-8,-12).

The dimensions sum to352, as required by the separate full-model certificate. This calculation uses no new matrix rank or source coefficient computation.

## 3. The 32-dimensional target separates into 2 and30

Let D8 stabilize the pair partition (01)|(23), and epsilon=sign restricted to D8. It contains one identity, two transpositions, three double transpositions and two four-cycles. The epsilon multiplicities of (1,V,U,V tensor sign,sign) are respectively

    (0,0,1,0,1).

Thus (1) recovers dimension30+2=32. The full alternating idempotent e_sign=(1/24)sum_g sign(g)g has rank2 on this target and kernel30. Both projections are defined over Q.

For a class R already in the genuine D8 epsilon sector, take coset representatives identity, (12), and (132), with coordinates labeled0,1,2,3, the latter cycles acting on1,2,3, and the convention rho(g)V_i=V_g(i). Naturality identifies their images with R_(01,23), R_(02,13), R_(03,12). Therefore

    e_sign R = (R_(01,23)-R_(02,13)+R_(03,12))/3.          (2)

This is an equality of cohomology classes with the authenticated geometric permutation action. At the cochain level, all first-order gerbe representatives, source order changes, transports and comparison boundaries must be retained. In particular one must not permute only a pruned harmonic row and call it the genuine action.

## 4. Omega cancels in the alternating pair sum

For fixed edge transitions A and B and commuting source derivations, let H_ab=A^-1 V_a V_b A and J_ab=A^-1 B^-1(V_a V_b B)A. These are symmetric in a,b. The symbols for the three partitions are

    8 Omega_(01,23)=[J02,H13]-[J03,H12]-[J12,H03]+[J13,H02],
    8 Omega_(02,13)=[J01,H23]-[J03,H12]-[J12,H03]+[J23,H01],
    8 Omega_(03,12)=[J01,H23]-[J02,H13]-[J13,H02]+[J23,H01].

Every term cancels in the signed combination, giving the exact identity

    Omega_(01,23)-Omega_(02,13)+Omega_(03,12)=0.           (3)

This uses only mixed-derivative symmetry and the four commutator signs, not actual source vanishing or a scalar primitive. It is compatible with the nonzero fixed-source value of the first symbol: the three symbols obey one relation, and their span has the (2,2) pair-partition behavior.

Equation (3) removes this highest symbol from the pointwise alternating combination. It does not say that the remaining Q2/Q4/E terms or the full 2-dimensional global sign projection vanish. Those terms, plus any needed cochain comparison, remain explicit work.

## 5. Operational consequence

There are now two rigorously distinct targets: the fully alternating global projection (at most two coordinates), where the highest Omega symbol cancels formally, and the remaining30 coordinates, where the actual nonzero symbol must be retained. A zero result in only one target would not settle the other. This is not a reduction of the full32 scalar tests to two, nor an authorization for any numerical replay.

The companion check verifies all five characters, their irreducible decomposition, the D8 multiplicities, and the Omega identity on all324 single-slot sl2 basis pairs using independent Fraction matrix multiplication. It uses invented arrays only and does not import the actual source or rerun its specialization.

A source-level cochain implementation of the projector has not been constructed here. The geometric class identity (2) and the same-edge symbol identity (3) are separate verified statements. Any implementation must reconcile the three representatives on one cover/order and retain the resulting comparison terms. No reduction of the admitted whole-source pole ledger, owner traversal, or runtime follows merely from the representation dimensions or symbol cancellation.
