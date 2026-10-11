# Five framed parameters for a homogeneous formal lift

This package isolates a finite exact calculation and its all-order formal consequence for one fixed plane model. The first jet has four framed coordinates `(a,b,c,d)` at the prescribed positive pairing. The scalar obstruction to the second jet is identically zero. A fifth coordinate `lambda` remains at order two. Every such homogeneous two-jet has a compatible formal extension, unique under a gauge equal to the identity through order two.

The claim is **formal**. It does not construct a parameter-uniform algebraic carrier, a flat family of reflexive hulls, a constant defect length, or a zero-defect member. Automorphisms with nontrivial restriction to the original plane are not quotiented out.

## Run

Requires Python 3.10+ and SymPy 1.14.0. Install the one dependency if needed:

```sh
python -m pip install -r requirements.txt
python replay.py
python -m unittest discover -s tests -v
```

Run with assertions enabled, without `python -O`. All paths are relative to this package's own location. No network access or ancestor files are used by the replay. Exact rational calculation may take several minutes. `build/` contains regenerated certificates; the replay compares their parsed contents against `certificates/`. `SHA256SUMS` covers the shipped files, excluding itself and generated outputs.

## What is checked

- The complete prescribed source at order one has dimension 22, rank 19 and kernel dimension 3. Evaluation on that kernel has rank 1, leaving two fixed-pairing directions; two genuine `H^1(W_1)` directions give four in total.
- The exact origin and all four Laurent–Čech directions agree with `data/first_jet.json`. Original-cover regularity, plane degrees, character weights, and the origin's prescribed nonzero pairing are checked.
- The complete order-two block is `16 x 15`, of rank 15. The code reconstructs the vector quadratic polynomial over `Q[a,b,c,d]`, its scalar detector, and an explicit polynomial preimage `y` with `D2 y = obstruction`. This is exact polarization of a proved degree-at-most-two expression, with three extra off-grid checks.
- The complete order-three through order-six blocks have sizes `9,5,2,1` and determinant 1. Every rational inverse `Rk` is exported with `Dk Rk = I`. The full supplied maps respect the grading; at orders five and six the complete relation maps are checked, including their actual pivot sets and zero prescribed columns.
- Section matrices `N2,N3,N4` have full column ranks `84,112,144`. Explicit maximal minors have determinants `16,-512,-16384`. These constants are units in `Q[a,b,c,d,lambda]`; the last two are not determinant-one integer minors.
- All ten `W` filtration lines and four `U` lines give the parameter-independent weight bound; the section cutoff and ordered Čech homotopy signs are checked too.

The proofs, gauge convention and basis conventions are in [the theorem note](formal-chart.md). The output includes the full scalar/vector quadratic certificate, the constant higher inverses, and the section-minor indices.

## Dependency boundary

This is a self-contained **replay from supplied complete coefficient maps**, not a new derivation of those maps from all earlier transition matrices.

`data/order_1.json` through `data/order_6.json` contain the complete rational `D`, evaluation, `N` and, where relevant, `C` maps needed here, together with their source/target labels. No selected obstruction span is substituted for a complete map. `data/first_jet.json` fixes the coordinate convention. The checker rebuilds the actual first Čech cochains, bracket, mixed-square defect, relation division and quadratic obstruction from the displayed model; it does not read stored obstruction values.

The construction of the fixed rank-four symplectic plane object, and the identification of the supplied complete matrices with its sheaf-cohomology maps, are explicit inputs. This package checks the consequences of those inputs, their grading compatibility, the exact coordinate reconstruction, and the quadratic identity. It does not independently replay the omitted plane object's full rank-five symplectic presentation, all preceding higher-order normal-jet expansions, or any carrier/hull computation. No unavailable ancestor is needed for the advertised commands. The mathematical extension argument in the note uses the fixed object's symplectic structure and its stated homogeneous linearization; it is not a claim that a finite test alone proves every geometric hypothesis.

## Contents

- `formal-chart.md`: theorem, 4+1 conventions, section/gauge proof, all-order bound, and public references
- `data/`: compact complete coefficient inputs and frozen first-jet coordinates
- `check_early.py`: Laurent reconstruction and symbolic quadratic certificate
- `check_higher.py`: complete higher blocks, right inverses, and exact section minors
- `check_weights.py`: filtration cutoffs and universal elementary identities
- `certificates/`: expected exact outputs
- `replay.py`, `tests/`: isolated replay, integrity and regression checks

No Artin-approximation, uniform algebraization, reflexive-hull base-change, or defect-semicontinuity assertion is used.
