# Root mathematical review

Reviewed INDEPENDENT-DERIVATION.md SHA256: `cd399441e16ecd29971c9f84e3a097e5952b120d4eb99e2a7801db0a2745ef3c`.

Accepted conditional on the pinned actual module, pairing, and representation inputs. I independently checked the full-extension exclusion and its use in resolving the symmetric kernel.

If every map from W to H_d extended, each qA would extend for all q in S_d and A in End(W). Applying such a map to a quadratic relation indeed says that every q kills its A-transformed class in H_2. Perfect pairing with H_3, and generation of H_3 from W, show that no nonzero H_2 element can be killed by all of S_d for d=0,1,2. Thus the relation space would be stable under every matrix unit on W. Extracting the two coefficients then makes them quadratic scalar annihilators, contradicting I_2=0. This argument excludes full extension; it does not incorrectly assume that an individual endomorphism is normalizer-equivariant.

The space of all graded S-linear endomorphisms is stable under normalizer conjugation. In each of the three degrees, its ambient space modulo the scalar subspace is the stated irreducible. Hence there are only two subspace possibilities, and the exclusion forces exactly the scalar subspace. The use of I_2=0 ensures that the quadratic scalar subspace is embedded with its full dimension.

The tensor-Hom grading is correct: a functional on tensor degree n pairs an endomorphism of degree5-n through the total-degree-five perfect pairing. Balance is equivalent to S-linearity, and swap corresponds to the ordinary adjoint without a super sign. Scalar maps are self-adjoint. Combining the low-degree bridge of PR490 with the newly determined endomorphism degrees proves the remaining degrees3,4,5 of the symmetric map; generation and support exclude all other degrees. The global isomorphism therefore follows, not merely equality of one Hilbert coefficient.

Dualizing this exact scalar pairing identifies all self-adjoint endomorphisms with the actual scalar copy of R. The skew part has dimensions5 and1 in degrees4 and5 from the known exterior square. Its products vanish by degree, and scalar S-actions commute with all S-linear endomorphisms. Thus the canonical commutative square-zero extension and its seventy-dimensional Hilbert series are justified.

The result resolves the higher symmetric kernel, but not the separate Betti parameters or fixed-pair/source, higher-order, or algebraicity questions. This is mathematical review, not formal proof-assistant verification; no selected HM/source-instance computation, numerical rank calculation or coefficient search was used.
