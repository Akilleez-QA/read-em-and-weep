# Recovering the quartic intersection at a forward endpoint excludes two profile-(1,1) labels

## Result and scope

The following two zero-defect maximal profile-(1,1) labels are impossible:

    G3.11.18ad6075be86:
      A_q=O(-10)+O(-8)+O(14), B_q=O(-16)+O(6)+O(8);
    G3.11.86279023dea2:
      A_q=W O(-9)+O(14),     B_q=O(-16)+W O(7).

Both original determinant defects are zero. The new step is recovery of the exact tensor-quartic sheaf intersection when E^+ is an endpoint. We do not assume either H0(E^+)=0 or (E^+)^-=E. Instead, the actual positive quotient, a degree obstruction to a constant fifteen-space lying in E^+, and an elementary lower-slope bound recover the needed intersection. The resulting independent internal and projected derivative contributions force a longer backward plateau.

This excludes exactly the two named labels. It does not exclude any other profile-(1,1) label or the source2 profile-(2,1) label, and does not establish the original global rank goal. No selected actual coefficients, parameters, points, derivatives, matrices, source-instance ranks, model experiments, scans, or large computation are used.

## 1. Immutable public dependencies and complete source lists

All original source and quotient data are at commit

    db51525015bb7c5e825833d550d08dedf6f6ea96

under

https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/

The exact files are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md, one-one-endpoint-necessary-pairs.json, and rank-three-quotient-frontier-144.json.

The stable labels have source_index4 and source_index6 in the one-one catalog, respectively. Their complete compatible source tuples are:

    index4:
      (0,0,0,0,0,2,0,1), (0,0,0,0,1,1,0,1),
      (0,0,1,0,0,1,0,1), (0,1,0,0,0,1,0,1);
    index6: all four above, together with
      (0,0,0,0,0,1,1,0), (0,0,0,0,1,0,1,0),
      (0,0,1,0,0,0,1,0), (0,1,0,0,0,0,1,0).

Using the catalog formula, the first four are

    E0 = (P+2D) O(-2)+2 O(-8)+O(-10),
    U6 = (2P+D) O(-2)+Wp O(-5)+O(-8)+O(-10),
    E3 = (V+P+D) O(-2)+V O(-4)+O(-8)+O(-10),
    E6 = (P+D) O(-2)+T O(-3)+O(-8)+O(-10).

The four additional types are

    E10 = (P+2D) O(-2)+O(-8)+W O(-9),
    U13 = (2P+D) O(-2)+Wp O(-5)+W O(-9),
    E12 = (V+P+D) O(-2)+V O(-4)+W O(-9),
    E13 = (P+D) O(-2)+T O(-3)+W O(-9).

The notation U6,U13 merely names the two displayed extra types, not a new catalog indexing convention.

The following structural statements are used at their exact public pins:

- PR796, d2b43060c83328dd5118aee6b9288fcfa0c873ac, research/hm/profile12-quadratic-block-exclusion/PROOF.md, Sections2-5,7-8: basepoint-free top systems, actual saturated derivative-image lemma, small kernel computations, and the profile-free quadratic Gauss-gap lemma.
- PR797, cdee9396133fb96d4a91babba87b1a7a35903635, research/hm/profile12-tensor-quartic-block/PROOF.md, Sections2-5 and7: the small V+D kernel support, rank-three quotient and constant-span classifications, and Euler-extension argument. The old use of H0(E^+)=0 and the old interior-stage intersection argument are not imported.
- PR798, 2bbf244bafc380cf5b0ce1114f86fcd8053e4e55, research/hm/profile12-backward-plateau-exclusion/PROOF.md, Sections3-6: the generic internal/projected rank argument. It is restated below with the present hypotheses, which supply its needed actual maps.

The corresponding direct links are

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

https://github.com/Akilleez-QA/read-em-and-weep/blob/cdee9396133fb96d4a91babba87b1a7a35903635/research/hm/profile12-tensor-quartic-block/PROOF.md

https://github.com/Akilleez-QA/read-em-and-weep/blob/2bbf244bafc380cf5b0ce1114f86fcd8053e4e55/research/hm/profile12-backward-plateau-exclusion/PROOF.md

Work over C with the binary-icosahedral notation W,Wp,A=Sym2 W,S=Sym3 W,D=Sym4 W,T=Sym5 W,V,P. All irreducibles are self-dual. E has rank17, degree-54, is saturated in H O, and satisfies H0(E(1))=0 and H0(E^-(2))=0. Its Gauss rank is three. A maximal backward index one means the Gauss rank of E^- is less than three, regardless of the forward index.

## 2. Reduce the source lists without using an interior-stage condition

For a source with top block F=R O(-2), the strict-top vanishing injects R=H0(E(2)) into H0(A_q(2))=Sym16 W. Since

    Sym16 W=V+P+2D,

the types U6 and U13, whose top coefficient is 2P+D, are immediately impossible: their two copies of P cannot inject into a representation containing only one.

For every other listed type, this injection gives at least nine independent sections of O(16). Their common zero divisor would be invariant and, if nonempty, have degree at least twelve, leaving at most five independent sections. Thus the top-block map p:F->O(14) is onto. Because the original defect is zero, O(14) is saturated in Q(-2), where Q=(H O)/E.

Write K0=ker p and let J be the image of the actual internal derivative K0->(E/F)(-2). When J is saturated, the full image is saturated and

    0 -> J -> I -> O(14) -> 0,
    0 -> F -> F^+ -> I(2) -> 0.                         (1)

For E0 and E10 the exact kernel has all degrees between -6 and -3, whereas the target has degrees at most -10. Hence J=0.

For E3 and E12 the complete kernel possibilities are

    T O(-3)+D O(-4),
    (S+T) O(-3)+O(-8).

Only O(-8)->V O(-6) is not excluded by ordinary degrees, and it is zero equivariantly because V does not occur in Sym2 W=A. Again J=0.

The profile-free quadratic Gauss-gap lemma says that, for a quadratic rank-r block with rank-one derivative and F^+/F=O(b), either b=2r or b<=r-1. Equation (1) with J=0 gives b=16. This is impossible for r14 and r12. Thus E0,E10,E3,E12 are all excluded, without using H0(E^+)=0.

Only E6 remains for the first label; only E6,E13 remain for the second. The mismatched E6 source cannot surject onto W O(-9): only its O(-10) summand can map there, so the image has rank at most one. Therefore the only matching pairs left are

    G3.11.18ad6075be86 with E6 and L=O(-8)+O(-10),
    G3.11.86279023dea2 with E13 and L=W O(-9),            (2)

where L is both the high-negative part of E and A_q/O(14).

## 3. Force the same genuine tensor-quartic subsystem

For either source in (2), put F=(P+D) O(-2). The exact top kernel has H1(K0(2))=V+D and chi(K0(3))=0. The complete small support gives precisely

    (V+D) O(-4),
    S O(-3)+V O(-4)+O(-8),
    T O(-3)+Wp O(-7).

The first two give J=0 by degree and the zero Hom O(-8)->T O(-5). The third has only the one-dimensional channel Wp O(-7)->T O(-5). If J=0, (1) gives r9,b16, contrary to 8<16<18 in the profile-free gap lemma. Thus the third kernel occurs and its channel is nonzero. It is the standard everywhere-injective quadratic map Wp O(-2)->Wp tensor Sym2 W O, twisted by -5, so J=Wp O(-7) is saturated.

Equation (1) gives rank F^+=12 and degree F^+=-12. Here we replace the profile-(1,2) no-section argument by first-polar generation. For any actual quadratic inclusion R O(-2)->H O with coefficient map R tensor Sym2 W->H, its value-plus-derivative space at an arbitrary line l is the image of R tensor l W. Thus the first-polar map

    R tensor W tensor O(-1) -> H O

has exactly the raw first-osculation image. In the present case that image is already saturated by (1), so it surjects onto F^+. Therefore F^+(1) is globally generated. Since F^+ is a subbundle of a constant bundle, its degrees are between -1 and0. Rank12 and degree-12 force every degree to be -1. Its exact character from (1) is

    F^+=(Wp+S+T) O(-1).                                 (3)

Now the quotient and constant-span argument of PR797 Sections4-5 applies unchanged: it requires (3), not a section condition on E^+. For clarity, the actual quotient X=F^+/F satisfies

    0 -> Wp O(-5) -> X -> O(16) -> 0,
    rank X=3, deg X=6, H0(X)=P+D, chi(X(-1))=T.

Because X is a quotient of O(-1)^12, all its degrees are at least -1. The complete rank-three degree-six parity list with these characters leaves V O(2) or Wp O(-1)+O(8). The latter cannot surject onto O(16), since the O(8) component has no invariant degree-eight map and cannot lie in the negative kernel Wp O(-5). Hence X=V O(2).

The linear bundle F^+ reaches its constant span C0 after one forward transform. If C=(C0 O)/F^+, then C is positive, of degree12, and its rank is at most three because the derivative factors through X. Rank one is excluded by Hom(V O(2),O(10))=0. Rank two forces two positive even lines summing12, and only the line of degree10 could receive a nonzero map after twisting by -2; the generic image could then have rank at most one. Thus rank C=3, and the generically full-rank equal-degree map V O(2)->C(-2) is an isomorphism.

The actual quotient is the complete evaluation sequence for V O(4). Consequently

    C0=V tensor Sym4 W,     dim C0=15,
    F=V tensor U_2^4,
    F^+=V tensor U_3^4,
    (C0 O)/F^+=V O(4),                                  (4)

where U_j^4 is the complete quartic osculating bundle. In particular the derivative of F^+ induces an isomorphism

    F^+/F=V O(2) -> ((C0 O)/F^+)(-2)=V O(2).            (5)

This is an actual constant subsystem, not an abstract bundle splitting.

## 4. Recover the forward intersection even though E^+ is an endpoint

Let G0=E intersect F^+. The original saturated quotient (1) gives

    G0/F=Wp O(-5),    F^+/G0=O(16).                     (6)

These are exact sheaf quotients, with no divisor correction.

Although (E^+)^- need not equal E, it always contains E. Thus the derivative of E^+, restricted to F^+, kills G0. By (5), its image is the image of the constant-space projection

    ((C0 O)/F^+)(-2) -> (H O/E^+)(-2).

The left source is the actual derivative quotient of F^+, and (6) shows that the image has generic rank at most one. Equivalently C0 O/(E^+ intersect C0 O) has generic rank at most one.

It cannot have rank zero. If C0 O were contained in E^+, its map to E^+/E=A_q(2) would have no component in the negative part L(2), by degrees. Its O(16) component is already onto on F^+ by (6), so it would be onto on C0 O. Its kernel would then be a rank14 degree-16 subbundle of E. But H0(E(1))=0 forces every degree of that kernel to be at most -2, hence its total degree at most -28, a contradiction.

Therefore the image has rank one. The kernel of the restricted derivative on F^+ has rank11 and contains the saturated G0 of rank11. Since F^+/G0 is a line bundle, the two kernels agree as sheaves. Using (5)-(6), and writing

    Nplus=E^+ intersect (C0 O),

we obtain

    0 -> F^+ -> Nplus -> Wp O(-3) -> 0,
    (C0 O)/Nplus=O(18).                                (7)

This is a sheaf-intersection assertion, not an assertion that full fiberwise intersections cannot jump. The induced O(18)->H O/E^+ is not assumed saturated.

## 5. Recover the backward intersection by its lower slope

Every ordinary degree of Nplus is at least -3. Indeed, twist the extension in (7) by three. Its subbundle F^+(3) is globally generated and has H1=0, and its quotient Wp O is globally generated; hence Nplus(3) is globally generated.

The negative summands L(2) of E^+/E have degrees at most -6. Thus every map Nplus->L(2) vanishes. Its image in E^+/E lies only in O(16), and is onto there because F^+ already maps onto it. Consequently, setting N=E intersect (C0 O),

    0 -> N -> Nplus -> O(16) -> 0,
    rank N=13,    deg N=-34.                            (8)

Since N lies in E and in the actual constant C0, its derivative lies in both E^+ and C0, hence in Nplus. Therefore N is contained in (Nplus)^-.

On the other hand, the derivative of Nplus into (C0 O/Nplus)(-2)=O(16) is onto: its restriction to F^+ is the onto quotient in (6), by (5). Thus (Nplus)^- also has rank13 and degree-34. The inclusion is an equality:

    N=(Nplus)^-.                                       (9)

This recovers precisely the needed backward intersection without asserting (E^+)^-=E.

## 6. The internal Euler extension and actual residual image

Equations (6)-(9) give

    0 -> Wp O(-5) -> N/F -> Wp O(-3) -> 0.               (10)

The map to the final quotient is onto because any derivative in O(16) can be canceled by a local section of F^+. Its kernel is G0/F.

The equivariant extension space in (10) is one-dimensional, namely (End(Wp) tensor H1(O(-2)))^G. The split extension is impossible: its Wp O(-3) summand would have zero map into E/F=T O(-3)+L, by irreducibility at the equal degree and ordinary degrees for L. It could not embed in E/F. The nonzero Euler extension therefore gives

    N/F=P O(-4),
    N=(P+D) O(-2)+P O(-4)

as equivariant bundles in the last equality. The latter splitting uses ordinary Ext vanishing, not horizontality.

The unique nonzero map P O(-4)->T O(-3) is the Wp-tensor of the standard quadratic Euler kernel, with quotient Wp O(-1). All its components into L are zero by degrees. Thus the actual locally free image sheaf of E in (H/C0) O is

    E/N=Wp O(-1)+L.                                    (11)

We do not assume saturation of this entire projected image.

## 7. The backward endpoint has two independent derivative contributions

Put K=E^-=ker(E->A_q). The displayed blocks of N have no maps to L, and F maps onto O(14), so N maps onto exactly O(14). The induced surjection E/N->L is zero on Wp O(-1) and is an isomorphism on L, since it is a surjective equal-rank equal-degree map. The kernel diagram therefore gives

    0 -> K intersect (C0 O) -> K -> Wp O(-1) -> 0.       (12)

The map of this actual projected image into (H/C0) O is represented by a nonzero constant intertwiner P=Wp tensor W->H/C0. Since P is irreducible, it is injective. Hence Wp O(-1) is the genuine tautological subbundle of a constant P space and has Gauss rank two. This proves saturation of the projected K, without asserting it for all of (11).

The quotient (7) is the composite

    C0 O -> V O(4) -> O(18).

The second arrow is onto, so its underlying degree-fourteen three-section system is basepoint-free. The composite is the product of that system with complete quartics. At any arbitrary point, a nonvanishing member of the first system is a unit on jet spaces, and its multiples by the complete quartic system generate jets through order four. Thus the composite system generates those jets everywhere.

Let J_i be the kernel of order-i principal-parts evaluation C0 O->P^i(O(18)). These are saturated for the needed i. Then J_0=Nplus, J_1=N, and J_i^-=J_(i+1). Differentiating jet constraints and using generation of the next jet gives the nonzero rank-one derivative of J_2 into (J_1/J_2)(-2). In particular

    rank J_2=12, deg J_2=-48,
    J_1/J_2=O(14),
    beta_(J_2) has rank one into O(12).                 (13)

Because C0 is constant and E intersect C0 O=N as sheaves, the kernel of the derivative of N modulo E equals its kernel modulo N. Hence

    K intersect (C0 O)=N^-=J_2.                         (14)

At the generic point the quotient H/K maps onto (H/C0)/Wp O(-1). The derivative of K followed by this quotient has rank two by (12). On its kernel J_2, equation (13) gives a nonzero rank-one derivative image inside C0, nonzero modulo K since N intersect K=J_2. This internal image lies in the kernel of the quotient and is independent of the projected image. Therefore

    generic rank beta_K >=2+1=3.                       (15)

All maps here are induced by the original constant connection and actual sheaf quotients. Generic-point rank additivity does not require saturation of the whole residual E/N or identification of jumping fiberwise intersections.

## 8. Maximal backward index one gives the contradiction

For maximal profile (1,1), K=E^- is the backward endpoint of the rank-three plateau and has Gauss rank strictly less than three. Otherwise the same plateau extends one step farther backward. Equation (15) is a contradiction.

The source reduction in Section2 was exhaustive, and the mismatched source was separately ruled out. Thus both full labels stated at the beginning are excluded.

## Verification boundary

The new endpoint-safe dependency is Sections4-5. The original quotient forces the forward intersection to have codimension one in C0; the alternative of containing all C0 violates the strict negative slope of E. A lower-slope bound on that intersection then recovers N=(Nplus)^- without treating the endpoint as an interior stage. This is why the previously reviewed backward rank contradiction applies here.

No global projection saturation is presumed, no connection is placed on an abstract complement, and no numerical splitting envelope is rerun. The other profile-(1,1) labels, source2, and the global research goal remain separate.
