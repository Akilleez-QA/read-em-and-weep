# First-normal coherence factors the local vertex variation

## Inputs and scope

Work over k=C(L), in the fixed actual completed harmonic frame of [PR692 at 858f96ba1539afb1293f31239b8761af08e46f60](https://github.com/Akilleez-QA/read-em-and-weep/blob/858f96ba1539afb1293f31239b8761af08e46f60/research/hm/vertex-scalar-filtration/PROOF.md), sections 1–2. Retain its actual filtered pair and equation/frame units. This proof uses the first-normal multiplicative coherence J3|2Q=F Ns, not merely the second-normal equation J3²=0. The additional leading-vertex formula used in section 3 is a separate dependency: [PR713 at 5b3943980ecaef78ee7f56fbc015d40955fb24f0](https://github.com/Akilleez-QA/read-em-and-weep/blob/5b3943980ecaef78ee7f56fbc015d40955fb24f0/research/hm/leading-vertex-obstruction/PROOF.md).

Write n=n8 and T=T4 for the leading coefficients of Ns=H(n_full)+qH(T_full) modulo q². A trace-free matrix of weight d has diagonal, upper and lower entry degrees d,d−2,d+2. Thus n has weight eight and T weight four. Let f3,g5 be the actual regular initial pair, with common nonzero coefficient unit u0 retained. Put I0=(f3,g5) in S=k[X,Y]. The negative source a is a unit over k and q-independent; the nonzero positive source h lies in S4. Set f=a²h. If s is the degree-zero part of F1, first-normal coherence gives precisely

    P=f n,
    M=f T+s n+B1(f,n).

These are respectively the weight-twelve and weight-eight coefficients of J3. Higher filtered coefficients cannot contribute to these weights. The harmonic product B1 lowers weight by four and is ordered entrywise before matrix multiplication. Its convention is [the pinned universal harmonic-product theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/UNIVERSAL-SECOND-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-DEFECT.md).

## 1. Ordered associativity supplies the missing factor

Transport multiplication of harmonic lifts modulo q² to coefficient pairs. For matrices A=A0+qA1 and B=B0+qB1 this gives

    A*B=A0 B0+q(A0 B1+A1 B0+B1(A0,B0)).

Here the coefficient named B1 in the operator B1(A0,B0) is distinct from the first coefficient of B. This product is associative because ambient multiplication is associative. Scalar coefficient pairs are central because the underlying scalar algebra is commutative. Matrices themselves are not assumed to commute. The coefficient-one associativity identity is

    B1(A,B)C+B1(AB,C)=A B1(B,C)+B1(A,BC).

These statements hold entrywise and termwise in the actual completion and hence in the homogeneous weights under consideration.

Let D be any trace-free weight-four matrix with {n,D}=nD+Dn=0. In the coefficient algebra take N=n+qT, F=f+qs and D with first coefficient zero. Centrality and associativity give

    (F*N)*D+D*(F*N)=F*(N*D+D*N).

The right inner zeroth coefficient is zero. Its first coefficient is

    Z=TD+DT+B1(n,D)+B1(D,n).

Consequently the first coefficient on the right is f Z: both s{n,D} and B1(f,{n,D}) vanish. The first coefficient on the left is

    MD+DM+B1(P,D)+B1(D,P).

Thus, as an ordered matrix identity,

    MD+DM+B1(P,D)+B1(D,P)=f Z.                    (1)

The coefficientwise anticommutator of two trace-free two-by-two matrices over a commutative scalar algebra is scalar. In particular Z is scalar. With sc=tr/2, define the homogeneous degree-eight form

    Ψ(D)=sc(TD+DT+B1(n,D)+B1(D,n)).

Equation (1) yields the exact scalar identity

    sc(MD+DM+B1(P,D)+B1(D,P))=a²h Ψ(D).          (2)

No inversion of h occurs. This identity holds for every local tangent D, including those which are not globally realizable completion changes. For fixed n,T and harmonic frame, Ψ does not involve h,s or the source correction b. The normalized variation below retains only the scalar factor a. This is independence of the operator's displayed inputs, not an assertion about a parameter-dependent choice of D or changes of frame.

## 2. A two-dimensional obstruction to first-normal trace orthogonality

The regular-pair convention gives

    tr(n [[x,y],[z,−x]])=u0(2f3 g5 x+g5² y−f3² z).

The weight-four trace kernel is exactly

    D=ell [[f3/2,0],[g5,−f3/2]],   ell in S1.

For completeness, the general polynomial syzygy has y=f3 y1, z=g5 z1 and x=(f3 z1−g5 y1)/2; at weight four y1 has degree −1 and vanishes, while z1 has degree one. Regularity of the pair, rather than any selected evaluation, gives this calculation. Hence the source has dimension two over k.

Seek a homogeneous first-normal lift D+qD1, where D1 is trace-free of weight zero. Its anticommutator with N has zero zeroth coefficient and first coefficient

    Z+{n,D1}=(Ψ(D)+tr(nD1)) Id.

Equivalently the first harmonic coefficient of tr(N*(D+qD1)) is Ψ(D)+tr(nD1). There is no factor-two correction: sc({A,B})=tr(AB) for ordinary trace-free rank-two matrices, and the same coefficientwise polarization holds for *.

A regular weight-zero D1 has constant diagonal x, upper entry zero and quadratic lower entry z. Therefore its trace image is exactly

    u0(2f3g5 k−f3² S2)=(I0²)8.

The two summands have dimensions one and three and zero intersection: f3g5 in f3²S2 would imply that f3 divides g5, contradicting the regular pair. The image has dimension four and S8 dimension nine. It follows that

    O_N: ker(tr(n−))4 -> S8/(I0²)8,
    D |-> [Ψ(D)]                                            (3)

is a well-defined linear map from a two-dimensional space to a five-dimensional space. A homogeneous first-normal trace-orthogonal lift exists if and only if O_N(D)=0. A solution then obeys tr(nD1)=−Ψ(D). Changing the initially chosen first coefficient of a lift changes Ψ by this trace image, so (3) is its obstruction class in the fixed actual frame.

No rank or value of (3) is asserted. In particular this is not an identification with the actual second or fourth Bockstein.

## 3. Consequence for the leading fourth-square formula

The leading-vertex formula defines C(P,M,R), with R of weight four, and gives

    [rho4,8]=[C(P,M,R)/(a h)] in S8/(I0²)8.

At fixed P,M, two local solutions R and R+D of the leading second-normal trace equation differ by precisely the D above. Its previously retained variation is the left side of (2). Therefore

    C(P,M,R+D)−C(P,M,R)=a²h Ψ(D),
    [C(P,M,R+D)/(a h)]−[C(P,M,R)/(a h)]=a O_N(D).    (4)

If the base numerator is divisible by h, as for actual R, every local translated numerator is now divisible by h as well. This removes the divisibility caveat under the stronger first-normal coherence input. It does not deduce divisibility from the bare second-normal trace equation alone. It also does not show O_N=0, eliminate the dependence on R, or make every local R+D into a global actual completion.

Indeed [PR685 at 449a8df60662bd7a1d93e318ea4f7e6dab28e5ad](https://github.com/Akilleez-QA/read-em-and-weep/pull/685) classifies actual global completion changes with second-normal order at least eight, so they do not change R4 at all. Formula (4) instead identifies the residual local dependency as first-normal trace-orthogonality. It replaces a conditional degree-twelve numerator test by the definite degree-eight obstruction map (3). Determining whether that map vanishes is the next structural gate; it is not decided here. There is no actual source-instance, point, derivative, matrix-rank evaluation or large computation, and no algebraicity claim.
