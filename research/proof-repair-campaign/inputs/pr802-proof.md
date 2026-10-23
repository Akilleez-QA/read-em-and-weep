# A polar obstruction and constant projection exclude the two zero-defect O(16) labels

## Result and scope

The following full maximal profile-(1,1) labels are impossible:

    G3.11.16ee1aa30a9c:
      A_q=O(-10)+O(-8)+O(16), B_q=O(-18)+O(6)+O(8);
    G3.11.db4688c30472:
      A_q=W O(-9)+O(16),     B_q=O(-18)+W O(7).

Both original determinant defects are zero. The new structural steps are a three-channel quadratic polar obstruction and a constant-projection argument: the only surviving first osculation would be a genuine constant ten-space, after whose removal the entire negative top block would be horizontal. A negative horizontal subbundle of a constant bundle is impossible.

The argument excludes exactly these two labels and uses their complete necessary source overlists. It does not exclude any other label, does not exclude source2, and does not establish the original global rank goal. It does not assume H0(E^+)=0 or (E^+)^-=E. No selected actual HM/source coefficients, parameters, points, derivative values, matrices, source-instance ranks, selected-model experiments, scans, or large computation are used.

## 1. Immutable dependencies and the complete source lists

All original actual-bundle, source, quotient, and label data used here are at commit

    db51525015bb7c5e825833d550d08dedf6f6ea96

of Akilleez-QA/read-em-and-weep, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact files are:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md;
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md;
- ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md;
- one-one-endpoint-necessary-pairs.json;
- rank-three-quotient-frontier-144.json.

The stable labels have source_index46 and source_index51, respectively, in the one-one catalog. Their complete compatible source tuples are:

    index46:
      (0,0,0,0,0,2,0,1), (0,0,0,0,1,1,0,1),
      (0,0,1,0,0,1,0,1), (0,1,0,0,0,1,0,1);
    index51: all four above, together with
      (0,0,0,0,0,1,1,0), (0,0,0,0,1,0,1,0),
      (0,0,1,0,0,0,1,0), (0,1,0,0,0,0,1,0).

The catalog formula gives, in that order,

    E0 = (P+2D) O(-2)+2 O(-8)+O(-10),
    U6 = (2P+D) O(-2)+Wp O(-5)+O(-8)+O(-10),
    E3 = (V+P+D) O(-2)+V O(-4)+O(-8)+O(-10),
    E6 = (P+D) O(-2)+T O(-3)+O(-8)+O(-10),

and

    E10 = (P+2D) O(-2)+O(-8)+W O(-9),
    U13 = (2P+D) O(-2)+Wp O(-5)+W O(-9),
    E12 = (V+P+D) O(-2)+V O(-4)+W O(-9),
    E13 = (P+D) O(-2)+T O(-3)+W O(-9).

U6 and U13 are just names for the two displayed extra types, not additional catalog indices.

We use the profile-free quadratic Gauss-gap lemma and saturated derivative-image lemma from PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac, Sections 3 and 8:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

We also use the first-polar generation principle from PR799, commit 2172e4a7abbbe232f9f448bea6fa01dee7927460:

https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md

All three principles are restated below in the form needed here. The profile-(1,2) no-section and interior-stage arguments are not imported.

Work over C with G the binary icosahedral group, W its defining two-dimensional representation, Wp the other two-dimensional representation, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P the remaining even irreducibles of dimensions three and four. All irreducibles are self-dual. For an actual saturated subbundle M of a constant bundle, beta_M denotes its derivative into the quotient twisted by -2, M^- its kernel, and M^+ its saturated first forward transform.

The pinned actual source E is saturated in the constant thirty-space H O, has rank17 and degree-54, and satisfies

    H0(E(1))=0,    H0(E^-(2))=0.

Its actual Gauss quotient is A_q=E/E^-. Original defect zero identifies A_q with B_q^*(-2), a saturated subbundle of Q(-2), where Q=(H O)/E. Consequently the raw derivative image is already saturated, and

    E^+/E=A_q(2).                                      (1)

## 2. The top positive quotient is onto and has no divisor correction

For any source above, let F=R O(-2) be its canonical top block. It is saturated in E and hence in H O. The quotient map E->A_q restricts to

    p:F -> O(16),

because all components to the negative part of A_q vanish by degrees. The strict-top vanishing injects R=H0(E(2)) into H0(O(18)). Thus the section system of p has dim R independent members, with dim R at least nine.

Every nonempty G-invariant effective divisor on P1 has degree at least twelve. A common zero divisor would therefore leave at most h0(O(6))=7 independent sections of O(18), which is impossible. Thus p is onto everywhere. If K0=ker p, then

    0 -> K0(2) -> R O -> O(18) -> 0.                    (2)

The positive O(16) is saturated in Q(-2), by original defect zero. Let J be the image of the actual internal derivative

    kappa:K0 -> (E/F)(-2).

If J is saturated, the full derivative image I of F in (H O/F)(-2) is saturated and satisfies

    0 -> J -> I -> O(16) -> 0,
    0 -> F -> F^+ -> I(2) -> 0.                         (3)

Indeed the quotient by I is an extension of the locally free quotient of (E/F)(-2) by J and the locally free quotient of Q(-2) by O(16). This proves that (3) concerns the actual derivative and actual saturated forward bundle, not an abstract splitting or a generically equal line modified by torsion.

When J=0, F has Gauss rank one and F^+/F=O(18). The profile-free quadratic gap says that, for a saturated F=O(-2)^r with Gauss rank one and F^+/F=O(b),

    b=2r, or b<=r-1.                                   (4)

To recall why, quadratic values and first two derivatives span the full constant coefficient space, so F^{++} is that constant span. The derivative of F^+ kills F and factors through its line quotient. Hence the span has dimension r+1 or r+2. In the first case its degree zero gives b=2r; in the second its quotient by F^+ is O(2r-b), and the nonzero map O(b)->O(2r-b-2) gives b<=r-1. No maximal-profile assumption enters.

## 3. Complete small kernel support

The identities used below are

    Sym18 W=A+V+2P+D,
    Sym19 W=W+Wp+S+2T,
    P tensor W=Wp+T,
    D tensor W=S+T,
    V tensor W=T,
    A tensor W=W+S,
    Wp tensor W=P,
    Sym6 W=V+P,
    Sym7 W=Wp+T.

Equation (2) gives H0(K0(2))=0, so every degree of K0 is at most -3. For the three top coefficients 2P+D, V+P+D, and P+D, the relevant characters are respectively

    R              H1(K0(2))        chi(K0(3))
    2P+D           A+V              Wp+T-W
    V+P+D          A+P              T-W
    P+D            A+V+P            -W.                (5)

These follow directly from H1(K0(2))=Sym18 W-R and chi(K0(3))=R tensor W-Sym19 W.

Here is a complete support check, not an all-twist envelope. A block U O(-j), j>=4, contributes U tensor Sym(j-4) W to H1(K0(2)). This character must be a subcharacter of A+V+P, whose dimension is ten. Center parity forces U even for j even and odd for j odd. The complete allowable blocks are

    A O(-4), V O(-4), P O(-4), Wp O(-5),
    O(-6), O(-10),                                    (6)

with H1 contributions A,V,P,P,A,V+P, respectively.

For completeness, at j=4 the claim is immediate. At j=5, only Wp tensor W=P is allowed: the other odd representations either contain 1 or D after tensoring W, or exceed the dimension budget. At j=6, only the trivial coefficient survives; A tensor A contains 1 and D, while V tensor A=P+D. At j=7 only coefficients W,Wp fit the budget, and their products with S both contain D. At j=8 only the trivial coefficient fits, giving D, which is forbidden. At j=9 or j=11 or j=13 the smallest odd coefficient already exceeds the budget. At j=10 only the trivial coefficient fits, giving V+P. At j=12 only the trivial coefficient fits, giving P+D, which is forbidden. For j>=14 even the trivial coefficient exceeds the budget. Thus (6) is exhaustive. For smaller H1 budgets in (5), retain only the blocks whose H1 contributions fit that row.

The j=3 blocks contribute only their coefficient to chi(K0(3)). For j>=4 the contributions to this Euler character are respectively

    0,0,0,-Wp,-W,-T

for the six blocks in (6). Therefore matching both columns of (5), with nonnegative multiplicities of all j=3 blocks, gives exactly:

    R=2P+D:
      K0=(Wp+T) O(-3)+V O(-4)+O(-6);

    R=V+P+D:
      K0=T O(-3)+P O(-4)+O(-6),
      or K0=(Wp+T) O(-3)+Wp O(-5)+O(-6);

    R=P+D:
      K0=V O(-4)+P O(-4)+O(-6),
      or K0=Wp O(-3)+V O(-4)+Wp O(-5)+O(-6),
      or K0=T O(-3)+O(-6)+O(-10).                     (7)

To see the last matching explicitly, each of A and P must be supplied either by its degree-four block or by O(-6) and Wp O(-5), respectively; alternatively V+P is supplied jointly by O(-10). The choices with A O(-4) would require a negative W multiplicity among the degree-three coefficients and are impossible. The remaining three choices give precisely (7). The same check yields the first two rows. This is a complete classification of the indicated small exact kernel, not a claim that every listed kernel is realizable.

## 4. Reduce the complete source lists to the matching E6/E13 cases

For E0 and E10, (2) makes K0(2) a strictly negative rank13 bundle of degree-18. Each degree of K0 is therefore at least -8. The target (E/F)(-2) has all degrees at most -10, so kappa=0. Equation (4) contradicts r14,b18 because 13<18<28.

For U6 and U13, (7) has every degree at least -6. The target has largest degree -7, so again J=0. The gap contradicts r13,b18 because 12<18<26.

For E3 and E12, the two kernels in (7) have all degrees at least -6. The only possible internal degree exception is O(-6)->V O(-6), which is zero equivariantly by Hom_G(1,V)=0. Thus J=0, contrary to the gap for r12,b18 because 11<18<24.

This leaves E6 for the first label and E6,E13 for the second. For the second label E6 cannot surject onto W O(-9): only its O(-10) summand can map there, so the image has rank at most one. The only remaining matching cases are therefore

    G3.11.16ee1aa30a9c with E6 and L=O(-8)+O(-10),
    G3.11.db4688c30472 with E13 and L=W O(-9),          (8)

where in both cases

    E=(P+D) O(-2)+T O(-3)+L,
    A_q=O(16)+L.

For either case let F=(P+D) O(-2). The first two kernels in the last row of (7) give J=0: the only apparent extra degree channel O(-6)->T O(-5) is zero because Hom_G(1,T tensor W)=0, and Wp O(-5)->T O(-5) is zero by irreducibility.

In the third kernel, only O(-10) can have a nonzero internal derivative. Its possible components are the unique quintic channel to T O(-5) and, in the E6 case only, the scalar channel to the lower O(-10) in (E/F)(-2). Thus either J=0 or

    J=O(-10).                                         (9)

Every nonzero map here is saturated. If its T component is nonzero, it is the complete quintic tautological line O(-10)->Sym5 W O(-5), which is everywhere a line subbundle. If that component is zero, its scalar lower component is an isomorphism onto an O(-10) summand. A graph with both components is equally saturated. This proves the needed saturation in (3) in every case, without evaluating any actual coefficient.

## 5. First-polar generation and the nonzero internal channel

For an actual quadratic inclusion R O(-2)->H O, write its constant coefficient map as R tensor Sym2 W->H. At an arbitrary line l in W, the values and first derivatives are the image of R tensor lW. Euler's identity therefore identifies the raw first-osculation image with the image of

    R tensor W tensor O(-1) -> H O.                    (10)

When (3) says the raw image is saturated, (10) is onto F^+ everywhere. Thus F^+(1) is globally generated, while F^+ is a subbundle of a constant bundle. Its splitting degrees are only 0 and -1. This argument allows constant summands and does not invoke H0(E^+)=0.

Suppose now that (9) is nonzero. Equations (3) give rank F^+=11 and degree F^+=-8. In the representation ring they give

    chi(F^+)=-P-D-Sym6 W+Sym18 W=A,
    chi(F^+(1))=Sym19 W-Sym5 W=W+Wp+S+T.

Since A tensor W=W+S, the degree-zero and degree-minus-one parts are forced:

    F^+=A O+(Wp+T) O(-1).                              (11)

The constant A is canonical: it is the image of H0(F^+) in H. Call this actual constant three-space C. Constant projection to (H/C) O sends F^+/C to the saturated embedded bundle

    Rlin=(Wp+T) O(-1).                                 (12)

Saturation follows from H O/F^+ being locally free. Under this constant projection the derivative of the projected F lands in Rlin, since the derivative of F lands in F^+.

The equivariant projected map

    (P+D) O(-2) -> (Wp+T) O(-1)                        (13)

has exactly three one-dimensional channels:

    lambda:P O(-2)->Wp O(-1),
    mu:P O(-2)->T O(-1),
    nu:D O(-2)->T O(-1).

There is no D-to-Wp channel, since Wp tensor W=P. The other multiplicities are one, using T tensor W=V+P+D. The letters denote abstract scalar choices of the actual channels; no choice is evaluated.

The nu channel must be nonzero. Otherwise the whole rank-five D O(-2) would lie in the rank-three constant C. The lambda channel must also be nonzero. Otherwise the image of (13) would have rank at most six, so its kernel inside C would have rank at least three. It would have rank exactly three and equal C generically. Because F is saturated in H O, generic containment of C implies C O is contained in F as a sheaf, contrary to H0(F)=0.

Up to nonzero scalars the two nonzero channels lambda and nu are the standard Euler and multiplication maps, respectively:

    0 -> Wp O(-3) -> P O(-2) -> Wp O(-1) -> 0,
    0 -> D O(-2) -> T O(-1) -> O(4) -> 0.              (14)

In the first sequence P=Wp tensor W and the map is the Wp-tensor of the usual Euler map. In the second D=Sym4 W and T=Sym5 W, and the map multiplies by the tautological line. Thus the first is everywhere onto and the second is everywhere injective.

If mu=0, the projected F contains the whole Wp O(-1) summand of Rlin. The first forward span of any embedded pure degree-minus-one bundle is a nonzero constant space: its linear value and derivative columns span the full constant coefficient space. Its derivative must lie in Rlin because the derivative of the projected F does. This would put a nonzero constant subbundle in Rlin, contradicting H0(Rlin)=0.

Suppose instead that mu is nonzero. Compose its restriction to the first kernel in (14) with the second quotient:

    gamma:Wp O(-3) -> T O(-1) -> O(4).                 (15)

This composite is nonzero. If it were zero, the composite P O(-2)->O(4) would factor through Wp O(-1). But

    Hom_G(Wp O(-1),O(4))=Hom_G(Wp,Sym5 W)=0.

Thus the composite P O(-2)->O(4) would be zero, forcing mu to factor through D O(-2). That is impossible because Hom_G(P,D)=0.

The nonzero equivariant map (15) consists of two independent degree-seven sections, since Wp is irreducible. Their common zero divisor is invariant and has degree at most seven. The minimum nonempty invariant orbit has degree twelve, so there is no such divisor. Hence gamma is onto everywhere.

Now (13) is onto everywhere. Its Wp component is onto by lambda. After killing that component, the image of ker lambda together with the D source spans T O(-1): the latter gives the kernel of the second quotient in (14), and (15) surjects onto its quotient. Therefore the projected F equals Rlin as an image sheaf. Differentiation of projected F lands in Rlin, so Rlin is horizontal in the constant quotient (H/C) O.

A horizontal subbundle of a constant bundle over P1 in characteristic zero is constant: its associated Grassmannian map has zero differential and hence is constant. In particular its degree is zero. This contradicts deg Rlin=-8. Both cases for mu are impossible, and consequently the nonzero internal channel (9) is excluded.

## 6. The zero internal channel gives an actual constant ten-space

It remains that J=0. Equations (3) now give

    rank F^+=10,    deg F^+=0,
    F^+/F=O(18).

A saturated degree-zero subbundle of a constant bundle has every splitting degree zero and is itself an actual constant subspace. Write

    F^+=C0 O,
    C0=A+V+P,    dim C0=10.                            (16)

The character follows from chi(F^+)=-P-D+Sym18 W=A+V+P. This is a genuine constant subsystem of the given H, not an abstract direct summand selected by a bundle splitting.

Moreover C0 O is contained in E^+. Its map into E^+/E=A_q(2) is precisely the saturated positive O(18), and C0 O/F maps isomorphically onto that summand. These assertions follow from the actual derivative-image sequence (3) with J=0. Therefore

    E intersect (C0 O)=F,
    (E+C0 O)/E=O(18).                                  (17)

Since O(18) is saturated in E^+/E and E^+ is saturated in H O, the sum E+C0 O is saturated in H O. Consequently constant projection gives an actual saturated subbundle

    Z=(E+C0 O)/(C0 O)=E/F=T O(-3)+L

of (H/C0) O. Here the claimed projection saturation has been proved from (17); it is not inferred merely from local freeness of an image sheaf.

## 7. The projected top block would be horizontal

Because C0 is constant, the raw first derivative span of Z is exactly the projection of the raw first derivative span of E. The latter is E^+ by original defect zero. As C0 O lies in E^+, this projected bundle is saturated, and

    Z^+=E^+/(C0 O),
    Z^+/Z=E^+/(E+C0 O)=L(2).                           (18)

The derivative map to this quotient, twisted by -2, is exactly the original quotient E->A_q followed by A_q->L, factored through E/F. It is onto. Thus the actual Gauss quotient of Z is L, not merely a quotient or a torsion modification of L.

In the splitting Z=T O(-3)+L, every map T O(-3)->L vanishes by ordinary degrees. The induced map L->L is onto and therefore an isomorphism. It follows that

    Z^-=T O(-3).                                       (19)

By the kernel statement, the derivative of T O(-3) lands in Z. Its remaining internal component lands in

    (Z/T O(-3))(-2)=L(-2).

That component is zero by ordinary degrees: L has degrees -8,-10 or -9. Hence the derivative of T O(-3) lands in T O(-3) itself. This is a horizontal rank-six degree-minus-eighteen subbundle of the constant (H/C0) O, contradicting the degree-zero necessity for horizontal subbundles.

This excludes the zero internal channel as well. Together with Sections 3-5, every member of each complete source overlist is excluded. The two labels in the result are therefore impossible.

## 8. Contribution and boundaries

The new obstruction is structural. The nonzero internal channel produces a canonical constant A quotient and three multiplicity-one polar channels, whose exact Euler sequences force a forbidden horizontal negative bundle. The zero channel produces a genuine constant C0 of dimension ten; its saturated positive quotient allows exact constant projection, after which the full negative top block must be horizontal. Neither argument relies on the section-free interior-stage condition, a repeated numerical envelope, or any actual source-instance evaluation.

The proof claims only the two named exclusions. Source2 and every unnamed branch remain outside its scope. All source classifications above are necessary formal overlists, and no listed bundle is asserted to arise from actual HM data.
