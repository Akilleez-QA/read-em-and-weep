# Independent audit of the degree-65 exclusion

## Status and dependencies

PASS. I read the complete final degree-sixty-five-pencil-exclusion/PROOF.md and independently checked the mathematical steps below. The verdict is conditional on the previously audited degree-60 lifting lemma, the normalizer genus lower bound 326, the invariant integral quintic-surface exclusion, and the established Horrocks–Mumford representation identities. No substantive gap or correction was found.

Read sources: degree-sixty-curve-frontier/PROOF.md; quadratic-deficiency-exclusion/PROOF.md and INDEPENDENT_GEOMETRY_AUDIT.md; rank-four-degree-sixty-lower-bound/PROOF.md; rank-four-degree-fifty-equality/PROOF.md; binary-group-genus-thirteen/PROOF.md; cubic-massey-module-reduction/PROOF.md; lower-weight-image-symmetry/PROOF.md.

## Integrality exhausts reducible curves

For a reduced invariant curve of degree65 with no lines or conics, an A-orbit of25 components costs at least75. An A-orbit of5 produces all six distinct stabilizer axes and therefore at least30 components, costing at least90. Every component is A-stable, spans P4, and has degree divisible by5.

A nontrivial component orbit under the perfect quotient G=SL2(F5) has at least5 members. Its common degree is consequently at most13 and is a multiple of5, hence5 or10. The previously established stabilizer estimate gives at least20 members in such an orbit, costing at least100. All components are therefore individually N-stable. The exclusion through degree55 makes each degree at least60, so total degree65 forces integrality. This step does not require first importing the degree60 exclusion.

## Complete series, equations, and numerical bounds

Write L for the pullback of O_C(1) to the normalization X. Faithfulness gives g(X)>=326. Heisenberg central-character divisibility applies to H0(X,L^n), H0(C,O_C(n)), and the relevant Rao spaces for n=1,2,3.

If h0(L)>=10, Castelnuovo in P9 gives pi(65,9)=224, since64=8*8. Thus h0(L)=5 and M1=0.

The degree60 no-cubics argument extends unchanged to degree65: a cubic base locus without surface components would give a degree27 complete-intersection curve containing C. Its reduced surface part has degree at most9. An A-orbit of25 surface components costs at least25, and an A-orbit of5 forces at least30 components through the six stabilizer axes. Both exceed9, using only positivity of component degrees. Every surface component is therefore A-stable; five-divisibility leaves a unique invariant integral quintic surface, which is prohibited. No additional small-degree surface stabilizer estimate is required. Hence I_C(2)=I_C(3)=0 and the general hyperplane section has h(1)=4,h(2)=10.

If h0(L^2)>=25, pi(130,24)=300, because129=23*5+14. Therefore h0(L^2)<=20 and dim M2 is0 or5. If h0(L^3)>=50, pi(195,49)=296, because194=48*4+2. Therefore h0(L^3)<=45 and dim M3 is0,5, or10.

Whenever multiplication M2 --ell--> M3 is injective, the hyperplane restriction sequence gives I_Gamma(3)=0 and h(3)=20. Uniform-position growth gives the lower bounds

    4,10,20,23,29,39,42,48,58,61,65.

Their degree65 deficits sum to

    61+55+45+42+36+26+23+17+7+4=316.

Thus p_a(C)<=316, contradicting g(X)>=326. In particular M2 cannot be zero, so M2=A* has dimension5.

## The zero multiplication case

The mixed identity is V* tensor A*=A tensor (T* direct-sum W'^*), with T of dimension3 and W' of dimension2 irreducible. If multiplication is zero, I_Gamma(3) has dimension5. The audited degree60 extraction/lifting argument applies word for word with65 replacing60:65>27 ensures a base curve contains the full section by symmetric sectional monodromy; five independent cubics and no quadrics force that integral curve to have degree5;65>22 meets the lifting threshold, and65>25 proves uniqueness of the containing quintic surface. This contradicts the invariant-quintic prohibition.

Hence multiplication is nonzero. Since dim M3<=10, isotypic tensor-Hom and irreducibility force M3=A tensor W'^*, and the multiplication map is a nonzero scalar multiple of the unique projection with kernel A tensor T*. This proves the actual multiplication identification, rather than merely identifying an eligible map.

## Rigorous identification of the kernel involution

Indices below are in F5. Use Schrödinger bases x_i of V*, y_j of A*, and a_k of A. The shift sends each index to index+1, and the clock weights are respectively -i,-2j,2k. In V* tensor A* put

    k=2i-j,  r=i-j.

The inverse is i=k-r, j=k-2r. Therefore

    a_k tensor e_r  ->  x_(k-r) tensor y_(k-2r)

identifies the H5 module with A tensor E, for a five-dimensional multiplicity space E.

The central element z=-I of G acts by index reversal on each five-dimensional Schrödinger extension. Here there is no unresolved scalar sign: its action must be plus or minus index reversal, since z has order2 and conjugates both generators to their inverses. Reversal on five indices has determinant+1; its negative has determinant-1. The determinant character on the perfect group G is trivial, so only the positive sign occurs.

Consequently z acts on A tensor E by a_k tensor e_r -> a_-k tensor e_-r, and its action on E is e_r -> e_-r. Its plus eigenspace has dimension3 and its minus eigenspace dimension2. In the HM decomposition E=T* direct-sum W'^*, z acts positively on T* and negatively on W'^*. Thus the projection kernel is exactly the plus eigenspace of residual reflection at fixed k.

Translated to (i,j), that reflection is

    (i,j) -> (3i-2j,4i-3j).

For a decomposable tensor ell tensor y, membership in this kernel is equivalent to equality of the paired coefficients. Substituting i=2j-l gives exactly

    x_(2j-l) y_j = x_(2l-j) y_l   for all j,l.

This is a representation-theoretic kernel calculation; no problem-specific source or rank instance is substituted.

## Generic injectivity

The pairs (j,l)=(0,1),(1,2),(2,0) give

    x4*y0=x2*y1,
    x0*y1=x3*y2,
    x4*y2=x3*y0.

Eliminating y1,y2 without division gives

    (x4^2*x0-x2*x3^2)*y0=0.

On the nonempty open set where all x_i are nonzero and x4^2*x0-x2*x3^2 is nonzero, y0=0. The equations with j=0 then give every y_l=0. The open set is nonempty because the displayed polynomial is the difference of distinct monomials; no explicit coefficient instance is evaluated.

Thus multiplication by a general linear form is injective. Its open condition can be intersected with the usual nonempty open set of transverse uniform-position hyperplanes. The resulting sectional genus bound316 contradicts326. No assertion about special hyperplanes is needed.

## Next-frontier arithmetic

The final proof correctly records pi(140,24)=351, pi(210,49)=356, pi(140,29)=276, and pi(210,54)=309. These allow quadratic Rao dimension10 and cubic Rao dimension15 at degree70. The degree65 argument does not claim to cover this changed situation.

## Scope

Only local proof documents, general representation theory, symbolic identities, and small arithmetic bounds were checked. No physical source, source coefficient, source input, operation matrix, rank instance, or source-app write was used. No actual source-instance evaluation is claimed.
