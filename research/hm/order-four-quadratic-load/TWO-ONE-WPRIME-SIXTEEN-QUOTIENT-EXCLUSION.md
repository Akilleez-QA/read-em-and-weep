# One impossible cohomology surjection reduces the frontier to 143

## Claim

The profile (2,1) quotient pair

    A = Wprime O(-5) + O(16),   B = O(-18) + Wprime O(3)

is impossible. Its unchanged stable ID is **G3.21.bf8462f3a0d7**, source pair index 11. Consequently the published 144-case necessary frontier reduces to **143**, with profile counts (122,10,11). This excludes one quotient case, not a whole profile. It does not assert realization of any retained case or resolve smoothing/SF.

## Published inputs, not a new splitting search

Use the established actual presentation

    0 -> E -> M3 O(-1) -> M4 O -> 0,
    M3 = 3Wprime + 3S + 6T,
    M4 = 2V + 4P + 3D.

These are the established actual source characters, also recorded in the published rank-eleven endpoint proof. In the profile (2,1) flag, write K=E^-, M=K^-, J=K/M. The exact sequences are

    0 -> K -> E -> A -> 0,
    0 -> M -> K -> J -> 0,
    0 -> J -> A(-2) -> T_def -> 0.

Here T_def is any torsion defect sheaf. No zero-defect restriction or endpoint splitting enumeration is required. For every twist r the last two sequences give surjections

    H1(K(r)) -> H1(J(r)) -> H1(A(r-2)) -> 0,

since H2(M(r))=0 on P1 and H1(T_def(r))=0 for torsion. Thus the composite is onto even for positive second defect. We never identify J with A(-2).

## The obstruction at twist -2

Because K embeds in E and E embeds in M3 O(-1),

    H0(K(-2)) = 0.

Additivity of Euler characters in the first exact sequence therefore gives

    H1(K(-2)) = chi(A(-2)) - chi(E(-2)).

The standard P1 cohomology formulas, with determinant-one W and self-dual irreducibles, give

    chi(A(-2)) = Sym^14 W - Wprime tensor Sym^5 W = V,
    chi(E(-2)) = M4 - M3 tensor W = -3A_std -4V -5P -6D.

Thus

    H1(K(-2)) = 3A_std +5V +5P +6D.                 (1)

On the other hand, A(-4)= Wprime O(-9)+O(12), so

    H1(A(-4)) = Wprime tensor Sym^7 W
               = one + A_std + V + P + D.          (2)

The composite surjection above would require

    H1(K(-2)) -> H1(A(-4)) -> 0,

for every possible torsion defect. Equivariant representations in characteristic zero are semisimple. The trivial multiplicity in (1) is zero; that in (2) is one. Such a surjection is impossible.

This proves the claim without choosing any K or M splitting, any source type E, or any coefficients or points. The contradiction is independent of B once the profile (2,1) interior flag is established.

## Reproduction and scope

Run `python3 verify_two_one_wprime_sixteen_quotient_exclusion.py`.

The small checker independently reconstructs the binary-icosahedral character ring in Q(sqrt(5)), verifies irreducible orthogonality, computes the four displayed characters, checks the exact stable ID using the pinned frontier hash, and writes only `two-one-wprime-sixteen-quotient-exclusion.json`. It neither imports nor executes old checkers and does not read the unpublished first-kernel coupling dataset. The JSON is a small character certificate, not an edited old frontier.

Only universal finite character arithmetic is used. There are no selected actual coefficients or points, actual matrices or rank tests, scans, spikes, or consumed experiments.

Published presentation and exact-sequence reference: [rank-eleven endpoint proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/0b55b84466c62c24f05f7e691f3e7a3d528b7ebf/research/hm/order-four-quadratic-load/TWO-ONE-RANK-ELEVEN-ENDPOINT-SPLITTINGS.md), and [frozen 144-label frontier](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json).
