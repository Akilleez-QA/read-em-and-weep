# A full-equivariant isolated rank-two realization of the length-sixteen family

## The new statement and its boundary

Let R=C[[x1,x2,x3,x4]] and H=mu5 × (B ⋊ C4), with the action and coefficient conventions of the length-sixteen candidate. Choose lambda in C*, lambda^4 != 1, and choose epsilon=-1. Let P be the candidate module with Hilbert function (4,6,4,2).

There exists an explicit H-equivariant reflexive R-module M of rank two, locally free away from the closed point, with an equivariant nondegenerate alternating self-duality, such that

    Ext^1_R(M,R) = P,
    Ext^2_R(M,R) = D(P), where D(P)=Ext^4_R(P,R).

In particular M is nonfree exactly at the closed point and both defects have length sixteen. This resolves the isolated LOCAL realization question for this member of the residual family. It is not a global equivariant sheaf on P4, an actual HM kernel, a source-instance evaluation, or a construction with prescribed global Chern classes. The global rank-eight exclusion is unaffected.

The previously proved candidate normal forms, finite length and H action are the only candidate inputs. No claim of impossibility for all other epsilon choices is needed here.

## 1. Presentation and an invariant symplectic bivector

Use indices i in {1,2,3,4}, reduced modulo five. Put A=R tensor T, with basis t1,...,t4. Let E=R tensor V have ten ordered basis vectors m_i, l_i (i=1,...,4), c1,c2. Define L:E -> A by

    L(m_i)=x_i t_(3i),
    L(l_i)=x_i t_i-lambda x_(-i)t_(3i),
    L(c1)=x1 t4-x4 t1,
    L(c2)=x2 t3-x3 t2.

Thus coker L=P. The relation representation V is O3 + O2 + the clock pair with epsilon=-1; its central mu5 character is trivial. Under the chosen C4 generator g,

    m_i -> m_(2i), l_i -> l_(2i), c1 -> c2, c2 -> -c1.

The B weights of m_i and l_(3i) are negatives: respectively (4i,3i^2) and (i,2i^2). The weights of c1,c2 are (0,3),(0,2), likewise opposite.

Define J: E* -> E by the alternating matrix whose nonzero upper/lower paired entries are

    J[m_i,l_(3i)]=1,  J[l_(3i),m_i]=-1,
    J[c1,c2]=-lambda, J[c2,c1]=lambda.

These pairs have disjoint basis supports. Hence det J=lambda^2, so J is invertible. Every paired tensor has B weight zero; simultaneous cyclic permutation preserves the first four pairings, and c1 wedge c2 is g-invariant because g(c1 wedge c2)=c2 wedge (-c1)=c1 wedge c2. Central characters also cancel. Thus J is H-equivariant.

## 2. Exact isotropy identity

More generally replace the four m/l pairing coefficients by a and the c1/c2 coefficient by b. Direct multiplication gives, in row order t1,t2,t3,t4,

    (L J L^t)_(12) = (a lambda+b)x3 x4,
    (L J L^t)_(13) = -(a lambda+b)x2 x4,
    (L J L^t)_(14) = 0,
    (L J L^t)_(23) = 0,
    (L J L^t)_(24) = (a lambda+b)x1 x3,
    (L J L^t)_(34) = -(a lambda+b)x1 x2.

The lower triangle is the negative transpose and the diagonal is zero. For example the (1,2) entry from the m/l block is a lambda x3 x4, while the clock block contributes b x3 x4. This verifies the sign independently of a determinant or numerical specialization.

Taking a=1 and b=-lambda proves L J L^t=0 identically. This is a universal polynomial identity for the abstract family, not an evaluation of an HM/source instance. The restriction lambda^4 !=1 is needed for P's finite length, not for isotropy or invertibility of J.

## 3. The symplectic monad and reflexivity

Define b=J L^t:A* -> E and K=ker L. The isotropy identity gives im b subset K. Set

    M=K / im b.

Since P has finite length, L is surjective at every nonmaximal prime. Therefore L^t is a split injection there, as is b. Over the fraction field b has rank four; since A* is free over a domain, b is injective everywhere. Off the closed point the symplectic reduction of the rank-ten symplectic module E by the rank-four isotropic direct summand im b is locally free of rank two.

For depth, let I=im L. From 0 -> I -> A -> P -> 0, the depth lemma gives depth I=1, and from 0 -> K -> E -> I -> 0 it gives depth K=2. The exact sequence

    0 -> A* --b--> K -> M -> 0

gives depth M >=2. Any torsion in M would be supported at the closed point, because M is free at every other prime. A nonzero finite-length submodule contradicts positive depth; therefore M is torsion-free. It satisfies S2 at the closed point and at all other primes, hence is reflexive over the regular normal domain R.

The alternating form corresponding to J^{-1} makes K the orthogonal complement of im b. Thus it induces a nondegenerate alternating form on M off the closed point. The associated map M -> M* extends uniquely across the codimension-four point because both are reflexive; the inverse extends too. The extended form remains alternating since it is so on the dense free locus. All maps are H-equivariant, giving equivariantly trivial determinant as well.

## 4. Exact defect calculation

For finite-length P over this regular local fourfold, Ext^j(P,R)=0 for j<4. Dualizing 0 -> I -> A -> P -> 0 therefore gives

    I*=A*, Ext^1(I,R)=Ext^2(I,R)=0,
    Ext^3(I,R)=D(P).

Dualizing 0 -> K -> E -> I -> 0 gives

    0 -> A* --L^t--> E* -> K* -> 0,
    Ext^1(K,R)=0, Ext^2(K,R)=D(P).

Finally dualize 0 -> A* --b--> K -> M -> 0. It gives

    0 -> M* -> K* --b*--> A -> Ext^1(M,R) -> 0,
    Ext^2(M,R)=Ext^2(K,R)=D(P).

The map b* is induced from b^t=L J^t:E* -> A. Because J^t is invertible, its image equals im L. It descends through E*/im L^t precisely because L J^t L^t=0. Consequently coker b*=coker L=P, proving Ext^1(M,R)=P. All identities are equivariant; the duality D already incorporates the canonical-character factor and no extra character is appended.

Since P is nonzero, M is not free at the closed point. Its singular support is exactly that point. Since finite duality preserves length, both Ext modules have length sixteen.

## 5. What is now excluded as an approach

The abstract residual length-sixteen family cannot be ruled out merely by demanding isolated rank-two reflexivity, full H-equivariance, equivariantly trivial determinant, or alternating self-duality: the epsilon=-1 subfamily satisfies all of them. A further exclusion in the global HM problem must use genuinely additional data, such as its global kernel presentation, orbit compatibility, or global Chern/cohomology constraints.

For comparison, the epsilon=+1 clock pair does not admit a nondegenerate invariant alternating form at multiplicity one: g acts on it with determinant -1. Thus the displayed constant-coefficient symplectic ansatz cannot apply to epsilon=+1. This is only an exclusion of that ansatz, not a proof that no other realization of epsilon=+1 exists.

## Verification and dependencies

The candidate presentation, H conventions and finite-length normal forms are in ../length-sixteen-local-defect/CANDIDATE.md; its independently reviewed status is kept separate from this new construction. The present proof derives isotropy, depth, self-duality and both Ext identifications explicitly. A tiny optional symbolic check verifies the six displayed matrix entries, but the proof does not depend on it. No global or actual-source instance is evaluated.

## 6. The next step: uniqueness of the invariant form and a genuine family

For fixed lambda, every H-equivariant constant alternating map V* -> V has the two-parameter shape used in Section 2. Indeed O2 and O3 are distinct dual irreducibles, each of multiplicity one, and neither is dual to the clock pair. Their invariant alternating pairings form one one-dimensional hyperbolic block. The clock pair is an irreducible self-dual two-dimensional representation with g^2=-1 and opposite nonzero B weights, so its invariant alternating pairings form a second one-dimensional block. There are no other invariant blocks.

The isotropy identity forces b=-lambda a. Nondegeneracy then amounts to a!=0, because lambda!=0. Thus the invariant constant symplectic form satisfying isotropy is unique up to scalar. Scaling J does not change im(J L^t), and hence does not change M. The construction therefore has no hidden choice of constant pairing for the fixed presentation.

As lambda varies over C* minus the fourth roots of unity, the resulting M_lambda are pairwise nonisomorphic as H-equivariant R-modules, with the fixed action on R. To see this, an isomorphism would induce an H-equivariant R-isomorphism of Ext^1 modules P_lambda and P_mu. Their common top T=O0, with its fixed central twist, is irreducible: B has four distinct weight lines and C4 permutes them transitively. Schur's lemma makes the induced top map scalar. Hence the induced map on W tensor T, and on its initial linear relation subspace, is the same scalar. In each relevant two-dimensional weight space, that relation subspace is the line

    span{x_i t_i-lambda x_(-i)t_(3i)}.

Equality with the corresponding mu line forces lambda=mu, since both coefficients of the first monomial are normalized to one. Higher-order terms of a filtered isomorphism do not alter this initial degree-one statement. Thus no isomorphism exists when lambda!=mu.

This is a family in the elementary sense of explicit formulas and pairwise distinct equivariant isomorphism classes; no moduli representability, flat universal family over a parameter scheme, or classification of all isolated rank-two defects is asserted. It strengthens the exclusion of a purely local full-H obstruction: there is not merely one accidental local realization.
