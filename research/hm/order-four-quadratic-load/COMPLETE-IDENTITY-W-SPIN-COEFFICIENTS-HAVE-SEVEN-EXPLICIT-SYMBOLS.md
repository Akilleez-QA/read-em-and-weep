# Seven explicit identity-W Spin-to-Spin coefficient symbols

## Scope

This constructs a basis of the **coefficient** spaces with Spin input and
Spin output for identity-on-W middle symbols: six Rq coefficients and one
Rh coefficient. It gives concrete additional formulas for the coupled
source construction. It does not assert independence after exterior
presentation, a complete middle family, a source solution, or any fourth
Bockstein value.

The only executable dependency is the public PR697 foundation
(715bb7c683988da6cf220f26629b92d3575a0287). Let U denote the positive spinor
representation, V=Sym²U, and let A=Sym²W be the distinct negative
three-dimensional representation. The fixed actual cubic marking
f:Sym³W→Sym³U is a G-equivariant isomorphism, symplectic up to a nonzero
scalar. All physical scales are retained in the subsequent exterior
operator; the following formulas only specify its coefficient matrices.

## 1. Universal coefficient maps

Write C=Sym³U and let i_C:C→V⊗U and pi_C:V⊗U→C be the public Cartan
inclusion and projection. For H0 in the positive rank-two Cartan summand,
let H6 be its unique extension acting on the V factor, normalized by
pi_C H6 i_C=H0. Define

    Phi_H(R)=tr_V(H6 i_C R pi_C),    R in End(C).            (1)

This is a map to End(U). It is SL(U)-equivariant. On the rank-one and
rank-three summands of End(C), it takes values in sl(U); on the rank-two
summand, it takes scalar values. Each of these three bilinear maps is
nonzero. The helper checks the positive-frame normalization and the
nonzero full-polynomial maps; the verifier checks equivariance under all
three sl2 generators with every coefficient of R and H0 free.

Use the unnormalized transvectant (p,q)_j and set

    L2(p)z=(p,z)_1/2,
    L4(p)z=(p,z)_2/12,
    L6(p)z=(p,z)_3/120,

acting on binary cubics. On linear forms L2 has its analogous 2×2
matrix, denoted L2_spin. Let Cplus be the Casimir on End(C), with
values j(j+1) on rank j. Explicitly it is

    ad(H)^2/4+(ad(E)ad(F)+ad(F)ad(E))/2.                   (2)

## 2. The seven formulas

For the full negative Lie element D and base vector (u,w), put

    d=k S²−2h ST−l T²,          n=(−w S+u T)².

Every following coefficient has degree two in D and degree two in
(u,w). Form the transported Cartan endomorphisms

    R1=f L2(d(d,n)_2) f^-1,
    R2=f L2(n(d,d)_2) f^-1,
    R4=f L4((d²,n)_1) f^-1,
    R6=f L6(d²n) f^-1.

The negative sextic summand is V+P4. In positive Cartan coordinates its
V part lies in rank one, and its P4 part lies in rank three. Therefore

    RV=(12R6−Cplus(R6))/10,       RP=R6−RV.                (3)

Here equivariance of the actual marking matters: the negative A and
positive V are distinct. This is not an arbitrary identification of two
three-dimensional spaces.

Let qH=L4^-1(H0) and q4=L4^-1(R4), with the complete quartic inverse of
the public foundation. The six Rq Spin matrices are

    Phi_H(R1), Phi_H(R2), Phi_H(R4),
    L2_spin((qH,q4)_3), Phi_H(RV), Phi_H(RP).              (4)

The sole Rh Spin matrix is the rank-one transfer of RV to U. In standard
cubic monomial coordinates it is

    [[RV00/3, RV01], [RV10/3, −RV00/3]].                 (5)

Place these 2×2 matrices in the SS block of C⊕U, with every other block
zero. They are intended for identity-on-W coefficient action, not for a
second insertion of D on W.

## 3. Completeness at the coefficient level

The negative coefficient representation is

    N=Sym²A⊗A=2A+V+P4+D5.

Since End(U)=1+V,

    dim Hom_G(D5⊗N,End(U))=6,
    dim Hom_G(N,End(U))=1.                               (6)

These equalities are verified by exact A5 character arithmetic. The
six directions in (4) realize respectively the two A contributions,
the scalar and vector D5 contributions, and the V and P4 contributions.
The formulas are independent; (5) is nonzero. Thus they fill (6).

For an all-scale symbolic independence check, choose arbitrary
C5 eigenbases. Take the negative W eigenweights ±2 and positive U
weights ±1. Equivariance forces the cubic marking shape

    [[0,0,FC,0], [FA,0,0,0], [0,0,0,FD], [0,FB,0,0]],
    FA=−9 FB FC/FD,          FB FC FD nonzero.            (7)

This is the complete uniform eigenframe shape, not a numerical choice
of an actual source coefficient or point. The relation is exactly
f^t J3 f=3 FB FC J3. All three scale symbols stay free. Coefficient
elimination for a putative relation among (4) uses only the Laurent-unit
pivots

    −16 FD/FC, 16 FD/FC, 32 FD/FC,
    1728 FB/FD, 54 FB/(5 FD), −12 FD/FC.

Consequently independence holds for every nonzero frame scale, not
merely generically in an unexamined denominator. The scalar pivot test
is on universal polynomial coefficient identities; no actual-instance
matrix or rank is formed or evaluated.

## 4. Use and remaining equations

`build_identity_w_spin_symbols(f,H0)` returns the six Rq and one Rh
6×6 coefficient matrices in balanced Cartan-four plus Spin-two frames.
The full coupled construction must still apply the exterior operator,
quotient any presentation identities, reconstruct general K0, and
retain the entire c companion. A coefficient direction can become a
presentation identity or overlap an already present middle symbol.
Neither possibility is ruled out here. In particular these seven
formulas cannot simply be counted as seven independent new middle
operators or seven free actual deformation parameters.

Run

    python universal_complete_identity_w_spin_symbols.py
    python verify_complete_identity_w_spin_symbols.py

The tests include full SL2 covariance, all-scale coefficient
independence, exact bidegrees, SS support, and the character counts (6).
They do not solve the remaining source balance.
