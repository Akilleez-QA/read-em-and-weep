# Structural first retraction and the exact remaining primitive defect

## Result and boundary

For every one of the six pinned carriers, independently of primitive A and of any historical execution receipt,

    H0_i gamma = Id5.

The proof identifies H0_i with the coordinate-supported inverse of a sparse five-by-five gamma minor. Five carriers are the same four-cycle elimination problem plus one forced coordinate; the auxiliary carrier is triangular. Literal support and selected diagonal records further give

    H0_i I_i=0, H0_i H1_i=0, P_i I_i=Id2, P_i H1_i=0.

This is a new proof of these individual identities, NOT a proof of

    A_i: gamma H0_i + I_i P_i + H1_i delta = Id15.

An exact block normal form below reduces the remaining A_i obligation to four explicitly identified smaller families. None of those remaining families is declared zero here. In particular the earlier determinant-one transition theorem remains conditional on A; its contraction consequences are not used anywhere in this proof.

No physical matrix product, actual polynomial expansion, source evaluation, source jet, detector, or production evaluator was run. The formula derivation is symbolic elimination for one abstract sparse linear system. Executable checks compare immutable bytes, supports, signed exponent labels, and literal records only; invented rational controls are clearly separate.

## 1. Source and scalar conventions

The authenticated input is `research/hm/null-operator-compiler/hm-pinned-model.json`, Git blob `fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761`, SHA256 `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`, 16,803 bytes. The same blob was read at current PR79 head `31f5b074f7c212f9bb6498ed2920e0c93cc781a9` on 2026-10-18. Immutable source:

https://github.com/Akilleez-QA/read-em-and-weep/blob/31f5b074f7c212f9bb6498ed2920e0c93cc781a9/research/hm/null-operator-compiler/hm-pinned-model.json

The earlier authenticated source-formula decoder divides stored H0 and H1 numerators by `dh`, I by `di`, and P by `dp`. In every actual chart these three denominator records coincide. No historical output is an input to this proof. The sparse-minor facts used later are reproduced in the included prior proof/review snapshots; only their direct support-derived determinant identities are used, never their A-dependent volume or contraction consequences.

Work over Q(v1,v2,v3,v4), with v0=1, or over the polynomial ring localized at the relevant stored denominator. Indices are zero-based. Subscripts within each five-coordinate block are reduced modulo five. Coordinate inclusions E_F, E_D, E_S retain the specified order; E_F^t is coordinate restriction, not an inner-product assertion.

## 2. The universal four-cycle inverse

Consider five independent labels t,a,b,c,d and D=t(abcd-t^4). In the displayed source-coordinate orders the selected gamma equations are

    y1 = b x3 + t x4,
    y2 = t x1 + c x2,
    y3 = -d x1 - t x3,
    y4 = -t x2 - a x4,
    y5 = t x0.

Thus the sparse matrix is

    G = [ 0  0  0  b  t ]
        [ 0  t  c  0  0 ]
        [ 0 -d  0 -t  0 ]
        [ 0  0 -t  0 -a ]
        [ t  0  0  0  0 ].

If D is a unit, then t and Delta=abcd-t^4 are units. The last equation gives x0=y5/t. For the other four equations, successively express x3 from the third equation, x4 from the first, and x2 from the fourth, then impose the second. The one closing equation is

    Delta x1 = -(act y1 + t^3 y2 + abc y3 + ct^2 y4).

Back-substitution gives the following inverse numerator table, where every entry on the right is divided by D:

    D x0 = (abcd-t^4)y5,
    D x1 = -act^2 y1 - t^4 y2 - abct y3 - ct^3 y4,
    D x2 =  at^3 y1 + abdt y2 + abt^2 y3 + t^4 y4,
    D x3 =  acdt y1 + dt^3 y2 + t^4 y3 + cdt^2 y4,
    D x4 = -t^4 y1 - bdt^2 y2 - bt^3 y3 - bcdt y4.       (1)

This is an elimination proof of the inverse of G. Existence follows by the successive equations and their closing equation, and uniqueness by the same procedure for y=0. It is not a claim obtained by multiplying the stored physical matrices. Equivalently, the support graph consists of one forced pivot and a four-cycle; the two cycle matchings give det G=-D.

## 3. Exact identification of all five primary H0 records

For chart r=0,...,4 use the UNSORTED ordered coordinates

    f_r = ((r+1) mod5, (r+4) mod5,
           5+(r+2) mod5, 5+(r+3) mod5, 10+r),
    q_r = (r, r+1, r+2, r+3, r+4) mod5.

The gamma submatrix with rows f_r and columns q_r is exactly G after relabeling

    (t,a,b,c,d)=(v_r,v_(r+1),v_(r+2),v_(r+3),v_(r+4)).

The stored denominator is exactly

    dh_r = product_(j=0..4) v_j - v_r^5 = D.

All stored H0 columns outside f_r are empty lists. In domain row order q_r and ambient column order f_r, its numerator is exactly the coefficient table (1). This is a literal metadata statement: relabel the five formal labels, erase occurrences of v0=1, count each remaining label's exponent, and compare the signed exponent tuples with the stored records. No entries from one stored polynomial are multiplied with entries from another, no polynomial is evaluated, and no full-I equivariance is assumed.

The static certificate checks all five copies separately. In particular the first row in cyclic domain order has the two-term numerator abcd-t^4 at ambient coordinate 10+r, while all sixteen cycle entries have the stated single signed monomial. This catches the pivot-row factor 1/v_r that a naive cyclic rewrite of the finite chart0 can miss.

Consequently, writing F_r for the same coordinates in increasing order and G_r=E_F^t gamma,

    H0_r = G_r^-1 E_F^t,
    H0_r gamma = Id5.                                (2)

Changing from f_r to sorted F_r merely applies the same column/row permutation to the inverse factors; no sign factor multiplies the linear map (2).

## 4. Auxiliary triangular inverse

For chart5 put a=v1,b=v2,c=v3,d=v4 and

    F_5=(4,7,8,10,11),   dh_5=-a^2 c d.

The selected gamma equations in the ordinary domain order are

    y1=x1+c x2,   y2=-d x1-x3,   y3=-x2-a x4,
    y4=x0,       y5=a x1.

Since dh_5 is invertible, so are a,c,d. Solve in the order x0,x1,x2,x3,x4:

    x0=y4,
    x1=y5/a,
    x2=y1/c-y5/(ac),
    x3=-y2-d y5/a,
    x4=-y1/(ac)-y3/a+y5/(a^2 c).                       (3)

After writing these over the common stored denominator -a^2cd, the nonzero numerator records, in column order F_5, are

    row0: col4 -a^2cd,
    row1: col5 -acd,
    row2: col1 -a^2d, col5 +ad,
    row3: col2 +a^2cd, col5 +acd^2,
    row4: col1 +ad, col3 +acd, col5 -d.

Here col1,...,col5 mean positions within F_5, not ambient indices. These are exactly the stored lists; every other H0 entry is empty. Thus (2) also holds on chart5. The determinant of its selected gamma minor is a^2c, by its unique perfect matching, independently of any contraction premise.

## 5. Immediate literal-support consequences

For each chart use sorted F, and set

    D_r=(r,r+5), r<5;     D_5=(5,14),
    S = increasing complement of F union D in {0,...,14}.

The complete pinned support facts are

    I[F,:]=0,
    H1[F union D,:]=0,
    P[:,S]=0,
    I[D,:]=J,       P[:,D]=J^-1,

where

    J=diag(1,v_r) on primary chart r,
    J=diag(1,-v4/v1^2) on chart5.

The P diagonal statement is checked independently from its stored numerator and denominator records, not inferred from A. For the primary second diagonal its numerator is the denominator divided by v_r, visible as a one-step exponent shift; on chart5 its numerator is +v1^4 v3 and the denominator is -v1^2 v3 v4. The I off-diagonal and P off-diagonal entries at D are literally zero.

Since H0 is supported on F, these facts prove H0I=H0H1=0 directly. Since P is supported on F union D, they prove PI=J^-1 J=Id2 and PH1=0 directly. Also

    gamma H0 is idempotent, im(gamma H0)=im(gamma),
    ker(H0)=ker(E_F^t)=span(E_D,E_S),
    Id-gamma H0 projects onto this coordinate complement.

No equation involving delta is needed for any assertion in Sections 2–5.

## 6. Unconditional coordinate reduction of A

Put the ambient coordinate rows in order (F,D,S), and write

    gamma = (G;B;C),    I = (0;J;K),
    H0=(G^-1,0,0),     H1=(0;0;H),
    P=(P_F,J^-1,0),    delta=(delta_F,delta_D,delta_S).

Let R=gamma H0+IP+H1delta-Id15. This definition is a formal matrix expression, not an evaluated source product. From the proven supports,

    R = [ 0                           0                 0       ]
        [ B G^-1 + J P_F             0                 0       ]
        [ C G^-1 + K P_F + Hdelta_F   K J^-1+Hdelta_D   Hdelta_S-Id8 ].  (4)

Therefore A holds if and only if the FOUR displayed possibly nonzero blocks vanish. They have shapes 2x5,8x5,8x2,8x8: 130 scalar positions, instead of the original 225 positions. This is a block equivalence, not an independence/minimal-generator claim. It does not assert that any one of these four blocks is zero.

In particular the earlier whole 15x15 defect already takes values in ker H0, and the entire first five output rows in this split are removed by a proved identity rather than a historical receipt.

## 7. Split-basis normal form and the next structural obligations

There is a second, useful form that separates quotient normalization from the common complex and the complementary inverse. Define

    N=[gamma | I | E_S].

This is invertible WITHOUT A: in rows (F,D,S), it is lower block triangular with diagonal blocks G,J,Id8. In particular the first block row of N^-1 is H0. Its second block row is

    Q = J^-1 E_D^t (Id-gamma H0),

which is not silently identified with P. That identification is exactly part of the remaining quotient obligation.

Retain the independently proved pivot splitting W,L,eta and literal B (H1 eta=0). They give H1=H1WL, without A. The separately structural C (ev delta=0) also gives delta=WLdelta; C is used below only when identifying the full complex equations, not for the block normal form itself. Define

    T=E_S^t H1 W,       M=Ldelta E_S.

Because the two pivot columns of H1 are literal zero, H1W consists just of its nonpivot columns in the source's cyclic order. T therefore requires no physical matrix multiplication to identify from stored records.

The already support-proved minor formulas are

    det M=-v_r^3 dh_r on primary chart r,
    det M=-v3 v4 on chart5.

Both are units on the stated denominator localization. These sparse determinant facts came from one forced block and two matchings (primary), or a unique matching (auxiliary). They were proved directly in the prior determinant package independently of A. Reusing them here does not import that argument's contraction conclusion.

Using H0gamma=Id5, H0I=0, PI=Id2, PE_S=0 and the support of H1, the exact conjugated defect is

    N^-1 R N =
        [ 0             0           0         ]
        [ Pgamma        0           0         ]
        [ T Ldelta gamma  T Ldelta I  T M-Id8 ].         (5)

For example Rgamma=I(Pgamma)+E_S T(Ldelta gamma), while RI=E_S T(Ldelta I). Thus (5) does NOT assume that P is the middle block row of N^-1.

Since M is invertible, TM=Id8 makes T=M^-1 and hence invertible. Therefore A is equivalent, under the already structural B and the proved support data, to the four remaining families

    P gamma=0                 (2x5),
    L delta gamma=0           (8x5),
    L delta I=0               (8x2),
    T M=Id8                   (8x8).                     (6)

C identifies the second and third with delta gamma=0 and delta I=0, respectively. This proof does not import delta gamma=0 from the three-family contraction theorem, since that would be circular.

A natural next small proof is the first family: the support data imply

    Pgamma=0  iff  P_F=-J^-1 B G^-1  iff  P=Q.

It can be attacked through the same sparse inverse recurrence, with only the two additional selected rows B of gamma. The complementary inverse TM=Id8 is a separate eight-dimensional sparse solve. The complex equations must likewise be established independently or supplied by a separately authenticated structural proof. Solving only the quotient family would still not prove full A.

## 8. Evidence classification and remaining boundary

The new mathematical advancement is a source-specific primitive retraction with four support-derived side identities and two exact smaller presentations of the unresolved A defect. It is not merely a general lemma conditional on an unknown inverse: Sections 2–4 and the signed-exponent certificate identify the actual stored inverse on every carrier.

The byte/literal checks establish source binding. The cyclic/triangular elimination proves the inverse theorem. The invented controls test the abstract block reduction and retain countermodels where all newly proved retraction/support identities hold but A fails. These are different kinds of evidence, and none is relabeled as a physical execution receipt.

Full primitive A, the remaining geometric/common-frame premises, legal regular extension where not already supplied by separate work, exact implementation semantics, retained-test values, and the global obstruction are not resolved by this artifact.
