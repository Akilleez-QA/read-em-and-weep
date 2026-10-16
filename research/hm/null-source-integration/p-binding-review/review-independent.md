# PB01 independent review: actual P constructor denotation

## Disposition

Accept the coefficient-free semantic binding at PR87 commit `b429d19f6b3fd4f4fe3968a37a848ec980a574a2`, for both ordered coordinate pairs and the stated increasing target-source domain. No correction is required in the reviewed PB01 files. This accepts the denotation of the pinned INS constructor and physical Catalog under the explicit accepted CLR/contraction/PH premises. It does not admit physical coefficient execution or authenticate an unrelated P callback.

Reviewed implementation and proof:

- [PB01 implementation](https://github.com/Akilleez-QA/read-em-and-weep/blob/b429d19f6b3fd4f4fe3968a37a848ec980a574a2/research/codex-swarm/source-faithful-P/p_binding.py), Git blob `b0a6f1712bfb12056fefe2b40a737327fa0f3565`.
- [PB01 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/b429d19f6b3fd4f4fe3968a37a848ec980a574a2/research/codex-swarm/source-faithful-P/PROOF.md), Git blob `5c3654d4942c7796607ac5db0a16675d3ca852c8`.
- [Immutable dependency manifest](https://github.com/Akilleez-QA/read-em-and-weep/blob/b429d19f6b3fd4f4fe3968a37a848ec980a574a2/research/codex-swarm/source-faithful-P/source-pins.json), SHA256 `0ac211d49398b2d64b1dac25f19e304d473890aa8d74188eca76a7de5f371fab`.

## Mathematical checks

1. **Primitive normalization is source-specific.** The literal primary denominator is -H; multiplying the actual entry N/(-H) by H squared gives -HN. For auxiliary5, H=v1*v3*v4 and the stored denominator is -v1 squared*v3*v4; cancellation gives -v3*v4*N. These are exactly the multipliers in the pinned INS Catalog, not arbitrary primitive declarations. Substitution sends every stored v exponent to the corresponding elementary-symmetric polynomial, retaining its coefficient.

2. **The auxiliary homogeneous factor is not dropped.** The actual homogeneous auxiliary H is v0*v1*v3*v4 of degree4. Its degree4 stored denominator homogenizes to -v1 squared*v3*v4, equivalently -v1*H/v0, not the degree5 expression -v1*H. PH supplies the weighted identity H squared*X_hom=-v3*v4*hom_(6+w)(N); the total degree is 8+w. Primary normalization has degree10+w. PB records the correct per-entry I-column/P-row weights and bounds; its literal exponent inspection agrees with the accepted primitive premise.

3. **The graph identity is an induction, not a hash inference.** The 153-node graph/root152 matches the CLR artifact. Every opcode has the same entrywise or ordered-matrix denotation as the pinned INS interpreter: literal transpose, trace, exact rational scale, scalar broadcast, left-to-right multiplication, nonnegative powers and partials after elementary substitution. The physical Q numerator and binary gerbe numerator remain separate. Applying these rules to the CLR rational construction yields the same fully padded P. The accepted CLR rational/contraction identity is the substantive input to P=(product C)F; byte hashes select that input and implementation but do not prove it.

4. **Both pairs retain target order.** Pair23 changes only raw coordinate axes, including all legal/mask/derivative axes. Primitive slots, matrix products and constants stay fixed. The implementation agrees with INS pair_nodes. It never sorts the raw inverse image or identifies differently ordered nonlinear cochains. This is precisely the domain allowed by the complementary-pair theorem.

5. **Owner-specific degrees have a proof dependency.** PB returns D_i=sum_owner[14*d_owner+pair_indicator*degree(ell_owner,i)]-2*pair_indicator. This is the actual homogeneous target degree, not a claim that the top coefficient is occupied. CLR's critical cancellation proves the finite bound, and PH derives the physical source transition independently before clearing. Consequently the chart exponent D_i-a_i is nonnegative and identifies the actual homogeneous P. Merely checking graph shape or returning D_i would not establish this result without those named premises. PB's proof states this distinction correctly.

6. **The domain preserves ownership.** Owners must have one seed, distinct occurrences and strictly increasing common source keys. Different standard tags at equal physical labels remain admissible; the particular pulled-back source then has repeated-source zero while all clearing occurrences are retained. Output metadata uses fresh copies. Physical coefficient and alternating-coefficient methods refuse before argument inspection, including malformed and negative demands. This is an ordinary API contract, not a hostile-Python security boundary.

## Independent evidence and replay

All 15 manifest dependencies were independently retrieved at their immutable revisions and matched by SHA256 and Git blob, including the original 153-node artifact, model, source definitions, contraction receipt, PH proof and complementary-pair theorem. No historical physical checker was run.

Six independent tests in `test_independent.py` pass in normal and optimized Python. They cover an independently implemented matrix-shape pass over the exact graph; both raw-pair mappings; 1,728 owner/pair degree cases using integer metadata; primitive entry-degree records; source/common repeat distinctions; occurrence/seed/order guards; deep-copy isolation; malformed opcode rejection; and unconditional physical refusals. They do not construct any actual Catalog polynomial, evaluate a coefficient, or enumerate actual fibers.

For this review, repository bytes were obtained through the contents API rather than a Git checkout. The replay supplied those exact digest-verified bytes at the `git show` read boundary; the unchanged constructor still performed its own full SHA256/Git-blob checks and local dependency comparisons. No semantic method, source graph, model data, proof flag or coefficient API was patched. This validates the mathematical/metadata path, not the availability of historical Git objects in a particular checkout.

To reproduce using a checkout containing the pinned history, place the companion test in `research/codex-swarm/source-faithful-P/`, then run:

    python -B research/codex-swarm/source-faithful-P/test_independent.py -v
    python -BO research/codex-swarm/source-faithful-P/test_independent.py -v

## Remaining boundaries

- Physical P coefficients and their executor remain unavailable; this is a denotation certificate.
- Actual complete fibers, Qhat inputs and their partition/source-domain application remain separate.
- A consumer must use this exact binding in the same source order, pair, owners and domain; unrelated callbacks acquire no identity from it.
- Whole-standard-target extension, harmonic/primitive application, complete outer Rsharp/J0–J3 identity and closure must be established by their respective artifacts.
- Historical source-order comparison, detector values, obstruction decisions and physical operation/live-storage admission do not follow.

No physical polynomial arithmetic, actual source coefficient evaluation, actual fiber enumeration or external publication was performed for this review.
