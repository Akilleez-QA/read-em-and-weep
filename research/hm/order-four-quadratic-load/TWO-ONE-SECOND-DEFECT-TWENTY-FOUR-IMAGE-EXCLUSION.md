# Two second-defect-24 branches fail a stabilizer-fiber quotient test

## New bounded reduction

For the profile (2,1) cases

- G3.21.d610e381ed75, source index 2: A=O(-8)+O(2)+O(16);
- G3.21.d41783aef00b, source index 10: A=O(-8)+Wprime O(9),

the second defect s=24 is impossible. Each published second-defect list sharpens from {0,12,20,24} to {0,12,20}.

Neither quotient case is excluded: their other branches remain necessary possibilities. This reduction does not decrease the frontier143 case count again.

## Published torsion possibilities and the local quotient

The profile (2,1) image sequence is

    0 -> J -> A(-2) -> T_def -> 0.

The published rank-eleven endpoint theorem, source indices 2 and 10, leaves exactly two s=24 torsion alternatives:

    O(6)|2D12,
    O(4)|D12 + O(6)|D12.

The first is cyclic and the second semisimple; they must not be conflated. At a point of the special orbit D12, the binary stabilizer is C10. Tensoring the surjection A(-2)->T_def with the residue field remains right exact. Therefore the stabilizer representation on the source fiber must surject onto the module top T_def/m T_def.

## Character conventions and the missing generator

Choose the stabilizer generator so that the fiber of O(1) has weight 1 modulo 10. The standard representation W has weights {1,-1}; Wprime has weights {3,-3}. The latter follows directly from its character at a primitive order-ten element: if phi=zeta+zeta^-1, then

    trace(Wprime) = 1-phi = phi^3-3phi = zeta^3+zeta^-3.

Its determinant is one because the binary icosahedral group is perfect. Trace and determinant determine the two eigenvalues. Reversing the generator negates every weight in the argument and does not change the obstruction.

For source index 2,

    A(-2) = O(-10)+O(0)+O(14),

so the source fiber weights are {0,0,4}. For source index 10,

    A(-2) = O(-10)+Wprime O(7),

whose weights are {0,7+3,7-3}={0,0,4} again.

For the cyclic module O(6)|2D12, its top has the single generator weight 6. Its socle has weight 6-12=4 modulo 10 because the conormal of D12 is O(-12)|D12. The socle weight 4 is not a substitute for the absent generator weight 6: quotient surjectivity is tested on the top.

For the semisimple module O(4)|D12+O(6)|D12, the top has weights {4,6}. It again requires weight 6.

Neither source fiber contains weight 6, so neither possible top can be its equivariant quotient. Hence neither torsion alternative can occur, and s=24 is excluded for both cases.

## Reproduction and limits

Run `python3 verify_two_one_second_defect_twenty_four_image_exclusion.py`.

The standalone verifier reconstructs exact characters over Q(sqrt(5)), verifies the restriction of Wprime, pins the published frontier144 and rank-eleven endpoint JSON, checks both stable IDs and the exhaustive two-alternative s=24 lists, and verifies the two source fibers and missing generator weight. It writes `two-one-second-defect-twenty-four-image-exclusion.json`.

No splitting enumeration or unpublished common-kernel datasets are needed. No actual coefficients, selected points, matrices, ranks, scans, spikes or consumed experiments are used. The stabilizer calculation is universal over the invariant orbit, not an actual-point evaluation. This is a necessary defect-branch exclusion only, with no realization, smoothing or SF claim.

## Immutable dependencies

- [Rank-eleven endpoint possibilities](https://github.com/Akilleez-QA/read-em-and-weep/blob/0b55b84466c62c24f05f7e691f3e7a3d528b7ebf/research/hm/order-four-quadratic-load/TWO-ONE-RANK-ELEVEN-ENDPOINT-SPLITTINGS.md).
- [Frozen 144-case index](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json). The checker pins the dependency bytes with SHA-256.
- [Separate one-case exclusion, PR689](https://github.com/Akilleez-QA/read-em-and-weep/pull/689), establishes the later count143. It is not a premise of the fiber argument.
