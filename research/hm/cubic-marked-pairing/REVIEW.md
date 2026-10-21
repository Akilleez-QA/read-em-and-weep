# Independent review: the unique possible marked pairing

## Verdict and reviewed version

**PASS, conditional on the explicitly pinned geometric inputs.** The proof establishes the claimed uniqueness theorem, including the actual affine normalizer action and the formula

    tau(i,j) = (2i-j, 3i-2j),   i != j in F5.

It does not establish the existence of equal-image pairs and does not exclude r=1. No correction to the reviewed proof is required.

Reviewed proof SHA256:

    dd29da9eb8d5d515662c9f91daa1988974e0d186c52955b5ea69764a9993de57

The supplied dependency files were also read. Their SHA256 values are:

- cubic-fixed-directions/PROOF.md: 9b86fe9b9c552119ed8ab01ab4a1894a7033118d69fa09e8ce7f9247d556dfe7
- cubic-embedding-locus/PROOF.md: 75afda202609d76b2780bfeff6824c6780457bf39a6b21a9306bdd9430b17601

This review checks the new derivation and the consistency of its imports with those supplied dependencies. It is not a fresh verification of every earlier actual-primary dictionary or external-source result. Only abstract finite-group, incidence, and character-weight reasoning was used; no actual HM/source coefficient, vector, matrix, point, kernel, or rank was evaluated.

## 1. Incidence and the two pentagons

The K5 conclusion follows from the actual component stabilizers, not from a presumed combinatorial model. At a node, all four incident component stabilizers must be its unique order-five eigenline direction. Each opposite endpoint is therefore one of the other four eigenlines of that direction. Distinct joining lines cannot have the same endpoints. Consequently all four possible opposite endpoints occur, giving six disjoint K5 graphs and exactly sixty edges.

The nondegenerate Heisenberg commutator makes U/G act regularly on each five-element eigenbasis. A translation-invariant pentagon has five edges and must be one orbit of unordered edges under this cyclic translation action. The two such edge orbits are precisely the two nonzero differences modulo sign. Thus the complementary-pentagon description is justified by the imported translation invariance; no unproved pairing of cusps is inserted.

## 2. The normalizer action is genuinely affine and transitive

For the exponent-five Heisenberg group, every symplectic automorphism of U lifts to a center-fixing group automorphism in the displayed intrinsic model. The character of the faithful-central-character irreducible module is unchanged: it vanishes off the center and is five times the fixed central character on the center. The resulting intertwiner proves that the projective normalizer realizes SL2(F5), rather than merely assuming this realization.

For a fixed direction, restriction of a normalizer automorphism to its central extension acts on the extension characters by a scalar on differences and possibly a common character translation. Hence the induced permutation is affine. Heisenberg translations supply every additive translation, and the direction stabilizer in SL2(F5) supplies every nonzero scalar. The induced permutation group is therefore exactly AGL1(F5), sharply two-transitive on that eigenbasis. Combined with SL2(F5)-transitivity on the six directions, this gives one orbit on all 120 marks.

The full normalizer preserves the union of all thirty eigenlines, hence Z and its complete cubic system. The proved K5 incidence also makes its preservation of component joins and marks intrinsic. No independent preservation assertion for the entire original surface S is needed here. Equivariance of the relevant morphism and of equal-image pairing does not require a chosen equivariant matrix for the primary resolution.

## 3. Involution classification

Under r=1, the sixty disjoint double fibers use 120 distinct marked points and thus exhaust all 120 marks. Their two endpoints are the endpoints of their associated component, so the partner belongs to the same K5.

Normalize (i,j) to (0,1). If its partner is (a,b), distinct endpoints give a != 0 and the mark condition gives b != a. Affine equivariance then forces

    tau(i,j) = (i+a(j-i), i+b(j-i)).

Writing d=b-a, involutivity gives d^2=1 and a(1+d)=0. Since a != 0 and the characteristic is five, d=-1 and b=a-1. The case a=1 is exactly the pair of own-direction marks of the connecting edge, excluded by the r=1 geometry. The remaining a=2,3,4 are all fixed-point-free incidence-compatible involutions. Each gives one unordered pair over each edge because multiplication by a bijects the nonzero endpoint differences.

There is no hidden combinatorial contradiction: one of these involutions can satisfy every listed incidence condition.

## 4. Cubic characters select the unique involution

The exceptional evaluation at the mark (i,j) is the nonzero image of L_i^2 L_j in the equivariant quotient Sym^3(A) -> W*. This is the first derivative of cubic evaluation at the base eigenline, with any polarization constant irrelevant. Its nonvanishing is supplied by generation of 3H-E; no coefficient evaluation is needed.

If a chosen generator has eigencharacters lambda eta^i on L_i, the corresponding evaluation line has character lambda^3 eta^(2i+j). The same fixed linear action on W* is used at both marks. Consequently two equal projective image lines must have equal eigencharacters, even though the map is considered projectively.

For the normalized pair (0,1), (a,a-1), this gives 1=3a-1, hence a=4. Substitution yields exactly the claimed formula. A common scalar change of linearization shifts both characters equally and cannot alter this conclusion. Conversely, equal character alone does not imply equal lines: the proof correctly stops short of that invalid inference.

## 5. Independent fixed-edge weight derivation

There is a second derivation that does not use the classification of global equivariant involutions. Fix an edge with endpoints i != k in one eigenbasis. Let V_i and V_k be the four-dimensional vector spans of the embedded exceptional divisors in W*. Use exponent labels relative to the common factor lambda^3.

Since each exceptional divisor is linearly embedded, the four marked evaluation lines in V_i are independent and have distinct weights 2i+j for j != i. Thus V_i has exactly the weights

    F5 minus {3i},

each with multiplicity one. Similarly V_k has all weights except 3k, each with multiplicity one.

In the r=1 case K=V_i intersect V_k is a one-dimensional invariant subspace. Its weight belongs to F5 minus {3i,3k}. The embedded component line has vector span generated by its two endpoint evaluation lines, of weights 2i+k and i+2k. Its bad intersection point P(K) is outside that component image by the imported r=1 statement.

The weight 2i+k is therefore impossible for K: its weight space in V_i is one-dimensional and is precisely the component's endpoint line at i, so K would equal that endpoint line. Likewise weight i+2k is impossible by the unique corresponding weight space in V_k. This multiplicity-one argument is essential: disjointness from the component span alone would not exclude these weights in an unrestricted target eigenspace.

The five exponents

    3i, 3k, 2i+k, i+2k, -i-k

are distinct when i != k. For example, after the affine normalization i=0, k=1 they become 0,3,1,2,4. The only remaining possible weight of K is therefore -i-k.

At endpoint i, solving 2i+j=-i-k gives j=2i-k. At endpoint k, solving 2k+l=-i-k gives l=2k-i. Hence the forced pair over edge {i,k} is

    (i, 2i-k) paired with (k, 2k-i).

Putting k=2i-j recovers

    tau(i,j) = (2i-j, 3i-2j).

This is an independent local weight-elimination confirmation of the same unique pairing. It also remains only a necessary condition for actual equality of the two image lines.

## 6. Compatibility and remaining boundary

Writing j=i+delta, the formula pairs (i,i+delta) with (i-delta,i-2delta). Applying it twice returns the original flag. Its endpoints are distinct, neither mark points along their joining edge, and both marks point outward along adjacent sides of the same difference-class pentagon. The formula commutes with every affine change of character label, including those induced between distinct eigenbases by the normalizer.

The final target-multiplicity refinement also checks: the central character on W* is the cube of that on A and remains faithful. The same commutator conjugation argument cyclically permutes the five eigenvalues of a direction generator, with equal multiplicities. Since dim W*=10, every target weight space has dimension exactly two, so its projectivization is P1. This also explains why equal character does not force equality of the two image points.

The new theorem therefore resolves the formerly unspecified marks in the r=1 alternative and locates the residual coincidence question inside a definite target P1. It does not choose between r=0 and r=1, calculate the actual intersection subspaces, establish equality of same-character evaluation lines, or determine local analytic branch types, conductor structure, full-adjoint, or higher-lifting assertions. These limitations are correctly stated in the proof.
