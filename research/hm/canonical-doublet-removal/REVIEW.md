# Whole-proof review of the canonical doublet removal

Verdict: ACCEPTED for the stated actual structural conclusions, conditional on the single authenticated immediate input SIXTEEN. The complete final proof, verifier, input manifest and reproduction instructions were read and checked independently. The immediate original was freshly fetched from its exact GitHub commit, rather than authenticated only from the author's audit copy. Review completed on 2026-10-23 UTC. This is mathematical review, not proof-assistant formalization.

## Final bytes reviewed

SHA-256:

    PROOF.md
    f2daa4d106fc02dbdf869335eafa4305de308e71d6e917296a84f9265caa6536
    verify.py
    9fbf57d7399d35e5e0bb5b4de87a42606673315a49a8ba4c03feec9a6dac33c6
    INPUTS.json
    39369f6f25cd5f43a300e2f14d06a24e16eb70441542656fb4352990228eac00
    REPRODUCE.md
    14ee627257a9d9d34391bd997478d7ca188449de25a053413d5fd21c162d72bd

All four hashes were recomputed from the reviewed local bytes and matched these values. A change to any of these files requires a corresponding review update. REVIEW.md does not hash itself.

## Fresh immediate-input authentication

The complete SIXTEEN proof was fetched through the GitHub connector from Akilleez-QA/read-em-and-weep at commit 8d17ad2bae45df6078dbb50ff963228c6105c815, path research/hm/sixteen-source-opposite-pencil/PROOF.md. Its fresh UTF-8 payload contained 13,697 bytes and matched audit-inputs/SIXTEEN.md byte for byte. Independently computing Git's SHA-1 identifier from `blob <byte-count>\0<content>` gave:

    5c2d6599bdb1e5b5e7227cc2e3b6b4990bf6989d

This agrees with both the connector's reported blob and INPUTS.json. The fresh original was read in full. It supplies the actual sixteen-source exact presentation, the weighted extension with one-dimensional trivial multiplicity J, local freeness of C, and the exhaustive necessary saturated-image/quotient alternatives used here. Its earlier inputs remain imported theorems; this review does not claim a fresh independent authentication of the entire transitive dependency chain.

## Mathematical checks

1. The unique W' isotypic source is intrinsic. Its constant projection has only the P channel, by W' tensor W=P. If that projection vanished, the source would inject on every fiber into the rank-two weighted bundle F. Equal-rank fiberwise injectivity would make this an isomorphism, contradicting degrees -2 and 10. This proves actual nonvanishing, not only the availability of a representation channel. The unique nonzero channel is the tensor Euler inclusion and has locally free quotient Q isomorphic to W' O(1).

2. The preimage Y_P of the actual constant P component admits equivariant splittings because H1(O(5))=0. Applying equivariant Hom(-,F) to the Euler sequence proves that restriction from Hom_G(P_act O,F) to Hom_G(U' O(-1),F) is an isomorphism: its endpoint groups vanish by Hom_G(1+V,D)=0 and H1(O(4))=0. Consequently there is exactly one splitting agreeing with the actual source lift. The resulting lifted P subbundle is canonical relative to the actual maps, not a chosen normalization that discards a graph component. Named irreducible identifications need not choose scalar coordinates.

3. Quotienting the source doublet and its actual image preserves C and yields the stated rank-fourteen source and locally free Z19. The lifted P quotient gives a canonical Q subbundle and the split F+Q inside Z19. Defining Y17=Z19/Q gives precisely the weighted extension with constant quotient H15=1+2A+V+D.

4. Both Hom_G(Y17,Q) and Ext1_G(Y17,Q) vanish. For the constant quotient this uses absence of P in H15 and H1(O(1))=0. For F it uses H0(O(-4))=0 and the equivariant Serre-duality character test Hom_G(1+V,A)=0. The long exact sequence therefore proves existence and uniqueness of the equivariant splitting Z19=Q+Y17. It does not claim a canonical splitting of the remaining weighted extension of H15 by F.

5. The forbidden quotient Hom_G(C,Q)=0 follows in all seven necessary cases from the authenticated image/quotient table. Every atom of degree greater than one has zero Hom into W' O(1), and the only remaining possible atom W O(1) is excluded because W and W' are distinct. The Hom exact sequence proves this even without splitting C as its image plus quotient. The proof does not choose an actual row.

6. The actual source projection E14 O(-1)->Q cannot vanish, since otherwise the nonzero projection Z19->Q would factor through C. Its sole representation channel is the unique T6 source, using W' tensor A=T6. A nonzero map in this one-dimensional channel is the universal surjection obtained from complete quadratic evaluation. Its kernel is P O(-2). The other isotypic source summands have zero Q projection, so the full kernel is the actual canonical direct sum P O(-2)+(2W+S) O(-1). The independently checked cross Hom identity is (2W+S) tensor W=2+3A+D, containing no P; the stated cross Ext vanishings also hold.

7. Crucially, Section 5 defines Y17->C through the unique section Y17->Z19, followed by Z19->C. It does not incorrectly assert that Y21->C descends through quotienting by the lifted P target. Surjectivity of the source projection onto Q shows that this section-induced map is onto C, with exactly the computed source kernel. Thus the final sequence preserves the actual C and is fiberwise exact. The original weighted F lies in the same canonical complement because Hom_G(F,Q)=0; its actual map to C is unchanged.

8. The final source has rank12 and degree-16; the target has rank17 and degree10. Their difference gives rank5 and degree26, agreeing with the imported C. All subbundles, sections, quotients and retained maps arise from the actual presentation. No additional cancellation, C-type selection, marked-line identification or comparison with separately marked conditional subspaces is asserted.

## Replay and scope

Both `python3 verify.py` and `python3 -O verify.py` passed after fresh-input authentication. The verifier uses explicit runtime requirements, so optimization does not disable its checks. Its nine-class character arithmetic, seven conditional forbidden-quotient tests and universal rank/degree balances support the proof's fixed representation assertions; the geometric conclusions were separately reviewed above. REPRODUCE.md correctly reconstructs the omitted audit input from the exact commit and invokes both checker modes.

No selected actual HM/source coefficient, point, parameter, matrix, instance rank, scan or large computation was evaluated. No external write was performed for this review. The reviewed result is the canonical twelve-source presentation and its two forced actual channels, not a determination of the actual row or any unresolved actual scalar.
