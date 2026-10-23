# The degree-six image pencil of the source2 V-channel radical

## Result and scope

Work over C. Let G be the binary icosahedral group, W its defining
two-dimensional representation, and X=P(W), with the invariant
symplectic identification W=W*. Write

    A=Sym^2 W, S=Sym^3 W, D=Sym^4 W, T=Sym^5 W,

and let V, P, W' denote the other three-, four-, and two-dimensional
irreducibles. All representations used here are self-dual.

For every balanced degree-eighteen endpoint and every residual coupling
in the source2 constant normal forms, each nonzero V-channel radical
element induces a square-zero degree-preserving endomorphism

    (n2,n3,n4)

of the two fixed negative multiplication pencils. Its exact image
characters and ranks are

    (im n2, im n3, im n4) = (D,T,P),
    (rank n2, rank n3, rank n4) = (5,6,4).               (1)

More precisely, its image is isomorphic, with the same pencil variables,
to the fixed pencil system associated with the unique V-subsystem V6 of
Sym^6 W:

    N2,V=Sym^4 W,   N3,V=Sym^5 W,
    N4,V=Sym^6 W/V6=P,
    A_V,l(s)=l s,   B_V,l(s)=[l s].                     (2)

For every nonzero l in the same fixed two-space W, A_V,l is injective
and B_V,l is surjective. The system (2), including its two pencils,
is independent of the balanced endpoint and of whether the residual
quotient coupling is zero or nonzero. Its common constant space is V6.
There is no change in the pencil variables.

Conditionally on the published actual-source inputs of PR790, (1)-(2)
are therefore necessary conditions on the fixed actual source2 tensors.
No actual tensor, parameter, coefficient, matrix, point, or source-instance
rank is evaluated here. No actual endomorphism algebra is measured and
no source is excluded. This is a theorem over the entire normal-form
family, not a check of an abstractly chosen member.

## 1. Exact dependencies and the constant normal form

The following sources in Akilleez-QA/read-em-and-weep were read at the
stated immutable public commits:

- [PR754, abstract balanced degree-eighteen systems](https://github.com/Akilleez-QA/read-em-and-weep/blob/044add76ebb14043a0edf73171517c90b9ef0c13/research/hm/order-four-quadratic-load/ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md),
  commit 044add76ebb14043a0edf73171517c90b9ef0c13. Sections 3-5 identify
  V18=f12 V6, the unique endpoint P-space divisible by f12, and the
  balanced open locus.
- [PR786, endpoint Wronskian](https://github.com/Akilleez-QA/read-em-and-weep/blob/575c0720268af5bb4b305e29284f65614ba9f9ca/research/hm/source2-endpoint-wronskian/PROOF.md),
  commit 575c0720268af5bb4b305e29284f65614ba9f9ca, Section 1. We use
  the projective orbit sizes 12,20,30,60, uniqueness of the orbit D12,
  and perfectness of G.
- [PR789, residual coupling normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md),
  commit 2d1642ad40ae1111b84b50eeaca0426bfbfbb314. We use its genuine
  endpoint quotient, arbitrary-coupling graph classification, and the
  exact annihilator sequence in Section 6.
- [PR790, first constant block](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md),
  commit af0e03d26da5e47d18ae732291aca46f4d448dc5. We use its genuine
  constant splitting and its Section 6 identification of the natural
  reconstruction with the fixed original pencils.
- [PR791, exact source2 endomorphism algebra](https://github.com/Akilleez-QA/read-em-and-weep/blob/2cd033a4a5ba549d07330427cd779364cb83c0fb/research/hm/source2-pencil-endomorphism-algebra/PROOF.md),
  commit 2cd033a4a5ba549d07330427cd779364cb83c0fb, Sections 4-7,
  identifies the V channel as part of the square-zero radical and
  supplies the contravariant fixed-pencil transfer. Its proof SHA-256 is
  8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290.

All geometric and rank arguments are supplied below; the algebra theorem
is used to identify the radical channel and its transfer. No unpublished
mathematical dependency is used.

Here are all of the normal-form data needed. Put

    U_j^e=Sym^j W O(j-e) subset Sym^e W O,
    (U_j^e)_[ell]=ell^(e-j) Sym^j W.

For an arbitrary balanced endpoint t, write

    H_t=A18+V18+P_t subset H^0(O(18)),
    F_t=H_t*,  C=O(-18),  c_t:C -> F_t O.

The endpoint evaluation is onto and has kernel

    E_C=ker(H_t O -> O(18))=(P+D)O(-2).                (3)

The full constant inclusion is

    H*=V0 direct-sum Hbar,       Q*=U direct-sum R,
    V0=Sym^10 W=A+V+D,          U=U_8^10,
    Hbar=V1 direct-sum F_t,     V1=Sym^8 W=P+D.        (4)

Its residual has the genuine constant quotient

    R intersect V1 O=A0=U_2^8,
    0 -> A0 -> R -> C -> 0,                            (5)

where the last map is induced by projection to F_t O and c_t. Every
allowed residual coupling is retained. We neither split (5) constantly
nor replace its endpoint by a chosen bundle lift.

Dualize (4) and put

    E0=ann_V0*(U)=W O(-9),
    E_R=ann_Hbar*(R),    E=E0 direct-sum E_R,
    Q=U* direct-sum R*.

For these constant evaluation sequences the fixed-pencil reconstruction
is natural and gives

    N2=H^0(Q(-2)),  N3=H^0(Q(-1)),  N4=H^1(E),
    A_l(s)=l s,    B_l(s)=delta(l s),                  (6)

with delta the evaluation connecting map. In the actual-source
application PR790 identifies (6) with the original fixed tensors, not
merely with spaces of the same character.

Let b:Hbar -> V0 be a nonzero constant V-channel map: it is zero on V1
and on the A and P parts of F_t. The algebra theorem proves

    b(R) subset U,

and the endomorphism n of H* which is b on Hbar and zero on V0 belongs
to the radical, with n^2=0. Its dual h=n* preserves E. Under (6) h
induces the claimed triple. Duality reverses composition, but preserves
square-zero and commutation with each fixed pencil.

## 2. Divide the V channel by the orbit form inside the saturated block

Let f12 be any nonzero invariant form of degree twelve. Its divisor is
the reduced orbit D12. No coefficients or normalization are selected.
PR754 gives

    Sym^6 W=V6+P6,       V18=f12 V6.                   (7)

The three independent sections V6 are basepoint-free: a nonempty common
base divisor would be G-invariant and would have degree at least twelve,
whereas its degree is at most six. Thus there is an exact sequence

    0 -> E_V -> V6 O --ev6--> O(6) -> 0.              (8)

On R, b factors through the quotient C in (5), and b c_t is nonzero
because c_t has full constant span and b is nonzero on its V constituent.
By (7), as a map into V0 O it has a factorization

    C=O(-18) --f12--> O(-6) --a--> V0 O.              (9)

The map a actually lands in U. Indeed U is saturated and

    Z=(V0 O)/U=W O(9)

is locally free. The composite of a with Z becomes zero after
multiplication by f12, because b c_t lands in U. Multiplication by the
nonzero section f12 is injective on the locally free sheaf Z after the
appropriate twists, so that composite is already zero. This proves
factorization through U at every point, including D12; generic containment
alone would not suffice without this torsion-free quotient argument.

The map a:O(-6)->U is nonzero. The universal decomposition Sym^8 W=P+D
gives

    Hom_G(O(-6),U)
      = (Sym^8 W tensor Sym^4 W)^G
      = Hom_G(Sym^8 W,Sym^4 W),    dimension one.      (10)

It is exactly the D channel. Put q_V=a*:U*->O(6). After twisting by
-2 and taking H^0, it is the nonzero Schur projection

    Sym^8 W=P+D -> Sym^4 W=D.                         (11)

In particular it is onto. On the twist by -1 its map of sections is
the composite

    Sym^8 W tensor W -> Sym^4 W tensor W
                            -> Sym^5 W,              (12)

where the last arrow is ordinary polynomial multiplication. It is onto
as well. These are assertions about universal intertwiners and full
section spaces, not numerical rank calculations.

Let p:V0*->V6 be the nonzero constant projection dual to the V-channel
identification. Equation (9), divided by f12, says exactly that p and
q_V give a morphism of evaluation sequences

    0 -> E0  -> V0* O -> U*   -> 0
         |g       |p      |q_V
    0 -> E_V -> V6 O  -> O(6) -> 0.                  (13)

In particular g:E0->E_V is a genuine bundle map. Its cohomology map,
not a pointwise fiber rank of b, will determine n4.

## 3. The degree-six kernel is W' O(-3)

From (8), E_V has rank two and degree -6. Since V6 consists of
independent sections, H^0(E_V)=0. Its ordinary splitting degrees are
therefore negative. If the splitting is not O(-3)+O(-3), its unique
highest-degree line summand is O(-1) or O(-2).

That line is intrinsic and hence G-stable. Any equivariant line bundle
with underlying bundle O(-r) differs from the standard G-linearization
by a character. G is perfect, so this character is trivial. A nonzero
inclusion O(-r)->E_V->V6 O, for r=1 or 2, would give

    Hom_G(O(-r),V6 O)
       = Hom_G(V,Sym^r W) != 0.

This is impossible: Sym^1 W=W and Sym^2 W=A are irreducible and neither
is V. Hence the ordinary splitting is balanced. Equivariantly, set
K=H^0(E_V(3)); evaluation identifies

    E_V=K O(-3),      dim K=2.                        (14)

The inclusion into V6 O yields K subset V tensor Sym^3 W. The character
identity

    V tensor Sym^3 W=W'+S+T                           (15)

forces K=W': its right side has exactly one two-dimensional irreducible
and no one-dimensional summands. For completeness, (15) follows from
V tensor W=T, W tensor T=D+V+P, W tensor D=S+T, and
W tensor P=W'+T, using the ordinary Clebsch recurrence. Consequently

    E_V=W' O(-3),
    H^1(E_V)=W' tensor W=P.                           (16)

The evaluation cohomology of (8) also identifies this P naturally with
Sym^6 W/V6, since H^0(E_V)=0 and H^1(V6 O)=0.

## 4. The first map of kernels has reduced determinant D12

The constant map p in (13) is projection onto the unique V constituent
of V0*. Under the invariant apolar pairing,

    E0=U_1^10=W O(-9).

Thus the generic rank of g is the generic rank of the first-jet map
of the unique three-dimensional subsystem V10 of H^0(O(10)).
This correspondence uses the same symplectic point convention as (4):
the projected complete first osculating bundle is dual to evaluation
of value and first derivative of V10. It is not an evaluation at a
chosen point.

Here is why that generic rank is two. The subsystem V10 is basepoint-free:
as before an invariant nonempty base divisor would have degree at least
twelve, greater than ten. Its independent sections define a nonconstant
morphism X->P(V10*). Over C such a morphism has nonzero differential
generically. Indeed, if all its affine coordinate ratios had zero
differential, they would be constants in the characteristic-zero
function field of X, contradicting nonconstancy. Hence its value and
first derivative span two dimensions generically. This proves generic
rank two without a selected coefficient, derivative value, or point.

Since E0 and E_V have rank two, g is an injective sheaf map with torsion
cokernel. Its determinant is a nonzero invariant section of

    Hom(det E0,det E_V)=O(12).                         (17)

The determinant coefficient characters are trivial by perfectness.
Every nonzero invariant effective divisor of degree twelve is the unique
reduced orbit D12. Therefore

    div(det g)=D12,
    0 -> E0 --g--> E_V -> T12 -> 0,                   (18)

where T12 is a torsion sheaf of length twelve, supported with length one
at every point of D12. In particular g has fiber rank two off D12 and
rank one on D12. Nothing here asserts that its sheaf image is saturated
in E_V; it is not.

Since H^1(T12)=0, (18) proves the needed surjectivity

    H^1(E0) -> H^1(E_V)=P -> 0.                       (19)

Together with (11)-(12), (19) says that the morphism (13) induces a
surjection onto the degree-six system in each of its three pencil
spaces. Surjectivity in degree four is established geometrically, not
by a multiplicity count.

## 5. Balancedness makes the endpoint map injective on H^1

Multiplication by f12 identifies V6 with the constant vector subspace
V18 of H_t. Denote this constant linear inclusion by j:V6->H_t.
Although its definition multiplies binary forms, j is a map of constant
coefficient spaces. The corresponding map of line bundles is the
nonconstant multiplication map O(6)->O(18). This gives the commutative
diagram of exact evaluation sequences

    0 -> E_V -> V6 O --ev6--> O(6)  -> 0
          |        |j            |f12
    0 -> E_C -> H_t O ------> O(18) -> 0.             (20)

All three vertical maps are injective as sheaf maps. The snake lemma
therefore gives

    0 -> E_C/E_V -> (A18+P_t)O
                            -> O(18)|D12 -> 0.       (21)

This also verifies saturation of E_V inside E_C: its quotient in (21)
is a subsheaf of a locally free sheaf on the smooth curve X and hence
is locally free. It is not legitimate to replace this quotient by a
chosen abstract bundle complement.

We claim

    H^0(E_C/E_V)=0                                    (22)

for every balanced t. By (21) this is the kernel of restriction of
A18+P_t to D12. A form vanishes on D12 exactly when it is divisible by
f12. There is no A in Sym^6 W=V+P, so the restriction is injective on
the irreducible A18.

For the irreducible P_t, a nonzero restriction kernel would be all of
P_t, and would force

    P_t=f12 P6.

PR754, Section 4, identifies precisely this endpoint as the unique
b-zero parameter, one of the two excluded nonbalanced points. Thus the
restriction is also injective on P_t for every balanced t. The images
of A18 and P_t cannot cancel: they are inequivalent irreducibles and
the restriction map is G-equivariant. Its kernel is therefore zero,
proving (22).

The cohomology sequence of (21) now makes the map in (20) injective:

    H^1(E_V)=P -> H^1(E_C)=P+D.                       (23)

This is the distinguished P in the balanced endpoint cohomology.
Balancedness is used here in an essential way; we make no uniform
claim of (23) at the excluded b-zero endpoint.

## 6. The genuine residual quotient preserves that injection

For every residual coupling, dualizing the intersection and projection
data in (5) gives the exact sequence

    0 -> E_C -> E_R -> ann_V1*(A0) -> 0,
    ann_V1*(A0)=T O(-3).                              (24)

One may obtain it directly by dualizing the quotient sequence induced
by the saturated inclusion (5); it is the annihilator sequence of
PR789, Section 6. Neither (24) nor its maps require a constant splitting
of R into A0 and C.

Since H^0(T O(-3))=0, (24) yields an injection

    H^1(E_C) -> H^1(E_R).                             (25)

Likewise the quotient map R->C gives an actual subbundle inclusion

    C*=O(18) -> R*,                                   (26)

so it is injective on H^0 after either twist -2 or -1. Combining
(20) with (24) and (26) gives a morphism from the degree-six evaluation
sequence (8) into the residual evaluation sequence

    0 -> E_R -> Hbar* O -> R* -> 0.                   (27)

It induces injections in all three reconstructed pencil spaces: in
degrees two and three by multiplication by f12 followed by (26), and
in degree four by (23)-(25). This proves coupling independence at the
level of actual maps, not just at the level of abstract splitting types.

## 7. The factorization computes the entire image pencil

The composite constant map in (13), (20), and (27) is

    V0* --p--> V6 --j--> H_t -> Hbar*.

It is precisely the restriction of h=n* to V0*, and h vanishes on
Hbar*. The quotient composite is

    U* --q_V--> O(6) --f12--> C* -> R*.               (28)

The maps on kernels are E0->E_V->E_C->E_R. Thus the complete
endomorphism triple factors through the reconstructed degree-six
evaluation sequence. The first factor is surjective on its three
spaces by (11), (12), and (19); the second is injective by Section 6.
Its image is therefore exactly, not merely contained in, that system.

In the residual section spaces the first two images are

    im n2 = f12 Sym^4 W subset H^0(C*(-2))
                             subset H^0(R*(-2)),
    im n3 = f12 Sym^5 W subset H^0(C*(-1))
                             subset H^0(R*(-1)).      (29)

The last image is the embedded H^1(E_V)=P of (23)-(25). Equations
(16) and (29) prove the rank profile (1).

Naturality of the connecting maps in (20) and (27) identifies the
restricted B pencil with

    Sym^5 W -> Sym^6 W/V6,     s -> [l s],             (30)

and multiplication identifies the restricted A pencil with
Sym^4 W->Sym^5 W, s->l s. This proves (2), including the actual
maps rather than their image characters alone.

For every nonzero l, multiplication is injective on binary forms. To
check surjectivity in (30), l Sym^5 W is the hyperplane in Sym^6 W
of sections vanishing at the zero of l. Basepoint-freeness of V6 says
that V6 is not contained in that hyperplane. Therefore

    l Sym^5 W+V6=Sym^6 W,

which is precisely surjectivity of (30), for every l.

The common constant reconstruction of (2) is (8), with constant space
V6. Indeed E_V=W'O(-3) and O(6)*=O(-6) meet the same negative-degree
hypotheses as (6), and the standard natural reconstruction recovers
its constant evaluation sequence. The rank-two sheaf image of E0 in
E_V from (18) is not that saturated kernel; its torsion discrepancy
does not obstruct the surjection on H^1 in (19). This distinction is
why a pointwise image-bundle assertion cannot replace the proof above.

Choosing another nonzero generator f12 or another generator of the
one-dimensional V channel only changes the displayed identifications
by nonzero scalars. It does not change the image subspaces or the
isomorphism type of their fixed-pencil system. No canonical scalar
normalization or endpoint coordinate is asserted.

## Evidential boundary

The proof uses exact constant normal forms, representation identities,
saturation on P1, generic separability in characteristic zero, and
natural cohomology sequences. Each generic assertion is proved for
the relevant entire invariant subsystem and is used to derive a global
sheaf statement. No member of the balanced endpoint family is selected
or tested, and both residual coupling classes remain present throughout.

The additional necessary source2 constraint is the specific nonzero
square-zero commuting endomorphism with image pencil (2), not a measured
property of the actual HM algebra. No realization, exclusion, parameter
identification, or large computation is claimed. This is a written
structural proof, not proof-assistant certification.
