# What extending every full-character Ext² class actually implies

## Conclusion

Under the inputs in the [canonical Massey theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/721fdc556714bb40f0a805f01fae51cf6d555fd5/research/hm/cubic-loci/foundation-p04/CANONICAL-MASSEY.md), [ordered-product theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/ORDERED-PRODUCTS.md), and [relative obstruction-bundle theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/92ccceb1a023dd86bf4d17f4b86b779cc1b7c44f/research/hm/relative-models/relative-obstruction-locus/PROOF.md), extending every full-character class R along the smooth invariant coefficient family yields the mixed identity

    m(R,a,b) + m(R,b,a) + m(a,R,b) = 0.

Its pairing with every c in K is exactly the already-established reversal/cyclic identity for the invariant ordered operation M. Perfect Serre duality makes these constraints equivalent. This specific second-order family-extension argument therefore supplies no additional condition on M and does not prove M=0. This is a bounded exclusion of this shortcut, not a completeness theorem about geometric constraints, higher orders, or other constructions. No geometric nonvanishing is asserted.

All statements below are formal cochain calculations. Formal coefficients describe the existence of an already-established family; no actual source, model, point, jet, residual, or detector is evaluated.

## 1. Inputs and character conventions

Use the deck-character-graded Dolbeault DGA A of End E on the fourfold X, in characteristic zero. Its differential has degree +1, with d(xy)=dx·y+(-1)^|x|x·dy. Write 1 for the invariant deck character and χ for the full deck character, and put

    K=H¹(A)_1, T=H²(A)_1, V=H²(A)_χ.

The ordered-product addendum proves K K=0. The relative theorem supplies perfect Serre pairings

    H³(A)_χ × K → H⁴(O_X)_χ,
    V × T → H⁴(O_X)_χ,

and V is the fiber of a locally free relative cohomology sheaf commuting with arbitrary base change along a smooth family whose tangent image is K. These are imported geometric inputs. The invariant Ext row (1,79,352,0,0) is now independently proved in https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/INVARIANT-COHOMOLOGY.md, using the independently identified classical presentation and published classical cohomology theorem; no historical finite-model numerical premise is reintroduced here. The actual presentation identification, existence of the family, and relative local-freeness/base-change arguments remain inherited inputs, not new certifications in this note.

Fix a nonzero volume form to turn the top trace into a scalar functional I. For homogeneous cochains of total degree four,

    I(xy)=(-1)^(|x||y|)I(yx),  I(dz)=0.

Before trivialization the target line has deck character χ and geometric S4 sign character. No additional S4 sign belongs in the graded cyclicity formulas below: that character describes equivariance under geometric transformations, not interchanging cochain factors.

The scalar cohomology H¹(O_X)_1 and H²(O_X)_1 vanish. Also H²(O_X)_χ=H³(O_X)_χ=0: by Künneth the full character of the four elliptic factors occurs in scalar cohomology only in degree four. These last two vanishings are needed for the mixed rank-two reversal argument.

## 2. Both mixed cup products vanish, for every R

For R∈V and a,b∈K, associativity and graded cyclicity give

    I((Ra)b)=I(R(ab))=0,
    I((aR)b)=-I(R(ba))=0.

Perfectness of H³_χ against K implies Ra=aR=0. This applies to every class in V, not only a specified residual or a representation subspace. It is crucial for all subsequent primitive-independence claims.

## 3. Canonical mixed operations

For homogeneous closed x,y,z with both neighboring products exact, choose character-homogeneous primitives dh_xy=xy, dh_yz=yz and define

    m(x,y,z)=[x h_yz+(-1)^(|x|+1)h_xy z].

The differential of this expression is zero. Primitive changes have indeterminacy

    x H^(|y|+|z|-1)_(char(y)char(z))
       + H^(|x|+|y|-1)_(char(x)char(y)) z.

For the three placements of one V input and two K inputs, these are sums of V K or K V; for the outer V placement one summand is V K with the degree-one factor in K. All vanish by Section 2. Hence the operations are singleton cohomology classes in H³_χ.

For completeness, representative changes are harmless with the following updates. Put p=|x|, q=|y|. Replacing x by x+dξ and h_xy by h_xy+ξy changes the defining cocycle by d(ξh_yz). Replacing z by z+dζ and h_yz by h_yz+(-1)^q yζ changes it by (-1)^q d(h_xy ζ). Replacing y by y+dυ, h_xy by h_xy+(-1)^p xυ, and h_yz by h_yz+υz leaves it unchanged. These formulas plus primitive independence establish representative independence. Linear sections of cycles and boundaries prove trilinearity.

All primitives must stay in the prescribed deck character. Arbitrary unrestricted primitives have larger indeterminacy and are not justified by this argument.

## 4. Rank-two identities and their exact hypotheses

Rank-two adjugation τ(u)=tr(u)Id−u satisfies

    τ(xy)=(-1)^(|x||y|)τ(y)τ(x), dτ=τd.

The scalar vanishings in Section 1 permit trace-free closed representatives r,a,b of R,a,b. They also imply τ=−id on H³_χ. Choose primitives p_ab with dp_ab=ab and τp_ab=−p_ba, and choose u_a with du_a=ra. Put v_a=τu_a, so dv_a=ar and τv_a=u_a. The normalization of p is achieved by averaging an arbitrary bilinear primitive with its reversed adjugate; no assertion that every primitive is trace-free is needed.

In this system,

    m(r,a,b)=[r p_ab−u_a b],
    m(a,r,b)=[a u_b+v_a b],
    m(a,b,r)=[a v_b+p_ab r].

Applying τ and using τ=−id on H³_χ yields

    m(a,b,R)=−m(R,b,a),
    m(a,R,b)=m(b,R,a).

In particular the mixed outer-reversal sign differs from the all-degree-one outer-reversal sign. The difference is forced by degree, not by a choice of Serre trivialization.

## 5. Why a relative extension exists

A vector bundle of relative H²_χ classes admits local sections through every fiber vector R. After shrinking the smooth base near the chosen point, choose such a section. Arbitrary base change transports it to the formal two-parameter base in any two prescribed tangent directions a,b. Smoothness and the tangent isomorphism ensure the existence of the corresponding formal map to the coefficient family.

A relative cohomology class has a cocycle representative in the corresponding relative complex. In an equivariant smooth trivialization of the underlying family, the differential is d_η=d+[η,−], where η has degree one and satisfies dη+η²=0. Finite-group equivariance allows the representatives and trivialization to respect deck characters. The initial representative can be arranged to equal any fixed r by an exact adjustment. Thus relative local freeness and base change really do furnish the closed family cochain used below, rather than only unrelated pointwise classes.

No canonical extension of R, flat connection on V, or assertion that the actual residual is constant is needed. The argument uses the existence of some extension of every R.

## 6. Second-order closedness, with all choice terms accounted for

Use formal parameters t,s and write only the relevant coefficients:

    η=ta+sb+ts e+…,
    r(t,s)=r+t x+s y+ts z+… .

The Maurer–Cartan equation and relative closedness give

    de=−(ab+ba),
    dx=ra−ar, dy=rb−br,
    dz=−(a y−y a+b x−x b+e r−r e).

One may replace e in the cohomological obstruction expression by −p_ab−p_ba: the difference is a closed invariant degree-one cochain, whose products with R vanish in cohomology. Likewise replace x by u_a−v_a and y by u_b−v_b: their differences are closed full-character degree-two cochains, whose products with K vanish. Thus these replacements do not assume that a chosen extension has specially normalized first derivatives. They use precisely Section 2.

Set

    A=m(R,a,b), B=m(R,b,a), C=m(a,R,b),
    D=m(b,R,a), E=m(a,b,R), F=m(b,a,R).

Expanding the obstruction in the last closedness equation, with these replacements, gives

    A+B+C+D−E−F=0.

Section 4 gives D=C, E=−B, F=−A. Consequently, in characteristic zero,

    A+B+C=0.

There is no missing first-derivative term: arbitrary derivative classes disappeared using their already-proved products with K. There is also no extra condition arising from requiring r(t,s) to remain in character χ; the whole construction and all primitives respect this grading.

## 7. Pairing the mixed operations

The all-degree-one operation is M(a,b,c)=[a p_bc+p_ab c]. The trace identities, including their signs, are

    I(m(R,a,b)c)=I(R M(a,b,c)),
    I(m(R,b,a)c)=I(R M(b,a,c)),
    I(m(a,R,b)c)=I(R M(b,c,a)).

For the first, integration by parts gives

    −I(u_a b c)=−I(u_a d p_bc)=I(d u_a p_bc)=I(r a p_bc).

For the third, graded cyclicity and integration by parts give

    I(a u_b c)=−I(u_b c a)=−I(u_b d p_ca)=I(r b p_ca),
    I(v_a b c)=I(v_a d p_bc)=−I(a r p_bc)=I(r p_bc a).

These establish the displayed identities with no suppressed signs. The second is the first with a,b exchanged.

Pairing the extension relation with c therefore yields

    I(R [M(a,b,c)+M(b,a,c)+M(b,c,a)])=0.

But outer reversal gives M(b,a,c)=M(c,a,b), so the bracket is exactly the existing cyclic-zero relation. Conversely, that cyclic relation and the displayed trace identities imply that A+B+C pairs to zero with every c∈K; perfect H³_χ–K duality then gives A+B+C=0. Thus the mixed family-extension identity and this already-known invariant cyclic identity are equivalent, given the rank-two and pairing inputs.

The perfect V–T pairing does not strengthen this to M=0: it kills only the displayed sum, which already vanishes, not each summand separately. Requiring extension for every R does not change that logical limitation.

## 8. Scope

This calculation excludes only the proposed second-order argument from the existence of arbitrary relative Ext²_χ extensions. It does not rule out extra information from distinguished extensions, extra structures, higher-order compatibility, a separate geometric theorem, or a different detector. It neither proves M nonzero nor proves any residual nonzero. It does not require the actual residual-section premise of the relative theorem: its vector-bundle and base-change conclusion suffices.

## 9. Exact public dependencies and reuse

- [PR179 coefficient family](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/COEFFICIENT-FAMILY.md): smooth coefficient base and invariant tangent image, with the invariant identification in the same foundation.
- [PR179 ordered invariant products](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/ORDERED-PRODUCTS.md): K K=0, stronger than polarized vanishing alone.
- [PR179 independent invariant cohomology](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/INVARIANT-COHOMOLOGY.md): the geometric dimension input; no historical numerical evaluation is reintroduced.
- [PR185 canonical Massey theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/721fdc556714bb40f0a805f01fae51cf6d555fd5/research/hm/cubic-loci/foundation-p04/CANONICAL-MASSEY.md): rank-two adjugation, outer reversal and the existing cyclic-zero relation. These are reused, not new conclusions here.
- [PR252 relative obstruction-bundle theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/92ccceb1a023dd86bf4d17f4b86b779cc1b7c44f/research/hm/relative-models/relative-obstruction-locus/PROOF.md), §§1–5: local freeness and arbitrary base change under geometric presentation and cohomology premises P and D only. Its extra actual-source premise S and residual zero-scheme conclusions are not used.

The distinct derivation is Sections 2–7: all mixed products, canonical mixed operations, corrected second-order expansion, three signed trace transpositions, and equivalence with the pre-existing cyclic relation. This boundary supplies no additional vanishing and makes no claim that these are all possible geometric constraints.
