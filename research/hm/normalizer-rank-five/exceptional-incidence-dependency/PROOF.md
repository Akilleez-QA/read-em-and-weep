# Universal incidence dependencies and the unique extremal four-plane

## Result and limit

For the universal eight-dimensional clock space and five incidence spaces below, let L be a four-plane containing none of the four repeated-coordinate lines. We prove:

1. The intersection sum is at most six, and equality holds if and only if L=D, the distinct-index four-plane.
2. An intersection sum of five requires either a full repeated-edge cycle dependency or a complete opposite pair of distinct-index directions in the projected intersections.
3. In the cycle case, L intersects R in a hyperplane avoiding every coordinate line. For the actual full-normalizer fixed kernel this forces the four nonzero vectors (I−C/5)r_i to be collinear.

These are general symbolic incidence constraints. They do not exclude residual rank five at M600. In particular we do not compute any of the displayed universal projectors on an exceptional eigenbasis, evaluate an operation or source coefficient, or calculate a selected rank instance. Abstract sharpness examples are not claims of realization by the specified full-normalizer module.

## 1. Arrangement and invariants

Over C let R have basis r1,r2,r3,r4 and D have basis t1,t2,t3,t4. Put U=R⊕D and

    P1=span(r1,r3), P2=span(r2,r1),
    P3=span(r3,r4), P4=span(r4,r2),
    Hj=Pj⊕C tj  (j=1,2,3,4),
    H0=span(t1+t4,t2+t3).

These are precisely the universal spaces in ../heisenberg-universal-rank-four/PROOF.md, Section 3. Let L⊂U have dimension four, with L∩C ri=0 for all i. Write S_j=L∩H_j, h=dim S_0, and

    epsilon_j=dim(S_j∩R),
    delta_j=dim(proj_D S_j),
    e=sum epsilon_j, k=sum delta_j.

Each epsilon_j and delta_j is zero or one: a two-dimensional intersection with P_j would contain coordinate lines, while H_j projects to a line. Set A={j:delta_j=1}. Let p be the number of pairs among {1,4} and {2,3} which are entirely contained in A. Let rho be the dimension of the relation space among the nonzero edge lines S_j∩R.

Every nonzero edge vector has both endpoint coordinates nonzero. The leaf argument on the four-cycle proves that every proper collection of these edge lines is independent. Consequently rho∈{0,1}, and rho=1 requires all four edges. Their span has dimension e−rho.

Define r=dim(L∩R) and d=dim(proj_D L)=4−r. Then

    r ≥ e−rho.                                      (1)

The subspace W_A=span{tj:j∈A} is contained in proj_D L. Also S_0⊂proj_D L. Since

    W_A∩H0=span{t1+t4 if {1,4}⊂A,
                 t2+t3 if {2,3}⊂A},

its dimension is p. Thus

    d ≥ dim(W_A+S_0) ≥ k+h−p.                        (2)

Combining (1) and (2) yields the refined inequality

    I(L):=sum_(j=0)^4 dim(L∩Hj)=e+k+h ≤ 4+rho+p.    (3)

All quantities here are intrinsic incidence data, with no operation map involved.

## 2. Cycle branch is bounded by five

If rho=1, then e=4 and r≥3. The exclusions imply r≤3, because r=4 would give R⊂L. Hence r=3 and d=1. In particular k≤1, so p=0, and (2) gives k+h≤1. Therefore

    rho=1 implies I(L)≤5.

If I(L)=5 in this branch, exactly one of the following holds:

    (k,h)=(0,1), or (k,h)=(1,0).

Thus either the sole extra direction is a line of H0, or precisely one nonzero Hj contributes a distinct-index direction and H0 contributes none. In both cases L∩R is exactly the three-dimensional span of the four dependent edge lines.

## 3. The unique equality case I(L)=6

If I(L)=6, Section 2 excludes rho=1. Equation (3) therefore forces p=2. This implies k=4, hence d=4 and r=0. Thus e=0, and I(L)=6 forces h=2.

Projection identifies L with D, so L is the graph of a linear map A:D→R. Since delta_j=1, the graph vector tj+A(tj) lies in Hj; hence A(tj)∈Pj. Since h=2, H0⊂L, so

    A(t1)+A(t4)=0, A(t2)+A(t3)=0.

But P1∩P4=0 and P2∩P3=0, since the relevant edges have disjoint endpoint sets. Therefore every A(tj)=0 and L=D.

Conversely L=D avoids all coordinate repeated lines and has intersections of dimensions (2,1,1,1,1), totaling six. This proves the equality characterization and the bound: when rho=0 equation (3) gives I≤6, while rho=1 gives I≤5.

For the universal residual-rank formula rank Q=10−I(L), residual rank four therefore requires exactly L=D. This is a conditional representation-incidence statement, not an evaluation of the actual kernel.

## 4. Rank-five dependency disjunction and sharpness

If I(L)=5, equation (3) gives rho+p≥1. Therefore either:

- rho=1: all four repeated-edge lines occur and have one dependency; or
- p≥1: the projected S_j contain both t1 and t4, or both t2 and t3.

In the second alternative there are fixed-kernel candidates v_j=tj+a_j∈L∩Hj with a_j∈Pj for each member of a complete pair. Mere presence of these two projected directions does not assert that their sum lies in L∩H0.

Both branches of this necessary disjunction occur for abstract four-planes satisfying all four repeated-coordinate exclusions:

Cycle example: let R0={sum x_i r_i:sum x_i=0} and L=R0⊕C(t1+t4). Then each S_j∩R is an edge line; their four lines span R0 and have one relation. Here e=4,k=0,h=1 and I=5.

Noncycle paired example:

    L=span(t1,t4,r1+r2,r3+r4).

Here S1=Ct1, S4=Ct4, S2=C(r1+r2), S3=C(r3+r4), and S0=C(t1+t4). Thus e=2,k=2,h=1,rho=0,p=1 and I=5. No coordinate line lies in L. These examples establish sharpness for the stated arrangement hypotheses only; they are not shown to satisfy the actual full-normalizer fixed-space condition.

## 4A. Complete numerical incidence strata at I=5

The following list is exhaustive, and every row occurs abstractly. Entries are (r,e,k,h), where r=dim(L∩R):

    (0,0,3,2), (0,0,4,1),
    (1,1,2,2), (1,1,3,1),
    (2,2,2,1),
    (3,4,0,1), (3,4,1,0).

For r≤2 the cycle indicator is zero, so e≤r, k≤4−r, h≤2, and e+k+h=5. In addition k+h−p≤4−r, with p≤floor(k/2). If r=0 these give exactly the first two rows. If r=1 the candidate e=0 would require k=3,h=2, contradicting k+h−p≤3; hence e=1 and the two displayed possibilities follow. If r=2, e≤1 would require k+h≥4, and k=h=2 gives k+h−p≥3>2; thus e=2. Of k+h=3, (k,h)=(1,2) also violates this inequality, leaving (2,1). If r=3, L∩R is a hyperplane avoiding every coordinate line, so its defining linear functional has four nonzero coefficients. Every edge intersection is then a line, giving e=4 and rho=1; Section 2 applies. The case r=4 is forbidden by the coordinate-line exclusions.

In each noncycle row p≥1. These seven numerical strata cannot be reduced further using only the arrangement hypotheses. Besides the two examples above, representatives are as follows; any graph is taken over all D, and unspecified graph columns are zero.

- (0,0,3,2): graph of A with A(t1)=r1 and A(t4)=−r1. Then H0 is fixed by the graph, delta1=delta2=delta3=1, delta4=0.
- (0,0,4,1): graph of A with A(t1)=A(t2)=r1. All four columns lie in their prescribed Pj, and ker(A|H0) is a line.
- (1,1,2,2): L=H0+Ct1+C(r1+r3). Its projected coordinate directions are exactly t1,t4.
- (1,1,3,1): L=span(t1,t4,t2,r3+r4).
- (2,2,2,1): the noncycle example in Section 4.
- (3,4,0,1): the cycle example in Section 4.
- (3,4,1,0): L=R0+Ct1, with R0 as in Section 4.

Every example has dimension four and avoids each coordinate repeated line. Direct inspection of the displayed independent R and D coordinates verifies the claimed strata; no operation or selected representation instance is involved. This is a sharp classification of numerical incidence data, not a classification of all four-planes up to equivalence and not an assertion that any row survives the actual C/B constraints.

## 5. Consequences for the universal full-normalizer involution

Use the established central class sum C on the universal Schur module and put M=C/5. It is an involution commuting with the full normalizer. On the chosen exceptional-clock eight-space U its positive eigenspace is the actual four-plane L. Set A_minus=I−M. Then

    ker(A_minus|U)=L.

In the cycle branch of rank five, dim(L∩R)=3, hence A_minus|R has one-dimensional image. Repeated-coordinate exclusion says A_minus(r_i)≠0 for each i. Consequently all four images are nonzero and collinear; equivalently

    A_minus(r_i) wedge A_minus(r_j)=0 for every i,j,
    A_minus(r_i)≠0 for every i.                     (4)

Conversely, condition (4) forces dim(L∩R)=3. Write A_minus(r_i)=c_i w with all c_i nonzero. Then L∩R=ker(sum c_i x_i); its intersection with each edge Pj is a line with both endpoint coefficients nonzero. These four edge lines span that hyperplane and have one dependency, so rho=1. Thus (4) exactly detects the cycle branch under the fixed-space and line-exclusion hypotheses, although it alone does not force I=5 rather than I=4.

If any two A_minus(r_i) are independent, rank five must therefore use the paired alternative. In that alternative the complete pair has vectors tj+a_j satisfying

    A_minus(tj+a_j)=0, a_j∈Pj.                    (5)

The Sylow-five corrected operator B also commutes with M. Its four two-dimensional eigenspaces E_a contain fixed lines ell_a, and L=⊕ell_a. Equations (4) or (5) must hold for this specific L, not for an arbitrary four-plane or arbitrary product of lines. No inference that they do hold is made here.

Residual rank four, separately, would require M to fix D pointwise, by Section 3. A single universal proof that D is not pointwise fixed would exclude that equality case, but none is supplied or assumed.

## Evidence boundary and remaining step

The result improves the universal incidence classification and makes the cycle alternative an exact projector-collinearity condition. To eliminate rank five one still needs a general representation identity ruling out both the collinearity branch and the paired fixed-vector branch (or controlling their intersection sum). Evaluating these conditions on the selected exceptional kernel would be a pointwise route and was not undertaken. Only static proof reads, formal finite-dimensional linear algebra, and local artifact writes were used.

Dependencies: ../heisenberg-universal-rank-four/PROOF.md; ../exceptional-sylow-kernel-constraint/PROOF.md and AUDIT.md; ../../rank-four/full-normalizer-pure-t-nonvanishing/PROOF.md and AUDIT.md. Independent audit is recorded separately in AUDIT.md.
