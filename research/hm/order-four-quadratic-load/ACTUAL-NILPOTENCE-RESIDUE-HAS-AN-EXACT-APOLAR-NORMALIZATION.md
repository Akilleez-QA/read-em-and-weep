# Exact apolar normalization of the actual nilpotence residue

## Result and scope

Retain the marked cubic/quintic pair, actual regular X frame, fixed harmonic first-normal midpoint nilpotent, and scalar `chi` of `ACTUAL-HARMONIC-NILPOTENT-HAS-A-NONZERO-SECOND-NORMAL-RESIDUE.md`. Let `n_ap` denote the invariant degree-eight scalar section whose regular X representative is `n_x` in `APOLAR-NORMAL-SECTION-HAS-UNIT-EULER-COEFFICIENT.md`.

Then, in precisely that sign and marking,

`chi_bar = -(B lambda/4) n_ap`.

For the physical equation `q0=nu q`, the normalized scalar coefficient is

`chi_bar_physical = -(B lambda/(4nu²)) n_ap`.

All parameters remain unassigned. The factor is nonzero. This computes a scalar normalization of the **fixed midpoint nilpotent-extension obstruction**, not a fourth value. It does not set the unknown actual normal-generator scale `c_eta` or change the conic marking.

## 1. Fix the sign before reducing

The unit-Euler note uses `sigma=(f,g_x)` and

```
V1 = -2Ac X³z +3Bc XY²z² -B Y³,
V2 = -Bc lambda X³Y²/(2A) +3B²c lambda XY⁴z/A²,
sigma wedge V = f V2-g_x V1 = -n_x.
```

Thus `n_x=g_x V1-f V2`, not its negative. The verifier compares this scalar with the original `nx` in `verify_lowest_normal_class_apolar_reconstruction.py`; it does not rely only on a copied wedge formula.

The local `n_i` glue modulo `(f,g)²`, because their difference is `tr(n eta_ap)` in that ideal. Their vertex scalar class is the marked invariant nilpotent line; extend it by zero on the disjoint conic component. This defines the `n_ap` used here independently of an arbitrary scale for the actual deformation generator.

## 2. Reduce both representatives

Use the unique homogeneous remainder from the companion proof: eliminate `f² Sym²` first, then the residual `f g_x` pivot. Define

```
Phi = A²X⁴ -3ABc²z⁵X⁴ -4ABcz³X³Y +2ABzX²Y²
     +2B²c²z⁶X²Y² -4B²cz⁴XY³ +B²z²Y⁴.
```

The exact remainder of `n_x` is

`R_ap=lambda Y⁴ Phi/(Ac²z⁷)`.

The independently computed exact remainder of `chi` is

`R_chi=-B lambda² Y⁴ Phi/(4Ac²z⁷)`.

Consequently `R_chi=-(B lambda/4) R_ap` as complete polynomials, not merely on one coefficient. Both reductions are performed before taking their ratio. The ratio is independent of `X,Y,z`.

## 3. Stronger regular-chart identity

In fact the comparison holds with the following explicit regular ideal correction:

`chi+(B lambda/4)n_x = Q f²+a f g_x`,

where

```
Q = B²lambda²/(140A³) *
    (207Ac²z²X² -95AcXY -134Bc²z³Y²),
a = 7B²lambda c²z⁴/(6A).
```

These coefficients are polynomial on the entire X chart; no base poles or positive-variable denominators remain. This identity supplies a direct ideal-membership certificate in addition to the two complete normal-form reductions. It does not kill `chi` itself, because the surviving scalar class `n_ap` is nonzero.

The companion gluing theorem identifies the actual global residue as lying entirely in the invariant nilpotent line: its conic component and vertex constant vanish. Therefore this local marked equality determines its global proportionality, with the physical normal-line factor `nu^-2` retained.

## Verification

Run `python verify_actual_nilpotent_apolar_residue_normalization.py`.

It reruns the complete harmonic obstruction calculation, reduces both scalars, verifies the full regular ideal identity, and checks the sign against the original apolar reconstruction. No selected coefficients, actual-instance rank test, global second-normal midpoint extension, or endpoint nilpotent is introduced. The mathematical definitions and predecessor conventions are unchanged.
