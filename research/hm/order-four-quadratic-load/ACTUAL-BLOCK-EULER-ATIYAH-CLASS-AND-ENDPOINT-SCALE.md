# The actual block-Euler Atiyah class and the remaining endpoint scale

## Result

Fix the physical normal equation `q0`, the actual Serre marking on the cone, and

    J0=[[0,-1],[1,0]],   n=sigma sigma^t J0,
    N_C=-n,
    t=rho_C/z.

The conic transition in these conventions is `I+tN_C=I-t n`. Let `D0` be the projective vector field which scales the negative coordinates `(u,v)` and fixes the positive coordinates. Its trace-free ambient representative is

    diag(-(2/5) I_V, (3/5) I_W).

No additional integral normalization of the block-Euler field is implicit. With the positive Atiyah cocycle `D(P)P^(-1)`, the exact actual comparison is

    At_G(D0)|U = -4rho_C [N_C/z] = 4rho_C [n/z],
    U=X minus C.                                      (1)

The factor FOUR uses both residue characters. Differentiating the conic character `mu^(-2)` alone would give the wrong answer.

Let `eta_ap` be the globally normalized invariant normal class whose leading apolar representative is the one in APOLAR-NORMAL-SECTION-HAS-UNIT-EULER-COEFFICIENT.md. Then

    [eta_ap,n] = (1/(2rho_C)) At_(F_Q)(D0).             (2)

This is an actual comparison of the invariant cohomology lines, not merely a count of their dimensions.

The remaining absolute comparison is a SINGLE distinct ambient multiplier. Define

    a At_F(D0) = q0 kappa At_F(D_a),                   (3)

using the fixed Hamiltonian convention for `a -> D_a`. The actual cyclic and Atiyah theorems prove that `kappa != 0`, but do not evaluate it. For `N=n`, the boundary-normalized actual probe and the bracket-normalized normal displacement obey

    c_eta_b/k = 2rho_C/kappa.                         (4)

The positive logarithmic transition displacement has the opposite sign, as made precise in Section 3. Thus (4) does not silently identify an arbitrary invariant tangent vector with the actual endpoint displacement, or silently choose a sign for it.

No spinor bundle on `2Q`, midpoint extension to `3Q`, or fourth Bockstein value is asserted. All source, residue, and comparison scalars remain unassigned. Existing frozen artifacts are unchanged.

## 1. Why the normalized infinitesimal conic weight is minus four

The actual marked extension on X has residue expression

    e=rho_C e_C+rho_v e_v,

where the block torus `phi_mu` has weights `mu^(-2)` and `mu^2` on the two summands, respectively. This includes the physical determinant factors, as proved in ACTUAL-CONIC-RESIDUE-FORCES-VERTEX-SERRE-COCYCLE.md. Therefore

    phi_mu^* e=mu^(-2)rho_C e_C+mu^2rho_v e_v.

To compare the varying MIDDLE bundles with the fixed vertex eigenextension, normalize the vertex residue, not the conic residue. Multiplying the marked extension class by the common factor `mu^(-2)` gives

    e(mu)=mu^(-4)rho_C e_C+rho_v e_v.                 (5)

Rescaling the outer terms in an extension does not change the isomorphism class of its middle bundle. Its induced determinant factor can be adjusted by a central square root near `mu=1`; this changes only the scalar part of the connection, not the trace-free Atiyah class. This normalization is a family of cone markings, not a spinor lift to a normal thickening.

The homogeneous triangular presentation is the unique vertex eigenextension, including its full extension character, by ACTUAL-GLOBAL-SERRE-LIFT-FROM-THE-CONIC-COCYCLE.md, Section 1. Its torus linearization trivializes its contribution to the orbit derivative on U. In these comparison frames the ONLY varying transition is

    I+mu^(-4)t N_C.

Its derivative at `mu=1`, multiplied by its inverse, is exactly `-4tN_C`. The putative quadratic term is zero because `N_C^2=0`. This proves (1).

Equivalently, the pure vertex linearization has subline/quotient ratio `mu^(-2)`, so conjugation gives N_C the character `mu^(-2)`. The coefficient t has the physical `O(-2)` character `mu^(-2)`. Their product therefore has character `mu^(-4)`. This is the same calculation retaining the two line factors individually.

Twisting `F_Q` to the stack Serre bundle G changes its Atiyah class only by a scalar line-bundle contribution. The trace-free classes in (1) are consequently those of the actual `F_Q`. No torus action on the actual G is assumed: the torus acts on its orbit, and a linearization is used only for the pure vertex comparison bundle.

## 2. Comparison with the apolar bracket

The apolar Euler theorem proves, using its full regular wedge lifts and physical coefficient lines,

    [eta_ap sigma]=[sigma/z],
    [eta_ap,n]=tau([sigma/z])=2[n/z].                (6)

The first equality is not obtained by taking just the diagonal of eta_ap; that diagonal has coefficient four, whereas its section image has coefficient one. The source theorem retains the compatible nilpotent trace corrections responsible for this distinction.

Both the actual bracket and the restriction of `At_F(D0)` lie in the invariant line `H1(B_Q)^G`. The latter's lowest coefficient is nonzero by (1), because `rho_C != 0` and the Euler class is nonzero. Hence comparison of their lowest coefficients in (1),(6) identifies their full invariant cohomology classes and proves (2). Higher parts of the actual normal class cannot change this ratio: the projection of this one-dimensional invariant target to its displayed lowest coefficient is injective.

If the pre-existing nilpotent marking is `N=theta n`, retain theta rather than setting it to one. Then (2) reads

    [eta_ap,N]=(theta/(2rho_C))At_(F_Q)(D0).          (7)

The factor theta is a fixed marking conversion, not an additional ambient multiplication scalar.

## 3. Which displacement has bracket equal to the actual boundary?

Let m be the midpoint first-normal extension. Its actual adjoint has the unique lift of N from MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md. In particular `delta_m(N)=0`. The extension F restricted to `2Q` is the chosen actual endpoint.

Fix source-to-target transition matrices and define the Cech boundary of local adjoint lifts by

    delta_e(N)_ij=(N_j-P_ij^e N_i (P_ij^e)^(-1))/q0.

This is the target-minus-transport convention already used for the normal operator discrepancies. Write the actual endpoint relative to m as

    P_ij^F=P_ij^m(I+q0 eta_+,ij) mod q0^2.           (8)

Using the midpoint's actual adjoint lift in the boundary formula gives

    delta_F(N)=-[eta_+,N].                           (9)

Thus define the BRACKET-normalized displacement

    eta_b=-eta_+,
    P_ij^F=P_ij^m(I-q0 eta_b,ij),
    [eta_b,N]=xi_Q,
    xi=delta_(q0,F)(N).                              (10)

The last equality fixes xi by the actual ambient boundary. Naturality of the restriction sequences identifies its restriction with `delta_F(N)` above, without a freely chosen scalar. The bracket is an isomorphism of invariant lines, so (10) uniquely specifies eta_b. An arbitrary nonzero eta is not automatically eta_b: it may be any scalar multiple of it.

There is a useful independent sign check. Under the POSITIVE transition change in (8), the target-minus-transport defect of a first-order operator has variation

    [O,eta_+]+H rho eta_+,

where `Dq0=rho q0`. Indeed the transformed connection is

    A -> A+q0([eta_+,A]-H Deta_+-H rho eta_+),

so its target-minus-transport discrepancy has the opposite sign. This is exactly the sign of the endpoint secondary operator `L_4` computed in the two-input package. Therefore, in these conventions, the actual endpoint-minus-midpoint contribution to that operation uses eta_+, whose scale is minus the bracket-normalized scale in (4). A simultaneous reversal of Cech boundary convention reverses the corresponding definitions together; it is not permission to change just one sign.

This argument takes place entirely in the adjoint of the actual first-normal extensions. It does not require a Serre section or spinor line to lift to `2Q`.

## 4. Reduction to the one ambient Atiyah multiplier

The actual orbit-tangent isomorphism and invariant multiplicity give a unique nonzero r with

    xi=r At_F(D0).

The actual fixed-probe relation is

    a xi=q0 zeta_a,
    zeta_a=k At_F(D_a).

Dividing these equalities by r gives (3) with

    kappa=k/r.                                      (11)

This defines an actual ambient multiplication coefficient; its nonzeroness follows from `k,r != 0`. Its value is not supplied by the one-dimensional A multiplicity.

Write `eta_b=c_eta_b eta_ap`. Combining (7),(10),(11) gives the complete comparison

    c_eta_b=2rho_C r/theta,
    c_eta_b/k=2rho_C/(theta kappa),
    c_eta_+/k=-2rho_C/(theta kappa).                  (12)

If the published cyclic generator was independently normalized as xi_old, it must first be compared to the actual boundary: if `delta_F(N)=b xi_old`, then `k_boundary=b k_old`. Formula (12) uses the boundary-normalized k, not k_old with b silently omitted. The current task's normalization `xi=delta_F(N)` is precisely the one in (10)-(12).

Under a rescaling of the Serre section with determinant fixed, `sigma -> l sigma`, the variables change as `n -> l^2 n`, `rho_C -> l^(-2)rho_C`, and, if N is held fixed, `theta -> l^(-2)theta`. Thus the right side of (12) is marking invariant. If `q0 -> nu q0` with N fixed, then `xi -> xi/nu`, `k -> k/nu^2`, `kappa -> kappa/nu`, and `eta_b -> eta_b/nu`; both sides of (12) transform identically. This retains the physical normal-equation factor rather than assigning it a value.

## 5. A genuine remaining mismatch: cone data do not select kappa

Let `phi=phi_mu` with `mu^2=-1`, and let `F'=phi^*F`, marked by the established cone isomorphism. The fixed vector fields `D0,D_a` commute with phi, while

    phi^*a=-a,       phi^*q0=q0.

Naturality of the actual Atiyah class applied to (3) therefore gives

    kappa_(F')=-kappa_F.                            (13)

The cone bundle and the restricted Atiyah classes for D0 and D_a are the same under this marking. Thus their cone descriptions, even with all the residue factors above, do not fix the sign of the ambient coefficient in (3). A further actual ambient multiplication comparison is necessary.

It is essential to distinguish TWO normalizations of xi under this exchange. The cone marking sends the naturally pulled-back nilpotent to `-N`. If N is held fixed and xi is defined as its endpoint boundary as in (10), then

    r_(F')=-r_F,
    k_(F')=r_(F') kappa_(F')=k_F.                   (14)

The endpoint displacements and their c_eta scales change sign. In contrast, if xi is transported naturally, rather than redefined as the boundary of the fixed N, its Atiyah coefficient r is unchanged and its cyclic scalar k changes sign. These are different legitimate normalizations. Importing the latter sign rule into (12) would silently change the boundary normalization.

Equations (12)-(14) isolate the unresolved quantity rather than claim that the endpoint scale has been evaluated. Specifying the absolute Euler coefficient of xi_Q would also determine it directly, but merely stating that xi is an actual boundary does not compute that coefficient. No fourth value follows from this comparison.

## Sources and verification

The actual Atiyah/cyclic normalization is ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md. The two residue characters, conic cocycle, and unique homogeneous vertex marking are in the conic-residue theorem and ACTUAL-GLOBAL-SERRE-LIFT-FROM-THE-CONIC-COCYCLE.md. The normalized apolar bracket is APOLAR-NORMAL-SECTION-HAS-UNIT-EULER-COEFFICIENT.md. The midpoint and its actual adjoint lift are in MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md. The ambient/cone invariant restriction isomorphism and orbit tangent are the pinned negative-monad and EXACT-AMBIENT-ADJOINT-DEFORMATIONS.md results.

Run `python verify_block_euler_atiyah_endpoint_scale.py`. It reruns the exact apolar Euler certificate, checks the two residue weights and normalized torus derivative, checks the boundary and operator signs for the same positive transition, and checks all scalar, marking, equation-frame, and endpoint-exchange relations above. It assigns no actual coefficient or parameter values, performs no rank calculation, and changes no frozen file.
