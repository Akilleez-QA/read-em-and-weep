# Independent audit: smooth-quadric kernel involution constraints

## Verdict

**PASS.** The necessary numerical profiles, exact pencil-base-point counts, and at-most-four-blowup conclusion in `PROOF.md` are correct under its stated inherited ordered-factor hypotheses. No missing infinitely near base points or invalid graph-intersection identification were found. The additional ruling-base obstruction in Section 6 also checks out. This is a necessary-condition reduction, not an existence classification or an exclusion of all nonlinear profiles.

Audit performed on 19 October 2026. I read the proof and checked the hypotheses in `../nonplanar-factor-degree-bounds/PROOF.md` and the stated application of `../nonplanar-linear-correspondence-exclusion/PROOF.md`. 

## 1. Kernel degree along a general ruling line

The rank-at-most-two locus is a proper closed subset of the smooth surface Q. A general member of either ruling therefore has generic matrix rank three. Selecting three rows independent over the function field of that line gives four signed cubic minors, not all zero. They generate the kernel of that three-row matrix, and on the dense rank-three locus they generate the kernel of the full matrix as well.

After dividing by the homogeneous gcd, the minors are homogeneous forms of a common degree d ≤ 3 without a common zero on P¹. Consequently the induced morphism to P³ has pullback O(d). This is its parametrized degree, irrespective of whether its image is a line, conic, or cubic or whether the parametrization is multiple-to-one.

Each coordinate pencil, after fixed divisors are removed, has only finitely many proper base points. A general ruling member avoids both sets. Avoiding those proper points also avoids all infinitely near base-point clusters lying above them. Restricting the two pencils and taking Segre products gives a base-point-free presentation of the same map, with pullback degree r+t or s+u. Thus both sums are ≤ 3. Rank drops at isolated points on the chosen line cause no problem: the gcd-removed minors describe the unique extension of the same rational map to P¹.

## 2. Graph symmetry and the diagonal entries of the bidegree matrix

On the graph, transposition exchanges the classes from the two Q factors. It therefore identifies the intersection numbers p*A · q*B and p*B · q*A. On a resolution these equal u and r, respectively, because A²=B²=0 and A·B=1. Hence u=r.

An involutive lift on the chosen resolution is not needed. The equality is an equality of intersection numbers on the symmetric graph, and is preserved on any dominating smooth resolution. In particular graph symmetry does not require s=t; the proof correctly makes no such assertion.

## 3. Pencil identities and infinitely near multiplicities

A succession of point blowups resolving both pencils makes q=(f,g) a morphism. It is birational because the original rational map is birational. For a general fiber of either projection on the target, the fiber avoids the finitely many images of q-exceptional curves. Its total pullback is then a smooth rational curve, with self-intersection zero and canonical intersection −2. Also q*A · q*B=1 by the degree-one projection formula.

With total-transform exceptional classes E_i, the intersection matrix is diagonal with E_i²=−1 even when some blowup centers are infinitely near. The canonical formula is K_S=p*K_Q+ΣE_i. Thus the five displayed identities (*) follow exactly as written. Using prime exceptional curves instead would change the intersection matrix; the proof explicitly avoids that mistake.

The coefficients a_i and b_i are the nonnegative multiplicities of the moving pencils at successive centers after earlier fixed exceptional factors have been removed. They are not multiplicities against prime exceptional curves in the final model. This interpretation applies to satellite as well as free infinitely near points. Any proximity restrictions can only further restrict realizability; ignoring them cannot invalidate these necessary identities.

## 4. Why resolving the other pencil creates no omitted base points

This is the potentially delicate point, and it is sound. Locally, a resolved pencil is represented by two sections with no simultaneous zero. Under any subsequent blowup their pullbacks still have no simultaneous zero: at a point over x, a section nonzero at x remains nonzero after pullback in the pulled-back line-bundle trivialization. Thus a blowup made for the other pencil does not introduce a new base point into a pencil already resolved.

More generally, at a center which is not a base point of a particular pencil, that pencil's exceptional multiplicity is zero. Further base points cannot suddenly appear above that center for that pencil. At an actual base point, dividing the pullback pair by its common exceptional factor produces the next moving pencil, whose further base points are precisely the usual infinitely near base points and are included among later indices.

One may construct the simultaneous resolution by repeatedly blowing up a current base point of at least one pencil. Each center then has (a_i,b_i) ≠ (0,0), and the process terminates by resolution of surface pencils. There is no need to blow up additional centers merely to make q a morphism after both coordinate maps are morphisms. Hence the number of these centers is exactly the cardinality of the union of the two positive-multiplicity supports. Arbitrary extra resolution blowups can instead be recorded with both coefficients zero and omitted when asserting an upper bound.

This establishes that the counts in the proof include all required successive infinitely near points and genuinely bound the number of blowups resolving τ, not merely the number of its proper indeterminacy points.

## 5. Integer profiles and exact counts

- r=0: the square sums vanish; the linear sums force s=t=1. There are no base points.
- r≥1: the two degree bounds imply r≤3. If s=0 or t=0, the corresponding square and linear sums force r=1. Thus r=3 is impossible, and r=2 forces s=t=1.
- r=1: equality of each square sum and linear sum forces every multiplicity to be 0 or 1. The support sizes are 2s and 2t. The mixed sum is st, exactly the size of their common support. Their union therefore has N=2s+2t−st points.

For completeness, the possible N values, with t=0,1,2 listed in order, are:

- s=0: 0, 2, 4;
- s=1: 2, 3, 4;
- s=2: 4, 4, 4.

- r=2,s=t=1: both square and linear sums are four, so each support consists of four simple points. The mixed sum is four, forcing the supports to coincide.

There are eleven necessary numerical profiles before applying the compatible square-avoiding linear-correspondence exclusion: nine r=1 profiles, one r=0 profile, and one r=2 profile. Exactly two of these have no base points. Their pencils define automorphisms of Q, so they preserve O(1,1) and extend to projectivities of P³. Excluding these two leaves nine profiles, exactly as claimed.

## 6. Additional ruling-base obstruction

The inherited ordered-factor hypotheses give aτ(a)∈K and ensure τ is nonidentity by the generic rank-two product condition. If τ fixes the first ruling base, its restriction to the generic P¹ fiber is a nonidentity involution in PGL₂ of the base function field. On a general complex fiber, it has two distinct opposite eigenvalues after scalar normalization. In eigen-coordinates, vT_u(v) is proportional to x²−y² with independently varying coefficients x² and y²; these products span a two-dimensional subspace of Sym²V.

All graph products then lie in D=Sym²U⊗Sym²V, of dimension nine. Their span J has dimension at most five, so its annihilator in D* has dimension at least four. The resulting homogeneous quadratic three-entry rows are linearly independent over C and pointwise lie in the one-dimensional annihilator of the two-dimensional fiber span. Their generic row rank is therefore one.

The primitive-row argument is valid over C[u₀,u₁]. A polynomial row spanning the generic row line can be divided by the gcd of its entries to give a homogeneous primitive row w of degree d≥0. Every polynomial row in that generic line is a polynomial multiple of w: any denominator in a reduced multiplier would divide every entry of w. Homogeneous degree-two multiples therefore form a space of dimension at most dim C[u₀,u₁]_(2−d)≤3. This contradicts the annihilator dimension of at least four. The other ruling is identical.

The final statement is properly limited: fixing the ruling base pointwise is excluded; acting by a nonidentity involution on that base is not excluded.

## Optional expository clarification

No repair is required. For maximal transparency, the sentence asserting that the union resolves both pencils could be followed by the local base-point-free pullback observation in Section 4 of this audit. Also, the opening hypotheses could repeat explicitly that the graph products lie in K and are generically rank two, rather than relying on the inherited meaning of the ordered-factor surface. Both are clarifications of valid reasoning, not mathematical gaps.
