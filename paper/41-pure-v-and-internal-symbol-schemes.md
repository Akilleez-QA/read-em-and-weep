# Pure-V geometry and internal-symbol schemes

**Supersession through PR973:** under actual Type II and full-radical Q compatibility, μ is now proved zero. The nonzero-μ discriminant scheme and kernel calculations below remain valid universal results under their explicit scalar alternative, but that alternative cannot arise under these actual hypotheses. The original second symbol and actual quotient first-symbol transfer are recorded in [chapter43](43-radical-naturality-and-second-symbol.md).

**Craig Ward · 23 October 2026 · Update through PR969**

The necessary relation remains **four pairs across three stable labels**, distributed **2 + 1 + 1**. The results below constrain different maps and parameter spaces; their ranks and exceptional loci must not be combined into a claim of full repair. No Q-compatible pure-V line or actual Type II scalar branch is selected.

## 1. Pure-V quotient: twelve reduced linear-arrow degeneracies

[PR963](https://github.com/Akilleez-QA/read-em-and-weep/blob/410fc6d7dac16afc4af29590fa5d4e8b8a5dc0a4/research/hm/source2-pure-v-torsion-quotient/PROOF.md) treats every balanced source2 endpoint and both residual coupling classes without assuming Q compatibility. For a nonzero pure-V radical j, the quotient N/im(j) has dimensions (36,48,33). Its first linear arrow has rank 36 away from the invariant orbit D12 and rank 35 on it. The maximal-minor degeneracy scheme is exactly the **reduced twelve-point divisor**, with length one at each point. The common first-arrow kernel is zero, and every nonzero second arrow is onto the last 33-space.

The embedded endpoint quotient is a genuine torsion evaluation pencil of dimensions (12,12,5): multiplication on sections of O(16), O(17) and O(18) restricted to D12, with the final space quotiented by the endpoint-dependent restriction of A18+P_t. This retains both actual arrows and the embedded endpoint data.

The universal first-arrow cokernel has torsion of length twelve. Its torsion-free quotient is Sym⁸(W) O(1) ⊕ A O(5), rank twelve and degree 24. The sheaf sequence splits equivariantly but not canonically. **This is not a splitting of the full two-pencil residual extension**, Q stability, or an equivalent cancellation of the pure-V obstruction problem.

## 2. Pure-V image: ten reduced bad quadratic directions

The different map in [PR966](https://github.com/Akilleez-QA/read-em-and-weep/blob/4d0a6713a9c81fe669967e1d23838bdc8f4162b6/research/hm/source2-pureV-quadratic-discriminant/PROOF.md) is the image subsystem

T_a: H⁰(O(4))=D → H⁰(O(6))/V6=P, s↦[a s].

For nonzero negative quadratics a it has rank four except at exactly **ten reduced projective directions**, where rank is three. Every exceptional quadratic has distinct roots: the fixed points of one cyclic order-three subgroup of the projective icosahedral group. Together the roots form its twenty-point orbit. **Every nonzero square quadratic has rank four.** These ten points in P(Sym²W) are not the twelve linear-arrow points in P(W) from section1.

The proof uses the length-two restriction of V6. A Wronskian of degree twelve and orbit-size bounds show that its degree-six plane map is everywhere immersive, excluding double-point divisors from the bad locus. The map is birational onto its image. A universal evaluation sequence gives the rank-drop scheme length ten; symmetry forces one orbit with local length one. The maximal-minor scheme of T_a agrees with that evaluation scheme by equality of cokernel Fitting ideals, not just equal supports.

If a pure-V radical is Q-compatible, its **image** complex is D[[t]]→P[[t]] with differential tT_a. Away from the ten points its cohomology has free kernel rank one and four length-one torsion cokernel summands. At the ten points these become free kernel rank two, free cokernel rank one and three length-one torsion summands. These groups are not automatically the full obstruction complex's groups; no acyclic image cancellation follows.

### Classical attribution and missing bridge

The plane curve is the **classical Winger rational sextic**. [Dolgachev, §7, pp.130–131, with representation conventions on p.120](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/icosahedron-Dolgachev.pdf) gives the degree-six map from the binary-icosahedral two-space into the projectivized dual of the other three-dimensional representation and identifies its image. The comparison here is representation-theoretic: identify that two-space with W; pullback embeds the other irreducible three-space in Sym⁶W. Multiplicity one forces it to be V6, up to target projective coordinates. The curve and ten-node geometry are therefore not claimed as novel.

[Dolgachev–Farb–Looijenga, Remark 5.12 and §4.1](https://link.springer.com/article/10.1007/s40879-018-0231-3) describe the ten nodes through antipodal pairs in the twenty-point orbit, consistent with the intrinsic subgroup description. This attribution does not establish source2 compatibility.

[Hulek, VIII.3.7–3.9, pp.122–123](https://www.numdam.org/item/AST_1986__137__1_0.pdf) places the sextic in tangent-at-origin incidence geometry of elliptic normal quintics and an invariant-quintic evaluation condition. Those scalar **quintics must not be conflated with our quadratic Q**. [Barth–Hulek–Moore, Proposition 6.1 and Remark 6.2, pp.749–751](https://gdz.sub.uni-goettingen.de/id/PPN235181684_0277) give the corresponding planar parametrization; their subsequent rational curve in projectivized HM section space has a different target. No identification of that latter curve with the plane sextic, or transport of these incidence conditions to the present obstruction operation, is established here.

The attribution rests on the cited primary-source passages checked for this project, not an independent reproof of those papers. Novelty of the present conditional obstruction-interface application is not settled by identifying the classical curve.

**Scope update through PR970:** of the two historical P-surplus footprints used below, only (2,0,0) remains possible under full-radical compatibility. The universal symbol and scheme results retain their stated scalar hypotheses; the actual μ branch is not selected. See [chapter42](42-polar-integrability.md).

## 3. Type II: the full internal symbol and its two scalar alternatives

Assume an actual Type II occurrence, full radical Q compatibility, and one of the two P-surplus footprints (1,1,0) or (2,0,0). [PR965](https://github.com/Akilleez-QA/read-em-and-weep/blob/de8e1d1a90d6f41dffa74df7cc7220c4e84bf4e7/research/hm/source126-typeII-internal-discriminant/PROOF.md) determines the internal first symbol in binary-form coordinates:

b_a(k,h)=λ a k + μ {a,h}₁, with λ≠0, k∈A=Sym²W and h∈D=Sym⁴W.

The first transvectant {a,h}₁ is the alternating first-derivative pairing. Multiplicity-one G-equivariant Hom spaces force this expression. Its universal SL₂ covariance is then used to classify ranks; no SL₂ action on the actual HM module is presumed.

| Scalar branch | Nonzero quadratic direction | Rank | Kernel dimension | Cokernel dimension |
|---|---|---:|---:|---:|
| μ=0 | Any | 3 | 5 | 2 |
| μ≠0 | Square | 4 | 4 | 1 |
| μ≠0 | Nonsquare | 5 | 3 | 0 |

At this historical checkpoint the vanishing choice of μ was unresolved; PR973 now selects zero under the actual full-radical hypotheses. These are internal first-symbol ranks. Its internal D cokernel maps to zero in the original P cokernel, so this does not contradict original first-Bockstein vanishing or prove original-map surjectivity.

## 4. Reduced projective conic, affine ideal and the Tor correction

Under the further branch μ≠0, [PR969](https://github.com/Akilleez-QA/read-em-and-weep/blob/3e1d81ec3bd42a55d06321b57ee1f62822a6dcc3/research/hm/source126-typeII-symbol-cokernel/PROOF.md) upgrades the preceding rank locus to a scheme and bundle theorem. Put C equal to the discriminant conic in P²=P(Sym²W), and let Φ:8O(-1)→5O be the universal symbol. Its cokernel is i_*O_C(2), and its kernel K is locally free of rank three:

0→K→8O(-1)→5O→i_*O_C(2)→0.

The projective maximal-minor scheme is the **reduced conic**. In homogeneous coordinates with Δ=β²−4αγ and m=(α,β,γ), the raw ideal is **I₅(Φ)=Δ m³**, not (Δ). Saturation gives (Δ); the affine cone vertex retains additional structure. A transverse universal derivative establishes multiplicity one, and exact minors establish the full homogeneous ideal.

The kernel class is [K]=8[O(-1)]−6[O]+[O(2)], with c₁(K)=−6H and c₂(K)=12H². Along the Veronese parametrization ν:P¹→C, two different kernels must be distinguished:

- the ambient kernel restricted to C: ν*K=Sym²W⊗O(-4), rank three;
- the kernel of the restricted map: ker(ν*Φ)=Sym³W⊗O(-3), rank four.

They fit into 0→ν*K→Sym³W⊗O(-3)→O→0. The last map is a nonzero multiple of complete cubic evaluation; the quotient is the Tor₁ correction, not an additional direct summand of K|C. Equal total degrees do not make the two kernels identical.

These conclusions concern the forced universal internal expression under explicit conditional hypotheses. They do not select μ, exclude either P-surplus footprint, determine an original higher obstruction, or lower the pair count.

## 5. Evidence and live boundaries

Independent reviews report ordinary and optimized verification passing **192 checks for PR963, 127 for PR965, 76 for PR966 and 146 for PR969**, with immutable inputs authenticated. PR969 includes all 56 maximal minors and a ten-minor cubic spanning certificate. The universal written arguments supply geometry, gluing, reducedness and filtration claims; bounded exact checks are supporting evidence, not actual-source experiments or proof-assistant verification of the full chain.

The remaining conditions include pure-V Q compatibility, the actual Type II μ branch and the original obstruction problem beyond these image/internal restrictions. The published stronger joint-row theorem PR970 is incorporated in chapter42; no unpublished scalar-selection claim is incorporated. Historical diagrams remain unchanged, and no total completion estimate is attached to these advances.
