# Independent whole-proof review: the positive rank-three endpoint image

## Verdict and bound artifact

PASS, conditional on the explicitly inherited actual geometric and source premises. I independently checked the proposed image theorem before reading the completed proof, then reviewed the whole completed proof, its published top-three predecessor, the actual-kernel capacity derivation, the orbit-divisor argument, and the applicable arbitrary-rank Gauss-transform facts. I found no mathematical correction needed for the stated conclusions.

Reviewed artifact: PROOF.md.

SHA256: 106268a3899b137baa0133e4e57c620a97c204ebe01e9b3803f20b5c14edba9b.

The conclusions are necessary actual-map structure at the maximum-degree-three boundary. They neither construct a configuration nor select a kernel form, determine the original rank-four determinant defect, or close the boundary or full profile.

## Independent arithmetic and source audit

The companion verify_independent.py does not import the author's character helper, verifier, result files, or any earlier checker. It reconstructs the nine fixed irreducible characters using exact Q(sqrt(5)) class values and the closed binomial symmetric-power trace formula. It checks character orthogonality, all relevant Hom spaces and the complete Sym10 decomposition. It reconstructs the scalar and negative source-row lists separately for each of the three prescribed K forms.

It also checks all six ordered two-column height choices of total eleven and all fourteen ordered three-column choices of total ten, the exact completed-square identities and unique integral optimizers, and all stated ranks, degrees and twists. These are two fixed universal capacity domains, not a search over hypothetical bundle candidates or actual coefficients.

All eleven retained full inputs are authenticated against their recorded byte counts, SHA256 hashes and Git blob identities. This is independent authentication of the retained copies, not a claim of a second network fetch or proof-assistant certification of their geometric premises.

The ordinary and optimized Python executions pass 458 explicit checks and return byte-identical JSON. The checks use explicit failures, not assertions disabled by optimization. INDEPENDENT-RESULT.json records the complete bounded capacity rows and source identities.

## 1. The actual V-row and its coherent rank

The near-top coefficient argument applies to the actual derivative and does not assume a horizontal Birkhoff splitting. A killed coefficient line O(-4) is a saturated line in K and the original constant ambient. Its derivative would lie in (K/O(-4))(-2), with top degree at most -5, so it is zero by degree. Horizontalness would make this negative saturated line constant in characteristic zero, a contradiction.

The V-row is therefore nonzero. Its O component vanishes by Hom_G(V,Sym4 W)=0, and its O(-10) component vanishes by degree. Thus it lands in W O(1).

If its coherent image had rank one, that torsion-free image on the smooth parameter curve would itself be a line bundle. It is a quotient of V O(-4), so twisting by four makes it generated and gives degree at least -4. Its inclusion into W O(1) gives degree at most 1. Equivariance gives the standard linearization up to a one-dimensional character, which is trivial because G is perfect. Every degree in this interval would require V in Sym0 through Sym5 W, where it does not occur. This excludes rank one without ever replacing the image by its saturation.

## 2. Why the rank-two V-row is everywhere onto

The three maximal minors of the generic-rank-two V-row have ordinary degree ten. The zero scheme where they all vanish is the rank-drop scheme of an equivariant map, hence G-invariant. Equivalently, changing equivariant frames mixes the minors by invertible changes and units, preserving the minimum vanishing order at each point. Thus their common zero divisor is invariant, even though no individual minor must itself be invariant.

At least one minor is nonzero, so the common divisor has degree at most ten. Every nonempty invariant effective divisor has degree at least twelve on the physical A5 line. Its common divisor is therefore zero. On a smooth curve the minors then generate the unit ideal locally, so the map has full rank everywhere and is onto W O(1) as a sheaf.

This justifies the crucial upgrade from generic rank to actual coherent-image equality. It does not amount to silently saturating an image or ignoring exceptional parameters.

## 3. Completeness and global behavior of the scalar rows

The full scalar-source list is correct:

- In K_T, only S4 O(-3) and T6 O(-5) can map equivariantly to O.
- In K_W, only S4 O(-3) and W' O(-7) can map equivariantly to O.
- In K_1, only S4 O(-3) and D O(-4) can map equivariantly to O.

The V and P degree-minus-four blocks cannot contribute because Sym4 W=D. The tail O(-10) cannot contribute because Sym10 W=A_std+D+V contains no invariant. Every possible nonzero scalar row has homogeneous degree at most seven. Its base divisor is invariant and has degree below twelve, so any such nonzero row is onto O everywhere. Consequently a nonzero whole scalar projection is onto everywhere as well.

The negative projection can come only from the unique O(-10) summand of K_1, through a constant scalar. There are no negative projection rows in the other two types. A nonzero negative projection is therefore also everywhere onto.

If both projections were nonzero, the V block supplies two independent W O(1) directions. The scalar row supplies an additional direction on the complement of the negative tail, on which the negative projection is zero. The tail supplies a fourth direction with nonzero negative coordinate. This contradicts the endpoint rank bound of three. Possible upper components of the tail do not affect this independence argument.

The three remaining image alternatives are exhaustive. Their global coherent-image equalities follow by first lifting the scalar coordinate locally and then correcting its W component using the already-surjective V-row. This is stronger than a generic direct-sum argument and is sufficient to compute the following kernel degrees exactly.

## 4. Capacity is applied only to actual negative kernels

For either excluded alternative, start with F0=K, F1=K^- and thereafter Fj+1=Fj^- in the same original constant ambient. Derivative kernels remain saturated there. Every nonzero stage is negative, so no nonzero stage is horizontal. The ranks strictly decrease and the chain terminates.

Writing C=K/K^-, the actual successive quotients Gj=Fj/Fj+1 inject coherently into C(-2j). Their ranks are positive and nonincreasing, bounded by rank C. Their sum is rank K^-, and their degrees sum to deg K^-. Exterior powers give the ordinary degree bounds, with no need for saturated images in C(-2j). Summing produces the stated ordered-height capacity.

For C=W O(1), K^- has rank eleven and degree -56. The capacity is

    -h1^2-h2^2 = -121/2 - 2(h1-11/2)^2,

with h1+h2=11 and h1>=h2>=0. Its integral maximum is -61, uniquely at (6,5), contradicting -56.

For C=W O(1)+O(-10), K^- has rank ten and degree -46. With z=h3 and h1+h2=10-z, its capacity is exactly

    -50-z-(3/2)z^2-(h1-h2)^2/2.

This is at most -50 for every allowed three-column height, with equality only at (5,5,0). The degree -46 is impossible. In particular this exclusion does not omit positive third-height possibilities or improperly truncate to two columns.

These arguments operate on K^- and its actual descendants, not on the ordinary quotient K/S4 O(-3), and require no descended flat connection on that quotient.

## 5. The positive image, kernel, and actual forward transform

The only remaining alternative is the full coherent image W O(1)+O, everywhere. The exact quotient gives rank K^-=10 and degree -56. Since the image is a saturated subbundle of A_q(-2), its twist by two is precisely K^+/K=W O(3)+O(2), not merely its generic fiber.

The preimage of that subbundle in E is the kernel of the actual O(-8) quotient coordinate. All other source blocks have zero Hom to O(-8), and the displayed source O(-8) has a nonzero scalar component because the quotient is onto. Its kernel is therefore exactly the displayed E0, even if the source tail also has upper components. E0 has rank sixteen and degree -46 and is saturated in the original ambient.

The derivative of E0 kills K because K^+=E0. Its projection to Q(-2) is beta_E restricted to E0, whose sheaf kernel is K. Thus the derivative kernel of E0 is exactly K and its generic rank is three. Both inclusions in this kernel argument are actual sheaf inclusions; no numerical kernel comparison is substituted for them.

## 6. Scope of the unramified conclusion

The adjacent graded derivative

    K/K^- -> (E0/K)(-2)

is the image isomorphism already proved, so this particular rank-three step has zero determinant defect. The proof correctly calls beta_E0 only generically rank three: it does not claim that the next derivative is everywhere full rank or that the original rank-four determinant defect vanishes.

No separate rank-three theorem with incompatible central rank or degree is imported. All three K forms remain unresolved necessary alternatives. No actual source coefficients, parameters, points, jets, tensors, instance matrices or ranks were chosen or computed, and no public write was performed during this review.
