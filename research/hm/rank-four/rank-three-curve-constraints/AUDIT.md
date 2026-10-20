# Independent audit of the rank-three curve constraints

## Verdict

**The stated conditional theorem is valid. No gap was found in the audited argument.** Assuming the stated Schrödinger/normalizer action, equivariance and rank identity for the linear matrix b, and dim Z₅ ≤ 1, the reduced one-dimensional part of Z₃ is empty or consists of exactly 25 distinct lines forming one N-orbit and one free A-orbit. This is a necessary configuration, not an existence assertion or a proof of finiteness of Z₃.

The audit checked PROOF.md against these local dependencies:

- ../normalizer-small-curve-exclusion/PROOF.md, including its group-action and Castelnuovo arguments;
- ../normalizer-small-curve-exclusion/ADDENDUM_DEGREE_30.md, Sections A–E;
- ../rank-one-middle-curve-exclusion/PROOF.md, especially Sections 1–4 and 7.

The decic-closure result dim Z₅ ≤ 1 and the actual construction/equivariance of the source map are premises here, not independently re-established by this audit. No source map or numerical instance was evaluated.

## Checks

1. **Determinantal multiplicity and degree bound.** The 10-minors are degree-ten forms with base support Z₅. The dimension hypothesis permits three members forming a homogeneous regular sequence; Cohen–Macaulayness rules out embedded associated primes during avoidance. Every curve component of Z₃ is a component of their pure complete intersection W of degree 1000. At its generic point the ambient regular local ring has dimension three, rank b ≤ 7, and block elimination gives I₁₀(b) ⊂ m³. The resulting parameter ideal q satisfies qⁿ ⊂ m³ⁿ. Comparing length(R/qⁿ) = length(R/q) binom(n+2,3) with length(R/m³ⁿ) = binom(3n+2,3) yields length(R/q) ≥ 27. The fundamental-cycle degree formula therefore gives deg Γ₃ ≤ 37. No transversality, smoothness of the original curve, or invariance of W is needed.

2. **Divisibility for a reduced union.** An A-invariant reduced curve has an H₅-linearized restriction of O(1), even if its components are permuted or meet. On H⁰(O_D(n)), the central character is nontrivial for 5 ∤ n. The clock/shift relation then forces equal dimensions in each of five cyclically permuted eigenspaces, so the whole section space has dimension divisible by five. Serre vanishing and the Hilbert polynomial dn + χ(O_D), evaluated at large consecutive n congruent to 1 and 2 modulo five, give 5 | d. This reasoning applies to the union itself, with no additivity assumption for global sections over components.

3. **Faithful SL₂(F₅)-actions in genus at most eight.** The imported genus-at-most-six proof is sound, including its only possible genus-five branch configuration: an involution of A₅ fixes two nonbranch points, and its lifts to the even degree-12 hyperelliptic equation both have order two, whereas its lifts in SL₂(F₅) have order four. For genera seven and eight, the central quotient has genus at most four. Quotient genera one, two, and three are correctly excluded; the genus-three Riemann–Hurwitz congruence in the addendum checks out. Quotient genus zero would require a branch set of size 16 or 18, impossible from A₅ orbit sizes 12, 20, 30, 60. Quotient genus four leaves two branch points in genus eight, also impossible. In genus seven the central involution is free; cyclic point stabilizers must then have odd order three or five. The quotient formula reduces to 20a + 24c = 63 when the final quotient is rational, and is plainly impossible for positive quotient genus. Thus this last unramified case is covered, without incorrectly excluding A₅-actions in genus four.

4. **N-stable integral components.** A-stability makes a component nondegenerate. A projective transformation fixing an integral nondegenerate curve pointwise is scalar, so the normalization action is faithful. Castelnuovo gives g ≤ 176 in degree at most 35, and the A-quotient has genus at most eight. The induced N/A-action is faithful by the invariant-function-field deck-group argument. This supplies the claimed contradiction.

5. **All component orbits.** The A-orbit sizes 1, 5, 25 exhaust the possibilities. An orbit of size 25 forces a full N-orbit of exactly 25 lines under the degree bound; its invariant remainder has degree at most 12 and is excluded by the small-cycle theorem. A size-five orbit gives at least 30 components via the six axes. Higher-degree components already exceed the bound, while lines give at least 60 components: the axis normalizer acts transitively on ten unordered eigenline pairs, and lines belonging to different axes cannot coincide. If all components are A-stable, each has degree a positive multiple of five, so there are at most seven. Orbit sizes divide 120; perfection excludes sizes two, three, and four, leaving one, five, or six. Singletons have degree at most 35 and are excluded by item 4. Orbits of size five or six have quintic components. Their faithful A-action forces elliptic normalization; A acts by translations, and conjugation through elliptic automorphisms bounds |N_C/A| by six, forcing orbit size at least 20. This excludes the final cases.

## Dependency and scope observations

- Importing the separate degree-30 theorem in Section 2 is redundant: the complete orbit analysis in Section 5 excludes degree 30 directly.
- The proof controls the entire reduced curve part, not just one irreducible component. Degree 35 is genuinely excluded.
- The argument leaves isolated points and scheme-theoretic multiplicities of Z₃ unclassified. The additional rank-at-most-two finiteness statement, if invoked under its own premises, justifies generic residual rank exactly three on any hypothetical lines.
