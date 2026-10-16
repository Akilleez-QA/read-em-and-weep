# Complete standard branch: executable finite coefficient requests

`standard.py` executes

    B = R (K_cov Pi + A h S Pi) F.

It implements both terms using actual finite chain maps, rather than a prism-only substitute or declarative operator nodes. Its only executable domain is bounded artificial data. No physical coefficient, historical seed, or obstruction value has been evaluated.

Run from this directory:

    python -B run_controls.py

This runs the 12 producer controls normally and with `-O`, each under a hard 512 MiB address-space limit, a 59-second CPU limit, and a 60-second parent wall timeout. The receipt records measured process maximum RSS separately from the address-space limit. The controls check all 81 tensor cells and all 560 standard triangles, a nonzero example needing both branches, tensor-h predicates/signs, derivative shifts, cleared-numerator convolution with source ordering, full owner preservation, whole-standard extension, F12/F34 harmonic remainders, and physical admission rejection.

## Interfaces and execution

The shared types are imported as the single Python module `interfaces` from `../inserted-coefficients/interfaces.py`. Owners retain all five fields `(seed, occurrence, carrier, legal_mask, standard_tag)`. Standard tags use high-bit coordinate order. Source ordering is auxiliary-first carrier, numeric low-bit mask, then standard tag. A cleared source oracle accepts only source-sorted triples and does not apply another alternating sign.

`PiCoefficientProgram(F, Qhat, fibers, extension, pair)` consumes the shared `ClearedFOracle`, `QuotientOracle`, `FiberProvider`, and `RegularExtensionWitness` contracts. It executes the finite convolution of three Qhat factors with the source numerator P. Each query is at the demanded exponent minus the sum of factor exponents. It never enumerates a Laurent box. Full physical fibers cannot pass the artificial fiber and operation caps. Repeated physical source labels vanish only in this F pullback adapter; that rule is not applied to a general common-cover cochain or B.

Every contributing summand requires a witness for the **whole coefficient on the target standard intersection**, bound to the complete owned clearings and domain. A claim of regularity only on a common-cover open is rejected. A synthetic witness is an input premise, not an authenticated physical theorem. For direct finite fixtures, `SyntheticStandardCochain` checks every supplied Laurent monomial against the whole standard target's line-bundle regularity inequalities.

`StandardProgram(pi).coefficient(full_output_owners, exponent, derivative_direction=None)` performs R by restricting along the output standard tags in the global finite Laurent frame. Its trace records target/source standard tuples and coefficients. For a complementary derivative, the factor is `e[d]+1` and the requested input exponent is shifted **before** h's predicates run. Equal standard tags give zero by alternating pullback; equal physical labels alone do not.

`StandardEdgeOracle(program).bind(full_output_owners)` returns `coefficient(e)` and `support_box()` for `inserted_program.WholeNumerator`. The enclosure uses numerator degree bounds and finite Qhat support extrema; it requests no numerator values and may overestimate after cancellation. K, A, h, and S preserve exponents. This B adapter does not insert the output `C_a C_b Z`: `WholeNumerator` owns that padding.

## Mathematical limit

The identity is `delta B + B delta = 1 - A I P S` on the standard complex. There is one harmonic H2 coordinate in either pair character. A closed source need not satisfy `delta B = F`: the program explicitly retains `P S F`, and the nonzero harmonic control rejects the false universal claim. Actual source harmonic vanishing or a separately proved first-order primitive identity is still required.

Both pair twists `(-2,-2,0,0)` and `(0,0,-2,-2)` are implemented structurally. The complementary-pair theorem supplies a dependency for a future freshly evaluated F34 numerator. It does not authorize sorting the inverse-image raw F12 triple before nonlinear evaluation or identifying two differently ordered source cochains. No such source-order bridge is asserted here.

`proof.md`, `source-pins.json`, and `contract.json` give the conditional source bridge and exact scope. All physical execution and actual-source identity/extension/closure gates remain false. This package supplies a finite executable standard-B program and artificial controls, not a computed global obstruction.
