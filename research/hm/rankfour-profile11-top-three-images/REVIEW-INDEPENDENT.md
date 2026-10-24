# Independent whole-proof review: matched Euler images and the two-value defect bound

## Verdict and artifact

PASS, conditional on the explicitly inherited actual geometric and source premises. I read the complete proof and the preceding low-top and top-three proofs, checked the actual-connection steps independently, and independently reconstructed the fixed character and degree calculations. No flaw or missing case was found in the stated conclusions.

Reviewed artifact: PROOF.md.

SHA256: 8cab9ce788af9929a3c314718ccb1e5f29a49f227889466bfb31d5070c2255f1.

The conclusion is conditional necessary actual-map structure at maximum quotient degree three. It is not an occurrence theorem, does not eliminate the three surviving K forms, and does not close this boundary or the full rank-four profile.

## Evidence and independent verification

The retained inputs include the original actual inclusion, ambient convention, strict-top lemma, four-source theorem, double-channel theorem, capacity argument, arbitrary-rank plateau theorem, physical character reference, preceding low-top and top-three theorems, and the invariant-orbit divisor argument. I authenticated all eleven retained full files against the recorded byte length, SHA256 and Git blob identities. The author performed the fresh immutable-source fetches; this review independently authenticates the retained bytes rather than claiming a second network fetch. The older files retain the identities already inspected in the previous packets.

The independent script does not import the author's characters.py, verify.py, result files, or any earlier checker. It uses exact Q(sqrt(5)) class characters, a closed binomial symmetric-power trace formula, and class inner products. It checks all nine irreducible character orthogonality relations, the relevant Hom dimensions, universal rank/degree identities, all twelve ordered height triples of sum nine, the completed square, both capacity maximizers, the invariant defect values, and the immutable-input identities. Ordinary and optimized Python runs return identical JSON and pass 267 explicit checks. Optimization cannot disable the checks.

The computational checks are not proof-assistant certification of the source geometry. The sheaf and actual-connection arguments are reviewed below.

## 1. Source cancellation and the canonical top subbundle

The original O(-8) quotient coordinate can receive a map only from the displayed source O(-8). Its scalar coefficient is nonzero because the full quotient is surjective. For a vector in the kernel this forces its O(-8) source coordinate to vanish, even if that source line has nonzero upper components. Therefore K really lies in F+M, and restriction to F+M surjects onto P_plus. This is cancellation of an actual quotient, not a choice of horizontal splitting.

The top subbundle U=H0(K(3)) O(-3) is canonical because K has no degree above -3 and its degree-minus-three coefficient is exactly S4. Its maps into M vanish: equal-degree maps to W' and T6 vanish by inequivalence, and maps to the lower-degree terms vanish by degree. Its only component is the nonzero map to D O(-2). The identity W tensor D=S4+T6 makes that Hom one-dimensional. Thus the image is the standard quartic evaluation kernel, with quotient O(2), not merely a generically equivalent subspace.

Since the actual quotient kills U, its F-row factors through O(2). If this row vanished, F would be contained in K; that contradicts the strict-top bound H0(K(2))=0. Both components of the nonzero factor j have one-dimensional Hom spaces. The first is the Euler injection and the second a scalar.

For nonzero scalar component the written target automorphism splits off j. For zero scalar component the Euler quotient is O(4), leaving the independent O(2) summand. These prove saturation in both cases and exactly the two claimed R types. Quotienting by U and the saturated j identifies K/U with the actual kernel in M. The projection-to-M argument is an isomorphism of sheaves because j is an everywhere-injective subbundle map; it is not merely generic elimination.

## 2. Matching the two actual images

The crucial matching statement is valid, and I independently found the same degree argument before comparing it with the completed proof.

Since U is contained in E^-, the actual derivative of U lies in E modulo U. Projecting it further modulo F gives an O-linear map U to (E/F)(-2). The target has top degree at most -5 and the source is pure degree -3, so the map vanishes as an ordinary bundle map. Thus the derivative lies in (F/U)(-2)=O.

This factor cannot be zero. U is saturated in the original constant ambient through its locally free successive quotients in E. If its entire second fundamental form vanished, it would be a horizontal saturated negative subbundle. In characteristic zero its Grassmannian map would be constant, contradicting its negative degree.

The one-dimensional Hom from S4 O(-3) to O consists of multiples of cubic evaluation. Hence the factor is a nonzero scalar multiple of that surjective evaluation. Projection from E/U to E/K is exactly the original j on F/U, so the restriction of beta_K is j(-2) composed with cubic evaluation. In particular its two coefficients are not independent of the original quotient-row coefficients. No differentiation of an arbitrarily chosen abstract splitting has been substituted for the actual connection.

The actual image is saturated because cubic evaluation is surjective and j is a subbundle inclusion. Its actual kernel is A_std O(-4), the standard cubic evaluation kernel. It is also U^- for the original constant connection, because the earlier factorization was a factorization of beta_U itself.

## 3. The quotient map and the exact kernel sequence

Quotienting the actual beta_K by U in its source and its saturated image I in its target gives the O-linear map gamma. Since I has rank one and is the full image of the restriction to U, generic ranks give rank gamma=rank beta_K-1. The endpoint rank bound therefore gives rank gamma at most two.

The snake argument has no hidden surjectivity problem: a local section of ker gamma has a local lift to K whose derivative lies in I; the surjection U to I supplies a local cancelling lift. Thus K^- maps onto ker gamma as a sheaf. Its kernel is exactly A_std O(-4). This proves the displayed exact sequence, not only an equality after passing to the function field.

The proof correctly avoids treating gamma as a Gauss derivative for a flat connection on N. Nothing in the quotient construction grants such a connection, and no horizontal-negativity or endpoint-capacity argument is improperly applied to N. For the first two tails the O(-10) component vanishes by degree; in the third only the O(-10) tail can supply it. The proof does not silently discard that last possible component.

## 4. The universal V-row rank obstruction

Every surviving K has a V O(-4) direct block. The preceding near-top lemma applies to its actual derivative: a killed coefficient line would be a saturated O(-4) in K whose derivative lands in a bundle of top degree at most -5, forcing it to be horizontal. Therefore this V row is nonzero.

Its scalar O component vanishes because V is absent from Sym4 W=D, and its O(-10) component vanishes by degree. Thus it maps to W O(1). If its coherent image had rank one, that image would be an equivariant line bundle because a torsion-free sheaf on the smooth curve is locally free. It is a quotient of V O(-4), so twisting by four makes it generated and gives degree at least -4. Its injection into W O(1) gives degree at most 1. The group has no nontrivial one-dimensional character; each possible map is consequently controlled by V in Sym^(d+4) W. None of degrees zero through five contains V. This excludes rank one and proves rank two.

The endpoint upper bound is three, so the actual endpoint derivative has rank two or three. When j has nonzero scalar component, its top image I has a nonzero scalar O coordinate and is independent of the generic W O(1) image of the V row. The rank is then exactly three. This is an all-row structural statement, not an instance-rank calculation.

## 5. The defect bound and its sharp capacity value

The quotient A_q has degree zero. Thus the original determinant identity gives deg B=-8-t and deg L=-46+t, retaining the original nonnegative defect. The actual injection B to A_q*(-2) has ordered target degrees 6,-4,-5,-5.

The componentwise bound on the ordered B degrees is justified: if the j-th B degree exceeded the j-th target degree, the first j source summands would have zero maps into the last 5-j target summands. They would map into a rank j-1 target, contradicting generic injectivity. Saturation of B's image is unnecessary.

The inherited three-column capacity applies to the actual dual endpoint L, which has rank nine, derivative rank at most three, and lies in the negative actual S. Substituting the componentwise target bounds gives the stated quadratic. With h2=y and h3=z it is

    -53/2 - 2[(y-3/2)^2+(z-1)^2+(y-3/2)(z-1)].

The bracket is nonnegative, since twice it is the sum of the three squares (y-3/2)^2, (z-1)^2 and (y+z-5/2)^2. The continuous optimum is -53/2 at (h1,h2,h3)=(13/2,3/2,1), satisfying the ordering constraints. The integer maximum is -27 and is attained exactly at (6,2,1) and (7,1,1). Therefore -46+t<=-27, giving t<=19 with the correct sign.

## 6. Orbit support and the cokernel at defect twelve

The projective A5 action has orbit sizes 12,20,30,60, with one exceptional orbit of each of the first three sizes. The retained original orbit argument applies to any equal-rank equivariant determinant map, not only the rank-two applications later in that source. The determinant of the actual B injection is such a map, so its zero divisor is invariant. The degree bound 19 leaves only 0 and 12 in the orbit semigroup.

For defect zero the equal-rank injection is an isomorphism. For defect twelve invariance forces the unique reduced 12-point orbit, with multiplicity one at every point. Local Smith normal form has total valuation one, so exactly one elementary divisor has valuation one and the remaining ones have valuation zero. The cokernel is therefore one-dimensional over the residue field at each point. It is an invertible module on the reduced orbit with its induced equivariant structure. The proof appropriately does not call its stabilizer characters trivial.

## Verification boundary

No substantive correction is needed for the reviewed proof. No public write was performed. No actual HM coefficients, points, parameter values, jets, tensors, instance matrices or rank scans were selected.

