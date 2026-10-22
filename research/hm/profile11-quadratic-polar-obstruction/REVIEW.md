# Independent review of the quadratic polar obstruction

## Verdict and exact version

**PASS.** The frozen proof establishes the exclusion of the full formal profile-(1,1) label

    G3.11.003c6b04f1cc
    A_q = 2 O(-8) + O(14)
    B_q = O(-16) + 2 O(6)
    original determinant defect = 0.

The reviewed file is `PROOF.md`, with SHA256

    3a55f2c37548c7b05bf0f39f775ab37807c9f852d3601f77271fc0dd052022ed

This review is of that exact version. The proof was not edited. No mathematical gap was found in its new first-polar argument, its use of the actual connection, or its reduction from the complete necessary source overlist.

In particular, the proof does **not** assume that the endpoint E^+ is section-free. The constant three-space in F^+ is retained, and only its genuine constant ambient quotient is used in the decisive section-free argument.

## 1. Public dependencies and source-list audit

I read the following immutable public inputs at commit `db51525015bb7c5e825833d550d08dedf6f6ea96` of `Akilleez-QA/read-em-and-weep`, under `research/hm/order-four-quadratic-load/`:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`;
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`, Git blob `d7506dae49b4be43230450c4132bd5db91f137ef`;
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`, Git blob `dcacf0bcdef8377c1ed7654e5b82659ea409456e`;
- `one-one-endpoint-necessary-pairs.json`, Git blob `fe0afa410d89340d3082dc814277f89fbb582c19`;
- `rank-three-quotient-frontier-144.json`, Git blob `8b5971092f9ef762584912609fd5e9301c4e271d`.

The label record has profile `11`, source_index 49, the displayed A_q and B_q, and original_defect 0. The source_index 49 record has exactly the three compatible source tuples

    (0,0,0,0,0,2,0,1)
    (0,0,0,0,0,1,1,0)
    (1,0,1,0,0,2,0,0).

Substitution in the eight-block catalog and its top-block formula gives, respectively,

    E0  = (P+2D) O(-2) + 2 O(-8) + O(-10)
    E10 = (P+2D) O(-2) + O(-8) + W O(-9)
    E18 = 2D O(-2) + Wp O(-3) + V O(-4) + 2 O(-8).

This is the complete necessary source overlist for this label, not a choice of convenient sources. The overlist is used in the correct direction: any realization must have one of these sources. No realization of any catalog entry is assumed.

I also read `research/hm/profile12-quadratic-block-exclusion/PROOF.md` at commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`, Git blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`. Its Sections 3, 5, and 8 supply the saturated derivative-image lemma, the E18 kernel calculation, and the profile-free quadratic Gauss-gap lemma. Those statements were checked below without importing that publication's separate interior-stage condition H0(E^+)=0.

The profile-(1,2) result at commit `2bbf244bafc380cf5b0ce1114f86fcd8053e4e55` is contextual, not a premise of this exclusion. The broader frontier count and the global rank goal are not independently certified by this review.

## 2. The actual quotient, basepoint-freeness, and saturation

Let F=R O(-2) be the canonical top-slope block of one of the three sources. It is saturated in E, and consequently in the original constant bundle H O. The actual derivative quotient E -> A_q restricts to an actual map p:F -> O(14), since Hom(O(-2),O(-8))=0.

The strict-top lemma gives H0(E^-(2))=0. Applying H0 to the actual quotient sequence therefore makes R=H0(F(2)) inject into H0(O(16)). This justifies the asserted dimension 14 or 10 of the section system. It is not a claim of fiberwise injectivity of p.

The common-zero divisor of this equivariant system would be G-invariant. Every nonempty projective A5 orbit has size at least 12. A nonempty divisor would thus force all these independent degree-16 sections into a space of dimension at most 5. Both possible source dimensions exceed 5. Hence p is everywhere onto and

    0 -> K0(2) -> R O -> O(16) -> 0

is exact in vector bundles. Injectivity on H0 makes every splitting degree of K0(2) strictly negative.

The zero original determinant defect is used essentially and correctly. The actual rank-three injection A_q -> B_q^*(-2) is then an isomorphism. As B_q is a locally free quotient of Q*, its dual embeds as a subbundle of Q. Thus A_q is saturated in Q(-2), as is its top summand O(14). This does not presume a saturated image merely from equal generic ranks.

For the internal derivative, the map K0 -> (E/F)(-2) is O-linear: differentiating a scalar multiple adds a term in F, which vanishes in this quotient. If J is its image and I is the full derivative image of F in (H O/F)(-2), projection to Q(-2) gives

    0 -> J -> I -> O(14) -> 0.

When J is saturated, the ambient quotient by I is an extension of (E/F)(-2)/J and Q(-2)/O(14), both locally free. Thus I is saturated, and the actual forward transform satisfies

    0 -> F -> F^+ -> I(2) -> 0.

All maps here come from the same original constant connection. No connection on an abstract complement has been introduced.

## 3. Independent check of the preliminary exclusions

For a quadratic subbundle F=O(-2)^r with generic derivative rank one, let F^+/F=O(b). In a local coordinate, values and the first two derivatives of its arbitrary quadratic columns span their entire constant coefficient space. Therefore F^{++} is exactly that constant span. The derivative of F^+ vanishes on F and factors through the line O(b), so the constant span has dimension either r+1 or r+2.

If its dimension is r+1, saturation makes F^+ itself constant and gives b=2r. If its dimension is r+2, the quotient of the constant span by F^+ is O(2r-b). The next derivative is nonzero and induces

    O(b) -> O(2r-b-2).

Consequently b<=r-1. This verifies the profile-free gap statement. It uses no section-vanishing assertion for E^+.

For E0 and E10, K0(2) has thirteen strictly negative degrees summing to -16. Every such degree is between -4 and -1, so every degree of K0 lies between -6 and -3. The target (E/F)(-2) has all degrees at most -10. Hence J=0 by ordinary degree vanishing. The exact saturated derivative sequence gives b=16 and r=14, contradicting 13<16<28.

For E18, exact cohomology gives H1(K0(2))=V+P and chi_G(K0(3))=S-Wp. A block R' O(-j), j>=4, contributes R' Sym^(j-4)W to the first representation and has (j-3)dim R'<=7. Central parity and this bound leave exactly:

    V O(-4), P O(-4), Wp O(-5), O(-10).

Here is the completeness check. At j=4 only V and P are supported. At j=5 the dimension bound leaves W and Wp, and their products with W are 1+A and P, respectively. At j=6 only the trivial representation remains and contributes A. At j=7 no odd irreducible is small enough. At j=8 the trivial representation contributes D. At j=9 no odd irreducible fits. At j=10 the trivial representation contributes Sym6 W=V+P. No larger j can fit the budget.

The V+P budget has only the three assemblies stated in the proof. The assemblies V O(-4)+P O(-4) and O(-10) would give H0(K0(3)) equal to S-Wp and S+T-Wp, respectively, which are not genuine representations. The remaining assembly gives H0(K0(3))=S and hence

    K0 = S O(-3) + V O(-4) + Wp O(-5).

The only possible internal derivative component is the constant Wp O(-5) -> Wp O(-5) map. Schur's lemma makes its image zero or the full target top block; both are saturated. If it is zero, r=10 and b=16 contradict the same gap lemma. Otherwise

    0 -> Wp O(-3) -> F^+/F -> O(16) -> 0,
    rank F^+ = 13,
    deg F^+ = -10.

This leaves exactly the nonzero-channel branch treated by the new argument.

## 4. First-polar generation is valid for the embedded F^+

An actual quadratic inclusion F=R O(-2) -> H O has a coefficient map a:R tensor Sym2 W -> H. At an arbitrary line l in W, its fiber is a(R tensor l^2). Its values and first derivatives span a(R tensor lW). This is precisely the fiberwise description of the global first-polar map

    R tensor W tensor O(-1) -> H O.

There is no unproved saturation step here. Locally its image is generated by the original quadratic columns and their first derivatives. The derivative image I has already been proved saturated in Section 2. Thus those generators give the actual F^+ itself, rather than merely a subsheaf with the same generic fiber. The first-polar map is onto F^+ as a sheaf.

It follows that F^+(1) is globally generated, so all degrees of F^+ are at least -1. Since F^+ is a subbundle of a trivial bundle, all are at most 0. Therefore its splitting degrees are exactly of the allowed types 0 and -1. In particular H1(F^+)=H1(F^+(1))=0.

The extension in the preceding section yields

    chi_G(F^+) = -2D - Wp W + Sym16 W = V,
    chi_G(F^+(1)) = -Wp + Sym17 W = S+2T.

Thus C=H0(F^+) is the genuine representation V and has dimension three. Evaluation of these sections inside H O embeds C O as the corresponding actual constant subspace. This is the degree-zero part, not an arbitrary bundle summand chosen to be horizontal.

Writing U=F^+/(C O), all degrees of U are -1. Twisting and taking H0 shows its multiplicity representation is

    (S+2T) - V W = S+T,

so U=(S+T) O(-1). Both successive quotients are locally free, and

    ((H/C) O)/U = (H O)/F^+

is locally free. Consequently U is saturated in the genuine constant quotient (H/C) O and H0(U)=0. The quotient connection exists because C is constant. No horizontal splitting of F^+ or E is needed.

## 5. The two universal channels force the contradiction

Write F=D tensor M O(-2), with dim M=2. Since

    S W=A+D,
    T W=V+P+D,

each of Hom_G(D O(-2),S O(-1)) and Hom_G(D O(-2),T O(-1)) is one-dimensional. Therefore the actual projection F -> U has precisely the two channels

    phi_S tensor lambda,
    phi_T tensor mu,

with lambda,mu in M*. This describes the entire equivariant Hom space; it does not evaluate any selected actual map.

If lambda and mu were dependent, there would be a common nonzero multiplicity vector annihilated by both. Equivalently the projection would factor through at most one D O(-2), of rank five. Its kernel would have rank at least five. But F embeds into F^+, and the kernel of F -> F^+/(C O) embeds into the rank-three bundle C O. This is impossible. Independence is therefore forced by the actual embedding, not assumed as a generic property.

Choose a constant basis of M separating the two linear forms. The first copy of D O(-2) then maps by phi_S into U_S=S O(-1) and has zero U_T component. The S channel is everywhere onto: using D=Sym4 W and S=Sym3 W, contraction by the nonzero covector annihilating l gives Sym4 W -> Sym3 W at every arbitrary line l. In characteristic zero this contraction is surjective. This is a nonzero SL2-equivariant bundle morphism, so it spans the one-dimensional G-equivariant Hom space. No rank statement about the T channel is needed.

Hence the actual projected image of F contains the whole subbundle U_S. This inclusion is saturated because U_S is a direct summand of U and U is saturated in (H/C) O.

Every local section of U_S has a local lift to F through the onto S channel. Differentiating this lift gives a section of F^+ tensor Omega1. Projection by the constant C commutes with differentiation, so the derivative of U_S lies in U tensor Omega1. The saturated first forward transform U_S^+ in (H/C) O is consequently contained in U.

On the other hand, any actual linear inclusion U_S=S O(-1) -> (H/C) O reaches its constant coefficient span after one forward transform. For arbitrary local linear columns q_i(z)=v_i+z w_i, the span of q_i and q_i' is the span of v_i and w_i. The same statement is intrinsic at the other chart, and saturation extends it globally. The coefficient span is nonzero because U_S is a nonzero embedded bundle. Thus U contains a nonzero constant subbundle, contradicting H0(U)=0.

This verifies the decisive contradiction in the actual constant quotient, rather than in an abstract bundle quotient with an invented connection.

## 6. Verification boundary and conclusion

The representation identities were independently checked using only exact abstract binary-icosahedral character arithmetic:

    Sym6 W = V+P
    Sym16 W = V+P+2D
    Sym17 W = Wp+S+2T
    D W = S+T
    S W = A+D
    T W = V+P+D
    Wp W = P
    V W = T.

Only the self-contained character-definition prefix of an existing verifier was used, stopping before its pinned-input assertion and scan/main body. No catalog scan, selected actual coefficient, parameter, point, derivative evaluation, matrix, source-instance rank, selected-model experiment, or large computation was performed. The geometric claims were verified by the structural derivations above, not by numerical tests.

The exact source overlist is exhausted: E0 and E10 are excluded by the profile-free quadratic gap; E18's zero internal channel is excluded by that gap; and E18's nonzero channel is excluded by the first-polar and linear-osculation argument. The full displayed profile-(1,1) label is therefore excluded, not merely one internal-channel stratum.

This review does not exclude any other profile-(1,1) label, does not resolve the separate source2 profile-(2,1) branch, and does not establish the original global rank goal. It relies on the stated immutable actual-bundle and necessary-catalog inputs; it is an independent written mathematical audit, not proof-assistant certification. No external publication or repository change was made in this review.
