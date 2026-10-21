# Independent review of the exact beta chart

Verdict: the proof and its stated universal consequences are correct.

Reviewed `BETA-LOCAL-MODEL.md`, SHA-256 `5dddf5bd946606b6b30b1059a1296ba0eeca9e216d53866de14bdb7b797307c3`.

## Exact coordinate change

The sign convention is consistent. For example omega1=b2 wedge b3 has contraction coefficients (0,-a3,a2), so its mixed coefficients after b is replaced by b+t c are (0,t3,-t2)=-K(t). Consequently b'=b-s1 c1-s2 c2 contributes exactly the skew matrices K(s_l), leaving the symmetric matrices S_l. Rewriting the symmetric mixed terms in the new coframe changes only the coefficient of c1 wedge c2. The corrected z' depends polynomially on the other coordinates and has coefficient one on z. The inverse reconstructs M_l=S_l+K(s_l) and then z, so this really is an affine polynomial automorphism, not a formal or first-order normalization.

## Incidence over arbitrary complex algebras

Contraction of the mixed term S_l(i,j)b'_j wedge c_l has B' coefficient -r_l S_l(i,j). Thus the displayed equation K(a)=r1 S1+r2 S2 is correct. Symmetric and skew matrices intersect trivially over every C-algebra because two is invertible. It follows exactly that a=0 and H r=0. The remaining coefficients give z'_i r1=z'_i r2=0. Since the vector is projective and a=0, the two standard radical charts have one r-coordinate invertible, yielding z'=0 scheme-theoretically. There is no cancellation by a nonunit and no reducedness assumption in this elimination.

The incidence therefore has the claimed product structure. Its image has precisely the rank-one-matrix support, and the independently proved primeness of that minor ideal identifies the reduced image scheme. This conclusion does not assert that the original wedge-minor scheme equals that reduced image.

## Ring and singularity checks

The elementary row/column-margin sorting argument proves that the kernel of h_(i,l) mapping to u_i v_l is exactly the two-by-two minor ideal. Distinct margin classes give distinct monomials after substitution, so grouping terms establishes the assertion for arbitrary polynomials, not only binomials. The image is exactly the torus-invariant subring. If an element of its fraction field is integral over the invariant ring, the same monic equation makes it integral over the ambient polynomial ring; normality of that polynomial ring puts it there, and invariance then puts it in the invariant subring. This proves normality without assuming normality of the determinantal ring.

A nonzero-entry pivot gives seven smooth parameters. At the zero matrix the minor ideal has no linear terms, so tangent dimension is twelve and local dimension is seven. After the six shear parameters are restored, the reduced net locus has dimension thirteen and tangent dimension eighteen at beta. The zero-matrix locus is exactly the beta-net locus in the chart: the net is the exterior square of the sheared three-space. Thus the local singular locus identification is exact.

## Global and derived consequences

The relative-Grassmannian description makes J smooth and irreducible of dimension thirteen. On the one-dimensional-radical locus, a four-by-four contraction pivot identifies the contraction rank-at-most-four scheme with the kernel-line incidence via its residual Schur column. Since this incidence open is smooth, its reduced support is X itself. The beta charts and this complementary open cover X, proving global normality and the stated singular locus.

The beta incidence is Hom(C^2/L,C^6), hence Tot(O_P1(-1)^6), with a P1 exceptional fiber. Product with the six free parameters gives exceptional dimension seven in dimension thirteen, so no exceptional divisor occurs. Properness follows from the closed incidence inside the product with P1, not from the vector-bundle projection.

For the structure-sheaf calculation, affine projection to P1 gives the direct sum of Sym^n(C^6*) tensor O(n). Its positive cohomology vanishes, and its global function algebra is the Segre rank-one cone algebra (the two-dimensional factor is identified after a harmless choice of bases). Since the target chart is affine and the contraction map is proper, the Leray calculation identifies those groups with global sections of the higher direct-image sheaves. Quasi-coherence on the affine target then gives their vanishing. The same computation after product with affine six-space, together with the isomorphism elsewhere, proves the global direct-image statement. Normality, smoothness of J, and this vanishing justify the rational-singularity conclusion for X.

Finally, every wedge minor has zero linearization at beta because the wedge map vanishes there. The tangent dimension of the unreduced wedge-minor scheme is therefore twenty-one, strictly exceeding the reduced tangent dimension eighteen. This proves nonreducedness at beta; it does not measure the nilradical length or imply square-zero structure.

## Scope

This is an independent exact mathematical audit, not formal proof-assistant verification. No selected HM/source coefficient, matrix, numerical rank, source membership, or large computation was evaluated. The universal reduced locus X, the original wedge-minor scheme D, and any actual-family pullback remain distinct. Neither normality nor rational singularities nor nonreducedness is transferred to an actual HM family by this review.
