# Independent review of the exact ten-source coverage theorem

## Verdict and version binding

**PASS. No missing original source, scope mismatch, or unresolved dependency was found.** Under the pinned original rank-three-frontier hypotheses and the cited source theorems, the complete stable label **G3.11.ad509d55173f**, original **source_index 113**, is excluded. This is a whole-label coverage result, not a current global frontier or necessary-pair recount.

Review date: 2026-10-23 UTC. This verdict binds to the final files with these SHA256 hashes:

- `PROOF.md`: `8597b61030fec7dde2e8adc6841110d65554d145f0a0f8a6cc3a32adc7aa0162`.
- `coverage.json`: `45548a94f6b36d6ab2e599d7676e568be85f2bfbcac2c98d37eb34de11b46fd9`.
- `verify.py`: `10b6cbd74c59ead7e016fac2c9ea02b6b58850d788da9a6f91543a7b14de02e7`.
- `characters.py`: `25d2c28c294298624ee50ce73b2a55422913f7e78b4817c7cb6e813e5004f1fc`.
- `REPRODUCE.md`: `a9f6fa60fbf631cc421d6a10d74d623b86bc0f138671a5b5a6bcd9d3fcd913dd`.
- `source-proof-pins.json`: `5d4c48b22022606a9fe8cb4590f9ecf1f12e5aa90383e91f9f9b8c927c79e741`.

The additional independent check, `review_independent.py`, has SHA256 `dd6def3aced02694772054d8785464cf5c6a9372cc6d3a186248c47055ad8936`. It and the supplied verifier both passed. The independent check requires the original four inputs and the seven exact theorem audit copies; the supplied verifier does not require those theorem copies. REPRODUCE.md specifies how to obtain the additional inputs and run the independent check. No publication was performed by this reviewer.

## 1. Original universe and decoder

I independently read the original catalogs, splitting theorem and strict-top lemma. Their local Git blob hashes agree with the four hashes stated in Section 1 of the proof. I also checked those blob identities through GitHub at the exact original commit `db51525015bb7c5e825833d550d08dedf6f6ea96`.

The stable label occurs exactly once and maps to source_index 113. Both catalog records have A_q=O(-10)+O(2)+O(16), B_q=O(-18)+O(-4)+O(8), and determinant defect zero. The original compatible_E_types array, not a filtered survivor list, is exactly:

1. ff: (0,0,0,0,0,2,0,1).
2. ef: (0,0,0,0,1,1,0,1).
3. ee: (0,0,0,0,2,0,0,1).
4. cf: (0,0,1,0,0,1,0,1).
5. ce: (0,0,1,0,1,0,0,1).
6. cc: (0,0,2,0,0,0,0,1).
7. bf: (0,1,0,0,0,1,0,1).
8. be: (0,1,0,0,1,0,0,1).
9. bc: (0,1,1,0,0,0,0,1).
10. bb: (0,2,0,0,0,0,0,1).

This agrees with both the written proof and manifest, in original order, with no duplicate or omission. It is also exactly the ten unordered two-letter choices from b,c,e,f, with a=d=g=0 and h=1. Applying the original eight-block decoder gives rank 17 and degree -54 in every row, and the source bundles asserted in the cited theorems. The conclusion uses necessity of the original list, not realizability of any entry.

## 2. Direct exclusions

The original decoder gives the top coefficient

    R2=(c+g+h-1)V+(d+e+g+h)P+(f+g)D.

The actual strict-top lemma applies because E is saturated in the constant ambient bundle and every splitting degree is at most -2. It gives H0(E^-(2))=0, so the original quotient map injects H0(E(2))=R2 into H0(A_q(2)). The negative endpoint contributes no sections, and

    H0(A_q(2))=Sym4 W+Sym18 W=A+V+2P+2D.

I independently checked this decomposition using the five even A5 characters and the recurrence Sym(2n+2)=(Sym2-1)Sym(2n)-Sym(2n-2), rather than importing the supplied binary-character implementation. For ee the source is 3P; for cc it is 2V+P. Semisimplicity makes the respective P and V multiplicity excesses impossible. These arguments exclude the entire two source strata and require no high-line or divisor-branch assumption.

## 3. Immutable theorem scope and dependency audit

I independently retrieved the six distinct source-theorem files and PR861 at their exact manifest/proof commits. For every file, the calculated Git blob matched the GitHub-reported blob, and its SHA256 matched the final source-proof-pins.json record. The supplied theorem copies initially had one extra trailing newline; they were normalized to the exact retrieved bytes before this hash-bound audit. No mathematical text was changed.

- **ff, PR848:** its statement and conclusion exclude the entire source113 tuple. The unresolved neighboring source127 branch is explicitly separate and is not imported into this coverage.
- **ef, ce, be, PR846:** its statement lists these three exact source113 tuples. Sections 3, 5 and 4 respectively give whole-source exclusions, including the relevant internal-image alternatives. Its other source125/source127 results are not counted here.
- **cf, PR868 plus PR861:** PR861 at `7b5b3371a82cb92f46ea60895e45617d0891a5b0` excludes the basepoint-free branch, forces the degree-twelve branch, and proves the actual constant nine-space and both exact intersections used by PR868. PR868 at `fb398486839583f8fbd561d6dfaa6ab7b9d3ad67` explicitly imports those conclusions and excludes the remaining divisor-twelve branch. Its conclusion is therefore a whole-source exclusion only in this stated combination. The final coverage proof supplies the dependency's exact URL; it does not miscount PR861 alone as a source cut or assume saturation that PR861 left unproved.
- **bc, PR874:** the exact tuple and original A/B endpoints match. Its statement and conclusion exclude both common-divisor branches of this source, not merely the related cf source.
- **bb, PR877:** the exact tuple and original endpoints match. The source theorem excludes the divisor branch and all five basepoint-free kernel branches, not a conditional subset.
- **bf, PR881:** the immutable file at `4234903e84705791da6772ef85085509bd08ef2d` has Git blob `207831458536fcb06afd1a58c391fccb43830df6` and SHA256 `f900fa54aa5ad18adc94bd7552b94891d77ccf1c5797af05414dbd8b851b4f63`. This is exactly the separately independently reviewed and root-reviewed proof, not an earlier draft. Its statement and final conclusion exclude the entire source113 bf edge, including the divisor branch and all five kernel alternatives.

Thus the eight source-cut rows are precisely ff, ef, cf, ce, bf, be, bc, bb. PR846 supplies three distinct rows, not three copies of one edge. The seven theorem-byte records consist of six distinct whole-source documents plus the essential PR861 dependency.

## 4. Conclusion and limits

Every original necessary source for this label has an applicable exclusion. An actual instance would have one of the ten types and would contradict its corresponding direct multiplicity argument or cited source theorem. This proves the coverage implication asserted in the final PROOF.md.

This independent review verifies the assembly, direct exclusions, exact source interfaces and theorem-byte identities. It uses the cited geometric source theorems as lemmas rather than claiming a new independent reconstruction of every underlying HM argument. The check scripts corroborate finite arithmetic, hashes and set equality; they do not replace the written geometric proofs. No selected actual coefficients, parameters, points, derivative values, instance matrices, instance ranks, models, scans, large computation, stronger global conclusion or present global count was used or produced.
