# Independent review: root-line characteristic transport

## Verdict

**The formal calculation checks, including the rank-two identity and the global first-order consequence under the stated hypotheses.** No blocking algebraic or normalization error was found. The one local wording correction identified below has been applied and checked. The result remains a cohomological characteristic comparison, not a construction of transport of module torsors or of higher-order lifts.

Reviewed `RESULT.md` and the supporting `../../null-pair-quotient-bracket/canonical-bracket-0517/RESULT.md`, `../../null-factor-surfaces/relative-surface-0502/COTANGENT_TARGET.md`, `../../null-module-boundary-audits/module-lifting/RESULT.md`, `../../null-simple-fiber-moduli/simple-fiber-0518/RESULT.md`, and `../../null-simple-fiber-moduli/family-lift-torsor-0523/RESULT.md`. This review uses static reading and universal formal identities only. No physical source or jet values are evaluated in this argument.

## 1. Rank-two Atiyah-square identity: checked

Interpret the square as the Atiyah cup product followed by exterior multiplication of the cotangent factors, with the declared total Čech–forms signs. It is an identity in `H²(End(E) ⊗ Ω²)`, not a claim about an unprojected tensor square with coefficient `Ω¹ ⊗ Ω¹`.

A Chern-curvature representative has entries of total differential-form degree two. These scalar entries commute, even though endomorphism composition itself need not commute. Thus Cayley–Hamilton over the even-form commutative algebra legitimately gives

    R₀² = (tr(R₀²)/2) Id.

The identity is frame invariant, and its passage to Dolbeault cohomology proves the displayed identity for `At(E)₀`. It does not need stability or simplicity. The determinant-normalized case follows either from a determinant-one metric or, in cohomology on a compact Kähler manifold, from vanishing of the determinant Atiyah class. The stated real-first-Chern-class hypothesis suffices here because the determinant Chern curvature is of type (1,1), and the Kähler ∂∂̄ lemma allows a flat determinant metric. Rank two alone would not imply that the unnormalized square is scalar; the report correctly says so.

## 2. Characteristic signs and root twist: checked within declared HKR conventions

With the specified evaluation

    κ_E(π,v,b) = ½ ι_π A² + v⌟A − b Id,

putting `A ↦ A+ℓ Id` yields

    κ_(E⊗L)(π,v,b)
      = κ_E(π, v+D_πℓ, b−v⌟ℓ−½ι_πℓ²).

The minus signs in the new gerbe coordinate are necessary: evaluation subtracts that coordinate. The module-lifting report independently fixes the minus-gerbe sign through the literal defect variation. The simple-fiber report fixes the bivector normalization and its trace pairing.

The definition of `D_πℓ` by its contraction identity avoids an otherwise real ambiguity in left/right contraction and total-form signs. It should be understood as the natural contraction operation for arbitrary Atiyah factors, not as uniquely reconstructing a vector-valued class from pairing with one fixed bundle. On the plane, contraction with the identity canonical-valued bivector is an isomorphism `Ω¹ → T⊗ω`. Since `H/2` is nonzero in `H¹(Ω¹_P²)`, its image is nonzero.

A convention cannot by itself prove that a particular physical ambient cocycle has these HKR coordinates. The full characteristic–Atiyah formula and identification of the actual first-order source remain prerequisites of the physical application. The report explicitly retains those prerequisites in its global conclusion; this review does not independently evaluate that physical source.

## 3. Degree-eight canonical trace: checked

The character line and canonical line identification is the normalized finite canonical trace after multiplication by the dual volume:

    j_Ω(l) = Tr_p(lΩ)/8.

On the étale locus the pulled-back volume identity and trace–pullback identity give exactly the identity symbol `P`, and equality extends as a sheaf morphism across ramification. No inversion of a ramified differential is needed globally. The same natural sheaf morphisms, applied to cup-product representatives pulled back from the plane, justify the middle-component contraction comparison.

For `ℓ=p*H/2`,

    j_Ω(½ι_πℓ²) = H²/8.

Therefore the physical scalar coordinate `−15Π` becomes `−15H²/8`; applying the root transport subtracts another `H²/8`, producing `−2H²`. Unnormalized trace would scale the complete canonical-coefficient direction by eight, rather than changing only its gerbe entry.

## 4. Numerical checks and resolved wording correction

For rank two, `c1(E)=−H`, `c2(E)=4H²` imply `ch2(E)=−7H²/2`. The trace of the root-normalized bivector evaluation is

    −7H²/2 − H²/2 + H²/4 = −15H²/4.

Its scalar-inclusion coordinate is therefore `−15H²/8`. For the transported plane direction, the characteristic trace is

    −7H²/2 − H²/2 + 4H² = 0.

All rank factors are correct. Stable-plane simplicity makes the trace map an isomorphism, so this trace cancellation alone proves the claimed plane vanishing. Independently, the rank-two identity shows that the bivector-plus-middle term is already scalar.

**Resolved wording correction in section 3:** the earlier sentence saying that “the scalar gerbe in (2) cancels its scalar component” immediately follows discussion of the *root-normalized bivector evaluation*. Literally these scalar coordinates differ:

- Root-normalized bivector: `−15H²/8 Id`, cancelled by the pushed-down physical gerbe `−15H²/8`.
- Transported plane bivector plus middle term: `−2H² Id`, cancelled by the transported gerbe `−2H²` in (2).

The difference is the `H²/8 Id` root-square term. The revised section 3 now explicitly distinguishes these two cancellations. I reread the corrected text and verified that it resolves the issue without altering any displayed formula or conclusion.

## 5. Global first-order consequence: checked, conditionally

For a genuine rank-two bundle `F` on the stipulated compact abelian fourfold with trivial determinant and `c2(F)=15θ²`, the universal identity gives

    At(F)² = ½tr At(F)² Id = ch2(F) Id = −15θ² Id.

Hence for any stipulated bivector and `Π=½ι_πθ²`,

    ½ι_π At(F)² = −15Π Id.

For a genuine first-order ambient algebroid whose *full* characteristic coordinates are `(π,0,−15Π)`, the first-order obstruction is zero globally. This conclusion does not depend on restricting to simple fibers and is stronger than fiberwise trace cancellation. In the locally free square-zero gluing framework, with an acyclic cover/refinement, zero obstruction suffices for existence of an abstract global first-order module lift.

The hypotheses that matter are genuine local freeness, determinant/Chern identities, genuine first-order ambient descent data, the characteristic–HKR comparison, and absence of a first-order middle class. They are not supplied merely by identifying endomorphism sheaves. A higher-order unary term does not enter this first-order calculation; an actual first-order unary class does. The report states these distinctions correctly.

There is no implication for a chosen first-order representative, a chain-level root/Morita comparison, compatibility of relative-family torsors, the frozen second-order module problem, higher formal existence, or any of the thirty mixed obstruction values. In particular no contradiction arises with the earlier family report's warning that a physical lift cannot trivialize a naively defined plane torsor by an endomorphism-sheaf identification alone.
