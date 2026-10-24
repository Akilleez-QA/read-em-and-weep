# Independent entire-proof review

## Verdict and exact binding

**ENTIRE-PROOF PASS, conditional on exactly the imported actual-geometric hypotheses.**

I read every byte of the complete frozen `PROOF.md` (13,289 UTF8 bytes), both complete direct original proofs in `INPUTS.json`, and both complete Python sources. This verdict binds only:

`PROOF.md` SHA256 `9da994c73b8c5365de31fc8b5552ba364bfc6af624108acdb8567feba9365103`.

I found no mathematical gap in the exclusion of the intersections of original K4 and K5 with the retained full-positive triplet, original t=0, local delta=12, residual simultaneous rank-seven, forced k=2 geometry. The conclusion is not a closure of that branch. With the imported K2 exclusion it leaves K1 and K3 as necessary alternatives, without asserting their realization or impossibility.

This is a review of the entire new argument, not a verdict inferred from successful arithmetic. The two direct original proofs were read completely; their stated transitive actual-geometric hypotheses are retained, not silently removed or claimed to have been independently reproved here.

## Fresh original authentication

I independently fetched each original twice through the read-only GitHub connector: once by its immutable commit and repository path, and once by its exact Git blob. For each of all four complete returned contents, I reconstructed UTF8 bytes, calculated their complete length and SHA256, computed the Git object SHA1 with the exact `blob <length>\0` header, and compared the bytes with the local original. Every comparison passed. The path responses also returned the expected blob and exact immutable URL. The blob responses expose content rather than a separate SHA field; their requested object and recomputed complete Git hash bind them to the expected blob.

1. PR1226, commit `c565bd8b5b65829e99bdd96a7c5f076b01050465`, path `research/hm/rankfour-profile11-triplet-simultaneous-kernel-two-exclusion/PROOF.md`: 13,703 bytes; SHA256 `0165fa9a854879e5b2c67885f3b0bede6c3f48b34e1c761c0ca846645a3247fa`; Git blob `cb46875b07d8d79e82aebe980685c418d975d87b`.
2. PR1198, commit `7d71f0e2a3963cff64a069198f4415c5cfd0fe9b`, path `research/hm/rankfour-profile11-triplet-kernels/PROOF.md`: 8,501 bytes; SHA256 `4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a`; Git blob `163ba2126b6130befcc2351db7f6910d85fac2ec`.

`REVIEWER-AUTHENTICATION.json` records the results. The four raw connector responses are in `REVIEWER-FRESH-SOURCE-FETCHES.json`, which is excluded from publication and replay.

## Audit of the imported actual geometry

The full coherent endpoint image A(2) is an explicit retained branch hypothesis for the cubic alternatives. It is not inferred from PR1198's full-image theorem, which proves that assertion only for K1 and K2. What PR1198 does prove for all five necessary alternatives is the actual V_alt(-4) row's everywhere-surjective image onto the fixed canonical W(1) in A(2). Its proof uses the near-top coefficient injection, absence of V_alt in Sym8 W, the rank-one parity/degree obstruction, and the invariant minor-divisor bound. Its kernel is therefore an actual line of degree -14. Perfectness of G fixes the scalar linearization. The new proof uses precisely this all-five conclusion, not the stronger two-case conclusion.

The complete PR1226 proof first propagates the small jets to Z4 in F and proves Z5 is not in F. Its propagation factors actual derivatives through the coherent lower O(-10), not merely its positive saturation. Its noncontainment induction kills actual successive quotient maps, with degrees 10,8,6,4,2 and negative lower degrees, and would otherwise put rank-eleven Z10 in rank-ten F.

The lift in that original is genuinely actual: the O(-10) line in K^- has complete eleven-dimensional coefficient span because its constant projection already has that dimension. The constant projection is consequently an isomorphism on coefficient spaces. The identification of the first four lifted jets with the inverse-image bundles is separately proved by the actual preimage decomposition and the zero map to H(-2)=O(-12); the inverse of an arbitrary bundle isomorphism is not differentiated. Thus the imported inclusions Zhat4 in K^- and Zhat5 in K are available. If Zhat6 were in K, the actual derivative of Zhat5 would lie in K, hence Zhat5 would lie in K^-, forcing Z5 in F. This verifies the noncontainment used by the new proof without assuming K2.

## Section 2: universal non-composition lemma

I checked all rank, parity, saturation, and extension steps.

For a hypothetical generic-rank-one j:W(-9) to P(-4), its saturated image is a G-equivariant line O(e) with e at most -4. Since the central element acts trivially on P(-4) and G has no characters, e must be even. A nonzero source map further gives e at least -9. This exhausts exactly e=-4,-6,-8. Sym5 W and Sym3 W contain no W; only e=-8 survives the source test, but the target inclusion would require P in Sym4 W=D. Thus generic rank one is impossible.

For generic rank two, each maximal minor has degree ten. The common vanishing divisor is invariant, and its degree is bounded by a nonzero minor's degree. The invariant orbit minimum twelve excludes all degeneracy. This proves an everywhere rank-two inclusion with locally free quotient, not merely generic injectivity. The same argument with degree-eight entries proves every nonzero q:P(-4) to O(4) is everywhere surjective.

If qj=0, write B=ker q. Its rank and degree are three and -20. Since j is saturated already in P(-4), P(-4)/j(W(-9)) is a vector bundle. Its induced map to O(4) is surjective. The kernel B/j(W(-9)) is therefore a line bundle, not a line plus hidden torsion, and its degree is -20-(-18)=-2. Its equivariant type is the unique O(-2).

The obstruction to splitting 0 to W(-9) to B to O(-2) to 0 is correctly the equivariant group (W tensor H1(O(-7)))^G. Serre duality gives (W tensor Sym5 W*)^G, which vanishes because W tensor T6=D+V_alt+P has no scalar. Finite-group invariants are exact over C, so this does give an equivariant splitting. Ordinary Ext is not zero and is not needed. The resulting O(-2) subline in P(-4) is impossible even nonequivariantly by degree. The lemma is sound without choosing either morphism or evaluating a composition.

## Section 3: forced cubic row and actual kernel identification

The component of Zhat5=T6(-5) in either deep block N is zero by ordinary degree. If the cubic component also vanished, the actual inclusion would land in R(-4). For the actual sequence 0 to Zhat5 to Zhat6 to O(2) to 0, the obstruction to extension into R(-4) is (R tensor H1(O(-6)))^G=Hom_G(D,R), which is zero. The extended map into K and the actual sixth-jet map into the original constant ambient agree on Zhat5. Their difference factors through O(2), whose Hom to a constant bundle is zero. Therefore they agree as actual ambient maps, contrary to the preceding noncontainment. No horizontal splitting is used.

The nonzero cubic map is unique up to scalar because S4 tensor Sym2 W=T6+S4+W. The claimed generator is a genuine everywhere-surjective complete-jet quotient, not a type or degree guess. For the complete degree-five system, its order-three principal-parts quotient is Sym3 W(2); the kernel consists universally of forms divisible by the fourth power of the variable line, namely ell^4 W. After twisting by -5 inside the complete degree-ten coefficient model, this kernel is ell^5(ell^4 W)=ell^9 W. That is exactly the intrinsic first-jet fiber of the actual lifted complete degree-ten curve. Hence the unique nonzero cubic row has kernel the actual Zhat1, not merely an abstract isomorphic W(-9).

Since the deep component is zero, this actual kernel lies in the actual R(-4) summand inside K. Saturation in R follows from saturation in the original constant ambient: R/Zhat1 embeds into the locally free ambient quotient, so it is torsion-free and therefore locally free on the smooth curve. The derivative kills Zhat1 because it lies in the retained actual Zhat4 in K^-. None of these assertions differentiates a chosen Birkhoff summand or equips a quotient with a connection.

## Section 4: actual near-top compatibility

The P component j_P of the actual first-jet inclusion cannot vanish. Otherwise the inclusion lies in V_alt(-4), its actual derivative is zero, and the map factors through the actual V-row kernel O(-14). Hom(W(-9),O(-14)) is zero by ordinary degree, contradicting the inclusion.

The V-row has zero projection to O(4). Consequently the actual identity beta_K|Zhat1=0 gives q_P j_P=0. The universal lemma, applied to this nonzero j_P, forces q_P=0. Thus the entire R(-4) row lands in the canonical W(1), and its image equals W(1) because the V row already surjects onto it. This is an actual compatibility statement, not the inference that equal abstract bundle types yield equal embedded images.

## Section 5: exhaustive row audit and contradiction

Every row in each displayed cubic splitting is covered:

* The S4(-3) row has zero O(4) projection because Sym7 W=T6+W' has no S4.
* Both summands of R(-4) have zero O(4) projection by the previous section.
* For K4, the only remaining row is W(-9) to O(4). Its degree-thirteen Hom space has W multiplicity one. Multiplication of the nonzero degree-one W submodule by any nonzero invariant f12 supplies that unique copy. Every such row is therefore f12-divisible, including the zero row, through O(-8).
* For K5, the O(-8) row is a scalar multiple of f12 because the degree-twelve invariant space is one-dimensional. The O(-10) row is zero because there is no degree-fourteen invariant. The orbit-size argument and the checked Sym14 decomposition agree on that vanishing.

Thus the entire composite pi beta_K factors through the proper subsheaf O(4)(-D12). The invariant f12 has a nonempty divisor of degree twelve; the orbit minimum also makes it the reduced twelve-point orbit. It is unnecessary to choose its scale. This factorization cannot be an everywhere surjection to O(4), whereas the retained beta_K and canonical pi are both everywhere surjective. The contradiction is coherent-sheaf theoretic and does not mistake saturation of an image for its full coherent image.

## Independent selected-only replay and checker review

After the author finalized the support files, I reread the final `REPRODUCE.md` and `verify.py`. I created a newly empty isolated directory and copied exactly the seven files listed there, preserving relative paths. I ran separate normal and optimized Python processes with `PYTHONPATH` empty and `PYTHONDONTWRITEBYTECODE=1`. Both exited zero with no stderr, identical complete output, 47 main checks and 81 character-module checks. The directory contained exactly the same seven files afterward, with no bytecode or changed bytes.

Final support bindings:

* `verify.py`: SHA256 `bf80de810e4edd42f948a9941bfd51c9ad47e71ae1ead2035a54937fe631a375`.
* `characters.py`: SHA256 `a4ccb5192de0eb1818dc4aaf2b12c6d8d12cc56fbad7ea7e561c77ec38e7a7dc`.
* `REPRODUCE.md`: SHA256 `a456f482252d6572d726e41340a8dd4cdf0e5d58d00d278b527dd451c00aa7bf`.

`REVIEWER-REPLAY.json` binds every selected file and records both complete results. The revised checker independently pins the current proof and both immutable original identities rather than merely trusting editable input metadata. Its guards raise explicit exceptions and survive optimization. The character module checks the fixed nine-class McKay relations with exact Q(sqrt(5)) arithmetic; its recurrence computes only the fixed requested universal products. The three possible rank-one image degrees are the complete local bound of the proof, not a search for source instances or kernel tuples. No source-instance values, candidate parameters, selected points, tensors, matrices, or ranks are computed.

## Findings and retained boundary

No blocking issue remains in the frozen proof or the final support packet. The initial support-file ambiguity and missing current-proof binding were corrected before isolated replay; the proof itself was never altered during this review. Fresh response authentication, complete-text reading, arithmetic replay, and the structural proof audit are separate evidence and have not been substituted for one another.

The verified new content is the actual first-jet compatibility forcing the near-top positive quotient to vanish, followed by the exhaustive low-row divisor obstruction. K1 and K3 remain untreated; the simultaneous image, cyclic image, other local defects, F18 alternatives, original higher-jet separation, algebraicity, and whole-profile goals remain open at their earlier scope. No GitHub write, merge, upstream submission, selected actual evaluation, or large computation was performed by this reviewer.
