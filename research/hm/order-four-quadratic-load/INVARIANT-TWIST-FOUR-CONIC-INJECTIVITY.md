# Invariant twist-four conic detection excludes the distinguished product family

## 1. New result

For the actual normalized HM bundle F, restriction to the invariant conic C0 is injective on invariant sections:

    H0(P4,F(4))^G -> H0(C0,F_C0(4))^G.

Thus no nonzero invariant twist-four section vanishes on C0. In particular the prescribed diagonal-scalar lift cannot equal t6 sigma4. This excludes that entire product family, not non-product lifts.

## 2. Conic vanishing forces vanishing on the fixed plane

On R the exact conic sequence is

    0 -> F_R(2) --q0--> F_R(4) -> F_C0(4) -> 0.

Its section restriction kernel is q0 H0(F_R(2))=q0 D5, with no invariants. Here q0 is invariant and multiplication is injective. Therefore an invariant ambient sigma4 vanishing on C0 vanishes on R.

## 3. Normal parity and the actual next-order vanishing

The first ordinary normal quotient is

    (I_R/I_R^2) tensor F_R(4) = W tensor F_R(3).

It is center-odd because W is odd and F_R(3) is center-even. An invariant sigma4 vanishing on R has zero first normal image, so lies in H0(I_R^2 F(4)). The actual section-bundle dictionary gives

    H0(I_R^n F(n+2)) = H0(T,W O_T(n-3)).

At n=2 this is H0(T,W O_T(-1))=0. Thus sigma4=0, proving invariant conic injectivity. No ambient restriction rank has been assumed.

## 4. Optional dimension bound, not existence

The actual Steiner sequence gives

    0 -> A O_R(1) -> D5 O_R(2) -> F_R(4) -> 0.

There is no intervening H1 of A O_R(1). Since A and V are distinct irreducible three-spaces, (A tensor V*)^G=0. Since Sym^2 V*=1+D5, the invariant section space of D5 O_R(2) has dimension one. Thus h0(F_R(4))^G=1, and the preceding injection also gives

    dim H0(P4,F(4))^G <= 1.

Existence of a nonzero invariant ambient section is not asserted. Any such section necessarily restricts nontrivially to C0.

## 5. The distinguished product family is entirely excluded

The actual t6 is nonzero and invariant. Symmetric multiplication by it defines an injective sheaf map

    F(4) -> Sym^2 F(10)=B(9).

Over the function field this is multiplication by a nonzero vector, hence injective; torsion-freeness of the source proves sheaf injectivity. If t6 sigma4 is invariant, then t6(g sigma4-sigma4)=0 for every g, so sigma4 itself is invariant.

The necessary conic test in DIAGONAL-SCALAR-LIFT-NONPRODUCT-OBSTRUCTION.md shows that the prescribed fourth-normal tensor requires sigma4|C0=0. Indeed the leading pure quartics of t6 span D5 and generate F_R(2), so at every conic point some leading value is nonzero; symmetric multiplication by it is injective.

Sections 2-3 force sigma4=0. But the prescribed q0 low-D5 tensor is nonzero. Therefore no member of t6 H0(F(4)) realizes the prescribed invariant diagonal-scalar lift.

## Inputs and limits

The actual Y=W O_T(-3), ordinary ideal-power dictionary, t6 and its pure-quartic leading term are recorded in DISTINGUISHED-GLOBAL-SECTION-AND-DOUBLE-SCROLL.md. The actual D5 generators, center-even F_R and Steiner presentation are established in FIXED-PLANE-CONIC-BALANCE-AND-FOURTH-JETS.md and ACTUAL-CHORD-INCIDENCE-AND-CONIC-EVALUATION.md. The necessary conic test is Section 4 of DIAGONAL-SCALAR-LIFT-NONPRODUCT-OBSTRUCTION.md.

This is a new exact-sequence and parity deduction. No selected coefficients, matrix/rank evaluation, or experiment is used. The non-product invariant Koszul classes remain unresolved, as does the diagonal scalar.
