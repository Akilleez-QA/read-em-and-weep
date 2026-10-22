# The divided class determines the actual third-neighborhood adjoint

## Fixed data and structural inputs

Work over C with the actual marked monad M on X=P4, its locally free
cohomology F, and B=End_0(F). Put Q=(q=0), with q the fixed invariant
quadratic, and rQ=(q^r=0). Retain the published fixed-duality summand and
physical-center parity. Fix a,h,b,U_a,Z_a, where a,h,b are quadratics,

    dU_a=q^2 Z_a,  U_a|Q=aN.

Here a is a quadratic in the negative coordinate representation W and is
center-even, as are h and b. The symbol b is the fixed source
correction L_can(a,h). In particular b below never denotes a varying
adjoint. A completion means global cochains C of degree zero and twist4,
and closed V of degree one and twist2, satisfying

    dC=a h Z_a-qV.

The actual fifth-neighborhood theorem supplies at least one such completion.
The associated section is induced by

    J(C)=(a h-q b)U_a-q^2 C,  dJ(C)=q^3(V-bZ_a).

Thus J(C) is a section of B_(3Q)(8), not necessarily an ambient closed
cochain. The theorem below compares induced sections, not their raw matrices.

We use the established inputs in PR683: homogeneous completable middles K
have a canonical surjection rho:K -> H0(B_Q(4)); for dD=-qT its induced
section eta satisfies delta_q eta=-[T]; H0(B(4))=0; and
H0(B_Q(4))_+=N(A+D), of dimension8. The parameter representation is
P2=Sym^2(A) tensor D=1+A+V+2P+3D. These are structural inputs, not
selected-source evaluations.

## 1. Exact classification, including the cochain-to-bundle comparison

For two completions put D=C'-C and T=V'-V. Then

    dD=-qT,  eta=rho(D_middle),
    delta_q eta=-[T],  J(C')-J(C)=-q^2 eta.             (1)

The last equality is an equality of actual adjoint sections on3Q. To justify
it without assuming a global cochain homotopy, split the monad locally into
its cohomology F and contractible summands. Such splittings exist because
the monad end sequences and F are locally free; they remain splittings after
any base change to rQ. Consequently taking induced endomorphisms commutes
with restriction and scalar multiplication. Since D is closed modulo q,
q^2D is closed modulo q^3 and induces precisely q^2 times its Q adjoint eta.
These local identifications agree on overlaps by functoriality on monad
cohomology. This proves the last equality in(1), including its minus sign.

As q is a nonzerodivisor on X and B is locally free, there is an exact
sequence of actual sheaves

    0 -> B_Q(4) --q^2--> B_(3Q)(8) -> B_(2Q)(8) -> 0.  (2)

Locally injectivity says q^2x in(q^3) implies x in(q), componentwise in a
free module over the ambient local ring. No smoothness of Q is required.
Taking H0 preserves the injection. Also

    0 -> B(2) --q--> B(4) -> B_Q(4) -> 0

and H0(B(4))=0 make delta_q injective. Therefore

    [V']=[V] if and only if eta=0 if and only if J(C')=J(C).  (3)

This is uniqueness for fixed divided COHOMOLOGY CLASS, not merely for fixed
V as a cochain, and only with a,h,b,U_a held fixed.

## 2. Exhaustion, square-zero preservation and the family quotient

Every eta in H0(B_Q(4)) is realized by a homogeneous completion by the
surjectivity of rho in PR683. Adding it to one fixed completion gives all
differences in(1). In the even sector, the set of induced J(C) is therefore
an affine torsor under q^2N(A+D), canonically identified with A+D through
the injective map in(2). Its dimension is8. The divided classes form the
corresponding affine translate of -delta_q N(A+D); (1) identifies these
two torsors. There is no assertion that an arbitrary class of H1(B(2)) is
reachable.

For nonzero a,h the published corrected-lift theorem gives one square-zero
J. The classification also directly shows that every even completion has
the same property: writing eta=Ns, the square difference on3Q is

    (J-q^2Ns)^2-J^2=-q^2((J|Q)Ns+Ns(J|Q))=0,

because J|Q=a^2hN and N^2=0; the term q^4(Ns)^2 is already zero on3Q.
Thus square-zero does not select among these eight directions. This does
not assert square-zero for arbitrary unrelated lifts or arbitrary source
corrections. In zero-source cases the same argument applies whenever the
chosen base lift is square-zero.

For Gamma-equivariant polynomial P2 families, exactness of Hom_Gamma(P2,-)
in characteristic zero and the PR683 polarized existence argument give
an affine quotient of dimension

    dim Hom_Gamma(P2,A+D)=1+3=4.

Consequently the734-dimensional middle and829-dimensional full fixed-class
families of PR683 all induce the SAME J(C). They remain unquotiented
cochain-completion freedoms; their size is not a count of distinct third
neighborhood adjoints. If compatible vertex data are also fixed, PR684's
680 middle/775 full fibers still induce the same J. Conversely the vertex-
zero class map remains onto, so fixing a reachable vertex does not reduce
the four-dimensional family of distinct J's. No canonical representative
or splitting of these affine spaces is provided.

## 3. Next step: a compatible fifth-boundary variation, not its value

Suppose one J4 on4Q extends aJ(C), as in the published ladder, and let
J(C')-J(C)=-q^2Ns with s in H0(O_Q(2))_+=A+D. Lift s to a global quadratic
tilde s; this is possible from the quadric restriction sequence and H1(O)=0.
The lift can be kept center-even by averaging.
Then a compatible new fourth-neighborhood section is

    J4'=J4-q^2 U_a tilde s  on4Q.                     (4)

Indeed the correction has differential -q^4 Z_a tilde s, hence is closed
on4Q, and its3Q restriction is -q^2 aNs=a(J(C')-J(C)). In the exact
fifth-neighborhood boundary with target H1(B_Q(4)), naturality gives

    partial_5(aJ4')-partial_5(aJ4)=-[a tilde s Z_a|Q]. (5)

The sign uses the same convention delta=[d(cochain)/q^r] as the published
ladder. All twists agree: q^2 U_a tilde s has twist10, a times it twist12,
and division by q^4 leaves twist4. Replacing tilde s by tilde s+q c changes
(4) by -q^3 c U_a, whose multiplication by a is already closed on5Q
(its differential is -q^5 c aZ_a); hence(5) is independent of the lift.

In fact the boundary is independent of the even fourth lift of a fixed J.
The exact sequence

    0 -> B_Q(4) --q^3--> B_(4Q)(10) -> B_(3Q)(10) -> 0

shows that any two such fourth lifts differ by q^3 eta_4, with
eta_4 in H0(B_Q(4))_+=N(A+D). Write eta_4=N t and lift t to a global
quadratic. After multiplication by a the difference extends to5Q via
q^3 U_a tilde t: its differential q^5 Z_a tilde t vanishes on5Q.
Its fifth boundary is therefore zero. Thus(5) is the intrinsic variation
of this boundary on the affine space of even J's, whenever one fourth
lift exists. Construction(4) then also proves existence for all these J's.
Here a in Sym^2W is center-even: negative coordinate type is not odd
center parity and must not be confused with the extra Serre involution.

## 4. The variation is exactly second-symbol indeterminacy

Set xi=delta_q(N) in H1(B). Naturality gives delta_q(Ns)=s xi.
The canonical actual lift supplies

    q zeta_a=a xi,  [Z_a]=zeta_a.

These are the published identities in the positive first-Bockstein theorem,
not an additional choice of normalization. Every s in A+D corresponds to
a vector s xi in the original kernel of q:H1(B(2))_+ -> H1(B(4))_+.
Associativity gives

    a(s xi)=q(s zeta_a).

Thus s zeta_a is a first divided class, and the next multiplication gives
the second-symbol representative [a s zeta_a] in the q-cokernel.
Its image under restriction to H1(B_Q(4)) is exactly [a s Z_a|Q].
This is the same identification of the second-symbol target used by the
actual fifth-neighborhood theorem; restriction kills q-multiples.

There are two published sign conventions, which must not be conflated.
POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO, Section4, expands the pencil
q+t a and defines beta2(s xi)=-[a s zeta_a].
FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING, Section3, explicitly uses
q-t a and writes beta2_a(s)=[a s zeta_a], the convention compatible with
its ambient divisions and the fifth-neighborhood ladder. With this latter
notation equation(5) becomes

    partial_5(aJ4')-partial_5(aJ4)=-beta2_a(s).         (6)

With the earlier q+t a notation it is +beta2_a(s xi). Either convention
gives exactly the same second-symbol image and therefore the same conclusion:

    [partial_5(aJ4)] modulo im(beta2_a)
    is independent of ALL even completion classes V,
    with a,h,b,U_a fixed.

Together with Section3 this also removes the choice of even J4. The
source s ranges through all A+D, not merely the surviving D fourth-source
space. In particular this conclusion does not require generic rank3,
a nonsingular smoothing direction, or inversion of the second symbol at
the exceptional axes. It is an image-containment statement for every a.
The published vanishing on D is consistent with it but not needed.

The earlier fourth-Bockstein note already states the abstract cohomological
second-symbol indeterminacy. The new content here is its exact geometric
realization through the classified J3 torsor and the actual fifth boundary.
Thus the large cochain freedom, the eight-dimensional third-adjoint
freedom, and the even fourth-lift freedom cannot alter the fourth quotient
value. This does not compute that common value, prove it zero, remove the
fixed correction b, or assert independence under arbitrary source/Schur
normalization changes. Higher lifting and algebraicity remain unresolved.

## 5. Exact remaining raw-boundary freedom

The pinned fourth-Bockstein note, Section1, states that beta2 vanishes on D
and its A restriction is injective as a sheaf on P(A), with fiber rank3
away from the six axes and rank2 at those axes. These published structural
facts sharpen the variation count without evaluating any fourth value.

For a fixed nonzero a, the affine map from the eight-dimensional even J3
torsor to raw fifth boundaries therefore has image dimension3 and fibers
dimension5 off the axes; at an axis these dimensions are2 and6. This is
about the raw boundary, not the fourth quotient, which is constant.

For equivariant P2 families the four-dimensional parameter space decomposes
as Hom_Gamma(P2,A) of dimension1 and Hom_Gamma(P2,D) of dimension3.
All three D-valued families have zero boundary variation. No nonzero
A-valued polynomial family can have identically zero variation: the
sheaf-injective map beta:A O(-2)->P O is injective on polynomial sections
after any twist, and tensoring with the constant h-parameter space preserves
injectivity. Thus the family boundary-variation map has image dimension1
and kernel dimension3. The A-valued family s has degree2 in a and degree1
in h; its second-symbol image has degree4 in a and degree1 in h. This is
not the pointwise dimension3 image, and the two counts must not be confused.
Neither count supplies the affine base boundary or its fourth-quotient value.

## Immutable dependencies and verification scope

- [Second-symbol definition for q+t a](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md).
- [Ladder-compatible q-t a convention and divided-class indeterminacy](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING.md).

- [Whole-Q completion and exact class map, PR683](https://github.com/Akilleez-QA/read-em-and-weep/blob/d4008b924e9ddff9726f86ccccc1574677da9218/research/hm/completion-kernel-dimensions/PROOF.md).
- [Compatible vertex/class fibers, PR684](https://github.com/Akilleez-QA/read-em-and-weep/blob/98802dcdee6a4293ae1b119bfa1d591ff3cc8b62/research/hm/vertex-completion-intersection/PROOF.md).
- [Actual fifth-neighborhood ladder](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md).
- [Actual corrected third lift square-zero](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md).

The argument is authored structural mathematics. The independent review is
recorded separately. The bounded verifier checks only formal differential
identities, twists and dimension arithmetic, not the geometric dependencies,
an actual selected instance, or proof-assistant formalization.
