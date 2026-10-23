# Independent review: onto rank-four quadratic top subsystems

## Verdict and exact scope

PASS. No blocking mathematical issue was found in `ONTO-RANK-FOUR-TOP-SUBSYSTEMS.md` at SHA-256

`87244e453597105dffb298743c1725ac29b00c8b8dc1cafad37f55235c81ea34`.

Its Git blob identifier is `2c6fc5ba815f57af69b21ec27e92dfbe7c27c835`.

For the source

`E = P O(-2) + 2T O(-3) + O(-10)`,

in either specified original-zero-defect label, the assumption that the quadratic top block maps onto the positive rank-two quotient forces the stated doublet kernel, saturated internal image, complete linear first-polar system, and exactly two intrinsic constant-span types. For the split target, a generic rank-two top image is automatically onto. Combined with the separately pinned rank-one exclusion, this exhausts the possible top subsystems for this source in that label.

The result does not exclude the entire source or either full label. The balanced target's possible length-twelve torsion branch is not excluded by this argument. The two constant-span types are necessary intrinsic configurations, not realization assertions for the original source.

## Immutable inputs

The source data are pinned to commit `db51525015bb7c5e825833d550d08dedf6f6ea96` of `Akilleez-QA/read-em-and-weep`, under `research/hm/order-four-quadratic-load/`:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The following Git blob identifiers were independently recomputed and agree with the proof's pins:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`: `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.
- `one-one-endpoint-necessary-pairs.json`: `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`: `8b5971092f9ef762584912609fd5e9301c4e271d`.

The label records identify source indices 69 and 72, respectively, and original determinant defect zero in both cases:

- `G3.11.863639aa192e`: `A_q = O(-10)+O(4)+O(6)`.
- `G3.11.73682b4c817f`: `A_q = O(-10)+W O(5)`.

Both compatible-source lists include `(0,2,0,0,0,0,0,1)`. The pinned splitting formula decodes this tuple to the displayed E, of rank 17 and degree -54.

The saturation input is PR796, Section 3, at commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

The corresponding proof bytes have SHA-256 `622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1` and Git blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`.

The quadratic first-polar statements are pinned to PR799, commit `2172e4a7abbbe232f9f448bea6fa01dee7927460`, and PR802, commit `e484640a6565c278321bf6557860262c1ac1b7df`:

https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md

https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

Their proof-byte SHA-256 values are, respectively, `3a55f2c37548c7b05bf0f39f775ab37807c9f852d3601f77271fc0dd052022ed` and `a18a6990f719592d71853692157161a9ca5fe6b7f2a78edacbfa060bb3513459`.

The separate rank-one top-image exclusion is pinned to PR814 at commit `1f94be65b3a470a1b594e61d56df7f6057c9d907`:

https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/RANK-ONE-TOP-EXCLUSION.md

Its reviewed proof bytes have SHA-256 `2f480884b26a089bcd6f3633e75e790472cc493d9908dd83f0497c6b1fbe8d50` and Git blob `1ee578edc099516fc2ba995a752d4886f681fbaf`. The onto-branch theorem does not depend on this exclusion. It is used only to pass from the split-target rank-two statement to an exhaustive statement about that source's top image.

## 1. Complete rank-two kernel classification

Set `F=P O(-2)`, and suppose `p:F->U` is onto. The positive quotient U has rank two and degree 10. Its twist-two section representation is `V+2P+D` for both targets. Strict-top vanishing injects `P=H0(F(2))` into that representation. Hence

`rank K0=2`, `deg K0=-18`, `H0(K0(2))=0`, and `H1(K0(2))=V+P+D`.

Equivariant Birkhoff-Grothendieck splitting is legitimate for this finite group in characteristic zero. If the two ordinary degrees differ, their canonical slope blocks have rank one. The group is perfect, so their coefficient representations are trivial; center-evenness forces both degrees to be even. The strict-top bound excludes degree -2 and all larger degrees. Therefore the unequal-degree possibilities are exactly

`O(-4)+O(-14)`, `O(-6)+O(-12)`, and `O(-8)+O(-10)`.

If the ordinary degrees agree, both are -9 and the coefficient representation must be an odd two-dimensional representation. The only choices are W and Wp. Thus the five bundles listed in the proof are exhaustive, not merely a support shortlist.

Equivariant Serre duality gives `H1(Z O(-j)(2))=Z Sym^(j-4)W`. The needed universal identities are

`Sym^6 W=V+P`, `Sym^7 W=Wp+T`, `Sym^8 W=P+D`, `Sym^9 W=S+T`, `Sym^10 W=A+V+D`,

`W T=V+P+D`, and `Wp T=A+P+D`.

They yield exactly the proof's five H1 characters. Only `W O(-9)` and `O(-8)+O(-10)` match `V+P+D`.

## 2. Saturation and exclusion of the line-sum kernel

For the line-sum kernel, every map to `O(-12)` vanishes by degree. The map from `O(-8)` to `T O(-5)` vanishes because T is absent from `Sym^3 W=S`. The map from `O(-10)` to one copy of `T O(-5)` has a one-dimensional equivariant channel, since `Sym^5 W=T` is irreducible. Its nonzero member is the full quintic tautological inclusion, so it has no zero fiber. Two target copies change only its constant multiplicity vector. Thus the internal image is zero or the saturated line `O(-10)`.

The original determinant defect zero makes U saturated in `Q(-2)`. PR796's image argument is valid with a rank-two external image: if J is the saturated internal image, the full derivative image I fits into

`0 -> J -> I -> U -> 0`.

The ambient quotient by I is an extension of the two locally free residual quotients. It is therefore locally free. Consequently

`0 -> F -> F^+ -> I(2) -> 0`

has no omitted saturation divisor.

If J is zero, `rank F^+=6` and `deg F^+=6`, impossible in a constant bundle. If `J=O(-10)`, the rank and degree are 7 and -2. The first-polar surjection makes `F^+(1)` globally generated, while its constant ambient inclusion bounds its ordinary degrees above by zero. Thus all degrees are zero or -1. Euler characteristics give

`chi_G(F^+)=D`,

`chi_G(F^+(1))=Wp+S+T`.

Since `D W=S+T`, this forces `F^+=D O+Wp O(-1)`.

The degree-zero part is the actual constant subspace `H0(F^+)`, not an arbitrarily chosen horizontal complement. Its constant projection gives a saturated `Wp O(-1)` in the quotient ambient space. The projected map from F is zero or the unique nonzero equivariant map

`P O(-2)=(Wp W) O(-2) -> Wp O(-1)`.

The latter is the Wp-tensored Euler quotient and is onto everywhere. Since the derivative of projected F stays in the projected first span, this onto map would make the latter horizontal, contradicting its negative degree. If the map is zero, F and all its derivatives lie in the five-dimensional constant part, contradicting `rank F^+=7`. This excludes the line-sum kernel.

## 3. The doublet image and complete first polars

For `K0=W O(-9)`, the channel to `T O(-5)` is one-dimensional because `W Sym^4 W=S+T`. Its nonzero map is multiplication by the fourth power of the tautological line. Multiplication by a nonzero fourth power is injective on W at every fiber, so its rank is always two and its image is saturated. A nonzero combination of the two T channels remains injective and saturated, with one constant multiplicity line. There is no degree-allowed map to `O(-12)`.

The zero internal image would again produce positive degree 6 for F^+, and is impossible. Therefore `J=W O(-9)` and the exact image sequences give

`rank F^+=8`, `deg F^+=-8`.

The first-polar generation bound makes all eight degrees -1. The coefficient character is

`chi_G(F^+(1))=(Wp+S+2T)-W Sym^4 W=Wp+T=Sym^7 W`.

The first-polar morphism

`P W O(-1) -> F^+`

is onto and has equal rank and degree on both sides. It is therefore an isomorphism. This verifies the essential completeness assertion: the linear bundle is the entire first-polar system of the original quadratic block, not a quotient with an unaccounted relation or an independently chosen subsystem.

## 4. Universal linear coefficient-kernel lemma

The coefficient-kernel assertion in Section 4 can be established directly by the universal Euler sequence. Let `M=R O(-1)` be saturated in its constant coefficient span `C O`. Write

`a:R W -> C`, `K=ker a`, and `N=(C O)/M`.

The coefficient map a is onto by definition of C. For every tautological line l, saturation and fiberwise injectivity of M imply

`K intersect (R tensor l)=0`.

Projecting K along the tautological subbundle in

`0 -> R O(-1) -> R W O -> R O(1) -> 0`

therefore gives an everywhere injective bundle map and an exact sequence

`0 -> K O -> R O(1) -> N -> 0`.

After twisting by -2, its quotient map is the actual second fundamental form of the linear inclusion, under the Euler identification. Equivalently, the values and first derivatives of linear sections span all their constant coefficients at every point. Thus

`0 -> K O(-2) -> M -> N(-2) -> 0`,

`M^-=K O(-2)`, and `M^+=C O`.

This proves the claimed actual Gauss-kernel identification, including its equivariant coefficient representation and its twist. It also shows that no derivative ramification is suppressed.

Apply the lemma with `M=F^+` and `R=Wp+T`. Since F differentiates into M, it lies in `M^-`. Its inclusion between degree-minus-two bundles induces an injective coefficient map `P->K`. Furthermore

`R W=V+2P+D`.

The constant span has dimension at least nine: if it had dimension eight, the saturated rank-eight M would equal that constant bundle, contradicting degree -8. Hence `dim K=16-dim C<=7`. Semisimplicity and the displayed ambient representation now leave only `K=P` or `K=P+V`. In particular neither a second P nor D fits the remaining dimension budget.

The constant spans of F and F^+ agree: taking first polars cannot leave the coefficient span of F, and F is contained in F^+. Thus the C just classified is also the full actual constant span of F.

If `K=P`, then `C=V+P+D`, of dimension twelve. The quadratic coefficient surjection `P Sym^2 W->C` has equal source and target dimensions and is an isomorphism. This identifies the actual inclusion with the canonical P-tensored quadratic tautological inclusion, up to an equivariant identification of its constant span.

If `K=P+V`, then C has dimension nine, and N is an equivariant line of degree eight. It is `O(8)` with its standard linearization because the group has no nontrivial character. Both H0 and H1 of M vanish, so `C->H0(O(8))` is an isomorphism. The quotient map is therefore the complete evaluation map. Its kernel and derivative kernel are

`M=Sym^7 W O(-1)`,

`M^-=Sym^6 W O(-2)=(V+P) O(-2)`.

The P summand has multiplicity one and there is no map from P to V. Consequently F is exactly that unique P-isotypic summand. These are identifications inside the actual constant span, not merely character equalities.

## 5. Split-target torsion is impossible

Suppose the top map has generic rank two and image sheaf I with torsion quotient of length d in U. The sheaf I is locally free on the smooth curve. Since `I(2)` is a quotient of `P O`, it is globally generated, so H1 vanishes. The strict-top injection factors through its sections. Therefore

`4<=h0(I(2))=16-d`.

If d is positive, equivariance and the minimum orbit size imply `d>=12`, while the preceding inequality gives `d<=12`. Hence `d=12`, `deg I=-2`, and `H0(I(2))=P`.

The splitting degrees of I are at least -2 and sum to -2. Equivariant splitting and central parity leave exactly

`O(-2)+O`, `W O(-1)`, or `Wp O(-1)`.

The first two have twist-two sections `1+A`, while the last has P. Hence `I=Wp O(-1)`.

For the split target, the component to `O(4)` has equivariant Hom

`Hom_G(Wp,Sym^5 W)=Hom_G(Wp,T)=0`.

The image of I in `O(4)+O(6)` would then have generic rank at most one, contradicting its definition. This proves onto-ness for every generic rank-two split top image. Rank zero is already impossible by the strict-top section injection; PR814 excludes rank one. The split-target exhaustion follows.

This argument does not apply to `W O(5)`. In that case the relevant representation channel is nonzero, so the same contradiction is unavailable. Keeping the balanced torsion branch open is mathematically necessary.

## Verification boundary

This certificate uses exact bundle sequences, complete finite representation support, universal tautological and Euler identities, and the pinned zero-defect and strict-top hypotheses. It uses no selected actual HM or source coefficients, parameters, points, evaluated derivatives, instance matrices, instance ranks, model experiments, scans, or unapproved large computation. No new whole-source or whole-label exclusion is claimed.
