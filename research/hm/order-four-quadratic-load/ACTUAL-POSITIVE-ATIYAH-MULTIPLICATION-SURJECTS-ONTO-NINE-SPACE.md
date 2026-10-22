# Actual positive Atiyah multiplication surjects onto the nine-space

## The new conclusion

Let C=H1(B_Q(2))_+, and let C^{phi+}=P4+D5 be its nine-dimensional Serre-involution eigenspace. The actual map

    D5 tensor A -> C,   h tensor a |-> h At_F(D_a)|_Q     (1)

is onto C^{phi+}. Both its P4 and D5 channels are nonzero. This is proved by the intrinsic Serre residue and a universal compact-Casimir argument, without selecting HM coefficients or testing an actual matrix rank.

This does NOT prove that the actual third Bockstein is nonzero. The previously established extra multiplication by a kills this entire nine-space. The result determines the image before that annihilation and supplies the actual residue map underlying the canonical cone operator correction.

## 1. The socle functional, with its line bundle

Work over the negative projection on the complement of the conic, using the root gerbe over L=P(W) when necessary to retain the half twists. The transverse coordinate algebra has degree-d term Sym^d(Wprime) O_L(-d/2). The actual homogeneous vertex ideal is a relative regular (3,5) complete intersection. Its fibers have Hilbert function 1,2,3,3,3,2,1, so it is finite flat of rank15 over the gerbe. The even pieces, including the socle, descend to L.

The Serre section identifies its normal determinant with det G=O(2). The relative ambient canonical line is O_L(-1), since the two transverse cotangent directions each have twist-1/2. Relative complete-intersection duality therefore identifies the relative dualizing module with R tensor O_L(1), where R is the full vertex algebra. Equivalently its graded socle is O_L(-1), and the actual residue gives a perfect graded pairing through

    lambda: Sym^6(Wprime) O_L(-3) -> O_L(-1).           (2)

This normalization incorporates the actual Serre extension residue; it is not a choice of a quintic lift. Replacing a local quintic generator by g+p f leaves the normalized Grothendieck residue unchanged.

The map (2) is nonzero and equivariant. Since Sym^6(Wprime)=A+P4 and H0(O_L(2))=A, its coefficient map is precisely the nonzero complete quadratic channel to A, up to a common scalar. In particular, for h in D5=Sym^4(Wprime) and r in V=Sym^2(Wprime), the coefficient

    B(h,r)=lambda(h r) in H0(O_L(2))=A

is a nonzero equivariant bilinear map D5 tensor V -> A. Binary multiplication onto Sym^6(Wprime) proves nonzeroness; there is no inference from arbitrary nonzero composite legs.

The pairing R4 tensor R2 -> socle is perfect. At twist2 it identifies the actual degree-four residue space with V tensor A=P4+D5, consistently with the cubic even quotient theorem.

## 2. Exact comparison with the actual tangent operator

Choose a local negative base coordinate z and transverse coordinates x,y. Choose homogeneous generators f,g normalized to the actual Serre residue and the physical determinant frame. This simultaneous choice is legitimate: the Serre double-cover calculation gives the FULL block-torus eigencharacter mu^2 of the actual G-invariant vertex residue, not merely its order-four sign. This is exactly the full character of the homogeneous (3,5) residue. Only the full character excludes higher-cover-degree unit factors. Their ratio is therefore a degree-zero unit, depending only on z, and can be absorbed by rescaling one generator without losing its degree. Thus the residue below has no omitted variable normalization factor. The natural negative sl(W) vector field takes the form

    D=w(z) partial_z + kappa(z)(x partial_x+y partial_y).

A positive quartic h(x,y), representing a positive physical quadratic, has constant transverse coefficients. The natural frame action on O(2)=det G is -4 kappa: this follows equally from the fact that the global positive polynomial h is fixed by the negative SL2 action. Take also a transverse quadratic r(x,y) with constant coefficients.

The vector field theta=h D preserves the actual ideal. Indeed hD f and hD g have cover degrees7 and9, above the socle degree6. Choose a relation matrix M with

    hD(f,g)^T=M(f,g)^T.

Its trace has degree4. The intrinsic derivative of the Serre residue is

    rho_theta=4 kappa h-tr M                            (3)

modulo the ideal. The sign convention here views the residue as a section of det(normal) tensor (det G)^(-1). The conormal action has trace M, so its dual contributes -tr M; the inverse determinant line contributes +4 kappa h. This formula retains the determinant factor explicitly.

The Grothendieck residue differentiation identity gives

    w partial_z lambda(h r)
       =lambda((8 kappa h-tr M)r).                     (4)

To verify (4), replace w partial_z f by Df-3 kappa f and w partial_z g by Dg-5 kappa g in the derivative of the fraction hr/(fg). The off-diagonal entries of M leave fractions with only f or only g in the denominator and hence vanish in the codimension-two local-cohomology residue. No division by an actual coefficient is used.

The coefficient line in (2) is O_L(2), whose natural frame action is -4 kappa. Subtracting 4 kappa lambda(hr) from (4) therefore proves the invariant identity

    lambda(rho_theta r)=(Lie_D lambda)(h r).            (5)

All connections have now been included. Thus, after the perfect pairing, the actual residue map is

    J(h,a)(r)=D_a acting on B(h,r) in A.                (6)

On A this is the adjoint sl2 action, up to the fixed nonzero normalization of A≅sl(W). Formula (5) also proves independence under local frames and generator lifts, because both sides are intrinsic. The nonsplit quintic extension has not been replaced by a split model.

## 3. Both channels of J are nonzero

Transpose B to a nonzero embedding j:D5->V tensor A. Write S=j(D5) and T=S-perpendicular=P4, using invariant Hermitian forms. Equip A with the compact spin-one representation of su2 and V with any invariant positive Hermitian form. Let J_i be three Hermitian generators acting on the A factor, with

    sum_i J_i^2=c identity, c>0.

The image of (6) is the span of J_i S. It is G-stable. If it were contained in S, S would be an sl2 submodule of three copies of its irreducible three-dimensional representation. Its dimension5 makes this impossible.

If it were contained in T, each J_i has block form [[0,B_i*],[B_i,C_i]] relative to S+T. The S block of the Casimir identity gives

    sum_i trace(B_i* B_i)=5c.

The T block gives

    sum_i trace(B_i B_i*)+sum_i trace(C_i^2)=4c.

Hermitian positivity and equality of the two B traces would imply 5c<=4c, a contradiction. Hence neither projection is zero. Since V tensor A=P4+D5 is multiplicity-free, J is onto that nine-space.

## 4. Passing from residue to the actual Atiyah class

For any linear combination of symbols theta=hD, a positive global operator on G of twist2 must preserve the section line: the established primary calculation gives

    H0(G(2))_+=sigma H0(O_X(2))_+=A+D5.

Its trace can be adjusted by a scalar operator so that its determinant action is the fixed natural action. Compatibility with the Serre extension then says exactly that rho_theta is the restriction of a global scalar in H0(O_X(2)), up to the invertible factor2 from the opposite subline and quotient scalar actions.

The pure degree-four vertex residue space meets the image of ambient positive quadratics only in zero. A D5 adjustment creates a nonzero conic component, and an A adjustment creates a nonzero reduced-vertex component. Therefore such an operator exists if and only if rho_theta=0.

This is global sufficiency as well as necessity. The relevant obstruction lies in Ext^1(I_Z(2),O_X(2)); its residue detects it because Hom(I_Z(2),O_X(2))=O_X and H1(O_X)=H2(O_X)=0. A vanishing residue kills the global obstruction and gives compatible middle-bundle action. Tensoring by the spinor line does not change operator existence, since that line has the natural negative SL2 action. Thus

    ker(1)=ker J.

Section3 proves rank9. Naturality of Atiyah under the Serre involution puts (1) in C^{phi+}, whose dimension is9. This proves the stated surjectivity and both channel nonvanishings.

## Dependencies and verification

Actual inputs: the regular homogeneous Serre vertex scheme and its nonzero complete cubic relation; the primary H0(G(2)) calculation; and the proved nine/twenty-one involution decomposition. These are supplied by the Serre double-cover, cubic even quotient, square-shadow, and eigenspace notes. The residue quotient and canonical scalar adjustment are in POSITIVE-SERRE-RESIDUE-AND-CANONICAL-CONE-OPERATOR-CORRECTION.md.

Run verify_positive_atiyah_residue_surjectivity.py. It checks character identities, the relative-duality degrees, and the universal coefficient accounting in (4)-(5). The proof of the two-channel assertion is the uniform Casimir argument, not a matrix evaluation.
