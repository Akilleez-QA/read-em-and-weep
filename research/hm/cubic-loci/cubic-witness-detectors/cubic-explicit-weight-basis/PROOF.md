# An explicit twenty-value cubic basis, without value evaluation

## Result

Use the opposite-cochain weights and literal derivative classes D_i, i in F_5, of [the cubic single witness selection manuscript](../cubic-single-witness-selection/PROOF.md). All index and weight arithmetic below is in F_5, with d=1,2 ordinary representatives. The following twenty actual canonical cubic values form a basis of J3:

    R_(i,d) = f(D_i,D_i,D_(i+d)),       i=0,...,4, d=1,2;
    A_(m,d) = f(D_m,D_(m-d),D_(m+d)),   m=0,...,4, d=1,2.

This specifies values, proves each is nonzero, and proves independence without evaluating any value. It does not normalize their nonzero scalar coordinates.

The resulting 100 once-coordinate multiples span J2, and the 500 twice-coordinate multiples span J1. A coefficient-basis construction below gives an explicit finite indexed family of 17,600 retained upstairs detector values spanning the retained twelve-dimensional target. It is overcomplete; no particular twelve-element basis is selected.

## 1. Imported facts and weight conventions

The following established results are used:

- [the cubic structural nonvanishing manuscript](../../cubic-structural-nonvanishing/cubic-structural-nonvanishing/PROOF.md): f(u,u,w) is nonzero for independent u,w; the image span of the actual f is J3.
- [the cubic massey module reduction manuscript](../../canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md): trilinearity, equivariance, outer reversal f(u,v,w)=f(w,v,u), cyclic zero, and genuine scalar-module multiplication identities.
- [the weight two image sectors manuscript](../../foundation-p05/WEIGHT-SECTORS.md): the distinct J2 weights (b,2b²+epsilon), epsilon nonzero, and its exact permutation transport formulas.
- [the corrected lift theorem](../../foundation-p05b/UPPER-TRANSFER.md): corrected SL5 lifts and equivariant Serre duality without a determinant character for these lifts.

The derivative weights are wt(D_i)=(-i,-i²). Negating the J2 weights under Serre duality gives exactly the twenty one-dimensional J3 weight lines

    (a,3a²+delta),    a in F_5, delta in F_5^×.

Indeed a=-b, and -2b²=3a², with delta=-epsilon. The quadratic diagonal subgroup lies in SL5, so no character factor is missing.

## 2. Repeated-input weights

For j=i+d, the total weight of (D_i,D_i,D_j) is

    a=2i-d,    b=2i²-2id-d²,
    delta=b-3a²=d².

For fixed d, i↦2i-d is a bijection. Values d=1,2 give delta=1,4, respectively. These are precisely the ten square-delta target lines. The structural nonvanishing theorem makes every displayed R_(i,d) nonzero.

Any basis-input triple with exactly two equal indices has square delta, regardless of its ordering. An all-equal triple has delta=0, whose target weight is absent; it also vanishes by cyclic zero. These observations will exclude repeated indices from every nonsquare target weight.

## 3. Distinct-input weights and uniqueness of the arithmetic progression

Every three-element subset of F_5 has a unique midpoint m and an endpoint pair {m-d,m+d}, with d unique up to sign. To see uniqueness, two different choices of midpoint within one triple would force 3 times their difference to vanish, which is impossible. There are five midpoints and two nonzero endpoint pairs, giving ten distinct subsets, which exhaust the ten three-element subsets.

For this unordered triple the total weight is

    a=-3m=2m,
    b=-((m-d)²+m²+(m+d)²)=2m²-2d²,
    delta=b-3a²=3d².

Thus d=1,2 give delta=3,2, respectively, the nonsquares. The ten unordered triples give ten distinct nonsquare target weights: a determines m, and delta determines d up to sign. In particular no other unordered basis-input triple can supply the same nonsquare line.

## 4. Reflection sign, including the matrix-lift audit

Let r_m be the affine permutation i↦2m-i. It has one fixed index and two transpositions, so its determinant is +1. Its ordinary permutation matrix is already its corrected SL5 lift. Formal derivative transport therefore sends D_i to D_(2m-i), without an extra scalar minus sign. (The multiplier-2 generator requires a negative lift, but its square is the unsigned multiplier-4 permutation.)

On J2, the multiplier-2 formulas in the sector proof square to

    e_(p,T,i) ↦ -e_(p,T,-i).

Translations are unsigned on these quotient basis vectors. Conjugating the multiplier-4 permutation by translation therefore gives

    r_m e_(p,T,i) = -e_(p,T,2m-i).

This is also consistent with the recorded stipulated reversal at m=2. No quotient-relation correction is involved: the Z-zero basis is preserved by these actions.

The inverse weight to the AP triple's J3 weight has first coordinate -a=-2m=3m. The J2 basis index is characterized by first coordinate 3i, so this dual line has index i=m. It is therefore fixed by r_m with eigenvalue -1. Equivariant Serre duality for r_m in SL5 has trivial trace character; the dual J3 line also has eigenvalue -1.

Set X=f(D_(m-d),D_m,D_(m+d)). Equivariance and outer reversal give

    r_m X=f(D_(m+d),D_m,D_(m-d))=X.

But its target line has r_m eigenvalue -1. Therefore X=0. This is an exact forced vanishing, not a value calculation.

## 5. Nonzero order classes on every AP set

The image span of f is all J3. Expand its inputs in the basis D_i and use trilinearity. Consequently the span of its 125 ordered basis-input values is J3. Equivariance places each of those values in its total diagonal weight space.

Fix a nonsquare target line. Sections 2 and 3 show that only the six orderings of its unique AP set can contribute to it. They must therefore include a nonzero value, or that line would be missing from the image span.

Outer reversal groups the six orderings into three classes, determined by their middle argument. The class with middle argument m vanishes by Section 4. Cyclic zero makes the other two class values negatives of one another. Hence both are nonzero. One of them is precisely

    A_(m,d)=f(D_m,D_(m-d),D_(m+d)).

Replacing d by -d negates this value; selecting d=1,2 fixes one representative for each endpoint pair. No transitivity assertion or uncomputed reflection character is needed.

The R and A families now give one nonzero vector in each of twenty distinct one-dimensional target weight spaces. They form a basis.

## 6. Explicit finite spanning families for the mixed operations

Let x_0,...,x_4 be the five homogeneous coordinate sections. List the twenty ordered input triples above as

    (u_t,v_t,w_t),  t=1,...,20,
    B_t=f(u_t,v_t,w_t).

Define

    U_(t,l)=m011(x_l u_t,v_t,w_t)=x_l B_t,
    L_(t,l,h)=m001(x_l u_t,x_h v_t,w_t)=x_l x_h B_t.

Here t has twenty values and l,h range from 0 to 4. The multiplication-surjectivity theorem [the koszul cohomology multiplication manuscript](../../foundation-p05b/KOSZUL-MULTIPLICATION.md) gives

    span{U_(t,l)}=J2,
    span{L_(t,l,h)}=J1.

The second conclusion uses surjectivity in both successive coordinate multiplications. These are families of 100 and 500 actual ordered mixed values. Some can vanish or repeat; neither the theorem nor this construction claims otherwise. Keeping ordered l,h avoids an unnecessary symmetry choice, although the scalar products commute.

## 7. Finite coefficient transfer to the complete retained detector

Write C1=V1 for the eleven-dimensional degree-one coefficient-generator space in the canonical filtration, distinct from any historical HM module named V1. Fix a basis c_1,...,c_11 of C1 once. This is a coefficient-space choice, with no Massey calculation.

For a concrete symbolic choice, fix the two standard basis vectors in each of the four two-dimensional factors of H0(Y,O(1,1,1,1)). Let t_S, S⊂{1,2,3,4}, be their sixteen elementary tensors. C1 is the quotient by the five symmetric-tensor sums, one for each cardinality |S|=k. In each cardinality delete the prefix subset {1,...,k}, including the empty subset for k=0. The images of the remaining eleven t_S form a basis: each of the five disjoint-support relations solves uniquely for its deleted tensor. This specifies coefficient directions formally, without evaluating any polynomial or multiplication instance.

Let j:C1⊗U1→K_nt be the inverse of the canonical associated-graded identification. It exists canonically because the S4-trivial subspace K0 splits off by its Reynolds projector and C1 has no trivial summand; see [the filtered massey target manuscript](../../foundation-p04/FILTERED-TARGET.md), Section 2. Let

    P=e_(D8,triv) e_[22] e_+

be the retained dual projector. Take the following finite actual detector family:

    Upper_(t,l,r,s)
      =P M(x_l u_t, j(c_r⊗v_t), j(c_s⊗w_t)),
      20·5·11·11 = 12,100 values;

    Lower_(t,l,h,r)
      =P M(x_l u_t, x_h v_t, j(c_r⊗w_t)),
      20·5·5·11 = 5,500 values.

All multiplied inputs x_l u_t are actual classes in K0=U0. Their possible Euler relations cause no difficulty because these families only need to span.

By the exact lower transfer theorem, the lower family's span equals the canonical four-dimensional lower retained subspace: the C1 basis and the spanning J1 family give the full coefficient tensor image before projection. Lower filtration-zero ambiguity has zero [22] projection.

By the exact upper transfer theorem, the upper symbols are the retained projections of

    mu11(c_r,c_s) ⊗ x_l B_t.

The products of all coefficient-basis pairs span C2, since Sym² C1→C2 is surjective. The once-coordinate multiples span J2. Their indexed independent variation therefore spans the full upper retained quotient of dimension eight. Upper values may have additional lower components; they are not asserted to lie in a selected complementary subspace.

The union of these 17,600 values spans the full twelve-dimensional retained target by the subspace-plus-quotient argument. Accordingly, an actual physical retained class is zero if and only if all its Serre pairings with this finite family vanish. This uses the established perfect sign-valued pairing and the D8-trivial detector projector. It selects neither a minimal twelve-value subset nor a normalized set of scalar tests, and decides no actual physical class.

