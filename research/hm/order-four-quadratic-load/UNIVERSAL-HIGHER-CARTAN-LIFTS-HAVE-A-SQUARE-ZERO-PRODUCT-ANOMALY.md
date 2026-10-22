# Higher Cartan lifts and their square-zero multiplication correction

## Checked result and scope

The universal global skew Cartan lift from
`UNIVERSAL-CARTAN-KOSZUL-MULTIPLIER-HOMOTOPY.md`, Section 2, extends from
quadratic symbols to every positive homogeneous degree. It is NOT a module
homomorphism in the coordinate coefficients. In the quartic case needed for
the next ambient division, its exact failure of multiplicativity is a
regular square-zero operator. Any two such corrections have zero product.

This is a new universal operator identity, not a construction of the desired
next-division cochains C_h,V_h. In particular it does not replace the full
positive off-diagonal interface in
`ACTUAL-POSITIVE-ATIYAH-DERIVATIVE-HAS-A-SURJECTIVE-P4-TENSOR.md`.
It supplies a concrete correction that must be retained if a quadratic
Cartan lift is multiplied by a negative quadratic direction or is instead
rebuilt as a quartic lift. Those procedures need not agree.

## 1. Global lift in every positive degree

Keep every actual channel and determinant marking from the frozen full
homotopy. Let E=U ker(i_x:Lambda^2 H -> H), and let P be the Cartan summand
in U tensor Lambda^2 V. For an arbitrary endomorphism R of P, use the same
coefficient operator E_R: it is R on the positive two-form Cartan summand,
minus its apolar adjoint on the mixed Cartan summand, and zero on the spin
complements and on U Lambda^2 W. This definition includes selfadjoint R.

Let S(w) be an End(P)-valued homogeneous polynomial of degree d>0. Define

    T_d(S)(eta)=(1/d) sum_i i_x[e_i wedge E_(partial_i S)(eta)].       (1)

Derivatives in (1) act only on the coefficients of S. They do not act on eta.
Equation (1) is invariant under changes of the W basis: the derivative and
the inserted vector are contracted naturally. It is a global polynomial
map E -> E(d). Its twist is exactly d, with no suppressed determinant factor.
The endomorphism and its adjoint are transported through the ACTUAL conformally
symplectic cubic f; its conformal scalar cancels in adjoints but is not reset.

The coefficient identities F_R(e_i wedge eta)=e_i wedge E_R(eta) and
F_R^dagger=-E_R from the frozen proof do not use the degree of S. They therefore
prove that (1) is skew for the determinant-valued middle pairing in every
positive degree. Contraction squared is zero, so its image is in E.
Furthermore

    T_d(S) B=0,
    [T_d(S) A]_(VV,Cartan)=S Pi(A).                              (2)

The second identity is Euler's formula sum_i w_i partial_i S=d S. The first
retains the full b-channel, not just its compressed part. No actual source
coefficient, matrix, or rank evaluation enters this argument.

## 2. Exact multiplication formula

If f(w) is scalar homogeneous of degree e>0, then direct Leibniz differentiation
in (1) gives

    T_(d+e)(fS)-f T_d(S)
      =1/(d+e) sum_i i_x[e_i wedge
           E_((partial_i f)S-(e/d)f(partial_i S))].                (3)

In particular, for quadratic f and quadratic S, put Delta(f,S)=T_4(fS)-fT_2(S).
Then

    Delta(f,S)=1/4 sum_i i_x[e_i wedge E_(f_i S-f S_i)].           (4)

Both sides of (4) have twist four and are globally skew. Their positive
VV coefficient block is zero, by the two Euler identities. That does NOT
imply their full operators are zero.

There is a convenient invariant binary formula. In a compatible basis write
w=(u,w), omega=e_u wedge e_w, and j=i_w omega=-w e_u+u e_w. Define

    {f,S}_omega=f_u S_w-f_w S_u.

Invariantly this is the coefficient of df wedge dS relative to omega. Thus
an independent rescaling of omega rescales this bracket inversely and j
by the same factor, and their product below is unchanged. Equation (4) is
exactly

    Delta(f,S)(eta)=(1/8) j wedge i_x E_({f,S}_omega)(eta).        (5)

For the sign and factor, Euler gives

    f_u S-f S_u=(w/2){f,S}_omega,
    f_w S-f S_w=-(u/2){f,S}_omega.

The inserted vector in (4) is consequently -(j/2). Since i_x j=0,
contracting -j wedge E_R(eta) gives +j wedge i_x E_R(eta), proving (5).
No physical-q normalization, cubic-channel normalization, or new scalar
choice appears in this calculation.

## 3. A common square-zero correction space

For an arbitrary coefficient endomorphism R(w), define

    V_R(eta)=j wedge i_x E_R(eta).

Its image is in U tensor (j wedge ker i_x), a coherent isotropic image
subsheaf of E. It may have smaller fiber dimension at w=0; no vector-bundle
rank claim is needed. For any U-valued one-form alpha, E_R(j wedge alpha)
is again divisible by j: the mixed block acts separately and identically
on the W factor, and the W^2 block is killed. Hence

    V_R(j wedge alpha)=0,
    V_R V_T=0                                                     (6)

for all R,T, with any coefficient degrees. In particular every Delta(f,S)
is square-zero, and any two multiplication corrections have zero product.
They also kill B. Their images pair to zero since j wedge j=0.

These are literal polynomial identities on the middle bundle, not merely
trace identities or identities after restricting to the quadric. They do not
say that a complete chain cochain with this middle component is closed, nor
that its source components may be omitted. A generic correction is nonzero.
Its zero compressed VV block is therefore a concrete example of information
lost by retaining a Cartan principal action alone.

## 4. Application boundary for the pending division

For the next actual division, f can be the negative quadratic a(w), and S
can be any quadratic Cartan symbol occurring in a proposed correction. Then
(4)-(5) give the exact global difference between a T_2(S) and T_4(aS).
Both are legitimate regular skew middle operators, but substituting one for
the other without Delta changes the cochain. The common nilpotent image in
(6) can simplify products in a full ansatz; it does not license discarding
its linear contribution to either monad arrow.

The open equation remains the explicit residual equation from the preceding
positive-interface note:

    k E_(a,h)+d J_h=-q0 V_h.

This note neither solves that equation nor identifies a fourth Bockstein.
All previously frozen notes and verifiers remain unchanged.

## Reproduction

Run `python verify_higher_cartan_lift_and_product_anomaly.py`.
The verifier retains all 16 entries of an arbitrary Cartan endomorphism,
all five quartic coefficients, all quadratic coefficients in both factors,
and all coefficients of universal differential forms. By linearity this
checks the complete 80-dimensional quartic-symbol tensor, not selected actual
HM data. It verifies (2), the full operator formula (5), and annihilation of
the entire j-wedge image in (6). The skewness proof is the same exact
coefficient-adjoint identity as the frozen full homotopy, with its degree
independence made explicit above.
