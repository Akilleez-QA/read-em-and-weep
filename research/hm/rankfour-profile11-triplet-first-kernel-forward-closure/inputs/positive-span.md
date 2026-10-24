# Full positive triplet image forces two spanning scalar curves

## 1. Statement and exact boundary

Work over C on the physical binary-icosahedral line P(W*), with G=SL2(F5), its fixed determinant convention, and the original saturated inclusion E in H tensor O, dim H=30. Retain rank E=17, deg E=-54, its full constant span H, and the original actual rank-four maximal ordered plateau (1,1). Assume

    A_q=E/E^-=A(4)+O(-8),   A=Sym2 W,
    im beta_K=A(2),         K=E^-.

The last equality is an equality of actual coherent images, not just generic rank or saturation. PR1198 forces it for K1,K2; PR1199 permits it for K3,K4,K5 as well. This theorem treats precisely this full-positive-image branch, not their other image alternatives.

Use the physical representations W,W',A,V,S4,D,P,T6, where A=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W. The actual section gates and source-D restriction of PR1194 are retained before the present analysis. Thus

    E=D(-2)+(W'+T6)(-3)+V(-4)+O(-8),
    E0=D(-2)+(W'+T6)(-3)+V(-4),
    K^+=E0,  E0^-=K,  E0/K=A(4),
    rank E0=16, deg E0=-46, rank beta_E0=3.

The proof of these actual subbundle equalities in PR1198 Section 5 applies whenever its full-image hypothesis holds: the negative quotient projection comes only from the source octic, and the full image identifies the forward transform. No theorem with central rank seventeen is transferred to E0.

Let C be the minimal constant span of E0. Then:

1. dim C=21, and the actual octic source has a complete nine-dimensional constant span J with H=C direct-sum J.
2. In the genuine constant ambient C, put S0=(C O/E0)*, L0=S0^-, B0=S0/L0. Then

       B0=A(-6),  L0=O(-10)+O(-18).

   The first equality identifies the actual transpose with an everywhere isomorphism. The original defect remains t=0.
3. The actual derivative of L0 has rank two everywhere. It gives

       0 -> L0 -> A(-8) -> O(4) -> 0.

   Its actual saturated first forward transform M=L0^+ in C* O is

       M=W(-9)+W(-17),    S0/M=O(6).

4. The actual coefficient map of the two scalar curves is surjective:

       Sym10 W direct-sum Sym18 W ->> C*.

   Here C*=2A+2V+P+D and the coefficient kernel is equivariantly isomorphic to P+D. In particular both scalar curves retain their A and V coefficient components, and those two A components (respectively V components) are independent in C*. The degree-ten curve has constant span either A+V or A+V+D. The degree-eighteen curve has span either A+V+P or A+V+P+D. At least one retains D. If both retain D their spans intersect in exactly that constant D; otherwise their spans are disjoint.

These are new necessary actual-map and coefficient-span constraints. No whole triplet quotient, K splitting, maximal profile or coarse bin is excluded or realized. In particular neither scalar curve is assumed to have a complete coefficient system; the degree-eighteen one necessarily loses one of its two P copies.

## 2. Complete immutable inputs

INPUTS.json records complete freshly fetched source files and their exact commit, path, Git blob SHA1, byte length and SHA256. Inputs are PR1196 (zero original defect), PR1198 (five kernels and full image), PR1199 (other image alternatives and the universal principal-parts identity), PR1197 (the distinct decomposable argument, used only as methodological context), PR1194 (actual top-four gates/source), PR1185 (actual coherent Gauss filtration before its low-top assumption), and ACTUAL (original presentations and physical representations).

Their transitive actual-geometric premises remain assumptions. The present proof supplies the triplet argument independently; it does not apply PR1197's decomposable conclusion to a different quotient. No actual parameter, coefficient, point, jet, tensor, matrix or instance rank is selected or evaluated. Universal jets below mean sheaf constructions for every coefficient system, not selected actual jet data.

## 3. A minimal-span bound and an actual constant complement

Write m=dim C. Since E spans H and E/E0=O(-8), the actual coefficient map induces a surjection

    Sym8 W=P+D ->> H/C.

Thus m>=21. The derivative of E0 has the same rank three in C O as in H O: C is constant and C O/E0 embeds in H O/E0. Define S0,L0,B0 as above. Then

    rank S0=m-16, deg S0=-46,
    rank B0=3, rank L0=m-19,
    B0 -> A(-6)

is the actual full-rank coherent transpose injection. Hence deg B0<=-18 and deg L0>=-28. Minimality of C gives H0(S0)=0, so S0 and all its saturated derivative kernels have top degree at most -1.

Apply the actual coherent kernel filtration in this constant ambient. If n=rank L0>=4, its graded ranks q1,q2,... are nonincreasing, at most three, sum to n, and their coherent images inject into B0(-2j), hence A(-6-2j). The negative-horizontal argument makes the filtration terminate. Consequently

    deg L0 <= -8q1-10(n-q1)
            = -10n+2q1 <= -10n+6 <= -34,

contradicting deg L0>=-28. Therefore m<=22. The quotient H/C has dimension eight or nine, and is a quotient of the inequivalent irreducibles P+D of dimensions four and five. Semisimplicity forces dimension nine. Thus m=21.

Choose the actual equivariant source splitting E=E0+O(-8); it exists since the negative quotient row is the nonzero scalar on the octic and zero on all other source rows. Its octic coefficient map tau:Sym8 W->H becomes an isomorphism after projection to H/C. Thus tau is injective, J=im tau is a constant nine-space, J intersect C=0, and H=C direct-sum J. This derives a connection-preserved splitting of the constant ambient; it never declares an ordinary source splitting horizontal in advance.

The octic inclusion in J O is the complete Veronese line. Its annihilator is Sym7 W(-1), and its actual derivative quotient is O(6), everywhere, with kernel Sym6 W(-2). Uniform first-jet separation follows from H1(O(6))=0 on every length-two neighborhood. This is a universal full-Veronese statement after completeness has been proved for this octic alone.

It follows in the actual constant dual splitting that

    S=S0+Sym7 W(-1),
    B=B0+O(6).

PR1196 gives the original actual B=A(-6)+O(6), with original determinant defect zero. More intrinsically, the actual transpose is block diagonal in the derived constant decomposition, and the octic block has defect zero. Thus the defect of B0->A(-6) is exactly the original t=0. Its torsion cokernel vanishes, proving B0=A(-6). In particular rank S0=5 and rank L0=2, deg L0=-46-(-18)=-28.

## 4. The two scalar endpoint curves are forced

The octic annihilator Sym7 W(-1) is acyclic, so ACTUAL gives

    H1(S0)=M2=A+2V+3P+4D.

Both B0 and S0 are negative. Their quotient exact sequence and fixed-determinant Serre duality give

    H1(L0)=H1(S0)-H1(B0)
           =M2-H0(A(4))
           =V+2P+3D.

Here H0(A(4))=A+V+P+D. The center acts trivially on L0. An equivariant rank-two Birkhoff splitting is either one odd doublet in an odd degree or two scalar lines of even degree, since G has no nontrivial characters. A doublet would have degree -14 on each line, which has the wrong central parity. Hence L0=O(-j)+O(-(28-j)), with j even and 2<=j<=14.

For j=2,4,6,8,12,14 the character Sym^(j-2) W+Sym^(26-j) W has respectively a forbidden trivial, A, trivial, A, A, trivial constituent. The remaining pair j=10 has exactly

    Sym8 W+Sym16 W=(P+D)+(V+P+2D)=V+2P+3D.

Therefore L0=O(-10)+O(-18). This is seven fixed scalar degree partitions, not a bundle-candidate search.

## 5. The endpoint derivative is an everywhere rank-two injection

Write U=O(-10) and T=O(-18) for an equivariant splitting of the actual L0. Its actual derivative factors through

    beta_L0:L0 -> (S0/L0)(-2)=A(-8).

Its U row is nonzero. If it vanished, the derivative of U would land in (L0/U)(-2)=O(-20), impossible by degree, making the negative saturated line U horizontal in the constant ambient. Equivariant Hom(U,A(-8)) is one-dimensional, because A=Sym2 W. Every nonzero row is the canonical dual quadratic evaluation inclusion O(-10)->A(-8), up to scalar. Its image is a saturated line isomorphic to U.

The T row is also nonzero. Otherwise its own second fundamental form would factor through (L0/T)(-2)=O(-12). This equivariant Hom is H0(O(6))^G=0 because Sym6 W=V+P. Again a negative horizontal line would result. This does not assume the splitting is preserved by the connection.

The two rows are generically independent. Otherwise the T row would factor regularly through the saturated U image, whereas Hom_G(T,U)=H0(O(8))^G=0. Thus beta_L0 has generic rank two.

Let Ibar be its saturated image in A(-8), and d the length of Ibar/im beta_L0. Then deg Ibar=-28+d. The determinant-degree bound in wedge2 A(-8)=A(-16) gives d<=12. Its saturation-defect divisor is effective and G-invariant, so a nonzero d must be at least twelve. If d=12, det Ibar=O(-16) with its unique G-linearization, and its nonzero generic determinant map to A(-16) would require an invariant vector in A, impossible. Therefore d=0. The actual image is saturated and beta_L0 is rank two everywhere.

Its cokernel is a line of degree -24-(-28)=4, equivariantly O(4). This proves the claimed exact sequence without computing any actual covariant or minor.

## 6. Intrinsic first jets recover the actual forward transform

Twisting the image in Section 5 by T_P1=O(2) gives a saturated rank-two image N in B0=A(-6), with B0/N=O(6). Its preimage in S0 is precisely M=L0^+: it contains L0 and all its derivatives and is saturated, and the actual derivative generates N everywhere. Therefore

    rank M=4, deg M=deg L0+deg N=-28-24=-52,
    S0/M=O(6).

For the actual inclusion L0 in C* O, differentiating its coefficient sections defines the intrinsic map

    P^1(L0*)* -> C* O.

Its generic image is M. The universal principal-parts identity on the fixed binary line gives

    P^1(L0*)*=W(-9)+W(-17).

This has rank four and degree -52. Since M is saturated, the differential-evaluation map factors regularly through M. It is generically full rank between equal-rank equal-degree bundles, hence an everywhere isomorphism. This proves the displayed splitting of M as an actual subbundle, without completeness assumptions on either scalar coefficient system.

## 7. The two actual coefficient systems together span the whole small ambient

Let C' be the constant span of L0. A constant subspace containing L0 contains all its derivatives, hence M. The composite S0->(C*/C')O therefore factors through S0/M=O(6). But Hom(O(6),O)=0, so that composite vanishes. Thus S0 lies in C' O.

The actual S0 spans C*: otherwise a nonzero constant vector in C annihilating every S0 fiber would lie in every E0 fiber and give a nonzero section of E0. This is impossible because E0 has strictly negative top degree. Consequently C'=C*. The actual coefficient map of U+T is therefore surjective:

    Sym10 W+Sym18 W ->> C*.

For completeness, the original exact sequence 0->S->H* O->E*->0 gives

    [H*]=[H0(E*)]-[H1(S)]=2A+2V+2P+2D.

Removing the genuine octic complement J=P+D gives C*=2A+2V+P+D. Meanwhile

    Sym10 W=A+V+D,
    Sym18 W=A+V+2P+D.

The coefficient kernel is consequently equivariantly isomorphic to P+D. This identifies its representation type, not a canonical embedded kernel subspace or a selected relative position of the two D coefficients. On the A and V isotypic components the map is an isomorphism of the full two-copy spaces; each individual scalar curve contributes its A and its V, independently of the other. The P part occurs only for T and maps onto the one P in C*, with one P kernel. The two D copies together map onto one D. Thus at least one curve retains D; if both do, their coefficient spans intersect precisely in that D. These statements give exactly the constant-span alternatives in the theorem.

## 8. Contribution and limits

The full-positive triplet branch now has a genuine small constant ambient, an exact rank-two scalar endpoint, an unramified rank-two derivative, a rank-four intrinsic first-jet subbundle, and a jointly surjective actual coefficient map with completely identified representation loss. The coefficient-span conclusion is stronger than a dimension bound and does not replace a partial linear system with a complete one.

The original t=0 is preserved. No claim concerns the K3 negative image or the K4/K5 invariant-divisor image of PR1199, and no decomposable W-positive work is duplicated. No whole kernel, triplet quotient, maximal profile or coarse bin is removed. Higher-order realization, algebraicity, generic rank-five bounds and the original repair remain outside this conclusion.
