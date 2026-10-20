# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: restricted monad and conductor cohomology bounds

## Verdict

The proposed structural bound is correct. For the normalized Horrocks–Mumford bundle `F` and `B=End₀(F)`, write the restriction to the quadruple-root rational normal quartic as

    F|C ≅ O(a) ⊕ O(-4-a),          -2 ≤ a ≤ 8.

For every integer `t≥1`, the conductor quotient is

    Q_t = B|C(4t-2),
    h¹(C,Q_t) = max(2a+5-4t,0) ≤ max(21-4t,0).

Consequently normalization induces a surjection on second cohomology at every twist, with kernel of dimension at most 5 at `t=4`, at most 1 at `t=5`, and zero at every `t≥6`. Thus it is an isomorphism for `t≥6`.

These are bounds for the positive-twist normalization comparison. They do not bound the fourth-power image in the ambient ten-dimensional group: that comparison is at twist `-4`, where the conductor group has dimension at least 51.

The interval for `a` and the corresponding bound for `h¹(Q₄)` are sharp for the exact restricted-monad package alone, even if its natural symplectic self-duality is imposed. This does not assert that the extremal splitting occurs for the actual HM bundle on this particular quartic, or that the normalization kernel attains the upper bound.

## Inputs checked

Read and checked the local proofs in:

- `../nullcone-normalization/PROOF.md`: normalization, conductor, quotient line, and complete cohomology sequence.
- `../effective-collision-bound/PROOF.md`: normalized HM monad and bundle exactness, with determinant `det F=O_P4(-1)`.
- `../fourth-power-cohomology/PROOF.md`: the exact fourth-power image and the positive-twist Koszul boundary.

The audit introduces no new source-specific matrix or cohomology-rank input.

## 1. Restriction of the Euler sequence

Let `i:C≅P¹→P⁴` be the rational normal quartic. Then `i*O_P4(1)=O_P1(4)`. Restricting the Euler sequence gives

    0 → i*Ω¹_P4(1) → 5O → O(4) → 0.

The map on global sections `C⁵→H⁰(O(4))` is an isomorphism because this is the complete degree-four linear series. Thus the kernel has no global sections. By splitting on `P¹`, all four summands of this rank-four, degree-minus-four bundle have degree at most `-1`; their sum is `-4`, so all four are `O(-1)`.

Therefore

    Ω¹_P4(1)|C ≅ 4O(-1),
    Ω²_P4(2)|C = Λ²(Ω¹_P4(1)|C) ≅ 6O(-2).

This argument uses the defining complete-linear-series property of the rational normal quartic, without evaluating its coordinates.

The HM monad restricts to

    A=5O(-4) → M=12O(-2) → D=5O.

Pullback preserves the two relevant short exact sequences: their quotients are locally free, so the sequences are locally split. With `K=ker(M→D)` we obtain

    0 → K → 12O(-2) → 5O → 0,
    0 → 5O(-4) → K → F|C → 0.

In particular `rank K=7`, `deg K=-24`, and `deg(F|C)=-4`.

## 2. The splitting estimate and its direction

Write `K=⊕_{r=1}^7 O(k_r)`. Every summand maps nontrivially to `12O(-2)`, so `k_r≤-2`. Since their sum is `-24`, fixing any index gives

    k_r = -24 - Σ_{s≠r} k_s ≥ -24 + 12 = -12.

Thus every summand is between `-12` and `-2`. In particular `K(12)` is globally generated. Its quotient `(F|C)(12)` is also globally generated, so every summand of `F|C` has degree at least `-12`.

Choose the larger summand to be `O(a)`. The determinant gives the other as `O(-4-a)`. Ordering and the minimum-degree bound give

    a ≥ -4-a,         -4-a ≥ -12,
    hence -2 ≤ a ≤ 8.

The quotient argument is valid; no unsupported upper-degree bound on quotients of negative bundles is being used. Quotients may have positive degree, and the upper bound `a≤8` comes from the determinant and the lower bound on the other summand.

## 3. Exact conductor dimensions

Over characteristic zero the trace splitting gives

    B|C ≅ O ⊕ O(2a+4) ⊕ O(-2a-4).

Using the audited normalization quotient, therefore,

    Q_t ≅ O(4t-2) ⊕ O(4t+2a+2) ⊕ O(4t-2a-6).

For all integer `t`, the exact formula is

    h¹(Q_t)
      = max(1-4t,0)
        + max(-4t-2a-3,0)
        + max(2a+5-4t,0).

For `t≥1` the first two terms vanish, yielding the stated formula. More precisely:

- At `t=4`, `h¹(Q₄)=0` if `a≤5`, equals 1 if `a=6`, equals 3 if `a=7`, and equals 5 if `a=8`.
- At `t=5`, `h¹(Q₅)=0` if `a≤7`, and equals 1 if `a=8`.
- At every `t≥6`, `h¹(Q_t)=0` for every permitted splitting.

Since `deg(B|C)=0`,

    χ(Q_t)=12t-3.

In particular the exact target dimension of the first-normal-derivative descent map at `t=4` is

    h⁰(Q₄)=45+h¹(Q₄) ∈ {45,46,48,50}.

These target dimensions do not determine the rank of that derivative map.

## 4. What the normalization comparison actually proves

Put

    E_t = ν*B ⊗ O_S(3t,t),
    r_t:H²(N,B(t)|N) → H²(S,E_t),
    β_t:H¹(S,E_t) → H¹(C,Q_t).

The normalization sequence supplies the exact terminal segment

    H¹(S,E_t) --β_t→ H¹(C,Q_t)
      → H²(N,B(t)|N) --r_t→ H²(S,E_t) → 0.

The final zero follows because `Q_t` is supported on the curve `C`, so its second cohomology vanishes. Hence

    ker r_t ≅ coker β_t,
    dim ker r_t = h¹(Q_t) - rank β_t.

It follows that `r_t` is always surjective, `dim ker r₄≤5`, `dim ker r₅≤1`, and `r_t` is an isomorphism for `t≥6`.

The possible dimensions `{0,1,3,5}` at `t=4` concern `H¹(Q₄)`, not the kernel itself. The kernel can have smaller dimension, depending on the unevaluated map `β₄`. A positive conductor `H¹` also does not establish that normalization changes second cohomology.

## 5. Essential warning about the negative fourth twist

The fourth-power image is

    im[H²(P⁴,B(-4)I_N) → H²(P⁴,B(-4))]
      = ker[H²(P⁴,B(-4)) → H²(N,B(-4)|N)].

It is therefore controlled by the comparison on `N` at twist `-4`, not by `r₄`. At that negative twist,

    Q_-4 = B|C(-18)
          = O(-18) ⊕ O(2a-14) ⊕ O(-2a-22),
    h⁰(Q_-4)=max(2a-13,0) ∈ {0,1,3},
    χ(Q_-4)=-51,
    h¹(Q_-4)=51+h⁰(Q_-4) ∈ {51,52,54}.

Thus the positive-twist bound `dim ker r₄≤5` supplies no bound of 5, or any analogous nontrivial bound, for the fourth-power image in its ten-dimensional ambient space. Its exact description remains the annihilator of the image of the Koszul boundary

    δ_N:H⁰(N,B(4)|N) → H²(P⁴,B(-1)).

Normalization identifies that boundary's domain with `ker D₄`, where `D₄` has target `H⁰(Q₄)` of dimension 45, 46, 48, or 50. Neither these dimensions nor the positive-twist normalization comparison determines `rank D₄` or `rank δ_N`.

## 6. Conceptual sharpness for the restricted-monad package

The following argument constructs only abstract exact bundles and pullbacks of a universal Euler sequence. It evaluates no chosen polynomial, matrix, or rank instance.

The complete degree-five linear series on `P¹` gives the pulled-back Euler sequence

    0 → 5O(-1) → 6O → O(5) → 0.

The splitting of the left term follows by exactly the no-global-sections and degree argument in Section 1. Pull back along any degree-two morphism `P¹→P¹`, then twist by `O(-2)`. Local splitting preserves exactness and gives

    0 → A=5O(-4) --i→ E=6O(-2) → L=O(8) → 0.    (A)

Dualize and tensor by `T=O(-4)`:

    0 → L∨⊗T=O(-12) → E∨⊗T=6O(-2)
      --i∨⊗T→ A∨⊗T=5O → 0.                     (B)

Now take the hyperbolic bundle `M=E⊕(E∨⊗T)=12O(-2)`, map `A` into its first summand using `(i,0)`, and map `M` onto `A∨⊗T` using `(0,i∨⊗T)`. The composite is zero, and (A) and (B) give a genuine locally free monad. Its middle cohomology is

    L ⊕ (L∨⊗T) = O(8) ⊕ O(-12).

The hyperbolic alternating pairing on `M` is `T`-valued; `A` is isotropic and the two monad arrows are adjoint up to the conventional sign. Thus this example also respects the natural symplectic structure of a rank-two determinant-`T` monad.

It follows that the bare bundle terms, local exactness, determinant, and symplectic self-duality cannot improve `a≤8` or `h¹(Q₄)≤5`. Additional information genuinely specific to the global HM monad and its restriction to this quartic would be required. No claim is made that this constructed monad extends to the specified HM monad on `P⁴`, or that its conductor cohomology map has any prescribed rank.

## 7. Audit of the guaranteed order-two descending subspace

The newly written `PROOF.md`, Section 5, is correct. The conductor identification is the equality of `O_N`-modules

    I_{C/N}=ν_*O_S(-2Δ),

not merely equality after extension to `S`. Locally both sides are the ideal `d²R=(d²,d³)A` in the audited cusp model. Since `B(4)|N` is locally free, the finite projection formula gives

    B(4)|N ⊗ I_{C/N} = ν_*(G₄(-2Δ)).

The exact restriction sequence to the reduced curve `C` then yields

    0 → H⁰(S,G₄(-2Δ)) → H⁰(N,B(4)|N)
      → H⁰(C,B|C(16)).

Using the established identification `H⁰(N,B(4)|N)=ker D₄` and `Δ` of class `(1,1)`, this becomes

    0 → H⁰(S,ν*B ⊗ O_S(10,2)) → ker D₄
      → H⁰(C,B|C(16)).

No surjectivity of the last arrow is needed. For `d=2a+4∈{0,2,…,20}`, the last target has dimension

    17 + (17+d) + max(17-d,0)
      = 51 + max(d-17,0) ∈ {51,52,54}.

Thus the dimension of the descending domain modulo this guaranteed order-two subspace is at most 54. The proof correctly leaves the Koszul boundary's values on both parts undetermined. The section inclusion is canonical even though the splitting used to count the target is not.

## Scope and completion

The claims proposed for audit pass. The additional structural refinements are the exact formula for every twist, the `t=5` bound, the possible derivative-target dimensions, the negative-twist warning, and abstract sharpness of the restricted-monad estimate. No source-app changes, actual HM matrix evaluations, source representatives, selected polynomial-instance evaluations, or large computations were performed.
