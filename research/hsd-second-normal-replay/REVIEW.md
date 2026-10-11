# Independent replay of the second-normal section equation

Pin: `22b800836385cf4c869c200bfc6715e07613aad6`.
Source of the first jet and the fifteen W primitives: `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`.
This review does not modify that branch, and it does not run the third-order computation.

## Result

The 405 exported second-section terms solve the right-hand side rebuilt below, exactly over Q. There are 15 monomials and 9 opens (3 finite, 3 infinity, 3 mixed), hence 135 equations. All 135 residuals are zero in G: each is an exact multiple of the relation, and the quotient is regular on that open.

Frozen right-hand side SHA-256, written before the 405-term file was opened:

`b9125f86d68b0eeb0fcca82dfad8c72a05aad0aed76ad6fd6411c59f324e02bf`

The opposite sign on the quadratic term, with every other convention held fixed, fails 42 of those 135 equations. The constant monomial on the finite overlap (0,1) is one witness: in the P slot, the monomial z^5 X^{-6} Y has relation-reconstruction -3/2 on the wrong residual and the wrong residual itself is -1/2.

## The equation that was rebuilt

The vector transition through order h^2 is

```
g̃_ij = (1 - h A_ηij + h^2 (½ A_ηij^2 - A_κij)) g_ij.
```

With v = E0 fixed by g, and with the first-order equation g ξ_j = ξ_i + A_ηij v, the h^2 coefficient is

```
g σ_j - σ_i = A_κij(v) + A_ηij(ξ_i) + ½ A_ηij^2(v).
```

On each base chart, g acts as the identity on the G-valued correction σ, so the left side is the Čech difference σ_j - σ_i. The mixed leg uses the same right-hand side in the finite frame, and the left side is T_B σ_∞ - σ_finite. Here T_B is the source matrix diag(z^3, 1, z^4, z^3) with the extra entry T_B[E0, E1] = z C. That is the matrix satisfying T_B r_∞ = z^3 r_finite. An extra factor z^{-1} (the sheaf formula T_U = z^{-1} T_B) leaves a nonzero mixed residual on D(W), where the infinity section is present. The equation checked here is the one written with T_B.

A_η(x) = {η, x} is the fiberwise bracket grad(η)^T Ω grad(x), with the source form

```
Ω(E0,E1) = F,  Ω(E0,E2) = g,  Ω(E1,E2) = W^6
```

on the finite chart and F, z^{-1} g, S^3 on the infinity chart. Diagonal Hamiltonian terms are differentiated as written, so a stored coefficient of E_i^2 contributes the factor two from ∂/∂E_i. The pairing with the completion coordinate is the displayed one, Ω(B, q) = (1, a0 λ), and λ(r_E) = 1 was recomputed on all six displayed covectors. The origin section is ξ = t0 q + s with t0 = z on the finite chart and t0 = 1 on the infinity chart. Parameter directions have no q term. The fifteen κ primitives are the coefficientwise W cochains; every other field of the certificate, including the order-three block, was dropped before any arithmetic.

The frozen object stores the three summands separately. Their sum is the right-hand side. The opposite-sign control replaces +½ A^2(v) by -½ A^2(v) and changes nothing else: same κ, same A(ξ), same j→i direction, same T_B.

## Uniqueness

For a fixed middle transition and a fixed β, two second-section solutions differ by a global section of G I^2. That group is zero, so the solution in G is unique. No further normalization is required.

The lines of B I^2, with I = O(0,-1), are

```
P I^2 = O(3,-5),  E0 I^2 = O(0,-2),  E1 I^2 = O(4,-6),  E2 I^2 = O(3,-6).
```

Each plane degree is negative, so H^0(B I^2) = 0. The relation line is A = O(3,-6), and A I^2 = O(3,-8). Künneth gives

```
H^1(O(3,-8)) = H^1(P^1, O(3)) ⊗ H^0(P^2, O(-8)) + H^0(P^1, O(3)) ⊗ H^1(P^2, O(-8)).
```

H^1(P^1, O(3)) = 0, H^0(P^2, O(-8)) = 0, and H^1(P^2, O(n)) = 0 for every n, so H^1(A I^2) = 0. The sequence 0 → A I^2 → B I^2 → G I^2 → 0 therefore has H^0(G I^2) = 0.

A B-valued representative is unique only modulo a multiple of r. The exported 405 terms are one such representative of the unique G-section. This review checks that representative against the equation. It does not rerun the ordered Čech homotopy that chose it.

## Two inputs re-derived from the source

These are not read off the second-normal checker.

1. Transport polynomial. With S = X^2 + Y^2, the binomial expansion is S^3 = X^6 + 3 X^4 Y^2 + 3 X^2 Y^4 + Y^6. The cross terms in g C cancel, leaving S^3 - z^3 W^6. The same identity is the E0 component of T_B r_∞ = z^3 r_finite, which was checked on all four frame slots.
2. One pinned contraction. The origin finite cochain on (0,1) has the term -2 z X^{-2} Y^{-1} E0 E1. Because Ω(E1, E0) = -XY,

```
{-2 z X^{-2} Y^{-1} E0 E1, E0} = 2 z X^{-1} E0.
```

The general bracket code reproduces that literal. The same source file's first-jet hash is `2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10`, and the certificate hash is `c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4`.

A separate 2×2 matrix calculation, truncated at h^3, checks that exp(hA) exp(hB) equals exp(h(A+B) + h^2/2 [A,B]) over Q, and that the opposite quadratic sign disagrees.

## What is still shared

The right-hand side still uses the frozen first-jet tensors, the fifteen W primitives, and the first-order section corrections. An error common to those inputs is not removed by rewriting the bracket. The two derivations above are the part that does not pass through the second-normal checker. The 405-term file and the check receipt were not inputs to the right-hand side.

## Scope

This is a check that those 405 terms satisfy the second-order section equation on the stated cover. It is not an ancestor identification, a carrier, a reflexive hull, or a defect. The order-three computation was not run.

## Reproduction

From the repository root, with only the Python standard library:

```
python3 research/hsd-second-normal-replay/build_rhs.py
python3 research/hsd-second-normal-replay/check_solutions.py
python3 -m unittest research.hsd-second-normal-replay.test_replay -v
```

`build_rhs.py` rewrites `frozen_rhs.json` and must be run before `check_solutions.py`. The same check was run under `python3 -O`.
