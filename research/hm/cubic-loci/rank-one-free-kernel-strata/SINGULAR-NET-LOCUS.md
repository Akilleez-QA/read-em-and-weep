# Bound singular-net loci on Gr(3,5)

Let G=Gr(3,C^5), let S be its tautological rank-three bundle, and let J be a finite-dimensional complex vector space. Let T:Schur_(2,1)S → J⊗O be a fixed bundle map on Gr(3,C^5). Assume every kernel is rank-one-free after identifying Schur_(2,1)W with sl(W)⊗det W, and has dimension at most four. The closed locus where a kernel contains a singular three-dimensional net has dimension at most four; its net incidence is finite and bijective on geometric points, not claimed to be an isomorphism. The proof below is conditional only on these explicitly stated hypotheses, not on a specific operation. The net conjugacy theorem is proved in [unit one](../constant-rank-nets/PROOF.md).

## 1. Uniqueness of a singular net inside a rank-one-free four-space

Let U be three-dimensional and K a four-dimensional subspace of sl(U) containing no nonzero rank-one element. Suppose L subset K is a three-dimensional determinant-zero subspace. By the imported classification, after conjugation L is the full skew-symmetric space for a nondegenerate symmetric form, which we put in standard coordinates.

Choose an element outside L and subtract its skew-symmetric part. This gives a nonzero symmetric traceless matrix B, and K = L direct-sum C B.

B is invertible. Indeed, if its rank were at most two, its symmetric quadratic polynomial would factor over C as the product of two nonzero linear forms. Thus B=(uv^T+vu^T)/2 for nonzero u,v. Since tr B=0, one has v^T u=0. The nonzero rank-one matrix A=uv^T is then traceless, while A-B is skew-symmetric. Hence A belongs to K, a contradiction.

Write C(x) for the universal cross-product skew operator with parameter x in C^3. The determinant polynomial on K is

    det(C(x)+tB) = t (x^T B x + t^2 det B).

To check the identity without any evaluated instance, use the polarized determinant expansion. The constant term is det C(x)=0. The coefficient of t is tr(adj(C(x))B)=x^T Bx, because adj(C(x))=xx^T. The coefficient of t^2 is tr(adj(B)C(x))=0, since adj(B) is symmetric and C(x) is skew-symmetric. The coefficient of t^3 is det B.

The quadratic factor is nondegenerate in the four variables (x,t): B and det B are invertible. In particular it is irreducible over C. The only linear factor of the determinant polynomial is therefore t, up to scalar.

Every three-dimensional determinant-zero subspace of K is a hyperplane. Its defining linear form divides this determinant polynomial, by restricting the polynomial to the hyperplane. Consequently it must be L. The displayed nondegenerate quadratic also proves the asserted smooth-quadric description. When dim K=3, uniqueness is immediate; smaller K contains no net.

## 2. The proper incidence of singular nets

Put D=det S and E=sl(S) tensor D. Inside the relative Grassmannian Gr_G(3,E), take the closed incidence Y defined by the two conditions on its tautological rank-three bundle L:

- T|L=0;
- the restriction of the determinant polynomial to L is identically zero.

The determinant condition is intrinsically the vanishing of a section of Sym^3(L^*) tensor the appropriate determinant-line twist. Thus Y is closed in a projective G-scheme and is proper over G. Its image C is closed.

At every geometric point of Y, L is rank-one-free, since it lies in K_W. The imported classification applies, so it is a constant-rank-two net. Section 1 shows that each geometric fiber of Y -> G has at most one underlying point. Thus this proper finite-type morphism is quasi-finite and hence finite. We may replace Y by its reduced scheme when computing dimensions or constructing the bundles below. The morphism from that reduced scheme remains finite and is bijective on geometric points over the reduced image C.

## 3. A relative net gives a conformal structure on S

We now work on the reduced Y. All bundles from G are pulled back without further notation. Set L'=L tensor D^(-1), a rank-three subbundle of sl(S). Its trace-square pairing is everywhere nondegenerate by the imported classification. Therefore

    L' is isomorphic to (L')^*.

On p:P(L')->Y, with projective space parametrizing lines, consider the universal endomorphism

    N:p^*S -> p^*S tensor O(1).

Every geometric fiber has rank two. The determinant is identically zero by the defining incidence condition. Since the base P(L') is reduced, the minors give the constant-rank condition scheme-theoretically; alternatively the determinant already vanishes by construction. Splitting an invertible 2-by-2 minor shows that R=ker N is a line subbundle.

On each geometric projective-plane fiber of p, the net classification proves R=O(-1). Consequently R tensor O(1) restricts to the trivial line bundle on every fiber. Cohomology and base change gives a line bundle M=p_*(R tensor O(1)) on Y and an evaluation isomorphism

    R = O(-1) tensor p^*M.

The kernel inclusion R -> p^*S, by adjunction, determines a bundle map

    L' tensor M -> S.

On each geometric fiber this is the linear isomorphism parametrizing the kernel lines in the constant-rank-net classification. Hence it is an isomorphism of rank-three bundles on Y. In particular S has a nondegenerate symmetric quadratic form valued in M^2, transported from the trace pairing on L'. No choice of local normal form is required to glue this structure.

## 4. The Chern relation

All equalities in this section use rational Chow classes; they may equivalently be pulled back to a smooth projective resolution of any integral component under consideration.

Self-duality of L' implies c1(L')=c3(L')=0 rationally. Write m=c1(M) and a=c2(L'). From S=L' tensor M, the splitting principle gives

    c1(S)=3m,
    c2(S)=a+3m^2,
    c3(S)=ma+m^3.

It follows that the pullback to Y of the class

    R_G = 27c3(S) - 9c1(S)c2(S) + 2c1(S)^3

vanishes. This conclusion is valid as an operational Chern-class identity even when Y is singular. To avoid that language, pull the displayed bundle isomorphisms to a smooth projective resolution and apply the same computation there.

## 5. No divisorial image

Let H=c1(S^*) be the Plucker hyperplane class on G. Write sigma_lambda for the usual Schubert classes indexed by partitions in the 3-by-2 rectangle. Then

    c1(S)=-H, c2(S)=sigma_(1,1), c3(S)=-sigma_(1,1,1).

The elementary Pieri calculations are

    integral_G H^6 = 5,
    integral_G H^4 sigma_(1,1) = 3,
    integral_G H^3 sigma_(1,1,1) = 1.

For completeness these are the numbers of saturated Young-diagram chains from the empty partition, (1,1), and (1,1,1), respectively, to (2,2,2). The corresponding standard-tableau counts are 5, 3, and 1. Therefore

    integral_G R_G H^3 = -27 + 9*3 - 2*5 = -10.

Suppose Y had an integral component Y0 of dimension five. Since Y -> G is finite, its image is an integral divisor on G. Let X -> Y0 be a smooth projective resolution, and g:X->G the composite. The cycle g_*[X] is a positive multiple of that divisor, so equals dH in the divisor class group for an integer d>0. This uses Pic(G)=Z H and positivity of the degree of a nonzero effective divisor. Pullback of R_G to X vanishes by Section 4. The projection formula would imply

    0 = integral_X g^*(R_G H^2)
      = integral_G R_G H^2 (dH)
      = -10d,

a contradiction.

Nor can Y have a six-dimensional component. Its finite image would then be all of G, with positive degree e, and the same projection-formula argument using R_G H^3 would give 0=-10e. Since G has dimension six and Y is finite over G, these exclusions prove dim Y <=4 and hence dim C <=4.

The Chern argument excludes dimension six without an operation-specific example.

