# A constant splitting and a sextic-net apolar obstruction exclude O(-8)+O(2)+O(16)

## 1. Statement and exact scope

Work over C on the fixed physical binary-icosahedral parameter line, with G=SL2(F5), defining representation W, and the original actual saturated plane-section inclusion

    0 -> E -> H O -> Q -> 0,   dim H=30,
    S=Q* inside H* O,
    K=E^-, L=S^-, A=E/K, B=S/L.

Superscript minus means the actual kernel of the second fundamental form for the constant connection. Suppose that the actual Gauss rank is three and its maximal rank-three plateau has profile (1,1). In particular rank E=17, rank S=13, both degrees are -54, top S<=-1, rank L=10, and the derivative of L has rank at most two.

We prove that

    A=O(-8)+O(2)+O(16)                                (1)

is impossible. The original necessary profile-(1,1) theorem and its complete 159-pair list give exactly two ordered records with this A:

    original index 119: B=O(6)+O(-16)+O(-18), defect 12;
    original index 127: B=O(6)+O(-4)+O(-18), defect 0.    (2)

We exclude the first directly by endpoint degree capacity. For the second, equality has two possible endpoint heights. Height 8 is excluded by the full degree-ten polynomial system and its apolar annihilator. Height 7 gives a genuine constant splitting of the actual inclusion, reducing to a rank 16 bundle in a constant 21-space. A partial degree-ten polynomial system is allowed in this residual argument; a basepoint-free sextic-net lemma forces it to be full before the final ambient-dimension contradiction.

This is a narrow A-shape exclusion within maximal profile(1,1), not a full profile-(1,1) exclusion or global rank-three theorem. The two row labels are historical identifiers, not a live-frontier count. The geometric necessity of the original list is an imported written theorem, not inferred from JSON. No selected actual HM/source coefficients, points, parameters, jets, matrices, tensors, instance ranks, scans or large computation are evaluated.

Seven complete immutable inputs are retained in inputs/ and pinned by full URL, byte count, SHA256 and Git blob ID in INPUTS.json. The original actual inclusion, strict-top theorem, profile11 theorem/list and physical character source are at db51525015bb7c5e825833d550d08dedf6f6ea96. The primary four-source theorem is PR1123 at 504b7eb800407dfc7e6340c98c72cdd553939f54. Each retained file was freshly read at its immutable public URL and compared byte-for-byte. No later ledger or unproved profile coverage is used.

The primary theorem leaves four actual E types. Only its D-type has any summand of degree at most -8; the other three admit no nonzero map to O(-8). The onto composite E->A->O(-8) therefore forces

    E=D O(-2)+(W'+T)O(-3)+V O(-4)+O(-8),              (3)

where D=Sym4 W, T=Sym5 W, dim W'=2, dim V=3, and V is the nonstandard three-dimensional representation, distinct from A_std=Sym2 W. We use the universal identities

    Sym6 W=V+P,  Sym7 W=W'+T,
    Sym8 W=P+D,  Sym10 W=A_std+V+D,                  (4)

with dim P=4. All irreducibles are self-dual, and G has no nontrivial one-dimensional representations. Thus every equivariant line occurring below has the stated O(e) linearization, with no additional character twist. The fixed determinant identification identifies the parameter line with P(W); the same choice is used throughout.

## 2. Actual endpoint capacity and its equality case

Let F_0=S, F_1=L and F_(j+1)=F_j^- thereafter. These are saturated subbundles of the original constant H* O. Put G_j=F_j/F_(j+1), q_j=rank G_j for j>=1 and G_0=B. The actual derivative induces sheaf injections

    G_j -> G_(j-1)(-2) -> ... -> B(-2j).              (5)

To justify the first injection, differentiation of F_j stays in F_(j-1), and the kernel of its projection modulo F_j is exactly F_(j+1). This is an actual coherent-image statement, not an assertion that the image is saturated in the target. It also gives q_(j+1)<=q_j. Since L is the endpoint, q_1<=2.

Every F_j is negative, as a subbundle of S. A nonzero such bundle cannot be horizontal: its Grassmannian map would have zero differential, hence be constant in characteristic zero, making the saturated subbundle constant of degree zero. Thus the chain terminates in zero and

    sum q_j=10,   deg L=sum deg G_j.

Let lambda_1>=lambda_2>=lambda_3 be the ordinary degrees of B. Taking determinants in (5) gives

    deg G_j <= sum_(i=1)^q_j lambda_i -2j q_j.

With h_i=#{j:q_j>=i}, one has h_1>=h_2>=0, h_1+h_2=10, and

    deg L <= h_1 lambda_1-h_1(h_1+1)
             +h_2 lambda_2-h_2(h_2+1).               (6)

There are just six universal rank partitions, h_1=5,...,10. For index 119 their capacities, in that order, are

    -110, -90, -74, -62, -54, -50.

But deg L=-54-(-28)=-26, exceeding even the maximum -50. This excludes the positive-defect record without any zero-defect argument.

For index 127 the six capacities are

    -50, -42, -38, -38, -42, -50,

and deg L=-54-(-16)=-38. Therefore equality holds in every individual determinant bound, and the height pair is (7,3) or (8,2).

Here the three degrees 6,-4,-18 are distinct. The highest-degree summand in wedge^q B is unique for q=1,2. Equality makes the determinant map a nonzero constant into that summand; all lower components vanish by degree. The generic image is consequently the top q-summand subspace. The map factors through that top subbundle everywhere, because the projected map vanishes generically and its target is torsion-free. Its determinant has no zero, so

    G_j -> B(-2j) identifies G_j with B_(q_j)(-2j),    (7)

where B_q is the top q-summand subbundle. These are exact images of actual composite derivative maps. In particular the highest-line channel of each intermediate derivative is nonzero: composing it with the preceding identification gives the nonzero highest-line channel in (7). It is an isomorphism on that line after the indicated twist.

Writing h=h_1, the last nonzero F_h is the saturated line

    C=O(6-2h).                                       (8)

Its first k derivatives, for 0<=k<=h, have a new nonzero leading component in the successive graded terms and are generically independent. Their span has rank k+1 and lies in F_(h-k). All assertions refer to the actual constant connection; no connection is assigned to a Birkhoff complement.

## 3. Height 8 is excluded without strengthening top S

If h=8, C=O(-10). Its actual inclusion in H* O has an equivariant coefficient map Sym10 W->H*. The nine independent directions from Section 2 force its image to have dimension at least 9. By (4), every proper quotient of Sym10 W=A_std+V+D has dimension at most 8. Hence the coefficient map is injective. Its image is a genuine constant space U_11 isomorphic to Sym10 W.

For a complete degree-e polynomial line in Sym^e W O, its kth osculating bundle is

    Sym^k W O(k-e), with fiber l^(e-k) Sym^k W.       (9)

This is the universal differentiation/multiplication identity, not a selected-parameter evaluation. Its generic containment in a saturated F_(h-k) extends everywhere. Thus Sym8 W O(-2) lies in S inside U_11 O.

Under invariant apolarity on Sym10 W, the annihilator of l^2 Sym8 W is l^9 W. The projection of E into U_11* O therefore factors through W O(-9). But every summand of (3) has degree at least -8, so this morphism is zero even without equivariance. Consequently all of U_11 annihilates E and U_11 O lies in S, contradicting H0(S)=0. This argument uses only top S<=-1, not the stronger profile21 bound.

## 4. Height 7 gives a genuine constant splitting

Suppose h=7. Now C=O(-8); its coefficient map Sym8 W->H* has image dimension at least 8. Since Sym8 W=P+D and every proper quotient has dimension at most 5, it is injective. Let U_9 be its actual constant image. Formula (9) puts

    Sym7 W O(-1) inside S and inside U_9 O.

Its annihilator in U_9* O is the complete degree-eight line J_0=O(-8). Thus the actual projection

    p:E -> U_9* O

factors through J_0. For the exact source (3), only its O(-8) summand can map to J_0; all higher-degree summands have zero Hom. The resulting scalar on O(-8) is nonzero. Otherwise U_9 O would be a constant subbundle of S, again impossible.

Put N=ker(H->U_9*), a constant 21-space. Choose an equivariant Birkhoff splitting E=F+J with

    F=D O(-2)+(W'+T)O(-3)+V O(-4),  J=O(-8).        (10)

This splitting is not assumed horizontal. Its actual embedded F lies in N O. The actual inclusion J->H O has a coefficient map Sym8 W->H. Its composition with H->U_9* is an isomorphism on coefficient spaces, because p|J is a nonzero isomorphism onto the complete line J_0. Hence that coefficient map is injective and its image C_9 is a constant complement to N:

    H=N direct-sum C_9,
    E=F direct-sum J as actual embedded bundles.     (11)

This proves the constant splitting rather than selecting a horizontal complement from (10). Equivalently the entire degree-eight graph is removed by a constant linear shear, justified by completeness of its coefficient system. No coefficient is chosen or evaluated.

The inclusion F->N O is saturated: the quotient of (11) is

    H O/E=(N O/F) direct-sum (C_9 O/J),

and it is locally free. Thus both actual summands in the constant decomposition have their own well-defined Gauss derivatives. Those derivatives are block diagonal. The nonconstant line J has Gauss kernel zero and quotient J=O(-8), so cancellation from (1) gives the actual Gauss quotient

    A_F=O(2)+O(16).                                 (12)

Here and below cancellation is of actual direct sums; uniqueness of splitting on P1 gives the written ordinary and equivariant degrees. Rank F=16 and deg F=-46.

## 5. The residual dual endpoint is a forced three-step chain

Set S_F=(N O/F)* and S_J=(C_9 O/J)*. Equation (11) gives the actual constant decomposition

    S=S_F direct-sum S_J,
    rank S_F=5, deg S_F=-46.

The complete degree-eight line J has apolar annihilator

    S_J=Sym7 W O(-1),
    L_J=S_J^-=Sym6 W O(-2).                         (13)

For example, the fibers are l Sym7 W and l^2 Sym6 W; differentiation modulo l Sym7 W proves the second identity, which is a saturated kernel. The quotient B_J=S_J/L_J is O(6). Its rank is one, as is the derivative rank of L_J: the latter is at most one by its induced injection into B_J(-2), and cannot be zero because L_J is negative and saturated.

Let L_F=S_F^-. Block diagonal differentiation gives

    L=L_F direct-sum L_J,  rank L_F=3,
    B=B_F direct-sum O(6), B_F=S_F/L_F.

Cancelling O(6) from the exact zero-defect B in (2) yields

    B_F=O(-4)+O(-18),   deg L_F=-46-(-22)=-24.       (14)

The endpoint condition rank beta_L<=2 and rank beta_(L_J)=1 imply rank beta_(L_F)<=1. It is positive by negativity. Applying the actual kernel construction repeatedly to S_F gives

    M_0=S_F, M_1=L_F, M_2=M_1^-, M_3=M_2^-,
    M_4=0,

with ranks5,3,2,1,0. Indeed all successive derivative ranks are at most one by (5), and positive while the bundle is nonzero.

Each line quotient M_j/M_(j+1), j=1,2,3, injects into B_F(-2j) and hence has degree at most -4-2j. Their sum is deg L_F=-24, precisely

    (-6)+(-8)+(-10)=-24.

Thus equality holds separately. As in (7), the exact composite images are the top lines, and M_3 is the saturated line O(-10). Its first three actual derivatives lie in S_F and give four independent generic directions. We will not infer from this that its coefficient system is complete.

## 6. A partial coefficient quotient and its apolar factor

Let

    q:Sym10 W -> R subset N*

be the actual coefficient map of M_3=O(-10), with R its constant image. It is a quotient onto R, possibly proper. Duality embeds R* into (Sym10 W)*. The actual projection of F to R* O followed by this embedding is a map

    F -> R* O -> (Sym10 W)* O.                       (15)

The four osculating directions of M_3 are images under q of the universal fibers l^7 Sym3 W. They lie in S_F, which is annihilated by F. Therefore (15) annihilates l^7 Sym3 W. The full apolar annihilator of these universal fibers is l^4 Sym6 W, and hence(15) factors through the saturated bundle

    (Sym6 W) O(-4)=(V+P)O(-4).                      (16)

This uses the injection R*->(Sym10 W)*, not a fictitious full rational-normal system inside R. It is valid for every quotient q, irrespective of ramification or the rank of the projected osculating image. Under the fixed self-duality, (16) embeds in (Sym10 W)* O by multiplication by l^4.

By(10), all summands of F except V O(-4) have zero Hom to(16) by degree. The V block has only the scalar channel to the unique V in Sym6 W. This scalar is nonzero: if (15) were zero, the projection F->R* O would be zero, making the nonzero R a constant subspace of S_F. But S_F is a subbundle of S and H0(S)=0.

Consequently the constant subspace R* inside (Sym10 W)* contains l^4 V for every parameter line l. Section 7 proves that these fibers span the whole Sym10 space. Thus R is necessarily full and dim R=11. The rank 13 subbundle

    D O(-2)+(W'+T)O(-3) inside F

is killed by the projection N O->R* O. Its constant kernel has dimension 21-11=10. An injection of a rank 13 bundle into this rank 10 bundle is impossible. This is the desired contradiction.

## 7. The universal sextic-net span, without a coefficient calculation

The copy V in Sym6 W is three-dimensional and consists of independent binary sextics. Its common-zero divisor, if nonempty, is G-invariant on P1 and has degree at most 6. Projectively G acts as A5. Every point stabilizer is cyclic: a finite group fixing a point embeds by its tangent character in C*, because a finite-order transformation with trivial tangent multiplier is the identity. The cyclic subgroups of A5 have order at most 5. Hence every orbit has size at least 60/5=12. A nonempty invariant divisor of degree at most 6 is impossible, so the sextic net V is basepoint-free.

Its evaluation sequence is therefore exact in vector bundles:

    0 -> T_V -> V O -> O(6) -> 0.

Here rank T_V=2 and deg T_V=-6. The coefficient inclusion V->H0(O(6)) is injective, so H0(T_V)=0. Birkhoff splitting writes

    T_V=O(-a)+O(-b),  a,b>=1, a+b=6.

In particular a,b<=5. Twisting by 4 gives H1(T_V(4))=0 because each line degree is at least -1. Hence the global-section map is onto:

    V tensor Sym4 W -> Sym10 W.                    (17)

Pure fourth powers span Sym4 W in characteristic zero. Thus the span of l^4 V over all lines l is exactly the image in (17), which is the full degree-ten space. This is the fact used in Section 6. It holds for any independent basepoint-free sextic net; no special coordinates, matrices or actual coefficients enter its proof.

## 8. Contribution, checks and boundaries

The new exclusion uses both original B possibilities in (2), keeping their different defects and endpoint degrees separate. The difficult zero-defect height 7 branch is resolved by actual constant splitting, a residual rank-one endpoint chain, and dual injection of a possibly partial polynomial quotient into the full apolar space. Completeness is proved only after the universal sextic-net span applies. No non-horizontal bundle projector is substituted for the constant projection.

The bounded verifier authenticates all seven inputs, the exact two historical records, both six-partition capacities and equality optimizers, all rank/degree identities, the relevant universal character identities, Hom-degree vanishings and every possible pair a,b>=1 with a+b=6 in the sextic-net argument. It does not rerun the historical enumeration, prove its geometric coverage, sample a parameter, or evaluate any actual instance. The geometry and saturation arguments are supplied in this proof and are subject to independent whole-proof review.

All other profile11 A shapes remain outside this note. No global COV theorem, generic rank-four lower bound, maximal Gauss rank, obstruction value, full-adjoint invertibility, smoothing, algebraicity or original-theorem repair is claimed.
