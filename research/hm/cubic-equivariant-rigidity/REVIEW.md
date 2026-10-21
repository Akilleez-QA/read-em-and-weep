# Independent review: Heisenberg-equivariant abstract Artin rigidity

Verdict: PASS.

Reviewed artifact: PROOF.md.

Reviewed SHA256: 2d7234048dff908e4bf5e83ee85bfe63dbe5b682ed2ac204e17a6b41825d83eb.

This is an independent mathematical review, not machine-checked formal verification. The reviewer read the complete proof and checked its use of the pinned PR610 and PR614 dependencies. No selected source-instance evaluation or large computation was performed.

## Checks

1. The tangent space to P4 at the eigenline L_i has the four nonzero direction weights k-i. A U-invariant tuple of center tangent vectors must have each component fixed by its stabilizer, which contains the corresponding cyclic direction. Thus the tuple vanishes. Exactness of finite-group invariants over C then implies H1(Theta_M)^U=0 from the canonical center-motion sequence.

2. In the universal blowup chart at the marked eigendirection p_ij, the normal coordinate has weight j-i and the three exceptional-chart directions have weights k-j for k distinct from i,j. All four are nonzero. Consequently the direct sum of tangent spaces at all 120 conductor preimages has no U-invariants. The natural conductor tangent exact sequence from PR614 therefore gives H1(Theta_V)^U=0. Neither a splitting of this sequence nor a numerical evaluation map is required.

3. The canonical identification T1(V)=H1(Theta_V) is supported by the local cotangent T1 vanishing in the cited dependency. Thus the invariant vanishing concerns the full abstract first-order deformation tangent, not only an ad hoc presentation deformation space.

4. PR614 supplies affine Artin rigidity and the lifting of local trivializations compatible with a specified reduction. Across a small extension, their overlap differences are a Cech one-cocycle with coefficients Theta_V tensor I. The constant deformation gives a distinguished origin. An extended U-action makes the resulting marked lift class invariant, because the reduction identification is equivariant and the base action is trivial. Its invariant subspace is zero, so the class is zero and the underlying lift is trivial relative to the prescribed reduction.

5. The difference of two relative trivializations is an infinitesimal automorphism in H0(Theta_V) tensor I, which vanishes. Therefore conjugation by each group element leaves the trivialization unchanged. Induction through a finite chain of small extensions proves unique marked equivariant triviality over every local Artin C-algebra. This avoids any unsupported upgrade from a first-order calculation to a higher-order claim.

6. Retaining Gamma implies retaining U. The uniqueness established inductively also forces the constant trivialization to respect Gamma; equivalently, the same proof applies to Gamma-invariants. No injectivity assertion for Picard pullback or global cotangent T2 vanishing is used.

## Scope

The theorem requires the fixed complex-linear U-action on the special fiber, an extending action on the deformation, and a trivial action on the Artin base. It does not make the unrestricted 576-dimensional abstract deformation space rigid. It does not assert algebraization, convergence, or a result for the original full adjoint system. Those boundaries are correctly stated in the proof.

No corrections are required for the reviewed artifact.
