# A finite flat Gorenstein family and its exact relation bundles

## 1. Inputs and conventions

Work over C. Let S=Sym(T), dim(T)=5, and let H be the original module with W=H_0 of dimension two. Use its symmetric perfect S-balanced pairing b in total degree five. Put I=Ann_S(H) and R=S/I. The actual trace identification N=Sym^2_S(H)=D_5(R), where D_5(R)_d=R_(5-d)^*, is given by

Phi(hh')(q)=b(qh,h').

[PR514](https://github.com/Akilleez-QA/read-em-and-weep/blob/d915ed6a7f0c679343447106707692eb7bdee6f7/research/hm/cyclic-submodule-duality/PROOF.md) proves uniformly for every nonzero w in W that the apolar algebra of F_w(q)=b(qw,w) is G_w=S/T_w, with Hilbert function (1,5,15,15,5,1). Moreover T_w=Ann_S(w^2 in N), I is contained in T_w, and G_w is the coisotropic quotient Sw/(Sw)^perp.

The actual binary multiplication model from [PR494](https://github.com/Akilleez-QA/read-em-and-weep/blob/72ab9a7524aef8c9d1c1fd989f8b0e83826dc916/research/hm/higher-symmetric-powers/PROOF.md) identifies S_2=E tensor Sym^2(W) and N_2=E tensor Sym^4(W), where dim(E)=5; multiplication by w^2 is ordinary binary multiplication in these identifications. Also N_1=T tensor Sym^2(W) and N_0=Sym^2(W). The dimensions of I_3,I_4,I_5 are 10,55,123. The scalar resolution in [PR500](https://github.com/Akilleez-QA/read-em-and-weep/blob/86d7e1b5d3aee770ea3e7652c950b29bca1aba10/research/hm/scalar-last-ghost-exclusion/PROOF.md) gives dim(T I_3)=40.

Let P=P(W) parameterize lines, with tautological line bundle L=O_P(-1). Tensor products of finite-dimensional vector spaces with O_P are abbreviated by omitting O_P. All splitting statements below are ordinary vector-bundle statements, not equivariant or canonical splittings. A choice of nonzero determinant form on W is allowed in the explicit binary calculation.

## 2. The relative apolar algebra

The quadratic dependence on w defines a morphism

F:S_5 tensor O_P -> O_P(2).

For 0<=d<=5 define the catalecticant morphism

C_d:S_d tensor O_P -> S_(5-d)^* tensor O_P(2),

by C_d(f)(g)=F(fg). Put J_d=ker(C_d), and put J_d=S_d tensor O_P for d>=6. The constant fiber ranks supplied by PR514 are (1,5,15,15,5,1). Consequently each J_d is a subbundle, its quotient is locally free, and these kernels and quotients commute with base change. The inclusions S_e J_d subset J_(d+e) follow directly from F((af)g)=F(f(ag)). Thus J is a homogeneous ideal sheaf in S tensor O_P.

The quotient A=(S tensor O_P)/J has graded pieces

A_0=O_P, A_1=T, A_2=Sym^2(T),
A_3=Sym^2(T)^* tensor O_P(2),
A_4=T^* tensor O_P(2), A_5=O_P(2),

and A_d=0 for d>5. Indeed C_d is injective for d<=2 and surjective for d>=3. In particular X=Spec_P(A) is finite flat of degree 42 over P, with fiber G_w at [w]. It is a family of quotients of the original R, since I tensor O_P is contained in J.

Multiplication followed by the top-degree projection gives a pairing

A_d tensor A_(5-d) -> O_P(2).

It is perfect on every fiber and therefore perfect as a bundle pairing. If tau:A->O_P(2) is zero off degree five and identity in degree five, the map a |-> (c |-> tau(ac)) is an isomorphism of ungraded A-modules

A -> Hom_O_P(A,O_P(2)).

Hence the finite-flat dualizing module Hom_O_P(A,O_P) is the invertible ungraded A-module A tensor O_P(-2). This establishes relative Gorensteinness, not just Gorensteinness of individual fibers. The family is a flat algebraic family; no assertion about algebraicity of the separate original deformation problem follows.

## 3. Compatibility with the universal coisotropic quotient

Let M be the image of S tensor L -> H tensor O_P given by multiplication. Its fiber is Sw. PR514 gives constant graded image ranks, so M is a graded subbundle of H tensor O_P. The fixed pairing defines its orthogonal subbundle M^perp. Fiberwise M^perp is contained in M, hence the inclusion holds globally: the composite M^perp -> (H tensor O_P)/M vanishes on all fibers of the reduced scheme P.

The quotient Q=M/M^perp has the induced perfect pairing with values in O_P, in total degree five. Its degree-zero piece is L. The natural cyclic map S tensor L -> Q identifies

Q tensor L^* = A

as graded S-modules: its kernel after tensoring by L^* is exactly the catalecticant ideal J. The unital algebra structure on the right is supplied by the cyclic quotient of S, not asserted on Q itself. Twisting both entries of the O_P-valued pairing explains the precise O_P(2) trace line of A. Thus the relative construction globalizes the actual coisotropic reduction without choosing a generator separately on each fiber.

## 4. An elementary binary quotient lemma

Fix m>=2 and a nonzero determinant form on W. For a line Cw, let lambda_w in W^* be its annihilator, chosen linearly in w by that determinant form. The differential of a binary form f in Sym^m(W), evaluated at lambda_w, defines a bundle morphism

D_m:Sym^m(W) tensor O_P -> W tensor O_P(m-1).

It is homogeneous of degree m-1 in w. For m=2 or 4 its kernel on the fiber at [w] is precisely w^2 Sym^(m-2)(W). Indeed choose coordinates with lambda_w=(1,0) and w the second basis vector. Both partial derivatives vanish exactly when the coefficients of the first-variable monomials of degrees m and m-1 vanish; in characteristic zero this is exactly divisibility by w^2. The derivatives of the forms x^m and x^(m-1)y are independent there, so D_m is surjective. Therefore, for m=2,4, there is an exact sequence

0 -> Sym^(m-2)(W) tensor O_P(-2)
  -> Sym^m(W) tensor O_P
  -> W tensor O_P(m-1) -> 0,

whose left map is multiplication by w^2. This proves the quotient splitting explicitly, without invoking a jet-bundle splitting theorem.

## 5. Exact cubic, quartic and quintic annihilator bundles

The cubic catalecticant gives the exact sequence

0 -> J_3 -> S_3 tensor O_P -> S_2^* tensor O_P(2) -> 0.

Thus J_3 has rank 20 and degree -30. More precisely, factor out its constant subbundle I_3 tensor O_P. Dualizing the induced surjection from R_3, and using R_3^*=N_2, identifies (J_3/I_3)^* with the quotient of

E tensor Sym^4(W) tensor O_P

by E tensor Sym^2(W) tensor O_P(-2), with the actual multiplication map from Section 1. Section 4 identifies this quotient with E tensor W tensor O_P(3). It follows that

J_3/(I_3 tensor O_P) = E^* tensor W^* tensor O_P(-3).

The extension by I_3 tensor O_P splits, because Ext^1(O_P(-3),O_P)=H^1(P,O_P(3))=0. Thus, noncanonically,

J_3 = 10O_P direct sum 10O_P(-3).

The same argument in degree four uses R_4^*=N_1=T tensor Sym^2(W) and the inclusion T tensor O_P(-2) given by w^2. In degree five it uses R_5^*=Sym^2(W) and the same inclusion with no T factor. Section 4 with m=2 therefore gives

J_4/(I_4 tensor O_P) = T^* tensor W^* tensor O_P(-1),
J_5/(I_5 tensor O_P) = W^* tensor O_P(-1).

The analogous extensions split by H^1(O_P(1))=0, so

J_4 = 55O_P direct sum 10O_P(-1),
J_5 = 123O_P direct sum 2O_P(-1).

All these identifications concern the actual annihilator family, rather than a bundle reconstructed only from its ranks and degrees.

One immediate consequence is H^0(P,J_d)=I_d for d=3,4,5. There are no globally constant additional annihilator relations common to the entire family. More sharply, the moving cubic quotient has no sections after twisting by O_P(r) for r<3, and has exactly ten sections for r=3. The moving quartic and quintic quotients first acquire sections at twist one, with dimensions ten and two respectively.

## 6. A global map controlling quartic minimal generators

There is a canonical multiplication map of bundles

T tensor (J_3/(I_3 tensor O_P)) -> J_4/((T I_3) tensor O_P).

It is well-defined because changing a cubic representative by an element of I_3 changes its product by an element of T I_3. The target is an extension of J_4/I_4 by the 15-dimensional constant space I_4/(T I_3), and splits because H^1(O_P(1))=0. After noncanonical choices of splittings, this is a map

50O_P(-3) -> 15O_P direct sum 10O_P(-1).

Its fiber cokernel at [w] is exactly (T_w)_4/(T (T_w)_3), the space of quartic minimal generators of G_w. Thus the unresolved quartic-generator parameter a(w) is the actual cokernel dimension of this global morphism. In homogeneous coordinates on P its upper block has entries of degree three and its lower block entries of degree two. Rank-drop conditions, and hence the loci a(w)>=r, are consequently determinantal closed subschemes. No rank of this map, generic value of a, or nonemptiness of a jump locus is asserted.

This supplies a global, bounded-degree structural object for the unresolved generator question, in addition to constructing the finite flat family and determining all three relation bundles.

## Scope

These are structural deductions from the pinned original-module pairing, universal compressed Hilbert function, actual binary multiplication model and scalar resolution. No selected HM/source-instance evaluation, coefficient search, numerical rank computation or large computation is used. The proof is authored mathematics, not a proof-assistant verification. It neither determines the unresolved connecting-map ranks in the Gorenstein resolution nor resolves the original fixed-pair first-order residual, higher-order lifting or algebraicity questions.
