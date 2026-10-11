# Two replays of the second normal neighborhood

Pin: `22b800836385cf4c869c200bfc6715e07613aad6`.
Source of the first jet and the fifteen W primitives: `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`.
This review does not modify that branch. It does not run the third-order computation, and it does not open a new regularity job: the central plane relation and the cover are unchanged.

Scope A checks the section formula. Scope B checks the middle cocycle κ. A pass of A does not certify κ.

## Scope A — section formula

The 405 exported second-section terms solve the right-hand side rebuilt below, exactly over Q. There are 15 monomials and 9 opens (3 finite, 3 infinity, 3 mixed), hence 135 equations. All 135 residuals are zero in G: each is an exact multiple of the relation, and the quotient is regular on that open.

Frozen section right-hand side SHA-256, written before the 405-term file was opened:

`b9125f86d68b0eeb0fcca82dfad8c72a05aad0aed76ad6fd6411c59f324e02bf`

The opposite sign on the quadratic term, with every other convention held fixed, fails 42 of those 135 equations. The constant monomial on the finite overlap (0,1) is one witness: in the P slot, the monomial z^5 X^{-6} Y has relation-reconstruction -3/2 on the wrong residual and the wrong residual itself is -1/2.

### The equation that was rebuilt

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

### Kernel of this formula

κ enters only through A_κ(v) = {κ, E0}. Any Hamiltonian supported on the span of P and E0 has vanishing bracket with E0, because Ω(E0, E0) = Ω(P, E0) = 0. In particular

```
{X^{-1} Y^{-1} W^2 E0^2, E0} = 0.
```

Adding that monomial to the finite (0,1) origin primitive leaves the section right-hand side unchanged. Scope A cannot see it. The same monomial is the first must-fail control of scope B.

### Uniqueness

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

### Two inputs re-derived from the source

These are not read off the second-normal checker.

1. Transport polynomial. With S = X^2 + Y^2, the binomial expansion is S^3 = X^6 + 3 X^4 Y^2 + 3 X^2 Y^4 + Y^6. The cross terms in g C cancel, leaving S^3 - z^3 W^6. The same identity is the E0 component of T_B r_∞ = z^3 r_finite, which was checked on all four frame slots.
2. One pinned contraction. The origin finite cochain on (0,1) has the term -2 z X^{-2} Y^{-1} E0 E1. Because Ω(E1, E0) = -XY,

```
{-2 z X^{-2} Y^{-1} E0 E1, E0} = 2 z X^{-1} E0.
```

The general bracket code reproduces that literal. The same source file's first-jet hash is `2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10`, and the certificate hash is `c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4`.

A separate 2×2 matrix calculation, truncated at h^3, checks that exp(hA) exp(hB) equals exp(h(A+B) + h^2/2 [A,B]) over Q, and that the opposite quadratic sign disagrees.

## Scope B — middle cocycle

The quadratic BCH equations in Sym², checked modulo the relation, are

```
δκ_F = ½ {η_F on (0,1), η_F on (1,2)},
δκ_I = ½ {η_I on (0,1), η_I on (1,2)},
T κ_I − κ_F − δκ_H = ½ ({h, T η_I} − {η_F, h}).
```

The coboundary on the triple is (δc)_{012} = c_{12} − c_{02} + c_{01}, and on a pair it is (δc)_{ij} = c_j − c_i. The bracket is the same Poisson bracket as in scope A. T is z^{-4} Sym²(T_B): each infinity coordinate is replaced by its T_B image and the quadratic is multiplied by z^{-4}. A cross monomial u_i u_j is the sum of both orders; a square u_i² uses that direction once. h is the mixed first-jet cochain. The mixed equation is written in the finite frame.

The fifteen right-hand sides are rebuilt from the first jet alone, and their hash is frozen before the certificate is opened:

`4f07c4346fa1a2a4dae6bae4242060c57a08ee8b8b2392d6d674ff18abcfe112`

Each of the fifteen κ primitives is then compared with that frozen right-hand side. There are five equations per monomial (finite triple, infinity triple, three mixed pairs), hence 75 equations. All 75 differences are exact symmetric multiples of the relation, over Q.

Three conventions are pinned by hand, before those 75 equations are used as evidence:

1. {E0², E1²} = 4 XY E0 E1, from the two diagonal derivatives and Ω(E0, E1) = XY.
2. z^{-4} Sym²(T_B) sends E2² to z² E2², because T_B carries E2 by z³.
3. A cochain supported on the face (0,1) appears with sign +1 on the triple.

### Must-fail controls

Both mutations are added to the actual origin finite (0,1) primitive. The prediction uses only the Čech signs. An E2-free monomial reconstructs the zero partner vector, so the relation gate reports that signed monomial and nothing else. A mutation that passed would mean the gate had failed.

1. Add X^{-1} Y^{-1} W^2 E0². Its action on E0 is 0, which is why scope A is blind to it. The finite triangle mismatch is that monomial in the E0² slot. The mixed equation on (0,1) mismatches by the same monomial with sign −1, because that equation subtracts κ_F. Infinity and the other two mixed pairs stay exact.
2. Add X^{-1} E0 E1. Its action on E0 is −Y E0, so this term is outside the kernel of scope A. The finite triangle mismatch is that monomial in the E0 E1 slot, and the mixed (0,1) mismatch is the same monomial with sign −1. The other three equations stay exact.

## Independence record

Shared source inputs, both read from `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`:

| Input | SHA-256 | Scope A | Scope B |
| --- | --- | --- | --- |
| `first_jet.json` | `2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10` | η inside Aη(ξ) and ½ Aη²(v) | η inside the Poisson bracket of the BCH right-hand side |
| `certificate.json` | `c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4` | the fifteen W primitives, only through their action on v = E0 | the same primitives as the cochain under test; not an input of the right-hand side |

Shared derived geometry, recomputed in `common.py` from the displayed chart formulas: Ω, the relation r, and T_B.

Scope A alone also reads `FIRST_NORMAL_SECTION_CORRECTIONS.json` (the section ξ) and tests `SECOND_NORMAL_SECTION_CORRECTIONS.json` (the 405 terms). Scope B's right-hand side is frozen from the first jet before the certificate is opened, and scope B never reads either section file.

An error in the shared first jet is invisible to both replays. An error in a W primitive that lies in the kernel of {·, E0} is invisible to scope A and visible to scope B; the first mutation is that detector.

## Scope

Scope A is a check that the 405 terms satisfy the second-order section equation. Scope B is a check that the fifteen W primitives satisfy the quadratic BCH equations modulo the relation. Neither is an ancestor identification, a carrier, a reflexive hull, or a defect. The order-three computation was not run.

## Reproduction

From the repository root, with only the Python standard library:

```
python3 research/hsd-second-normal-replay/build_rhs.py
python3 research/hsd-second-normal-replay/check_solutions.py
python3 research/hsd-second-normal-replay/build_kappa_rhs.py
python3 research/hsd-second-normal-replay/check_kappa.py
python3 -m unittest research.hsd-second-normal-replay.test_replay -v
```

`build_rhs.py` rewrites `frozen_rhs.json` and must be run before `check_solutions.py`. `build_kappa_rhs.py` rewrites `frozen_kappa_rhs.json` and must be run before `check_kappa.py`. The same checks were run under `python3 -O`.
