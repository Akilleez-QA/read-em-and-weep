# A common coherent high image excludes the source127 a-c-c-f edge

## Result and scope

The entire original source

    G3.11.cce6e3ba4eeb, source_index127,
    (1,0,2,0,0,1,0,0),
    E=(V+D) O(-2)+Wp O(-3)+2V O(-4)+O(-8),
    A_q=O(-8)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(6), original defect zero

is impossible. This is a whole-source exclusion, not a whole-label exclusion or necessary-pair count. It says nothing about the separate a-b-c-f edge or c-d-f abstract family.

The new step couples the canonical top V block to the already forced full eight-dimensional span of the Wp cubic block. Either its kernel has a nonzero internal image, making the cubic coefficient span impossible, or two disjoint first spans have the same coherent high image. The latter gives a rank-seven pure degree-minus-two subbundle, incompatible with the actual top coefficient V+D.

No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, models, scans or large computation are used. Only fixed abstract characters and exact catalog identity are checked.

## 1. Immutable actual interface and the reviewed cubic reduction

The original actual-presentation note, strict-top theorem and two catalogs are pinned at db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep, under research/hm/order-four-quadratic-load. Their exact URLs and Git blob hashes are recorded in audit-inputs/manifest.json. They give saturated full-span E in H O, with

    H=2A+2V+2P+2D, rank E=17, degree E=-54,
    H0(E^-(2))=0,
    Q=H O/E,
    E^+/E=O(-6)+O(4)+L, L=O(18) saturated in Q. (1)

The last equality uses the original defect-zero convention. Work over C with binary icosahedral G. Here W is its defining two-space; A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W; Wp,V,P are the other irreducibles of dimensions2,3,4. All are self-dual. Nonempty invariant effective divisors have degree at least twelve, and there are no nontrivial line characters.

The sole newer dependency is PR901's exact proof at commit

    12d7fbb02ffbfd920bd5133c197ca9166cbabc5a,
    research/hm/profile11-source127-wp-scalar-reduction/PROOF.md,
    Git blob 8734e450297032410ac5625efeddd3cea34fd654.

https://github.com/Akilleez-QA/read-em-and-weep/blob/12d7fbb02ffbfd920bd5133c197ca9166cbabc5a/research/hm/profile11-source127-wp-scalar-reduction/PROOF.md

For this exact source its Sections2,3,6,7 prove the following actual, not merely generic, data. With R=Wp O(-3), its saturated raw first span is

    M_R=R^+=P O(-2),
    C_R=the constant coefficient span of R and M_R=V+D. (2)

Its image in Q is exactly a coherent line O(6) included in L by the nonzero invariant form f12 of degree twelve:

    M_R/(E intersect M_R)=O(6) --f12--> L.      (3)

In particular (3) is not saturated in L, and this proof does not replace it by L. The dependency retains the optional V internal component and proves the scalar internal component nonzero. No additional hypothesis on either row is imposed here. We need no claim concerning E^+ intersect C_R or the final cubic flag.

## 2. The top V block has an exact divisor-twelve high row

Put B=V O(-2), the canonical top V summand of E. Its external derivative toward O(-8) vanishes by degree; its row toward O(2) vanishes because V is absent from Sym4 W=D. Its high row is nonzero by strict-top: H0(B(2))=V injects into H0(A_q(2)), and no other external row can support it.

The V multiplicity is one in both Sym6 W=V+P and Sym18 W=A+V+2P+D. Multiplication by f12 therefore identifies these covariant spaces, so the exact high row factors as

    B=V O(-2) -> O(4) --f12--> O(16).          (4)

The first map is onto, because a common-zero divisor of a nonzero degree-six V covariant has degree at most six and is invariant. Hence its exact image is O(4), not the saturated O(16).

Its kernel is the universal bundle

    K_B=Wp O(-5).                              (5)

For a direct verification, the unique nonzero Wp O(-3)->V O has generic rank two: a rank-one coherent image O(e), e<=0, would require Wp in Sym^(e+3) W, absent in degrees at most three. Its determinant zero divisor is invariant of degree at most six, so the map is saturated, with quotient O(6). Dualizing and twisting by -2 gives (5) and the onto first map of (4), by the one-dimensional V degree-six Hom space.

## 3. The entire internal derivative has only two possibilities

The internal target of K_B is

    (E/B)(-2)=D O(-4)+Wp O(-5)+2V O(-6)+O(-10).

The only possible map is to the equal-degree original Wp(-5) row. The D(-4) channel vanishes because D W=S+T has no Wp, and the remaining targets are too low. Thus the complete internal image is

    J_B=0 or the entire original Wp O(-5).     (6)

Both alternatives are retained. Let I_B be the complete raw derivative image, and M_B the raw first span. Because the external image is the nonsaturated O(4), use exact image sequences only:

    0 -> J_B -> I_B -> O(4) ->0,
    0 -> B -> M_B -> I_B(2) ->0.               (7)

If J_B=0, then rank M_B=4 and degree M_B=0. It is a locally free subsheaf of a constant bundle, so all its splitting degrees are nonpositive and hence zero. Its inclusion is therefore an actual saturated constant four-space. Its character is

    chi_G(M_B)=chi_G(V(-2))+chi_G(O(6))
              =-V+(V+P)=P.

Thus this alternative is

    M_B=P O constant,
    M_B/B=O(6) --f12--> L.                    (8)

If J_B=Wp(-5), then rank M_B=6 and degree M_B=-6. The raw first polar of B is a quotient of V W O(-1)=T O(-1). The ranks and degrees agree, so it is exactly T O(-1). Its possible saturation defect in the ambient constant bundle is at most six, because its saturation has nonpositive degree. The invariant defect divisor must therefore be empty. Consequently

    M_B=T O(-1) is actually saturated.         (9)

The preimage of the internal derivative image in E/B is the actual original R, not an abstract isomorphic subbundle. Equations (7) therefore give

    (E intersect M_B)/B=R,
    R subset M_B.                             (10)

The constant coefficient span of M_B equals that of B: differentiation cannot enlarge the constant span, while M_B contains B. It is a quotient of

    V Sym2 W=P+D.

A saturated negative rank-six bundle cannot span only six constants. The only quotient of P+D with dimension greater than six is P+D itself. Thus (9) would give the exact constant span P+D. But (10) would then place the full V+D span of R from (2) inside P+D, impossible because V is absent. This excludes the nonzero internal-image alternative.

## 4. The zero internal image gives an impossible top coefficient

Only (8) remains. Its constant coefficient P is disjoint from C_R=V+D as a subrepresentation of H: their intersection is a common subrepresentation, and they have no common irreducible constituent. Therefore their actual sheaf sum is direct:

    S0=M_B+M_R=P O direct-sum P O(-2),
    rank S0=8, degree S0=-8.                  (11)

Both summands lie in E^+. Their images in Q are exactly the same coherent line O(6) inside L. This assertion is stronger than equality of the generic line: (3) and (8) are both onto O(6), followed by multiplication by f12. Since the invariant degree-twelve space is one-dimensional, their nonzero inclusions differ only by a nonzero constant scalar. They therefore have the identical image subsheaf of L, including the full divisor twelve. No saturation or division by f12 is performed.

Let N=E intersect S0. The actual image just identified gives an exact sequence

    0 -> N -> S0 -> O(6) ->0,
    rank N=7, degree N=-14.                   (12)

Every splitting degree of N is at most minus two, since it injects into E, whose largest splitting degree is minus two. Equality of degree in (12) forces every degree to be exactly minus two. Thus N=U O(-2) for a seven-dimensional genuine G representation U. Its injection into E induces an injection on top coefficient sections

    U=H0(N(2)) -> H0(E(2))=V+D.               (13)

The only possible dimensions of a subrepresentation of the multiplicity-free V+D are0,3,5,8. Seven is impossible. This contradicts (12), excluding the last alternative of (6).

## Conclusion

Both complete internal-image alternatives for the canonical top V block are impossible. Hence the whole displayed a-c-c-f source is excluded. The proof depends only on the exact reviewed cubic reduction (2)-(3), the forced top V covariant, and actual coherent image/intersection arguments. It does not need to assume or classify either low or high row of the top D block.
