# Independent whole-proof review

Verdict: PASS for the theorem and the explicitly limited scope stated in PROOF.md. No mathematical correction is required. This is a mathematical review relative to the authenticated inputs, not a formal proof-assistant certificate or a certification of the separate rank-three coverage argument.

## Frozen artifacts

Reviewed PROOF.md SHA256:

`d5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e`

Other reviewed artifact SHA256 values:

- verify.py: `d82507bdbab9f54b3c177727367010b2186c24572e8a1bda657d9474248bf06e`
- RESULT.json: `b1a7e2c0487b20e2857c7c8e99de5a69a8bf072abe6659c07cd98fff82a37641`
- INPUTS.json: `f855db17d0fe579f791cf56b4fabe994c6c4d541effef8fa61e075ff64c798eb`
- REPRODUCE.md: `6ce04560ff7dd6213e908d188ba841c6ad676ab43871e420cc775a01ff986afe`

The author confirmed the proof hash frozen before this review was written.

## Independent input authentication

I fetched each of the six complete originals independently through the GitHub file API, specifying repository Akilleez-QA/read-em-and-weep, the exact immutable commit, and the exact path in INPUTS.json. Each returned Git blob ID matches the manifest. I independently recomputed its Git blob SHA1 and SHA256 from the freshly fetched UTF-8 bytes, checked its byte length, and compared those bytes with the supplied local input. All six checks passed.

| Original | Bytes | SHA256 |
|---|---:|---|
| PR477 | 10321 | `0325c7b3cf237e27d4466e17c50cdb7f1a5cd874c310f32c03516acc250a2a38` |
| PR486 | 10493 | `0e7df08243d9cd60c812d29f57a88edd8bd87880670f640f7e6ac4562d740e41` |
| PR1120 | 10894 | `b47031d81c8c138aa5f1b4c4cee992f9ae04ee74adb8c403cedd2e74c51a2d2e` |
| PR1122 | 8009 | `7be070050a035ceec64c5698fd1ae70857225a405e1a43d4cbebc4019f5a342a` |
| PR1056 | 10582 | `1ee98092e1322841d031d65649dee205299b88d9ba726599f0678d8b1e5b2a1e` |
| ACTUAL | 9672 | `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256` |

The independently fetched originals byte-match the complete originals in inputs/. Returned immutable URL/blob metadata is retained in REVIEW-1-AUTHENTICATION.json; INPUTS.json records their digests and byte lengths. This authentication establishes the identity of the cited originals; it does not silently prove every earlier dependency cited inside them.

## Whole-proof audit

1. **Actual primary pencil.** PR477 supplies an actual polynomial-module injection, not only an equivariant embedding in isolated degrees. PR486 gives absence of a degree-five socle. PR1120 supplies the physical parity and actual primary representations used here. Positive coordinates therefore kill Y=1+A, while a vector killed by its negative multiplication would produce a degree-five socle vector in K. This proves injectivity of the actual curry, hence its isomorphism with Hom(W,Z). Evaluation on the tautological line is consequently onto everywhere, with kernel Z O(-2), and tensoring with U gives the stated 16-to-8 coefficient-space pencil. No scalar normalization or selected direction is used.

2. **Canonical slope filtration.** The threshold piece E_{>=-3} is the canonical Harder--Narasimhan slope-filtration subbundle, including all degrees -2 and -3. Since H0(E(1))=0, no larger degrees occur. Its quotient has all degrees at most -4. The filtration is G-invariant; an arbitrary noncanonical direct-sum projection is unnecessary. The degree-minus-three graded coefficient representation defined in the proof is the same isomorphism type as ACTUAL's R3.

3. **Terminal reconstruction and parameter conventions.** Pushing the diagonal resolution tensored by F(1) yields the asserted exact sequence whenever H0(F)=H0(F(1))=0, and this construction is natural in F. In PR1056's convention, cohomology multiplication by u and v corresponds respectively to m_y and -m_x. The diagonal expression v mult_u-u mult_v therefore gives v m_y+u m_x. This is the actual terminal pencil with its original common parameter marking, not a separately rotated substitute. All quotient coefficient maps therefore intertwine both actual terminal arrows.

4. **Hom vanishing uses both arrows.** The induced map from (U tensor Z) O(-2) to E_{<-3}(1) is zero, because its target degrees are at most -3. Exactness then forces the source coefficient map to factor through (U tensor Z) O. The factor into a direct sum of O(-1) is zero, and surjectivity of the primary pencil forces the target coefficient map to be zero too. This reasoning is valid for the entire lower-slope quotient, not just for a single line summand. It avoids the invalid inference from an arbitrary kernel-bundle injection alone.

5. **Actual embedded subspace, not character matching.** Vanishing H0(E_{<-3}(1)) makes H1(E_{>=-3}(1)) inject into H1(E(1)); H2=0 gives the displayed short exact sequence. The actual primary target map has zero image in its quotient, so its entire injected image lies in this canonical subspace. The top-slope exact sequence has left term R2 O(-1), which is acyclic. It canonically identifies that subspace with R3 tensor H1(O(-2)), hence with R3 after the fixed determinant trivialization. The resulting W'+T6 inclusion is genuinely injective and equivariant. Only at this point is representation subtraction used.

6. **Four-case classification.** The equations and R2 formula in Section 5 agree with the complete authenticated ACTUAL original. The new inclusion forces a>=1 and b>=1, and the first equation forces a=1 and d=g=h=0. The remaining nonnegative slack equation (b-1)+(c-1)+e+f=1 has exactly four solutions. Substitution gives precisely the four displayed bundles, each of rank 17 and degree -54. This uses the W' constituent as well as dimension; a mere dimension-eight lower bound would be weaker. PR1056's displayed E10, E13 and E14 have R3 equal respectively to 0, T6 and 0, so all three are excluded.

7. **Scope.** Sections 1--4 establish an actual HM terminal-space obstruction relative to the pinned HM inputs, independently of a source-pair ledger. The four-type statement additionally uses ACTUAL's necessary classification. The proof does not assert occurrence of any surviving type, identify a marked primary component with a noncanonical negative-pencil block, claim horizontal or positive-coordinate projectors, or infer rank-three geometric coverage from a finite ledger. In particular its exclusions of E10/E13/E14 are not by themselves a global rank-three exclusion or a repair of the original theorem. These boundaries are accurately and repeatedly stated.

## Bounded checker audit

I inspected verify.py and ran both `python verify.py` and `python -O verify.py`. Their outputs agree byte-for-byte with one another and with RESULT.json. Both report PASS and 150 checks. The explicit require routine remains active under optimization.

The checker authenticates the six local inputs, checks the relevant fixed nine-class representation identities, verifies the four universal coefficient solutions, their rank/degree and cohomology characters, and the required elementary P1 cohomology controls. I separately checked the small universal integer solution set of the displayed equations: 28 formal solutions before the new inclusion and exactly the same four afterward. These are checks of universal representation multiplicities, not calculations on actual HM/source instances. The written argument, not these checks, supplies the actual-module injectivity, terminal functoriality, canonical subspace inclusion, and scope.

No actual HM/source coefficient, tensor, matrix, point, parameter, derivative, jet, selected-instance rank, actual-instance scan, or large computation was evaluated. No public write was made.
