# Positive double-hyperplane multiplication is an actual Gauss derivative

## Result

Let T=P(W*) and let H_l be the negative hyperplane l=0. Put M_j=H1(B(j)), with inversion signs displayed below. The proved uniform hyperplane vanishings give actual maps

    A_l:M_2,+ -> M_3,-,             injective, dimensions 41 -> 54,
    B_l:M_3,- -> M_4,+,             surjective, dimensions 54 -> 37.

Both maps are multiplication by l. The exact section and quotient bundles are

    E=H0(B_H(4))_+, rank17, degree -54,
    0 -> E -> H0(B_R(4)) O_T -> D_lin(1) -> 0,
    rank D_lin=13, degree D_lin=41.

Let SF:E->D_lin(-1) be the second fundamental form of the displayed ACTUAL subbundle of a constant thirty-space. Then, fiberwise at every l,

    ker(l^2:M_2,+->M_4,+) = ker(SF_l),
    coker(l^2:M_2,+->M_4,+) = coker(SF_l),            (1)

with the natural one-dimensional parameter factors understood. In particular

    rank(l^2)=24+rank(SF_l),
    h0(B_(2H_l)(4))_+=17-rank(SF_l).                (2)

The actual SF is not identically zero. However its maximal rank13 is not proved. Thus the double-hyperplane square route is reduced to a geometric derivative of a KNOWN actual kernel bundle, not to a rank inference from the already-surjective plane boundary.

## Exact local comparison

Use an affine coordinate z on T with l=u+zv. The negative-coordinate Koszul sequence and the vanishings H0(B(4))=H0(B(3))=H2(B(2))=0 identify the plane section space with the middle cohomology

    H0(B_R(4)) =
    ker[(u,v):M_3,-^2 -> M_4,+] /
    im[(v,-u):M_2,+ -> M_3,-^2].                    (3)

Here the map from the kernel to plane sections is injective modulo the indicated image: this follows from the two short exact Koszul sequences and ambient H0(B(4))=0. The H2(B(2)) vanishing supplies surjectivity onto the relevant H1(I_R B(4)); taking its kernel toward M_4 gives precisely H0(B_R(4)).

A local section of E is represented by k(z) in M_3,- with l k=0. Its plane restriction is the class of

    (k,zk)

in (3). Differentiating gives the class (k',zk'+k). It still belongs to the numerator of (3), since l k'=-v k.

The relative plane boundary to D_lin(1) is represented, in this affine frame, by

    [(x,y)] -> [y-zx] modulo l M_2,+.                (4)

Indeed a Koszul gauge (vm,-um) changes y-zx by -lm; and its kernel consists exactly of classes [(k,zk)] with lk=0. Formula (4) is therefore the actual quotient map, with a possible common boundary sign.

Applying it to the derivative yields

    SF(k)=[k] in M_3,- / l M_2,+.                   (5)

The derivative is independent of how k is locally continued: changing the continuation changes its derivative by a section of E, which disappears under the quotient. Globally the cotangent factor is O_T(-2), so the target is D_lin(1) tensor Omega_T=D_lin(-1).

On the other hand the exact linear-algebra comparison for the two actual maps A_l and B_l is

    0 -> ker(B_l A_l) -> ker B_l
      -> coker A_l -> coker(B_l A_l) -> 0,           (6)

because A_l is injective and B_l is surjective. Its middle arrow is precisely k->[k], hence (5) identifies it with SF. This proves (1)-(2), rather than merely matching the dimensions.

## A genuine but limited geometric exclusion

If SF were identically zero, the classifying map T->Gr(17,H0(B_R(4))) would have zero differential. In characteristic zero a nonconstant morphism from a smooth curve has nonzero differential at the generic point. Thus the classifying map would be constant, and E would be the constant rank17 subbundle, of degree zero. This contradicts deg E=-54. Consequently SF is nonzero and the actual generic positive double-hyperplane multiplication has rank at least25.

This modest bound is not an improvement of the rank36 bound along the invariant-cone smoothing pencil: these are different specializations. It is an actual geometric nonvanishing of the alternate square-endpoint gate. It neither selects the cubic coefficient of the q0-centered Bockstein nor proves maximal rank of SF.

## Relevance and remaining input

If SF is generically surjective, then at a general square a=l^2 the actual positive map a is surjective. The pencil q0+t a is then generically surjective, by the nonzero leading coefficient of a maximal minor. This would settle the remaining generic section count, though it would not identify the first nonzero Bockstein order. Conversely, failure of this endpoint criterion does not prove that the q0-centered pencil is rank deficient or that its third obstruction vanishes.

The unresolved geometric input for this route is exactly rank(SF)=13, not uniform hyperplane cohomology or surjectivity of the plane boundary, both of which are already known. No chosen actual coefficients, actual matrix ranks, scans, or local-model experiment are used.

## Dependencies and reproduction

- [Uniform twist-four and twist-five hyperplane cohomology](UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md), especially its actual quotient sequence (4).
- [Uniform lower hyperplane vanishing](UNIFORM-HYPERPLANE-LOWER-VANISHING-AND-JUMP-BOUND.md).
- [Exact hyperplane syzygy bundle](EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md).

Run `python verify_positive_double_hyperplane_gauss.py` for the quotient-gauge, derivative and degree identities. Geometric exactness is proved above using the stated inputs; the verifier does not prove surjectivity of the second fundamental form.
