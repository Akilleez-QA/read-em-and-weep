# Independent receipt: c-d-f duality/complement barrier

## Verdict

PASS for the precise insufficient-inference claim, with the scope qualifications below. The reviewer read the entire proof, verifier, and original actual-presentation input. The other four input copies were verified byte-identical to the complete proofs already read in the preceding independent c-d-f review. All five input SHA-256 and Git blob hashes authenticate against the pinned IDs.

The packet establishes that graded trace/Serre adjunction, the stated endpoint/kernel/cokernel characters, one-sided preservation and the scalar compatible-algebra condition do not imply complementary preservation. It does NOT provide a counterexample satisfying the complete actual HM multiplication tensors, original Bocksteins or bundle realization conditions. It cannot rule out a complementary-preservation theorem using additional actual geometry. This review is verification, not another deduction.

## Exact duality interfaces

The trace pairing on sl₂ has the displayed Gram matrix and determinant −2, so it gives a nondegenerate conjugation-invariant pairing on End₀(F_HM). Serre duality on P⁴ pairs H¹(B_ad(d)) with H³(B_ad(−d−5)). Multiplication by the invariant quadratic consequently transposes to the map H³(B_ad(−9)) → H³(B_ad(−7)). Invariant trace and the equivariant canonical-bundle identification preserve the matching dual eigenspaces; the perfect binary icosahedral group introduces no determinant character. This is a dual arrow of dimensions 37 → 41, not a second arrow in the original 41 → 37 window.

The direct trace cup of the two original endpoint classes has target H²(O(6))=0. Abstract self-duality of individual irreducibles supplies neither a perfect cross-pairing between spaces of different dimensions nor identifications of repeated multiplicity spaces or marked complements.

The pinned actual-presentation note explicitly gives both P¹ sequences written in the packet. Applying P¹ Serre duality to the covariant reconstruction gives X*=H¹(Q_bundle*) and Y*=H⁰(E*(−2)). Dualizing the ambient exact sequence exchanges E and Q_bundle*, whose ranks are 17 and 13. On the B block, the respective bundle ranks are seven and four and the endpoint dimensions are 24 and 21. These operations do not make the marked Q block self-adjoint in its original window.

Under one-sided preservation PR1001 further forces the actual total kernel inside X_B and Y_B inside the total image. The reduced marked source has dimension 16, while the marked target still has dimension 21. The stated impossibility concerns a perfect cross-pairing aligning those particular marks, not every possible pairing or duality involving their surrounding spaces.

## Annihilators, not complements

For Q:X→Y, the identity <Qx,z>=<x,Q∨z> proves Q(U)⊂Z if and only if Q∨(Z⊥)⊂U⊥. In the specified splitting this is Q∨((Y_F⊕Y_L)*)⊂X_F*. The desired complementary condition would instead give Q∨(Y_B*)⊂X_B*. These are distinct block conditions. No equality between them follows from taking a transpose. This argument does not choose an orthogonal complement or identify Q with its transpose.

## Counterfamily over the Laurent ring

The formal family is valid over R=C[t,t⁻¹,u,u⁻¹], not merely at a numerical specialization. Its V map is invertible. Its P map is split injective, with split quotient functional (−u,0,0,1). Its D map is split surjective; the displayed right inverse uses only the allowed Laurent unit t⁻¹, and its kernel is exactly the second B-source D. Thus the total kernel is A+D, the image character is 2V+3P+3D and the cokernel is P. The B restriction has image V+2P+D and cokernel D. The whole Y_B is in the image.

All B-source columns outside Y_B vanish. The complementary D entry t·id_D is nonzero and remains nonzero as a transposed opposite block. Accordingly the family genuinely violates complementary preservation while satisfying one-sided preservation and the necessary character data.

The algebra action used in the commutator calculation is exactly PR924's represented endpoint action, including its genuine P radical arrow L→F. The V equation forces d=a, the D equation t(b−a)=0 forces b=a, and the P equation uw=0 forces w=0. Both implications hold over R since t and u are units. Common scalars suffice in all remaining entries. Thus the compatible subalgebra inside that represented algebra is exactly R·1, not merely a generic or dimension-count conjecture.

Evaluation pairings between the formal spaces and their duals are perfect, and adjoining the transpose gives the exact adjunction identities. The degree-one/degree-three interchange can carry the usual graded sign without changing adjunction for degree-zero multiplication. This realizes the claimed linear graded-duality data. It does not manufacture actual cohomology of an HM bundle.

In particular the family does not include the fixed negative quadratic maps T_a or enforce their original Bockstein relations. The full represented negative-pencil algebra is used as an externally specified algebra of endpoint actions in which compatibility is tested; the model is not claimed to reconstruct every underlying negative-pencil tensor or bundle presentation. The packet states these limitations expressly. Its counterexample is sufficient for the narrowly stated inference and insufficient for an assertion that all actual-geometry routes fail.

## Terminology and limitations

Before final freeze, the opening phrase was changed from “representation-faithful family” to “character-faithful family” at the parent reviewer’s direction. This is an editorial clarification only: the center-even endpoint representations are not claimed to be faithful representations of the binary group.

No actual HM/source coefficients, parameters, points, jets, instance ranks, local-model spike, or public writes were used in this review. The generic symbols t,u are independent Laurent-ring indeterminates. The universal sl₂ Gram calculation is not an actual HM matrix calculation. The imported geometric theorems are not reconstructed through all their transitive dependencies here. No source or pair is removed, no preservation/occurrence theorem is proved, and no original fourth value is selected.

## Verification

Independent runs of python verify.py and python -O verify.py both pass all 46 checks, with actual_instance_evaluations=0. They agree with both stored JSON reports. Explicit exception checks survive optimization. The input hashes below match the manifest, including the original actual-presentation blob b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3. Authentication is independent content-hash comparison against the pinned IDs, not a fresh remote retrieval of each commit.

The finite checks corroborate the exact identities; they are not proof-assistant certification of duality or of the stated inferential boundary.

## Final reviewed bytes

| File | Bytes | SHA-256 | Git blob SHA-1 |
|---|---:|---|---|
| PROOF.md | 9428 | 7016e0f67e9d0e92c711f0bf870bf5d9821a138cbee7dd4608e6ec2946d331b3 | c748e22b0bcd774a508cdc394aab0e85099339ea |
| verify.py | 3458 | adbe2ba42e99e133f982f047c69e98f4f99c2c9b2c79d197df3f08c4ac1f8bfb | f5861524e377e96a0c76118efd5700062da72e12 |
| INPUTS.json | 909 | 1bc9087cad49555354b386df69bbaa0e6da672e1b09c9e794626c220061a86bd | 94622e3a2c71456161face8d67d7ee84d73ae1d8 |
| README.md | 708 | 8fb090fee45281a5c825644a53e38e31c869b918912da8ca2c42039f0f24d64d | 341ef87bce6d265aa4db48336108afb6eefb6ff3 |
| checks-normal.json | 314 | 82bde4b719663c29d7cc1518ae4b18e94e3c136467f320e6eecab7cee68a4042 | 5a159211ae5ac39ec7cb1ccd4517c3db6bf0d651 |
| checks-optimized.json | 314 | 82bde4b719663c29d7cc1518ae4b18e94e3c136467f320e6eecab7cee68a4042 | 5a159211ae5ac39ec7cb1ccd4517c3db6bf0d651 |
| inputs/1001.md | 7335 | e07a59e7b8e8d35b2f9a164515ff65eeddeca4baca4a0964c731b36b7713e38d | eebebae694f59e786aaebc64c3838d732b2a3832 |
| inputs/924.md | 18095 | 0d740d6f70de924b0442af71cb37e050165efbe9ab984a76f0e1e40b5d27a599 | 83f5aee293995257459229e6b323522224ce8f3d |
| inputs/935.md | 11636 | 06fe9d6bf5f51d1d38ff5f594f93703cf91b48d6cffcf7256c3e281de631365d | 187fe2a8c1499e11afdb5002091aa3c144e1b4a3 |
| inputs/939.md | 4455 | 8263fd71ba117d916411829cc2063c73ae70ca04433d2237b0c05600542301b0 | 00452eb96b90000d9f938a8d96c0ecb780d02160 |
| inputs/presentations.md | 9672 | a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256 | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 |
