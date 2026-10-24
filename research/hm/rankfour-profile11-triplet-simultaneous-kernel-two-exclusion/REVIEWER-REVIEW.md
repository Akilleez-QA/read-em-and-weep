# Independent entire-proof review

## Verdict: PASS, for the exact conditional statement only

I independently read the entire frozen `PROOF.md`, all four complete direct originals listed in `INPUTS.json`, and both complete Python sources. I found no mathematical gap in the claimed conditional exclusion.

This verdict binds exactly:

- Proof length: **13,703 UTF-8 bytes**.
- Proof SHA256: **0165fa9a854879e5b2c67885f3b0bede6c3f48b34e1c761c0ca846645a3247fa**.
- Reviewer: `review_conditional_kernel_two_exclusion`, separately assigned to review the author's frozen artifact.

The conclusion is only that the original alternative `K2=(V_alt+2P)(-4)+W'(-7)` cannot coexist with the retained full-positive triplet, original `t=0`, local `delta=12`, residual simultaneous rank-seven coherent-image geometry and its forced `k=2` flag, under the stated transitive actual-geometric assumptions. It does not exclude K2 in other coherent-image branches, exclude the simultaneous branch with another original kernel, establish a remaining case, or establish original degree-eighteen tenth jets or algebraicity.

## Fresh independent source authentication

For each direct original I independently invoked both the immutable repository-path fetch and the Git-blob fetch against `Akilleez-QA/read-em-and-weep`. I compared their complete UTF-8 bytes against each other and the retained input, checked length and SHA256, computed the Git blob SHA1 including the Git object header, and checked the path response's returned blob SHA and immutable URL. All four routes-pairs agree exactly:

| Complete original | Immutable commit | Bytes | SHA256 | Git blob SHA1 |
|---|---|---:|---|---|
| quartic-normal-map | 06385eec63b85efac6cc25441d4b58d4fa5a8adb | 15127 | 205256f2772d21d81025e6c511a52de564bfd7e9e0d94cce79fc3f684b6d17ba | 243adcdfe618e0792f330534c5c74931ad2741ac |
| common-kernel-ladder | 5249c844765cfd96ffb51bdfd4aaef8307d49b1f | 13135 | 0a24ab99c6f3d6c2f60212532c7f4aed2bd7d5fba17823243dd479a83a7308dd | d64a0db4f2bcbd61651cdefc37a37b672c321176 |
| eighteen-jets | 913892c66403ea57ed1681957ae1b9f8db9e5e15 | 17528 | 33a3c8866f072f4aec607c2d6647222ee0031a3f1bbbaef550e58df5075b3dbf | 730021d4e97c4c1307a1d3c6c5303e4e9792202d |
| five-kernels | 7d71f0e2a3963cff64a069198f4415c5cfd0fe9b | 8501 | 4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a | 163ba2126b6130befcc2351db7f6910d85fac2ec |

`REVIEWER-AUTHENTICATION.json` records the requests, immutable paths, checks, and raw-response digest. `REVIEWER-FRESH-SOURCE-RESPONSES.json` retains the complete fresh responses locally and must be excluded from publication. The blob API returned content without a separate SHA field; authentication therefore uses its exact requested SHA and the independently recomputed Git blob hash, rather than claiming a nonexistent returned field. No GitHub write was made.

## Whole-proof geometric audit

### 1. Actual inputs and coherence

The eighteen-jets original supplies the constant ambient restriction, the exact sequence `0 -> H -> K -> J -> 0`, and the everywhere injective restriction on `K^-` with actual saturated image `F`. Thus `H=O(-10)` is the primal kernel line, not an auxiliary line in the other ambient. Its intersection with `K^-` is zero fiberwise. The same input supplies ranks 13 and 10 and degrees -58 and -64.

The common-kernel-ladder original supplies the exact upper kernels and the embedded coherent images `I3`, `I4`, and `I5`, with the same lower `O(2)(-D12)=O(-10)`. In particular, restricting to an upper kernel really leaves a regular map to coherent `O(-10)`, not just a map to its saturation `O(2)`. This distinction is essential and is used correctly.

The quartic-normal-map original proves completeness of the actual auxiliary degree-ten line independently of the original degree-eighteen coefficient system, and supplies its saturated intrinsic jets through order ten. The five-kernels original labels the second alternative with top representation `V+2P`, where its alternate triple `V` is the present `V_alt`, not `A=Sym2 W`. No kernel classification is transported between unrelated ambient ranks.

### 2. Propagating the small jets

The three applications use the exact upper kernels in the correct order: `Z1` is in `F6=ker(upper beta_F5)`, then `Z2` is in `F5=ker(upper beta_F4)`, then `Z3` is in `F4=ker(upper beta_F)`. The remaining coherent maps have ordinary degree differences -1, -2, and -3, respectively, and therefore vanish without equivariant coefficient choices. Derivatives then lie in the named actual parent bundle. Saturation of that parent in the constant ambient permits the corresponding saturated jet span to lie there. This proves exactly `Z2 subset F5`, `Z3 subset F4`, and `Z4 subset F`, not an unjustified extra step.

### 3. The forbidden fifth-jet containment

Under the temporary assumption `Z5 subset F`, the derivative of `Z4` lies in `Z5`, so `beta_F` kills `Z4` before any line-quotient factorization is made. At each later induction step the same predecessor argument applies. The quotient is the actual equivariant line `Zj/Z(j-1)=O(2j-10)`; the scalar-character ambiguity is absent because the group has no nontrivial characters.

The upper invariant degrees are exactly 10, 8, 6, 4, 2 for j=5 through 9, all zero invariant spaces. The lower degree is -2j and is negative. The induction thus reaches the rank-eleven `Z10` inside rank-ten `F`, a contradiction. The accompanying incidence statement is consistent: on `Z4`, the nonzero normal map kills `Z3` and factors through `O(-2)` into `O(10)`, giving degree twelve. It neither selects its nonzero scalar nor assumes continued containment.

### 4. Actual lifting, completeness, and the normal twist

The lifted `R0` is an actual equivariant line of degree -10. Its coefficient span has dimension at most eleven by the scalar degree-ten bound; its constant projection spans the already proved eleven-dimensional projected coefficient space. Hence its span is exactly eleven and the constant restriction is an isomorphism between these two coefficient spaces. This proves completeness of the lifted curve and identifies all its projected intrinsic jets, without treating the inverse of `p|K^-` as a constant ambient map.

For j=0 through 3 the derivative of `Rj` lies in `K`, and constancy of `p` puts its projection in `Z(j+1)`. Since `R(j+1)` already maps isomorphically onto that subbundle and is disjoint from `H`, the actual preimage is `R(j+1) direct-sum H`. This is a geometric splitting of the actual preimage, not an imposed horizontal splitting.

The derivative modulo `R(j+1)` is O-linear: the Leibniz extra term lies in `Rj subset R(j+1)`. Its global target is `H tensor Omega^1=H(-2)=O(-12)`, not untwisted `H` or `H(2)`. The degree difference from `Symj W(j-10)` is `-j-2`, so it vanishes for all four steps. Thus the genuine lifted jet spans equal `Rj` through j=4. The saturated fifth jets then lie in `K`, because derivatives of `K^-` lie there. The sixth jets exist in the original constant ambient by the complete lifted curve, but are not prematurely claimed to lie in `K`.

### 5. Equivariant extension obstruction

In type K2, the lower component of `T6(-5) -> W'(-7)` is zero by ordinary degree. The fifth-jet map therefore lands in the canonical top subbundle of type `R(-4)`, where `R=V_alt+2P` and `D` is absent. The actual jet sequence has quotient `O(2)`, as also confirmed by degrees `7(-4)-6(-5)=2`.

The obstruction group is correctly equivariant, not ordinary: `Ext^1_G(O(2),R(-4))=(R tensor H1(O(-6)))^G=Hom_G(D,R)=0`. Finite-group invariants are exact in characteristic zero; Serre duality gives the physical degree-four dual representation with no determinant-character correction. Ordinary `H1(O(-6))` is nonzero, so the proof's explicit reliance on the missing equivariant summand matters. Vanishing of this obstruction suffices for the actual sequence, without selecting an extension coefficient or using a polarization normalization.

### 6. Equality with actual ambient jets and contradiction

The extension followed by the actual inclusion of `K` and the genuine sixth-jet inclusion agree on the canonical fifth-jet subbundle. Their difference consequently factors through the actual quotient `O(2)`. There is no map from this positive line to the original trivial ambient, so the maps agree everywhere. This is the required actual containment, not merely an abstract map into a bundle of the same type.

Since the first derivatives of the fifth jets are contained in the actual sixth jets, they now lie in `K`. The fifth-jet subbundle therefore lies in the actual derivative kernel `K^-`. Applying the original constant `p` gives the previously forbidden `Z5 subset F`. The contradiction excludes precisely the stated K2 intersection.

## Checker inspection and selected-only independent replay

I inspected `verify.py` and `characters.py` completely. Their checks use explicit exceptions and survive Python optimization. The character module performs 81 fixed rational McKay identities; the main checker performs 61 fixed authentication, representation, degree, and exact-sequence arithmetic checks. Neither script performs actual-source evaluations, a search, network access, package installation, or remote writes. These checks are arithmetic evidence, not substitutes for the geometric review above.

I created a newly empty isolated directory and copied **only the nine files listed in REPRODUCE.md**, preserving paths. With `PYTHONPATH` empty and bytecode writing disabled, both normal Python and `python -O verify.py` returned identical PASS objects with **61** checks and the frozen proof hash. A separate import in each mode confirmed **81** character-module checks. Exactly the nine selected files remained afterward, with no cache, author result file, raw fetch, or reviewer artifact present in the replay directory.

`REVIEWER-REPLAY.json` records the selected-file hashes, isolated location, environment, exact commands, return codes, complete standard outputs, and matching normal/optimized results.

## Issues and retained limits

No blocking issue or correction was found in the frozen proof. The imported transitive assumptions remain assumptions: this review freshly authenticates and reads the four direct originals, and does not claim to have re-fetched the entire transitive research history. The proof does not equip a quotient with a connection, assume a Birkhoff summand horizontal, transfer full span to an arbitrary subbundle, evaluate selected actual data, or upgrade higher auxiliary jets to original degree-eighteen jets. The untouched alternatives and the conditional scope are stated accurately.
