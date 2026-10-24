# Independent entire-proof review: split actual dual extension exclusion

Verdict: PASS, conditional on exactly the retained actual-geometric hypotheses and transitive source/section gates. No correction to the frozen proof is required.

## Exact reviewed object and evidence

I read every paragraph of the complete 6,373-byte PROOF.md, SHA256
57a435c44d7de7f2ef0e97b168530acc32aa37dc25258adfff48ba06f848cc82,
including its statement, boundaries, complete-input description, all three argument sections, and final stopping point. This verdict is bound to those exact bytes, not a later file with the same name.

I also read both COMPLETE immutable direct originals, not extracts:

- PR1211, commit 430bdab090b2319313e5855c66fd7cc102c09e35, research/hm/rankfour-profile11-triplet-dual-extension/PROOF.md: 16,075 bytes; SHA256 c0b961a3a851b21906218865208c304df8390dedb72b73fb9e2b912a33d68d0b; Git blob 54acabb5c6a641ca602f494956d209e1d268a955.
- PR1221, commit 84b418e22f03b5718409bdeb23ae353ecc4eb681, research/hm/rankfour-profile11-triplet-mixed-jet-pairing/PROOF.md: 14,593 bytes; SHA256 3e1ce0d1589d694d578796a90398cbdaf8fdf6fb340158b5098ad3f79cdfa95b; Git blob 91e0c23867113c0a7d5b032098c8e365b356859d.

For EACH source I independently called the connected GitHub immutable-path read and the Git-blob read. The path response was complete base64; the blob response was complete UTF8 text. Decoding/re-encoding and hashing established exact equality of fresh path bytes, fresh blob bytes, and local original bytes. Length, SHA256, Git blob SHA1, the returned path SHA, and immutable URL all match. No author's cached response was used as fresh authentication. Details are in REVIEWER-AUTHENTICATION.json. Raw responses are explicitly LOCAL REVIEWER-FRESH evidence in REVIEWER-FRESH-SOURCE-FETCHES.json and excluded from replay.

## Frozen proof: statement and input boundary

The statement has the correct orientation: the original scalar line is in V O, the auxiliary line and its jets are in V* O, and S=ann(F) is in V O for the actual constant pairing. The same symbol V denotes the actual fifteen-dimensional ambient, not an irreducible character label.

PR1221 supplies the full span of the actual auxiliary line and identifies its actual globally separated fourth jets. PR1211 supplies the actual extension with subbundle T3 and quotient O(-4), its alternatives, and the embedded incidence conclusions in the nonzero case. The new proof explicitly retains those facts and all transitive gates rather than claiming the small checker proves them.

The residual simultaneous rank-seven defect and forced k=2 flag are retained. There is no silent passage to every coherent-image branch, no assumption of either K1/K3 alternative, and no transfer from an unrelated rank-seventeen ambient. The ordinary splitting in the conclusion is correctly distinguished from an ambient horizontal splitting.

## Frozen Section 1: diagonal and principal-parts convention

The convention is unambiguous: source coordinate is the first factor, base coordinate is the second, and P4(L) is the pushforward of the source line bundle restricted to the fifth infinitesimal diagonal. Thus order four uses I_Delta^5, not I_Delta^4.

On P1 times P1 the diagonal has bidegree (1,1). Tensoring its fifth ideal power by O(18,0) gives O(13,-5). The determinant-line linearization that accompanies the diagonal equation becomes trivial for the physical determinant-one action; its fifth power is also trivial. No residual scalar-character assertion or arbitrary identification of the actual V with V* is needed.

The displayed sequence (4) is exact on the product. Its pushforward gives the exact sequence (5): the product projection formula identifies the left pushforward as H0(O(13)) tensor O(-5), and H1(O(13))=0 kills the possible connecting obstruction to surjectivity. The middle pushforward is H0(O(18)) tensor O. These are entire-bundle statements over the whole base.

The universal kernel has rank 14 and degree -70. The quotient rank is 5 and its principal-parts filtration has successive degrees 18,16,14,12,10, summing to 70. These checks agree with the sequence but do not replace its proof. The coefficient representation is Sym13 W after the fixed determinant-one duality. No splitting of the quotient is used.

## Frozen Section 2: incomplete system and exact annihilator kernel

The injection c has the right domain. For the auxiliary line U0=O(-18) in V* O, dual evaluation is V O -> O(18), hence the constant coefficient map is c:V -> H0(O(18)). In PR1221, r:E -> V* is onto and E=H0(O(18))*; therefore c=r* is injective. Confusing this with the ORIGINAL coefficient map V* -> H0(O(18)) would invalidate the argument, but the frozen proof explicitly avoids that error.

The fifteen-dimensional system remains incomplete inside the nineteen-dimensional complete system. Tensoring c with O is injective, and the fourth-principal-parts map composed with it is the actual auxiliary evaluation map epsilon4. Nothing in this construction enlarges the system to all nineteen sections.

For precision about the jet identification, locally a constant v in V pairs with a local representative of the auxiliary scalar line to give a scalar section of O(18). Its principal part modulo the fifth diagonal ideal consists of its derivatives through order four. Dualizing produces the span of the corresponding derivatives of that local representative. Under changes of coordinate or trivialization these generators change by the usual invertible triangular transformations. This is the intrinsic osculating construction, not a connection on a quotient and not evaluation of selected actual data. The supplied global separation makes its image exactly the actual subbundle U4, not merely a generically matching or unsaturated image.

For a bundle map epsilon4 into a locally free principal-parts bundle, the annihilator of its dual image is its kernel in the original constant pairing. Thus ann(U4)=ker(epsilon4) is the correct sheaf identity. Restricting the injective map c tensor O embeds this kernel in the universal kernel. The actual inclusion U4 subset F reverses under annihilators and yields S subset ann(U4). Combining the two gives the asserted embedding into O(-5)^14.

No equality between the incomplete-system kernel (rank 10 here) and the complete-system kernel (rank 14) is claimed. No saturation of the latter embedding is needed. Full auxiliary span is precisely the hypothesis ensuring the coefficient injection, and the proof correctly identifies where it is essential.

## Frozen Section 3: exclusion and inherited consequences

Every component of a morphism O(-4) -> O(-5)^14 belongs to H0(O(-1))=0. Therefore such a morphism vanishes. An actual O(-4) subline in S would compose with its established injection to a nonzero morphism, a contradiction.

The zero extension class of PR1211 really yields an actual complementary O(-4) subline, not only a label in an abstract splitting. This is enough for exclusion. Conversely, the retained surjection S -> O(-4) is NOT excluded by this Hom calculation; it has the opposite direction. Nonzero extensions of more negative subbundles can and here do have that quotient.

Once the split class is excluded, PR1211's nonzero alternative supplies S=W'(-11)+A(-14), its actual canonical highest-slope C=W'(-11), the exact sequence 0 -> T0 -> C -> O(-4) -> 0, both intersections with T3 and T2 equal to T0, and C+T3=S. The pushout sequence is inherited from PR1211's actual incidence proof. None of those embedded statements is inferred just from an abstract direct sum.

The ordinary slope bound is valid: every splitting summand O(a) has a nonzero composite into O(-5)^14, so H0(O(-5-a)) must be nonzero, forcing a<=-5. This uses ordinary Birkhoff-Grothendieck summands only, without a horizontal or equivariant choice.

The final paragraphs preserve the correct stopping point: necessary non-splitting within the residual case, neither exclusion nor realization of that case, no K1/K3 input, and no new original higher-jet, endpoint, local-defect, or algebraicity claim.

## Entire direct-source audit

PR1211: I read the statement and all Sections 1-7. The actual quotient is obtained in the stated constant pairing from the retained saturated flag. The extension-space computation and universal degree-twelve polarization use the declared determinant convention. The two-variable apolar complete-intersection argument gives generator degrees adding to fourteen; the invariant-divisor bound excludes the unequal case with smaller degree below seven. The degree-seven generator representation is W'. Polarization/contraction identifies the twisted connecting-map kernels only in its stated range 0<=m<=9. Cohomology and total degree force the nonzero splitting, rather than assuming a type from extension-space dimension. The actual quotient restricted to the top doublet is nonzero and everywhere onto by the degree-seven invariant-divisor argument. Its kernel lies in T2 and uniqueness of the equivariant scalar-line map identifies it with the actual T0. Consequently the intersection and pushout statements used by the frozen proof are justified within the retained assumptions. The separate derivative claims and all end boundaries were read; the new proof does not need to promote them to higher-jet conclusions.

PR1221: I read the statement and all Sections 1-8. The actual mixed-jet rectangle supplies whole-diagonal multiplicity twelve by adjacent derivative identities. The residual invariant biform space has precisely the stated two symmetric components under the supplied small character identities. The coefficient-map orientations H=r* q and, after symmetry, H=q* r are consistent. The fixed apolar identification yields an order-six transvectant plus scalar identity; the leading symbol is nonzero by homogeneity, independently of a selected actual form or point. The rational Wronskian argument bounds its kernel by six. The representation gap excludes a strict enlargement of the four-dimensional K, giving exact kernel K. The actual factorization then forces r=hq with h invertible and symmetric. Thus the full auxiliary span is proved, not assumed circularly. Constant h preserves the already-established original separated jet maps, giving precisely the actual auxiliary fourth jets needed here. The later at-most-two embedded-kernel restriction and final boundaries were also read, but they are not extra inputs to this exclusion.

This audit does not claim fresh independent verification of the transitive originals not listed in INPUTS.json. Their geometric, section, representation, and source gates remain the expressly retained premises.

## Independent exact replay and restrictions

I inspected the complete verify.py and REPRODUCE.md. The verifier uses explicit require calls, so optimization does not disable its 34 checks. It hard-codes the complete frozen proof pin and both complete source pins independently of the manifest. Its numerical scope is fixed small diagonal twists, ranks, degrees, and line-bundle Hom arithmetic; it is not a geometric certificate.

I created a NEW empty isolated directory, /workspace/shared/REVIEWER-FRESH-split-dual-replay-dt0tt8hv, and copied exactly:
PROOF.md; INPUTS.json; REPRODUCE.md; verify.py; inputs/dual-extension.md; inputs/mixed-jet-pairing.md.

Both normal Python and Python -O returned success with byte-identical output: PASS, 34 checks, 6,373 proof bytes, and the exact frozen SHA256 above. Both source and replay copies of all six files remained unchanged; the isolated directory still contained exactly those six files and no cache/helper/reviewer outputs. REVIEWER-REPLAY.json contains the commands, complete outputs, and before/after hashes.

No frozen proof, checker, manifest, reproduction instructions, or immutable input was modified. No GitHub write or local Codex was used. No selected actual HM/source-instance coefficient, scalar, parameter, point, jet, tensor, matrix, instance rank, or normalization was evaluated. No broad scan or large computation was performed.

Final verdict: the frozen proof rigorously excludes the split actual dual extension under its explicitly retained residual hypotheses. It does not exclude the residual branch or either K type and does not assert realization.

