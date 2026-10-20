# Independent publication check: repeated-input schemes and ambient blowup

Verdict: PASS for the exact versions below, with the explicit hypotheses and genuinely proved predecessor inputs. Review date: 2026-10-20 UTC.

## Reviewed versions

- INPUTS.md: `d1ccc23d492cd6fd00c6f8168979eed09a059a89924112a5533485232a466940`
- README.md: `4130a6969effe1802bc1b2e02cc6809c3801902bf0ce4bc45ac18e5353c940c3`
- extension-locus-singularity/PROOF.md: `4b40a8437dc0aac2058002cfc63ea6de3a26724b8c20b719d514daf62a93a438`
- repeated-extension-slice/PROOF.md: `9cb8f93ebb114e6647a016793c6aba1f32fc108250467060e9fbc440d0437dcd`
- repeated-slice-blowup/PROOF.md: `533120980ce1a875dd23c436339aec55039dc107c33590f99be80680c7d4acf3`

## Mathematical and dependency verification

The singularity theorem is explicitly conditional on the nonzero cubic scalar and surjective linearization, discharged by unit05. Twenty independent homogeneous cubics give twenty minimal generators at the origin; this is not surjectivity of the polynomial map to the target. Unit04 supplies the exact affine-test-scheme filtered functor.

For repeated inputs, universal nonvanishing induces a constant-rank subbundle map on projective direction space. Local left inverses identify the restricted zero ideal scheme-theoretically with the tautological proportionality ideal. Saturation gives the radical determinantal support, while the original cubic ideal retains nilpotents on the zero-axis stratum. The proof does not silently replace that scheme by its reduction, and its ideal statements commute with arbitrary base change.

On the ambient blowup, the total transform factors as the exceptional equation squared times the weak-transform ideal. The strict transform is the stated rank-two vector bundle over projective four-space and resolves the reduced support. The total inverse image retains the doubled exceptional component. The intersection calculation excludes additional embedded components on the blowup. The proper birational contraction and canonical-bundle calculation are consistent. Its small-exceptional-locus assertion is birational terminology, not the stronger intersection-cohomology smallness/semismallness condition.

The actual universal filtered family pulls back where the cubic obstruction vanishes; resolving reduced support is not a resolution of the original nonreduced moduli functor. Only units04–05 and their genuine prerequisites are needed logically; the later explicit weight basis is contextual. No new source-instance computation is used.

Availability and immutable public pinning of the named predecessors remain publication requirements. Historical receipts describe their original manuscripts, not these normalized bytes. Subsequent edits require renewed review; staging alone is not publication. This check does not establish novelty.

## Evidence boundary

The review used static proof reads, universal mathematical reasoning, and file checksums. No actual HM/source/model matrix, product, rank, selected input, point, jet, residue, detector, or Massey value was evaluated. No actual physical residual was identified or decided.
