# Independent audit: finiteness of limiting support hyperplanes at rank two

Status: PASS. The producer's `ADDITIONAL_RANK_TWO.md` has been read, including its optional uniform bound of six, and all claims have been independently verified. The argument below rules out a positive-dimensional set of limiting support hyperplanes at a residual-rank-two point. It does not assert uniqueness there, and makes no exclusion claim at rank one.

## 1. Fixed-point setup and correction continuity

Fix a middle point b. Put E=V/U_b, so dim E=4, and suppose rank Q_b=2. Then K=ker Q_b⊂Sym²E has dimension eight, and its annihilator pencil P=K^⊥⊂Sym²E* has dimension two.

Every limiting support three-plane A⊂E carries a limiting five-plane K_A⊂K∩Sym²A. Existence of K_A is justified by closing the augmented graph recording both the support and the five-dimensional kernel, then using proper surjectivity onto the support graph. Closed incidence gives both containments.

There is a well-defined linear correction v:K→E at b, satisfying square avoidance. Locally near b, a regular left inverse to the everywhere-injective repeated-input bundle map extends the correction to the entire ambient Sym²(V/U). Therefore the good-locus support relation passes to every augmented graph limit:

    v(K_A)⊂A.

This statement does not assume constant rank of Q near b. Its proof is detailed in `AUDIT.md` under rank-three uniqueness.

## 2. Infinitely many limiting supports force a pencil of rank at most two

Restriction P→Sym²A* has rank at most one, since its kernel annihilator K∩Sym²A has dimension at least five inside the six-dimensional space Sym²A. Thus some nonzero q∈P vanishes identically on A. If a∈E* defines A, the homogeneous polynomial q is divisible by a, so q=aℓ for a linear form ℓ and has rank at most two.

The limiting-support set is projective. If it has positive dimension, choose a projective curve of distinct supports. Every fixed nonzero quadratic polynomial has at most two distinct linear factors. Consequently infinitely many different members [q]∈P(P) occur. The condition rank q≤2 is closed in this projective line, so every member of P has rank at most two.

## 3. Elementary classification of such quadratic pencils

Claim: a two-dimensional space P of quadrics of rank at most two either lies in Sym²M for a two-dimensional subspace M⊂E*, or has the form ℓM for a fixed nonzero ℓ∈E* and a two-dimensional M⊂E*.

First, the pencil has rank-two members. Otherwise two independent rank-one members, written as squares of independent linear forms over C, would have a rank-two sum. Choose two independent rank-two members. Factor them as

    q0=xy,    q1=lm,

where x,y are independent, as are l,m. If the combined span of x,y,l,m has dimension four, the sum q0+q1 has rank four, a contradiction. If that span has dimension two, P lies in its symmetric square, proving the binary case.

In the remaining case choose a third linear form z and write

    l=ax+by+cz,    m=dx+ey+fz,

with at least one of c,f nonzero. Every q0+tq1 has zero determinant as a ternary quadratic form. With the convention that xy has symmetric matrix entries 1/2 in positions (1,2) and (2,1), the coefficient of t in its determinant is −cf/4. Thus cf=0. Interchange l and m if necessary to assume c≠0 and f=0. Now the determinant is exactly

    det(q0+tq1)=t² c² d e/4.

Hence de=0. Since m is nonzero, it is proportional to x or y. Therefore q0 and q1 share a linear factor, giving P=ℓM with dim M=2. This completes the classification without invoking an unproved classification of larger linear systems.

## 4. The moving hyperplanes form one pencil

In the binary case P⊂Sym²M, every linear factor of every nonzero member lies in M. This follows by factoring the binary polynomial over C, or by uniqueness of factorization in the full polynomial ring. Therefore every limiting support has defining form in M.

In the common-factor case P=ℓM, every factor is either the fixed ℓ or a member of M. Thus the factor locus is contained in the projective line P(M), together with the possible isolated point [ℓ]. A positive-dimensional irreducible family is therefore the full line P(M) in both cases.

Set W=ann(M)⊂E, of dimension two. Every q∈P vanishes on W: in the binary case both factors vanish there, and in the common-factor case its M-factor does. Thus Sym²W⊂K.

For a general varying hyperplane A=ker(a), [a]∈P(M), restriction of P to A has rank exactly one. Rank zero would mean that a divides every member of P. There is at most one such common-factor direction: two distinct common linear factors would force every degree-two member to be a scalar multiple of their product, contrary to dim P=2.

For such a general A,

    dim(K∩Sym²A)=6−1=5,

so K_A=K∩Sym²A. Since W⊂A and Sym²W⊂K, it follows that Sym²W⊂K_A. Correction continuity therefore gives v(Sym²W)⊂A for all general A in the hyperplane pencil. Their intersection is exactly W, whence

    v(Sym²W)⊂W.

## 5. Square-avoidance contradiction and exact conclusion

The expression e↦e∧v(e²) is a homogeneous binary cubic with values in det W. It has a nonzero zero over C, including when it is identically zero. For that e, e²∈K and v(e²)∈Ce, a compatible square forbidden by the repeated-input hypothesis.

Thus the limiting-support set at a rank-two point cannot have positive dimension. As a closed subset of a projective variety, it is finite as a set. Nonreduced zero-dimensional structure is irrelevant to this conclusion. The argument does not exclude more than one isolated limiting support.

Combining this with uniqueness at residual ranks at least three, and with the positive flag-Chern boundary argument, gives the precise strengthening:

    If the bad middle locus of B is finite, some bad point of residual
    rank at most one has a positive-dimensional family of limiting
    support hyperplanes.

No assertion about impossibility or uniqueness at residual rank one follows from this audit.

## 6. Verification of the optional numerical bound

The producer's supplement additionally claims at most six distinct limiting supports at a rank-two point. This is valid. If the pencil is not entirely of rank at most two, one of its 3×3 minors is a nonzero homogeneous cubic on P(P). Every rank-at-most-two member is among its at most three distinct roots, and each member has at most two distinct linear factors. Thus there are at most six candidate supports, and in particular at most six limiting supports.

If the whole pencil has rank at most two, the classification above applies. Apart from at most one support defined by a common factor of all members, every possible support lies in the pencil with base W and has restriction rank one. Any two distinct nonexceptional limiting supports A and B would force Sym²W⊂K_A∩K_B and v(Sym²W)⊂A∩B=W, producing the same forbidden compatible square. There is therefore at most one nonexceptional support and at most one exceptional support, giving at most two in this case.

The uniform bound six counts distinct geometric limits. It is not a bound on fiber length, intersection multiplicity, or the number of irreducible components of a resolution fiber.

All calculations above are symbolic universal algebraic geometry.
