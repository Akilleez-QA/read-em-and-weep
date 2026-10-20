# A finite tracefree line-complex model for normalized restriction

## Result

Let F be the normalized HM bundle, B0=End0(F), Y=P4, and f:S=P1×P1→Y, (l,m)↦l³m. All work is over C. There are finite complexes C and D with row degrees k, and a comparison T of row degree +2, such that

    C: C^-3(150) → C^-2(400) → C^-1(245),
    D: D^-3(1200) → D^-2(6800) → D^-1(13720)
                     → D^0(11649) → D^1(3920) → D^2(400),

and

    H²(Y,B0(-4)) = H^-2(C),
    H²(S,f*B0⊗O(-12,-4)) = H^0(D),
    rS = H(T): H^-2(C) → H^0(D).

Numbers in parentheses are vector-space dimensions, not evaluated ranks. The map T has precisely three possibly nonzero components

    T_-3: C^150 → C^13720,
    T_-2: C^400 → C^11649,
    T_-1: C^245 → C^3920.

They are supplied by a finite, explicit homotopy-transfer formula below, involving exactly two contractions. In particular, zero termwise maps H4→H2 DO NOT imply zero normalized restriction. These matrices are not instantiated or evaluated here.

The tracefree correction 11682→11649 is essential: the scalar summand downstairs has H²(O(-12,-4)) of dimension 33 even though O_Y(-4) is acyclic. A strict chain-level supertrace projector handles this correction before restriction or contraction.

## 1. Replace the monad by a strict line complex

Use the normalized HM monad A=5O(-1)→M=2Ω²(2)→5O, with arrows a,b. The standard exterior Euler/Koszul coresolution is

    0→M --j→20O --u→10O(1) --v→2O(2)→0.

Dualizing gives 0→2O(-2)→10O(-1)→20O→M∨→0. The line bundles O(-1),O(-2) are acyclic on P4, so H⁰(20O)→H⁰(M∨) is an isomorphism. Thus b extends uniquely to a constant map btilde:20O→5O. Since b is a bundle surjection, btilde has rank five. Choose a constant splitting 20O=V⊗O⊕5O with V=ker btilde, dim V=15.

The arrow ja lands in V⊗O because btilde ja=ba=0. Define

    L^-1=5O(-1), L^0=15O, L^1=10O(1), L^2=2O(2),
    d^-1=ja, d^0=u|V, d^1=v.

All arrows are linear in the homogeneous coordinates; their composites vanish. The complex has only F in cohomological degree zero. Indeed ker(u|V)=j(ker b), so its degree-zero cohomology is ker b/im a=F. Injectivity at degree -1 follows from a. Exactness at degree1 follows because u(V)=u(20O): given e, lift btilde(e) locally to m∈M with b(m)=btilde(e), then e-jm∈V and u(e-jm)=u(e). Surjectivity at degree2 is the Koszul surjectivity. This gives a strict complex without any unjustified lifting of both monad arrows into unrelated resolutions.

Equivalently cancel the constant acyclic pair in the complex with degree1 equal to 5O⊕10O(1). The choice of constant splitting is harmless; every resulting L represents F and its scalar/trace maps are intrinsic in the derived category. Pullback preserves this quasi-isomorphism: these are bounded bundle complexes with locally free cohomology, hence locally split exact away from F.

## 2. Derived endomorphisms and strict trace splitting

Let E=Hom•(L,L)(-4) with d_E(φ)=d_Lφ-(-1)^kφd_L on degree k. It represents End(F)(-4). Since L^p=n_p O(p), n=(5,15,10,2) in p=-1,0,1,2,

    E^k = M_k⊗O(k-4),
    dim M_k = Σ_p n_p n_(p+k),
    (dim M_-3,...,dim M_3)=(10,80,245,354,245,80,10).

In degree zero define str(φ)=Σ_p(-1)^p tr(φ_pp), and set str=0 on other degrees. Supertrace of a graded commutator is zero, so str:E→O(-4) is a chain map. The scalar map s:O(-4)→E, λ↦λ id_L, is a chain map and

    str(id_L)=-5+15-10+2=2.

Consequently P0=id_E-(1/2)s str is a strict chain projector. Its image E0=ker str is a subcomplex and

    E = O(-4) ⊕ E0,     E0 ≃ B0(-4).

Locally split L into F plus contractible pairs; the supertrace on its cohomology is the ordinary trace on F because the contractible pairs cancel. This verifies the last identification, not just a formal dimension assertion. E0^k=E^k for k≠0, while E0^0 is 353O(-4). The projector commutes with pullback. Thus f*E0 represents f*B0⊗O(-12,-4), and restriction is tracefree at chain level. No scalar class can leak into the target comparison.

## 3. Collapse the cohomology rows

For Y=P4, O(t) has no intermediate cohomology, and for -7≤t≤-1 only H4 can survive. Its dimension is binomial(-t-1,4) for t≤-5; it is zero otherwise. Therefore the only row of E0 with cohomology is q=4, in k=-3,-2,-1. Its dimensions are

    10·15=150, 80·5=400, 245·1=245.

Its differential is H4(d_E0). This is C. Its row index k has total degree k+4.

On S, f*O(t)=O(3t,t). For negative t, Kunneth gives H0=H1=0; H2 has dimension (-3t-1)(-t-1) for t≤-2, and all cohomology is zero for t=-1. Thus D^k=H²(S,f*E0^k) is nonzero only for -3≤k≤2, with total degree k+2. Its dimensions are the displayed six numbers: for k≠0 use m_k(11-3k)(3-k), and at k=0 use 353·11·3=11649.

Concrete dual descriptions are

    C^k = M_k ⊗ H⁰(P4,O(-k-1))∨, k=-3,-2,-1,
    D^k = M_k^0 ⊗ [H⁰(P1,O(10-3k))⊗H⁰(P1,O(2-k))]∨,

where M_0^0=ker supertrace and M_k^0=M_k otherwise. Fixed volume/Serre conventions identify these spaces; determinant factors can be retained if group-equivariance is desired. Differentials are the duals of multiplication by the linear entries of d_E0 on Y and their bidegree-(3,1) pullbacks on S. This specifies finite matrix slots without evaluating the HM coefficients.

There are no higher differentials within either collapsed model: only one cohomology row survives. An explicit contraction proof is given next so that the comparison is also controlled.

## 4. The restriction is a two-contraction transfer

Take the five standard affine opens Ui={xi≠0} of Y and their preimages Vi=f^-1 Ui. The morphism f is finite onto its closed image (normalization followed by closed immersion), as established in [the binary-quartic prerequisite](NORMALIZATION-INPUT.md), so these preimages and intersections are affine. The two Čech constructions give a strict restriction map R between double complexes of E0 and f*E0, preserving internal and Čech degrees. Both Čech complexes are bounded in Čech degrees 0,...,4. They have infinite-dimensional cochain spaces; we do not claim otherwise.

Write the total differential as d_v+δ, where d_v is the signed Čech differential and δ is the signed internal differential, so d_vδ+δd_v=0. Choose for each internal degree a vector-space contraction onto its finite Čech cohomology:

    p i=id,   id-i p=d_v h+h d_v,
    h²=0, h i=0, p h=0.

Such contractions are completely specified by choosing Cech decompositions B^q⊕Hrep^q⊕U^q, with d_v:U^q→B^(q+1) an isomorphism: h inverts this isomorphism on B and is zero on the other summands. Use coefficientwise choices so the scalar projector commutes with the contractions. On Y one may use the usual Laurent-monomial contraction; on S the finite cohomology bases above can be represented through the common refinement with the standard four product opens. A choice of representatives and complements is part of the model, not an additional geometric assertion.

The bounded internal range implies (hδ)^7=(δh)^7=0. The elementary perturbation identities therefore give finite chain maps

    I_Y=(1+h_Yδ_Y)^-1 i_Y,
    P_S=p_S(1+δ_S h_S)^-1,
    T=P_S R I_Y.

The transferred differential is pδ(1+hδ)^-1i. Any term using a contraction lowers Čech degree and therefore cannot land in the sole surviving cohomology row. Thus the transferred differentials are exactly H4(d_E0) and H2(f*d_E0), namely those in §3.

The source inclusion begins in Čech degree4; the target projection requires degree2. Each h lowers Čech degree by one, R preserves it, and δ preserves it. Exactly two h's must occur. Expanding the inverse polynomials therefore leaves precisely

    T = p_S [ (δ_S h_S)² R
                + δ_S h_S R h_Y δ_Y
                + R(h_Y δ_Y)² ] i_Y.                 (*)

The plus signs arise because the total number of factors from the two negative geometric series is two. All signs of the bicomplex are already included in d_v,δ,h. Formula (*) raises internal degree by two and has total degree zero. It is the promised exact finite comparison formula. Its domain and target are finite even though its auxiliary Čech realization is not. No bound on denominators in a chosen rational representative, nor a completed implementation of the auxiliary contractions, is claimed.

The perturbation identities prove d_D T_k=T_(k+1)d_C. Thus only T_-3,T_-2,T_-1 can be nonzero, with the dimensions stated at the start. Choice changes give chain-homotopic comparison maps after the canonical cohomology identifications. This is ordinary derived restriction, because R is the actual cochain restriction and I_Y,P_S are quasi-isomorphisms. Replacing it by maps between the original E1 pages would erase precisely this comparison data.

## 5. Exact remaining dependency and kernel test

For x∈ker(d_C:C^-2→C^-1),

    rS([x])=[T_-2 x] ∈ ker(d_D:D^0→D^1)/im(d_D:D^-1→D^0).

Its normalized restriction vanishes exactly when there is y∈D^-1 with

    T_-2 x=d_D y.

Changing x by d_C z changes T_-2 x by d_D T_-3 z, so the test is well defined. Consequently ker rS is the x-projection of the kernel of the finite block map

    ker d_C × D^-1 → D^0, (x,y)↦T_-2 x-d_D y,

modulo im d_C from C^-3. This closes the construction dependency: the remaining input is an actual transferred comparison and actual finite differentials, not an unqualified surface cohomology dimension or a nonexistent termwise H4→H2 map.

From the negative-H¹ HM table in [the supplied cohomology input](../pairing-foundation-inputs/COHOMOLOGY.md) and [primary proposition](../hm_primary_source_verification.md), h¹(B0(-4))=0 and h³(B0(-4))=h¹(B0(-1))=5. Hence the ambient arrows have ranks150 and240, and H^-2(C) has dimension400-150-240=10. These ranks are consequences of previously proved cohomology, not fresh selected-matrix rank evaluations. On the surface, negative total degrees and degrees above2 vanish; thus D is exact at k=-3,1,2. The group H^-2(D)=H⁰(S,f*B0⊗O(-12,-4)) is not set to zero without a further argument. No unknown middle ranks or rank rS are supplied.

The exact positive tail supplies further canonical compression without any selected rank evaluation: D¹→D² is surjective, so ker(D¹→D²) has dimension3520; exactness at D¹ gives rank(D⁰→D¹)=3520. Hence

    Z_S=ker(D⁰→D¹) has dimension8129,
    H²(S,f*B0⊗O(-12,-4))=Z_S/im(D^-1→D⁰).

Likewise Z_Y=ker(C^-2→C^-1) has dimension160 and its boundary space has dimension150. Thus rS is equivalently induced by the restricted map Z_Y(160)→Z_S(8129), modulo the known150-dimensional ambient boundary and the still-unknown image of D^-1(13720). This is a further exact dependency count, not a claim that the target has dimension8129. As a consistency identity only, the alternating sum of D is9, so h⁰(G)-h¹(G)+h²(G)=9; neither h⁰ nor h¹ is discarded.

The Gysin map δS from historical-source:normalization-gysin-factorization/PROOF.md is the dual of this induced map. The cusp correction β remains a separate test on ker rS. Nothing here evaluates either map, any physical source, or any of the retained thirty obstruction values.

## Scope and dependencies

This is a universal construction from the normalized monad, line-bundle cohomology, and exact chain identities. No actual HM/source coefficients, selected polynomial instance, numerical matrix rank, or obstruction value were evaluated. No source-app writes or large computation occurred.

- historical-source:effective-collision-bound/PROOF.md: normalized monad and Koszul conventions.
- [Normalization prerequisite](NORMALIZATION-INPUT.md): f is finite and f*O(1)=O(3,1).
- historical-source:normalization-gysin-factorization/PROOF.md: relation to δS and the remaining cusp test.
- [Cohomology input](../pairing-foundation-inputs/COHOMOLOGY.md): verified ambient cohomology dimensions.
- AUDIT.md: independent check of construction and comparison.
