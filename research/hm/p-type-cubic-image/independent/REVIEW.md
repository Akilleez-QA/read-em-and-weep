# Independent P-type cubic-image review

PASS for the stated necessary-condition theorem, conditional on its explicit actual saturated P-type source hypotheses and authenticated imported results. Full frozen proof, checker, character implementation, manifest, and five complete inputs were read. No mathematical correction required. This is independent written review, not proof-assistant verification.

## Geometric reasoning independently checked

For P-type, PR1140 proves H0(K(3)) is zero or one Wprime. Cubic sections of E consist of the top Wprime+T and displayed Wprime+T. If nonzero kernel Wprime has nonzero projection onto the displayed Wprime, Schur's lemma makes that projection invertible. Its evaluation morphism is therefore a graph over the displayed Wprime O(-3). This graph is saturated in E, and its quotient retains top degree at most -2. The actual quotient E to A kills it, so the actual second fundamental form kills it. The near-top horizontal-negative contradiction rules it out. No projection is assumed horizontal. Thus the kernel Wprime lies wholly in the top P O(-2).

The unique equivariant Hom from Wprime O(-3) to P O(-2) is the Euler inclusion: P=Wprime tensor W and the standard determinant-one Euler sequence gives saturated image and cokernel Wprime O(-1). The top quotient to A kills this inclusion and so factors. The factor is nonzero because strict-top makes H0(E(2))=P inject into H0(A(2)). Consequently Hom_G(Wprime O(-1),A)=0 rules out every nonzero cubic kernel.

For a nonzero factor, its coherent image is locally free, of rank one or two. Rank two implies zero sheaf kernel and image isomorphic to Wprime O(-1); this does not imply saturation in A. Rank one is O(e) since the group is perfect, and a nonzero equivariant map requires Wprime in Sym^(e+1) W. First occurrence is seven, so e>=6. The degree is that of the coherent image, not its saturation.

If H0(K(3))=0, maxdeg K<=-4. K is saturated in the same constant ambient. Strict-top applied to K gives H0(Kminus(4))=0, so H0(K(4)) injects into H0(A(2)). Euler additivity makes H0(A(2))+chi(A(4))-chi(E(4)) genuine. No extra H0(A) term occurs, and chi must not be replaced by H0.

## Evidence

Five complete pinned source files independently retrieved via GitHub connector, compared bytewise after removing the extra newline from local patch transport, then authenticated to the author's manifest. AUTHENTICATION.json retains full URLs, SHA256, Git blob IDs, and byte counts. Stored originals now have exact source bytes.

Independent exact character checker: 682 explicit checks under Python normal and -O, identical RESULT JSON. It uses exact rational Q(sqrt5) class arithmetic, not author's code or tensor recurrence; verifies first Wprime occurrence, unique Hom, source cubic character, source chi4, fifteen Euler character exact sequences, and the universal formal polynomial Euler composition. This is supporting arithmetic, not proof-assistant verification of geometry.

No actual HM coefficients, parameters, points, jets, tensors, matrices, or instance ranks were evaluated. No profile closure, ledger cut, or complete repair is claimed.

## Strengthened revision

The updated converse and complete top-kernel descriptions independently check. A factorization of the actual row through the fixed Euler quotient kills its Wprime Euler subbundle and hence forces nonzero cubic kernel. Abstract nonzero Hom alone is not enough, as the proof explicitly states. Rank-two image leaves exactly the Euler kernel. Rank-one coherent image O(e) gives a line kernel O(-e-2) in Wprime O(-1); pulling back gives an extension of that line by Wprime O(-3). The ordinary Ext1 is Wprime H1(O(e-1))=0 for e>=6. Averaging a splitting over the finite group gives an equivariant splitting. It is noncanonical, not horizontal, and describes K_F rather than all K. No correction required.

## Frozen packet and replay

PASS for the updated freeze. Author verifier: 142 explicit checks, plus 81 character-module tensor-identity checks. Independent verifier: 682 explicit checks. Both pass normal and optimized Python with byte-identical outputs; author replay matches RESULT.json. Five public input files remain unchanged and authenticated. This receipt supersedes REVIEW-original-freeze.md for the revised packet.

PROOF.md SHA256 4b68be856e9504b38bf21dcab29c73a70a6a9065d0281b726360fd2f5ad58091

verify.py SHA256 decd93420db6de12c46994a86c4423818c3e6edcc4d19b1019d72c1177c0d9d5

characters.py SHA256 5b3b1d415f26ca467670afeb73357cbb0e9c125a6b1acd25155b6d85eef4e4f1

INPUTS.json SHA256 1e24b7b623cfa6b37fe92172328bfe7f2b3704e280e65577068d8f06e08c2ade

RESULT.json SHA256 e3d8f0885210cbaadca360574310d2cb483c0753578314361267a24d6d74fe35

The rank-one parity follows from central action: Wprime has sign -1 and Sym^(e+1) W has sign (-1)^(e+1), forcing e even. The maxdeg A<=5 corollary follows because a sheaf injection O(e) into A requires e<=maxdeg A.
