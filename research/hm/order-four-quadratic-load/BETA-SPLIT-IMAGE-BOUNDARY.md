# Residual beta plane: split evaluation image and a three-dimensional boundary

## Scope and inputs

Work over the complex numbers. Let E be the rank-two Horrocks–Mumford bundle twisted so that c1(E)=5, c2(E)=10, and U=H0(E) has dimension four. Let D be an integral ACM sextic in a hyperplane P3, with arithmetic genus three, and let Z consist of the 25 reduced points at which D meets the evaluation rank-one locus. Assume these points are smooth on D and evaluation has local elementary-transform form diag(1,t). These are the sextic-lane inputs, not conclusions of this note.

Let J be the image of U tensor O_D → E|D. It is locally free, and there is an exact sequence

0 → J → E|D → T → 0,

where T is a length-25 sheaf supported on Z, with one-dimensional stalk at each point. In particular T is noncanonically isomorphic to O_Z. Its determinant is L=O_D(5)(−Z), of degree five. The Plücker kernel map D → Gr(2,U) is assumed to have image spanning a beta plane: its kernel planes K_x all lie in one fixed three-dimensional B⊂U, and their Plücker image is not contained in a line. This is a conditional description of the residual beta case, not its exclusion.

Public input: SEXTIC-PLUCKER-FLAGS.md at a82e9aeaad55a4e58a0fea12581bab1dcf42e4b0, and INTEGRAL-SEXTIC-ACM-RESOLUTION.md at 7c7bf54af204daa4a00ddfec0b69e3c3dda94424, in Akilleez-QA/read-em-and-weep/research/hm/order-four-quadratic-load.

## Proposition: the image bundle splits

There is an exact sequence

0 → L → J → (U/B) tensor O_D → 0.

It splits after choosing a vector-space complement of B in U. Consequently J≅L⊕O_D. Moreover B→H0(L) and U→H0(J) are isomorphisms.

Proof. The surjection U tensor O_D→J has locally free kernel K. Since the kernel map has image in Gr(2,B), its composite K→(U/B) tensor O_D is zero. Thus J surjects onto (U/B) tensor O_D, with kernel B tensor O_D/K, a line bundle. Its determinant is det J=L, after choosing a basis of the constant one-dimensional U/B. A complement U=B⊕⟨t⟩ supplies a right inverse by sending the constant class of t to its evaluation in J. This proves splitting.

D is integral and Cohen–Macaulay of arithmetic genus three, so its dualizing sheaf is rank-one torsion-free of degree four; Gorensteinness is not required or asserted. Since deg L=5, Serre duality gives H1(L)=H0(ω_D tensor L^−1)^*=0. Indeed the latter rank-one torsion-free sheaf has degree −1. A nonzero section would inject O_D with a zero-dimensional quotient, forcing nonnegative degree, a contradiction. Riemann–Roch gives h0(L)=3.

If a nonzero b∈B mapped to zero in H0(L), it would belong to every K_x. All K_x would then be planes in B containing the fixed line ⟨b⟩. Their Plücker image is a projective line, contradicting the beta-plane-spanning assumption. Thus B→H0(L) is injective and hence an isomorphism. The chosen complementary constant section gives U→H0(J) as an isomorphism as well. ∎

## Corollary: exactly three possible residue constraints

The cohomology sequence takes the form

0 → C^4 → H0(E|D) → C^25 --δ→ C^3 → H1(E|D) → 0.

Writing r=rank δ, necessarily 0≤r≤3, and

h0(E|D)=29−r,   h1(E|D)=3−r,   χ(E|D)=26.

Indeed H1(J)≅H1(O_D) tensor (U/B), which has dimension three, because H1(L)=0. The long exact sequence and H1(T)=0 prove the claim. The target identification is canonical up to the one-dimensional constant factor U/B; choosing a complement is not needed for its dimension. Each point of Z contributes one local principal-part coordinate to H0(T). The only obstructions to lifting such principal parts to a global section of E|D are the three coordinates of δ.

This is not the ambient restriction-lifting problem, and by itself it does not prove r=3. Nor does it split E|D: only its elementary-transform subsheaf J splits. In particular the constant summand of J need not remain a nowhere-vanishing section of E|D at Z.

## What is new and what remains

The residual beta configuration forces an actual splitting of the image bundle, and reduces the on-curve principal-part boundary to a three-dimensional target with the exact numerical alternatives above. This is a structural deduction, not a review of a claimed solution. Excluding beta, explicitly computing the entries of δ, lifting an on-curve section to P4, and proving the complete repair remain open here; the final theorem below does determine the generic rank of δ under one additional public vanishing input. No selected coefficients, ranks, or one-shot experiments were evaluated.

## Sharpening: five active points force the boundary to be surjective

Call p∈Z active if B is not the kernel of the rank-one fiber evaluation U→E_p. If at least five points are active, then r=3. Consequently

h0(E|D)=26 and H1(E|D)=0.

Equivalently, failure of boundary surjectivity forces every section in B to vanish at at least 21 of the 25 marked points.

Proof. At a smooth marked point choose a parameter t and bases in which J→E|D is diag(1,t). Its fiber kernel is a line ℓ_p⊂J_p, and the elementary modification is locally generated by adjoining t^−1v_p, for a lift v_p of a nonzero vector of ℓ_p. Thus the boundary from the local length-one quotient is the principal-part boundary with direction v_p. After projection J→(U/B) tensor O_D, its direction is nonzero exactly when ℓ_p is not the fiber L_p. Since both are lines, ℓ_p=L_p is equivalent to L_p mapping to zero in E_p, hence to all B sections evaluating to zero. Fiber evaluation on U has rank one at p, so its kernel has dimension three and this is precisely B=ker(U→E_p).

By Serre duality, the transpose of δ evaluates a canonical differential at each marked point, multiplied by that projected principal-part direction and a nonzero local scalar. At an active point the scalar is nonzero; at an inactive point the coordinate is zero. If an element of ker δ* were nonzero, it would therefore be a nonzero section of ω_D vanishing at every active point. All these points are smooth, so their divisor A is Cartier. For five or more active points, ω_D(−A) is rank-one torsion-free of degree at most −1, and has no nonzero section by the injection-and-length argument above. Thus δ* is injective, δ is surjective, and r=3. ∎

This criterion alone does not assert that five active points have been proved to exist in the actual configuration; the final theorem below supplies that conclusion generically using the additional no-common-section input. It isolates the remaining failure case as a concrete incidence constraint: a fixed three-dimensional space of global sections simultaneously vanishes at 21 or more distinct marked points. No actual evaluation at those points was performed.

## Generic closure using the no-common-section input

Assume additionally that the intrinsic beta assignment H↦B_H is equivariant under the projective Heisenberg action, that evaluation has rank exactly one everywhere on C, and that H0(I_C tensor E)=0. The latter is the no-common-section input of PR557, head 212f18bb3afb52171068d1aaf8a0dbfbf9954d2b; it is an additional dependency, not proved again in this note. Then for general H every point of Z_H is active. In particular the residual generic beta lane satisfies

H1(E|D_H)=0 and h0(E|D_H)=26.

Proof. On each component line L_i⊂C, rank-one evaluation defines a regular map κ_i:L_i→Gr(3,U), sending p to ker(U→E_p). For each label i the equality B_H=κ_i(H∩L_i) is an equality of rational maps on the irreducible hyperplane parameter space. It either holds generically or fails on a dense open subset. Taking the intersection of these finitely many dense open subsets makes the generic inactive-label set constant. Equivariance of the beta assignment and evaluation makes this set invariant under the transitive Heisenberg permutation of the 25 lines. It is therefore empty or all 25 labels.

Suppose all labels are inactive generically. Choose two distinct component lines L_i,L_j; they are skew. The rational map H↦(H∩L_i,H∩L_j) is dominant onto L_i×L_j. Indeed for a general pair (p,q), hyperplanes containing the line pq form a projective plane, and a general such hyperplane contains neither L_i nor L_j. Equality of the two kernel maps for general H consequently implies κ_i(p)=κ_j(q) on a dense subset of the product. A map depending only on p and one depending only on q can agree on a dense product only when both are constant with the same value B0. Comparing every other component line similarly gives κ_k≡B0 for all k, and B_H≡B0.

Every section of B0 then vanishes at every point of the reduced curve C. It is therefore in H0(I_C tensor E), contradicting that group's vanishing, since dim B0=3. All-inactive is impossible. Thus all 25 marked points are active for general H, and the preceding five-active-point criterion applies. ∎

The new conclusion closes the on-curve principal-part boundary in the generic residual beta case under the listed public inputs. It does not close the ambient restriction map H0(E)→H0(E|D_H): its source is four-dimensional while the newly computed target is 26-dimensional. No complete repair or beta exclusion follows from this cohomology statement alone.

## Saturated beta line and the 22-dimensional extension space

When every marked point is active, the composite L⊂J→E|D is a line subbundle everywhere. Away from Z, J→E|D is an isomorphism. At each p∈Z, activity states L_p≠ker(J_p→E_p), so the image of its local generator remains nonzero in E_p. A generator nonzero in the fiber of a vector bundle extends to a local basis. Thus the quotient is locally free, including at Z. Taking determinants gives

0 → L → E|D → O_D(Z) → 0,

up to a constant one-dimensional factor fixed by trivializations of det U and U/B. This is an extension, not an asserted splitting.

Both line bundles have degree greater than deg ω_D=4, so H1(L)=H1(O_D(Z))=0 by the same rank-one torsion-free duality argument. Riemann–Roch gives h0(L)=3 and h0(O_D(Z))=23. The long exact sequence independently verifies h0(E|D)=26 and H1(E|D)=0.

Extensions of the displayed type are parametrized, before quotienting by automorphisms or imposing ambient realizability, by

Ext1(O_D(Z),L)=H1(L(−Z)).

Here deg L(−Z)=−20, so H0(L(−Z))=0 and Riemann–Roch gives h1(L(−Z))=22. Thus the remaining on-curve bundle data lie in a specified 22-dimensional extension vector space. This is not a percentage-completion estimate or proof that every extension arises from the ambient HM bundle. In particular it does not count a finite search space, exclude beta, or solve ambient lifting.
