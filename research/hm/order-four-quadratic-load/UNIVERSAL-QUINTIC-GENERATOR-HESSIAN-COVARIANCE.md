# Universal quintic-generator covariance of the Hessian correction

## Results

For the first-normal nilpotent correction in UNIVERSAL-HESSIAN-CORRECTION-FOR-FIRST-NORMAL-NILPOTENCE.md, changing a quintic generator by g'=g+p f, with p quadratic, produces an explicit residual which generally is NOT a regular commutator near the zero scheme.

With canonical SL2-harmonic lifts of even quartics, the residual is

    N_tilde(f,g') - P N_tilde(f,g) P^{-1}
      = -q mix(H_f,H_p)/16 · [[f,0],[2g',-f]] mod q^2,   (1)
    P=[[1,0],[p,1]].

The entries on the right are even functions despite the displayed odd factors. For the actual nonsplit quintic-generator extension, this particular residual is governed by a cocycle in Wprime O_L(-5), whose G-invariant H1 vanishes. Thus the residual has a unique invariant cochain primitive (up to the zero global-section space). This is a specific gluing correction, not a claim that local differences are all gauge commutators.

The calculation does not yet identify the resulting local correction system with the global midpoint bundle, nor compute the differential-operator obstruction or the positive cubic gate.

## 1. The compatible-transport convention

Put j=Jac(f,p)/15 and use Euler decompositions

    f=aF+bH, g=aG+bK, j=aJ1+bJ2.

Let q=xz-y^2 and C=[[x,y],[y,z]]. The linear even polynomials F,H,J1,J2 have unique lifts in x,y,z. Define

    delta=(-yJ1-zJ2, xJ1+yJ2)^t.

Then C delta=q(-J2,J1)^t. On the cone, delta=(-b j,a j)^t. Euler identities show that a compatible lift of grad(g')/5 is

    gvec'=gvec+p fvec+delta.

If N0 denotes the uncorrected Gram nilpotent, this gives

    N0'=P N0 P^{-1}+q R,
    R11=H J1-F J2,
    R12=0,
    R21=2(KJ1-GJ2)+2p(HJ1-FJ2)+j^2,
    R22=-R11.                                         (2)

These are polynomial equalities modulo q^2 with the indicated even-lift choices. The rule is additive in p and compatible with composing triangular changes.

## 2. Hessian transformation and the nongauge residual

Let M=mix(H_f,H_p). Differentiating g'=g+pf and using the Euler identities gives

    mix(H_f,H_g')-mix(H_f,H_g)=4p det(H_f)+f M,
    Jac(f,Jac(f,p))=(3/2)(f M-p det(H_f)).              (3)

Substitute (2)-(3) in the explicit Hessian correction T. The total residual in this compatible-transport convention is

    R+T'-P T P^{-1}
      =-M/144 · [[f,0],[2g',-f]].                     (4)

The lower-left entry contains g', NOT g. This is also forced by the linearized nilpotence equation relative to P N0 P^{-1}. The companion verifier independently checks all entries for fully generic cubic, quintic and quadratic polynomials, with every coefficient an independent indeterminate.

When f M is nonzero, its cover degree is4. The diagonal of any regular commutator with the cone matrix N(f,g') belongs to the ideal (f^2,g'^2), whose nonzero homogeneous terms start at cover degree6. Therefore the residual (4) cannot be absorbed by a regular identity-mod-q change of frame. This argument is a degree comparison, not a rank evaluation. It does not assert that M is nonzero for every actual transition.

## 3. Canonical harmonic lifts change the coefficient

It would be incorrect to discard the even-lift convention. For binary quartics, use the canonical harmonic lift

    a^4 -> x^2, a^3b -> xy, a^2b^2 -> (xz+2y^2)/3,
    ab^3 -> yz, b^4 -> z^2.

It is the SL2-equivariant section of restriction to the cone, with Laplacian d_x d_z-(1/4)d_y^2 annihilating its image. The harmonic lift of grad(g')/5 differs from the transported lift in Section1 by q times a constant vector E. The exact universal coefficient calculation gives

    aE1+bE2=-8 M/144.

Changing gvec by qE changes the first-normal nilpotent by

    q(aE1+bE2) [[f,0],[2g',-f]] mod q^2.

Adding this to (4) proves (1): the harmonic-convention coefficient is -9/144=-1/16. Both coefficients are retained to show explicitly where a hidden choice of even representatives would otherwise alter the formula.

## 4. The actual invariant residue is a coboundary

The actual quintic-generator extension is

    0 -> V O_L(-3) -> P4 O_L(-1) -> O_L(5) -> 0.

Its triangular change p is consequently a cocycle in V O_L(-8). The cubic generator inclusion

    O_L(-2) -> Sym^3 Wprime O_L(1)

is a global cubic F with base coefficients of degree3. Taking two transverse derivatives and contracting against H_p leaves one transverse variable. Hence the map p -> mix(H_F,H_p) is an actual G-equivariant sheaf map

    V O_L(-8) -> Wprime O_L(-5).                       (5)

It follows that the residual cocycle in (1) has class in H1(Wprime O_L(-5))^G. By P1 duality this is the invariant part of Wprime tensor Sym^3 W. Since Sym^3 W=S4 and S4 is not Wprime, that invariant space is zero. Also H0(Wprime O_L(-5))=0. Thus the residual has an invariant cochain primitive, unique modulo global sections, with no scalar or coefficient evaluation.

The kernel matrix in (1) itself transforms tensorially under the triangular change:

    P [[f,0],[2g,-f]] P^{-1}=[[f,0],[2g',-f]].

Adding suitable local multiples of this kernel matrix therefore compensates the displayed cocycle while preserving first-normal nilpotence. This settles the QUINTIC-GENERATOR component of the Hessian gluing discrepancy, including its nongauge nature and its cohomological correction. Other frame identifications, determinant normalizations, comparison with a specified global first-normal bundle, and lifting the twisted differential operator must still be tracked before computing Psi. In particular, a change of local generator frame can include a Koszul-stabilizer matrix which fixes the pair (f,g); it is not necessarily exhausted by the displayed triangular change. The scalar and stack factors relating F to the spinor-twisted G must also be compared explicitly. Vanishing of the cohomology class in (5) alone does not settle either issue.

## Verification and scope

Run verify_universal_quintic_generator_correction.py. It checks the full symbolic identities, the harmonic-lift coefficient, and the invariant cohomology multiplicity. The input coefficients are all independent symbols, never selected actual HM coefficients. No actual matrix rank, actual-instance scan, or local-model experiment is performed.
