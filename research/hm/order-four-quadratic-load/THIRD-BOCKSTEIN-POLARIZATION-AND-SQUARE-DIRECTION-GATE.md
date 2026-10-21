# Third Bockstein polarization and the square-direction channel

## New constraints

The actual second scalar is nonzero. Hence the remaining third obstruction is the global map D5 O_P(A)(-3)->I_Z(6), where Z is the length24 second-symbol degeneration scheme, disjoint from the discriminant conic Delta of square binary quadratics.

Two precise constraints hold:

1. The proved nonzero antisymmetry coefficient c cancels from the polarized third obstruction through the explicit correction below. It does not by itself choose a nonzero third channel.
2. The two-dimensional space of equivariant third gates has a canonical one-dimensional subspace of gates vanishing on Delta. The quotient is detected by any square direction. A nonzero quotient channel is nonzero at every square direction, so it supplies the final rank at order three there and generically.

No claim is made that the actual quotient channel or the discriminant-divisible channel is nonzero.

## 1. Explicit cancellation of the antisymmetric correction

For h in D5 and a,b in A, the actual second-order D-input vanishing implies

    [a h zeta_b]=0 in P4.

Indeed polarization gives vanishing of the sum with [b h zeta_a]; their difference is c h(a cross b)xi, whose P4 class is zero by the first-Bockstein vanishing. Therefore choose v_(a,b,h) with

    q0 v_(a,b,h)=a h zeta_b.

The established identity a zeta_b-b zeta_a=c(a cross b)xi gives

    v_(a,b,h)-v_(b,a,h)=c h zeta_(a cross b) modulo K,

where K=(A+D5)xi is the original kernel. Multiply by any d in A and project to P4. The K ambiguity contributes zero by beta1=0, while the displayed correction contributes

    c[d h zeta_(a cross b)]=0

by the polarized D-input identity just proved. Thus the third quotient is insensitive to this interchange. Equivalently one may replace v_(a,b,h) by its symmetrized version, with the explicit half-correction c h zeta_(a cross b)/2, without changing the third P4 class.

This is an actual associativity constraint. In particular the known fact c!=0 cannot be turned into third nonvanishing by keeping an antisymmetric term that already dies in the second-order quotient.

## 2. Exact restriction of the two third channels

Let delta be the discriminant equation, of degree two on P(A). Since Z is disjoint from Delta, there is an exact sequence

    0 -> I_Z(7) --delta--> I_Z(9) -> O_Delta(9) -> 0.

The Hilbert--Burch sequence of the second symbol, twisted by one, is

    0 -> A O(-1) -> P4 O(1) -> I_Z(7) -> 0.

It gives H1(I_Z(7))=0 and H0(I_Z(7))=P4 tensor A=V+P4+D5. The third-gate calculation gives H0(I_Z(9))=A+2V+3P4+2D5. Taking equivariant Hom from D5, an exact operation for the finite group, therefore yields

    0 -> C -> C^2 -> C -> 0.

The first line consists exactly of discriminant multiples. The final line is the unique D5 channel in H0(O_Delta(9))=Sym^18 W, since Delta is the quadratic Veronese P(W)->P(A). Thus the quotient channel is precisely the actual restriction of beta3 to square directions; this is not a freely chosen scalar decomposition.

## 3. Nonzero square restriction has no basepoints

A nonzero equivariant map D5->Sym^18 W is injective. If its five binary forms had a common zero, their greatest common divisor would have a nonempty G-invariant divisor on P(W), of degree at most18. For the faithful projective A5 action on P1, a point stabilizer is cyclic (the derivative at a fixed point is faithful for a finite subgroup), hence has order1,2,3 or5. The orbit sizes are therefore60,30,20 or12. Consequently the only possible nonempty invariant divisor of degree at most18 has degree12. Equivalently, the group being perfect, its defining binary form is invariant up to a trivial character.

Dividing the five forms by that invariant degree12 factor would give a nonzero equivariant injection D5->Sym^6 W. This is impossible because Sym^6 W=V+P4. Hence the five forms have no common zero.

Consequently, if the actual third quotient channel is nonzero, beta3 is a nonzero D5-to-line map at EVERY square direction. The second Bockstein has rank three at those directions, so this adds the last target rank at order three. If the actual square restriction vanishes, beta3 can still be a nonzero discriminant multiple, but only that single remaining channel is available.

## Scope

These constraints do not settle the actual third coefficient. The remaining geometric primitive is being tracked separately. The argument retains I_Z rather than treating the third target as a line bundle at the six special second-order axes, and does not infer flat deformation of a rank-one image from nilpotence.
