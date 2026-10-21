# A special-fiber ordinary-square criterion for Cartan boundary nonvanishing

The subsequent SPECIAL-FIBER-PRIMARY-VANISHING-AND-EXACT-OCTIC-GATE.md proves that the primary correction retained below is zero in this actual special geometry, making the octic extension test an equivalence. The two-stage formulation here records which vanishing is required.

## Scope

Fix any order-five hyperplane H and its actual nonvertex eigen-section w of E=F_H(2). Let C=Z(w), R=(u=0), and Z=C intersect R. The established special-curve theorem gives C=Q disjoint-union Y, with the actual ordinary ideal sheaf

    I_Y=(x^2,xq,q^2,kappa x z^2-aq),
    I_Q=(z,q_c(y,u)),

where all actual parameters retain their proved nonzero and coprimality conditions. The notation q_c denotes the eigen-section conic equation; it is NOT the invariant positive-plane conic q0.

The following supplies a sufficient geometric test for nonzero delta_H(q0 P4), and an exact two-stage lifting criterion. It does not assert that any tested octic fails to extend. Thus it does not itself exclude the scalar a=18 possibility.

## 1. The actual polynomial shadow of a plane adjoint

Write D5=H0(F_R(2)). The actual square identification gives H0(B_R(3))=Sym^2 D5. Wedge against w_R defines

    D5 -> H0(I_Z(3)),       s |-> w_R wedge s.

Its symmetric square is the actual quotient map on sections

    mu_w: Sym^2 D5 -> H0(I_Z^2(6)),
    s1 s2 |-> (w_R wedge s1)(w_R wedge s2).

For v in the Cartan P4 summand, the corresponding section q0 v of B_R(5) has polynomial shadow

    f_v=q0 mu_w(v) in H0(I_Z^2(8)).                 (1)

These are actual wedge products, not arbitrary octics with the correct stabilizer weight.

## 2. Ordinary-square restriction retains the correct ideal

The actual C is a regular codimension-two curve, and it has no component in R. Thus u is a nonzerodivisor on O_C. The quotient O_H/I_C^2 is Cohen-Macaulay: the first infinitesimal neighborhood of a regular immersion has a filtration with locally free O_C conormal graded piece. Its associated primes are therefore the curve components, none contained in u=0. Hence

    (I_C^2:u)=I_C^2.

Restriction of the ordinary square has image I_Z^2. Consequently there is an exact sheaf sequence

    0 -> I_C^2(7) --u--> I_C^2(8)
      -> I_Z^2(8) -> 0.                            (2)

No symbolic square or unsaturated polynomial ideal is substituted.

## 3. A sufficient nonvanishing test

Symmetric multiplication by the regular section w gives exact rows

    0 -> F_H(3) -> B_H(4) -> I_C^2(7) -> 0,
    0 -> F_H(4) -> B_H(5) -> I_C^2(8) -> 0,
    0 -> F_R(4) -> B_R(5) -> I_Z^2(8) -> 0.

Multiplication by u and restriction to R make these a commutative diagram. Naturality of connecting morphisms says

    boundary_(2)(f_v)
      = image of delta_H(q0 v) in H1(I_C^2(7)).      (3)

Therefore, if even one f_v in (1) is NOT the restriction of a section of I_C^2(8), then the actual P4 boundary at this special hyperplane is nonzero. This would exclude scalar a=18 by its established exceptional-zero theorem.

The required nonextension is an exact ideal-sheaf statement for the actual ribbon parameters. Uniform H1(I_C^2(8))=0 does not imply the restriction in (2) is onto; its obstruction lies at twist seven.

## 4. Exact second-stage correction when the octic extends

Conversely, suppose f_v extends to F in H0(I_C^2(8)). Actual primary acyclicity H1(F_H(4))=0 lets F lift to beta in H0(B_H(5)). Its plane restriction differs from q0 v by a unique w_R sigma, with sigma in H0(F_R(4)), using the last row above.

The desired adjoint lift exists precisely when one can choose F and beta so that sigma lies in the image

    H0(F_H(4)) -> H0(F_R(4)).

For any fixed extension choice, its obstruction is the boundary of sigma in H1(F_H(3)). Different extension choices must be retained; declaring this primary obstruction zero without proof would be incorrect.

Equivalently, (3) detects the image of the full adjoint obstruction; if it vanishes, the remaining adjoint obstruction lies in the image of H1(F_H(3)). Neither the known uniform adjoint cohomology nor the ordinary-square calculation alone removes that correction.

## Sources and limits

The special section curve and its actual parameters are in SPECIAL-HYPERPLANE-ADJOINTS-ARE-EXACTLY-SQUARES.md. SURJECTIVE-PLANE-BOUNDARY-BY-CONIC-RESIDUALS.md supplies primary F_H(4) acyclicity and ordinary-square residual calculations. UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md deliberately retains possible H1(F_H(3)). SCALAR-CARTAN-BOUNDARY-OCCURRENCE-GATES.md supplies the a=18 exceptional-zero implication.

The new result is the exact actual-map reduction (1)-(3) and its retained second-stage correction, not a claim that a special fiber has been evaluated. No actual coefficients, matrices, rank scans or experiments are used.
