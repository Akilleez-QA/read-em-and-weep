# Independent review: full ambient symmetry closure

The new closure argument was independently reviewed against the actual primary page images. No mathematical blocker found. The earlier INDEPENDENT-REVIEW.md is preserved unchanged and remains the receipt for the restricted normalizer argument.

## Final bytes and replay

- FULL-SYMMETRY-CLOSURE.md: c7022ca603985108dba5cbf8f72cf619d7150f87469ce91fbe9dec6621a7b91e
- verify_full_symmetry.py: fbd82e800756486b2940ac2de8a4cd3d9930fc9b4d4dc80c4d75ba574bc42f64
- PRIMARY-SOURCE.json: 20e9e9af40e58ca8347d28480e0a0cc959a4f53fa912b0964da6ab020488d5d7
- FULL-SYMMETRY-INPUTS.json: aa4cef56f82ef9ffe25641eee3fde1f806d334da3fd8d94cc87dd5fe4e20c213
- FULL-SYMMETRY-RESULT.json: 9e9db7327b280f02f1bb1f5d2236353aa8fdef2318cc134dbf49858790c6f997

Both normal and optimized executions with the separately held primary PDF passed 19 checks, including its digest, with identical stdout and result JSON. Whole-volume PDF SHA256: b151a38d279eaa771478f78bdcb890f5b99d3e6c74fb7458e1000626d1a97b95. The full scan was not copied into the publishable packet.

## Primary theorem verification

Independently read printed pages 103, 106, 107 and 109 of Decker, Math. Z. 188 (1984), DOI 10.1007/BF01163877, from the page images rather than relying only on OCR or the paper title. Section 2.1 identifies the normalized HM bundle and its coordinate pullbacks. Definition 4.1 is the full SL5 stabilizer under inverse pullback. Section 4.2 defines the Heisenberg normalizer and its order 15000. Theorem 4.2.3 explicitly identifies that normalizer with the full stabilizer; its proof establishes the reverse inclusion, not merely finiteness or an exhibited subgroup. These primary statements are sufficient for the use made here.

## Passage and application

Every projective linear map over C has an SL5 representative by determinant rescaling, and the kernel of SL5 to PGL5 is mu5. Those scalar lifts induce the identity on projective space and preserve the bundle. Thus Decker's equality implies the full projective group is exactly N5/mu5, of order 3000. The inverse-pullback convention does not change the subgroup. Twisting by O(k) preserves the stabilizer, and a coordinate change conjugates the bundle stabilizer and its associated Heisenberg normalizer together.

The previously reviewed argument now applies to the entire ambient projective group: preservation of Q0 forces preservation of its vertex line, whose 25-element orbit and existing order-120 stabilizer force equality with G. Requiring preservation of the specified negative family retains precisely G. Since the canonical octic vector is G-fixed, no additional ambient projective same-bundle, same-Q0 automorphism supplies a nontrivial octic character.

Vertical scalar automorphisms of the stable bundle are not extra base automorphisms, and their conjugation action on its adjoint is trivial. This does not classify automorphisms of the cone restriction, formal neighborhoods, or abstract complexes lacking an authenticated ambient compatibility theorem.

## Scope

The outside-normalizer qualification in the earlier result is genuinely removed by the primary full-group theorem. Decker's theorem itself is imported published mathematics, not a new discovery or a computer-verified theorem. The new application closes the additional-ambient-character route for the fixed octic gate. It neither selects the actual scalar nor excludes a source pair or proves a full repair. No actual HM parameter, coefficient, matrix, or rank was evaluated.
