# Independent mathematical review: paired-character collision filtration

## Verdict and exact edition

**PASS within the stated geometric and coefficient hypotheses. No blocking
finding.**

This review binds `PROOF.md` with SHA-256
`41fd8967a1bd876c0375ab35c889d3eec431e5a72cd66ca2fa74937e503cbca1`,
read in full and independently checked on 20 October 2026. A changed proof
requires renewed review; this verdict is not a certificate for unspecified
later editions.

The reviewed result is the exact filtration of the whole ordinary
`sgn|H` coefficient, its full ideal-coefficient H² vanishing for k≥7,
and the stated conditional source consequences. It is not an actual-source
evaluation, proof-assistant verification, or an assessment of uninspected
claims elsewhere in the repository.

## Checks that support the verdict

1. **Correct character and two-divisor alternant.** The section
   d=σ₂−σ₃ has divisor Δ₁₂+Δ₃₄, not the six-divisor Vandermonde.
   The characters on (12), (34), and (13)(24) are respectively −1, −1,
   and +1. The ordinary permutation linearization is trivial on the fixed
   diagonal coefficient fibers. Smoothness of Z therefore permits regular
   division by both distinct prime divisors. Dividing removes exactly one
   A-degree and leaves an H-invariant section.

2. **The colon equality is global ordinary-ideal algebra.** Since x,y form
   the stated regular sequence, gr_I is O_D[X,Y]. The symbol of d is
   Y−X, a nonzerodivisor over any coefficient ring. The finite leading-term
   argument proves (Iᵏ:d)=Iᵏ⁻¹ without symbolic powers, generic diagonal
   smoothness, normality of D, or completion. It includes quadruple roots.

3. **The cubic algebra is the correct invariant coefficient.** The
   quotient tower in PR387 identifies Z/K with P²×P² and the remaining
   block swap with (13)(24). Consequently the block-even cubic algebra
   from PR139 is exactly (q_*O_Z)^H. PR139 supplies an everywhere basis
   1,σ,τ with τ=σ²−u/6; its proof does not invert the trace pairing.
   The normalizations u=2Σσᵢ² and v=2Σσᵢ³ give the displayed cubic
   T³−UT/4−V/6.

4. **Strictness is proved, not inferred from generic ranks.** Replacing τ
   by σ² preserves the filtration because uK_(n−2)⊂K_n. With the imported
   weighted associated graded, gr_F is the displayed cubic algebra over
   O_N. Setting S=(X+Y)/3 and D=Y−X gives
   U=3S²+D² and V=6S³−(3/2)US. Eliminating V and replacing U by U−3T²
   reduces the comparison to T↦S and U−3T²↦D². Distinct monomials
   SᵃD²ᵇ are independent over any coefficient ring. Together with the
   whole-fiber injection O_N→q_*O_D, this proves the graded injection
   globally, including the nonnormal image and quadruple-root locus.
   The finite first-nonzero-grade argument then proves equality of the
   actual filtered subsheaves.

5. **Twists and inclusion maps are retained.** Multiplication by d,
   followed by tensoring with B₀(−2), produces the three terms
   B₀(−3)K_(k−1), B₀(−4)K_(k−2), and B₀(−5)K_(k−3).
   The same basis identifies their maps to unrestricted coefficients with
   the ordinary ideal inclusions. The k=0 and k=1 conventions are
   consistent. Exact finite pushforward and characteristic-zero
   character projection justify the quotient statement.

6. **The cohomology argument uses sufficient outer groups with the right
   shifts.** For B₀(−a)K_n, their Serre-dual twists are a+dᵢ−5 for H²
   and a+eᵢ−5 for H¹. The adjacent syzygy degree is
   eᵢ=dᵢ+3(bᵢ₊₁−bᵢ)≥n+3. In every summand a+n=k+2, so k≥7 gives
   H² twists at least 4 and H¹ twists at least 7. The cited PR167
   bounds therefore annihilate the entire coefficient H², not merely
   its image in unrestricted cohomology.

7. **The source consequences preserve their boundaries.** The finite
   quotient restriction is injective, not asserted surjective. A quotient
   primitive can be lifted on the stated quotient-adapted affine cover,
   and the remaining ideal-valued cocycle has an ideal-valued primitive.
   This is existence, not a construction of a preferred primitive.
   PR434's complete-source comparison and PR435's normalization remain
   conditional inputs. Their nonzero scalar factors do not create
   ideal membership. The proof correctly treats order-seven
   representability of the same class as equivalent to its vanishing,
   not as an independently established property of the actual source.

## Public dependency verification

The following public files were read at their specified commits, and their
Git blob identifiers matched the manuscript:

- PR158 at `aab61d34a84c9b8b5a908606a7beb7212d45fe7c`:
  weight geometry `507b5281144debc5395f88ac605e5a89c4867b87`;
  fourth-power proof `9ac68fc3222ec751864310a74bebffd95bbd2cb4`;
  all-powers proof `cea0e8cf665c2800bc141759e97921ec71277032`.
- PR139 at `c5fb4a0bcc3c8e35093fcfcff9a73a79a45a18e5`:
  cubic reconstruction `daf01b27c34233f81aa2f2a2eae0f4f90827ef89`.
- PR387 at `e276e0e181e62a60c3ae24759b8bfed746f2492b`:
  normalized coefficient transport `35c0afd278af0d6a106e3514239080d4a3576953`.
- PR167 at `063da90fc4543304e87e701cdefcc08225412f17`:
  sharp regularity `58785a8799c43fd2c7da089d0ddc5e05822132a9`.

The relevant source-scope statements were also read in PR434 at
`9a37da0a0ef67d8790b20e8edbf8d930de658251`, blob
`f037bf94acd583c42c073a56c8e89c6f0e1cecc7`, and PR435 at
`da5a08b7fba20a3c8f87050a5a1bd237276b93d0`, blob
`632e375869b0a425c9dda27bbb1a593635293145`. This does not independently
re-prove all source premises underlying those publications.

The comparison with PR167's finite-neighborhood proof (blob
`d18426bf9fc42b2495cf5d6d566be3ad28bb096f`) and PR383's full-target criterion
(blob `40df1e4752fab008aba0373449c5066a2c04a898`) supports the stated limited
distinction: the current proof computes the whole character filtration
and kills its entire ideal-coefficient group. It does not claim a new
numerical order-seven threshold. No exhaustive originality search is
certified.

## Remaining mathematical questions

This review does not decide the degree-six multiplication quotient,
minimal sufficient order, actual source ideal membership, an actual
obstruction value, a literal primitive, higher continuation, or
algebraicity. No actual HM matrix, source, generator, or checker was
executed, and no external state was changed.
