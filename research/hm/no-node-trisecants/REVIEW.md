# Independent review: no node trisecants and ample cubic polarization

Verdict: **PASS**. No mathematical correction is required within the stated scope and pinned inputs. This is an independent mathematical review, not formal proof-assistant verification.

## 1. Review scope and sources

I reviewed `PROOF.md` in full and checked its uses of the supplied local copies of the following immutable source proofs:

- PR587, commit `865ab24e91333688d7ae76303d7d594aae8521f8`, [eigenline-interpolation/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/865ab24e91333688d7ae76303d7d594aae8521f8/research/hm/eigenline-interpolation/PROOF.md), especially Sections 1 and 4.
- PR602, commit `13647efe962d87c3344729e28c2a5e9ceeb0f2ba`, [cubic-map-geometry/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/13647efe962d87c3344729e28c2a5e9ceeb0f2ba/research/hm/cubic-map-geometry/PROOF.md), Sections 1–7.

The review is relative to their explicitly pinned primary-surface, normalization, ideal-generation, and syzygy inputs. It does not replace those antecedent proofs with new instance computations. The new argument concerns abstract finite Heisenberg representations and its stated geometric consequences.

## 2. Character projectors and the exact overlap

All normalizations in the representation-theoretic argument are correct.

For a noncentral element, nondegeneracy of the commutator pairing gives a conjugation differing by a nonidentity central element. A nontrivial character of the prime-order center is faithful, so conjugacy invariance forces the trace to vanish. Central traces are exactly `p chi(z)`. Averaging a Hermitian form over the finite group legitimately makes the representation unitary without changing its eigenlines or their projective incidence.

Each inverse image `A_L` has order `p^2` and is abelian. Its characters extending the fixed central character number exactly `p`. The displayed average with denominator `p^2` is its orthogonal character projector. Only the `p` central elements contribute to its trace; each contributes `p`. Thus its trace, and hence its rank, is one. Distinct character spaces in a single `A_L` are orthogonal and supply the entire `p`-dimensional representation.

For different directions `L` and `K`, the condition `ab` central forces both `a` and `b` to be central, because their quotient classes lie in distinct lines and sum to zero. There are exactly `p^2` contributing pairs. Each summand in the product-projector trace is `p`, and the denominator is `p^4`, giving precisely `1/p`. No conjugation or missing character factor is concealed in this count: both extending characters agree with `chi` on the center, and `chi(ab)=chi(a)chi(b)` cancels the two inverse factors.

The trace of the product of two rank-one orthogonal projectors is the squared absolute inner product of unit spanning vectors. This proves the claimed uniform cross-basis absolute inner product `1/sqrt(p)` and also rules out a common eigenline between two directions.

## 3. Uniform triple independence

For three distinct eigenlines, every off-diagonal absolute inner product is at most `1/sqrt(p)`, including zero for vectors from the same basis. The lower bound on the squared norm is valid for arbitrary complex coefficients because each real cross term is bounded below by the negative product of absolute values.

Adding the three inequalities `2|a_i||a_j| <= |a_i|^2+|a_j|^2` gives

    sum_(i<j) |a_i||a_j| <= sum_i |a_i|^2.

Consequently the asserted lower bound is exactly

    (1-2/sqrt(p)) sum_i |a_i|^2.

Its coefficient is strictly positive for every prime `p>=5`. Thus every three distinct eigenlines are represented by linearly independent vectors. The proof covers all distributions among the eigenbases, with no exceptional case needing a selected incidence calculation. It makes no corresponding claim for `p=3`, where this strict estimate would not suffice.

## 4. Identification with the actual node support

The use of PR587 is exact, not a numerical cardinality analogy or a substitution of eigen-hyperplanes in the dual space. Its Section 1 fixes eigenlines in the actual ambient module, and its Section 4 proves that all thirty are singular points of the actual primary surface.

In that source argument, rank eight makes every nine-by-nine cofactor of a ten-by-ten defining minor vanish, so every such defining minor has zero first derivative. The scheme equality with the primary degeneracy scheme therefore gives the full ambient tangent space at each eigenline. Since the surface has dimension two, these are singular points. Their distinctness together with the independently established exact thirty-node singular locus identifies the two reduced supports. The target proof accurately invokes this chain.

Applying the universal triple result with `p=5` therefore excludes every line in the ambient `P4` containing three actual nodes, not merely those lines already known to lie on the surface.

## 5. Finiteness, normalization, and ampleness

PR602 supplies the exact contracted-curve classification for the ambient resolved cubic morphism and its surface restriction. Its proof excludes exceptional curves and establishes both directions of the characterization. The new no-trisecant conclusion consequently removes every contracted integral curve for both maps.

The subsequent finiteness argument is sound. A positive-dimensional projective fiber over a closed point contains an integral projective curve. Thus no such fiber exists. For these proper finite-type morphisms, upper semicontinuity of fiber dimension then rules out positive-dimensional fibers over other points as well. Zero-dimensional finite-type fibers are quasi-finite, and proper quasi-finite morphisms are finite. No reduced-fiber assertion is required.

Crucially, the surface birationality is a separate conclusion of PR602, not an automatic restriction of ambient birationality. The source proves it using the finite node-trisecant family, finiteness of the lines contained in the surface from positive geometric genus, and the resulting generic rank-four inverse on the surface. The present proof uses exactly that independently established conclusion.

The ambient point blowup is smooth and integral, and the smooth integral strict-transform surface is part of the pinned input. A finite birational map from either normal source to its integral reduced image is the normalization map. The affine integral-closure argument in Section 5 is correct: finiteness makes every element of the source algebra integral over the target algebra; conversely any element of the common function field integral over the target algebra is integral over the source algebra and hence belongs to it by normality.

Finally, each generated cubic line bundle is the pullback of the image's hyperplane bundle. Pullback of an ample line bundle by a finite morphism is ample, proving both ampleness claims. This avoids the invalid implication from strict nefness alone to ampleness. The intersection numbers and image degrees remain the previously proved `51` and `75`. The optional observation about an individual two-node secant is also correct: its generated restriction has degree one on `P1` and embeds that curve as a projective line.

## 6. Restrictions and remaining boundary

The new proof and this review require no selected actual HM/source coefficients, coordinate vectors, matrices, point evaluations, numerical rank tests, numerical searches, or large computation. The projector identities and norm estimate are universal symbolic statements, not evaluations of a selected Gram matrix.

The conclusions stop correctly at finite birational normalization maps and ample globally generated polarizations. They do not establish normality of either image, singleton or reduced special fibers, infinitesimal separation, very ampleness, embeddings, or extension of the quartic inverse. The full-adjoint, prescribed-source, higher-lifting, and original algebraicity questions remain untouched.

**Final verdict: PASS, with no required corrections.**
