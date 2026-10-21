# Independent audit of exact eigenline postulation

Reviewed 2026-10-21. Mathematical verdict: **PASS**. The Section 6 scope correction recorded below has been made and verified. This is an independent symbolic audit, not formal verification. No evaluation matrix, numerical rank calculation, selected HM/source coefficient test, or public write was used.

## Universal hypothesis and character argument

The stated nontrivial-central-character irreducible five-dimensional Heisenberg hypothesis is necessary and correctly retained. A Schrödinger basis transports the intrinsic configuration to the thirty stated points; change of basis does not change any restriction dimension or regularity conclusion.

Restriction of a monomial to a normalized chirp gives exactly the character with index (sum of squared indices, sum of indices). The two root-of-unity sums prove independence of all twenty-five characters. Linear monomials have distinct such indices. For a quadratic, its sum S and squared sum Q determine its product (S²-Q)/2 and hence its unordered pair of indices, including multiplicity. All fifteen quadratic characters are therefore distinct. These facts prove the Hilbert values 1,5,15 in degrees zero through two without an evaluation-rank computation.

The displayed seven cubic triples and their squared sums are correct. Translation by t changes their character index by the formula stated, which supplies all twenty-five characters. For a collision with a pure cube, translation to its index zero gives u+v+w=u²+v²+w²=0. Eliminating w and dividing by 2 gives u²+uv+v²=0. If v is nonzero, its discriminant is 2, which is not a square in F5; otherwise u is immediately zero. Thus the pure cube is the only monomial with its character. This argument avoids any unproved assertion that the seven displayed triples exhaust the S=0 triples.

Consequently vanishing on the chirps forces all five pure-cube coefficients to vanish, hence forces vanishing at the five coordinate points. The cubic restriction kernels are identical, so the exact full-support image dimension is 25 and the cubic ideal dimension is 35-25=10.

## Explicit image equations

Fourier extraction of the coefficient of character (3i²,3i) uses the factor zeta^(-3ai²-3bi)/25, as written. Its value is exactly the coefficient of x_i³ and thus P(e_i). This proves necessity of all five equations (1). Chirp surjectivity proves sufficiency. Each equation has a distinct coordinate value c_i with coefficient one, proving independence. The equations exactly describe a codimension-five subspace; they are not merely an incomplete collection of relations.

## Quartics, Hilbert series, and regularity

The quartic separators vanish on all chirps because the sum of all indices and the sum of their squares vanish modulo five. They restrict to the five coordinate delta functions. The x_0 multiplier preserves normalized chirp values, and the five separators correct the coordinate values independently. This reestablishes full degree-four interpolation. Multiplication by a linear form avoiding the finite support proves stabilization in every later degree.

It follows that the precise Hilbert function is (1,5,15,25,30,30,...), with first differences (1,4,10,10,5). The homogeneous ring injects into the product of the coordinate rings of its reduced points; a linear form nonzero at each point is therefore a nonzerodivisor. This justifies the asserted Artinian-reduction interpretation and Hilbert series, not merely the formal difference calculation.

The ideal-sheaf exact sequence gives h¹(I_Omega(3))=5 and H¹(I_Omega(k))=0 for k>=4. For 5-regularity the other required groups are H²(I_Omega(3)), H³(I_Omega(2)), and H⁴(I_Omega(1)); all agree with the stated ambient line-bundle cohomology and vanish. Nonvanishing of H¹(I_Omega(3)) excludes 4-regularity, and regularity propagation excludes every smaller integer. Thus the exact ideal-sheaf regularity is five.

The claimed generation of the saturated homogeneous ideal in degrees at most five is a valid consequence: regularity gives multiplication surjectivity in degrees n>=5, and saturation identifies the graded ideal pieces with H⁰(I_Omega(n)). No claim of a necessary minimal quintic generator or a specified resolution is made. These are point-ideal statements, not surface-ideal statements.

## One-section conductor consequence and its limit

The extra quadratic normalization-section hypothesis is expressly conditional and correctly requires its branch difference to be nonzero at every node. A branch-difference vector that is merely nonzero globally would not suffice. O_S-linearity then identifies the single-section product image with an invertibly rescaled ambient cubic restriction image. Its dimension is exactly 25. Dividing each output coordinate by the corresponding nonzero difference coordinate transports equations (1) to equations (2), with all twists accounted for by compatible fiber trivializations.

These five equations constrain only the indicated product subspace, not arbitrary degree-five normalization sections. The general degree-m statement follows in exactly the same way. Quartic multipliers are therefore the sharp threshold for full interpolation by this one fixed nowhere-zero section.

### Scope correction requested during review

The initial draft said that the full actual rho_5 image “may equal all thirty fibers.” This is not justified and conflicts with the already pinned PR578 input: its Section 3 explicitly records 1<=h¹(O_S(5)), so in that actual geometry r_5<=29. The accurate statement is that the full image can be larger than the single-section subspace and this calculation does not determine its exact dimension. Conditional on the quadratic-section hypothesis and retaining PR578's lower-defect bound, the combined bounds are 25<=r_5<=29.

This correction concerns the scope of a possible-value sentence, not the new interpolation proof or any displayed symbolic formula. The corrected file has been reread: it no longer allows full rank thirty, and explicitly preserves the other primary-geometry constraints. No exact r_5 is established here.

## Dependencies and verification limits

This reviewer previously read the immutable PR553, PR554, PR573, and PR578 source files directly during the independent audit of the universal eigenline interpolation proof; their exact commits and file blobs are recorded in that review. The present exact postulation theorem is reproved symbolically in the new file and needs no further actual-geometry input. No repository publication or coordination assertion is part of this mathematical certification.

The verified new conclusions are the exact Hilbert function, the five cubic-image equations, the Hilbert series/h-vector, exact regularity five of I_Omega, and the sharp dimension-25 limitation of the specified one-section cubic multiplication construction. No ambient projective-normality or exact full degree-five conductor-rank assertion follows.

## Final addendum: strengthened actual-primary conclusions

The final additions to Sections 6 and 7 were reread and audited after the preceding review. **Final verdict remains PASS**, now including the actual-primary sharp stabilization and exact structure-sheaf regularity assertions.

The quadratic conductor-generation proof was read directly through the read-only repository connector at commit 7547a6a0d84d29478a0bad2d30bda271c37c269e, path research/hm/quadratic-conductor-generation/PROOF.md, returned blob e48254444b55f816d5ee1e08315ddee11f8c17bb. Its Sections 2–3 explicitly establish nonzero projection of im(rho_2) onto every node fiber; its Section 5 establishes 7-regularity of O_S. These are the exact inputs cited by the final additions, not an identification inferred from matching numerical invariants. The separate quadratic-generation theorem is treated as a pinned, independently reviewed input, rather than being made a consequence of the present point-configuration proof.

Finite hyperplane avoidance applied to its nonzero coordinate functionals yields a single quadratic section with nowhere-zero branch difference. The already audited product-image calculation then supplies r_5>=25. The independently checked PR578 lower bound h¹(O_S(5))>=1 and normalization cohomology identity supply r_5<=29. Thus both displayed inequalities 25<=r_5<=29 and 1<=h¹(O_S(5))<=5 are valid.

PR578's strict-growth lemma applies at n=5, giving r_6>r_5 and hence r_6>=26. Its nontrivial-central-character divisibility applies at n=6, and the target dimension is thirty; the only possible multiple of five is therefore r_6=30. Fullness propagates to all later degrees by multiplication by a linear form avoiding the support. The same propagation shows that fullness in any earlier degree would contradict r_5<30. Consequently degree six is indeed the exact first degree of full conductor surjectivity, while the exact value of r_5 remains undetermined.

For O_S, the pinned 7-regularity gives the upper bound. The nonzero H¹(O_S(5)) violates the i=1 condition for 6-regularity. Regularity propagation rules out every lower index. Therefore the exact Castelnuovo-Mumford regularity of O_S is seven. This is explicitly different from the exact regularity five of I_Omega proved here; it gives no corresponding exact regularity of I_S or ambient projective-normality conclusion.

All final strengthened conclusions are thus certified relative to their stated immutable geometric dependencies. No additional evaluation, numerical rank test, or public write was used.
