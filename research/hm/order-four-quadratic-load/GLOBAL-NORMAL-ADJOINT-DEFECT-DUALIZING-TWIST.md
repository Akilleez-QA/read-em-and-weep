# The global normal adjoint defect and its dualizing twist

## Statement

Let X be the smooth weighted stack P(1,1,2,2), let G be the actual rank-two Serre bundle with determinant L=O_X(2), and let sigma be its regular section with zero ideal I. Write B=End_0(G), and let N be the associated square-zero section of B tensor L. Define the tangent-modulo-conjugation sheaf

    M=ker(B tensor L --tr(N·)--> L^2)
        /im(ad N:B -> B tensor L).

There is an intrinsic isomorphism

    M = Ext^2_X(O_(2Z),O_X) tensor L^(-1)
      = omega_(2Z)(1),                              (1)

where 2Z is the ORDINARY square thickening defined by I^2. Its dualizing sheaf need not be invertible. In particular this is not a sheaf supported only on reduced Z.

For first-normal corrections N_tilde=N+qT, with q of physical degree two, the corresponding defect sheaf is

    M(-2)=omega_(2Z)(-1).                           (2)

This identifies the determinant and normal-equation line factors omitted by a bare local presentation I/(f^2,g^2). It does not prove that local formulas glue to a specified bundle or that the positive cubic obstruction vanishes.

## 1. Identify the tangent kernel and gauge map intrinsically

The canonical rank-two identification B tensor L=Sym^2 G takes N to sigma^2. Multiplication by sigma gives an injection

    G -> Sym^2 G.

Its image is exactly the tangent kernel of the quadratic discriminant at sigma^2. Locally sigma=(f,g), with f,g a regular sequence; the two regular syzygies are the matrices S1 and S2 in REGULAR-NILPOTENT-COMMUTATOR-DEFECT-IS-SQUARE-DUALIZING-MODULE.md. Thus this kernel identification remains valid along Z, not only where sigma is nonzero.

Under it, ad N corresponds, up to the fixed nonzero scalar two and a common sign, to

    B -> G,  X -> X sigma.

Consequently

    M=coker(Sym^2 G tensor L^(-1) -> G).            (3)

No assertion that an arbitrary tangent discrepancy is a commutator is used; (3) retains the cokernel measuring precisely that failure.

## 2. Dualize the square-ideal resolution

The regular pair gives the global Hilbert--Burch resolution

    0 -> G* tensor L^(-1) -> Sym^2 G* -> I^2 -> 0.

Dualizing, and using 0->I^2->O_X->O_(2Z)->0, identifies

    Ext^2_X(O_(2Z),O_X)
      =coker(Sym^2 G -> G tensor L).

The map is the determinant-twisted version of the map in (3), as can be checked in a regular generator frame. Tensoring (3) by L proves the first equality in (1). The construction uses the global bundles and evaluation by sigma, so it is unchanged by quintic-generator changes, Koszul stabilizers, or different local orientations.

The square of a codimension-two regular ideal is Cohen--Macaulay of codimension two by this resolution. Since X is smooth of dimension three, its dualizing sheaf is

    omega_(2Z)=Ext^2_X(O_(2Z),omega_X).

Here omega_X=O_X(-3) in physical twists. Therefore Ext^2(O_(2Z),O_X)=omega_(2Z)(3). Combining with L^(-1)=O_X(-2) proves M=omega_(2Z)(1). Finite G is perfect, so there is no omitted G-character in this canonical line identification. If a larger block torus is retained, its determinant characters must still be retained in omega_X and L rather than discarded.

## 3. First-normal corrections have an additional shift

The actual section N has twist two, while q has twist two. Thus a first-normal correction T has twist zero. A normal change of frame is 1+qX with X of twist minus two, and changes T by [X,N]. The entire tangent/gauge complex in Section 1 is consequently twisted by O_X(-2). This proves (2).

The annihilator of this defect sheaf is I^2, by the regular-sequence local calculation. This supplies a coordinate-independent home for the nongauge Hessian gluing residue. It does not make that residue zero.

## 4. A precise dual cohomology formulation, not a vanishing assertion

Proper Cohen--Macaulay duality on the one-dimensional tame stack 2Z gives, for every physical integer t,

    H1(M(-2)(t)) = H0(O_(2Z)(1-t))* .              (4)

The same statement holds after taking G-invariants in characteristic zero. Thus a first-normal adjoint-defect obstruction of twist t can be studied through sections of the explicitly specified ordinary square thickening.

No vanishing of the right side is asserted here. On a nonreduced curve, negative twists can have nilpotent sections; reduced-support negativity is insufficient. Nor does (4) identify the full differential-operator lifting obstruction with this one quotient sheaf without checking the surrounding complex. These are remaining comparisons, not consequences of duality alone.

## Reproduction and scope

The local syzygy and commutator identities are verified in verify_regular_nilpotent_commutator_defect.py. The global argument above supplies the line factors, and verify_global_normal_defect_twists.py checks their arithmetic. No actual HM coefficients, multiplication matrices, or ranks are evaluated.
