# Independent review: source2 specialization

Reviewed 2026-10-23 UTC. Result: PASS as an identity-based correction of a historical necessary-pair overlist, conditional on the cited written structural proofs. This is not 77 new geometric exclusion theorems, not source2 elimination, not a realization, and not proof-assistant certification.

## Mathematical checks

I independently read the full local PR790 and PR795 proof texts and original actual E/Q* convention note, and independently fetched the immutable PR751, PR758 and PR795 proof texts. PR758 and PR795 remote text bytes matched the copied files exactly. PR751 explicitly identifies G3.21.d610e381ed75, source index2, and already proves the unique primal E in Step2 and saturated endpoint kernel (P+D)O(-2) in Step3. Thus the balanced endpoint condition in PR795 is a consequence for the actual source, not an extra chosen specialization.

The actual E is the kernel in 0→E→H O→Q→0, equivalently the annihilator of Q* in H O. PR790's separated constant block identifies E0=W O(-9) and U_8^10=(P+D)O(-2) in Q*. PR795 Sections2–3 give 0→(P+D)O(-2)→E_R→T O(-3)→0 for both residual coupling classes and every balanced endpoint. Ext1 is H1(T*⊗(P+D)O(1))^G=0. The residual 0→A O(-6)→R→O(-18)→0 splits by H1(A O(12))=0. Finite-group invariants over C are exact. Both conclusions are equivariant bundle splittings only; neither eliminates the nonzero constant residual coupling.

Hence E=W(-9)+T(-3)+P(-2)+D(-2), and Q*=P(-2)+D(-2)+A(-6)+O(-18). Their ranks/degrees are (17,-54) and (13,-54). Original tuple conventions give (0,1,0,0,0,0,1,0). Independently inspected catalogs and the exact through917 row identify local E13 and Q21 as the unique matching pair among 78. The disjoint removal is 72 E mismatches plus 5 remaining Q* mismatches, leaving total37=4+32+1 and three labels. No other source is filtered by this theorem.

## Artifact and reproduction checks

A draft emitted stale copied row removal metadata; that issue was corrected before this review. The final row now has input78, remaining1, removed77 with the exact removed list. Other source rows remain unchanged. I ran verify.py, all21 unit tests in normal mode, and all21 under python -O successfully. The tests include identity/orientation rejection, manifest tamper, transported catalog reindexing, input/output partition consistency and unchanged unrelated rows. The GATES list records reviewed hypotheses; it does not machine-prove them.

Reviewed exact SHA-256 digests:

- PROOF.md: c2267164486a1ed0b6cddb759cb7ef1c4c5c0ee96a8fbc6d90cd675a742cca92
- verify.py: 6e3af4ed4ea427885ddb61d9dff0981be23d24f92580c87cf40cd2a1afbf18d9
- test_verify.py: 787abb879e6033b8e2c11ec662de56c9f5e50af6d274c97153c8a7a84ca9f453
- specialization.json: 6e110fa34d2cf5af767938160bb656bf19cc4a41240d58da2e2155a3fd87d5bb
- manifest.json: 20d4bd14e769540c62926d90924ac97697c08b89946e81e1b97491f506fdb262

No actual HM coefficient, chosen parameter, point, matrix, rank evaluation, external write or spike was used. This review supports the author's new propagation certificate; the review itself is not counted as new mathematical progress.
