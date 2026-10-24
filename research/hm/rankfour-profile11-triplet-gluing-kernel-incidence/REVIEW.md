# Independent entire-proof review: actual lower gluing rows and kernel incidence

## Verdict

**ACCEPT**, subject exactly to the conditional hypotheses and nonconclusions stated in the frozen proof. No mathematical gap or required revision was found.

This is a new independent review by `/root/advance_triplet_local_defect/review_gluing_kernel_incidence`, not the preparatory audit and not an author self-check. I read the entire frozen PROOF.md, every line of verify.py, README.md, INPUTS.json, INPUTS.md, PROVENANCE.md, FROZEN.json, AUTHOR-VERIFICATION.md, and all four complete direct original PROOF.md files. I also cross-checked the packet's source-response and replay evidence. No preparatory draft or preparatory audit was used as a premise or substitute for this review.

The accepted new endpoint is:

- Both components of the actual map h:(W'+T6)(-3)->O(4) are nonzero.
- The actual gluing kernel G7=ker(f:E0->F10) has equivariant type H_6(-4)=(V_alt+P)(-4), transferred through the actual canonical quotient-map kernel isomorphisms.
- The necessary intermediate conclusions are Q5 of type V_alt(-4)+W'(-5), and the actual equality R13 intersect (C7 O)=b7(Q5), with b7:C7*->C7.

This does not identify G7 with the same-typed top of K1. It is not a K1 exclusion, realization, branch closure, full ten-dimensional coefficient-span claim, new derivative-fullness claim, higher-order matching theorem, or algebraicity theorem.

## 1. Exact reviewed object and independent evidence

Packet: `/workspace/shared/rankfour-profile11-triplet-gluing-kernel-incidence`.

External freeze anchor: FROZEN.json, 1,818 bytes, SHA256 `78235458ecdba60eae419d90874fb080542d89c84185f285c65f05708fab6e89`.

The exact ten-file core is:

| Path | UTF8 bytes | SHA256 |
|---|---:|---|
| PROOF.md | 21478 | b20161802eb43ae4a69de779146be620126fe2a0332afd0f19929517b7806807 |
| README.md | 3434 | a775bddc3f68c7f1677f40149bc2e4fd5f688eb278c06e23ce05e4f5746b8a59 |
| INPUTS.json | 14721 | 2684a4c05582e59b6a6d783b12b8ad893298fa279a2798fe9c2b7467e7e2a654 |
| INPUTS.md | 7359 | 9a695c78ef3d6589f0f8f022857c53ae37adf3f1d39d502fc9a5f7b79eb7b48f |
| PROVENANCE.md | 7334 | ee0fb75051f3a442498179b58010146311cd445c04358836ca4444189e3b5bdb |
| verify.py | 9109 | 98b72a8bbec9b7ee7da7636de5f191c9042b38f7d4cc4b5b9b7a2c451f6cc3ea |
| inputs/r13-extension-incidence.md | 19230 | 4819cebda47b3ef7a48ecbcb1fe01295a3a3a7ea7986df540421e1433d547b21 |
| inputs/f18-gluing-surjectivity.md | 12798 | 3919909cd67055e266299a0841e4642c465185eba28500a3b00b4a284f93693a |
| inputs/orthogonal-top-incidence.md | 28094 | 407d35049bb17ab4b8f4e270627adb416fc5601eab1445a21685f2cc27bcb637 |
| inputs/first-kernel-forward-closure.md | 18052 | 90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137 |

I independently made eight fresh read-only GitHub connector requests: one complete base64 exact-commit/path read and a separate complete Git blob read for each original. No request had a line limit. I decoded and compared every byte against the retained original, strictly round-tripped UTF8, recomputed SHA256, and recomputed SHA1 of `blob <byte length>\0<bytes>`. All comparisons passed. These are fresh reviewer responses, not copies of the author's responses.

The authenticated original pins are:

- PR1242: commit `66ef0616fdd0607272b8bbd23892bc33120ac7f2`; path `research/hm/rankfour-profile11-triplet-r13-extension-incidence/PROOF.md`; returned and recomputed Git blob `5ac2f53aec71adda224d3578fb6e871ac6a8fecb`.
- PR1243: commit `dde84900cd6f9ad117800c39042844bb897a2f79`; path `research/hm/rankfour-profile11-triplet-f18-gluing-surjectivity/PROOF.md`; returned and recomputed Git blob `700257a6d8f41f9cfbae7fdf8d78d77795a07bb9`.
- PR1240: commit `3fbaa182b1aceb6915be88088ef158d6d15e34fb`; path `research/hm/rankfour-profile11-triplet-orthogonal-top-incidence/PROOF.md`; returned and recomputed Git blob `f00b059695615d9b8ab6d315798940e3ab0a58d4`.
- PR1236: commit `092fc5f31dfaa5553ee5ea687f175ecba1878a2a`; path `research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md`; returned and recomputed Git blob `f77cfb52743be86e46e0c40570ec036e69aebaf3`.

REVIEWER-SOURCE-AUTHENTICATION.json records the exact fresh requests, UTC start/end times, canonical source and blob URLs, response hashes, full-byte comparisons, and full-reading attestation. All four raw reviewer responses are retained separately under evidence/. The author's raw responses were independently checked against these same full bytes. Transitive earlier originals remain assumptions, not additional sources freshly authenticated in this review.

## 2. Statement and Section 1: imported data and actual-map conventions

The conditional scope is consistent across the statement and all four direct sources: the retained full-positive triplet branch, original t=0 and local delta=12, residual simultaneous rank-seven k=2 geometry, and original K1 remain assumptions. Work is over complex numbers for the physical determinant-one binary-icosahedral representation, not in defining characteristic.

The proof correctly separates V=V_alt from PR1240's seven-space V=C7*. The low-degree H_n identities are present in the direct originals or follow from their stated fixed identities; no fifth original is silently imported. H_n denotes sections and H^i denotes sheaf cohomology. The Serre-dual convention H^1(O(-n-2))=H_n* is correct.

The E0 type, canonical top D0, and canonical W' image N are genuinely supported by PR1242. The absence of other equivariant components of N follows from D tensor W=S4+T6, irreducibility against T6, and the negative-degree V component. Thus N is an actual intrinsic image rather than a selected Birkhoff summand. R13's T6(-3) top is likewise canonical as its maximal-degree block.

PR1236 supplies the saturated coherent image A(4) of beta_E0 in the full normal bundle. PR1243 retains K=K1 and supplies the actual diagram with the isomorphism on the shared T, surjectivity of f and g, the saturated D_Q row, and the onto quotient row h. The proof's kernel identifications follow from those actual quotient maps and their indicated isomorphisms on T and D0. They are isomorphisms in different ambients, not equality of embedded kernels. The unique D0 correction is never differentiated.

PR1240 supplies the actual constant splitting S=Z+C7, the original complete degree-ten restriction in Z*, the annihilator relations, and the saturated projected flags Q_r. Its rank/degree table gives Q5/Q4 of degree 2 and rank one; Q4 saturated in the constant ambient implies it is saturated in Q5. Absence of characters fixes the quotient's equivariant type O(2). The orthogonal form indeed has direction C7*->C7. All imports used later are supported without assuming the desired new kernel type.

## 3. Section 2: exclusion of the zero W' lower row

The actual quotient E0->F18 sends N isomorphically to its W'(-3) block. It cannot vanish, since that would factor N through T=V(-4), and its other blocks vanish by the listed Hom calculations. The same remains true after quotienting by D0.

The restriction beta_E0|N is nonzero because any zero restriction would factor the inclusion N->E0 through K, while Hom(N,K)=0 by ordinary degrees. To rule out generic rank one, saturating the coherent rank-one image in A(4) gives an equivariant O(a). A nonzero O(a)->A(4) requires A in H_(4-a), so a<=2. A nonzero N->O(a) requires W' in H_(a+3), so a>=4. These incompatible bounds are valid even if the original coherent image has torsion defect relative to its saturation. Only generic rank is being compared.

Under a zero W' row of h, the actual composite N->Q lands in D_Q and vanishes by Hom_G(W',D tensor W)=0. The composite to F10 then lands in T and vanishes by ordinary degree. Thus the actual N lies in the constant kernel M10, not merely in an isomorphic ambient.

The coefficient map is correctly directed M10*->H^0(N*), with constant span equal to the image of its dual. H^0(N*) has type D+V, whereas M10=A+V+P, so the span lies in the actual constant V-isotypic three-space. Since N has rank two there, the derivative image modulo E0 has generic rank at most 3-2=1. This is a derivative in a constant subspace, not a quotient connection. It contradicts the previously established rank two. The exclusion is complete and noncircular.

## 4. Section 3: the nonzero Q5 extension and complete dual test

The exact extension P(-6)->Q5->O(2) is an actual extension of saturated bundles. A zero equivariant extension class would embed O(2) in the constant seven-space bundle, impossible by ordinary degree. Equivariant Ext is the invariant part of ordinary Ext because the finite group is linearly reductive over C. Its dimension is one by the single P constituent in H_6=V+P.

The functional representing the class is correctly written on P* tensor H_6, not just on H_6. After twist three, the connecting map is H_5->P tensor H^1(O(-3)). The pairing identity tests every lambda in P* and every t in H_1. If the connecting map vanished, the extension functional would annihilate the image of id_(P*) tensor multiplication. Binary multiplication H_1 tensor H_5->H_6 is surjective, so this would annihilate its entire domain, contradicting the nonzero extension class. There is no missing dual factor and no reliance on a chosen self-pairing of P. A harmless uniform Serre-duality sign does not affect this argument.

The derivation of P tensor W=W'+T6 is valid reciprocity: W' and T6 each have multiplicity one, and their dimensions exhaust eight. Since H_5=T6 is irreducible, the connecting map is injective with W' cokernel. The exact cohomology sequence therefore gives H^0(Q5(3))=0 and H^1(Q5(3))=W'.

Vanishing of H^0 bounds every ordinary splitting degree by -4. Rank five and total degree -22 permit exactly the two listed partitions of the deficit two. In the (-6,-4,-4,-4,-4) case the canonical rank-four top is cohomologically zero after twist three; the canonical bottom quotient is O(-6) with no character ambiguity and produces W, not W'. This correctly excludes the case without pretending that a bottom embedded line is canonical. In the remaining case the bottom coefficient representation is W' because H^1(O(-2)) is trivial. At twist four, chi=H_6-P=V identifies the top coefficient representation. The remaining ordinary extension splits since H^1(O(1))=0, and averaging makes the splitting equivariant. This is only a type classification, not a horizontal splitting. Q5=V(-4)+W'(-5) follows.

## 5. Section 4: actual intersection in the primal seven-space

The coefficient span of the original degree-ten curve restricts to exactly Z*, so S intersect ker p10 is the actual constant C7. This follows from the original span under a constant restriction and does not transfer an auxiliary curve's span.

For L5=ann_S(R13), rank five is correct. The bundle contains rank-three x2. It also contains y and its first intrinsic jets: R13^+=R15 and y(R15)=0 make the differentiated constant pairing vanish. Their constant projection to C7* is the actual first-jet map of y7. Its generic rank two, combined with the rank-three kernel contribution x2, forces the generic projection image to be exactly Q2's generic fiber. No saturation of a projected coherent image is assumed.

Ordinary linear algebra over the generic field gives R13 intersect C7=ann_C7(Q2). The proof then separately establishes saturation on the left as a kernel with quotient embedded in (C O)/R13, and on the right as the annihilator of a subbundle. The left quotient is torsion-free and therefore locally free on the smooth curve. Equal generic fibers of these saturated subbundles give equality everywhere, including D12.

Finally Q2^perp=Q5 is an identity in C7* under the constant symmetric form. Applying its directed isomorphism b7:C7*->C7 gives precisely b7(Q5)=ann_C7(Q2). This is the correct primal/dual conversion; scaling the form has no effect on the image. The actual equality and the type assertion in (4.3) are consequently both valid.

## 6. Section 5: common octic image and exclusion of the zero T6 row

If the T6 row vanished, the nonzero W' row is onto. Its base divisor is invariant, has degree at most seven, and is therefore empty under the minimum twelve assumption. Its line kernel has degree -10 and standard linearization. Thus the actual canonical T6(-3) block lies in ker h and transports to a genuine J6 in ker f, hence in M10 O. Independently the canonical top of actual R13 supplies J6'.

Both inclusions into E0 project to the degree-minus-three top of E0/D0. Their V(-4) components vanish by ordinary degree and W' components by irreducibility. Their T6 components cannot vanish: otherwise a rank-six inclusion would factor into rank-five D0. Hence both project isomorphically onto the same canonical T6 constituent. This does not identify the two rank-six subbundles in E0.

The unique equivariant scalar-map line O(-8)->T6(-3) is the complete fifth-power inclusion with the indicated twist, and is everywhere injective. The map Hom_G(O(-8),E0)->Hom_G(O(-8),E0/D0) is injective because its kernel Hom_G(O(-8),D0)=(D tensor H_6)^G vanishes. The two scalar Hom lines have the same nonzero quotient image, so injectivity forces their lifts to be the same line. The independent block count (0,0,1,0) confirms dimension one. No relative scalar value or normalization is needed.

The common image is therefore an actual nonzero line subbundle contained in both R13 and M10 O, hence in R13 intersect C7 O. For the already proved intersection type, Hom_G(O(-8),V(-4)+W'(-5)) equals (V tensor H_4)^G+(W' tensor H_3)^G=0. This contradiction excludes the zero T6 row. The crucial argument is equality of scalar-map lines in an injective Hom map, not equality of unrelated same-typed subbundles. No moving inverse is differentiated.

## 7. Section 6: the complete degree-seven kernel and endpoint

H_7=W'+T6 is multiplicity-free, and each relevant component Hom space is one-dimensional. Complete degree-seven evaluation is nonzero on both constituents because it is the evaluation of their nonzero section subspaces. Thus an actual h with both components nonzero is obtained from complete evaluation by an invertible constant block automorphism. This asserts existence only, not a computed scalar ratio.

The universal kernel of H_7 O->O(7) is H_6(-1), identified by divisibility by the vanishing linear form at the variable tautological line; the determinant-one convention supplies the equivariant identification. Twisting by -3 gives (6.1), with rank seven and degree -28. Transport through the actual quotient-map kernel isomorphisms gives the type of G7. No new embedded equality with K1 follows, and none is claimed. The concluding restrictions correctly distinguish actual fourth-order projected seven-space jets from any higher-jet conclusion for another curve or the full original degree-eighteen system.

## 8. Entire direct-original review: PR1242

I read and checked the complete original, including its statement, provenance, and Sections 1-8, not merely the portions imported by the new proof.

- Section 1 accurately retains actual maps and full conditional hypotheses; the V versus C7* distinction is explicit.
- Section 2's canonical D0 and N statements follow from maximal ordinary degree and the displayed equivariant Hom vanishings; their direct sum is a subbundle, not a horizontal choice.
- Section 3's zero D-row contradiction uses the actual quotient R13/R11=W(3). The unique map D(-2)->W(3) factors through quartic evaluation and the Euler inclusion; its S4(-3) kernel cannot map into R11 by ordinary degree.
- Section 4 excludes ranks one and two using the saturation degree versus the globally generated image after twist two. The rank-three minors have degree six, so their common divisor is empty. The rank-two kernel's degree -10 and impossible unequal top force ordinary type O(-5)^2; cohomology and center parity identify W', not W or characters.
- Section 5's only nonzero Ext block is End_G(W'), and its nonzero class is the physical Euler extension with middle P(-4). The two abstract alternatives are exhaustive but not themselves an incidence proof.
- Section 6 supplies that incidence proof: the zero alternative places canonical N in R13 and the constant Z block. Actual y first jets and x2 annihilate N; the nonzero actual y_Z top symbol generates x3 modulo x2. Complete degree-ten jet annihilation gives H_6(-4), which cannot contain W'(-3). The symbol is of actual constant-ambient differentiation, not a quotient connection.
- Section 7 identifies the actual Euler subextension E4 and splits only the subsequent zero-Ext type calculation. Its conclusion supports the canonical T6 top used in the new proof.
- Section 8 correctly proves the actual V(-4)->V O row nonzero from saturation and the constant A intersection, then excludes ranks one and two by degree inequalities. Its degree-twelve determinant has reduced invariant support; DVR Smith exponents sum to one. The resulting R13->F18 is explicitly only a sheaf injection over D12, with the correct reduced cyclic cokernel. This result is not confused with a subbundle inclusion in the new proof.

No gap was found under this original's retained transitive hypotheses.

## 9. Entire direct-original review: PR1243

I read and checked the complete statement, provenance, and Sections 1-6.

- Section 1's actual diagram, constant p10 restriction, M10 type, original first-jet annihilator, and K type are consistent with the other direct sources.
- Section 2's universal quartic maps have the stated directions. Multiplying fourth and third tautological powers by a square gives the scalar and first-jet sixth-power images. The other H2 row kills W(-5) by the explicitly decomposed Hom vanishing.
- Section 3 accounts for every coefficient row of a hypothetical D0 inclusion in M10 through the H2+H6 coefficient decomposition. Rank five rules out a zero H6 row. The actual composed degree-six scalar curve is nonzero, and its actual first jets remain in D0, so it lies in K. The two Hom vanishings against K exclude it. No connection on an abstract D0 splitting is used.
- Section 4 correctly transfers the canonical D top through the quotient, rules out its vanishing under g, and identifies the unique nonzero row with the saturated universal degree-five evaluation kernel.
- Section 5 uses an actual preimage B8 if h vanished. Its annihilator extension has zero equivariant Ext and hence an O(-4) subline; the actual constant restriction embeds it in S0, whose retained exact sequence forbids that line. Nonzero h is onto because its degree-seven base divisor must be empty.
- Section 6 obtains onto f by the actual shared-T diagram and derives the canonical kernel isomorphisms. It asserts only rank and degree, not the new splitting type, so the focused proof does not use its own conclusion circularly.

No gap was found under this original's retained transitive hypotheses.

## 10. Entire direct-original review: PR1240

I read and checked its complete statement, provenance, and Sections 1-11.

- Sections 1-2 retain the stationary-uniqueness premise and actual projected vanishing sequences explicitly. The formal DVR jet-minor lemma has a nonzero Vandermonde leading coefficient, including when individual falling factorial entries vanish. The minimum maximal-minor valuation correctly equals the saturation length.
- Section 3's principal-parts degrees, local deficits, and saturated degrees are consistent for all seven rows. In particular Q4 has degree -24 and Q5 degree -22. The annihilator of saturated Q6 is a saturated degree-minus-eighteen line.
- Section 4's cofactor orders, after removing the common valuation, yield the reflected sequence with distinct component orders and full coefficient span. The independent anti-triangular constant-pairing argument also proves full dual span and biduality without a moving inverse.
- Section 5 applies the retained stationary-uniqueness theorem to two invariant complete seven-space coefficient images. The inverse involved is solely between fixed constant coefficient spaces. Its transpose gives the correct direction V->V*. The fixed A and P representations are orthogonal, so every equivariant map between these multiplicity-free blocks is symmetric; the constructed map is already an isomorphism.
- Section 6 differentiates only the constant-form zero pairing. The resulting generic orthogonality extends as a bundle identity and saturation gives Q_r^perp=Q_(7-r). The degree-zero quotient Q4/Q3 has a nondegenerate line form.
- Section 7 derives the actual annihilator incidence from the original forward chain. Generic rank plus an equal-degree determinant proves the projection L9/x4->Q4 is an everywhere isomorphism, rather than presuming saturation survives projection.
- Section 8 places the actual L9 in x5+Q4 and describes its quotient graph. The three actual complete-flag symbols turn the nonzero a_Z into a nonzero graph line map. The associated-graded Leibniz argument is valid without evaluating coefficients. Equal degree makes the map an isomorphism, giving both actual intersections.
- Section 9 descends both fixed form lines to nondegenerate line forms. Each restriction to the graph is nonzero, so the one-dimensional kernel in their two-dimensional sum has both components nonzero. Its block form is nondegenerate and vanishes on all of L9, proving maximal isotropy. Uniqueness is restricted to these specified form lines, as required.
- Section 10 correctly directs the constant form S*->S, identifies its image of L9 with actual Bhat, and then uses the actual D(-6) inclusion and Schur's lemma to identify the quotient as P(-6). This supports the new Q5 extension without assuming a type from rank and degree alone.
- Section 11 maintains the conditional and computational boundaries, including the distinction between third-order Q4 and fourth-order Q5.

No gap was found under this original's retained transitive hypotheses. The stationary-uniqueness theorem remains an explicit transitive premise, not a theorem reauthenticated here.

## 11. Entire direct-original review: PR1236

I read and checked its complete statement, provenance, and Sections 1-10.

- Sections 1-2 specify the original ambient data and use the actual annihilator transpose to prove saturation of beta_E0's A(4) image and full derivative of E19. The annihilator-forward identity uses saturated actual bundles; no rank-seventeen general theorem is imported.
- Section 3's two nonzero projected W-to-A Euler rows are saturated graph inclusions, yielding actual R13 and R15 with the stated intersections and degrees.
- Section 4's constant quotient q cannot have rank one by the low-degree W' absence; its degree-six minors then give a saturated rank-two inclusion. Its nonzero derivative onto O(4) forces pi(E0) onto V_alt O. The actual R13 intersection and internal normal line O(8) follow. The subsequent splitting is used only for Hom calculations.
- Sections 5-6 isolate the nonzero O(16) projected row by the actual rank obstruction, identify its one-dimensional universal gradient line, and prove its surjectivity from reduced f12. The possible internal row on its kernel is exactly a multiple of f12; it is not assumed nonzero.
- Section 7 rules out the zero internal row by constructing the actual rank-sixteen span N inside the original degree-ten annihilator. The projected first jets have generic rank two and equal determinant degree, proving saturation after projection. Transposing their actual derivative factorization then forces beta_N=0, incompatible with negative degree. All derivative directions are actual constant-ambient ones.
- Section 8 keeps coherent image W(5) separate from its saturation O(6)+O(16). The equivariant Ext vanishes, the determinant is a nonzero f12 multiple, and the onto projected row ensures the reduced cyclic local defect.
- Section 9 obtains the exact saturated rank-seventeen annihilator and its final onto derivative by the vanishing high-degree row and nonhorizontal negative degree, closing the flag in the actual constant S.
- Section 10 correctly does not turn that forward closure into a K1 exclusion or a new degree-eighteen jet claim.

No gap was found under this original's retained transitive hypotheses.

## 12. Packet documentation and checker audit

README.md, INPUTS.md, INPUTS.json, and PROVENANCE.md agree with the frozen proof's endpoint, source pins, actual-map imports, and computational restrictions. Historical publication-status wording in the retained originals is transparently preserved and is not misrepresented as this packet's status. The author evidence is clearly labeled non-independent. FROZEN.json binds exactly ten core files and excludes itself, author evidence, and raw responses. Its external hash is independently fixed above.

I inspected all of verify.py. It reads only the ten named core files and FROZEN.json, uses explicit runtime `check` calls rather than removable Python assertions, and has no network calls, subprocesses, directory scan, source-instance input, or hidden dependency on author evidence. Its nine-character fixed W-multiplication graph and recurrence stop at H_7. The character checks are finite formal identities, not a derivation of geometry. The listed degree/rank checks are correct, including Q5's deficit two, L5's rank budget, the hypothetical -10 W' kernel, and the final seven-dimensional kernel of degree -28.

The checker validates the recorded source metadata, but cannot prove that a fetch or full reading occurred; the fresh reviewer connector calls and the present mathematical review independently supply those obligations. Likewise checker success does not establish nonvanishing, saturation, actual incidence, or any actual source-instance rank. This limitation is accurately disclosed throughout the packet.

## 13. Two fresh selected-only replay directories, four executions

I created two new empty directories, separate from the author's replays:

1. `/tmp/reviewer-gluing-kernel-selected-1-xcndmnzy`
2. `/tmp/reviewer-gluing-kernel-selected-2-thg11ybi`

Each received exactly the ten FROZEN.json core paths plus FROZEN.json. No reviewer report, author evidence, raw response, preparatory text, or other file was copied into either directory. I ran the runtime Python executable once normally and once with `-O` in EACH directory. All four exited 0, emitted no stderr, and passed all 116 explicit checks. Complete stdout was identical in every run, with SHA256 `5d0eced28c3b4258868f7fa14ff51265fcfb22ed33be8004b0303f11ea145d1c`; empty stderr has SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

REVIEWER-REPLAYS.json records complete before/after file inventories with sizes and hashes, the exact executable and arguments, UTC times, return codes, full stdout and stderr, output hashes, and parsed results for every run. It also binds the original packet's before/after inventories. Both selected directories and the original ten-file core plus freeze were unchanged. The replay script and separate complete output files are retained under evidence/.

## 14. Final acceptance and limits

There are no required mathematical, provenance, or replay corrections. Acceptance is bound to the exact proof, checker, and entire core hashes in Section 1, not to a mutable title or branch. ARTIFACT-MANIFEST.json binds the final reviewer artifacts and independently rechecks the external frozen core; it is not an upstream publication operation.

This review used no selected actual HM/source coefficients, parameters, points, tensors, matrices, normalizations, jets, eigenlines, or instance ranks; no broad scan, large computation, historical enumerator, quotient connection, differentiated moving inverse, or horizontal splitting; and no GitHub write, local Codex operation, merge, upstream submission, or frozen-file edit. Only read-only source authentication, fixed small byte/character/degree verification, and structural mathematical reasoning were used.

The accepted contribution is a new necessary actual compatibility in the retained conditional branch. G7 and the top of K1 merely share an abstract equivariant type; the proof neither equates them nor establishes further derivative or coefficient-span properties. Publication selection remains the parent's separate responsibility after this accepted entire-proof review.
