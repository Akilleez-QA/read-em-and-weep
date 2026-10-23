# Independent mathematical review

Independent mathematical review dated 2026-10-23.

## Verdict and scope

PASS. The final proof establishes the claimed canonical reductions of the actual opposite-parity multiplication pencil, conditional on the explicitly pinned geometric and cohomological input theorems. No blocking mathematical defect was found.

This review is bound to PROOF.md SHA256
`69e72653c1b7fe6925743c877210f0ee5714b284d9e1d370afd8bff279e4c1d8`.
The actual maps, equivariant parity, parameter/vertex identification, sheaf-versus-fiber distinctions, saturation, degree-zero Plücker argument, representation calculations, and mixed-ideal pushforward were checked mathematically. The five immediate source files were independently retrieved at their stated commit/path and compared byte-for-byte. Their returned Git blob identifiers and independently recomputed Git blob hashes agree with the manifest.

The review checks the use and applicability of the imported theorems. It does not independently recreate the entire transitive HM geometry behind the imported nonzero-vertex and hyperplane-exhaustion theorems, and does not claim that the arithmetic verifier proves those theorems.

## 1. Restriction rows and parity

The line splitting gives the stated physical eigensummands:
$$
B|_L(2)=O(9)_-\oplus O(2)_+\oplus O(-5)_-,\qquad
B|_L(3)=O(10)_+\oplus O(3)_-\oplus O(-4)_+.
$$
Thus the restriction targets have dimensions four and three, and representations Sym³W and Sym²W. Equivariant Serre duality uses the determinant-one binary representation; there is no extra one-dimensional character.

The ideal Koszul resolution for I_L B(2) requires exactly H²B(1), H³B(0), and H⁴B(-1). The first two are imported in the authenticated reachability theorem. For the last, the primary tensor resolution has E₀(-1)=15F(-4)⊕4F(-3), whose H⁴ is dual to 15H⁰F(0)⊕4H⁰F(-1), hence vanishes. Other controlling diagonal groups are above degree four. This correctly proves source restriction surjectivity. Target restriction surjectivity and the identification of R with the positive-generated middle are explicitly supplied by the reachability input.

Restriction and multiplication commute on actual bundles, hence the diagram (8) is a diagram of actual maps. The source of the opposite pencil is the negative 44-dimensional eigenspace tensored with the center-odd O_T(-1), not the positive 41-dimensional eigenspace. Nothing in this step identifies U₀ with a preceding positive-generated subspace.

## 2. Universal incidence and the crucial kernel comparison

The annihilator map from the hyperplane parameter line to its vertex in L is an actual, canonical projective-line identification. Keeping ν until the restriction has been formed prevents an unnoticed substitution of negative variables.

The universal equation remains a non-zero-divisor on L×T: its zero locus is the vertex graph of bidegree (1,1). Consequently restriction yields the claimed morphism between exact incidence sequences. Pushforward connecting maps are natural.

The positive part of the line sequence retains both O_T(10) and O_T(-4). The map from H⁰(O_L(10))⊗O_T evaluates onto O_T(10), with zero O_T(-4) component. The boundary therefore has kernel precisely O_T(10) and identifies O_T(-4) with ker β. This checks the potentially delicate H⁰ contribution; it cannot be discarded.

The actual extending F(2) sections are positive. Their vertex values therefore lie in O_T(-2), not O_T(5). Their quadratic products lie in O_T(-4), with zero O_T(10) component. Combining restriction of products with the natural connecting maps and the imported actual square-section identification proves that the induced map ker Γ→ker β is Sym²(ev), up to the harmless common boundary-sign convention stated in the proof. The argument is a sheaf argument on all of T, not a generic-fiber calculation.

## 3. Reduced kernel and unchanged cokernel

For a rank-two bundle surjecting onto a line, with line kernel M, multiplication identifies the kernel of its symmetric-square quotient with M⊗Y. This can be checked in a local basis of M and a lift of a generator of the quotient, and uses no global splitting.

Here it gives
$$
\ker(\operatorname{Sym}^2(ev))=O(-4)\otimes W O(-3)=W O(-7).
$$
The map onto O(-4) is surjective everywhere because ev is. The snake lemma therefore gives both the asserted reduced kernel and the canonical isomorphism coker Γ₀→coker Γ. The latter is the actual isomorphism induced by inclusion R⊗O_T→P₃⊗O_T; it is not a numerical identification. Rank five and total degree 26 are consistent in all presentations and include torsion degree.

The base-change exact sequence (15) is valid: factor Γ₀ through its locally free image J, tensor the exact kernel-to-image sequence, and then use Tor for 0→J→R⊗O_T→C→0. It does not require C to be locally free.

An individual reduced fiber-kernel section is tested only by its O(-4) vertex component. A possible O(10) component is killed by the line boundary. The distinction between such exceptional sections and extending vertex-vanishing square sections is correctly retained.

## 4. Canonical constant subpencil and the Plücker step

The image sheaf J is locally free because it is torsion-free on the smooth curve T. The cohomology of O_T(-1) gives
$$
H^0(J)=H^1(W O_T(-7))\simeq W\otimes\operatorname{Sym}^5W,
$$
with dimension twelve and character V+P+D.

Its inclusion in R is actual. Under J⊂R⊗O_T, evaluation of a basis of H⁰(J) gives independent constant vectors. Hence C₁₂⊗O_T is a constant subbundle, rather than merely a generically injective evaluation image. The induced injection
$$
J/(C_{12}\otimes O_T)\hookrightarrow(R/C_{12})\otimes O_T
$$
proves that the quotient is torsion-free, hence locally free. This supplies precisely the saturation needed for the preimage E to be a subbundle of U₀⊗O_T(-1).

The rank and degree of E are 14 and -14. Therefore E(1) is a degree-zero subbundle of a trivial bundle. Its determinant has degree zero on P¹ and is trivial. The nonvanishing Plücker coordinates are global functions, hence constants, so its Grassmannian map is constant. This proves that E=H₁₄⊗O_T(-1) for the actual subspace H₁₄=H⁰(E(1))⊂U₀. No chosen direct-sum decomposition of Γ₀ is needed.

Twisting the first sequence (17) gives the representation identity
$$
[H_{14}]=[W\otimes C_{12}]-[W\otimes\operatorname{Sym}^4W]
=[W\otimes\operatorname{Sym}^6W]=[W'+2T_6].
$$
The stated binary-icosahedral identities and dimensions agree. In particular W′ is the other odd two-space, not V.

Quotienting by the preimage removes exactly the original kernel and C₁₂⊗O_T. The induced 26-to-31 map has zero sheaf kernel and the same C. It need not be fiberwise injective: its fiber kernel is Tor₁(C,k(t)). Thus no exceptional torsion has been removed by this operation.

## 5. Mixed ideals and actual first products

Since the blowup center and L are disjoint, p is an isomorphism near L, Z=p⁻¹(L) is its vertex section, and π|Z is an isomorphism. Left exactness of pushforward identifies π_*(I_Zp*B(3)) with the actual kernel of vertex evaluation, namely W O_T(-7).

The positive vertex-ideal higher direct image instead fits in
$$
0\to O_T(10)\to D_{\mathrm{vert}}\to C\to0.
$$
The surviving O(10) term is necessary. The final proof states the correct limited torsion consequence: tors(D_vert) injects into tors(C), but their equality or the existence and length of tors(D_vert) when C has torsion is not determined.

The identity
$$
p_*(I_Z O_X(-nE_{R_+}))=I_L I_{R_+}^n\quad(n\geq0)
$$
is checked locally near L and away from L, using the ordinary blowup ideal-power identity. Projection formula uses only the local freeness of B. No higher-direct-image vanishing or exceptional-fiber surjectivity is silently assumed. This proves the section formula for every n≥0, including the vanishing through n=6.

For F the vertex-vanishing pushforward is O_T(-4). After twisting, its first section is an invariant line at order four; multiplying it by the actual W at order three gives exactly the first adjoint W at order seven. The twist calculation F(6)×F(5)→B(10) and the ideal orders agree. This is an actual product statement, not merely a character calculation.

## 6. Independent bounded replay and limits

Both commands were independently run successfully against the final package:

- `python verify.py`
- `python -O verify.py`

The verifier uses explicit runtime checks, so optimization does not suppress its tests. It checks fixed nine-class character arithmetic, line-bundle parity/cohomology bookkeeping, dimensions, twists, rank/degree identities, and the five copied Git blob hashes. The old imported character script was read for its conventions, not executed.

The verifier does not certify the incidence comparison, naturality, same-cokernel assertion, saturation, or Plücker argument; these were checked mathematically above. No selected actual HM/source parameter, point, coefficient, matrix, derivative, or instance rank was evaluated. No large computation or external write was used.

The result remains a constraint on and a canonical presentation of the actual marked map. It does not determine the remaining quotient arrow, C's torsion lengths or local freeness, all mixed-square conditions, or actual source membership. No source exclusion or frontier-count change is justified by this review.

## 7. Exact reviewed files

SHA256:

- PROOF.md: `69e72653c1b7fe6925743c877210f0ee5714b284d9e1d370afd8bff279e4c1d8`
- verify.py: `f5e572f306d7fa1dd8281e07d637f4f08049c18494a5f4754559d456491e76ba`
- REPRODUCE.md: `6e7102be92e6011f07fa6548cbe72c272979085faea5b34aa617f99003271098`
- audit-inputs/manifest.json: `3e2e1ac009970ff9c5af4766c6b7c94a31887dee4af8c1c8e504cde9a0b59d23`
- audit-inputs/REACHABILITY.md: `2f135afb909aa11483274a1eae49cbb3aa311f36b66b478bbeab59ad38072f8b`
- audit-inputs/OPPOSITE.md: `58c5f822864f63a8ba2ff106692740c8e23c65475dacc7a52fb60d2052d4991d`
- audit-inputs/VERTEX.md: `82bf62d0e54ff7e2a57e9dee492cb6d720e20ce6ee1abcd12829cc9d8cca6691`
- audit-inputs/REGULARITY.md: `91334643653347f002f37a4b4346fb96e6e0edad31306a935a732858ef66a067`
- audit-inputs/CHARACTERS.py: `e81f548a7e0ea4069ea293ca3b86b1110c2fd6c2906e8637d1441b35f6f14af2`

## 8. Independently authenticated commit/path/blob associations

Repository: Akilleez-QA/read-em-and-weep. For each entry below, a fresh repository-file read at the exact commit/path returned the stated blob, and the returned UTF-8 content matched the local file byte-for-byte. Recomputing SHA1 of the Git blob header plus bytes gave the same blob.

- REACHABILITY.md: commit `e28d3b74d4288239426ad1e675e806310fadf8be`; path `research/hm/positive-reachable-middle/PROOF.md`; blob `060ad3bacb45086349e911265d6c0d6157bef4a0`.
- OPPOSITE.md: commit `db51525015bb7c5e825833d550d08dedf6f6ea96`; path `research/hm/order-four-quadratic-load/EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md`; blob `c9af11e07dd1c4535d9afee94a3c134607d534a3`.
- VERTEX.md: commit `c779b2919a36b9d45a6319d46551bd6380154bba`; path `research/hm/order-four-quadratic-load/NONZERO-VERTEX-EVALUATION.md`; blob `335702d20ff8a297050f81c7a2931302241f3ce4`.
- REGULARITY.md: commit `063da90fc4543304e87e701cdefcc08225412f17`; path `research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md`; blob `58785a8799c43fd2c7da089d0ddc5e05822132a9`.
- CHARACTERS.py: commit `db51525015bb7c5e825833d550d08dedf6f6ea96`; path `research/hm/order-four-quadratic-load/verify_negative_vertex_scalar.py`; blob `9eb58f03edde15dd612087440d8180e9e16d1755`.

The final PROOF.md was additionally checked against the earlier reviewed SHA256 `353e27435cb034a03c1da572571244ad20b4d54806b8b67a72f0388f3eec9e5f`: the only change is the precise Section 6 torsion limitation recorded above.

