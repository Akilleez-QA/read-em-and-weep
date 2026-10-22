# Clean source-balance tensor foundation

This is a definitions-and-identities foundation for the source-balance
calculations, not an operator-family exclusion or a curve-class computation.

The sole repository dependency is the already public
[universal monad Clifford verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/verify_universal_monad_clifford_homotopy.py),
SHA256 `4e71b3c14ad9a85b099a9ee4261e4ebccd61e5aca1760462069bfe939982317b`.
It supplies the free-symbol exterior algebra, physical Clifford equation,
and marked A/B/C columns. The new module imports no unpublished verifier
and performs no curve division or coefficient specialization.

## Six-space and Euler definitions

The module fixes the Cartan inclusion Kinc and spin splitting so that
cliff·spin=I, Pi=I−spin·cliff, and Kinc·extract=Pi. Put

    G=[[0,1/2,0],[1/2,0,0],[0,0,1]],
    J6=G tensor J,  adj6(R)=J6^(-1)R^t J6,
    up=G tensor I, low=up^(-1).

For a six-space coefficient R, fullE is R on positive two-forms and
−up·adj6(R)·low on mixed two-forms, zero on negative two-forms. The
corresponding fullF is R on VVW and −up·adj6(R)·low on VWW, zero on VVV.
These signs give

    pair(fullF(R)u,v)=−pair(u,fullE(R)v),
    fullF(R)(dw_i wedge v)=dw_i wedge fullE(R)v.

For a homogeneous negative coefficient R of degree d, define

    fullT(R,d)(v)=sum_i i_x(dw_i wedge fullE(R_i/d)(v)).

These formulas specify both off-diagonal blocks and the whole Euler
operator, not merely its positive-form component.

## Hamiltonian and Clebsch definitions

FW is R tensor D on VVW and zero on the other three-form sectors. Its
literal determinant adjoint is −up·adj6(R)·low tensor D on VW and zero
on the other two-form sectors, since D is trace-free on a two-dimensional
space. The module retains the entire physical parameter a and the
positive trace-free tensor H.

For a binary quartic p, op4(p) maps a cubic z to (p,z)_2/12. Its complete
coefficient inverse quartic is fixed by all five quartic coefficients,
not by evaluations. The Spin-to-Cartan map mixed5(p) maps a linear form
z to (p,z)_1/4. These are the only binary Clebsch functions needed below;
the complete33 coefficient family is not imported or asserted.

## Reproducibility

Run `python universal_source_balance_helpers.py`. With all36 entries
of R and every exterior input coefficient free, it verifies both
adjoint identities, negative-wedge compatibility, and the full five-
coefficient quartic inversion. The imported public verifier checks its
own Clifford and exterior identities. No actual HM/source value,
instance matrix/rank calculation, curve reduction, or scan is used.
