# A stable field-three carrier with six genuine mixed obstructions

Over C, an explicit rank-seven quadric containing the Segre fourfold X=(P¹)⁴ has projective radical disjoint from X. Projection gives g:X→Q⁵ with g*O(1)=O(1,1,1,1). Its image is the singular normal Klein-four quotient, a (2,3) complete intersection; the projection need not be flat.

For every normalized Cayley bundle C on Q⁵, g*C is slope-stable. Product elliptic double covers, with actual determinant-normalizing line bundles, give stable rank-two bundles E on principally polarized abelian fourfolds with det E=O and c₂(E)=3θ². Their Euler characteristics are χ(E)=18 and χ(End E)=288.

The actual weak first-order test fails: all six mixed Atiyah evaluations are nonzero and independent. The full HKR evaluation has rank 18 and kernel dimension 10, whereas the Chern-character annihilator has dimension 16. The exclusion holds for every Cayley parameter on this carrier and every finite abelian pullback to X, including actual isogeny descent.

The rank-seven quadratic form is smooth on its rank-at-most-seven component, with projective tangent dimension nine. Every radical-disjoint point of that component is equivalent under PGL₂⁴. Other components and unrelated bundles are not classified here.

## Proof order

1. `rank7_construction.md`: explicit quadratic and cubic identities and geometric basepoint-freeness.
2. `image_geometry.md`: scheme image, normal quotient, singularities, and nonflat fibers.
3. `cayley_pullback_stability.md`: stability on X and the abelian double-cover source.
4. `spinor-cohomology-certificate.md`: exact Cayley–spinor acyclicity; the essential invariant differential has determinant −3.
5. `cayley_weak_reduction.md`: exact ACM pushforwards, six genuine Atiyah tests, and kernel dimensions.
6. `cayley_finite_pullback_noescape.md`: simultaneous differential-trace retractors for arbitrary finite abelian maps.
7. `rank7_orbit_component.md`: exact tangent computation, stabilizer, and exclusion of radical-disjoint boundary variants in this component.

## Reproduction

Python 3 and SymPy are required. From this directory run:

- `python primitive_certificate.py`
- `python verify_geometry.py`
- `python clifford_certificate.py`
- `python verify_spinor_cohomology.py`
- `python pair_module_generation.py`
- `python verify_finite_pullback_character.py`
- `python rank7_tangent_certificate.py`

These certificates check exact polynomial identities, ranks, Clifford relations, Lie-algebra differentials, and the multiplication maps used in the proofs. They supplement the sheaf-theoretic, representation-theoretic, and geometric arguments; finite-field checks are used only to certify maximal characteristic-zero ranks of integer matrices. No solution of an ambient higher-order obstruction or of the original withdrawn theorem is asserted.
