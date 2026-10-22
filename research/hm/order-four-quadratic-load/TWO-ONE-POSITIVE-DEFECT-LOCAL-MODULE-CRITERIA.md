# Exact local module tests sharpen the positive second-defect alternatives

## New result and precise scope

Across the surviving profile (2,1) cases, the published rank-eleven endpoint output has 34 positive-second-defect torsion alternatives. The two previously proved s=24 branch exclusions remove four alternatives. The complete local module quotient test below removes **eleven further alternatives**, leaving **19 locally possible alternatives**.

This adds no whole-defect or quotient-case exclusion: every remaining positive defect degree still has an alternative. In particular the frontier143 count is unchanged. The new content is the complete local necessity-and-sufficiency criterion, the forced kernel fibers, and pruning invisible to Euler-character tests.

## General local criterion, including socles and kernels

Let C=A(-2), and consider the required quotient C->T_def with kernel J. At a special orbit D_d, the binary stabilizer has order m, where

    (d,m) = (12,10), (20,6), or (30,4).

Fix O(1) fiber weight 1 modulo m. Work in the completed local DVR R. The uniformizer has weight -d because the conormal is O(-d)|D_d. Equivariant averaging and Nakayama give an eigenbasis for the free source module C, whose generator weights are exactly its fiber weights.

A cyclic summand O(k)|ell D_d is locally R/(z^ell) with generator weight k. Its successive radical layers have weights

    k, k-d, ..., k-(ell-1)d.

Only the first layer belongs to its top T_def/z T_def; the last is its socle. A direct sum of cyclic modules therefore requires one source-fiber generator of each top weight k, with multiplicities. This top-multiplicity containment is necessary by right exactness after tensoring with R/(z).

It is also sufficient for an equivariant surjection of completed local modules: select distinct matching source eigen-generators and map each to the corresponding cyclic generator, sending remaining generators to zero. The map respects weights and R multiplication and is onto. This is local sufficiency only; it supplies neither a global bundle morphism nor the actual Gauss derivative.

The kernel fiber is forced as well. For each selected source generator k supplying a cyclic summand of length ell, replace its weight k by

    k-ell d modulo m.

Unselected generator weights remain unchanged. This follows either from the explicit kernel generator z^ell e or from the equivariant Tor1 exact sequence. The subtraction is by ell d, not the socle shift (ell-1)d. At an orbit outside the torsion support, the kernel fiber equals the source fiber.

## Application to all published alternatives

The source restrictions used are

    W: {1,-1} at every stabilizer;
    Wprime: {3,-3} at C10, {1,-1} at C6 and C4;
    one: {0}.

They follow from the exact character values and determinant one. The verifier independently reconstructs the character ring and checks those trace values, then shifts by each degree in A(-2). Repeated tops consume repeated source weights; merely finding a nonzero Hom for each summand separately is insufficient.

The eleven newly excluded alternatives, in the published source-index notation, are:

- Index 2: s=12 with O(2)|D12 or O(6)|D12.
- Index 5: s=12 with O(6)|D12.
- Index 9: s=12 with O(2)|D12 or O(6)|D12; s=24 with cyclic O(6)|2D12 or semisimple pairs {2,4}, {2,6}, {4,6} on D12.
- Index 10: s=12 with O(2)|D12 or O(6)|D12.

Exact stable IDs and original alternative IDs are preserved in the output; the four previously excluded index-2/index-10 s=24 alternatives are separately marked and not counted again.

## A distinction Euler characters cannot make

For index 9, A=O(-8)+O(6)+O(16), the C10 source fiber is {0,4,4}. Of its six formerly allowed s=24 torsion alternatives, only

    cyclic O(4)|2D12,
    semisimple 2 O(4)|D12

are locally possible. Their forced C10 kernel fibers are respectively {0,0,4} and {0,2,2}.

The excluded semisimple O(2)|D12+O(4)|D12 has the same all-twist Euler characters as cyclic O(4)|2D12, by the cyclic conormal filtration. Nevertheless its top requires absent weight 2. Thus the new local test genuinely distinguishes torsion module structures that no Euler-character test can separate.

The s=32 disjoint-support alternative is checked separately at D12 and D20. No generator from one orbit can supply a top weight at the other.

## Reproduction and boundaries

Run `python3 verify_two_one_positive_defect_local_module_criteria.py`.

Inputs are the pinned published frontier144, rank-eleven endpoint output, and the already published two-case s=24 certificate. The checker writes `two-one-positive-defect-local-module-criteria.json`, including all 34 alternatives, the three local source/top comparisons, forced kernel fibers for locally possible alternatives, and the precise new/previous counts. No old files are changed.

These are abstract stabilizer characters and local module identities. There are no selected actual coefficients or points, actual matrices or rank tests, scans, spikes, or consumed experiments. No global realization, additional whole-case exclusion, smoothing, or SF conclusion is asserted.

## Immutable input references

- [Rank-eleven endpoint classification](https://github.com/Akilleez-QA/read-em-and-weep/blob/0b55b84466c62c24f05f7e691f3e7a3d528b7ebf/research/hm/order-four-quadratic-load/TWO-ONE-RANK-ELEVEN-ENDPOINT-SPLITTINGS.md).
- [Prior four-alternative exclusion, PR693](https://github.com/Akilleez-QA/read-em-and-weep/blob/dc2103075cd6b0852fcff8ee0349659cff1695e6/research/hm/order-four-quadratic-load/TWO-ONE-SECOND-DEFECT-TWENTY-FOUR-IMAGE-EXCLUSION.md).

The accompanying verifier pins its input bytes. This result is stacked on PR693 and does not modify those inputs.
