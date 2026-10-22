# A leading-jet formula for the vertex fourth-square class

## Scope and inputs

Work at the generic point of the vertex line, with coefficient field k=C(L), in the actual completed binary harmonic frame of [PR692](https://github.com/Akilleez-QA/read-em-and-weep/pull/692), commit 858f96ba1539afb1293f31239b8761af08e46f60. All orders below are weighted matrix orders: a matrix of weight d has diagonal, upper, lower entry degrees d,d-2,d+2. Retain the actual filtered pair and all equation/frame units. The leading nilpotent matrix n8 is given by the actual regular pair f3,g5, with a nonzero common leading unit allowed.

The inputs are J3 squared zero on 3Q; J3=H(L0)+qH(L1)+q^2H(L2), with orders at least 12,8,4; and J4=a Jtilde+q^3H(K), with K initially of order at least -2. Here Jtilde is the lift with no q^3 harmonic coefficient. Write J4^2=q^3 S4 Id. [PR691](https://github.com/Akilleez-QA/read-em-and-weep/pull/691), commit dac9a7eca25d112dff9702ec863d161709792326, gives S4=a^3 h rho4. PR692 proves that rho4 has exactly the single possible global binary-degree-eight block. This means its only possibly nonzero block is degree eight; it does not assert that it is nonzero. The scalar a is q-independent and is a unit over k; h is a nonzero binary form of degree four.

For matrices, Bj denotes ordered entrywise harmonic multiplication followed by matrix multiplication. It lowers weighted degree by 4j. Set sc(X)=tr(X)/2 for a scalar matrix X.

## 1. The apparent weight-minus-two fourth coefficient vanishes

The scalar square coefficient of Jtilde has order at least twelve by the eight-term estimate of PR692. Its name here is chi. Exactly,

    S4=a^2 chi+a^3 h tr(nK).

Since S4=a^3 h rho4 has binary degree twelve, its degree-ten part is zero. The only possible degree-ten term on the right is

    a^3 h tr(n8 K_{-2}).

A regular trace-free matrix of weight -2 has only a constant lower entry. The upper entry of n8 is a nonzero unit times -f3^2. The binary polynomial ring over k is a domain, so cancellation of a^3 h f3^2 forces K_{-2}=0. Thus K has order at least zero in the actual generic-vertex frame. This conclusion uses global scalar block reduction; regularity alone would not give it.

## 2. Eliminate the fourth coefficient modulo the square ideal

Put P=(L0)12=a^2 h n8, M=(L1)8, R=(L2)4. Define the scalar homogeneous degree-twelve form

    C(P,M,R)=sc(MR+RM+B1(P,R)+B1(R,P)+B1(M,M)
                   +B2(P,M)+B2(M,P)+B3(P,P)).

The expression inside sc is scalar: it is the degree-twelve coefficient of the square of a trace-free rank-two harmonic lift. All eight ordered products are retained. Homogeneity and the three lower bounds imply chi12=C(P,M,R); no higher coefficient of any Lj can contribute. Since K_{-2}=0, no higher coefficient of n can contribute either. Therefore

    rho4,8=C(P,M,R)/(a h)+tr(n8 K0).                 (1)

In particular h divides C(P,M,R) for the actual data: this follows from (1) and regularity of rho4,8 and tr(n8 K0), not from declaring h invertible.

Let I0=(f3,g5) in k[X,Y]. In the displayed regular-pair convention K0 has constant diagonal entry x, zero upper entry, and quadratic lower entry z. Hence

    tr(n8 K0)=u0(2 f3 g5 x-f3^2 z) in (I0^2)8,

where u0 is the nonzero leading determinant unit if present. Thus the degree-eight associated square-ideal quotient class is

    [rho4,8]=[C(P,M,R)/(a h)] in k[X,Y]8/(I0^2)8.  (2)

Equation (2) eliminates every fourth coefficient and every higher weighted jet. It is a formula for the actual leading obstruction class in the fixed harmonic frame. It is not an evaluation of that class, a proof of its vanishing, or permission to replace the full actual ideal by its initial ideal in other degrees.

## 3. Precisely what second-normal information remains

The degree-sixteen part of J3^2=0 is

    {P,R}+M^2+B1(P,M)+B1(M,P)+B2(P,P)=0.          (3)

Thus the fixed lower data P,M impose a linear trace equation on R. The difference D between any two homogeneous weight-four solutions of (3) obeys tr(n8 D)=0. The regular-pair syzygy calculation gives exactly

    D=ell [[f3/2,0],[g5,-f3/2]],   ell in k[X,Y]1. (4)

Indeed the general kernel has upper entry f3 y1, lower entry g5 z1, and diagonal (f3 z1-g5 y1)/2. At weight four, y1 has degree -1 and is zero, while z1 has degree one. Nonzero common units cancel from the trace equation.

The corresponding exact change in C is

    C(P,M,R+D)-C(P,M,R)
      =sc(MD+DM+B1(P,D)+B1(D,P)).                (5)

The ambient weight-four trace-free space has dimension 5+3+7=15. The trace map has image (I0^2)12, which is the whole 13-dimensional space of degree-twelve binary forms by the published square-quotient socle bound eleven. Alternatively its two-dimensional kernel (4) and rank-nullity give the same surjectivity. Since the actual R exists, the solution set of (3) is an affine two-dimensional local space. Formula (5) defines a linear map from its translation space to k[X,Y]12/(a h (I0^2)8). Its rank is not determined here. Only on changes for which the numerator is divisible by h does division give a map to k[X,Y]8/(I0^2)8.

There is no quadratic term in D at cubic q order. Equation (5), including both first-harmonic products, is the remaining dependency test. Eliminating R by (3) alone requires proving that (5) belongs to a h (I0^2)8 for the allowed changes. No such identity is asserted here. For arbitrary local solutions of (3), even divisibility of (5) by h is not supplied by (3) alone. An arbitrary local trace-kernel change is not automatically an actual global completion.

For actual global completion changes at fixed a,h,b and Ua, [PR685](https://github.com/Akilleez-QA/read-em-and-weep/pull/685), commit 449a8df60662bd7a1d93e318ea4f7e6dab28e5ad, gives J3 changes of the form -q^2 N s, with s in A+D. Their L2 change has weighted order at least eight, since N starts at eight and s is regular. Consequently the actual R=(L2)4 is unchanged by every classified global completion change. The local two-dimensional trace kernel (4) must not be identified with global cochain freedom.

## 4. The generic class detects global scalar vanishing

The exact relation-bundle sequence in [the pinned square-filtration theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md), section 1, twisted by six, is

    0 -> P4 O_L(-2) -> Sym^8 U tensor O_L(2) -> Q4(6) -> 0.

Its quotient is locally free: the cited actual regular initial-pair theorem gives the same degree-eight quotient dimension at every point of L, so the relation map has constant fiber rank. Since H0(O_L(-2))=0, the induced map from the 27-dimensional polynomial target H0(Sym^8 U tensor O_L(2)) to H0(Q4(6)) is injective. A section of the latter vector bundle which vanishes at the generic point of the integral line L vanishes everywhere.

The generic restriction of the image of rho4 is exactly (2). Consequently

    rho4=0 globally  if and only if
    C(P,M,R) belongs to a h (I0^2)8 over k=C(L).    (6)

This is a complete criterion for vanishing of the fourth-square scalar, not a computation deciding the criterion. It does not use Hartogs for the nonreflexive square ideal. Instead, it uses the global single-block theorem and the torsion-free relation-bundle quotient, then its injectivity on global polynomial sections. It also does not identify this scalar gate with the subsequent Bockstein value.

## Contribution and remaining gate

The vertex scalar class and its global vanishing criterion now need only the three leading weighted jets P,M,R and the fixed harmonic products; no fourth-normal coefficient or higher actual-pair jet is needed. The outstanding mathematical input is a structural determination of the actual R, or a proof that the explicitly retained dependence (5) dies in the square-ideal quotient for the appropriate admissible changes. The first-order, higher-order lifting, and algebraicity claims remain distinct. No selected actual coefficient, point, derivative, matrix rank, local model experiment, or large computation was used.
