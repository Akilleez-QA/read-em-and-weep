# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent structural audit of the full coefficient family

## Verdict and exact bytes

The 79-dimensional Kodaira–Spencer injectivity claim in [FULL-COEFFICIENT-FAMILY.md](../COEFFICIENT-FAMILY.md) passes this independent structural audit, conditional on precisely its stated locally free exact-presentation premise and literal first differential. No mathematical correction is required.

This audit binds the following SHA-256 hashes:

    FULL-COEFFICIENT-FAMILY.md: 7d0b36952133976e30a039538238b56cd0e80455d67f2f49e34c113276efdf6e
    PROOF.md: 70e5d13105abe01bc6c88d2c244bd6a8741469c7c2eeedf221bd026605d0b986
    AUDIT.md: e5f6745ecc81ff3b8f0a7df3c655e3b5f858ec33f130ecfade186b6c1b47a7d9

All three bound documents were read in full. The mathematical checks below were made independently from their displayed arguments. This audit does not independently verify the external historical source or exactness assertions summarized in the earlier audit.

## Checks

1. **The complete section space has dimension 16.** On the stated genus-one curve, Riemann–Roch and duality give two sections of O(2O), with basis 1,z. The pole order of z makes the basis basepoint-free also at O. Degree-zero Künneth identifies both section spaces with the corresponding fourfold tensor products. Factorwise pullback is an isomorphism, hence so is q*. Thus W really includes every section of the fixed N², not merely a selected subspace. Surjectivity of q also proves equivalence of generation upstairs and downstairs.

2. **The parameter space and family are global.** The common-zero incidence subscheme on Y×P(W⁵) is closed, and proper projection has closed image. Its complement is precisely the generating locus. The product of four nonzero binary linear forms is nonzero over every geometric residue field, so the original tuple lies in that locus. It follows that U is nonempty, open, smooth, and 79-dimensional. The tautological construction correctly gives the universal quotient line L⊠O_U(1), and after q-pullback the quotient is N²⊠O_U(1). Consequently the stated bundle family exists globally, despite the extra parameter-line factor.

3. **The normalized chart legitimately fixes the presentation terms.** A functional nonzero at v trivializes the parameter-line factor near [v]. Pullback of the assumed bounded locally free complex with sole locally free cohomology is legitimate without flatness of the map: locally that complex splits into its cohomology and contractible complexes. The terms after twisting are exactly 5N⁻¹, 15N, 10N³, 2N⁵. Arbitrary tangent representatives differ by cv; normalization merely selects a representative and creates no missing tangent direction.

4. **Zero class forces a constant strict equation.** For internal degree r in the Hom complex the line-bundle exponent is 2r, with −3≤r≤3. Negative-r terms have their cohomology only in degree four, so their total degree is at least one. The only total-degree-zero entry is (0,0). The first differential out of this entry imposes the chain-map equation; higher outgoing targets have negative cohomological degree, and higher incoming sources have total degree minus one. There are no global degree-minus-one homotopies. This proves the asserted identification of strict chain maps with derived maps. It holds over the dual numbers and is natural under reduction. Thus an identity-reducing bundle trivialization lifts uniquely to an identity-reducing strict map, whose four blocks are constant over the dual numbers. Its first equation is δγ=Pγ−γQ with unrestricted constant P,Q.

5. **The reduction from 80 coefficient directions is valid.** Every entry of γ lies in S=span(v₀,…,v₄). The right side of the strict equation therefore has entries in S. The singleton entry in row 10+i is precisely v_i, so its variation is precisely δv_i. Hence every zero-class coefficient variation satisfies δv_i∈S. Disjoint nonempty squarefree-monomial supports prove that the five v_i are independent. There is consequently a unique matrix B with δv=Bv. This step uses linear subspace membership, not any specialization or evaluation.

6. **The symbolic target kernel is exactly the scalar direction.** The cyclic support descriptions give one occurrence of every (column, variable-label) pair. The other-column support property in every double row excludes cancellation when the singleton-row equations are compared. These equations force Q and B diagonal before any diagonality of P is assumed. Pairwise-disjoint row supports then force P diagonal. The two displayed cyclic differences and their three-step comparison have the stated signs. The resulting annihilating polynomial factors as (1−t)(t²+3t+1). The displayed coefficient identities prove that its greatest common divisor with t⁵−1 is t−1 in characteristic zero. Bézout therefore forces all diagonal entries of B equal. Conversely a common scalar preserves the projective map and gives zero class.

7. **The conclusion has the claimed size and the stated limits.** The affine coefficient tangent has dimension 80 and its kernel is kv. The projective tangent therefore injects with dimension 79. The family parametrizes generating ordered five-tuples for the fixed N² modulo the common scalar; it does not quotient by source automorphisms or vary the polarization in Pic(X). The stated inclusion of target and factorwise projective families is compatible with their tuples remaining in H⁰(Y,L)⁵; previously counted directions must not be added again. This audit does not independently re-audit the numerical overlap theorem in INTERSECTION.md (historical optional overlap calculation, not imported here).

## Conditional scope and evidence boundary

The audit establishes the implication from the specified exact presentation to the 79-dimensional injection at the original tuple. It does not establish the historical contraction/exactness assertion called “A,” does not replace that assertion by the name “HM,” and does not establish that a differently normalized or differently presented HM bundle meets the premise. The literal first differential and the sole locally free degree-zero cohomology hypothesis are both indispensable inputs.

No assertion of injectivity at every parameter point, versality, exact Ext¹ dimension, moduli-chart status, residual response, star admission, or mixed-product nonvanishing follows from this audit. Any source-extension or residual-commutation statement requires its own argument and is outside this audit.

Work was restricted to static reads of the three bound proof documents, formal structural mathematics, document hashing, and writing this separate audit. No actual-source/model execution, numerical matrix construction, rank calculation, polynomial-instance evaluation, point/jet/residual/detector evaluation, external write, merge, upstream action, or local Codex task was performed. Public source links remain available in the audited documents; none was fetched for this audit.
