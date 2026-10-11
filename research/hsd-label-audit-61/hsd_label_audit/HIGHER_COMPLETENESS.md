# Completeness for orders k = 4, 5, 6

The bases and connecting maps below are computed from the same fixed frame, the same original cover, and the same triangular transport as the k = 2, 3 audit. They are not read off a stored label list. Arithmetic is exact over Q. Weight-only disappearance still begins at k ≥ 7. The required character is k − 4, so the three orders here ask for characters 0, 1 and 2.

## 1. What changes at these orders

The extensions are the ones already named for k = 2, 3:

| subobject S | quotient Q |
| --- | --- |
| AE0 | AE1 |
| PE0 | PE1 |
| E0E2 | E1E2 |
| E0² | E0E1 |
| span{E0², E0E1} | E1² |

Each has the long exact sequence

```
H¹(Q) → H²(S) → H²(E) → H²(Q) → H³(S).
```

The first map can only identify or kill classes that already come from S. It does not create new H² classes. The obstruction to lifting a class of Q is the connecting map δ: H²(Q) → H³(S). Exactness gives

```
dim H²(E) = dim coker(H¹(Q) → H²(S)) + dim ker δ.
```

H¹ of every quotient above is zero at k = 4, 5, 6. Each quotient is a line of negative plane degree, and H¹(O(b, p)) = H¹(P¹, O(b)) ⊗ H⁰(P², O(p)) vanishes for p < 0. The first map is therefore the zero map out of the zero group, of rank 0. Its cokernel is H²(S).

H³(S) vanishes for AE0, PE0, E0E2 and E0E1, because each has base degree −1 or 0 and H¹(P¹, O(b)) = 0 for b ≥ −1. The single exception is

```
E0² = O(-4, 2-k).
```

H³(O(−4, 2−k)) = H¹(P¹, O(−4)) ⊗ H²(P², O(2−k)). The base factor has dimension 3, with Čech basis z⁻¹, z⁻², z⁻³. The plane factor is zero for k = 4 (plane degree −2) and has dimensions 1 and 3 for k = 5 and k = 6. The resulting dimensions are 0, 3 and 9.

## 2. The inner connecting map

On 0 → E0² → span{E0², E0E1} → E0E1 → 0 the off-diagonal is z⁻³ C, with C = S² + z S W² + z² W⁴. A class z⁰ m in H²(E0E1) transports to z⁻³ C m on E0². The class in H³ is the part of that product on the gap z ∈ {−1, −2, −3}, projected to all-negative plane monomials.

The matrix of this map, in the ordered Čech bases, has shape and rank

| order | shape H³ × H²(E0E1) | rank | dim ker | dim coker |
| --- | --- | ---: | ---: | ---: |
| 4 | 0 × 10 | 0 | 10 | 0 |
| 5 | 3 × 15 | 3 | 12 | 0 |
| 6 | 9 × 21 | 9 | 12 | 0 |

H²(E0²) = 0, so dim coker(H¹(Q) → H²(S)) = 0 and dim H²(span) equals dim ker. The map is surjective at k = 5 and k = 6, so H³(span) = 0.

It is not the zero map. Its nonzero blocks, graded by the finite character, are

| order | character | source | target | rank |
| --- | ---: | ---: | ---: | ---: |
| 5 | −8 | 5 | 1 | 1 |
| 5 | −6 | 3 | 1 | 1 |
| 5 | −4 | 1 | 1 | 1 |
| 6 | −9 | 6 | 2 | 2 |
| 6 | −8 | 5 | 1 | 1 |
| 6 | −7 | 4 | 2 | 2 |
| 6 | −6 | 3 | 1 | 1 |
| 6 | −5 | 2 | 2 | 2 |
| 6 | −4 | 1 | 1 | 1 |

Every nonzero entry preserves character. Characters −7 and −5 at order 5 have source classes and a zero target, so they survive. No block meets character 0, 1 or 2.

These ranks, including surjectivity at k = 5 and k = 6, are computations on the matrices of those two orders. Surjectivity of δ_inner is not extrapolated beyond k = 6.

## 3. Weights of the H³(E0²) monomials

The finite weight is χ = 2s + x + y. The coordinate W has weight 0, and the finite frame weight of E0² is 0, so the character equals the weight. The basis monomials are zˢ X⁻ᵘ⁻¹ Y⁻ᵛ⁻¹ W⁻ʷ⁻¹ with s ∈ {−1, −2, −3} and u + v + w = k − 5.

At k = 5 the only plane monomial is X⁻¹ Y⁻¹ W⁻¹. Its three weights are −4, −6, −8.

At k = 6 the three plane monomials give

| actual exponents | weights |
| --- | --- |
| (−1, −1, −2) | −4, −6, −8 |
| (−1, −2, −1) | −5, −7, −9 |
| (−2, −1, −1) | −5, −7, −9 |

Two plane monomials contribute −9, −7, −5 and the third contributes −8, −6, −4. Every one of these twelve weights is at most −4. None equals a required character 0, 1 or 2. The same enumeration shows H³(E0²) = 0 at k = 4, where the plane degree is −2 and no all-negative monomial exists.

## 4. The outer connecting map

On 0 → span{E0², E0E1} → F → E1² → 0 the target of δ is H³(span) ≅ coker(δ_inner). That cokernel is zero at all three orders, so δ is the zero map and every E1² class lifts. The dimension identity gives

```
dim H²(F) = dim H²(span) + dim H²(E1²).
```

A direct cocycle check agrees. Transport of an E1² monomial produces an E0² component through C² and an E0E1 component through 2z C. The E0E1 component is a coboundary on the line of base degree 0. After that cochain homotopy, the remaining gap in H³(E0²) lies in the image of δ_inner: 0 of the 180 classes at k = 4, 33 of the 225 classes at k = 5, and 99 of the 275 classes at k = 6 have a nonzero gap, and none of those gaps falls outside the image. In the required characters the gap is the zero vector in the whole of H³(E0²), not merely in an empty character slice. Those classes are z³ X⁻¹ Y⁻¹ W⁻⁸ and the three z⁴ monomials of character 0 at order 4, the two z⁴ monomials of character 1 at order 5, and z⁴ X⁻¹ Y⁻¹ W⁻¹⁰ of character 2 at order 6. The order-4 class is the frozen E1² representative of character 0 with actual exponents (−1, −1, −8) and dual indices (0, 0, 7). The W exponent is that actual exponent.

The three extensions with base degree −1 have δ = 0 for the stronger reason that H³(S) = 0 in every character. Their required-character quotient spaces are the AE1 classes, and at order 4 the E1E2 class. Each has an explicit finite/infinity representative, so the lift is a cocycle and not only a dimension count.

## 5. Required-character bases

A free line O(β, p) with β ≥ 0 and p ≤ −3 contributes the monomials zᵉ X⁻ᵘ⁻¹ Y⁻ᵛ⁻¹ W⁻ʷ⁻¹, 0 ≤ e ≤ β, u + v + w = −p − 3. Its character 2e − u − v − 2 − d is at most 2β − 2 − d. The attained maxima on the generated monomials are 2 on AE1 and on E1², 0 on AE2 and on E1E2, and at most −1 on every other free line. E0E1 reaches at most −4, so the classes killed by δ_inner are outside characters 0, 1 and 2.

The required slices are therefore the split-line monomials of character k − 4. The lines that actually appear are the E1-type lines, not E0²:

| order | character | source | target |
| --- | ---: | --- | --- |
| 4 | 0 | AE1 (4), AE2 (1) | E1² (4), E1E2 (1) |
| 5 | 1 | AE1 (2) | E1² (2) |
| 6 | 2 | AE1 (1) | E1² (1) |

Every other filtration line contributes the empty set. The finite representative of each listed monomial is the triangular transport, keeping lower terms with z ≥ max(β_lower + 1, 0). At order 6 the E1² representative contains the all-negative E0² term z² X⁻¹ Y⁻¹ W⁻², through C². That term is part of the lift. It is not an H² class. Coordinate reduction subtracts the full transport, including this term. The coordinate matrix on the required set is the identity. That identity reduces each required-character representative to a unit coordinate. Those characters lie outside the inner kernel. It is separate from the raw-coordinate identity of the full target, and it is not a kernel-coordinate presentation.

Full corrected dimensions, after removing the kernel complement of δ_inner and keeping every E1² class, are

| order | dim H²(U) | dim H²(W) before δ_inner | rank δ_inner | dim H²(W) |
| --- | ---: | ---: | ---: | ---: |
| 4 | 520 | 701 | 0 | 701 |
| 5 | 627 | 891 | 3 | 888 |
| 6 | 744 | 1104 | 9 | 1095 |

U is unchanged: H³(AE0) = 0 and H²(AE0) = 0.

Multiplication by the finite relation, followed by the all-negative projection and this reduction, lands in the required W basis. In that ordered basis the matrices and their determinants over Q are

```
k = 4:  [[1, -1, 0, -1, 0],
         [0,  1, 0,  0, 0],
         [0,  0, 1,  0, 0],
         [0,  0, 0,  1, 0],
         [0,  0, 1,  0, 1]]    det 1

k = 5:  I_2    det 1
k = 6:  [1]    det 1
```

No required-character connecting map is nonzero, and the dimension identity holds on every extension in the required character and in total. The inner map is nonzero in characters ≤ −4. That changes the full group at orders 5 and 6 and does not change characters 0, 1 or 2.

## 6. Raw coordinates and kernel coordinates

The ordered identity on the full target, at orders 5 and 6, compares the split basis before δ_inner with the shipped raw labels. The lists have lengths 891 and 1104, and the change of basis is the identity. This is an identity of raw coordinates.

The corrected group removes a complement of ker(δ_inner). Elimination on δ_inner chooses pivot coordinates and free coordinates inside the E0E1 summand. A kernel basis vector has coefficient 1 on one free coordinate and restores each dependent pivot coordinate from the elimination row. The frozen kernel basis at order 5 contains the vector with value 1 on z⁰ X⁻³ Y⁻¹ W⁻³ and value −1 on z⁰ X⁻¹ Y⁻³ W⁻³, both of character −6, and the vector with value 1 on z⁰ X⁻³ Y⁻³ W⁻¹ and value −2 on z⁰ X⁻¹ Y⁻⁵ W⁻¹, both of character −8.

The shipped rows are the ordered complement of those pivot positions in the full raw list: 888 rows at order 5 and 1095 rows at order 6. A surviving row labels one free coordinate. It does not carry the restored pivot entries, so it is not a pure raw cohomology class. Entrywise agreement of the rebuilt maps with the shipped maps is agreement of these coordinate presentations.

At order 4, δ_inner has rank 0. There are no pivot coordinates, and the raw list is already the corrected list.

## 7. The cutoff k ≥ 7

On a free line the character is 2e − u − v − 2 − d, with 0 ≤ e ≤ β and u, v ≥ 0, so

```
χ ≤ 2β − 2 − d.
```

The base degree β and the finite frame weight d belong to the line. They do not depend on k. The plane degree does depend on k, and it changes which monomials occur, but the inequality uses only e ≤ β and u, v ≥ 0. The bound is uniform in k.

The quantity 2β − 2 − d equals 2 on AE1 (β = 3, d = 2) and on E1² (β = 4, d = 4), equals 0 on AE2 and on E1E2, and is at most −1 on every other free line that has H². A line with β < 0, or with plane degree greater than −3, contributes no H² class. Every free-line character therefore satisfies χ ≤ 2 at every order.

Each step of the filtration is an equivariant extension 0 → S → E → Q → 0. Equivariance makes the long exact sequence exact in each character:

```
H¹(Q)_χ → H²(S)_χ → H²(E)_χ → H²(Q)_χ → H³(S)_χ.
```

If χ is absent from H²(S) and from H²(Q), then H²(E)_χ injects into the zero group H²(Q)_χ. An extension cannot acquire a character absent from both adjacent H² pieces. By induction along the filtration, every character of H²(U_k) and of H²(W_k) already occurs on some free line. Characters χ > 2 are absent for every k.

The required character of order k is χ = k − 4. For every k ≥ 7 that character is at least 3, so the required slice is empty. Orders 4, 5 and 6 ask for characters 0, 1 and 2. The bound does not remove those slices; they are the computation of the preceding sections.

The certificate also records, for k = 7, …, 12, that the required character exceeds the maximum attained by the monomials generated at k = 4, 5, 6. That record is a finite check against a computed maximum. It is not the argument above.

The vanishing for k ≥ 7 does not use surjectivity of δ_inner. Surjectivity is known at k = 5 and k = 6, where the cokernel in H³(E0²) is zero, and it is not extrapolated beyond k = 6. For k ≥ 7 the required character is already absent from both adjacent pieces, whether or not δ_inner stays surjective at those larger orders.

## Reproduce

From `research/hsd-label-audit-61/hsd_label_audit`:

```sh
python3 generate_higher.py --output frozen/higher_certificate.json
python3 compare_higher.py --json-output comparison_higher_receipt.json --markdown-output comparison_higher_receipt.md
python3 -m unittest discover -s tests -v
```

`compare_higher.py` reads the shipped blocks only after the certificate exists. It is not part of the enumeration.

The certificate records `content_sha256`, the SHA-256 of the canonical JSON of the certificate with that field removed. Python 3.10 or newer is enough; the arithmetic uses `fractions.Fraction` only.
