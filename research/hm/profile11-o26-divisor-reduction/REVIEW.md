# Independent exact-version review: O(26) common-divisor reduction

## Verdict and exact scope

**Sound for the stated, limited conclusion.** I found no mathematical defect in the reviewed version. The proof excludes the degree-twelve common-divisor stratum for all sources in the three stated zero-original-defect profile-(1,1) labels. It also shows that a degree-twenty divisor can occur only in the matching E6/E13 source types and then forces an actual complete degree-ten osculating subsystem.

The reviewed `PROOF.md` has SHA256

    16d4c27256932b57b3395edd39ec7118e37e7b00757a4d969a7e17b0b2c84bad

This verdict does **not** exclude any of the three full O(26) labels. It leaves their degree-zero divisor strata open; it does not exclude or constantly separate the surviving degree-twenty strata. It makes no new source2 or global-rank conclusion. The proof was not edited in this audit.

The most important successful distinctions are between the raw first span and its saturation, between sheaf intersections and intersections of fibers, and between the actual modified projected kernel M' and its saturation M. None of these distinctions is silently discarded.

## 1. Immutable inputs actually read

All following files were retrieved from the specified immutable commits of [Akilleez-QA/read-em-and-weep](https://github.com/Akilleez-QA/read-em-and-weep), and their contents were read. The retrieved bytes were also checked against the returned Git blob identifiers.

At commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, under `research/hm/order-four-quadratic-load/`:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`, blob `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`, blob `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.
- `one-one-endpoint-necessary-pairs.json`, blob `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`, blob `8b5971092f9ef762584912609fd5e9301c4e271d`.

The five structural dependencies read were:

1. [PR796 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md), commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`, blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`, SHA256 `622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1`.
2. [PR797 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/cdee9396133fb96d4a91babba87b1a7a35903635/research/hm/profile12-tensor-quartic-block/PROOF.md), commit `cdee9396133fb96d4a91babba87b1a7a35903635`, blob `f397008bad1724ba3e81bdf84b5071fbc516f015`, SHA256 `863bb17be118558b5c6199d0b3b73a7257cdd1f6871cdd903be2a19128574c98`.
3. [PR798 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/2bbf244bafc380cf5b0ce1114f86fcd8053e4e55/research/hm/profile12-backward-plateau-exclusion/PROOF.md), commit `2bbf244bafc380cf5b0ce1114f86fcd8053e4e55`, blob `835404ada200cea294aa0cf0b13d962bd604cdc0`, SHA256 `4ddb4c7993039cf0e4504c2cd7403b45925a508a6489cc366ac9892ba39f53e0`.
4. [PR799 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md), commit `2172e4a7abbbe232f9f448bea6fa01dee7927460`, blob `a62a56f6b8f97e02b3eab6fe3a47ec3bedb6c6b1`, SHA256 `3a55f2c37548c7b05bf0f39f775ab37807c9f852d3601f77271fc0dd052022ed`.
5. [PR804 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/ae34a9403c0c2abf00516ca35dd494723034c38a/research/hm/profile11-degree28-simple-polar-exclusion/PROOF.md), commit `ae34a9403c0c2abf00516ca35dd494723034c38a`, blob `5c12041ebd5282024aa994062232e781242ca535`, SHA256 `5f145e5fb7c6b791c9200d5c58d58618312443c80cc5ae30db1dbef132a41527`.

PR797's interior-stage intersection proof is not imported. Only its small kernel and quotient classifications, constant-span calculation, and Euler-extension calculation are used after their hypotheses are re-established. Similarly, PR796's profile-(1,2) absence-of-sections contradictions are not imported. Its degree-sixteen kernel calculations and profile-free quadratic Gauss gap are sufficient.

## 2. Exact labels and source lists

Direct inspection of the pinned JSON confirms:

- `G3.11.dc58cc54f352` is source index 112, with A_q=O(-10)+O(-8)+O(26), B_q=O(-28)+O(6)+O(8), and original defect zero.
- `G3.11.4b6dad66f329` is source index 115, with A_q=W O(-9)+O(26), B_q=O(-28)+W O(7), and original defect zero.
- `G3.11.8ae96830fd21` is source index 126, with A_q=2 O(-8)+O(26), B_q=O(-28)+2 O(6), and original defect zero.

Index 112 has exactly the four tuples

    (0,0,0,0,0,2,0,1), (0,0,0,0,1,1,0,1),
    (0,0,1,0,0,1,0,1), (0,1,0,0,0,1,0,1).

Index 115 has those four and exactly

    (0,0,0,0,0,1,1,0), (0,0,0,0,1,0,1,0),
    (0,0,1,0,0,0,1,0), (0,1,0,0,0,0,1,0).

Index 126 has exactly

    (0,0,0,0,0,2,0,1), (0,0,0,0,0,1,1,0),
    (1,0,1,0,0,2,0,0).

Substitution into the pinned catalog formula

    R_2=(c+g+h-1)V+(d+e+g+h)P+(f+g)D

and its eight lower-block rows gives precisely the displayed E0, U6, E3, E6, E10, U13, E12, E13, and E18 types. U6 and U13 are local descriptive names, not claimed catalog indices. No source is omitted from these overlists.

## 3. Common divisor and raw-span audit

Let F=R O(-2). The genuine quotient E->A_q has zero negative components on F by degree. The strict-top vanishing injects R into H0(O(28)). If delta is the common-divisor degree, division by its invariant equation leaves an injection into H0(O(28-delta)), with basepoint-free evaluation. Every listed R has dimension at least nine, so delta<=20. The possible projective orbit sizes are 12,20,30,60. Thus only 0,12,20 occur; each positive possibility is a reduced single orbit. Perfectness removes any nontrivial semi-invariant character.

The raw construction is valid without projection saturation. If I is the image of the derivative of F in (H O/F)(-2), then projection to Q(-2) has image O(26-delta). Its kernel is the internal image J of K0. Hence

    0 -> J -> I -> O(26-delta) -> 0.

Taking the inverse image of I(2) in H O gives the raw span B and

    0 -> F -> B -> I(2) -> 0.

These are sequences of locally free image sheaves on the smooth curve, but they do not say that B is saturated in H O. In particular, external base zeros do not imply zeros of the full internal-plus-external image.

For the saturation F^+, the quotient F^+/B is invariant torsion. Its nonzero length is at least twelve. Since F^+ embeds saturatedly in a constant bundle, deg(F^+)<=0, and therefore

    0<=length(F^+/B)<=-deg B.

The first-polar map has image B itself, not merely its generic span. This follows locally from the value and derivative of a quadratic column; the Euler relation supplies the value from first polars and the derivative is the other first-polar direction. Thus B(1) is generated by global sections. An injective sheaf map B->H O rules out positive splitting degrees even before saturation. Consequently B has only degrees -1 and 0. This reasoning does not incorrectly use fiberwise injectivity of the image sheaf at a torsion point.

I also independently recover the gap used repeatedly: a saturated rank-r quadratic block with rank-one first quotient O(b) reaches its constant coefficient space after two transforms. The next derivative factors through O(b), so that space has dimension r+1 or r+2. The first case gives b=2r. The second gives a nonzero map O(b)->O(2r-b-2), hence b<=r-1. No endpoint/interior hypothesis enters.

## 4. Degree-twelve source reductions

The residual degree-sixteen system has character Sym16 W=V+P+2D. The top 2P+D is therefore impossible immediately, removing U6 and U13 in this stratum.

For E0 and E10, K0(2) has thirteen strictly negative degrees with total -16. Each is at least -4, so all K0 degrees are at least -6. The internal target degrees are at most -10, and J=0. The raw B has rank 15 and degree -12. Its saturation defect is 0 or 12. The zero case gives the forbidden gap r=14,b=16. The defect-twelve case makes F^+ a constant fifteen-space. Its quotient by F is O(28), and the constant character is

    Sym28 W-(P+2D)=A+V+P+D.

The map O(28)->Q lands in the positive O(28), is nonzero, and has equal source and target degree. It is therefore an isomorphism onto that saturated line. In this actual constant space the full derivative of F has image f12 O(14) in O(26), exactly as required for the polar obstruction.

The PR804 obstruction does not depend on its old lower tail or old label. Its applicable content is local to this constant quotient: the unique V in Sym28 equals f12 times the unique V in Sym16. The latter system is basepoint-free, since a common degree-twelve divisor would require a nonzero map V->Sym4 W=D. The simple zeros of f12 therefore make the quotient's projective derivative nonzero at every point of D12, while the full Gauss derivative of its kernel vanishes there. This contradiction applies to both current source types.

For E3 and E12, the two possible exact K0 types are those in the proof. The only component not immediately killed by degree would be O(-8)->V O(-6), and its Hom vanishes because Sym2 W=A does not contain V. Thus J=0, rank B=13, deg B=-8; no invariant nonzero torsion of length at most eight is possible. The gap at r=12,b=16 excludes them.

For E18, the degree-sixteen kernel is S O(-3)+V O(-4)+Wp O(-5). The only internal channel is the scalar Wp O(-5) endomorphism. Its zero case has (rank B,deg B)=(11,-4), and its nonzero case has (13,-10). Both are already saturated by the torsion bound. The first violates the gap. In the second, first-polar characters give B=V O+(S+T) O(-1). The actual constant V projection is legitimate, and the independent two D channels force S O(-1) in the projected F. Its constant first span cannot lie in the pure degree-minus-one projected B. This is exactly the profile-free part of PR799, with saturation established anew.

Only P+D remains. The mismatched E6 source cannot surject onto W O(-9), since only its O(-10) line can map to that rank-two target. Thus the remaining negative summand is exactly the matching L in both surviving source cases.

## 5. The rank-nine raw alternatives and the constant-twelve-space case

For F=(P+D) O(-2), the degree-sixteen kernel calculation gives exactly the three types listed in the proof. In the first two, J=0; the apparent O(-8)->T O(-5) channel vanishes because Sym3 W=S has no T. A zero J gives rank B=10, degree -2, no torsion, and the forbidden gap r=9,b=16.

The remaining unique nonzero channel Wp O(-7)->T O(-5) is the Wp tensor of the complete quadratic line inclusion. It is saturated internally, and gives

    0 -> Wp O(-5) -> B/F -> O(16) -> 0,
    rank B=12, deg B=-12.

First-polar generation forces B pure degree -1; its coefficient character is Wp+S+T. The only possible saturation lengths are 0 and 12.

When the length is twelve, F^+=C O is a genuine constant twelve-space. Its positive image in E^+/E contains f12 O(16), so it is either f12 O(16) or O(28). The former would make E∩C O have rank eleven and degree -16, impossible since all degrees of a subbundle of E are <=-2. Thus the positive image is O(28), and N=E∩C O has rank eleven and degree -28.

The raw intersection E∩B has the same rank and degree, since its quotient by F is Wp O(-5). Its inclusion in N is therefore equality, proving N/F=Wp O(-5), rather than merely a generic identification. The unique quadratic inclusion into T O(-3) has quotient P O(-2), and it has no component into L. Hence E/N=P O(-2)+L.

Moreover C O/N is the entire saturated O(28) in Q. Consequently E+C O is saturated in H O, and E/N is actually saturated in (H/C) O. The induced derivative there factors through L. It kills P O(-2) by degree, and the internal derivative of this top block into L(-2) is zero as well. This makes the nonzero negative top block horizontal in a genuine constant quotient, an impossibility in characteristic zero. The saturation step needed for this contradiction is proved, not presumed.

## 6. Quartic identification and endpoint-safe intersections

When the length is zero, F^+=B is saturated and pure degree -1. The rank-three quotient classification of PR797 uses only the exact sequence above, its cohomology, and this splitting. It gives F^+/F=V O(2). The constant-span argument then gives the actual complete evaluation sequence

    0 -> F^+ -> C0 O -> V O(4) -> 0,
    C0=V tensor Sym4 W,
    F^+=V tensor U_3^4,  F=V tensor U_2^4.

In particular the induced derivative V O(2)->V O(2) is an isomorphism. These conclusions do not need the interior condition from the old application.

Set I0=E∩F^+. The raw image sequence gives I0/F=Wp O(-5) and F^+/I0=O(16), whose image in E^+/E is f12 O(16). Because I0 is in E, its derivative is in E^+. The derivative isomorphism above therefore shows that C0 O/(E^+∩C0 O) has generic rank at most one.

Generic rank zero would imply C0 O⊂E^+ as sheaves, since E^+ is saturated. Its image in E^+/E has no negative component. The two possible positive images would give kernels of rank fourteen and degrees -16 or -28 in E. The first violates maxdeg(E)<=-2. The second must be O(-2)^14, but every map from that bundle to E lands in its rank-nine top block. Both are impossible.

The generic rank is thus one. The derivative kernel on F^+ has rank eleven and contains I0. Both are saturated in F^+, so equality holds as sheaves. This is the replacement for the inapplicable assertion (E^+)^-=E. It yields

    Nplus/F^+=Wp O(-3),
    C0 O/Nplus=O(18),
    rank Nplus=14, deg Nplus=-18.

Twisting the displayed extension by three and using H1(O(2))=0 proves that Nplus(3) is globally generated. Hence Nplus has no component mapping to L(2). Its positive image contains f12 O(16), so its rank-thirteen intersection N=E∩C0 O is well defined with one of the same two possible divisor choices.

The constant connection gives N⊂Nplus^-. The derivative of Nplus onto O(16) is already surjective on F^+, by the derivative isomorphism and the quotient F^+/I0. Therefore Nplus^- has rank thirteen and degree -34. Both N and Nplus^- are saturated in C0 O. Their equal-rank inclusion gives equality, without using fiberwise intersections. Consequently

    N=Nplus^-,  deg N=-34,  Nplus/N=O(16).

Its image in E^+/E must therefore be the degree-sixteen sheaf f12 O(16), not O(28). This verifies the essential twelve-point modification rather than erasing it.

The ensuing exact extension of Wp O(-3) by Wp O(-5) is forced to be the nonzero Euler extension: a split Wp O(-3) cannot inject into T O(-3)+L. Thus N/F=P O(-4). The unique linear inclusion into T O(-3) has quotient M=Wp O(-1), giving the actual image sheaf E/N=M+L. Saturation of the whole image is neither proved nor used.

## 7. Modified backward image and independent derivative ranks

The image of N under E->A_q is exactly f12 O(14). Containment follows by differentiating into Nplus and twisting its established positive image by -2; equality follows already from the image of F. Therefore the induced quotient is

    E/N=M+L -> L+T12,
    T12=O(26)/(f12 O(14)).

The L component is zero on M and an isomorphism on L. Even if there is an additional component from L to T12, it does not change the kernel: an element in the kernel has zero L coordinate. Surjectivity onto L+T12 then proves M->T12 is onto. Accordingly the actual projected image of K=E^- is

    M'=ker(M->T12),  rank M'=2,  deg M'=-14.

This is not M as a sheaf and is not saturated. Nevertheless the actual inclusion M->(H/C0) O corresponds to a nonzero constant intertwiner Wp tensor W=P->H/C0. Irreducibility of P makes it injective, identifying M with a saturated tautological plane bundle whose Gauss rank is two. M' and M have the same generic embedded plane, so their generic Gauss ranks agree. No fiberwise claim at D12 is needed.

Internally, N=Nplus^- is the first jet kernel for the quotient C0 O->O(18). That quotient is a degree-fourteen three-section system multiplied by the complete quartic system. At every point one of the degree-fourteen sections is nonvanishing, and multiplication by it is invertible on finite jets. The complete quartics therefore supply all jets through order four. This is a uniform arbitrary-point statement, not a selected evaluation.

It follows that N^- is the second jet kernel, and its derivative has nonzero rank one into (N/N^-)(-2)=O(12). Since multiplication by f12 is injective as a sheaf map, K∩C0 O=N^-. Thus this internal derivative remains nonzero modulo K.

At the generic point, the projection H/K->(H/C0)/M' sends the derivative of K onto the rank-two projected derivative. The internal rank-one image just identified lies in its kernel and is nonzero. Hence rank(beta_K)>=3. This contradicts maximal backward index one. As a degree check, deg(K)=-54-8=-62, agreeing with deg(N^-)=-48 plus deg(M')=-14 in both matching branches.

## 8. Degree-twenty complete degree-ten block

At delta=20 the residual degree-eight injection R->Sym8 W=P+D forces R=P+D and is an isomorphism. It is therefore the complete degree-eight evaluation system, whose kernel after the indicated twist is

    K0=Sym7 W O(-3)=(Wp+T) O(-3).

Every internal target degree is <=-5, so J=0. The raw span has rank ten, degree -10, and quotient B/F=O(8). Its saturation defect is zero because any nonzero invariant torsion has length at least twelve. First polars make F^+ pure O(-1).

The quadratic coefficient span is reached after two transforms. The derivative of F^+ kills F and factors through O(8), so its constant span C has dimension at most eleven. It cannot have dimension ten: that would make the saturated F^+ itself constant, contradicting degree -10. Thus dim C=11 and C O/F^+=O(10).

The nonzero induced derivative O(8)->O(8) is an isomorphism. Since H0(F^+)=H1(F^+)=0, the quotient sequence identifies C with all H0(O(10)), not merely an unspecified eleven-dimensional subsystem. It is the complete degree-ten evaluation sequence. Therefore

    C=Sym10 W=A+V+D,
    F^+=U_9^10,
    F=(F^+)^-=U_8^10,
    F^{++}=C O.

These are identities of actual embedded objects after constant equivariant identification. The kernel equality follows from the derivative isomorphism and saturation, not from agreement of abstract splitting types. The same negative-quotient argument excludes the mismatched E6 case. This leaves exactly the two matching source possibilities claimed.

## 9. Verification boundary

The audit checked the exact catalog records and tuple translations, read the pinned structural proofs, and independently followed all new image, saturation, intersection, Euler-extension, jet, and generic-rank arguments. A bounded recurrence in the fixed nine-dimensional representation ring independently confirmed Sym6, Sym7, Sym8, Sym10, Sym12, Sym16, Sym17, Sym28 and the needed Wp tensor identities. No old envelope verifier was executed.

No actual selected HM/source coefficients, parameters, points, derivative values, matrices, source-instance ranks, selected models, scans, or large computation were used. All ranks here are universal deductions under the formal branch assumptions. No external write or publication was performed by this audit.

The result is a written exact-version mathematical review, not proof-assistant certification. The original actual-bundle inputs remain explicit dependencies. Within that boundary, the degree-twelve exclusion and degree-twenty complete-block necessity are established; the degree-zero strata, the surviving degree-twenty strata, source2, and the original global goal remain unresolved.
