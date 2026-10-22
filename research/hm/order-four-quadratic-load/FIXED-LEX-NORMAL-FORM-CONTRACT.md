# A regression contract for polynomial quotient certificates

## Purpose

A parameter-linear quotient certificate requires a linear normal-form map. A remainder routine that merely returns some remainder is insufficient. This note provides a small independent regression, not a geometric exclusion or an actual-instance computation.

## Counterexample

Over Q[x,y], fix lexicographic order x>y and F=x(y+1). Set a=xy^2 and b=xy. Then a+b=yF lies in (F). SymPy's recursive `div(...,x,y)` returns a and b respectively as the separate remainders, but zero for their sum. Thus extracting parameter coefficients after that operation can falsely declare a combination nonzero modulo F.

The genuine lexicographic normal forms are NF(a)=x, NF(b)=-x and NF(a+b)=0. The singleton {F} is a Groebner basis. Reduction by its leading monomial xy leaves a unique linear combination of monomials not divisible by xy, so NF is Q-linear.

## Required contract

A reusable exclusion checker must fix its coefficient domain, variables and monomial order. It must establish reconstruction p=qF+r and that no term of r is divisible by LM(F). These establish the unique normal form in this principal-ideal example. Linearity then makes coefficientwise equations legitimate.

If F is independent of auxiliary parameters h,c, extension of this same normal-form map coefficientwise to Q[h,c][x,y] commutes with extracting h,c coefficients. This is not a license to extract coefficients of parameters appearing in the divisor, nor to invert parameters without tracking exceptional loci.

The accompanying test reproduces the failure, checks 25 reconstructions and standard-monomial remainders, 625 additive and 625 rational-linear identities, and three parameter-extraction identities. These finite tests are regressions; the preceding uniqueness argument is the reason the contract holds generally. No finite test suite certifies all later geometric calculations.

## Reproduction

Run `python verify_fixed_lex_normal_form_contract.py` with SymPy. Verified with SymPy 1.14.0 on 2026-10-22. The explicit assertion reproducing the old behavior may fail in a future SymPy version if that behavior changes; the normal-form contract remains the intended invariant.
