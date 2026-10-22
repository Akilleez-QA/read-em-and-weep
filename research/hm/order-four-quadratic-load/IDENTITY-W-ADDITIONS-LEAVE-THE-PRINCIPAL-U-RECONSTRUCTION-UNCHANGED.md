# Identity-W additions leave the principal U reconstruction unchanged

## Scope and dependencies

This is a full exterior identity for an arbitrary six-space coefficient, including all four Cartan/spin blocks. It applies to every identity-W generator in the complete marked coefficient theorem. It does **not** preserve an old mixed-U screen or solve the c companion.

Executable dependency: `universal_source_balance_helpers.py`, frozen in PR697 at `715bb7c683988da6cf220f26629b92d3575a0287`. Its unique public Clifford dependency is pinned in `CLEAN-SOURCE-BALANCE-TENSOR-FOUNDATION.md`. The reconstruction consequence uses `GENERAL-CARTAN-EULER-SYMBOLS-HAVE-A-REGULAR-FULL-U-RECONSTRUCTION.md`, PR714 at `6ebdea2d92a2e15d67132f5fba58e56546805412`.

## 1. The supported identity-W operator

Write `j=i_w omega`, and use the fixed exterior coordinates and determinant pairing of PR697. Let K be **any** six-by-six matrix. Define F_I(K) on three-forms to act by K on the VVW coefficient, identically on its W factor, and to vanish on VVV and VWW. Its determinant adjoint acts on a mixed two-form coefficient Y by

    Y -> up adj_6(K) low Y,

with a **plus** sign. It vanishes on the VV and WW sectors. This sign follows either directly from the determinant pairing or from the full twenty-by-twenty free-input identity in the verifier.

For a positive covector r define

    L_I(K,r) = i_x ( F_I(K) e_r - e_r F_I(K)^* ).

Coefficient functions may depend arbitrarily on the negative variables: this is a multiplication operator, so no coefficient derivative is introduced in this formula.

## 2. Complete operator formula, including the c input

Let E_r denote wedge with r from positive one-form coefficients to six-space two-form coefficients, and put

    R = K E_r - E_r up adj_6(K) low.

For an arbitrary two-form F, write Y_i=getY(F,(i,)), i=3,4. Then the entire operator is

    L_I(K,r) F = i_x sum_i putp(R Y_i,(i,)).               (0)

Indeed both supported operators ignore the VV and WW input sectors, and on the mixed input their primitive difference is exactly the displayed VVW three-form. In particular its output WW sector vanishes and

    (L_I F)_VV = R (uY_3+wY_4).

If F is closed under i_x, its positive one-form closure equation is uY_3+wY_4=coeff(i_v F_VV). Hence its principal image, including for the actual c input, is exactly R coeff(i_v F_VV). Formula (0), not only this principal projection, retains both mixed output columns.

All statements are checked on all20 free two-form coefficients and all36 entries of K. The closed-input assertion is checked on i_x applied to an arbitrary three-form. This is an operator identity; it neither declares the c quotient zero nor discards its companion.

## 3. Exact full-U formula

Put Y_L=stack(M0,M1,M2), so the mixed component of B(p) is `-Y_L p wedge j`. Let E_r map a positive one-form coefficient to the six-space coefficient of its wedge with r. Then

    Y = (E_r up adj_6(K) low Y_L - K E_r Y_L) p,
    L_I(K,r) B(p) = i_x( putp(Y) wedge j ).                 (1)

The WW component of B contributes nothing to either supported operator. Also i_w j=0. Consequently (1) has only mixed VW coefficients:

    (L_I B)_VV = 0,       (L_I B)_WW = 0.                  (2)

Both identities hold for every p and all36 independent entries of K; no block is omitted. Moreover L_I(K,r) A(p)=0, since e_r A(p) is VVV and the adjoint kills A(p).

The verifier checks the full adjoint pairing, literal equality (1), both zero sectors (2), and A-input annihilation. No source coefficient is specialized.

## 4. Exact consequence for the coupled reconstruction

In PR714 the principal U reconstruction first reads the VV component of E=(b_m/a_m)T0 B to determine Y, then its Clifford compatibility and the uniquely specified P and K0. Adding any combination of the operators in Section1 leaves that principal VV component unchanged. Hence the principal Y, its compatibility equation, P and K0 are unchanged. In particular, the separate test `T4(K0) B=B P` has the same value.

This statement is valid for the complete identity-W coefficient space, not merely the old smaller ansatz. It gives a justified reuse of **these principal equations only**. The mixed U image in (1) generally changes. Its Cartan preimage, the resulting additional Euler repair, the reverse source block, and the complete low/high c companions must all be recomputed jointly. No previous mixed-U or c filter is inherited by this argument.
