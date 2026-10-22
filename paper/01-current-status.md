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

After the generic second-stage calculation, the surviving positive source is five-dimensional and the remaining target is one-dimensional. The actual third Bockstein is identically zero, including the extra specialized kernel line at each of the six second-symbol axes. The next possible obstruction is fourth order; if the last generic Smith factor has finite exponent e, then 4 ≤ e ≤ 31. See [Section 15](15-third-vanishing-and-fourth-frontier.md). A nonzero higher obstruction would force rank 37 and four sections. Persistence of the final cokernel would instead give rank 36 and five sections along that pencil. Neither alternative is decided by the results collected here.

The canonical raw cubic and its unique canonical correction L_can are nonzero, but their final third quotient is zero. The corrected fourth source has nonzero parameter trace; its full lower input cannot be reconstructed from the effective vector shadow alone. A complete test uses the entire D5-family first ideal-sheaf jet at one axis and one C5-square fiber. All actual fourth coefficients remain unevaluated. See [Chapter 16](16-canonical-fourth-input-and-complete-test.md).

The full corrected C5-square lower source is nonzero, already in the canonical realization Cminus≅H⁰(D,O_D(−2,10)). Absolute midpoint and Atiyah sections recover the previously lost polynomial-nine data. A global trace null-homotopy isolates the secondary endpoint P4, whose actual normal variation is now nonzero; its nilpotent square-shadow component must still be retained in the adjoint lift. Secant restriction plus parameter trace reconstructs lower families as 13→11+2, while the two endpoint channels restrict isomorphically as 2→2. None of these results evaluates a fourth coefficient. See [Chapter 17](17-absolute-lower-source-and-secondary-endpoint.md). Nonzero lower source is not nonzero fourth value; the required ambient division and final quotient remain.

The actual normal trace has both α≠0 and β≠0, with β proved nonzero by restriction to 2C. Global wedge cancellation fixes γ=−1/(12ν) in the shared normalization. The nonzero conic Euler cocycle completes the homogeneous pair to a genuine global G(4) section, with full root/triangular gluing and Hartogs extension. The lowest η diagonal is nonzero. A regular scalar-lift commutator correction contributes to the displayed old-K terms in degree twelve, not four; the full actual normal-K comparison remains open, while Chapter 19 now evaluates the lower endpoint on two canonical inputs. See [Chapter 18](18-actual-cone-lift-and-nilpotent-trace.md). PR660 gives a secant-plus-intrinsic-cubic-jet fourth-family test, while PR661 detects both endpoint channels at one C5-square secant fiber; neither evaluates the actual family.

The actual endpoint is now evaluated on two canonical inputs at a=t²: X⁴ gives zero and XY³ gives c_eta·3k/(Bc)[Y/z]≠0. The common nonzero scale c_eta is retained. The invariant normal line injects into the two-dimensional quadratic endpoint-family space. Every nonzero direction has a nonzero entire lower endpoint map; at every square its secant restriction is also nonzero. This neither asserts nonzero values on individual inputs nor evaluates the fourth obstruction. [Chapter 19](19-actual-endpoint-values-and-last-gauss-quotient.md).

The actual quadratic lower endpoint is reconstructed. The entire (3,1) and (1,3) Gauss profiles are excluded; the remaining possible profiles are (1,1), (1,2), (2,1), (2,2), not realizations. Generic SF ≥ 3 and square rank ≥ 27 remain unchanged. The complete two-arrow Cartan–Koszul homotopy determines C_mult=−χ/g_L and κ=−(χ/g_L)(a_m/b_m), with the physical equation, full-trace volume and actual channel markings retained. The genuine midpoint pair's residue χ̄=−Bλ/(4ν²)n_ap remains nonzero. Its complete leading affine law and scalar compatibility now give a unique weight-four correction, but higher weights and the full actual R2 comparison remain unresolved. The checked next-weight interface normalizes midpoint Z4 only, allows Z6 from arbitrary q² repairs, and retains the endpoint η terms and Op2 defect. Global conic regularity excludes global K4 differences without proving existence or the value of the selected actual coefficient. Mr. Slop's PR668–670 determine the universal detection scheme as sixteen reduced axes, exactly two exceptional channels, and exact residue-lifting and division-free reconstruction tests. These do not determine actual source membership or the fourth value. [Current bounded update, Chapter 22](22-full-saturation-and-cartan-koszul-multiplier.md).

Even a proof of the four-section alternative would close only this adjoint gate. It would not by itself identify the required original source, construct the necessary lifting data, or prove the intended Weil class algebraic. Those require their own mathematical bridges.

## Pinned source references

[O]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ec080c229105457eafcd2583c8a47b362627a62e/research/hm/order-four-quadratic-load/SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c/research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md
[F]: https://github.com/Akilleez-QA/read-em-and-weep/blob/846968261441fef2cad247d22b66d37aed3f0f8f/research/hm/order-four-quadratic-load/POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md
[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/04fb081d710f1d7e175f252601b96dddcd93106e/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md
[N]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9f28cb10c38d7a0e29c1eb994594325fea7f22bf/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md
[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/72aa6fb732a803eb9201f45f1f82e60f54d296b4/research/hm/order-four-quadratic-load/POSITIVE-GENERIC-FOUR-OR-FIVE-SECTIONS.md
