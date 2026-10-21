# Independent mathematical review

Verdict: PASS, conditional on the pinned repository inputs. This is a mathematical review, not a proof-assistant check.

Reviewed file: PROOF.md

Reviewed SHA256: 5b15161d0cce2c1b7c99b129d079c2571812ad93b85163b311006e96fb6e7e3c

## Checks

1. The hypotheses suffice for the required universal constants statement. Geometric reducedness is open; upper semicontinuity and nonemptiness give h0=1 near the marked fiber. Field base change then gives geometric connectedness. Stacks 0E0L applies to this proper flat finitely presented family and all its base changes. No unjustified neighboring-integrality claim is needed.
2. The section construction is genuinely pointed etale: a smooth point of the central integral complex variety lies in the smooth locus of the flat family, and pulling a smooth-coordinate etale chart back along a constant affine-space section provides the section after etale base change. It is an existence argument, not a selected HM/source evaluation.
3. Picard representability and local finite presentation are separate requirements, correctly supplied by Stacks 0D2C and 0DNI. The section plus universal constants identifies relative Picard classes with actual line bundles rigidified along that section, as in Stacks 99.11.4 and 99.11.7. Therefore the construction does not silently discard a Brauer obstruction.
4. The root-class fiber R is locally of finite presentation. Its Artin lifting property is evaluated on the specified family Y_(A'), not by assuming the entire Picard space is smooth. PR632's fixed-central-root theorem gives existence and uniqueness of classes. An etale chart transfers this to the ordinary local Artin smoothness criterion 02HX; the relative tangent space is zero, yielding etaleness. Residue fields at the chosen points are C, as required.
5. Equality m ell=[M] in the relative Picard space yields only L^m tensor M^(-1)=f^*N initially. The proof explicitly trivializes N near the marked point before asserting an actual power isomorphism. Scalar correction of beta imposes the prescribed central compatibility. No global extraction of varying unit roots or base-line-bundle roots is presumed.
6. Relative ampleness follows from the actual central root and 0D2S. Taking a connected component of the smooth curve preserves the marked point and yields an integral finite-type base.
7. Pointed etale localization preserves the completed local ring and its finite quotients. The powered finite-jet identification from PR629, followed by PR632 uniqueness on the same underlying infinitesimal family, identifies the original-polarized jets. This improves the single-power method without asserting descent of the entire original formal arc.
8. The automorphism consequence correctly reapplies PR629's Artin/formal-faithfulness proof after base change rather than assuming automorphism groups cannot grow under base extension. PR630's generic degree-one section-loss argument applies to the recovered actual root. Neither consequence asserts trivial geometric generic-fiber automorphisms.

9. Section 5 correctly extends the construction to a finite-type complex base with a C-point. Smoothness or dimension one of the base was not used before choosing the final curve component. Applying this extension to the high-power universal Hilbert family yields an actual relatively ample root on a pointed etale chart. PR631 supplies smoothness and dimension n^2+635, preserved by the etale chart. The claim is a parameter family, not representability of polarized moduli, a quotient theorem, or a global uniqueness assertion.

## Primary references independently inspected

- https://stacks.math.columbia.edu/tag/0D2C
- https://stacks.math.columbia.edu/tag/0DNI
- https://stacks.math.columbia.edu/tag/0E0L
- https://stacks.math.columbia.edu/tag/0BDN
- https://stacks.math.columbia.edu/tag/0D24
- https://stacks.math.columbia.edu/tag/02HX

The pinned local proofs for PR632, PR629 and PR630 were also read at their relevant interfaces. The proof distinguishes local etale root existence from a global root on the original curve and from global root uniqueness. No blocking mathematical defect found.
