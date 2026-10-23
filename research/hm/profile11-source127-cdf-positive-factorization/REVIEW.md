# Independent review of the positive-linear factorization proof

Reviewed 2026-10-23. Verdict: **PASS for the stated universal and formal-model conclusions, relative to the explicitly imported actual-HM theorems. No mathematical gap found in the reviewed proof.** This is an independent mathematical audit with bounded exact arithmetic, not proof-assistant certification or an actual-HM realization certificate.

## Exact reviewed versions

- `PROOF.md` SHA-256: `5b0dff3dd55c0d9ca9bb26c2b3cbadc3456e6a829ef96aa4e36b7c97639f283c`.
- `verify.py` SHA-256: `ae4db73b4979b6c391384a64d937c8fe2c449ceed097f57f6865673058389740`.
- `audit-inputs/manifest.json` SHA-256: `a5cc0b1cb8332c5519b5b82f2eb03853a6ff22acc4e884afb3b96f4020e2b5f5`.

The reviewer did not edit the proof or checker. The exploratory `derive_middle_character.py` is not the release verifier and is not needed for this verdict.

## 1. Independent source authentication and dependency scope

I read all five retained original inputs in full. For each, I independently recomputed the Git blob SHA-1 from the exact bytes, including the Git blob header, and obtained the manifest value. I also made five read-only GitHub file requests using each exact repository path and immutable commit. Each returned the same blob SHA. Thus authentication checks both retained bytes and the commit/path-to-blob association, not merely internal consistency of a local manifest.

Repository: `Akilleez-QA/read-em-and-weep`.

1. `AGGREGATE.md`: commit `38235cda736a554ca2c16af504a56e1daf756624`, path `research/hm/profile11-source127-cdf-aggregate-sharpness/PROOF.md`, blob `4dd68998c565b3a34ac95bc8dfa447144a5c9d60`.
2. `ACTUAL-MONAD.md`: commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, path `research/hm/order-four-quadratic-load/NEGATIVE-VERTEX-EVALUATION-SCALAR.md`, blob `4d2737b94c19b84816382984db9ecb91af66ef0e`.
3. `ACTUAL-OPPOSITE.md`: the same commit, path `research/hm/order-four-quadratic-load/EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md`, blob `c9af11e07dd1c4535d9afee94a3c134607d534a3`.
4. `REGULARITY.md`: commit `063da90fc4543304e87e701cdefcc08225412f17`, path `research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md`, blob `58785a8799c43fd2c7da089d0ddc5e05822132a9`.
5. `CHARACTERS.py`: commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, path `research/hm/order-four-quadratic-load/verify_negative_vertex_scalar.py`, blob `9eb58f03edde15dd612087440d8180e9e16d1755`.

The source assertions actually needed are present: the PR927 normal forms and formal maps; the normalized equivariant monad with `N=A+W'`; the actual coordinate representation `V+W` with `V=Sym²W'`; self-duality; the actual `H⁰B(3)=0`; the section resolution and primary vanishings; and the nonzero opposite-parity universal map with kernel `A O(-6)`. The proof uses these as imported results. This audit does not recursively reprove their upstream geometric theorems or independently revalidate every literature dependency of those original files.

## 2. Canonical factorization theorem

The curried map `C_q:T⊗X→T*⊗Y` is equivariant. Its image and evaluation give the asserted canonical factorization; symmetry of `q` gives precisely the positive-positive commutation identity.

For any other factorization, the restriction of the curried second arrow maps `im(a)` onto `im(C_q)`. Maschke semisimplicity over `C` therefore implies the required representation containment. Conversely an equivariant embedding and retraction produce the factorization. The reachable/observable quotient is exactly `im(a)/(im(a)∩ker(b̃))`, hence is canonically the image of `C_q`. If the entire middle dimension equals `dim M(q)`, the first arrow is onto and the second curried arrow is injective, giving the claimed isomorphism with the canonical factorization. No hidden rank or genericity assumption is needed.

## 3. Cohomological concentration and equivariant conventions

The normalized rank-two monad has ordinary first Chern class `-1`, so the underlying determinant is `O(-1)`. Two linearizations of this line bundle differ by a character: its invertible global functions are constants. Since `SL₂(F₅)` is perfect, there is no nontrivial character ambiguity. Thus the equivariant identity `End₀(F)(3)=Sym²(F)(4)` is valid.

The imported tensor-section resolution at twist three has terms `E₀=15F+4F(1)`, `E₁=35F(-1)`, `E₂=20F(-2)`, `E₃=2F(-4)`. On the controlling diagonal for `H³`, the only possible groups are `H³E₀` and `H⁴E₁`. They dualize to sums of `H¹F(-4)`, `H¹F(-5)`, and `H⁰F(-3)`, which vanish by the imported primary results. On the `H⁴` diagonal only `H⁴E₀` survives the dimension bound; it dualizes to `H⁰F(-4)` and `H⁰F(-5)`, also zero. The exact-kernel-sequence argument is valid. Together with imported `H⁰B(3)=H²B(3)=0` and trace splitting, it proves `[H¹B(3)]=-χ_G(B(3))`. No Euler-character equality is being promoted to actual cohomology without concentration.

The Euler-sequence class `Λ²H-Ht+t²` and all four coefficients `c_i` of the monad class are correct. Adams operations are applied in equivariant K-theory before taking the Euler characteristic. The rule `ψ²(t)=t²` and the character rule `χ_{ψ²(c)}(g)=χ_c(g²)` give exactly equation (1). Every final line twist is between two and eight, so there are no negative-twist Euler terms or omitted higher line cohomology. The source self-dual convention removes the coordinate/dual notation ambiguity. Central signs are then read on the resulting genuine cohomology representation, not guessed from total dimension.

## 4. Exact arithmetic and independent alternative calculation

I read the complete release checker and ran both `python verify.py` and `python -O verify.py`; both pass. Its explicit `require` checks are unaffected by optimization. Arithmetic is exact in `Q(√5)`. The nine character rows are orthonormal and complete, and the square-class map is exactly `(0,0,5,5,3,3,7,7,1)` in the retained ordering. The code implements the written λ-ring formula, verifies all nine class values, tests central signs and dimensions, and checks nonnegative integral multiplicities of the middle, minimal image, and complement.

For an independent computational cross-check, I did not use the release checker's `sn` plethysm routine. Starting with the authenticated binary trace values, I constructed each power-class map through `tr(g^k)=tr(g)tr(g^(k-1))-tr(g^(k-2))`. I computed the complete symmetric characters using Newton's recurrence

    h_n(H) = (1/n) Σ_{k=1}^n ψ^k(H) h_(n-k)(H).

These agree with the retained symmetric characters in degrees zero through eight. I then replaced the release checker's Adams formula by the rank-two identity

    Sym²(F)(4) = (F⊗F)(4) - O(3),

and evaluated the corresponding Euler character from the monad. This separate tensor/determinant route reproduces the result on every class. In the retained ordering the full `K₄` character is

    (100, -8, -(1+√5)/2, 5(1+√5)/2,
     -(1-√5)/2, 5(1-√5)/2, 1, 1, -2).

The resulting decomposition is

    K₄⁺ = 1+4A+2V+3P₄+3D,
    K₄⁻ = 3W'+3S+6T₆.

The central character value is `46-54=-8`, independently consistent with the parity dimensions. The tensor identities `V⊗V=1+V+D` and `V⊗P₄=A+P₄+D` also check at all nine classes.

The release checker's original-input authentication is conditional on the manifest being present. It was present and all five entries passed in the audited complete package. The checker certifies only bounded character identities and byte hashes; it does not itself certify the mathematical concentration argument or the imported geometric assertions.

## 5. Formal constructions and retained missing dependency

For the actual positive coordinate representation `V`, irreducibility, self-duality, and odd dimension imply that its invariant bilinear form is nondegenerate and symmetric. Each of the three PR927 maps has a surjective auxiliary `r:N₂→Π`, including the two single-support cases. Consequently its curried image is exactly `V*⊗Π`, not merely a quotient of it.

The minimal character is `1+A+V+P₄+2D`, of dimension 21. Subtracting it from the genuine positive middle character gives `3A+V+2P₄+D`, of dimension 25, with no negative multiplicities. The prescribed-middle embeddings and retractions therefore exist; the displayed arrows reproduce each original aggregate map and commute in the positive-positive square. Since these composites are unchanged, PR927's scalar and two `C²` compatible-algebra calculations remain applicable to the aggregate interface.

I checked the source and target of every equation in section 5. The four displayed remaining equations are exactly the two mixed squares from the two degree-three parities, the second positive-positive square, and the second negative-negative square. The necessary inclusions `ker γ⊆ker C` and `im D⊆im δ̃` follow from the stated factorizations and are not presented as sufficient. The proof expressly retains the actual opposite map with rank-three kernel bundle; it neither replaces it by zero nor assumes constant fiber kernels or torsion-free cokernel. It correctly disclaims a marked full-window realization, a full-module extension, actual coefficient identification, source exclusion, and a frontier-count change.

## Audit boundary

The positive-linear factorization condition alone is now genuinely resolved for all three formal aggregate alternatives through the authenticated actual middle representation. The remaining mixed-map/marked-relation problem is not resolved and is not hidden by this verdict.

All executed calculations were bounded abstract character arithmetic on nine fixed classes and finitely many symmetric powers through degree eight, plus local byte hashing and read-only source authentication. No selected actual HM/source parameters, actual coefficients, derivatives, actual matrices, instance-rank evaluations, or large computation were used. No publishing, merging, upstream submission, or external mutation occurred.
