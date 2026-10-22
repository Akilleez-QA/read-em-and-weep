# The actual square Atiyah sequence is complete quintic evaluation

## New conclusion

On the square conic P(W)->P(A), ell |-> ell^2, the actual positive Atiyah multiplication has the exact factorization

    0 -> D5 O(-2) -> T6 O(-1) -> O(4) -> 0,             (1)

where T6 O(-1) is the subbundle V tensor (ell^2)^perp of the trivial nine-space C^{phi+}=V tensor A. The full cokernel is canonically, equivariantly

    coker[D5 O(-2)->C^{phi+} O] = O(4) + V O(2).        (2)

Sequence (1) is the complete-quintic evaluation sequence twisted by-1, up to its fixed nonzero normalization. Thus it supplies another short proof of uniform square-direction injectivity, without using the six-axis classification.

The map here is h->h At_F(D_(ell^2)) before the extra annihilating multiplication by ell^2. Statements (1)-(2) do not evaluate the third Bockstein or assert any property of the separate primary Gauss map.

## Proof

The actual residue comparison identifies the map with (1 tensor ad_(ell^2))j, where j:D5->V tensor A is the nonzero embedding. Invariance of the Killing pairing puts its image in V tensor E, where

    0 -> E -> A O -> O(2) -> 0

is complete-quadratic evaluation on P(W). Therefore E=W O(-1), and V tensor W=T6 gives V tensor E=T6 O(-1).

The actual factor map D5 O(-2)->T6 O(-1) is nonzero. If it were zero for every ell, the linear-in-a map (1 tensor ad_a)j would vanish on the spanning Veronese conic and hence identically, contradicting the residue-surjectivity theorem.

The space of equivariant morphisms between these two bundles has dimension one:

    Hom_G(D5 O(-2),T6 O(-1))
       = Hom_G(D5,T6 tensor W) = C,

since T6 tensor W=D5+P4+V. The standard complete-quintic evaluation sequence

    0 -> Sym^4(W) O(-1) -> Sym^5(W) O -> O(5) -> 0

provides a nonzero morphism in precisely this one-dimensional space after twisting by-1. Its kernel term is D5 O(-2). Hence the actual factor is a nonzero scalar multiple of that subbundle injection, proving (1) at every point.

The quotient by V tensor E in V tensor A O is V O(2). Combining with (1) gives

    0 -> O(4) -> coker -> V O(2) -> 0.

Its extension class vanishes because Ext^1(V O(2),O(4))=V tensor H1(O(2))=0. The group is finite in characteristic zero, so an equivariant splitting exists by averaging. It is unique because

    Hom_G(V O(2),O(4))=(V tensor A)^G=0.

This proves (2), including the asserted canonical equivariant splitting. The chosen identification of the residue nine-space with V tensor A is only determined up to the fixed common normalization; no assertion of an additional absolute scalar is made.

## Verification

Run verify_square_atiyah_quintic_sequence.py. It checks the universal representation multiplicities and line degrees. The actual input is the already proved residue comparison, not an evaluated HM matrix. No selected coefficients, actual rank tests, or parameter scans occur.
