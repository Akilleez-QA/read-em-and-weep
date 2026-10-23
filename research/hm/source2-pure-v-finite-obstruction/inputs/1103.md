# Negative quadratic rank bounds shorten the positive Smith frontier

## Theorem

Retain the actual source2 hypotheses giving PR790's genuine fixed-negative
pencil summand. For the ORIGINAL positive41-to37 pencil M_a(t)=Q+tT_a,

    rank T_a <= 30 for every nonzero negative quadratic a;
    rank T_a <= 27 whenever a is a square.

Consequently every maximal37-minor is a polynomial in t of degree at
most30, or at most27 on the entire square conic. These assertions do not
require Q to preserve either separated block.

Where the original second symbol has rank3, the known first and third
vanishings leave33 unit factors, three t^2 factors, and a last factor
of exponent e or no last pivot. If the last pivot exists, then e<=24;
on square directions it satisfies e<=21. In the surviving residual-large
case with alpha=0, the finite generic range is therefore5<=e<=24,
not5<=e<=31. On every square direction it is5<=e<=21, or the last pivot
is absent. In the residual-large case with alpha nonzero, the twelve
conic exceptional points likewise have e in5..21 or no last pivot;
outside the known exceptional scheme the exponent remains4 by PR1102.

No last pivot, coefficient value or source occurrence is selected. These
are upper bounds, not a claim that each allowed exponent occurs. The
full rank bounds30 and27 are not asserted sharp for actual HM tensors.

## 1. The spaces are the actual positive component

PR790 Section6 explicitly reconstructs the fixed original negative maps
A_l:M2->M3 and B_l:M3->M4, under simultaneous isomorphisms N_i=M_i.
Its equations(22) and(24) retain the original variable l and actual maps;
they do not identify only characters or transpose the entire complex.
The determinant/symplectic convention acts on the negative two-space,
not by interchanging the original source and target.

Its Section7 gives genuine idempotents e2,e3,e4 with

    e3 A_l=A_l e2,       e4 B_l=B_l e3,

and dimensions(9,18,16) for their images. PR795 identifies their
complements as NR of dimensions(32,36,21). Thus the actual negative
system splits N=N0 direct-sum NR with fixed-variable arrows. These
M2,M4 are precisely H1(B(2))_+, H1(B(4))_+, of dimensions41 and37,
used by PR1102; M3 is the intervening negative-parity space. Two negative
linear multiplications return to positive parity. Associativity gives
T_{lm}=B_l A_m=B_m A_l, extended linearly to Sym2 W. Therefore

    e4 T_a=T_a e2,
    T_a = T_a,0 direct-sum T_a,R : (9+32) -> (16+21).

This proves rank T_a<=9+21=30. Nothing asserts e4 Q=Q e2; the invariant
quadratic Q may mix these two blocks. Constant separate changes of
source and target coordinates preserve all ranks and minor degrees.

## 2. The exact residual quotient and quadratic maps

PR795 gives the actual fixed-variable exact sequence

    0 -> NC -> NR -> N8 -> 0,

with NC4 of dimension9. Both negative arrows commute with these maps,
so their quadratic products do as well. No horizontal splitting of NR
is needed. The complete evaluation descriptions give

    N0,2=Sym8 W,
    N0,4=(Sym8 W tensor Sym2 W)/Delta_(8,2)(Sym10 W),
    T_a,0(f)=[f tensor a];

    N8,2=Sym2 W tensor Sym4 W,
    N8,4=(Sym2 W tensor Sym6 W)/Delta_(2,6)(Sym8 W),
    T_a,8(u)=[a u].

Here multiplication acts on the second factor. The first quotient is
H1(E0) from the complete degree-ten evaluation sequence in PR790;
the second is H1(E8) from the complete degree-eight sequence in PR795.
Their constant evaluation maps are complete polarizations Delta, not
arbitrary summands. Taking global sections and connecting maps proves
the displayed quadratic maps by naturality. A common nonzero scalar in
either polarization does not change its image or the following ranks.

Fix an ARBITRARY nonzero linear form l and an arbitrary independent
form m. Write X=l,Y=m as formal coordinates. This is a covariant proof
for all l, not the evaluation of an actual tensor at a selected point.
Complete polarization is natural under every invertible change of this
formal basis.

For a=l^2, a vector f tensor l^2 lies in Delta_(8,2)Sym10 exactly when
the corresponding degree-ten form has all its eighth derivatives
divisible by l^2. In the formal X,Y monomial expansion this forces the
form to be proportional to X^10: every monomial containing Y produces
a nonzero eighth derivative with a remaining Y. Conversely X^10
polarizes into a nonzero multiple of X^8 tensor X^2. Thus ker T_l²,0
is exactly C l^8 and rank T_l²,0=8.

For N8, the kernel of multiplication into the quotient is identified
with those f in Sym8 whose three second derivatives are divisible by
l^2. Expanding in X,Y shows this is exactly

    f in l^4 Sym4 W,

of dimension5: exponents of X below4 give a nonzero second derivative
whose X exponent is below2, and no cancellations occur between distinct
monomials in a fixed derivative. The converse follows by differentiation.
Since multiplication by l^2 is injective before taking the quotient,
rank T_l²,8=15-5=10.

For comparison, the same argument for two arbitrary independent factors
a=lm gives the N8 kernel l^3 m^3 Sym2, of dimension3, and rank12.
The N0 kernel is zero: divisibility of every eighth derivative by lm
would require a degree-ten form divisible by l^9 m^9. Thus its nonsquare
rank is9. These statements concern universal quotient blocks, not
evaluations of the remaining actual residual coupling.

The image of T_l²,R projects into im T_l²,8 and its intersection with
the quotient kernel is contained in NC4. Hence, by the actual exact
sequence rather than a chosen residual splitting,

    rank T_l²,R <= dim NC4 + rank T_l²,8 = 9+10=19.

Adding the separated rank8 proves the full square bound27. Additional
relations in the actual residual map could lower the rank, and are not
excluded by this argument.

## 3. Polynomial degree of every maximal minor

For any rectangular matrices Q,T over a field with rank T<=r, expand
each k-by-k determinant of Q+tT multilinearly in its columns. The
coefficient of t^j is a sum of determinants using j columns from T.
Every term vanishes for j>r because those j columns are dependent,
including after restriction to the chosen rows. Therefore every minor
has degree at most min(k,r). This does not require simultaneous block
forms for Q and T, or any relation between their image spaces.

Apply this to k=37 and r=30, or r=27 on squares. Over the generic
direction field, the positive-page inputs leave a1-by5 row after33
unit pivots and three t^2 pivots. If its least finite valuation is e,
the maximal-minor ideal has valuation6+e. Some original maximal minor
then has exactly that order; it is a nonzero polynomial of degree at
most30. Hence6+e<=30 and e<=24. At any square direction the identical
argument gives6+e<=27 and e<=21.

## 4. Applying the bound to the surviving residual mechanism

The retained original third theorem proves that the only second-rank
drops are the six semisimple C5 axes, where the rank is2. These are not
on the square conic: their quadratic representatives have two distinct
factors. Equivalently a six-point invariant orbit cannot lie on the
conic, whose projective icosahedral orbits have at least12 points.
Thus every square direction has second rank3 and the preceding bound
applies there without an extra specialized A-kernel.

PR1102, using PR1097 rather than the excluded endpoint-nine branch,
proves the generic last exponent is4 exactly when alpha is nonzero.
When alpha=0 the original fourth vanishes on D identically, so the last
row is divisible by t^5. Combining this with Section3 gives the improved
generic range5..24 and square range5..21, or an absent pivot.

When alpha is nonzero, PR1102 gives the fourth component ideal of
Z disjoint-union E12. At E12 the second target is a line and its
determinant embedding is a fiber isomorphism. The component row vanishes
there, hence the original fourth is zero there. Its last exponent, if
finite, consequently lies in5..21. This does not calculate the fifth
or any later obstruction. At the six second-rank drops the pivot
pattern changes, and no last-exponent formula is asserted here.

## Reproduction and scope

INPUTS.json pins PR790, PR795, the actual third-vanishing theorem,
PR1102 and PR1044's exact conic base stratum. The checker authenticates
all five originals, verifies the
polarization/divisibility kernels using full monomial coefficient
spaces, and checks the exterior-degree and Smith-order arithmetic.
All adapted-coordinate calculations are universal identities in the
complete blocks. No actual coefficient, direction, parameter or source
rank is evaluated. The proof supplies actual-map transport and the
rank inequality through the nonsplit residual sequence.
