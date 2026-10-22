# Four middle-parameter directions are exterior presentation identities

## Result and dependencies

The four formulas below give zero **middle endomorphisms** on every pair of
exterior two-forms. Thus their vanishing precedes application to the monad
arrows A, B, C. No source correction, curve restriction, normal-form
algorithm, or actual coefficient evaluation occurs.

All definitions and physical determinant conventions are those of
`CLEAN-SOURCE-BALANCE-TENSOR-FOUNDATION.md` and
`universal_source_balance_helpers.py`, published at
715bb7c683988da6cf220f26629b92d3575a0287 (PR697). The companion verifier
imports only this public module and its pinned public Clifford dependency.
The numbered labels below are mnemonic names for the explicit formulas
here. Identification with any historical parameter family, and completeness
of such a family, are not conclusions or premises of this theorem.

## 1. Conventions

Write the six-space as the direct sum of binary cubics and binary linears,
with alternating forms J_P=-J_3/2 and J_S=-J_1/3. Use the block embeddings
E_C(X), E_S(Y), E_10(B), and

    E_01(B) = J_S^(-1) B^t J_P

in their indicated blocks, zero elsewhere. Transport these blocks to the
physical six-space by B6=(Kinc Pstd, spin). The matrix Pstd is extracted
from the *complete polynomial* A(r squared,r), with binomial coefficients;
there is no chosen value of r. Consequently B6^t J6 B6=diag(J_P,J_S).

For a negative W-action D and positive one-form R, let L_R(K) be the
middle operator

    i_x ( F_(K,D) e_R - e_R F_(K,D)^adj ).                 (1)

Both coefficient-action terms are retained. The identity-W action is not
substituted for D. Coefficients of K commute with these algebraic wedge
and contraction operations; no differentiation of K is part of (1).
Let R_q and R_H be the physical quadratic gradient and its positive
trace-free deformation used in the public foundation.

Let H=op4(h), where op4(h)(z)=(h,z)_2/12 acts on cubics, and let
B_h(z)=(h,z)_1/4 map linears to cubics. The quartic h is the complete
positive H parameter. For a cubic endomorphism X, write

    pr_V(X)=tr(H_bin X) H_bin/20
             +(tr(F_bin X) E_bin+tr(E_bin X) F_bin)/10.

For Z in this positive sl2, write z(Z) for its action on linears and
b(Z) for the cubic-valued map given by multiplication by

    tr(F_bin Z) S squared/10
      -tr(H_bin Z) ST/10-tr(E_bin Z) T squared/10.

These constants and both determinant pairings are fixed, not absorbed.

## 2. Three universal zero identities

For arbitrary Z in the positive sl2, put

    K19(Z)= -E_C(Z)/2+E_S(z(Z))/2-E_10(b(Z))+E_01(b(Z)).

Then

    L_Rq(K19(Z))=0.                                      (2)

For arbitrary h, put

    K28(h)=-2 E_C(H)+8 E_10(B_h)+8 E_01(B_h).

Then

    L_Rq(K28(h))+L_RH(I_6)=0.                            (3)

A common scalar coefficient, such as the Hamiltonian quadratic a,
may multiply (3) without changing it.

For any second quartic q, let Q=op4(q),

    Z=pr_V(HQ-QH),
    c=(h,q)_4/(4!) squared,      j=(h,q)_2/144.

Set

    K32(h,q)= (3/2)c I_6
       -(15/32)(E_C(Z)+E_S(z(Z)))
       -(3/2)E_C(op4(j))+6 E_10(B_j)+6 E_01(B_j),
    L32(q)= -E_C(Q)/4+E_10(B_q)+E_01(B_q).

Then the exact bilinear identity is

    L_Rq(K32(h,q))+L_RH(L32(q))=0.                       (4)

These are identities on the entire exterior two-form middle term, not
only on the image of the source monad map.

## 3. The fourth direction reduces to (2)

Let X=op6(s) for any sextic s, where op6(s)(z)=(s,z)_3/120.
Set Z=pr_V(HX+XH). The positive-spin-one projection of X B_h satisfies

    pr_spin1(X B_h)=-(5/8)b(Z).                          (5)

Here the projector is (24-Casimir)/16 on Hom(linears,cubics).
Therefore

    K9(h,s)=(5/16)(E_C(Z)-E_S(z(Z)))
              -E_10(pr_spin1(X B_h))+E_01(pr_spin1(X B_h))
            =-(5/8) K19(Z),

and L_Rq(K9)=0 as well. This treats the whole sextic coefficient space,
not a selected transported Lie element.

## 4. Exact verification and consequence

Run `python verify_four_middle_presentation_identities.py`. The verifier
constructs the determinant-adjoint operator (1), keeps a completely free
20-coefficient pair of exterior two-forms, arbitrary negative Hamiltonian
coefficients, all five positive H coefficients, and, in (4), all five
coefficients of q. It expands every exterior coefficient and verifies
(2), (3), (4), and (5) exactly. The sextic in (5) has all seven coefficients
free. Thus linearity verifies the full operators, not selected inputs.
The only division is by the displayed nonzero rational normalization
constants, fixed invertible determinant pairings, and the nonzero physical
quadratic normalization theta in R_q and R_H. Theta is retained symbolically;
it is not assigned a value.

The four displayed coefficient directions are presentation redundancies.
In any family containing these explicit coefficient pairs, they
cannot alter any full U or c error, the forced source companion, or the
scalar deficit of a fixed member. This is stronger than their vanishing
after composition with A, B, C. It does not exclude new middle symbols,
prove any other presentation parameters independent, evaluate the fourth
Bockstein, or complete the original lifting problem.
