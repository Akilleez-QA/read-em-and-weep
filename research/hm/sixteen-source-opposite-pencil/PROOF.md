# A sixteen-source actual opposite presentation and its evaluation bridge

Work over C with G=SL2(F5), W the physical negative doublet, W' the other doublet, A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, V=Sym2 W', and P the even four-dimensional irreducible. All line bundles are on T=P(W*) with standard equivariant linearizations. No selected actual HM/source coefficients, points, parameters, matrices or instance ranks are evaluated.

## 1. Exact immutable interface and result

INPUTS.json authenticates two originals in Akilleez-QA/read-em-and-weep.

INCIDENCE is PR1067, commit0201d67280fbfe0f87c84e7e726c3dc6c12bbecb, research/hm/weighted-incidence-line/PROOF.md. It retains the actual exact sequences

    0 -> A O(-6) -> R O(-1) --d--> Z -> C -> 0,
    0 -> K tensor V O(2) -> Z -> H28 O -> 0,       (1)
    R=2W+2W'+3S+2T6, H28=1+4A+2V+P+D.

Here dim K=2. It proves the induced weighted map to C is nonzero, with canonical multiplicity-kernel line K0. The preimage L of K0 tensor V O(2) is a saturated subbundle of R O(-1), canonically split as

    L=W' O(-1)+V O(-2)+O(-4),                    (2)

and maps onto K0 tensor V O(2) with kernel A O(-6). Its three summands reach, respectively, only the W', T6 and S source isotypic components. This input also supplies the seven necessary C types and the one-dimensional spaces Hom_G(V O(2),C) and Hom_G(W' O(5),C). The universal sequence

    0 -> O(-4) -> V O(2) -> W' O(5) -> 0          (3)

makes precomposition an isomorphism between those Hom lines.

REDUCED is PR934, commit8c9847612b5f575b987cec9c62b72b099d745e44, research/hm/reduced-opposite-pencil/PROOF.md. Its canonical actual reduced presentation is

    0 -> E26 O(-1) -> H31 O -> C -> 0,           (4)
    H31=1+3A+V+2P+2D,

with exactly the same C as the original full opposite pencil. Its historical torsion alternatives are not used; INCIDENCE uses the subsequently proved locally free C.

Write J=K/K0, a one-dimensional trivial multiplicity space. We prove an actual fiberwise-injective presentation

    0 -> E20 O(-1) -> Y -> C -> 0,               (5)
    E20=2W+W'+2S+T6,
    0 -> J tensor V O(2) -> Y -> H22 O -> 0,
    H22=1+3A+V+P+D.                              (6)

The target extension splits equivariantly but not canonically. Thus the displayed source has rank20, target rank25 and degree6, and the cokernel remains the actual rank5 degree26 bundle C. The weighted map in (6) is the nonzero surviving map of INCIDENCE.

A further actual cubic-lift and constant-graph cancellation proves the final sixteen-source presentation (13), whose target is an extension of H19 O by J tensor W' O(5), with H19=1+2A+V+P+D.

Naturality of complete evaluation identifies a new canonical J tensor T6 subspace of the historical reduced source E26, with selected coefficient target J tensor(P+D) in H31. This does not identify the original degree-one-generated marked T6 with this new one: its multiplicity line in K may equal K0 and be killed by the passage to J.

## 2. Quotient by the actual rank-six preimage

Quotient the first complex in (1) by the actual preimage sequence

    0 -> A O(-6) -> L -> K0 tensor V O(2) -> 0.

The quotient diagram gives

    0 -> G26:=R O(-1)/L -> Z':=Z/(K0 tensor V O(2))
      -> C -> 0.                                (7)

Both quotients are locally free by the saturation statements in INCIDENCE and (1). Hence the left map in (7) is injective on every fiber. The target has an actual extension

    0 -> J tensor V O(2) -> Z' -> H28 O -> 0.     (8)

To identify G26, use the component restrictions of (2). The constant W' O(-1) inclusion removes one W' source copy. The V O(-2) inclusion into its selected T6 O(-1) is the unique tensor Euler inclusion

    0 -> V O(-2) -> T6 O(-1) -> V O -> 0.

The O(-4) inclusion into its selected S O(-1) is the universal cubic inclusion

    0 -> O(-4) -> S O(-1) -> A O -> 0,

obtained by dualizing complete cubic evaluation and twisting by O(-1). These components lie in different isotypic source summands and have no cross components. Taking constant equivariant complements to their selected coefficient lines consequently proves

    G26 ≅ E20 O(-1) + (A+V) O.                   (9)

The displayed splitting may depend on complement choices. What is canonical is its complete-evaluation image

    F:=im[H0(G26) tensor O -> G26],
    F≅(A+V) O,       G26/F≅E20 O(-1).            (10)

This retains the actual quotient and its maps rather than replacing them with an arbitrary split model.

## 3. Cancel only the actual constant image

Map F into Z' using (7), then project to H28 O in (8). This is a constant equivariant map. Its kernel, if nonzero, is a constant sum of A and V copies whose injection into Z' would factor through J tensor V O(2). But

    Hom_G(A O,V O(2))=Hom_G(A,V tensor A)=0,
    Hom_G(V O,V O(2))=Hom_G(V,V tensor A)=0,

because V tensor A=P+D. This contradicts injectivity of F->Z'. Thus the constant projection is injective. Its coefficient image is an actual A+V subspace of H28. In particular F maps fiberwise injectively, its image has zero intersection with the weighted subbundle, and its quotient in Z' is locally free.

Define Y=Z'/F using this actual image, not a selected target summand. The quotient diagram of (7) by F yields (5), with source G26/F. Quotienting (8) gives (6), with constant character H28-(A+V)=H22. Its equivariant extension class is zero since H1(O(2))=0 and finite-group invariants are exact. An equivariant splitting exists but is not selected canonically. All remaining actual off-diagonal maps are retained.

The rank and degree checks are

    rank G26=26, deg G26=-20;
    rank Z'=31, deg Z'=6;
    rank Y=25, deg Y=6;
    rank C=25-20=5, deg C=6-(-20)=26.

## 4. Quotient the surviving cubic lift and its actual constant graph

The surviving weighted map J tensor V O(2)->C kills J tensor O(-4) from (3). Exactness of (5) therefore gives a unique lifted injection

    J tensor O(-4) -> E20 O(-1)

whose image in Y is precisely this weighted subbundle. The lift is saturated: Y/(J tensor O(-4)) is locally free, still surjects onto C, and its kernel is E20 O(-1)/(J tensor O(-4)). This is also the surviving quotient of INCIDENCE's canonical doubled cubic lift, by uniqueness of the lift through the injective source map.

Only the two S source copies receive this cubic map, because Hom_G(O(-4),E20 O(-1))=Hom_G(S,E20). Its nonzero coefficient direction selects a single S copy. Universal cubic evaluation then identifies the source quotient G19 up to an equivariant splitting as

    G19≅E16 O(-1)+A O,
    E16=2W+W'+S+T6.                              (11)

The intrinsic constant subbundle is F_A=H0(G19) tensor O≅A O; no splitting of G19 is chosen to define it. The target quotient Y24=Y/(J tensor O(-4)) fits into

    0 -> J tensor W' O(5) -> Y24 -> H22 O -> 0,
    0 -> G19 -> Y24 -> C -> 0.                   (12)

Project the actual image of F_A in Y24 to H22 O. If this constant coefficient map vanished, the rank-three bundle A O would inject into the rank-two bundle J tensor W' O(5), impossible at the generic point. Thus it is nonzero. Irreducibility of A makes it a constant injective coefficient map, hence fiberwise injective. Its image in Y24 may have a NONZERO weighted component; that component is retained, not set to zero.

Quotient Y24 by this actual lifted image, and quotient G19 by F_A. The resulting actual sequence is

    0 -> E16 O(-1) -> Y21 -> C -> 0,
    0 -> J tensor W' O(5) -> Y21 -> H19 O -> 0,
    H19=1+2A+V+P+D.                              (13)

This is the final sixteen-source presentation. Its target extension splits equivariantly since H1(O(5))=0, but such a splitting is not canonical. Source rank16 and degree-16, target rank21 and degree10 give the unchanged rank5 degree26 cokernel. All source and target quotients and the remaining maps are inherited from the actual diagram. C is locally free, so the injection in (13) is fiberwise injective everywhere.

## 5. Complete evaluation identifies the new reduced subblocks

Both H0 and H1 of E20 O(-1) vanish. Therefore (5) canonically identifies H0(Y) with H0(C). The weighted subbundle J tensor V O(2) of Y injects on global sections, selecting J tensor(P+D) inside this common coefficient space, since V tensor A=P+D. This remains true if its induced sheaf map to C has rank only one or two; injectivity on these global sections is a different assertion.

Y is globally generated by its splitting type from (6). Denote complete-evaluation kernels by M_Y and M_C. The exact evaluation diagram of the weighted subbundle in (6), whose constant quotient H22 O has zero evaluation kernel, gives canonically

    M_Y ≅ J tensor T6 O(-1).

This is the kernel of quadratic evaluation tensored with J tensor V. Next the evaluation diagram for (5), using H0(Y)=H0(C), gives the actual exact sequence

    0 -> M_Y -> M_C -> E20 O(-1) -> 0.           (14)

In (4), H0/H1(E26 O(-1))=0 identifies H31 canonically with H0(C), and its target arrow with complete evaluation. Thus M_C is exactly the historical actual E26 O(-1), not only a bundle with the same character. Equation (14) therefore identifies a canonical coefficient subspace J tensor T6 inside that reduced source. Its image in H31 O is the universal saturated block

    J tensor T6 O(-1) -> J tensor(P+D) O,

with quotient J tensor V O(2). The extension (14) splits equivariantly because H1(O)=0, but no complement is asserted canonical. It recovers E26=E20+T6=2W+W'+2S+2T6.

The construction uses the surviving multiplicity quotient J, not an identification of a chosen full44 T6 with a chosen reduced26 T6. In particular it does not decide whether the initial marked line of the degree-one-generated submodule survives the quotient by K0.

The final presentation (13) gives the stronger compatible bridge. Since E16 O(-1) is acyclic, H0(Y21)=H0(C) canonically. Complete evaluation of its weighted subbundle has coefficient space

    H0(J tensor W' O(5))=J tensor(A+P+D),

using W' tensor T6=A+P+D. Its evaluation kernel is J tensor W' tensor D O(-1)=J tensor(S+T6) O(-1). The same evaluation diagrams therefore give

    0 -> J tensor(S+T6) O(-1) -> M_C=E26 O(-1)
      -> E16 O(-1) -> 0.                         (15)

This is a new canonical actual ten-dimensional coefficient subspace in the historical reduced source, with coefficient target J tensor(A+P+D) in H31. Its block quotient is J tensor W' O(5). As before the named direct-sum representation identifications do not choose scalar coordinates. Formula (15) recovers E26=E16+S+T6. It does not decide the survival of the initial marked line in K.

## 6. The surviving weighted map has saturated image

The nonzero map J tensor V O(2)->C factors through J tensor W' O(5) by (3). Up to the harmless one-dimensional factor J, let gamma:W' O(5)->C denote its nonzero Hom-line generator. Its image is canonical. We now show it is saturated in every necessary actual C type, without selecting that type.

INCIDENCE's Hom table locates its unique contributing target atom. The outcomes are

    row    image I          C/I
      9    O(12)            O(2)+V O(4)
     10    O(18)            O(2)+A O(2)
     14    W' O(5)          O(2)+W' O(7)
     15    W' O(5)          O(2)+W' O(7)
     17    W' O(5)          O(14)+W O(1)
     18    O(18)            W O(1)+W O(3)
     20    W' O(5)          W O(1)+O(14).           (16)

Here is the uniform justification that no hidden zero divisor occurs. Every nonempty orbit of G on T has length at least twelve: the projective group is A5, point stabilizers are cyclic, and its maximum element order is five. Thus the degree-seven W' system giving W' O(5)->O(12) has no common zero. For degree thirteen, a nonempty invariant common divisor could only have degree twelve; removing it would leave a nonzero W' system of degree one. The divisor's defining section has trivial character since G is perfect, so the residual representation would still be W'. But H0(O(1))=W contains no W'. Thus W' O(5)->O(18) also has no common zero. Both maps are everywhere onto their line targets, not injective.

Rows14 and17 use the identity of the unique W' O(5) atom. In row15 the unique channel is the tensor Euler inclusion

    0 -> W' O(5) -> P O(6) -> W' O(7) -> 0,

using P=W' tensor W. In row20 dualizing (3) and twisting by O(10) gives

    0 -> W' O(5) -> V O(8) -> O(14) -> 0.

Uniqueness of the nonzero Hom line identifies gamma with these universal maps up to a scalar in the indicated rows. This proves constant fiber rank and local freeness of C/I in every case. The ranks vary: gamma has rank1 in rows9,10,18 and rank2 in the other rows. Neither alternative is selected. Since (3) is onto, the actual image of the weighted term J tensor V O(2) in C is exactly I as well.

## 7. Scope and reproduction

The substantive construction is the actual sixteen-source weighted presentation, through the twenty-source intermediate, and its complete-evaluation bridge, followed by saturation of the remaining canonical weighted image. It leaves the actual row and the relative position of the initial marked line versus K0 unresolved. Table (16) is conditional on exhaustive necessary types, not a realization or a new source cut. No equality with separately marked conditional im-h or mixed-Q subspaces is asserted.

The verifier authenticates both immutable originals and checks only fixed representation channels, seven conditional Hom-space tests, and universal rank/degree balances. REPRODUCE.md reconstructs omitted audit inputs. REVIEW.md records independent whole-proof review of the final bytes; no proof-assistant formalization or actual-instance computation is claimed.
