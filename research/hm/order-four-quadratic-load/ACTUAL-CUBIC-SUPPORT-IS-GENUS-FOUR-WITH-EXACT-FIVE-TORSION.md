# The actual cubic support is a smooth genus-four curve with exact five-torsion

## Result

Let D=(f=0) in P(Wprime) times P(W) be the actual cubic divisor appearing in the homogeneous vertex Serre presentation. Then D is a smooth integral curve of genus four. Its two projection pencils have degree three, and

    K_D=O_D(1,1),    T=O_D(1,-1),    ord(T)=5.

The canonical model is a complete intersection of a smooth quadric and a cubic in P3. These are statements about the actual support of the double-cubic operator-residue description, not a selected numerical curve or a claimed solution of the remaining positive obstruction.

The order-five assertion concerns D. It must not be extended automatically to the ambient line O_(2D)(1,-1) on its square thickening.

## 1. Actual geometric inputs

The actual cubic relation has bidegree (3,3), and is nonzero on every fiber of the second projection. Thus D is finite flat of degree three over L=P(W). The actual quintic generator has local bidegree (5,-5), with changes g'=g+p f. Fiberwise regularity of the cubic/quintic pair implies that g has no zero on D. Hence the local quintics glue there to a nowhere-zero section of O_D(5,-5).

These are the actual generator and regular-pair inputs of VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md, with uniformity established there from INVARIANT-CONE-UNIQUE-VERTEX-MODULE.md and VERTEX-EXT-ANNIHILATOR-LENGTH-EIGHT.md. The double-cubic pushforward note retains their actual nonsplit transitions; no arbitrary divisor of bidegree (3,3) is substituted.

## 2. Irreducibility and reducedness

Finite degree three over L permits at most three distinct irreducible components. The projective A5 action cannot permute a set of at most three nontrivially. Equivalently its perfect binary lift has no nontrivial homomorphism to a subgroup of S3. Each component is therefore G-stable.

A component of bidegree (a,b) has an equation spanning a G-stable line in

    Sym^a(Wprime) tensor Sym^b(W),    0<=a,b<=3.

Perfectness of G makes that line invariant. But the powers in this range are

    Sym^0 W=1, W, A, S4,
    Sym^0 Wprime=1, Wprime, V, S4.

The only common nontrivial representation in these two lists is S4, at (a,b)=(3,3). Thus the only nonconstant invariant bidegree in the indicated rectangle is (3,3). A proper component, including the reduced support of a multiple divisor, is impossible. Consequently D is integral and reduced.

## 3. Smoothness and the canonical curve

Adjunction on P1 times P1 gives arithmetic genus

    p_a(D)=(3-1)(3-1)=4.

For an integral complex curve the total singularity delta invariant is p_a minus the genus of the normalization, so is at most four. Every singular point contributes at least one.

On either projective line, the faithful projective A5 action has point stabilizers cyclic of orders at most five. One elementary justification is that a finite stabilizer acts faithfully on the tangent line at its fixed point in characteristic zero. Thus its point orbits have size at least twelve. A point orbit in the product has at least the size of either projected orbit. A singular point of D would consequently produce at least twelve singular points, contradicting the delta bound. Hence D is smooth of genus four.

Adjunction now gives K_D=O_D(1,1). The Segre line O(1,1) is very ample, and its four sections restrict to the complete canonical system: the kernel sequence has O(-2,-2), with vanishing H0 and H1. Thus the canonical image lies on the smooth Segre quadric. A divisor of type (3,3) on that quadric is cut by a cubic surface, because H1(P3,O(1))=0. This gives the canonical complete intersection of degrees two and three. The two projections give distinct basepoint-free degree-three pencils.

## 4. Exact order five

The nowhere-zero quintic on D trivializes T^5. To show that T itself is not trivial, use

    0 -> O(-2,-4) -> O(1,-1) -> O_D(1,-1) -> 0.

The ambient H0 of O(1,-1) vanishes. Kunneth gives H1(O(-2,-4))=0: each of its two tensor summands has a zero H0 factor. Therefore H0(D,T)=0. In particular T is not the trivial degree-zero line bundle. Since five is prime and T^5 is trivial, its order is exactly five.

## 5. Intrinsic filtration of the double-cubic residue sections

The actual defect line in the double-cubic description is

    L_2=O_(2D)(-2,12).

Its restriction to D is isomorphic to K_D^5 tensor T^3. The conormal of D in the surface is O_D(-3,-3)=K_D^-3. Thus the square-thickening restriction sequence becomes

    0 -> K_D^2 tensor T^3 -> L_2
      -> K_D^5 tensor T^3 -> 0.                      (1)

The two end line bundles have degrees twelve and thirty. Their H1 groups vanish by Serre duality, and Riemann--Roch gives h0 equal to nine and twenty-seven. Consequently (1) gives an exact 9-to-36-to-27 sequence of global sections.

Its actual G-characters are

    H0(K_D^2 tensor T^3)=P4+D5,
    H0(K_D^5 tensor T^3)=A+2V+2P4+2D5.

For a direct check, the corresponding divisor restriction sequences compute these characters as

    Sym6(Wprime) tensor Sym6(W)
      minus Sym3(Wprime) tensor Sym9(W),

and

    Sym3(Wprime) tensor Sym9(W) minus Sym12(W),

respectively. The positive-degree H1 vanishings above justify converting these Euler expressions to actual H0 characters. Their sum agrees with the independently obtained character of H0(M8).

This is a filtration of the actual 36-dimensional residue section space, not the already different 32-dimensional kernel of its boundary to P4. A section in either part need not have a nonzero image under that boundary. The actual operator residue still must be computed and projected.

## 6. The intrinsic nilpotent boundary is onto

Put N8=pi_*O_D(-5,9), the rank-three nilpotent subbundle of M8. The pure-u tangent coefficients give the exact sequence

    0 -> V O_L(-4) -> T6 O_L(-1) -> N8 -> 0.       (2)

Indeed a class r=f u+g v vanishes on D exactly when v is a multiple of f. A scalar gauge removes that multiple, leaving the pure-u representative. Its remaining gauges are precisely f times quadratic forms. This proves (2) fiberwise by the actual coprimality.

The actual quintic relation sequences, twisted by minus one, are

    0 -> V O(-4) -> K5(-1) -> O(4) -> 0,
    0 -> K5(-1)=P4 O(-2) -> T6 O(-1) -> Wprime O(1) -> 0.

Consequently 0->O(4)->N8->Wprime O(1)->0 is exact. It splits because H1(O(3))=0, and the equivariant splitting is unique because Hom_G(Wprime,Sym3 W)=0. Thus

    N8=O(4) plus Wprime O(1).

The first summand is exactly the scalar/class(N) subbundle. In cohomology, (2) gives H0(N8)=H1(V O(-4))=D5+P4. Its inclusion into the actual quotient sequence of M8 makes the operator boundary the natural map

    H1(V O(-4)) -> H1(J8)=P4.

The gauge extension 0->V O(-4)->J8->O(4)->0 has the already proved nonzero, hence injective, connecting map D5->D5+P4. Therefore the actual boundary restricted to this intrinsic nilpotent space is the exact quotient

    0 -> D5 -> H0(N8) -> P4 -> 0.                 (3)

This determines a nonzero boundary channel geometrically. It does not assert that the particular corrected operator residue lies in N8, or has a nonzero P4 component there.

## Reproduction and scope

Run verify_cubic_genus_four_five_torsion.py. It checks the complete small-bidegree invariant test, the genus/degree/Riemann--Roch arithmetic, and the two actual-character formulas using universal representation data. The finite-flat, regular-pair, singular-orbit, and line-trivialization arguments are the geometric proof. No actual coefficients, matrices, rank tests, or parameter scans are used.
