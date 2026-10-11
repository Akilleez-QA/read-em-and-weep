# Completeness of the bases of H²(U_k) and H²(W_k) for k = 2, 3

The bases below are derived from the fixed bidegrees, the finite and infinity frame weights, the original plane cover, and the triangular transport. They are not read off a stored label list. Arithmetic is exact over Q. The argument is restricted to normal orders k = 2 and k = 3.

## 1. Fixed input

The base is P¹ with coordinate z, weight 2, and the plane is P² with homogeneous coordinates X, Y, W of weights 1, 1, 0. The ordered frame of B is (P, E0, E1, E2), with bidegrees

```
(base, plane) = (3, -3), (0, 0), (4, -4), (3, -4)
```

and finite frame weights d = (3, 0, 2, 2). The infinity frame weights are (3, 6, 0, 2). The scalar bundles are A = O(3, -6), L = O(4, -2) and I = O(0, -1). Thus

```
U_k = A ⊗ B ⊗ L^{-1} ⊗ I^k,    W_k = Sym²(B) ⊗ L^{-1} ⊗ I^k.
```

The scalar factor of U_k is O(-1, -4 - k), and the scalar factor of W_k is O(-4, 2 - k). A symmetric W slot (i, j) therefore has base degree b_i + b_j - 4 and plane degree p_i + p_j + 2 - k. A U channel i has base degree b_i - 1 and plane degree p_i - 4 - k.

The infinity-to-finite transport of B is the triangular matrix

```
TB = diag(z^3, 1, z^4, z^3),    TB[E0, E1] = z C,
C = S² + z S W² + z² W⁴,    S = X² + Y².
```

The induced transports are TU = z^{-1} TB and TW = z^{-4} Sym²(TB). The finite relation is r0 = (-a0, W⁶, -g, XY) with a0 = X³ + Y³ and g = S - z W², and the infinity relation is ri = (-a0, S³, -z^{-1} g, XY). These are tied to the transport by the polynomial identity TB ri = z³ r0, including the off-diagonal entry S³ - C g = z³ W⁶. The generator checks that identity before enumerating bases.

The original plane cover is D(X), D(Y), D(W). A negative Laurent monomial is written

```
[X^u Y^v W^w]* = X^{-u-1} Y^{-v-1} W^{-w-1},    u, v, w ≥ 0.
```

Its plane degree is -(u + v + w + 3) and its weight is 2 e - u - v - 2 when multiplied by z^e.

## 2. Split lines

For an external product O(b, p) on P¹ × P², the Čech complex of the product of the standard covers is the tensor product of the two Čech complexes. Line bundles on P² have vanishing H¹, and the cohomology of P¹ vanishes above degree 1, so

```
H²(O(b, p)) = H⁰(P¹, O(b)) ⊗ H²(P², O(p)),
H³(O(b, p)) = H¹(P¹, O(b)) ⊗ H²(P², O(p)).
```

H⁰(P¹, O(b)) is zero for b < 0 and has basis 1, z, …, z^b for b ≥ 0. H¹(P¹, O(b)) is zero for b ≥ -1. H²(P², O(p)) is zero for p > -3. For p ≤ -3 its Čech basis on the triple overlap, modulo the ordered homotopy below, is the set of negative monomials with u + v + w = -p - 3. The count of those monomials is dim H⁰(P², O(-p - 3)).

The ordered plane homotopy contracts the first nonnegative plane exponent. On every support pattern it satisfies δK + Kδ = 1 - Π, where Π retains a cochain only when every inverted coordinate is negative. The generator checks this identity on every support pattern in degrees 1 and 2. Consequently the all-negative projection loses nothing in H², and it does not change z exponents, so it preserves finite and infinity regularity.

A split line with b ≥ 0 and p ≤ -3 therefore has the monomial basis

```
z^e X^{-u-1} Y^{-v-1} W^{-w-1},    0 ≤ e ≤ b,    u + v + w = -p - 3.
```

Every other bidegree has H² = 0. In particular, at orders 2 and 3 the W lines PE0, E0² and E0E2 have negative base degree or plane degree greater than -3, and the U line AE0 has base degree -1. None of them contributes an independent H² summand. E0² has plane degree 2 - k ≥ -1, so it has no all-negative monomials at all.

## 3. Invariant subbundles

TB is upper triangular in the ordered frame, with the single off-diagonal entry in column E1 and row E0. The following subbundles are invariant, and the indicated quotients are split lines:

| subbundle | quotient | diagonal transition of the quotient |
| --- | --- | --- |
| span{E0} | span{E0, E1}/span{E0} ≅ E1 | z⁴ |
| span{P, E0} | the PE1 direction | z³ on PE1 |
| span{E0, E2} | the E1E2 direction | z³ on E1E2 |
| span{E0², E0E1} | the E1² direction | z⁴ on E1² |

P², PE2 and E2² are already split. Sym²(B), and likewise the scalar twists U_k and W_k, decompose as a direct sum of these invariant pieces. Cohomology is the sum of the cohomologies of the pieces.

## 4. Connecting maps vanish

Each extension 0 → S → E → Q → 0 gives

```
H²(S) → H²(E) → H²(Q) → H³(S).
```

For every subbundle S that appears at k = 2 or k = 3, H³(S) = 0. Indeed H³ of a split line is the product of H¹(P¹) and H²(P²), and each relevant line has either base degree ≥ -1 or plane degree > -3. The same vanishing holds for the rank-two piece span{E0², E0E1}, because both of its graded lines have H³ = 0 and the connecting map of that smaller extension lands in zero. The generator records the five bidegrees and the resulting zero products.

Therefore H² of each extension surjects onto H² of its split quotient. The kernel is H²(S). That kernel is zero except for the E1² extension, where

```
H²(span{E0², E0E1}) ≅ H²(E0E1),
```

since H²(E0²) = 0. The group H²(E0E1) is the split-line group of base degree 0: the monomials z⁰ [X^u Y^v W^w]* of plane degree -2 - k.

## 5. Explicit lifts and the normalization

Transport of a pure infinity monomial z^{e-β} m on a free slot of base degree β reproduces z^e m on that slot and, when the slot involves E1, a lower component. Expanding Sym²(TB) or TB gives the lower component before projection:

| free slot | lower slot | coefficient of z^{-3} C m |
| --- | --- | --- |
| AE1 | AE0 | 1 |
| PE1 | PE0 | 1 |
| E1E2 | E0E2 | 1 |
| E1² | E0E1 | 2 |

The factor 2 is the cross term in (z C E0 + z⁴ E1)². The square also produces an E0² component through C². Its plane degree is 2 - k, so its all-negative projection is empty at these orders. No other slot appears.

C is a sum of plane-degree-4 monomials. A product term is kept only when every plane exponent is negative. On a lower line of base degree β, the finite representative keeps only the surviving terms with z ≥ β + 1. Terms with z ≤ β are not part of this finite representative.

This cutoff is the connecting normalization. Global sections of the lower line are the powers 0 ≤ z ≤ β. For β = -1 that range is empty, so the whole finite-regular part z ≥ 0 stays with the higher class, and there is no independent lower basis vector. For E0E1 one has β = 0, so z ≥ 1 stays with the E1² lift and the z = 0 monomials are left to the E0E1 basis. Two lifts of the same E1² symbol differ by a class in H²(E0E1). Setting the z = 0 coefficients to zero picks exactly one lift.

The free lines and their ranges at order k are the split lines of section 2:

```
U:  AP  (β = 2, plane -7-k),  AE1 (β = 3, plane -8-k),  AE2 (β = 2, plane -8-k)
W:  P², PE1, PE2, E0E1, E1², E1E2, E2²
    with base degrees 2, 3, 2, 0, 4, 3, 2
    and plane degrees -4-k, -5-k, -5-k, -2-k, -6-k, -6-k, -6-k.
```

## 6. Finite and infinity regularity

Let F_all be the all-negative part of the transport of the pure infinity leading monomial. Write L for a lower component of F_all. Put the terms of L with z ≥ β(L) + 1 into the finite representative, and carry the terms with z ≤ β(L) by the diagonal preimage on the lower line. If the lower transition multiplies z-exponents by β, a finite term z^s is the image of z^{s-β}. Every cancelled exponent satisfies s ≤ β, so s - β ≤ 0, and the infinity representative is regular at infinity. Every kept exponent satisfies s ≥ β + 1. For the lower lines that actually occur, β ≥ -1, hence s ≥ 0, and the finite representative is regular at the finite chart.

The leading monomial already has 0 ≤ e ≤ β, so its infinity exponent e - β is ≤ 0. The generator builds this pair for every enumerated monomial and checks the identity

```
(all-negative part of transport(infinity)) = finite representative,
```

together with the sign conditions on z. Because the set of monomials is finite, the check is a proof for k = 2 and k = 3, not a sample.

Worked monomials, both of character -2 at order 2:

- E1², z² X^{-1} Y^{-1} W^{-6}. Every term of C except W⁴ meets a nonnegative X or Y exponent. The surviving term is 2 z W⁴ · z² X^{-1} Y^{-1} W^{-6}, that is coefficient 2 at z¹ X^{-1} Y^{-1} W^{-2} on E0E1. The cutoff z ≥ 1 keeps it.
- AE1, z¹ X^{-1} Y^{-1} W^{-8}. The same cancellation leaves coefficient 1 at z⁰ X^{-1} Y^{-1} W^{-4} on AE0. The cutoff z ≥ 0 keeps it.

## 7. Spanning and independence

Order the filtration so that each step quotients by an invariant subbundle onto one free line. At each step the symbol map H²(E) → H²(Q) is surjective because the connecting map into H³(S) is zero. The kernel is spanned by the basis already chosen on S: that basis is empty, or it is the split basis of E0E1.

The explicit lift of section 5 is a section of the symbol map. Its leading symbol is the chosen monomial with coefficient 1, and the normalization makes its coordinate on every earlier summand zero. The generator checks this on every vector: after the forced terms with z ≥ β + 1 are removed, the coordinate vector is the corresponding unit vector. The coordinate matrix on the enumerated set is therefore the identity. The classes are linearly independent. By induction along the filtration they span H².

The same identity shows that the forced-component formula, with multiplicity 1 or 2, agrees with the expanded transport. A mismatch of multiplicity, cutoff, or slot would move a unit vector off the diagonal.

Dimensions are the sums of (β + 1) times the number of negative monomials of the free lines. They are outputs of the enumeration. For these two orders the enumeration produces

| order | dim H²(U_k) | dim H²(W_k) |
| --- | ---: | ---: |
| 2 | 336 | 390 |
| 3 | 423 | 534 |

and the per-line sum reproduces those totals. No stored dimension is used as an input.

## 8. Characters

The finite character of a monomial is its weight minus the finite frame weight of its slot. Each term of C has weight 4, and z^{-3} has weight -6, so multiplication by z^{-3} C lowers weight by 2. Replacing one E1 factor by E0 lowers the frame weight by 2. The character is unchanged. The generator checks the equality on every forced term.

On each free line the base degree β and the two frame weights are related by 2β = d_finite - d_infinity + 4. The infinity representative, including every diagonal preimage of a cancelled term, therefore has infinity character equal to the finite character minus 4. The generator checks that shift on every infinity monomial it builds.

The character histograms are recorded in the certificate as outputs. The order-k slice is the character k - 4, because a finite W coefficient of slot (i, j) is required to have weight k - 4 + d_i + d_j, and the analogous rule for U uses one frame weight.

## 9. The relation lands in the W basis

Multiplication by r0 sends U channel i to the symmetric W slots (i, j). The plane degree matches because deg(r0) = (3, 6, 2, 2) and the scalar plane degrees of W and U differ by 6. The character matches because the weight of the j-th entry of r0 equals d_j. After the all-negative projection and the removal of forced lower terms, every one of the 336 order-2 source vectors and every one of the 423 order-3 source vectors lands in the enumerated W coordinate space, with integral coefficients. This is again an exhaustive check. It is not a comparison with a stored matrix.

## 10. Boundary

The argument uses the fixed frame, the displayed transport, and the original cover. It does not reconstruct the rank-four plane object, produce the quadratic obstruction, replay orders above 3, or compute a carrier hull. Equality of these bases with any stored label list is a separate comparison and is not an input to the enumeration.

## Reproduce

From `research/hsd-label-audit-61/hsd_label_audit`:

```sh
python3 generate_bases.py --output frozen/basis_certificate.json
python3 -m unittest discover -s tests -v
```

The certificate records `content_sha256`, the SHA-256 of the canonical JSON of the certificate with that field removed. `verify_certificate` recomputes it. Python 3.10 or newer is enough; the arithmetic uses `fractions.Fraction` only.
