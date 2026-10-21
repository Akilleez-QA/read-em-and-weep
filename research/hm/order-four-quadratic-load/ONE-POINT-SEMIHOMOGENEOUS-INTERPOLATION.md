# One-point semihomogeneous form of the actual interpolation

## Setup and result

Use the actual smooth beta blowdown (A,P,Sigma) of GENERIC-BETA-ABELIAN-INTERPOLATION.md and ACTUAL-THETA-KERNEL-INTERPOLATION.md. Choose the origin in Sigma and a type(1,5) square root Theta of P. Then

    G=Sigma=K(Theta),   |G|=25,
    rho:A -> B=A/G,    rho^(-1)(0)=Sigma.

The isogeny rho is finite etale. For n=1 and3 there are simple rank-five vector bundles W_n on B with

    rho_*P^n = W_n^directsum5,
    rho*W_n = (P^n)^directsum5.

They are semihomogeneous, meaning that every translate of W_n is isomorphic to W_n tensored with a suitable line in Pic0(B). Their cohomology is

    h0(W_1)=4,   h0(W_3)=36,
    H^i(W_n)=0 for i>0.

The actual fat-point groups become

    H1(A,P I_Sigma^2)=H1(B,W_1 I_0^2)^directsum5,
    H1(A,P^3 I_Sigma^4)=H1(B,W_3 I_0^4)^directsum5,

where the two one-point spaces have dimensions11 and14. This is a geometric reduction from25 points to one point on an isogenous surface, not a rank conclusion.

## 1. The pushforward endomorphism algebra

Put L=P^n. Since every g in G preserves Theta, it preserves L. For each g choose an isomorphism t_g*L -> L. Composing pullback of sections with this isomorphism defines an endomorphism of rho_*L. By finite-etale adjunction,

    Hom_B(rho_*L,rho_*L)
      = Hom_A(rho*rho_*L,L)
      = directsum_(g in G) Hom_A(t_g*L,L).

Every summand is one-dimensional. Thus the25 deck operators form a basis of the entire endomorphism algebra. Their multiplication is that of the twisted group algebra of G determined by the theta-group cocycle of L. Its commutator, possibly with the opposite convention depending on the chosen operators, is

    e_Theta^(2n) on G times G.

The theta commutator e_Theta on K(Theta) is a perfect alternating pairing. Since2n is invertible modulo5 for n=1,3, this new pairing is also perfect. The center of the twisted group algebra therefore consists only of scalars: a basis element indexed by g commutes with every basis element precisely when g lies in the radical of the commutator pairing. Maschke's averaging argument gives semisimplicity over C. A central semisimple C-algebra of dimension25 is Mat_5(C).

Choose matrix units in this algebra. Their diagonal idempotents have vector subbundles as images; the off-diagonal units identify all five image bundles. Hence rho_*L=W_n^directsum5 and rank(W_n)=25/5=5. Furthermore

    End_B(W_n)=C,

because it is a diagonal corner of Mat_5(C). The decomposition depends on matrix-unit choices and is not claimed canonical.

Pulling back the decomposition gives (rho*W_n)^directsum5=L^directsum25. Krull–Schmidt for vector bundles on the proper variety A implies rho*W_n=L^directsum5. Alternatively, the matrix-unit action on the split deck sum has a five-dimensional multiplicity representation and each minimal idempotent has image L^directsum5.

## 2. Semihomogeneity and exact cohomology

Let b be any point of B and choose a in A with rho(a)=b. Then

    t_b*(rho_*L)=rho_*(t_a*L).

The line t_a*L tensor L^(-1) lies in Pic0(A). Pullback rho*:Pic0(B)->Pic0(A) is an isogeny and is surjective, so choose alpha in Pic0(B) pulling back to this line. Projection formula gives

    t_b*(W_n^directsum5)=(W_n tensor alpha)^directsum5.

Since W_n is simple, hence indecomposable, Krull–Schmidt identifies the individual summands. Thus t_b*W_n=W_n tensor alpha.

Finite pushforward preserves all cohomology. The ample abelian line L=P^n has h0=chi=20n^2 and no higher cohomology. Dividing the five isomorphic summands gives

    h0(W_n)=chi(W_n)=4n^2,
    H^i(W_n)=0 for i>0.

The pullback equality also gives

    rho*c1(W_n)=5n c1(P),
    c1(W_n)^2=40n^2,
    ch(W_n)=5 exp(c1(W_n)/5).

These Chern identities are checks on the actual bundle construction; they are not used to infer existence or simplicity.

## 3. All25 point conditions become one fat point

Because rho is etale and Sigma is exactly the reduced inverse image of0,

    I_Sigma^m=rho*(I_0^m)

for every m>=0. Therefore

    rho_*(P^n tensor I_Sigma^m)
      =(rho_*P^n) tensor I_0^m
      =(W_n tensor I_0^m)^directsum5.

The earlier actual evaluation injectivity gives H0(W_1 I_0^2)=H0(W_3 I_0^4)=0. The length of a double point on a smooth surface is3; the length of a fourth-order point is10. Since W_n has rank5 and no higher cohomology, the corresponding jet evaluations have defects

    h1(W_1 I_0^2)=5*3-4=11,
    h1(W_3 I_0^4)=5*10-36=14.

Their five copies recover the exact55 and70 dimensions. The vanishings of the section kernels are inherited from the actual beta geometry; they are not an assumption that these jets impose independent conditions.

## 4. The multiplier stays structured

The actual ambient quadric corresponds to

    q in H0(A,P^2 I_Sigma^2),   dimension15.

Multiplication by q gives

    rho_*P tensor I_0^2 -> rho_*P^3 tensor I_0^4.

After choosing the decompositions, this is a five-by-five block morphism

    (W_1 I_0^2)^directsum5 -> (W_3 I_0^4)^directsum5.

It is not generally diagonal and its blocks are not independently chosen. All blocks come from multiplication by the same q. On first cohomology it is the original55 -> 70 map, now displayed as linked14-by11 blocks.

One can quantify the constraint without evaluating any coefficients. Finite adjunction and the deck splitting give

    Hom_B(rho_*P,rho_*P^3 tensor I_0^2)
      = directsum_(g in G) H0(A,P^2 I_Sigma^2),

of dimension25*15=375. On the other hand its decomposition into five-by-five blocks is25 copies of H0(B,Hom(W_1,W_3) tensor I_0^2). Hence

    h0(B,Hom(W_1,W_3) tensor I_0^2)=15.

The multiplication-by-q family is a15-dimensional subspace of that375-dimensional entire block-morphism space. Replacing it by arbitrary blocks would discard the actual problem.

## 5. Descent warning

Theta does not descend as a line bundle through the degree25 quotient rho. Its commutator pairing on G is nondegenerate, so there is no G-linearization that would permit such descent. The vector-bundle pushforward and its matrix-algebra decomposition retain this noncommutativity rather than suppress it.

A maximal isotropic subgroup H of G has order5. Theta can descend through A -> A/H after choosing a splitting of the restricted theta extension; the descended polarization is principal because its Euler characteristic is5/5=1. That is a different degree-five route and does not justify descending Theta through all of G.

## Boundary

The one-point reduction supplies actual simple semihomogeneous bundles and the precise allowed multiplier family. No rank of the linked11-to14 blocks, the original55-to70 map, or the universal20-to20 boundary is asserted. A semihomogeneous decomposition of the source and target is not a simultaneous diagonalization of multiplication by a general quadric.

Dependencies: the two companion notes in this directory; the theta-group pairing and finite-etale identities are explicitly used above to prove the needed decomposition. No selected HM coefficients, arithmetic specialization, or numerical rank test occurs.
