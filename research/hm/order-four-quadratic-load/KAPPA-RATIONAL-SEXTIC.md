# The rank-zero-B parameter locus is one rational sextic

## Scope and precise inputs

Work over the complex numbers. Let E be the Horrocks–Mumford bundle on P4 with determinant O(5), U=H0(E) of dimension four, and C the reduced disjoint union of its 25 evaluation-degeneracy lines. Use the actual evaluation map U tensor O -> E, rank two off C and rank one on C, whose maximal minors generate I_C scheme-theoretically. For p in C let kappa(p) be its three-dimensional evaluation kernel, viewed in P(U*).

Public inputs read for this deduction:

1. PR543, BETA-IMAGE-DIMENSION-DROP.md at f5b50172bd65d1772d1af3d4a511decc8363183e, including the actual ideal-generation and rank assumptions and definition of kappa.
2. PR557, research/hm/sextic-alpha-exclusion/ALPHA-EXCLUSION.md at 212f18bb3afb52171068d1aaf8a0dbfbf9954d2b: H0(I_C tensor E)=0; H5 acts trivially on U; the normalizer's actual U is chi_4, factoring through A5 because the central -I of SL2(F5) has character value +4. Its primary source pin is Horrocks–Mumford (1973), equation (4.12), printed p.74, and character table printed p.81.
3. PR541, research/hm/generic-cubic-primitive-closure/PROOF.md at 9ce30d8d783da881be68548d158ebcb48e122850, Section 3: H5/Z acts regularly on the 25 lines, and a chosen component L is preserved by an SL2(F5) complement in the normalizer. The primary source is Horrocks–Mumford (1973), Sections 1 and 3, equation (3.6).
4. PR1 coordination was read through comment 6312024934 on 2026-10-21. This target is the exceptional rank-zero-B parameter curve, not Mr. Slop's primary bad-quadric scheme.

The argument below is a new symbolic deduction from these inputs, not a selected-coefficient computation or a claim of full proof repair.

## 1. The evaluation splitting on each component line

Fix a component L. Its rank-one evaluation has line-bundle image M and quotient Q, and a rank-three kernel K:

0 -> K -> U tensor O_L -> M -> 0,
0 -> M -> E|L -> Q -> 0.

The derivative of a map along its rank-one degeneracy locus canonically maps the normal bundle to Hom(K,Q). Here this map is an isomorphism:

N_{L/P4} = Hom(K,Q).

For completeness, locally choose a unit entry and reduce evaluation to the matrix with first row (1,0,0,0) and second row (0,a,b,c). Its maximal-minor ideal is (a,b,c)=I_C locally. Since C is a smooth codimension-three line there, these generators give a basis of I_C/I_C^2. Their derivatives identify the normal bundle with the three entries of Hom(K,Q). Thus this is an actual normal-bundle identification, not an assumption of generic transversality for an unrelated map.

Since L is a linear line, N_{L/P4}=O_L(1)^3. Taking determinants, with constant vector-space factors suppressed, gives

O_L(3) = M tensor Q^3,
M tensor Q = O_L(5).

Therefore Q^2=O_L(-2). Pic(P1) has no torsion, so

Q=O_L(-1), M=O_L(6), K=O_L(-2)^3.

The last equality follows directly from K* tensor Q=O_L(1)^3. In particular E|L=O_L(6) directsum O_L(-1), since Ext1(O(-1),O(6))=H1(O(7))=0. The image M is the positive summand, and evaluation is a basepoint-free four-section linear system in O_L(6).

## 2. Nondegeneracy and the two initial degree possibilities

The restriction U -> H0(L,M) is injective. Indeed, if s in U vanishes on L, H5-invariance of s transports this vanishing to every translate of L. Transitivity on the 25 components implies s vanishes on the reduced curve C, contradicting H0(I_C tensor E)=0 unless s=0.

Consequently kappa_L:L -> P(U*) is nonconstant and its image Gamma_L spans P3. Moreover kappa_L*O(1)=M=O_L(6). It is finite onto its integral image, since it is a nonconstant proper morphism from a curve. Let e be its degree onto the normalization of that image and d its projective degree. Then ed=6 and d>=3 because Gamma_L spans P3. Thus the only possibilities are

(e,d)=(1,6), or (2,3).

The normalization is P1: its function field is a subfield of C(P1), or equivalently Riemann–Hurwitz rules out positive genus for a nonconstant map from P1. In the second case the image is a twisted cubic. One can see this without a classification theorem: its normalization has a degree-three line bundle supplying four independent sections, hence all of H0(O_P1(3)), and the associated map is the degree-three Veronese embedding.

## 3. Equivariance rules out the double twisted cubic

Choose the component L stabilized by the SL2(F5) complement supplied by input 3. Evaluation and kappa_L are equivariant for this complement. By input 2 its action on P(U*) factors through A5 and is faithful: a nontrivial kernel would be all of the simple group A5; a trivial projective action would make the four-dimensional irreducible representation scalar, impossible.

This action remains faithful on Gamma_L. Indeed any projective transformation fixing every point of the integral nondegenerate curve Gamma_L has that curve in its union of projective eigenspaces. Irreducibility forces containment in one eigenspace, and nondegeneracy then forces that eigenspace to be all of P3. The transformation is the identity.

Suppose kappa_L had degree two onto the twisted cubic. A degree-two map between smooth complex projective lines has a branch divisor consisting of two distinct points. This follows from Riemann–Hurwitz: ramification degree two, each ramification index is at most two, and two ramified points cannot have the same image in a degree-two fiber. Equivariance makes that branch pair invariant under A5 acting faithfully on the target twisted cubic, hence on its P1 normalization.

But A5 cannot preserve a pair of points under a faithful action on P1. Its permutation action on that pair is trivial, since A5 has no quotient of order two. Thus it would fix each point. A finite subgroup of PGL2(C) fixing a point is cyclic: send the fixed point to infinity, average the orbit of any affine point to get a second fixed point, and conjugate the group into C*. A5 is not cyclic. This contradiction excludes degree two.

Hence kappa_L is finite birational onto a nondegenerate integral rational sextic Gamma_L in P3.

## 4. The 25 images coincide

The H5 action on U is trivial, so kappa(gp)=kappa(p) for every g in H5. The projective Heisenberg group acts regularly on the component lines. Therefore all 25 kappa_L have exactly the same reduced image Gamma, and are identified by the group isomorphisms between their source lines.

Thus the entire exceptional rank-zero-B locus kappa(C) is one integral nondegenerate rational sextic Gamma, with each component line mapping finitely birationally to it. The map C -> Gamma has generic degree 25, meaning a general point of Gamma has exactly one preimage on each of the 25 lines.

Equivalently, for a general B on Gamma, B evaluates with rank zero at precisely one point on each component line, whereas B outside Gamma evaluates with rank one everywhere on C. This refines the previously known dimension-at-most-one bound on the exceptional parameter locus. It does not exclude beta families whose parameter image is contained in Gamma or, by itself, establish smoothness of Gamma; Section 5 supplies that sharpening.

## 5. The sextic is smooth, and every component maps isomorphically

Castelnuovo's arithmetic-genus bound for a nondegenerate integral degree-six curve in P3 is p_a(Gamma)<=4. The bound is for arithmetic genus and does not presume smoothness. A checked public research source is Vincenzo Di Gennaro, "The genus of curves in P4 and P5 not contained in quadrics", Section 2(v), formula (13), https://link.springer.com/article/10.1007/s12215-022-00788-x . In its notation s=2, d-1=5=2*2+1, so G(3;6)=binom(2,2)*2+2*1=4. Section 2 discusses arithmetic genus throughout; its reference is Harris, Curves in Projective Space, Theorem (3.7), p.87. This standard bound is imported and credited, not a new theorem here.

Since the normalization of Gamma is P1, the normalization quotient has total length delta=p_a(Gamma)<=4. Every singular point contributes at least one. The singular-point set is finite and A5-invariant.

There is no orbit of size one in P(U*), because an A5-fixed projective point would give an invariant one-dimensional subspace in the irreducible four-dimensional representation U*. There are no orbits of sizes two, three, or four either: a transitive action on such an orbit gives a nontrivial homomorphism A5 -> S_n, which would be injective by simplicity, impossible since 60>n!. Thus every A5 orbit of points in P(U*) has size at least five.

If Gamma had even one singular point, its entire orbit would contribute at least five to delta, contradicting delta<=4. Therefore Gamma is smooth. Each finite birational kappa_L:P1 -> Gamma is then an isomorphism. In particular C -> Gamma is the disjoint union of 25 isomorphisms, and EVERY parameter B in Gamma, not merely a general one, has exactly one rank-zero-B evaluation point on each component line.

## Boundaries and reproducibility

The proof does not evaluate selected HM coefficients, source matrices, minors, or ranks, and does not run any experiment. It does not restart the local-model spike or the consumed one-shot experiment. Smoothness of Gamma uses the additional explicitly credited arithmetic-genus bound and the orbit argument of Section 5; birationality alone would not imply it. No conclusion about normality of the exceptional degree-ten or degree-fifteen surfaces follows. The residual beta branch and Q4 remain open.

Repository source links are obtained by appending each path above to https://github.com/Akilleez-QA/read-em-and-weep/blob/ and its displayed immutable commit. Primary HM source: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf .
