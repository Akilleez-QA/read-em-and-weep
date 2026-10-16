# Independent review of the combined-inner numerator

## Verdict and scope

The combined numerator and its differentiated owned-denominator identity are correct as a conditional algebraic certificate. This accepts a formula-level implication, not a physical-source implementation or an admission of any global regularization group. The input assumptions remain substantive: the actual source-clearing homogeneous identity, fixed polynomial partition quotients, fixed standard-cover maps, and their stated support/domain properties. No coefficient of a physical source was calculated in this review.

Two convention clarifications were identified, implemented by the author, and independently rechecked: general common-cover alternation is now separated from the stronger source-pullback zero rule, and output edges are explicitly increasing before alternating extension. The latest revised artifact is accepted within the conditional scope above. These corrections do not alter the displayed numerator or numerical bounds.

## Sources compared

Read the supplied PROOF.md, certificate.py, certificate.json and test_certificate.py against:

- math-progress/refined-tracefree-pole-domain.md, especially sections 1–3;
- math-progress/transposed-scalar-demand-grammar.md, especially sections 2–5 and 7;
- the original hm-transition-scalar-finite-demand.md, sections 1–5;
- hm-transition-only-first-lift-alternative.md, sections 2–5;
- hm-regular-cover-transport.md, sections 2–3 and 7.

The comparison used local text copies, not a fresh authentication of the remote repository or a replay of the physical source proofs.

## Verified algebra

Writing the first prism summand as rho_u P_[u,a,b]/(C_u C_a C_b) leaves denominator C_a C_b. The second summand is negative and leaves only C_b after cancelling C_u C_v. Consequently the common-denominator numerator is exactly

    C_a C_b Z_ab B_ab
      + Z_ab sum_u Qhat_u P_[u,a,b]
      - C_a Z_ab sum_(u,v) Qhat_u Qhat_v P_[u,v,b].

The unequal C_a padding in the second family is required. It is not legitimate to give both families the same unchanged suffix.

The finite-frame multiplier of each inserted quotient is x_i^(-14 d_v-deg(ell_vi)[i in pair]) at each infinity bit. It appears once, with no extra pair-character factor on the scalar weight. Coupled legal quotient/degree cases give pair-coordinate negative bounds 553 for mask zero and 554 for mask one. Complementary coordinates give 553. Thus one designated output factor of order 5250 clears each inserted quotient. When the two inserted tags coincide, their two designated output occurrences still supply two factors.

The radical-labelled-factor derivative formula follows directly from the product rule. Treating two equal polynomial values as two owned factors remains valid: both occurrences contribute to the derivative sum, and the bound is conservative rather than artificially merged. Factors of order zero do not enter Delta. The formula differentiates the regularized numerator, and does not assert separate cancellation of raw Leibniz pieces.

The frame identity is correct:

    (partial_x f_A)_B = -partial_t f_B + n f_B/t

when the output twist is n-2. Only n=0 supplies the complementary geometric derivative with no connection term. The other-chart boundary bound uses the homogeneous source hypothesis and raw-weight degree bound 1747, together with the standard-branch bound max(1668,5248+2)=5250; polynomiality in a single affine frame alone would be insufficient.

## Standard branch domains

The standard-branch regularity assertion is supported by the actual map definitions, not merely by a Laurent support rectangle:

- Every K simplex lies in the coordinate rectangle of its output edge. If both endpoint bits agree, all its vertices have that same bit, so no additional coordinate inversion is introduced.
- Each S staircase intersection is exactly its tensor-cell intersection.
- h sends exponents to A only at e>=0 and to B only at e<0 and e<=n. J selects the specified constant/harmonic states.
- A restricts entries from a containing tensor domain onto the output intersection; R restricts again.

Thus both finite endpoints force exponent >=0, both infinity endpoints force exponent <=n, and mixed endpoints allow either direction. The support rectangle [-1668,5248]^4 then supplies the advertised finite-frame clearing and physical-frame pole bounds for the complete B cochain. This does not certify arbitrary rational leaves obtained by splitting that cochain.

The transpose rules correctly test h at the shifted exponent eta=kappa+unit_i with coefficient kappa_i+1, kill the zero coefficient, use the B constant for a zero-twist prefix, and retain the prefix-C Koszul sign.

## Convention clarifications implemented and verified

1. A full owner is (seed, occurrence, carrier, legal mask, standard tag). Common-cover geometric equality forgets seed/occurrence but retains the standard tag. For arbitrary common-cover cochains, only repeated common vertices force alternation zero. For the actual F=s*F_source, the original first-lift proof gives the stronger rule: repeated source labels (carrier, legal mask) give zero even if their standard tags differ. The new source_F_sort applies that stronger rule, and prism_branch uses it without changing the general common-cochain sorter or merging denominator owners. Equal carriers alone, with different masks, do not imply zero.
2. The original prism is defined on increasing common output tuples and extended alternatingly. The revised proof and recipe state this convention for (3), and prism_branch rejects a raw reversed output edge. If one instead applies the raw two-prism expression directly to reversed edges of an arbitrary cleared cochain, alternation would need an extra argument or closure hypothesis. The universal algebra identity does not by itself supply it.

## Checks executed

After inspecting the code, ran the original 17 abstract tests and then re-inspected the corrected files and reran the revised suite: all 20 tests passed. The revised JSON again exactly matches its generated metadata and recipe. Independently checked exact certificate.json equality with support_metadata()/full_sum_recipe(), all 256 standard-edge endpoint rectangles, and 82 one-coordinate monomial frame controls. Reproduced the source/common repetition distinction with equal (carrier, mask) and unequal standard tags. These are abstract algebra and integer/label checks only; no physical-source polynomial, jet, sample, partition expansion, source adapter, or compiler execution was used.

## Exact accepted conclusion

With the verified convention clarifications incorporated, the artifact proves that the stipulated whole-source clearing identity and fixed quotient/cover premises imply the complete inner solver has a polynomial common-finite numerator with no inserted carrier/legal denominator, and its complementary derivative has conservative per-output-owner orders carrier 15, legal 2, standard 5251 (undifferentiated 14, 1, 5250). The source circuit-to-clearing witness, executable B/partition coefficient realization, global admission, obstruction value, product count and peak-memory certificate remain unproved here.

## Reviewed revised file hashes

- PROOF.md: 03673d6f120cb0b89d6d3887b7ab0bfee6aa33acf2abcc0ddbb116071b159c25
- certificate.py: 57fc3b13f0853a1364d2a5911884fe0d89bd3b287c9913bf2f377f24da0eff26
- certificate.json: cd97c643c479d25dcdbc11297a0989ed4e83511e9784ff908fbe7b2acb21e218
- test_certificate.py: 2ae73e6b16b3a234d47c0b7120c0f5ec1935a1ad01e4ff63154f82e770135fa7
