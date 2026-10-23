# The universal hidden-symbol cokernel, reduced discriminant scheme and kernel bundle

## Theorem and boundary

Work over C and assume the two P-surplus Type II hypotheses of PR965.
Restrict to the scalar alternative lambda·mu≠0 in that theorem. This
assumption is NOT a determination of the actual scalar mu. On
P=P(Sym²W)≅P², let the universal internal first symbol be

    Phi:(A⊕D)⊗O_P(-1)→D⊗O_P,
    Phi_a(k,h)=lambda·ak+mu·{a,h}_1,
    A=Sym²W, D=Sym⁴W.                                     (1)

Let C⊂P be the smooth discriminant conic and i its inclusion. Then:

1. The maximal-minor degeneracy subscheme in P is the REDUCED conic C.
2. There is an exact sequence

       0→K→8O_P(-1) --Phi--> 5O_P→i_*O_C(2)→0,           (2)

   where K is a rank-three vector bundle.
3. With H=c1(O_P(1)),

       [K]=8[O_P(-1)]-6[O_P]+[O_P(2)],
       c1(K)=-6H,  c2(K)=12H².                           (3)

4. Let nu:P(W)≅P¹→C, [l]↦[l²]. The kernel of the RESTRICTED
   map nu*Phi has rank four and is Sym³W⊗O_P¹(-3), whereas

       nu*K ≅ Sym²W⊗O_P¹(-4).                           (4)

   They fit into the nontrivial exact sequence

       0→nu*K→Sym³W⊗O(-3)→O→0.                          (5)

The right map is a nonzero scalar multiple of complete cubic evaluation.
Its target is Tor_1^P(i_*O_C(2),O_C), not an extra summand of K|C.

There is also an exact homogeneous ideal statement. Write
R=C[alpha,beta,gamma], a=alpha x²+beta xy+gamma y²,
Delta=beta²-4alpha gamma and m=(alpha,beta,gamma). Then

       I_5(Phi)=Delta·m³.                               (6)

Here lambda,mu are fixed nonzero complex scalars. Thus the SATURATED
projective ideal is (Delta); the raw affine ideal is not (Delta) and
retains additional structure at the cone vertex. Statement 1 is about
the projective degeneracy scheme, not a false global affine equality.

These statements concern the universal model of an internal first
symbol, not the original multiplication map or its original first
Bockstein. They select no actual coefficient or direction, prove no
actual occurrence of mu≠0, and exclude no source or catalogue pair.

## 1. Exact dependency and universal-model scope

The sole direct mathematical input is PR965, commit
de8e1d1a90d6f41dffa74df7cc7220c4e84bf4e7,
research/hm/source126-typeII-internal-discriminant/PROOF.md in
Akilleez-QA/read-em-and-weep. INPUTS.json records its exact Git blob
and SHA256; inputs/965.md is its authenticated content.

That theorem proves the actual internal symbol equals (1), with
lambda≠0, because its two equivariant Hom spaces have dimension one.
It proves rank four at nonzero squares and rank five at nonsquares
when mu≠0. In the chosen binary-form identifications, the expression
is SL2-equivariant. No SL2 action on the actual HM module is assumed.
All rank, scheme, and sheaf arguments below concern this forced
universal expression, under the explicit mu≠0 alternative.

Scaling the A and D domain factors by lambda and mu is an invertible
constant equivariant automorphism. Consequently cokernel, kernel
isomorphism class and determinantal ideal may be computed with
lambda=mu=1. This is normalization by an isomorphism, not evaluation
or selection of actual geometric coefficients.

## 2. A transverse derivative gives multiplicity one

At the square a=x², the image in D is x·Sym³W, of dimension four.
Consider the universal transverse family a_gamma=x²+gamma y² and
choose the domain vector

    k=y²,  h=-lambda/(6mu)·xy³.

At gamma=0 its image is zero, since {x²,xy³}_1=6x²y².
Differentiation of the UNIVERSAL polynomial expression in gamma gives

    lambda y² k + mu {y²,h}_1 = (4lambda/3)y⁴.           (7)

The class of (7) in D/(x·Sym³W) is nonzero. Also
Delta(a_gamma)=-4gamma, so this is a genuine normal derivative to C.
No actual parameter or bundle derivative is evaluated here.

At any point of C a 4×4 minor is a unit. Elementary row and column
operations over its local ring put Phi in block form diag(I_4,v),
where v is a 1×4 row of functions. Its entries vanish on C because
the fiber rank is four everywhere on C, so each is divisible by a
local equation t for the reduced smooth conic. Equation (7) says
that at [x²] at least one entry of v/t is a unit. The SL2 action is
transitive on C and the universal expression is equivariant, so the
same holds at every point. Further column operations give the local
normal form

       diag(I_4,t,0,0,0).                               (8)

The notation denotes a 5×8 matrix: four identity pivots, one t pivot
and three zero columns. Hence its maximal-minor ideal sheaf is (t),
its cokernel is locally O/(t), and its kernel is free of rank three.
Off C the map is surjective with locally free rank-three kernel.
This proves reducedness and local freeness asserted above.

In particular (8) rules out a thicker cokernel supported on C: the
cokernel is annihilated by the ideal of C itself, not only by a power.
Thus it is i_*L for a line bundle L on C.

## 3. Exact homogeneous determinantal ideal

For completeness we prove the stronger affine-coordinate statement (6),
which also distinguishes saturation from the raw ideal. Use the column
order

    A: x²,xy,y²;   D: x⁴,x³y,x²y²,xy³,y⁴,

and output order x⁴,x³y,x²y²,xy³,y⁴. Every 5×5 minor is homogeneous of
degree five. It vanishes along the irreducible quadratic Delta=0 by
the square rank theorem, so is Delta times a cubic. Therefore
I_5(Phi)⊂Delta m³ in the normalized lambda=mu=1 coordinates.

Ten minors, namely columns (0,1,2,p,q) for 3≤p<q≤7, have the following
quotients by Delta, all with the common factor 16 omitted:

    (p,q)     quotient /16
    (3,4)     -gamma³
    (3,5)      beta gamma²
    (3,6)      gamma(alpha gamma-beta²)
    (3,7)     -beta(2alpha gamma-beta²)
    (4,5)     -alpha gamma²
    (4,6)      alpha beta gamma
    (4,7)      alpha(alpha gamma-beta²)
    (5,6)     -alpha² gamma
    (5,7)      alpha² beta
    (6,7)     -alpha³.

These span all cubic monomials: the displayed pure and mixed terms
give gamma³,beta gamma²,alpha gamma²,alpha beta gamma,alpha² gamma,
alpha² beta,alpha³ directly; subtracting their multiples from the
remaining three gives beta²gamma,beta³,alpha beta². Thus their span
is R_3 and their ideal is m³. This proves the reverse inclusion and
(6). The coefficient-matrix determinant in the verifier's stated
monomial order is 2^40; no rank of an actual geometric matrix is used.

Restoring nonzero lambda,mu multiplies each chosen minor by the same
unit lambda³mu². Invertible column rescaling preserves the full minor
ideal, so (6) holds for every allowed pair of scalars.

## 4. Identify the cokernel line and its twist

Pull back along the Veronese parametrization nu:[l]↦[l²]. The rank-four
image is l·Sym³W⊂Sym⁴W at every l. Globally it is the image of

    Sym³W⊗O_P¹(-1)→Sym⁴W⊗O_P¹,

induced by the tautological inclusion O(-1)⊂W⊗O. This is an injective
bundle map, since multiplication by any nonzero l is injective. Its
quotient is Sym⁴(W/O(-1))=O_P¹(4), because det W is trivial and the
quotient line W/O(-1) is O(1). Therefore

    nu*L=O_P¹(4).

As nu identifies P¹ with C and nu*O_C(1)=O_P¹(2), it follows that
L=O_C(2). This proves the cokernel term in (2), including its twist.
The identification uses the actual image bundle of the universal
expression, not only its fiber dimension.

## 5. Ambient kernel class and Chern classes

The conic's standard divisor sequence, twisted by two, is

    0→O_P --Delta--> O_P(2)→i_*O_C(2)→0.

Combining its K-class with (2) gives (3). Equivalently,

    ch(K)=8e^(-H)-6+e^(2H)=3-6H+6H².

Since ch_2=(c1²-2c2)/2, c2=(36-12)H²/2=12H².
Rank-three local freeness was proved using (8), not inferred from
this virtual class alone.

## 6. Kernel of restriction and the Tor correction

On C, put a=l². The identity {l²,h}_1=2l{l,h}_1 shows that
Phi_a(k,h)=0 is equivalent to

    lambda·l k + 2mu·{l,h}_1=0.                         (9)

For l=x this says that ∂_y h is divisible by x, so h is divisible by x;
SL2 covariance gives h=l r for a unique r∈Sym³W. Then
{l,lr}_1=l{l,r}_1, and (9) forces

    k=-(2mu/lambda){l,r}_1,  h=l r.                    (10)

The map from r to the pair is linear in the tautological l. Thus the
UNTWISTED kernel family inside (A⊕D)⊗O_P¹ is Sym³W⊗O(-1).
The actual restricted domain in (1) has the additional twist
nu*O_P(-1)=O_P¹(-2). Therefore

    ker(nu*Phi)=Sym³W⊗O_P¹(-3).                         (11)

It is not nu*K: fiberwise rank jumps on C. The exact sequence with
Tor is

    0→nu*K→ker(nu*Phi)→nu*Tor_1^P(i_*L,O_C)→0.          (12)

One can obtain (12) either from the local form (8), or by tensoring
the two short exact sequences through im Phi. In the latter argument,
im Phi is locally free by (8), so K|C embeds in the kernel of restriction;
the remaining term is exactly Tor_1 of the cokernel. For a Cartier
divisor it equals L⊗O_C(-C). Here L=O_C(2) and O_C(-C)=O_C(-2), so
its pullback is O_P¹. This proves the target and ranks in (5).

We identify the right map, not just its line-bundle degree. Take l=x
and the kernel pair (10) with r=y³. Differentiating along
x²+gamma y² yields -8mu·y⁴ modulo x·Sym³W, nonzero. This is the local
Tor boundary (up to the common nonzero normal-coordinate factor).
The construction is SL2-equivariant. The space of equivariant maps
Sym³W⊗O(-3)→O is one-dimensional, since it is the invariant line in
(Sym³W)*⊗H0(O(3)). Its nonzero representative is complete cubic
evaluation via W→W/O(-1). Consequently the map in (12) is a nonzero
scalar multiple of that evaluation.

The ordinary degree-three evaluation sequence on P¹, twisted by -3,
is

    0→Sym²W⊗O(-4) --multiply by l--> Sym³W⊗O(-3)
      →O→0.

It identifies its kernel with nu*K and proves (4). The degrees check:
deg(nu*K)=3(-4)=-12 equals 2c1(K), while the rank-four kernel (11)
also has degree -12 but one additional rank. Neither can be substituted
for the other merely from their equal total degree.

## 7. Verification and limits

The bounded verifier checks the universal 5×8 polynomial matrix,
all 56 maximal minors, the ten-minor cubic spanning certificate,
the transverse derivatives, the parameterized square-kernel identity,
and the K-class/Chern arithmetic. All computations are exact universal
polynomial identities and authenticate the immutable input. They do
not select actual coefficients or identify the actual scalar branch.
No original-map generic surjectivity or source exclusion follows.
