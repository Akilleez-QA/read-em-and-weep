# Independent review of excess-factor contraction invertibility

The derivation is correct over the complex numbers, conditional on the pinned PR498 and PR501 identifications. It proves that the degree-two Koszul map of C is invertible and therefore selects b=0. This is independent mathematical review, not formal proof-assistant verification.

## Transpose and normalization

With i_s(v wedge u)=s(v)u-s(u)v and alpha=s wedge t, direct expansion of the trace expression gives

s(v)t(Xu)-s(u)t(Xv)-t(v)s(Xu)+t(u)s(Xv).

This equals alpha(Xv wedge u+v wedge Xu). Hence the stated transpose is exact, with no missing factor two and no conjugation. At X=identity it specializes to the factor two in PR501's trace identity. The trace pairing identifies End(V) with its dual equivariantly: it pairs opposite character spaces, but does not change the conjugation action on the identified domain. Thus the use of the same character chi in the displayed transpose blocks is valid.

The replacement of the original multiplication by contraction is justified by the nonzero multiplicity-one normalization already proved in PR501. The identification W with W* is an isomorphism; changing that identification or multiplying the whole map by a nonzero scalar cannot affect invertibility.

## Finite-group and spectral steps

For the level-five Heisenberg group, the quotient by its center has exponent five. Consequently g^5 is central and its image in the irreducible V is c times the identity with c nonzero. This is sufficient; no stronger group exponent convention is required. Nondegeneracy of the commutator pairing and the nontrivial central character of V ensure that coset representatives give all 25 conjugation characters exactly once in End(V).

The polynomial z^5-c has simple roots over the complex numbers. Thus X=V(g) is diagonalizable. Two eigenvalues cannot sum to zero, since their equal fifth powers would then be negatives of each other. The infinitesimal exterior-square operator rho(X), whose eigenvalues are the pairwise sums, is therefore invertible. This argument concerns rho(X), not the different group operator exterior^2(X).

Under p, the chi-character space of End(exterior^2 V) is End(A)_chi tensor End(W). Since End(A)_chi has dimension one and Gamma acts trivially on W, rho(X) factors uniquely as Y_chi tensor M_chi after choosing a nonzero Y_chi. An invertible tensor-product operator cannot have a singular factor: a nonzero kernel vector of either factor tensored with any nonzero vector would lie in its kernel. Therefore M_chi is invertible. The transpose consequently maps each two-dimensional chi-block isomorphically to the corresponding two-dimensional block. These exhaust both spaces. This proves invertibility without a matrix or rank evaluation.

## Resolution consequence

PR501 identifies b with both the kernel and cokernel dimension of this square Koszul map. Hence b=0. The claimed later diagonal vanishing follows by induction from minimality: a degree-i basis element in F_i with no lower-degree target has zero differential, while a basis element cannot belong to the next image, which lies in the homogeneous maximal ideal times F_i. Exactness rules it out. Since C has regularity one, the remaining Betti numbers are uniquely fixed by its Hilbert numerator. The displayed pure resolution has ranks 5, 15, 50, 75, 45, 10 and shifts 0, 1, 3, 4, 5, 6, respectively.

This establishes a module-theoretic result only. It gives no evaluation of an original fixed pair or selected source instance and no higher-order lifting or algebraicity conclusion. The review used symbolic identities and representation theory only, with no selected HM matrices, numerical rank tests, coefficient search, or large computation.

## Public dependencies

- PR498: https://github.com/Akilleez-QA/read-em-and-weep/blob/77018c2e6904a4ef9adfee5f2f48e49894b63fe9/research/hm/determinantal-excess-module/PROOF.md
- PR501: https://github.com/Akilleez-QA/read-em-and-weep/blob/0a71d8568cbad799d2dfda335752dadcf89c1a0c/research/hm/excess-linear-syzygy-bound/PROOF.md
