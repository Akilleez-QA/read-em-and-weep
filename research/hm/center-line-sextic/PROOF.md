# The projection-center line maps to a rational ten-nodal sextic

Status: authored structural proof. Independent review, if supplied, is recorded separately. Not formally checked. Work over C.

## Pinned geometric inputs and statement

The objects here belong to the actual primary evaluation maximal-minor scheme, not a fixed-beta surface.

- PR567, commit e0f15a5c6a49d2101dae450dae4d26171a259331, gives the unique integral normalizer-invariant surface S containing the twenty-five distinguished lines. It is smooth near their union. For each such line L, the three ambient linear forms vanishing on L generate the invertible sheaf A=O_S(H-L), defining a morphism f_L:S -> P2. Its restriction to L has A|L=O_L(6).
- PR563, commit 56c3c4c37bd51fc710eec4b80662c5506f357f8f, Sections 3–4, identifies the stabilizer complement I=SL2(F5) and the splitting A_ambient*=B direct-sum C, where B is an irreducible even three-dimensional representation and C a faithful binary two-dimensional representation. The line is L=P(C*). The space of ambient linear forms vanishing on L is B. In particular the projective target of f_L is P(B*), with irreducible three-dimensional A5 action.
- PR562, commit 86b643fe2adecbd321d1c8f98be84fe2082bcd10, gives the stabilizer action on these actual lines. Its quotient G=I/{+1,-1}=A5 acts faithfully on L=P1.

**Theorem.** For every distinguished L, the restriction g=f_L|L is the normalization map of an integral rational plane sextic Gamma_L. This sextic has exactly ten singular points, all ordinary nodes, forming one A5 orbit. Their twenty normalization preimages form one A5 orbit on L. Thus g has injective differential at every point (equivalently, it is unramified), is injective away from those twenty points, and identifies them in ten pairs. It is not a globally injective map or a scheme-theoretic immersion.

The theorem determines the curve coming from the projection center. It does not determine deg(S), the other twenty-four projected lines, or the global singularities of S.

## 1. Equivariance and nondegeneracy

The stabilizer I preserves S and L. The natural equivariant surjection from the three ambient forms through L to O_S(H-L) makes f_L equivariant. The central involution acts scalarly on both L and the three-dimensional target, so this descends to the stated G=A5 actions.

Since g*O_P2(1)=O_P1(6), the map g is nonconstant. Its reduced image Gamma_L is therefore an integral projective curve. Its projective linear span is G-invariant. The irreducibility of the target representation implies that this span is all P2, so Gamma_L is not a line.

Equivalently, the restriction of the equivariant generating space B to H0(L,O_L(6)) is a nonzero map from an irreducible representation, hence injective. No actual coefficients or choice of evaluation point are required for this argument.

## 2. Small source orbits do not exist

For a faithful action of A5 on P1, every point stabilizer is cyclic. Indeed a finite subgroup of PGL2 fixing a point can be written as a finite group of affine transformations after moving that point to infinity. Averaging the orbit of any finite point produces a second fixed point. After translating it to zero the group acts by multiplication, and hence is cyclic.

The only possible element orders in A5 are 1,2,3,5. Thus any cyclic stabilizer has order at most five, and every orbit on L has at least 60/5=12 points. In particular every nonzero effective G-invariant divisor on L has degree at least twelve, since its multiplicity is constant on each orbit.

## 3. Birationality and degree six

Let nu:N -> Gamma_L be the normalization. The nonconstant morphism from the smooth curve L factors uniquely as g=nu composed with h, where h:L -> N is finite of degree e. The smooth projective curve N has genus zero: in characteristic zero Riemann–Hurwitz for h gives

-2=e(2g(N)-2)+deg(R_h), with deg(R_h)>=0,

which excludes g(N)>=1. Hence N is P1. Put m=deg(Gamma_L). Pulling back a general hyperplane divisor gives

6=e m.

By nondegeneracy m>=2. Consequently (e,m) is one of (3,2), (2,3), or (1,6).

Every automorphism of Gamma_L lifts uniquely to its normalization. The uniqueness of normalization factorization then makes h equivariant. Its ramification divisor R_h is therefore G-invariant, whether or not the action on N is faithful. If e=2 or 3, Riemann–Hurwitz gives deg(R_h)=2e-2=2 or 4. These positive degrees contradict Section 2. Thus e=1 and m=6. A degree-one finite map between smooth projective curves is an isomorphism, so g itself is the normalization of a rational plane sextic.

## 4. No target orbit of size at most five

There is no orbit of size one in P(B*), since that would give an invariant line in the irreducible representation B*. There is no orbit of size 2,3,4: its permutation action would give a nontrivial homomorphism A5 -> S_n, which by simplicity would be injective, contrary to n!<60.

Suppose there were an orbit of size five, and let K be a point stabilizer. The coset action embeds A5 in S5. Its image has index two, and therefore is the alternating group. Thus K is isomorphic to A4, with normal Klein four subgroup V and quotient K/V cyclic of order three.

The representation B* of A5 is faithful, and its determinant character is trivial because A5 has no nontrivial one-dimensional characters. Every nonidentity involution therefore has eigenvalues 1,-1,-1, and trace -1. The averaging projection onto V-invariants has trace

(dim(B*)+sum over the three nonidentity elements of V of their traces)/4

=(3-3)/4=0.

Thus (B*)^V=0. But if K fixed a projective point, its representative line would be a one-dimensional K-representation. Every such character is trivial on V, since the commutator subgroup of A4 is V. This would supply a nonzero V-fixed vector, a contradiction. There is no five-point orbit.

Therefore every target orbit has at least six points. Among orbit sizes at most ten, only six and ten are possible, since orbit sizes divide |A5|=60.

## 5. The genus budget forces ten ordinary nodes

A plane sextic has arithmetic genus (6-1)(6-2)/2=10. For the normalization g:L -> Gamma_L the exact sequence

0 -> O_Gamma_L -> g_*O_L -> Q -> 0

has Q supported at the singular points, with length at p equal to the positive integer delta_p. Taking Euler characteristics, since L has genus zero, gives

sum_p delta_p=10.

The finite singular set is G-invariant and delta_p is constant on each orbit. By Section 4 each orbit contributes at least six to this sum, so there is exactly one orbit. Its size is either six or ten. Size six would require 6 delta_p=10, impossible for an integer delta_p. Hence there are exactly ten singular points in one orbit, and each has delta_p=1.

For a reduced plane curve singularity with local analytic branches Gamma_i, the branch formula is

delta_p=sum_i delta(Gamma_i)+sum_{i<j} intersection_multiplicity(Gamma_i,Gamma_j).

In particular delta_p=1 allows at most two branches. If there are two, each is smooth and their intersection multiplicity is one, which is exactly an ordinary node. Branch number is constant on the single singular orbit. If instead every singularity had one branch, its inverse image under normalization would consist of one point. The ten singularities would then give a G-invariant set of ten points on L, contradicting Section 2. Thus all ten singularities are ordinary nodes. This argument does not require a separate classification of cusps.

At a node the normalization has injective differential along each of its smooth transverse branches; elsewhere it is an isomorphism to the smooth curve. Hence g has injective differential at every point. This is an analytic immersion statement, not a claim that g is a scheme-theoretic immersion. The singular inverse image consists of twenty distinct points. Every orbit on L has at least twelve points, so an invariant set of twenty points cannot be a union of two or more orbits. It is one orbit, with the normalization pairing it into ten fibers of size two.

## Contribution, dependencies and scope

The degree-six statement of PR567 is a statement about a pulled-back line bundle, not the degree of its image. Sections 2–3 resolve precisely that covering-degree ambiguity. Sections 4–5 then determine the singular locus and the local analytic type of every singular point of the center-line image. They make no genericity assumption about an arbitrary plane projection: the small-orbit exclusions force the nodal conclusion for this actual equivariant map.

The construction uses only the published geometric and representation-theoretic interfaces, Riemann–Hurwitz, normalization, and the local plane-curve delta formula. It requires no selected actual HM/source evaluation or large computation. It is an ordinary geometric theorem, not a claim of formal verification, a higher-order lifting theorem, a proof of global normality, or a resolution of Q4 or algebraicity.

Public dependencies:

- https://github.com/Akilleez-QA/read-em-and-weep/pull/567 at e0f15a5c6a49d2101dae450dae4d26171a259331.
- https://github.com/Akilleez-QA/read-em-and-weep/pull/563 at 56c3c4c37bd51fc710eec4b80662c5506f357f8f.
- https://github.com/Akilleez-QA/read-em-and-weep/pull/562 at 86b643fe2adecbd321d1c8f98be84fe2082bcd10.
- Riemann–Hurwitz: https://stacks.math.columbia.edu/tag/0C1B .
- The representation inputs are those of the Horrocks–Mumford appendix used in PR563: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf .
