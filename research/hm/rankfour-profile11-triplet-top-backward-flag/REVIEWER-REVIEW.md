# Independent entire-proof review

## Verdict and immutable binding

**PASS, conditional on the complete retained actual-geometric hypotheses.** I found no blocking mathematical defect in the entire frozen proof. This verdict applies to all of `PROOF.md`, not merely the terminal argument or the executable checks:

- UTF8 length: 16,724 bytes.
- SHA256: `5a9a86e376cce495818f2ffefd0442b0a45e9b249143cf333d48c7ed9d302959`.
- Git blob SHA1 computed locally: `2407aeca994376c073fb4ded46e988bab0c7ca70`.

I read every paragraph of the frozen proof, all of its one complete direct immutable original, all of `verify.py`, all of `characters.py`, the input manifest, and the reproduction instructions. The proof was not edited. This review supplies mathematical reasoning separately from the bounded executable replay.

The resulting theorem is an actual backward-flag and coherent-defect theorem in the common constant ambient. It does not exclude either original K1 or K3, prove realization of either case, assert a new original higher-jet statement, or prove algebraicity. Auxiliary full constant span is neither necessary for the argument nor a conclusion of it. The transitive geometric hypotheses retained by PR1231 remain assumptions; this review does not purport to freshly authenticate every transitive source separately.

## Independent source authentication and selected replay

I independently fetched the complete PR1231 original through both of these read-only routes:

1. The repository path `research/hm/rankfour-profile11-triplet-top-normal-extension/PROOF.md` at immutable commit `192f771436114029ccbaf0413a5e8f96edb6fce5`, using the file-content connector with no line limits.
2. The Git blob endpoint `https://api.github.com/repos/Akilleez-QA/read-em-and-weep/git/blobs/59d734b137e2bfc014a6932ad1844d26a27ac147`.

Both complete decoded UTF8 responses are byte-for-byte equal to `inputs/top-normal-extension.md`. Each is 16,808 bytes, with SHA256 `074dba0e590290f7b811a848b5fb4910ab6eebe5597f855111b66d5cd5fe71d0` and independently recomputed Git blob SHA1 `59d734b137e2bfc014a6932ad1844d26a27ac147`. The immutable path response also reports this blob SHA. The full responses, not truncated display excerpts, were retained and used for byte comparison. `REVIEWER-AUTHENTICATION.json` records the request identities and results, bound to the frozen proof identity above.

I created a new empty isolated directory and copied exactly the six selected files enumerated in `REPRODUCE.md`, preserving their relative paths. I then ran `python verify.py` and `python -O verify.py`, with `PYTHONDONTWRITEBYTECODE=1` and empty `PYTHONPATH`. Both exited zero without stderr and returned the identical PASS object: 47 packet checks and 81 exact-rational universal character consistency checks. Their stdout is byte-identical. Before/after identities of all six source files and all six isolated copies agree, and the isolated final inventory still consists of exactly those six files. `REVIEWER-REPLAY.json` contains the complete output objects, commands, environment details, inventories and identities.

The raw fetches and complete fresh copies are named `REVIEWER-FRESH-*`. The isolated directory and raw stdout/stderr are named `REVIEWER-LOCAL-*`. These are explicitly excluded from publication and from selected replay. No GitHub write, local Codex use, dependency installation, selected actual HM/source-instance evaluation, broad computation, or unapproved large computation was performed.

## Audit of the complete direct original

The direct original explicitly keeps the two original-kernel cases separate when obtaining their common F type, then uses that common type and actual embedded geometric data. Its shared row argument computes F^- in both cases rather than silently transferring a K1-specific assertion to K3. The degree and representation arguments identify actual Z4 as the D block and actual Z3 as the highest block of F^-.

The original's lower U4 derivative comparison uses the actual quotient isomorphism B6/F6 -> B3/F supplied by the sum/intersection data. It therefore identifies the coherent lower O(-10), including its D12 defect, without differentiating a quotient or treating equality of degrees alone as an incidence. This proves U4 is not contained in B. Consequently the restriction of beta_B to F^- has nonzero scalar quotient O(-12), determining its exact kernel C.

The actual image of beta_B is first placed inside the rank-two normal extension E and shown to have rank two and degree -2. Only then does equality of degree prove coherent surjectivity onto E. The classification E=W(-1) correctly uses the required everywhere-surjective scalar quotient E -> O(10), excluding each unequal splitting type; it does not use the invalid inference that a vanishing lower component puts P in the full derivative kernel. The balanced coefficient is W because the section inclusion into Sym11 has only that two-dimensional subrepresentation. Its forward quotient and rank/degree statements then follow from the actual image, not from a transported connection.

Thus the current proof's stated direct inputs B, C, the exact B derivative, B^+, Z3/Z4, and the U3/U4 incidence are present in the complete direct original. The retained actual jet systems and their consecutive line quotients are used under the declared complete transitive hypotheses. The current proof also spells out why the equal-degree consecutive derivative maps give exact coherent jet generation; it does not promote an unrelated abstract splitting to an actual jet identity.

## Sections 1–2: intrinsic kernels, Euler saturation, and capacity

All minus operations are kernels of the intrinsic second fundamental form of the actual subbundle of the constant ambient. All plus operations are its saturated forward span. Every target subsequently described by an abstract type is first an actual quotient of nested embedded bundles. No step differentiates a quotient identification.

The sheaf equality Z4 intersect C = Z3 is justified in both directions. Differentiating Z3 stays inside Z4 subset B, giving inclusion in C=B^-. Conversely, the restriction of beta_F to Z4 factors through Z4/Z3 as a nonzero f12 row, so its sheaf kernel is Z3. Membership in the kernel of beta_B implies membership in the beta_F kernel. The zero divisor of f12 does not enlarge this sheaf kernel, because a nonzero map of line bundles is injective as a sheaf even at its zeroes.

The induced injection O(-2) -> W(-1) is the unique nonzero equivariant degree-one Euler column up to scalar. Its two linear entries have no common zero, so it is saturated and has quotient O. This is stronger than a mere generic injection. Combining that actual inclusion with the exact Z3 jet derivative gives the full coherent O(-4) column of beta_C and kernel Z2. Consequently the complementary quotient is genuinely O(-2), permitting the stated row q.

The capacity inequality is established internally and is valid for the coherent image, not a saturated substitute. For each actual backward kernel Q_i, the induced derivative map on G_i=Q_i/Q_(i+1) lands regularly in G_(i-1)(-2); its Leibniz term disappears modulo Q_i and its kernel is exactly Q_(i+1). This gives coherent injections of successive quotient bundles. Kernels are saturated in the preceding subbundle and hence in the constant ambient, since all relevant quotients are torsion-free on a smooth curve.

If the initial coherent derivative image has rank one, every successive nonzero derivative quotient has rank at most one. It cannot have rank zero while the kernel remains nonzero: the negative top is inherited by subbundles, whereas a horizontal subbundle of a constant bundle in characteristic zero has constant Grassmannian map and degree-zero constant type. Thus there are exactly n rank-one quotients and no surviving horizontal residue. Their degrees are at most c, c-2, ..., c-2(n-1), proving deg Q <= nc-n(n-1).

Applying this to the hypothetical image O(-4) of C gives -70, strictly less than the actual -52. Therefore q is nonzero. Its common-zero divisor is invariant of degree at most six; the minimum nonempty invariant divisor degree is twelve, so q is everywhere onto O(-2). The full Euler subline plus the surjective quotient row yields coherent surjectivity of beta_C onto the entire W(-3), not just saturation of its image.

## Sections 3–4: exact R5 and R3

The row-kernel calculation for N=ker q is sound at each twist. At twist eight the nonzero section map on the irreducible V_alt is injective, excluding splitting degrees >=-8. At twist nine the source V_alt tensor W is the irreducible T6; nonvanishing follows from global generation of the twisted source bundle, so this section map is also injective. At twist ten, the previous top bound limits h0(N(10)) to two, whereas every nonzero subrepresentation of D+P has dimension at least four. Its section kernel is therefore zero. At twist eleven the W' constituent is absent from the target Sym9 but present in the source, and the same rank-two budget forces exactly W'. With deg N=-22 and top N<=-11, this determines N=W'(-11), not merely a possible splitting.

The actual kernel diagram then gives 0 -> Z2 -> R5 -> W'(-11) -> 0. Its ordinary extension vanishes by H1(O(3))=0, and finite-group averaging gives an equivariant splitting. Actual Z2 is the canonical top because no map from its degree -8 block to degree -11 exists. This identifies an actual saturated kernel embedded in C; it does not give a horizontal direct sum.

The second Euler column is also justified from the actual restriction, rather than asserted from type: Z3/Z2 injects nontrivially into C/R5=W(-3), and the one-dimensional degree-one Hom makes it saturated Euler. The Z2 derivative fills O(-6) with exact kernel Z1. If q' vanished, the capacity bound for rank five and coherent image O(-6) would give -50, contradicting -46. The degree-seven quotient row cannot have an invariant common-zero divisor, so beta_R5 fills all of W(-5).

The complementary scalar-row kernel has rank one and degree -18. There are no nontrivial scalar characters. Its extension by actual Z1 splits because H1(O(9))=0 and equivariant averaging is exact. This gives rank three, degree -36, and type W(-9)+O(-18) for actual R3. At this point the scalar summand has not yet been identified with U0; the proof appropriately makes that identification separately.

## Sections 5–6: actual U0 and the terminal nonzero row

The nested containments U2 subset C, U1 subset R5, and U0 subset R3 follow directly by differentiating the retained auxiliary jets in the constant ambient. Each uses both a section's inclusion in the relevant actual bundle and its derivative's inclusion in that same bundle. None differentiates an inverse splitting isomorphism.

The possible graph component of actual U0 into Z1 is exactly Hom_G(O(-18),W(-9)), which vanishes because Sym9=S4+T6 has no W. Its other component is a nonzero endomorphism of scalar O(-18), hence an everywhere isomorphism. Thus the embedded direct sum R3=Z1+U0 is established, and the scalar tail is the existing auxiliary line, not a newly selected abstract line of the same degree.

The third Euler inclusion is obtained from the actual restriction of beta_R5 to Z2. It yields the full O(-8) column and exact kernel Z0 for the restriction of beta_R3 to Z1. The remaining projected row q'' has scalar degree twelve.

The proposed contradiction when q'' vanishes is valid and uses two distinct Hom vanishings. First, a lift of beta_R3(U0) into the Euler O(-8) would have degree ten and is zero because Sym10 has no invariant. This says actual derivatives of U0 lie in R3. Second, the intrinsic derivative of U0 now factors through (R3/U0)(-2)=W(-11), and this map vanishes because Sym7=T6+W' contains no W. O-linearity holds since differentiating a scalar multiple adds a section of U0, killed in the quotient; no connection on R3/U0 is introduced. These two facts would make U0 itself horizontal, contrary to its degree -18. No full-span theorem is used.

Therefore q'' is nonzero. Since its degree is twelve and its scalar linearizations are trivial, its invariant divisor is exactly the unique reduced D12. This proves a simple one-direction terminal defect without selecting a scalar representative, a point, or any actual jet coefficient.

## Section 7: coherent inverse image, cyclic defect, and terminal kernel

The inverse-image description I_R3=pi^(-1)(O(-18)) is an actual equality of coherent subsheaves of W(-7). Surjectivity to the lower quotient is understood onto the coherent image of q'', not onto the saturated O(-6). Locally one lifts that quotient section using U0, then subtracts it; the remaining Euler-line section is filled by Z1. This proves both inclusions and does not discard the torsion defect.

The exact quotient is consequently O(-6)|D12. Since the divisor is reduced, each of its twelve points contributes a cyclic length-one cokernel. The ordinary extension 0 -> O(-8) -> I_R3 -> O(-18) -> 0 splits by H1(O(10))=0, and equivariantly by finite-group averaging, but this abstract splitting is not substituted for the actual inverse image and is not horizontal.

For the actual kernel, projection of a killed section (z,u) to O(-6) gives q''(u)=0. Sheaf injectivity of the nonzero scalar row forces u=0, including at points of D12. The known Euler column then forces z in actual Z0. Thus R3^-=Z0, rather than a larger fiberwise kernel mistaken for a subbundle. Z0^-=0 follows from its nonconstant negative scalar line and actual first jets Z1.

Finally, I_R3 has full rank in the actual rank-two normal target, so its saturation is W(-7); the preimage description of the forward span gives R3^+=R5. The higher two maps were already proved everywhere onto, yielding R5^+=C and C^+=B with no defect. The distinction between the terminal coherent defect and the preceding full normal images is maintained throughout.

## Section 8: mixed coherent sums, lengths, and support

The generic forward-span lemma is valid: on a dense open set where A1+A2 is a subbundle, differentiation of a section of their sum is generated by the derivatives of both summands, and the Leibniz terms stay in the original sum. Equality of the resulting generic subspaces yields equality of their saturations in the constant ambient. This is an argument about actual sections on the open set, not a quotient connection.

Starting from the proved actual direct sum R3=Z1+U0, the lemma gives the stated saturations R5, C, B, B^+. The ranks of the source summands equal the ranks of these saturations, so their generic intersections vanish. Their sheaf intersections also vanish because they are torsion-free. Thus their coherent sums have the degrees of the direct sums, and the saturation lengths are exactly 12, 24, 36, 48. All four rank and degree calculations check independently.

The first local identification needs coherent, not merely saturated, jet generation. That condition is available: the consecutive jet derivative maps between equal-degree line quotients are nonzero everywhere isomorphisms. Hence first derivatives of Z1+U0 coherently generate Z2+U1, and (Z2+U1)/R3=I_R3(2) inside R5/R3. This identifies the first cokernel precisely as O(-4)|D12.

Outside D12, the first coherent sum already equals R5. Differentiating this equality and using the full coherent images for R5, C and B, together with the exact coherent jet-generation statements, gives Z3+U2=C, Z4+U3=B and Z5+U4=B^+ on that same open set. Therefore every later saturation defect is supported inside D12. Their positive total lengths make them nonzero. The proof does not infer that these later defects are cyclic, reduced, or of any particular elementary-divisor type. Its stated local support claim is therefore justified without overreach.

## Checker scope and final boundary

The helper contains only bounded exact rational arithmetic in Q(sqrt(5)), nine fixed physical character values and the fixed tensor adjacency. Its 81 consistency guards use explicit exceptions. The checker authenticates the complete original and complete frozen proof, then checks the finite symmetric-power identities, the two capacity substitutions, the stated ranks/degrees, the Hom multiplicities, the divisor-degree inequalities and the ordinary Ext inequalities. Its guards also use explicit exceptions, so optimization removes none of them. No source-instance parameter, coefficient, point, jet, matrix, tensor, normalization or instance rank is selected or evaluated.

The replay corroborates authentication and bounded universal arithmetic only. The preceding entire-proof audit supplies the independent geometric reasoning. Under the stated retained hypotheses, the proof establishes the advertised actual backward flag, identifies its scalar tail with existing U0, proves the exact cyclic terminal defect, and determines the four coherent mixed-sum saturation lengths with the stated support restriction. Neither K1 nor K3 is excluded. No correction to the frozen mathematical proof is required by this review.
