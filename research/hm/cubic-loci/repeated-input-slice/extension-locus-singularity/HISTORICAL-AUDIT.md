# Historical review receipt

This review concerns its original manuscript version, not the normalized publication bytes. It is not a final publication-scope approval.

# Independent audit of the conditional singularity lemma

## Verdict and reviewed artifact

PASS, conditional on the explicitly imported representation theorem and surjectivity of the linearized trilinear map, and on lambda being nonzero. The persisted proof agrees with the independent formal commutative-algebra review. No mathematical correction is required.

Reviewed file: the extension locus singularity manuscript

SHA-256 of the exact reviewed bytes:

    f6ca6479b329db05a5190f671fdf0bcc43705b6b0fc948538ec4945ca4c630ae

The hash was independently computed from the persisted file and matches the expected hash. Review date: 2026-10-18 UTC.

## Scope and verification

This audit checks the formal algebraic implication from the hypotheses in the reviewed proof. It does not independently re-audit the imported filtered-extension representation theorem or establish linearized surjectivity for an actual instance. It does not establish the nonvanishing of lambda or incorporate any separate pending nonvanishing theorem.

The following steps are valid:

1. Dualizing the surjective linear map gives twenty independent multidegree (1,1,1) forms, using three independently labeled input copies.
2. Since the ideal is generated in degree three, its quotient by the irrelevant ideal times itself is its degree-three generating space. Localization preserves this residue-field vector space, so the twenty generators remain minimal locally.
3. Containment in the cube of the maximal ideal gives the stated canonical quotients modulo its second and third powers and tangent dimension fifteen.
4. Containment in each coordinate-slot ideal gives the scheme-theoretic coordinate ten-planes. Their local rings give the local lower dimension bound as well as the global one.
5. Nonvanishing of the ideal in the polynomial domain and its localization gives the upper dimension bound fourteen. The prime-chain argument is valid both locally and globally. Containment in a height-five coordinate prime gives the upper height bound five; nonvanishing gives the positive lower bound.
6. Embedding dimension fifteen and dimension at most fourteen prove singularity. The minimal generator count twenty exceeds the ideal height, ruling out generation by a regular sequence.
7. The regular-ambient criterion identifies this failure with intrinsic failure of the local-complete-intersection property. Both cited primary-source statements were checked: [Stacks Project, Lemma 23.8.3](https://stacks.math.columbia.edu/tag/09Q1) and [Stacks Project, Lemma 10.135.4](https://stacks.math.columbia.edu/tag/00SC).
8. Multiplication by a nonzero scalar leaves the ideal literally unchanged.

## Important qualifications

- Surjectivity here concerns the linear map from the tensor product. Surjectivity of the associated polynomial map from the threefold direct product is neither assumed nor inferred.
- The conclusions depend on nonvanishing together with the absence of linear equations; properness of an ideal alone would not imply singularity.
- The precise formal-neighborhood assertions concern maximal-ideal powers two and three. The proof explicitly fixes its infinitesimal-neighborhood numbering convention and makes no assertion about equality modulo the fourth power.
- The proof provides bounds, not an exact dimension, and makes no claim about radicalness, reducedness, or the complete list of components.
- The conclusion is about the conditional scheme represented by the imported theorem. It is not a verification of that theorem or of an actual model.

