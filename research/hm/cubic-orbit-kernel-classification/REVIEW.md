# Independent mathematical review

Verdict: PASS, conditional on the explicitly pinned geometric inputs.

Reviewed artifact: PROOF.md, SHA-256

    9bbd28cdf0b3685b1d07b7af79c323106eccf4a903c06be370540f04d87d1c44

This is an independent mathematical review, not proof-assistant verification. The review checked the proof against the stated conductor and automorphism inputs in PR623, PR637 and PR639 and reconstructed the new group-theoretic and section-module deductions.

## Actual action and scalar independence

The index dilation D_a sends g to g^(a^(-1)) and s to s^a. This is an actual complex-linear normalizer element, not a Galois action. For a=2 it exchanges the two nonzero difference classes modulo sign. Transitivity on the six directions therefore extends to transitivity on the twelve node-orbit labels. U acts trivially on these labels; inversion fixes each label by the paired-flag calculation. The action hence factors through PSL2(F5), of order sixty, with point stabilizer of order five and pentad stabilizer of order ten.

A polarized automorphism acts on the vanishing subspaces of the actual ten-dimensional section space independently of scalar choices of bundle lift. Thus kernel equality is invariant without asserting a coherent Gamma-linearization or any linear representation on a multiplicity space. Branch-orientation signs affect gluing ratios, not this vanishing-subspace argument.

## Block classification

The simplicity argument using conjugacy-class sizes 1,15,20,12,12 is valid: no proper nonidentity union containing the identity has cardinality dividing sixty. Orders fifteen, twenty and thirty are then excluded by their coset actions of degrees four, three and two. Sylow theory gives six order-five subgroups, so the normalizer of a point stabilizer has order ten. Any order-ten overgroup normalizes its index-two subgroup of order five and is therefore that unique normalizer. It equals the pentad stabilizer.

The block-stabilizer correspondence consequently gives only block sizes one, two and twelve, with the unique two-element block the complementary pentad pair. The known complementarity of that pair excludes both nonsingleton equality classes. All twelve kernels are distinct. Their pairwise intersections vanish by irreducibility under the same Heisenberg cover. Since each kernel and each evaluation target has dimension five, the combined map for every two distinct orbits is an isomorphism.

## Section strata and finite order

The exact conductor equation imposes K_i precisely at field-valued parameters with lambda_i different from one. It therefore gives h0 equal to ten at the identity, five with exactly one active coordinate, and zero with two or more. The reduced positive-section support is exactly twelve coordinate subtori of dimension one and codimension eleven. Restriction to the ample open neighborhood preserves all twelve irreducible components and their dimensions. No assertion about a nonreduced determinantal structure is required.

For two distinct indices and parameters 1+t^k,1+t^l over R_n, the combined evaluation isomorphism identifies the section module with the direct sum of the two five-dimensional targets tensored with Ann(t^k) and Ann(t^l). Each annihilator has dimension min(k,n+1), respectively min(l,n+1), and has nonzero reduction exactly when its exponent exceeds n. This verifies the total dimension and the three stages of the reduction image. In the intermediate stage the surviving subspace is the kernel of the earlier changing orbit. Over C[[t]] both annihilators vanish.

The result is a structural strengthening of PR639, not a selected HM/source-instance evaluation. Its boundary statements correctly leave full linearization, nonreduced jump loci, higher adjoint Bocksteins and Weil-class algebraicity unresolved.
