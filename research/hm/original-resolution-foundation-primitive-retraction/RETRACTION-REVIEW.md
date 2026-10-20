# Independent review: sparse left retractions on all six HM carriers

## Verdict and boundary

The stored maps satisfy

    H0_i gamma = Id5,   i=0,...,5,

by a new, source-bound sparse inverse argument. Primitive A, the historical contraction receipt, determinant normalization, and any previously claimed execution success are not premises. The five primary inverses follow by solving one four-cycle; the auxiliary inverse follows by triangular substitution. Exact source-label comparison identifies these inverses with the stored H0 numerators and denominators.

Literal supports additionally prove H0_i I_i=0, H0_i H1_i=0, P_i I_i=Id2, and P_i H1_i=0. These are mathematical consequences of the inspected supports and reciprocal diagonal records, without computing source matrix products. They do not establish A.

The remaining A equation admits a precise 5+2+8 block normal form with 130 potentially nonzero scalar slots per carrier, instead of 225. This is a presentation of the remaining equations, not a claim that those equations hold or are algebraically independent. Independently proving the first complex identity would remove 40 further slots, but that identity must not be imported from A.

The final producer PROOF.md, SHA256 `c4ac035e0a50bcb449e0ee151910c1ffa3bda9b297e38d95dd63ab5e8ea84841`, was independently checked, including Sections 6–7. Both residual formulas and their equivalence statements are accepted. No correction remains outstanding. See `retraction-review-pins.json` for the reviewed version.

## Source binding and independent method

The inert model is `inputs/hm-pinned-model.json.txt`, exactly 16,803 bytes:

- SHA256: `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`
- Git blob: `fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761`
- Current immutable source: https://github.com/Akilleez-QA/read-em-and-weep/blob/31f5b074f7c212f9bb6498ed2920e0c93cc781a9/research/hm/null-operator-compiler/hm-pinned-model.json

The producer independently fetched that current-head URL and reported the identical blob and byte count. The reviewer independently recomputed both hashes of the local bytes. The preceding determinant package authenticated the same blob at `48b4ae6d9ccf4a8f12ef54f7514f0ec8f4a1d4ba`; the newer commit does not change the reviewed model bytes. Current branch status and geometric-owner regularity are outside this review.

The decoder convention is H0=N0/dh, H1=N1/dh, I=NI/di, P=NP/dp; the copied `inputs/source-formulas.js.txt` explicitly reads those pairs. This review uses only that denotation, not the production implementation or an execution receipt. Work takes place over Q(v1,v2,v3,v4), with v0=1, or over the stated denominator localizations.

The companion `check_retraction_metadata.py` checks immutable bytes, dimensions, ordered sparse gamma patterns, all 150 selected H0 inverse-label slots, all off-support zeros, and the inclusion/projection diagonal labels. Its only arithmetic on actual source-related data counts factor names to form expected exponent labels and compares those labels. It contains no polynomial multiplication, expansion, cancellation, rational evaluator, matrix product, inverse routine, source specialization, or jet evaluator. The inverse formulas below were derived independently by ordinary symbolic recurrence before being transcribed as expected labels.

Normal and `python -O` runs pass with identical logs and certificates. One-byte source drift is rejected in both modes. Deliberately reversing one primary inverse coefficient sign or one auxiliary inverse coefficient sign is also rejected. These negative controls test the static binding; they are not physical model evaluations.

## 1. Five primary inverses by a single cycle

For carrier k in {0,...,4}, use the ordered coordinate list

    f=(k+1,k+4,5+k+2,5+k+3,10+k),

where each index inside a five-coordinate block is reduced modulo 5. The domain order is (k,k+1,k+2,k+3,k+4), modulo 5. Put

    t=v_k, a=v_(k+1), b=v_(k+2), c=v_(k+3), d=v_(k+4),
    Delta=abcd-t^4,  dh=t Delta.

Direct source-label inspection identifies the selected gamma block in those orders as

    G = [ 0   0   0   b   t ]
        [ 0   t   c   0   0 ]
        [ 0  -d   0  -t   0 ]
        [ 0   0  -t   0  -a ]
        [ t   0   0   0   0 ].

Write Gx=y, with x=(x0,...,x4) and y=(y1,...,y5). Its equations are

    b x3+t x4=y1,    t x1+c x2=y2,
    -d x1-t x3=y3,  -t x2-a x4=y4,  t x0=y5.

On the stored localization dh is a unit. Since dh=t Delta in a commutative ring, both t and Delta are units. Solve the third, first, and fourth equations successively for x3, x4, x2 in terms of x1. The second equation then closes the cycle and determines x1. This procedure divides only by t and Delta, never by a, b, c, or d individually. The result is

    x0=y5/t,
    Delta x1=-(act y1+t^3 y2+abc y3+ct^2 y4),
    Delta x2= at^2 y1+abd y2+abt y3+t^3 y4,
    Delta x3= acd y1+dt^2 y2+t^3 y3+cdt y4,
    Delta x4=-(t^3 y1+bdt y2+bt^2 y3+bcd y4).

These formulas solve the equations uniquely for every y, so they give G inverse without assuming any other primitive identity.

To compare with the literal denominator dh=t Delta, the numerator of x0 is Delta y5. Every other displayed row numerator acquires a factor t. This is a statement about the handwritten formula; the checker merely compares its signed factor-label multisets with stored exponent records. In exact cyclic order those numerator coefficient rows are

    [0,0,0,0,abcd-t^4],
    [-act^2,-t^4,-abct,-ct^3,0],
    [at^3,abdt,abt^2,t^4,0],
    [acdt,dt^3,t^4,cdt^2,0],
    [-t^4,-bdt^2,-bt^3,-bcdt,0].

All these records agree with the source after the two explicit cyclic coordinate permutations. No determinant sign is at issue in this inverse comparison: both the row and domain orders are retained, and the checker checks each slot in its actual source position.

Let E_f^t select the five coordinates in the displayed order. All other H0 columns are literal zero. Therefore the source map is exactly G inverse followed by E_f^t, with the output domain order restored. Since E_f^t gamma=G, this proves H0 gamma=Id5 on all five primary carrier localizations.

## 2. Auxiliary inverse by triangular substitution

For carrier 5, retain the ambient coordinate order f=(4,7,8,10,11) and the ordinary domain order. Put a=v1, c=v3, d=v4. The selected gamma block is

    G = [ 0   1   c   0   0 ]
        [ 0  -d   0  -1   0 ]
        [ 0   0  -1   0  -a ]
        [ 1   0   0   0   0 ]
        [ 0   a   0   0   0 ].

The source denominator is dh=-a^2 c d. Inverting dh makes a, c, and d units. Solving in the order x0,x1,x2,x3,x4 gives

    x0=y4,
    x1=y5/a,
    x2=y1/c-y5/(ac),
    x3=-y2-d y5/a,
    x4=-y3/a-y1/(ac)+y5/(a^2 c).

With the stored common denominator dh, the five numerator rows are

    [0,0,0,-a^2 c d,0],
    [0,0,0,0,-acd],
    [-a^2 d,0,0,0,ad],
    [0,a^2 c d,0,0,acd^2],
    [ad,0,acd,0,-d].

Again every signed exponent label agrees literally with the stored record, and every off-f H0 column is zero. Thus H0_5 gamma=Id5. The extra denominator factor d in the stored expression causes no new inversion issue, because it is already a unit on this carrier localization.

## 3. Further support consequences, independent of A

Let F be f sorted, let D=(k,k+5) for the primary carrier k and D=(5,14) for the auxiliary, and let S be the increasing complement of F union D. The source arrays have

    I_F=0,  (H1)_(F union D)=0,  P_S=0.

The selected diagonal blocks are

    J:=I_D=diag(1,v_k),  P_D=diag(1,1/v_k)       for k=0,...,4,
    J:=I_D=diag(1,-v4/v1^2), P_D=diag(1,-v1^2/v4) for k=5.

The checker establishes these interpretations using denominator labels and their signed exponent shifts. In particular it does not evaluate I_D P_D as a source product.

H0 only sees F, so I_F=0 and H1_F=0 prove H0 I=0 and H0 H1=0. Since P sees only F union D, while H1 vanishes on those rows, P H1=0. Since I_F=0, P_S=0, and P_D=J inverse, the two columns of I have P-coordinate exactly Id2. Thus PI=Id2.

None of these facts proves P gamma=0 or either complex identity. An invented rank-(1,3,2,1) example shows the distinction: take gamma=e1, H0=e1 transpose, I=e2, P=e2 transpose, H1=0, delta with rows e3 transpose and 0, and ev=(0,1). The displayed retraction, support, and PI identities hold, but gamma H0+IP+H1 delta is diag(1,1,0), so A fails. This is an abstract counterexample, not a physical source specialization.

## 4. Exact residual normal form and remaining work

Set E_S to the ordered coordinate inclusion and put

    N=[gamma | I | E_S].

After ordering ambient rows as (F,D,S), N is block lower triangular with diagonal blocks G, J, Id8. Consequently N is invertible on the actual carrier localization, with no use of A. Define the A defect using the following fixed sign:

    R=gamma H0+IP+H1 delta-Id15.

The support consequences above give directly

    R gamma=I(P gamma)+H1(delta gamma),
    R I=H1(delta I),
    R E_S=H1(delta E_S)-E_S.

Write H1=E_S H. The pivot construction provides W,L,eta with WL+eta ev=Id10. The two evaluation-pivot columns of H1 are literal zero, so H1 eta=0. Hence H1=H1 W L. Define

    T=H W,       M=L delta E_S.

Because H1 vanishes on pivot columns and W is a coordinate inclusion plus pivot-coordinate corrections, T is just H with the eight nonpivot columns selected in L order. No matrix multiplication is necessary to identify its literal records.

Taking coordinates in N gives the exact normal form

    N inverse R N =
       [ 0             0             0       ]
       [ P gamma       0             0       ]
       [ T L delta gamma  T L delta I  TM-Id8 ].

This identity does not require C=ev delta=0: H1 eta=0 alone justifies the L insertion. C is needed if one wants to interpret L delta gamma=0 and L delta I=0 as the full complex/cycle identities.

The earlier sparse determinant proof, whose selected delta minor calculation itself does not assume A, gives

    det M=-v_k^3 dh_k   for the five primary carriers,
    det M=-v3 v4       for the auxiliary carrier.

These are units on the same localizations. Thus M is invertible independently of A. If TM=Id8 holds, then T=M inverse is invertible too. It follows that A is equivalent to the four remaining blocks

    P gamma=0           (2 by 5),
    L delta gamma=0     (8 by 5),
    L delta I=0         (8 by 2),
    TM=Id8              (8 by 8).

There are 10+40+16+64=130 displayed scalar slots. This count expresses matrix block sizes, not algebraic independence or a minimum generating set. The final obligation can instead be phrased as identifying the literal T records with the inverse of the already sparse M. If delta gamma=0 is supplied by a separate noncircular proof, the 8-by-5 block disappears and 90 slots remain. If delta I=0 is independently supplied too, only the 2-by-5 and 8-by-8 blocks remain. Neither premise is certified by this review.

The normal form sharply locates the remaining work but must not be reported as proving the contraction, as proving the larger determinant theorem unconditionally, or as granting physical-source execution. No physical source, detector, residual, owner, or jet was evaluated. Geometric regularity and the global obstruction remain separate obligations.

## Reproduction

From this directory:

    python check_retraction_metadata.py
    python -O check_retraction_metadata.py
    python check_retraction_negative_controls.py

Both must report PASS and emit `retraction-metadata-certificate.json`. The retained logs are `retraction-normal.log`, `retraction-optimized.log`, and `retraction-negative-controls.log`. Source drift is rejected before metadata is interpreted. A PASS establishes only the source identity and metadata correspondences claimed by the checker; the recurrence proof and block argument above supply their mathematical meaning.
