# Independent publication check: actual cubic components and multiplicities

Verdict: PASS for the exact versions below, with their explicit hypotheses and genuinely proved predecessor inputs. Review date: 2026-10-20 UTC.

## Reviewed versions

- INPUTS.md: `65d79e0211f5ee72180b4ed00943bd14b5ad7684b582f9d697b026f330fcfdcb`
- README.md: `ff581728e8fe2d4276232c7af26f3697397b1db052ea4ed0e6644c38c9cdac4f`
- SCOPE-AND-SHARPENING.md: `f6706634a01ee1d9e201b5a8a8412481961ea6d18270d77c959ccc0b854e1b9d`
- applications/constant-rank-kernel-nets/PROOF.md: `cf6f0ceb6634e3feaf1aa5bd2002cc90e50a72ee15a591a984e3a725e3759170`
- applications/exceptional-net-locus-bound/PROOF.md: `695e74e6d9bf3582371024355b56816aad53fed5a701cf2984610c1350ead52d`
- applications/four-kernel-empty-incidence/PROOF.md: `ccdd8631587af64d107a80800d85654a235e7682ee58ac5a7c1686980b6c48a3`
- applications/isotropic-four-kernel-exclusion/PROOF.md: `8ee34553b1b0874d529a37e97379253328c5f27bd10944ec60c0840ba5c86bd3`
- applications/reducible-four-kernel/PROOF.md: `85fa90291b37ea530fb77725d86f8983dcefedff9a42265134607517798d66e8`
- coordinate-component-multiplicities/PROOF.md: `5c9a81f938bf0233393a5735ad92b5ac03d7b286c87457e2ee235a245e31f3be`

## Mathematical and dependency verification

Unit09 verifies rank-one-freeness and the dimension-at-most-four bound for every actual structural kernel, using the canonical operation and structural nonvanishing. Therefore the universal results in units01–03 apply to this actual bundle map. Their hypotheses are not discharged by public abstract cofactor geometry alone.

The extracted application sections retain all conclusions of the earlier full source proofs while importing, rather than duplicating, their universal parts. The fixed three-dimensional singular-net hypotheses and notation are explicit. Its normalized oriented cover is the smooth irreducible affine quadric q=2, and the three nonzero eigenline bundles give a smooth irreducible five-dimensional frame scheme. The four-dimensional existence corollary is preserved: the isotropic exclusion removes q=0, while the determinant-factor argument excludes an empty spectral incidence when q is nonzero. This proves nonempty pure five-dimensional fixed-kernel frame fibers without a reducedness assertion in general.

The reducible-kernel application explicitly imports its normal form, two smooth components, and transverse intersection curve. Finite etale orientation and smooth torus factors preserve its reduced double-crossing local structure, with four-dimensional smooth singular locus. It does not infer an oriented-cover component count or existence of that actual kernel stratum.

The singular-net base bound of four excludes the former net branch of independent ten-dimensional components. The image-line empty-incidence Chern argument bounds the whole four-kernel stratum by four, excluding the other branch. Together with the lower-kernel estimates this gives independent-triple dimension at most nine. The dependent classification leaves exactly the three coordinate ten-planes as top-dimensional components. The AP-plane existence theorem supplies an independent zero and hence at least one smaller component. The former exact frontier criteria remain logically correct and are now settled negatively; SCOPE-AND-SHARPENING distinguishes these successive conclusions and preserves the remaining unknown smaller geometry.

For each omitted slot, the global zero scheme is the kernel scheme of the bilinear fixed-pair bundle map. Over its injectivity open a local left inverse equates the cubic ideal to that coordinate-plane ideal. The independent incidence bound gives the codimension-at-least-two bad-pair locus. The dependent-pair calculation treats nonzero proportional and zero-input pairs separately. Along each coordinate plane, tangent dimension is ten plus kernel dimension, giving the exact rank-drop singularity criterion. The stated Fitting-ideal restriction is valid without misidentifying it with a universal singular subscheme on this non-equidimensional scheme. The algebraic kernel line proves rank drop equals crossing another component set-theoretically.

The generic local rings of the three top components are fields, so all three have multiplicity one. Their top-dimensional projective degrees sum to three; lower-dimensional or embedded components do not change that leading term. The standard-graded Hilbert-function summation gives Hilbert–Samuel multiplicity three at the origin. No global reducedness, Cohen–Macaulayness, or multiplicity assertion about smaller components follows. The separate fixed-two-plane double structure and degree-27 necessary cycle constraint are not confused with these global conclusions.

The genuine dependency closure is units01–09 with pairing foundation00 and P01–P06 including P05B. No speculative unreviewed Porteous continuation is needed. Availability and immutable public pinning of the named predecessors remain publication requirements. Historical receipts concern original manuscripts, not these normalized bytes. Subsequent edits require renewed review; staging alone is not publication. This check does not establish novelty.

## Evidence boundary

Only static proof reads, universal mathematical reasoning, and file checksums were used. No actual HM/source/model matrix, product, rank, selected input, point, jet, residue, detector, or Massey value was evaluated. No actual physical residual was identified or decided.
