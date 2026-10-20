# A regular ambient extension through order three

## Result and scope

The proposed construction works modulo h^4. It extends the specified order-two ambient algebroid, with explicit local product coefficient μ3 and explicit overlap coefficient F3=0. The triple-unit coefficient c exists in a regular equivariant acyclic Čech model on X=C^4, but no particular c is calculated here. The result is an ambient existence statement, not a module lift, a period identification, an all-orders extension, or an evaluation of an obstruction vector.

This is a universal cochain derivation. No rational-function substitution, physical matrix product, finite-model coordinate, jet evaluation, repository experiment, or actual module value is used. The inputs are the differential/cochain identities in the pinned second-order source and the accompanying total de Rham calculation.

## 1. Inputs and conventions

Work over C[h]/(h^4). The commuting global fields V1,...,V4 have dual closed one-forms ω1,...,ω4. Put

π12=V1∧V2, π34=V3∧V4, π=π12+π34,
ω12=ω1∧ω2, ω34=ω3∧ω4, ω=ω12+ω34.

The bracket is {f,g}=π(df,dg). In particular H_f={f,−} satisfies ι_{H_f}ω=−df. Use ordinary Čech δ and total de Rham differential D=δ+(-1)^p d on Čech degree p.

The regular input cochains satisfy

δq_r=0, dq_r=(δa_r)ω_r, d(a_rω_r)=0,

with each pair supported on its indicated factors. The total cup product includes sign (-1)^(form degree of first factor times Čech degree of second factor). Thus η_r=a_rω_r+q_r is D-closed. Writing

β=λ(η1η2+η3η4)=ζ+α+b

gives precisely

ζ_i=λ(a1_i a2_i ω12+a3_i a4_i ω34),
b=λ(q1∪q2+q3∪q4),
α=λ(−a1∪q2 ω1+q1∪a2 ω2−a3∪q4 ω3+q3∪a4 ω4).

For the source's T,

T=λ[(a1∪q2)V2+(q1∪a2)V1+(a3∪q4)V4+(q3∪a4)V3],

one has α=ι_Tω and therefore

dζ=0, δζ=dα=L_Tω, δα=−db, δb=0, δT=H_b.

These hold on the ordinary Alexander–Whitney nerve, without replacing cup products by strictly anticommuting representatives.

## 2. Exact inverse convention and explicit correction

Define the local formal two-form ω_i(h)=ω−h²ζ_i. Here “inverse bivector” means the convention agreeing with the displayed π and bracket. In the displayed dual frames, the coefficient matrices W of ω and P of π are both J⊕J, where J=[[0,1],[-1,0]]. Consequently P=−W^(-1), not W^(-1).

If Z_i is the coefficient matrix of ζ_i, expansion gives

P_i(h)=−(W−h²Z_i)^(-1)=P−h²P Z_i P modulo h^4.

Thus π_i(h)=π+h²ρ_i, with

ρ_i=λ(a1_i a2_i π12+a3_i a4_i π34).

In this matrix convention the formula is ρ_i=−P Z_i P. Writing “+πζπ” without specifying which contraction convention is meant risks a sign error.

The differential of the inverse operation sends L_Tω to L_Tπ, by naturality. Since ρ is the differential at ω applied to −ζ, the identity δζ=L_Tω yields

δρ=−L_Tπ.

Equivalently, on either independent two-dimensional block, L_Tω has coefficient div(T), L_Tπ has coefficient −div(T), and ρ has the same scalar coefficient as ζ. This also checks the sign without matrix notation.

## 3. Local associative products

Let μr^M be the globally defined commuting-field Moyal coefficients, with μ0(f,g)=fg and μ1(f,g)={f,g}/2. Explicitly,

μ3^M(f,g)=(1/48) Σ π^{a1b1}π^{a2b2}π^{a3b3}
  (V_a1 V_a2 V_a3 f)(V_b1 V_b2 V_b3 g).

Define on U_i

f⋆_i g = fg+h μ1(f,g)+h² μ2^M(f,g)
             +h³[μ3^M(f,g)+(1/2)ρ_i(df,dg)].

All coefficients are regular normalized bidifferential operators. The Moyal product is associative because the fields commute. At order h³ the new correction enters associativity only by its Hochschild differential. Every biderivation is a Hochschild two-cocycle, so this differential vanishes. Hence ⋆_i is unital and associative modulo h^4.

No order-four assertion is made. In particular one must not interpret substitution of a variable bivector into the constant-coefficient Moyal formula as an all-orders construction.

## 4. Algebra maps with F3=0

Take Fij=id+h²Tij, interpreted as a map from the j algebra to the i algebra. The h² algebra-map condition is the ordinary Leibniz identity for Tij. At h³ the difference

Fij(f⋆_j g)−Fij(f)⋆_i Fij(g)

has coefficient

(μ3,j−μ3,i)(f,g)+Tij μ1(f,g)
  −μ1(Tij f,g)−μ1(f,Tij g)
= (1/2)(δρ+L_Tπ)ij(df,dg)=0.

Thus Fij is an algebra isomorphism modulo h^4; its inverse is id−h²Tij to this order. No h³ correction is required: F3=0 explicitly.

## 5. Triple-inner equation has no new h³ condition

Set

Aijk=exp(hbijk)+h³cijk
=1+hbijk+(h²/2)bijk²+h³(bijk³/6+cijk).

Here exp is the ordinary scalar exponential, truncated modulo h^4. For any scalar b,c, symmetry of μ2^M and normalization of the coefficients give

[A,f]_{⋆_i}=h²{b,f}+(h³/2){b²,f}
           =h²{b,f}+h³ b{b,f} modulo h^4.

The c term has no commutator before h^4. Since A^{-1}=1−hb+O(h²), multiplication on the right by A^{-1} gives

Ad_{⋆_i}(A)(f)=f+h²{b,f} modulo h^4.

Indeed the h³ term b{b,f} cancels the ordinary multiplication term −{b,f}b; derivative corrections from that inverse multiplication start at h^4. Local μ3 contributes no term of order at most h³ in this calculation, by normalization and the extra h in A−1.

Consequently

Fij Fjk=Ad_{⋆_i}(Aijk) Fik modulo h^4

is exactly δT=H_b, already part of the input. There is no h³ inner-gluing coefficient to solve.

## 6. Pentagon and the existential coefficient c

Expanding

Aijk⋆_i Aikl=Fij(Ajkl)⋆_i Aijl

gives the sole remaining order-three condition

δc=Ψ,
Ψijkl=(1/2){bijk,bikl}−(1/2){bjkl,bijl}−Tij(bjkl).

The local correction ρ and μ3^M do not enter this scalar equation: a normalized star coefficient sees two nonconstant arguments, each of which already costs h. The h³ term of F is zero, and even a unital nonzero F3 would not enter at this order.

The prior universal pentagon calculation proves δΨ=0 solely from δb=0 and δT=H_b. More explicitly, for C equal to the bracket portion and D=T∪b, both δC and δD equal {b012,b234}. Thus δ(C−D)=0.

Closedness alone is insufficient on an arbitrary space. Here is the additional regular-geometric input that proves existence, without computing c. Use a deck-invariant acyclic affine Čech model on X=C^4. Let P=χ1χ2 and Q=χ3χ4. The scalar b has characters P and Q, the derivation cochain T is invariant, and the bivector π has characters P and Q. Every term of Ψ therefore has character P or Q: a bracket term has the product of three characters chosen from {P,Q}, and P²=Q²=1. This statement uses the actual scalar cochain characters, not labels assigned to finite-model outputs.

Künneth gives H³(X,O_X)=⊕_{|S|=3} C_{χ_S}. Indeed H⁰(C,O_C) is trivial and H¹(C,O_C) is the sign character for the elliptic involution; the latter follows also by duality from its action on the invariant differential. There is no P or Q summand. Since the regular acyclic Čech complex computes this cohomology, the closed regular cochain Ψ is exact. A regular c with δc=Ψ exists. Averaging a primitive by the P and Q character projectors chooses c in those characters.

This uses existence in the actual regular Čech complex; no universal polynomial expression for c follows merely from the free differential identities. If one drops regularity, acyclicity, the X=C^4 geometry, or the stated character behavior, retain δc=Ψ as an obstruction equation rather than asserting its solvability.

## 7. Conclusion and explicit/existential boundary

On the regular equivariant affine cover of the stated X, the data

μ3,i=μ3^M+(1/2)ρ_i,  ρ_i=λ(a1_i a2_i π12+a3_i a4_i π34),
Fij=id+h²Tij,
Aijk=exp(hbijk)+h³cijk,  δc=Ψ,

define an ambient algebroid modulo h^4 extending the pinned order-two presentation. The local products and maps are explicit. The scalar unit correction is existential and regular; its coefficients are not supplied. No statement about an order-three module, the pending order-two module obstruction, or a formal period is implied.

Sources read: [proof.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/99411ca8810ba70158126e9bebd01eb79104003c/research/hm/null-scalar-pentagon/proof.md) and the pinned PR16 source (see README) (the latter records commit c8aec970fd65a105f39f4e8aeb8a17f0f0053f89). The companion total de Rham proof is [RESULT.md](../total-de-rham/RESULT.md).

## Appendix: polarized two-parameter version

The same proof works over C[s,t]/(s,t)^4 under the source's disjoint-pair support identities. Write π=P_biv+Q_biv, b=bP+bQ, T=TP+TQ, and ρ=ρP+ρQ, where the labels denote the (1,2) and (3,4) factor pairs rather than cochain degrees. Use the global Moyal expansion with first-order bivector sP_biv+tQ_biv, and add the degree-three biderivation

(1/2)(s³ρP+t³ρQ).

Set Fij=id+s²TP,ij+t²TQ,ij and

Aijk=exp(s bP,ijk+t bQ,ijk)+s³cP,ijk+t³cQ,ijk.

Disjoint support implies L_TP Q_biv=L_TQ P_biv=0, TP(bQ)=TQ(bP)=0, and the mixed Hamiltonian contractions vanish. The algebra-map defect is consequently the sum of the already vanishing s³ and t³ defects. The inner equation at degree two is δTP=H^P_bP and δTQ=H^Q_bQ; the degree-three inner contribution still vanishes by symmetry of the second Moyal coefficient. The scalar unit defect is s³ΨP+t³ΨQ, with no mixed terms, because every mixed bracket and derivation term vanishes. Each ΨP or ΨQ is closed, has its indicated pair character, and admits a regular primitive cP or cQ by the same H³ argument. Thus this is an explicit-products-and-maps, existential-units ambient extension through total degree three. No degree-four or module assertion follows.
