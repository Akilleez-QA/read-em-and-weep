# A forced nonzero secondary homotopy in the source2 pure-V branch

## Result and scope

Retain the exact actual-source hypotheses of PR949 and PR950. Suppose a
nonzero pure-V negative-pencil radical element j is compatible with Q.
This is a conditional branch hypothesis, not an existence assertion.
There is a unique G-equivariant h:N4 -> N2 with

    h Q = j2,                 Q h = j4.

It has rank nine and image character P+D. It satisfies

    j2 h = h j4 = 0.

For every negative quadratic a define the same-direction chain endomorphism

    K_a = (h T_a, T_a h)

of the ORIGINAL family Q+tT_a. On its Q-cohomology H0=A+D, H1=P,

    k_a^0(x,d) = (0, mu a x),       k_a^1=0,       mu != 0.      (1)

Here a x is ordinary binary-quadratic multiplication into D=Sym4 W,
after fixed nonzero equivariant identifications. The scalar is not evaluated.
In particular k_a^0 has rank three for EVERY nonzero a, kernel exactly D,
and square zero. The nonzero secondary channel and the exact factorization
below are new constraints, not a recomputation of the radical-image quotient.
No higher original Bockstein is asserted zero, no compatible radical is
excluded, and no source or catalogue pair is cut.

## 1. Exact inputs and duplicate boundary

INPUTS.json and inputs/ retain public immutable proofs with SHA256 and Git
blob hashes. PR950 is pinned at 54c7e78bd5351b3ecbdcc4b3b558a0012eb79566;
PR949 at e8d9943ed8402be90a6f249a1ad3dd51dcc3c628; the negative image
identification is PR792 at 2f01f18960ce56b8b2a0c1260c277de3c5f916bf.
The original first-symbol vanishing is at eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c;
the original second nonvanishing is at 6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0.
All their geometric hypotheses are retained. These supply actual fixed
negative multiplication maps, not arbitrary representation substitutes.

PR950 supplies the exact embedded equalities

    im j2 = (ker Q)_D = D,       ker j4 = im Q,
    im j4 = I4 = P subset im Q,  ker Q = A+D, coker Q=P.

The original first Bockstein vanishes globally. The original second is zero
on D and nonzero on A. PR792 identifies the actual restricted image map as

    L_a=T_a|D : Sym4 W -> Sym6 W/V6 = I4,     d |-> [a d].      (2)

Local source2 image, quotient, discriminant, compatibility and fingerprint
packets were searched. The source126 Type-II secondary-homotopy packet has
an analogous canonical construction but different source/target complexes
and a remaining optional D->D scalar. Its conclusion is not imported here.
The present self-endomorphism has a FORCED NONZERO A->D scalar instead.


## 2. Canonical homotopy and its exact image

The maps induced by j on Q-cohomology vanish. On ker Q=A+D this follows
from equivariance, multiplicity-freeness and j2^2=0: each Schur scalar is
zero. On coker Q it follows from im j4 subset im Q.

A cohomologically zero map of finite-dimensional two-term complexes is
nullhomotopic, by splitting into cohomology and contractible pairs. Averaging
over the finite group gives an equivariant h. The difference of two choices
annihilates im Q and lands in ker Q, hence factors through

    Hom_G(coker Q,ker Q) = Hom_G(P,A+D) = 0.

Thus h is unique. The identities hQ=j2 and Qh=j4 give j2h=hj4.
Moreover (j2h)Q=j2^2=0 and Q(j2h)=j4Qh=j4^2=0. This common map factors
through the same zero Hom space; therefore j2h=hj4=0.

Since Q maps onto im Q, h(im Q)=im j2=D. On the other hand Q(im h)=I4=P.
If hy belongs to ker Q, then j4y=0, so y belongs to im Q and hy belongs
to D. Thus ker(Q|im h)=D. The exact sequence

    0 -> D -> im h --Q--> I4 -> 0

proves im h has character D+P and dimension nine. This is an actual-map
rank deduction, not an evaluation at a selected source instance.

## 3. Secondary chain map and the vanishing channels

Set K0=hT_a, K1=T_ah. Direct computation gives

    QK0-K1Q = j4T_a-T_aj2 = 0,
    T_aK0-K1T_a = 0.

Consequently K_a commutes with Q+tT_a for the SAME direction a; no
claim is made that K_a commutes with T_b for unrelated b.

For x in ker Q, first-symbol vanishing puts T_ax in im Q. Hence
K0x belongs to h(im Q)=D. Also T_aD subset I4 by image-pencil preservation,
and h(I4)=h(im j4)=0. Thus K0 annihilates D.

Finally j4T_ah=T_aj2h=0. Therefore T_ah lands in ker j4=im Q on ALL of N4,
not merely on selected representatives. Its induced cokernel map is zero.
This proves all channel vanishings without a generic-rank or skew-channel
argument, and without importing any higher obstruction.

The remaining family is equivariant and linear in a, from A to D.
Since Sym2 W tensor Sym2 W=Sym4 W+Sym2 W+1, its D channel is unique and
is ordinary multiplication. Therefore k0(x,d)=(0,mu a x).

## 4. Exact original-second factorization forces mu nonzero

The map j4 descends to an isomorphism

    iota: coker Q -> I4,        [y] |-> j4y,

because ker j4=im Q. For x in ker Q choose any correction u with
Qu=-T_ax, possible by global first vanishing. The original second class is
beta2_a(x)=[T_au]. Any two choices differ by ker Q, whose T_a-image is
in im Q, so this is the canonical original class, not a surrogate.
Then

    j2u=hQu=-hT_ax=-k0_a(x),
    iota beta2_a(x)=j4T_au=T_aj2u=-L_a k0_a(x).                (3)

Using (1) and (2), on A this is exactly

    iota beta2_a(x) = -mu [a^2 x] in Sym6 W/V6.               (4)

If mu were zero, (3) would annihilate the ENTIRE original second family,
contradicting the pinned actual nonvanishing theorem. Thus mu is nonzero.
No chosen value or normalization of mu or iota is needed.

Polynomial multiplication by every nonzero quadratic is injective on
Sym2 W, since C[x,y] is an integral domain. Hence the rank-three and
kernel assertions in the theorem hold for every nonzero direction,
including original-second exceptional directions. Those exceptional
ranks can drop only in the subsequent map L_a, not in this secondary map.

## 5. A uniform rank-two secondary quotient bundle

On X=P(A), multiplication gives the subbundle exact sequence

    0 -> A O_X(-1) --mu m--> D O_X -> E -> 0.

The preceding everywhere-injectivity makes E locally free of rank two,
with c(E)=(1-H)^(-3)=1+3H+6H^2. The full secondary cohomology map
(A+D)O(-1)->(A+D)O has kernel D O(-1), cokernel A O plus E, and image
isomorphic to A O(-1). These statements concern the secondary map only;
E is not substituted for the original Bockstein cokernel or a source
quotient, and no higher obstruction comparison is assumed.

An A input with nonzero original second Bockstein does not survive to the
next page, so naive later-page naturality cannot be applied to that input.
On the D summand, which survives beta2, k0 is already zero. This theorem
alone therefore supplies no vanishing conclusion for the original fourth
or later obstruction.

## 6. Verification limits

verify.py authenticates exact inputs, checks symbolic universal synthetic
chain identities (including first correction and the minus sign in (3)),
checks multiplication compositions with unspecialized binary coefficients,
and checks characteristic-polynomial character arithmetic and Chern data.
It selects no actual HM coefficient, point, parameter, jet, matrix or
instance rank.
The written actual-map identifications depend on the pinned geometric
proofs; the script is not proof-assistant certification.
