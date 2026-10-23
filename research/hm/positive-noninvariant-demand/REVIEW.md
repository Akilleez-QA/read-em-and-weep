# Independent mathematical review dated 2026-10-23

Verdict: PASS, relative to the two explicitly imported geometric/representation-theoretic inputs. No mathematical gap was found in the new deduction. This is a mathematical audit with bounded exact character checks, not formal proof-assistant certification.

Reviewed proof: `PROOF.md`, SHA-256 `a7c1e8716ef1ade79dac2b7c2bc4b6c986985f69e30bfd3da33513955ce34195`.

The review includes the opening clarification that a standalone positive-linear factorization means `q_D(st⊗x)=b_s a_t(x)` through the same prescribed middle. It is not an ordinary factorization of the linear map `D⊗N₂→N₄`.

## 1. Independently authenticated sources

I read both complete local original inputs, then independently fetched their contents from GitHub at the exact repository paths and immutable commit refs. The returned bytes equal the local originals exactly. Independently recomputing the Git blob hash of each returned UTF-8 file gives the stated blob:

- FACTOR: repository `Akilleez-QA/read-em-and-weep`, commit `1a8fb75aa886f9bb6c07e357759d37630cdd127d`, path `research/hm/profile11-source127-cdf-positive-factorization/PROOF.md`, blob `92e389cc07e7c2e61b64a04b17b91d0c1650c7dd`.
- INVARIANT: same repository, commit `eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c`, path `research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md`, blob `019c1f31773476f0a4877d88632ce5d46fbd4b9f`.

GitHub PR928 metadata independently identifies its head as the cited FACTOR commit. The original factor proof includes the upstream pins for the actual positive coordinate representation, normalized HM monad, cohomology vanishings, actual middle, and character conventions. Its canonical factorization theorem is universal; its middle-character derivation does not assume the c-d-f formal source construction used elsewhere in that file.

I also independently fetched the pinned `verify_negative_vertex_scalar.py` at commit `db51525015bb7c5e825833d550d08dedf6f6ea96` and authenticated its Git blob `9eb58f03edde15dd612087440d8180e9e16d1755`. Its nine traces, class sizes, and definitions of A, V, P, D agree with the conventions used here. I inspected this upstream file; I did not run its additional calculations.

The invariant original states an actual canonical invariant-product theorem with kernel A+D, source A+2V+3P+4D, image 2V+3P+3D, and target 2V+4P+3D. Thus its image dimension is 33 and target dimension is 37. Its statements about the generic sector and higher obstructions are explicitly separate and are not imported into the new argument. D5 and P4 in that original are the D and P used here.

This review authenticates and checks the exact immediate inputs and their use. It does not independently reprove the entire upstream cone-spinor/moving-line/Ext-annihilator dependency chain.

## 2. Invariant projection and normalization

The fixed-character identity Sym²V=1+D makes its invariant line and D-isotypic complement intrinsic. For nonzero q₀ on that line, the unique equivariant functional ε with ε(q₀)=1 annihilates D. Consequently the projection is s↦ε(s)q₀ and the stated q_inv is precisely the actual product restricted to that projection.

Replacing q₀ by a q₀ replaces Q by aQ and ε by a⁻¹ε, so q_inv and q_D remain unchanged. In particular, the image character imported for Q is independent of its nonzero normalization. This procedure selects no actual coefficient, coordinate point, or instance parameter.

The bilinear form (s,t)↦ε(st) is symmetric, invariant, and nonzero. Its radical is a G-subrepresentation of irreducible V and cannot be all of V; hence its radical is zero. Therefore ε♯:V→V* is an isomorphism. The self-duality/odd-dimension explanation in the proof is also valid; symmetry already follows directly from ε being a functional on Sym²V.

## 3. Image inequality and factorization

For h=f+g, f=h−g gives im f⊆im h+im g. The addition map im h⊕im g→im h+im g is surjective. Over C for the finite group G, semisimplicity gives the displayed inequality on each irreducible multiplicity, without requiring directness or a particular intersection. An embedding of im h in the prescribed P then gives the stated lower bound for im g. Positive multiplicities yield a subrepresentation up to equivariant isomorphism, not a canonical complementary subspace.

The application uses f=C_inv, g=C_D, h=C_+; these satisfy h=f+g. Thus the subtraction and every sign are correct. Currying is linear, and C_inv=ε♯⊗Q, so its image is exactly V*⊗im Q.

Actual multiplication by two positive degree-one variables factors through H¹(B(3))₊=K₄⁺. The canonical minimal-factor theorem in FACTOR therefore embeds im C_+ in this actual middle. This statement uses the actual module structure, not any asserted actualness of the formal constructions elsewhere in FACTOR. Conversely, each proposed standalone positive-linear factorization of q_inv or q_D would embed its curried image in that middle. The resulting dimension contradictions 99>46 and 53>46 are valid.

There is no contradiction in their sum factoring: addition of the two maps may make their curried images cancel on common source directions. The proof neither assumes that the separate images are nested nor claims that their sum is direct.

## 4. Independent bounded arithmetic

I inspected `verify.py` in full. It only performs rational arithmetic in Q(√5) on nine fixed abstract classes, constructs the stated character expressions, and authenticates the local input blobs. It contains no actual HM maps, selected coefficients, parameter substitution, matrix rank computation, or unbounded calculation. Its checks use explicit `require` calls, so they survive Python optimization. Both `timeout 10s python verify.py` and `timeout 10s python -O verify.py` completed successfully.

I additionally used an independent explicit-character-row calculation, rather than the verifier's symmetric-power recurrence. Let φ=(1+√5)/2 and ψ=(1−√5)/2, in the nine-class order of the authenticated original. The rows used were:

- 1: (1,1,1,1,1,1,1,1,1).
- A: (3,3,φ,φ,ψ,ψ,0,0,−1).
- V: (3,3,ψ,ψ,φ,φ,0,0,−1).
- P: (4,4,−1,−1,−1,−1,1,1,0).
- D: (5,5,0,0,0,0,−1,−1,1).

With class sizes (1,1,12,12,12,12,20,20,30), these five rows are orthonormal. The zero-based square-class map is (0,0,5,5,3,3,7,7,1). Direct calculation verifies Sym²V=1+D and all three stated tensor-product identities at every class.

The independently calculated characters are:

- L=im C_inv: (99,99,(3+√5)/2,(3+√5)/2,(3−√5)/2,(3−√5)/2,0,0,−1).
- K₄⁺: (46,46,1+√5,1+√5,1−√5,1−√5,1,1,−2).
- L−K₄⁺: (53,53,ψ,ψ,φ,φ,−1,−1,1).

Their irreducible decompositions are respectively (2,6,5,6,8), (1,4,2,3,3), and (1,2,3,3,5) in the order (1,A,V,P,D). All dimension arithmetic checks: 33·3=99; 1+12+6+12+15=46; 1+6+9+12+25=53; 99−46=53. These are identities of fixed representations, not evaluated ranks of actual tensors.

The verifier intentionally checks only arithmetic if its manifest is absent. In the reviewed execution the manifest and both exact originals were present, and both blob checks passed; no missing-input fallback was used.

## 5. Scope and conclusion

The new conclusion follows globally for the actual HM cohomology module from its intrinsic invariant product and actual middle representation. It has no c-d-f source-occurrence assumption. It proves the genuine lower-bound subrepresentation 1+2A+3V+3P+5D in im C_D⊆Hom(V,N₄), so q_D is nonzero and has no standalone positive-linear factorization through K₄⁺.

The dimension 53 is not the dimension of a subspace of the 37-dimensional N₄, not the image dimension of D⊗N₂→N₄, and not the rank of one selected non-invariant quadratic. The proof does not determine sharpness, positions of curried images, actual coefficients, source membership, the scalar/C² alternative, marked mixed squares, or the original source/lifting/Weil-class goal. No such conclusion was smuggled in through a generic-versus-actual substitution.

All review activity was read-only externally. Local writes were limited to this review. No publication, merge, upstream submission, actual/source-instance evaluation, derivative computation, or large computation was performed.
