# Scope and later implications

The universal lemmas below remain valid. Intermediate unresolved-case descriptions are historical: the universal K7 and K8 bounds are supplied by diagonal-hartogs-fiber-bound/PROOF.md and UNSQUARED_PENCIL.md. For any actual canonical operation satisfying a later global rank-at-least-five theorem, residual-rank-one through four loci are empty; these are not simultaneous live canonical alternatives. Conditional global dimension implications retain their separately stated hypotheses.

# Prior mathematical audit

This audit concerns the source manuscript. It is not a formal verification or a review of later normalized publication bytes.

# Independent audit: finite partner planes and the transverse-basepoint obstruction

## Verdict

PASS. Independently checked `PROOF.md`, Sections 1–5, on 2026-10-19. Both new exclusions are valid over C, and the stated Grassmannian-general K7 dimension bound follows. The exceptional degenerate-net cases remain open exactly as stated. No universal K7 dimension-two bound or conclusion about generic middles of a fixed operation follows.

## 1. The universal projective incidence is genuinely closed and finite

The condition aU⊂K is closed on P(E)×Gr(3,E). On that closed incidence the coefficientwise identity v(ab)∧a∧b=0 for every b∈U is also closed. It is equivalent to compatibility on the independent pairs; the wedge identity alone at b=a is not being mistaken for square compatibility.

If a∈U, the two distinct directions b,c modulo Ca yield v(a²)∈span(a,b)∩span(a,c)=Ca. Thus square avoidance removes the entire incidence divisor, including limiting pairs. With dim E=4 and dim U=3, this divisor has ample bundle O(1,1), so a positive-dimensional projective reduced support cannot avoid it. Equivalently, complementary line/hyperplane pairs are exactly rank-one idempotents, an affine variety. Hence the incidence has finite support. The argument does not claim that its scheme structure is reduced.

The complement/projector argument specifically uses that U is a hyperplane complementary to Ca. It is not a dimension-free assertion for arbitrary common-factor subspaces. Independence from dim K is correctly claimed.

## 2. Fixed-factor fibers and threefold projection dimensions

For M_a of vector dimension at most three, any surface component fills a projective plane. When M_a=E, the pencil T−λπ has generic rank three: a maximal minor has a nonzero leading coefficient because π has rank three. The locus over the generic λ has dimension one in total. Exceptional λ are finite, and rank zero is excluded by T(a)≠0, which is square avoidance. Consequently each surface component is a full projective plane.

Moreover [a] lies in none of these exceptional kernels because (T−λπ)(a)=T(a)≠0. There is no extra surface hidden in the excluded diagonal point or a limiting eigenvalue. The plane belongs to the closed incidence from Section 1. Thus only finitely many first factors can have surface fibers. A threefold over a curve would have surface fibers over a dense set of curve points, contradicting this finiteness; a point image contradicts the universal fiber bound two. The argument works equally for either projection, even when geometric fibers have multiple components. No chosen plane family or monodromy assumption is needed.

## 3. The derivative obstruction is valid at a regular base point

If M(a) has rank three and a is a base point, ker M(a)=Ca. In a neighborhood of [a], the projectivized kernel is therefore a regular map φ with φ(a)=a. Dominance of a compatible ordered component over P(E) forces that component to agree generically with this graph: there is a unique partner on the rank-three open.

For local normalized representatives, differentiating the symmetric bilinear kernel identities gives M(a)(h+dφ(h))=0. Modulo Ca, this is dφ=−Id. Differentiating the wedge identity, valid by density on the graph, gives −2v(a²)∧a∧h=0 for every tangent direction h. In dimension four this forces v(a²)∈Ca, contradicting square avoidance. The proof does not rely on extending actual square compatibility by closedness; the derivative is the necessary additional step.

One rank-three base point already guarantees generic polar rank three. If generic polar rank is at most two, no such point exists, so this argument supplies no contradiction. This is a genuine branch: W=span(x0²,x0x1,x1²) has three independent quadrics but generic polar rank two and a projective-line base locus, with rank zero at every base point. This example illustrates the rank exception only; it does not assert existence of compatible threefolds or a suitable correction v.

## 4. Surface factor images and the general-net conclusion

A surface image of an ordered threefold has generic one-dimensional partner fiber, forcing rank M≤2 throughout the image by closure. Thus it is contained in D_W. If all nonzero quadrics of W have rank at least three and one is nonsingular, the determinant is a nonzero homogeneous quartic on P(W). Its zero locus consists entirely of rank-three forms. Their one-dimensional kernels vary regularly, and every point of D_W arises from such a form by a row relation. Therefore dim D_W≤1.

The general-net claims have the stated dimensions: rank-at-most-two forms in P(Sym²E*)=P9 have dimension six, so a general plane misses them. Three general quadrics in P3 form a transverse complete intersection of eight points. The required open conditions therefore hold for general W. Combined with the two projection exclusions they rule out every compatible threefold, and hence every larger compatible locus by taking an integral three-dimensional subvariety meeting the compatible open densely. This establishes the general-K7 bound two.

## 5. Numerical dependency and exact scope

The universal bound three for arbitrary K7 uses the pointwise K6 theorem in `../rank-four-compatible-fiber-bound/PROOF.md`. Its opening hypothesis is precisely a six-dimensional subspace with square-avoiding correction; it does not require that the restriction remain an entire residual kernel. Hyperplane slicing preserves square avoidance and the dense compatible rank-two open, so its use here is valid. This audit checked that dependency's formulation and its use, rather than re-auditing its entire earlier classification chain.

The new geometric exclusions themselves have no K6 dependency. Dimensions are support/Krull dimensions, not tangent dimensions or multiplicity assertions. Generic rank ≤2 nets, rank-three nets with only degenerate base points, and nets with surface-sized D_W are not classified. Grassmannian-general K is not identified with a generic middle kernel of any specific operation. There is no missing repair in the current draft.


