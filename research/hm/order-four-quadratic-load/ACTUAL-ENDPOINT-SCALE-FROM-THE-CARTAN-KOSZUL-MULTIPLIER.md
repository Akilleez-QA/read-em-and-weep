# The fixed-boundary endpoint scale after the Cartan--Koszul comparison

## Exact marked consequence

Retain the physical normal equation q0, the actual three-channel monad coefficients
(a_m,b_m,c_m), the algebraic Clifford tensor M=i_v L, and the volume tau. Define

    r=a_m/b_m,
    M(v)^2=chi q0(v) I,
    tr(M(xi)[M(eta),M(zeta)])=g_L tau(xi,eta,zeta).

The trace is the full two-dimensional trace. All coefficients and normalization
constants below remain unassigned. The complete global homotopy in
UNIVERSAL-CARTAN-KOSZUL-MULTIPLIER-HOMOTOPY.md gives

    kappa=-(chi/g_L) r,
    a At_F(D0)=q0 kappa At_F(D_a).                       (1)

This note records the exact consequence for the already fixed actual boundary
normalization. It introduces no new evaluation of a source instance or fourth
Bockstein value.

Use the cone marking n=sigma sigma^t J0, the actual nilpotent N=theta n, and the
actual conic transition I-(rho_C/z)n. Define the cyclic source and probe by

    xi=delta_(q0,F)(N),    a xi=q0 zeta_a,
    zeta_a=k At_F(D_a).

Let eta_ap be the apolar generator with [eta_ap,n]=2[n/z]. Define eta_+ as the
POSITIVE logarithmic transition displacement from the midpoint m to the chosen
actual endpoint:

    P^F=P^m(I+q0 eta_+) mod q0^2,
    eta_+=c_+ eta_ap.

For the target-minus-transport boundary convention, the fixed equality is
xi_Q=-[eta_+,N]. Thus the bracket-normalized displacement is eta_b=-eta_+,
not eta_+. Substitution of (1) in the independently proved boundary comparison
c_+/k=-2rho_C/(theta kappa) gives

    c_+/k = 2rho_C g_L/(theta chi r),
    c_b/k = -2rho_C g_L/(theta chi r).                 (2)

These are ratios in the fixed geometric markings. In particular the sign in
(2) is not selected by merely choosing an invariant tangent direction.

## Compatibility with the normal-root marking

The actual edge and monad-ratio comparison supplies the nonzero constants

    eta_E=C_ap a_m b_m eta_ap,
    d=K_cup b_m^2,
    eta_+=eta_E/(2d),
    rho_C=C_res r^2.

The last equality uses a fixed vertex residue; it is not the transformation law
of an unnormalized raw conic residue. Consequently

    c_+=C_ap r/(2K_cup),
    k=theta C_ap chi/(4C_res K_cup g_L).                (3)

No constant in (3) has been set to one. The conformal scalar of the actual cubic,
the Serre marking, and the normal-cup normalization remain retained in their
respective constants. Equation (3) compares their already fixed meanings; it is
not a license to identify those constants or to replace the actual probe by an
independently normalized cyclic generator.

## Frame checks

1. If q0 is replaced by nu q0 with N fixed, chi and kappa are divided by nu,
   while g_L and r are unchanged. The normal-root marking changes
   C_ap -> nu C_ap and K_cup -> nu^2 K_cup. Thus c_+ -> c_+/nu,
   k -> k/nu^2, and both sides of (2) acquire the factor nu.
2. If sigma -> l sigma with determinant fixed, rho_C and theta are both
   divided by l^2. Equation (2) is unchanged. Since C_res is divided by l^2,
   equation (3) is unchanged as well.
3. Reexpressing the same channels by L -> sL and tau -> t tau requires
   a_m -> a_m/t and b_m -> b_m/s. Then chi -> s^2 chi,
   g_L -> (s^3/t)g_L and r -> (s/t)r. Hence kappa and the ratio in (2)
   are unchanged. This is a channel reexpression, not an assigned source value.
4. At the marked endpoint exchange mu^2=-1, r changes sign and rho_C is
   unchanged. With N held fixed and xi redefined as its actual endpoint
   boundary, k is unchanged whereas c_+ changes sign, exactly as in (2).
   Transporting an independently normalized xi would be a different convention.

An independent change of determinant frame does not change the ALGEBRAIC
Clifford tensor used to define chi and g_L. It must not be confused with changing
only the pairing-defined cross operator while silently retaining its scalar
identification with M=i_v L.

## Scope and sources

The sign, trace-free block-Euler normalization, and fixed actual boundary are
proved in ACTUAL-BLOCK-EULER-ATIYAH-CLASS-AND-ENDPOINT-SCALE.md. The edge,
normal-root, residue and equation-frame factors are in
ACTUAL-AMBIENT-ATIYAH-MULTIPLIER-IS-THE-MONAD-RATIO.md. The only new input
in this consequence is the complete displayed global multiplier homotopy.

This does not identify a displayed monad null-homotopy with a second division
q0 v_h=a h zeta_a, and it does not compute any fourth Bockstein value.

Run python verify_actual_endpoint_scale_from_cartan_multiplier.py. The verifier
checks every equality and all four frame tests with free nonzero symbols. No
actual source coefficient, actual-instance matrix, rank, or scan is used.
