# Independent review: one planar factor exclusion

## Verdict

The abstract theorem in Sections 1–4 of `PROOF.md` is correct over the complex numbers. The proof excludes an integral ordered-factor surface whose first projection dominates a plane and whose second image is nonplanar, when its products span a subspace of dimension at most five. No compatibility or square-avoidance hypothesis is needed.

This review checks the mathematical argument independently. It does not verify the prior exclusions invoked in Section 5 or the repository and discussion facts in Section 6.

## Checks of the delicate steps

### Quotient surjectivity

Replacing the original subspace by the span of the actual products ensures that K′ is contained in UE. Nonplanarity of the second image implies that its w-coordinate does not vanish identically. On this nonempty open subset of the integral surface, the first projection remains dense in P(U). The quotient images of the products are the vectors b_w a, whose projective classes are therefore dense in P(U). They span U, giving dim K0 = dim K′ − 3 ≤ 2.

### Excluding generic rank at most two

For every general a, a vector kernel of dimension at least two intersects the three-dimensional U nontrivially inside the four-dimensional E. A nonzero n in this intersection gives the nonzero product an in K0.

The multiplication map P(U) × P(U) → P(Sym²U) is finite onto its image: its fibers have at most two ordered factor pairs, by unique factorization, and the map is projective. Consequently its inverse image of P(K0) has dimension at most one. This inverse image cannot dominate P(U). The argument also covers dim K0 equal to zero or one.

Existence of the original surface gives generic rank at most three, so the generic rank is exactly three. The unique generic kernel line then identifies the surface with the closure of the corresponding rational graph.

### Choice of the square submatrix

The annihilator basis yields rows independent over C. Select three rows independent over C(x,y,z), then any remaining row. The resulting four rows remain independent over C, while the 4 × 4 matrix has rank three over the function field. Its generic right kernel agrees with that of the full matrix.

### Primitive adjugate factorization and degrees

The factorization adj(N) = h c rᵗ is valid in C[x,y,z], without assuming that any minor is nonvanishing everywhere. A nonzero adjugate column divided by its homogeneous gcd gives a primitive homogeneous vector c. Each remaining column is a rational multiple of c. For every irreducible polynomial, some coordinate of c has zero valuation; hence a rational scalar taking c into polynomial coordinates has nonnegative valuation everywhere and is polynomial. Factoring the gcd from the polynomial scalar vector gives h and primitive r.

All nonzero coordinates in each vector have a common degree, and deg h + deg c + deg r = 3. A homogeneous polynomial vector of degree at most one in three variables cannot have nonplanar projective image in P³. Thus deg c ≥ 2. Constant r would give a forbidden constant row dependence, so deg r ≥ 1. The asserted degrees 2, 1, and 0 follow.

### The cases for the linear left syzygy

For coefficient span one, the left syzygy immediately gives a constant row dependence; primitivity also rules it out.

For coefficient span two, coprimality of the two independent linear forms forces the corresponding rows to be scalar multiples of one fixed, nonzero constant row t. The right-kernel equation then gives t c = 0. This places the entire rational second image in a fixed projective hyperplane, contradicting nonplanarity.

For coefficient span three, the normalization to r = (x,y,z,0) is legitimate. In fact, no change of source coordinates is necessary: write r = C a with C a rank-three 4 × 3 constant matrix, and choose an invertible constant row operation T with T⁻ᵗ C equal to the matrix consisting of the 3 × 3 identity followed by a zero row. Constant row operations preserve symmetric blocks. The simultaneous source/target U basis change described in the proof is also valid.

After normalization, the identity Σ a_i A_i a = 0 and symmetry of each A_i imply

    ∂/∂a_j (Σ a_i aᵗ A_i a) = aᵗ A_j a.

The cubic on the left is identically zero, so all three A_i vanish in characteristic zero. The remaining linear forms have a skew-symmetric 3 × 3 coefficient matrix. Its rank is at most two, producing a nonzero constant dependence among the first three rows of N. This contradicts their constant independence.

## Suggested clarification

The proof can be slightly simplified by using only constant row operations to normalize the rank-three left syzygy, as above. This eliminates any need to explain coordinated source and target basis changes. It is a presentational improvement, not a correction to the proof.

## Scope

The theorem settles the one-planar/one-nonplanar ordered-factor surface configuration. It does not settle the configuration with both factor images nonplanar, nor does it independently establish the other cases mentioned in the broader classification discussion.
