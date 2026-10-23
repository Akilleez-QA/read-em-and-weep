# 133. Canonical doublet retraction and the smaller negative tail

**23 October 2026 · Checkpoint through PR1127.** This chapter distinguishes a new source-independent actual-map construction from the conditional endomorphism algebras of the four necessary bundle types. [Full immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/60dda5a940d5ba7ee081a86cd1b1a783a5952a39/research/hm/primary-quotient-composition/PROOF.md), commit `60dda5a940d5ba7ee081a86cd1b1a783a5952a39`, in [PR1127](https://github.com/Akilleez-QA/read-em-and-weep/pull/1127).

## A partial splitting becomes canonical

The preceding primary-summand theorem constructs the canonical saturated image H=(W′+T6)O(-3) inside the actual negative kernel bundle E. In this chapter Q denotes the bundle quotient E/H, not the invariant quadratic multiplication. This quotient has H1(Q(1))=2T6 and H0(Q(1))=0. Although a complement to all of H has a two-dimensional equivariant ambiguity, its distinct doublet piece L=W′O(-3) has a canonical retraction.

Indeed, Serre duality gives Hom_G(Q,L)=Hom_G(2T6,W′)=0 and Ext¹_G(Q,L)=0. Restriction therefore identifies Hom_G(E,L) with Hom_G(H,L). The canonical projection H→L extends to one and only one equivariant map p:E→L. For the actual inclusion i:L→E, pi=id_L. Consequently

    E = L ⊕ K,       K=ker p,
    rank K=15,       degree K=−48.

Both the retraction and K are canonical relative to the actual primary inclusion and fixed physical marking. Moreover every equivariant bundle endomorphism preserves K, because Hom_G(E,L)=C·p. This does not imply that every endomorphism preserves L or that the idempotent ip is central.

The remaining sequence 0→T6 O(-3)→K→Q→0 still has an affine two-dimensional space of equivariant sections. Thus a canonical doublet splitting does not remove the ambiguity in choosing a complement to the full eight-dimensional primary summand. This construction does not use the four-type classification or any source2 occurrence hypothesis.

## The actual negative tail reduces from 54→37→20 to 48→33→18

The original negative tail identifies naturally with

    H1(E(-1)) → H1(E) → H1(E(1)),

using the same determinant convention for both arrows. Parameter multiplication commutes with the canonical bundle projector, so this is an actual splitting of negative maps, not a subtraction of matching characters.

The L summand has cohomology characters T6→P→W′ and dimensions 6→4→2. Its canonical complement has characters

    3W′+3S+5T6 → 2V+3P+3D → 3T6,

and dimensions 48→33→18. In particular the terminal 37→20 pencil canonically splits as 4→2 plus 33→18. Here S=Sym³W, D=Sym⁴W, and W is the negative coordinate doublet.

The scope stops at this actual three-degree negative tail. No projection to M2, positive-coordinate multiplication, invariant-quadratic multiplication, ambient Gauss compatibility or full graded-module splitting is supplied. The reduced dimensions are map dimensions, not a measure of proof completion.

## Conditional endomorphism algebras of the four formal types

For the four formal E types I–IV in [Chapter 132](132-canonical-primary-quotient-and-four-types.md), subtracting the actual equivariantly split H gives the abstract quotient types

    Q1 = D O(-2) + V O(-4) + O(-8),
    Q2 = P O(-2) + V O(-4) + W′ O(-5),
    Q3 = V O(-2) + 2V O(-4),
    Q4 = T6 O(-3) + V O(-4).

No quotient type or source occurrence is selected. The complete two-sided Hom and composition calculation gives:

| Formal type | dim End_G(E) | Dimension of Jacobson radical | Semisimple quotient | Radical products |
|---|---:|---:|---|---|
| I | 9 | 4 | C⁵ | Square has dimension 1; cube is zero |
| II | 10 | 5 | C⁵ | Square has dimension 1; cube is zero |
| III | 10 | 3 | C³ × Mat₂(C) | Square is zero |
| IV | 8 | 2 | C × Mat₂(C) × C | Square is zero |

The types I–III have vanishing feedback H→Q_i→H. Their H diagonal block is complement-independent even when an endomorphism does not preserve H. Type IV has a nonzero feedback line supported on T6; the same H-diagonal conclusion does not extend to it. The canonical doublet retraction remains valid in every case.

Nonvanishing of the short reverse compositions in types I and II is established by full binary-polynomial polarization and an sl2-invariance obstruction, not solely by a dimension count. Exact character and block-gauge checks support the algebra calculation. These conditional algebras do not identify the actual type, construct an actual source or settle the geometric coverage bridge.

## Evidence and edition boundary

The proof uses the complete immutable primary-summand, canonical-slope and actual-pencil sources. [Independent review](https://github.com/Akilleez-QA/read-em-and-weep/blob/60dda5a940d5ba7ee081a86cd1b1a783a5952a39/research/hm/primary-quotient-composition/REVIEW.md) accepts its actual-map construction and the conditional algebra calculation. The exact standard-library checker passes 185 checks in normal and optimized modes, authenticating inputs and verifying nine-class representation arithmetic, symbolic polarization and block-gauge identities. Separate independent synthetic controls pass 3,855 block-conjugation checks in both modes. These checks support the written proof; they do not constitute proof-assistant certification of the geometric dependencies.

Chapters 131–132 remain unchanged. The historical four-pair ledger is not revived as a compatible frontier, and the four formal bundle types are not asserted realized. No rank-three coverage, full-adjoint invertibility, higher lifting, algebraicity or complete original repair follows.

The delivered v0.3 PDF remains the fixed 23 October 2026, 19:16 UTC snapshot through PR1117. This is a living Markdown continuation only; no PDF replacement is made.
