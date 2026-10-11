# Readme

This repository contains mathematical manuscripts and supporting proof artifacts produced by an internal OpenAI model. 

As part of model development, we evaluate our models on open research problems. We expanded these evaluations after performance on our existing mathematical evaluations saturated. Some outputs build upon earlier results produced by the models.

This collection includes results at different stages of verification. Not all have accompanying Lean formalizations. We will continue to update this repository with Lean formalizations as we obtain them. 

Some of the unformalized results could have issues. We will endeavor to fix any such issues quickly.
We are also exploring community-hosted repositories for these materials. 

## Navigating the collection

The current catalogue contains 719 manuscripts organized into 372 families. A family groups related papers, which may include a principal result, companion arguments, consequences, or alternative proofs. Each family is classified by mathematical discipline.

- Start with the [overview](overview.pdf) for descriptions of the families.
- Use the [manuscript map](CONTENTS.md) to find individual papers and their supporting materials.
- The [`preprints/`](preprints/) directory contains PDFs, source files, and manuscript-specific citation and build instructions.
- The [Lean library](lean/README.md) and [formalization catalogue](lean/formalization.yaml) describe the available formal proofs, their associated papers, and verification configurations. See the [Comparator instructions](lean/ComparatorChallenges/README.md) for additional checking instructions. The repository has ~42% top-line results formalized.
- Updates to the repo are described in the [history](history.md).
- The Horrocks–Mumford and carrier gate ladder is in [`research/hsd/README.md`](research/hsd/README.md). For the fixed chosen carrier, the independent checks (PR #1, comments [6104798062](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6104798062) and [6104803214](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6104803214), the latter a SymPy Groebner-basis reproduction of the same displayed module) establish the displayed finite module and the conditional Ext-to-central-defect bridge, with \(\operatorname{length}_B(Q)=12\) for that module. They share a source identification, so the geometric attribution is not independently certified twice. The total-resolution and source-identification artifacts are still requested, and the geometric exclusion of the global vector-bundle extension (G2) for this carrier is conditional on those artifacts. The formal continuation (G1) has status formal construction reported; immutable artifact review pending. Other formal-lift and carrier choices stay **OPEN**. As of the earlier checkpoint, before 6104798062, that length was uncomputed. The original theorem, the central conditions for other carriers, and the Horrocks–Mumford second-order obstruction computation are not settled by this result. A Horrocks–Mumford Frobenius or Cartier fixture test runs in characteristic \(3\), or in an extension of \(\mathbf{F}_3\) with the coefficient Frobenius handled. A large prime of another characteristic cannot validate those identities. The current fixtures are formal over \(\mathbf{F}_3\), and no carry defect is reported. arXiv:2502.03415v2 contains Lemma 8.3.4 (kernel equality and surjectivity) and Remark 8.3.5 (kernel equality only; injectivity on the image of the obstruction map). The same statements are Lemma 8.2.4 and Remark 8.2.5 in v1, where (8.3.4) and (8.3.5) are displayed equations. The claim that the v2 numbers are absent is withdrawn. [PR #67](https://github.com/Akilleez-QA/read-em-and-weep/pull/67) withdraws the claim of a single surviving strategy.

### Reasoning summaries

We are also releasing abridged summaries of the model's reasoning, covering the following results:

| Family | Subject |
|---|---|
| 007 | [Ordinary two-point correlations of multiplicative functions](reasoning_traces/ordinary-two-point-correlations.pdf) |
| 017 | [The irrationality exponent of π](reasoning_traces/irrationality-exponent-of-pi.pdf) |
| 087 | [Symmetric and general Mahler conjectures](reasoning_traces/symmetric-and-general-mahler-conjectures.pdf) |
| 102 | [Ordinary NP-hardness at the basic semidefinite threshold](reasoning_traces/basic-semidefinite-threshold-np-hardness.pdf) |
| 159 | [Quasipolynomial bounds for arithmetic progressions](reasoning_traces/quasipolynomial-arithmetic-progressions.pdf) |
| 197 | [Kaplansky's direct-finiteness conjecture in characteristic two](reasoning_traces/kaplansky-direct-finiteness-characteristic-two.pdf) |
| 221 | [The Mézard–Parisi formula for diluted spin glasses](reasoning_traces/mezard-parisi-formula.pdf) |
| 271 | [Spontaneous magnetization in the quantum Heisenberg ferromagnet](reasoning_traces/spontaneous-magnetization-quantum-heisenberg-ferromagnet.pdf) |
| 287 | [Isomorphism of free group factors](reasoning_traces/free-group-factor-isomorphism.pdf) |
| 362 | [The three-dimensional relativistic Vlasov–Maxwell system](reasoning_traces/relativistic-vlasov-maxwell.pdf) |


## How the results were produced

The vast majority of results were obtained with the same procedure using an unreleased internal OpenAI model. On average, each result used three hours of ChatGPT Pro thinking compute with that model. Over the course of the evaluation, the model was posed approximately 4,000 problems. Aggregating the output into result families and manuscripts and requiring an appropriate level of significance led to the catalog outlined above.

Exceptions to this fixed procedure include work on a zero-free region for the Riemann zeta function and proof of the Hodge Conjecture for CM abelian varieties. Additionally, the writeup for the Re(s) > 11/12 zero-free region for the Riemann zeta function was human edited for readability. 


## Versions and citations

We will preserve the public release history of this collection. Corrections and revisions will be recorded as new versions, with previously released versions remaining accessible. 

To cite the individual manuscript, use the BibTeX block in its directory. 
