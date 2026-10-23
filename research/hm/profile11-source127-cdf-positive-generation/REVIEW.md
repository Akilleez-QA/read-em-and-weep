# Independent whole-proof review

Review date: 2026-10-23 UTC.

## Verdict and exact reviewed package

**PASS, with the conditional scope stated in the proof.** I independently read the entire new proof, all three immediate pinned proof documents, the verifier, reproduction instructions and manifest. I reconstructed the new deductions rather than treating the checker or the author's summary as a mathematical certificate. I found no mathematical gap in the new theorem on the authenticated dependency interfaces.

This verdict binds the following SHA-256 hashes of the final reviewed files:

- `PROOF.md`: `af574b04eb9d96a1117f8cfee327429bb9e38b4bad3932db4f45af849d4480a2`
- `verify.py`: `c308f2c48373bcd2184ff3c0020f1fb95725d41fc2bca058c5f1fcf4f5f17710`
- `REPRODUCE.md`: `f1f3510e28673c7a268bec6f0458c11d05f1a6d01f67539d61c858f52ab36ec4`
- `audit-inputs/manifest.json`: `c4f738ff926949137e22a31b4987895c8741083e1ffc1caf1648970c8ef808f9`

All four matched the frozen handoff before review and again after the checks. I did not edit any of these files or the three input proofs. This review is authored mathematical review, not formal proof-assistant verification.

## 1. Independent authentication and dependency scope

I fetched each complete input through the repository connector at its exact immutable commit and path, using its base64 source-byte response. For each response I decoded the bytes, compared them byte-for-byte with the local audit input, and recomputed the Git object hash as SHA-1 of `blob <byte-count>\0` followed by those bytes. All three matched both the connector's returned blob identifier and the recorded input identifier. This authenticates against repository originals, not merely against a locally self-consistent manifest.

1. **PR476 / actual generation.** Commit `3aa461bc3581fb72fbf923fbe869ddee023b435a`, path `research/hm/five-generator-module/PROOF.md`, Git blob `3d308f6fbdb5c224a085b41eec26e917a6031692`, 8,920 bytes. The local file SHA-256 is `e05d41c601aac6d89b427b4ed036e8b83a400375a53504d96a605d35646143e6`.
2. **PR818 / grading and marked extension.** Commit `f4a73af666900ad2cb34a756d24b88e19dd6feaa`, path `research/hm/negative-truncation-extension/PROOF.md`, Git blob `2ba0a7eee6ef2eb5413683e85618d7902dca3970`, 16,647 bytes. The local file SHA-256 is `7525df1e58ac8683a5a0b828209f4f35cc79a09527307ee47b35025d5c2ad636`.
3. **PR924 / represented c-d-f algebra and actual bridge.** Commit `c6c25eaf0e5a67c27eee7c3ba4f000df55997692`, path `research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md`, Git blob `83f5aee293995257459229e6b323522224ce8f3d`, 18,095 bytes. The local file SHA-256 is `0d740d6f70de924b0442af71cb37e050165efbe9ab984a76f0e1e40b5d27a599`.

### PR476 is the needed actual cover

The generation input defines `K_d=H^1(End_0(F)(d-1))` with its actual cohomological polynomial action. Its Section 1 obtains actual multiplication from naturality of the monad edge maps, not just matching representations. Section 2 uses that multiplication in the coordinate Koszul sequence and closes the next generation step by universal exterior contraction. Section 3 checks the negative tail, assembles the remaining actual multiplication surjections and vanishing bounds, and concludes the graded surjection `Sym(T_coord) tensor K_0 -> K`. Thus the interface used here really is degree-zero generation of this module. It is not an arbitrary presentation with the same character or Hilbert function.

I checked the internal degree bookkeeping and the direction of that conclusion. The new proof needs neither the identification of every higher relation nor the assertion that low relations generate the full kernel. PR476 explicitly leaves higher relations unresolved; the new proof does not silently fill them in. The imported vanishing and multiplication theorems used inside PR476 remain transitive premises; this review is not a fresh recursive authentication or reproof of that entire historical chain.

### PR818 supplies universal, not source2-specific, interfaces

Section 1 identifies `N_2=K_3^+`, `N_3=K_4^-`, `N_4=K_5^+`, with the same actual negative variable in each successive multiplication. Its rule is `m_t(K_d^sigma) subset K_(d+1)^(tau sigma)` when `t` has sign `tau`. This fixes both degree shifts and parity.

Section 4 defines the positive quadratic test and proves that it is necessary for a full five-variable window endomorphism, not sufficient. Section 5 proves the marked-submodule criterion for any equivariant negative subpencil. I independently checked that proof: the minimal span generated in degrees 3, 4 and 5 has positive degree-five piece

    Sym²(T_+) X_2 + Sym²(W) X_2 + W X_3 + X_4.

Negative-pencil stability handles the two terms involving W; the positive quadratic term is exactly the remaining condition. Mixed-sign products lie in the unmarked degree-five parity. This argument is about actual images and survives arbitrary module relations. Its sufficiency neither demands a direct summand nor prescribes other degrees. No source2-specific radical dimensions, algebra types, or decomposition is imported into the new proof.

The full-module scalar theorem uses the degree-zero generators and their actual Euler relation. It is correctly kept separate from the new argument and from the window-only problem.

### PR924 supplies a represented algebra, not just an abstract algebra type

I read all seven sections. The proof treats all constant endomorphisms preserving the source, including singular maps. Its block argument and its covariant, fully faithful reconstruction identify the whole fixed-variable equivariant pencil commutant, not just its units. The actual identification uses the same original A and B maps and one determinant convention on W. Consequently composition, the two negative intertwining equations, and the radical's represented components are transported simultaneously. Replacing these with unrelated representation isomorphisms would not suffice; the pinned proof explicitly does more.

The immediate interfaces needed here are:

- `e=(a,b,d,w)` with product `(aa',bb',dd',a w'+d' w)`, for rightmost-first composition;
- `e_2` has the two diagonal scalars a and b on nonzero blocks of dimensions 17 and 24, with no L block or radical action there;
- `e_4` has diagonal scalars a, b and d on blocks of dimensions 9, 21 and 7;
- the radical arrow goes from the L block to the F block, and every nonzero radical element acts on N_4 (actual K-degree five) as a nonzero scalar multiple of the P projection `V+P -> P subset P+D`;
- the radical rank triple is `(0,8,4)` and its dimension is one.

The nonzero P map is established from an actual nonzero bundle map and its complete coefficient inclusion under Serre duality. It is stronger than an allowed-character calculation. The middle rank follows from the nonzero Wp channel together with surjectivity of the actual B pencil forcing the T channel to be nonzero. The quoted image and kernel dimensions therefore agree with this represented action. The new proof uses PR924's universal conclusions, without selecting its classification parameter. PR924's imported classification, full-faithfulness and original actual-presentation theorems remain transitive hypotheses of this review.

## 2. The new parity-factorization lemma

For every coordinate monomial of degree at least three, two coordinate factors have the same inversion sign. Their product is in either `Sym²(T_+)` or `Sym²(W)`, and is inversion-even. Removing that pair preserves the coordinate monomial's sign.

The generator's sign must also be included. The proof does include it: decompose `M_0` into its two involution eigenspaces and use the equivariant degree-zero cover. Projecting a lift to the required total eigenspace is valid in characteristic zero. For a tensor of coordinate sign tau and generator sign eta, removing an even pair preserves the total sign `tau eta`. Thus the remainder maps into exactly `M_(n-2)^sigma`, regardless of the generator's sign. No assertion that all five actual generators have one parity is used.

This gives the spanning identity in the free cover and then its image in M. The reverse inclusion follows from multiplication's parity rule. Unknown or nontrivial relations can identify or kill summands, but cannot destroy this spanning equality. No inverse to the cover and no canonical representative in a quotient is needed.

At `n=5`, `sigma=+`, the identity is precisely

    N_4 = im q_+ + im q_-.

The two images need not be disjoint. Both maps aggregate all quadratics of the indicated type. The lower bound `n>=3` is genuine: a degree-two monomial with one variable of each sign has no such pair.

## 3. Surjectivity of the two asserted projected channels

For a radical element, the actual negative commutation equations and `j_2=0` give

    j_4 B_u A_v = B_u j_3 A_v = B_u A_v j_2 = 0.

Hence j_4 annihilates the entire image of q_-. Applying j_4 to the new image equality gives `im(j_4 q_+)=im j_4`. The latter is the four-dimensional P by the authenticated represented action. This proves the claimed surjection for every nonzero j; it does not infer nonvanishing from full-module scalar rigidity.

The analogous statement for the whole scalar-target block is also valid. The element `(0,0,1,0)` is an actual pencil idempotent with zero N_2 component, and its N_4 component projects onto the seven-dimensional L block `V+P`. It too kills `im q_-`. Applying that projector to the image equality therefore makes the L projection of q_+ onto all `V+P`. The radical P channel is its subsequent P projection, followed by a nonzero scalar.

These statements are intrinsic after transporting the chosen normal form. Rescaling the generator of the one-dimensional radical changes neither its image nor the surjectivity assertion. Neither argument proves that one fixed positive quadratic has a surjective component.

## 4. The marked-filtration conclusion

Since the radical is one-dimensional and square-zero, its joint image and common kernel are those of any nonzero j, with `U subset Vker`. The dimensions `(0,8,4)` and `(41,46,33)` agree with the actual total dimensions `(41,54,37)`.

For U, its degree-three marked part is zero, so the positive-quadratic condition is vacuous. The minimal full polynomial span of its marked pieces therefore is a legitimate extension with the prescribed intersections.

For Vker, the degree-three marked part is all N_2 and the degree-five positive marked part is `ker j_4`. The extension criterion is exactly `j_4 q_+=0`, which contradicts the proved surjection onto nonzero P. The separate direct check is correct as well: any graded submodule containing N_2 must contain both quadratic images and hence all N_4. It cannot have positive degree-five intersection equal to the proper kernel of j_4.

Consequently the marked common-kernel extension and the nested marked pair are impossible, while the image extension exists. This does not assert that the latter is generated in degree zero, splits K, or has a prescribed Hilbert function elsewhere. The supplied interfaces contain no premise forcing the common-kernel extension under source occurrence, so its failure is not a contradiction to occurrence.

## 5. Compatible algebra and idempotents

Suppose a pencil endomorphism e has `e_2=lambda id` and satisfies the positive-quadratic test. The test gives `e_4=lambda id` on `im q_+`; the negative squares give the same equality on `im q_-`. Their sum is all N_4, so `e_4=lambda id` everywhere. The represented algebra then forces `a=b=d=lambda` and `w=0`: the first two scalars are visible on the two nonzero N_2 blocks, d on the nonzero L block in N_4, and w on the faithful nonzero off-diagonal P map. No invertibility hypothesis occurs at any point, and no middle-component-only endomorphism is left over because the exact represented algebra has already been identified.

This verifies both the injectivity on the two-dimensional `(d,w)` subspace and the resulting at-most-one-dimensional kernel after quotienting by the common scalar line. The scalar quotient here is only a vector-space quotient; it is not used as an algebra quotient.

For the stronger assertion, direct expansion confirms the product identity

    Theta_+(ef)=e_4 Theta_+(f)+Theta_+(e)(1 tensor f_2).

Thus `D_+=ker Theta_+` is a unital complex subalgebra. The map `pi(e)=(a,b)` is an algebra homomorphism by the correctly oriented product law. If its value is zero, the preceding argument with `lambda=0` makes e zero. Its image is therefore a complex linear unital subalgebra of C² containing the diagonal, so is either the diagonal or all C². This proves exactly the C/C² dichotomy, without assuming a compatible map is invertible.

In the second case, the preimage p of `(0,1)` exists and is unique. Multiplicativity and injectivity imply `p²=p`. Substitution of `p=(0,1,d,w)` into the product law yields `d²=d` and `d w=w`, with no sign or opposite-algebra reversal. Accordingly either `(d,w)=(0,0)`, or `d=1` with one w fixed by the actual compatibility map. The latter is a parameterized type across possible maps, not a claim that all w are compatible for one map. There are only two structural types, not a proof of finitely many universal w values. The proof states this distinction.

Both p and `1-p` are compatible idempotents. Commutation with q_+ sends their marked image subpencils into the corresponding degree-five image, giving the two marked extensions by PR818. It does not give complementary extensions in the other eigenspaces or degrees, and hence does not give a full-module splitting. No uniqueness of such extended submodules beyond their minimal spans is asserted.

## 6. Verifier, reproduction and evidentiary limits

I inspected the entire verifier before executing it. It reads the three local proofs and the manifest, authenticates their Git blobs against hardcoded expected values, enumerates exactly 126 formal degree-five monomials, and checks both generator signs for 252 total parity checks. It also includes the mixed degree-two negative control and fixed integer dimension arithmetic. It constructs no actual HM tensor or matrix, chooses no actual source parameter or point, performs no differentiation or instance-rank evaluation, uses no network, and performs no large search.

Both commands completed successfully with exit code zero:

    python3 verify.py
    python3 -O verify.py

The explicit `require` checks remain active under optimization. The bounded checks corroborate the stated universal combinatorics and arithmetic. They do not establish the generation theorem, actual-source identification, or the new surjectivity and algebra claims by themselves; those were checked in the written derivations above.

The reproduction note points to the exact commit/path sources and provides a blob-API alternative that verifies decoded object hashes. Its requirement to obtain actual source bytes, rather than HTML, is important. Repository access may be required, as the note acknowledges. The checker does not itself query remote commit/path provenance; the independent remote authentication in this review supplied that separate step.

No selected actual HM/source coefficients, parameters, points, derivative values, matrices or instance ranks were evaluated during this review. Only the two advertised bounded runs, input-byte authentication and fixed file hashes were used. No external state was modified.

## 7. Contribution and stopping boundary

The genuine new structural step is that actual degree-zero generation forces the positive-quadratic action to provide every target component absent from the negative quadratic image. For this represented c-d-f algebra it resolves PR924's previously conditional radical P channel, strengthens it to the whole scalar-target projection, obstructs the marked common-kernel extension, and reduces positive-quadratic-compatible endomorphisms to the precise C/C² alternatives.

The review approves none of the following stronger claims:

- surjectivity for a chosen single positive quadratic;
- determination of the full positive tensor or its relation embeddings;
- sufficiency of the positive-quadratic test for all five-variable window squares;
- a nonscalar full-module endomorphism or a global splitting;
- realization or exclusion of the abstract c-d-f source in the actual HM module;
- removal of a source, stable label, source-dual pair, or frontier count.

The proof keeps these boundaries explicit. Its conclusion is a new conditional necessary-compatibility theorem and a failed marked-extension route, not a source exclusion.
