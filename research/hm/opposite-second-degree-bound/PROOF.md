# A second-degree invariant bound for the actual opposite bundle

Work over C in the current normalizer convention: G=2I, H=V⊕W is the coordinate representation, N=A⊕W', K=Ω²P4(2), and B=End0(F) for the normalized HM bundle. C is the actual opposite bundle on the negative parameter line T. All parameter line bundles have their standard equivariant linearizations.

## 1. Immutable interface and statement

INPUTS.json specifies the exact immutable originals.

- TWIST (PR455) supplies the graded symmetric-square monad representing B(-1), and the exterior Euler resolution of K. Its old multiplicity labels are not identified with current labels.
- MONAD (PR928) supplies the actual current monad N* O(-1)→W'⊗K→N O, with N=A⊕W' and H=V⊕W.
- PLANE (PR952) supplies H1(B_R(1))=A⊕V and H1(B_R(2))=H1(B_R(3))=0, the exceptional direct-image filtration for the blowup p:X=Bl_R(P4)→P4, and π*O(1)=p*O(1)(-E).
- AMPLE supplies ampleness, H0(C*(1))=0 or W, and the nine remaining types numbered as in PR948. It also retains the identification C=(R1π_*p*B(3))_+.

We prove the new bound

    dim H0(T,C*(2))^G ≤ 1.                         (1)

It excludes two further types, rows7 and12, leaving exactly rows9,10,14,15,17,18,20 as necessary possibilities. This is a structural exclusion; it does not assert that any survivor occurs.

## 2. Universal untwisted tensor vanishing

The exterior Euler sequence is

    0→K→Λ²H O→H O(1)→O(2)→0.

Tensoring with K gives an exact resolution of K⊗K by Λ²H⊗K, H⊗K(1), and K(2) in degrees0,1,2. Bott cohomology gives Hq(K)=0 for every q, and Hq(K(1))=Hq(K(2))=0 for q>0. Consequently

    H2(K⊗K)=coker[H⊗H0(K(1))→H0(K(2))].           (2)

The homogeneous degree-three and degree-four pieces of the ordinary Koszul complex of Sym(H) give the canonical identities

    H0(K(1))=Λ³H,
    0→Λ⁴H→H⊗Λ³H→H0(K(2))→0.                      (3)

Indeed H0(K(t)) is the kernel of Λ²H⊗Sym^t H→H⊗Sym^(t+1)H. Exactness of the positive-degree Koszul complex identifies that kernel with the image of its preceding term. For t=1 that term is Λ³H; for t=2 it is Λ³H⊗H with kernel Λ⁴H. The map in (2) is precisely multiplication by H under these identifications. Thus it is onto and

    H2(K⊗K)=0.                                    (4)

This is a universal exact complex, not a selected tensor or point calculation. In characteristic zero Sym²(W'⊗K) is a direct summand of (W'⊗W')⊗(K⊗K), so its H2 also vanishes.

## 3. The remaining total-degree-two term

The graded symmetric square of the actual monad, quasi-isomorphic to B(-1), has terms in degrees -2 through2:

    Λ²N* O(-2),
    N*⊗W'⊗K(-1),
    Sym²(W'⊗K) ⊕ (N*⊗N) O(-1),
    W'⊗N⊗K,
    Λ²N O.

Its hypercohomology E1 terms of total degree2, other than the last term's H0, vanish: H4(O(-2))=0, H3(K(-1))=H3(Ω²(1))=0, the central H2 vanishes by (4) and H2(O(-1))=0, and H1(K)=0. Hence the only possible associated-graded contribution to H2(B(-1)) is E∞^(2,0).

No spectral differential leaves (2,0): the complex ends at degree2. Incoming differentials may be nonzero and are not discarded. Therefore there is a natural equivariant surjection

    Λ²N → H2(P4,B(-1)).                            (5)

The current fixed character identity Λ²N=1⊕A⊕T6 now gives

    dim H2(P4,B(-1))^G ≤1.                         (6)

No assertion that (5) is an isomorphism is required.

## 4. Two Leray sequences with the connecting maps retained

Set

    M=p*B(3)⊗π*O(-4)=p*B(-1)⊗O_X(4E).

Then p_*M=B(-1), Rq p_*M=0 for q≥2, and J=R1p_*M has the actual successive layers

    i_*B_R(1),   i_*(W⊗B_R(2)),   i_*(A⊗B_R(3)).   (7)

These are the j=2,3,4 exceptional layers, with Sym^(j-2)W and twist j-1 after tensoring by B(-1). We do not split their extensions. The last two layers have H1 zero. Their exact sequences show that H1(J) is an equivariant quotient of H1(B_R(1))=A⊕V. In particular H1(J)^G=0.

In the two-row p-Leray spectral sequence the only total-degree-two contributions are E∞^(2,0) and E∞^(1,1). The latter has no invariants, since it is a subquotient of H1(J). The former is the quotient of H2(B(-1)) by the possibly nonzero transgression from H0(J). Exactness of invariants therefore gives

    dim H2(X,M)^G ≤ dim H2(B(-1))^G ≤1.            (8)

On the curve T, π-Leray has the canonical injection

    H1(T,(R1π_*p*B(3))(-4)) ↪ H2(X,M).

The summand C(-4) supplies an injection on its H1. Equivariant Serre duality on T, using det W=1 and ω_T=O(-2), identifies H1(C(-4)) with H0(C*(2))*; taking invariants proves (1).

## 5. The seven remaining possibilities

For a positive splitting atom L O(d), its contribution to H0(C*(2)) is L*⊗Sym^(2-d)W when d≤2, and zero otherwise. Thus O(2) contributes one invariant, W O(1) contributes one, and A O(2) contributes none. The exact invariant dimensions on AMPLE's nine rows are:

    row:        7  9 10 12 14 15 17 18 20
    dimension:  2  1  1  2  1  1  1  1  1.

Rows7 and12 are therefore impossible. The survivors are

 9. O(2)⊕O(12)⊕V O(4)
10. O(2)⊕O(18)⊕A O(2)
14. O(2)⊕W' O(5)⊕W' O(7)
15. O(2)⊕P O(6)
17. O(14)⊕W O(1)⊕W' O(5)
18. O(18)⊕W O(1)⊕W O(3)
20. W O(1)⊕V O(8).

The rank-one top obstruction case remains exactly row9, and only that row can carry a nonzero invariant vertex extension, as already proved in AMPLE. Neither its scalar nor the actual surviving row is selected here. No source/frontier ledger is changed. The only arithmetic is a fixed character calculation and a filter of nine authenticated abstract rows; no selected actual HM/source coefficients, points, parameters, jets, derivatives, matrices, or instance ranks are evaluated.

## 6. A canonical quotient and a forced invariant transgression value

Every surviving row has invariant dimension exactly one in the table. Thus

    Hom_G(C,O(2))=H0(C*(2))^G≅C.

Every nonzero map in this line is onto. For rows9,10,14,15 it is the projection to the O(2) summand, up to scalar. In row10 the A O(2) summand contributes no invariant map. For rows17,18,20 it is the unique equivariant Euler map W O(1)→O(2); all remaining summands have degrees greater than two and admit no map to O(2). The Euler sequence is

    0→O→W O(1)→O(2)→0.

It follows that the actual C has a canonical rank-four subbundle Q, independent of the nonzero scalar chosen for the quotient map, with

    0→Q→C→O(2)→0,      rank Q=4, deg Q=24.

The possible Q types, in the same row order, are

 9. O(12)⊕V O(4)
10. O(18)⊕A O(2)
14. W' O(5)⊕W' O(7)
15. P O(6)
17. O⊕O(14)⊕W' O(5)
18. O⊕O(18)⊕W O(3)
20. O⊕V O(8).

The quotient sequence splits equivariantly in the first four cases and has its nontrivial Euler component in the last three. This is a structural description of the unique quotient, not a choice of the actual row.

Finally the lower bound one from the table forces equality throughout (8) and the π-Leray invariant injection. Therefore

    dim H2(B(-1))^G=dim H2(X,M)^G=1,
    H1(C(-4))^G → H2(X,M)^G is an isomorphism.

Since H1(J)^G=0, the p-Leray filtration identifies H2(X,M)^G with the quotient of H2(B(-1))^G by the invariant transgression. Equality of their dimensions proves that the actual map

    H0(J)^G --d2--> H2(B(-1))^G

is zero. This vanishing is forced by exact geometry and the authenticated finite list, without evaluating that differential.

This last vanishing is not a new nontrivial scalar evaluation: it is also immediate from H0(J)^G=0. Indeed PLANE gives H0(B_R(1))=0, H0(B_R(2))=A and H0(B_R(3))=1⊕P⊕2D; neither W⊗A nor A⊗(1⊕P⊕2D) contains an invariant. Applying exactness of invariants to the filtration (7) proves the asserted domain vanishing. The substantive additional equality is the nonzero one-dimensional H2(B(-1))^G and its identification through Leray with the unique quotient line.
