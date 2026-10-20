# Rank-at-most-three middle locus is at most a curve; affine independent-zero bound seven

## Hypotheses and dependencies

Work over C in the established equivariant trilinear setup: dim V=5, dim J=20; f:V^3 -> J is outer symmetric and cyclic-zero; every repeated-input map A_a:V/Ca -> J is injective. Retain the full standard normalizer N=H5 semidirect SL2(F5), irreducibility of V and J, and all bundle hypotheses used in ../quintic-normalizer-exclusion/COROLLARY.md and ../rank-ten-fitting-strata/ADDENDUM.md. In particular the following established consequences are used, not derived from the abstract tensor identities alone:

1. Generic residual rank is ten, the image bundle G has rank fourteen, and there are exact sequences

       0 -> O(-3) -> O(-1)^15 -> G -> 0,
       0 -> G -> O^20 -> R -> 0,

   with R torsion-free of rank six.
2. The residual map Q has source rank ten and target rank sixteen, after removing the repeated-input rank-four subbundle.
3. The total residual rank-drop support Z={rank Q<=9} has dimension at most two (hypothesis (H), obtained in the cited normalizer corollary).
4. For S=Ext^1(R,O), its effective codimension-two cycle has total degree delta<=70.
5. H5-equivariant proper-support sheaves satisfy the established Hilbert-coefficient divisibility theorem of ../heisenberg-defect-hilbert-congruence/PROOF.md.

The geometric exclusion in ./PROOF.md is used together with ../rank-one-middle-quintic-reduction/SECTIONAL_GENUS.md and its independent PASS audit SECTIONAL_GENUS_INDEPENDENT_AUDIT.md. Thus an arbitrary integral N-invariant degree-five surface in P4 is impossible; no normality assumption is imposed.

The conclusions below remain conditional on the stated source/equivariance/bundle inputs. This file does not independently re-prove that the source operation satisfies them.

## 1. Eliminate all rank-at-most-three surface components

Let W be the reduced union of two-dimensional irreducible components of Z_3={rank Q<=3}. It is N-stable. Suppose W is nonempty.

At the generic point of each component, let r<=3 be the residual rank and j=10-r>=7. The local-duality calculation and rank-six generator budget proved in ../rank-one-middle-quintic-reduction/PROOF.md, Section 1, apply to every residual rank, and give singularity-cycle multiplicity

    lambda >= max(j,2j-6) >= 8.

Consequently

    8 deg W <= delta <= 70,

so deg W<=8. H5-equivariance of O_W and the proper-support divisibility theorem imply 5 divides deg W, whence deg W=5.

For each H5-orbit of irreducible components, its reduced orbit-union is H5-invariant and its positive degree is divisible by five. Since their total degree is five, there is exactly one such orbit. The center acts trivially projectively, so its size is 1, 5, or 25. Size 25 is impossible by degree. Size 5 forces all five components to be planes. The transitive action of A=H5/Z(H5)=F5^2 on five planes has kernel a one-dimensional subspace of A. Because the plane set is N-stable, this kernel is preserved by the standard SL2(F5) action. That representation has no invariant line, a contradiction.

Thus W is an integral invariant quintic, excluded by the cited geometry. There is no surface component of Z_3. Since Z_3 is closed and lies in Z of dimension at most two, this proves

    dim { [u] in P(V) : rank Q_u <=3 } <=1.             (1)

The empty case is included. This stronger conclusion does not assert that this locus is finite or empty.

## 2. Pointwise fiber bounds and the global affine bound

For independent zero triples, exact outer reconstruction identifies the separately projectivized fiber over [u] with the compatible ordered rank-two locus for K_u=ker Q_u, without additional lift parameters. The following previously established bounds are used:

- Residual rank zero is impossible: ../rank-one-boundary-support/PROOF.md, Section 7 (the top Chern class of Q(2) on P3 is 15h^3).
- Residual rank one has projective fiber dimension at most three: ../rank-one-residual-fiber-model/PROOF.md, Section 1.
- Residual rank two has projective fiber dimension at most two: ../diagonal-hartogs-fiber-bound/UNSQUARED_PENCIL.md, Section 5, including all pencil cases.
- Residual rank three has projective fiber dimension at most two: ../diagonal-hartogs-fiber-bound/PROOF.md.
- Residual rank four has projective fiber dimension at most two: ../rank-four-compatible-fiber-bound/PROOF.md.
- Residual rank five has projective fiber dimension at most two: ../full-support-rank-five-dimension-bound/PROOF.md, including its Section 6 for ternary support.
- Residual ranks at least six contribute affine independent-zero dimension at most six: ../rank-six-surface-reduction/COROLLARY.md.
- The full-support rank-five stratum contributes affine dimension at most six: ../full-support-rank-five-dimension-bound/PROOF.md.

Restoring three independent nonzero input scalings adds exactly three dimensions. Applying the fiber-dimension theorem and (1) gives:

    residual rank one:   affine dimension <=1+3+3=7;
    residual ranks 2,3:  affine dimension <=1+2+3=6;
    residual ranks 4,5:  affine dimension <=2+2+3=7.

Together with the rank-at-least-six bound, every independent-zero component has affine dimension at most seven. These are dimensions of reduced supports; no assertion about tangent-space dimensions or nilpotent thickening is made.

## 3. Exact remaining possibilities for dimension seven

Let T be an irreducible affine independent-zero component of dimension seven. On a dense open subset its residual rank is constant, and where necessary the support dimension of K_u is constant. The preceding bounds leave exactly the following necessary alternatives:

1. Generic residual rank one; the projective middle image is a curve; the generic separately projectivized fiber has dimension three.
2. Generic residual rank four; the projective middle image is a surface; the generic separately projectivized fiber has dimension two.
3. Generic residual rank five with three-dimensional tensor support of K_u; the projective middle image is a surface; the generic separately projectivized fiber has dimension two.

For case 3, rank-five full support is excluded by its stronger affine bound six; support at most two is impossible because dim K_u=5 exceeds dim Sym^2(C^2)=3. Thus the remaining support is exactly three-dimensional.

The dimensions of the middle images and fibers follow by equality in the respective sums. Generic fibers refer to the component T, so no irreducibility of an entire ambient fiber is assumed. Special lower-rank boundary strata cannot enlarge the dimension of T beyond its dense open part.

These are necessary cases, not existence results. No sharpness of the affine bound seven is claimed. This does not complete the broader main proof or exclude dimension seven. All inputs zero or non-independent triples are outside the independent-zero statement and require their separately established treatment.  No actual source-instance evaluation is claimed.
