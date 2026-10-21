# Independent review: the projection-center sextic

## Verdict and reviewed artifact

**PASS.** The structural proof in `PROOF.md`, SHA-256

`5a7e1aedaedcc4e2a34616a66369d319fb4799708e83f0d3d0d1fdd0c8a65df9`,

has been independently checked over C. This is a mathematical review, not formal proof-assistant verification and not an actual HM/source-instance evaluation.

## Dependency audit

The review checked the representation statements in PR563, pinned at `56c3c4c37bd51fc710eec4b80662c5506f357f8f`, and the projection construction in PR567, pinned at `e0f15a5c6a49d2101dae450dae4d26171a259331`.

In PR563 the splitting is A_ambient*=B+C with B=U' irreducible of dimension three and C faithful of dimension two; the actual line is P(C*). The ambient forms through this line are precisely B, so the projection target is P(B*), not a reducible target representation. PR567 gives an actual globally defined equivariant morphism on the integral surface S. Its pullback to L has degree (H-L).L=1-(-5)=6. Smoothness is needed only near L; no assumption of global normality of S enters this argument.

## Independent checks

1. **Nondegeneracy.** The degree-six pullback prevents a constant map. The projective span of its integral image is invariant. Irreducibility of B* excludes a point or line as span. Hence the image degree is at least two.

2. **Source orbit bound.** A finite subgroup of PGL2 fixing a point is cyclic: in an affine coordinate a finite orbit average supplies a second fixed point, after which the group is a subgroup of C*. The possible cyclic subgroup orders of A5 are 1,2,3,5. Every source orbit therefore has size at least twelve. This also bounds every nonzero effective invariant divisor, including divisors with multiplicity.

3. **Covering-degree exclusion.** Normalizing the image yields a smooth genus-zero curve by Riemann–Hurwitz. The degree identity em=6 leaves covering degrees e=1,2,3. The action lifts uniquely to normalization, and the factor map is equivariant even without assuming faithfulness on that normalization. If e=2 or 3, its invariant ramification divisor has positive degree 2 or 4, contradicting the source orbit bound. Thus the map is birational onto a sextic.

4. **Small target orbits.** Irreducibility excludes orbit size one; simplicity and the orders of S2,S3,S4 exclude sizes two through four. For an orbit of size five its stabilizer is A4. Every nonidentity element of its normal Klein four subgroup has trace -1 in B*: faithfulness excludes the identity matrix, and determinant one forces eigenvalues (1,-1,-1). Averaging gives zero Klein-four invariant vectors. Every one-dimensional A4 character is trivial on that Klein four subgroup, so A4 cannot fix a projective point. This establishes the claimed size-five exclusion without requiring a character-table lookup.

5. **Entire singularity budget.** The normalization sequence gives total delta ten, since the sextic has arithmetic genus ten and normalization genus zero. Singularities form invariant orbits, each contributing its orbit size times a positive integral delta. The only orbit sizes at most ten are six and ten; two singular orbits already exceed the budget. Six does not divide ten. Therefore there is exactly one orbit of ten singularities, each with delta one.

6. **Nodes rather than unibranch singularities.** Branch number is constant on the singular orbit. The unibranch alternative would give ten invariant normalization points, impossible. The plane-curve branch formula then forces exactly two smooth branches with intersection multiplicity one at each singularity. Thus all ten points are ordinary nodes. No assumption of generic projection or separate cusp classification is used.

7. **Normalization fibers and differential.** The twenty branch preimages form one orbit because every source orbit has at least twelve points. Each node has two preimages and elsewhere normalization is an isomorphism. The differential is injective on the two smooth branches at every node and at every other point. The final wording correctly distinguishes this unramified map from a scheme-theoretic immersion or a globally injective map.

## Scope and correction resolved

The initial draft's phrase “immersion everywhere” was replaced by the precise injective-differential statement. No mathematical obstruction remains in the reviewed text.

The result concerns the center-line image in the projection of the actual primary surface. It neither identifies this sextic with the different fixed-beta space sextic nor proves global normality of S, determines its degree, or resolves Q4/algebraicity. The proof uses no selected source coefficient, matrix, numerical rank, or large computation.

Dependency links: https://github.com/Akilleez-QA/read-em-and-weep/pull/563 ; https://github.com/Akilleez-QA/read-em-and-weep/pull/567 .
