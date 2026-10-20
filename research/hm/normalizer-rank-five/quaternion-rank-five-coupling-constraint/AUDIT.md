# Independent audit of the quaternion-axis coupling constraint

## Verdict

The argument in `PROOF.md` is valid under its stated standing representation-theoretic and geometric assumptions. In particular, the implication

> residual rank five at a quaternion-axis point forces α=0, and then the parity ranks are (5,4)

is supported without using an upper bound of six on the even block. The argument does not prove that α is nonzero for the actual operation and does not exclude the quaternion orbit.

This audit only checks universal identities and representation constraints. It performs no evaluation of the actual operation, its coefficients, or an actual rank instance.

## Checks

### 1. Fifteen-axis interpolation

The edge-midpoint description is correct. Edges within one coordinate family yield the coordinate axes. Edges between coordinate families give, up to scaling, independent signs and cyclic permutations of (1,φ²,φ). There are four projective sign choices for each of the three cyclic permutations, and these twelve lines are distinct from one another and the coordinate axes.

After the coordinate axes kill the pure-cube terms, the four sign characters isolate the three groups xy²/xz², yx²/yz², zx²/zy² and the xyz term. For the first group the three equations have coefficient ratios φ², 1/φ⁴ and φ², respectively. In particular, at least two ratios are distinct, which suffices to kill both coefficients. The same cyclic argument handles the other groups. The proof works over C as well as R.

For the other three-dimensional irreducible, exchanging the two five-cycle classes amounts to precomposing the icosahedral representation with the outer automorphism. This preserves the unordered image subgroup and the set of order-two axes. Thus the interpolation assertion applies to either choice of T.

### 2. Odd rank

Evaluation at an axis twists the source by its line character, but that character is trivial on the center of Q8. The odd source and target therefore retain negative central action. A Q8 module with this central action is a sum of the unique two-dimensional irreducible, so every equivariant image has even dimension.

The entries of the odd block are linear in the evaluation vector. If its rank were at most two at one axis, equivariance would make every cubic three-minor vanish at all fifteen axes. The interpolation lemma would force those minors to vanish identically, contradicting the imported odd-rank-at-least-five assertion on the canonical conic. Consequently the odd rank is 4 or 6; the upper bound is the six-dimensional odd source.

### 3. Pure-T models and mandatory coefficients

Both displayed models are outer-symmetric and have cyclic sum zero. The symmetric tensor F5 has zero trace by cancellation of the two scalar triple products. They are nonzero maps into the inequivalent multiplicity-one summands T and P5 of S_(2,1)T, so they exhaust the pure-T possibilities up to their respective normalizations.

For isotropic nonzero t, F3(t,t,a)=q(t,a)t. Thus β=0 would make the restriction a↦f(t,t,a) on T have rank at most one. Repeated-input injectivity on V/Ct implies that this restriction has kernel exactly Ct and rank two. This proves β≠0.

Outer symmetry makes the mixed WW values factor through Sym²W=T'. The decomposition T'⊗T=P4⊕P5 leaves no T-valued mixed map and precisely one P5-valued map. If its coefficient δ vanished, cyclic zero and outer symmetry would give 2f(w,w,t)+f(w,t,w)=0 with both terms zero, contradicting repeated-input injectivity for w≠0 and t≠0. Thus δ≠0.

### 4. Cubic interpretation and the extra direction

The decompositions Sym³T=T⊕T'⊕P4 and T⊗P5=T⊕T'⊕P4⊕P5 are correct. The T' cubic summand is harmonic because contraction is an equivariant map to T. Its inclusion into T⊗P5 is therefore nonzero, and multiplicity one identifies it, up to a nonzero scalar, with the curried nonzero mixed map g.

Consequently the fully contracted mixed tensor is the nonzero cubic C_s(u), up to common normalization. If every such contraction vanished at one axis, equivariance would make every cubic in this nonzero T' subspace vanish on all axes. Section 1 excludes this. Hence some mixed value has nonzero uu entry at each axis.

All pure-T P5 values have zero uu entry. Projection to P5 alone thus separates the new mixed value from the entire pure-T image, even when the latter also has a nonzero T component. This is the crucial valid reason the mixed contribution increases the full even rank.

### 5. Pure-T rank and the conclusion

At u=e1, the pure-T P5 image is exactly the four-dimensional space spanned by symmetric entries 12, 13, 23 and the diagonal difference 22−33. Its kernel is span(e1²,e2²+e3²). F3 vanishes on the first kernel vector and is nonzero on the second. Therefore the full pure-T rank is four for α=0 and five for α≠0.

The mixed direction established above raises these to lower bounds five and six, respectively. In particular, α≠0 implies total rank at least 6+4=10, or residual rank at least six using the imported shift by four. This establishes the claimed necessary condition freshly, without any even-rank upper-bound assumption.

For α=0, exact even rank five has an even simpler proof than the one supplied: both pure-T and mixed WW values lie in P5, so the full even image has dimension at most five. The preceding lower bound gives equality. The stated Q8 character proof is also correct.

## Additional useful consequence

Under the same assumptions, α=0 forces the residual rank at an axis to belong to {5,7}: the even rank is exactly five and the odd rank is either four or six. More precisely,

- residual rank five is equivalent to α=0 together with odd rank four;
- if α=0 and odd rank six, the residual rank is seven;
- if α≠0, residual rank is at least six.

Thus proving only α=0 would still leave an odd-block condition to settle. In particular, α=0 by itself is not sufficient for residual rank five.

## Scope and dependencies

The proof imports, rather than proves, the honest group action, the identifications V=T⊕W and J+=T⊕P5, the inequivalence T≠Sym²W, repeated-input injectivity, the conic odd-rank lower bound, the interpretation of the quaternion orbit as these axis configurations after the relevant equivariant identifications, and rank Q=rank b−4. Subject to those standing inputs, no blocking mathematical issue was found. The wording “entire map S_(2,1)T→T vanishes” is correct because this Hom space is one-dimensional.
