# CM obstruction upgraded by global Hom lifting

## Result and precise evidence boundary

The proposed projective-space lifting theorem is correct. It gives

    Hom_P4(E, S*E) = 0,

for the pinned four-term homogeneous complex, **conditional on admitting the authenticated historical exact A-identity receipt** described below. Here E is its degree-zero cohomology, and S[v0:...:v4]=[v0:−v1:v2:−v3:v4]. The source twists are verified, not guessed. A static denominator audit plus the existing three-premise contraction theorem establishes the needed global exactness from that imported A premise; global exactness is not inferred from a generic-point calculation alone.

There is a stronger, initially unexpected conclusion. On the stated elliptic product X=C^4, with N=O(sum pr_i*infinity), the physical cohomology bundle F satisfies

    Hom_X(F, sigma*F) = 0,

under the same imported A premise and the stated physical-bundle identification. For this specific four-term complex, higher cohomology after pullback cannot contribute to total degree zero. Thus a generic warning that pullback may introduce additional maps does not leave a loophole here. This is a conditional global regular bundle statement; rational/meromorphic maps are not excluded.

No model/source/jet evaluation, production import, polynomial matrix product, numerical experiment, or external post occurred. The only new executable check reads literal shapes, coefficients, denominators and integer monomial degrees. All detector values and production admission remain unchanged. The work concerns frozen sources; it does not reauthenticate the current remote fork.

## 1. Source conventions and evidence hierarchy

Take a characteristic-zero field k containing i. Define P=P^4_k and

    K^{-1}=O(-1)^5, K^0=O^15, K^1=O(1)^10, K^2=O(2)^2,
    d^{-1}=gamma, d^0=delta, d^1=ev.

The pinned model has these matrix shapes. Its homogeneous prescription applies hom(p,1) to all three differentials; every nonzero literal entry has degree at most one. Hence all three maps have homogeneous weight +1, giving exactly the displayed twists after normalizing K^0 to O^15. The two I columns have weights (0,1), P rows (0,−1), and H0,H1 have weight −1. The homogeneous auxiliary maps are rational bundle maps with these assigned twists, not all degree-zero functions.

The independent ambient specification explicitly places ranks (5,15,10,2) in degrees (−1,0,1,2), with physical powers N^(−1),N,N^3,N^5. Let f:X→P be the elementary-coefficient map obtained from C^4→(P1)^4→Sym^4(P1)=P4. Its coordinate sections are coefficients of product(Y_a+X_a z). The root-line proof identifies N as the external product of O_C(infinity), and the degree-two x map gives f*O(1)=N². Consequently the specified physical complex is

    K_X = N tensor f*K.

The physical frame factors nu^(−2) are precisely the coefficient change for these adjacent powers. This agrees with the separately reviewed physical-frame bridge, rather than interpreting its physical line exponents as P4 twists directly.

Exactness evidence has three different levels:

1. B: H1 eta=0 is proved by literal empty numerator columns by the literal pivot-column check reproduced here.
2. C: ev delta=0 is proved structurally by the literal skew-support check reproduced here: 20 skew-column pairs and 10 zero block columns. This supersedes the older bridge's unevaluated-C qualification.
3. A: gamma H0+IP+H1 delta=Id15 is an imported historical computation premise. The authenticated receipt counts 1350 E_identity entries, covering all six 15×15 carrier identities. Its producer, pinned model, manifest and full reported result are bound together. It is not a replayable zero-reduction proof object, and no new A products were computed here.

Thus the final theorem is conditional on accepting A's existing exact-SymPy computation receipt. This report neither silently upgrades that receipt to a fresh proof nor treats it as unlocated evidence.

## 2. Global cover and exactness from the imported identities

Write T=product(v0,...,v4) and h_j=v_j^5−T. Use six projective opens

    U_j=D_+(h_j), j=0,...,4;
    U_*=D_+(v0 v1 v3 v4).

They cover P. Indeed, if all h_j vanish and one coordinate vanishes, then T=0 and all coordinates have fifth power zero, impossible at a projective point. Thus at a common zero of all h_j every coordinate is nonzero and U_* contains that point. This argument holds after any field extension.

The new metadata checker verifies regularity domains without symbolic matrix products. Applying the literal homogenization rule, the common primitive denominator on chart 0 is

    hom_4(v1 v2 v3 v4−1)=v1 v2 v3 v4−v0^4=−h0/v0,

with at most one additional v0 in each entry denominator. On charts 1–4 it is −h_j, with no additional v0 denominators. On the auxiliary chart it is −v1²v3v4, with at most two additional v0 factors (H0 needs at most one). Therefore all the specified primitives are regular as bundle maps on their respective U_j or U_*. The pivots are j on chart j and 0 on the auxiliary chart. Since h_j=v_j(v_j^4−product_{k≠j}v_k), v_j is nonzero on U_j; v0 is nonzero on U_*. Hence eta,W,L are regular there too. These opens lie inside a pivot affine chart, so the line twists can be trivialized for the following matrix argument. In particular, the two columns of I have domain O⊕O(−1); this is locally trivial on that pivot chart. The square inverse argument is not treating unequal homogeneous weights as equal globally.

The literal ev gives a split pivot evaluation:

    LW=Id8, ev W=0, L eta=0, ev eta=Id2,
    WL+eta ev=Id10.

The existing three-premise theorem, valid over commutative rings, uses A,B,C to give

    U=(gamma,I,H1 W), Q=(H0;P;L delta), UQ=QU=Id15,
    delta gamma=0, delta I=0,
    delta H1=Id10−eta ev, H0 gamma=Id5, PI=Id2,

and all cross contractions. Thus each restricted complex is the direct sum of three contractible paired blocks of ranks 5,8,2 and a rank-two block in degree zero. The globally defined polynomial compositions are zero because they vanish on this cover. We obtain K quasi-isomorphic to a locally free rank-two E concentrated in degree zero, with no extra cohomology at the complement of a merely generic chart. Local splitting also means arbitrary pullback preserves the quasi-isomorphism, so K_X is quasi-isomorphic to F=N tensor f*E.

## 3. Exact P4 global-Hom lifting argument

Put L=S*K and define the ordinary internal Hom complex

    A^p = direct_sum_a Hom_sheaf(K^a,L^{a+p}),
    d_A(t)=d_L t−(−1)^p t d_K.

Because K is bounded and locally free, A represents derived internal Hom(K,L). Equivalently, it is the ordinary tensor complex K^dual tensor L. The perfect-duality justification is standard and is set out in [Stacks, Duals](https://stacks.math.columbia.edu/tag/0FP7).

Since both complexes have K^a=O(a)^{r_a}, every summand of A^p is O(p). The internal degrees are −3≤p≤3. Projective-space line-bundle cohomology gives H^q(P,O(p))=0 for q>0 throughout that range: intermediate cohomology vanishes, and the top group H^4 can occur only for p≤−5. See [Stacks, Cohomology of projective space](https://stacks.math.columbia.edu/tag/01XS).

For completeness, take a finite standard affine cover of P and the Čech double complex of A. Every finite intersection is affine and the terms are quasi-coherent, so its total complex computes RΓ(A). Filtering first by internal degree gives

    E1^{p,q}=H^q(P,A^p) => H^{p+q}(RΓ(A)),
    d_r:E_r^{p,q}→E_r^{p+r,q−r+1}.

Here only q=0 survives, so H^0(RΓ(A))=H^0(Γ(A)). Degree-zero cocycles in Γ(A) are precisely global chain maps; degree-zero coboundaries are chain homotopies. In fact Γ(A^−1)=0 because its terms are O(−1), so there are no nonzero global homotopies. The comparison with derived cohomology can also be formed using the standard Čech-hypercohomology construction in [Stacks, Čech cohomology of complexes](https://stacks.math.columbia.edu/tag/01FP).

Since K≃E[0] and L≃S*E[0], this proves that every sheaf map E→S*E is induced by a global chain map K→L. It is not the false assertion that every map between arbitrary complexes of vector bundles lifts globally without acyclicity.

## 4. Orientation and use of the rank-250 certificate

A degree-zero global chain map has four constant components

    T^−1=N_5, T^0=M_15, T^1=R_10, T^2=Q_2,

because Hom(O(a),O(a))=k and S*O(a) is identified with O(a). Its degree −1 chain equation is exactly

    M_15 gamma(v) = gamma(Sv) N_5.

This is the orientation of the published constant-gamma-elimination certificate, with no transpose, inverse, or replacement of S by a different coordinate action. That rational rank-250 certificate proves M_15=N_5=0 over every characteristic-zero extension, including k. It follows directly that the map induced on ker(delta)/im(gamma) is zero: the representing map on K^0 is zero. Hence every sheaf morphism E→S*E is zero.

We do not need to prove the other two chain components vanish to obtain this conclusion. Nor do we confuse sheaf cohomology H^0(K)=E with the vector space of global sections H^0(P,E). The former is the object on which the chain map induces zero.

## 5. Elliptic product: why the extra-cohomology caveat does not survive here

Let sigma act simultaneously by (x_a,y_a)↦(−x_a,i y_a). It fixes infinity on every factor, so it preserves the divisor defining N. This supplies sigma*N≅N; choosing its divisor-induced identification fixes the rational section 1. Also f∘sigma=S∘f. Consequently

    sigma*K_X ≅ N tensor f*S*K,
    Hom_sheaf^p(K_X,sigma*K_X) is a sum of N^(2p).

This identification is about bundles and differentials; it does not assume an isomorphism F≅sigma*F, which is the assertion to be ruled out.

Write N^(2p)=external_product_a O_C(2p infinity). For p>0, each factor has positive degree and H^1=0 by Serre duality and the trivial canonical line of an elliptic curve; hence the product has cohomology only in q=0. For p<0, each factor has no H^0, so only q=4 can be nonzero. At p=0, O_X has cohomology in q=0,...,4. These statements follow directly by tensoring the four factor cohomologies via [Stacks, Künneth formula](https://stacks.math.columbia.edu/tag/0BEC).

Apply the same hypercohomology spectral sequence, now on X. Since −3≤p≤3:

- Negative-p contributions have q=4, and p+q≥1.
- Positive-p contributions have q=0, and p+q≥1.
- At p=0, the only total-degree-zero term is q=0.

Thus total degree zero is supported only at (0,0). A higher incoming differential would originate at (−r,r−1), r≥2. For r≤3 its cohomology degree is below 4 and vanishes; for r≥4 its internal degree is outside the complex. Higher outgoing differentials from (0,0) have negative q. Therefore

    H^0(RΓ Hom_sheaf^•(K_X,sigma*K_X))
      = E2^{0,0} = H^0(Γ Hom_sheaf^•(K_X,sigma*K_X)).

The global chain-map comparison is consequently surjective (indeed an isomorphism in degree zero). This is not a claim of termwise acyclicity on X or of degeneration of the entire spectral sequence.

The degree-zero chain components are constant matrices because H^0(X,O_X)=k. Their first chain equation is the pullback of M gamma(v)=gamma(Sv)N. The elementary symmetric polynomials v1,...,v4 are algebraically independent on the finite x chart, so equality after this pullback forces the same coefficient equations. Equivalently, f is surjective. The existing rank certificate again gives M=N=0. With K_X≃F[0], the induced sheaf morphism vanishes. Thus Hom_X(F,sigma*F)=0, even without an equivariance requirement.

In other settings pullback can create Hom classes; the amplitude bound 3 versus dimension 4 and the equal positive degree on all four elliptic factors are essential here. The result is global: on a generic point both rank-two bundles are vector spaces and do admit rational isomorphisms. Coordinate-dependent local maps or rational gauges therefore are not contradicted. What is excluded is their gluing to a global regular bundle isomorphism.

## 6. Scope for the CM idea

Conditional on the imported A receipt and the declared geometric identification, simultaneous CM has no global regular lift to this pinned cohomology bundle at all. In particular it cannot furnish a covariance symmetry of the whole source by a global bundle isomorphism. This is stronger than the previously published constant-presentation obstruction.

This does not compute an obstruction/detector, classify complete scalar characters, prove absence of accidental scalar covariance, alter any of the 30 remaining detector values, or authorize source evaluation. It does not establish any claimed present remote head. The inherited A trust boundary must remain visible when quoting the strengthened theorem.

## 7. Frozen source links

- [Pinned model, commit 10810ee](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-operator-compiler/hm-pinned-model.json), SHA256 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926.
- [Homogeneous producer, commit 08b7363](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/checks/verify_homogeneous_identities.py), SHA256 ad6fdb925262b9661bd51c0f65fe1a48d8f4ab1927bbf14b23786a4f0e1503bf. Read only, never executed here.
- [Imported exact receipt](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/certificates/homogeneous-identities.json), SHA256 55e78bbc838a971b64531379788192acf8877c04f2d797fb13b4f4a68e47b018.
- [First-order specification](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md).
- [Ambient specification](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/ambient-second-jet.md).

