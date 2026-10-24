# Independent entire-proof review

## Verdict and exact scope

**PASS for the entire conditional theorem in the exact frozen proof.**

- File: `PROOF.md`, 13,135 UTF-8 bytes.
- SHA256: `0a24ab99c6f3d6c2f60212532c7f4aed2bd7d5fba17823243dd479a83a7308dd`.
- All sections, including the statement, both complete direct inputs, and the exact stopping boundary were read. No mathematical gap requiring revision was found.
- This verdict retains the stated actual-geometric hypotheses and the original condition `delta=12`. It does not certify any transitive hypothesis independently of the imported source assumptions.
- The proof establishes actual coherent images `I4=O(8)+O(2)(-D12)` and `I5=O(6)+O(2)(-D12)`, followed by precisely the necessary alternatives `I6=O(4)+O(2)(-D12)` or `I6=E6(-D12)`. Neither alternative is excluded or shown to occur.

## Independent source authentication

I independently fetched each complete immutable repository path and its complete exact Git blob through the GitHub connector. For each source, both fresh responses and the selected local input agree in every UTF-8 byte. I independently recomputed byte length, SHA256, and Git blob SHA1, including the Git blob header. No author `LOCAL*` record or separate working/follow-on draft was read or used as proof evidence.

1. PR1216, commit `66a6bfe8dd424da58f3d775be1818d1f4f71eff1`, path `research/hm/rankfour-profile11-triplet-nine-jets/PROOF.md`: 12,744 bytes; SHA256 `44ee429fa26b65b68b2668ce69dff219e4a4daf0a6bdaa9fac0e94aa8a631b3a`; Git blob `916cc6a3bc1cf8ad07e019f00a1f5ebf867311d6`.
2. PR1215, commit `8ca4ccd046248752714a84dfb05aae42a6433f55`, path `research/hm/rankfour-profile11-triplet-twelve-orientation/PROOF.md`: 12,396 bytes; SHA256 `a9b56b6f84c9a11dedb94639bf16ab5c1065e21a91d067c52f75435d4b014da2`; Git blob `e698ba5aa8caf0ffdc0aa28baec9d0ba8f036eda`.

The complete PR1216 source supplies the actual adjacent annihilator flag, coherent surjections and principal-parts identifications, not a merely formal degree sequence. Its proof distinguishes the original jets from auxiliary dual jets. The complete PR1215 source supplies the embedded lower-normal orientation and actual `B3/F=O(4)`, not just the ordinary splitting type of its image. Its torsion-Hom argument is consistent with its stated assumptions. These are precisely the imported facts used here. Fresh authentication details are in `REVIEWER-AUTHENTICATION.json`.

## Section-by-section geometric audit

### Statement and Section 1: ambient, flag and equivariance

The fifteen-dimensional ambient, negative-top inclusion `B3 subset Sym14 W(-4)`, original jet annihilators, adjacent quotient degrees and coherent fullness of `phi_j` are all present in the complete direct inputs. Each `Fj` and every later actual backward kernel stays inside `B3`, so negative top is inherited. The original `delta`, the later image defect lengths, and the independent PR1216 endpoint `e9` are kept separate.

The physical line linearizations and absence of nontrivial scalar characters justify treating equivariant scalar-line maps as invariant sections of the stated physical `O(d)`. The invariant-divisor orbit sizes imply that a positive invariant section of degree below 14 can only have degree 12. Degree 14 is impossible: its divisor cannot be a sum of orbits of sizes 12, 20, 30 or 60, counting multiplicity. No source-instance evaluation is needed.

### Section 2: actual coherent two-column capacity

The backward kernels are saturated actual subbundles of the same constant ambient. If a nonzero negative-top stage had zero derivative, its Grassmannian map would be constant in characteristic zero, yielding a constant degree-zero subbundle, a contradiction. The sequence therefore ends at zero.

The derivative of a section of `Qi` lies in `Q_(i-1)` because `Qi` is the actual kernel of the preceding second fundamental form. Its quotient modulo `Qi` yields the coherent injection `Ri -> R_(i-1)(-2)` with exact kernel removed. This is not a connection on either quotient. Consequently positive quotient ranks are two for `k` stages and one thereafter; `1<=k<=floor(n/2)`. Composing the injections retains every torsion deficit. Summing the rank-two determinant bounds and rank-one top-degree bounds gives exactly equation (7). The rank-one special case gives equation (8).

### Section 3: actual intersections, splitting and the lower projection

The first normal projection is the restriction of the actual adjacent derivative `phi_(j-1)`, by naturality in the constant ambient. Under (9) it is coherently onto, so its kernel is the actual `F_(j-1) intersect B_j`. Both exact sequences (11) follow by the sum/intersection identity; the quotients are locally free. This proves saturation of the new kernel in the ambient.

The two actual subbundles `F_(j-1)/Fj` and `B_j/Fj` in `B_(j-1)/Fj` have zero intersection and sum to the whole bundle. They therefore produce the displayed actual direct sum (13). This is a transversality argument. It is valid at `j=6` without any Ext-vanishing claim for the normal extension.

Because `Fj subset B_j=B_(j-1)^-`, its derivative lies in `B_(j-1)` and factors through the actual normal subbundle `E_j`. Projection onto `B_(j-1)/F_(j-1)` agrees with restriction of the previous second fundamental form. Taking the kernel of the previous upper projection in the surjection to the previous coherent image leaves an everywhere surjection onto exactly `O(2)(-D12)`. Thus (14)-(15) are coherent statements with the same divisor and actual lower line, not claims obtained after saturation.

The rank and degree computations are `(9,-74)`, `(8,-82)`, `(7,-88)`. If one derivative had rank one, its coherent line image would surject onto `O(-10)` and hence be isomorphic to it. The rank-one capacity bounds are respectively `-162`, `-136`, `-112`, all impossible. Hence all three derivatives have rank two. Since `E_j` is itself a subbundle of the ambient quotient, full generic rank makes it exactly the saturation of each coherent image.

### Sections 4 and 5: the two forced embedded images

Surjectivity to `O(-10)` implies that the lower ordinary splitting degree is at most `-10`. For rank nine, the assumption `a<=-2` makes the four capacity values `-82,-78,-78,-82`, contradicting degree `-74`. Thus the canonical equivariant top line has `a>-2`, and its only possible nonzero component goes to `O(8)`. The invariant degree `8-a` is in `[0,9]`, so it is zero. The image contains the entire actual upper normal line; together with lower coherent surjectivity this gives the full preimage, not merely an abstract isomorphism.

For rank eight, `a<=-6` gives `-94,-88,-86,-88`, contradicting degree `-82`. The same argument with invariant degree `6-a` in `[0,11]` forces the entire actual `O(6)` summand. These steps establish (18) and (19) with the orientation needed to run the next common-kernel construction.

### Section 6: honest two-alternative rank-seven endpoint

If `a<=-10`, both degrees are at most `-10`. The three universal capacity bounds are `-100,-92,-88`. Equality with the actual degree `-88` requires `k=3` and, since both degree coefficients are strictly positive, `a=b=-10`. For the equivariant bundle `R O(-10)`, center parity makes the two-dimensional multiplicity representation `R` center-even. The imported center-even irreducible dimensions therefore force `R=1+1`. Both components into `O(4)` would be invariant sections of `O(14)` and vanish, violating generic rank two. This rules out equal degree without silently allowing a center-odd two-dimensional representation.

Thus `a>-10`; the canonical top line has no lower component. Its invariant upper degree `4-a` is below 14, forcing `a=4` or `a=-8`. The quotient line must map surjectively to `O(-10)`, so `b=-10`.

Use of the lower summand as an equivariant line is legitimate: for unequal splitting degrees the canonical top-line sequence splits ordinarily since `H1(O(a-b))=0`, and a splitting can be averaged over the finite group. This is a splitting of the coherent image itself, not a splitting of the normal extension by an invalid Ext argument. In the `a=-8` case the remaining upper component has invariant degree 14 and therefore vanishes. The top-line upper inclusion has divisor exactly the reduced `D12`. Hence the second endpoint is precisely the embedded `E6(-D12)`, with local elementary divisors `(1,1)` and total defect 24, rather than a cyclic order-two defect or an unspecified extension.

For `a=4`, the full actual upper line and the surjective lower image give (5a). The comment retaining (5b) is correct: restriction of the identity gives a nonzero element of `Hom_G(O(4),O(4)|D12)`, so the preceding torsion-Hom vanishing pattern cannot be asserted at this endpoint.

### Section 7: full constant span and stopping boundary

Nestedness identifies the recursive intersections with `F intersect B_j`. Actual transversality inductively yields `F+B_j=B3`, so the adjacent `O(4)` quotients are the inherited ones. Dualizing the actual ambient inclusions gives exactly `0 -> T_j -> ann(Fj) -> O(-4) -> 0`. Both end terms have zero global sections because `T_j=Sym^j W(j-18)` and `j<=6`. Thus `H0(ann(Fj))=0`, proving that each entire `Fj` spans all fifteen constant dimensions.

This argument does not pass full span to a proper tail or scalar subline. The proof expressly avoids that invalid transfer. It also does not infer new original jets beyond order nine, algebraicity, a rank-seventeen transfer, a quotient connection, horizontal summands, any realization statement or a whole-branch/profile exclusion.

## Bounded checker inspection and isolated replay

I read both Python files completely before running them. The executed code consists of exact source/proof authentication, the three fixed common-kernel degree stages, four/four/three fixed capacity values, fixed defect arithmetic, and small universal character facts. The imported character module checks 81 fixed exact-rational McKay identities. Its unused convenience helpers do not evaluate a source instance. Explicit `require` calls remain active under optimization.

I copied exactly the seven paths named in `REPRODUCE.md` into a newly empty isolated directory. No local records, drafts, old outputs, reviewer files or caches were copied. With bytecode writing disabled, both `python verify.py` and `python -O verify.py` exited zero, reported **PASS, 51 explicit verifier checks**, and printed the exact frozen proof hash above. Their result objects agree. The isolated directory contained exactly those seven files after each run, and every selected byte remained unchanged. Source bytes were also unchanged during replay. Full file hashes and captured outputs are in `REVIEWER-REPLAY.json`.

The checker corroborates bounded arithmetic only. The geometric verdict above is based on the entire independent proof audit, not on successful execution. No GitHub writes, selected actual coefficients, parameters, points, jets, tensors, matrices, instance ranks or normalizations, broad scan, or large computation were performed.
