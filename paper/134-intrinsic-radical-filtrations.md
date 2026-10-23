# 134. Intrinsic radical filtrations in the four necessary bundle types

**23 October 2026 · Conditional geometry through PR1132.** All statements in this chapter are conditional on the indicated formal type from Chapter 132. None selects, realizes or eliminates a type. The canonical complement K from Chapter 133 has rank 15 and degree −48; E=L⊕K with L=W′O(-3).

## Immutable proof sources

- [Types I and II: radical-square geometry](https://github.com/Akilleez-QA/read-em-and-weep/blob/7c569012b78497f8f0340b7ea9fca347f96860bb/research/hm/radical-square-geometry/PROOF.md), [PR1130](https://github.com/Akilleez-QA/read-em-and-weep/pull/1130), commit `7c569012b78497f8f0340b7ea9fca347f96860bb`.
- [Type III: image equals annihilator](https://github.com/Akilleez-QA/read-em-and-weep/blob/4bed227b0c6bd0656e1d89df2ec9d4ab513db5ef/research/hm/type-three-radical-filtration/PROOF.md), [PR1131](https://github.com/Akilleez-QA/read-em-and-weep/pull/1131), commit `4bed227b0c6bd0656e1d89df2ec9d4ab513db5ef`.
- [Type IV: doubled Euler filtration](https://github.com/Akilleez-QA/read-em-and-weep/blob/cb9e9b4f8abda70e6d43b9f9ac319afe1fa60004/research/hm/type-four-radical-filtration/PROOF.md), [PR1132](https://github.com/Akilleez-QA/read-em-and-weep/pull/1132), commit `cb9e9b4f8abda70e6d43b9f9ac319afe1fa60004`.

## Different radical constructions must be labeled

Let N=rad End_G(E). In types I and II the new construction uses the **square N²**, whose dimension is one. In types III and IV it uses the **first radical J=rad End_G(K)**, identified with N because L is isolated in those types. Their images are different constructions; the following ranks must not be read as a common decreasing case counter.

| Formal type | Intrinsic construction | Rank | Degree | Further structure |
|---|---|---:|---:|---|
| I or II | S=image(N² acting on E), contained in K | 3 | −12 | Saturated; abstractly V O(-4) |
| III | S=J·K=Ann_K(J) | 6 | −18 | Saturated; V O(-2)⊕V O(-4) |
| IV | S=J·K | 6 | −24 | Saturated; 2V O(-4) |
| IV | A=Ann_K(J), containing S properly | 12 | −36 | Saturated; 2T6 O(-3) |

These images and common annihilators are intrinsic sheaves and are preserved by global equivariant bundle endomorphisms. The calculations may choose decompositions to identify their abstract types, but they do not make those decompositions canonical or establish invariance under additional operators.

## Types I and II: the radical-square image is saturated everywhere

The nonzero square-radical channels are the universal maps

    I:  V O(-4) → D O(-2),
    II: V O(-4) → P O(-2).

Full polynomial maximal-minor certificates show that both have rank three at every point of the parameter line. Symbolic charts retain an indeterminate; they are not sampled-direction tests. Consequently each image is a saturated subbundle, not merely a generically injective sheaf.

The exact top-block quotients are W′O(1) in type I and O(4) in type II. The type-I balancing proof uses the absence of degree-two transpose syzygies to show H0(C*)=0, then degree two forces C=2O(1). Its equivariant coefficient representation is W′. The type-II rank-one quotient is determined by degree and the absence of nontrivial one-dimensional characters.

Crucially, the original source V O(-4) is **retained** in the total quotients. The image S lies inside the top D/P block, not inside that source block:

    I: E/S ≅ W′O(1)+(W′+T6)O(-3)+V O(-4)+O(-8),
    II: E/S ≅ O(4)+(W′+T6)O(-3)+V O(-4)+W′O(-5).

Both have rank 14 and degree −42. Removing the canonical L gives

    I: K/S ≅ W′O(1)+T6 O(-3)+V O(-4)+O(-8),
    II: K/S ≅ O(4)+T6 O(-3)+V O(-4)+W′O(-5),

each of rank 12 and degree −36. These are abstract quotient isomorphism types, not canonical direct-sum splittings. A positive-degree quotient does not produce a positive subbundle of E and gives no contradiction with its negative splitting degrees.

## Type III: image equals annihilator, but the filtration is nonsplit

The three radical channels are the Euler arrow T6 O(-3)→V O(-2) and two arrows V O(-4)→T6 O(-3). The exact Euler sequence

    0 → V O(-4) → T6 O(-3) → V O(-2) → 0

gives J²=0 and the intrinsic equality J·K=Ann_K(J)=S. The quotient is

    K/S ≅ V O(-2)⊕2V O(-4),

of rank 9 and degree −30. On total E, the image remains S but Ann_E(J)=L⊕S, of rank 8 and degree −24.

The sequence 0→S→K→K/S→0 does not split, even as ordinary vector bundles. After twisting by O(2), K has three sections, whereas a split sum of S and K/S would have six. Local chart splittings do not supply a global splitting. Square-zero composition in the endomorphism algebra therefore does not imply that its induced sheaf filtration splits.

## Type IV: a proper image–annihilator inclusion

The two independent radical channels map V O(-4) into the two T6 O(-3) copies. Their images give S=2V O(-4), while the common annihilator is A=2T6 O(-3). Thus S is properly contained in A, unlike type III. Their quotients are

    A/S ≅ 2V O(-2),       K/A ≅ V O(-4).

On total E, Ann_E(J)=L⊕A has rank 14 and degree −42. The middle sequence 0→S→A→A/S→0 is a doubled Euler extension and is nonsplit: after twisting by O(2), its middle term has no sections but a split sum would have six. The different outer sequence 0→A→K→K/A→0 does split in the indicated type, without a canonical choice being asserted.

## Evidence and unchanged boundary

The three full proofs and their accepted independent reviews were read. Whole-coefficient minors, symbolic-chart image/kernel identities, exact cohomology controls and independent Euler-overlap checks support the statements. They do not formally verify every pinned geometric dependency.

These are conditional intrinsic-filtration refinements, not a reduction from four cases to fewer cases. Actual occurrence, the geometric coverage bridge, positive-coordinate or invariant-quadratic compatibility, Gauss compatibility and the original repair remain unresolved. No full-adjoint, higher-lifting or algebraicity conclusion follows.

Earlier chapters and archive 52 are preserved. The delivered v0.3 PDF remains the fixed 23 October 2026, 19:16 UTC snapshot through PR1117; no replacement PDF is supplied by this Markdown continuation.
