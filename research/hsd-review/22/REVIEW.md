# High School Diploma — review of PR #22

Pinned head: `9be62063a9b922f9d31042403dd70bf57f9f40e3` (the head of #22 at review time; one commit, `research/carriers/rank-two-ext-bound.md`).

Result: **agreement**. Line-by-line reading produced no gap. Every numerical input was recomputed by `research/hsd-review/22/check-exact.js`, a dependency-free Node script using `BigInt` rationals and an 8-generator exterior algebra. It does not read or run any other file in the repository. `node research/hsd-review/22/check-exact.js` exits 0.

The input `ext¹=87` is the note's HM plug-in. The checker confirms the arithmetic consequence `7372` and does not rederive that rank. The note already says the same.

## Line-by-line

### Proposition (lines 3–10)

Hypotheses used later are exactly these: complex abelian fourfold, simple rank two, `c₁=0` in rational cohomology, `∫ c₂²>0`. The three conclusions are `χ` positive even, `ext¹≥8`, and

```text
ext² = 16χ − 2 + 2 ext¹ ≥ 46.
```

The dimension exclusion (full semiregularity, and surjectivity of `ev: HH² → Ext²`) is the comparison with two 28-dimensional spaces, proved below. The note does not claim nonexistence, an ambient class, or failure of the weak image criterion in Markman Question 11.4. That scope matches Lemma 11.3, whose semiregularity criterion needs both `ker(ev)=annihilator of ch` and surjectivity of `ev`. Ruling out surjectivity and ruling out injectivity of `σ` leaves the image-restricted question open. No gap.

### Parity (lines 12–22)

`H^*(X,ℤ)≅∧^* H¹(X,ℤ)` is torsion-free, so rational vanishing of `c₁` upgrades to integral vanishing, and `det E ∈ Pic⁰`. Over `ℂ`, `[2]: Pic⁰→Pic⁰` is surjective, so `L` with `L²≅(det E)^{-1}` exists. Then `det(E⊗L)≅O` and `ch(E⊗L)=ch(E)`.

The wedge pairing `F⊗F→O` is fiberwise perfect and alternating. Cup product of two degree-2 classes swaps with sign `(−1)^{2·2}=+1`; the coefficient swap contributes the wedge sign `−1`. The induced pairing on `H²(X,F)` is alternating. Serre duality, using `F≅F^*` and `ω_X≅O`, makes it perfect. A perfect alternating form on a finite-dimensional `ℂ`-vector space forces even dimension: a skew-symmetric matrix `A` satisfies `det A = (−1)^n det A`, so `n` odd implies `det A=0` in characteristic not 2. The checker confirms `det=0` on a concrete `3×3` skew matrix and `det=1` on the standard `2×2` symplectic block. Thus `h²(F)` is even. Self-duality gives `h⁴=h⁰` and `h³=h¹`, so

```text
χ(F) = 2h⁰ − 2h¹ + h²
```

is even, and `χ(E)=χ(F)`.

Chern character, two derivations, both exact:

- Newton–Girard with `c₁=c₃=c₄=0`: `p₂=−2c₂`, `p₄=2c₂²`, so `ch₂=p₂/2=−c₂` and `ch₄=p₄/24=c₂²/12`.
- Splitting principle, roots `r,−r` with `r²=−c₂`: `ch=2cosh` series gives the same `2 − c₂ + c₂²/12`.

`T_X` is trivial, so every Chern root of `T_X` is 0 and `Td(X)=1`. Riemann–Roch is the codimension-4 component: `χ=∫ c₂²/12`. The hypothesis makes this positive. A positive even integer is at least 2. No gap.

### Eight directions (lines 24–29)

Scalar inclusion `H¹(O)→Ext¹(E,E)`, `λ↦λ·id`. Trace of that class is `2λ`. Over `ℂ`, multiplication by 2 is injective, so these are 4 independent classes. Dimension `h¹(O_X)=4` is `C(4,1)`.

Translations `v↦v⌟At(E)` for `v∈H⁰(T_X)≅ℂ⁴`. The sentence "suppose the image is zero" is the kernel of one vector, and the rest of the paragraph proves that kernel is zero:

- Trace powers of the Atiyah class recover Chern classes. If `v⌟At(E)=0`, then `v⌟tr(At^k)=k tr((v⌟At)At^{k−1})=0`, so `v⌟ch_k=0`. With `c₁=0`, `ch₂=−c₂`, hence `v⌟c₂=0`.
- Leibniz on an even-degree class: `v⌟(c₂∧c₂)=2(v⌟c₂)∧c₂`. The checker tests this on a degree-4 class whose square is a nonzero volume monomial, and tests the vanishing implication on a class killed by `∂/∂z₀`.
- `∫c₂²>0` means `c₂²` is a nonzero multiple of the translation-invariant volume form. Contraction `ℂ⁴→H^{3,4}` on that line is injective: the four forms `∂/∂z_k ⌟ vol` are distinct basis 7-forms. The checker records rank 4.

Trace of a translation is `v⌟c₁=0`, while Picard traces fill `H¹(O)`. The two 4-planes meet only at 0, so `ext¹≥8`. No gap.

### Euler characteristic of End (lines 31–41)

`E^*` has the same Chern character because `c₁=0` (equivalently `E^*≅E⊗(det E)^{-1}` and `det E∈Pic⁰`). Then `ch(End E)=ch(E)²`. Exact product, truncated at codimension 4:

```text
(2 − c₂ + c₂²/12)² = 4 − 4c₂ + (4/3)c₂²
```

(the `u³` and `u⁴` terms are `−1/6` and `1/144` and vanish on a fourfold). The same polynomial comes from eigenvalues `0,0,2r,−2r`. Therefore

```text
χ(End E) = ∫ (4/3) c₂² = (4/3)·12·χ(E) = 16χ(E).
```

Simplicity gives `ext⁰=1`. Serre duality on the abelian fourfold gives `ext⁴=ext⁰` and `ext³=ext¹`. Hence

```text
16χ = ext² − 2 ext¹ + 2,
ext² = 16χ − 2 + 2 ext¹.
```

The corner `χ≥2`, `ext¹≥8` is `32−2+16=46`, because both coefficients are positive. The Picard-only predecessor `ext¹≥4` gives `38`, as the note says. No gap.

Comparison spaces, from `dim H^{p,q}=C(4,p)C(4,q)`:

| summand | dimension |
|---|---|
| `H^{0,2}` | 6 |
| `H^{1,3}` | 16 |
| `H^{2,4}` | 6 |
| total | 28 |

HKR for `HH²` is `C(4,0)C(4,2)+C(4,1)C(4,1)+C(4,2)C(4,0)=6+16+6=28`. Since `ext²≥46>28`, `σ` cannot be injective and `ev` cannot be surjective. No gap.

### Principal polarization (lines 43–50)

Symplectic basis `θ=Σ_{i=0}^{3} x_i∧y_i`. Exterior multiplication gives the identity

```text
θ²/2 = Σ_{i<j} (x_i∧y_i)∧(x_j∧y_j)
```

with six terms, each carrying coefficient `+1` in front of that wedge. In the ordered basis `x₀<⋯<x₃<y₀<⋯<y₃` each coordinate is `−1` (one swap of `y_i` past `x_j`). Absolute values are 1 and the gcd is 1, so the class is primitive either way. The note's "coefficient 1" is the unsorted expression; it is not a gap.

Thus `c₂=d θ²=k(θ²/2)` with `k=2d`. An integral class equal to a rational multiple of a primitive class forces that multiple to be an integer, so `k∈ℤ`. The checker rejects lowest-terms multipliers with denominator `>1` and accepts integers.

`θ⁴=24 Ω` with `Ω=α₀∧α₁∧α₂∧α₃`, by direct multiplication (3 pair-partitions, 2 orders, and the factor `4` from `(θ²)²=(2S)²`). Hence `χ=∫(d θ²)²/12=24d²/12=2d²=k²/2`. Integrality of `k²/2` forces `k` even: an odd integer has odd square. So `d=k/2` is an integer. Checked for every integer `k` with `|k|≤31`, and by the square mod 2.

Then `16χ=32d²` and

```text
ext² = 32d² − 2 + 2 ext¹ ≥ 32d² + 14.
```

Plugging the stated HM pair `(d,ext¹)=(15,87)`:

```text
32·225 − 2 + 2·87 = 7200 − 2 + 174 = 7372.
```

The same value is `16·450 − 2 + 174`. For `d=8`, `32·64+14=2062`, and `χ=2·64=128`, `χ(End)=16·128=2048`. No gap.

### Honest descent (lines 52–57)

An isogeny `q:X→Y` of degree `g` is finite flat and surjective, so `q^*` is injective on `Hom` and on rational cohomology. Simplicity of `E=q^*G` forces simplicity of `G`, and `c₁(E)=0` forces `c₁(G)=0`. For a top class, `∫_X q^*α = g ∫_Y α`, so `∫_Y c₂(G)²>0`. The proposition applies to `G` on any abelian fourfold, with no polarization hypothesis.

`χ(E)=g χ(G)` with `χ(G)` a positive even integer, say `2t`, `t≥1`. Then `χ(E)/2 = g t`, so `g` divides `χ(E)/2`.

From `d=15`, `χ=450` and `450/2=225`. From `d=8`, `χ=128` and `128/2=64`. Positive divisors:

- `225`: `1,3,5,9,15,25,45,75,225`
- `64`: `1,2,4,8,16,32,64`

`7` does not divide `225` and `3` does not divide `64`, so the restrictions are proper. The note does not claim that any such `g` occurs. Twisted descent, higher rank, and complexes are excluded in the same paragraph. No gap.

### Sources (lines 59–66)

The citations are foundations (Riemann–Roch, Serre duality, the cohomology and polarization facts for abelian varieties) plus Markman's separation of full semiregularity from the weak image condition, plus the translation sharpening. The `38→46` comparison is the Picard-only corner versus the Picard-plus-translation corner. No extra numerical claim is hiding there.

## Recomputed values

| quantity | value |
|---|---|
| `ch(E)` | `2 − c₂ + c₂²/12` |
| `ch(End E)` | `4 − 4c₂ + (4/3)c₂²` |
| `χ(End E)` | `16 χ(E)` |
| corner `ext²` | `46` |
| Picard-only corner | `38` |
| semiregularity and `HH²` | `28` |
| `∫θ⁴` | `24` |
| `θ²/2` | 6 monomials, gcd 1 |
| `d=15`, `ext¹=87` | `χ=450`, `ext²=7372`, `g\|225` |
| `d=8` | `χ=128`, `ext²≥2062`, `g\|64`, `χ(End)=2048` |
| volume contraction | rank 4 |

## Not a gap

Sorted coordinates of `θ²/2` are `−1`, not `+1`. The identity asserted in the note is the unsorted sum, whose coefficients are `+1`, and primitivity uses only the gcd. The integrality of `d` is unchanged.
