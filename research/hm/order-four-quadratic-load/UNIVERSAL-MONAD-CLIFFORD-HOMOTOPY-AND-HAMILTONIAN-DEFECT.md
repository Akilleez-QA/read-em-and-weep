# Universal Clifford homotopy and the Hamiltonian lift defect

## Checked result and remaining gate

There are two explicit global tensor constructions for the actual three-channel monad, with all source coefficients `a_m,b_m,c_m` unassigned and nonzero:

1. A determinant-compatible degree-two chain homotopy for `q0 delta_D0 M`. This gives an explicit monad-level certificate of the already known cohomological annihilation `q0 At_F(D0)=0`.
2. A determinant-compatible lift of `q0 delta_D M`, for every negative trace-free Hamiltonian `D`, whose entire remaining defect is the explicit rank-one tensor in (7) below. An off-diagonal source gauge removes its volume-channel part and leaves (9).

These are new chain-level formulas, not a determination of `C_mult`. In particular, the remaining defect is not asserted to equal the negative-quadratic multiple of the block-Euler derivative with any proposed constant.

## 1. Fixed tensors and determinant markings

Write `H=V+W`, `U=Wprime`, and `N=A+U`. Choose the fixed volume tensors `tau in Lambda^3 V` and `omega in Lambda^2 W` that define the channel markings, and put `Omega=tau wedge omega in Delta`. In this determinant frame the middle pairing is

    J_E(eta,zeta) (i_x Omega)=epsilon_U(eta wedge zeta),

for `E=U Omega^2(2)` and `x=(v,w) in H*`. Its intrinsic value lies in `Delta O(-1)`; writing a scalar coefficient uses the displayed frame and does not discard that line.

Let `L in End(U) tensor V` be the fixed traceless binary Clifford tensor and write `M_alg(v)=i_v L`. Define normalized channel arrows

    A_x(u)=u i_v tau,
    B_x(u)=i_x(L(u) wedge omega),
    C_x(z)=i_x Ctilde(z),

where `Ctilde:A -> U tensor Lambda^2 V tensor W` is the actual fixed third channel. Thus

    alpha|U=a_m A+b_m B,       alpha|A=c_m C.          (1)

Use the symplectic adjoint on the U source, defined by

    epsilon_U(u,A* eta)=J_E(Au,eta),

and similarly for B. Before trivializing Delta, `A*,B*` have target `U Delta`, and `A*B` has the additional factor `Delta O(1)`. In all subsequent adjoint formulas, define `M=A*B`. In the compatible frame `Omega=tau wedge omega`, the cross-pairing calculation gives `M=M_alg`. If Omega alone is rescaled while the channel tensors tau, omega and L are held fixed, the pairing-defined M rescales but M_alg does not; their displayed equality is then replaced by the corresponding frame factor.

## 2. Universal pairing identities

Exterior multiplication, with no source coefficient evaluation, gives

    A*A=B*B=A*C=B*C=0,
    A*B=M(v),                 B*A=-M(v).              (2)

For the cross identity, directly expand the four-form:

    (i_v tau) wedge i_x(L wedge omega)
       =M(v)[(i_v tau) wedge omega-tau wedge i_w omega]
       =M(v) i_x Omega.

The identities with C can also be read from the separately vanishing `a_m c_m` and `b_m c_m` coefficients of universal monad isotropy. They do NOT require concluding that separate nonzero maps have nonzero composite. In the intrinsic Cartan description, the C coefficient is the kernel of the Clifford contraction `U tensor V -> U`; this gives the same identities directly.

Put

    M(v)^2=Q(v) I,                 Q=chi q0, chi != 0. (3)

Here chi retains the physical-equation and fixed-channel normalization. It is not set to one. Intrinsically Q is Delta-squared valued. Formulas containing Q and two adjoints below have that same factor, so division by its constant coefficient chi is determinant-covariant.

## 3. A complete two-arrow annihilator homotopy

Set

    L_B=B M(v) B*,
    T0=-(2b_m/(a_m chi)) L_B,
    T_-=T_+=0.                                        (4)

This is globally of twist two: the two channel arrows and the linear Clifford tensor have precisely the required twists. There is no division by the coordinate polynomial q0.

Because `M*=-M`, one has `L_B*=-L_B`. Using (1)-(3),

    L_B alpha|U=-a_m Q B,
    L_B alpha|A=0.

Consequently `T0 alpha=q0 (0,2b_m B)`, exactly the source-gauge-reduced `q0 delta_D0 alpha`. The right monad arrow is the determinant dual of the left. Taking its adjoint gives

    delta beta=-beta T0=T_+ beta-beta T0.

Thus (4) solves BOTH arrow equations and preserves the fixed duality. This is an explicit certificate for a known annihilator, not a new inference about the unresolved mixed multiplier.

If the determinant frame Omega alone is replaced by `nu Omega` while A, B and L are held fixed, each adjoint and the pairing-defined `M=A*B` is multiplied by `nu^-1`. The held-fixed algebraic tensor `M_alg=i_v L` does NOT rescale. Thus Q and L_B, defined using the pairing-derived M, are both multiplied by `nu^-2`; their ratio in (4) is unchanged. This checks determinant-frame covariance without silently retaining `M=M_alg` in an incompatible frame.

## 4. A global middle lift for every negative Hamiltonian

Let D act on W with trace zero and trivially on V. Choose the fixed quadratic polar vector `r(v) in V` satisfying

    v(r(v))=q0(v).

Put `ell=w composed with D in W*` and

    P_D=q0 D-r(v) tensor ell.                          (5)

This polynomial endomorphism of H has degree two and satisfies

    x composed with P_D=0,              tr(P_D)=0.

It therefore induces `R_D=rho^2(P_D)` on `K=ker(i_x:Lambda^2 H -> H)`, and hence on E. It is global, of twist two, and skew for the determinant-valued middle pairing: the induced action on `i_x Omega` is zero. No pole along q0 occurs.

The naturally linearized monad deformation is the COEFFICIENT action

    delta_D(i_x Z)=i_x rho^3(D)Z
                 =rho^2(D)i_x Z+i_(x composed with D)Z.

The second summand alone is only differentiation in a fixed ambient wedge frame. It is not the monad cochain used here; the first summand is the natural K-pullback frame contribution. For ANY constant three-form coefficient tensor Z, the exterior derivation rule gives the exact identity

    q0 i_x rho^3(D)Z-R_D i_x Z
       =i_x[r(v) wedge i_ell Z].                       (6)

This is a universal tensor identity, not a claim modulo cohomology.

## 5. Exact residual channels and an off-diagonal gauge

Set `t=i_ell omega in W`. Define the polynomial source map `s_D:A -> U` of degree two by

    r(v) wedge i_ell Ctilde(z)=s_D(z) tau.

Applying (6) to the three coefficient types gives the complete left-arrow defect

    q0 delta_D alpha-R_D alpha:
      U -> b_m i_x[L wedge r(v) wedge t],
      A -> c_m A s_D.                                  (7)

The volume channel contributes zero. All signs in (7) follow from `i_ell(L wedge omega)=-L wedge t`.

Now take the degree-two source endomorphism whose only nonzero block is

    T_-|A -> U=-(c_m/a_m) s_D,                          (8)

and take the negative dual endomorphism on the right. Together with `T0=R_D`, this is a full determinant-compatible degree-zero chain cochain. Its differential minus `q0 delta_D M` has left-arrow component exactly

    U -> -b_m i_x[L wedge r(v) wedge t],
    A -> (b_m c_m/a_m) B s_D.                          (9)

The right-arrow residual is its prescribed determinant dual, not an independently omitted condition. Thus (9) isolates the remaining problem after a genuinely global, polynomial, two-arrow lift. It is not automatically zero, nor is its relation to the desired negative-quadratic b-channel established here.

## Reproduction and scope

Run `python verify_universal_monad_clifford_homotopy.py`. It checks the exterior identities and (6)-(7) with generic coordinate, Hamiltonian, polar-vector and Cartan symbols; the universal binary Clifford square; the skew-adjoint product; and the two-arrow algebra in (4). It constructs no actual HM monad matrix, chooses no source parameter values, computes no ranks and performs no scans. The only 2-by-2 matrices represent the universal sl2 Clifford identity. Universal isotropy, the actual channel identification and the physical comparison `Q=chi q0` are the retained geometric inputs. The mixed homotopy defining C_mult remains open.
