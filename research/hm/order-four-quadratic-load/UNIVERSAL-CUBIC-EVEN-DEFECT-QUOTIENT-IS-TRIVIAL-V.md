# The universal cubic even-defect quotient is the trivial V-bundle

## Result and application boundary

Let G=SL2(F5), let W be the negative binary representation, W' the other binary representation, and put

    A=Sym^2 W, V=Sym^2 W',
    S4=Sym^3 W=Sym^3 W',
    D5=Sym^4 W=Sym^4 W'.

Here equality between the two realizations of S4 or D5 means equivariant isomorphism, unique up to a nonzero scalar. On L=P(W), use the standard convention H0(O_L(1))=W, after its determinant pairing identification. Let

    0 != f in [Sym^3 W' tensor Sym^3 W]^G.

This invariant space is one-dimensional. Multiplication of the positive binary cubic f by positive linear forms defines a vector-bundle exact sequence

    0 -> W' O_L(-5) --multiply by f--> D5 O_L(-2)
      -> G2 -> 0.                                  (1)

The universal conclusion is

    G2 = V tensor O_L                              (2)

equivariantly. In particular G2 is NOT A tensor O_L. The distinction is forced by W' tensor Sym^3 W = V plus D5.

Both irreducible S4 and T6 channels of the cohomology map obtained by twisting (1) by -1 are isomorphisms. No value of either channel scalar is selected or evaluated.

This theorem is unconditional universal representation geometry. Its use for an actual even-defect grade requires the separately established identification of that grade with the cokernel (1), and the nonzero cubic relation f. A generic local cubic relation alone would not justify replacing an actual global graded sheaf by (1). This note proves the bundle statement once that global sequence is present; it does not silently supply that identification or settle the positive rank33 gate.

## 1. The cubic relation is everywhere nonzero

The invariant f defines an equivariant map

    F_f:(Sym^3 W')* -> H0(O_L(3))=Sym^3 W.

Both sides are the same irreducible four-space S4, so F_f is an isomorphism. Thus, in any basis of Sym^3 W', the four coefficient functions of f form a basis of the complete cubic linear series on L. They have no common zero. For every point ell of L, the specialization f_ell is therefore a nonzero binary cubic in the W' variables.

Multiplication by a nonzero polynomial in the binary polynomial ring is injective. Hence

    W' -> Sym^4 W', l |-> l f_ell

is injective at every ell. Consequently the map in (1) is a subbundle injection, not merely a generic injection, and G2 is a rank-three vector bundle. Its degree is

    5*(-2) - 2*(-5) = 0.                           (3)

This argument is independent of any actual HM coefficient or any chosen fiber matrix.

## 2. The associated first cubic relation has quotient A

For comparison, the full binary-cubic evaluation sequence on L is

    0 -> A O_L(-1) -> S4 O_L -> O_L(3) -> 0.

Its kernel is the standard binary syzygy bundle. One explicit description is multiplication by the tautological kernel of W O_L -> O_L(1): its degree-three syzygies form Sym^2 W tensor O_L(-1). Dualize the evaluation sequence and twist by O_L(1). The result is

    0 -> O_L(-2) --f--> Sym^3 W' O_L(1)
      -> A O_L(2) -> 0.                            (4)

The f arrow agrees up to scalar with the unique invariant cubic. Thus the first relation has quotient A O(2), while the even-product quotient (1) has constant representation V. These are different constructions, so there is no contradiction between the two representations.

## 3. Exact H0 and H1 of the even-product quotient

Taking cohomology in (1) gives

    0 -> H0(G2) -> W' tensor H1(O_L(-5))
      --c_f--> D5 tensor H1(O_L(-2))
      -> H1(G2) -> 0.                              (5)

We prove c_f is onto structurally. Serre duality identifies its dual with

    (Sym^4 W')* -> (W')* tensor H0(O_L(3)).

This is the composition of the dual of ordinary binary multiplication

    Sym^4(W')* -> (W')* tensor Sym^3(W')*

and the isomorphism id tensor F_f. The multiplication

    W' tensor Sym^3 W' -> Sym^4 W'

is onto, so its dual is injective. Therefore c_f is onto. No equivariant scalar is left undecided in this argument.

The exact character identity is

    W' tensor Sym^3 W = V direct-sum D5.

The target in (5) is D5. It follows that

    H0(G2)=V, H1(G2)=0.                            (6)

The three-dimensional summand is V, not A. Both are irreducible genuine three-spaces, but they are not isomorphic.

## 4. A dimension gap proves both remaining channels are nonzero

Twist (1) by O_L(-1). Its cohomology injects H0(G2(-1)) into

    W' tensor H1(O_L(-6))
      = W' tensor Sym^4 W
      = S4 direct-sum T6.                          (7)

Any nonzero G-subrepresentation of this ten-space has dimension at least four. On the other hand, multiplication by any nonzero linear section of O_L(1) gives an injective sheaf map G2(-1)->G2, and hence an injective linear map

    H0(G2(-1)) -> H0(G2).

This last map need not be equivariant; it is used only to bound dimensions. By (6), its target has dimension three. Thus H0(G2(-1)) cannot be nonzero. We have proved

    H0(G2(-1))=0.

Rank three and degree zero give chi(G2(-1))=0, so H1(G2(-1))=0 as well. The cohomology map for (1) twisted by -1 is therefore an isomorphism

    W' tensor Sym^4 W -> D5 tensor W.

Both sides are S4 plus T6, with each constituent occurring once. Each of its two irreducible channel scalars is consequently nonzero. This is a dimension-and-representation proof, not a numerical or selected-matrix calculation.

For any point p of L, the sequence

    0 -> G2(-p) -> G2 -> G2|p -> 0

and the just-proved acyclicity show that evaluation H0(G2)->G2|p is an isomorphism. Hence global evaluation gives the equivariant isomorphism

    V O_L -> G2,

proving (2) without needing to assume a splitting type.

## 5. A unique global quadratic quotient map

The quotient arrow in (1), after identifying G2 with V O_L, is a nonzero equivariant map

    D5 O_L(-2) -> V O_L.

Its equivariant Hom space has dimension one, because

    V tensor Sym^2 W = V tensor A = P4 direct-sum D5.

Thus (1) also determines a unique everywhere-surjective quadratic quotient map, up to a nonzero scalar and the equivariant identification of G2. Its kernel is exactly W' O_L(-5). This recovers the whole universal exact sequence rather than only its Euler characteristic or generic fiber dimensions.

## Evidence and limits

The representation names and exact character arithmetic use verify_pure_cross_block_couplings.py and the normalized binary-icosahedral convention used throughout the cone notes. INVARIANT-CONE-UNIQUE-VERTEX-MODULE.md identifies the unique actual three-step vertex module, but its existence alone is not substituted for the global grade identification required in the opening paragraph.

The companion verify_universal_cubic_even_quotient.py checks the invariant dimensions, all character decompositions, the degree and Euler arithmetic, the low-dimensional representation gap, and universal surjectivity of ordinary binary multiplication. It does not read or evaluate any actual HM coefficient, actual map, or selected rank.
