# Independent review: Picard defect under blowup

**Verdict: PASS (independent mathematical review; not formal verification).**

Reviewed `PROOF.md`, titled “Blowing up the universal Picard defect does not split the family.” Review scope is the one-node structural continuation of the pinned universal residue complex. No selected actual HM/source-instance evaluation, numerical experiment, large computation, repository write, or public communication was performed.

## Dependency verification

The reviewer independently fetched and read the exact dependency:

- Repository: `Akilleez-QA/read-em-and-weep`.
- Commit: `df1e09bb456974ec43ab598709bd60d0378cfedf` (PR584).
- Path: `research/hm/picard-defect-singularity/PROOF.md`.
- Returned Git blob SHA: `b01265502444518ca1d4aaf81b7c04359048bb2e`.
- Source: <https://github.com/Akilleez-QA/read-em-and-weep/blob/df1e09bb456974ec43ab598709bd60d0378cfedf/research/hm/picard-defect-singularity/PROOF.md>.

That source supplies the regular four-entry column, its resolution of K, the actual reduced residue complex, the inherited conductor inclusion, and the residue-extension class `(t1,1)`. The new proof preserves these inputs rather than replacing the actual family by a model inferred from dimensions. Replacing the column `−δ` by `δ` is an invertible target change and does not affect the conclusions.

## Checks and findings

### 1. Blowup charts and geometry

The substitution `τ=t1`, `δj=t(j+1)−t1` correctly expresses the Laurent parameter ring as the stated localization of a polynomial ring. The center is a smooth coordinate subspace of codimension four. The chart ring in equation (4) is correct, including all four inverted factors `τ+e uj` and the convention `ua=1`. It is a domain, and e is a nonzerodivisor. The charts have no extraneous components. The trivialized conormal bundle gives `D ≅ Z0 × P³`.

### 2. Saturated line and exceptional twist

The saturated line is **O_X(D), not O_X(−D)**. Indeed, on a chart the map sends the frame `1/e` to the unimodular column v, and the original column is `δ=e v`. On overlaps, `eb=ub ea` and `vb=va/ub`, precisely matching the transition of `1/e`. Thus the subline is the pullback of the tautological O(−1) under the direction morphism to P³. Its restriction to D is `O_D(D)=O_D(−1)`.

The exact divisor sequence `0 → O_X → O_X(D) → i_*O_D(D) → 0` and successive quotients give the asserted canonical sequence

`0 → i_*O_D(−1) → f*K → Q → 0`.

Q is a rank-three vector bundle because v has a unit coordinate. The kernel is exactly parameter torsion: it is killed locally by e, while the quotient is torsion-free on integral X. Locally `f*K ≅ B³ ⊕ B/(e)`.

### 3. Global extension is genuinely nonsplit

The argument by restriction to an exceptional fiber F is valid. Since Q is locally free, tensoring the torsion extension with O_F preserves its injection. Right-exact restriction of the presentation identifies `(f*K)|F` with O_F⁴, because the column becomes zero. The resulting sequence is the tautological sequence

`0 → O_F(−1) → O_F⁴ → Q|F → 0`.

Any splitting would give a retraction `O_F⁴ → O_F(−1)`, impossible because `H⁰(P³,O(−1))=0`. This global nonsplitting is compatible with chartwise direct-sum decompositions and is distinct from the node-complex Postnikov obstruction.

### 4. Ordinary and derived pullback to X

The resolution of K has length one. Its pulled-back column remains injective because one coordinate is e and e is a nonzerodivisor. Therefore all positive parameter Tor groups vanish and `Lf*K ≃ f*K`. This correctly does **not** imply that f is flat or that f*K is torsion-free.

The terms of the actual node complex are parameter-flat; `E_A ≅ R⊗A` suffices for this purpose. Its derived pullback is the displayed termwise complex. The residue extension stays exact since its quotient is A-flat. Consequently its recomputed cohomology is exactly `m_X` and `f*K` in degrees zero and one.

### 5. Actual residue block and exact annihilator

The unimodular target column v can be extended to a basis on each chart, without changing the source or residue map. This yields the actual block `[E_B → B]` with differential `eβ`, plus `B³[−1]`. The short exact sequence of global complexes in equation (11) is also correct; the cohomological shift conventions consistently put the quotient Q in degree one.

The calculation `Ext¹_(R⊗B)(B,m_B)=B²` follows by scalar extension over C of the degreewise finite-rank nodal free resolution. It does not require B to be A-flat. In the inherited normalization basis, the residue class is `(τ,1)`, as required by the pinned input.

The long exact Ext sequence for `0 → B --e--> B → B/(e) → 0` gives the claimed injection `B²/eB² → Ext²(B/(e),m_B)`. Its image of `(τ,1)` is precisely the Yoneda splice for the actual residue block. The unit second coordinate proves the exact parameter annihilator `(e)`, including at every localization along D. Additivity in the first Ext argument gives the full chart Postnikov class `(κ_res,0)`.

The sheafified annihilator is O_X(−D). The cyclic subsheaf generated by the canonical local Postnikov section is `O_X/O_X(−D)=i_*O_D`; the proof's O_D notation here is naturally understood on X via pushforward. It is correctly distinguished from the twisted torsion sheaf `i_*O_D(D)`.

### 6. Exceptional restriction and pointwise splitting

Derived restriction of the parameter-flat actual complex to D has zero differential, so its degree-zero cohomology is E_D rather than m_D. The residue extension measures the difference.

Derived restriction of f*K has an **untwisted** degree-minus-one Tor line O_D and degree-zero cohomology O_D⁴. Both assertions follow immediately from its two-term vector-bundle resolution with zero differential on D. Independently, the twist check is `O_D(D) ⊗ O_D(−D)=O_D`.

Thus exceptional restriction and passage to a torsion-free quotient are not interchangeable. On D the derived family splits after its cohomology changes; near D in X the unchanged relative family has nonzero Postnikov class. Away from D the chart residue block is quasi-isomorphic to m_B. These statements explain pointwise splitting without asserting unjustified global splitting on the complement.

## Overall assessment

No mathematical correction is required. The proof establishes its stated claims, including the signs/twists, canonical torsion sequence, global nonsplitting, exact exceptional annihilator, and derived-base-change distinction. Its conclusions remain conditional on the pinned geometric residue complex and do not establish selected HM/source-instance results, a full adjoint statement, higher-order lifting, multiplicative formality, or formal verification.
