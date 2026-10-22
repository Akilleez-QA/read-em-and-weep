# The actual ambient Atiyah multiplier is the monad ratio

## Result and retained constants

Fix the three irreducible channel maps in the pinned monad family, the physical equation q0, the negative Hamiltonian volume, and the determinant/Serre markings. Write the NONZERO formal monad coefficients as `(a_m,b_m,c_m)`, and put `r=a_m/b_m`. The letter a without a subscript denotes a smoothing direction, not a monad coefficient.

The actual ambient multiplication coefficient defined by

    a At_F(D0)=q0 kappa_F At_F(D_a)

has the precise form

    kappa_F=C_mult r,              C_mult != 0.           (1)

Here C_mult is one UNIVERSAL constant in the fixed channel and equation conventions. It is not evaluated in this note. It cannot be set to one and then called an evaluation in the old markings.

There is a second exact comparison. Let beta_E be the fixed left-edge generator of `H2(B(-4))^G`, and normalize `eta_E` by `delta_q0(eta_E)=beta_E`. Let eta_ap be the FULL invariant normal class whose lowest component is the fixed apolar identity tensor. Then

    eta_E=C_ap a_m b_m eta_ap,        C_ap != 0.          (2)

The normal quadratic theorem gives `d=K_cup b_m^2`, with `K_cup != 0`, in the obstruction `s+s^2d` relative to beta_E. Consequently the actual endpoint-minus-midpoint in the POSITIVE transition convention is

    eta_+=(eta_E)/(2d),
    c_eta+=C_ap/(2K_cup) r.                              (3)

Formula (3) uses the two actual roots and fixes the affine displacement; it does not label an arbitrary tangent generator as that displacement. A fixed-boundary comparison then relates these constants to the cyclic probe, as in Section 5 below.

Finally, Section 6 identifies the exact missing determination of C_mult as a GLOBAL degree-two chain homotopy of the determinant-valued monad. Every term of its twist-two chain-Hom complex is higher-cohomology acyclic, so no unmentioned Cech correction is hidden in this criterion.

All source parameters remain unassigned. No actual-instance coefficient, matrix, rank, or scan is evaluated; no midpoint extension to 3Q or fourth value is claimed. Earlier frozen files are unchanged.

## 1. Exact covariance of the ambient multiplication

The monad channel maps have types

    a_m: Wprime -> Wprime tensor Lambda^3 V,
    b_m: Wprime -> Wprime tensor V tensor Lambda^2 W,
    c_m: A -> Wprime tensor Lambda^2 V tensor W.

Independent source gauges R on A and S on Wprime send the coefficients to `(S a_m,S b_m,R c_m)`. Their dual gauges on the right give an isomorphism of the full self-dual monad over the identity of projective space. They therefore leave both kappa and r unchanged.

Let `g=(lambda I_V,mu I_W)` act by PULLBACK of coordinate functions. The channel weights are

    (a_m,b_m,c_m) ->
      (lambda^3 a_m,lambda mu^2 b_m,lambda^2 mu c_m).

Each fixed Hamiltonian D_a and D0 commutes with this block scalar. Pulling back the defining equality of kappa gives

    mu^2 a At_(g*F)(D0)
       =lambda^2 q0 kappa_F At_(g*F)(D_a).

Thus, after DIVIDING by mu^2,

    kappa_(g*F)=(lambda^2/mu^2) kappa_F.                (4)

This is the weight of r, not its inverse. The order-four specialization alone would not distinguish the inverse weights. The general two-scalar formula (4) is essential.

Source gauges and block scalings act transitively on the whole subbundle torus `a_m b_m c_m != 0`. Therefore kappa/r is constant, proving (1). Nonzeroness of C_mult follows from the already proved ACTUAL relation `kappa=k/r_xi`, where `xi=r_xi At_F(D0)` and both k and r_xi are nonzero. It does not follow by composing two merely nonzero channel maps.

The Hamiltonian rule under an arbitrary GL(W) change is `g*D_a=(det g)^(-1)D_(g*a)`. For the scalar block this says exactly that each FIXED D_a commutes with g. Replacing it by `D_(g*a)` without its determinant factor would invalidate (4).

## 2. The apolar transport weight, including actual frames

On a negative chart write the transverse positive root coordinates as X,Y. Under the block scaling, they transform by

    (X,Y) -> T(X,Y),       T^2=lambda/mu.

The lowest normal adjoint has form

    eta_8=[[R,0],[P,-R]],

where R has positive-cover degree zero and P degree two. Its physical twist is -2. The actual homogeneous cubic/quintic generators have degrees three and five, so the comparison of their middle frames is diagonal with factors `T^(-3),T^(-5)`, up to a common scalar. Consequently

    diag(T^-3,T^-5) [[R,0],[T^2 P,-R]]
        diag(T^3,T^5) = [[R,0],[P,-R]].                (5)

The common scalar used to adjust the determinant has no effect on this adjoint identity. The physical O(-2) frame on the negative chart contributes mu^(-2), while the base coordinate z=v/u is fixed. Thus the lowest component transports with factor mu^(-2), independently of lambda.

This calculation remains valid for the ACTUAL bundle, not just its homogeneous approximation. A triangular quintic-generator transition has degree-two lower entry, preserves the zero upper entry, and leaves the diagonal unchanged. The actual conic correction is `I-t n`, where the entries of n have cover degrees 6,8,10. Its conjugation raises the relevant trace degree by eight and cannot alter the degree-zero diagonal. The earlier normal-diagonal theorem proves that the actual invariant normal line projects NONTRIVIALLY to this lowest diagonal line. Since the source line is one-dimensional, this projection is injective. The computed leading transport therefore determines transport of the full invariant class:

    g*eta_ap=mu^(-2) eta_ap,new.                       (6)

Under source coefficient gauges the actual bundle and its fixed Serre/vertex marking can be identified over the identity, so eta_ap is unchanged. The full higher parts of eta_ap are not asserted to vanish.

There is a separate equation factor when transporting a first-normal DISPLACEMENT. The transition `I+q0 c eta_ap` pulls back to `I+lambda^2 q0 c g*eta_ap`. Hence its coefficient in the new fixed-q0 description is multiplied by `lambda^2 mu^(-2)`, not merely by mu^(-2). This distinction will make (3) covariant.

## 3. Edge normalization versus apolar normalization

Retain `Delta=det(V+W)` in the monad:

    M: N O(-1) -> Wprime K -> N* Delta,
    K=Omega^2(2),  det F=Delta O(-1).

The symmetric adjoint complex is twisted by `(Delta O(-1))^(-1)`. Its invariant beta_E line is `Lambda^2(Wprime) Delta^(-2)`. The equivariant hypersurface sequence adds the equation line R_q to the eta_E edge. Since R_q has block weight lambda^2, the exact transport factors are

    source Wprime gauge S:   eta_E -> S^(-2) eta_E,new,
    block scaling:          eta_E -> lambda^(-4) mu^(-4) eta_E,new.

These are TRANSPORT factors between canonically generated edge lines; they are not the coordinate transformation of a scalar function multiplying eta_ap.

Write `eta_E=f(a_m,b_m,c_m) eta_ap`. Comparing the two sides of this identity under the preceding transports and (6) gives

    f(S a_m,S b_m,R c_m)=S^2 f(a_m,b_m,c_m),
    f(lambda^3 a_m,lambda mu^2 b_m,lambda^2 mu c_m)
         =lambda^4 mu^2 f(a_m,b_m,c_m).

The product a_m b_m has exactly these weights. Transitivity therefore gives (2). Both generators are nonzero and the lowest projection is an actual isomorphism of invariant lines, so C_ap is nonzero. This uses the full determinant factor: dropping Delta would change these weights and break the comparison.

## 4. The root comparison is an actual affine comparison

Use the actual F|2Q as origin and the positive exponential transition convention. The normal derivative theorem, with `delta_q0 eta_E=beta_E`, identifies the obstruction as

    ob(s)=(s+d s^2) beta_E|Q,
    d=K_cup b_m^2 != 0.

Its two actual ambient roots are `0` and `-1/d`. The midpoint is `-1/(2d)`. Thus the displacement FROM the midpoint TO the actual endpoint is exactly `eta_E/(2d)`, proving (3). Its bracket-normalized counterpart is its negative, by the independently checked boundary sign.

The constants in the b-square theorem and in (1) are different constants: K_cup is a normal cup coefficient in `H2(B_Q(-4))`, whereas C_mult specifies actual multiplication in `H1(B(2))`. Their both being nonzero does not identify them.

Under a block change, d acquires weight lambda^2 mu^4. The natural pullback of `eta_E/(2d)` therefore has factor lambda^(-2) relative to the NEW displacement. Multiplication by the additional lambda^2 from `g*q0` gives exact covariance of the transition. Equivalently (3) has the weight of r, as required by Section 2. Under source gauges both eta_E and d change by the same scalar coordinate factor, so the displacement is gauge-independent.

## 5. The Serre parameter and the boundary probe

Fix a common nonzero reference vertex residue across the one-parameter quotient family; this is a marking, not an assigned actual channel value. Let rho_C denote the resulting conic cocycle coefficient. The intrinsic conic and vertex residue characters are mu^(-2) and mu^2 when the positive block is fixed. Vertex normalization therefore gives rho_C weight mu^(-4). Since r has weight mu^(-2), transitivity gives

    rho_C=C_res r^2,             C_res != 0.             (7)

The common scalar block acts trivially on this residue ratio, so its general block weight is `(lambda/mu)^4`. If one retains an unnormalized varying vertex residue, (7) applies to its ratio with the conic residue, multiplied by the chosen reference vertex residue; it must not be asserted for an independently rescaled raw residue.

There is an exact deformation diagram behind (7). Let KS_r be the Kodaira-Spencer class of the monad ratio curve, with the other gauges fixed. The block-Euler vector differentiates r as `-2r`, so

    At_F(D0)=-2r KS_r.

In the normalized Serre presentation `I-rho_C n/z`, differentiation gives `KS_rho=-[n/z]`. Restriction of KS_r and the derivative of (7) therefore give

    KS_r|Q=-(2rho_C/r)[n/z],
    At_F(D0)|Q=4rho_C[n/z].                            (8)

This recovers the independently established full normalized weight four. The diagram compares AMBIENT and CONE moduli tangents. It does not identify either with the first-normal tangent eta_E, which belongs to a different relative deformation problem.

Finally fix `N=theta n` and define `xi=delta_(q0,F)(N)`, with theta retained. The existing boundary/sign comparison says

    c_eta+/k=-2rho_C/(theta kappa_F).

Combining (1),(3),(7) gives the exact relation among universal normalizations

    k=-theta C_ap C_mult/(4 C_res K_cup).               (9)

Thus k is constant along this normalized monad ratio family. Equation (9) does not evaluate any of its constants; an independently normalized cyclic xi would require its additional comparison factor. In particular the root theorem alone has not computed C_mult.

As frame checks, replacing q0 by nu q0 with N fixed sends

    kappa,C_mult -> (kappa,C_mult)/nu,
    eta_E,C_ap -> nu(eta_E,C_ap),
    d,K_cup -> nu^2(d,K_cup),
    c_eta+ -> c_eta+/nu,       k -> k/nu^2.

Equations (1)-(3),(9) remain unchanged as framed identities. Rescaling the fixed Hamiltonian volume rescales C_mult and k together. Rescaling the two monad channel bases independently changes the displayed universal constants; that is why declaring C_mult=1 by a basis change is not an evaluation in the pinned geometric markings.

## 6. The exact remaining global homotopy

Let `D_M=Hom^bullet(M,M)` be the full chain-Hom complex of the locally free monad. It computes End(F). The trace-free direct summand computes B; one can equally use the determinant-valued symmetric adjoint complex. Differentiate the NATURALLY LINEARIZED monad under a projective field D to obtain its closed global degree-one deformation cochain `delta_D M`. Its class is precisely At_F(D), not an arbitrary isomorphism of representation spaces.

For D0 use the trace-free ambient representative

    diag(-(2/5) I_V,(3/5) I_W).

Its left-channel derivative is

    (-6a_m/5, 4b_m/5, -c_m/5).

Infinitesimal source gauges remove the a_m and c_m entries and leave exactly `(0,2b_m,0)`. Apply their dual gauges on the right as well. This keeps Delta fixed and avoids silently dropping the determinant contribution from a trace-two Euler representative. Each negative trace-free Hamiltonian acts only on the c_m channel; the a_m volume(V) and b_m volume(W) channels are fixed. Both differentiated arrows still belong to the full closed deformation cochain.

At twist two, every sheaf term `Hom(M^i,M^j(2))` has no higher cohomology. Apart from constant coefficient spaces and determinant lines, the terms are

    O(1), O(2), O(3), K(2), K(3), End(K)(2).

For the last one use `K*=K(1) Delta^(-1)` and

    End(K)(2)=Delta^(-1) [S_(2,2)Q*(3)
                       +S_(2,1,1)Q*(3)+Lambda^4 Q*(3)].

Each displayed Schur bundle is Bott-dominant: its twist 3 is at least its largest partition part. The K terms satisfy the same criterion, and the line bundles are positive. Consequently

    H1(B(2)) = H1(Gamma(D_M(2)))_trace-free.             (10)

In particular C_mult is determined by the following GLOBAL identity, with the smoothing direction a left arbitrary:

    d_M T_a = a delta_D0 M
               -q0 C_mult (a_m/b_m) delta_Da M.         (11)

The degree-zero homotopy consists of polynomial maps on the three monad terms. Writing its components as T_-,T_0,T_+, (11) includes BOTH equations

    (delta alpha)_required = T_0 alpha-alpha T_-,
    (delta beta)_required  = T_+ beta-beta T_0.

The determinant-valued adjoint relation must be respected, or imposed by the fixed-duality trace-free projection. The actual cyclic theorem proves that a unique scalar C_mult admits such a homotopy. Formula (10) shows there is no extra higher-Cech obstruction to finding it. This note does not construct T_a or determine that scalar.

One may express the c-channel intrinsically through the Cartan projection `A tensor W -> Sym^3 W`, the fixed invariant cubic isomorphism `Sym^3 W -> Sym^3 Wprime`, and the Cartan embedding into `Wprime tensor V`. The b-channel is the universal binary Clifford tensor, and the a-channel is volume(V). Such expressions can be used to try to prove (11) by universal contractions. Nonzero legs, the common four-dimensional cubic constituent, and the separate b-square normal cup do not by themselves prove (11) with any proposed constant.

## Sources and verification

The channel classification and transitivity are the pinned three-channel monad-family theorem (PR643), also recorded locally in UNIVERSAL-THREE-CHANNEL-MONAD-ISOTROPY.md. The determinant edge factors and K_cup are from NORMAL-QUADRATIC-COEFFICIENT-UNIVERSAL-B-SQUARE.md, with nonzeroness and both actual roots supplied by the Serre-residue double-cover theorem. The nonzero lowest diagonal, apolar generator, and full conic transition are their separately frozen actual theorems. The boundary/Atiyah normalization is ACTUAL-BLOCK-EULER-ATIYAH-CLASS-AND-ENDPOINT-SCALE.md.

Run `python verify_monad_ratio_edge_apolar_root_comparison.py`. The verifier checks the full two-scalar covariance, unique character monomials, root-frame and stabilizer identities, exact root displacement, equation-frame factors, the deformation derivatives, and every Bott dominance condition used in (10). It performs no actual coefficient assignment or rank test. Identity (11) is the explicit remaining task, not a test silently claimed to have passed.
