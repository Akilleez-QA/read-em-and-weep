# Exact positive Smith profile in the nonzero nine-endpoint branch

## Theorem and precise hypothesis

Retain the conditional actual source2 nonzero pure-V Q-compatible radical
and the nine-dimensional generated endpoint. PR1075 proves that its
remaining scalar gamma is nonzero under these hypotheses. The present
deduction uses that exact theorem, not a numerical coefficient value, and
does not assert source occurrence.

Let M_a(t)=Q+tT_a be the ACTUAL POSITIVE component

    H1(B(2))_+[[t]] → H1(B(4))_+[[t]],
                  41 → 37.

Let Z be the prescribed length34 scheme (six length-four C5 local ideals
and ten reduced C3 points), and E12 the disjoint reduced twelve-point conic
orbit. Put E=Z disjoint-union E12. Its length is46, and its support has28
points in the projective direction plane P(A). For EVERY nonzero direction
with projective class outside supp(E), the formal Smith form over C[[t]] is

    [ diag(1 repeated33 times, t²,t²,t²,t⁴) | 0_(37×4) ].   (1)

The same statement holds over K[[t]] for the symbolic generic direction,
where K=C(P(A)), using a local trivialization of the direction line. Thus

- the positive component has row rank37 over K((t));
- its formal kernel is free of rank4;
- its formal cokernel is (K[[t]]/(t²))^3⊕K[[t]]/(t⁴), length10;
- the ideal of maximal37-minors is exactly (t^10).

For each allowed fixed direction the analogous statements hold over
C((t)) and C[[t]]. All maximal minors have order at least10 and at least
one has order exactly10. This does not mean every maximal minor has that
order or is nonzero.

The original determinant-embedded fourth D row has component ideal sheaf
exactly I_E. This ideal statement is stronger than its support count; it
is not the degeneracy scheme of the lift matrix R. No Smith profile at
points of supp(E) is asserted. No conclusion of full adjoint invertibility,
completion of the original proof repair, or source realization follows.

## 1. Exact original inputs

INPUTS.json authenticates the following published originals:

- PR1019: actual Q rank33, ker Q=A+D, coker Q=P, and nonzero second
  channel B_a(x)=−mu[a²x] on A, zero on D, with mu≠0.
- POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md at
  eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c: the ORIGINAL positive first
  Bockstein vanishes identically, using actual cohomological multiplication.
- ACTUAL-THIRD-BOCKSTEIN-VANISHES-IDENTICALLY.md at
  db51525015bb7c5e825833d550d08dedf6f6ea96: the ORIGINAL third is zero
  in every direction, including additional specialized A-kernel inputs.
  It also records that the second A symbol has rank3 away from precisely
  the six C5 axes, where it has rank2; its maximal-minor scheme Sigma is
  the six length-four ideals, with no other rank-drop support.
- PR1025: the actual equality iota beta4|D=−sL in coker B, with the
  original fourth defined on surviving D and its unique quadratic lift R.
- PR1044: the complete nonic component scheme for every nonzero lift
  coefficient pair; on the R1 line it is exactly E=Z disjoint-union E12.
- PR1046: the determinant-embedded original-fourth row H=FL has the
  SAME projective component ideal sheaf as F, including the C3 rank drops.
- PR1069: in endpoint nine, R=gamma R1 in the fixed basis and conventions.
- PR1075 at 672852c59ebeb95a0329a34c1081f25476a2ff8f: gamma is NONZERO
  in that branch, by the actual joint-negative kernel and prolongation
  argument. Its complete conditional hypotheses are retained.

All geometric hypotheses of these originals remain. In particular this is
not a claim about the abstract quotient-third matrix replacing the actual
41-to37 map. The rank and vanishings refer to that original positive map.
Thus gamma≠0 is discharged by PR1075, not added as an unproved premise.

## 2. The exact open set and the fourth target

Since gamma≠0, multiplying the R1 row by gamma does not alter its component
ideal sheaf. PR1044 and PR1046 therefore give I_E for the determinant image
of the actual fourth restricted to D, up to its harmless common sign.

The original second target has the exact sheaf presentation

    A O(-2) --B--> P O → I_Sigma(6) → 0.

The map B is injective as a sheaf. On the complement of the six C5 axes,
it has rank3 on fibers and its cokernel is a line bundle; its kernel on
the original H0=A+D is exactly D. In particular the full relevant fourth
source there is D, not a smaller sheaf or an enlarged specialized source.

The determinant row N of signed maximal minors of B identifies its
cokernel with I_Sigma(6)⊂O(6). Away from Sigma this embedding is an
isomorphism on fibers. Hence on that open set, nonzero evaluation of the
determinant-embedded original fourth is equivalent to a NONZERO map from
D into the one-dimensional fourth-page target.

Every point of Sigma lies in supp(Z)⊂supp(E). Therefore at every direction
outside supp(E), B has rank3 and the determinant row of the original
fourth is nonzero. Its fourth Bockstein has rank1. This is an actual-page
conclusion, not an inference of fiberwise injectivity of an ideal sheaf
at a singular point. All singular target points are excluded here.

The ten C3 axes and the twelve conic points also lie in supp(E); they are
not silently included in the asserted uniform Smith profile. At those
points the fourth D row vanishes. At the C5 axes the second rank changes
as well. No profile is deduced at any of these exceptional directions.

## 3. Formal elimination and the exact valuations

Work first over the function field K, or over C at one arbitrary allowed
direction, and let R0 be the corresponding power-series discrete valuation
ring in t. Since Q has rank33, unit row and column operations split off
33 unit pivots. The remaining matrix has four rows and eight columns,
with zero constant term. Its coefficient of t represents beta1. Since
beta1=0, the entire residual matrix is divisible by t².

The coefficient after dividing by t² represents beta2. Its rank is3 by
Section2. Constant operations then give a three-by-three invertible block
in this coefficient. Power-series elimination splits three factors t²,
leaving a one-by-five residual row divisible by t³. Its coefficient at
t³ is the original third Bockstein on the surviving D, in the quotient
by the second image. That Bockstein vanishes, so the residual row is
actually divisible by t⁴. Its coefficient at t⁴ is the fourth Bockstein.
By Section2 this coefficient row is nonzero, so its common valuation is
EXACTLY4. A further unit operation makes it a single t⁴ pivot.

For clarity, the local algebra after dividing the four-by-eight residual
matrix by t² can be written, through the relevant orders, as

    [ I3+tA+O(t²)       tB+O(t²) ]
    [ tC+O(t²)          tD+t²E+O(t³) ].

Its Schur residual before the outer t² is

    tD+t²(E−CB)+O(t³).

Thus beta3=0 means D=0 in this already normalized quotient, and beta4 is
E−CB, not merely the uncorrected lower-right t² coefficient E. The
certificate verifies this universal correction term with fully symbolic
block coefficients. This explicitly retains the correction induced by
the three second-order pivots.

The resulting37 nonzero Smith pivots are exactly (1). There are41 source
columns, so precisely four zero columns remain. The structure theorem
over a DVR gives the asserted free kernel, finite cokernel and its length.

## 4. Determinantal orders and the rectangular-rank boundary

Invertible row and column operations preserve determinantal ideals over
R0. For the form (1), the maximal-minor ideal is generated by the product
of the37 nonzero pivots:

    t^(33·0+3·2+4)=t^10.

More generally the determinantal valuations are0 for sizes1 through33,
then2,4,6,10 for sizes34,35,36,37. The maximal-minor ideal is nonzero,
so the original positive matrix has row rank37 over the Laurent-series
field. Because the original pencil has polynomial entries in t, this
also means row rank37 on a nonempty Zariski-open set of t for each
allowed direction, and generically in the full direction/parameter family.
It is not a claim of row rank37 at t=0 or at every nonzero t.

The surviving free kernel has dimension4 over the Laurent-series field;
it is not a target obstruction. The positive matrix is rectangular and
cannot be called invertible. Nothing here supplies the behavior of the
other parity component, a full adjoint isomorphism, an opposite-bundle
selection or a source-classification exclusion.

## Reproduction

Run python verify.py and python -O verify.py. The verifier authenticates
the retained inputs, checks exact source/page dimensions and exponent
counts, and proves the universal Schur correction and final row pivot
identities over symbolic coefficient rings. No actual HM matrix, source
coefficient, direction or parameter is evaluated. The actual Bockstein
and ideal-sheaf comparisons are mathematical inputs, not conclusions of
this formal algebra calculation.
