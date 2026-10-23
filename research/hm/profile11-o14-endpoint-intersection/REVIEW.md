# Independent exact-version review: endpoint-safe tensor-quartic intersection

## Verdict and version

**PASS for the stated two-label exclusion, conditional on the explicitly pinned actual-bundle and source-overlist inputs. No mathematical correction is required to the reviewed version.**

Reviewed file: `PROOF.md`.

Exact SHA256:

    f300e8ee2f36b85d1698b89f1150f20e6842bae925866c75506c340d78a4044d

This review covers the complete proof, particularly its new endpoint-safe Sections 4–5. It does not import the profile-(1,2) conclusions `H0(E^+)=0` or `(E^+)^-=E` into profile (1,1). Neither is needed.

The conclusion is exactly the exclusion of the full zero-original-defect maximal profile-(1,1) labels

    G3.11.18ad6075be86,
    G3.11.86279023dea2.

It does not exclude any other profile-(1,1) label, does not resolve the source2 profile-(2,1) branch, and does not establish the original global rank goal.

## 1. Public dependencies actually read

The following public files were fetched and read at their stated immutable commits, rather than treating earlier review verdicts or local filenames as evidence of their contents.

At commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, under [order-four-quadratic-load](https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load):

- [ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md).
- [NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md).
- [ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md).
- [one-one-endpoint-necessary-pairs.json](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json).
- [rank-three-quotient-frontier-144.json](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json).

The structural dependencies were also read directly:

- [PR796 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md), commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`. Its saturated derivative-image lemma, small kernel classifications, and independent Section 8 quadratic Gauss-gap lemma are applicable. Its interior-stage no-section argument is not used here.
- [PR797 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/cdee9396133fb96d4a91babba87b1a7a35903635/research/hm/profile12-tensor-quartic-block/PROOF.md), commit `cdee9396133fb96d4a91babba87b1a7a35903635`. The small kernel support, rank-three quotient classification, linear constant-span argument, and Euler extension were checked. Its Section 6 interior-stage recovery of the intersections is not imported.
- [PR798 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/2bbf244bafc380cf5b0ce1114f86fcd8053e4e55/research/hm/profile12-backward-plateau-exclusion/PROOF.md), commit `2bbf244bafc380cf5b0ce1114f86fcd8053e4e55`. Its projected tautological image and internal jet-derivative argument were checked against the actual maps reconstructed in the present proof.

The older necessary-pair enumeration is an explicit dependency, not a newly rerun enumeration. Reading its necessity argument and the exact complete records is sufficient for the present exhaustive source reduction; no claim is made that this review independently reruns the full 159-pair classification or reproves the original geometric presentations.

## 2. Verified hypotheses and exact source coverage

The actual setup is over C, on P1, with the stated binary-icosahedral linearizations and center-even constant ambient representation. The pinned actual-bundle input supplies rank E=17, degree E=-54, saturation in the constant thirty-space, and H0(E(1))=0. The strict-top lemma supplies H0(E^-(2))=0 independently of forward plateau length. All derivatives in the proof are induced by the original constant connection.

Both catalog records have a=-4, b=-2, and original defect zero. Consequently the original equal-rank transpose injection identifies A_q with B_q^*(-2), and its injection into Q(-2) is saturated. In particular its O(14) summand is saturated. This implication uses the genuine quotient B_q of Q*, not just equality of numerical degrees for an arbitrary map.

The stable frontier records identify:

    G3.11.18ad6075be86: source_index=4,
      A_q=O(-10)+O(-8)+O(14),
      B_q=O(-16)+O(6)+O(8).

    G3.11.86279023dea2: source_index=6,
      A_q=W O(-9)+O(14),
      B_q=O(-16)+W O(7).

The complete source_index=4 record contains exactly

    (0,0,0,0,0,2,0,1), (0,0,0,0,1,1,0,1),
    (0,0,1,0,0,1,0,1), (0,1,0,0,0,1,0,1).

The source_index=6 record contains exactly those four and

    (0,0,0,0,0,1,1,0), (0,0,0,0,1,0,1,0),
    (0,0,1,0,0,0,1,0), (0,1,0,0,0,0,1,0).

Substitution into the published eight-multiplicity formula gives precisely E0,U6,E3,E6 and E10,U13,E12,E13 as displayed in the reviewed proof. In particular the extra U6 and U13 types have not been silently omitted. These lists are complete necessary overlists, not realization assertions.

## 3. Source elimination and the profile-free gap

The injection H0(E(2)) -> H0(A_q(2)) is valid because its kernel is H0(E^-(2)). The exact universal decomposition Sym16 W=V+P+2D excludes both U types: 2P+D cannot inject into a target with only one P.

For every remaining type, at least nine independent sections of O(16) represent the top quotient. Any common zero divisor is invariant. A nonempty invariant divisor has degree at least twelve, leaving at most five sections of the residual degree-four line. This proves everywhere-surjectivity, not merely nonzero generic rank.

For E0/E10, rank K0=13 and degree K0(2)=-16 with all its degrees strictly negative give the interval [-6,-3] for K0. All internal targets have degree at most -10, so the internal derivative vanishes. For E3/E12, the two displayed kernel types are exhaustive by their D cohomology budget. Their only degree-compatible exceptional component would be O(-8) -> V O(-6), and it vanishes because V is absent from Sym2 W.

The derivative-image lemma then gives F^+/F=O(16), with no torsion correction. Its saturation proof is valid: the quotient of the full ambient derivative target by the image is an extension of the locally free quotients on the internal and external sides.

The independent quadratic Gauss-gap lemma needs only an actual quadratic inclusion in a constant bundle, a rank-one derivative, and its saturated line quotient. The values and first two derivatives reach the actual constant coefficient span. Its possible dimensions are r+1 or r+2; respectively, the degree argument gives b=2r or b<=r-1. Thus b=16 is impossible for r=14 and r=12. No hypothesis on H0(E^+) occurs here.

After this reduction, the mismatched E6 source for the second label is also impossible: only its O(-10) line could contribute to W O(-9), so an onto rank-two quotient cannot result. The two matching source/label pairs are therefore exhaustive.

## 4. Quadratic kernel and first-polar replacement

For F=(P+D) O(-2), the kernel has rank eight, H1(K0(2))=V+D, and chi(K0(3))=0. The small support classification in PR797 has exactly the three kernel types stated in the reviewed proof. The first two have zero internal derivative, including the potential O(-8) -> T O(-5) component because T is absent from Sym3 W.

The remaining channel Wp O(-7) -> T O(-5) has multiplicity one and, when nonzero, is the tensor of the complete quadratic line inclusion. It is everywhere injective with locally free cokernel. The zero case is excluded by the same profile-free gap with r=9,b=16. Hence the actual derivative image is saturated, and rank F^+=12, degree F^+=-12.

The replacement for the old no-section argument is correct. For a quadratic coefficient map R tensor Sym2 W -> H, the first-polar map R tensor W tensor O(-1) -> H O has fiber image equal to the values and first derivatives of R O(-2). Euler polarization includes the values themselves. Because the raw derivative image has already been proved saturated, this first-polar image is exactly F^+, not merely a proper sheaf with the same generic span.

It follows that F^+(1) is globally generated. Since F^+ is a subbundle of a constant bundle, its ordinary degrees are at most zero, while global generation after twisting makes them at least -1. Rank twelve and degree -12 force all twelve degrees to be -1. Its character is Wp+S+T. This establishes the needed pure linear bundle without any assertion about H0(E^+).

## 5. Genuine tensor-quartic constant subsystem

The actual quotient X=F^+/F has rank three, degree six, minimum degree at least -1, H0(X)=P+D, and chi(X(-1))=T. The complete rank-three parity/character classification leaves V O(2) or Wp O(-1)+O(8). In the latter case the O(8) component cannot map to O(16), since Sym8 W has no invariant, and cannot lie in the negative kernel. Therefore X=V O(2).

For the constant span C0 of the linear F^+, the quotient C is globally generated and has no degree-zero summand: such a summand would give a constant functional annihilating the full span. Its degree is twelve. The derivative factors through X, bounding its rank by three. Rank one is excluded by the absence of V in Sym8 W. In rank two, parity leaves only positive even lines summing to twelve, of which at most the degree-ten line can receive a nonzero derivative component. The derivative would then have rank at most one. Thus rank C=3.

The generically full-rank map V O(2) -> C(-2) has equal degrees and is an isomorphism. The quotient is consequently the complete evaluation sequence of V O(4), not an arbitrary sequence with the same Euler character. This identifies an actual invariant fifteen-space and the actual osculating subbundles:

    C0=V tensor Sym4 W,
    F=V tensor U_2^4,
    F^+=V tensor U_3^4.

The derivative F^+/F -> ((C0 O)/F^+)(-2) is an isomorphism. This exact map is what the endpoint argument uses.

## 6. New forward-intersection recovery

The original saturated quotient gives G0=E intersect F^+, with G0/F=Wp O(-5) and F^+/G0=O(16). In particular G0 has rank eleven and is saturated in F^+.

The universally valid inclusion E subset (E^+)^- implies that the derivative of E^+ kills G0. Transport through the preceding derivative isomorphism shows that the projection of C0 into H O/E^+ has generic rank at most one. This uses only containment of the kernel, not equality with E.

Rank zero would imply C0 O subset E^+, since the projection has torsion-free target. Its map to E^+/E=A_q(2) has no component in the negative summands. It is onto O(16), already on F^+. Its kernel would have rank fourteen and degree -16 and inject into E. H0(E(1))=0 then forces every kernel degree to be at most -2, giving total degree at most -28, a contradiction. Thus the projection has rank exactly one.

The derivative kernel on F^+ therefore has rank eleven and contains G0. Their quotient, if nonzero, would be torsion inside the line bundle F^+/G0. It must vanish. Transporting this equality through the actual derivative isomorphism gives the exact sheaf quotients

    Nplus/F^+=Wp O(-3),
    (C0 O)/Nplus=O(18),
    Nplus=E^+ intersect (C0 O).

This step is valid at a forward endpoint. It proves saturation of Nplus inside C0 O, but does not prove saturation of the induced injection O(18) -> H O/E^+. The reviewed proof makes that distinction explicitly.

## 7. New backward-intersection recovery

Twisting the extension for Nplus by three gives a globally generated subbundle F^+(3) with H1=0 and a globally generated quotient Wp O. Lifting the quotient sections proves that Nplus(3) is globally generated. Therefore its minimum splitting degree is at least -3.

Every negative summand of A_q(2) has degree at most -6. All components from Nplus to that negative part vanish. The remaining map to O(16) is onto because its restriction to F^+ is onto. Its kernel is precisely N=E intersect (C0 O), hence

    rank N=13, degree N=-34.

Differentiation of N stays in C0 because C0 is constant, and in E^+ because N lies in E. Thus N is contained in (Nplus)^-. The derivative Nplus -> ((C0 O)/Nplus)(-2)=O(16) is onto, already on F^+. Its kernel has the same rank and degree as N. The inclusion is therefore equality as sheaves:

    N=(Nplus)^-.

No global equality (E^+)^-=E is asserted or needed. This verifies the essential new dependency.

## 8. Euler extension and the residual image

The map N -> Nplus/F^+ is onto by locally canceling any derivative with a section of F^+. Modulo F, it gives the exact extension of Wp O(-3) by Wp O(-5). The equivariant extension space is one-dimensional. A split Wp O(-3) summand would have zero map to E/F=T O(-3)+L, by irreducibility and degrees, contradicting the actual inclusion. Thus the extension is the nonzero Euler extension, giving N/F=P O(-4).

The extension of this quotient by F splits as bundles by ordinary Ext vanishing. This splitting is not declared horizontal. The unique nonzero component P O(-4) -> T O(-3) is the saturated tensor-quadratic Euler inclusion with quotient Wp O(-1); all components to L vanish. Consequently E/N has the displayed bundle type Wp O(-1)+L and is the actual locally free projected image sheaf.

Local freeness of that image alone does not imply a locally free ambient cokernel. The proof correctly leaves saturation of all E/N in (H/C0) O open.

## 9. Projected backward kernel and saturation actually proved

Since N maps onto precisely O(14) in A_q, the induced E/N -> L is onto. It vanishes on Wp O(-1), and its L component is an isomorphism by equal rank, equal degree, and surjectivity. The kernel diagram therefore identifies the actual projection of K=E^- as Wp O(-1).

Its map into (H/C0) O is determined by a nonzero constant intertwiner Wp tensor W=P -> H/C0. Irreducibility of P makes this constant map injective. Hence the projected K is a genuine saturated tautological subbundle of a constant P space, with Gauss rank two.

This supplies the specific saturation used later. It does not retroactively establish saturation of the full residual E/N or of a larger sum with C0.

## 10. Jet derivative and independent internal rank

The quotient C0 O -> O(18) factors through the complete evaluation quotient V O(4), followed by an everywhere-surjective degree-fourteen three-section system. At any arbitrary point, one member of the latter is a unit in a local trivialization. Multiplication by that unit is invertible on every finite jet space. Its products with complete quartics generate jets through order four. This is a universal arbitrary-point argument, not an instance evaluation.

Thus the principal-parts kernels J_i are saturated through the needed orders. The first two are J0=Nplus and J1=N. Differentiating the constraints through order i shows J_i^-=J_(i+1), and generation of the next jet makes the derivative onto (J_(i-1)/J_i)(-2). In particular J2 has rank twelve, degree -48, and a nonzero rank-one derivative into O(12), with J1/J2=O(14).

Because C0 is constant and E intersect C0 O=N as sheaves, vanishing of the derivative of N modulo E is equivalent to vanishing modulo N. Therefore K intersect C0 O=N^-=J2. The internal derivative is nonzero modulo K because N intersect K=J2.

At the generic point, H/K maps onto (H/C0)/Wp O(-1). The projected derivative of K has rank two. The nonzero derivative contribution from J2 lies in the kernel of that target projection, so it is independent of the projected contribution. Rank additivity gives rank beta_K at least three. This generic-point argument requires neither global saturation of E/N nor equality with jumping full fiberwise intersections.

## 11. Endpoint contradiction, checks, and limits

The pinned maximal-profile convention says that backward index one makes K=E^- an endpoint with Gauss rank strictly smaller than three. The established lower bound contradicts that condition, excluding both remaining matching pairs. Together with the complete source reduction, this is a full exclusion of both stated labels, not just of a preferred source stratum.

For independent arithmetic checking, only the abstract character arithmetic prefix was used, stopping before the original verifier's `assert PINNED and` continuation. Explicit checks included Sym6 W=V+P, Sym8 W=P+D, Sym16 W=V+P+2D, Sym17 W=Wp+S+2T, Wp tensor W=P, Wp tensor A=T, Wp tensor S=V+D, and the two multiplicity-one Hom spaces used for the saturated internal maps. No scan or verifier main was run.

No actual HM/source coefficients, parameters, selected points, derivatives, instance matrices, source-instance ranks, model experiments, or large computation were used. The proof was not modified. This is an independent written mathematical audit, not proof-assistant certification.

The essential new result is that the endpoint projection has rank exactly one by a negative-degree obstruction, and its recovered intersection has sufficient lower slope to reconstruct the backward kernel. That closes the missing profile-(1,1) dependency for these two labels while preserving all stated unresolved branches and saturation boundaries.
