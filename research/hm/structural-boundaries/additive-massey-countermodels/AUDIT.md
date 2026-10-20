# Formal audit

The construction in PROOF.md is algebraically valid, conditional on its explicitly imported geometric module dimensions and upper-weight vanishing. No actual HM matrices or Massey values were evaluated.

- The multiplication is associative and S-balanced, the differential satisfies the graded derivation identity, and the projection killing P and J is an S-DGA quasi-isomorphism.
- The decreasing filtration is multiplicative, and its only nonzero differential is the indicated d5. In weight 2, the source has dimension 10, target dimension 30, and cokernel dimension 20.
- For an arbitrary graded S-module M supported in weights at most 1, the top-weight identity (Lambda^2_S M)_2 = Lambda^2_k M_1 is valid. A balancing relation using a polynomial of strictly negative weight cannot have total weight 2: its two unmultiplied module factors would need weights summing to more than 2. Thus replacing the Euler example by the actual H1 coordinate module does not invalidate the dimension argument.
- The actual H2 coordinate module may likewise be used as T with its full S-action. These substitutions preserve coordinate-module structures, not the actual cohomological products or derived-endomorphism realization.
- All degree-one triple Massey sets are exactly {0}: the selected primitives multiply to zero, and the entire degree-one product indeterminacy is zero in cohomology. The word canonical here correctly describes the singleton Massey value; it does not assert a canonical choice of transferred higher operations.
- The smooth formal MC family and the stated graded anti-involution/trace identities hold. The anti-involution must retain its displayed Koszul sign.
- The example is bounded in cohomological degree and filtration length; it need not be bounded in internal weight or finite-dimensional as a vector space. Its stated exclusion is therefore correctly limited to the listed abstract structures.

The imported HM facts and references to the separate transgression proof are assumptions/background for this formal audit, rather than independently re-proved geometric assertions. No substantive flaw was found in the final text.

## Additional comparison limits

The model has d1=0, so it does not reproduce the actual initial Hom-complex E1 differential. Its asserted comparison is only with the selected global-cycle/transgression-stage data, not the entire actual spectral sequence. The actual-module substitution preserves the S-actions on H1 and H2 only; it does not preserve actual degree-zero endomorphism cohomology, other cohomological degrees, or a sheaf realization. These limitations should remain explicit whenever the countermodel is summarized.
