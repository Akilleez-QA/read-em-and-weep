# Independent whole-proof review: PASS

## Reviewed object and scope

I read the complete `PROOF.md`, including every geometric step, the seven forced residual forms, all target-dependent rank exclusions, and the final extension calculation. This review is bound to the exact proof SHA256

`793c635439cf05c0234b4152aca4e9213780258d096d9036902b808a952f39e4`.

The result is correct under its explicitly imported actual-geometric hypotheses. It is a new application of the previously proved universal principal-parts identity, not a new universal identity, a realization theorem, or an exclusion of either primal form. No revision of the mathematical proof was required.

## 1. Source authenticity and hypothesis boundary

I independently fetched all three complete original files through GitHub at their immutable commit refs. Each fetched file agrees byte-for-byte with the retained input, its declared byte length and SHA256, and both the returned and independently recomputed Git blob SHA1. `REVIEW-AUTHENTICITY.json` records the full evidence, source URLs and exact proof hash.

- Endpoint-jet theorem: PR1200 at `99a0ce465e605210b1c64fcfd4e0e0b78de0472b`, proof SHA256 `bbe7c05e9055b70ba511c77ebc0514a0fdf89d75844199f971e7e774355c08c6`.
- Pair-defect theorem: PR1197 at `0156405384eefb3efe08d724e682b4a839157bfc`, proof SHA256 `95cc7824898dd0bffe13f86ab1ede2947451eb3d4632e189baa608ad0de3fdec`.
- Universal principal-parts source: PR1199 at `95af2c0fa1e3cce92496a44ef9023708735e1ec7`, proof SHA256 `09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26`.

I read the complete endpoint and pair-defect texts, and read the complete principal-parts source while restricting the import to Section 4's universal bundle identity and actual differential-evaluation construction. No triplet-specific flag, degree, image or defect has been transferred into this theorem. Earlier actual-geometric premises remain conditional imported premises, rather than newly proved claims of this review.

## 2. Actual second jets, not a complete coefficient system

The first everywhere isomorphism in (3) makes the local classes of `u,u'` a frame of the actual `L0`. The second isomorphism is induced by the actual second fundamental form of `L0`, whose kernel is `U`. It therefore takes the nonzero first-derivative class to a generator of `(M/L0)(-2)`. Equivalently, `u''` generates `M/L0` in any local coordinate and frame. Changes of coordinate and frame have invertible triangular transition on this filtration, so no selected actual parameter or jet is needed.

Consequently the dual of the actual coefficient-system evaluation to second principal parts has fiberwise rank three everywhere and image exactly `M`, not just its generic image or saturation. The evaluation itself is surjective. All maps are natural under the physical group action. Applying the established identity with `n=10,k=2` gives the physically linearized `M=A_std(-8)`, of rank three and degree -24. This argument neither assumes nor proves that the map `C -> H0(O(10))` is complete or injective.

## 3. The residual target and unchanged torsion

The line `ell=M/L0` is the same embedded saturated line in `B0` and in `F*(-2)`, by the endpoint input. Quotienting the exact coherent inclusion by this common line gives an injective map `B0/ell -> F*(-2)/ell` with the original torsion cokernel. Since `B0/ell=S0/M`, this is exactly (11); its length twelve and inherited equivariant torsion characters do not change. The argument does not silently saturate `R -> Q`.

The descriptions of `Q` are correct: a nonzero constant direction in the repeated scalar block leaves `O(-4)+O(-6)`; an Euler line with zero scalar component has that same quotient; a nonzero scalar component makes the line a graph and leaves `W(-5)`. These are universal zero/nonzero alternatives, not selected coefficients.

Both targets are negative, hence so is the coherently injected residual bundle. Thus `H0(R)=0`, making the cohomology subtraction valid. The rank, degree and character are

- `rank R=2`, `degree R=-22`;
- `H1(M)=V+2P+2D`;
- `H1(R)=A_std+V+P+2D`, of dimension twenty.

No connection is assigned to a quotient.

## 4. Complete small residual exhaustion and rank exclusions

Finite-group equivariant Birkhoff splitting, perfectness and center-even action justify exactly the two odd doublets at degree -11 or the five unordered even scalar partitions displayed in (16). A repeated scalar degree would be odd and have the wrong central sign. There are no omitted rank-two representation blocks. Keeping the `j=2` partition is harmless although the negative target gives a stronger degree bound.

The independent closed-character calculation gives exactly the five character survivors in (17). The `j=2` and `j=8` rows each have a trivial constituent and the stated different character.

The fixed Hom exclusions use only zero components and resulting upper bounds on generic rank. For the scalar target, the physical doublet vanishes, the other doublet reaches only one target line, and the `(-10,-12)` pair vanishes. For `W(-5)`, the physical doublet vanishes, the `O(-4)` source line vanishes by degree, and both `(-10,-12)` lines vanish. Every discarded form is therefore incompatible with a rank-two coherent injection. Every retained form remains only a necessary possibility. Neither a nonzero Hom space nor an array of dimensions is mistaken for an actual full-rank map.

## 5. Extension calculation and four middle bundles

Equivariant Ext is the invariant part of ordinary Ext because invariants are exact for finite `G` in characteristic zero. The `W'(-11)` residual has ordinary Ext zero. For the `(-6,-16)` residual, the potentially nonzero ordinary term is `A_std`, whose invariants vanish; the other term has zero ordinary H1. Both residual forms therefore give the claimed equivariant splits.

For `(-4,-18)`, only the `O(-4)` term contributes. Its invariant extension space is `(A_std tensor Sym2 W)^G`, which has dimension one. The canonical cubic evaluation sequence has kernel `A_std(-8)` and middle bundle `S4(-7)`; it cannot split even ordinarily because `Hom(O(-4),S4(-7))=0`. It therefore represents the unique nonzero equivariant class up to scaling a boundary line. The separate `O(-18)` extension is zero. This gives precisely the two additional middle-bundle possibilities.

The target restrictions on the four forms are correct, and the proof explicitly avoids declaring these equivariant Birkhoff summands horizontal. The original defect remains twelve.

## 6. Independent executable audit and replay

`review_verify.py` was written independently and imports only Python standard-library modules, not `characters.py`, `verify.py`, or any author checker. Its representation model uses exact closed binary-icosahedral conjugacy-class traces in `Q(sqrt(5))`, class sizes and the elementary SU(2) symmetric-character recurrence. It verifies the physical irreducible basis, the fixed cohomology/products, exactly two doublets and five scalar partitions forced in this proof, the small universal Hom spaces, five relevant Ext dimensions, and structural rank/degree arithmetic. It performs no broad candidate or historical search.

The final executable uses explicit counted `require`/`RuntimeError` checks, not Python assertions. It requires `INPUTS.json`, binds the exact three source hashes and lengths, and fails if the frozen proof hash changes. It emits JSON only to stdout.

Normal and optimized execution both passed 413 explicit guards, including internal exact-arithmetic integrality checks, and produced byte-identical `REVIEW-RESULT.json`. A fresh isolated replay containing only the independent checker, proof, manifest and three inputs also produced byte-identical output with both `python -I` and `python -I -O`. In that isolated copy, changing the proof or removing the source manifest was rejected under both execution modes. The executable checks support but do not replace the full geometric review above.

No actual HM/source coefficient, parameter, point, jet, tensor, matrix or instance rank was selected or evaluated. The review performed no public write, merge, upstream submission, or local-Codex task.

## Conclusion

PASS for the entire exact-hash proof. The new contribution is the intrinsic actual second-osculating bundle and the subsequent target-dependent residual and extension restrictions, yielding four necessary small-dual bundle types. The proof does not close the two primal branches or the wider rank-four problem.
