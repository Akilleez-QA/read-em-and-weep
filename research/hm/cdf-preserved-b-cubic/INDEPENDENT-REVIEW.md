# Independent review: one-sided c-d-f cubic gate

## Verdict and scope

PASS for the conditional theorem in the exact final bytes below. The reviewer read the complete packet proof and verifier, the PR979/982/966 and original-third inputs in full, and the PR924 and preserved-B inputs already reviewed in the immediately preceding independent review. The preserved-B copy is byte-identical to that reviewed proof and is now pinned to PR1001, commit a7aa990e7705dd9dbf3d0fd34e437fa735c9e0f1, Git blob eebebae694f59e786aaebc64c3838d732b2a3832.

The accepted conclusion is: under the SAME one-sided preservation hypothesis, the internal quadratic vanishes globally, the canonical internal cubic belongs to a raw three-dimensional equivariant Hom space, and its nonvanishing is equivalent to nonvanishing of the generic original fourth Bockstein. Neither value, actual preservation, actual occurrence, nor any source/pair exclusion is established. This review is verification and is not itself a new deduction.

## Actual interfaces and third comparison

PR1001 supplies the actual embedded kernel A+D, zero D first symbol, multiplication on A, H¹(S)=D, quotient H⁰(T)=D and H¹(T)=P, and the connecting/projection isomorphisms. None requires Q to preserve a complement. Its factorization of the original second differential identifies the quotient of b_T by b_T δ⁻¹(aA) with the genuine original second-image quotient. The imported third-zero note explicitly identifies the generic second kernel as D and proves the original third vanishing. The universal PR966 result gives generic rank four for this same projected multiplication family; it does not import source2 occurrence.

A fixed equivariant section of Q_S on its image gives a polynomial first correction for every D input. Its residual modulo the multiplication subbundle defines s globally, not just rationally. Section changes produce only the first-symbol image. Since H¹(S) → H¹(M) is zero, the next original correction exists. Its quotient connecting class is the negative internal residual, giving the third comparison in the correct page target. The original first vanishing handles changes of this correction; the original second-image quotient handles changes of the earlier correction.

On the common dense open, the induced quotient-first map from E has rank one and rank-one kernel. Original third vanishing therefore forces s to have generic rank at most one.

## Universal rank-one exclusions

The exclusions used here are independent of full-radical compatibility. For a hypothetical rank-one image, saturation in the rank-two vector bundle E has torsion-free quotient. On the smooth projective plane the depth lemma makes this saturated rank-one sheaf reflexive and hence a line bundle O(k). Its G-linearization is unambiguous because A5 has no nontrivial characters. Thus the source factor and the equivariant injection both impose the stated representation restrictions.

For the quadratic case, the only possible k is zero; H⁰(E)^G=0 excludes it. Hence nonzero s would be generically onto, contradicting the third comparison. Vanishing extends globally because source and target are vector bundles on an integral plane.

For the cubic case, the only possible k are −1 and 1. They are excluded respectively by H⁰(E(1))^G=0 and H⁰(E(−1))=0. The latter vanishing and the upper bound on k follow from the exact multiplication sequence and H¹(O(n))=0 on P², including negative n. The character recurrence and inner products give the raw cubic Hom dimension three. These are universal statements, not an assertion that three actual coefficients are freely realizable.

## Cubic construction and original fourth comparison

The global vanishing of s gives unique sheaf factorization of the quadratic residual through A O(−1). Its factor has linear polynomial entries. This is not pointwise division or a selected parameter calculation. Subtracting that kernel-valued factor produces a normalized first correction with zero residual already in H¹(S), so a global quadratic second correction exists.

The cubic residual modulo aA is independent of both corrections. Differences of normalized first corrections have no A component, by injectivity of multiplication by a, and are D-valued. Their effect on the cubic is the already-zero internal second class. Differences of second corrections contribute only aA. This establishes a global canonical r, with the usual intrinsic identifications rather than any fixed numerical normalization.

Using these same S corrections inside M produces an allowed third original correction because H¹(S) → H¹(M) is zero. Its connecting class is the negative cubic residual. Projection then gives the original fourth differential modulo the actual original second image. The original first and third differentials vanish, so this is the correct fourth-page target and generic surviving domain D, not a new obstruction of matching dimensions.

The full noncommuting Schur expansion retains the quotient and connecting corrections. After the displayed normalization, its other quartic terms contain s₁|D or s₂|D and vanish. The direct correction argument is primary; the symbolic expansion corroborates it. Since every nonzero raw cubic map is generically onto E and the induced quotient-first map has rank one, the comparison proves exactly the claimed equivalence. It does not compute the specialized original fourth at exceptional directions or select its generic value.

## No imported radical naturality

PR979/982 were checked at their exact reuse boundaries. Their full-J hypotheses and reverse radical chain maps are not supplied by one-sided preservation and are not used in the argument above. In particular neither sκ=0 nor rκ=0 is needed to kill the internal quadratic or construct the raw cubic. There is no justified decrement from three cubic parameters to two in this packet, and no secondary ν is constructed.

The separate reverse-map claim is valid in its explicitly limited category. A full fixed-negative-linear-pencil morphism N/N_B → N_B would compose with quotient and inclusion to an endomorphism of N whose image lies in B and which kills B. PR924 describes the ENTIRE represented endomorphism algebra, including singular elements: the three scalar vertices and the sole L→F radical arrow. Image in B forces the F and L scalars and that arrow to vanish; killing B forces its scalar to vanish. The composite is therefore zero, and degreewise surjectivity/injectivity of quotient/inclusion makes the proposed reverse map zero. This does not prohibit an unrelated two-term quadratic-family map or a new geometric relation established by other means.

## Novelty and mathematical limitations

This is an application of existing universal quadratic/cubic rank-one exclusions and correction methods to the actual one-sided c-d-f interfaces established by PR1001. It is not a new proof of original third vanishing, the original second generic-rank theorem, or the universal PR966 discriminant theorem. The full-J source126 two-dimensional conclusion is deliberately not transferred. The comparison was made with the supplied existing c-d-f and source126 results, not an exhaustive search of every remote publication.

The one-sided hypothesis Q(X_B) ⊂ Y_B remains unproved. The original fourth value remains unresolved. There is no source cut, pair cut, complete repair, claim of actual generic surjectivity, or claim that every raw Hom-space member is realized. The underlying geometric theorems remain imported; this review does not reconstruct all of their transitive dependencies.

## Verification and authentication

Both independent executions completed successfully:

- python verify.py: pass, 53 checks.
- python -O verify.py: pass, 53 checks.

Both report actual_instance_evaluations=0, raw_cubic_hom_dimension=3 and naturality_reduction_imported=false. Their output agrees with the stored JSON reports. Checks use explicit exceptions and survive optimization. All six input copies match both their SHA-256 values and their pinned Git blob IDs. Authentication here means independent computation of content hashes against the immutable pins; the reviewer did not perform a fresh remote retrieval of commit contents.

The synthetic block matrices contain unconstrained symbolic coefficients and are not actual HM instances or equivariant realizations. Their tests establish identities only. The full argument above, rather than the numerical check count or the test asserting 3 != 2, supplies the theorem and its scope. No selected actual coefficients, parameters, points, jets, instance ranks, local-model spike, or public write was performed during review.

## Exact final reviewed hashes

| File | Bytes | SHA-256 | Git blob SHA-1 |
|---|---:|---|---|
| PROOF.md | 10730 | 6a077b4b7595273a544af6cc2cae36541c6a9af513c533550a0affa389ad5cf3 | c66f64c10162f6989843e3cf3e9c9bf33ee6361a |
| verify.py | 5072 | e8987a808a1f36a6c45a706fa29d86a955728de32ed3b57ff393a21ffddc424b | c58825a50e5ea83a602d0d084f4366afd6495356 |
| INPUTS.json | 1814 | 965ed14d5752128417f032e3e079dd752df4db6eb547df9fbb88943d5a5156d3 | 74ed466960e5a60cf2af54470850868253adcc90 |
| README.md | 949 | 87c0e3613cfe941c773640b7ff357fe5ad932f2a6ee3bde9018d6c34b9ccf794 | 650ef05982a6af2afbc3e7eaea993d6a7b909663 |
| checks-normal.json | 335 | 1d82c6c9452f4f5757c2da8300ec223b418fe39e801367faddeb65aa0ebfd4cc | dd06edc3b1c3c1898778ce81713ae329e535a840 |
| checks-optimized.json | 335 | 1d82c6c9452f4f5757c2da8300ec223b418fe39e801367faddeb65aa0ebfd4cc | dd06edc3b1c3c1898778ce81713ae329e535a840 |
| inputs/924.md | 18095 | 0d740d6f70de924b0442af71cb37e050165efbe9ab984a76f0e1e40b5d27a599 | 83f5aee293995257459229e6b323522224ce8f3d |
| inputs/966.md | 10479 | a62f8f6266601987fbfb2f67690a912a9eb9ccb41b04e1d8915652e545390ac4 | 6197582777ccd6f8899ff16e16d335315fd52a99 |
| inputs/979.md | 11137 | 15c1aaaa1517b06a86f942d9b416f920f87251e95f0ad2ab8e00585199564f24 | 59e79d627214f092a4a9be9de6efe3448909e66d |
| inputs/982.md | 12073 | 064b115e5b583ecb98c5d6fae5ca84fc54424c775fbad7d7578fa816f25b4acb | 9b1e90b99f24263b0e97f4d5721e04495454e9bf |
| inputs/preserved-b.md | 7335 | e07a59e7b8e8d35b2f9a164515ff65eeddeca4baca4a0964c731b36b7713e38d | eebebae694f59e786aaebc64c3838d732b2a3832 |
| inputs/third-zero.md | 6221 | 243e242a15ff2bb678b6c1c3cb33f203bbbed5b8bb0c23d8564e14536d9075cd | 7c09fe95015d7c8d932b3a27be302ca09888112d |
