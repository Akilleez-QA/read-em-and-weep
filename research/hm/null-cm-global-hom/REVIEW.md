# Independent CM hyper-Ext audit

## Verdict

The proposed strengthening is mathematically sound, **conditional on accepting the authenticated historical exact-computation receipt for identity A** and on identifying the geometric bundle in question with the explicitly constructed cohomology bundle below. The global-cover claim is independently verified by literal degree/support inspection. There is no remaining spectral-sequence lifting gap. In particular, for that constructed bundle the result is stronger than failure of equivariant descent:

- Hom on P4 from E to S*E is zero.
- Hom on the complete elliptic fourfold X from F to sigma*F is zero, where F=N tensor f*E.

These are ordinary global bundle Hom spaces, with no equivariance condition. They do not rule out rational gauges, maps on proper open subsets, or arbitrary unrelated bundles called F. No detector value or production/source execution follows.

## 1. Exact object and imported premise

Work over C (the coefficient obstruction already holds over any characteristic-zero extension of Q). Let K in cohomological degrees −1,0,1,2 be

    5 O(−1) --gamma--> 15 O --delta--> 10 O(1) --ev--> 2 O(2).

All three differentials use exactly the pinned model, degree-one homogenization of each literal polynomial. Model SHA256 is 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926. We do not silently substitute a different HM presentation.

The imported premise is the truth of all six homogeneous identities

    gamma H0 + I P + H1 delta = identity15.                 (A)

The authenticated receipt is the historical 1350-entry E_identity computation at commit 08b73637d4136f91606aad332c46cafd064417f8, already bound to this identical model and to the historical homogeneous producer. Its SHA256 is 55e78bbc838a971b64531379788192acf8877c04f2d797fb13b4f4a68e47b018. A is NOT independently recomputed in this audit. Authentication establishes binding, not mathematical validity of the claimed execution. See the [receipt](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/certificates/homogeneous-identities.json) and [producer](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/checks/verify_homogeneous_identities.py).

## 2. Independent global-cover audit

Put h_j=v_j^5−v0v1v2v3v4. The opens D(h_j), j=0,...,4, together with D(v0v1v3v4), cover P4: if all h_j vanish, all v_j^5 equal their product. A zero coordinate would force every coordinate to be zero, impossible projectively. Thus at such a point every coordinate is nonzero and the auxiliary open contains it.

Each h_j is divisible by v_j. Thus D(h_j) makes its specified pivot v_j invertible. The auxiliary carrier has pivot v0, also invertible. This fact is essential for W, L, eta, in addition to the four stored primitives.

The independent script checks every numerator monomial's degree against its weight, and all denominator supports, for I, P, H0, H1 on all six carriers. Under the authenticated homogenization rule, denominator degree D, entry weight w and numerator degree d give extra v0 denominator exponent max(0,d−D−w). Bounds are at most 1 on chart0, 0 on primary charts1–4, and 2 on the auxiliary chart. Homogeneous denominators are:

- chart0: v1v2v3v4−v0^4 = −h0/v0;
- charts1–4: v0v1v2v3v4−v_j^5 = −h_j;
- auxiliary: −v1^2 v3 v4.

Consequently all primitive entries are regular sections of their stated twists on these opens. Chart0 and auxiliary absorb any extra v0 poles because v0 is invertible there. W has entries 1 and −v_r/v_p, L has constant selector entries, eta has entries 1/v_p. They too are regular maps of the appropriate twists on the cover.

The I columns have weights 0 and 1, P rows 0 and −1; thus their intermediate rank-two bundle is O direct-sum O(−1), restricted to the chart. It is trivializable there since the pivot is invertible. H0 and H1 have weight −1. One must retain these twists or trivialize them before interpreting the block inverse as an ordinary square matrix.

The audit independently verifies B: the two selected columns p and 5+p of each H1 numerator are literally zero. Hence H1 eta=0. It also independently verifies C: each nonzero delta block-column has exactly the skew support epsilon(v_s e_r−v_r e_s) against ev's literal row (v0,...,v4), proving ev delta=0 abstractly by commutativity. Neither check forms physical polynomial-matrix products.

Given A, the pivot split gives U=(gamma,I,H1 W) and Q=(H0;P;L delta) with UQ=identity15. Over a commutative ring, a square right inverse is also a left inverse, after local trivialization. Reading QU proves all required contractions; C then gives delta gamma=0, delta I=0 and delta H1=W L. The split ev eta=identity2 and the contraction show K is split exact away from degree0, with degree0 locally free of rank2. Thus K is quasi-isomorphic to E[0] globally. The covering and regularity are proved here, rather than left as an extra unverified exactness premise. Locally split exactness also survives ANY pullback; flatness of f is unnecessary for this step.

## 3. P4 lifting theorem

Let L=internal Hom(K,S*K). Its degree-p terms are direct sums of O(p), with −3≤p≤3. Every such O(p) has no higher cohomology on P4. Also H0(O(p))=0 for p<0. Consequently the natural map from the global Hom complex to its derived global sections is a quasi-isomorphism. Its degree0 cohomology consists exactly of global degree0 chain maps, with no nonzero global degree−1 homotopies.

Because both K and S*K have cohomology only in degree0, their derived degree0 morphisms are precisely Hom(E,S*E). Every such bundle map therefore has a global chain representative. This is not the generally false assertion that taking H0 is faithful for arbitrary complexes: the concentration in one degree is essential.

Each degree0 component is a constant matrix. The equation at the first differential is

    M gamma(v) = gamma(Sv) N5,   S(v_j)=(−1)^j v_j.

The certified coefficient system has rank250 on its 250 unknowns, forcing M=N5=0. A chain map with degree0 component M=0 induces the zero map on ker(delta)/im(gamma). Thus Hom(E,S*E)=0. It is not necessary to separately prove its degree1 and degree2 components vanish.

## 4. Elliptic-fourfold lifting theorem

Let C be the smooth projective completion of y²=x³−x, O its origin, X=C^4, and N the external tensor product of O_C(O) from the four factors. Let f:X→P4 be the product degree-two maps C→P1 followed by the symmetric product map (P1)^4→Sym4(P1)=P4. Then f*O(1)=N². On the affine chart its coordinates are (1,e1(x),...,e4(x)), so this is the same elementary-coordinate substitution as the source.

For sigma induced by (x,y)↦(−x,iy) on each factor, the origin divisor is invariant, giving the natural identification sigma*N=N. Under its square, the sections 1,x of O_C(2O) transform as 1,−x. Hence f sigma=S f, including the indicated linearization, not just an abstract unrelated projective action.

The locally split pullback complex for F=N tensor f*E is

    5 N^(−1) → 15 N → 10 N³ → 2 N⁵.

Its Hom into its sigma pullback has degree-p terms equal to copies of N^(2p), for −3≤p≤3. Riemann–Roch and Serre duality on an elliptic curve give cohomology of a positive degree line bundle only in degree0, of a negative degree line bundle only in degree1, and h0(O_C)=h1(O_C)=1. Kunneth therefore gives:

- p>0: only q=0;
- p<0: only q=4;
- p=0: q=0,1,2,3,4, with multiplicities binomial(4,q) per copy.

The spectral sequence E1^{p,q}=Hq(X,Hom^p) has d_r of bidegree (r,1−r). On total degree0 its only nonzero E1 entry is (0,0), since every negative-p,q4 entry has total at least1. There are no E1 entries of total degree−1. The d1 from (0,0) imposes the chain-map equation; incoming d1 has source (−1,0)=0. For r≥2, an incoming arrow would come from (−r,r−1), absent from the table; outgoing higher arrows have negative q and vanish. Thus E2^{0,0}=E_infinity^{0,0}, and there is only one filtration piece in total degree0, so no extension ambiguity. The edge map identifies derived Hom degree0 with global chain maps.

All their components are constant because H0(X,O_X)=C. The first-differential relation is the same gamma equation after pullback. The five pulled-back coordinate sections are linearly independent: f is surjective, since C→P1 is surjective and each degree4 homogeneous binary form factors over C. Hence the identical coefficient-system obstruction applies. The induced map on degree0 cohomology is zero, proving Hom_X(F,sigma*F)=0.

Caution: the entire X spectral sequence need NOT collapse; the conclusion is only the total-degree0 lifting result. Higher q at p0 and q4 at negative p genuinely exist. For example the support permits d5 from (−3,4) to (2,0), irrelevant to Hom degree0. We make no claim about such differentials' actual values.

## 5. Controls, limits and sources

`check_static.py` is independent of the author's checker. It checks literal metadata, B/C patterns, all primitive degree bounds and formal spectral-sequence support. Normal and optimized results agree. Internal-Hom multiplicities by p=−3,...,3 are 10,80,245,354,245,80,10. The pre-existing independent constant checker was also rerun successfully: exact CM rank250/nullity0, identity-action rank249, identity pair verified, author elimination certificate replayed. Its scope excludes physical source evaluation and polynomial-matrix products.

General facts used: [projective-space cohomology](https://stacks.math.columbia.edu/tag/01XS), [Cech cohomology of complexes](https://stacks.math.columbia.edu/tag/01FP), and [Kunneth formula over a field](https://stacks.math.columbia.edu/tag/0BEC). These support the stated standard tools; the object-specific cover, cohomology-support argument and vanishing deduction are proved above.

Still outside this verdict: independently replaying A, validating physical arithmetic/source implementations, identifying a separately defined physical global object beyond the explicit F construction, transitions/determinants required for other claims, higher residual/HPL assertions, and any of the 30 detector evaluations. No actual source/jet values, physical matrix products, production imports, or external posts occurred.
