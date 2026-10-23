# Independent whole-proof review

## Verdict and scope

PASS for the stated structural theorem, conditional on the authenticated input interfaces and on the retained nonzero-mu branch. I independently read the complete final PROOF.md, verify.py, INPUTS.json and REPRODUCE.md, fetched all three originals at their pinned commits, and checked the deductions below. I found no blocking mathematical, inheritance, normalization, or scope defect.

The result classifies the actual inherited core by intrinsic channel vanishing. It does not determine the value of mu or any channel, select the actual row, establish that every abstract channel pattern occurs for HM data, or supply an actual-instance computation. The verifier is a bounded consistency and input-authentication check, not a formal proof of the geometric arguments.

## Final author-byte binding

The review applies to these SHA-256 hashes, verified directly after the final author files were frozen:

```text
2e7771e1b7405d4bf0def56be1e0fd20924040ff8679bb806c700ed999d2d3ca  PROOF.md
1a5d9ed3985ee7dc966853287ca3c120874d2512ead2af587237b88f87e71aa9  verify.py
06b843629010f06cf2f19007b51cbe386958a6265404ba6d5a72724fe76a0b0b  INPUTS.json
ad119aca062293511820a60228f15d61a43bd80ae5a6ecb2b6ab9282479c1584  REPRODUCE.md
```

Any change to one of these files requires a new byte-bound review. REVIEW.md itself is excluded from this list to avoid a self-referential hash.

## Independent input audit

I fetched the following repository files independently, rather than accepting the author's local audit copies as authority. The fetched content has the Git blob identity shown in INPUTS.json and is byte-identical to the corresponding local audit input.

- SMALL: commit 7df3f6d6cd19964d5576954790de192d7f8ef8e1, research/hm/small-opposite-core/PROOF.md, Git blob 5a90ecfefb8ac339a5ee4cf8812bfaea6ea715e3.
- UNIVERSAL: commit 893845c20e964035dd2446897211814f184f93bd, research/hm/one-source-opposite-core/PROOF.md, Git blob 186043a2d37e07641803e68de6bb0048b49bc6a0.
- TYPES: commit 54dc2b2b301f8a7e453b3101d5813c643beed71a, research/hm/opposite-second-degree-bound/PROOF.md, Git blob 4666dacbbe7c4d68b25e80d65af37ea80f3592be.

SMALL supplies the actual nonzero-mu rank-two source, canonical target extension, and actual Q. Its equivalence of the mu and lambda branches is through the same Hom(Q,O) obstruction, not matching representation labels. TYPES supplies the row names and actual canonical quotient of C. UNIVERSAL is used only for its branch-independent universal square inclusion and degree-thirteen basepoint-free system. Its separate zero-mu assumption is not imported into the present argument.

## Mathematical review

### 1. Universal degree-ten A system

The fixed identity A tensor Sym5 W = W' + S + 2T6 gives a one-dimensional Hom space from W' O(-5) to A O. A hypothetical rank-one saturated image is an equivariant O(-e). Its inclusion in A O gives e at least zero, while its nonzero source factor gives e at most five and would require W' in Sym^(5-e) W. None of those six symmetric powers contains W', so generic rank is two.

The maximal-minor system is nonzero and has degree ten. Its common-zero divisor is G-stable; every nonempty projective orbit has at least twelve points. Therefore it has no common zero, and the map is everywhere a subbundle inclusion. The quotient is the equivariant O(10), because its degree is ten and G has no nontrivial one-dimensional characters. Dualization and twisting give the claimed O(-8) to A O(2) sequence with quotient W' O(7). The A multiplicity in Sym10 W is one, so this identifies every nonzero map in the required channel, not merely a selected example.

### 2. Universal degree-nine S system

The nonzero S system in Sym9 W is basepoint-free by the same orbit bound. Its kernel K has rank three and degree minus nine. The inclusion in a constant bundle and H0(K)=0 force all splitting degrees to be at most minus one.

After the first twist, the section space has dimension at most three and embeds in A+D. If A occurred, all three ordinary summands would have degree minus one, contradicting total degree minus nine. Thus no first-twist sections occur. After the second twist, the section space again has dimension at most three and embeds in W+S+T6, so W is its sole possible nonzero value. That value would give the degree-minus-two subbundle W O(-2). Its map to S O is the unique universal square inclusion, whose quotient is W O(2). The nonzero S evaluation would then factor through an equivariant W O(2) to O(9) map, but that Hom space vanishes because Sym7 W contains no W. This rules out the second-twist sections.

Consequently K is balanced of type O(-3)^3. Twisting by three and taking sections is exact on the right because H1(K(3))=0. The identity S tensor S - Sym12 W = V determines the equivariant multiplicity, so K=V O(-3). Dualization and twisting give the required O(-8) to S O(1) sequence with quotient V O(4). No multiplication-rank assumption or actual HM evaluation is hidden in this kernel argument.

### 3. Actual zero-theta graph

When theta is zero, the actual L2 map factors through F and remains fiberwise injective. The degree-seven W' system is basepoint-free, and its quotient has degree twelve. Quotienting source and target by this actual image yields the stated rank-five extension, not a replacement bundle with the same character.

The remaining L8 projection to B4 must be nonzero: if it vanished, an everywhere injective map between O(-8) and O(12) would result, impossible for unequal-degree line bundles. The universal degree-nine sequence then gives the actual quotient extension of V O(4) by O(12). Its Ext group vanishes by H1(O(8))=0; averaging yields equivariant splitting, and Hom_G(V,Sym8 W)=0 makes that splitting unique equivariantly. This derives the row9 type without assuming it from the row list.

### 4. Actual nonzero-theta normalization

The one-dimensional theta channel has the dual complete cubic evaluation as universal model, with saturated quotient R=A O(2). The groups Hom_G(R,F) and Ext1_G(R,F) both vanish: the first uses W' tensor S=V+D, and the second H1(O(3))=0. The resulting restriction isomorphism of equivariant Hom spaces is exactly what is needed to correct any initial target splitting so that it agrees with the actual L2 lift.

This correction exists and is unique equivariantly. The proof explicitly does not assert uniqueness among ordinary splittings. Quotienting the actual L2 image in this compatible lift preserves every graph component of L8 and leaves the same actual Q. Therefore alpha and beta are well-defined intrinsic projections in the resulting relative direct sum. A change of representation identifications only rescales their generators and cannot alter their vanishing.

### 5. Channel extension and four cases

The alpha and beta channels are one-dimensional. The degree-thirteen W' basepoint-freeness proof in UNIVERSAL remains valid independently of that input's actual branch: a nonempty base divisor would have degree twelve, and dividing by its invariant section would force W' into Sym1 W. The beta channel has already been treated universally above. Their line or rank-two quotients and degrees are therefore established uniformly.

If alpha vanishes, the actual quotient is W' O(5)+W' O(7). If beta vanishes, it is O(18)+A O(2). They cannot vanish together because the inherited full source map is fiberwise injective. If both are nonzero, the saturated beta quotient gives an extension of W' O(7) by F. Its class is the connecting image of alpha, up to the inessential pushout sign. The two vanishings used for the compatible lift also make this connecting map an isomorphism, so the class is nonzero.

The equivariant Ext space is one-dimensional. The W'-tensored Euler sequence has middle term P O(6) and cannot split even ordinarily because its proposed reverse map has negative degree. Hence every nonzero class has that middle isomorphism type; no canonical endpoint normalization beyond what is claimed is required. The four resulting Q types are distinct. They establish the reverse implications as well as the forward ones, with row names and C=O(2)+Q supplied by TYPES in the retained nonzero gate branch.

### 6. Inheritance and exclusions

At every quotient step the sources and target extensions are the inherited maps from SMALL. In particular the inclusion of F into the successive quotients is the induced actual map, whether or not it is itself injective in a particular channel case. There is no identification with an older core coefficient merely because the representation labels agree. All stated ranks and degrees balance, and the argument stops at exact channel criteria rather than selecting a branch, channel value, actual row, source pair, marked line, or vertex scalar.

## Checker review and replay

The verifier uses exact rational arithmetic in Q(sqrt(5)) on nine fixed conjugacy classes. I reviewed its full source, including the representation construction, orthogonality checks, symmetric-power recurrence, Hom tests, cohomology dimensions, orbit inequalities, rank/degree balances, and Git blob authentication. The fixed identities were also recomputed during review. In particular the low symmetric powers, W' tensor S=V+D, W' tensor W=P, and S tensor S-Sym12 W=V agree with the proof.

The following commands both completed successfully on the final files:

```sh
python3 verify.py
python3 -O verify.py
```

Both returned the declared PASS output. In an isolated copy, appending one newline to SMALL.md caused both ordinary and optimized runs to fail with `immutable input mismatch: SMALL`. The executable checks use explicit require calls rather than assertions, so optimization does not disable them. No author files or authenticated audit originals were changed by this negative test.

REPRODUCE.md's git-show reconstruction preserves the pinned file bytes, and its verifier commands need only the Python standard library once those authenticated inputs are present. The executable confirms fixed arithmetic and input identities. The actual-map inheritance, saturation, balanced-kernel deduction, normalization, and extension interpretation remain the mathematical arguments reviewed above, not claims of machine proof or instance evaluation.
