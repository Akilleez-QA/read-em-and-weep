# Beilinson reconstruction makes Gamma restriction an isomorphism on sections

## Statement

On the established common open, the natural restriction

    H0(Xhat,M4) -> H0(S_Gamma,M4|S_Gamma)

is an isomorphism. In particular the actual conductor-descent space H0(K4) is exactly the actual twist-four endomorphism space, not merely a sufficient vanishing test. This does not prove that either space is zero.

## 1. The four derived cohomology inputs

Set Fder=R f_*M4 on P3. The checked ambient cohomology gives

    R Gamma(Fder)=K directsum R[-1],
    R Gamma(Fder(-1))=P[-1],
    R Gamma(Fder(-2))=R Gamma(Fder(-3))=0,

where K=H0(B_Q(4)), R=H1(B_Q(4)), and P=H1(F_Q(2)), of dimension5. The first line is the pinned fifty-point boundary, including vanishing of H2 and H3. The last line follows from the blowup exceptional twists of orders2 and3 and relative projective-bundle acyclicity. For the second line M4-A=L-H+Zexc pushes to F_Q(2), whose only cohomology is the established five-dimensional H1.

## 2. Reconstruction and the absence of a hidden extension

The diagonal resolution on P3 times P3 has terms O(-i) external tensor Omega^i(i), i=0,1,2,3. It is the Koszul resolution of the diagonal defined by the tautological map into the universal quotient bundle. Applying it to the bounded coherent complex Fder reconstructs Fder from R Gamma(Fder(-i)) tensor Omega^i(i). The two last inputs vanish, so reconstruction gives the triangle

    P tensor Omega^1(1)[-1]
      -> K tensor O directsum R tensor O[-1]
      -> Fder -> .

The possible component of the first arrow into K tensor O lies in

    Hom(Omega^1(1)[-1],O)=Ext^1(Omega^1(1),O)
      =H1(T_P3(-1))=0.

The last vanishing follows directly from the Euler sequence 0->O(-1)->O^4->T(-1)->0. Therefore Fder is isomorphic to

    K tensor O directsum [P tensor Omega^1(1) -> R tensor O],

where the displayed two-term complex is in degrees0 and1. Its differential is actual, not replaced by a generic map. No vanishing of K or R is used. The K-summand agrees with the canonical evaluation of global sections because H0(Omega^1(1))=0.

## 3. Derived base change and Gamma

The proper morphism f is flat and M4 is invertible. Derived base change to the regular embedding Gamma->P3 therefore identifies the derived restriction of Fder with R(f|S_Gamma)_*(M4|S_Gamma). The two terms in the displayed reconstruction are locally free, so restriction is ordinary on those terms.

The restricted Euler sequence gives

    H0(Gamma,Omega^1(1)|Gamma)
      =ker[H0(Gamma,O)^4 -> H0(Gamma,O(1))]=0.

Here Gamma is connected and nondegenerate. Its degree6 and the Clebsch equation are not needed for this vanishing. A complex in degrees0 and1 has degree-zero hypercohomology equal to the kernel on global sections of its first differential. Thus the restricted two-term complex contributes no H0. The only contribution is K tensor H0(O_Gamma)=K. This identifies the natural restriction map with an isomorphism, not just an equality of dimensions.

## Consequences for the preceding extension notes

The cubic reduction, jet cohomology, and actual Gamma-resolution spectral sequence remain valid calculations. However the extension boundary from H0(S_Gamma,M4|S_Gamma) to H1(M4 tensor I_S) is identically zero. It is therefore not an additional unresolved test. In particular the 45-intersect-400 conductor criterion is now necessary and sufficient for actual twist-four sections. The nonzero obstruction target can still have other significance, but its rank alone must not be interpreted as an obstruction to extending these sections.

No selected coefficients, jet ranks, or generic-matrix assumptions occur. This removes the ambient-extension uncertainty while leaving the twist-four vanishing itself open.

## 4. The entire ambient ideal cohomology is concentrated in degree two

The preceding reconstruction also computes the ideal contribution, not only the boundary on sections. Since Gamma is a connected rational curve,

    H^i(P3,I_Gamma)=0 for every i.

Nondegeneracy and O_Gamma(1)=O_P1(6) give I_Gamma(1) only one nonzero cohomology group, H1 of dimension3. Tensoring the Euler sequence by I_Gamma is exact, since its quotient is locally free:

    0 -> Omega^1(1) tensor I_Gamma -> O^4 tensor I_Gamma
      -> I_Gamma(1) -> 0.

Consequently Omega^1(1) tensor I_Gamma has only H2, of dimension3. The Beilinson model is a complex of locally free sheaves, so derived tensoring it with I_Gamma is computed term by term. Projection formula for the proper flat f then gives

    R Gamma(Xhat,M4 tensor I_S)
       = P tensor H1(P3,I_Gamma(1))[-2].

In particular

    H1(Xhat,M4 tensor I_S)=0,
    h2(Xhat,M4 tensor I_S)=15,

and every other cohomology group vanishes. This proves that the jet-syzygy obstruction target identified earlier is itself zero, not merely that the extension boundary has zero image. Hence the actual map

    (C6*)^3 -> (C5*)^9

is injective, without any injectivity assumption on the individual jet maps.

The restriction long exact sequence also gives

    0 -> H1(Xhat,M4) -> H1(S_Gamma,M4|S_Gamma)
      -> P tensor H1(I_Gamma(1)) -> 0,

so h1 on S_Gamma is r+15, and H2(S_Gamma,M4|S_Gamma)=0. The fifteen-dimensional degree-two ideal group is compatible with the independently calculated Euler characteristic. None of these identities forces r=0.

## 5. Every infinitesimal neighborhood has exactly the ambient sections of this eigenline

The independently checked ACTUAL-GAMMA-BALANCED-NORMAL-BUNDLE.md at f47658e8c723428503cdf69f20bdf81768d93494 proves

    N_Gamma/P3=O_P1(11) directsum O_P1(11).

For n>=1 define nGamma by I_Gamma^n. Since Gamma is a regular embedding, its successive structure-sheaf layers are

    I_Gamma^m/I_Gamma^(m+1)=Sym^m(N_Gamma/P3*)
                          =O_P1(-11m)^(m+1),    m>=1.

Each such layer has no global sections. The constant section1 lifts through every thickening. Induction in the exact sequences of successive thickenings therefore gives H0(O_{nGamma})=C for every n, with the restriction maps acting as the identity on constants. It follows from 0->I_Gamma^n->O->O_{nGamma}->0 that

    H0(I_Gamma^n)=H1(I_Gamma^n)=0.

Also H0(I_Gamma^n(1))=0 because I_Gamma^n is a subsheaf of I_Gamma and Gamma is nondegenerate. Tensoring the Euler sequence by I_Gamma^n gives

    H0(Omega^1(1) tensor I_Gamma^n)
     =H1(Omega^1(1) tensor I_Gamma^n)=0.

The Beilinson locally free model from Section2 now implies

    H0(Xhat,M4 tensor I_S^n)
     =H1(Xhat,M4 tensor I_S^n)=0    for every n>=1.

Indeed flatness identifies f*I_Gamma^n with I_S^n, including its injection into O_Xhat, and the projection formula computes the cohomology from that model tensored by I_Gamma^n. Its O-summands and Omega-summand have no cohomology in the degrees that could contribute0 or1.

Thus for every n>=1 the natural restriction is an isomorphism

    H0(Xhat,M4) -> H0(nS,M4|nS).

These isomorphisms are compatible with restriction from (n+1)S to nS. Consequently every section of this fixed eigenline on the formal completion along S is the restriction of a unique ambient section.

Scope is essential: this is a statement about the already fixed line bundle M4 and the infinitesimal neighborhoods of this particular S. It is not an algebraization theorem for arbitrary sheaves, not a solution of the original proof-repair higher-lifting problem, and not a proof that H0(Xhat,M4) vanishes. No splitting of the whole formal neighborhood is assumed; only its verified graded conormal layers are used.

Source pins: the four-twist calculations are in AMBIENT-EXTENSION-CUBIC-REDUCTION.md at583f16a90de1a4cfc5d365cdcf01617b83d092c7 and QUADRIC-FIFTY-POINT-BOUNDARY.md at22bdcb7e9c833e7a1819d0ec28e5e615be9c7a4f. Flatness is in UNIFORM-FLAT-EVALUATION-FIBRATION.md at1c8166298f30f30a8ab30cde5c27467f9bef8e22. The exact Gamma resolution is e3c9ef8a5525a8d94890270f3f3bb4f6a85ece81. The argument above reconstructs the needed diagonal resolution explicitly, without an unproved generic map replacement.
