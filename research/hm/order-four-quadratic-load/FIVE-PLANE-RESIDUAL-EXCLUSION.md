# The degree-ten beta branch cannot have a five-plane residual

## Statement

In the actual HM evaluation data, suppose the fixed beta surface X_B has an invariant integral degree-ten component S containing the 25-line curve C. Its residual fundamental cycle cannot be an orbit of five planes under the projective Heisenberg group. Consequently the degree-five residual alternative in this branch is an invariant integral quintic surface.

This excludes the five-plane residual for every parameter B satisfying the stated hypotheses, not merely for a general member of a parameter curve. It does not exclude the integral quintic residual or prove the complete beta exclusion.

## Inputs and provenance

1. The degree-ten component has C subset S, and the remaining cycle is either an invariant integral degree-five surface or an orbit of five planes: BETA-DEGENERACY-SURFACE.md at 26240e70230aef0de1f1b8714a06bd644adeec69, PR543.
2. A point p of C is smooth on X_B whenever B evaluation there has rank one. Thus if p belongs to two distinct surface components of X_B, necessarily B=kappa(p): BETA-IMAGE-DIMENSION-DROP.md at f5b50172bd65d1772d1af3d4a511decc8363183e.
3. The map kappa on each component line of C is an isomorphism onto the same smooth rational sextic Gamma: KAPPA-RATIONAL-SEXTIC.md at 3edb50b13b8a5ce876f52a2085ecc8d16b3181c0. It is invariant under the Heisenberg group, which acts trivially on U.
4. The normalizer preserves C and acts on the projective Heisenberg quotient G=F5^2 through SL2(F5). One component L0 is the projectivization of the negative eigenspace of reversal iota; all component lines are its Heisenberg translates. Pinned repository derivation: PR541, research/hm/generic-cubic-primitive-closure/PROOF.md at 9ce30d8d783da881be68548d158ebcb48e122850, Section 3.
5. The primary representation source, read directly, is Horrocks–Mumford (1973), Section 1, printed pp.64–66: the translation and diagonal-character operators on Map(F5,C), irreducibility, character equation (1.2), and reversal x(i) -> x(-i). The line identification is equation (3.6), as used in input 4. Source: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf .

All vectors in the proof below are universal symbolic basis vectors in this published group representation, not selected coefficients of HM evaluation, multiplication, or source matrices. No actual rank or minor is evaluated.

## 1. Reduction of an orbit-five plane to an eigenplane

A plane R in an orbit of size five has an order-five stabilizer in G. By the normalizer's SL2(F5) action, conjugate that subgroup to the diagonal-character subgroup. The normalizer also transports B,S,X_B and C equivariantly, so proving impossibility after this conjugation proves it before conjugation.

Write e_i, i in F5, for the five standard eigenvectors of the diagonal-character generator. Its eigenvalues are distinct. Any invariant three-dimensional vector subspace is therefore a sum of exactly three eigenlines. We may write

R=P(span(e_a,e_b,e_c)), with a,b,c pairwise distinct in F5.

This is a representation-theoretic classification of invariant subspaces, not a selected evaluation.

## 2. Every pair of eigenlines supplies a point on C

Let h_m be the Heisenberg translation acting by e_i -> e_{i+m}. Reversal sends e_i to e_{-i}. Therefore h_m*iota*h_m^{-1} sends e_i to e_{2m-i}. Its negative eigenspace is the translate h_m of the negative eigenspace of iota, so its projectivization is a component L_m of C.

For two distinct indices a,b in the chosen three-element set, put

m=(a+b)/2, d=(a-b)/2 in F5.

Then p_ab=[e_a-e_b] belongs to R and to L_m. Translation h_m^{-1} sends it to

r_d=[e_d-e_{-d}] in L0.

Heisenberg invariance of kappa gives kappa(p_ab)=kappa(r_d). Replacing d by -d gives the same projective point. There are exactly two such points:

r_1=[e_1-e_4], r_2=[e_2-e_3].

They are distinct points of L0, so input 3 gives kappa(r_1) different from kappa(r_2).

## 3. A three-element set supplies both values

The three pairwise differences in any three-element subset of F5 meet both sign classes {1,-1} and {2,-2}. To prove this, suppose they all lay in one class {d,-d}. Translate one member to zero. The two remaining distinct members would have to be d and -d, whose difference 2d is not in {d,-d} in F5, a contradiction.

Division by two permutes these two sign classes. Consequently, among the three points p_ab, p_ac, p_bc in R intersect C, at least one has kappa-value kappa(r_1) and at least one has kappa-value kappa(r_2). Thus R intersect C is not contained in a single fiber of kappa.

## 4. Contradiction with smoothness along the rank-one locus

If R were a residual plane component of X_B, every p in R intersect C would also lie on S because C is contained in S. The integral degree-ten surface S and the plane R are distinct irreducible surface components. Their local union at p cannot be regular. Input 2 therefore forces B=kappa(p) at every such intersection point.

Section 3 supplies two points for which these required values are different. No single B can satisfy both. This contradiction excludes R and hence the whole five-plane residual orbit.

Therefore only the invariant integral quintic residual cycle remains in the degree-ten branch. This is a statement about irreducible components and their fundamental cycle; it does not assert Cohen–Macaulayness of a separately chosen residual subscheme, normality of either component, or a particular intersection multiplicity.

## Boundaries

The proof uses exact group equivariance, the actual line identification, and the already checked kappa isomorphism. It does not replace an actual matrix by a generic one. No coefficient scan, selected source instance, local-model spike, one-shot experiment, or numerical rank computation was used. The surviving degree-ten-plus-integral-quintic case and the integral degree-fifteen case remain open.
