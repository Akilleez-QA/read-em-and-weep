# Ancestor source inventory

Search date: 2026-10-11. Base tree: `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb` (tip of `research/carrier-five-parameter-formal-chart`). Every remote branch was listed, and every `research/` tree was searched for an ancestor of the fixed plane model in the five-parameter chart: open covers, rank-five symplectic data, frame or gauge identifications, and restriction or chain maps. Distinctive model strings (`O(3,-6)`, `W^6`, `omega(E0,E1)`, `X^2+Y^2`, rank-five symplectic presentation) occur only in that chart package and in the review copy of the same package.

Items (a), (b), and (c) are absent. The restriction-consistency script is therefore not part of this inventory. No comparison of ancestor data with the fixed-plane data or with the 66 stage objects was run, and no agreement is claimed. Ancestor existence and existence of a zero-defect member stay separate open questions; a future match under identical homotopy conventions would be a consistency test only.

## (a) Explicit ancestor cover

No explicit ancestor cover is present.

The fixed rank-four model has its own original cover, which is not an ancestor cover. At `ca9226569ddb5ed29d2809f1f4e4e1ae7c646ea8` and unchanged at `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`:

- `research/carrier/formal-five-parameter-chart/formal-chart.md` states the ordered plane cover `D(X), D(Y), D(W)` with both base charts, the relation vectors `r0`, `ri`, and the transition `TB`.
- `research/carrier/formal-five-parameter-chart/data/README.md` records the same ordered plane cover and the Čech degree conventions of `data/first_jet.json`.

The original-cover audit that evaluates cochains on that fixed cover was added at `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`:

- `research/carrier/formal-five-parameter-chart/audit_original_cover/check_original_cover.py`
- `research/carrier/formal-five-parameter-chart/audit_original_cover/README.md`
- `research/carrier/formal-five-parameter-chart/audit_original_cover/certificate.json`

`research/carrier/formal-five-parameter-chart/README.md` (same commit `ca9226569ddb5ed29d2809f1f4e4e1ae7c646ea8`) states that the replay uses no ancestor files and does not replay the omitted plane object's rank-five symplectic presentation. The review copy `research/hsd-review-61/REVIEW.md` at `1e7cc818973b38246d8616b0f475e426eda7fe73` records the same omission and does not reconstruct it. That review tree has no `audit_original_cover/` directory.

Missing source data:

- The ancestor ambient space and the rank-five symplectic presentation (bundles, symplectic form, and presentation or relation matrices).
- The ancestor open sets, their coordinates, and the transition cocycle on those opens.
- Any identification of an existing carrier or Segre construction as that ancestor.

Other Segre and carrier files were read and contain none of those data for this plane model:

| Commit | Path | Geometry recorded there |
|---|---|---|
| `1d7e6e558ae785469f14cc0dd03323ba13c3b04c` | `research/carriers/cayley/rank7_construction.md`, `image_geometry.md`, `README.md`, `verify_geometry.py` | Rank-seven quadric and Segre fourfold `(P^1)^4` |
| `2ab5ea8481adec9e9ba2240dc0eb3259c4c172ea` | `research/carriers/explicit-lange-abelian-monad.md` | Hamiltonian ribbon on a Segre graph |
| `dc6f35c003c80f14da5f34e2fbbe8c4d87e4869c` | `research/carriers/lange-relative-monad.md` | Ribbon on the Segre quadric `P^1 × P^1 ⊂ P^3` |
| `eb44f135c897e58922ccadf115028b3950f0b6fe` | `research/carriers/primitive_triple_obstruction.md` | Primitive-triple obstruction on a graph-Segre support |

## (b) Frame and gauge identifications

No frame or gauge identification from an ancestor to the fixed-plane chart is present.

The fixed model does record its own frame, at `ca9226569ddb5ed29d2809f1f4e4e1ae7c646ea8` (unchanged at `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`):

- `research/carrier/formal-five-parameter-chart/formal-chart.md`: ordered `B` coordinates `(P, E0, E1, E2)`, finite weights `d = (3, 0, 2, 2)`, infinity weights `(3, 6, 0, 2)`, transport `TB`, `TU = z^{-1} TB`, `TW = z^{-4} Sym^2(TB)`, and the formal gauge that is the identity through order two.
- `research/carrier/formal-five-parameter-chart/data/README.md`: coordinate order `0=P, 1=E0, 2=E1, 3=E2`.
- `research/carrier/formal-five-parameter-chart/check_weights.py`: the same weights and the off-diagonal relation identity `TB ri = z^3 r0`.
- `research/carrier/formal-five-parameter-chart/audit_original_cover/check_original_cover.py` at `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`: the same frame, `alpha`, and `Ω`, checked for transport and for the radical identity.

Missing source data:

- A basis identification from an ancestor frame to `(P, E0, E1, E2)`.
- The gauge, or an identity-gauge statement, taking ancestor cochains to `data/first_jet.json`.
- An identification of an ancestor alternating form with the displayed finite `Ω` entries `XY`, `X^2+Y^2-zW^2`, `W^6`.

## (c) Restriction and chain maps to the fixed-plane chart

No restriction morphism and no chain map from an ancestor complex to the fixed-plane chart is present.

The fixed-plane inputs that such a map would have to hit are:

- `research/carrier/formal-five-parameter-chart/data/first_jet.json` and `data/order_1.json` through `data/order_6.json` at `ca9226569ddb5ed29d2809f1f4e4e1ae7c646ea8`.
- The 66 c,d stage objects in `research/carrier/formal-five-parameter-chart/audit_original_cover/certificate.json` at `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`, under `c_d_raw_stages`.

Missing source data:

- The geometric restriction (which plane, which conormal, and the quotient by the line `A`).
- The induced map on Čech cochains, including signs and the cover refinement it uses.
- The explicit image of that map in the fixed-plane matrices and in the 66 stage objects.

## (d) Homotopy conventions for the 66 c,d stage objects

Present. Source: `research/carrier/formal-five-parameter-chart/audit_original_cover/check_original_cover.py` and `certificate.json` at `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`. The prose convention is in `formal-chart.md` §6 and `audit_original_cover/README.md` at the commits above. The support-pattern sign check is `check_weights.py` at `ca9226569ddb5ed29d2809f1f4e4e1ae7c646ea8`, recorded as `plane_homotopy_basis_checks: 20` in `certificates/weight_certificate.json`.

The 66 objects are the stage cochains of the six monomials `c`, `d`, `a*c`, `a*d`, `b*c`, `b*d`. Each monomial stores these 11 stages, and `6 × 11 = 66`:

`finite_BCH`, `infinity_BCH`, `mixed_BCH`, `relation_defect`, `relation_quotient`, `relation_finite_primitive`, `relation_infinity_primitive`, `relation_mixed_primitive`, `closed_finite`, `closed_infinity`, `closed_mixed`.

The certificate also stores `c*c`, `c*d`, and `d*d`. All 11 stages of each are empty, so those three monomials are outside the 66. Term counts on the six nonempty monomials are 241, 238, 107, 100, 94, and 94.

Conventions used to build those stages, all exact over `Q`:

- Exponent order `(z, X, Y, W, P, E0, E1, E2)`. A Hamiltonian occupies the last four slots. The bracket is `{p, q} = grad(p)^T Ω grad(q)` by polynomial differentiation. Finite `Ω` is `ω(E0,E1)=XY`, `ω(E0,E2)=X^2+Y^2-zW^2`, `ω(E1,E2)=W^6`.
- For first cochains `(eF, eI, h)`, the quadratic BCH components are `qF = {eF01, eF12}/2`, `qI = {eI01, eI12}/2`, and `qH_ij = ({h_i, T eI_ij} - {eF_ij, h_j})/2`. The factor `1/2` is the polarized normalization. These three tensors are `finite_BCH`, `infinity_BCH`, and `mixed_BCH`. They do not use the plane homotopy.
- `relation_defect` is `T qI - qF - δ qH`. `relation_quotient` is exact division by finite `alpha`, using the geometric unit `alpha_E0 = W^6` on the triple overlap, accepted only after every coefficient is reconstructed.
- `relation_finite_primitive` and `relation_infinity_primitive` are the triangular base split of the projected relation, with transitions `z^2, z^3, z^2` on `P, E1, E2` and `z^{-1}` on `E0`.
- The ordered plane homotopy is applied to the residual after that split. It produces `relation_mixed_primitive`. `closed_mixed` then subtracts `alpha` times that primitive. `closed_finite` and `closed_infinity` subtract `alpha` times the base primitives and do not call the homotopy again.
- Plane order is `X, Y, W`, indices `0, 1, 2`. For each monomial the pivot is the first of these coordinates whose exponent is nonnegative. If that pivot lies in the current open simplex, it is removed. The sign is `(-1)` to the position of the pivot in the ordered open tuple. Exponents are unchanged. The zero polynomial is dropped. The Čech differential on a simplex is the alternating sum of faces, sign `(-1)^i`.
- `formal-chart.md` §6 requires `δK + Kδ = 1 - Π` on positive Čech degrees, where `Π` is projection to the all-negative top cohomology. `check_weights.py` checks that sign identity on support patterns. The 66 objects themselves are produced by the monomial-wise homotopy in `check_original_cover.py`, not by a second convention.

## Character bookkeeping

Character bookkeeping: with `d=(3,0,2,2)` and `wt(z,X,Y,W)=(2,1,1,0)`, each nonzero `Ω_ij` in `{XY, X^2+Y^2-zW^2, W^6}` has `wt+d_i+d_j=4` on pairs `(E0,E1)`, `(E0,E2)`, `(E1,E2)`, so the bracket character is `0-3-2+4=-1`.

Exact integer check, run with this inventory: `XY` has weight `2` and `d_E0+d_E1=2`; each of `X^2`, `Y^2`, and `zW^2` has weight `2` and `d_E0+d_E2=2`; `W^6` has weight `0` and `d_E1+d_E2=4`. Each sum is `4`. The sum `0-3-2+4` equals `-1`. The summands are the finite-convention characters used for this bracket: parameter `λ` has weight `0`, the order-1 offset of `η_1` is `k-4=-3`, and `κ_2=z^{-1}E_0^2` has `χ=2s+x+y=-2`.
