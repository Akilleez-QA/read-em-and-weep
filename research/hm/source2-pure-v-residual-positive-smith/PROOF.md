# Surviving residual-large positive Smith criterion

## Theorem

Retain the actual source2 nonzero pure-V compatible-radical hypotheses,
and specifically the residual-large mechanism: P_h has zero actual N0
projection and nonzero actual N8 projection. By PR1097 its unique fourth
lift is R=alpha R1, with alpha unselected and possibly zero.

Let M_a(t)=Q+tT_a be the ORIGINAL positive map from dimension41 to
dimension37. Let K=C(P(A)) be the direction function field, with a local
trivialization of the direction line. The following are equivalent:

1. alpha is nonzero.
2. The original fourth Bockstein on its surviving D is nonzero generically.
3. The maximal37-minor ideal of M_a(t) over K[[t]] is (t^10).
4. The Smith exponents over K[[t]] are 33 zeros, three twos and one four.

When these equivalent conditions hold, put E=Z disjoint-union E12,
where Z consists of six length-four C5 ideals and ten reduced C3 axes,
and E12 is the reduced twelve-point conic orbit. The determinant-embedded
original-fourth D row has component IDEAL SHEAF I_E, of length46 and
support cardinality28. For every direction outside supp(E), the same
Smith profile holds over C[[t]]. Its kernel is free of rank4, its
cokernel is (C[[t]]/(t^2))^3 plus C[[t]]/(t^4), and its length is10.
Over K the identical statements hold with C replaced by K.

If alpha=0, every generic maximal minor is divisible by t^11. The last
Smith pivot is either absent, or has exponent e with 5<=e<=31. Thus
alpha=0 does NOT imply failure of Laurent-series row rank37. No value
of alpha, realization of the residual mechanism, full adjoint rank or
completion of the original repair is asserted.

## 1. Audit of the excluded-branch predecessor

PR1077 is retained for a full hypothesis audit, not invoked as a theorem
about this surviving branch. Its endpoint-nine hypothesis enters in
exactly two places: PR1069 supplies R=gamma R1 in that branch, and PR1075
supplies gamma nonzero. Those two implications are NOT imported here.
The opening theorem and Section1 of PR1077 therefore cannot simply be
relabeled. Its Section2 component-ideal argument uses only a nonzero R1
lift, and Sections3–4 use only the original page ranks and vanishings.

We instead use PR1097 for the surviving residual-large line constraint
and retain alpha nonzero as an explicit condition. The original first,
second and third symbols, the actual fourth comparison and the universal
ideal-sheaf results are re-applied below under their own hypotheses.
INPUTS.json retains those six independent originals, plus PR1097 and the
audited PR1077. Neither endpoint-nine nonvanishing proof is a dependency.

## 2. Actual pages and the fourth component scheme

PR1019 gives rank Q=33, ker Q=A+D of dimension8, coker Q=P of dimension4,
and the exact original second map B_a(x)=-mu[a^2x] on A, zero on D,
with mu nonzero. The retained original first-vanishing proof uses actual
cyclic cohomological multiplication and gives beta1=0. The retained
original third-vanishing theorem gives beta3=0 in every direction,
including the extra specialized A-kernel at the six second-rank drops.
That theorem also identifies the exact second-rank-drop scheme Sigma:
six length-four C5 ideals, with rank B=3 off them and rank2 on them.
None of these statements assumes endpoint nine.

The second target is the actual torsion-free cokernel

    A O(-2) --B--> P O -> I_Sigma(6) -> 0.

PR1025 supplies the original corrected-lift identity

    iota beta4|D = -s L,       s=[LR],

and proves beta4|D identically zero iff R=0. This is a statement about
the original fourth, not a substitution of the quotient third for the
original matrix. The determinant embedding N of coker B gives the row
-H=-NLRL. PR1044 identifies the nonic row NLR on every nonzero R1 lift
with the complete scheme E=Z disjoint-union E12. PR1046 proves equality
of the component ideal sheaves of NLR and NLRL, including the ten axes
where L is not onto. Thus alpha nonzero gives I_E for the ORIGINAL
fourth D row. This is not a rank-degeneracy scheme of R, nor an equality
of raw graded ideals generated in different degrees.

Outside supp(E), B has rank3, so the whole surviving original source is
D and its target is a line. The determinant embedding is an isomorphism
on that target fiber because Sigma is excluded. Nonvanishing of H is
therefore equivalent to rank1 of the actual fourth. Hence alpha nonzero
gives fourth rank1 at every such direction and at the generic direction.
If alpha=0, PR1097 gives R=0 and the original fourth on D is zero.
Conversely generic fourth vanishing forces R=0 by PR1025 and hence
alpha=0. This proves the equivalence of conditions1 and2 without any
source evaluation or reliance on excluded endpoint-nine arguments.

## 3. Formal elimination and the exact determinant threshold

Work over K[[t]], or at any fixed direction outside supp(E) when alpha
is nonzero. The constant rank33 splits off33 unit pivots. The remaining
matrix has size4 by8. First vanishing makes it divisible by t^2. Its
leading coefficient is the original beta2 of rank3, so three t^2 pivots
split off. The remaining row has size1 by5 and order at least3.
Its coefficient at order3 is beta3 and vanishes. Its coefficient at
order4 is the corrected original fourth, not an uncorrected matrix
coefficient.

Explicitly, after the outer t^2 the block form can be written

    [ I3+tA+O(t^2)       tB+O(t^2) ]
    [ tC+O(t^2)          tD+t^2E+O(t^3) ].

The Schur residual is tD+t^2(E-CB)+O(t^3). Thus beta3=0 kills D,
and beta4 is E-CB. If alpha is nonzero, Section2 makes this row nonzero;
a unit row/column elimination gives its single pivot t^4. There remain
four zero source columns. The Smith form and all module claims follow.
Its determinantal valuations are0 through size33 and then2,4,6,10.

If alpha=0, the same elimination through degree4 gives a final row
divisible by t^5. In either case, maximal-minor valuations are the sum
6 plus the least valuation of that final row; invertible operations
preserve these ideals. Consequently the maximal-minor ideal is (t^10)
if and only if alpha is nonzero. If alpha is zero, it is contained in
(t^11), possibly the zero ideal. This proves all four equivalences.

If the final row is nonzero, its least valuation e is finite. Some
original maximal minor is then a nonzero polynomial in t of degree at
most37 because the ORIGINAL pencil is linear. Its least possible order
is6+e, so e<=31. This proves the stated alternative 5<=e<=31 in the
zero-alpha case. In particular later nonzero obstructions could still
give Laurent row rank37: fourth vanishing alone does not decide it.

## 4. Scope and reproducibility

The new content is the surviving residual-large conditional Smith theorem
and the exact scalar/nonvanishing/determinantal-threshold equivalence.
The already known universal R1 scheme and the formal Smith algorithm
are inputs and algebra, not new classifications. No conclusion is drawn
at points of supp(E), where the fourth row vanishes or the second rank
changes. No conclusion is transferred to the nonzero-N0 mechanism or
the opposite parity component.

Run python verify.py and python -O verify.py. The checker authenticates
all eight inputs and reproduces the universal Schur correction, row
elimination, determinantal exponents and both alpha alternatives with
formal coefficients. It evaluates no actual source, parameter or direction.
The exact geometric and original-page comparisons are the written proof
using the authenticated inputs, not deductions from symbolic test counts.
