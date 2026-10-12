# Candidate presentation and identification audit

This note exports one cokernel and audits it against the rank-four plane-completion extension. The cokernel is called C. Both gates below fail to pass, so C is not identified with that extension. No length is computed. This is not a proof of the Weil-class theorem, and it is not a full solution.

Public sources are commits in `Akilleez-QA/read-em-and-weep` and the Stacks Project tags cited below. Reproduce the identities with `python3 -m unittest discover -s tests -t .` from this directory (`sympy==1.14.0`).

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

The formal chart fixes `beta(v)=+t0 h`. The scalar representative of `t0` is `z` on the finite base chart and `1` on the infinity chart. The central equation is `t0=0`.

The module exported here is C, the cokernel of the column below. The required ambient ring is a local ring of P^1×P^3 at the central points of `t0=0`, or an affine chart containing those points. Comment 6118997562 on PR #1 exports finiteness of support only: no support ideal and no point list are pinned, so no chart is certified to contain every central point.

The ring actually used is the affine chart

```
A = Q[z, x, y, h]
```

of the finite base chart times `W ≠ 0`, with `x=X/W`, `y=Y/W`, and normal coordinate `h=H/W`.

The proposed comparison is the zero-section pullback of the plane completion along `Tot(O(0,1)) → Y`, with section `v=E0` of D-component 0, tested against the required pairing `+t0 h`. The finite-jet packages on the same plane-completion commit are the alternative route. The Horrocks–Mumford pullback on C^4 is a different object and is not a presentation of this extension.

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

The zero-section section is `v=E0` with D-component 0, so the pairing is 0. The required finite value is `z h`, and `z h` is not the zero polynomial. The local correction `v+q(t0 h)` has D-component `z h` and pairs to `z h` on each trivializing open. The plane-completion lemma states that those local sections do not automatically glue. The explicit base-isometry note states that the unchanged pullback does not admit a global section reducing to E0 and satisfying the required pairing even modulo `h^2`.

The first-normal, second-normal, and third-normal packages on `fa685b9dd33e1c8a4336f6a8086c56f3ceb3bc3b` realize jets through `h^3` on the completed plane object. Each states that it does not identify a carrier. The formal chart states that a relative carrier presentation, total-space reflexive hull, central reduction, and central hull are not computed. `order_1.json` has keys `D`, `Ev`, and `N` (plus bases and one preimage), which are maps in that deformation complex.

## Missing map

The missing comparison is a homomorphism of presented modules

```
phi: C|U -> E|U
```

or a structured finite-jet certificate of that same homomorphism, on a common affine chart of an open `U ⊂ P^1×P^3` such that `D ⊂ U` and every irreducible component of the complement has codimension at least 2. No such matrix is in the pinned commits.

## Gates

Gate 1, reflexivity over a regular ring A: torsion-free and `codim Supp Ext^e(C,A) ≥ e+2` for every `e ≥ 1` (Stacks [31.13.13](https://stacks.math.columbia.edu/tag/0AVT)). Status: not run. The stop rule fires on the missing comparison, so no Ext module was computed and no inequality is reported as failed. Vanishing of `Ext^1(C,A)` and `Ext^2(C,A)` was not used.

Gate 2, identification: an actual isomorphism `C|U ≅ E` on a common open containing D whose complement has codimension at least 2, together with reflexivity of C, identifies the underlying sheaf with the reflexive extension by Stacks [31.13.12](https://stacks.math.columbia.edu/tag/0EBJ). Status: failed. Naming such a U does not supply `phi`. The zero-section pairing is 0 rather than `+t0 h`.

C stays C. No length is reported.

## Scope

Comment 6120496899 on PR #1: passing this carrier gate is not a proof of the Weil-class theorem. This audit does not pass the gate.
