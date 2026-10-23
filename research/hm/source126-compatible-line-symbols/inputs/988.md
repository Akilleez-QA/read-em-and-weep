# Six necessary compatible-line rank footprints for source126

## Statement and scope

Retain the actual source126 balanced-bundle, negative-pencil, invariant-product and original second-symbol hypotheses of the immutable inputs. Let 0≠j be one radical element commuting with the actual invariant quadratic Q. This includes, but does not require, dim J_Q=1. Then its endpoint rank pair belongs to

    Type I:       (4,4), (9,9), (5,4), (9,4);
    Type II:      (4,4), (9,9), (5,4), (10,9), (9,4), (14,9).
    Type III:     (9,9), (10,9), (14,9).

These are exhaustive NECESSARY footprints, not asserted actual realizations. In every type each nonzero radical has nonzero fourth-endpoint P row. The Type III assertion extends the published Types I/II row theorem without assuming that its Y inclusion is an actual first polar.

The two pairs (9,4) and (14,9) force every j-commuting map N2→N4 to have rank at most36. For the actual family Q+tT_a this forces exact generic rank36 and vanishing of every original generic Bockstein after the second. The other four rows admit surjections between their abstract square-zero endpoint modules, so endpoint-module rank data alone cannot exclude surjectivity there. This is not an actual HM construction or a source/pair exclusion.

No selected actual parameters, coefficients, points or instance ranks are evaluated. No full-J collective-image argument is imported. The full-J image/top calculation was read to separate this single-element classification from that work.

## 1. Exact interfaces and the Type III P row

PR944 gives

    N2=A+2V+3P+4D, N4=2V+4P+3D,
    ker Q=A+D, coker Q=P.

Here dimensions are A=V=3, P=4, D=5. Every radical maps the residual R block into F and kills F. The common actual bundle data are

    F=(P+2D)O(-2)⊂C O, C=A+V+P+D, C O/F=O(28),
    R=X⊕Y, X=O(-8), Y=W O(-9).

The endpoint F characters are N2_F=A+2V+2P+2D and N4_F=P+2D. The residual characters are N2_R=P+2D and N4_R=2V+3P+D. Type I radicals kill the isolated X vertex, leaving source N2_Y=P+D and target N4_Y=V+2P+D. Types II/III only need the residual character bounds here.

PR970 already proves that a nonzero Type I/II radical cannot have zero P row. We prove the same in Type III. Suppose its P row is zero. By the natural Serre-dual isomorphism of PR946, its actual bundle map R→F lands in 2D O(-2). Its restriction to X is zero, since Hom_G(X,D O(-2))=0: Sym6 W=V+P contains no D. Type III has actual constant span X=P+D. Therefore the constant map b defining j has b_P=b_D=0. Because R spans its ambient residual space, j nonzero implies its Y restriction nonzero.

As an ABSTRACT equivariant bundle Y=W O(-9), it has a unique map to D O(-2), up to scalar. PR959 identifies this map with dr8 and proves: any degree-two polynomial matrix p with p dr8=0 is zero. This statement depends on the abstract Y bundle and unique D-valued degree-eight covariant, not on the actual inclusion of Y. The two D components of j|Y therefore factor through one constant multiplicity line D O(-2)⊂2D O(-2), with inclusion p into C O. Since b_P=b_D=0, the P and D projections satisfy p_P dr8=p_D dr8=0, hence p_P=p_D=0. Thus p embeds D O(-2) into (A+V)O.

This is saturated: the copy is a direct summand of F, and F⊂C O has locally free quotient. Its quotient inside (A+V)O is an equivariant line O(10), with no character twist because G is perfect. The top map q:C O→O(28) kills F, so its restriction to (A+V)O factors through O(10)→O(28). The restriction is nonzero, since otherwise H0(F)=0 would contain nonzero constant sections. But H0(O(18))^G=0, as in PR970. Contradiction.

Consequently the linear P-row map from the two-dimensional radical is injective in Type III as well. No integrability or first-polar identity for the Type III Y inclusion was used.

There is a further Type III constraint for COMPATIBLE nonzero j. PR946 proves its Y-arrow component is nonzero. PR862 Section3 identifies J_Y as the kernel of the two scalar A,V restrictions to the tail Hom space, with the V restriction nonzero. Hence any nonzero Y-arrow has nonzero constant A coefficient: setting that coefficient to zero would force its V coefficient to zero as well. If j had zero D row at N4, natural Serre duality would make its bundle map land in P O(-2). But the coefficient span of any equivariant inclusion P O(-2)→C O is contained in P⊗A=V+P+D, with no A. The actual image b(R) has nonzero A coefficient span because R spans Hbar and b_A≠0. Contradiction. Therefore every compatible nonzero Type III j has nonzero D row as well.

## 2. Single-element image multiplicities

Write actual images as

    im j2=uP+vD,       im j4=P+δD.

The first statement follows from the residual source and F target characters; u∈{0,1}, 0≤v≤2, and v≤1 in Type I. The second follows from Section1 and the single residual D copy, with δ∈{0,1}, and Section1 forces δ=1 in Type III. These denote actual subspaces, not preferred irreducible copies.

Q is injective on its entire P source and onto its entire D target. Compatibility yields

    Q(im j2_D)=im j4_D.

Indeed j4 Q=Q j2 and Q maps N2_D onto N4_D. Let k be the multiplicity of the intersection im j2_D∩ker Q_D. Since ker Q_D is irreducible, k∈{0,1}. Rank-nullity now gives the exact equality

    v=δ+k.                                                   (1)

In particular k is not inferred from a common-kernel dimension or individual rank bound.

For U=ker j2 and Z=ker j4, square-zero equivariant action on the multiplicity-free ker Q=A+D is zero. Thus ker Q⊂U, and U→Z is an actual negative subpencil. Its characters are

    U=A+2V+(3-u)P+(4-v)D,
    Z=2V+3P+(3-δ)D,
    Q(U)=2V+(3-u)P+(3-v)D,
    coker(Q|U)=uP+kD.                                      (2)

If u=k=0, Q|U is onto Z. For an original A kernel vector h, solve Qu=-T_a h inside U. Since U→Z is a negative subpencil, T_a u lies in Z=Q(U), so the original second obstruction is zero. Comparison with any canonical first correction differs by ker Q, on which the ORIGINAL first symbol vanishes. Thus this would annihilate the same actual second A-to-P symbol, contradicting its retained nonvanishing theorem. Therefore

    (u,k)∈{(1,0),(0,1),(1,1)}.                             (3)

Enumerating (1)-(3) with δ∈{0,1} gives exactly the six rows:

| u | k | δ | v | rank j2 | rank j4 | Type I allowed |
|---|---|---|---|---|---|---|
|1|0|0|0|4|4|yes|
|1|0|1|1|9|9|yes|
|0|1|0|1|5|4|yes|
|0|1|1|2|10|9|no|
|1|1|0|1|9|4|yes|
|1|1|1|2|14|9|no|

For Type III only the three rows with δ=1 survive the additional coefficient-span argument.

The imported faithfulness excludes j2=0 independently; our list already has positive first rank. The quotient Q on N2/U→N4/Z has kernel kD and cokernel (1-u)P: on P, if Qx∈Z, Qj2x=j4Qx=0 and P-injectivity forces x∈U; on D, surjectivity of Q gives quotient surjectivity. This is another exact invariant of every row.

## 3. The single-image quotient obstruction

Any j-commuting f carries im j2 into im j4. Hence a surjective f would induce a surjection

    N2/im j2 → N4/im j4.

Their dimensions are 41-rank j2 and 37-rank j4. Necessary surjectivity is therefore rank j2-rank j4≤4. In the table this difference is

    4(u-1)+5k.

The two u=k=1 rows have difference5. Their quotient target exceeds source by one, so every commuting f has cokernel dimension at least1, or rank≤36. This remains valid after any scalar-field extension and does not assume f is G-equivariant. It therefore applies to all actual Q+tT_a, since the fixed-pencil radical commutes with every negative quadratic.

At the generic negative direction, Q has rank33, the original first symbol vanishes, and the original second has rank3, as recorded in the pinned original theorem. Over the generic formal Laurent-series field this gives rank at least36. Combining the preceding upper bound gives exactly36. Cancelling 33 unit pivots and three order-two pivots leaves a 1×5 formal residual matrix. Any nonzero entry would increase rank to37, so the residual matrix is zero. Thus all generic original symbols after the second vanish. No exceptional-direction extra A-kernel assertion is made.

## 4. Sharp endpoint-module boundary

A square-zero operator of rank r on an n-dimensional vector space gives the module

    R^r⊕S^(n-2r), R=C[ε]/(ε²), S=R/(ε).

A surjection from a source module with dimensions (n,r) to a target (m,s) requires r≥s, by mapping ε-images onto ε-images, and n-r≥m-s by the preceding top-quotient argument. These conditions are sufficient: assign s source R blocks identically to target R blocks; use remaining source blocks through their simple tops to cover the m-2s target S blocks. The number available is (r-s)+(n-2r)=n-r-s, at least m-2s precisely when the top inequality holds.

Every row here has rank j2≥rank j4. Thus the four non-forbidden rows satisfy both criteria and have abstract module surjections; the last two fail exactly the top inequality. This does not assert that these abstract maps are actual multiplication maps, preserve G, or arise from a source occurrence. It identifies the precise limit of the endpoint square-zero module obstruction.

The checker constructs constituentwise synthetic Q/j diagrams for all six rows with the correct full Q kernel/cokernel, compatibility, image ranks and quotient kernels. It then explicitly constructs commuting surjections in all four permitted endpoint-module rows. These examples prevent accidentally treating a necessary footprint as an actual HM realization or extending the top obstruction to rows where it does not apply.

## Evidence and remaining gate

All source bytes are pinned by Git blob and SHA256 in INPUTS.json. The bounded checker uses only exact synthetic matrices, finite multiplicity enumeration and imported universal invariant facts. It does not re-run an actual experiment. The remaining geometric task is to select or exclude the possible single-line image multiplicities, or prove an obstruction beyond square-zero endpoint-module ranks. No such selection is made here.
