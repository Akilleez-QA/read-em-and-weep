# Independent whole-proof review

Verdict: PASS for the entire frozen proof, under its expressly retained actual-geometric hypotheses.

- Reviewed file: PROOF.md.
- Exact UTF-8 length: 15139 bytes.
- Exact SHA256: a6e56f535af652d3ff437cc5041527636f601751ae24285ba1ec91670f4db7ae.
- Review completed: 2026-10-24 UTC.
- This verdict covers the statement, all eight sections, the actual-map arguments, and the retained stopping boundary. It is not an arithmetic-only or excerpt-only review.

I independently compared the exact amendment against my earlier isolated copy and reread the entire current proof. The only proof changes are the two j-indexing clarification sentences. The verifier changes only its proof hash and length pins; the reproducer changes only its proof hash pin. All mathematics and direct inputs are unchanged. I reran the exact eight-file isolated normal and optimized replay in a newly empty directory and rebound all three final review records to the current proof above. No earlier proof hash is the final verdict.

## Independent source authentication

I read all three complete direct inputs. For each, I independently called the GitHub connector twice: once at the exact immutable commit/path and once for the stated Git blob. I compared the complete returned UTF-8 bytes against one another and against the selected local input, including byte length, SHA256, and independently recomputed Git blob SHA1. All comparisons passed. I did not use LOCAL-SOURCE-FETCHES.json or author replay outputs to establish authentication or validity.

1. common-kernel-ladder.md: commit 5249c844765cfd96ffb51bdfd4aaef8307d49b1f; 13135 bytes; SHA256 0a24ab99c6f3d6c2f60212532c7f4aed2bd7d5fba17823243dd479a83a7308dd; Git blob d64a0db4f2bcbd61651cdefc37a37b672c321176.
2. nine-jets.md: commit 66a6bfe8dd424da58f3d775be1818d1f4f71eff1; 12744 bytes; SHA256 44ee429fa26b65b68b2668ce69dff219e4a4daf0a6bdaa9fac0e94aa8a631b3a; Git blob 916cc6a3bc1cf8ad07e019f00a1f5ebf867311d6.
3. deep-images.md: commit 95af2c0fa1e3cce92496a44ef9023708735e1ec7; 12085 bytes; SHA256 09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26; Git blob 9cf95f42505f37900f5a24c25cff07acca1b499f.

The immutable repository paths, returned URLs, individual comparisons, and reviewer raw-fetch hashes are recorded in REVIEWER-AUTHENTICATION.json. Transitive geometric hypotheses remain hypotheses, as the proof states; this review does not claim to have independently reauthenticated every transitive input.

## Sections 1 and 2: actual normal targets and coherent flags

The imported common-kernel ladder supplies the actual bundles, degrees, sum/intersection splittings, and restrictions into the coherent lower O(-10), not only their abstract isomorphism classes. The nine-jet input supplies the original annihilator flag in the genuine fifteen-dimensional ambient. The Omega twist gives beta_B2 target O(12), beta_B1 target O(14), and beta_B0 target O(16). The proof uses these corrected targets consistently.

The capacity argument remains at the actual rank-seven bundle. Every nonzero backward kernel has negative top as a subbundle of B3, so a horizontal residual cannot survive. The quotient ranks are indeed k initial twos followed by 7-2k ones. Summing the separate coherent degree bounds gives -98+12k-2k^2 and exact deficits 0,6,8 for k=1,2,3. Each rank-two determinant deficit is an invariant effective divisor of degree at most eight and must vanish. Each rank-one map has invariant component degrees e and e-2, so only e=0 or e=2 is possible in this range. This excludes k=3, forces all upper lines for k=1, and all three lower scalar quotients for k=2. The equivariant rank-two equality maps preserve both columns: one off-diagonal entry vanishes by negative degree, the other by the absence of invariant quadratic forms.

The amended proof now explicitly restricts the backward recurrence B_j=B_(j-1)^- in (5) to j>=1. Its j=0 paragraph explicitly restricts the ambient convention to C/B0=O(18) and beta_B0's target, and expressly disclaims B0=C^-. This fully resolves the indexing clarification. The j=0 target follows directly from the original scalar line and its first jets.

## Section 3: principal parts and saturation-projection

The principal-parts identity is supplied by the complete deep-images input and applies to a possibly incomplete actual coefficient system. Generic rank alone is never substituted for global saturation: regular factorization through a saturated image and a nonzero degree-zero determinant are both used when asserting an intrinsic-source isomorphism.

The saturation-projection fact is correct. If J is the coherent rank-one derivative image and S its saturated line, generic containment of its projection in L implies regular containment in L. Since J already maps onto L, the line map S to L is surjective, hence an isomorphism. Consequently J=S. This proves both the forward quotient and the intersection statement without a connection or horizontal complement. When the entire normal quotient is a line, the residual quotient identification follows from the actual sum and intersection.

For every saturated auxiliary jet span, the generic derivative rank is at most one: over the function field, differentiation of its span adds at most the next derivative of its original scalar generator. Saturation does not change that function-field span. This remains valid after ramification and requires no claim that the auxiliary line spans the entire constant ambient.

## Section 4: the genuinely ramified K to U6 step

The k=1 equality tail produces actual fourth jets Q1 of rank five and degree -70, followed by actual fifth jets K of rank six and degree -78. Equal-degree principal-parts comparison is valid at both steps. The quotient F6/K is the lower O(-10).

The restriction of beta_F5 to F6 has that coherent lower target. Its restriction to K vanishes by Hom_G(T6,Sym3 W)=0. Therefore K's derivatives lie in F5. The equivariant extension of O(6) by O(-10) in F5/K splits because H1(O(-16))^G=(Sym14 W)^G=0. This is an actual quotient-bundle splitting only, not a horizontal structure. The lower component of beta_K vanishes by Hom_G(T6,W)=0; the upper component is the actual inherited O(-8) image inside O(4). Its saturation is the entire O(4), which gives the stated preimage U6, U6/K=O(6), U6 intersect F6=K, and F5/U6=O(-10).

The proof correctly retains deg U6=-72 instead of identifying it with the degree -84 intrinsic sixth-jet source. The difference is the degree-twelve ramification contribution. Nothing in the subsequent argument assumes an unramified sixth source or transfers the full span of F6 to this auxiliary tail.

## Section 5: actual full projections and the nonsplit quotient

Hom_G(U6,O(-10)) vanishes by restriction to K followed by factorization through O(6). This kills the actual restricted lower map from F5 into the normal target of F4, placing derivatives in F4. The upper map through beta_F5 has kernel F6, and U6/K maps isomorphically to F5/F6. It is therefore an everywhere surjective projection onto O(6), not merely a generically nonzero map. The saturation-projection lemma yields U7/U6=O(8), U7 intersect F5=U6, and F4/U7=O(-10).

The identical restriction/factorization argument at the next actual ladder step gives U8/U7=O(10), U8 intersect F4=U7, and F3/U8=O(-10). Since U8 is in B3 and B3=B2^-, its derivatives lie in B2. The actual beta_B3 projection has kernel F4 on F3 and is onto through U8/U7. Thus U9/U8=O(12), U9 intersect B3=U8, and B2/U9=B3/U8.

The latter rank-two quotient Q has degree -6 and the exact sequence O(-10) to Q to O(4). In particular top Q<=4: a line of degree greater than four could map neither to the quotient O(4) nor to the kernel O(-10). No splitting is needed. All subsequent identifications of Q are consequences of actual sum/intersection statements.

## Section 6: the corrected zero-or-isomorphism climb

Since U8's derivatives lie in B2, beta_B2 kills U8. Its restriction to U9 is therefore a scalar O(12) to O(12), not a map to O(14). There is no claimed invariant-Hom vanishing at this equal degree. Both cases are treated.

If the scalar is zero, derivatives of U9 stay in B2 and their coherent image lies in Q(-2), whose top is at most two. Generic rank is at most one by the auxiliary-jet argument. It cannot be zero because U9 has strictly negative top. Applying the actual rank-one capacity in that same ambient gives -42<=-70, a contradiction. A nonzero scalar is everywhere invertible and the saturation-projection lemma yields U10/U9=O(14), degree -28, with the same residual Q.

The next two scalar maps are likewise O(14) to O(14) and O(16) to O(16). Their zero cases give respectively -28<=-88 and -12<=-108. Their nonzero cases produce quotient increments O(16) and O(18). The final span has rank thirteen and degree six, impossible as a subbundle of a constant bundle on P1.

All three negative-top uses have an independent justification: the original fifteen-dimensional coefficient system embeds into the complete degree-eighteen coefficient space, as retained in the nine-jets input. Its annihilator kernels B2, B1, and B0 inject into the complete evaluation kernels Sym15 W(-3), Sym16 W(-2), and Sym17 W(-1). Thus U9, U10, and U11, respectively, have strictly negative top. This is an inclusion of the actual partial-system kernels into universal complete-system kernels, not a completeness claim for the auxiliary line. It uses no selected point or jet evaluation and no rank-seventeen transfer theorem.

## Section 7: the surviving k=2 lower-column incidence

The exact lower scalar tail gives the actual first and second jets of the final O(-18), with Q2 of rank three and degree -48. Its next derivative has the full lower O(-14) image in R1(-2), producing U3/Q2=O(-12). Rank four and degree -60 identify the intrinsic third-jet source with U3.

The already-established rank-two equality map R1 to R0(-2) preserves the lower column. Therefore beta_U3's projection onto the lower O(-12) is everywhere onto. Its generic rank is one, so the saturation-projection lemma gives U4/U3=O(-10) and U4 intersect Q1=U3. Rank five and degree -70 identify U4 with the intrinsic fourth jets D(-14). The quotient map F6 to R0=I6 identifies beta_F6(U4) with precisely the actual lower O(-10), not an arbitrarily chosen abstract line.

The quotient M then has kernel Q1/U3=O(-10) and quotient O(-8). The equivariant Ext group is H1(O(-2))^G, of dimension one. The zero class gives O(-8)+O(-10); a nonzero class gives the determinant-one Euler extension with middle W(-9). This classifies necessary quotient types only and supplies no quotient connection or realization claim.

## Isolated replay and restriction audit

I inspected REPRODUCE.md, verify.py, and characters.py in full. I copied exactly its eight selected files into a newly empty independent directory, with relative paths preserved and with no LOCAL files, author outputs, drafts, raw fetches, or caches. I ran python verify.py and python -O verify.py independently. Both exited zero, emitted identical PASS results with 67 explicit main checks and the exact frozen proof hash, and had no stderr. The character module's 81 fixed exact-rational McKay checks remain explicit under optimization. All eight selected files were byte-identical before and after both runs, and the original selected files were unchanged. REVIEWER-REPLAY.json records the inventory and outputs.

These are only bounded universal identities and displayed degree arithmetic. No actual coefficients, parameters, points, jets, tensors, matrices, instance ranks, or normalizations were selected or evaluated. There was no large computation or broad scan, no GitHub write, no quotient connection, no horizontal splitting, and no full-span transfer to an auxiliary tail. The geometric arguments above, not the checker, establish the proof's validity.

## Exact accepted contribution and stopping boundary

Inside the simultaneous rank-seven image E6(-D12), the proof excludes the k=3 small-slack flag and the k=1 upper-column equality flag, leaving exactly the k=2 lower-column flag and its actual quartic-jet subbundle and two possible rank-two quotient types. It does not exclude or realize the simultaneous image itself, the other rank-seven image, delta=12, either quotient type, or any whole branch/profile. It adds no original jet-separation claim beyond order nine, no algebraicity, and no change to e9 or the original t. The whole frozen proof is accepted with this precise scope.
