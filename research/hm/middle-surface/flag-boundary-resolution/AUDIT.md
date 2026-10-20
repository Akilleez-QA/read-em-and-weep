# Audit of the full-flag boundary resolution

Status: PASS. The producer's `PROOF.md`, Sections 1–7 and the introductory result, have been read and independently checked. No substantive mathematical defect was found. The additional rank-four and rank-three uniqueness sharpenings are independently verified below.

## Scope

This is a universal algebraic-geometric audit over C of the construction continuing `/research/hm/middle-surface/rank-five-middle-families/PROOF.md` and `/research/hm/middle-surface/ternary-metric-boundary/PROOF.md`. Those two predecessor proofs have been read. Their canonical-complement construction and positivity theorem are the inputs being continued here; their underlying operation-theoretic hypotheses are not replaced or strengthened.

## Verified geometric argument

Let B be the integral projective middle surface and let B° be its dense good open. On B° the canonical flag satisfies C⊂H⊂V, with dimensions three and four, and H=U⊕C. Close its graph in B×Flag(3,4;V), and take a smooth projective resolution X of the integral graph component. Its map to B is birational. The closed incidence U⊂H holds on X because it holds densely and is the vanishing of U→V/H. Both C and H are tautological subbundles, including along the exceptional locus.

The middle map U→R=V/C factors through the line subbundle L=H/C. It is generically nonzero. Consequently it defines an effective Cartier divisor A and a canonical identification L⊗U*=O(A). Locally, after a splitting R=L⊕N and trivialization of U, its section has coordinates (a,0), with a a nonzero element of a regular integral local ring. Its full zero ideal is therefore (a), not merely its divisorial part. This verifies scheme structure, multiplicities, and absence of a residual isolated zero scheme.

Put F=R⊗U*, N=V/H, h=c1(U*), n=c1(N). The exact sequence

    0 → O(A) → F → N⊗U* → 0

implies c2(F)=A·(n+h) in the Chow group of zero-cycles. Independently, global generation of R and nefness of h yield deg c2(F)=deg(c2(R)+h c1(R)+h²)≥deg B>0. Both h and n are pullbacks of hyperplane classes from projective spaces and hence nef. For A=Σm_iD_i, each term m_i deg((n+h)|D_i) is nonnegative. At least one is positive. This is an excess-Chern intersection identity, not a length assertion about the divisor.

The zero locus lies over B\B° because the canonical flag extends there with U transverse to C. If B\B° is finite, every D_i maps to a single middle point and h·D_i=0. Positivity then forces n·D_i>0 for some i. Equivalently, the support-hyperplane map is nonconstant on that curve, giving a positive-dimensional family of limiting hyperplanes over one bad point. This proves that unique hyperplane limits at all finitely many bad points are impossible. It does not say that every bad point has varying limits.

## Comparison with an old complement resolution

The flag graph projects properly and birationally to the old complement graph by forgetting H. For any chosen old smooth complement resolution X0, use a smooth resolution Y of the main component of X0 times the flag graph over the complement graph. This supplies a morphism π:Y→X0 and retains the old C and U by pullback. Thus F_Y=π*F_0 and the total top-Chern number is unchanged.

More explicitly, on X0 write the zero ideal of the section as O(-A0) I_Z, where Z is the residual zero-dimensional local complete intersection. On the complement of its zero scheme, H is uniquely C+U. The closure of this direction graph in the projective bundle of lines in R is the blowup of the section's ideal. Multiplication of an ideal by an invertible ideal does not change its blowup, so it is also the blowup of I_Z. This can be checked directly by the Rees algebra or by the closure of the graph of the ratio of the two local section coordinates.

On a smooth resolution dominating that blowup, I_Z O_Y=O(-E) for an effective divisor E, and the full new zero divisor is

    A_Y=π*A0+E.

This exhibits how residual isolated zeros become divisorial on the flag resolution. It does not assert that A is an invariant reduced boundary, a strict transform of A0, or always the original metric discriminant. The preserved quantity is the total Chern number:

    deg A_Y·(n_Y+h_Y)
      = deg c2(F_0)
      = length(Z)+deg A0·(c1(F_0)-A0).

If Z is empty, the old section already supplies a regular direction after dividing its Cartier factor, and the same argument applies with no new principalization contribution E. A further blowup of an already fixed flag model pulls back its complete Cartier divisor, potentially adding exceptional components to its displayed decomposition; this is compatible with, and not a substitute for, the comparison above.

## Claims not justified by this argument

- It does not prove that the bad locus must have a curve downstairs: a finite bad locus with varying hyperplane limits is allowed.
- It does not give individual nonnegative summands in the old unflagged formula A0·(c1(F_0)-A0).
- It does not identify all divisor multiplicities with discriminant multiplicities outside the corank-one hypotheses of the predecessor proof.
- It does not establish existence or nonexistence of an actual seven-dimensional independent-zero family or a universal affine bound six.


## Additional sharpening: rank-four points have unique limiting support

The following additional proposed corollary is valid. At a point b of residual rank four, ker Q_b has dimension six inside Sym²(V/U_b), whose dimension is ten. Every limiting support three-plane E_A=H_A/U_b carries some limiting five-plane K_A with K_A⊂ker Q_b and K_A⊂Sym²E_A. To justify existence for every flag limit, close the augmented graph recording K as well as (C,H) in the relative Grassmannian. Its projection to the original integral flag graph is proper, has dense image, and hence is surjective. The two stated inclusions are closed incidence conditions and hold on its closure.

If H_A and H_B were distinct, E_A and E_B would be distinct three-planes in the same four-dimensional space. Their intersection has dimension two, and

    Sym²E_A ∩ Sym²E_B = Sym²(E_A∩E_B)

has dimension three. This identity follows by choosing a basis of their intersection and extending it separately to the two three-planes. But two five-planes inside the six-dimensional ker Q_b intersect in dimension at least four. This is a contradiction.

At residual rank five the limiting K is ker Q_b itself and its unique three-dimensional support similarly gives unique H. Alternatively, the same intersection estimate is even stronger there. Since residual rank is at most five everywhere on B, the positive-dimensional family of limiting H forced over a finite bad locus must occur at a point of residual rank at most three.

This dimension-only strengthening still does not show that all bad points have rank at most three, nor does it exclude a finite bad locus containing such a point. At rank three, the dimension estimate alone permits a three-dimensional intersection of the limiting K spaces. The correction and square-avoidance hypotheses give the stronger result in the next section.

## Further sharpening: rank-three uniqueness using square avoidance

The further extension argument is also valid. Work locally near b, trivializing the middle line and choosing a regular splitting of V→V/U. The repeated-input map A_u:V/U→J is injective everywhere under the standing hypothesis. It is therefore an injective bundle map with locally free quotient, and locally has a regular left inverse L. Let B_u denote the ambient symmetric outer-input numerator used to define Q_u. The composite L∘B_u defines a regular linear map on the whole Sym²(V/U). On ker Q_u its value is precisely the actual correction v_u, because there B_u lands in im A_u. This provides a regular ambient extension of the correction even where the dimension of ker Q jumps. No extension of the kernel as a constant-rank subbundle is assumed.

For each limiting K_A supported on E_A, the relation v(K_A)⊂E_A passes to the limit by closed incidence on the augmented graph, using this regular ambient extension. Different choices of left inverse have no effect on its restriction to ker Q_b.

At a residual rank-three point, ker Q_b has dimension seven. For two distinct limiting supports E_A,E_B and W=E_A∩E_B of dimension two,

    dim(K_A∩K_B)≥5+5−7=3,
    K_A∩K_B⊂Sym²W,  dim Sym²W=3.

Thus K_A∩K_B=Sym²W and v(Sym²W)⊂E_A∩E_B=W. On W consider the homogeneous degree-three expression

    e ↦ e∧v(e²) in det W.

Over C it has a nonzero zero: a nonzero homogeneous binary cubic has a root in P(W), while an identically zero cubic vanishes everywhere. At that nonzero e, e² lies in ker Q_b and v(e²) lies in Ce. This is a compatible square, forbidden by the standing repeated-input hypothesis. Distinct limiting supports at rank three are therefore impossible.

Consequently every point of residual rank at least three has a unique limiting support hyperplane. Combining this with the flag-Chern obstruction, a finite bad locus must contain a point of residual rank at most two with a positive-dimensional family of limiting H values. This is a necessary condition, not a claim that such a low-rank configuration exists or that a finite bad locus is impossible.

At rank two the intersection estimate only guarantees a two-dimensional subspace of Sym²W, so the binary-cubic argument on the entire Sym²W does not apply. No uniqueness conclusion at rank two is justified by the argument audited here.

## Manuscript-specific checks

- The draft correctly distinguishes an effective Cartier zero scheme on the integral singular graph from the purity assertion on its smooth resolution; no unwarranted Cohen–Macaulay assertion about the singular graph is made.
- Its Rees-algebra description uses the graph component, avoiding extraneous components of the bare incidence U,C⊂H.
- Its identity p_*(E²)=-[Z] follows from the two exact Chern formulas and the projection formula. Since Z is the residual local complete intersection on the old smooth surface, the zero-cycle carries its actual scheme lengths.
- Its statement that exceptional curves introduced only by resolving singularities cannot manufacture new H values is correct, since the H map factors through the original flag graph.
- Its total Chern lower bound requires only the stated birational surface map, global generation, and nefness; singularities of B do not invalidate the projection formula for h².
