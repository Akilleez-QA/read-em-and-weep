# Excluding the last rank-one shapes in the (3,1) plateau

## Result and scope

This excludes the last three necessary first quotients in
`EXTREMAL-31-RANK-ONE-DEGREE-ELEVEN-EXCLUSION.md`: e=9 and
A0=B+O(-8), for B=2O(4), O(4)+O(6), or W O(5).
Combined with the previously excluded rank-two and rank-three dual-image
branches, this excludes the entire maximal (k,l)=(3,1) profile.
It does NOT infer a stronger global SF or positive-square bound: other
profiles require their own exclusions. No actual HM coefficients, points,
instance matrices, rank experiments, or scans are used.

All bundles below retain their equivariant linearizations. Write
K=E^-, K2=E^{--}, F0=E^{---}; their ranks are 14,11,8, and deg(E)=-54.
Set A1=K/K2 and A2=K2/F0. These are the ACTUAL derivative images in
A0(-2) and A1(-2). Only these three known interior steps have rank three.
All later kernels are saturated Gauss kernels; their ranks are determined
below, not assumed. Bundle graph changes and splittings are never declared
horizontal.

The rank-two branch closure is EXTREMAL-31-SINGLE-GAUSS-EXCLUSION.md.
The recursive saturated-kernel rule is Section1 of
EXTREMAL-31-FIRST-REMAINING-QUOTIENT-EXCLUSION.md.
The pinned inputs are the two preceding rank-one notes and their verifiers,
`ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, and
`EXTREMAL-31-DUAL-CUBIC-IMAGE-HAS-RANK-AT-MOST-TWO.md`.
Persistence gives max degree(K2)<=-3 and max degree(F0)<=-4, and

    H0(K2(3)) embeds in H0(A1(1)).

Use U=chi(E(3))=Wp+2T and E4=chi(E(4))=3V+3P+2D.
Invariant effective divisors have degrees in <12,20,30>.

## 1. The actual first image has no torsion defect

Put D0=B(-2), so A1 is a full-rank subsheaf of D0+O(-10).
Since deg(K2)<=-33, its determinant defect is at most15 for B=2O(4)
and at most19 for the other two B. It is therefore zero or12.
The image of the low projection is O(-10-d), with d=0 or12.
If d=12 the high image is exactly D0 and the extension splits, giving
A1=D0+O(-22). If d=0 and the total defect is12, its high kernel H
has degree deg(D0)-12 and every degree at most max degree(D0).
Thus every degree of H is at least -10, and
Ext1(O(-10),H)=H1(H(10))=0. Hence A1=H+O(-10).

The complete high-kernel list is:

- D0=2O(2): H=O(-10)+O(2), O(-8)+O, O(-6)+O(-2), 2O(-4).
- D0=O(2)+O(4): H=O(-10)+O(4), O(-8)+O(2), O(-6)+O,
  O(-4)+O(-2), W O(-3), Wp O(-3).
- D0=W O(3): the preceding list without O(-10)+O(4).

This is exhaustive equivariant rank-two splitting, not an assertion of
realizability. For each candidate set C=chi(K2(3)) and
M=H0(A1(1))-C. Necessarily H1(K2(3))<=M. The verifier checks that M
is either not genuine, or admits no negative splitting block mapping to
the low target in A1(-2), namely O(-12) or O(-24). Thus all defect12
cases contradict rank three at K2. Consequently, in all three cases,

    A1=B(-2)+O(-10).                                      (1)

The low-block test is finite: a block R O(-j), j>=5, costs
R Sym^(j-5)W in H1(K2(3)), so j<=dim(M)+4.

## 2. Complete necessary splittings of K2

For B=2O(4), equation (1) gives

    chi(K2(3))=-Wp+S-T, H1(K2(3))<=Wp+S+T.

For the larger B it gives

    chi(K2(3))=-Wp-T, H1(K2(3))<=Wp+S+2T.

The only blocks able to map to the low O(-12) in A1(-2) are O(-12)
in the first case, and O(-12) or W O(-13) in the larger cases.
The W O(-13) possibility consumes the entire latter H1 budget. Its
rank-nine complement would have H1=0 and H0=S+T of dimension10 at
twist three. Since all its degrees are <=-3, this is impossible.
Therefore O(-12) occurs, once, and has a nonzero scalar low projection.
Remove its high graph in the target. Let Y be its rank-ten bundle
complement in K2. Exact identities give

    B=2O(4): chi(Y(3))=S, chi(Y(4))=A+2V+D, H1(Y(3))<=S;
    larger B: chi(Y(3))=0, chi(Y(4))=2V+P, H1(Y(3))<=S+T.

The exhaustive splitting check, including the EMPTY negative tail, gives

    B=2O(4): Y=S O(-3)+2V O(-4);
    larger B: Y=(2V+P) O(-4), or T O(-3)+V O(-4)+O(-10). (2)

To reproduce exhaustiveness, enumerate all negative blocks whose H1 costs
fit the displayed budget. Their multiplicities are bounded by those costs.
For each multiset N, H0(Y(3))=chi(Y(3))+H1(N(3)) is the coefficient
of O(-3). Subtract its tensor product with W and chi(N(4)) from chi(Y(4));
the remainder must be the genuine coefficient of O(-4). Check rank ten.
No positivity-only surrogate replaces this two-twist character check.

For B=2O(4), the target high part is 2O. Maps from S O(-3) to its two
copies are scalar multiples of the same complete cubic evaluation; they
have combined rank at most one. The V O(-4) components have zero Hom to
O. Thus the whole derivative has rank at most two, a contradiction.
For B=O(4)+O(6), the high target is O+O(2). Every block of either Y
in (2) has zero Hom to O. This again contradicts rank three.
Only B=W O(5) remains.

## 3. Force the next actual image in the W case

Here deg(K2)=-52. The actual rank-three image A2 lies in
W O(1)+O(-12), of degree -10. Because deg(F0)<=-32, its determinant
defect is at most10. Invariance forces defect zero, so

    A2=W O(1)+O(-12).                                    (3)

This conclusion uses the actual image and the divisor bound, not merely
equal generic ranks. In both possible K2 splittings,

    chi(F0(3))=-S-T, chi(F0(4))=V-D.                      (4)

## 4. The T-containing K2 splitting

After removing the scalar low graph, the high map is

    T O(-3)+V O(-4)+O(-10) -> W O(1).

Persistence H0(F0(3))=0 forces its T component to be nonzero. The
unique T=Sym5 W summand of W tensor Sym4 W is the upper Clebsch
summand: the complete first-jet evaluation of quintics. It is surjective
and has kernel S O(-5). One can see the kernel at [1:0] as the quintics
divisible by the square of the vanishing linear form, and transport
SL2-equivariantly; this gives the standard kernel Sym3 W O(-5).
The other two source blocks lift through this surjection, since their
Ext1 groups with S O(-5) have line degrees -1 and5, both with zero H1.
Equivariant lifts follow by averaging. Removing these SOURCE graphs gives

    F0=S O(-5)+V O(-4)+O(-10).                            (5)

Its next derivative takes values in A2(-2)=W O(-1)+O(-14).
Only the S O(-5) block has a nonzero Hom. Here S=Sym3 is the LOWER
summand of W tensor Sym4, not the upper first-jet summand. Thus its
nonzero map factors as complete cubic evaluation onto O(-2), followed
by the saturated Euler-line inclusion O(-2)->W O(-1).
Its actual image is O(-2), and its saturated kernel is
A O(-6)+V O(-4)+O(-10).

A nonzero all-negative saturated subbundle of the original constant bundle
cannot have zero Gauss derivative: in characteristic zero a zero derivative
makes its Grassmannian map constant. Therefore each ensuing derivative
must be nonzero. The complete Hom computations leave exactly these
successive kernels and actual quotients:

    A O(-6)+V O(-4)+O(-10) -> quotient O(-4), kernel W O(-7)+V O(-4)+O(-10);
    W O(-7)+V O(-4)+O(-10) -> quotient O(-6), kernel O(-8)+V O(-4)+O(-10);
    O(-8)+V O(-4)+O(-10)  -> quotient O(-8), kernel V O(-4)+O(-10);
    V O(-4)+O(-10)       -> quotient O(-10), kernel V O(-4).

The first two maps are complete quadratic and linear evaluations; the
last two are scalars. The final V O(-4) has zero Hom to O(-12), its
next derivative target. It would be horizontal, a contradiction.

## 5. The all-degree-four K2 splitting

Now K2=(2V+P) O(-4)+O(-12). Apply the same exhaustive splitting
method to (4), max degree(F0)<=-4, and rank eight. Six formal splittings
survive the two characters. Requiring every block to admit an injection
into this K2 leaves exactly

    (a) F0=V O(-4)+D O(-6);
    (b) F0=2V O(-4)+Wp O(-9);
    (c) F0=(V+P) O(-4)+O(-14).

The verifier checks all six before filtering, so this does not assume a
particular high map or a horizontal complement.

In (a), only D O(-6) maps to W O(-1)+O(-14). Its map is the lower
Sym4 summand in W tensor Sym5, hence complete quartic evaluation onto
O(-2) followed by the Euler-line inclusion. The successive kernels are

    V O(-4)+S O(-7), V O(-4)+A O(-8),
    V O(-4)+W O(-9), V O(-4)+O(-10), V O(-4).

The actual quotients after the first O(-2) are O(-4), O(-6), O(-8),
and O(-10). Each nonzero map is forced by the zero-derivative contradiction
and is the unique complete evaluation. The final V O(-4) is horizontal.

In (b), only Wp O(-9) maps to W O(-1). Wp occurs in Sym7 W but
not Sym9 W, so it belongs to the lower Clebsch summand. Its septic
pencil has no common zero: a common-zero divisor would be invariant of
positive degree at most7, less than12. Thus the actual image is O(-2)
and the kernel is 2V O(-4)+O(-16). The next target is O(-4); only
O(-16) can map to it, through the unique invariant of degree12. Its
image is isomorphic to O(-16), NOT its saturation O(-4). Consequently
the kernel is 2V O(-4), whose next target is O(-18), and it is horizontal.

In (c), the V and P blocks have zero Hom to W O(-1)+O(-14).
Only O(-14) supports the nonzero derivative. Whatever its high and low
components, its actual image is isomorphic to O(-14), with kernel
(V+P) O(-4). The latter has zero Hom to O(-16) and is horizontal.

All cases are contradictory. The saturated descent uses no rank-three
assumption after F0 and never substitutes saturation for an actual image.

## Reproduction and boundary

Run `python3 verify_extremal_31_last_rank_one_exclusion.py`. It imports the
pinned exact character verifiers, checks all defect alternatives, exhausts
negative-tail multisets including the empty multiset, checks both Euler
twists, all necessary embeddings, and every Hom support and Clebsch branch
used above. The polynomial evaluation and saturated Gauss arguments are
proved in this note. Together with the prior branch exclusions, (3,1) is
excluded; no global improved SF bound follows from this result alone.
