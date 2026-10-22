# The actual degree-eight defect as a double-cubic pushforward

## Result and scope

Let M8 be the vertex cover-degree-eight piece of the actual operator defect M(4)=omega_(2Z)(5), with the global quotient established in ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md. Then there is an actual equivariant bundle identification on L=P(W)

    M8 = pi_* O_(2D)(-2,12) = A O_L(6) plus V O_L(4).       (1)

Here D is the cubic divisor of bidegree(3,3) in P(Wprime) times L, pi is projection to L, and 2D is its square thickening in that smooth surface. This 2D is NOT 2Z, and neither is the ambient first-normal thickening 2Q. The identification uses the actual nonsplit quintic generator transitions. It does not evaluate the actual operator residue or the remaining Bockstein.

## 1. The cubic divisor and the quintic trivialization

VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md gives

    K3=O_L(-2) subset Sym^3 Wprime O_L(1),
    0 -> V O_L(-3) -> K5=P4 O_L(-1) -> O_L(5) -> 0.

Consequently the actual cubic f has bidegree(3,3), and local quintic lifts g have bidegree(5,-5). On overlaps their non-diagonal change is

    g' = g + p f,

where p is a quadratic in positive cover coordinates, with base degree -8. All ordinary base-line transition factors are understood as well. The divisor D=(f=0) is finite flat of degree3 over L: the cubic is nonzero in every fiber. Actual fiberwise coprimality of f and g implies that g has no zero on D. Thus these local quintics give a nowhere-zero section of O_D(5,-5). Smoothness or reducedness of D is not needed. Each local g is also invertible as a section of its line bundle on 2D, since invertibility lifts across nilpotents.

## 2. Cancellation of the nonsplit generator transition

Use the regular-pair tangent basis

    S1=[[f,0],[2g,-f]], S2=[[g,-2f],[0,-g]].

An element R=u S1+v S2 of degree8 has diagonal coefficient

    r=f u+g v,

where u and v have cover degrees5 and3. The local commutator quotient in this degree is all binary octics modulo f^2 times quadratics: I_8 is the entire octic space, because the actual CI has socle degree6, while g^2 has degree10. Thus its dimension is6 in every fiber.

For P=[[1,0],[p,1]], conjugation gives

    r'=r+2p f v.

Since r=g v modulo f, one has the exact congruence

    r' g^2-r(g+p f)^2 = -f^2(2p g u+p^2 r) = 0 modulo f^2.   (2)

Therefore r/g^2 glues on 2D. The diagonal coefficient r has bidegree(8,2): its physical twist is6 and its cover degree8 consumes four base twists. Dividing by g^2 gives bidegree(-2,12). For a base frame change, the cubic and quintic polynomial components carry the line factors O_L(3) and O_L(-5), respectively, as read directly from K3 and K5. A degree8 diagonal entry of B(6) has base factor O_L(6-8/2)=O_L(2); diagonal conjugation itself has weight zero on that entry. Thus the ratio has the ordinary base factor O_L(2+10)=O_L(12), not merely triangular invariance. Its positive projective degree is8-10=-2. This checks the full line transition in addition to (2). Scalar spinor factors cancel in the adjoint. Koszul stabilizers fixing the oriented pair have the form I+tN; their effects on this leading degree are zero, consistently with REGULAR-SERRE-STABILIZERS-HAVE-ZERO-NORMAL-DEFECT-RESIDUE.md. This is a statement about the homogeneous vertex piece, not an assertion of a global torus grading on the whole cone bundle.

On each fiber, octics modulo f^2 quadratics identify with H0(O_(2D)(8)); division by the locally invertible g^2 is an isomorphism to the indicated line bundle. Indeed the restriction sequence has kernel O(2) with vanishing H1. Equation(2) then proves the first identification in (1), including its actual nonsplit gluing.

## 3. Pushforward and the canonical representation splitting

The divisor sequence for 2D, twisted by (-2,12), is

    0 -> O(-8,6) --f^2--> O(-2,12)
      -> O_(2D)(-2,12) -> 0.

Its pushforward gives the exact sequence

    0 -> M8 -> Sym^6(Wprime) O_L(6) --f^2--> O_L(12) -> 0. (3)

Both preceding H0 fiber terms vanish; the displayed map is contraction with f^2 under relative Serre duality. It is surjective because it is dual fiberwise to multiplication of a nonzero scalar by the nonzero sextic f^2.

The actual invariant tensor f^2 belongs to

    Sym^6(Wprime) tensor Sym^6(W)
      = (A plus P4) tensor (V plus P4).

The only common irreducible is P4. Therefore f^2 lies in the P4 tensor P4 channel and is nonzero there. The A O(6) summand in (3) maps to zero, while the map on P4 O(6) is the unique nonzero equivariant sextic evaluation, up to scalar. The proven quintic-extension evaluation sequence, twisted by7, is

    0 -> V O_L(4) -> P4 O_L(6) -> O_L(12) -> 0.

This proves the second identification in (1). No actual coefficient or actual-instance rank is evaluated.

## 4. Independent finite-duality check

Let R be the finite flat vertex algebra of the actual square scheme 2Z over L. Finite duality gives pi_*omega_(2Z)(5)=R^* tensor O_L(3). The degree8 residue pairs with cover degree6 under the local CI pairing for (f^2,g^2), whose socle degree is14. Its degree6 algebra has the exact sequence

    0 -> O_L(-9) --f^2--> Sym^6(Wprime) O_L(-3)
      -> R6 -> 0.

Indeed the ordinary cubic ideal line has degree -9/2, while six cover coordinates have base degree -3. Dualizing and tensoring by O_L(3) recovers exactly (3). This independent derivation verifies the full line factors in the double-cubic description without choosing a quintic splitting.

## 5. Global sections and the remaining value

The two summands have h0=21 and15 and no H1. Their total character is

    H0(M8) = A plus 2V plus 3P4 plus 3D5,

which agrees with the previously proved exact global quotient

    0 -> H0(E8) [dimension32] -> H0(M8) [dimension36] -> P4 -> 0.

The actual normal operator residue still has to be inserted into this quotient, and then reduced by the actual second-symbol image. In particular a nonzero section of either split summand need not have nonzero quotient class. Formula(2) supplies a potentially useful way to compute that section without discarding the quintic transition correction.
