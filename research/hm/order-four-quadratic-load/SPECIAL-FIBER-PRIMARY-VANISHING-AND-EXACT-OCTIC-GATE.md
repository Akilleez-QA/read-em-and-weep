# Special-fiber primary vanishing and the exact octic extension gate

## Scope and inputs

Fix an order-five hyperplane H=P3 and the established nonvertex eigensection w of E=F_H(2). Its regular zero curve is C=Q disjoint-union Y. Use the actual special-curve coordinates

    I_Q=(z,q_c(y,u)),
    I_Y=(x²,xq,q²,g),  g=bx-aq,
    a=c y, b=kappa z², q=A y²+B u²,

with c,kappa,A,B nonzero. To justify the refinement a=c y from the source statement a=a(y,u): inversion fixes the conormal generators x and q, and fixes the nonzero coefficient b=kappa z². Equivariance of the Ferrand quotient therefore fixes its target trivial-line linearization and forces a to be inversion-even as well. Since y is even and u is odd, the linear form a is c y; c is nonzero because the Ferrand map is surjective. The binary quadratic q_c is diagonal, has nonzero coefficients, and is coprime to q. These are ideal sheaves. The Ferrand quotient sends x to a and q to b, giving

    0 -> I_Y -> I_Q' -> O_Q' -> 0,
    Q'=(x,q),
    0 -> O_Q' -> O_Y -> O_Q' -> 0.

The two conics Q and Q' are reduced unions of two lines in their respective planes; these statements and the sequences are valid for that reducible geometry. This proof does not substitute generic smooth conics. The input is SPECIAL-HYPERPLANE-ADJOINTS-ARE-EXACTLY-SQUARES.md at repository commit d29d27e5c92cf105b60bce4e828f4860582a2bee.

## 1. The ribbon has no cubic postulation defect

Since Q' is a plane complete intersection (1,2), H1(I_Q'(3))=0. The image of H0(I_Q'(3)) in H0(O_Q'(3)) is

    a H0(O_Q'(2)) + b H0(O_Q'(1)).

The ambient polynomial restriction maps in these degrees are surjective. Hence its cokernel is the degree-three part of

    C[y,z,u]/(q,a,b) = C[z,u]/(z²,u²).

This Artinian ring has no degree-three part. Therefore

    H1(I_Y(3))=0.

The ribbon sequence gives h0(O_Y(3))=2(2*3+1)=14 and H1(O_Y(3))=0, so

    h0(I_Y(3))=20-14=6.                             (1)

## 2. Two explicit quartic trace lifts

Let Pi=(z=0). The intersection T=Y intersect Pi has ideal sheaf (x²,q) on Pi. Indeed restriction of the displayed ribbon ideal gives (x²,xq,q²,aq); a is invertible near the support (x=q=0), since q has nonzero y² and u² coefficients. Away from that support both ideals are the unit ideal. Thus T is the length-four complete intersection (2,2).

A quartic in I_C restricts to q_c times a quadratic vanishing on T: q_c is invertible on T by coprimality. Its trace consequently lies in

    q_c H0(I_T(2)) = q_c span{x²,q}.

Both trace directions actually lift. The first lift is x² q_c. Write

    q_c=alpha q+beta a²,

which is possible because q and a² span the diagonal binary quadratics. Then a second lift is

    q_c q-beta a b x = alpha q²-beta a g.

The right side belongs to I_Y. The left side belongs to I_Q since b is divisible by z². Its trace is q_c q. These two traces are independent.

The kernel of the trace map is z H0(I_Y(3)): z is a nonzerodivisor on O_Y, as no component of Q' is contained in z=0, and the ribbon is Cohen-Macaulay. Also z belongs to I_Q. Thus

    h0(I_C(4))=6+2=8.                              (2)

The disjoint union and ribbon sequences give h0(O_C(4))=9+18=27 and H1(O_C(4))=0. Since h0(O_H(4))=35, equation (2) gives

    H1(I_C(4))=0.

Finally the section sequence

    0 -> O_H(1) -> F_H(3) -> I_C(4) -> 0

gives the new primary result

    h0(F_H(3))=12, H1(F_H(3))=0.                    (3)

The higher groups also vanish, from the same sequence and the preceding curve cohomology.

## 3. Exact five-dimensional octic obstruction

The symmetric-square section sequences are

    0 -> F_H(3) -> B_H(4) -> I_C²(7) -> 0,
    0 -> F_H(4) -> B_H(5) -> I_C²(8) -> 0.

Here squares are ordinary ideal sheaves. The established uniform adjoint dimensions h0(B_H(4))=20, h1(B_H(4))=5, h0(B_H(5))=63, H1(B_H(5))=0 and primary acyclicity at twist four combine with (3) to give

    h0(I_C²(7))=8, h1(I_C²(7))=5,
    H1(B_H(4)) is isomorphic to H1(I_C²(7)).        (4)

At twist five the curve sequence gives h0(I_C(5))=56-33=23, hence h0(F_H(4))=10+23=33. Therefore

    h0(I_C²(8))=30, H1(I_C²(8))=0.                (5)

Let R=(u=0), Z=C intersect R. Regularity and Cohen-Macaulayness of the ordinary first thickening give

    0 -> I_C²(7) --u--> I_C²(8) -> I_Z²(8) -> 0.

Equations (4)-(5) show that h0(I_Z²(8))=27, the octic restriction image has dimension 22, and its cokernel has dimension 5. This agrees independently with the plane symmetric-square sequence and the Steiner dimensions h0(F_R(4))=21, h0(B_R(5))=48.

## 4. Exact actual Cartan test, with no primary correction

For s in D5=H0(F_R(2)), wedge with w_R gives a cubic w_R wedge s in H0(I_Z(3)). Define the actual polynomial shadow

    mu_w(s1 s2)=(w_R wedge s1)(w_R wedge s2).

For v in the actual Cartan P4 summand of Sym² D5, put

    f_v=q0 mu_w(v) in H0(I_Z²(8)),

where q0 is the invariant conic in R, not the section conic q_c. Naturality identifies the obstruction to extending f_v with the image of delta_H(q0 v) under the isomorphism in (4). Consequently

    delta_H(q0 v)=0
    if and only if f_v extends to H0(I_C²(8)).     (6)

Thus the entire special P4 boundary vanishes if and only if its actual polynomial-shadow subspace is contained in the 22-dimensional restriction image. The previously possible H1(F_H(3)) correction is now proved zero, rather than dropped by assumption.

The scalar a=18 alternative forces this containment at all twelve order-five hyperplanes. To exclude it, it is enough to prove failure of containment at one such hyperplane. This note does NOT prove that failure and does NOT evaluate actual coefficients or ranks. Its new results are (3), the exact five-dimensional obstruction in (4)-(5), and the equivalence (6).

## Additional source dependencies

UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md supplies the adjoint dimensions; SURJECTIVE-PLANE-BOUNDARY-BY-CONIC-RESIDUALS.md supplies primary twist-four acyclicity; SCALAR-CARTAN-BOUNDARY-OCCURRENCE-GATES.md supplies the scalar-a=18 exceptional-zero implication. The naturality diagram is detailed in SPECIAL-FIBER-ORDINARY-SQUARE-EXTENSION-CRITERION.md. These filenames are source dependencies, not a claim that all are present at the immutable special-curve commit.
