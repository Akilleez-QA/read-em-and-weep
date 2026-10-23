# The actual positive gamma is a pairing with a provably nonzero first leg

Retain the rank-33 hypothesis at the invariant positive vertex from POSITIVE-INVARIANT-VERTEX-ONE-SCALAR-GATE.md. Write

K=ker[q0:H1(B(2))_+ -> H1(B(4))_+]=A direct-sum D5,
C=coker[q0:H1(B(2))_+ -> H1(B(4))_+]=P4.

The actual scalar gamma controlling first negative quadratic smoothing is not evaluated in this note. The new result is a two-linear-step factorization through the actual twist-three cohomology, together with a proof that its first T6 leg cannot vanish.

## 1. Actual multiplication and multiplicity spaces

Put Y=H1(B(3))_-. The checked ambient character is

Y=3W-prime direct-sum 3S4 direct-sum 6T6.

Let M_T=Hom_G(T6,Y), a six-dimensional multiplicity space, and similarly M_S=Hom_G(S4,Y). Negative linear multiplication, restricted to D5 subset K, is the actual map

L:W tensor D5 -> Y.

Since W tensor D5=S4 direct-sum T6, L is specified by a vector a_S in M_S and a vector a_T in M_T. These are the actual multiplication coefficients in intrinsic multiplicity spaces, not freely selected parameters. Equivariant decomposition makes this description independent of bases in Y.

Next let

R:W tensor Y -> C

be actual negative linear multiplication to H1(B(4))_+, followed by its actual quotient to C. The identities

W tensor S4=A direct-sum D5,
W tensor T6=D5 direct-sum V direct-sum P4,
W tensor W-prime=P4

show that R vanishes on the S4-isotypical part. Its T6-isotypical component is specified by a covector b_T in M_T*, after fixing a nonzero generator of the one-dimensional Hom_G(W tensor T6,P4). The W-prime component of R is irrelevant to L because L has no W-prime component.

## 2. A new nonvanishing consequence of uniform hyperplane vanishing

For every nonzero negative linear form u, the restriction sequence

0 -> B(2) --u--> B(3) -> B_Hu(3) -> 0

identifies the kernel of u:H1(B(2))_+ -> Y with H0(B_Hu(3))_-, because the equation u is odd and both ambient H0 groups vanish. UNIFORM-HYPERPLANE-LOWER-VANISHING-AND-JUMP-BOUND.md proves this hyperplane section space is zero for every u, including the exceptional directions. Thus multiplication by u is injective on H1(B(2))_+, and in particular on the five-dimensional D5 subset K.

If a_T were zero, the entire L would factor through a single copy of S4, the image of S4 tensor a_S. For each fixed u, its restriction D5 -> Y would then have rank at most four, contradicting injectivity on D5. Therefore

a_T != 0.

This uses the actual uniform hyperplane vanishing, not a generic tensor or multiplicity expectation. No claim that a_S is nonzero is needed.

## 3. Exact criterion for gamma

The composite R composed with (identity_W tensor L) is actual multiplication by two negative linear forms, followed by quotient modulo q0. Multiplication commutes, so its alternating part is zero and its symmetric part is precisely the first negative quadratic Bockstein on D5.

Only the T6 component can contribute, and its multiplicity contraction is b_T(a_T). The universal composite through T6 is nonzero: under T6=Sym^5 W and D5=Sym^4 W it is successive Cartan multiplication

W tensor W tensor Sym^4 W -> Sym^6 W -> P4.

Its symmetric part is the unique nonzero coupling Sym^2 W tensor D5 -> P4 used in the previous gate. Therefore, up to a nonzero convention-dependent normalization,

gamma = b_T(a_T).

In particular gamma vanishes if and only if the actual second multiplication covector annihilates the actual nonzero first-leg vector. Equivalently, let T_a subset Y be the actual copy of T6 defined by a_T. Then gamma=0 exactly when multiplication of W tensor T_a into H1(B(4))_+ has zero image in the actual P4 quotient C. This is a concrete cohomological subspace-inclusion criterion with both maps retained.

Changing irreducible model identifications rescales the displayed factors by nonzero constants and cannot change the vanishing criterion. Changing a basis in M_T changes the vector and covector contragrediently, preserving their pairing.

## 4. Precise remaining gap

The nonzero a_T does not force b_T(a_T) nonzero. The covector may vanish, or may annihilate that particular line. Neither dimension counts nor the proven generic odd maximal rank removes this possibility by itself: that would require an additional identity relating the odd block to these actual positive multiplication maps. None is assumed here.

Thus the next actual geometric target, within the rank-33 hypothesis, is to show that W tensor T_a is not carried entirely into q0 H1(B(2))_+. This is stronger and more precise than merely asserting that an allowed Schur coefficient ought to be nonzero. The first leg has now been proved nonzero using uniform geometry, while the second-leg pairing remains open.

Reproduction: python verify_positive_gamma_linear_factorization.py. The script checks the exact twist-three character and all tensor multiplicities. The first-leg nonvanishing is the injectivity/dimension proof above, not an evaluation of an actual coefficient or matrix.
