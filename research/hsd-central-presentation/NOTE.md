# Candidate presentation and identification audit

This note exports one cokernel and audits it against the rank-four plane-completion extension. The cokernel is called C. Local Gate 1 passed on `W≠0`, and global identification (Gate 2 (ii)) is open, so C is not identified with that extension. No length is computed. This is not a proof of the Weil-class theorem, and it is not a full solution.

Public sources are commits in `Akilleez-QA/read-em-and-weep` and the Stacks Project tags cited below. Reproduce the identities with `python3 -m unittest discover -s tests -t .` from this directory (`sympy==1.14.0`, Python 3.12). A skipped pinned-blob check is not verified provenance. `REQUIRE_PINNED_BLOBS=1` turns those skips into failures. The run reports `provenance_skip_count`.

## Pins

Reported before the polynomial checks in `audit.py`.

| Role | Commit | Path |
| --- | --- | --- |
| Formal chart, central equation, required pairing | `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb` | `research/carrier/formal-five-parameter-chart/formal-chart.md` |
| Deformation-complex matrices | `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb` | `research/carrier/formal-five-parameter-chart/data/order_1.json` (and `order_2.json` through `order_6.json`) |
| Plane completion and pullback obstruction | `fa685b9dd33e1c8a4336f6a8086c56f3ceb3bc3b` | `research/carrier/plane-completion-lemma/PLANE_COMPLETION_LEMMA.md` |
| Base-overlap frames | `fa685b9dd33e1c8a4336f6a8086c56f3ceb3bc3b` | `research/carrier/plane-completion-lemma/EXPLICIT_BASE_ISOMETRY.md` |
| Finite jets on the completed plane object | `fa685b9dd33e1c8a4336f6a8086c56f3ceb3bc3b` | `research/carrier/plane-completion-lemma/first-normal-comparison/FIRST_NORMAL_COMPARISON.md`, `second-normal-comparison/SECOND_NORMAL_COMPARISON.md`, `third-normal-comparison/THIRD_NORMAL_SECTION.md` |
| Horrocks–Mumford pullback on C^4, excluded | `3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f` | `research/hm-carrier-and-atlas.md` |
| Named defect branch, empty `research/` tree, excluded | `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` | `research/` |

The central equation is `t0=0`. The scalar representative of `t0` is `z` on the finite base chart and `1` on the infinity chart.

Two sections are distinct. `p` is a local generator of the marked line `P`, and `α(p)` lies in `V`. `s` is the distinguished section with `β(s)=t0 h` and the prescribed plane value. The formal chart writes that pairing as `beta(v)=+t0 h`; the symbol `v` there is this section `s`, not `p`. Since `P=rad(G)` is contained in `ker β`, one has `β(α(p))=0`, so `α(p)` is not the section with the nonzero pairing.

The module exported here is C, the cokernel of the column below. The required ambient ring is a local ring of P^1×P^3 at the central points of `t0=0`, or an affine chart containing those points. Comment 6118997562 on PR #1 exports finiteness of support only: no support ideal and no point list are pinned, so no chart is certified to contain every central point.

The ring actually used is the affine chart

```
A = Q[z, x, y, h]
```

of the finite base chart times `W ≠ 0`, with `x=X/W`, `y=Y/W`, and normal coordinate `h=H/W`.

Torus weights from the formal chart, pinned before the checks: `wt(z,X,Y,W,h)=(2,1,1,0,-1)`, finite frame weights `(P,E0,E1,E2)=(3,0,2,2)`, infinity frame weights `(3,6,0,2)`.

Structure group, from PR #1 comment 6120632461. `V` is the symplectic rank-four completion. `G=P⊥` has rank three and radical `P`. `P` is an isotropic line, not a Lagrangian. The lifting group is the subgroup of `Sp(V,Ω)` that fixes the marked inclusion `α: P→V` pointwise. Its Lie sheaf is `Sym²(G)⊗L⁻¹`, of rank six, not `sp(G)`. Form preservation is strict, with the line bundles identified exactly.

The full-neighborhood comparison is not exported. The route in use is a homogeneous isomorphism over `D₂={h³=0}` to the checked plane-completion model, built from transition equations and gauge. The Horrocks–Mumford pullback on C^4 is a different object and is not a presentation of this extension.

## Exported cokernel

Ordered generators `(P, E0, E1, E2, D)`. Write `S=X^2+Y^2`, `F=XY`, `a0=X^3+Y^3`, `g=S-z W^2`. The finite relation in the formal chart is `r0=(-a0, W^6, -g, F)`. At `W=1`, extended by a zero D-component and constantly in `h`,

```
u = (-(x^3+y^3), 1, -(x^2+y^2-z), x y, 0)^T
C = coker(A --u--> A^5).
```

The infinity relation and the infinity-to-finite transition pinned in the formal chart are

```
ri = (-a0, S^3, -z^{-1} g, F),
TB = diag(z^3, 1, z^4, z^3) with the extra entry TB[E0,E1] = z Cpoly,
Cpoly = S^2 + z S W^2 + z^2 W^4.
```

`audit.py` checks `TB ri = z^3 r0`, `g Cpoly + z^3 W^6 = S^3`, and `a0^2 = g Cpoly + z^3 W^6 + T F^2` with `T=-3S+2F`. These identities place the column on the pinned plane data. They do not identify C with the rank-four extension.

## Comparison

The local form in the plane-completion lemma is

```
Omega((p,e,d),(p',e',d')) = Omega_E(e,e') + p d' - d p' + psi(e) d' - d psi(e').
```

On the finite chart, `Omega_E` has `Omega(E0,E1)=F`, `Omega(E0,E2)=g`, `Omega(E1,E2)=W^6`. Take the first argument to be the generator P, so `(p,e,d)=(1,0,0)`. The formula collapses to the D-component of the second argument. The coefficient of `psi(E0)` is the D-component of P, which is 0.

On this chart the column is unimodular: its `E0` entry is the unit `1`. With `a=x^3+y^3`, `g=x^2+y^2-z` and `F=xy`,

```
q(p_coeff, e0, e1, e2, d) = (p_coeff + a e0, e1 + g e0, e2 - F e0, d)
```

satisfies `q(u)=0`, the section inserting `e0=0` splits `q`, and `ker q` is the free line on `u`. Every entry of `u` has derivative `0` in `h`. So on `W≠0`, `C` is free of rank 4, hence reflexive, and `Ext^e(C,A)=0` for `e≥1`. That does not identify `C` with the rank-four extension and does not evaluate a defect of that extension.

The unchanged pullback of the distinguished section `s=E0` has D-component 0, so its pairing is 0. The required finite value is `z h`, and `z h` is not the zero polynomial. The local correction of `s` by `q(t0 h)` pairs to `z h` on each trivializing open. The plane-completion lemma states that those local sections do not automatically glue. The explicit base-isometry note states that the unchanged pullback does not admit a global section reducing to `E0` and satisfying the required pairing even modulo `h^2`. That rejection is for this choice of `s`, with fixed `β` and fixed plane value. It does not rule out every comparison that uses different structure data. `β(α(p))=0` is the separate marking identity.

The first-normal, second-normal, and third-normal packages on `fa685b9dd33e1c8a4336f6a8086c56f3ceb3bc3b` realize jets through `h^3` on the completed plane object. Each states that it does not identify a carrier. The formal chart states that a relative carrier presentation, total-space reflexive hull, central reduction, and central hull are not computed. `order_1.json` has keys `D`, `Ev`, and `N` (plus bases and one preimage), which are maps in that deformation complex.

## Structure group, checked as linear algebra

On a 4-dimensional symplectic space the standard line is isotropic, its perpendicular has rank 3, and the radical of the restricted form is that line. A Lagrangian would have rank 2. The Lie algebra of endomorphisms that are infinitesimally symplectic and kill a generator of the line has rank 6, the same rank as `Sym²` of a rank-three bundle. These counts are the corrected stabilizer. They are not a matrix `φ_i`.

The order-0 frame shape exported by the plane-completion refinement is the identity on the `B` basis, with the extra column a shift of `q`. That matrix fixes the generator of `P` and does not depend on `h`. It is not a series modulo `h³`.

## Missing map

The missing comparison on `D₂={h³=0}` is a chartwise matrix `φ_i` with entries in `Q[z,X,Y,W,h]/(h³)`, valued in the stabilizer of `α`. No such matrix is pinned. That absence is an inspected-source / reporting conclusion, not a computed polynomial input, so the following checks are not evaluated and no entry is reported as a failed polynomial. They would be required modulo `h³` on every chart and overlap:

- (a) `g'_ij = φ_i g_ij φ_j^{-1}`,
- (b) `φ^T Ω φ = Ω`, strict,
- (c′) `φ(α(p))=α'(p)`, the pointwise marking, not a section identity,
- (d) `β'∘φ=β`, derived from (b) and (c′) alone, with no section hypothesis and no `H⁰` vanishing,
- (e) the torus weight of every entry of `φ`,
- (f) `φ(s)=s'`, only after (d), using `H⁰(G⊗I^k/I^{k+1})=0` from the exact pairing and the plane value.

The overlap formula `I - h A_η + h²(½ A_η² - A_κ)` is an operator on Hamiltonian cochains, not `φ_i`. `A_η` and `A_κ` from `Sym²(G)⊗L⁻¹` annihilate `α(p)` because `Ω(u,α(p))=0` for `u∈P⊥`, so their exponential gauge fixes `α` pointwise; they are target transition operators and do not supply candidate-to-target `φ_i`. Square-zero uniqueness does not supply the matrix. Automorphisms of a square-zero deformation of a smooth separated scheme are `H⁰` of the tangent sheaf twisted by the kernel (J. Alper, *Notes on Deformation Theory*, UW Math 581J, Fall 2021, Proposition 2.5(1); the notes cite Hartshorne, *Deformation Theory*, Corollary 10.3). That `H⁰` is not an input to (d).

## Reporting decisions

These statuses are reporting decisions, not computed certificates. The computed input is the splitting on `W≠0` and the pairing values. The absence of `φ_i` is an inspected-source / reporting conclusion, not a computed polynomial input, and no entry is reported as a failed polynomial.

Gate 1 on `W≠0`: passed. `C` is free of rank 4 there, hence reflexive, and `Ext^e(C,A)=0` for `e≥1` (Stacks [31.13.13](https://stacks.math.columbia.edu/tag/0AVT)). This does not identify `C` with the rank-four extension and does not evaluate a defect of that extension.

Gate 2 (i), the chosen structured section: computed. The unchanged pullback of `s=E0`, with fixed `β` and fixed plane value, has pairing `0` rather than `z h`.

Gate 2 (ii), an underlying sheaf comparison `C|U → E|U` on a neighbourhood of all of `D`, with any structure data: open, not failed. `C` is exported only on `W≠0`, and no global gluing is pinned. Neither (i) nor the cited obstruction of the unchanged pullback rules out every comparison with different structure data. Reflexive extension (Stacks [31.13.12](https://stacks.math.columbia.edu/tag/0EBJ)) is not applied. The `D₂` checks stay unevaluated because `φ_i` is missing.

One-column cokernels have projective dimension at most 1, so `Ext^2` vanishes. An exact length-one resolution proves zero defect only for the actual identified reflexive sheaf, with no inference through a later hull. Any defect statement is conditional on `φ`.

`C` stays `C`. No length is reported. The audit does not proceed to a defect number; that stop does not certify that every comparison fails.

## Scope

Comment 6120496899 on PR #1: passing this carrier gate is not a proof of the Weil-class theorem. This audit does not pass the gate.
