# The actual rank-four diagonal plateau (2,2) is impossible

## 1. Statement and precise scope

Retain the actual geometric hypotheses, fixed physical representation marking, and original parameter line in the five complete immutable originals pinned in `INPUTS.json`. The actual second fundamental form cannot have generic rank four with ordered maximal consecutive rank-four plateau lengths `(k,l)=(2,2)`.

This is one ordered-profile exclusion. It does not exclude the other rank-four profiles, prove a generic rank-five bound, prove positive-square surjectivity or full-adjoint invertibility, or repair the original theorem. The argument does not use a source-Z assumption or the four-source theorem. It imports or reruns no historical candidate enumeration. It computes no actual HM coefficients, parameters, jets, matrices, or actual-instance ranks. Its finite calculation is only a new bounded necessary domain of abstract equivariant bundle splittings and torsion characters.

Nonzero derivative defects are retained throughout. The argument allows an outer defect of length twelve until the final step; the final contradiction also covers that case. No torsion term is silently removed.

## 2. Actual inputs and geometric assumption ledger

Work over C with G=SL2(F5) on T=P(W*), using the standard determinant-one linearization of O(1). Fix the physical irreducibles

    1, W, A=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W, P, W', V,
    dimensions 1,2,3,4,5,6,4,2,3.

The center-odd irreducibles are W,S4,T6,W'; the others are even. All are self-dual; A and V are distinct. G is perfect, so it has no nontrivial one-dimensional character.

The actual saturated bundle inclusion and its two Euler presentations are

    0 -> E -> H O -> Q -> 0,
    rank E=17, degree E=-54, dim H=30,
    rank Q*=13, degree Q*=-54,

    0 -> E  -> M3  O(-1) -> M4  O -> 0,
    0 -> Q* -> M3* O(-1) -> M2* O -> 0,

    M2=A+2V+3P+4D,
    M3=3W'+3S4+6T6,
    M4=2V+4P+3D,
    H=2A+2V+2P+2D.

The last identity is the actual Koszul middle-cohomology class H=W M3-M2-M4. It is not an identification of H with the coefficient space M3.

The retained geometric premises are local freeness and saturation, equivariance of the actual Gauss transforms and their regular derivative maps, the kernel/forward-transform properties stated below, absence of a nonzero constant subbundle in E and Q*, and full constant span of each. We also retain H0(E(1))=0 and the actual cohomology identity

    H1(E(1))=W'+3T6.                                      (1)

These premises are taken from the complete originals, not established by finite character arithmetic.

For any representation R define e(R,t)=R Sym^t W for t>=0, e(R,-1)=0, and e(R,t)=-R Sym^(-t-2) W for t<=-2. Then

    chi(E(t))=e(M3,t-1)-e(M4,t),
    chi(Q*(t))=e(M3,t-1)-e(M2,t),
    chi(Q(t))=e(H,t)-chi(E(t)).                            (2)

In particular

    chi(E(2))=-V,
    chi(Q*(1))=-W-2S4-3T6,
    chi(Q*(2))=-1-2A-D-V.                                (3)

The checker uses both actual presentations at every twist, and checks their Serre-duality consistency. All Euler characters in this proof are equivariant.

## 3. Plateau geometry and persistence

Suppose the excluded plateau exists. Write its actual saturated chain as

    F0 < F1 < F2 < F3 < F4,
    F2=E, ranks 9,13,17,21,25,
    Li=Fi/F(i-1), rank Li=4.

At every interior stage the derivative kernel is the preceding stage and the saturated forward transform is the next. The derivative therefore induces regular generically invertible maps

    Li -> L(i+1)(-2), i=1,2,3.                            (4)

Endpoint derivative ranks are strictly less than four, but are not assumed equal or assumed to be one.

Every Fi with i<4 has no nonzero constant subbundle. Below E this follows by inclusion; above E a constant subbundle propagates backwards through the derivative kernels. Every Fi with i>0 spans H: otherwise its proper constant span propagates forward to E. The reversed annihilator flag

    Di=F(4-i)^perp, D2=Q*, ranks 5,9,13,17,21,

has the same interior properties.

Universal section persistence gives, for d>=0 and i+d<4,

    H0(Fi(d))=H0(Di(d))=0.                              (5)

For the endpoint i=0, a nonzero section saturates to a negative line O(-s), with 1<=s<=d, also saturated in the constant ambient. Its successive derivatives reach its nonzero constant coefficient span after at most s steps: the derivative-to-coefficient change is triangular with nonzero factorial diagonal. The first inclusion of this line's forward transform in F1 follows from dF0 contained in F1 tensor Omega; later inclusions follow from the interior transform identities. If s<4 the resulting constant span would lie in an interior stage, contradiction. The same argument applies to D0. This is a universal argument, not evaluation of any actual section or jet.

Thus both endpoints have ordinary splitting degrees at most -4. Writing

    a=degree F0, b=degree F4=degree D0,

we have a<=-36 and b<=-20. All stage and quotient determinants have even degree, since the center acts trivially and G is perfect. Also

    H0(F1(2))=H0(D1(2))=H0(Q*(1))=0.                    (6)

## 4. Exactly nine endpoint/defect degree cases

Put ci=degree Li. Taking determinants of (4) gives

    c(i+1)=ci+8+delta_i, delta_i>=0.                     (7)

Each delta_i is the degree of an effective invariant divisor. The projective A5 action has orbit sizes 12,20,30,60, so below or equal to twenty its allowed nonzero values are twelve and twenty.

The central and total degree equations give the exact identity

    a+b=-76+delta1+2delta2+delta3.                       (8)

Set a=-36-2u and b=-20-2v, with u,v>=0. Then

    2u+2v+delta1+2delta2+delta3=20,
    c1=-13+u-delta1/2.                                 (9)

Hence delta2=0. At most one outer defect is nonzero. A length-twenty outer defect forces u=v=0, making c1 odd, impossible. With no defect, u is one of 1,3,5,7,9. With one length-twelve defect, u is 1 or 3. Put B=L2, so degree B=c2. The complete possibilities are:

| a | b | delta1 | delta3 | degree B |
|---:|---:|---:|---:|---:|
| -38 | -38 | 0 | 0 | -4 |
| -42 | -34 | 0 | 0 | -2 |
| -46 | -30 | 0 | 0 | 0 |
| -50 | -26 | 0 | 0 | 2 |
| -54 | -22 | 0 | 0 | 4 |
| -38 | -26 | 0 | 12 | -4 |
| -42 | -22 | 0 | 12 | -2 |
| -38 | -26 | 12 | 0 | 2 |
| -42 | -22 | 12 | 0 | 4 |

There is no source-Z conclusion from l=2.

## 5. The exact torsion-retaining sheaf identity

Since delta2=0, the middle derivative is an equivariant isomorphism L3=B(2). Define the actual torsion cokernels

    0 -> L1 -> B(-2) -> T1 -> 0,
    0 -> B(2) -> L4(-2) -> T3 -> 0.                     (10)

Their lengths are delta1 and delta3. Exact K-theory additivity gives

    [E]-[F0]=[B(-2)]+[B]-[T1],
    [Q]-[D0*]=[B(2)]+[B(4)]+[T3(2)].                  (11)

Shifting the second equation by -4 and subtracting gives

    [F0]-[D0*(-4)]=[E]-[Q(-4)]+[T1]+[T3(-2)].          (12)

This keeps both possible torsion terms with their correct signs and twists. It identifies associated-graded classes, not a horizontal or bundle splitting of the flag.

If a defect has length twelve, its determinant divisor is the reduced exceptional orbit Delta of twelve points. Equivariance makes each stalk length one. Thus the cokernel is an equivariant line sheaf on that orbit. A point stabilizer in G is cyclic of order ten; O(1) has a primitive stabilizer character. Its five center-even characters are represented by

    O_Delta(r), r=0,2,4,6,8 modulo 10.

Here r labels T1 when delta1=12, and labels T3(-2) when delta3=12. The invariant orbit equation of degree twelve gives

    tau_r(t)=chi(O_Delta(r+t))
            =chi(O(r+t))-chi(O(r+t-12)).               (13)

All five characters are retained, along with their twist action. Replacing them by twelve copies of the trivial representation would be wrong. The checker verifies dimension twelve, parity, ten-periodicity in r, and the Euler twist recurrence.

For each endpoint pair and r, (12) is tested at twists zero and one. The lower identity (11) is also tested there. These are necessary identities only, so no sufficiency or bundle realization is presumed. In fact the equivariant Euler recurrence chi(t+1)=W chi(t)-chi(t-1) propagates either identity to every twist; the retained cases are independently checked at twenty-five twists.

## 6. Four valid positivity constraints

The first two relevant actual quotient sequences are

    0 -> F1 -> E -> B -> 0,
    0 -> D1 -> Q* -> B*(-2) -> 0.                      (14)

Using (6), set

    Ppr=chi(B(2))-chi(E(2))=H1(F1(2)),
    Pdu=-chi(B(-2))-chi(Q*(2))=H1(D1(2)).              (15)

They satisfy the stronger inequalities, in the genuine-representation order,

    H1(B(1)) <= W'+3T6,
    H1(B)    <= Ppr,
    H0(B)    <= Pdu,
    H0(B(-1)) <= W+2S4+3T6.                          (16)

The first follows from the quotient E->B and H2(F1(1))=0. For the second, F1(2)->L1(2) and L1(2)->B induce successive surjections on H1, the latter by (10) and the vanishing of H1 of torsion. For the third, D1(2)->L4*(2) induces a surjection on H1, and dualizing (10) gives an inclusion L4*(2)->B*(-2) with torsion quotient. Its H1 map is surjective. Serre duality identifies H1(B*(-2)) with H0(B)*. For the last, (14) at twist one gives H1(Q*(1))->H1(B*(-1)) onto, and the latter is H0(B(-1))*; use (3) and (6).

These arguments keep all connecting maps and torsion. In particular we DO NOT assert H1(D0(1))>=H1(Q*(1)): that would require an unproved vanishing of the quotient's H1, and is not used anywhere in the certificate.

## 7. A complete finite domain and its checked reduction

Use equivariant Birkhoff splitting only for bundle cohomology and Hom spaces. It exists by splitting the slope filtration and averaging over the finite group; it is never assumed horizontal.

For a rank-r endpoint of total degree d, every ordinary degree e lies in

    d+4(r-1) <= e <= -4.                              (17)

An irreducible coefficient has dimension at most r and central parity e modulo two. This is a finite complete endpoint domain, not a historical list.

For B, every negative irreducible block R O(-j), j>=3, contributes R Sym^(j-3) W to H1(B(1)). The first inequality (16) gives (j-2)dim R<=20, hence j<=22. Checking the nine physically marked irreducibles of dimension at most four in that freshly derived interval leaves exactly

    W' O(-3), P O(-4), V O(-4), W' O(-5),
    O(-8), W O(-9), O(-10).

Thus every ordinary B degree is at least -10. Since rank B=4 and degree B=dB,

    -10 <= e <= dB+30.                                (18)

The calculation enumerates all parity-compatible irreducible blocks in (17)-(18), and all nonnegative combinations with the required rank and degree. An independent enumeration first partitions the ordinary degrees and then decomposes each equal-degree coefficient representation. The two domain enumerations agree exactly.

It then applies (12), the lower equation (11), and all four inequalities (16). The number of surviving endpoint/torsion/B tuples is shown below. These tuples are necessary formal data only.

| a | b | delta1 | delta3 | after exact identities and (16) | after horizontal test below |
|---:|---:|---:|---:|---:|---:|
| -38 | -38 | 0 | 0 | 6 | 0 |
| -42 | -34 | 0 | 0 | 8 | 0 |
| -46 | -30 | 0 | 0 | 24 | 0 |
| -50 | -26 | 0 | 0 | 17 | 0 |
| -54 | -22 | 0 | 0 | 216 | 132 |
| -38 | -26 | 0 | 12 | 6 | 0 |
| -42 | -22 | 0 | 12 | 12 | 0 |
| -38 | -26 | 12 | 0 | 0 | 0 |
| -42 | -22 | 12 | 0 | 70 | 40 |

The full explicit surviving and rejected tuples, with their character-theoretic witnesses, are recorded in `RESULT.json`. No actual quotient is asserted to realize any tuple.

## 8. A torsion-safe horizontal-subbundle obstruction

Let A be either endpoint and S an equivariant direct summand of its abstract bundle splitting. If the actual endpoint derivative vanishes on S, then the second fundamental form of S factors through (A/S)(-2). Hence if both

    Hom_G(S, outer derivative target)=0,
    Hom_G(S, (A/S)(-2))=0,                            (19)

then S has zero second fundamental form in the constant ambient. In characteristic zero its Grassmannian classifying map is constant, so degree S=0. Any negative-degree S satisfying (19) is therefore impossible.

This argument does not choose a horizontal splitting: it proves horizontality of S from vanishing of the two intrinsic maps. S is saturated in the constant ambient because it is a direct summand of the saturated endpoint.

Torsion-safe larger targets suffice:

    F0 -> L1(-2) embeds into B(-4),
    D0 -> L4*(-2) embeds into B*(-6).                 (20)

The first follows from (10), and the second by dualizing its other sequence. Thus the checker tests (19) using B(-4) or B*(-6), including the defect-twelve cases. It tests each irreducible endpoint summand S. Its exact Hom dimension is

    dim Hom_G(R O(e), R' O(f))
       = multiplicity of R in R' Sym^(f-e) W

for f>=e, and zero otherwise. All 187 rejected tuples have an explicit negative summand for which both Hom dimensions are zero.

The remaining 172 tuples all satisfy the following common restrictions:

    D0=W' O(-5)+V O(-4),                              (21)
    B=O(-8)+C,

where C is one of exactly

    O(2)+O(4)+O(6),
    O(2)+W O(5),
    W O(3)+O(6),
    A O(4).                                          (22)

There are 132 tuples with (a,b)=(-54,-22) and no defects, and 40 with (a,b)=(-42,-22), delta1=12. In particular delta3=0 in every surviving case. The remaining F0 splittings and torsion characters need not be individually selected for the final contradiction.

## 9. All remaining cases force an impossible rank-one endpoint

For every C in (22), all ordinary degrees of C*(-6) are at most -8. The actual reversed endpoint derivative is

    D0 -> L4*(-2)=B*(-6)=O(2)+C*(-6),                 (23)

because delta3=0. From (21), Hom(D0,C*(-6))=0 simply by degree. Therefore (23) lands in the scalar line O(2), and the generic second fundamental rank of D0 is at most one. It is not zero: a zero second fundamental form would make D0 a constant subbundle, contradicting degree D0=-22. Thus its actual generic rank is one. This is a theorem forced by the hypothetical data, not an instance-rank computation.

Let U be the smallest constant span of D0 in H*, with dimension n. The successive forward rank-one Gauss transforms of D0 reach U after n-5 steps. They are contained in D1,D2,D3,D4 in the first four steps. Reaching a constant bundle in fewer than four steps would put a nonzero constant subbundle in an interior Di, forbidden by Section 3. Consequently n>=9.

The complete rank-one flag theorem gives degree D0<=-5(n-5), hence

    22 >= 5(n-5).

Together with n>=9, this forces n=9. Here the rank-one theorem applies inside the actual invariant span U: D0 has no constant subbundle, spans U, and has generic derivative rank one. Its backward positive-rank stages have derivative rank at most one and cannot have rank zero because they lie in D0, which has no constant subbundle. Its forward proper stages have derivative rank at most one and cannot have rank zero before reaching the minimal constant span U. Thus every step has increment exactly one. The construction gives a complete saturated flag from zero to U; no decomposition into line curves is assumed.

For completeness, write r=5, s=n-r=4, D=-degree D0=22. If epsilon_j denotes the effective determinant defect between consecutive line quotients of that complete flag, degree elimination gives

    n(D-rs)
      = s sum_(j<r) j epsilon_j
        +r sum_(j>=r) (n-j) epsilon_j.               (24)

This is the rank-one identity proved in the directly pinned complete rank-one original and recalled in the ramification original; it also follows immediately by expressing consecutive line degrees as c(j+1)=cj+2+epsilon_j, imposing total degree zero, and summing the first r degrees.

Every epsilon_j is the degree of an invariant effective divisor. Hence each is zero or at least twelve. The right side of (24) is either zero or at least 12 min(r,s)=48. But the left side equals

    9(22-5*4)=18.

This contradiction eliminates all 172 remaining tuples, including every retained length-twelve lower defect. Together with Sections 4-8 it proves the ordered (2,2) exclusion.

## 10. Audit and reproduction

Run `python3 verify.py` and `python3 -O verify.py` from any working directory. They must reproduce `RESULT.json` byte for byte. The checker uses only the Python standard library, authenticates all five originals, derives the numerical cases and bounds, verifies the physical McKay arithmetic against exact conjugacy-class characters over Q(sqrt5), and compares two complete enumerations of every new splitting domain. It retains all five torsion characters. Its controls reject recorded numerical/character mutations but are not a proof-assistant verification of the geometric ledger.

The five originals are used for the actual presentations and marking, the regular saturated Gauss construction, section persistence, determinant parity, the invariant-orbit gap, and the complete rank-one degree/defect identity. Their historical classifications and rank-two conclusions are not used. Byte authentication does not discharge every transitive geometric premise; the theorem remains conditional on the explicit actual-geometric ledger in Section 2.
