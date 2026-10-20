# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Discriminant localization and pole removal: independent audit

## Verdict

The stated bounded-pole and connecting-homomorphism claims are correct. They exclude a discriminant-localization shortcut: restriction to the discriminant complement kills **every** degree-two class, including any nonzero class one is trying to detect.

The essential qualification is that the obstruction is the image of `[q]` in

`H¹(Q_n) / im(H¹(F(nD)) → H¹(Q_n))`,

not necessarily `[q]` itself in `H¹(Q_n)`. For `F₂` at pole bound two this distinction cannot be dropped using the stated regularity. At pole bound three, for either `F₁` or `F₂`, the denominator vanishes and the principal-parts class itself is canonically the original obstruction.

This is a formal audit of the supplied hypotheses. It does not establish whether any retained class vanishes and does not evaluate a source, polynomial, selected rank, or geometric instance.

## Hypotheses and pole bounds

Let `Y = P⁴_C`, let `Δ` be the nonzero degree-six discriminant, and let `D = V(Δ)`. Since `Y` is integral, `D` is an effective Cartier divisor and `O_Y(D) = O_Y(6)`. Smoothness of `D` is unnecessary. Let `B₀` be locally free and 11-regular, and put

- `F₁ = B₀(−4)`;
- `F₂ = B₀(−3)`.

Persistence of Castelnuovo–Mumford regularity gives `H²(B₀(t)) = 0` for `t ≥ 9` and `H¹(B₀(t)) = 0` for `t ≥ 10`. Consequently:

- `F₁(3D) = B₀(14)`: both `H¹` and `H²` vanish;
- `F₂(2D) = B₀(9)`: `H²` vanishes; the stated hypothesis does not imply `H¹ = 0`;
- `F₂(3D) = B₀(15)`: both vanish.

Thus three and two are the smallest nonnegative pole bounds, respectively, for which the displayed `H²` threshold alone guarantees vanishing. They need not be sharp for the actual bundle or actual cocycle.

Here “poles at most n” means membership in `F(nD) ⊂ F(*D)`, or denominator at most `Δⁿ` with the appropriate homogeneous twist. No smooth-divisor residue formalism is being assumed.

## Fixed-cover cochain statement

Choose a finite affine cover of `Y`. Its finite intersections are affine because `Y` is separated. The Čech complexes of the quasicoherent sheaves in question compute their sheaf cohomology. Use this same cover throughout, or pass all data to a common refinement.

For a regular Čech two-cocycle `c ∈ Z²(F)`, view `c` in `Z²(F(nD))`. If `H²(F(nD)) = 0`, there exists

`h ∈ C¹(F(nD))`, with `δh = c`.

This is an actual compatible meromorphic one-cochain, not a collection of unrelated local primitives. It proves the claimed bounds for `F₁, n=3` and `F₂, n=2`. It gives existence, not a formula or a computational method for finding `h`.

For any smaller bound `n`, the exact condition for a class to admit an `n`-pole primitive is membership in `ker(H²(F) → H²(F(nD)))`. Thus the result does not rule out a genuinely stronger source-specific small-pole argument. It rules out treating unrestricted localization, or the supplied universal bounds, as vanishing tests.

The complement `U = D₊(Δ)` is affine, hence `H²(U,F|_U)=0`. This gives the unrestricted localization statement independently. The explicit bounds come from the regularity vanishings; affineness by itself does not supply these particular numerical bounds.

## Exact obstruction and proof of pole removal

For `E_n = F(nD)` and `Q_n = E_n/F`, use the short exact sequence

`0 → F → E_n → Q_n → 0`.

On every affine intersection, the section map `E_n → Q_n` is surjective, since the next term is `H¹` of a quasicoherent sheaf on an affine. Therefore these sheaves also give a short exact sequence of the chosen Čech complexes.

Set `q = π(h)`. Then `δq = π(c) = 0`. With the usual connecting-map convention, the boundary of `[q]` is `[δh] = [c]`. The relevant exact sequence is

`H¹(F) → H¹(E_n) → H¹(Q_n) → H²(F) → H²(E_n)`.

In particular, existence of a regular primitive of `c` is equivalent to

`[q] ∈ im(H¹(E_n) → H¹(Q_n))`.

The equivalence holds for any available `h`; it does not require `H²(E_n)=0`. That vanishing is what guarantees an `h` for every `c` and makes the following quotient identification surjective onto all of `H²(F)`:

`H¹(Q_n) / im(H¹(E_n) → H¹(Q_n)) ≅ H²(F)`.

For the constructive implication, choose a closed meromorphic one-cochain `z ∈ Z¹(E_n)` whose image represents `[q]`. Then `q−π(z)=δr` for some `r ∈ C⁰(Q_n)`. Lift `r` to `a ∈ C⁰(E_n)` using the termwise surjectivity above. The cochain

`b = h − z − δa`

lies in `C¹(F)` and satisfies `δb=c`. Conversely, if such a regular `b` already exists, then `z=h−b` is closed and maps to `q`.

One wording correction is important: `δa` here is a **meromorphic Čech coboundary**. It need not itself be regular. Its subtraction, together with the closed meromorphic correction `z`, leaves a regular primitive. A statement requiring that the coboundary correction itself be regular is stronger than the proof supports and generally cannot remove principal parts.

If one permits only a meromorphic coboundary correction to the given `h`, with no closed meromorphic one-cochain correction, then the criterion is the stronger condition `[q]=0` in `H¹(Q_n)`. These two notions of removing poles coincide when `H¹(E_n)=0` but need not coincide otherwise.

## Dependence on choices and increasing the pole bound

Changing `h` while fixing `c` changes `h` by a closed `E_n` one-cochain, hence changes `[q]` by the image of `H¹(E_n)`. Changing `c` by a regular coboundary and changing `h` by the corresponding regular one-cochain leaves `q` unchanged. Thus the quotient class above is independent of these choices and is exactly the original class `[c]` under the canonical isomorphism.

For `F₁` and `n=3`, the boundary is an isomorphism

`H¹(Q₃) ≅ H²(F₁)`.

For `F₂` and `n=2`, the precise statement is

`H¹(Q₂) / im(H¹(B₀(9)) → H¹(Q₂)) ≅ H²(F₂)`.

At `n=3`, it improves to `H¹(Q₃) ≅ H²(F₂)`. More precisely, the natural map `H¹(Q₂) → H¹(Q₃)` for `F₂` is surjective, with kernel exactly `im(H¹(B₀(9)) → H¹(Q₂))`. This follows by naturality of the boundary maps, not by a choice of primitive. Increasing the pole bound from two to three removes the ambiguity from closed meromorphic cochains; it cannot remove a nonzero original obstruction.

For either bundle, all transition maps `H¹(Q_n) → H¹(Q_m)` with `m ≥ n ≥ 3` are isomorphisms, identified with the identity on `H²(F)` by the boundary maps.

The distinction at `F₂, n=2` is real under the hypotheses alone. As a universal illustration, take `B₀=Ω¹_{P⁴}(−9)`. The Euler sequence verifies 11-regularity, `H¹(B₀(9))=H¹(Ω¹)=C`, and `H¹(F₂)=H¹(Ω¹(−12))=0`. Thus `H¹(B₀(9))` injects nontrivially into `H¹(Q₂)`. A nonzero closed meromorphic one-cochain representing that group can be used as `h` for the zero cocycle `c=0`: its `[q]` is nonzero, although the regular primitive zero exists. This example evaluates no data of the bundle in the original problem; it only disproves replacing the quotient criterion by raw vanishing on the stated hypotheses.

## Principal-parts filtration

For `k ≥ 1`, there is an exact sequence

`0 → Q_{k−1} → Q_k → i_*(F(kD)|_D) → 0`,

where `Q₀=0` and `i:D↪Y`. Hence the asserted associated graded sheaf is correct. This follows from the Cartier-divisor sequence tensored with the vector bundle `F(kD)`.

This filtration need not split. Its cohomology includes connecting maps between successive layers. Vanishing or cancellation of an informal leading-pole expression, or a list of graded-piece dimensions, is not by itself a proof that the global quotient obstruction vanishes. Any layer-by-layer argument must keep the extension and Čech compatibility data.

The layer criterion stated in the accompanying `PROOF.md` is correct. If `h ∈ C¹(F(kD))` has regular differential, its top symbol `s ∈ C¹(F(kD)|_D)` is closed. A `(k−1)`-pole primitive can be obtained, allowing a closed `k`-pole one-cochain correction and a meromorphic coboundary correction, exactly when

`[s] ∈ im(H¹(F(kD)) → H¹(F(kD)|_D))`.

Indeed, apply the same cochain proof to `0 → F((k−1)D) → F(kD) → i_*(F(kD)|_D) → 0`. If no closed one-cochain correction is allowed, `[s]=0` is necessary and sufficient for lowering the pole bound by a meromorphic coboundary. The lower layers still require their own compatible reductions.

## Why localization and regular reconstruction do not finish the problem

The restriction map `H²(Y,F) → H²(U,F|_U)` has zero target. Thus restriction does not distinguish zero classes from nonzero classes. Equivalently, all such classes disappear after allowing sufficiently many powers of the discriminant in denominators. Multiplication by the relevant power of `Δ` into the shifted `H²` group is already zero at the stated bounds.

The prior regular-reconstruction audit, at `prerequisite regular-reconstruction-update, document AUDIT.md (see the unit INPUTS.md)`, establishes that the Frobenius coefficient evaluation and reconstruction maps are mutually inverse regular chain maps. Given compatible **regular** weighted primitives, assembly therefore creates no further obstruction, even on the discriminant. Applying that inverse to meromorphic weighted primitives only gives a meromorphic assembled primitive. If a compatible assembled primitive were regular, applying the regular coefficient-evaluation maps would give regular weighted primitives as well. Assembly cannot conceal an unresolved principal-parts obstruction.

The stronger filtration statement in `PROOF.md` also holds: tensor both inverse sheaf maps by `O(nD)`. They remain inverse, commute with the inclusions for successive pole orders, and therefore induce inverse maps on polar quotients and their cohomology. This is preservation of the **common** pole filtration, with all coordinate twists retained; it does not assert preservation of different independent numerical bounds on the separate coordinates. Since the constant component is assumed to have a compatible regular primitive, its polar component is zero. The two retained coordinate obstructions cannot cancel under reconstruction. At common bound three their polar-part groups have dimensions ten and twenty if one imports those previously established dimensions; this audit does not independently recompute them.

The source-comparison qualifications in `PROOF.md` are necessary and correct. A regular correction changes no polar part, but compatibility and regularity of that correction must have been established on the common complex. Merely knowing that a differential lies in an inclusion image does not put its primitive in that image. The reconstruction step does not erase that earlier requirement.

Accordingly, the remaining task is still to prove the relevant regular `H²` classes vanish, or prove one nonzero. The principal-parts reformulation may be useful for an actual calculation, but its exact obstruction is canonically the same original cohomology class. Neither the affine complement nor the regular reconstruction inverse supplies that missing calculation.

Source for the supplied reconstruction premise: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6279132359 . No source refresh or external write was performed for this audit.
