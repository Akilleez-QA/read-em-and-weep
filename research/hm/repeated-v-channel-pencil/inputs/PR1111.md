# The marked positive contraction requires at least two intermediate channels

## Scope and actual maps

Work over C with the fixed G=SL2(F5) action. Retain the actual source2 hypotheses of PR1106, its marked V_C in NC2, and the genuine negative projector e0 in degree four. Let V_0=(N0,4)_V and let p_V:N0,4→V_0 be its canonical isotypical projection. Set p=p_V e0. The intermediate space is the actual positive space P3, not an opposite mixed block.

Use the actual positive arrows from PR931 and PR933:

    a:V⊗N2→P3,   b:V⊗P3→N4.

For the inclusion i:V_C→N2 define

    T(x,y,z)=p b(x,a(y,i(z))).

Ordinary multiplication gives T(x,y,z)=T(y,x,z). Neither e0 nor p is extended to P3. The second arrow b remains inside every composition below. Let q be the nonzero invariant positive quadratic defining Q2. Then contraction of T with q is exactly p Q2 i. Under residual-large tau=0, PR1106 proves this map is an isomorphism V_C→V_0.

The new conclusions are:

1. Every nonzero projected T requires at least two effective intermediate channels among 1,V,D. Consequently rank(a restricted to V⊗V_C) belongs to {4,6,8,9}. In particular this holds under residual-large tau=0.
2. There is one exact relation among the three actual channel composites and one further equation for zero invariant contraction, displayed below. No actual channel coefficient is evaluated.
3. If T is nonzero and its invariant contraction vanishes, all three effective channels are nonzero and a restricted to V⊗V_C is injective, of rank9. Thus failure of this first-arrow injectivity makes zero invariant contraction equivalent to T=0, not merely compatible with it.
4. The lower bound4 is sharp for universal commuting representation diagrams. This sharpness example is not an actual HM or source realization.

## Fixed representation normalization

The positive V is the three-dimensional orthogonal irreducible factoring through A5. Choose an invariant nondegenerate symmetric form and an invariant volume normalized compatibly so that x×(y×z)=y(x·z)−z(x·y). These exist because Sym²V=1+D, Λ²V=V and det(V)=1. Choose equivariant isomorphisms V_C≅V and V_0≅V only to write formulas. These choices do not identify their embedded subspaces, and do not identify V_C with A or an opposite mixed constituent.

The first-arrow domain has its canonical decomposition

    V⊗V_C = 1 ⊕ V ⊕ D.

For each summand J define a_J to be a restricted to that summand. Composing a_J with the actual b and p yields the effective J channel. Since V is self-dual,

    dim Hom_G(V⊗J,V)=dim Hom_G(J,V⊗V)=1

for each J=1,V,D. There are no further finite-group invariant tensors: Hom_G(V⊗V⊗V,V) has dimension3. In the chosen normalization the three basis tensors are

    F0(x,y,z)=x(y·z),
    F1(x,y,z)=y(x·z)−z(x·y),
    F2(x,y,z)=y(x·z)+z(x·y)−(2/3)x(y·z).

Here F0 factors through the scalar part of y⊗z, F1 through its alternating part, and F2 through its traceless symmetric part. The latter can be seen by applying the traceless symmetric matrix y z^t+z y^t−(2/3)(y·z)Id to x. The cross-product identity x×(y×z)=F1 gives the alternating factorization. All three tensors are nonzero and hence span their respective one-dimensional channel spaces.

There are therefore uniquely defined scalars c0,c1,c2 for the actual composed map:

    T=c0 F0+c1 F1+c2 F2.

A nonzero cJ implies a_J is nonzero, but the converse need not hold: b and p may kill that first-arrow channel. Thus these coefficients are not inferred from joint positive injectivity.

## Commutativity and invariant contraction

Collecting the three metric tensors gives

    T=(c0−2c2/3)x(y·z)+(c1+c2)y(x·z)+(c2−c1)z(x·y).

Swapping x and y shows that actual commutativity is precisely

    c0=c1+5c2/3.                                      (1)

Indeed the difference is the scalar c0−c1−5c2/3 times x(y·z)−y(x·z), which is a nonzero universal tensor.

For an orthonormal basis e1,e2,e3, contraction with q_metric=Σei² gives

    Σ F0(ei,ei,z)=z,
    Σ F1(ei,ei,z)=−2z,
    Σ F2(ei,ei,z)=(10/3)z.

Consequently

    T(q_metric,z)=(c0−2c1+10c2/3)z=(−c1+5c2)z.        (2)

The repository's canonical q equals a nonzero scalar multiple of q_metric; thus its contraction has exactly the same zero locus. The actual coefficient multiplying (2) is not selected or calculated. Under the residual-large tau=0 hypothesis the exact necessary condition from PR1106 is

    −c1+5c2 ≠ 0,                                    (3)

together with (1). This is a constraint on the actual two-arrow compositions and marked projector, not on free first-arrow maps alone.

## Support and kernel consequences

Equation (1) has nonzero coefficients on all three cJ. No nonzero solution of (1) can have only one nonzero cJ. Thus every nonzero T uses at least two effective channels. Each nonzero a_J is injective because J is irreducible. Their images are disjoint since 1,V,D are pairwise nonisomorphic. The possible dimensions of a first-arrow image containing at least two such summands are exactly among4,6,8,9. This is an allowed-rank statement, not evaluation of an actual-instance rank.

If contraction vanishes, (1) and (2) give

    (c0,c1,c2)=c2(20/3,5,1).

If T is nonzero, c2 is nonzero and every a_J is injective. Thus a:V⊗V_C→P3 is injective. Conversely, if this first arrow is not injective, one irreducible summand is killed. Its effective coefficient vanishes, so simultaneous (1) and zero contraction force all three coefficients to vanish, namely T=0. No converse from first-arrow injectivity to nonzero contraction is asserted.

As a useful companion, if precisely two effective channels survive, both the invariant and the non-invariant positive quadratic components of the projected T are nonzero. For the non-invariant component, write the symmetric tensor as

    T=α[x(y·z)+y(x·z)]+β z(x·y),
    α=c1+c2, β=c2−c1.

Its traceless-coordinate component vanishes exactly when α=0. Equations (1) and α=0 force (c0,c1,c2)=c2(2/3,−1,1), again all nonzero unless T=0. This statement concerns the projected T, not the entire image of q_D.

## Sharpness and remaining dependency

For universal sharpness take an abstract intermediate U=1⊕V, first arrow

    a(y,z)=(y·z,y×z),

and second arrow b(x,(s,t))=s x+x×t. Then

    b(x,a(y,z))=x(y·z)+y(x·z)−z(x·y)

is symmetric in x,y, has nonzero invariant contraction −z, and the first arrow has image1⊕V of dimension4. A three-term graded module with these arrows, zero higher arrows, and zero action below its source satisfies the relevant commutation relation. This is only a universal representation diagram showing the support bound cannot be improved from the local commutativity condition alone. It does not satisfy or claim to satisfy all actual HM/source constraints.

The actual residual-large tau=0 alternative is not excluded. To exclude it using this comparison, one still needs a structural vanishing or relation for the actual composites p b(Id⊗a_J), beyond (1), forcing the scalar in (2) to vanish. Neither the known joint positive injectivity nor character agreement selects these composites. No actual HM/source coefficient, point, parameter, derivative, jet, matrix or instance rank was evaluated. No higher-order or algebraicity conclusion is made.

## Immutable dependencies

- PR1106, 26ab0ded8bbe635d8aa81798e8fe8a6032e81ce2, research/hm/source2-pure-v-canonical-q-terminal/PROOF.md: actual V_C, projector and conditional nonzero contraction.
- PR931, e28d3b74d4288239426ad1e675e806310fadf8be, research/hm/positive-reachable-middle/PROOF.md: actual a, middle character and V⊗V=1+V+D.
- PR933, 804661fb49e245a8df884937bb8d38fb5d0dc17a, research/hm/positive-double-line/PROOF.md: actual b, two-step positive multiplication and Sym²V=1+D.

The proof is structural. The bounded checker verifies all universal tensor coefficients and channel-support implications, not an actual source instance.
