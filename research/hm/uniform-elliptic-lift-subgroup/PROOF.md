# Exact uniform elliptic projective-lift subgroup

## Theorem and scope

Over C let C be the smooth elliptic curve y²=x³−x, with origin O at infinity, and let X=C⁴. Use the actual carrier

    E=N⊗f*H,  N=⊠₁⁴ O_C(O),

where f is the elementary-symmetric x-coordinate map and H is the literal normalized HM bundle from the two input proofs. Let

    G=C[2]⋊Aut(C,O),

acting by the same elliptic automorphism on all four factors. Put T=(0,0), τ(x,y)=(−x,iy), j=[−1]=τ², and a=t_Tτ. Then the subgroup of G whose base automorphisms admit a global regular lift to P(E) is exactly

    L=⟨a⟩={1,a,j,a³} ≅ C₄.

Each such projective lift is unique, so the full group of projective automorphisms of P(E) covering elements of this specified G is itself C₄. The ordinary, untwisted vector-bundle lift subgroup inside G is exactly {1,j}. In particular, a and a³ have projective lifts but no nonzero ordinary maps E→g*E.

This is a bounded classification inside the simultaneous group G. It does not classify arbitrary translations, distinct automorphisms on different factors, arbitrary automorphisms of X, rational or meromorphic lifts, or scalar-detector covariance.

## 1. Inputs used, without new carrier calculations

The argument takes the following established geometric conclusions from the supplied proof packets:

1. [Positive inversion proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/97190240fa87b8ed68f2a90f701bda0e7236f0e7/research/hm/cubic-loci/foundation-p02/INVERSION-LIFT.md), §§1–6: a=t_Tτ is regular of order four, a²=j, and it has a coherent order-four projective lift. With Q=⊠₁⁴ O_C(T−O), one has a*E≅E⊗Q and Hom(E,a*E)=0. Moreover every vertical automorphism of P(E) is trivial. In particular the lift of a is unique.
2. [Rank-free CM exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/759d5531be57057c4d99f8ad1b190dc1cf469174/research/hm/cm-line-twist-exclusion/PROOF.md), §§2–3: τ has no global regular projective lift of P(E). This is the projective exclusion, not merely ordinary Hom vanishing.

No differential, matrix, coefficient, rank, or source calculation is repeated here. The only new input is finite-group structure and its consequence for the set of liftable base automorphisms.

## 2. Intrinsic structure of G and its central quotient

The automorphism group fixing O is ⟨τ⟩≅C₄. This is the usual characteristic-zero elliptic automorphism classification for the j-invariant 1728 curve; equivalently, in its short Weierstrass model the nonzero linear x coefficient and zero constant coefficient give the four origin-preserving scaling automorphisms. Thus |G|=4·4=16.

Write V=C[2] additively. Its nonzero points are T, U=(1,0), and U+T=(−1,0). These are the three nonidentity two-torsion divisors of the given Weierstrass curve. The CM automorphism fixes T and exchanges the other two. Intrinsically its action α on V therefore satisfies

    α(T)=T,  α(U)=U+T,  α²=1.

This identifies the action on the finite torsion group; it is not an evaluation of a source point, polynomial instance, or detector. In particular j=τ² acts trivially on V, and j is central in G.

Set J=⟨j⟩ and D=G/J. Then

    D=V⋊_α⟨c⟩,  c²=1,

where c is the image of τ. We write T and U also for their images as translations in D. In multiplicative notation put r=Uc. The semidirect-product law gives

    r²=U+α(U)=T,  r⁴=1,  crc=r⁻¹.

Since T≠0, r has order four. Also r and c generate V and c, because U=rc and T=r². Consequently D is the dihedral group of order eight. Its center is exactly {1,T}: in the presentation every nontrivial rotation other than r² fails to commute with c, and each reflection fails to commute with r.

The image s of a is Tc=r²c. It is a reflection, with s²=1 and s≠1. In the quotient x-line the classes c, T, and s act respectively by x↦−x, x↦−1/x, and x↦1/x, by the global rational identities already established in the positive input proof. No branch-point sampling is needed to identify D or its center.

## 3. A dihedral subgroup lemma

Let D=⟨r,c | r⁴=c²=1, crc=r⁻¹⟩, and let z=r². Every subgroup K≤D with z∉K has at most two elements.

Indeed K cannot contain r or r³, whose squares are z, nor can it contain z. Every remaining nonidentity element is a reflection r^m c. If K contained two distinct reflections r^m c and r^n c, their product would be r^(m−n), a nonidentity rotation. If m−n is even this product is z; if it is odd its square is z. Either case contradicts z∉K. Thus K contains at most one nonidentity element. In particular, if it contains the specified reflection s, it equals {1,s}.

## 4. Liftability is a subgroup, forcing exactness

Define L to consist of g∈G for which there is a global regular automorphism A_g of P(E) covering the simultaneous base action of g. The identity lifts. Composition of two lifts covers the product of their base maps, and inversion covers the inverse. Thus L is a subgroup, regardless of whether lifts are unique or selected coherently in advance.

The positive input gives a∈L and hence J=⟨a²⟩⊂L. Therefore K=L/J is a subgroup of D and contains s.

Its central element T cannot belong to K. If it did, some element above T would belong to L. The two elements above T are t_T and t_Tj. Since j∈L, either possibility implies t_T∈L. Together with a∈L this would imply

    τ=t_Ta ∈ L,

contradicting the projective CM exclusion. Hence T∉K. The lemma now gives K={1,s}.

Taking the full preimage in G yields

    L=π⁻¹({1,s})={1,j,a,aj}=⟨a⟩,

where π:G→D is the quotient map and aj=a³. Equality with the full preimage follows because J⊂L: every coset represented by an element of L lies wholly in L. This proves both exclusion of all other twelve elements and existence for the stated four, without checking those twelve elements individually.

The vertical-projective-automorphism result in the positive proof implies any two lifts of the same g differ by the identity. Hence the covering homomorphism from the group of all such lifts to L is bijective. Its inverse is a group homomorphism, so these unique lifts form the coherent C₄ action already constructed there.

## 5. Ordinary versus projective symmetry

The involution j fixes the origin divisor on each factor and fixes every x-coordinate. Hence j*N≅N and f∘j=f, giving j*E≅E. This admits a coherent order-two ordinary lift: O_C(O) has the natural involution linearization from its invariant divisor, while f*H has the identity lift over the unchanged target. The identity also lifts ordinarily.

The positive proof gives a*E≅E⊗Q and Hom(E,E⊗Q)=0. Since a³=ja and j*E≅E, contravariance of pullback gives

    (a³)*E=a*(j*E)≅a*E≅E⊗Q.

Consequently Hom(E,(a³)*E)=0 as well. Neither a nor a³ admits an ordinary bundle lift. Every ordinary lift projectivizes, so every element outside ⟨a⟩ is already excluded. Thus the ordinary subgroup in G is exactly J, whereas the projective subgroup is ⟨a⟩.

Equivalently, inside this bounded G the same four elements are precisely those with O_X-algebra isomorphisms End(E)≅End(g*E): line twists preserve the endomorphism algebra, and for rank two an isomorphism of those matrix-algebra bundles gives a line twist, hence a projective-bundle isomorphism, as established in the CM input proof. No claim is made about isomorphisms of the underlying End vector bundles alone.

## 6. Root cause and evidence boundary

The positive inversion symmetry supplies one reflection in the branch quotient and its central order-two kernel upstairs. The CM obstruction forbids the central quotient translation once that reflection is available. The elementary subgroup structure of D₄ then forbids every enlargement. This is why a single positive case and a single genuinely projective negative case classify this entire finite uniform group.
