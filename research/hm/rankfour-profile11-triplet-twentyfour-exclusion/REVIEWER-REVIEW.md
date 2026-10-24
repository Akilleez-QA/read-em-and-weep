# Independent whole-proof review

## Verdict and exact target

PASS. I independently read the entire frozen short proof, all three complete direct originals, the complete character helper and verifier, the input manifest, and the reproduction instructions. I found no mathematical gap in the stated conclusions, conditional on the retained actual-geometric hypotheses and conclusions of the immutable inputs. No proof edits were made or are requested.

The reviewed target is PROOF.md, 13,247 UTF-8 bytes, SHA256 b7f22a08e4c2e740bce1ab3340b88ef631b21f5045055c73f35fffad969c1aa5. The result reviewed is precisely H0(F(4)) contained in A+D, the absence of V and the trivial constituent in H1(F(4)), exclusion of delta=24, and the conditional actual cyclic defect description for delta=20. No stronger exclusion of D is part of this review or of the published assertion.

## Independent source authentication

All three originals were independently and freshly retrieved with complete read-only GitHub file calls at the exact commit and path specified in INPUTS.json. No line-range restrictions or snippets were used. The returned UTF-8 bytes were compared with the entire packet inputs. Their byte lengths, recomputed SHA256 hashes, recomputed Git blob SHA1 hashes, and GitHub-returned blob IDs agree exactly with the manifest:

- PR1212: 16,069 bytes; SHA256 135c74cc09d4f1da1fcae16c330e0c9d5a9d05d615e59a2461dd532cbb91a62f; blob 175af94697c44f3140bb2c1d04978931c255b3fe.
- PR1198: 8,501 bytes; SHA256 4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a; blob 163ba2126b6130befcc2351db7f6910d85fac2ec.
- PR1209: 17,528 bytes; SHA256 33a3c8866f072f4aec607c2d6647222ee0031a3f1bbbaef550e58df5075b3dbf; blob 730021d4e97c4c1307a1d3c6c5303e4e9792202d.

REVIEWER-AUTHENTICATION.json records the complete comparisons and exact source locations. Raw connector responses remain LOCAL-only; they are not publication components or replay dependencies. Authentication verifies the complete direct originals, not a new audit of every transitive historical theorem, whose stated actual-geometric hypotheses remain imported assumptions.

## Mathematical audit

### 1. Actual restriction and distinction of ambients

PR1209 Section 7 proves the actual everywhere bundle injection K^- into J^- induced by the constant restriction p, with locally free cokernel O(4). Its image F is therefore actually isomorphic to K^-, equivariantly and everywhere, not just at the generic point. The new proof uses this isomorphism only to identify splitting bounds and cohomology representations. Its derivative argument is made on K and K^- in their original constant ambient. It neither identifies the original constant span with the fifteen-dimensional projected span nor transfers a rank-seventeen theorem to F.

PR1198 supplies exactly the five K alternatives quoted. Its full-positive conclusion is stated only for K1 and K2, but this causes no logical enlargement here: the new proof explicitly assumes the full-positive branch, as retained by PR1212 and PR1209, before considering the necessary alternatives. It does not newly assert that K3, K4 or K5 has that branch.

### 2. Near-top rigidity and saturation

If U is the specified actual R(-4) subbundle of K and lies in K^-, every local section of U has derivative in K. Therefore its own second fundamental form in the original constant ambient factors through the regular bundle (K/U)(-2). The ordinary direct-summand property is sufficient to bound its top degree by -5. There are no ordinary maps from O(-4) to a bundle with all splitting degrees at most -5, so this second fundamental form vanishes.

U is saturated in the original constant ambient: it is a subbundle of K, which is a saturated actual kernel subbundle there. Thus the Grassmannian map exists everywhere. In characteristic zero, zero differential forces that map to be constant; the resulting subbundle is a constant bundle of degree zero. This contradicts degree -4 times rank U. The proof derives horizontality from the actual derivative condition. It never assumes a Birkhoff splitting is compatible with differentiation.

### 3. The actual top block and representation exclusion

The bound top K^- at most -4 follows from the actual isomorphism with F. After twisting by four, all summands have degree at most zero, so evaluation of H0(K^-(4)) is exactly the degree-zero summand, with no base-point defect. Twisting back gives a canonical saturated degree-minus-four block. A representation summand gives an actual R(-4) subbundle, and its composite inclusion in K is a subbundle inclusion.

For K1, K2 and K3, degree forbids every component into a deeper summand. The remaining map into the degree-minus-four block is constant, and its fiberwise injectivity makes its image an ordinary direct summand. Near-top rigidity excludes all such nonzero sections.

For K4 and K5, the twist-four section representation is A+D+V+P, with multiplicity one. Equivariance and S4 tensor W=A+D forbid V or P from mapping into the cubic block; degree forbids their components into N. Their images would consequently be direct summands of the degree-minus-four block and are excluded by the same argument. A and D are the only remaining possibilities. Finite-group semisimplicity then turns chi_G(F(4))=-P-2D into H1(F(4))=H0(F(4))+P+2D and proves the two asserted constituent absences. This is an equality of actual representation classes and does not assume H1 vanishes.

### 4. Genuine quotient cohomology obstructions

At delta=24, the retained coherent I has scalar lower quotient O(-22), yielding an actual everywhere quotient F to O(-22). Its kernel is locally free. The long exact sequence after twisting by four is surjective from H1(F(4)) to H1(O(-18)), because coherent H2 vanishes on the projective line. Serre duality with the fixed determinant and self-duality conventions gives H1(O(-18))=Sym16 W=V+P+2D. The missing V in the source is a decisive obstruction in the semisimple category.

Exactly the same reasoning excludes a quotient F to O(-18): the target after twisting is H1(O(-14))=Sym12 W=1+A+P+D, with a trivial constituent absent from the source. These are actual quotient maps, not chosen negative summands of F. The canonical quotient by the highest-slope line of I already suffices, so the argument does not depend on any connection-compatible choice of splitting.

### 5. Defect-twenty capacity and the unequal-top scalar argument

For delta=20, a+b=-8 and the imported coherent-image capacity is used with the correct I, not its saturation E. If a is nonpositive, 10-2k is nonnegative for the entire permitted range 1 through 5, and the bound becomes -90+12k-2k^2=-72-2(k-3)^2. This is strictly below -64. Thus a is positive, which, together with a+b=-8, proves unequal degrees before any scalar top-line claim is made.

The highest-slope line is then canonical and equivariant. Since G has no nontrivial scalar characters, its linearization is the physical O(a). Its nonzero inclusion into E has components in H0(O(2-a))^G and H0(O(10-a))^G. The nonnegative component degrees are all below twelve, and a nonzero positive-degree invariant section would have a forbidden invariant divisor. Hence a=2 or a=10. Equivariant splitting is legitimate: the ordinary splitting can be averaged over the finite group in characteristic zero, or one can use the canonical lower quotient directly. The two possible ordinary/equivariant types are consequently exactly O(2)+O(-10) and O(10)+O(-18). The second is excluded by the actual O(-18) quotient obstruction above.

### 6. Actual O(2) inclusion, orbit uniqueness and local defect

For the retained type O(2)+O(-10), the actual top line cannot have an O(10) component because H0(O(8))^G=0. Its O(2) component must be nonzero and constant, so it identifies the full actual O(2) summand of E with a subsheaf of I. This proves more than an abstract splitting type. The same degree-eight invariant vanishing removes ambiguity in the equivariant complement to E's O(10) line; no horizontal splitting is asserted.

Quotienting by the common O(2) gives a coherent line inclusion of degree -10 into O(10), so it is precisely O(10)(-D_delta), with determinant divisor of degree twenty. The allowed orbit sizes 12,20,30,60 leave only one reduced orbit of size twenty. Uniqueness is also justified: A5 has twenty elements of order three, hence ten distinct cyclic order-three subgroups. Each has two fixed points, no two different such subgroups share a fixed point because finite stabilizers are cyclic, and no stabilizer can be larger while containing order three. The resulting twenty points therefore form one orbit.

The quotient is consequently O(10)/O(10)(-D20). The common full subbundle supplies a unit elementary divisor, and the reduced determinant divisor supplies the other order one. This is the universal local-DVR consequence of the actual sheaf inclusion and not a selected point, coefficient, jet or matrix evaluation.

### 7. Scope and stopping boundary

The necessary defect set is correctly reduced to {0,12,20}. The proof establishes neither occurrence nor further exclusion of any remaining value. Its conditional delta=20 conclusion does not assert that I equals E. It leaves delta=12, both retained F18 splitting alternatives, both original dual-extension classes, the other triplet-image branches, and realization of the full-positive branch open. The original t=0 is not confused with delta. No fourth-jet separation, higher-order integrability, algebraicity or whole-profile conclusion is added.

## Checker inspection and isolated replay

The selected verifier and character helper use only standard-library exact arithmetic, fixed universal physical characters, one symbolic quadratic capacity identity, scalar cohomology-degree arithmetic, orbit arithmetic and source/proof hashing. Explicit RuntimeError checks remain active under optimization. The checker does not pretend to mechanically establish the derivative factorization, saturation, cohomology surjectivity or actual subsheaf arguments; those were reviewed above.

Exactly the eight files named in REPRODUCE.md were copied into an otherwise empty isolated directory. Both normal and optimized Python replay passed all 42 explicit verifier checks, with identical outputs and the exact reviewed proof hash. Bytecode writing was disabled only to preserve the exact selected-file set. The directory still contained exactly those eight files afterward and their contents were unchanged. REVIEWER-REPLAY.json records all eight file hashes and both complete run outputs.

The LOCAL-APOLAR draft, its sources, all LOCAL files, raw fetch responses and exploratory work were excluded from both the proof dependency set and isolated replay. No GitHub mutation, local Codex use, selected actual HM/source-instance evaluation, broad candidate scan or large computation was performed.
