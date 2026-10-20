# Independent review: literal invariant descent lifting

## Verdict

The missing bridge can be proved directly, without an equivariant representative-selection theorem. For the commutative classical algebra O_X, on the same finite inversion-stable affine cover, normalized polydifferential products and differential gluing maps with unrestricted higher coefficients admit the required literal invariant lifting whenever the invariant total obstruction cohomology vanishes. In particular, the stated HH³(X)^inversion = 0 supplies formal extensions of the invariant PR16 two-jet, preserving that two-jet literally. This does not fix the higher local product to Moyal, extend a module, or evaluate a bundle obstruction.

The proof below is universal algebra only. No actual model, jet, source evaluation, matrix product, experiment, or external posting was performed. Inputs read: [REVIEW.md](../historical-invariant-review/REVIEW.md) and https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md. The signs were derived independently and agree with the companion lemma.

## Setup and signs

Let R'=C[h]/(h^(N+1)), R=C[h]/(h^N), and t=h^N, with N>=1. Thus h t=t²=0. Start with unital differential descent data over R, reducing to ordinary commutative multiplication, identity overlap maps, and triple unit 1 modulo h. Lift coefficients arbitrarily to R', preserving units and normalization. Denote the lifted product on chart i by *, the lifted overlap map by F_ij, and the lifted triple unit by A_ijk. Products below are in the indicated target chart. All four defects lie in t times the classical cochain spaces:

S_i(x,y,z)=(x*y)*z-x*(y*z),
H_ij(x,y)=F_ij(x*_j y)-F_ij(x)*_i F_ij(y),
K_ijk(x)=F_ij F_jk(x)*_i A_ijk-A_ijk*_i F_ik(x),
P_ijkl=A_ijk*_i A_ikl-F_ij(A_jkl)*_i A_ijl.

Identify t-valued defects with their classical coefficient cochains. Write b for the usual Hochschild differential, including b a(x)=x a-a x for a zero-argument cochain. Use D=δ+(-1)^p b on Čech degree p. The obstruction is

O=(-S,H,K,-P)

in bidegrees (0,2),(1,1),(2,0),(3,-1) of the shifted Hochschild complex. The zero-argument cochains MUST be retained. For O to be a cocycle the identities are

bS=0,
δS+bH=0,
δH+bK=0,
δK+bP=0,
δP=0.

Here bP=0 because the classical algebra is commutative. Its vanishing is not permission to remove the zero-argument term: P and its Čech primitive are essential.

## Crucial normalization observation

S, H, and K are normalized: they vanish when an argument is the strict unit. Since they are t-valued, they also vanish when that argument is any element 1+h u. Consequently every near-identity element is in the nucleus of the possibly nonassociative lifted product: all its associators with arbitrary arguments vanish. The near-identity elements form an associative group under *, with their usual finite h-adic inverse. Reassociation involving such an element is legitimate, even though associativity on arbitrary arguments has not yet been repaired.

Likewise H(g,x)=H(x,g)=0 whenever g=1+O(h), so F is multiplicative when at least one input is a near-identity element. Also K(g)=0 on near-identity elements. Thus F restricts to a group homomorphism on these unit groups, and its triple-inner equation holds exactly on them. These observations justify every reassociation and unit substitution below; one must not assume the arbitrary lifts are already associative.

## Coherence checks

### Local associativity

For any product, its associator satisfies the exact telescoping identity

S(x*y,z,w)-S(x,y*z,w)+S(x,y,z*w)
 =S(x,y,z)*w+x*S(y,z,w).

All S terms are t-valued, so products and substitutions outside them can be reduced to ordinary multiplication. This is precisely bS=0.

### Overlap associativity

Expanding F(S_j(x,y,z)) using the definition of H twice gives

F(S_j(x,y,z))-S_i(Fx,Fy,Fz)
 =H(x,y)*Fz+H(x*y,z)-Fx*H(y,z)-H(x,y*z).

Modulo the small-extension annihilator, the right side is -bH. The left side is S_j-S_i. Hence δS+bH=0.

### Triple multiplicativity

Write I_A(x)=A*x*A^(-1). By the nucleus observation it is an exact automorphism of the lifted product, and F I_A=I_F(A) F. The inverse-free K equation gives

F_ij F_jk=I_Aijk F_ik+K_ijk,

because multiplying a t-valued K by A^(-1)=1+O(h) leaves it unchanged. The multiplicativity defect of F_ij F_jk is H_ij+H_jk, after taking coefficients. That of I_Aijk F_ik is H_ik. Adding a t-valued linear operator K to a map equal to identity modulo h changes its multiplicativity defect by -bK. Therefore

H_ij+H_jk-H_ik=-bK_ijk,

which is δH+bK=0.

### Quadruple comparison of compositions

Compare (F_ij F_jk)F_kl with F_ij(F_jk F_kl). Their inner-map parts are respectively

I_(Aijk*Aikl) F_il,
I_(Fij(Ajkl)*Aijl) F_il.

Their additive errors are respectively K_ijk+K_ikl and K_jkl+K_ijl. The two inner units differ by tP. Since tP commutes with every element in the commutative classical reduction, their inner maps are identical. Thus

K_jkl-K_ikl+K_ijl-K_ijk=0.

This is δK+bP=0 in this problem, because bP=0. The argument uses commutativity exactly here; no claim about a general noncommutative classical algebra is needed.

### Five-index pentagon

Use indices 0,1,2,3,4 and abbreviate A_ijk by a_ijk. All products in this paragraph are unambiguously associative by the nucleus observation. The defect equation is

a_ijk a_ikl=F_ij(a_jkl) a_ijl+tP_ijkl.

Compute W=a_012 a_023 a_034. Applying this equation first on 0234 gives

W=a_012 F_02(a_234) a_024+tP_0234.

Applying it instead on 0123, then 0134, then 1234 inside F_01 gives

W=F_01 F_12(a_234) F_01(a_124) a_014
  +t(P_0123+P_0134+P_1234).

The triple-inner equation is exact on the unit a_234, so substitute

F_01 F_12(a_234)=a_012 F_02(a_234) a_012^(-1).

The equation on 0124 then gives

W=a_012 F_02(a_234) a_024
  +t(P_0123+P_0134+P_1234-P_0124).

Comparing the two formulas proves

P_1234-P_0234+P_0134-P_0124+P_0123=0,

exactly δP=0. Multiplication or application of F to any tP coefficient has reduced to the identity, since h t=0.

## Corrections and literal lifting

Change the lifted coefficients by

μ_i -> μ_i+t u_i,
F_ij -> F_ij+t v_ij,
A_ijk -> A_ijk+t a_ijk,

where u,v are normalized polydifferential/differential cochains and a is a function. Direct expansion gives

ΔS=-b u,
ΔH=δu-bv,
ΔK=δv+b a,
ΔP=-δa.

In this commutative reduction b a=0; the displayed sign follows directly from x a-a x in the inverse-free K definition. Consequently ΔO=D(u,v,a). The defect class is independent of the arbitrary lift. A primitive D(u,v,a)=-O supplies corrected exact descent data over R' with literally unchanged reduction over R.

Every construction is natural under cover-preserving automorphisms. If the given descent data are invariant under an involution fixing h, choose an invariant coefficient lift (for example the zero new coefficient). Its defect is invariant. In characteristic zero, the Reynolds projector commutes with D, so vanishing of H²(Tot)^inversion supplies an invariant primitive by averaging the primitive of the linear correction equation. There is no averaging of a nonlinear solution.

## Geometric hypotheses and scope

On a separated smooth scheme with the specified finite affine cover and affine intersections, the normalized polydifferential Hochschild sheaves compute the relevant Hochschild hypercohomology. The shifted total degree two is HH³(X). Polynomial-order differential operator pieces are quasi-coherent and affine-acyclic, and filtered unions retain the needed affine acyclicity; hence the same affine Čech cover computes this cohomology. HKR is natural for inversion. On the stated abelian fourfold, the HKR summand H^q(X,Λ^p T_X), p+q=3, has inversion sign (-1)^(p+q)=-1, so the invariant obstruction group vanishes.

Composition, restriction, and finite products of differential operators remain differential; each coefficient produced remains regular on its designated affine intersection. No change of cover is needed. Arbitrary differential coefficients can be corrected in this same complex. Normalization keeps the strict unit fixed. The near-identity overlap maps are invertible h-adically with differential coefficients; triple elements remain invertible. Ordered Čech descent data suffice; inverse/degenerate data can be recovered consistently if that presentation is desired.

Starting with the supplied invariant order-two data over C[h]/(h³), apply the lemma with N=3,4,... and take compatible coefficientwise inverse limits. This produces literal formal descent data on the same cover with the same μ,F,A coefficients through h². All higher local products, overlap maps, and triple units may change. No fixed-all-order-Moyal assertion follows, and no statement about existence of a compatible bundle/module follows.
