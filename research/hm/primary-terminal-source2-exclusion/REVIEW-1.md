# Independent whole-proof review 1

## Verdict and exact reviewed artifacts

**PASS, relative to the explicitly retained hypotheses and authenticated theorem inputs.** The argument proves a conditional incompatibility of the actual primary terminal submodule with the genuine source2 terminal separation supplied by PR1072. I found no remaining mathematical gap in that implication. This verdict is not an unconditional exclusion of every meaning of source2, a realization result for another source, or a proof of the original broader goal.

The exact reviewed `PROOF.md` SHA-256 is:

`7be070050a035ceec64c5698fd1ae70857225a405e1a43d4cbebc4019f5a342a`

The exact reviewed `verify.py` SHA-256 is:

`0c990122d3a27e06830e6edec8c48d79f3f0adec42d70beebbe780e50571b08a`

The exact reviewed `RESULT.json` SHA-256 is:

`3c1d416e4777014b5cee326ce383a075851d2e96915eadee34d7ce0530292b79`

This review was performed independently against the full proof, all five complete local originals, fresh immutable GitHub-connector fetches of those originals, and the checker source and execution. I did not infer correctness from the other review or the checker result.

## 1. Independent source authentication

I fetched each complete original directly through the GitHub connector at the stated immutable commit. The fresh fetched content matched the corresponding local `inputs/PR*.md` bytes exactly. Independently computed Git blob hashes and SHA-256 digests agreed with both the connector and `INPUTS.json`; byte lengths also agreed. The exact successful records are in `AUTHENTICATION-REVIEW-1.json`.

- PR477, `ff87076794e97238150485b12183c3cd0f4711e4`, `research/hm/adjoint-primary-extension/PROOF.md`; Git blob `1cb91b7f5b7da08b6653c7fa48487ff7c3fd7198`.
- PR486, `0de9b4b71cbbf3c4492871d9835952a0dcb41e12`, `research/hm/level-section-resolution/PROOF.md`; Git blob `93a379dc422c45b4fad210d782169abc3583c286`.
- PR1120, `62587a0adde566cac718ee13c28ee13c239389e5`, `research/hm/scalar-cyclic-module/PROOF.md`; Git blob `af00766042cdc7e100731aa69b9ad8d32db0209f`.
- PR1121, `1b1c33a6a348a31e00d7b322a43ecd6d4a8cea7a`, `research/hm/scalar-channel-projector/PROOF.md`; Git blob `719ba5260fa9d0d1b548c867c2504d627552ba24`.
- PR1072, `d03beb727c7e778026dcceb3555c899a0808e093`, `research/hm/terminal-pencil-quotient/PROOF.md`; Git blob `65dda3e16ded2b79ad84c583f248b09c425e9881`.

I also fetched and read the complete PR1056, PR795, and PR1068 originals at the immutable commits linked by PR1072. These corroborate the ambient parity/degree identification and the actual-map transfer, rather than merely matching bundle characters. Their URLs and connector blob identifiers are recorded in the independent authentication record. This supplementary check does not replace the five primary originals or silently broaden the theorem's hypotheses.

## 2. Grading and actual module inclusion

PR477 constructs the injection before using dimensions to establish its injectivity. Its maps arise from the evaluation resolution, connecting maps, and Serre duality, and commute with multiplication by the same polynomial. Thus the proof legitimately uses a single graded module injection, not independently selected representation embeddings.

The degree translation is correct:

- `L5=U tensor H1(F(2))` embeds in `K5=H1(B(4))`.
- `L6=U tensor H1(F(3))` embeds in `K6=H1(B(5))`.
- `U=P` is positive, so the positive part used at the first vertex is exactly `U tensor Y`, where `Y=1+A`.
- `Z=H1(F(3))=W` is entirely negative, so the entire terminal primary space `U tensor Z` lies in `M5=H1(B(5))_-`.

The proof now explicitly defines `M4=H1(B(4))_+` and `M5=H1(B(5))_-`. PR1056 Section 1 independently confirms these are PR1072's actual terminal vertices. There is no degree shift error or replacement by equal-character spaces.

## 3. Parity, levelness, and the actual evaluation pencil

The central parity argument is valid under the retained physical marking: multiplication by a positive coordinate preserves parity, while the full target `Z` is negative. Therefore every positive coordinate kills every vector of `Y`.

If `c(y)=0`, every negative coordinate also kills `y`. The module injection then sends `u tensor y`, for any nonzero `u`, to a socle element of `K5`. PR486 proves that the actual five-coordinate socle is precisely `K6`, so this image is zero; injectivity forces `y=0`. This argument uses all five generators, not just the negative socle or a truncated module's socle.

The dimensions of `Y` and `Hom(W,Z)` are both four, so injectivity proves the actual curry `c` is an isomorphism. No unknown primary arrow scalar is assigned a value. The ensuing evaluation map is the original multiplication under this actual isomorphism.

On the common parameter line, evaluation on the tautological line gives kernel

`Hom(W/O(-1),Z) tensor O(-1) = Z O(-2)`.

Here `det W=1` gives `W/O(-1)=O(1)`. Tensoring with the constant `U` produces the claimed primary kernel `(U tensor Z)O(-2)`, source rank 16, target rank 8, kernel rank 8, and kernel degree -16. Surjectivity holds at every parameter because all linear maps `W -> Z` are present. This is a universal exact bundle sequence, not a generic-rank assertion or a chosen-direction computation.

## 4. Parameter convention and genuine projectors

The initial draft's wording identified `P(W)` as though it were literally PR1072's named line `P(W*)`. I requested an explicit common-line statement. The final proof now keeps PR1072's original line and, if using the determinant identification, pulls **both** pencils through the same fixed isomorphism. This resolves the precision issue.

PR1056 explicitly identifies its cohomological multiplication with the negative arrows after one determinant rotation. PR1072 Section 2 proves that the diagonal-resolution rotation cancels it, yielding the original pencil `u m_x+v m_y` again. PR1072 Section 3 then obtains the decomposition through degree five from the genuine kernel-bundle decomposition and natural cohomology maps. Consequently its coefficient projections at degrees four and five intertwine the same actual negative arrows used by the primary inclusion.

The proof does not assume that the projectors preserve positive-coordinate multiplication, the invariant quadratic, the primary subspace, or an intermediate positive channel. It only composes the primary inclusions with genuine coefficient-space projections at the two relevant vertices. That is enough to obtain the required morphism of terminal pencils.

## 5. Hom vanishing and factorization

The lemma is correct for any constant coefficient spaces, with no equivariance needed. A coefficient-space morphism induces a map from the first kernel bundle to the second. For `m>2`, its entries lie in `H0(O(2-m))=0`, so the first coefficient map annihilates the entire source kernel.

Since the source sequence is exact as sheaves and ends in the vector bundle `A2 O`, the coefficient map factors through that actual cokernel. The resulting map `A2 O -> C1 O(-1)` is zero because `H0(O(-1))=0`. Thus the first coefficient map vanishes. Commutation and the surjectivity of the source pencil force the second one to vanish as well.

There is no need to extend a map, invoke an unproved splitting, choose a parameter, or infer kernel annihilation from a character. The direction of the Hom vanishing is correct: maps from the short `O(-2)` kernel to the long `O(-m)` kernel vanish. The strict inequality is essential and is correctly retained.

## 6. Contradiction and claim scope

PR1072 supplies the exact first-block sequence with kernel `W O(-8)`. Applying the lemma to the composed coefficient maps forces both primary first-block projections to be zero. In particular the actual injective terminal primary map has image in the actual residual summand.

Its source has dimension `dim(U tensor Z)=8`; PR1072's residual terminal target has dimension 6. This alone is a contradiction. The alternative `W'`-versus-`T6` formulation is also valid but is not needed to make the argument work. It is used only after the actual containment has been proved, not to choose an embedded summand.

The retained actual-transfer and nonzero pure-V compatible-radical hypotheses are essential premises of the imported genuine splitting. The proof correctly excludes their simultaneous satisfaction for the fixed module, without claiming to exclude abstract source2 normal forms or every differently defined source2 condition. No residual-large choice, vanishing fourth/fifth obstruction, positive-projector preservation, primary/repeated-V incidence, or new source realization is inserted.

## 7. Checker audit and independent execution

I inspected every operation of `verify.py` and ran both `python verify.py` and `python -O verify.py`. Both passed all 56 controls and matched `RESULT.json` byte for byte. I separately compared all five manifest records against my independent fresh-fetch authentication records.

During review I found that an earlier version defined `Wp` by the very identity subsequently checked. I requested an independent fixed nine-class row. The frozen checker uses that independent row, so this particular identity is no longer tautological.

The evaluation matrices and the three pencil-morphism systems are universal formal binary models, not selected HM/source tensors or matrices. The two affine-chart checks establish a universal evaluation splitting and kernel generator on a covering, not a test at a selected actual parameter. The `m=2` nonzero control verifies the sharp boundary of the vanishing, while `m=3` and `m=8` give zero Hom controls. Explicit exceptions rather than Python assertions ensure the controls survive optimized execution.

The checker is appropriately bounded. It does not certify actual module maps, their naturality, source transfer, or geometric hypotheses through arithmetic alone. Those steps are supplied by the written argument and the authenticated source theorems, as both the proof and reproduction guide state.

## Final assessment

Both issues raised in this review, the parameter-line wording and the circular character control, were corrected in the exact artifacts identified above. There are no unresolved substantive objections to the conditional theorem. No selected HM/source coefficient, tensor, matrix, parameter, derivative, rank, or scan was evaluated in this review, and no public write was performed.

## Publication-hygiene readback

I verified that the final proof differs from the previously reviewed exact bytes only by removal of its final operational sentence about publication authorization. Restoring that sentence reconstructs the previous proof SHA-256 exactly. No mathematical text changed; the PASS verdict therefore applies to the current proof hash recorded above. `AUTHENTICATION-REVIEW-1.json` contains only public source identifiers, URLs, digests, byte counts, and authentication outcomes.
