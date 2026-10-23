# A two-dimensional pure-V quotient-third gate with exact original-fourth comparison

## Theorem and boundary

Retain the conditional Q-compatible nonzero pure-V source2 branch. Let M
be the original family, I=im j its image subcomplex, and U=M/I the genuine
quotient. The quotient-second theorem gives H0(U)=A+P, H1(U)=P,
beta1,U=0, and beta2,U=[B,0], where B is the original second map on A.

The quotient third is a global equivariant sheaf map

    s:P O_X(-3) -> J,          X=P(A),                         (1)

where J is the canonical subsheaf im L/im B of coker B. It has the exact
presentation

    0 -> A O_X(-2) + O_X(-5) -> D O_X(-1) -> J -> 0.           (2)

The direct sum in (2) is an actual splitting of the displayed kernel,
not an assumed splitting of the source module. The sheaf J is the already
known I_Z(6), with Z the length34 scheme of PR1000. In particular this
packet does not rediscover that scheme or claim new support multiplicities.

The space of possible equivariant maps (1) has dimension EXACTLY TWO.
Every such map has a UNIQUE equivariant homogeneous quadratic lift

    R:P O_X(-3) -> D O_X(-1),             s=[L R].             (3)

These are universal linear spaces; no coefficients of the actual s or R
are determined here. With the natural endpoint identification iota induced
by j4, the original fourth on its surviving D summand satisfies

    iota beta4,M,a(d) = -s_a(L_a d)                           (4)

in the original second-symbol cokernel, with canonical identifications of
the P spaces made below. Hence the original fourth on D vanishes identically
if and only if s=0, equivalently R=0. This is a two-dimensional reduction
of that conditional fourth gate, NOT its evaluation or a source exclusion.
No additional specialized A-kernel at a second-rank-drop direction is
claimed covered by (4).

## 1. Exact dependencies and normalization

INPUTS.json retains exact public proofs for PR950, PR966, PR1000, PR1019
and the original third-vanishing theorem. PR1019 is pinned at
3fb2475ffb275c5789acbaa8f9f84ed272713785. The quotient-second proof is
PR1022 at 5488bc153029391d647c3e18d9344e4e00e38a7f, retained unchanged
as a separate immutable dependency.

All original actual-source, bundle and fixed-variable hypotheses remain
in force. The new quotient-third claim is separate from the frozen first
and second packets. Their proofs and verifiers are not modified here.

At t=0 write q for Q and T_a for negative-quadratic multiplication. Then

    I=[D --t L_a--> I1],      I1=im j4=P,
    L_a(d)=[a d] in Sym6 W/V6,
    ker j4=im q,             q|D=0.

The quotient long sequence gives H0(U)=A+P and a connecting isomorphism
from its P-isotypical summand to I1. Let sigma:I1->H0(U)_P be its inverse.
We henceforth identify this SOURCE P with I1 via sigma. The descended
radical f:U->I gives f0 on degree-zero vector spaces and f1 on degree-one
vector spaces. Its induced H0 map is zero and its induced H1 map is an
isomorphism. Use that latter isomorphism to identify the TARGET H1(U)
with I1 as well. In these conventions the actual endpoint identities are

    f1 qbar=0,                f1 Tbar_a=L_a f0.               (5)

The identification H1(M)->I1 is iota([y])=j4y. PR1019 proves

    B_a(x):=iota beta2,M,a(x)=-mu [a^2 x],      mu != 0.

Set m_a(x)=a x from A to D. Thus B=-mu Lm and im B=im(Lm).
Only this nonzero scalar identification is used; no value of mu is chosen.

## 2. Global quotient corrections and global naturality

Because qbar is a fixed G-equivariant linear map, choose equivariant
constant splittings of its image and kernel. These give global polynomial
correction operators, with no denominators in the quadratic direction a.
Let x0:P->ker qbar be the canonical P inclusion sigma. Choose successive
corrections x1(a), x2(a), homogeneous of degrees one and two, satisfying

    qbar x1=-Tbar_a x0,
    qbar x2=-Tbar_a x1.                                       (6)

The first equation is soluble globally because beta1,U=0. The second is
soluble globally because beta2,U vanishes on P: the right side belongs
to im qbar, and a fixed equivariant inverse on im qbar supplies x2.

The quotient third is represented by [Tbar_a x2] in H1(U), modulo im B.
This gives a global map P O(-3)->coker B. Ordinary correction-choice
changes alter it only by B times a linear A-valued correction, so its
class is the canonical third symbol.

Apply the ACTUAL endpoint identity (5), before taking any fiber ranks:

    f1 Tbar_a x2 = L_a f0 x2.                                 (7)

Therefore the raw transformed representative lands in im L globally.
Modulo im B its class lands in J=im L/im B, as claimed. Equation(7) is
also a direct representative-level verification of the relevant
sheaf-page naturality: the E3-target map coker B->coker L annihilates s.
No inference from generic fibers to a torsion sheaf is used.

In fact R_a=f0 x2(a) already supplies an equivariant quadratic lift in(3).
Section4 proves this lift is unique among all equivariant quadratic lifts,
independently of the initial choices of equivariant qbar splittings.

## 3. Exact kernel resolution and identification of J

The universal image map has an exact sequence

    0 -> O(-5) --kappa--> D O(-1) --L--> P O -> C_L -> 0,       (8)

where C_L has length10 and is supported at the reduced order-three axes.
This is the universal rank-drop result of PR966. To spell out the kernel
bundle: L has rank4 off those points and rank3 at them. Near a rank3 point
it reduces to three identity rows and a one-by-two row (u,v) generating
the maximal ideal, since its maximal-minor scheme is reduced. Its kernel
is generated by (-v,u), hence locally free of rank one. Off the finite
set the determinant equation identifies that line with O(-5), and this
identification extends on the smooth surface. The equivariant line has
no character ambiguity because the projective group A5 has no nontrivial
characters.

Let m:A O(-2)->D O(-1) be ordinary multiplication. It is everywhere
injective on fibers. The original B=-mu Lm is injective as a SHEAF,
though its fibers drop rank at six points. Therefore im m intersects
ker L trivially as sheaves. The preimage of im B under L is exactly

    im m + ker L = im m direct-sum im kappa.

Indeed a local section mapped into im B can be corrected by a local
m-section to land in ker L; the intersection is zero because Lm is
sheaf-injective. Thus the map (m,kappa) yields the exact sequence (2).
This supplies a concrete split preimage, without an arbitrary splitting
of U or an ambient horizontal extension. Equivalently the abstract
preimage extension splits by H1(A O(3))=0, but the actual direct-sum maps
above are available here.

The quotient bundle E from multiplication is defined by

    0 -> A O(-1) --m--> D O -> E -> 0.

Projecting kappa to E(-1) gives an injective sheaf map O(-5)->E(-1),
or a nonzero invariant section of E(4). PR1000 identifies the unique
invariant line of such sections and its length34 zero scheme Z. Hence
its quotient is I_Z(6), and this is exactly J in(2). This identifies the
actual canonical subquotient with that previously analyzed universal
sheaf, not merely with a sheaf having matching Chern classes.

The inclusion J->coker B and quotient to C_L are exact. PR1000's Z consists
of six length-four complete intersections at the order-five axes and ten
reduced order-three axes. This older scheme result is retained, not counted
as a new finding of this packet.

## 4. Exact two-dimensional gate and unique quadratic lift

Twist (2) by three:

    0 -> A O(1) + O(-2) -> D O(2) -> J(3) -> 0.               (9)

On P2, H1(O(k))=0 for all integers k. Thus taking global sections gives
a surjection D tensor Sym2 A -> H0(J(3)), with kernel A tensor A.
Taking G-equivariant Hom from P remains exact in characteristic zero.
The exact character multiplicities are

    dim Hom_G(P,A tensor A)=0,
    dim Hom_G(P,D tensor Sym2 A)=2.

Therefore Hom_G(P,H0(J(3))) has dimension two, and the lifting map from
the second Hom space is an isomorphism. This proves both dimension and
uniqueness in(3). In particular the kernel ambiguity through kappa has
no global section because its source twist is O(-2), and the ambiguity
through m has no P-isotypical section because A tensor A=1+A+D.

Nothing in this representation calculation picks the two actual scalar
coefficients. The result is an exact ambient two-dimensional gate, not
a conclusion that every allowed universal map occurs for an actual source.

## 5. Exact comparison with the original fourth

Fix d in D and choose x in M0 lifting sigma(L_a d), so that

    q x = T_a d.

As in the quotient-second proof, beta1,U=0 and I1 subset im q imply that
T_a x belongs to im q. Choose y with qy=-T_a x. The quotient class of y
is a first correction for sigma(L_a d). Since beta2,U(P)=0 and
H1(M)->H1(U) is an isomorphism, T_a y belongs to im q as well. Choose z
with qz=-T_a y. Its quotient is a second correction.

The original successive lifts are

    d, -x, -y, -z.

Their q equations cancel consecutive T terms. Its fourth representative
is therefore -T_a z. The quotient third at sigma(L_a d) is represented
by Tbar_a bar z. Applying f1 to the latter and iota to the former gives
opposite classes in coker B. This proves(4), including its sign.

Original first and third vanishing and original second vanishing on D
ensure this original fourth is defined on the surviving D sheaf. All
correction ambiguities are precisely the lower-symbol images; on the
original target only im B remains. The construction can be made globally
polynomial using fixed equivariant q splittings, so(4) is a homogeneous
sheaf identity, not merely a pointwise comparison on a generic chart.
Its degrees are 1+3=4, or 1+2+1=4 using the unique R lift.

Finally L is generically onto by PR966. If the original fourth on D is
identically zero, (4) makes s zero generically. Its target J is torsion-free
since J is a subsheaf of the torsion-free original coker B. Hence s=0
globally. The converse follows directly from(4), and s=0 iff R=0 by
Section4. This equivalence does NOT supply a value for that gate.

## 6. Verification boundary

verify.py checks source digests, universal corrected-lift signs and exact
chain identities, the split kernel bookkeeping, the exact A5 character
multiplicities, and the resolution Hilbert polynomial and twists. The
symbolic chain tests use independent indeterminates in synthetic matrices,
not actual HM coefficients, points, source parameters or instance ranks.
The geometry of the sheaf identifications comes from the written argument
and the authenticated original proofs, not from a numerical experiment.
