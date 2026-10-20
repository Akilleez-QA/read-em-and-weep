# An independent complementary inverse for all six pinned carriers

## Result and exact scope

For every one of the six pinned carriers, independently of primitive A and every historical execution receipt,

    T_i M_i = Id8,
    T_i = M_i^-1,

where

    M_i = L_i delta E_(S_i),
    T_i = E_(S_i)^t H1_i W_i.

The proof solves one abstract sparse eight-coordinate system by a four-cycle recurrence and four forced equations. A triangular solve handles the auxiliary carrier. An inert signed-exponent certificate identifies the resulting coefficients with **all 900 stored H1 entries**, including the zero entries, on the six carriers. The same certificate checks all 384 selected delta entries and the six stored denominators. This is a source-specific inverse proof, not a conditional appeal to an unspecified inverse.

No physical matrix products, polynomial expansion of actual source expressions, source values, source jets, detectors, production imports, or large computation were performed. No identity involving I is proved here. In particular, this artifact does not prove delta I=0 or full primitive A. It does not reuse the A-dependent contraction or volume conclusions of earlier work.

## 1. Source identity, scalar ring, and coordinate conventions

The input is the previously authenticated inert snapshot of

    research/hm/null-operator-compiler/hm-pinned-model.json
    Git blob: fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761
    SHA256: 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926
    Bytes: 16803

The inherited latest verified PR79 head is `31f5b074f7c212f9bb6498ed2920e0c93cc781a9`. Immutable model link:

https://github.com/Akilleez-QA/read-em-and-weep/blob/31f5b074f7c212f9bb6498ed2920e0c93cc781a9/research/hm/null-operator-compiler/hm-pinned-model.json

The inherited intake also identifies PR1 comment `6249337640`; this package makes no new remote intake claim. Source and decoder bytes were rechecked locally. The inert decoder excerpt, blob `3dfed53a28b53b3c912a097971d89fc547330a5f`, identifies H1 as its stored numerator divided by dh and delta as the stored linear matrix. Its cyclic W and L orders are the ones below. The decoder is read as text, never executed or imported. Exact immutable pins and inherited retrieval provenance are in `source-pins.json`.

Work over Q(v1,v2,v3,v4), v0=1, or the polynomial ring localized at the relevant dh. Ambient and target indices are zero-based. Positions x1,...,x8 and y1,...,y8 in the displayed linear systems are one-based solely for readability. Coordinate inclusions keep the stated order.

For primary carrier r=0,...,4 put

    F_r = sorted{(r+1) mod5, (r+4) mod5,
                 5+(r+2) mod5, 5+(r+3) mod5, 10+r},
    D_r = (r,5+r),
    S_r = increasing complement of F_r union D_r.

For the auxiliary carrier set

    F_5=(4,7,8,10,11), D_5=(5,14),
    S_5=(0,1,2,3,6,9,12,13).

The target pivot is p=r on a primary carrier, p=0 on the auxiliary carrier. The exact cyclic nonpivot order is

    l = ( (p+k) mod5 for k=1,...,4,
          5+(p+k) mod5 for k=1,...,4 ).

L restricts to these target coordinates. Column (h,k) of W is

    e_(5h+(p+k) mod5) - (v_((p+k) mod5)/v_p)e_(5h+p).

The stored H1 pivot columns p,5+p are literal zero, so H1 W is exactly H1 with columns selected in order l. This identification needs no executed matrix multiplication. Moreover every stored H1 row outside S is literal zero.

## 2. Primary sparse system and its unique solution

Temporarily let t,a,b,c,d be independent formal labels and put

    Delta = abcd-t^4,     D=t Delta.

Let s0=(2,3,6,9,11,12,13,14). On primary carrier r, cyclically transport each coordinate within its own five-coordinate block:

    s_r[j] = 5 floor(s0[j]/5) + ((s0[j] mod5)+r) mod5.

This is generally an UNSORTED order on S_r. In the orders l for target coordinates and s_r for ambient coordinates, the actual delta minor is the following sparse system after the substitution

    (t,a,b,c,d)=(v_r,v_(r+1),v_(r+2),v_(r+3),v_(r+4)),

where variable subscripts are reduced modulo five:

    y1 =  t x2 + c x6,
    y2 = -t x5 + d x7,
    y3 = -a x6 + t x8,
    y4 = -t x1 - b x7,
    y5 =  t x7 - b x8,
    y6 = -t x3 + a x8,
    y7 =  t x4 - d x5,
    y8 =  c x5 - t x6.                              (1)

The stored dh is exactly D. On its localization both t and Delta are units. The four cycle equations are y2,y3,y5,y8. Successively write

    x6=(c x5-y8)/t,
    x8=(a x6+y3)/t,
    x7=(b x8+y5)/t.

Inserting these into the remaining cycle equation, t x5=d x7-y2, gives the single closing equation

    Delta x5 = t^3 y2 - bd t y3 - d t^2 y5 + abd y8. (2)

Equation (2) determines x5 uniquely, hence x6,x8,x7 uniquely. The other four equations determine

    x1=-(y4+b x7)/t,
    x2=(y1-c x6)/t,
    x3=(-y6+a x8)/t,
    x4=(y7+d x5)/t.                                 (3)

Conversely, (2) and this sequence satisfy all eight original equations: the equations used for substitution hold by construction, and (2) is exactly the unused cycle equation after reversible multiplication by powers of the unit t. This proves existence and uniqueness over the localization, without any determinant or contraction assumption.

Writing the result over the common denominator D gives the following complete inverse numerator table:

    D x1 = -ab^2c y2 + b^2t^2 y3 - Delta y4
             + bt^3 y5 - ab^2t y8,
    D x2 =  Delta y1 - c^2t^2 y2 + bc^2d y3
             + c^2dt y5 - ct^3 y8,
    D x3 =  a^2ct y2 - at^3 y3 - a^2cd y5
             - Delta y6 + a^2t^2 y8,
    D x4 =  dt^3 y2 - bd^2t y3 - d^2t^2 y5
             + Delta y7 + abd^2 y8,
    D x5 =  t^4 y2 - bdt^2 y3 - dt^3 y5 + abdt y8,
    D x6 =  ct^3 y2 - bcdt y3 - cdt^2 y5 + t^4 y8,
    D x7 =  abct y2 - bt^3 y3 - t^4 y5 + abt^2 y8,
    D x8 =  act^2 y2 - t^4 y3 - acdt y5 + at^3 y8. (4)

These are handwritten consequences of (2)–(3). They are not output from a physical matrix multiplication, symbolic inversion program, or polynomial evaluator. In the four entries involving Delta, the two formal terms are recorded separately for the static metadata comparison.

## 3. Exact binding of all five primary inverses

In row order s_r and column order l, every stored H1 numerator equals exactly the corresponding coefficient in (4). The entire denominator record is D. All entries outside those eight rows and eight columns are empty lists.

The static checker checks this separately on every carrier. Each expected monomial is represented by its sign and a list of inert label names t,a,b,c,d. After cyclic relabeling, occurrences of v0 are erased and occurrences of v1,...,v4 are counted to obtain the exponent key. The sign and exponent tuple must equal the stored record. The checker never multiplies two source cells, combines polynomials, evaluates variables, or assumes equivariance of another stored map.

In particular, all four Delta numerator entries are degree four before v0=1 is applied. They are not dh, whose homogeneous degree is five. Keeping this factor straight is essential on carriers r=1,...,4. The check includes the finite carrier and all four cyclic carriers individually, not only a generic or carrier0 pattern.

Let tilde M be the delta minor in the l,s_r orders and tilde T the H1 nonpivot submatrix in the s_r,l orders. Sections 2–3 identify tilde T with the unique inverse of tilde M. Therefore

    tilde T tilde M=Id8,      tilde M tilde T=Id8.    (5)

To recover the question's increasing ambient order, let R be the permutation matrix satisfying E_(s_r)=E_(S_r)R. Then

    tilde M=M R,      tilde T=R^-1 T.

Thus (5) is equivalent to TM=Id8 in the required coordinates. No orientation sign multiplies an inverse map; the same permutation acts on the two incident coordinate factors.

## 4. Auxiliary triangular system and exact binding

For carrier5 use the already increasing S_5, l=(1,2,3,4,6,7,8,9), and a=v1,b=v2,c=v3,d=v4. Its stored denominator is E=-a^2cd. The selected delta equations are

    y1 = x4 + c x7,
    y2 = -c x1 + d x8,
    y3 = b x1 - d x2 - a x7,
    y4 = c x2 - x3 - b x8,
    y5 = x8,
    y6 = -x5,
    y7 = x6,
    y8 = -x7.                                      (6)

On the E localization the factors a,c,d are units. Solve first

    x8=y5, x5=-y6, x6=y7, x7=-y8,

and then

    x4=y1+c y8,
    x1=(-y2+d y5)/c,
    x2=-b y2/(cd)-y3/d+b y5/c+a y8/d,
    x3=-b y2/d-c y3/d-y4+ac y8/d.                   (7)

The last equation's y5 terms cancel formally because x3=c x2-b y5-y4. All steps are reversible, proving existence and uniqueness. Over the common stored denominator E these formulas give

    E x1 =  a^2d y2 - a^2d^2 y5,
    E x2 =  a^2b y2 + a^2c y3 - a^2bd y5 - a^3c y8,
    E x3 =  a^2bc y2 + a^2c^2 y3 + a^2cd y4 - a^3c^2 y8,
    E x4 = -a^2cd y1 - a^2c^2d y8,
    E x5 =  a^2cd y6,
    E x6 = -a^2cd y7,
    E x7 =  a^2cd y8,
    E x8 = -a^2cd y5.                              (8)

The signed-label checker identifies (6) with every selected delta entry and (8) with all selected H1 numerator entries. It verifies every other H1 entry is empty and the denominator is E. Hence T_5=M_5^-1 and T_5 M_5=Id8, again without primitive A.

## 5. Consequences and remaining boundary

This removes exactly the complementary-inverse family from the previous split-basis normal form of primitive A. In that normal form, with N=[gamma | I | E_S] and under the previously proved retraction/support identities, the defect R=gamma H0+IP+H1delta-Id15 is

    N^-1 R N = [ 0                0             0       ]
               [ Pgamma           0             0       ]
               [ T Ldelta gamma   T Ldelta I    TM-Id8 ].

Our new theorem sets only the bottom-right block to zero and establishes that T is invertible. Together with that earlier normal-form theorem, A is therefore equivalent to the remaining three families

    Pgamma=0,      Ldelta gamma=0,      Ldelta I=0.

This is a compositional consequence, not a claim that those families are proved by this package. In particular neither the stored inclusion nor its delta-cycle identity enters the inverse proof. Independently proved C can identify the latter two families with delta gamma=0 and delta I=0, but C is not needed for Sections 1–4.

The direct sparse-minor values det M=-v_r^3 dh_r (primary) and det M=-v3 v4 (auxiliary) agree with this result. They were previously obtained independently of A; the present solve does not need even those determinant formulas as a premise.

No legal-owner regularity, physical-frame geometry, production arithmetic semantics, retained-test values, detector result, global obstruction is established here. The theorem is a rational/localized equality for the exactly pinned formulas. 

## 6. Check scope and reproducibility

`check_inverse_metadata.py` binds the complete stored H1 data and the selected delta data to the handwritten tables. Its source hash guards are mandatory, and all checks use explicit exceptions, so optimization does not disable them.

`check_negative_controls.py` checks byte drift, primary and auxiliary sign mistakes, wrong exponent labels, zero-support leakage, denominator drift, and coordinate-order mistakes. These are inert in-memory metadata mutations, not altered physical inputs passed to a production calculation.

`check_invented_controls.py` uses an unrelated three-cycle with one forced coordinate, all invented rational constants, plus an unrelated triangular four-coordinate system. It checks the general elimination logic, rejects a sign-drift candidate, and exhibits a singular cycle. It reads no model or source files and never evaluates the actual eight-coordinate source system. These controls support the proof method; they are not evidence that replaces the actual handwritten proof and static source binding.
