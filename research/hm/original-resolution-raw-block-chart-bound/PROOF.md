# All-standard-chart bound for the literal raw connection blocks

## Result

For the exact frozen `raw_engine.PhysicalModel.blocks(o,d)`, every one of its four returned blocks has **owned carrier/legal bound 5/1 on all 16 standard product charts**. The owner is the single occurrence `o` supplied to that call. More precisely, if `H_o` is its homogeneous carrier and `L_(o,d)` its legal section in the differentiated coordinate, then

    H_o^5 L_(o,d) B_(o,d)

is regular in each standard product chart. The product of all four of the owner's legal sections is a harmless weaker certificate. The middle rank-10 block has the stronger carrier bound 2/1, and the two extreme blocks have 0/1. These are sufficient upper bounds, not claims of sharp attained orders.

The same statement holds for the coefficient after the single odd curve factor in coordinate d is stripped, in its correct O(-2) coefficient line. This stronger coefficientwise assertion is proved directly below, without dividing a regular function by a possibly vanishing odd factor.

This discharges the **raw B5/1 premise** in the ownerwise residual/lift proof. It uses the accepted structural contraction, homogeneous primitive clearance, and actual product/root-frame bridge; it does not assume a previous raw-block pole estimate or a successful physical evaluation. The complementary stripped derivative premise of that residual proof remains separate. 

## 1. Exact source and accepted inputs

The inert raw-engine snapshot has SHA256

    c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9

and is the [frozen raw source](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-realization/raw_engine.py). `blocks` is at lines 140–155. Local exact copies and dependency hashes are listed in `source-pins.json`. No new remote source read is claimed.

The accepted dependencies supply these specific facts:

1. The actual space is X=C^4 for C: y^2=x(x^2-1), with N the external product of O_C(O), and N^2=f*O_P4(1). The coefficient morphism is defined by the coefficients v_j of the product of four binary linear factors.
2. On each standard chart A, the homogeneous maps gamma, delta, ev are polynomial; H0,H1,I,P are cleared by their own carrier H to power two. W and eta are cleared by H to power one; L is constant. Their degrees are gamma,delta,ev: +1; H0,H1,eta: -1; W,L: 0; the I columns: (0,1); the P rows: (0,-1). This is all-chart clearance, including the auxiliary v0=0 pole, not merely finite affine clearance.
3. The structural contraction and pivot identities prove

       U0=[gamma | I | H1 W],   Q0=[H0 ; P ; L delta],
       U1=[W | eta],            Q1=[L ; ev],
       U0 Q0=Q0 U0=Id15,        U1 Q1=Q1 U1=Id10.

   These inverse identities follow from the accepted contraction, including A, and do not require new matrix evaluation. They identify the source's Q with the actual inverse split bases. The denominator allocation below does not simplify any product using these inverses.
4. The actual legal root frames are e_0=1, e_1=y/x. For a four-bit mask m, e_m=nu_m e_ref with nu_m=product(y_r/x_r)^(m_r). The old root connection has coefficient alpha_m=(1/2)dlog h_m in the e_m frame, where h_m=product(1-x_r^-2)^(m_r). Its tensor-power coefficient on N^k is k alpha_m.
5. The exact mathematical derivation used by the raw `Mat.D` is V_d. On the finite chart V(x)=y and V(y)=(3x^2-1)/2. On the infinity chart t=1/x, u=y/x^2, u^2=t(1-t^2), and V(t)=-u, V(u)=(3t^2-1)/2. It preserves both local curve coordinate rings. This statement specifies the rational denotation of the source operation; no claim about execution of arbitrary field or jet software follows from the static check.

Items 1–4 are theorem inputs supplied by the accompanying accepted proofs, not numerical historical receipts. In particular we do not assume B5/1 among them.

## 2. What the frozen call actually returns

Let k=(-1,1,3,5), with corresponding ranks (5,15,10,2). The raw source multiplies columns of U0 by

    (nu^-2 repeated 5, 1, nu^-2, nu^2 repeated 8)

and columns of U1 by

    (1 repeated 8, nu^2 repeated 2).

It divides the corresponding rows of Q0,Q1 by those same factors and returns minus the invariant derivative of the scaled U times the scaled Q. Finally it subtracts k alpha_m(V_d) times the identity in each of the four resolution blocks. The extreme moving-basis parts are zero, so their returned values are +alpha_m(V_d)Id5 and -5 alpha_m(V_d)Id2.

The homogeneous column degrees and matched row degrees are:

| U group | multiplicity | column degree d_j | matched Q row | row degree |
|---|---:|---:|---|---:|
| gamma | 5 | 1 | H0 | -1 |
| I column 0 | 1 | 0 | P row 0 | 0 |
| I column 1 | 1 | 1 | P row 1 | -1 |
| H1 W | 8 | -1 | L delta | 1 |
| W | 8 | 0 | L | 0 |
| eta | 2 | -1 | ev | 1 |

Thus every raw column factor is exactly nu^(-2d_j); its matched row factor is nu^(2d_j). In particular the two I columns must be kept distinct in the logarithmic-weight term. There is no derivative of Q in the source operation.

## 3. Exact passage to any standard chart, with the ambient row factor accounted for

For standard infinity subset A, put tau_A=product_(r in A)t_r. The square-line frame is ell_A=tau_A^-1 ell_ref, the coefficient vector is v_A=tau_A v_ref, and the actual legal-to-standard ratio is

    c=c_(m,A)=e_m^2/ell_A=nu_m^2 tau_A.

The accepted root bridge proves these equalities for the specified actual frames; it does not adjoin a square root of tau_A. The degree table gives, column by column and matched row by row,

    U_ref,j=tau_A^(-d_j) U_A,j,
    Q_ref,j=tau_A^( d_j) Q_A,j.

Consequently the frozen scaled columns and rows themselves satisfy the exact identities

    U_source,j=nu^(-2d_j) U_ref,j=c^(-d_j) U_A,j,
    Q_source,j=nu^( 2d_j) Q_ref,j=c^( d_j) Q_A,j.             (1)

These are identities with the source matrices, not a rule that simply replaces nu^2 by c in an unchanged finite expression. They also show U_source is expressed in the actual ambient legal frame e_m^k for the relevant resolution term. On a standard-chart change v_B=lambda v_A and c_B=lambda c_A, both sides of each scaled-column/row identity agree.

There is a separate common ambient row factor if one chooses to express the same split basis in the common rational e_ref frame on N^k. It is

    U_common=nu^k U_source,    Q_common=Q_source nu^-k.

Then the split-connection coefficient changes by

    -(V U_common)Q_common=-(V U_source)Q_source-k Vlog(nu) Id.

The old connection coefficient in that same common frame is

    k alpha_m(V)-k Vlog(nu).

Their difference is therefore exactly

    B=-(V U_source)Q_source-k alpha_m(V) Id.                 (2)

The two ambient-row derivative terms cancel because they arise from the same change of frame. This applies also to the extreme identity split bases. Thus (2) is the actual End-valued difference of connections and the literal raw block, in either comparison. No ambient term is dropped from one connection while retained in the other.

We shall keep the actual e_m frame and use (1) to estimate (2). Although c is a unit on the owner's legal/standard intersection, its rational extension has zeros or poles on legal boundary divisors. The next sections explicitly charge these divisors; unit regularity only on the open would not prove the required clearance.

## 4. Literal Leibniz expansion and all four old-connection terms

Let beta=V_d log c. For each matched column/row, the scalar chain and product rules give

    V_d(c^(-d_j) U_A,j) c^(d_j) Q_A,j
       =(V_d U_A,j)Q_A,j-d_j beta U_A,j Q_A,j.

No matrix relation or cancellation is used in this identity. Summing precisely the source's matched groups yields

    B0= -[(V gamma)H0+(V I0)P0+(V I1)P1+V(H1 W)L delta]
        +beta[gamma H0+I1 P1-H1 W L delta]-alpha_m(V)Id15,   (3)

    B1= -[(V W)L+(V eta)ev]-beta eta ev-3alpha_m(V)Id10.    (4)

Here B0 is the rank-15 resolution block and B1 is the rank-10 block. The signs and coefficients in (3)–(4) come from the column degrees 1,0,1,-1 and 0,-1. The other two returned blocks are as stated in section 2. Each expression contains every derivative and each old-connection subtraction. In particular

    V(H1 W)=(V H1)W+H1(V W)

has both Leibniz branches. We do not replace H1 W L delta, gamma H0, or I1P1 by a simplified projector. The accepted A is used to identify the split inverse, not to reduce this denominator ledger.

## 5. Explicit legal factors, including infinity and stripped coefficients

For a single coordinate let z=y on the finite chart and z=u on the infinity chart. Put h=x^2-1 and s=1-t^2. The local representatives of the owner's legal section are

    finite:   L_0=1,       L_1=xh;
    infinity: L_0=t,       L_1=s.

These are representatives of Y and X(X^2-Y^2), with their actual degrees one and three. The infinity L_1 is s, rather than the untransported rational function x(x^2-1).

The legal-to-square ratio c is a product over coordinates. Its factor in the differentiated coordinate, and the two scalar coefficients needed in (3)–(4), are:

| chart | bit m | c factor | beta/z | alpha_m(V)/z |
|---|---:|---|---|---|
| finite | 0 | 1 | 0 | 0 |
| finite | 1 | h/x | (x^2+1)/(xh) | 1/(xh) |
| infinity | 0 | t | -1/t | 0 |
| infinity | 1 | s | 2t/s | t/s |

For the finite bit-one row, differentiate log(h/x): 2x/h-1/x=(x^2+1)/(xh). At infinity V=-u partial_t on base functions, so Vlog t=-u/t and Vlog s=2tu/s. The old connection is alpha_1=-t dt/s at infinity, hence alpha_1(V)=tu/s. It is not zero in the retained e_1 frame. These elementary scalar identities are written out mathematically, not tested by source or polynomial evaluation.

Multiplying the last two columns by the SAME row's legal section gives respectively

    finite bit0:    (0,0),
    finite bit1:    (x^2+1,1),
    infinity bit0:  (-1,0),
    infinity bit1:  (2t,t).

All are polynomials. Thus beta and alpha have no carrier denominator and at most one power of this owner's legal factor in coordinate d. This proof includes the infinity bit-zero t denominator; it is not removed by saying t is invertible only on the original legal open. No legal factor from another owner is used.

Every primitive coefficient depends only on the base coordinates. Define the polynomial-coordinate derivation

    partial_A,d = partial/partial x_d  on a finite factor,
    partial_A,d = -partial/partial t_d on an infinity factor.

Then V_d U_A=z_d partial_A,d U_A. Equations (3)–(4), together with the table, therefore give an explicit rational base-coefficient matrix b_(o,d) such that B_(o,d)=z_d b_(o,d). Its formula is obtained by replacing V by partial_A,d, beta by beta/z_d, and alpha(V) by alpha(V)/z_d. This is a direct formula for b; it does not infer regularity by dividing a cleared B by z_d at a branch point.

The same table is valid in every four-coordinate product, since V_d kills the other coordinate factors of c. Thus no legal denominator from another coordinate remains in (3)–(4), even if its bit is one. The base-coordinate rings are polynomial; the curve-coordinate rings are free of rank two over them, with bases (1,y) and (1,u). Hence polynomial clearance of b also proves polynomial curve-basis clearance of B.

## 6. Complete owned carrier ledger

On a fixed standard chart write H for the local representative of this owner's homogeneous carrier. If H^n F is polynomial and n>0, then

    partial_A,d F=[H partial_A,d(H^n F)-n(H^n F)partial_A,d H]/H^(n+1).

Thus a derivative increases that positive carrier allowance by at most one. A polynomial remains polynomial. This formula is valid for reducible H, with all divisor multiplicities retained. It requires no evaluation of a primitive numerator. It applies to the homogeneous local coefficients because their H-power clearance is already proved on this entire chart.

The exact terms of (3)–(4) have the following certificates. Entries are carrier/legal allowances at the one owner; the scalar beta and alpha bounds are from section 5.

| literal term | carrier allocation | resulting bound |
|---|---|---|
| (partial gamma)H0 | 0+2 | 2/0 |
| (partial I0)P0 | 3+2 | 5/0 |
| (partial I1)P1 | 3+2 | 5/0 |
| (partial H1)W L delta | 3+1+0+0 | 4/0 |
| H1(partial W)L delta | 2+2+0+0 | 4/0 |
| (beta/z)gamma H0 | 0+0+2 | 2/1 |
| (beta/z)I1 P1 | 0+2+2 | 4/1 |
| (beta/z)H1 W L delta | 0+2+1+0+0 | 3/1 |
| (alpha(V)/z)Id15 | 0 | 0/1 |
| (partial W)L | 2+0 | 2/0 |
| (partial eta)ev | 2+0 | 2/0 |
| (beta/z)eta ev | 0+1+0 | 1/1 |
| 3(alpha(V)/z)Id10 | 0 | 0/1 |
| +(alpha(V)/z)Id5 | 0 | 0/1 |
| -5(alpha(V)/z)Id2 | 0 | 0/1 |

The carrier factor of both I and P is the same owner's H, so their two allowances add in each derivative term: 3+2=5. A maximum across these two factors would be invalid. A maximum across the displayed summands is valid, since the terms are added, not multiplied. The logarithmic terms use carrier at most four and legal at most one; they are not multiplied by the derivative terms.

Taking maxima therefore gives the four returned resolution-block certificates

    rank 5: 0/1,    rank 15: 5/1,    rank 10: 2/1,    rank 2: 0/1.

Multiplying by the one-owner H^5 L_(o,d) produces polynomial coefficients in every standard chart. Multiplying additionally by the other three legal sections preserves regularity and gives the conventional uniform 5/1 certificate. The same conclusion holds for B and for its explicit stripped coefficient b in the appropriate local line frame.

This argument has not used a transition cocycle, inverse-transition cancellation, trace cancellation, curvature identity, raw residual closure, or a numerical primitive product. In particular the polynomiality of gamma, delta, ev is their accepted homogeneous polynomiality; no finite-chart bound is silently substituted at infinity.

## 7. Gluing, ownership, and use in the existing theorem

Equation (1) proves that the scaled source matrices agree on all standard overlaps with the actual legal frame fixed. Equation (2) shows B is a degree-zero End-valued one-form evaluated on the globally regular invariant field. On two standard charts its scalar matrix coefficients agree after coordinate substitution. On switching the differentiated factor from finite to infinity, z_infinity=u=t^2 y, so

    b_infinity=t^-2 b_finite(1/t),

with other coordinates unchanged. This is exactly the coefficient law of the single odd-character summand O(-2) in coordinate d. It is not an extra pole added to the already transported infinity coefficient. The table and homogeneous derivative formula prove clearance directly in that coefficient frame. In other coordinates there is no odd factor or O(-2) contribution from this block.

The clearing factors H and L are global homogeneous sections with their own chart changes. Since their products clear the explicit coefficient on every chart, the result is a regular section of the corresponding cleared line bundle. No unowned standard-chart equation, affine v0 inverse, or absent-owner factor is appended. At O, t has valuation two, not one; the proof uses powers of the named section t and remains valid with this ramification multiplicity.

If blocks from two occurrences later appear in one word, retain both occurrences and multiply their clearing factors, even if their carrier labels or divisors coincide. If two factors genuinely select the same occurrence, add their powers at that occurrence. The single-owner theorem here does not merge equal labels or allow an absent endpoint to pay a legal pole.

The ownerwise residual proof may consequently replace its explicit raw-B5/1 hypothesis by this theorem with the same constants. Its simultaneous assignment of the full residual to the declared sheaf, exact implementation semantics, complementary stripped derivative interpretation, and later HPL/class or obstruction interpretation are not established merely by this block bound. Those remaining obligations are unchanged. No new detector value or algebraicity conclusion is claimed.

## 8. Static and invented controls

`check_block_metadata.py` reads the frozen source only as text/AST, authenticates the dependency snapshots, and checks the exact `Mat.D`, `nu`, `blocks`, dimensions. It never imports those sources or the pinned model. Its remaining calculations use only integer degree, rank, carrier, legal-divisor and frame-exponent metadata. No actual primitive polynomial, source matrix, rational field object, physical source, jet, or detector is constructed or evaluated.

The checker verifies all 16 legal masks, 16 standard charts and four differentiated directions as combinations of the four proven scalar table rows. It verifies their owned legal-denominator exponents, not the scalar identities themselves; the identities are proved in section 5. A formal two-token connection check retains the common ambient derivative in both split and old terms. Active negative controls reject reciprocal-row mismatch, omitted W derivative, wrong old-connection sign, a missing I column multiplier, missing infinity bit-zero denominator, legal-zero clearance, max-instead-of-add for same-owner I/P, and a missing common ambient old-connection term.

Historical checker results are discussed below; no rerun is asserted here. Identical reports are recorded. Hashes identify reviewed bytes and these controls bind the formulas to source syntax; neither substitutes for the all-chart mathematical argument above.
