# Fixing the divided cochain: exact fibers and a global normal form

## Setup and result

Work over C on X=P4 with the marked actual monad and fixed-duality complex
of PR682. Write A0=S O(-1), S=U+A, E=U Omega^2(2), L=Delta O(-1),
B=End_0(F), Q=(q=0), and Z=P(W*) the reduced vertex of Q. Delta is
Gamma-trivial but retained in the bundle constructions. Let D0(t) denote
the space of global degree-zero fixed-duality cochains of twist t:

    C=(R,T,-R^dagger),
    D0(t)=H0(End(S) O(t)) directsum H0(sp(E)(t)).

No trace condition is imposed on R. All family dimensions mean
Hom_Gamma(P2,-) dimensions in the physical-center-even part, with
P2=Sym^2 A tensor D=1+A+V+2P+3D. No extra Serre eigenspace is imposed. Prescribed f, V and vertex assignments
must themselves be compatible P2-equivariant families for these family
counts to apply. For individual cochains without equivariance the ordinary
fixed-V fiber dimension is2450, or2220 with its middle vertex fixed.

For the equation dC=f-qV, with f fixed, each nonempty fiber obtained by fixing V as an actual global
cochain has family dimension618, rather than the
829-dimensional fiber obtained by fixing only [V]. Fixing additionally a
reachable middle vertex value leaves dimension564, rather than775.
The difference211 is precisely the space of attainable exact divided
cochain changes, not a numerical subtraction of unrelated kernels.
We prove these statements by exact sequences and an explicit global
normal form; existence is asserted only for fibers that are nonempty.

## 1. Ambient closed cochains and global homotopies

Let Pcal_X be the parabolic subbundle of sp(E) preserving A0, and let
Ncal_X be its rank50 kernel on the induced adjoint B. The canonical
sequences of PR682 hold on X itself:

    0 -> Ncal_X -> Pcal_X -> B -> 0,
    0 -> Lambda^2 A0 tensor L^-1 -> A0 tensor E tensor L^-1
      -> Ncal_X -> 0.                                      (1)

A closed degree-zero cochain is uniquely specified by a middle T preserving
A0: its source R is the unique regular factor of T alpha through alpha.
The right-arrow identity follows by fixed duality. Thus closed cochains
of twist t identify with H0(Pcal_X(t)), without requiring a global monad
splitting. The published ambient vanishings H0(B(2))=H0(B(4))=0 imply

    ker(d:D0(t)->D1(t)) = H0(Ncal_X(t)),  t=2,4.           (2)

Here and below the displayed Ncal sections are identified with their unique
full closed cochains, not just middle matrices. This is why the fixed-V
fiber has no additional source ambiguity.

Twisting (1) gives

    0 -> Lambda^2 S O(t-1) -> S E(t) -> Ncal_X(t) -> 0.    (3)

For t=2,4 the first two terms have no positive cohomology: O(1),O(3)
are positive, and E(2)=U Omega^2(4), E(4)=U Omega^2(6) have the positive
Bott vanishing already used in PR682. Hence Ncal_X(2) and Ncal_X(4)
are higher-acyclic. In particular their sections lift through S E(t).
The symmetric tensor map in (1) is the middle component of a fixed-duality
monad homotopy. This can be checked in a local symplectic splitting;
the resulting source is forced by alpha and glues. Thus every closed
cochain in (2) has a global homotopy representative, and its ambiguity
is exactly H0(Lambda^2 S O(t-1)). This is a structural statement about
cochain representatives, not a quotient of our affine solution spaces.

The ordinary dimensions are

    h0 Ncal_X(4)=5*560-10*35=2450,
    h0 Ncal_X(2)=5*90-10*5=400.                           (4)

## 2. Class-fixed completions have the normal form N4+qH2

Let Kcl be the space of homogeneous completions dC=-qV whose divided
cohomology class [V] is zero. The monad-to-bundle comparison and connecting
map of PR683 give delta_q(rho(C|Q))=-[V], with delta_q injective because
H0(B(4))=0. Therefore C|Q induces zero on F_Q, or equivalently is the
unique closed cochain associated to a section of Ncal_Q(4).

The restriction sequence is

    0 -> Ncal_X(2) --q--> Ncal_X(4) -> Ncal_Q(4) -> 0.

Its H0 restriction is onto by H1(Ncal_X(2))=0, proved above. Choose an
ambient lift n of that section. The full cochain C-n restricts to zero
on Q: this holds for the middle, and the source follows from the unique
factor through alpha_Q. Componentwise divisibility by the nonzerodivisor
q now yields a unique H in D0(2) with C-n=qH. Consequently

    Kcl = H0(Ncal_X(4)) + q D0(2),
    H0(Ncal_X(4)) intersect qD0(2) = q H0(Ncal_X(2)).      (5)

For the second equality, d(qH)=q dH=0 implies dH=0, since the ambient
cochain terms are locally free; then apply (2). This also proves that
any two decompositions C=n+qH differ exactly by

    (n,H) -> (n-qk,H+k),  k in H0(Ncal_X(2)).

There is no claimed canonical choice of n or H. In this normal form the
divided cochain is V=-dH. Thus (5) gives an exact sequence

    0 -> H0(Ncal_X(4)) -> Kcl --C maps to V--> dD0(2) -> 0, (6)

where the sign has no effect on the image. Surjectivity is explicit:
for any V=dH, take C=-qH. This is a proof that the image consists of all
global exact cochains in the displayed space; it does not assume that
an arbitrary cohomologically trivial cochain has a global primitive.
For any two actual completions with the same divided class, (6) applies
to their difference and proves that their divided cochain difference
has such a global primitive.

In an affine nonempty class-fixed fiber, the attainable V's are therefore
exactly V0+dD0(2). Every V in this translate has an affine completion fiber
under H0(Ncal_X(4)). This resolves both reachability and fiber size.

## 3. The vertex can still be prescribed independently

PR684 proves that Ncal_Q(4) restricts onto H0(Ncal_Z(4)). Composing with
the just-proved ambient restriction gives

    H0(Ncal_X(4)) -> H0(Ncal_Z(4)) onto.                 (7)

Also qH has zero middle restriction at Z, since q vanishes on Q and Z.
Thus (5) shows directly that vertex and divided-cochain changes can be
matched independently inside their reachable images. Given V=dH and a
vertex section z, choose n with n|Z=z and take C=n-qH. Its divided cochain
is V and its middle vertex is z. In particular the joint map from Kcl
to H0(Ncal_Z(4)) directsum dD0(2) is onto, and the kernel is exactly

    ker(H0(Ncal_X(4)) -> H0(Ncal_Z(4))).                 (8)

This concerns the middle vertex value used by PR684, not an arbitrary
independent full source restriction. The source is determined by the
middle for closed cochains. Fixing V, f and a middle T also leaves the
source unique by PR682. Thus the same618 and564 count middle and full
fixed-V completions, unlike the734/829 or680/775 fixed-class counts. In particular, one must not subtract211 from the
734-dimensional middle family: the middle alone does not specify V because
of the95-dimensional source-lift freedom. The canonical exact sequence (6)
is on full cochains and gives829-211=618 (or775-211=564 with vertex fixed).

## 4. Exact character computation

Put H=V+W and Gi=U tensor Lambda^(3+i)H. Exterior Euler gives

    [H0 E(4)]=G0 Sym^3 H-G1 Sym^2 H+G2 H,
    [H0 E(2)]=G0 H-G1,
    [H0 Ncal_X(t)]=S[H0 E(t)]-Lambda^2 S Sym^(t-1)H.

These Euler differences are section characters by the vanishings in Section1.
Together with PR683's sp(E)(2) character, exact abstract 2A5 character
arithmetic gives the following physical-even decompositions:

    N4 =20*1+65*A+58*V+83*P+103*D,  dimension1236, family618;
    N2 = 6*1+10*A+13*V+11*P+ 17*D,  dimension 204, family102;
    D0(2)=15*1+34*A+34*V+37*P+52*D, dimension627, family313;
    dD0(2)=9*1+24*A+21*V+26*P+35*D, dimension423, family211.

The last equality uses the proved kernel (2), not a presumed rank. Ordinary
h0 D0(2)=850+375=1225 and dim dD0(2)=1225-400=825 provide separate checks.
PR684's vertex character is2*1+6*A+5*V+7*P+9*D, dimension108, family54.
Subtracting the actual image (7), the fixed-V vertex-zero kernel is

    18*1+59*A+53*V+76*P+94*D, dimension1128, family564.

Exactness (6) recovers618+211=829 and (8) recovers564+211=775. These
are unquotiented cochain solution dimensions. The bounded verifier uses
all nine conjugacy classes with exact Q(sqrt5) arithmetic; it performs no
HM coefficient, point, derivative, matrix, or numerical rank evaluation.

## Consequence and remaining boundary

A global exact change of divided cochain can always be absorbed explicitly
by adding -qH to a completion, without changing its middle vertex or
induced third-neighborhood adjoint. The latter follows because its change
is q^3H on3Q. Fixing an actual cochain representative therefore imposes211
additional family conditions beyond fixing its cohomology class, but creates
no new vertex incompatibility within the previously attainable images.
No particular primitive H for a selected actual input is constructed here;
no fourth Bockstein value, original-source endpoint, higher lift, or
algebraicity assertion follows.

## Immutable dependencies

- [PR682: completion and ambient parabolic construction](https://github.com/Akilleez-QA/read-em-and-weep/blob/5a8249656bfb406d4a0a89994b0de6293e5acd8f/research/hm/source-completion-criterion/PROOF.md).
- [PR683: exact class map and character conventions](https://github.com/Akilleez-QA/read-em-and-weep/blob/d4008b924e9ddff9726f86ccccc1574677da9218/research/hm/completion-kernel-dimensions/PROOF.md).
- [PR684: vertex restriction surjectivity](https://github.com/Akilleez-QA/read-em-and-weep/blob/98802dcdee6a4293ae1b119bfa1d591ff3cc8b62/research/hm/vertex-completion-intersection/PROOF.md).
- [Ambient H0 vanishings in the cyclic Rao proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/CYCLIC-RAO-CUBIC-INJECTIVITY-AND-TWO-S4-LEGS.md).

Authored structural mathematics; independent review is recorded separately.
The verifier checks representation arithmetic, not proof-assistant certification.
