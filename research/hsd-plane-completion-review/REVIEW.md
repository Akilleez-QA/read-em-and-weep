# Independent review of the bounded plane-completion lemma

Reviewed against commit `1db993943e07d615624edcf30bc2e169652453f5` of draft PR #66, directory `research/carrier/plane-completion-lemma`. Characteristic zero. Exact checks were recomputed in the fraction field of `Q[X,Y,W,z,u]` with SymPy 1.14.0. The checker is `check_plane_completion.py`; `test_check_plane_completion.py` contains 18 tests and passes.

This review establishes four things, and only these:

- The three pinned files are the bytes named by the published digests.
- For the displayed presymplectic rank-three bundle `G` on `P1 × P2`, a global algebraic rank-four `L`-valued symplectic completion `V` exists, with `P ⊂ G = P⊥`, `V/G ≅ D`, and the canonical `P–D` pairing. Any two such completions are uniquely isometric by an isometry that fixes `G` and that pairing.
- Given compatible algebraic torus linearizations of `G`, `P`, `L` and of the pairings, that completion inherits a unique compatible linearization. The compatibility hypotheses are unpacked below.
- No locally free rank-five bundle `Q` satisfies the retained-`B` contract stated in item 6. The obstructing step is the equality `ℓ·XY = X^3+Y^3` in `H^0(O(0,3))`. Two controls show which hypotheses that nonexistence uses.

This review does not identify an ancestor, an alpha frame, or a frozen first-normal jet. It does not export homogeneous transition matrices on a six-open cover. It does not construct a carrier, a reflexive hull, a defect, or a zero-defect member, and it does not identify the formal chart's supplied coefficient maps with the cohomology of this `V`.

## Verdicts

| Item | Verdict | Reason |
| --- | --- | --- |
| 1. Pinned digests | Pass | All three SHA-256 values and the two recorded byte lengths match `git show` of the pin. |
| 2. Hypothesis inventory | Pass | Every listed input is used exactly where the argument needs it. Torus linearizations are used only for conditional equivariance. |
| 3. Local completions and eleven identities | Pass | Both charts, all eleven numerators, the chart form entries, and the transition identity are the zero polynomial. Signs included. |
| 4. Gluing, band, vanishing, uniqueness | Pass | The band is `O(2,-4)`. Künneth gives `H^0 = H^1 = 0` and `H^2` of dimension 9 with the stated summand. Uniqueness uses `H^0 = 0`. |
| 5. Conditional equivariance | Pass | The linearization cocycle follows from the unique isometry once the compatibility hypotheses below are granted. |
| 6. Rank-five no-go | Pass | Steps through the splitting are valid. The failed step is the cubic membership. Dropping the radical hypothesis, or dropping global retention of `B`, stops the argument. A non-canonical scalar pairing does not. |
| 7. FMEA | Pass | Each listed failure mode has a direct certificate. None is present in the note. |

No mathematical error was found in the lemma or in the independent review shipped at the same pin. That shipped review was not used as a proof; the identities and the cohomology were recomputed here.

## 1. Pinned digests

| File | Bytes | SHA-256 |
| --- | --- | --- |
| `PLANE_COMPLETION_LEMMA.md` | 12807 | `fcb28b552115339c62c4e751caebf6876ca33885db061e267ddde028c6c0cde0` |
| `INDEPENDENT_REVIEW.md` | 5344 | `f1e7807f73437acb88615ef0412c15fc105c5cef4841f23f09d54e8f0c48ff4f` |
| `manifest.json` | 754 | `b4f8f4147c8fcec09789bf1e903c71171c6faa4b04fa2397a38ab57365bcdf93` |

The manifest records the first two digests and byte lengths and does not record its own digest. The prefixes `fcb28b55`, `f1e7807f`, and `b4f8f414` match the request.

The pin is an ancestor of branch tip `ec02aa73e875dddf092439655aad1233d5d884e5`. The three files above are byte-identical at that tip. Files added after the pin are outside this review.

## 2. Hypothesis inventory

`Y = P1 × P2`. Line bundles are written `O(base, plane)`.

| Input | Used | Where |
| --- | --- | --- |
| `G = B/A`, locally free of rank 3, with the descended `L`-valued form | Yes | §2 builds `G`. §5 completes this fixed `G`. |
| `P ⊂ G = P⊥` | Yes | §2 identifies the radical. §5 identifies automorphisms fixing `G` with translations by sections of `P`, and requires the isometry to fix this `G`. |
| `D ≅ V/G ≅ L P^{-1} = O(1,1)` | Yes | §3 uses it as the local complementary line. §5 uses it as the quotient and as the source of `M = Hom(D,P)`. §6 uses it as `Q/B`. |
| `L = O(4,-2)` | Yes | Value line of every form. Enters `D` and `M = P^2 L^{-1}`. |
| Canonical pairing `P ⊗ D → L` | Yes | §3 writes it as `p d' - d p'` and reads the normal sign off that term. §5 uses it so that the difference of two completions vanishes on `P`. §6 uses it to force `ψ(r_E) = a`. |
| Algebraic torus linearizations of `G`, `P`, `L` and of the pairings | Only conditionally | One paragraph of §5. Existence, uniqueness, and the rank-five nonexistence do not use them. |

The arguments also use the following displayed data. Each is an input of the lemma, and each is used.

| Input | Used | Where |
| --- | --- | --- |
| `A = O(3,-6)`, `B = P ⊕ E`, relation `r = (-a, r_E)` | Yes | §2 through §6. The sign `-a` is the one that makes `r_E = a P` in `G`. |
| `E0 ≅ O`, `E/E0 ≅ O(4,-4) ⊕ O(3,-4)`, triangular `E0 ← E1` gluing, no `E1–E2` off-diagonal | Yes | §6, for the filtration whose graded pieces have `H^1 = 0`, and for the splitting of `Hom(E/E0, P)`. `E0` is also the vector in the local normal lift of §3. |
| `S = X^2+Y^2`, `F = XY`, `a = X^3+Y^3`, `g = S-z W^2`, `C = S^2+z S W^2+z^2 W^4`, `T = -3S+2F` | Yes | §4 and §5. |
| Finite `r_E = (W^6, -g, F)`; infinity `r_E = (S^3, -u S+W^2, F)`, `u = z^{-1}` | Yes | §2 through §6. The infinity second component equals `-g/z` on `u z = 1`. |
| Skew matrix `Ω_E` with entries `(r3, -r2, r1)` in the pairs `(E0,E1)`, `(E0,E2)`, `(E1,E2)` | Yes | §2 through §4 and §6. On the finite chart this is `(F, g, W^6)`. At infinity it is `(F, z^{-1} g, S^3)`. |
| `T_B r_∞ = z^3 r_finite`, with off-diagonal `T_B[E0,E1] = z C` | Yes, as consistency of the two relation frames | Re-derived from `g C = S^3 - z^3 W^6`. The gluing of `V` does not use an explicit matrix of this transition. |
| Frame weights `d(P,E0,E1,E2) = (3,0,2,2)` on the finite chart and `(3,6,0,2)` at infinity, with `wt(z,X,Y,W) = (2,1,1,0)` | Only in the weight check of §3 | These weights force `d_D = 1` on the finite chart and `d_D = 5` at infinity. See item 3. |
| `t0` and the normal coordinate `h`, with target pairing `+t0 h` | Only in the local normal-lift sentence of §3 | Checked for sign and for the typing `t0 h ∈ O(1,1)`. Not an input to descent, uniqueness, equivariance, or the no-go. |
| The undefined phrase "full rank-five symplectic presentation" | No | §1 records that a rank-five bundle carries no nondegenerate alternating form, and that this fact does not interpret the phrase. §6 then proves nonexistence only for the contract written there. |

## 3. Local completions and the eleven identities

On `D(r_i)`, set `ψ_i(e) = a e_i / r_i`, so `ψ_i(r_E) = a`. The local form on `B ⊕ D` is

```text
Ω_i((p,e,d),(p',e',d')) = Ω_E(e,e') + p d' - d p' + ψ_i(e) d' - d ψ_i(e').
```

Pairing a vector against `P` forces its `D` coordinate to vanish. Rank two of `Ω_E` then forces its `E` component to be a multiple of `r_E`, and pairing against `D` forces the `P` component to be `-t a`. The radical is exactly the graph line `A`. The quotient by `A` is a nondegenerate rank-four bundle on that open. The same formulas with the opposite cross term `d p' - p d'` would give the normal sign `-t0 h`. The displayed sign gives `Ω(P, q(t0 h)) = +t0 h`. The representative `t0 = (z, 1)` is the standard section of `O_{P1}(1)`, and `h` is a local generator of `O(0,1)`, so `t0 h` is a local section of `D = O(1,1)`.

The cyclic `E`-valued cochain

```text
b12 = a e3 /(r1 r2),  b23 = a e1 /(r2 r3),  b31 = a e2 /(r3 r1),  bji = -bij
```

satisfies `Ω_E(-, b_ij) = ψ_j - ψ_i`. A direct expansion gives `b12 + b23 + b31 = a r_E /(r1 r2 r3)`. In `G`, the relation `(-a, r_E) = 0` says `r_E = a P`, so the triple sum is the central section `R123 = a^2/(r1 r2 r3)` of `P`. Because each transition fixes `G` pointwise, the composition adds these shifts. There is no further commutator.

The eleven identities, each reduced to a numerator in `Q[X,Y,W,z,u]` and found to be the zero polynomial, are:

1. Finite `Ω(e, b12) - (ψ2 - ψ1)(e)`.
2. Finite `Ω(e, b23) - (ψ3 - ψ2)(e)`.
3. Finite `Ω(e, b31) - (ψ1 - ψ3)(e)`.
4. The same three pairings after substituting the infinity relation. (Items 4–6.)
7. Finite vector sum `b12 + b23 + b31 - a r_E/(r1 r2 r3)`, all three components.
8. Infinity vector sum, all three components.
9. Finite cancellation `c12 + c23 + c31 + a^2/(r1 r2 r3)`, with `c12 = T F/(W^6 g)`, `c23 = z^3/(g F)`, `c31 = C/(W^6 F)`.
10. Infinity cancellation, with `c12 = -T F/(r1 r2)`, `c23 = -1/(r2 r3)`, `c31 = 0`.
11. `a^2 - g C - z^3 W^6 - T F^2`.

The finite product identity `r1 r2 r3 = -W^6 g F` converts item 11 into the displayed partial-fraction formula for `R123`. Further numerators that also vanish: `g C - (S^3 - z^3 W^6)`, `a^2 - S^3 - T F^2`, the equality of the infinity second component with `-g/z` after `u = 1/z`, and all four components of `T_B r_∞ - z^3 r_finite`.

The opposite pairing `Ω(e, b12) - (ψ1 - ψ2)(e)` is not zero, and the sign-reversed finite cochain does not cancel `R123`. The displayed signs are the ones that work.

Weights. With `wt(z,X,Y,W,u) = (2,1,1,0,-2)`, the finite coefficients `a/r_i` have weights `(3,1,1)` and the infinity coefficients have weights `(-3,3,1)`. The pinned frame weights of `E` are `(0,2,2)` and `(6,0,2)`. The unique `d_D` making the canonical `P–D` term match total weight 4, respectively 8, is `d_D = 1`, respectively `d_D = 5`. With those values every `ψ` term and every displayed `Ω_E` entry has the same total, 4 on the finite chart and 8 at infinity. This is a consistency check of the local form against the pinned frame. It is not a derivation of a global linearization.

The principal opens cover. The polynomial identities `X^3 = X S - Y F` and `Y^3 = Y S - X F` put `X^3` and `Y^3` in the ideal `(S, F)`. Over a field, a common zero of `S` and `F` has `X = Y = 0`. On the finite chart the remaining equation forces `W = 0`. At infinity, `S = 0` forces the second component to be `W^2`, including at `u = 0`. No point of `P2` is omitted.

## 4. Gluing

### Band

`D = L ⊗ P^{-1}` has bidegree `(4,-2) - (3,-3) = (1,1)`. Then

```text
Hom(D, P) = P ⊗ D^{-1} = (3,-3) - (1,1) = (2,-4),
P^2 ⊗ L^{-1} = (6,-6) - (4,-2) = (2,-4).
```

The two expressions agree. The band is `O(2,-4)`, as the note states.

An automorphism that fixes `G` pointwise and preserves the canonical pairing has the form `q ↦ q + c` with `c ∈ G`. The isometry identity forces `Ω_G(-, c) = 0`, hence `c ∈ P`. The band is exactly `Hom(D,P)`. No `D–D` condition appears: `D` has rank one and the form is alternating. The `P` component of each `b_ij` is free before the cocycle correction, which is the same calculation.

### Vanishing

Künneth for an external product of line bundles gives

```text
H^k(P1 × P2, O(2,-4)) = ⊕_{i+j=k} H^i(P1, O(2)) ⊗ H^j(P2, O(-4)).
```

`H^0(P1, O(2))` has dimension 3 and `H^1(P1, O(2)) = 0`. On `P2`, `H^0(O(-4)) = H^1(O(-4)) = 0` and `H^2(O(-4)) ≅ H^0(O(1))` has dimension 3. Therefore `H^0(Y, M) = H^1(Y, M) = 0`, and

```text
H^2(Y, M) = H^0(P1, O(2)) ⊗ H^2(P2, O(-4))
```

has dimension `3 × 3 = 9`. The other Künneth summands in degree 2 are zero, so the displayed equality is the whole group. The same computation gives `H^1 = 0` on each filtration line `O(2,-4)`, `O(-1,-1)`, `O(3,-5)`, and `O(2,-5)` used in item 6. These are the groups supplied by the cohomology of projective space (Stacks, Tag 01XT) together with the Künneth formula on the product.

On `Gm × P2` the base factor `O(2)` is trivial, so `M` restricts as `pr2* O_{P2}(-4)`. Pushforward to `Gm` has `π_* = 0` and `R^1 π_* = 0`, because both `H^0` and `H^1` of `O_{P2}(-4)` vanish. Thus `H^0 = H^1 = 0` on the overlap. The two base charts meet in a single overlap, so the only cocycle condition is that the reverse gluing map is the inverse.

### Uniqueness uses `H^0 = 0`

`H^1(M) = 0` makes an `M`-torsor trivial, so at least one isometry exists. Two such isometries differ by a global section of `M`. That section is zero if and only if `H^0(M) = 0`, and then the isometry is unique. If the band had a positive-dimensional space of global sections, the same vanishing of `H^1` would still produce isometries, and they would form a torsor under that space. The sentence "unique up to a unique isometry fixing `G` and the pairing" depends on `H^0 = 0`. Both vanishings hold for this `M`, on `Y` and on `Gm × P2`.

### The `H^2` complement

Local completions and chosen isometries on double overlaps determine a class in `H^2(Y, M)`. Section 4 of the lemma produces a completion over `A^1_z × P2`, so this class restricts to zero on that open. The same holds over the infinity chart.

Restriction on the one nonzero Künneth summand is restriction of sections `H^0(P1, O(2)) → H^0(A^1)`, tensored with the identity on a 3-dimensional space. In the finite frame those sections are the polynomials of degree at most 2, and restriction to `A^1` is injective. The global class is therefore zero.

`H^2(A^1 × P2, M) ≅ k[z] ⊗ k^3` is not the zero group. The explicit cochain `c_ij` is what kills the class on each base chart. Each nonzero correction has plane degree `-4`. On its named overlap it evaluates to a rational number at a `Q`-point, including the infinity corrections at `u = 0` (values `1/2` and `-1` at `X = Y = W = 1`). Placing a correction on either of the other overlaps leaves a denominator factor coprime to the two inverted components, or a pole with nonzero numerator. The overlap assignment is part of the certificate.

The two-chart gluing and the `H^2` argument are separate existence proofs. Both close.

## 5. Conditional equivariance

Let `T` be the torus, `a: T × Y → Y` the action, and `p` the projection. A linearization of the completion is an isometry `a* V ≅ p* V` covering the given linearization of `G` and satisfying the cocycle on `T × T × Y`.

Transport the action pullback by the linearization of `G`. The result and the projection pullback are two completions of the same linearized `G`, with the same canonical pairing. Their isometries form a torsor under `p* M`. Since `T` is affine,

```text
H^i(T × Y, p* M) ≅ Γ(T, O_T) ⊗ H^i(Y, M).
```

Both groups on `Y` vanish, so both groups on `T × Y` vanish. There is a unique isometry. On `T × T × Y` the multiply-then-act composite and the act-then-act composite are isometries between the same two completions, so uniqueness forces them to agree. That is the cocycle.

This uses uniqueness, hence `H^0 = 0`, and existence of the isometry, hence `H^1 = 0`. It also uses the following compatibility, which the note summarizes as "compatible linearizations on `G`, `P`, `L` and their pairings" and which is required in full:

- The linearization of `G` preserves `P` and agrees on the inclusion with the given linearization of `P`.
- The form `G × G → L` is equivariant for the linearizations of `G` and of `L`.
- The canonical pairing identifies `D` with `Hom(P, L)`, and that identification is equivariant. The note does not list a separate linearization of `D`. The linearization of `D` that enters the quotient `V/G` is the one induced by `P` and `L`. A second, disagreeing linearization of the quotient would place the two pullbacks in different `D`-frames, and uniqueness would not apply to that pair.
- `T` is affine. A torus is affine. The same base-change vanishing is not claimed for a non-affine group.

Under those hypotheses the linearization statement follows. The argument does not produce the input linearizations.

## 6. Rank-five no-go

### The contract, restated

There is no locally free rank-five bundle `Q` on `Y` such that all of the following hold at once:

- `B ⊂ Q` is the given subbundle;
- `Q/B ≅ D = L P^{-1}`;
- `Ω_Q` is an `L`-valued alternating form restricting to the given `Ω_B`;
- the radical of `Ω_Q` is exactly the given line `A ⊂ B`;
- the induced pairing `P ⊗ (Q/B) → L` is the canonical isomorphism.

### Where it stops

`Ext^1(D, B) = H^1(Hom(D, B)) = H^1(B ⊗ P ⊗ L^{-1})`, because `D^{-1} = P ⊗ L^{-1}` and local `Ext` vanishes for locally free sheaves. The graded pieces of the filtration are

```text
P ⊗ P ⊗ L^{-1}  = O(2,-4),
E0 ⊗ P ⊗ L^{-1} = O(-1,-1),
E1 ⊗ P ⊗ L^{-1} = O(3,-5),
E2 ⊗ P ⊗ L^{-1} = O(2,-5).
```

Each has `H^1 = 0`. For a short exact sequence, `H^1` of the middle term vanishes whenever `H^1` of both ends vanishes, whether or not the extension splits. The triangular `E0 ← E1` gluing is covered by that long exact sequence. Every extension `0 → B → Q → D → 0` therefore splits.

A splitting and the form determine `ψ ∈ Hom(E, P)`. The canonical pairing contributes `-a` when the relation is paired with `D`, so the radical condition is `ψ(r_E) = a`.

`Hom(E0, P) = H^0(O(3,-3)) = 0`, so `ψ` vanishes on `E0` and factors through the split quotient `O(4,-4) ⊕ O(3,-4)`. Then `Hom(O(4,-4), P) = H^0(O(-1,1)) = 0` and `Hom(O(3,-4), P) = H^0(O(0,1))` has dimension 3. Thus `ψ = (0, 0, ℓ)` with `ℓ` linear in `X, Y, W`, and `ψ(r_E) = ℓ · XY`.

The step that fails is the equality `ℓ · XY = X^3 + Y^3` inside `H^0(O(0,3))`. That space has dimension 10. Multiplication by `H^0(O(0,1))` on `XY` has image of dimension 3, and every element of the image has coefficient 0 on `X^3` and on `Y^3`. The class of `a` has coefficient 1 on both, so the augmented rank is 4. Everything before this membership is valid. This membership is false.

### Controls

Drop the hypothesis that the radical equals the given line `A`, and keep the rest of the contract, including the canonical pairing and `B ⊂ Q`. On the split bundle `Q = B ⊕ D`, the form with `ψ = 0` extends `Ω_B`. Its radical is exactly `span(0, r_E)`. That line is a subbundle because `r_E` is nowhere zero, and it is not `A` because `a ≠ 0`. Here `ψ(r_E) = 0`, so the cubic comparison is never reached, and the rank-five form exists. Nonexistence does not apply to "a rank-five alternating extension of `Ω_B` that retains `B`".

Drop global retention of `B`. On each open `D(r_i)` the local form with `ψ_i` has radical exactly the graph of `A`: the nullspace is one-dimensional and contains the graph vector, and it does not contain the vertical vector. These are rank-five presentations of the local contract. The coefficient `a/r_i` is not a global section of `Hom(E, P)`, so the global membership argument does not see them. Nonexistence is not a local statement, and it does not touch the rank-four quotient completion.

Replace the canonical pairing by an arbitrary global pairing `P ⊗ D → L`. That group is `H^0(O) = k`, so the pairing is `λ` times the canonical one. If `λ ≠ 0`, the radical condition becomes `ψ(r_E) = λ a`, and `λ(X^3+Y^3)` is still outside the image because its `X^3` coefficient is `λ`. If `λ = 0`, the `P`-row of the form is identically zero, so the whole line `P` lies in the radical. The vectors `(1,0,0,0,0)` and `(-a, r_E, 0)` are linearly independent, so `P ≠ A` and the radical cannot equal `A`. This weakening does not produce an example. It is not a witness that the no-go has been over-read. The witnesses are the two drops above.

## 7. FMEA

| Failure mode | Detection | Status |
| --- | --- | --- |
| Sign convention on `Ω` or on the Čech correction | Chart entries equal `(F, g, W^6)` and `(F, z^{-1} g, S^3)`. The opposite pairing `ψ1 - ψ2` is nonzero. The sign-reversed finite cochain does not cancel `R123`. The normal term `p d'` gives `+t0 h`. | Absent. Pass. |
| Twist off by one | `Hom(D,P)` and `P^2 L^{-1}` both recompute as `O(2,-4)`. Every nonzero correction has plane degree `-4`. The frame weights force `d_D = 1` and `d_D = 5`, and both `ψ` totals and the displayed form totals then equal 4 and 8. | Absent. Pass. |
| Chart-overlap transition miscoded | Each `c_ij` is finite at a `Q`-point of its own overlap, including infinity at `u = 0`. Each swapped placement retains a denominator factor coprime to the two components inverted on that overlap, or a pole with nonzero numerator. | Absent. Pass. |
| Torsor band misidentified | The automorphism calculation gives exactly `Hom(D,P)`, and both bundle formulas give `O(2,-4)`. | Absent. Pass. |
| Quotient completion confused with the rank-five presentation | Control with `ψ = 0` is a global rank-five form whose radical is not `A`. Local `ψ_i` have radical `A` and do not globalize. The rank-four quotient exists by the gluing argument. The note states both and separates them. | Absent. Pass. |

## Boundary

The proved geometric statement is the rank-four completion of this fixed `G`, its uniqueness for that `G` and the canonical pairing, the conditional linearization under the hypotheses of item 5, and nonexistence for the rank-five contract of item 6.

The next constructive object named by the lemma, an explicit global homogeneous cocycle for `V` together with an identification of a prescribed frame and a prescribed first-normal jet, is outside this review. So is every ancestor, carrier, hull, and defect statement.

## Checks

From this directory, with SymPy 1.14.0:

```sh
python3 -m unittest test_check_plane_completion.py -v
```

The projective-space input is Stacks, Tag 01XT. The Künneth decomposition used above is the standard one for an external product of line bundles on a product of projective spaces. The Čech class and the band are computed from the displayed form, not taken from the general gerbe formalism.
