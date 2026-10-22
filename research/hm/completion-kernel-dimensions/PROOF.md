# Exact homogeneous whole-quadric completion kernel

## Statement and distinction

Keep the actual marked monad and physical quadratic q of PR682. Write
X=P(H*), H=V+W, S=U+A, A0=S O(-1), E=U Omega^2(2), and
L=Delta O(-1). All spaces are complex representations of Gamma=2A5.
Here U and W are its two binary two-dimensional representations; A=Sym^2W,
V=Sym^2U, P is the four-dimensional even representation, and D the five-dimensional
one. A plus subscript means physical-center-even, not the extra Serre involution.
The determinant character Delta=det(U)det(H) is trivial on Gamma and is retained
geometrically. The parameter representation is P2=Sym^2 A tensor D
=1+A+V+2P+3D.

Define K as the vector space of global T in H0(X,sp(E)(4)) such that T can be
completed by a global source component R to a fixed-duality degree-zero cochain
C=(R,T,-R^dagger) with dC divisible by q. This is a homogeneous condition;
the divided degree-one cochain is automatically closed. Then

    K_+ = 23*1 +78*A +70*V +99*P +123*D,
    dim K_+=1478,       dim Hom_Gamma(P2,K_+)=738.

The whole-Q quotient map on the 1203-dimensional equivariant middle family
therefore has image dimension465, not merely an upper bound. No selected
actual matrix, source coefficient, point, or rank evaluation enters this result.

## 1. Exact sequences determine the kernel

Put Pcal=ker(sp(E)_Q -> Hom(A0_Q,E_Q/A0_Q)), the rank53 parabolic bundle
preserving A0_Q. PR682 proves the fixed-middle completion criterion and the
surjective middle restriction, giving the exact sequence

    0 -> q H0(X,sp(E)(2)) -> K -> H0(Q,Pcal(4)) -> 0.

Indeed the homogeneous quotient equality is precisely preservation of A0_Q,
and every section of Pcal(4) extends to an ambient middle section because
H1(X,sp(E)(2))=0. The same criterion supplies a global source completion.

The canonical parabolic-to-adjoint sequence from PR682 is

    0 -> Ncal(4) -> Pcal(4) -> B_Q(4) -> 0,
    0 -> Lambda^2 S O_Q(3) -> S E_Q(4) -> Ncal(4) -> 0,

with the constant Delta^-1 line understood. Here B=End_0(F). Its rank50
kernel Ncal(4) has zero positive cohomology, so

    0 -> H0(Ncal(4)) -> H0(Pcal(4)) -> H0(B_Q(4)) -> 0.

Thus the character of K is the sum of the three displayed section spaces.
These are exact equivariant sequences; their character sums and induced
Hom_Gamma(P2,-) dimension sums are exact by characteristic-zero semisimplicity.
No canonical splitting of these sequences is asserted.

## 2. Actual adjoint input checked from the published cone proofs

At the pinned PR543 commit, NO-PRESERVING-POSITIVE-CONE-EXCESS proves that the
filtration-preserving physical-even adjoints are exactly N H0(O_Q(2))_+=N(A+D).
POSITIVE-CONE-MOVING-LINE-OBSTRUCTION-VANISHES proves that every actual even
adjoint preserves that filtration: its lower component lies in the ordinary
square ideal; the surviving homogeneous term is divisible by the cubic relation
and hence belongs to a bundle with no global sections. Combining these two
statements, rather than assuming preservation, gives

    H0(B_Q(4))_+ = N(A+D) = A+D.

The invariant nonzero nilpotent N has trivial character. The cyclic Rao note
also records this conclusion explicitly. Only this even part is needed here;
no assertion about the entire odd adjoint section space is required.

## 3. Exact bounded character computation

Write G_i=U tensor Lambda^(3+i)H. Exterior Euler and the restriction sequence
for the invariant q give, in the representation ring,

    [O_Q(3)] = Sym^3 H-H,
    [E_Q(4)] = G_0(Sym^3 H-H)-G_1(Sym^2 H-1)+G_2 H,
    [H0 Ncal(4)] = S[E_Q(4)]-Lambda^2 S[O_Q(3)].

The symmetric-square Euler resolution of sp(E)(2) has line twists
1,0,-1,-2,-3. These line bundles are higher-acyclic on P4, and the negative
ones have no sections. Therefore

    [H0 sp(E)(2)] = Sym^2 G_0 tensor H-G_1 tensor G_0.

The resulting even decompositions are

    H0 Ncal(4)_+ = 14*1+55*A+45*V+72*P+86*D,
    H0 sp(E)(2)_+ = 9*1+22*A+25*V+27*P+36*D.

Their dimensions are1032 and438 and their P2-family dimensions are516 and218.
The adjoint contribution A+D adds dimension8 and family dimension4. Hence
1032+438+8=1478 and516+218+4=738, as claimed. Ordinary dimensions2050 and850
provide independent Euler/Bott cross-checks of the first two terms.

For an explicit character verification, verify.py uses all nine conjugacy
classes and exact rational arithmetic in Q(sqrt5), checks table orthogonality,
then computes symmetric and exterior powers by Newton identities. It uses
only the abstract group characters. Choosing the natural center signs on
S and U computes the same center grading on adjoints as the marked physical
inversion; simultaneously reversing the scalar signs on the source and middle
leaves the product and exterior-square formulas unchanged.

PR677 gives the ambient even middle character

    R_+=38*1+123*A+118*V+162*P+200*D.

Consequently the image of the whole-Q quotient map has character

    R_+/K_+ =15*1+45*A+48*V+63*P+77*D,

dimension931 and P2-family dimension465. This image is not claimed to equal
all sections of the isotropy tangent bundle; it is the actual image specified
by the exact kernel above.

## 4. Affine forcing and full completion dimension

For a closed fixed-duality family f with parameter P2, the possible middle
families satisfying dC=f-qV are either empty or a torsor under
Hom_Gamma(P2,K_+). The published actual fifth-neighborhood theorem supplies
abstract global primitives for the actual f=a h Z_a. Since Z_a is linear in a, the forcing is quadratic in a and linear in h.
The tensors a squared tensor h span Sym^2 A tensor D by polarization.
Pointwise solvability for every a,h therefore places the entire polarized
P2 coefficient map in the image of the same linear map (C,V) -> dC+qV.
Polynomial family existence follows by choosing a linear lift through this
finite-dimensional image and averaging over Gamma. Thus this
actual middle solution set is nonempty and has affine dimension738, although
no particular member is constructed here.

For each such middle, PR682 proves that all source lifts differ by
qH, H in End(S) tensor H0(O(2)); V changes by the corresponding coboundary.
The even ambiguity character is6*1+12*A+9*V+10*P+16*D, dimension189,
and its equivariant P2-family dimension is95. The full solution space of
triples (R,T,V), with f fixed and V allowed to vary as a closed divided cochain,
is therefore an affine torsor of family dimension

    738+95=833.

Its even homogeneous character is29*1+90*A+79*V+109*P+139*D, dimension1667.
This is not a quotient by cochain gauge. If V or its cohomology class is
separately prescribed, these dimensions need not apply; changing the source
lift alone does not change that class.

## 5. The full cochain elimination has exactly810 family conditions

The source component of a global degree-zero cochain has section character
End(S) tensor Sym^4 H. Its even part is

    15*1+46*A+41*V+58*P+74*D,

dimension878 and P2-family dimension440. Together with the middle family,
the full degree-zero domain has family dimension1643. Consider its linear map
C -> dC|Q. Its kernel consists precisely of the homogeneous completions above:
V=-dC/q is uniquely determined, so forgetting V changes no kernel dimension.
The image therefore has exact even character

    24*1+79*A+80*V+111*P+135*D,

dimension1620 and family dimension810=1643-833. Thus the full divisible-cochain
condition imposes810 independent linear conditions on its image, whereas
eliminating the source leaves465 conditions on the1203 middle parameters.
The difference345=440-95 is exactly the loss of source freedom after fixing a
completable middle. This is an image-dimension statement for specified linear
maps, not a claim that an arbitrary chosen list of810 equations is independent.

## 6. Only four family directions change the divided cohomology class

There is a canonical surjection rho:K -> H0(B_Q(4)): restrict T to Q and use
its induced endomorphism of F=A0-perp/A0. The two exact sequences in Section1
prove surjectivity. A homogeneous completion C is a closed monad cochain on Q,
so the adjoint section it induces is exactly rho(T). Naturality of the monad
comparison and the restriction connecting map gives

    delta_q(rho(T))=[dC/q]=-[V] in H1(B(2)).

Here the homogeneous convention is dC=-qV. This also proves directly that
neither the source-lift ambiguity nor the kernel of rho changes the class.
The sign is the same boundary convention as the published fifth-neighborhood
note, not an independently chosen normalization.

The published CYCLIC-RAO-CUBIC-INJECTIVITY-AND-TWO-S4-LEGS, Section1, states
the established ambient vanishing H0(B(4))=0. The exact sequence

    0 -> B(2) --q--> B(4) -> B_Q(4) -> 0

therefore makes delta_q injective. Consequently the class-variation image of
K_+ is exactly delta_q(A+D), not just a subspace of dimension at most8.
Its equivariant P2-family dimension is exactly4. The class-preserving middle
kernel has character23*1+77*A+70*V+99*P+122*D, dimension1470 and family
 dimension734. The class-preserving full completion kernel has dimension1659
and family dimension829. The95 source-lift choices remain when only the
cohomology class [V] is fixed. If the cochain V itself is fixed, by contrast,
PR682 makes the source component unique for each fixed T; that is a different
constraint and is not counted by829.

For any nonempty affine forcing solution set, a separately prescribed divided
class can be attained exactly when its difference from the class of one
solution belongs to this image (with the displayed sign). Each nonempty
class-fixed fiber therefore has middle-family dimension734 and full-family
 dimension829. This is a precise class-matching criterion, not a claim that
an arbitrary class is reachable, nor a computation of a particular actual
primitive or the fourth Bockstein. The actual existence source supplies pointwise class-compatible primitives
for its previously chosen v_h. A class-fixed P2-family assertion additionally
requires that the prescribed class assignment is itself a P2-equivariant
family; no polynomial dependence of arbitrary Schur/Bockstein choices is
inferred from pointwise existence.

## Boundary and next dependency

This identifies the exact whole-Q completion kernel and eliminates465 of the
1203 ambient family directions. It neither constructs an actual primitive nor
determines the fourth Bockstein or algebraicity. The1095-dimensional kernel in
PR681 concerns a different joint vertex/ramification map. There is no claim
that it contains K, lies in K, or has an intersection obtained by subtracting
these dimensions. Compatibility with prescribed vertex or ramification values
requires the restriction of that map to K to be proved separately.

## Immutable sources

- [Ambient twist-four vanishing recorded in the cyclic Rao proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/CYCLIC-RAO-CUBIC-INJECTIVITY-AND-TWO-S4-LEGS.md).

- [Completion criterion and parabolic bridge](https://github.com/Akilleez-QA/read-em-and-weep/blob/5a8249656bfb406d4a0a89994b0de6293e5acd8f/research/hm/source-completion-criterion/PROOF.md).
- [Ambient middle character](https://github.com/Akilleez-QA/read-em-and-weep/blob/e8dc002a6de60d5feac936b2b291188fd2bdc6a9/research/hm/equivariant-middle-family/PROOF.md).
- [Preserving cone closure](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/NO-PRESERVING-POSITIVE-CONE-EXCESS.md).
- [Moving-line exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/POSITIVE-CONE-MOVING-LINE-OBSTRUCTION-VANISHES.md).
- [Abstract actual primitive existence](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md).
- [Distinct vertex/ramification kernel](https://github.com/Akilleez-QA/read-em-and-weep/blob/a930f9cc295d79c2342b4eebe6f34efc04ccf05d/research/hm/degree-one-restriction/PROOF.md).

The proof is authored mathematical reasoning checked independently as recorded
in REVIEW.md; the bounded verifier checks character algebra, not formal proof
assistant certification or an actual-source evaluation.
