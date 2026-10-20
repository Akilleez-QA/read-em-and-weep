# Literal small-extension descent: complete sign-checked proof

## Scope and hypotheses

This is a universal formal-algebra proof. No geometric source/owner/jet evaluations, matrix products, repository execution, production imports, or obstruction-coordinate computations are involved.

Let k have characteristic zero, let B be a sheaf of unital k-algebras on a cover, and use a fixed ordering of the cover indices. In the intended application B=O_X with ordinary multiplication. Restrict all expressions to the indicated intersections. Write

R'=k[h]/(h^(n+2)), R=k[h]/(h^(n+1)), I=(h^(n+1)) in R', n>=0.

Thus I^2=hI=0. The argument also works for a local Artin small extension whose kernel is annihilated by the maximal ideal. Suppose given unital descent data over R reducing modulo h to the literal data (ordinary product, identity maps, unit 1):

- products μ_i;
- overlap maps F_ij from chart j to chart i;
- triple elements A_ijk;
- F_ij F_jk=Ad(A_ijk)F_ik;
- A_ijk A_ikl=F_ij(A_jkl) A_ijl.

Choose arbitrary coefficientwise lifts to R', still unital, with normalized positive-arity deformation coefficients. Products of elements on chart i use the lifted μ_i, even before associativity is established. The lifts of F are invertible linear maps because F=id modulo h. We deliberately avoid defining conjugation using a possibly nonassociative lifted product.

Every defect below is I-valued. I-valued operations are canonically operations on B with coefficients in I: any multiplication, restriction, or F acting on such a value reduces to its classical operation. In particular h times any defect is zero.

## Complex and signs

Let C^r be normalized Hochschild cochains of arity r, including C^0=B. Set D^q=C^(q+1), q>=-1. Use the usual Hochschild differential

(bc)(x_1,...,x_(r+1)) = x_1 c(x_2,...,x_(r+1))
 + sum_(t=1)^r (-1)^t c(x_1,...,x_t x_(t+1),...,x_(r+1))
 + (-1)^(r+1)c(x_1,...,x_r)x_(r+1).

In particular (ba)(x)=xa-ax. The Čech differential is the alternating deletion differential δ. Set d=δ+(-1)^p b on Čech degree p. This is a complex because restrictions commute with b. No bracket or DGLA structure on this ordinary total complex is asserted or used.

Define raw defects:

S_i(x,y,z)=(x μ_i y) μ_i z - x μ_i (y μ_i z).

H_ij(x,y)=F_ij(x μ_j y)-F_ij(x) μ_i F_ij(y).

K_ijk(x)=(F_ij F_jk(x)) μ_i A_ijk - A_ijk μ_i F_ik(x).

P_ijkl=A_ijk μ_i A_ikl - F_ij(A_jkl) μ_i A_ijl.

The obstruction cochain is

O=(-S,H,K,-P)

in bidegrees (0,2),(1,1),(2,0),(3,-1), hence total degree 2, with coefficients in I. The inverse-free K is equivalent to the prescribed inner-gluing equation once associativity holds and A is a unit.

## Basic reduction rule

S is zero if any argument is 1; H is zero if either argument is 1; K(1)=0. This follows directly from unitality of the lifts. Since S,H,K are I-valued and hI=0, the same assertions hold with 1 replaced by any A=1 modulo h. Consequently:

1. Any reassociation with an A among the three entries produces zero error.
2. F(Ax)=F(A)F(x) and F(xA)=F(x)F(A), exactly in R'.
3. K(A)=0.
4. Factors equal to 1 modulo h and maps equal to id modulo h can be erased when acting on any defect.

These statements also hold for products of the A's and for their images under F, since those elements are again 1 modulo h. This rule justifies every reassociation and transport below; it does not assume that the arbitrary lifted products are associative or that the lifted F's are homomorphisms.

## Five coherence identities

All the following identities are exact in I, with b formed using the classical product:

bS=0,
δS+bH=0,
δH+bK=0,
δK+bP=0,
δP=0.

They imply dO=0 with precisely the signs declared above.

### 1. Associativity coherence

For any unital bilinear product, without assuming associativity, expand

x S(y,z,w)-S(xy,z,w)+S(x,yz,w)-S(x,y,zw)+S(x,y,z)w.

Each of the ten resulting parenthesized terms cancels with one other term. Thus this expression is identically zero. Since S is I-valued, replacing the surrounding lifted products by the classical products gives bS=0.

### 2. Homomorphism versus associativity

Write F=F_ij. Expanding the definition of H twice gives

F(S_j(x,y,z))-S_i(Fx,Fy,Fz)
 =H(x,y)Fz-Fx H(y,z)+H(xy,z)-H(x,yz).

Here xy and yz on the right are chart-j products. Reduction on defect values identifies the left side with S_j-S_i=δS and the right side with -bH. Thus δS+bH=0.

### 3. Inner gluing versus homomorphism

On a triple set G=F_ij F_jk, Q=F_ik, A=A_ijk. Let H_G and H_Q denote their homomorphism defects. Direct expansion of a composite map gives

H_G=H_ij+H_jk, H_Q=H_ik

as I-valued bilinear cochains (all transported arguments reduce to their classical values).

By definition G(x)A=AQ(x)+K(x). The basic reduction rule permits reassociation through A. Compute the difference of homomorphism defects, with A on the appropriate side:

H_G(x,y)A-A H_Q(x,y)
 =K(xy)-G(x)K(y)-K(x)Q(y).

For clarity, this follows by substituting G(xy)A=AQ(xy)+K(xy) and

(Gx Gy)A=A(Qx Qy)+K(x)Qy+Gx K(y).

After reduction on I this says δH=-bK. Hence δH+bK=0.

### 4. Pentagon defect versus inner gluing

Use indices 0,1,2,3, and set

G=F_01 F_12 F_23, V=F_03,
B=A_012 A_023, C=F_01(A_123) A_013, P=B-C.

Two applications of the K relation give

G(x)B=B V(x)+K_012(x)+K_023(x),
G(x)C=C V(x)+K_123(x)+K_013(x).

For the second equation, first transport the K_123 relation through F_01 and then apply K_013. Transport has no H error because the other factors are 1 modulo h. The first equation applies K_012 to F_23(x), then K_023; evaluating K on F_23(x) equals evaluating it on x.

Subtracting yields

G(x)P-P V(x)=K_012(x)+K_023(x)-K_123(x)-K_013(x)=-δK(x).

The left side is xP-Px=(bP)(x). Therefore δK+bP=0. For a commutative classical B, bP=0, so δK=0, but retaining bP displays the correct arity-zero term and convention.

### 5. Coherence on five indices

Use indices 0,1,2,3,4. Compare the two expansions of

L=A_012 A_023 A_034

toward

M=F_01 F_12(A_234) F_01(A_124) A_014.

Products in these displays can be parenthesized arbitrarily: all elements are 1 modulo h, so the basic rule applies.

First route, applying P_0123, P_0134, then F_01(P_1234):

L = F_01(A_123) A_013 A_034 + P_0123
  = F_01(A_123) F_01(A_134) A_014 + P_0134+P_0123
  = M + P_1234+P_0134+P_0123.

Second route, applying P_0234 then P_0124:

L = A_012 F_02(A_234) A_024 + P_0234
  = F_01 F_12(A_234) A_012 A_024 + P_0234
  = M + P_0124+P_0234.

The middle equality uses K_012(A_234)=0, rather than assuming inner gluing for arbitrary arguments. Comparing routes gives

P_1234-P_0234+P_0134-P_0124+P_0123=0,

which is exactly δP=0.

## Change of lifts and the total coboundary

Change the lifts by I-valued normalized operations

μ_i -> μ_i+u_i, F_ij -> F_ij+v_ij, A_ijk -> A_ijk+a_ijk.

Because I^2=hI=0, every changed expression is linear in the new operations and all other factors reduce to their classical values. Expanding directly gives

ΔS=-bu,
ΔH=δu-bv,
ΔK=δv+ba,
ΔP=-δa.

For example, the a contribution to K(x) is xa-ax, and the a contribution to P_ijkl is a_ijk+a_ikl-a_jkl-a_ijl. Hence

ΔO=(bu,δu-bv,δv+ba,δa)=d(u,v,a).

Thus O is a cocycle; its class is independent of the arbitrary coefficientwise lift; and a lift satisfying every descent equation exists exactly when [O]=0. If d(u,v,a)=-O, the modified lifts satisfy S=H=K=P=0 and retain the original data literally modulo h^(n+1).

Once S=0 the products are associative and unital. Since A=1 modulo h, its inverse exists by the finite geometric series in this nilpotent setting. Thus K=0 is equivalent to F_ij F_jk=Ad(A_ijk)F_ik, and P=0 is exactly the PR16 pentagon equation. The linear inverse of F exists because F=id modulo h, so H=0 makes F an algebra isomorphism. No gauge or change of presentation has been made.

## Differential, equivariant, and formal versions

If coefficients are algebraic polydifferential cochains, every defect above remains polydifferential: restriction, composition, and products of differential operators preserve that property. The normalized complex includes arity zero without truncation. The proof takes place on each designated intersection and never changes the cover.

All constructions are natural under cover-preserving automorphisms, including an involution fixing h. For a finite group in characteristic zero, start with an invariant coefficientwise lift. If the invariant part of total H^2 vanishes, the invariant cocycle O has a primitive; averaging that primitive gives an invariant solution to d(u,v,a)=-O. Only this linear correction is averaged, not a nonlinear solution.

Induction over n therefore extends any supplied strictly invariant finite-order literal descent presentation whenever the invariant total H^2 vanishes. The corrections begin at the first unspecified order. Taking coefficientwise inverse limits produces h-adic products, overlap isomorphisms, and triple units with exactly the supplied truncation. In particular, assuming the HKR/cohomology and invariant two-jet inputs in the reviewed note, this supplies its missing literal small-extension bridge for the full ambient differential algebroid problem. It proves neither extension with a frozen all-order local product nor quantization of any module or bundle.

## Application: the invariant ambient presentation on C^4

Here C denotes the elliptic curve, so X=C^4 is an abelian fourfold, not affine four-space. Take the finite product affine cover in the reviewed PR16 presentation, preserved memberwise by diagonal inversion ι. For normalized algebraic polydifferential cochains including arity zero, algebraic HKR and affine Čech computation identify

H^2(Tot Čech(D)) = direct_sum_(p+q=3) H^q(X, Λ^p T_X).

The ordinary unshifted Hochschild degree is p+q=3; the displayed total complex is shifted by one. This is a cohomology statement for ambient cochains, not Hochschild cohomology of the quotient stack.

On an abelian fourfold T_X is trivial. Inversion acts by -1 on invariant vector fields and by (-1)^q on H^q(O_X), hence by (-1)^(p+q)=-1 on every summand above. Consequently H^2(Tot Čech(D))^ι=0. Exactness of averaging in characteristic zero identifies this with H^2 of the invariant subcomplex. No Lie-formality theorem is needed.

For the actual supplied PR16 two-jet, diagonal inversion makes q_r and V_r odd and a_r even. The scalar b is a sum of products of two q's and is even. Every term of T contains one q and one V and is even. The Moyal coefficients are invariant because the underlying bivector is invariant. Thus μ through h^2, F=id+h^2 T, and A=1+h b+h^2 b^2/2 are literally invariant. Assume these stated two-jet descent identities, proved in PR16; they are the input finite-order solution, rather than a newly executed evaluation here.

Applying the lemma inductively, beginning with the extension k[h]/h^4 -> k[h]/h^3, gives invariant μ,F,A to every order with exactly these coefficients through h^2. Higher coefficients of all three kinds are free to vary. This is an unconditional ambient-extension implication from the stated geometric/HKR and verified formal two-jet hypotheses: it no longer requires an unproved relative comparison or a strictly invariant MC representative.

No premise about a bundle E, its first-order lift, its finite RHom model, or any imported bundle obstruction assertion is used. The ambient theorem remains separate from all such assertions. It does not establish a fixed all-order Moyal extension, quantization of E, or any value of an obstruction coordinate.

### Source provenance

- PR16 input, pinned at c8aec970fd65a105f39f4e8aeb8a17f0f0053f89, Sections 1–3: https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md . The proof above uses the locally supplied source copy and the review's pinned provenance; it does not claim a new remote-head verification.
- Prior independent review input: [REVIEW.md](../historical-invariant-review/REVIEW.md). This supplies the established HKR/involution calculation and identifies the literal-lifting gap closed here.
- Yekutieli, *Twisted Deformation Quantization of Algebraic Varieties*, https://arxiv.org/abs/0905.0488 : contextual reference for algebraic normalized differential cochains and geometric descent. Its gauge-class comparison is not substituted for the literal proof above.
- D'Agnolo–Schapira, *Quantization of complex Lagrangian submanifolds*, Section 3, https://arxiv.org/abs/math/0506064 : reference for the declared descent orientation. No Lagrangian existence theorem is invoked.

The five coherence identities and coboundary formulas in this artifact have been proved directly, not inferred from the comparison references.
