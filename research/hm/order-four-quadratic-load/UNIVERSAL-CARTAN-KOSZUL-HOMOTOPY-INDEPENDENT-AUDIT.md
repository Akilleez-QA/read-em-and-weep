# Independent audit of the Cartan–Koszul homotopy tensors

## Audited result and scope

The polynomial tensors used in UNIVERSAL-CARTAN-KOSZUL-MULTIPLIER-HOMOTOPY.md pass an independent implementation of the three critical checks:

1. The global quadratic Cartan lift is symplectic-skew for an ARBITRARY endomorphism of the Cartan four-space, including the apolar-selfadjoint sector. It is polynomial, maps to K, and annihilates the b-channel.
2. The full reverse-source cubic identity and both components of the complete sextic identity hold universally, with every representation coefficient unassigned.
3. The Cartan projection of the positive contraction has one precise common normalization: in the stated universal Clifford frame it is exactly -(2/3)rho^3(M_v), not an unspecified independently chosen factor in each term.

These checks validate the most delicate tensor identities of the exhibited five-equation homotopy with C_mult=-chi/g_L. The global chain-Hom comparison, actual channel identification and polynomial spin-complement argument are the mathematical proofs in the companion and its cited predecessors; this audit does not replace them by numerical experiments. No fourth-stage value is inferred.

## 1. General endomorphisms, not only symplectic ones

Write P=Sym^3 U for the Cartan summand. In the compatible universal Clifford realization, let Kinc:P->U tensor Lambda^2 V be the Cartan inclusion and extract its fixed projection inverse. For a completely arbitrary 4-by-4 operator R and arbitrary quadratic phi(w), define the VV block by

    RR=phi Kinc R extract.

Let J6 be the natural U-symplectic pairing matrix between VV and VW coefficient sectors. The other block is defined by the exact dual formula

    RV=-J6^(-1) RR^t J6.

This is the minus-adjoint block. It is NOT replaced by RR in the selfadjoint sector. Denote the resulting two-sector coefficient operator by E_S, where S=phi R. The lift is

    T_S=E_S-(1/2) sum_i e_i wedge i_x(partial_i E_S).

Derivatives act on the operator coefficients, not the input section. This is the same as sum_i i_x(e_i wedge E_(partial_i S/2)), by the quadratic Euler identity. The output is in K because i_x squared is zero.

The independent verifier takes every entry of R and every coefficient of phi as free symbols, and tests the determinant-valued pairing on arbitrary K inputs obtained by contracting arbitrary constant three-forms. It verifies ALL exterior coefficients of

    <T_S eta,zeta>+<eta,T_S zeta>=0,
    i_x T_S eta=0,       T_S B=0.

Linearity in S means the products of the three independent quadratic coefficients and sixteen independent R entries span the complete 48-dimensional coefficient space of quadratic End(P)-valued operators. This is a complete representation identity, not a point/rank test or an evaluation of an actual monad.

## 2. The exact common projected operator

Let G be the fixed positive quadratic pairing and I_v the coefficient map induced by contraction i_v:Lambda^2 V->V. With the fixed Cartan inclusions and projections in the two dual coefficient sectors, the precise projected map is

    J_actual=extract (G^(-1) I_v tensor I_U) Kinc.

The independently verified identity is

    J_actual=-(2/3) rho^3(M_v).

The positive Lie action on the Cartan summand is computed directly as the sum of the adjoint action on the V* factor and the fundamental action on U. No actual invariant-cubic coefficient enters this calculation.

Transport by the ACTUAL f gives J_v=f^(-1) J_actual f. The same definition, not independently rescaled copies, enters the base, commutator and anticommutator residuals. Because the transported positive V has no component in the negative A=Sym^2 W, this J_v lies in Sym^6 W. The actual f is conformally symplectic. Its nonzero conformal scalar cancels in transported adjoints, and no actual channel is rescaled to suppress it.

## 3. Full binary identities without coordinate division

The second independent implementation retains an arbitrary binary sextic, cubic, quadratic, Hamiltonian and base covector. It reconstructs the commutator and anticommutator differential operators directly, verifies their source ideal preservation, and verifies the full reverse-source identity

    (3/2)(D l)z+(S partial_u+T partial_w)(3DN-ND)z/24=0.

For the sextic residual it checks the TWO polynomial components

    36w Z_K+2Y_minus,u+Y_plus,u=0,
    -36u Z_K+2Y_minus,w+Y_plus,w=0.

Thus it does not divide by a chosen base coordinate even in the verifier. Together with the tangency identities these are exactly

    36 Z_K+2 Z_minus+Z_plus=0.

Every coefficient is checked. There is no selected sextic, source specialization, actual-instance matrix, differential rank, or scan.

## 4. Why the remaining spin term vanishes

For completeness, the final formal step in the full proof was also checked independently. After the component identities, the last residual is a regular b-type tensor E_C=B t. Full reverse-source equation (2b), skew-adjointness, equation (2d), and universal isotropy give

    A*E_C=-B*M_a C-MR=C_mult q0 B*delta_D C=0.

The last expression is zero because the natural coefficient derivative preserves the Cartan condition. Therefore M(v)t=0. The Clifford square gives chi q0 t=0; over the polynomial coefficient domain t=0. This is an exact proof of the composite cancellation, not an inference from nonzero separate maps. The regular b-type factorization is proved by coprimality of the two negative coordinate variables in the full note.

All operators have polynomial degree two and preserve the determinant-valued pairing. The negative dual source operator consequently gives the second monad arrow, not an omitted independent condition. The complete exhibited homotopy, rather than a claim that the gradient ansatz was without loss, is what determines the multiplier.

## Reproduction

Run `python verify_cartan_koszul_homotopy_independent_audit.py`. It uses only the frozen universal exterior helpers and independently constructs the arbitrary-End(P) lift, common projected action and full binary identities. Run the companion's full verifier separately for its additional coefficient-space adjoints and complete five-equation expansion. Every predecessor remains unchanged.
