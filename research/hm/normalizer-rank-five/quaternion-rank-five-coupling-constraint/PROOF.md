# A full-complement coupling constraint at the quaternion orbit

## Result

Use the standing honest K=SL2(F5) action, V=T⊕W, J+=T⊕P5, dim J−=12, and the outer-symmetric cyclic-zero operation f with repeated-input injectivity. The two three-dimensional A5 representations T and T'=Sym²W are inequivalent. Assume the already proved pointwise odd rank at least five on the canonical conic in P(T).

At every quaternion-axis point p in the unique orbit O375:

- the odd block has rank at least four and even rank;
- the even block has rank at least five;
- if the pure-T cubic operation has nonzero projection to the T summand of J+, the even block has rank at least six.

Consequently residual rank five (total rank nine) at O375 forces the entire K-map S_(2,1)T→T to vanish. In that case its parity ranks are exactly (even,odd)=(5,4).

This is a necessary coefficient-vanishing condition, not an exclusion of O375. It evaluates no actual-operation coefficient or rank instance. All coordinates used below describe the universal A5 orbit, independently of f.

## 1. No cubic contains the fifteen quaternion axes in P(T)

The fifteen axes of the order-two rotations of an icosahedron are the K-orbit of a quaternion fixed line. Here is a direct interpolation proof that their homogeneous cubic ideal is zero.

Put φ=(1+sqrt(5))/2 and realize the rotational icosahedral representation on R³ using vertices (0,±1,±φ) and their cyclic coordinate permutations. The axes through opposite edge midpoints consist of the three coordinate axes and the twelve projective lines represented by independent sign choices and cyclic permutations of (1,φ²,φ). Indeed adjacent vertices have distance two; edges between two different displayed coordinate families give these midpoint vectors, while the remaining six edges give the three coordinate axes. There are thirty edges and hence fifteen antipodal midpoint axes. The other three-dimensional representation is obtained by the other real icosahedral realization; equivalently the same argument can be applied after exchanging the five-cycle classes. Only the unordered image subgroup of SO3 matters here.

Let a homogeneous cubic F vanish on these axes. The coordinate axes kill its three pure-cube coefficients. At the sign choices of any triple (a,b,c) with nonzero entries, independence of the four sign characters on projective sign choices separates F into its x-, y-, z-, and xyz-parity terms. Thus its xyz coefficient vanishes, and if q,r are the coefficients of xy²,xz², then

    q b²+r c²=0.

Apply this to the three cyclic permutations of (1,φ²,φ). Their ratios b²/c² are not all equal, so q=r=0. The same argument kills the y- and z-parity coefficients. Therefore F=0.

## 2. The odd block cannot have rank two

At an axis u, its Q8 stabilizer acts on Cu by a nontrivial one-dimensional character χ. The odd source is T⊗W, of dimension six, twisted by χ when evaluating at u. The central involution acts negatively on both source and J−. Every complex Q8 representation with negative central action is a sum of its unique two-dimensional irreducible. Thus the odd image has even dimension.

If odd rank were at most two, all its three-minors, which are homogeneous cubics on T, would vanish on the entire fifteen-axis K-orbit. Section 1 makes them identically zero on P(T). This would give odd rank at most two on the canonical conic, contradicting the imported rank-five bound. Hence odd rank is at least four (and at most six).

## 3. The two mandatory P5 coefficient maps

Use an invariant metric q and orientation on T. There is the canonical decomposition

    S_(2,1)T ≅ T⊕P5.

Write α and β for the scalars of the pure-T operation on these two multiplicity-one summands. A model for its P5-valued component, up to a fixed nonzero normalization, is

    F5(a,u,b)=a⊙(u×b)+b⊙(u×a),

where ⊙ denotes the symmetric tensor product. Its trace is zero. Its T-valued component is proportional to

    F3(a,u,b)=2q(a,b)u−q(u,a)b−q(u,b)a.

Both obey the required argument symmetries, so these describe all pure-T maps.

The scalar β is nonzero. Otherwise for isotropic nonzero t the map a↦f(t,t,a) on T has image contained in Ct by the displayed F3 formula, whereas repeated-input injectivity requires its kernel to be exactly Ct and therefore its rank to be two.

Now set g(s,t)=f(w1,t,w2) for s=w1⊙w2∈Sym²W=T'. This is a K-map

    g:T'⊗T→T⊕P5.

Since T'⊗T=P4⊕P5, g is a scalar δ times the unique projection to P5. Moreover δ≠0: if g were zero, cyclic zero would give f(w,w,t)=−f(w,t,w)/2=0 for nonzero w∈W and nonzero t∈T, contradicting repeated-input injectivity.

## 4. A genuinely new mixed direction at every axis

The unique nonzero map g:T'⊗T→P5⊂Sym²T may be viewed, using invariant metrics, as a map

    T'→T⊗P5.

The character table gives

    Sym³T=T⊕T'⊕P4,
    T⊗P5=T⊕T'⊕P4⊕P5.

The T' copy in Sym³T is trace-free (contraction lands in the inequivalent T). Thus it lies in T⊗P5, and multiplicity one shows that the above g corresponds to this fully symmetric cubic copy. In particular, if C_s is the cubic associated with s∈T', then, up to one fixed nonzero scalar,

    q(g(s,u)u,u)=C_s(u).

Here a P5 tensor is viewed as a trace-free symmetric operator via q. If q(g(s,u)u,u)=0 for every s at one axis u, equivariance makes every cubic C_s vanish on all fifteen axes. Section 1 contradicts the nonzero T' embedding. Therefore for every axis u some mixed value g(s,u) has nonzero uu matrix entry.

On the other hand every pure-T P5 value F5(a,u,b) has zero uu entry, by orthogonality of u to u×a and u×b. Therefore at least one mixed WW value is outside the complete pure-T image, including when α is nonzero (projection to P5 already detects independence).

## 5. Exact even rank when α=0, and the necessary condition

The axis u is nonisotropic. Choose orthonormal coordinates with u=e1. For β≠0, the pure-T P5 map has rank four: its image consists of the two off-diagonal entries 12 and 13, the off-diagonal entry 23, and the diagonal difference 22−33. Its kernel in Sym²T is spanned by e1² and e2²+e3². The displayed F3 is zero on e1² and nonzero on e2²+e3². Thus the full pure-T map has rank four if α=0 and five if α≠0.

Section 4 increases these lower bounds by one. Hence even rank≥5 always and even rank≥6 if α≠0.

For completeness, if α=0 the even rank is exactly five. Restrict to Q8 and denote the three nontrivial V4 characters by χ1,χ2,χ3, with u of character χ1. The P5 restriction is two copies of the trivial character plus one copy of each χi. The pure-T image has one trivial direction and all three nontrivial directions: this is also immediate from the four matrices just listed. The mixed source Sym²W=T' contains χ1,χ2,χ3 once each, so after twisting by χ1 its image can only add a trivial direction or directions in the χ2 and χ3 target lines already filled. Section 4 supplies exactly one additional trivial direction. Therefore even rank=5.

If total rank is nine, odd rank≥4 gives even rank≤5, forcing α=0. The exact even rank then makes odd rank four. Since rank Q=rank b−4, this proves the stated residual-rank-five constraint.

## Limits and audit request

No claim is made that α is nonzero for the actual normalizer-equivariant operation. Proving its nonvanishing from the full N coupling would exclude O375; local Q8 types do not establish it. Audit should check the universal no-cubic orbit lemma, the multiplicity-one cubic interpretation of g, the pure-T models and their kernels, and the Q8 exact-rank argument when α=0.
