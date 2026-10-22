# A complete five-equation ansatz for the universal monad homotopy

## Result

The remaining ambient scalar problem has a complete, finite, determinant-compatible tensor ansatz. It does not require an actual-instance monad matrix. Write the normalized channel arrows as A0, B0, C0 and the left monad arrow as

    alpha=[c_m C0 | a_m A0+b_m B0],

where the columns have sources A and U=Wprime, respectively. The desired relation is multiplied by b_m to clear its known monad-ratio denominator.

After finite-group and torus equivariant projection, EVERY required global homotopy can be sought in the following form:

    T_middle=a_m M_a+b_m M_b,
    T_source,AA=a_m P_a+b_m P_b,
    T_source,UU=a_m Q_a+b_m Q_b,
    T_source,UA=c_m R,
    T_source,AU=(a_m b_m/c_m) S.                       (1)

The middle operator is symplectic-skew, and the right-source operator is the negative adjoint of the left-source operator. The coefficient maps in (1) depend LINEARLY on the smoothing direction a. Their polynomial coordinate types and complete intertwiner dimensions are established below.

The entire scalar determination is equivalent to the following FIVE universal identities:

    M_a A0=A0 Q_a,                                     (2a)
    M_a B0+M_b A0=A0 Q_b+B0 Q_a+C0 S,                  (2b)
    M_b B0-B0 Q_b=2a B0,                               (2c)
    M_a C0-C0 P_a-A0 R=-C_mult q0 D_a C0,              (2d)
    M_b C0-C0 P_b-B0 R=0.                              (2e)

The reverse source block S is allowed and cannot be omitted without proof. No assertion that its eventual value is nonzero is made. A tempting additional middle term `(a_m^2/b_m) M_2` is excluded EXACTLY by the absence of A in `V tensor V`. This is a genuine channel exclusion, not a dimension estimate for an actual map.

There are 14 possible intertwiners for M_a, 8 for M_b, and 12 for the six source-block coefficients together. These are dimensions of complete abstract representation spaces, not evaluated ranks. Equations (2) have not been solved, and C_mult has not been evaluated.

## 1. The symplectic homotopy is enough, with both arrows retained

Keep `Delta=det(V+W)` and the monad

    N O(-1) --alpha--> U K --beta--> N* Delta,
    N=A+U,   K=Omega^2(2),   beta=alpha^dagger.

The middle alternating form takes values in `Delta O(-1)`. The earlier twist-two acyclicity theorem identifies an exact cohomological relation with a GLOBAL degree-zero chain homotopy. Since its required deformation is fixed-duality and trace-free, projecting a homotopy by the duality involution gives one with

    T_middle^dagger=-T_middle,
    T_right=-T_source^dagger.

For such a homotopy the left equation is

    Z_alpha=T_middle alpha-alpha T_source.

Taking its adjoint gives the FULL right equation

    Z_beta=T_right beta-beta T_middle.

Thus the right equation is not dropped: it follows with its determinant line and sign from the imposed duality condition. The ansatz is a symplectic chain-homotopy ansatz, not an arbitrary endomorphism of the middle coefficient space.

Using the trace-free D0 representative and its actual source gauges, the required left deformation after multiplication by b_m is

    Z_alpha|U = 2 b_m^2 a B0,
    Z_alpha|A = -C_mult a_m c_m q0 D_a C0.              (3)

Here D_a differentiates the negative coordinate slot in C0, with the monad source coefficients held fixed. Changing that source linearization is a source gauge and belongs in P_a, not an unrecorded alteration of (3).

## 2. Why one may impose the parameter weights

The full parameter space is the affine torus `a_m b_m c_m != 0`. All its monads are coordinate/gauge equivalent, and their cohomology dimensions are constant. Thus the image and kernel sheaves of the finite global chain-Hom differential have constant rank. The actual scalar theorem says that the required section Z is in the image at every point.

The kernel sheaf is quasi-coherent on an affine torus, hence has no first cohomology. Therefore a global regular parameter-dependent homotopy exists. Its coefficients are Laurent polynomials, not arbitrary holomorphic functions. Finite-group invariants and the character components of the commuting algebraic tori are exact in characteristic zero, so a homotopy can be projected to the required equivariance and weight. This uses no evaluation of a parameter point or actual matrix rank.

For source gauges `g_N=diag(R_g I_A,S_g I_U)`, the left arrow becomes alpha g_N. The b_m-cleared Z transforms as `S_g Z g_N`. Hence

    T_middle,new=S_g T_middle,
    T_source,new=S_g g_N^(-1) T_source g_N.             (4)

For block coordinate scaling `(lambda I_V,mu I_W)`, the pulled-back relation and the fixed-Hamiltonian determinant rule give

    Z_new=lambda g*Z_old,
    T_new=lambda g*T_old.                              (5)

In (5) the direction a is the same fixed coefficient vector. Pullback of its polynomial contributes mu^2, while each fixed D_a commutes with the block scalar. The factor lambda follows from the b_m-clearing and is essential.

Combining (4),(5) yields the following possibilities before bounding coordinate weights. If p is an integer, they are

    middle and diagonal source blocks:
       a_m^p b_m^(1-p),    output block weight (2p,2-2p);
    source UA:
       c_m (a_m/b_m)^p,    output block weight (1+2p,1-2p);
    source AU:
       a_m^p b_m^(2-p)/c_m,
                             output block weight (2p-1,3-2p).

These are weights of the coordinate operators, not of actual numerical entries. Source coefficient spaces are constant under block coordinate scaling.

## 3. The complete coordinate bounds and the excluded channel

For a source-block operator the coordinate coefficients belong to Sym^2(V+W), whose positive-block degree is 0,1,or2. Consequently:

* diagonal source blocks allow only p=0,1;
* UA allows only p=0, with coordinate type V tensor W;
* AU allows only p=1, also with coordinate type V tensor W.

Thus P_a,Q_a have coordinate type Sym^2 V, while P_b,Q_b have type Sym^2 W=A. This proves all source blocks in (1), including the Laurent factor a_m b_m/c_m.

The middle symplectic operators have coefficient space

    H0(sp(U K)(2))
      =Delta^(-1)[V tensor S_(3,2,2)(V+W)
                  +S_(3,2,1,1)(V+W)]
         +V tensor Sym^2(V+W).                        (6)

This follows by splitting `Sym^2(U tensor K)` into `Sym^2 U tensor Sym^2 K` and `Lambda^2 U tensor Lambda^2 K`, retaining the determinant-valued alternating form. The Schur global sections are the Bott identifications already used in the twist-two acyclicity theorem.

In `S_(3,2,2)(V+W)` the positive degree ranges from 2 to7: its column heights are 3,3,1, and W has dimension two while V has dimension three. In `S_(3,2,1,1)` it ranges from 2 to6, by column heights 4,2,1. Subtracting the positive determinant degree three in (6), the possible middle positive block weights lie between -1 and4. The even weights `2p` therefore allow p=0,1,2 only.

The p=2 weight can occur solely in the pure-V piece of the first Schur summand. That coefficient is

    V tensor S_(3,2,2)V tensor det(V)^(-1)
      =V tensor V tensor det(V).

The finite perfect group has trivial det(V). Since `V tensor V=1+V+D5` and the parameter A is the OTHER three-dimensional irreducible, `Hom_G(A,V tensor V)=0`. The entire p=2 term is therefore absent. This proves the COMPLETE middle part of (1). Neither a hidden negative-power tail nor a further c_m-dependent middle term is left unaccounted for.

## 4. Exact coefficient extraction gives the five identities

Substitute (1) and alpha into `T_middle alpha-alpha T_source`.

On the U-source column the coefficients of `a_m^2`, `a_m b_m`, and `b_m^2` are, respectively,

    M_a A0-A0 Q_a,
    M_a B0+M_b A0-A0 Q_b-B0 Q_a-C0 S,
    M_b B0-B0 Q_b.

On the A-source column the coefficients of `a_m c_m` and `b_m c_m` are

    M_a C0-C0 P_a-A0 R,
    M_b C0-C0 P_b-B0 R.

Comparison with (3) proves equivalence with (2a)-(2e). No commutativity of the coefficient operators is assumed. The source parameters themselves commute and remain arbitrary.

This formulation isolates the true difficulty: one must solve the compatible Cartan/Clifford identities (2), with the same R appearing in (2d) and (2e), and with the S correction retained in (2b). A primitive for just one channel, or a Clifford identity proving q0 At(D0)=0, does not by itself supply (2).

## 5. Complete abstract intertwiner arithmetic

For reference, the source-block multiplicities are

    P_a: 3,   P_b: 3,   Q_a: 1,   Q_b: 1,
    R: 2,     S: 2.

Indeed `End(A)=1+A+D5`, `End(U)=1+V`, `Sym^2 V=1+D5`, and `A tensor U=V tensor W=T6`. The last two multiplicities use

    T6 tensor T6=1+2A+2V+2P4+3D5.

The middle weights in (6) can be checked without any source map. Put w=character(W), v=character(V), and let L count positive coordinate degree. The complete symmetric-function generating series for V+W is

    sum h_j t^j
      =1/[(1-vLt+vL^2t^2-L^3t^3)(1-wt+t^2)].

Use Jacobi-Trudi for the partitions (3,2,2) and (3,2,1,1), take coefficients L^5 or L^3, and add the last summand of (6). On the five A5 classes the resulting characters are

    M_a: [258,-6,0,4-2phi,2+2phi],
    M_b: [171, 3,0,1,1],

where `phi^2=phi+1`. Pairing with the parameter-A character, with class sizes 1,15,20,12,12, gives 14 and8. The excluded p=2 character is that of V tensor V and pairs to zero with A.

These 34 possible coefficient intertwiners need not be independent after applying the differential; homotopies may have their own kernels. No rank, solution, or numerical value is inferred from these counts. The substantive reduction is the complete form (1), the excluded p=2 channel, and the exact coupled equations (2).

## Verification and remaining task

Run `python verify_universal_monad_five_channel_homotopy.py`. It checks all parameter weight equations and their full integer ranges, the excluded Schur channel, the complete characters and multiplicities, and the noncommutative five-coefficient expansion. It never constructs an actual monad matrix, chooses actual parameter values, or evaluates an actual differential.

Inputs are the frozen monad-ratio/root comparison and its twist-two global-Hom reduction, the pinned three-channel theorem, and standard Schur/Bott identities stated explicitly here. The remaining task is to construct the symplectic middle intertwiners and source corrections satisfying (2), in the fixed channel, Hamiltonian, determinant and q0 normalizations. This note does not replace C_mult with the different normal cup constant.
