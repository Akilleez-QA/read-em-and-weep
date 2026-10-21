# A canonical obstruction map for the compressed quintic quotients

## Scope and pinned inputs

Work over C, with S=Sym(T), dim T=5. All statements are uniform in nonzero w in the binary generator space W. No selected-instance evaluation or numerical rank computation is used.

Use the original module H, scalar algebra R=S/I, column algebra A=A_lambda, and cyclic module L=Sw=S/K, with ker(lambda)=Cw. Put B=D_5(A), where D_5(M)_d=Hom_C(M_(5-d),C), and G=G_w=S/T_w.

The inputs are:

- [PR514, commit d915ed6a7f0c679343447106707692eb7bdee6f7](https://github.com/Akilleez-QA/read-em-and-weep/blob/d915ed6a7f0c679343447106707692eb7bdee6f7/research/hm/cyclic-submodule-duality/PROOF.md): exact sequences 0 -> L -> H -> A -> 0 and 0 -> B -> L -> G -> 0, together with 0 -> B -> R -> L -> 0. The quotient G is Gorenstein of Hilbert function (1,5,15,15,5,1). Also I is contained in K, which is contained in T_w, and both successive quotients K/I and T_w/K are isomorphic to B.
- [PR513, commit df947c1ce092c0c59dcef187639147da8a7b2873](https://github.com/Akilleez-QA/read-em-and-weep/blob/df947c1ce092c0c59dcef187639147da8a7b2873/research/hm/column-level-resolution/PROOF.md): the minimal resolution of A has terms S; 10S(-2); 15S(-3)+(5+u)S(-4); uS(-4)+26S(-5); 20S(-6); 5S(-7), with 0<=u<=40 and 5 dividing u.
- [PR500, commit 86d7e1b5d3aee770ea3e7652c950b29bca1aba10](https://github.com/Akilleez-QA/read-em-and-weep/blob/86d7e1b5d3aee770ea3e7652c950b29bca1aba10/research/hm/scalar-last-ghost-exclusion/PROOF.md): I has ten cubic and fifteen quartic minimal generators. 
- [PR499, commit 1112189481554b0353c64178e3adc0dede2c3fbe](https://github.com/Akilleez-QA/read-em-and-weep/blob/1112189481554b0353c64178e3adc0dede2c3fbe/research/hm/middle-euler-ghost-exclusion/PROOF.md): the original H has the pure resolution with terms 2S, 10S(-2), 20S(-4), 20S(-6), 10S(-8), 2S(-10).

The proof below concerns minimal resolutions of the original quotients, not the existence of deformations or algebraicity of a source instance.

## 1. The dual column resolution

Graded local duality gives Ext^5_S(A,S)=A^vee(5). Thus dualizing the minimal resolution of A and twisting by -10 gives the minimal resolution of B=A^vee(-5):

E_0=5S(-3),
E_1=20S(-4),
E_2=26S(-5)+uS(-6),
E_3=(5+u)S(-6)+15S(-7),
E_4=10S(-8),
E_5=S(-10).

In particular B is generated in degree three. The extension 0 -> B -> T_w/I -> B -> 0 is therefore generated in degree three as well: lift degree-three generators of the quotient and adjoin degree-three generators of the submodule. Consequently every minimal generator of T_w has degree three or four; any quartic generators are images of the fifteen quartic generators of I.

## 2. Full numerical template with two obstructions

There are exactly twenty cubic generators of T_w, by dim S_3-dim G_3=35-15=20. Write a=beta_(1,4)(G). The preceding argument gives 0<=a<=15.

Since G is codimension-five Artinian Gorenstein of socle degree five, its minimal resolution is self-dual with total shift ten. Its first positive shift is three, so the shifts in homological degree i are at least i+2. Self-duality gives the complementary upper bounds. In particular the second term has only shifts four and five, and the third only five and six. The Hilbert numerator is

1-20t^3+35t^4-35t^6+20t^7-t^10.

It follows that the entire resolution has the necessary template

F_0=S,
F_1=20S(-3)+aS(-4),
F_2=(35+a)S(-4)+bS(-5),
F_3=bS(-5)+(35+a)S(-6),
F_4=aS(-6)+20S(-7),
F_5=S(-10),

where b=beta_(2,5)(G)=beta_(3,5)(G). This does not assert that any particular pair (a,b) occurs.

## 3. The middle ghost is one canonical 26-dimensional obstruction

All Tor groups below are over S with residue field C. Consider the degree-five strand of the long exact Tor sequence of 0 -> L -> H -> A -> 0. The pure resolution of H gives Tor_3(H)_5=Tor_2(H)_5=0. Hence its connecting map is an isomorphism

delta: Tor_3(A)_5 -> Tor_2(L)_5.

Both spaces have dimension 26. The inclusion j:B -> L from coisotropic reduction induces a map Tor_2(j)_5. Define

Q_w = delta^(-1) composed with Tor_2(j)_5:
Tor_2(B)_5 -> Tor_3(A)_5.

Both its source and target have dimension 26. Its definition depends only on the exact sequences and the harmless chosen identification B=D_5(A), not on choices of free resolutions. Replacing that identification by an isomorphism does not change its rank or cokernel dimension.

Because Tor_1(B)_5=0, the long exact sequence of 0 -> B -> L -> G -> 0 gives

Tor_2(B)_5 -> Tor_2(L)_5 -> Tor_2(G)_5 -> 0.

Therefore

b=dim coker(Q_w)=26-rank(Q_w), and 0<=b<=26.

The degree-five strand one step earlier identifies the kernel as well. Indeed Tor_4(A)_5=Tor_3(H)_5=0 gives Tor_3(L)_5=0. Thus

0 -> Tor_3(G)_5 -> Tor_2(B)_5 -> Tor_2(L)_5 -> Tor_2(G)_5 -> 0.

Consequently both middle ghost spaces are exactly the kernel and cokernel of this one map. In particular the middle ghost vanishes if and only if Q_w is an isomorphism. This reduces the middle-resolution question to an intrinsic map, rather than a numerical Hilbert-series ambiguity. No rank for Q_w is asserted here.

## 4. An exact quartic-generation criterion

Set

rho=rank[ Tor_2(H)_4 -> Tor_2(A)_4 ].

The degree-four strand of the first exact sequence, using the pure H resolution, is

0 -> Tor_3(A)_4 -> Tor_2(L)_4 -> Tor_2(H)_4 -> Tor_2(A)_4 -> Tor_1(L)_4 -> 0.

Thus dim Tor_2(L)_4=u+20-rho and dim Tor_1(L)_4=5+u-rho. Define

sigma=rank[ Tor_1(B)_4 -> Tor_1(L)_4 ].

The second exact sequence and Tor_0(B)_4=0 give

a=5+u-rho-sigma.

Both defining maps have twenty-dimensional source, so rho<=20 and sigma<=20. Consequently max(0,u-35)<=a<=min(15,5+u). In particular the extreme allowed column value u=40 forces a>=5 and rigorously excludes cubic generation for that column. Conversely cubic generation requires u<=35, although that condition is not sufficient. More precisely, let p:Tor_2(A)_4 -> Tor_1(L)_4 be the connecting surjection. Then the natural composite

Tor_2(A)_4 -> Tor_1(L)_4 -> Tor_1(G)_4

is surjective, and its kernel is p^(-1)(image Tor_1(B)_4), of dimension rho+sigma. Therefore T_w is generated by cubics if and only if rho+sigma=5+u. The criterion does not require a choice of a lift of Tor_1(B)_4 through p.

For consistency, Tor_2(B)_4=0 gives an injection Tor_2(L)_4 -> Tor_2(G)_4. The same exact sequence then yields

dim Tor_2(G)_4=(u+20-rho)+(20-sigma)=35+a,

as required by the Hilbert numerator.

## 5. Equivariant size restrictions

Use the standard order-125 Heisenberg representation setup and references specified in the pinned PR513 proof. The Heisenberg group Gamma fixes W pointwise, so these sequences and obstruction maps are Gamma-equivariant. On internal degree four the central character is nontrivial; all irreducibles with that central character have dimension five. Hence a, rho and sigma are divisible by five. In particular a belongs to {0,5,10,15}, subject to the sharper bound above.

One can also describe the available characters of the middle obstruction without determining its rank. Let Reg denote the regular representation of Gamma/Z(Gamma), with its twenty-five characters. Since A_2 is a five-dimensional irreducible of central weight two and Lambda^3 T is two copies of the irreducible of weight three,

A_2 tensor Lambda^3 T = 2 Reg.

The preceding Koszul term A_1 tensor Lambda^4 T is End(T)=Reg. PR513 proves that its kernel is precisely the scalar boundary line; its image is therefore Reg-1. Since A_3=0, all of A_2 tensor Lambda^3 T is cycle space at this degree. Consequently

Tor_3(A)_5 = Reg + 1.

Duality gives the same character multiplicities for Tor_2(B)_5. Thus each nontrivial quotient character can contribute at most one dimension to coker(Q_w), and the trivial character at most two. Equivariance alone does not show that any of these scalar blocks is nonzero.

## Contribution and remaining dependency

The new conclusions are the exact kernel/cokernel realization of both middle ghost spaces by Q_w, the sharp bound b<=26 from the actual H extension, and a compatible exact criterion for cubic generation with a<=min(15,5+u). They are stronger than the loose b<=52 bound furnished by a horseshoe resolution of the two-layer filtration alone.

Neither cubic generation nor middle-ghost vanishing follows from these bounds. Proving surjectivity in the quartic criterion or invertibility of Q_w remains a genuine mathematical dependency. No generic-rank assertion, selected evaluation, or formal proof-assistant verification is claimed.
