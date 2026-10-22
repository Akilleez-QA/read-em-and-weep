# Clifford volume normalization of the remaining ambient multiplier

## Result

The unknown universal ambient multiplier has one residual normalization-free scalar. Let the fixed b-channel tensor be

    L in sl(U) tensor V,       M_x=i_x L,
    M_x^2=chi q0(x) I_U.

Let tau in Lambda^3 V be the fixed volume tensor defining the a-channel. Define g_L by the EXACT alternating identity

    tr(M_x [M_y,M_z])=g_L tau(x,y,z).                 (1)

Both chi and g_L are nonzero. With b_q the symmetric polar form of q0, the full Clifford triple product is

    M_x M_y M_z
      =chi[b_q(x,y)M_z-b_q(x,z)M_y+b_q(y,z)M_x]
         +(g_L/4)tau(x,y,z) I_U.                    (2)

Consequently the ratio

    c_abs=C_mult g_L/chi                            (3)

is unchanged by independent changes in the a-channel and b-channel scalar markings, and by rescaling the physical equation q0. Thus

    C_mult=c_abs chi/g_L.                            (4)

Equation (4) does NOT evaluate c_abs. The common Cartan/Clifford homotopy equations are still required to determine that number. In particular, neither (2) nor a normal cup scalar alone gives its value.

## 1. Intrinsic definition and nonvanishing

The nonzero Clifford tensor identifies V* with sl(U). This is an isomorphism of the fixed three-dimensional irreducibles, not a rank assertion at a coordinate point. The trace pairing on sl(U) is nondegenerate and its Cartan alternating form

    (X,Y,Z) -> tr(X[Y,Z])

is nonzero. Indeed, a zero form would make every bracket orthogonal to all of sl(U), forcing the bracket to vanish, contrary to sl(U) being a nonabelian simple Lie algebra. Pulling back along the isomorphism proves g_L != 0 directly. It is not an inference that a composite of nonzero maps is automatically nonzero.

The same isomorphism pulls back the nondegenerate trace quadratic to the nonzero invariant q0 line. This proves chi != 0 and gives

    (M_x M_y+M_y M_x)/2=chi b_q(x,y) I_U.            (5)

Here b_q(x,y)=(q0(x+y)-q0(x)-q0(y))/2, so q0(x)=b_q(x,x). The cubic coefficient g_L in (1), including the trace rather than half-trace, is part of the marking. It is not silently normalized to 1.

## 2. Proof of the exact triple product

Every traceless endomorphism of a two-dimensional space satisfies its characteristic identity. Polarizing yields

    XY+YX=tr(XY) I.

Applying this repeatedly, or polarizing the same identity once more, gives

    XYZ=(tr(XY)Z-tr(XZ)Y+tr(YZ)X)/2
          +tr(X[Y,Z]) I/4.                          (6)

Substitute X=M_x,Y=M_y,Z=M_z and use (1),(5). This proves (2) as an identity of actual universal tensors, not modulo a source gauge or cohomology class.

There is also an exactly marked commutator formula. Define the q0-cross product by

    b_q(x cross_q y,z)=tau(x,y,z).

Then nondegeneracy and (1) imply

    [M_x,M_y]=(g_L/(2chi)) M_(x cross_q y).          (7)

The factor 2 here and factor 4 in (2) are tied to the full trace convention in (1).

## 3. Channel changes versus physical equation changes

The fixed actual monad is written

    alpha=[c_m C0 | a_m A0+b_m B0],
    A0 defined by tau,    B0 defined by L and omega_W.

If tau -> t tau and L -> s L, the same monad has

    a_m -> a_m/t,       b_m -> b_m/s.

Its intrinsic ambient multiplier kappa is unchanged. Since the frozen ratio theorem gives kappa=C_mult a_m/b_m, the coefficient in the new channel markings is

    C_mult -> (t/s) C_mult.

Meanwhile

    chi -> s^2 chi,        g_L -> (s^3/t)g_L.

Thus (3) is invariant. Rescaling the Cartan channel alone is absorbed by c_m and has no effect on either side of (3).

For q0 -> nu q0 with all channel tensors fixed, the same ambient relation gives C_mult -> C_mult/nu, while chi -> chi/nu and g_L is unchanged. Again (3) is invariant. The Hamiltonian convention and its GL2 determinant line remain fixed throughout; an independent rescaling of the Hamiltonian map would change the remaining number and is not authorized by these invariances.

## 4. Determinant frames are not channel changes

In this note M_x=i_x L is the ALGEBRAIC Clifford tensor. In the compatible determinant frame Omega=tau wedge omega_W it agrees with the scalar representative of the pairing-defined A0*B0 used in the global homotopy.

If only the bookkeeping frame of Delta is rescaled while tau, omega_W and L are held fixed, the pairing-defined scalar representative rescales, but this algebraic M_x does not. One must transport the Delta factors in the adjoints; one must NOT replace M_x by its rescaled pairing representative in (1) while keeping tau and chi fixed. The full primitive and its Delta-squared cancellation are checked in the separate Clifford-homotopy note. This paragraph prevents a spurious determinant-frame dependence in (3).

## 5. Scope

The new exact input is the marked Fierz system (2),(5),(7), together with the reduction (4). It identifies the cubic Clifford-volume scalar that a successful remaining Cartan homotopy must respect. The number c_abs is not supplied by a choice of channel basis, the nonzero normal cup, a nonzero intermediate map, or an actual-instance test. No actual coefficient, point, monad matrix or differential rank is evaluated here.

Run `python verify_clifford_volume_multiplier_normalization.py`. It verifies the complete universal traceless-two-by-two identities and every stated scaling law with independent symbolic coefficients. The matrices in that verification are the universal representation of sl2, not selected source matrices. All previous frozen artifacts are unchanged.
