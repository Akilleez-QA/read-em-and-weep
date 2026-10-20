# Full deck-equivariant two-parameter ambient extension

## Result and precise scope

**The promotion is valid for the ambient differential algebroid.** Over a characteristic-zero field, the PR16 scalar descent presentation on the product affine cover of the abelian fourfold X=C^4 admits a literal G=(Z/2)^4-equivariant formal extension over k[[s,t]], where s has character P={1,2} and t has character Q={3,4}. Its first and second jets are specified below. The diagonal specialization s=t=h agrees literally with the supplied PR16 presentation through h².

This proves existence with higher local products, overlap maps, and triple units free to change. It does not extend an arbitrarily prescribed all-order Moyal product, prove a module family exists, compute an obstruction coordinate, or establish higher-order choice independence. Nor does it show an arbitrarily previously chosen one-parameter all-order extension is a diagonal slice: it constructs a compatible extension of the prescribed two-jet.

Only the three supplied static artifacts and universal formal algebra are used. No actual bundle model, source/jet evaluation, physical matrix products, production imports, or geometric computations are used.

## 1. Cochains, characters, and first directions

Use the fixed product affine cover from the supplied PR16 source. Every member is preserved by each deck inversion because its defining charts depend on x_i; restrictions are G-equivariant. No refinement needed solely for a bundle is part of this ambient construction.

Put

- πP=V1∧V2 and πQ=V3∧V4;
- bP=λ q1∪q2 and bQ=λ q3∪q4;
- TP=λ[(a1∪q2)V2+(q1∪a2)V1];
- TQ=λ[(a3∪q4)V4+(q3∪a4)V3].

These are precisely the split scalar cochains of source Sections 1–3. The q_i and V_i have character {i}, while a_i is invariant. Thus πP,bP have character P, πQ,bQ have character Q, and TP,TQ each have trivial character. On the indicated overlaps,

δbP=δbQ=0,
δTP={bP,-}_P,  δTQ={bQ,-}_Q,
{bP,-}_Q={bQ,-}_P=0.

Here {f,g}_P=πP(df,dg), and similarly for Q. The last identities follow because bP involves only factors 1,2 and bQ only factors 3,4. They are formal factor-separation identities, not evaluations on a model.

Let m=(s,t), give s character P and t character Q, and define

π(s,t)=sπP+tπQ,    β(s,t)=sbP+tbQ.

Both are invariant for the diagonal action on geometric coefficients and parameters. Their linear terms assign the two supplied bivector/gerbe first directions separately to s and t. The scalar λ is fixed as in the source; the argument applies in particular to its compensated normalization.

## 2. Derivation of the two-jet, including mixed coefficients

Work over R₂=k[s,t]/m³. Let m₀ be ordinary scalar multiplication, and define commuting bidifferential operators

DP=V1⊗V2−V2⊗V1,    DQ=V3⊗V4−V4⊗V3.

Set D=sDP+tDQ and define, on each chart,

μ(f,g)=m₀(1+D/2+D²/8)(f⊗g).

Explicitly,

μ=m₀+s μP+t μQ+s² μPP+st μPQ+t² μQQ,

μP=m₀DP/2,  μQ=m₀DQ/2,
μPP=m₀DP²/8,  μQQ=m₀DQ²/8,
μPQ=m₀(DPDQ+DQDP)/8=m₀DPDQ/4.

In particular the mixed coefficient is

μPQ(f,g)=1/4[(V1V3 f)(V2V4 g)−(V1V4 f)(V2V3 g)
                    −(V2V3 f)(V1V4 g)+(V2V4 f)(V1V3 g)].

Associativity follows directly from commuting derivations: on a triple tensor product the two iterated products are both ordinary triple multiplication composed with exp((D12+D13+D23)/2), truncated modulo m³. This proves all pure and mixed quadratic identities simultaneously. This local exponential is used only to verify the prescribed finite jet; no all-order constraint on μ is imposed later.

To determine F rather than guess a parameter substitution, write F=id+L₂ with L₂ homogeneous of degree two. For A=1+β+O(m²), the inner action through degree two is

Ad_μ(A)(f)=f+{β,f}_{π(s,t)} mod m³.

Indeed the first-order star commutator is π(s,t), so commuting the degree-one β with f first contributes in degree two; all ordinary scalar commutators vanish. Expanding its right-hand side gives

{β,-}_{π(s,t)}=s²{bP,-}_P
                 +st({bP,-}_Q+{bQ,-}_P)+t²{bQ,-}_Q
               =s²δTP+t²δTQ.

Thus choose

L₂=s²TP+t²TQ,    Fij=id+s²TP,ij+t²TQ,ij.

The mixed coefficient F_st is zero, justified by the vanishing cross Hamiltonians. Each L₂ is an ordinary derivation, so F is a μ-algebra homomorphism modulo m³: the derivation identity handles degree two against m₀, and its interaction with μ−m₀ starts in degree three. Its inverse exists because F=id modulo m.

Choose the triple units

Aijk=1+βijk+βijk²/2
    =1+sbP,ijk+tbQ,ijk+s²bP,ijk²/2
       +st bP,ijk bQ,ijk+t²bQ,ijk²/2.

The square and mixed product here are ordinary products of scalar functions on the same triple intersection, not a cup product of two Čech-degree-two cochains.

The inner-gluing equation now follows because δL₂={β,-}_{π(s,t)}. The pentagon follows coefficientwise from δβ=0. Through degree two, multiplying two elements 1+O(m) by μ agrees with multiplying their ordinary truncated exponentials: normalized differential corrections require positive-degree terms in both inputs and hence begin in degree three. Likewise F(1+β+β²/2)=1+β+β²/2 modulo m³. Consequently the two sides of the pentagon are the ordinary exponential of, respectively,

βijk+βikl    and    βjkl+βijl,

which are equal. This checks in particular its mixed st equation; it is not inferred merely from the diagonal s=t.

The full two-jet is strictly G-equivariant. Pure s² and t² coefficients have character 0; μPQ and bP bQ have character P△Q; first-degree coefficients have P or Q as required. Every parameter/coefficient product is invariant. At s=t=h the formulas give precisely μ through h² for πP+πQ, F=id+h²(TP+TQ), and A=1+h(bP+bQ)+h²(bP+bQ)²/2.

## 3. Multivariate literal small extensions

Let C be the total Čech complex of normalized algebraic polydifferential Hochschild cochains including arity zero, shifted by one, with differential d=δ+(−1)^p b on Čech degree p. This is the precise complex and sign convention in the supplied descent-lifting lemma.

For N≥3 consider

R'=k[s,t]/m^(N+1) → R=k[s,t]/m^N,
I_N=m^N/m^(N+1).

Then m I_N=0 and I_N²=0. The classical reduction is O_X. Every proof in the supplied lemma uses only these two annihilation facts, unital normalization, and the classical reductions μ=m₀,F=id,A=1. It never requires a generator of I. Therefore its defects and correction formulas apply unchanged, with values in C⊗I_N:

O=(−S,H,K,−Ppent),   dO=0,
ΔO=d(u,v,a).

For clarity Ppent denotes the pentagon defect, distinct from the character P. The individual formulas are

ΔS=−bu,  ΔH=δu−bv,  ΔK=δv+ba,  ΔPpent=−δa.

All defect multiplications and transports reduce to their classical operations because m annihilates I_N. Thus a solution of d(u,v,a)=−O changes only total-degree-N coefficients and preserves the previous truncation literally. The same argument proves normalized differential corrections remain in the specified category. No gauge replacement or comparison up to equivalence is involved.

Coefficientwise lifting is possible: lift the already chosen finite collection of homogeneous degrees using the same coefficients and initially set the new degree to zero. This is unital, normalized, differential, and G-equivariant. Its defects are invariant for the diagonal action. There is no need to average a nonlinear descent solution.

## 4. Vanishing of every equivariant ambient obstruction

Algebraic HKR and affine Čech computation, with the same hypotheses as the supplied lemma, give the G-equivariant identification

H²(C)=HH³(X)=⊕_(p+q=3) H^q(X,Λ^p T_X).

On X=C^4, invariant vector fields give T_X a basis of characters {1},{2},{3},{4}. Künneth similarly gives H^q(O_X) the exterior products of q singleton-character H¹ classes. Thus a character in H^q(X,Λ^p T_X) is the symmetric difference of p+q=3 singleton characters, counted with multiplicity across the two exterior factors. Its cardinality is odd, either 1 or 3. Repeated indices across the factors cancel in pairs and cannot change that parity.

Meanwhile a basis of I_N consists of s^a t^b with a+b=N. Its character is

(a mod 2)P △ (b mod 2)Q,

one of 0,P,Q,P△Q, all of even cardinality. No odd-cardinality character tensored with an even-cardinality character is trivial. Hence

(H²(C)⊗I_N)^G=0.

Because I_N is finite-dimensional over k and k has characteristic zero,

H²((C⊗I_N)^G)=(H²(C)⊗I_N)^G=0.

Here tensoring is exact over the field and finite-group invariants are exact by averaging. Therefore every invariant cocycle O above admits a primitive. Choose any primitive and average that linear primitive under G, producing an invariant correction (u,v,a) with d(u,v,a)=−O. This preserves all lower-order coefficients and enforces every descent identity over R'.

The same vanishing can already be detected by simultaneous inversion: it acts by −1 on HH³ and by +1 on every s^a t^b. Averaging the primitive under the entire G, rather than only simultaneous inversion, ensures full G-equivariance.

## 5. Compatible induction and what becomes available

Start with the explicitly checked two-jet over k[s,t]/m³. Apply Section 3 for N=3, then N=4, and so on, each time using Section 4. All choices extend the previous representative literally. Their inverse limit supplies m-adically continuous products, overlap algebra isomorphisms, and triple units on O_X[[s,t]], satisfying the algebroid descent equations exactly and carrying the prescribed semilinear G-action.

Units A and linear inverses F exist by the m-adic geometric series; after associativity and the homomorphism identities have been enforced, these are the required algebraic descent units and isomorphisms. The formal coefficients are algebraic polydifferential cochains; there is no claim of convergence or a uniform differential-order bound.

Thus the previously conditional **ambient-family existence premise** in the two-parameter character-selection review is now supplied for this literal two-jet. For any further genuinely G-equivariant construction over this family, coefficient comparison still gives character P^(a mod 2)Q^(b mod 2) to its s^a t^b coefficient. Its full-sign component therefore has the form st B(s²,t²).

This last conclusion remains conditional on the further construction being defined and equivariant. In particular, ambient extension does not construct an all-order module, solve its correction equations, produce equivariant module homotopies, show higher full-sign coefficients independent of choices, or determine any of the 30 requested obstruction values. The obstruction vanishing used here is HH³ ambient vanishing after invariant tensoring, not an Ext² module-vanishing statement.

## Static source provenance

1. [LEMMA.md](../descent/LEMMA.md): literal normalized small-extension descent proof, signs, differential category, and HKR hypothesis.
2. [review.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/03f681c944e6997b14117aad06dd562c408c63c8/research/hm/null-ordinary-character-audits/characters/review.md): two-parameter parity theorem and its limitations.
3. https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md, Sections 1–3 and 8: split π,b,T data and deck characters.

The first artifact identifies the PR16 provenance as commit c8aec970fd65a105f39f4e8aeb8a17f0f0053f89. This result uses the supplied static source, not a newly verified remote repository head.
