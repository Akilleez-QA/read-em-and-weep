# Positive-characteristic qualification of Laurent divergence certificates

This note extends the characteristic-zero criterion to arbitrary fields. It gives:

- The full positive-characteristic resonance criterion, rather than ordinary-residue vanishing alone.
- The gcd-based bad-prime set, safe support bounds, and a Bézout refinement.
- Denominator-one completeness with the modified resonance criterion.
- The multiplicity-sensitive logarithmic tangent condition.
- Limits on inferring characteristic-zero statements from modular certificates.

Read [PROOF.md](PROOF.md) for the arguments, hypotheses, and counterexamples. This is a qualification of the characteristic-zero dependency, not a correction to its stated theorem. It concerns ordinary coordinate derivatives of a complete finite Laurent scalar and does not discharge source identification, trace orientation, or geometric comparison premises.

**Review status: NOT independently reviewed.** The independent reviews of the dependency below do not apply to this extension.

## Pinned public sources

Dependency: [PR #79](https://github.com/Akilleez-QA/read-em-and-weep/pull/79), commit `4659e4425c6b5ab6b1899e6af93656ac03ff0862`, `research/hm/null-residue-certificate-route/`.

- [Dependency README](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-residue-certificate-route/README.md).
- [Characteristic-zero divergence proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-residue-certificate-route/original/PROOF.md).
- [Independent finite-bound review of the dependency](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-residue-certificate-route/independent/REVIEW.md).
- [Characteristic-zero logarithmic proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-residue-certificate-route/logarithmic/PROOF.md).
- [Public discussion, PR #1 comment 6253493539](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6253493539). This is provenance, not an independent mathematical review.
- [Stacks Project, tag 0FU8](https://stacks.math.columbia.edu/tag/0FU8), contextual reference for the positive-characteristic de Rham phenomenon; the argument here is coefficientwise and self-contained.

## Synthetic checks and recorded results

`check.py` uses only Python's standard library, invented exponent boxes, and small polynomial identities. The retained [normal output](normal.json) and [optimized output](optimized.json) each report 15,947 checks with status `pass`. These are previously recorded results, not a new execution or an independent review. The checker and both result files are preserved unchanged.

The finite checks are supporting examples and formula checks, not proofs of the general theorems. They contain no source-specific input or production imports.

For reproducibility, the commands are:

    python check.py
    python -O check.py

The general claims rest on the written arguments in PROOF.md, with the explicit review limitation above.
