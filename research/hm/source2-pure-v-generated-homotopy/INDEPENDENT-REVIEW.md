# Independent review: generated pure-V homotopy submodule

## Verdict and reviewed artifacts

**PASS**, conditional on the stated actual-source and compatible nonzero pure-V hypotheses. The proof establishes the exact first two generated spaces, the first-arrow cokernel, necessary endpoint alternatives, and the stated conditional consequence of the smallest endpoint. It does not select that endpoint or compute an actual source channel.

Reviewed SHA256:

- `PROOF.md`: `f788da29035b564f6f544629f724b90ceae5d975273eb15f0df9ac71fd4c643b`
- `verify.py`: `42f40624ee890c5cbc7fbf21086abd02b385dc7f2d55b9e790aefafaad4aff4f`

## Authentication

Each of the five proof files was freshly retrieved from its exact repository path at the immutable commit recorded in `INPUTS.json`. Retrieved bytes equal the retained input bytes; both SHA256 and Git blob hashes match the manifest. Matching Git blobs are:

| Input | Commit | Git blob |
|---|---|---|
| PR1048 | `9eaed2dfadf9c4877327d21db5974b6c94d3863d` | `0710577541a79a5d8d56e5aa693a8fc01c559112` |
| PR963 | `410fc6d7dac16afc4af29590fa5d4e8b8a5dc0a4` | `ac10e7a977f3c564bf16bc9841040be3edb97211` |
| PR1025 | `09f1377f83b027ca27eea0b3a9f40a1b92c6c466` | `d036adcf5bc2bfc53e07cd752ff180c5993251f7` |
| PR790 | `af0e03d26da5e47d18ae732291aca46f4d448dc5` | `0641ffadf54324d5520aec89767658e938815223` |
| PR792 | `2f01f18960ce56b8b2a0c1260c277de3c5f916bf` | `76bee93507d1a2d0840926d4e4e27edadfebb7d7` |

This authenticates these five retained proofs, not a new recursive reproof of their historical dependencies. PR950 and PR960 appear only in the novelty/scope audit and supply no new mathematical premise here.

## Mathematical audit

### Actual multiplication kernel and its quotient

PR790 identifies the original first arrows with multiplication on the actual bundle's sections. Its residual dual sequence has extension group
`Ext¹(A O(6),O(18)) = H¹(A* O(12)) = 0`.
Finite-group averaging permits an equivariant bundle splitting. This computes cohomology without declaring any residual splitting horizontal or imposing a splitting on the second arrows.

The degree-one evaluation sequence, using the fixed symplectic identification of the two-space with its dual, gives the actual kernel `H⁰(B(−3))`. All summands have degree at least −1, so the required H¹ vanishes. The dimensions independently check as 41, 54, and 28 for the two section spaces and kernel. The character is `W+2S+3T`.

The image subsystem's multiplication `W⊗D→T` is onto with kernel S. In the commuting exact diagram, this surjectivity eliminates the next snake-lemma term. Thus the quotient multiplication kernel is exactly `(ker m)/S`, not merely an abstract character difference; its character `W+S+3T` contains no W′.

### Canonical generated middle and twists

The P summand is the canonical isotypical summand of `im h`; it embeds into the actual quotient by I. The restricted multiplication domain is the multiplicity-free representation `W′+T`. Any nonzero kernel must therefore contain T, since the full quotient kernel has no W′. Its image would have dimension at most two. PR963's injectivity off its proper divisor forces the image to contain a four-dimensional first-arrow image of this same embedded P. This contradiction proves injectivity without choosing any direction or arbitrary P embedding.

Consequently the original P-generated middle image is disjoint from I3, and the actual restricted first-arrow system is the direct sum of complete `Sym⁴W→Sym⁵W` multiplication and the free P system. Their cokernels are respectively `O(5)` and `P O(1)`. Both are bundle cokernels everywhere, including both coordinate boundaries. Total rank five and degree nine match `9 O(−1)→14 O`. The cokernel is not confused with the shifted reconstruction bundle B.

### Endpoint and formal consequence

Commutativity of the original negative linear multiplications gives closure under the fixed two variables. The sandwich identity puts F4 in ker h; multiplication of the actual D image generates exactly I4. Hence `Q(F2)=I4⊂F4`, and quotienting the endpoint by I4 leaves the exact surjection from `Sym²W⊗P_h=V+P+D`. Semisimplicity and multiplicity one justify precisely the eight necessary endpoint dimensions. They do not assert realizability or force a nonzero channel. The graph description retains the possible P-valued relation into I4.

If F4 equals I4, the inverse of `Q:P_h→I4` gives a valid formal right inverse for the entire multivariable family. The five displayed kernel vectors have independent constant terms, so they remain independent over the formal fraction field. This bounds the original 41-to-37 rank by 36. Polynomial minors inject into the formal ring, making their vanishing identities on the affine family, not just at its origin. The generic rank-three second symbol on A supplies the matching lower bound. This proves the conditional generic rank 36 and permanent D lifts, not the existence of the smallest endpoint. The final zero-gate implication uses the pinned original-fourth comparison and asserts no converse.

All multiplication variables remain in the fixed negative W. No cross-direction commutation of homotopy-derived chain maps or extension of h as a graded module map is used.

## Executed verification

Both `python verify.py` and `python -O verify.py` passed all 33 checks with byte-identical output. Independently executed checks reconstructed all six signed maximal minors of the complete D first-arrow matrix, verified the full annihilating cokernel row, constructed free-P block splittings on both projective charts, checked the section/cohomology dimensions and vanishing threshold, verified the relevant Clebsch–Gordan identity through Laurent characters, and checked formal right-inverse/kernel-graph truncations through order seven with noncommuting symbols.

The reproduction commands above verify the bundled exact algebra. The naturality, actual-embedding, equivariance, and formal-to-polynomial arguments are mathematical proof obligations reviewed in the text, not claims of proof-assistant certification. No actual source coefficients or specialized source instances enter the verification.
