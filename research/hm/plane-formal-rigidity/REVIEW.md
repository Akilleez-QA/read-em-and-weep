# Independent structural review

Verdict: PASS, conditional on the explicitly pinned geometric premises. Reviewed PROOF.md SHA256 c6d1cd05249c5971b05876a2d23b674febd25d85e886a00e9903c353e356d350. No mathematical correction is required for these bytes.

## Scope and mathematical checks

1. The ambient projection is a genuine equivariant total-normal-bundle model on the complement of the negative line. Its tautological O(1) is pulled back from the plane. This splits the ambient formal scheme, not the actual vector bundle.
2. For square-zero ordinary-normal layers, determinant-fixed marked differences and isomorphism-lifting obstructions use H1(End0(F_R) tensor I^n/I^(n+1)); the kernel of marked automorphisms uses H0. Equivariant invariants are exact in characteristic zero. Stability kills the negative-twist H0, and scalar H0/H1 also vanish. Thus the compatible uniqueness argument does not leave an unaccounted gauge or determinant ambiguity.
3. The only invariant difference space is the one-dimensional second-normal space. Odd layers vanish by the central character, not by a claim of ordinary cohomology vanishing. Serre duality gives the fourth-layer character A+V, which has no D channel. The Steiner resolution gives H1(B_R(t))=0 for all t>=2 and therefore removes every later difference space.
4. Equality of second-normal classes uniquely lifts the marked isomorphism at every finite stage and hence in the inverse limit. This compares existing lifts; no H2 existence obstruction has been suppressed.
5. If the actual second-normal class vanished, the split homogeneous degree-two section would extend to 7R, contradicting the exact finite-neighborhood premise. The O(4) identification and prescribed degree-two leading term are retained, so this is an actual section contradiction rather than an associated-graded substitution.
6. Dilation acts by c^2 on the second-normal class. Since the actual class is nonzero over C, its dilations realize every nonzero class; the pullback realizes zero. Marked classification over the fixed base remains parametrized by the entire line, whereas quotienting by dilation gives two orbits. Existence is provided by constructions, not H2 vanishing.
7. The added dilation-stabilizer corollary is valid: nonzero kappa forces c^2=1. For unmarked isomorphisms, stability makes the restriction scalar and rescaling makes it marked. Its determinant then also agrees with the fixed determinant: a global formal unit restricting to 1 has no nonconstant terms, since H0(O_R(-n))=0 for n>0. Thus no extra unmarked stabilizers arise.
8. Dilation preserves ordinary ideal powers and rescales the nonzero leading candidate. Therefore the first failing order is constant on the nonzero formal locus, without selecting order four or six.

## Novelty and boundaries

The pinned KNOWN_SECOND_CLASS Section 4 explicitly treats zeta as the proved nonzero actual second-normal class. The candidate correctly labels this nonvanishing as known, with a new independent deduction, and places its new contribution in marked formal classification and the exclusion of independent higher formal choices. No global bundle-isomorphism, algebraization, opposite-pencil row, vertex scalar, or source/frontier selection is inferred.

## Reproduction and dependency audit

Independently ran python verify.py and python -O verify.py; both passed. The checker uses explicit RuntimeError guards rather than optimization-removable assertions. It verifies the complete abstract nine-class character table, the 0/1/0/0 invariant difference dimensions, central parity, and the byte count, SHA256, and Git-blob identity of each of the three local audit inputs against INPUTS.json. Independently checked the final proof SHA256 and inspected the known-class source's Section 4. The immutable-source acquisition was performed by the author; this review authenticates the resulting local bytes against the pinned manifest, not an additional independent network fetch.

The checker does not claim to machine-prove deformation theory, stability, or the infinite tail; those arguments are checked in the mathematical text above. No selected actual coefficient, point, jet value, matrix, derivative, or instance rank was evaluated during this review.
