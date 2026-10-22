# The actual upper quartic is the quintic-extension Gram composite

## Result

Let i be the actual quadratic inclusion in the nonsplit quintic-relation sequence

    0 -> V O_L(-3) --i--> P4 O_L(-1) -> O_L(5) -> 0.

Choose invariant nondegenerate symmetric pairings on V and P4. The actual upper-entry multiplication map from the squared-factor theorem is

    M_kappa: V O_L(2) -> V O_L(6).

There is a nonzero scalar c such that

    M_kappa=c i^t(3) i(5).                         (1)

The twists mean i(5):V O2->P4 O4 and i^t(3):P4 O4->V O6. This identifies the actual map with a natural composite, not merely with an unspecified nonzero quartic channel. Its nonzeroness comes from the already proved actual multiplication map, not from assuming a composite of nonzero maps is nonzero.

Moreover, as a twisted endomorphism of V, it satisfies

    M_kappa^3=(det M_kappa) identity_V.             (2)

At each of its twelve exceptional fibers it is regular nilpotent, after any choice of scalar identification of the source and target line fibers. These assertions concern the actual upper connection factor. They do not evaluate the full third Bockstein.

## 1. The unique scalar primitive as a global lift

The actual map h->n_h from D5 to H0(V O6) is supplied by multiplication with kappa=(d_L f)/g. Dualizing the quintic relation sequence and twisting by3 gives

    0 -> O_L(-2) -> P4 O_L(4) --i^t(3)--> V O_L(6) -> 0.  (3)

The obstruction to lifting n_h is in H1(O_L(-2))=1. The obstruction map is equivariant from D5, so it is zero. Since H0(O_L(-2))=0, every n_h has a UNIQUE global lift. Together they define

    L:D5 O_L -> P4 O_L(4).

This also identifies the scalar Cech primitive directly. If p_ij is the actual quintic transition class and tau is the invariant quadratic pairing on V, then tau(p_ij,n_h) is the obstruction cocycle in O_L(-2). The unique lift above supplies its unique local primitive. In the original, nondual sequence this is the unique extension of the functional V O(-3)->O3 given by n_h to P4 O(-1)->O3, evaluated on the local quintic lifts. Signs and common pairing scalars follow the chosen dual-sequence convention.

## 2. Descent through the cubic quotient

The actual quartic restriction sequence is

    0 -> Wprime O_L(-3) -> D5 O_L --Q--> V O_L(2) -> 0.

The identity n_h=M_kappa(Qh) implies that L restricted to ker Q lands in the kernel O_L(-2) of (3). But

    Hom_G(Wprime O_L(-3),O_L(-2))
      = (Wprime^* tensor H0(O_L(1)))^G = 0,

because Wprime and W are inequivalent irreducibles. Therefore L factors uniquely as T Q, with

    T:V O_L(2) -> P4 O_L(4).

Its equivariant Hom space is one-dimensional:

    Hom_G(V O2,P4 O4)=(V tensor P4 tensor A)^G=1,

using V tensor P4=A plus P4 plus D5. The actual i(5) is a nonzero element of this space. Thus T=c i(5). Since i^t(3) T=M_kappa is nonzero, c is nonzero. This proves (1).

Consequently the rank-three lift T is a subbundle inclusion everywhere, with cokernel O_L(10), by the original exact sequence twisted by5. Rank loss in M_kappa occurs when this actual image meets the kernel line O_L(-2) of the dual projection, not because either factor ceases to be a subbundle map.

## 3. Characteristic identity and the exceptional fibers

The trace of M_kappa is an invariant section of O_L(4). It is zero because Sym^4 W=D5 has no invariant. Similarly tr(M_kappa^2) is an invariant section of O_L(8), and

    Sym^8 W=P4 plus D5

has no invariant. The rank-three Cayley-Hamilton identity therefore reduces to (2). This uses only representation arithmetic and the universal characteristic identity, with no map coefficients evaluated.

The actual determinant is nonzero and has one reduced twelve-point zero orbit, as proved by multiplication on the integral cubic support. At each such point the actual map has rank2. Equation(2) then makes it a nilpotent endomorphism of rank2 on a three-dimensional space, hence a single length-three Jordan block. In particular its square has rank1 and gives the intrinsic flag ker M subset ker M^2. Scaling a local identification of O_L(4) does not change this flag.

Crucially, the cube in (2) is matrix composition after the stated pushforward-bundle identifications. It is NOT multiplication by kappa^3 on D: kappa carries the nontrivial torsion-line factor O_D(-2,2) in addition to its base twist. Consequently (2) does not identify the genus-four cubic support with a cyclic triple cover, and no assertion about such a cyclic cover follows.

Equivalently, the kernel line of i^t(3) meets the image hyperplane of i(5) exactly at these twelve points. Under the symmetric pairing this says that the corresponding quotient line is isotropic. The determinant's simple zeros supply transversality; no independent assertion about a chosen matrix or coordinate root is needed.

## Dependencies and verification

The actual quintic sequence and its nonzero inclusion are from VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md. The actual multiplication, n_h, and the determinant/rank facts are from ACTUAL-CONE-UPPER-CONNECTION-HAS-A-SQUARED-FACTOR.md. The scalar primitive also applies to the diagonal term of ACTUAL-NORMAL-OPERATOR-SQUARE-SHADOW-BY-HARMONIC-TRANSITION.md.

The companion verifier checks all representation multiplicities, line twists, and the universal rank-three characteristic identity. It does not instantiate HM coefficients or perform an actual map or rank evaluation. The remaining off-diagonal scalar-extension contribution is not removed by (1) or (2).
