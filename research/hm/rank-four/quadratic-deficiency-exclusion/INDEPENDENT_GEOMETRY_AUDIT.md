# Independent audit of the degree-60 lifting exclusion

## Verdict

PASS, conditional on the imported degree-sixty frontier, audited Horrocks–Mumford representation conventions, and invariant integral quintic-surface exclusion. I read the complete PROOF.md and the complete frontier proof. No substantive geometric gap was found. The abbreviated descent/family assertion is valid; its precise justification is supplied below. This audit does not independently re-prove the imported representation identity or quintic-surface prohibition.

## Sectional cubic base locus

The no-common-factor argument is valid. Uniform position plus quadratic evaluation rank ten implies every ten-point subset imposes independent quadratic conditions. A common linear factor would leave quadrics through at least 57 points; a higher-degree factor is impossible by dimensions.

Two sufficiently general cubics therefore have a pure complete-intersection curve of degree nine. Every one-dimensional base component is a component of this intersection, giving total reduced degree at most nine. Every isolated base point lies on a component of the complete intersection not contained in the base locus: a point on a base curve is not isolated. Choose the third cubic to avoid all non-base components. Restriction to each such reduced integral component bounds the number of distinct zeros by three times its degree. Adding gives at most 27 isolated points, independently of multiplicities or embedded structure. Thus the use of 60>27 is sound.

## Monodromy and incidence

Full symmetric sectional monodromy is appropriate for the integral complex curve C, including singular C after restricting to smooth transverse intersections. Kadets' paper explicitly records this characteristic-zero fact: https://arxiv.org/abs/1809.07293 . Further nonempty Zariski-open restrictions preserve this monodromy: a connected finite étale cover of a normal integral base remains connected after restriction to a dense open.

The joint finite permutation group G and its two projections are legitimate. Geometric generic components of the relative cubic base locus are defined over a finite separable extension of C(U). Pass to a Galois splitting extension, spread out, and remove its branch locus. After further shrinking, the component families and the point/component incidence relation are constant on the resulting finite étale labeling cover. Hence incidence in a fibre is invariant under the joint monodromy group.

For K=ker(G→S_m), p(K) is normal in S_60. Normal subgroup classification says it is trivial, A_60, or S_60. The trivial possibility would make S_60 a quotient of G/K, which has order at most 9!, impossible. Thus K is transitive on the 60 points while fixing every curve component. A component meeting one point contains all points. This deduction is valid; it does not assume that arbitrary monodromy permutations act geometrically on the ambient P3.

## Degree and uniqueness of the extracted curve

The extracted reduced component D is integral, nondegenerate, quadric-free, and contained in five independent cubics. If e>5, Laudal's lemma excludes a conic through its general plane section. That section has quadratic Hilbert function six, hence cubic Hilbert function at least six. Restriction of cubics through D is injective because I_D(2)=0, contradicting the available dimension at most four on the plane section. The exact integral-curve version of the lemma is also stated in Bothmer–Gallet–Schicho, Appendix B, Theorem B.5: https://arxiv.org/pdf/2012.05120 .

For e≤4, pullback to normalization injects global sections and a degree-2e line bundle on a smooth integral curve has at most 2e+1 sections. Ten ambient quadrics force a nonzero equation. Therefore e=5. There cannot be two such degree-five base components within total degree nine.

## Descent and family construction

Let F=C(U). The unique degree-five geometric generic component containing the full generic hyperplane section is invariant under Gal(Fbar/F), so its homogeneous ideal descends to F. Equivalently its Hilbert point is F-rational. Extend that rational Hilbert-scheme section over a nonempty open of U and pull back the universal family. Its generic fibre is geometrically integral, so shrink once more to obtain geometrically integral fibres throughout; flatness follows from the universal family. The containments in the universal hyperplane and around the universal section also spread after shrinking. The base U is smooth, and U→Grass(3,4) is a dominant smooth open immersion. Thus all required family conditions hold without asserting smoothness or normality of D or C.

## Exact lifting theorem and final uniqueness

I independently downloaded and rendered the original Chiantini–Ciliberto paper, https://numdam.org/item/AST_1993__218__95_0.pdf . Printed page 95 explicitly allows h+n≥r. Printed page 97 has remainder convention 0≤epsilon<r−n−1. Thus n=1 is allowed here, and (s,h,r,n)=(5,3,4,1) gives k=2, epsilon=0 and D=22. The family just constructed satisfies its hypotheses and 60>22 yields the integral degree-five surface.

The downloaded source and independently viewed images are in sources/lifting.pdf, sources/intro.png, and sources/theorem.png in this directory.

Final uniqueness is sound: two distinct integral quintic surfaces have general integral quintic hyperplane curves; if distinct these meet in at most 25 points, by projection to a general plane and plane Bezout. They cannot share 60 distinct points. Equality of general hyperplane sections forces equality of surfaces. Therefore every element of N preserves the lifted surface, contradicting the imported exclusion.

## Scope

Only proof documents, abstract geometry, and published mathematical references were examined. No problem-specific source data, coefficients, input values, or operation matrices were evaluated, and
