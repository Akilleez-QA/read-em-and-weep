# Universal second-normal harmonic product and operator defect

## Result and strict scope

The canonical harmonic splitting has the second-normal multiplication formula

    L(p)L(r)=L(pr)+q L(B1(p,r))+q² L(B2(p,r)) mod q³,

where, for binary degrees 2m,2n,

    B1(p,r)=tau2(p,r)/[2(2m-1)(2n-1)(2m+2n-1)],
    B2(p,r)=tau4(p,r)/[8(2m-1)(2m-3)(2n-1)(2n-3)
                       (2m+2n-3)(2m+2n-5)].                 (1)

Set B1=0 if min(m,n)<1 and B2=0 if min(m,n)<2. These are all-degree representation identities, not actual-source evaluations. Section 2 gives the full second-normal operator error, including its mixed first-normal products. Section 3 identifies the precise tangency condition and distinguishes the new operator correction from the previous one.

THIS IS A UNIVERSAL LOCAL IDENTITY, NOT AN ACTUAL SECOND-NORMAL MIDPOINT LIFT. MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md proves that the midpoint bundle on 2Q has nonzero obstruction -c²/(4d) to extension to 3Q. Accordingly the coefficient s used below is a formal local input, not a globally available actual midpoint section. The first-normal actual Hessian identification does not license such a global s. No actual fourth value is claimed.

Dependencies: UNIVERSAL-FIRST-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-RESIDUE.md for the splitting and first-normal conventions, and the preceding midpoint nonextension theorem for the global limitation. The symbols c,d in that obstruction are the nonzero coefficients of its normal-obstruction polynomial, unrelated to the local coefficient names below.

## 1. All-degree proof of the second-normal product

Use q=xz-y², cone parametrization (x,y,z)=(X²,XY,Y²), and

    Delta=partial_x partial_z-(1/4)partial_y².

For an even binary form p of degree 2m, L(p) is its unique harmonic degree-m lift. For harmonic H_l of ternary degree l,

    Delta(q^r H_l)=r(l+r+1/2) q^(r-1) H_l.                  (2)

Harmonic decomposition and restriction therefore identify the coefficients of each q power uniquely. Write N=m+n. Applying Delta² to the product and restricting to q=0 kills its harmonic and q-harmonic terms, and kills the restrictions of every q^j term with j>=3. Its q² term is multiplied by

    Delta²(q² H_(N-4))=((2N-3)(2N-5)/2) H_(N-4).           (3)

The resulting equivariant bilinear map from Sym^(2m) tensor Sym^(2n) to Sym^(2N-8) is a multiple of the unique fourth-transvectant channel. Our convention is

    tau4(p,r)=sum_(i=0)^4 (-1)^i binom(4,i)
                (partial_X^(4-i) partial_Y^i p)
                (partial_X^i partial_Y^(4-i) r).

To fix its coefficient, use the universal highest/lowest vectors p=X^(2m), r=Y^(2n). Their harmonic lifts are x^m,z^n, and

    Delta²(x^m z^n)=m(m-1)n(n-1)x^(m-2)z^(n-2),
    tau4(X^(2m),Y^(2n))=(2m)_4(2n)_4 X^(2m-4)Y^(2n-4).

Dividing by (3) gives exactly (1). If either m or n is below two, the channel is absent and its transvectant is zero. This determines the complete bilinear map; it does not infer a nonzero composite from nonzero constituent maps. The monomials here fix an abstract representation identity and do not select any actual HM/source coefficients.

## 2. Full second-normal operator coefficient

Let the coefficients be functions of auxiliary base variables. Assume D preserves the harmonic splitting, and Dq=rho q with rho a base scalar, independent of the positive variables X,Y. This includes the negative-block derivation plus vertical Euler action used in the first-normal calculation. The base-scalar hypothesis permits rho to pass through L and Bj. Without it extra harmonic product terms are needed.

For matrix-valued binary forms define Bj by matrix multiplication with Bj on each scalar-entry pair. Thus

    [U,V]_j=Bj(U,V)-Bj(V,U),

with B0 ordinary matrix multiplication. Entries of different positive degrees are handled separately; no equal-degree matrix assumption is made. The scalar lambda below includes the chosen local determinant/line action, not merely the physical eigenvalue before that action is added.

Take the purely local formal data

    Ntilde=L(n)+q L(t)+q² L(s),
    O=L(H)D+ad_(L(A)+q L(K)+q² L(J)),
    Lambdatilde=L(lambda)+q L(lambda1)+q² L(lambda2).

The displayed symbol has no q-dependent correction. If such symbol corrections are present in a different ansatz, their contributions must also be included. Put

    E=O(Ntilde)-Lambdatilde Ntilde
      =L(R0)+q L(R1)+q² L(R2) mod q³.

Direct harmonic multiplication gives

    R0=H Dn+[A,n]-lambda n,

    R1=H Dt+(H rho-lambda)t+[A,t]+[K,n]-lambda1 n
         +B1(H,Dn)+[A,n]_1-B1(lambda,n),                  (4)

and the requested complete second coefficient is

    R2=H Ds+(2H rho-lambda)s+[A,s]+[K,t]+[J,n]
         -lambda1 t-lambda2 n
         +B1(H,Dt)+rho B1(H,t)+[A,t]_1+[K,n]_1
         -B1(lambda,t)-B1(lambda1,n)
         +B2(H,Dn)+[A,n]_2-B2(lambda,n).                 (5)

In particular the terms rho B1(H,t), [K,n]_1 and -B1(lambda1,n) cannot be omitted. There is no derivative of K or J here: they act by an adjoint connection, whereas D acts on Ntilde. Formula (5) follows by combining

    D(q L(t))=q L(Dt+rho t),
    D(q² L(s))=q² L(Ds+2rho s)

with (1) in every product. The verifier independently reconstructs the entire coefficient with ordered bilinear tags, retaining noncommutative matrix order and all q degrees.

In the earlier actual first-normal convention lambda=H rho-u. This turns the linear s coefficient into H rho+u, not u or 2u. That substitution is an identity about the cone/line convention only; it does not supply an actual s, K, J, lambda1, or lambda2 on 3Q.

## 3. Tangency is not automatic at the second division

Suppose, additionally and only locally, Ntilde²=0 mod q³ and R0=0. The derivation property gives

    Ntilde E+E Ntilde=O(Ntilde²)-2 Lambdatilde Ntilde²=0 mod q³.

Taking its first and second harmonic coefficients yields

    {n,R1}=0,
    {n,R2}+{t,R1}+B1(n,R1)+B1(R1,n)=0.                    (6)

Here braces are ordinary matrix anticommutators. Thus R2 is not generally tangent to the cone nilpotent n. The actual first error must be canceled as a cochain, or the extra terms in (6) must explicitly be carried. Vanishing of a cohomology class alone does not justify deleting them. If R1=0 as a cochain, (6) does imply {n,R2}=0.

For reference the same square-zero hypothesis itself requires all three equations

    n²=0,
    {n,t}+B1(n,n)=0,
    {n,s}+t²+B1(n,t)+B1(t,n)+B2(n,n)=0.                   (7)

The actual midpoint theorem supplies the first two but does not supply a globally compatible third equation on 3Q.

A related finite-gauge check is useful. If the full data are transported by T=1+q L(B)+O(q²), then E transforms by conjugation. With R0=0 its second coefficient changes as R2 -> R2+[B,R1]. This is another reason not to treat the second coefficient as intrinsically tangent before the first error is canceled. If R1=0, this particular normal-frame change leaves R2 unchanged.

## 4. Which operator-lift terms actually disappear

For the regular-pair nilpotent

    n=[[fg,-f²],[g²,-fg]],

assume n,t,s and A,K,J are trace-free. Only when the tangency condition of Section 3 is satisfied may the old canonical-module coordinate be taken as R2_11 modulo (f²,g²). The exact diagonal expression is

    R2_11=H D(s11)+(2H rho-lambda)s11+A12 s21-A21 s12
         +K12 t21-K21 t12+J12 g²+J21 f²
         -lambda1 t11-lambda2 fg
         +B1(H,D(t11))+rho B1(H,t11)
         +B1(A12,t21)-B1(A21,t12)
         +B1(K12,g²)+B1(K21,f²)
         -B1(lambda,t11)-B1(lambda1,fg)
         +B2(H,D(fg))+B2(A12,g²)+B2(A21,f²)
         -B2(lambda,fg).                                 (8)

The NEW q² connection J disappears modulo (f²,g²), by the explicit term J12 g²+J21 f². The PREVIOUS q connection K does not disappear from this expression: its retained terms are

    K12 t21-K21 t12+B1(K12,g²)+B1(K21,f²).                 (9)

No claim is made that their actual sum is nonzero; the point is that the first-normal elimination of [K,n] cannot eliminate (9). An actual next division needs its first-normal operator/frame comparison as well as the genuine corrected input. Nor may -lambda2 fg be dropped locally: the corresponding scalar-line term requires a compatible global comparison, exactly as at first order.

## 5. Physical equation units

For a physical equation q0=nu q with a base unit nu, the same expansion is written using

    B1,physical=B1/nu,   B2,physical=B2/nu²,
    t_physical=t/nu,   s_physical=s/nu²,
    K_physical=K/nu,   J_physical=J/nu²,
    lambda1,physical=lambda1/nu,   lambda2,physical=lambda2/nu²,
    rho_physical=rho+D(nu)/nu.

For example D(t/nu)+rho_physical t/nu=(Dt+rho t)/nu, and the analogous s expression has 2rho. Consequently R1,physical=R1/nu and R2,physical=R2/nu². Treating nu as constant is valid only in a frame where it is constant. This records the exact equation-line transport and prevents omission of its derivative terms.

## Reproduction and limits

Run python verify_second_normal_harmonic_product_and_defect.py. It checks all 735 pairs in COMPLETE abstract monomial bases for 0<=m,n<=4 and for (m,n)=(2,5),(5,2), the all-degree normalization identity, the free ordered-bilinear q² operator coefficient, the retained tangency terms, the generic regular-pair diagonal, and the physical equation-unit transport. It also checks that an abstract degree-(6,6) product has a nonzero next term, so the congruence is not silently promoted to an exact equality.

All source parameters remain unassigned. No actual-instance coefficient, matrix rank, or scan is used. The global midpoint obstruction is a cited proved theorem, not a conclusion of these local algebra tests. An actual next Bockstein calculation must use extendable actual endpoint data or another licensed global construction; this note does not extend the midpoint by notation.
