# Independent review: shared-D compatibility

Verdict: PASS, conditional on the explicitly retained actual-geometric hypotheses. I found no mathematical gap in the complete new argument.

Reviewed file: PROOF.md (8,801 bytes).
Exact reviewed SHA256: f2e5b5d8bdb0f8a156aaf38695042f204b4d3cffd1a40a4a28870bed2ef13793.

## Source authentication and review scope

I read the complete proof, all three complete retained source proofs, INPUTS.json, and SOURCE-FETCHES.json. Independently of the producer's fetches, I used GitHub's read-only fetch_file tool for each exact repository/commit/path in INPUTS.json. I recomputed UTF-8 byte lengths, SHA256, and Git blob SHA1 using the actual Git preimage `blob <length>\0<bytes>`. All fresh contents equal the retained files and producer responses byte for byte; all recomputed blob hashes equal GitHub's returned blob hashes.

The full producer and independent connector responses are retained in local audit material but omitted from the publication slice to avoid duplicate source texts. The publication retains the complete source texts once in inputs/, their immutable manifest in INPUTS.json, and compact independent authentication metadata in INDEPENDENT-REVIEW-SOURCE-AUTHENTICITY.json. These published texts and metadata suffice for offline byte-length, SHA256, and Git blob identity checks; live repository authenticity was independently checked as described above. The transitive actual-geometric premises remain assumptions as the proof expressly states; this review does not silently re-prove or broaden them.

## Mathematical findings

1. The actual-subbundle bridge is valid. Duality for the nested saturated actual subbundles M inside S0 gives precisely
   0 -> E0 -> ann(M) -> O(-6) -> 0.
   The indicated extension group vanishes. Equivariant splitting by averaging is legitimate. More importantly, every slope at least -4 maps trivially to the actual O(-6) quotient, and its remaining scalar map is nonzero. Consequently the actual embedded kernel is F_{>=-4}, not merely a bundle abstractly isomorphic to it.

2. The first-jet summands are actual saturated subbundles. The imported principal-parts identification respects the direct sum U+T and its order-zero inclusion. A direct summand Mi of the saturated M is saturated in the constant ambient and in its own coefficient span. If the coefficient spans are disjoint, their genuine constant-space decomposition therefore gives F=F10 direct-sum F18. This is not a horizontal interpretation of an ordinary Birkhoff splitting.

3. The first disjoint alternative is impossible. Its F10 has rank 9 and degree -18, while every degree of a direct summand of F is at most -2. Thus all nine degrees would be -2, but F has only five such degrees. The optional complete-Veronese argument is also valid: completeness follows only in this case from the 11-dimensional coefficient isomorphism.

4. The second disjoint alternative is impossible. Equivariance forces each HN graded representation of F10 to be a subrepresentation of the corresponding graded representation of F. Irreducibility, the single available scalar, and the rank-four requirement leave exactly V(-4)+O(-6). HN truncation respects the actual constant direct sum, so the proof correctly obtains E0=E10 direct-sum F18 and then S0=S10 direct-sum M18. U and T lie in the indicated actual summands. Hence the actual quotient by L0 has M18/T as a direct summand. The first-principal-parts sequence identifies this quotient as O(-16), contradicting Hom(A(-6),O(-16))=0. No higher-order derivative or realization assertion enters this contradiction.

5. The conclusion on the coefficient kernel follows from Schur's lemma: both D coefficient maps are nonzero, so the D kernel projects isomorphically to each source D. The degree-ten system is therefore complete, while the degree-eighteen system still loses one P and has dimension 15.

The physical W, rather than W', is consistently used in principal parts and symmetric powers. Independent fixed universal representation-ring arithmetic confirms Sym8 W=P+D, Sym10 W=A+V+D, and Sym18 W=A+V+2P+D; the rank/degree arithmetic also checks. Results are retained in INDEPENDENT-REVIEW-FIXED-CHECKS.json.

The original t=0 remains an imported exact input, not a newly introduced defect or saturation assumption. The proof excludes precisely the two disjoint coefficient-span alternatives. It does not exclude or realize a whole kernel splitting, quotient, profile, or full-positive branch. No selected actual coefficient, point, jet, tensor, matrix, broad search, or external write was used.

## Supplement: publication-slice verifier review

I reviewed the revised verify.py, exact SHA256 771e7ac6c9f9f5ccc3b06b09c4666a7cd45bcc13bef17e3bcf450a4478dcf805, and REPRODUCE.md, SHA256 e26541d0e6d252646edb312d5d3f6880f9337dfba6f26c68c7890091f9294673. The verifier explicitly pins the three complete file/ref/path/blob/SHA256/byte tuples and the frozen proof hash. Its source pins agree with my independently authenticated results. Deliberate row-order checking against fixed tuples does not allow a mismatched pairing to pass. All checks use explicit exceptions and remain active under optimization.

I independently copied only PROOF.md, verify.py, characters.py, INPUTS.json, and the three inputs/*.md files to a fresh temporary directory. Both normal Python and python -O passed all 38 reported checks there, without any raw connector-response file or other local audit dependency. Exact replay results are in INDEPENDENT-REVIEW-SELECTED-REPLAY.json. This supplement does not alter the mathematical verdict or the exact reviewed proof hash above.

