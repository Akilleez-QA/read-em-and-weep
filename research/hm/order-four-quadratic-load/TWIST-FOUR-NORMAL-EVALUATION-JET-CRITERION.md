# The fifty normal evaluations are degree-one evaluations on the doubled torsion divisor

## Setup and current checked sources

Use the common-open geometry of TWIST-FOUR-KERNEL-ELEMENTARY-PRESENTATION.md (ddb6cd3e6f4bb0e24e1e5009ca95cb7e568f2c45), the exact forty-five-dimensional common-value space (a0540d89b6a8df1077251d320a0821c3a432706a), and the canonical torsion-square factorization (712e933c2b7e3f70ce1610113be78ea17028f02a).

On W let D be the union of fifty disjoint torsion lifts D_i, J the unmodified graph curve, and P_i=J intersect D_i its single transverse intersection with each lift. Put L=L4, M=L-J, B=L-2D, and G=B-J=M-2D. The established restrictions are

    L|D_i=O_P1(2),    M|D_i=O_P1(1),    M(-D)|D_i=O_P1(6).

All fifty P_i lie over distinct modular parameters. The actual common-value space H0(Y,A4) has dimension45 and injects by its B-divisor boundary into H1(W,G), of dimension485. The multiplication kernel in that latter space is the injective boundary image of H0(2D,M|2D), of dimension450.

## 1. The intrinsic degree-one representative

Take a common-value section whose boundary lies in this torsion image. It has a unique global lift u in H0(Kplus), because H0(W,M)=0. The common-value graph condition says u|J is divisible by the canonical section of 2D|J. Consequently u vanishes on J intersect 2D. The graph equation j is a nonzerodivisor on O_{2D}, since J has no component in D. The Cartier divisor sequence on 2D therefore gives a unique section

    t in H0(2D,M|2D),    u|2D=j*t.

Up to the harmless common sign determined by the boundary convention, this is precisely the representative of its boundary class in the injective torsion image. It is not a freely chosen neighborhood section.

Near P_i use regular parameters x,j on W, with x cutting out D_i and j cutting out J. Then u can be written

    u=j*t + x²*b.

The required doublepoint condition at P_i is u in (x,j)². Its constant and x-linear terms already vanish by this expression, and the remaining j-linear term vanishes exactly when

    t(P_i)=0.

Thus the actual fifty normal-direction functionals are ordinary evaluations of the degree-one restrictions t|D_i at their distinguished graph points. This identification is independent of the choices of local parameters and trivializations: changing them multiplies the relevant one-dimensional value by a unit.

Equivalently, u|D_i is a scalar multiple of j²|D_i, because it is a quadratic section with a double zero at the unique point P_i. The scalar belongs intrinsically to the one-dimensional space H0(D_i,L(-2J)|D_i); no simultaneous scalar normalization is asserted.

## 2. A specified four-hundred-dimensional subspace

Define

    T0=ker[H0(2D,M|2D) -> directsum_i M|P_i].

Restriction to D and the doubled-divisor sequence identify T0 as an extension

    0 -> H0(D,M(-D)|D) -> T0 -> H0(D,M|D(-sum P_i)) -> 0.

Surjectivity follows from H1(D,M(-D)|D)=0. The first space has dimension350 and the last dimension50. Hence dim T0=400. This is a specified subspace, not an abstract subspace in general position.

Combining Section1 with the torsion-square boundary proves the exact criterion

    H0(K4) = image[H0(Y,A4) -> H1(W,G)]
             intersect image[T0 -> H1(W,G)].

The two images have dimensions45 and400 inside a space of dimension485. The embedding of T0 is injective because H0(W,M)=0. This criterion retains the actual divisors, graph points, and neighborhood maps. Merely comparing the three dimensions does not prove the intersection zero.

## 3. Why paired torsion lifts do not supply an automatic relation

The deck involution of W->S(5) exchanges the two lifts over each torsion section. It preserves the modular parameter. However the marked point on one lift and the marked point on its paired lift have distinct modular parameters on the established common open. Thus the involution does not preserve the marked fifty-point set; the image of P_i is not the marked point of its paired lift.

Furthermore L contains the fixed-coordinate hyperplane h, and no deck-linearization of L has been established. An involution of the underlying surface alone does not act on its space of sections without a compatible line-bundle identification. Neither equality of paired constants nor a linear relation between the paired evaluation functionals follows from the pairing of the curves.

This supplies an actual jet-level injectivity criterion, but no claim of independence of the fifty evaluations, transversality of the displayed intersection, or a complete proof repair.
