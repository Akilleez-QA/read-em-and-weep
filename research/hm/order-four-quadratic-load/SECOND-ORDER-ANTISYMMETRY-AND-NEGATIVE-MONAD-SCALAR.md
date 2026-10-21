# Antisymmetry of the first correction detects the negative monad scalar

## Results

Retain the actual canonical map zeta:A=Sym^2 W -> H1(B)_A, characterized by q0 zeta_a=a xi. There is a scalar c such that

    a zeta_b - b zeta_a = c (a cross b) xi.

The cross product is any fixed nonzero equivariant identification Lambda^2 A=A; changing its normalization rescales c but not its vanishing. The exact new equivalence is

    c=0  if and only if  dim H1(B(-2))^G=1.

Thus this first-correction antisymmetry detects the actual invariant monad differential left undecided in FIRST-NORMAL-NONUNIQUENESS-INDEPENDENT-MONAD-CHECK.md. Neither side is selected here. The S4 leg of negative-linear multiplication of zeta(A) is nonzero regardless of c.

## 1. Antisymmetry and its linear interpretation

Multiplying a zeta_b-b zeta_a by q0 gives zero by associativity. The actual positive kernel of q0:H1(B(2))->H1(B(4)) is (A+D5)xi. Since Lambda^2 A=A and Hom_G(A,D5)=0, equivariance proves the displayed identity.

For a=u^2,b=uv in binary coordinates, the cross product is a nonzero scalar multiple of u^2. The identity becomes

    u (u zeta_uv - v zeta_u2) = c' u^2 xi.

Uniform H0(B_Hu(2))=0 makes u:H1(B(1))->H1(B(2)) injective, hence

    u zeta_uv - v zeta_u2 = c' u xi.

This describes exactly the W summand of W tensor A=W+S4. The ambient H1(B(1)) has a unique W, namely Wxi. Its S4 component on W tensor zeta(A) cannot vanish: otherwise, for fixed u, the injective three-dimensional map zeta(A)->H1(B(1)) would factor through a two-dimensional W. This uses uniform H0(B_Hu(1))=0.

## 2. Koszul division used in the implication c=0

Write M_j=H1(B(j)). The negative coordinates u,v cut the positive plane R. Splitting their Koszul complex into two exact sequences shows that, if H0(B_R(t))=0, then every pair x,y in M_(t-1) with vx=uy is of the form (u omega,v omega) for some omega in M_(t-2). Indeed H1(I_R B(t))->H1(B(t)) is injective under this H0 vanishing, and the first Koszul sequence is exact at M_(t-1)^2. If also H0(B(t))=0, the resulting omega is unique.

Both requirements hold for t=1 and t=0: ambient adjoint sections vanish, the plane is stable so H0(B_R)=0, and the plane Steiner calculation gives H0(B_R(1))=0. No H1 boundary is discarded in this division statement.

If c=0, the first section gives

    v zeta_u2 = u zeta_uv,
    v zeta_uv = u zeta_v2.

Apply the t=1 division twice to obtain unique eta_u,eta_v in M_-1 with

    (u eta_u,v eta_u)=(zeta_u2,zeta_uv),
    (u eta_v,v eta_v)=(zeta_uv,zeta_v2).

Then v eta_u=u eta_v, so t=0 division gives unique omega in M_-2 with u omega=eta_u and v omega=eta_v. Consequently a omega=zeta_a for every a in Sym^2 W. Uniqueness makes omega G-invariant, since zeta is equivariant. It is nonzero because zeta is nonzero. The independently computed bound dim M_-2^G in {0,1} therefore gives dimension one.

## 3. Converse and normalization

Suppose omega is a nonzero invariant class in M_-2. The invariant-cone rank33 closure implies H0(B_Q0)_+=0: multiplying a hypothetical section by a nonzero positive quartic puts it in the known positive twist-four centralizer, so it centralizes N; the no-divisorial-zero centralizer description would make it N times a section of O_Q0(-2), which is zero.

Therefore q0:M_-2^G -> M_0^G is injective. Since M_0^G=Cxi, normalize omega so q0 omega=xi. Then q0(a omega)=a xi=q0 zeta_a. Both a omega and zeta_a belong to the A summand of M_0, where q0 is injective, so a omega=zeta_a. Associativity now gives a zeta_b=b zeta_a, proving c=0.

## 4. What is still undecided

The lower second obstruction is theta_a=-[a zeta_a] in coker(q0:M_0,+->M_2,+)=V+3P4+3D5. Its quadratic dependence on a factors through Sym^2 A=1+D5, so it lies in the three-copy D5 part. The preceding nonzero S4 leg does not exclude alignment of its D5 image with q0(M_0,D5), and neither this note nor the monad calculation decides theta_a.

This is a link between two actual remaining scalar questions, not a generic-multiplicity inference and not a proof of positive maximal rank.
