# Structural invertibility of the excess-factor Koszul contraction

Work over the complex numbers. Let Gamma be the level-five Heisenberg group (of order 125), let V and A be its five-dimensional irreducible representations occurring in PR498, and let W be the two-dimensional representation on which Gamma acts trivially. Fix the equivariant isomorphism p:A tensor W -> exterior^2 V. Put T=V*, B=V tensor W*, and define mu(t,a)(w)=i_t p(a,w). A nonzero overall scalar in mu does not affect the conclusions.

The second diagonal Koszul map is

D: exterior^2 T tensor A -> T tensor V tensor W*,
D((s wedge t) tensor a)(w)=t tensor i_s p(a,w) - s tensor i_t p(a,w).

We prove D is invertible without evaluating a selected matrix.

## 1. Exact transpose

Pair End(V)=T tensor V with itself by (X,Z) -> trace(XZ). Pair exterior^2 T with exterior^2 V by natural evaluation. The transpose is

D*: End(V) tensor W -> Hom(A,exterior^2 V),
D*(X tensor w)(a)=rho(X)p(a,w),

where rho(X)(v wedge u)=Xv wedge u + v wedge Xu is the infinitesimal exterior-square action, not the group exterior-square action.

Indeed, for alpha=s wedge t and beta=v wedge u, direct expansion gives

trace(X [t tensor i_s beta - s tensor i_t beta]) = alpha(rho(X) beta).

Bilinearity proves the displayed transpose formula. The trace pairing is nondegenerate and Gamma-invariant, so no choice of inner product or complex conjugation is involved.

## 2. Every Heisenberg character block is invertible

The conjugation representation End(V) contains each of the 25 characters of Gamma/Z once. A representative group element g of each coset yields a nonzero eigenoperator X=V(g) for a conjugation character, and these characters exhaust all 25 because the Heisenberg commutator pairing is nondegenerate and V has nontrivial central character.

For every such X there is a nonzero scalar c with X^5=c I. Over the complex numbers X is diagonalizable, since x^5-c has no multiple roots. If lambda and nu are any two eigenvalues of X, lambda+nu cannot vanish: otherwise c=lambda^5=(-nu)^5=-c, impossible. Therefore all eigenvalues lambda_i+lambda_j (i<j) of rho(X) are nonzero. Thus rho(X) is invertible, including the identity-character case.

Conjugation equivariance of rho implies that rho(X) has the same Gamma/Z character chi as X. Under p, and using that Gamma acts trivially on W,

End(exterior^2 V) = End(A) tensor End(W).

The chi-space in End(A) is one-dimensional, so for a nonzero generator Y_chi of it there is a unique M_chi in End(W) such that

p^{-1} rho(X) p = Y_chi tensor M_chi.

Invertibility of rho(X) forces both factors Y_chi and M_chi to be invertible. The transpose formula now gives

D*(X tensor w)=Y_chi tensor M_chi(w)

under Hom(A,exterior^2 V)=End(A) tensor W. Consequently D* is an isomorphism on every two-dimensional character block. Taking their direct sum proves D*, and hence D, invertible.

## 3. Consequence for C

The module C of PR498 has C_0=A, C_1=B and no other graded components. PR501 identifies beta_(1,2)(C)=beta_(2,2)(C)=dim ker D. Therefore b=0, excluding its alternative b=24.

There are fifteen minimal linear relations and no minimal quadratic relations. Regularity is one because C is supported in degrees zero and one. Once beta_(2,2)=0, all later diagonal Betti numbers vanish: a degree-i generator in F_i could not map nontrivially into F_(i-1), whose least possible degree is then i, and such a zero column contradicts exactness and minimality. The Hilbert numerator of C is

(5+10t)(1-t)^5 = 5-15t+50t^3-75t^4+45t^5-10t^6.

Thus its minimal resolution is pure:

0 -> 10S(-6) -> 45S(-5) -> 75S(-4) -> 50S(-3) -> 15S(-1) -> 5S -> C -> 0.

## Dependencies and scope

- PR498: https://github.com/Akilleez-QA/read-em-and-weep/blob/77018c2e6904a4ef9adfee5f2f48e49894b63fe9/research/hm/determinantal-excess-module/PROOF.md
- PR501: https://github.com/Akilleez-QA/read-em-and-weep/blob/0a71d8568cbad799d2dfda335752dadcf89c1a0c/research/hm/excess-linear-syzygy-bound/PROOF.md

The argument uses only the canonical contraction, the pinned Heisenberg multiplicity-one decomposition, and odd-order spectral algebra. It uses no selected HM/source matrix evaluation, numerical rank, coefficient search, or large computation. It concerns this graded excess module and its minimal resolution, not fixed-pair source values, higher-order lifting, or algebraicity. This is an authored derivation with independent and root mathematical reviews, conditional on the pinned inputs; not a proof-assistant formal check.

- Public group input: Horrocks–Mumford (1973), Section 1, the central extension and nondegenerate commutator pairing: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
