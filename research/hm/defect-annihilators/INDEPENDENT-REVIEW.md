# Independent mathematical review

Verdict: conditional PASS on the pinned mathematical inputs. Reviewed proof SHA256: 4263cb7cc91446125f1980b53f0ada75262b7a5249f3fee7ce8fcbd7226f63b9. This is not formal proof-assistant verification.

## Checks

1. Over the polynomial ring on twenty independent matrix entries, maximal minors have grade nine and the classical generalized Eagon–Northcott complexes in the stated range resolve their zeroth homology. The source's generic-exactness theorem applies there, not to the five-variable specialization. Giving entries degree two changes grading, not exactness.
2. Each minor annihilates the generic zeroth homology: the adjugate identity kills the cokernel, hence each positive symmetric power, while the ordinary determinantal quotient is immediate. A lift of the zero module map on a free resolution is nullhomotopic. The displayed inductive construction has the correct indices and its final step uses injectivity of the final resolution differential. Homogeneous lifts have degree four.
3. Tensoring the homotopy identity preserves it without any flatness assumption. Thus all specialized homology is annihilated by the actual determinantal ideal, rather than only its radical. The accompanying Tor interpretation is legitimate because the universal complex is a free resolution over the twenty-variable ring.
4. Perfect evaluation between Q and its graded dual gives the orthogonal complement of J Q^vee as Ann_Q(J). The pinned Ann_S(J)=m^2 therefore identifies this image canonically with (S/m^2)^vee. After shift -15 the dimensions are five and one in degrees fourteen and fifteen. Its minimal generators, socle and annihilator follow from dualizing the elementary ring S/m^2.
5. The final optimal-annihilator corollary also follows: Q^vee is faithful over Q, so the annihilator of the top positive defect is exactly D. Since D kills every positive defect, the intersection of their annihilators is exactly D.
6. The common ideal-action kernel is R^vee(-15), while the quotient by it is J^vee(-15). These are ideal-generated image and common kernel, not the image and kernel of one linear operator. Their different lengths do not assert an invalid rank-nullity statement. Nonzero image rigorously excludes descent of this positive homology module to R.
7. For the self-dual middle module, balancedness shows both left and right orthogonal complements of J M equal 0:_M J. Square-zero J makes J M isotropic. Double orthogonality proves that the central quotient inherits a nondegenerate balanced pairing even without assuming symmetry or alternation. Every successive quotient is killed by J. The final term M itself need not be an R-module.
8. The Hilbert-function identity for the three layers follows from the dual outer layers. Support in degrees five through ten and the minimum degree three of J put J M in degrees eight through ten; m^2 J=0 gives m^2 J M=0. The reflected support and listed inequalities follow. No action rank or vanishing of J M is inferred.

## Clarification and evidence boundaries

The only requested correction was to state that the filtration's successive quotients are R-modules, rather than describe the entire filtration as being by R-modules. The mathematical argument already had the correct meaning. The final added optimal common-annihilator corollary was checked as described above.

The generic theorem was checked against Andrew R. Kustin, “Canonical complexes associated to a matrix,” introduction, especially the grade hypothesis following (1.0.2), and the cited classical construction: https://arxiv.org/abs/1509.04367 . The pinned excess-annihilator result was also checked. The remainder is elementary homotopy and finite-length duality.

No selected HM/source coefficients, numerical matrix ranks, coefficient search, or large computation were used. Fixed-source first-order vanishing, higher-order lifting, algebraicity, and exact middle-action ranks remain open.
