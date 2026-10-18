# Independent self-contained static review

## Verdict

The structural proof of C is sound for the inspected immutable model. The historical evidence for A is precisely scoped as an imported exact-computation report, not an independently replayed proof. No mathematical error was found in those two claims. The original report's conditional use of the earlier B proof and contraction theorem is not independently reviewed here.

## Provenance of this review

An earlier evidence-retrieval worker collected the historical public sources and their provenance records. This reviewer independently inspected and validated the resulting local files; it did not repeat the network retrieval or independently authenticate the remote repository. The public bundle is self-contained for its stated static checks. Independence here describes local source inspection and static revalidation, not a separate replay of A or an independently attested historical execution.

## What was independently checked

- Read REPORT.md, check_static.py, the historical checker and package verifier as inert text, the receipt and manifest, and selected literal model fields.
- Ran the original standalone check_static.py under ordinary Python and Python -O. Both passed, produced byte-identical outputs, and reported 20 paired and 10 zero block columns. Those original-checker review outputs are retained in the original evidence package. The portable checker outputs included here are static-report.json and static-report-O.json.
- Verified every entry in the original SHA256SUMS. All passed. Original evidence files were not edited.
- Inspected all six carrier dimensions: I is 15 by 2, P is 2 by 15, H0 is 5 by 15, H1 is 15 by 10. Pivots are 0,1,2,3,4,0.
- Confirmed the actual directory metadata includes matching Git blob entries for model, receipt and producer checker. The verifier is bound by the manifest, not by those three directory listings.
- No historical or production source was imported or executed. No actual polynomial products, rational-function reductions, model evaluations, numerical evaluations, or network retrievals were performed in this independent review.

## C: proof and interpretation

Each of the two rows of ev is (v0,v1,v2,v3,v4) on its own five-row block and zero on the other block. Each nonzero block column of delta has exactly two singleton terms, in rows r<s, with values epsilon v_s and -epsilon v_r. Its contraction is epsilon(v_r v_s-v_s v_r), which is zero in a commutative ring. Empty block columns also contract to zero. This symbolic argument is a universal algebraic identity, not multiplication of the model's polynomial records.

The inspected data has 20 such nonzero paired block columns and 10 empty block columns. All actual delta entries are lists. The original checker verifies the full ev literal pattern and traverses all 30 block columns. The reported pair map is consistent with its output.

The constant four-exponent token is 1 under the finite decoder, so v0=1. Under degree-1 homogenization it becomes v0, while the four coordinate tokens become v1 through v4. Thus the same proof works in both interpretations without localization. Shared model-level ev and delta mean that this C identity is common to all six carriers. Any subsequent rational formulas still require their own denominators to be invertible.

## A: scope and trust boundary

The historical checker iterates all model charts and checks every entry of I P - Id15 + gamma H0 + H1 delta, raising on any nonzero SymPy-cancelled entry. Six 15-by-15 matrices explain the reported 1350 E_identity checks. The complete receipt claims 3090 exact scalar checks overall. The producer's formulas specialize termwise at v0=1 to the finite numerator/denominator representation on its localization. These source-level facts support the report's identification and scope of A.

Manifest hashes and the compact-model hash bind the inspected source, model and receipt bytes. They do not establish successful historical execution, correctness of SymPy or the producer, or the truth of a fabricated receipt. The report explicitly makes these limits clear. Its wording that the 'receipt's producer and scope have now been authenticated together' should be read narrowly as identification and binding of source bytes, never authentication of execution. The portable README uses the narrower wording.

No reduction witnesses or independent execution attestation were recovered or validated by this review. A is not independently replayed. C and delta gamma must not be inferred merely from the receipt's list of contraction checks.

## Nonblocking checker limitations

1. The original checker has an absolute external path for the pinned model. It is not self-contained or portable.
2. Its directory loop validates matching entries when present but does not require that every expected entry appears exactly once. Empty or incomplete directory metadata could silently skip that additional check. This is a robustness gap, not a failed binding on the actual reviewed inputs: the expected entries are present, and all four principal files independently match the manifest.
3. Its docstring says 'JSON schemas', but the checks are selected shapes and literal patterns rather than complete schema validation. It does not explicitly reject every false-valued non-list delta entry or every numeric JSON type coercion. The actual hash-bound inputs have the intended literal lists and coefficients.
4. The original checker reports pair/zero counts rather than explicitly requiring 20 and 10. The verified input produces those exact counts.
5. The script trusts its supplied manifest and metadata rather than a fixed external trust anchor. SHA256SUMS was checked separately. Hash checks are integrity/source-consistency checks, not mathematical proofs or historical attestation.

None of these limitations invalidates the algebraic C proof for the actual pinned bytes. They should prevent treating this small checker as a general schema validator or comprehensive adversarial certificate verifier.

## Portable unpublished bundle

This public bundle contains a portable checker, a fresh public README, provenance coordinates, the historical model and pinned-model copies, the original manifest and receipt, and the two inert historical source files. No raw connector-directory responses were copied. Input bytes were preserved, with fixed SHA256 pins in the checker. The checker uses relative paths, checks selected carrier dimensions, requires list-valued delta entries and the exact 20/10 count, and leaves A_replayed false.

The portable checker passed in normal and -O modes from a different working directory; outputs are byte-identical. No external publication, repository write, upload, or sharing was performed. The bundle's source coordinates inherit the original package's provenance and have not been independently re-fetched. A modified entire bundle can replace its own hash pins; the hashes are not signatures.
