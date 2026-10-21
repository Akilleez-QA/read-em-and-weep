# 1. Current theorem and notation

## 1.1 Setting and conventions

Work over the complex numbers. Let F denote the fixed Horrocks-Mumford bundle in the normalization used by the pinned proofs, and B = End₀(F) its trace-free endomorphism bundle. For a quadric Q, write B_Q for its restriction. Superscripts + and −, or subscripts + and −, refer to the physical inversion eigenspaces, not to the local stabilizer parity of a weighted-stack presentation.

The projective coordinates split into positive and negative summands. Write W for the two-dimensional negative coordinate representation, A = Sym²W for its three-dimensional quadratic representation, D5 for the five-dimensional positive quadratic representation modulo the invariant quadric, and P4 for the four-dimensional cokernel representation. V denotes the three-dimensional representation occurring in the complementary sextic channel; in Section 5, the unrelated projective variety is always written V51. These dimensions must not be substituted for information about the actual maps.

Let q₀ be the invariant rank-three quadric and Q₀ its cone. A negative quadratic a ∈ A determines the pencil q₀ + t a. The positive cohomology multiplication map is

    M(t): H¹(B(2))₊ → H¹(B(4))₊,
    M(t) = multiplication by q₀ + t a.

Its source and target dimensions are 41 and 37. The ambient section vanishings used by the pinned arguments identify the positive section space on a quadric with the kernel of this multiplication map.

## 1.2 The current conclusion

**Theorem.** In this family, the odd section space vanishes for general smooth Q. The positive section space for general smooth Q has dimension four or five.

**Proof structure.** The odd proof establishes injectivity of the actual six-to-ten smoothing map, not merely the existence of an injective equivariant map. On the positive side, the actual invariant-cone map has rank 33. The first Bockstein is zero. The actual second Bockstein is zero on D5 and nonzero with generic rank three on A. The generic positive rank is therefore at least 36 and at most 37. Rank-nullity gives positive kernel dimension at most five and at least four. Intersecting the relevant nonempty open sets gives the total count. [Odd proof][O]; [positive integration][G].

“General” means on a nonempty Zariski-open subset of the parameter family. This does not assert the same dimension on every quadric, on every pencil, or on singular special fibers.

## 1.3 What remains open

After the generic second-stage calculation, the surviving positive source is five-dimensional and the remaining target is one-dimensional. The next possible obstruction is the third Bockstein, with later Bocksteins relevant if it vanishes. A nonzero higher obstruction would force rank 37 and four sections. Persistence of the final cokernel would instead give rank 36 and five sections along that pencil. Neither alternative is decided by the results collected here.

Even a proof of the four-section alternative would close only this adjoint gate. It would not by itself identify the required original source, construct the necessary lifting data, or prove the intended Weil class algebraic. Those require their own mathematical bridges.

## Pinned source references

[O]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ec080c229105457eafcd2583c8a47b362627a62e/research/hm/order-four-quadratic-load/SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c/research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md
[F]: https://github.com/Akilleez-QA/read-em-and-weep/blob/846968261441fef2cad247d22b66d37aed3f0f8f/research/hm/order-four-quadratic-load/POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md
[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/04fb081d710f1d7e175f252601b96dddcd93106e/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md
[N]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9f28cb10c38d7a0e29c1eb994594325fea7f22bf/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md
[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/72aa6fb732a803eb9201f45f1f82e60f54d296b4/research/hm/order-four-quadratic-load/POSITIVE-GENERIC-FOUR-OR-FIVE-SECTIONS.md
