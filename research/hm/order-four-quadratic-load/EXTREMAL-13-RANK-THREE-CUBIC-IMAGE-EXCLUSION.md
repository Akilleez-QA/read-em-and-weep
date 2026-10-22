# The rank-three cubic image in (1,3) is impossible

## Result and scope

Under the actual equivariant presentation and characteristic-zero Gauss
persistence hypotheses used in
EXTREMAL-13-RANK-THREE-CUBIC-IMAGE-THREE-EXACT-QUOTIENTS.md,
the canonical cubic evaluation image in the (1,3) plateau has rank at
most two. This excludes all three exact rank-three images in that note.
It does not exclude cubic-image ranks one or two, does not close the
(1,3) profile, and does not improve the global SF bound.

The proof uses exact representation arithmetic and an elementary
horizontal-subbundle obstruction, not actual coefficients, points,
instance matrices, or rank experiments. Bundle splittings below are not
asserted to be horizontal.

## 1. A multiplicity obstruction at the maximal bundle degree

Let K be a saturated equivariant subbundle of a constant bundle H O on
P1 in characteristic zero. Suppose all ordinary summands of K have
degree at most -a, with a>0, and K contains an isotypic direct summand
R O(-a) tensor M, where R is irreducible and dim M=m. Suppose its actual
second fundamental form factors through a bundle B, and

    dim Hom_G(R O(-a),B) < m.

The restriction of the form to the isotypic summand is a linear map
from M to this Hom space. A nonzero vector in its kernel gives a direct
subbundle C isomorphic to R O(-a) which is killed by the second
fundamental form of K.

The second fundamental form of C in H O consequently lands in
(K/C)(-2). Every ordinary summand of this target has degree at most
-a-2. Hence Hom(C,(K/C)(-2))=0, and C itself is horizontal. Its
Grassmannian classifying map has zero differential, so is constant in
characteristic zero. A saturated horizontal subbundle of H O is a
constant subspace tensor O and has degree zero. This contradicts
C=R O(-a), of negative degree.

In particular this obstruction does not require any rank assumption on
the endpoint derivative. It also does not require replacing an actual
image by its saturation.

## 2. Input and independent checks of the three-image reduction

Write W for the standard binary representation, W' for the other
binary representation, V for the nonstandard three-dimensional
representation, P for the even four-dimensional representation, D for
the five-dimensional representation, and T=Sym5 W.

For (1,3), the actual bundle is

    E=(W'+2T) O(-3)+V O(-4),

and K=E^- satisfies H0(K(3))=0. Assuming cubic-image rank three, the
preceding note proves that its actual image equals its saturation and
that the exact quotient A0=E/K is one of

    W' O(-3)+O(14),
    W' O(-3)+O(16),
    W' O(-1)+O(4).

The dual-envelope argument was checked independently: for the rank-ten
dual kernel Kd, its Euler characteristic in twist three is Dsat-17.
The two successive derivatives bound its sections by
H0(Sbar*(2))+H0(Sbar*), with the lowest dual kernel having no cubic
sections. The resulting representation inequality has exactly the four
saturated candidates stated there. Their degrees are at most 19, while
the globally generated actual cubic image has degree at least 11.
The possible saturation defect is therefore at most eight, below the
minimum positive invariant divisor degree twelve. The actual image and
saturation coincide. The degree-fifteen candidate has zero Hom into all
eligible actual target blocks. The predecessor verifier is rerun by our
companion script. These checks support that reduction; the new result
here is the exclusion below.

## 3. Exhaustive kernels for the first two quotients

Take A0=W' O(-3)+O(d), where d=14 or 16. Persistence forces every
ordinary summand of K to have degree at most -4. Exact Euler
characteristics give

    chi_G(K(3))=2T-Sym^(d+3) W,
    chi_G(K(4))=2T tensor W+V-Sym^(d+4) W.

Thus for d=14 these characters are -W'-S and -A+2V+D;
for d=16 they are -W-W'-S and -1-A+2V+P.
Here S=Sym3 W and A=Sym2 W.

For completeness, write K=R4 O(-4) plus its negative tail. Every tail
block R O(-j), j>=5, contributes the genuine representation
R tensor Sym^(j-5) W to H1(K(3)). Its dimension is dim(R)(j-4).
Therefore j<=dim H1(K(3))+4. Enumerate all central-parity-compatible
irreducibles and all multisets exhausting this genuine H1 budget.
For each tail the twist-four identity determines R4 uniquely; retain
it only if it is genuine. The enumeration includes the empty tail
when its budget is zero and never uses cancellation of positive costs.
It gives precisely:

    d=14:
      K=(2V+D) O(-4)+W' O(-5)+O(-8).

    d=16:
      K=(2V+P) O(-4)+W' O(-5)+O(-6)+O(-8), or
      K=(2V+P) O(-4)+W' O(-5)+W O(-7).

All have rank fourteen and degree -(48+d). These are necessary
splittings, not claims that the associated quotient maps exist.

The next derivative of K factors through

    A0(-2)=W' O(-5)+O(d-2).

The V O(-4) blocks have no map to W' O(-5), even nonequivariantly
by degree. Their Hom space to the scalar target has dimension one:
V has multiplicity one in Sym16 W for d=14, and in Sym18 W for d=16.
Specifically,

    Sym16 W=V+P+2D,
    Sym18 W=A+V+2P+D.

Every necessary K has two copies of V O(-4), so the obstruction of
Section 1 applies with a=4, R=V, and m=2. Both quotients are impossible.

## 4. The third quotient

For A0=W' O(-1)+O(4), the preceding reduction forces

    K=(2V+2P) O(-4).

Its next derivative factors through

    A0(-2)=W' O(-3)+O(2).

There is no equivariant map V O(-4)->W' O(-3), since W' tensor W=P
contains no V. There is exactly one map V O(-4)->O(2), since
Sym6 W=V+P. Once again two V copies map through a one-dimensional
space of equivariant maps. Section 1 gives a horizontal V O(-4), a
contradiction. No subsequent kernel enumeration is needed.

## 5. Reproduction and limitations

Run:

    python3 verify_extremal_13_rank_three_cubic_image_exclusion.py

The verifier reruns the predecessor, exhausts both negative-tail
splitting problems, checks the zero-budget empty-tail case of the third
quotient, checks rank and degree, and checks all endpoint Hom dimensions.
The geometric horizontal-subbundle argument is proved in Section 1;
this finite character verifier is not proof-assistant verification.

Only the cubic-rank-three branch of (1,3) is closed by this argument.
