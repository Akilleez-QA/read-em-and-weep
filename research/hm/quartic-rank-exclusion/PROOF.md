# Excluding the constant fifteen-quartic-generator case by a span obstruction

## Status and inputs

This is a structural proof of the exclusion of the constant fifteen-quartic-generator case. Its uniform consequence uses the separately established jump-divisor classification. No selected actual source-instance evaluation is involved.

Use the actual family and bundles of [PR519, commit cf328c6b0d05551a52911a3a4ba420c68f6fcc6f](https://github.com/Akilleez-QA/read-em-and-weep/blob/cf328c6b0d05551a52911a3a4ba420c68f6fcc6f/research/hm/gorenstein-flat-family/PROOF.md), with S=Sym(T), dim T=5, P=P(W), dim W=2, and J_d fibers (T_w)_d. Write

C=(T I_3) O_P, rank C=40;
B=J_4/C;
Q=J_4/(I_4 O_P)=10O_P(-1).

The canonical map f:T tensor (J_3/I_3 O_P)->B has fiber cokernel dimension a(w). The target B has rank25 and fits 0->15O_P->B->Q->0.

[PR516, commit 89b66cbede7513c4f196fdbda0ee3bb77c53d2e0, Section 1](https://github.com/Akilleez-QA/read-em-and-weep/blob/89b66cbede7513c4f196fdbda0ee3bb77c53d2e0/research/hm/gorenstein-resolution/PROOF.md) proves that T_w/I is generated in degree three, uniformly in w. This follows from the two-layer extension of the dual column module, itself generated in degree three. Therefore the composite f->Q is fiberwise surjective. It is consequently a surjective bundle map.

## 1. Cubic relations collectively span all cubics

The annihilator of J_3,w inside S_3^* factors through R_3^*=(S_3/I_3)^*. In the actual binary model of PR519 this annihilator is

E tensor w^2 Sym^2(W) subset E tensor Sym^4(W)=R_3^*,

where E has dimension five. The intersection over all lines Cw of w^2 Sym^2(W) is zero: a nonzero binary quartic cannot be divisible by the squares of infinitely many pairwise nonproportional linear factors. Hence the intersection of the annihilators of J_3,w is zero. Finite-dimensional duality gives

span_{[w] in P} J_3,w = S_3.

Multiplication by T now gives

span_{[w] in P} T J_3,w = T S_3=S_4,

which has dimension70.

## 2. Constant a=15 would force a smaller span

Suppose a(w)=15 everywhere. Then f has constant rank10, so its image M is a rank10 subbundle of B. Since f->Q is surjective, M->Q is a surjection between bundles of equal rank, hence is an isomorphism. In particular M is isomorphic to 10O_P(-1).

Let E_0 be the inverse image of M under J_4->B. There is an exact sequence of bundles

0 -> C -> E_0 -> M -> 0.

It splits as an ordinary sequence because Ext^1(O_P(-1),O_P)=H^1(P,O_P(1))=0. Thus

E_0 is isomorphic to 40O_P direct sum 10O_P(-1).

The inclusion E_0->J_4->S_4 O_P is a bundle morphism. Under any such ordinary splitting, its restriction from each O_P summand is a constant vector in S_4, while its restriction from each O_P(-1) summand has two vector coefficients, because H^0(P,O_P(1)) has dimension two. Therefore the total vector space spanned by all fibers of E_0 inside S_4 has dimension at most

40+2*10=60.

Every fiber T J_3,w lies inside E_0,w, by the definition of f and E_0. Section 1 then forces a 70-dimensional vector space to lie in this at-most-60-dimensional span, a contradiction. Thus a cannot be constantly15.

No graph-vanishing statement was needed. M can be a nonzero graph under a splitting B=15O_P direct sum Q; its abstract bundle type is still Q, and the extension E_0 still splits. In particular, this proof requires neither normalizer-equivariant splittings nor the identification of the constant multiplicity space with a specific three-dimensional binary icosahedral representation.

## 3. Consequence with the jump-divisor classification

The [quartic jump-divisor classification, commit c56173aab6e9e5d7be2f2f638d6f953c9d7f93b1](https://github.com/Akilleez-QA/read-em-and-weep/blob/c56173aab6e9e5d7be2f2f638d6f953c9d7f93b1/research/hm/quartic-jump-divisors/PROOF.md) says that a is constant in {0,5,10,15}, or is generically zero and equals five exactly on the unique size12 orbit. Section 2 removes constant15. Therefore the surviving list is:

- constant a=0,5, or10;
- generic a=0, with a=5 exactly on the size12 orbit.

In particular a(w)<=10 uniformly. This conclusion still does not determine the actual generic rank or the existence of the exceptional orbit.

Even without the jump classification, generic a=15 is impossible: the uniform bound a<=15 makes rank(f)>=10 everywhere, while generic rank10 bounds every fiber rank above by10. Thus generic a15 would imply constant a15 and yield the same contradiction.

## Verification boundaries

All arguments are structural and ordinary bundle-theoretic. The only additional input beyond PR519 is the already proved degree-three generation of T_w/I from PR516. There is no missing normalizer representation identity. Independent review is recorded separately; this proof has not been formally checked by a proof assistant. No computation of a selected actual matrix rank, coefficients, source-instance value, or large search was performed.
