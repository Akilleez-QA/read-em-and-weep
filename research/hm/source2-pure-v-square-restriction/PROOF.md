# Pure-V quotient-third restriction and the original-fourth complement

## New deduction and scope

Conditional on the Q-compatible pure-V source2 branch of PR1025, restriction
of the two-dimensional quotient-third gate to the discriminant conic is an
isomorphism onto its full two-dimensional equivariant target. Consequently
composition with the inherited universal L gives a two-dimensional subspace
of the old four-channel original-fourth space that maps isomorphically onto
ALL its square-restriction channels. It intersects the two-dimensional
square-invisible subspace trivially and provides a complement to it.

This is a constraint on the allowed universal gate. It determines neither
coefficient of the actual map and does not prove actual fourth vanishing,
nonvanishing, any source occurrence or exclusion. No direction, point, or
actual coefficient is chosen or evaluated.

## Inputs and novelty boundary

PR1025, commit 09f1377f83b027ca27eea0b3a9f40a1b92c6c466, proves

  s:P O_X(-3) -> J=I_Z(6),  X=P(A),
  0 -> A O_X(-2) + O_X(-5) -> D O_X(-1) -> J -> 0,
  iota beta4|D = -s L.

It also proves dim Hom_G(P,H0(J(3)))=2 and unique quadratic lifting.
The PR1000 proof in source126-typeII-octic-zero-scheme proves that Z has
length34 and is disjoint from the discriminant conic Delta. PR966 gives
L:D O_X(-1)->P O_X, with cokernel supported at the order-three axes,
all off Delta. In particular L|Delta is surjective.

The old FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING.md, pinned at
2f81e3510505ad842fb9bb00ff3a667cd36ea17f, already gives
Q4=Hom_G(D,H0(I_Sigma(10))) of dimension4, with a dimension2 kernel
of square restriction and dimension2 image Hom_G(D,Sym20 W).
FOURTH-SQUARE-CHANNELS-HAVE-A-C5-DETECTION-FILTRATION.md and
FOURTH-GATE-ONE-AXIS-JET-AND-ONE-SQUARE-FIBER.md were checked for novelty:
they describe detection of the unrestricted fourth space, not its new
pure-V two-dimensional transverse subspace. Those old detection statements
and all old scheme calculations are inputs, not new results here.

## 1. Cohomology retaining the nonzero connecting term

The discriminant is an invariant quadratic equation delta. Since Z misses
Delta, tensoring the divisor sequence with I_Z(9) gives exactly

  0 -> J(1) --delta--> J(3) -> O_Delta(9) -> 0.       (1)

There is no Tor correction: I_Z is locally free in a neighborhood of Delta,
and delta is a nonzerodivisor on the torsion-free I_Z. The notation O_Delta(9)
is the plane twist, hence pulls back to O_P1(18), not O_P1(9).

Twisting the inherited resolution by one gives

  0 -> A O(-1) + O(-4) -> D O -> J(1) -> 0.

P2 line-bundle cohomology yields

  H0(J(1))=D,  H1(J(1))=H2(O(-4))=A,  H2(J(1))=0.

Equivariant Serre duality has no determinant-character correction: the
three-dimensional A representation has trivial determinant. Also A is
self-dual. Twisting the resolution by three shows H1(J(3))=0. Thus (1)
gives the representation exact sequence

  0 -> D -> H0(J(3)) -> Sym18 W -> A -> 0.          (2)

In particular restriction on ALL sections is not onto: its cokernel is A.
The dimensions are 5,21,19,3, with alternating sum zero.

Taking Hom_G(P,-) in characteristic zero is exact. Both Hom_G(P,D) and
Hom_G(P,A) vanish. Hence

  Hom_G(P,H0(J(3))) -> Hom_G(P,Sym18 W)              (3)

is an isomorphism. Its kernel dimension is zero and image dimension two.
The exact character decomposition independently gives

  Sym18 W = A + V + 2P + D.

Therefore no nonzero allowed s vanishes identically along Delta. This does
not assert that a nonzero s is nonzero at every individual square direction.

## 2. The induced splitting of the four-channel original-fourth sequence

Write C=coker B=I_Sigma(6). The canonical inclusion j:J->C is an
isomorphism near Delta, because its quotient is coker L and this is
supported away from Delta. Define the linear map

  T:Hom_G(P,H0(J(3))) -> Q4,  T(s)=-j s L(-3).

Twists are D(-4) --L(-3)--> P(-3) --s--> J --j--> C.
Thus T has exactly the original fourth degree and codomain; it is not a
choice of a four-channel projection. Its agreement with the actual fourth
in this branch is the previously proved corrected-lift identity.

On Delta, L(-3) is surjective and j is an isomorphism. Consequently
T(s)|Delta=0 if and only if s|Delta=0. By (3) this holds if and only if s=0.
Thus square restriction composed with T is injective. The source and the
old square-restriction target each have dimension2, so it is an isomorphism:

  res o T : Hom_G(P,H0(J(3))) -> Hom_G(D,Sym20 W).    (4)

The old exact sequence is

  0 -> K_delta -> Q4 --res--> Hom_G(D,Sym20 W) -> 0,
  dim K_delta=2,  dim Q4=4.

Put S_pureV=im T. Then

  Q4 = K_delta direct-sum S_pureV,
  dim S_pureV=2,  S_pureV intersect K_delta=0.

The resulting right inverse to res is T(res o T)^(-1). It is defined by
the inherited maps, without choosing a basis of coefficients. Rescaling
T does not change its image or this right inverse. No claim is made that
a coordinate splitting previously used in the unrestricted four-channel
space agrees with this inherited complement. In arbitrary old coordinates,
the two square-invisible coefficients are linear functions of the two
square coefficients; they are not necessarily individually zero.

In particular, for the actual conditional gate on the surviving D summand,

  beta4|Delta=0  iff beta4=0 iff s=0 iff R=0.

Every statement refers to the entire source-family restriction. It neither
supplies a vanishing test on one chosen vector nor covers the additional
specialized A-kernel at the six second-rank-drop axes.

The L used here is the PR1025 multiplication map D(-1)->P, not the
D(-3)->A(-2) third lifting correction also denoted L in the old fourth
proof. These two different maps are not identified.

## 3. Reproducibility

verify.py uses exact A5 character arithmetic and the SU2 even-symmetric-power
recurrence, together with line-bundle cohomology dimensions and twists.
It checks the multiplicities, cohomology Euler dimensions, and two-plus-two
linear-algebra consequence. The sheaf exactness and the surjectivity of L
on Delta are proved above from the stated inputs, not inferred from finite
matrix tests. The test is not a formal verification of the full proof.
