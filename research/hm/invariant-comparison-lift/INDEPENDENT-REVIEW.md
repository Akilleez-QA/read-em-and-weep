# Independent review: invariant scalar-to-excess comparison

## Verdict and scope

The derivation in `PROOF.md` is valid, conditional on its pinned representation and resolution inputs. The conclusion is a forced isomorphism from the four-dimensional invariant minimal degree-five syzygy summand Qspin onto the Qspin summand of the degree-five free comparison target. This is an independent mathematical review, not a proof-assistant formal verification. No selected HM/source-instance evaluation or matrix computation was performed.

## Checks

1. **Degree-zero comparison.** Fixing the canonical identification on cubic generators leaves a possible degree-one polynomial map from the quartic generator space V⊗U to T⊗A⊗W′. The latter decomposes as V⊗(W′⊕Qspin⊕T_4), with no V⊗U. Semisimplicity and the pinned irreducible, inequivalent normalizer labels therefore force this map to vanish. The chosen quartic generators indeed lie in D and vanish under I→Z. Thus the comparison on covers is the projection onto the cubic block.

2. **Existence and uniqueness in degree five.** A degree-five syzygy representative maps to the kernel of F_0(Z)→Z, so exactness supplies a lift to F_1(Z). The kernel of F_1(Z)→F_0(Z) is the image of F_2(Z); its degree-five component vanishes because F_2(Z) is generated in degree six. The degree-five lift is therefore unique. This does not require an injectivity assertion in higher degrees.

3. **Source character.** Write K for the first syzygy module of I. The exact sequences in degree five are

   0 → K_5 → (F_0(I))_5 → I_5 → 0,

   0 → T⊗(V⊗W′) → K_5 → B → 0.

   The second sequence is exact on the left because the pinned scalar resolution has no second syzygies in degree five. Exactness of finite-group invariants yields

   [B^Γ] = [W′⊕Qspin] + [U] − [U] − [W′] = [Qspin].

   Since the normalizer quotient representation category is semisimple over C, this representation-ring equality determines the actual invariant representation. It is not merely a dimension count. Likewise the target invariant representation is W′⊕Qspin.

4. **Kernel exclusion.** If the comparison lift of an invariant syzygy vanishes, its cubic coefficient block vanishes under the projection of check 1. The syzygy is therefore supported solely on the quartic generators. Its coefficient vector lies in (T⊗V⊗U)^Γ≅U. The derivative identification places every derivative of each invariant quintic in the chosen V⊗U quartic summand. Euler's identity provides a preimage of 5f for every invariant quintic f. The Euler preimage is invariant, either by equivariance of the differential and contraction or by averaging. Hence multiplication U→I_5^Γ≅U is surjective and consequently injective. There is no invariant quartic-only relation. A zero syzygy representative represents zero in B, proving injectivity on B^Γ.

5. **Image and choices.** Normalizer equivariance excludes a map from Qspin to W′, so the injection lands in, and is an isomorphism onto, the unique Qspin target summand. Two equivariant choices of representatives differ by a map into the lower-syzygy multiples. On Γ-invariants these multiples are W′. The difference on Qspin is therefore zero. This verifies the stated independence from the choice of equivariant degree-five representatives, with the covers and representation identifications fixed.

## Essential distinction

The nonzero map is a component of a comparison of free resolutions with linear polynomial entries. It is not a nonzero degree-five map on Tor_1(I)→Tor_1(Z): Tor_1(Z) is concentrated in degree four, so the linear entries vanish after tensoring with S/m. In particular this result alone does not determine the subsequent degree-six comparison or the connecting map of PR503. The remaining degree-five syzygy components can contribute to the degree-six compatibility equations. The proof correctly leaves k in {15,25,35,45}, and makes no claim concerning a selected fixed-pair/source evaluation, higher-order lifting, or algebraicity.

## Dependency audit

The reviewed local dependency texts agree with the required statements of PR489 (quartic generators, derivative realization and invariant quintics), PR500 (absence of degree-five second syzygies of I), and PR502 (pure excess resolution, with second syzygies of Z beginning in degree six). The module identification from PR498 and the comparison boundary from PR503 are used as the pinned hypotheses cited in the proof. This review does not replace or re-prove those earlier dependencies.
