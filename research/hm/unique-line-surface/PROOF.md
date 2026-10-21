# One invariant surface contains all twenty-five primary lines

## Statement and immutable inputs

Work over C. Let D be the actual primary evaluation maximal-minor scheme in P4. This is not the fixed-three-section surface X_B and not the quadratic-parameter eightfold.

Use the following published structural inputs:

- PR555 at ff5a3164337016e96e3a29a9ad37891130a66e29: dim D<=2; the dual evaluation is a linear map 10O -> 3Omega(2) contained as a subbundle in 15O(1), and its rank-drop scheme is the same maximal-minor scheme after that inclusion. Its degree-ten minors have no common divisor.
- PR562 at 86b643fe2adecbd321d1c8f98be84fe2082bcd10: twenty-five distinguished, pairwise disjoint lines form the regular torsor of the projective Heisenberg group G=F5^2. The normalizer preserves D and these lines, and its SL2(F5) quotient acts on G in the usual way. A complement stabilizes a chosen line, so the action on the set of lines is the affine action G semidirect SL2(F5).
- PR566 at 11642c25ba1b3046e8bc97e3f0e95f077e010375: every distinguished line belongs to a surface component of D; D is smooth of dimension two at every point of these lines; their normal bundles in this smooth locus are O(-5).

**Theorem.** There is exactly one irreducible surface component S of D containing any distinguished line, and it contains all twenty-five. The integral reduced surface S is invariant under the full normalizer and agrees with D on a neighborhood of their union. Its degree d satisfies

10 <= d <= 95, and 5 divides d.

For every distinguished line L, projection from L extends to a globally defined morphism

S -> P2

associated to O_S(H-L). It is generically finite of degree d-7. Every other distinguished line maps isomorphically onto a line in P2. This does not assert that their image lines are distinct.

Other surface components of D, if present, contain none of the distinguished lines and do not meet their union. No global normality, global reducedness of D, or complete component classification is asserted.

## 1. A degree bound for a surface containing a negative line

Let T be any integral projective surface in P4, smooth on a neighborhood of a line L, with N_{L/T}=O_L(-5). Because T is smooth near L, its ideal I_{L/T} is invertible there. Away from L that ideal is the unit ideal, so L is a globally defined effective Cartier divisor on T.

The three ambient linear forms defining L generate I_{L/P4}(1). Restricting their ideal to T gives a surjection

O_T^3 -> I_{L/T}(1)=O_T(H-L).

Thus A=O_T(H-L) is globally generated. A globally generated line bundle on an integral projective surface has nonnegative self-intersection, without any normality or smoothness assumption away from L. Indeed its morphism to projective space has image of dimension at most two: the square is zero if the image has smaller dimension, and otherwise equals its positive generic degree times the degree of its image, by the projection formula.

The Cartier intersection calculation gives

A^2=(H-L)^2=deg(T)-2(H.L)+L^2=deg(T)-2-5=deg(T)-7.

Here H.L=1 because L is a line, and L^2=deg N_{L/T}=-5 because T is smooth near L. Therefore every such T has degree at least seven.

## 2. The sum of degrees of all surface components is at most 100

The degree-ten maximal minors of the linear 15 by 10 presentation have greatest common divisor one. Choose a nonzero linear combination f of them. It has finitely many irreducible factors. Since no factor divides every minor, one can choose a second linear combination g avoiding divisibility by each factor of f. Over the infinite field C this only excludes finitely many proper linear subspaces of the space of combinations.

Thus f and g have no common factor. They form a regular sequence of degree ten and ten in the homogeneous polynomial ring. Their projective complete intersection has pure dimension two and degree 100. It contains D scheme-theoretically. Every two-dimensional irreducible component of D is therefore a component of that complete intersection. Since every component has positive integral cycle multiplicity, the sum of the degrees of the distinct reduced surface components of D is at most 100.

This is only an upper bound. It does not identify D with that complete intersection or assert that D itself has degree 100.

## 3. The normalizer forces one component or twenty-five

Smoothness of D at every point of a distinguished line implies that there is a unique irreducible component of D through that point. Since the line is irreducible and already lies on a surface component, the entire line belongs to a unique surface component. Two lines are declared equivalent if their surface components agree. This is a partition of the twenty-five lines preserved by the normalizer.

Identify the set of lines with the affine plane G=F5^2 by choosing one as the origin. The subgroup G acts by translations; the origin stabilizer contains SL2(F5), which is transitive on the twenty-four nonzero vectors. Consequently the affine action is two-transitive: after translating the first point to zero, the stabilizer can send any distinct second point to any other.

A partition invariant under a two-transitive group has either one block or only singleton blocks. Explicitly, if the block of one point contains a second point, its stabilizer's transitivity on all other points forces that block to contain every point. Thus either all twenty-five lines lie on one surface component, or they lie on twenty-five distinct surface components.

In the latter case Section 1 gives sum of component degrees at least 25*7=175, contradicting Section 2. Therefore all twenty-five lines belong to one component S. The uniqueness makes S invariant under the normalizer. Any other component meeting one of the lines would contradict regularity of the local ring of D there, so other components avoid their union. The reduced integral structure on S and the scheme D agree on an open neighborhood of this union.

## 4. Heisenberg invariance forces degree divisible by five

For completeness the divisibility used here is a representation-theoretic Hilbert-polynomial argument, not a degree classification. The ambient five-dimensional representation is a Schrödinger representation of the order-125 Heisenberg group, with primitive central character. Because S is invariant, its homogeneous ideal is invariant, and the induced linearization on H0(S,O_S(n)) has central character zeta^(a n) for some a prime to five (the sign depends on the convention for sections).

Let sigma and tau be Heisenberg generators with commutator a central generator. On any finite-dimensional representation on which that central generator acts as a nontrivial fifth root lambda, taking determinants of the commutator yields lambda^dim=1. Therefore its dimension is divisible by five. It follows that h0(S,O_S(n)) is divisible by five whenever n is not divisible by five.

For all sufficiently large n this equals the Hilbert polynomial P_S(n), whose second finite difference is deg S=d. Choose n sufficiently large with n congruent to one modulo five. Then n,n+1,n+2 are all nonzero modulo five, so

d=P_S(n+2)-2P_S(n+1)+P_S(n)

is divisible by five. Combining d>=7 with divisibility gives d>=10; Section 2 gives d<=100.

This argument is valid for an integral projective surface without a normality or Cohen–Macaulay hypothesis.

The endpoint d=100 is impossible. If it held, the complete intersection of Section 2 would have S as its only component, of generic multiplicity one. A complete intersection is Cohen–Macaulay, hence has no embedded associated primes; generic reducedness then makes it reduced. It would therefore equal the integral reduced surface S. Complete-intersection adjunction would give omega_S=O_S(10+10-5)=O_S(15). On the smooth neighborhood of L this implies K_S.L=15. But adjunction on the same smooth neighborhood and L^2=-5 give K_S.L=-2-(-5)=3, a contradiction. Thus divisibility sharpens the upper bound to d<=95.

## 5. Projection from each line and its exact degree

Apply Section 1 to T=S. The three linear forms through L define a morphism f_L:S->P2 with f_L*O(1)=O_S(H-L). On S minus L it is the usual linear projection from L; the invertible ideal removes the apparent base locus along L.

Its square is d-7>=3, so its image has dimension two and therefore equals P2. The projection formula gives its generic degree exactly d-7. In particular the degree belongs to {3,8,13,...,88}.

For another distinguished line L', the two lines are disjoint. Hence L.L'=0 and

O_S(H-L)|L'=O_{L'}(1).

A basepoint-free linear system of degree one on P1 defines an isomorphism onto a projective line. Thus f_L maps each of the other twenty-four distinguished lines isomorphically onto a line. The images need not be distinct; the statement does not infer injectivity across different source lines.

On L itself the pullback has degree (H-L).L=6. No assertion about the degree of its image or birationality on L is needed here.

## Scope and verification

This is a structural deduction from the pinned actual primary geometry, the normalizer action, and Cartier intersection theory. It uses no selected HM/source coefficient, matrix, numerical rank, or large computation. It does not identify the invariant surface S with a fixed-beta surface, prove D globally irreducible or normal, or resolve the original Q4/source/algebraicity problem.

Public dependency links: https://github.com/Akilleez-QA/read-em-and-weep/pull/555 ; https://github.com/Akilleez-QA/read-em-and-weep/pull/562 ; https://github.com/Akilleez-QA/read-em-and-weep/pull/566 . The Heisenberg commutator and normalizer action are the same published group data used in PR562, with primary source Horrocks–Mumford (1973), Sections 1 and 3: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf .
