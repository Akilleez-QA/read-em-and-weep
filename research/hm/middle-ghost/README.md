# The degree-five middle ghost alternative

For the normalized Horrocks–Mumford bundle over C, the degree-five middle Tor multiplicity e is either zero or one. In the nonzero case both middle coefficient spaces are trivial representations of the classical normalizer. The proof also excludes the outer degree-five Tor groups independently of the earlier quintic-relation exclusion.

Read PROOF.md, AUDIT.md and AUDIT-PAIRING.md. The last audit contains an additional full totalization-sign derivation: the residual d3 form is symmetric, not alternating. It does not select a value of e. Both audits are historical mathematical reviews of the source proof identified by their embedded SHA-256; normalization for this edition changes prose about review methods only. These are written arguments, not formal verification certificates.

## Exact mathematical dependencies

- [PR91](https://github.com/Akilleez-QA/read-em-and-weep/pull/91), commit 872aca45943d3758e261a900e5984b981c18b3c4: twist-one vanishing, upstream of the actual low-H1 multiplication theorem.
- [PR136](https://github.com/Akilleez-QA/read-em-and-weep/pull/136), commit 7f258a10cdcc0b86a7ce77aaae2289b5b902cd79: quintic-scalar-propagation/PROOF.md §8, actual nonzero low-H1 multiplication, and the stated cohomological inputs.
- [PR138](https://github.com/Akilleez-QA/read-em-and-weep/pull/138), commit e20ec694f8f51bfc7895ce11813d1d93788ed288: middle-module-relations/PROOF.md §5, minimal-resolution degree bounds and self-duality; apolar-middle-module/PROOF.md supplies the pairing convention.
- [PR140](https://github.com/Akilleez-QA/read-em-and-weep/pull/140), commit d8680b41a0d2dfd6f0990712aed570c1a6b466df: cubic-relation-resolution/PROOF.md supplies the ancillary b∈{0,5,10,15,20} bound; middle-relation-dependency/LINEAR-STRAND-ADDENDUM.md supplies the ancillary d bound displayed in §6. Its earlier c=0 exclusion is compatible but is not an input to the independent c=0 argument here.

The theorem does not depend on twist-two vanishing or higher-twist section computations. Its resolution summary retains previously established necessary bounds; those bounds are not newly proved here. No value of a, b, d or e is selected, and no realizability or algebraicity claim follows. No selected HM/source-instance calculation is used.
