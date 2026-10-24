# Uniform exclusion of forward length three

## Theorem and scope

In the original constant rank-thirty ambient bundle, with the actual
equivariant presentations below, a maximal generic rank-three Gauss
plateau cannot have forward length l=3, for any backward length k>=1.
Thus this single argument excludes (1,3), (2,3), and (3,3) once the
finite range 1<=k,l<=3 is imposed.

This is a coverage strengthening and simplification of
EXTREMAL-13-FULL-SATURATION-EXCLUDES-THE-PROFILE.md. It does not use the
historical twenty-eight-type recursion, the adjacent-profile elimination
ledger, a classification of negative kernel tails, or the high-degree
target-block filter. In particular the apparent extra saturation
Wp O+O(15) is excluded directly by the same top-multiplicity argument.
Nothing here excludes k,l<=2 or evaluates the actual SF.

All ranks in the proof concern hypothetical bundles and consequences of
the assumed generic rank, not evaluated instance matrices. Bundle
splittings are never declared horizontal.

## 1. Exact inputs and the finite range

Let G=2.A5, with irreducibles 1,W,Wp,A,V,P,S,D,T of dimensions
1,2,2,3,3,4,4,5,6. W is the standard doublet, A=Sym^2 W,
S=Sym^3 W, D=Sym^4 W, T=Sym^5 W; V and Wp are the other triplet and
doublet. The even irreducibles are 1,A,V,P,D. All are self-dual.

On P(W*), retain the actual saturated inclusion E in H O, rank(H)=30,
rank(E)=17, degree(E)=-54, and Q=(H O)/E of rank13. The actual
presentations are

    0 -> E  -> M3 O(-1) -> M4 O -> 0,
    0 -> Q* -> M3 O(-1) -> M2 O -> 0,

    M2=A+2V+3P+4D,
    M3=3Wp+3S+6T,
    M4=2V+4P+3D.

Both E and Q* are center-even. The global input is H0(E(1))=0;
Q is ample, E contains no constants and spans H. The presentations and
this vanishing give

    H1(E(1))=Wp+3T,
    chi_G(E(2))=-V,
    chi_G(E(3))=U:=Wp+2T,
    chi_G(E(4))=3V+3P+2D,
    chi_G(Q*(3))=T-2W-S.                         (1)

These identities and their physical linearizations are authenticated in
the finite-range and actual-sequence originals in INPUTS.json. The
independent fixed character checks below reproduce all five identities.

Write the saturated plateau as F0<...<Fm, E=Fk, m=k+l, with all
graded ranks three. Every interior derivative kernel is the preceding
stage and every interior forward transform is the following stage.
Every interior stage contains no nonzero constant subbundle. A section
of Fi(d) saturates to O(-e) with e<=d; its e-th forward derivative span
is its constant coefficient span. Consequently

    i+d<m  implies  H0(Fi(d))=0.                  (2)

This follows from a polynomial lift and characteristic-zero factorials,
not an equivariant invariant-line assumption. The same holds in the
reversed dual plateau, where Q* has index l and forward length k.
Positive multiplicities in (1) give nonzero sections of E(3) and Q*(3).
Applying (2) at these two central stages gives l<=3 and k<=3.
The two adjacent rank-three blocks ensure k,l>=1.

## 2. The primal splitting when l=3, without twenty-eight-type enumeration

Assume l=3. Formula (2) gives H0(E(2))=0, hence all degrees of E are
at most -3. Equivariant splitting is legitimate by the canonical slope
filtration and finite-group averaging. Since chi_G(E(2))=-V,
H1(E(2))=V. Every block R O(-j), j>=4, contributes the genuine
representation R Sym^(j-4) W to this three-dimensional H1 budget.

For j=4 only R=V can occur. For j=5 the center-odd coefficient has
dimension at least2 and its cost has dimension at least4. For j=6 the
only possible dimension-one coefficient gives Sym^2 W=A, not V.
For j>=7 parity and dimension make the cost greater than3. Thus the
entire tail is exactly V O(-4). Equation H1(E(1))=Wp+3T and V W=T
then identifies the remaining degree-three coefficient:

    E=U O(-3)+V O(-4),  U=Wp+2T.                 (3)

Put K=E^- and I=(E/K)(3), the full actual derivative image in Q(1).
It has rank3. Persistence at index k-1 gives H0(K(3))=0 because
(k-1)+3=k+2<k+3=m. Thus top(K)<=-4 and degree(K)<=-56, whence

    degree(I)=-45-degree(K)>=11,
    U injects into H0(I).                         (4)

Let Sbar be the saturation of I in Q(1). The source E(4) is globally
generated, so Sbar(1) is generically generated and every degree of
Sbar is at least -1. An equivariant degree-minus-one summand has an
even coefficient of dimension at most3. The source U O has no map
to it; the source V O(-1) can reach it only when that coefficient is
V. That block has the full rank3, so Sbar=V O(-1), contradicting the
injection U -> H0(Sbar). Hence every degree of Sbar is nonnegative.

## 3. Dual envelope, uniformly for every k>=1

The three stages preceding Q* in the reversed dual plateau have ranks
10,7,4. Denote them Kd,Kd2,L0. The index of Q* is3; the index of L0
is0. Since m=k+3>=4, (2) gives H0(L0(3))=0.

Negative-transpose duality identifies the saturated full image as

    Sbar=(Q*/Kd)^*(1).

No actual image is identified with its saturation at this step. The
two regular dual derivatives and the actual subsheaf
Kd/Kd2 -> (Q*/Kd)(-2) give, in representation order,

    H0(Kd(3)) <= H0(Sbar*(2))+H0(Sbar*).

Subtracting the exact quotient from (1) gives the necessary inequality

    T-2W-S <= H0(Sbar*(2))+H0(Sbar*)+chi_G(Sbar*(4)). (5)

Only these two known interior dual derivatives were used. No condition
at a forward endpoint, and no assumption k=1, occurs.

## 4. A direct four-shape classification of Sbar

For a splitting block R O(e), e>=0, write Phi_e(R) for its contribution
to the right side of (5). Direct line-bundle cohomology gives

    e=0:  R(Sym4 W+Sym2 W+1),
    e=1:  R(Sym3 W+W),
    e=2:  R(Sym2 W+1),
    e=3:  R W,
    e=4:  R,
    e=5:  0,
    e>=6: -R Sym^(e-6) W.                         (6)

The coefficient parity is (-1)^(e+1), since Sbar is center-odd.
Every block receives a nonzero projection from U O+V O(-1).
Scalar blocks therefore have odd degree at least5: degrees1,3 have
neither U in Sym^e W nor V in Sym^(e+1) W. Three scalar blocks make
the right side of (5) nonpositive, impossible at the T coefficient.

An irreducible rank-three block has odd degree. At degrees1,3 it has
only6 or12 sections, insufficient to contain the14-dimensional U.
At degrees>=5 its Phi is nonpositive, again impossible at T.

Therefore Sbar=R O(a)+O(b), where R=W or Wp, a is nonnegative even,
and b>=5 is odd. If a>=4, its Phi has no positive T coefficient
(at a=4 it is R; thereafter nonpositive), so (5) is impossible.
The W blocks at a=0,2 are ruled out by the full-source Hom tests

    Hom_G(U,W)=Hom_G(V,W W)=0,
    Hom_G(U,W Sym2 W)=Hom_G(V,W Sym3 W)=0.

Thus R=Wp and a=0 or2. Since Wp Sym2 W=T and Wp Sym4 W=S+T,
the positive budgets in (5), after moving T-2W-S to the right, are

    a=0:  B0=2W+Wp+2S+T, dimension20;
    a=2:  B2=2W+Wp+S,    dimension10.             (7)

For b>=7, require Sym^(b-6) W <= Ba. Dimension gives b<=25 or15,
respectively. Degree(Sbar)>=11 from (4) rules out b=5 in both cases.

For a=0, U<=H0(Sbar) requires at least two T copies in Sym^b W.
Degrees7,9,11,13 have only one. Degrees21,23,25 have at least two T
copies in their cost Sym^(b-6), exceeding B0's single T. Degrees
15,17,19 satisfy both necessary conditions.

For a=2, the doublet contributes T to sections, so Sym^b W must
contain Wp+T. At b=9,11, Wp is absent. At b=13,15, the cost contains
T, absent from B2. At b=7, Sym7 W=Wp+T and the cost W fits B2.
This proves the exhaustive necessary list

    Sbar=Wp O+O(15), Wp O+O(17), Wp O+O(19),
          Wp O(2)+O(7).                          (8)

This is a rank-three shape argument with two short fixed scalar-degree
lists. It does not enumerate historical primal/dual splitting records.

## 5. Full-image saturation and one uniform contradiction

The determinant defect of I in Sbar is an invariant effective divisor.
Its degree is at most degree(Sbar)-11<=8. Every positive G-invariant
divisor on P(W*) has degree at least12, from orbit sizes12,20,30,60.
Consequently I=Sbar as sheaves. Therefore A0=E/K is one of

    Wp O(-3)+O(d), d=12,14,16;
    Wp O(-1)+O(4).                                (9)

No discarded target candidate or cubic-image rank hypothesis is needed.
Twist the exact sequence 0->K->E->A0->0 by4. In the order (9),
its Euler characters are

    chi_G(K(4))=2V+P;
                   -A+2V+D;
                   -1-A+2V+P;
                   2V+2P.                       (10)

Since H1 is genuine, each H0(K(4)) contains at least two copies of V.
And top(K)<=-4, so H0(K(4)) is precisely the coefficient space of
its top O(-4) block. Thus K has a direct top summand 2V O(-4).
There is no need to classify the lower tail of K.

The actual derivative of K lands in A0(-2). For the first three cases,
there is no map V O(-4)->Wp O(-5), and the scalar endpoint Hom has
dimension [V:Sym^(d+2) W]=1, for d=12,14,16. In the last case,
Wp W=P contains no V and Sym6 W=V+P gives one scalar endpoint Hom.
Hence the two-dimensional V multiplicity space maps to a
one-dimensional Hom space. A nonzero multiplicity vector is killed,
giving a direct C=V O(-4) in K killed by beta_K.

Its internal derivative lands in (K/C)(-2), all of whose degrees are
at most -6. Hom(C,(K/C)(-2))=0, so C is horizontal in the original
constant ambient bundle. C is saturated there because K/C and H O/K
are locally free. In characteristic zero its Grassmannian map is
constant, forcing degree(C)=0, contrary to degree(C)=-12.

All four shapes (9) are impossible. This proves l!=3 uniformly for
k>=1, completing the claimed column exclusion.

## Provenance and checks

The immutable source commit is
db51525015bb7c5e825833d550d08dedf6f6ea96 in
https://github.com/Akilleez-QA/read-em-and-weep . Exact originals and
Git-blob/SHA256 checks are in INPUTS.json. The essential mathematical
sources are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md,
EXTREMAL-13-FULL-SATURATION-EXCLUDES-THE-PROFILE.md,
EXTREMAL-13-RANK-THREE-CUBIC-IMAGE-THREE-EXACT-QUOTIENTS.md,
EXTREMAL-13-RANK-THREE-CUBIC-IMAGE-EXCLUSION.md, and the actual-sequence,
twist-one-vanishing, Gauss-transform, and invariant-divisor originals
listed in the manifest. The new simplifications are Sections2,4,5 and
the explicit uniform persistence indices in Section3.

Run python3 verify_l3.py and python3 -O verify_l3.py. Both give the exact
RESULT-L3.json, with388 fixed universal character requirements. The
script constructs only abstract G characters on nine conjugacy classes;
it imports no historical verifier and runs no historical profile or
negative-tail enumeration. The saturation and differentiation proof is
the text above, not a consequence of arithmetic checks alone.
