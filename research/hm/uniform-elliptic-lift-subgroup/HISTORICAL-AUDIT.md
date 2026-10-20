# Historical audit provenance

The following assessment belongs to the source edition. It is not a fresh independent audit of the edited publication packet. Exact source proof and audit hashes are bound in SOURCE-BINDINGS.json. The positive input is now the immutable PR181 INVERSION-LIFT.md; the negative input is T01.

# Independent audit: uniform elliptic lift classification

## Verdict

**Pass.** The theorem in `PROOF.md` follows from the two supplied proof packets. The finite-group reduction is correct and excludes all twelve elements outside the asserted cyclic subgroup without a new carrier calculation. The assertions about ordinary lifts, uniqueness, and the endomorphism-algebra formulation are also justified at the stated scope.

This is an independent audit of the new deduction and its use of the supplied inputs. It does not independently re-prove the older full-chain monomial theorem or the structural exactness theorem cited within those inputs.

## 1. Input alignment and exact dependencies

The three packets use the same curve, simultaneous action on four factors, scalar line, normalized HM bundle, and carrier. The new theorem works over C, where both imported projective conclusions hold.

The classification itself needs only:

1. The positive packet's global regular lift of a=t_Tτ, with a²=j=[−1].
2. The CM packet's exclusion of a **projective** lift of τ.

The CM packet provides precisely the second statement in §5. Its earlier ordinary Hom vanishing is not being incorrectly substituted for projective non-liftability. This distinction is essential and is handled correctly.

The other assertions have separate, explicit inputs:

- Uniqueness and identification of the full covering-automorphism group use triviality of the vertical projective automorphism group from the positive packet, §6.
- Ordinary exclusion of a and a³ uses the positive packet's line-twist identification and twisted Hom vanishing, §§3 and 5.
- The algebra-bundle reformulation uses the matrix-algebra/line-twist equivalence explained in the CM packet, §5.

No inference about ordinary or projective lifts is drawn merely from the existence of a chosen scalar-line twist.

## 2. The group and quotient

For this characteristic-zero elliptic curve, Aut(C,O)=⟨τ⟩ has order four. This is the standard origin-preserving automorphism classification for the j-invariant 1728 curve; it is not an additional claim about the HM carrier.

The asserted action on V=C[2] is the nontrivial involution fixing T and exchanging the other two nonzero elements. With a basis T,U of V, it is

    α(T)=T,   α(U)=U+T.

Since j=τ² acts trivially on V and commutes with τ, J=⟨j⟩ is central. Its quotient is genuinely

    G/J = V⋊_α C₂,

of order eight. Writing c for the image of τ and r=Uc gives r²=T, so r has order four, and c conjugates r to r⁻¹. Also r and c generate the entire quotient. Thus the quotient is the order-eight dihedral group, rather than an abelian group or the quaternion group. Stating its order avoids the competing conventions for the symbol D₄.

Its center is exactly {1,T}. The image s of a is Tc=r²c, a nonidentity reflection. The quotient's central element T is distinct from the central involution j that was killed upstairs. The proof keeps this distinction intact.

The x-line formulas are consistent with the imported geometric identities, but they are not needed for the subgroup deduction. The essential structural data are the torsion action and the dihedral presentation.

## 3. Center-excluding subgroup lemma

The lemma is correct for the order-eight dihedral group. A subgroup avoiding z=r² cannot contain either order-four rotation. If it contained two distinct reflections, their product would be a nonidentity rotation: either z itself, or a rotation whose square is z. Closure would then force z into the subgroup.

Consequently such a subgroup has order at most two. If it contains the specified reflection s, it must equal {1,s}. No assumption of normality is needed.

## 4. Liftability, closure, and exactness

The set L of base elements possessing a global regular projective lift is a subgroup. Identity, composition, and inverses suffice; prior choices or coherence of the lifts are unnecessary for this step. All these operations remain global and regular.

The positive case places a and J=⟨a²⟩ in L. It is therefore legitimate to form K=L/J as a subgroup of G/J.

If T belonged to K, L would contain a representative of the coset t_TJ. As J is already contained in L, this would force t_T itself into L. Closure would then imply

    τ=t_Ta ∈ L,

contrary to the imported projective CM exclusion. Thus K avoids the quotient center and contains s. The lemma gives K={1,s}.

Because J⊂L, passing back from this quotient subgroup gives its entire inverse image, not merely a choice of coset representatives:

    L={1,j,a,aj}=⟨a⟩≅C₄.

The four listed elements are distinct because a has order four. Since G has order sixteen, exactly twelve specified base elements are excluded. This argument neither assumes conjugacy invariance of liftability nor introduces an unproved symmetry of the carrier.

## 5. Uniqueness and coherence

Two projective lifts of the same base automorphism differ by a vertical projective automorphism. The imported vertical-triviality theorem therefore establishes uniqueness for **every** liftable element, not just for a.

It follows that the projection from the full group of projective automorphisms covering elements of G to L is an isomorphism. The unique lifts necessarily compose coherently, and their group is C₄. This agrees with the explicit coherent action in the positive packet.

This claim concerns projective lifts. It does not assert uniqueness of ordinary vector-bundle lifts, which would admit scalar multiples.

## 6. Ordinary lifts and the algebra formulation

The ordinary lift of j is justified independently of any projective-to-linear lifting assumption. The origin divisor is j-invariant, so its divisor line has its natural coherent involution linearization; f is unchanged by j, so the pulled-back HM factor has the canonical lift over the same target point. This yields a coherent order-two ordinary lift of E.

For a³=ja, pullback contravariance gives

    (a³)*E=a*(j*E)≅a*E≅E⊗Q.

The imported vanishing Hom(E,E⊗Q)=0 thus excludes ordinary maps for both a and a³. Every ordinary bundle isomorphism projectivizes, so the twelve projectively excluded elements cannot admit ordinary lifts. The ordinary lift subgroup is exactly {1,j}.

The final algebra statement is also correctly bounded: algebra isomorphisms of End bundles correspond to line-twist/projective equivalence, while isomorphisms of their underlying vector bundles alone do not. No conclusion about the latter is claimed.

## 7. Scope and evidence boundary

The classification is exact only inside the stated simultaneous finite group C[2]⋊Aut(C,O). The proof explicitly avoids extending it to arbitrary translations, independent factorwise actions, other automorphisms of C⁴, rational or meromorphic lifts, or covariance of selected sources or scalar detectors.

