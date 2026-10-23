# Independent review: complete universal nonic base-scheme classification

## Verdict

PASS. The seven authenticated inputs give an exhaustive classification of the component ideal sheaf of every nonzero universal pure-V nonic gate. There are exactly four exceptional projective coefficient points and one complementary open stratum. The open-stratum conclusion is uniform for every coefficient ratio in that stratum, not merely generic.

This is a completed universal base-scheme classification, conditional on the retained source2 pure-V identifications. It is not a proof of source occurrence, a computation of actual gate coefficients, or a repair of the original source-classification problem.

Reviewed final PROOF.md SHA256:

    a68ae2b4ca0b212ab442ad252ed23d0b26c3462d2774eb826ba8d10bbd5be658

## 1. Direct-input authentication and review scope

The reviewer freshly fetched all seven direct input proofs through the GitHub connector at their exact commit and repository path. Every returned UTF-8 file matched the retained bytes exactly. Both SHA256 and Git-blob SHA1 were independently recomputed and matched INPUTS.json. Matching Git blobs are:

- PR1030 at 418a7d9ebedaae9b5d00db9f69e449b5d8767108: aec4e3f550d3dc4bedb2911019de65e61852c436.
- PR1035 at 6effcd9b61b1942447a2c3f136a6776dda213c15: eb0b5dc78615331526b679eea952e4a46f7d01ea.
- PR1036 at bb22e239e9423b54487236dba8c4f70f9e6b738f: 718f987511b5bf6144a85fc14e8ef343612a4491.
- PR1037 at 6527465d81b7be4176ff57a0135a0a7f1ee756fd: 7fdcab9202a78e9f371c32903840969e0453c7b5.
- PR1040 at c8df54084115e242fd39457e95da187cb9952168: f42554d807c0b66a0eea5bc8453e3a2682b94919.
- PR1042 at 848e947ae1575434e93a82a4ec8ba235606e3224: c85eecff0c7bdc8caa7a74423b2bee318b35d700.
- PR1043 at 97321a949be30eeddf7a2a467aa28df9f798f4ee: 68bd6866c432983693cd1e66e313d06305187548.

The review read the exact input statements and relevant proofs, including the fifteen-axis occurrence if-and-only-if and ambient reducedness, the all-coefficient thirty-orbit exclusion, and the complete conic-line scheme. It does not present fresh authentication as a proof-assistant replay of every transitive dependency.

As an additional independent cross-check, the reviewer reconstructed F1 and I12=(delta,cP^T GP cP) from the fixed universal model, and independently verified in graded reverse lexicographic order that (F1)+I12²=I12 on the full p=1 chart and that its p=0 boundary is empty. Thus the ambient conic Nakayama certificate was also checked directly, without selecting a conic root.

## 2. The partition really is exhaustive

The retained lift/gate isomorphism identifies the coefficient plane with the two-dimensional nonic gate space. Its injectivity ensures that a nonzero pair gives a nonzero gate, so the imported finite-base theorem applies. Scaling a coefficient pair by a nonzero scalar leaves its component ideal unchanged.

The four forms beta−2alpha, beta+2alpha, beta+alpha, beta are pairwise nonproportional in characteristic zero. No nonzero pair lies on two of their kernels. Their product vanishes precisely on those four projective points; every other projective point is in the stated open stratum. At alpha=0 the product is beta^4, so [0:1] is included in the open stratum, not omitted as a coordinate boundary.

This partition is algebraic and exact. It does not infer global behavior from testing a finite list of generic coefficient values, and it does not leave room for an unexamined coefficient point at infinity.

## 3. Four exceptional schemes

Each special row is a direct application of an exact scheme theorem, not a conclusion from its length alone:

- At beta=2alpha, PR1037 gives m³ at all six C5 axes and m at all ten C3 axes, with no other support. The exact length is 6·6+10=46.
- At beta=−2alpha, PR1037 gives the fixed length-four C5 ideals and m² at all ten C3 axes, with no other support. The exact length is 6·4+10·3=54.
- At beta=−alpha, PR1040 gives precisely Z together with the fifteen reduced order-two axes. The exact length is 34+15=49.
- At beta=0, PR1043 gives precisely Z together with twelve reduced ambient conic points. The exact length is 34+12=46.

The two length-46 schemes are different. In the first, the six existing C5 ideals have changed to m³ while support remains the sixteen prescribed axes. In the second, all ideals on Z remain unchanged and twelve new reduced points occur on the conic. Consequently a mere list of allowed lengths would not be a complete scheme classification; the table correctly records support and local ideals.

All added reduced orbits are disjoint from Z and from each other. The ambient reducedness inputs, rather than only reduced intersections with a conic or mirror, are essential to the exact scheme statements.

## 4. Why the whole open stratum is exactly Z

For a coefficient pair off all four kernels:

1. Being off the two jet kernels makes the local component ideal equal to the prescribed ideal at every point of Z, by PR1030 and its placement in PR1036.
2. Being off beta=0 rules out every conic basepoint, not just the twelve known points on a selected member.
3. Being off beta=−alpha rules out the entire fifteen-axis orbit by the if-and-only-if in PR1040.
4. PR1042 rules out every thirty-point orbit for every nonzero pencil member, including any exceptional coefficient ratio inside the open stratum.
5. PR1035 exhausts the possible additional support and excludes free orbits and all other alternatives.

Thus every point outside the support of Z has unit component ideal, while every point of Z has exactly its prescribed local ideal. Equality at all stalks implies equality of ideal sheaves globally. In particular, there is no residual embedded thickness at an old support point and no extra zero-dimensional scheme hidden outside the listed support. The finite-base theorem also rules out divisorial components.

Therefore B(F)=Z for every pair in the entire open stratum, of exact length34. The deduction uses universal statements from the inputs, so it does not merely prove that the generic member has this scheme.

## 5. Ideal sheaves, zero pair, and distinct mathematical objects

The theorem correctly defines the base scheme using the component ideal sheaf, equivalently the saturated homogeneous ideal. Stalkwise scheme equality does not require equality of the raw four-generated homogeneous ideals; possible differences at the irrelevant affine origin are not part of the projective scheme being classified.

The zero pair is outside the projective classification. Its component ideal sheaf is zero and its base scheme is the entire plane, not the empty scheme or a finite scheme of length zero. The unknown actual gate may still be zero; the universal nonzero classification does not decide that.

Three objects must remain distinct:

- The nonic component ideal of the quotient-third gate s, which is classified here.
- The component ideal of the original fourth on its surviving D part, obtained by composition with L and the retained target identification.
- The matrix-rank degeneracy scheme of the quadratic lift R.

Global identical vanishing of s is equivalent to global identical vanishing of the original fourth on D, as inherited from the gate theorem. This does not identify their local component ideals. At the ten C3 axes, L is not surjective, so composition can change local base ideals there. The rank-three label for one coefficient point likewise does not equate its lift degeneracy scheme with its nonic base scheme. The proof preserves these distinctions and draws no unsupported conclusion about a completed original proof repair.

## 6. Reproducibility and conclusion

The reviewer replayed `python verify.py` and `python -O verify.py`: all 31 checks passed with byte-identical output. These checks authenticate the inputs and verify the coefficient partition and exact length bookkeeping. The exhaustive geometric conclusion is the written deduction from the authenticated support and local-ideal theorems, not something asserted to follow from bookkeeping alone.

No actual HM coefficient, parameter instance, selected orbit root, or source realization was evaluated. No logical gap remains in the complete universal component-scheme classification under the stated hypotheses.
