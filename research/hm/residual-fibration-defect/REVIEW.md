# Independent review: residual fibration defect

Verdict: PASS. Independent mathematical review; not a formal proof-assistant check.

Reviewed proof: `PROOF.md`. SHA256: `0554d5fb3ca714a55a36f3652261396abb43e345e22fb17d2467ebfff27e89c4`. A later status-only edit does not change this mathematical review.

## Dependencies and source check

The proof explicitly depends on PR572 for the six-nodal residual curve and the factorization gν=hπ, and on PR574 for the exact normalization sequence and transverse surface local rings. PR570 and PR573 identify these objects with the actual primary scheme. These are dependencies, not new claims established by this review.

The quoted BHM source was checked at printed p58 and pp63–64. It states the twelve I5 fibers, K_X=3F and χ(O_X)=5, that each singular fiber maps isomorphically to a pentagon, and that the only identifications are the paired vertices of paired singular fibers. In particular there are five surface double points for each pair. The proof correctly matches those pairs with the six normalization pairs of Γ using gν=hπ; no unproved compatibility of direction labels is needed.

## Direct-image argument

1. The smooth elliptic surface over the smooth curve is flat, with connected reduced genus-one fibers. The relative dualizing bundle is π*O(5). Relative duality therefore gives R¹π_*O_X=O(-5), and higher direct images vanish. Finiteness of h and ν justifies the displayed composite direct-image identity.
2. At a base node, functions from h_*O_B have the same value at all five vertices of each fixed elliptic fiber. The normalization quotient on S is the difference of the two branch residues. Thus its five coordinates are the same scalar difference, after consistent orientation.
3. The difference is surjective: the semilocal normalization has two distinct maximal ideals and the Chinese remainder theorem gives independent residues. The kernel is exactly the nodal base ring, so g_*O_S=O_Γ with its natural algebra structure.
4. The quotient of the five residue copies by the one-dimensional image is annihilated by the base maximal ideal and has dimension four. Hence K has length 24. The sheaf h_*O(-5) is torsion-free on integral Γ, proving K is the entire torsion subsheaf of R¹g_*O_S.
5. Vanishing of R^i g_*O_S for i≥2 follows from the same exact sequence and the corresponding vanishings for its other terms. No splitting or unsupported singular-base cohomology-and-base-change claim is used.

## Scheme fiber and nonflatness

The completed local map at each shared vertex is s↦(u1u2,0), t↦(0,v1v2). This follows from the two branches of the nodal base and the ordinary semistable node of each I5 fiber in the smooth normalization. Units can be absorbed in the regular parameters.

Quotienting the surface fiber-product ring by these two elements gives the fiber product of two reduced nodal curve rings over C. Equivalently its ideal in four formal variables contains all products of distinct variables. It is the reduced union of four coordinate axes, with no multiplicity. Its two pentagon branches meet in one reduced point. The calculation also verifies the exact fiber normalization/gluing sequence used globally.

The two pentagons each have χ=0 and degree five, and five reduced intersections contribute −5 to the Euler characteristic. Their union is connected, so χ=−5, h¹=6 and its Hilbert polynomial is 10n−5. Away from the six nodes the fiber is a smooth elliptic quintic, with polynomial 5n. Projectivity and relative ampleness make constancy of Hilbert polynomial a valid necessary condition for flatness. Every neighborhood of a node meets the smooth base locus, so the proof correctly concludes nonflatness over each node. This conclusion means the morphism is not flat over that base point; it does not claim nonflatness at every individual point of its fiber.

## Scope

No mathematical correction was required. The proof establishes the Stein property, the exact higher-direct-image torsion defect, and the complete reduced special-fiber description. It does not establish Q4, any selected source-instance evaluation, higher lifting or algebraicity. Review used structural algebra and pinned geometry only, with no numerical HM evaluation and no public repository write.
