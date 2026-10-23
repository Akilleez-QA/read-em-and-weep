# The bc source at index 113 is impossible

## Statement and scope

The entire original source edge

    G3.11.ad509d55173f, source_index 113,
    (0,1,1,0,0,0,0,1),
    E=(V+P) O(-2)+T O(-3)+V O(-4)+O(-10),
    A_q=O(-10)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(8),
    determinant defect zero

is impossible. Both common-divisor branches of the high quadratic subsystem are excluded. This is one whole source-edge exclusion, not an exclusion of the entire stable label or a global frontier count.

The proof uses no selected actual coefficients, parameters, points, derivative values, matrices, instance ranks, models, scans, or large computation. It uses universal representation and actual bundle/connection arguments. The bounded verifier checks only fixed abstract characters and exact original-catalog membership.

## 1. Immutable inputs and conventions

The original source list, decoder, actual-bundle presentation, quotient data and strict-top theorem are pinned at commit db51525015bb7c5e825833d550d08dedf6f6ea96:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact files are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, one-one-endpoint-necessary-pairs.json and rank-three-quotient-frontier-144.json. Their Git blob hashes are respectively b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3, d7506dae49b4be43230450c4132bd5db91f137ef, fe0afa410d89340d3082dc814277f89fbb582c19 and 8b5971092f9ef762584912609fd5e9301c4e271d.

The complete index-113 overlist consists of the ten tuples with a=d=g=0, h=1, b+c+e+f=2. The original decoder is

    E=((c+g+h-1)V+(d+e+g+h)P+(f+g)D) O(-2)
      +(a Wp+b T) O(-3)+(c V+d P) O(-4)
      +e Wp O(-5)+f O(-8)+g W O(-9)+h O(-10).

It gives the source displayed in the statement. In particular this proof concerns the bc tuple, not the different cf tuple treated by the following dependencies.

PR861, commit 7b5b3371a82cb92f46ea60895e45617d0891a5b0, supplies the universal exact-kernel classification for the rank-seven degree-eighteen line system and the degree-eight subsystem construction:

https://github.com/Akilleez-QA/read-em-and-weep/blob/7b5b3371a82cb92f46ea60895e45617d0891a5b0/research/hm/profile11-source113-cf-reduction/PROOF.md

PR868, commit fb398486839583f8fbd561d6dfaa6ab7b9d3ad67, supplies the double-divisor and dual-endpoint argument:

https://github.com/Akilleez-QA/read-em-and-weep/blob/fb398486839583f8fbd561d6dfaa6ab7b9d3ad67/research/hm/profile11-source113-cf-exclusion/PROOF.md

The necessary arguments and their changed source-dependent Hom tests are restated below. No whole-source conclusion is transferred merely from the common positive endpoint.

Work over C with the binary icosahedral group G and its irreducibles W,Wp,A,V,P,S,D,T. Here A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, dim V=3, dim P=4, and Sym6 W=V+P. All irreducibles are self-dual, G has no nontrivial one-dimensional characters, and every nonempty invariant effective divisor on P1 has degree at least 12; the divisor of degree 12 is the reduced exceptional orbit D12.

The actual E is a saturated subbundle of H O, dim H=30, has rank 17 and degree -54, spans H, and has all splitting degrees at most -2. The actual strict-top condition is H0(E^-(2))=0. Original defect zero makes

    E^+/E=A_q(2)=O(-8)+O(4)+O(18)                  (1)

a saturated subbundle of Q=H O/E. All derivatives below use the original constant connection, not an artificial connection on an equivariant splitting.

## 2. The basepoint-free branch has zero internal image and positive degree

Put F=(V+P) O(-2)=Sym6 W O(-2). It is a saturated direct summand of E. Its map to the negative quotient vanishes by degree; its map to O(2) vanishes because Sym4 W=D contains neither V nor P. Thus its external derivative lies only in O(16). Strict-top injects V+P into Sym18 W. The seven independent sections have a common invariant divisor of degree at most 12. Therefore its degree is either 0 or 12.

Suppose first that p:F->O(16) is onto. For K=ker p, strict-top and equivariant cohomology give

    rank K=6, deg K=-30,
    H0(K(2))=0,
    H1(K(2))=A+P+D,
    chi_G(K(3))=-W-S.                             (2)

The complete kernel classification of PR861 section 3 depends only on (2), not on the complementary source. Its four possibilities are

    P O(-4)+W O(-7),
    Wp O(-3)+Wp O(-5)+W O(-7),
    P O(-4)+O(-6)+O(-8),
    Wp O(-3)+Wp O(-5)+O(-6)+O(-8).                (3)

To recall exhaustiveness, the possible degree-at-most-minus-four atoms fitting the H1 budget in (2) are A(-4), P(-4), D(-4), Wp(-5), S(-5), O(-6), V(-6), W(-7), O(-8), Wp(-9), O(-12). Their H1 at twist 2 is respectively A,P,D,P,A+D,A,P+D,A+D,D,A+P+D,P+D. The negative W in chi at twist 3 forces O(-6) or W(-7), consuming the unique A. The latter leaves P(-4) or Wp(-5). The former additionally forces O(-8), then the same P alternatives. The degree-minus-three coefficients are forced by chi. This gives precisely (3).

For the present bc source the internal derivative target is

    (E/F)(-2)=T O(-5)+V O(-6)+O(-12).             (4)

Every equivariant map from any kernel in (3) to (4) vanishes. Besides degree and same-degree irreducibility, the only tests needed are

    T tensor A=Wp+S+2T,     V tensor W=T,
    Sym1 W=W, Sym2 W=A, Sym3 W=S.

In particular W(-7)->T(-5), W(-7)->V(-6), O(-6)->T(-5), O(-8)->T(-5), and O(-8)->V(-6) are all zero. The internal image is zero. Since the external O(16) is saturated in Q(-2), the full actual raw derivative image is itself saturated and isomorphic to O(16). Its inverse image M in H O consequently satisfies

    0 -> F -> M -> O(18) -> 0,
    deg M=-14+18=4.

A subbundle of a constant bundle has nonpositive degree. This contradiction excludes the complete basepoint-free branch.

## 3. The divisor-twelve branch produces an actual constant nine-space

Now suppose the common divisor is D12. Removing it gives the complete degree-six system Sym6 W, and the external derivative kernel is

    K=T O(-3).

Its internal target (4) has strictly lower degrees, so its internal derivative is zero. The full raw first-span sequence is

    0 -> F -> Mraw -> O(6) -> 0,
    rank Mraw=8, deg Mraw=-8.                    (5)

This sequence concerns the true external image O(4), embedded with divisor twelve in O(16); no saturation is silently substituted. If M is the saturation of Mraw in H O, its defect delta obeys 0<=delta<=8 by deg M<=0. A nonzero equivariant torsion defect has an invariant effective determinant divisor of degree at least 12. Thus delta=0 and M=Mraw is saturated.

First-polar generation makes the splitting degrees of M lie in {0,-1}. Its rank and degree make every degree -1; the character from (5) at twist 1 gives

    M=Sym7 W O(-1).

The derivative of M kills F, so its generic rank is at most one. It is nonzero because a negative saturated bundle cannot be horizontal. A linear bundle reaches its constant coefficient span after one derivative. Consequently the actual constant span C of M has dimension 9, with C O/M=O(8). This is the complete degree-eight evaluation sequence. Hence

    C=Sym8 W=P+D,
    M^-=F,
    C O/F=W O(7),
    M/F=O(6),
    C O/M=O(8).                                  (6)

These are actual subsystems of H O.

## 4. Both needed intersections are exact for the bc source

First C O is not contained in E^+. Otherwise C O/F=W O(7) would map to (1), with its two lower components zero by degree. Its nonzero map to O(18) is onto: the two degree-eleven sections cannot have a nonempty common invariant divisor. Its kernel is O(-4). Therefore

    (E intersect C O)/F=O(-4)

would inject into

    E/F=T O(-3)+V O(-4)+O(-10).                  (7)

But every equivariant Hom from O(-4) to (7) is zero: the first would require T in W, the second a V-invariant vector, and the last has the wrong degree. This is the source-dependent intersection test; it differs from the cf test but has the same vanishing conclusion.

Since M is saturated and lies in E^+, while C O has rank one more than M and is not contained in E^+, we have

    E^+ intersect C O=M.

For N=E intersect C O, derivatives lie both in E^+ and C O, hence in M. Also N lies in M. Therefore N lies in M^-=F, proving

    E intersect C O=F.                            (8)

No saturation of the residual projection (7) has been assumed.

## 5. Derivative compatibility and stabilizer characters force exact defect 2D12

Write B=C O/F=W O(7), L=O(18), Qplus=H O/E^+, and Z0=E/F. By (8) there is an injective sheaf map

    j:C O/M=O(8) -> Qplus.

The derivative of E^+ kills E, and its restriction to L is phi:L->Qplus(-2). The derivative of M induces the isomorphism M/F=O(6)->(C O/M)(-2). Since M/F maps to L by multiplication by f12, connection compatibility gives

    j(-2)=f12 phi                                (9)

up to a nonzero scalar. Hence j vanishes along D12.

Because L is saturated in Q, the map B->Q induces k:O(8)=B/(M/F)->Q/L. Its projection to Qplus is j. Thus at every point of D12 its fiber image lies in A_q(2)/L=O(-8)+O(4). For an arbitrary stabilizer over that orbit, its binary lift acts on the tautological line with an eigenvalue zeta of order 10. The fiber character of O(a) is zeta^(-a). The source O(8) has exponent 2 modulo 10, whereas the two lower rows have exponents 8 and 6. Equivariance forces k to vanish at every point of D12. Thus

    k factors as O(8) --f12--> O(20) -> Q/L.     (10)

This fiber-character argument does not presume a projection from Q onto its two lower Gauss rows.

Locally split L in Q and use a frame of B extending M/F. Its first column is divisible by f12 in L; by (10) its second column modulo L is also divisible by f12. Hence the determinant divisor of B in its saturation is at least 2D12.

The maps B->Q and Z0->(H/C) O have the same cokernel H O/(E+C O), so their saturation defect divisors agree. Write delta for the common length and Z for the saturation of Z0. Now the present bc source still has

    rank Z0=10, deg Z0=-40, dim(H/C)=21,
    rank Z=10, deg Z=-40+delta, delta>=24.       (11)

Since E spans H, Z spans H/C. As Z is a subbundle of a constant bundle, h0(Z*)=rank Z-deg Z=50-delta. Full span injects (H/C)* into H0(Z*), so delta<=29. The residual invariant divisor after subtracting 2D12 has degree at most 5 and must be empty. Therefore the defect is exactly 2D12, delta=24, and deg Z=-16.

Let U be the saturation of B in Q. Then deg U=14+24=38. It contains L, which remains saturated. Hence

    0 -> O(18) -> U -> O(20) ->0.                (12)

The equivariant extension space H1(O(-2)) is the one-dimensional trivial representation. Its two bundle types are U=O(18)+O(20) and U=W O(19). This is only an abstract splitting classification, never a horizontal splitting.

## 6. The original negative endpoint excludes both extension types

Let R=(Q/U)*. There is an exact sequence

    0 -> R -> Q* -> U* ->0,
    rank R=11, deg R=-16.                       (13)

The pinned actual bundle presentation is independent of the source tuple:

    0 -> Q* -> M3* O(-1) -> M2* O ->0,
    M3=3Wp+3S+6T,
    M2=A+2V+3P+4D.

Thus H0(Q*)=0, H1(Q*)=M2, and

    chi_G(Q*(3))=T-2W-S.

Every splitting degree of Q* and R is at most -1. We do not assume the stronger H0(Q*(1))=0. Both types in (12) have the same equivariant K-class, with

    H1(U*)=Sym16 W+Sym18 W=A+2V+3P+3D,
    chi_G(U*(3))=-Sym13 W-Sym15 W.

Consequently (13) gives

    H1(R)=D,
    chi_G(R(3))=-W+Wp+S+4T.                     (14)

For completeness the only degree-at-most-minus-two atoms supplying H1 budget D are D O(-2) and O(-6). Indeed U0 O(-j) contributes U0 Sym(j-2) W, and (j-1)dim U0<=5. At j=2 only D fits; at j=3 none of W W=1+A, Wp W=P, S W=A+D, T W=V+P+D fits; at j=4 the only eligible scalar gives A; at j=5 no odd coefficient fits; at j=6 the scalar gives D; all later atoms are too large. The remaining degree-minus-one terms contribute no H1. Thus

    R=L6 O(-1)+D O(-2),
    or R=L10 O(-1)+O(-6),                        (15)

for genuine odd coefficient representations of dimensions 6 and 10. In the first case, (14) and D W=S+T force L6 A=-W+Wp+3T, not a genuine character. In the second case they force L10 A=Wp+S+4T. The identities

    W A=W+S, Wp A=T,
    S A=W+S+T, T A=Wp+S+2T

then force L10=2Wp+T. Therefore

    R=(2Wp+T) O(-1)+O(-6).                       (16)

The universal strict-top theorem applied to actual Q* gives H0((Q*)^-(1))=0. Its original negative-endpoint quotient is exactly B_q=O(-18)+O(-4)+O(8), not a quotient transferred from any other label. Hence

    H0(R(1))=2Wp+T -> H0(Q*(1))
      -> H0(B_q(1))=Sym9 W=S+T                  (17)

is injective. The target has no Wp, contradicting (16). This excludes the divisor-twelve branch.

Sections 2 and 6 together exclude the entire original bc source tuple. The proof makes no whole-label claim; bf and bb, and any other source not separately excluded, are outside its conclusion.
