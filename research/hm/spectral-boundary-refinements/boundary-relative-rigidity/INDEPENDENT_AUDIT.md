# Independent audit: determinant boundary over the polar scheme

## Verdict

The proposed scheme upgrade is valid over arbitrary nilpotent test bases. Let R be the finite rectangular determinantal scheme from `https://github.com/Akilleez-QA/read-em-and-weep/blob/85402222aca57fa071310a21f421755ecf35fe42/research/hm/incidence-foundations/finite-rectangular-incidence/PROOF.md`, let B be its actual determinant-zero boundary (not its reduction), and let D be the determinantal polar-pair scheme. Then the intersection-line morphism B → D exists on the original schemes, is finite and unramified, and has geometric fibers reduced of length 0, 1, or 3. Consequently

    length_C(B) ≤ 3 length_C(D).

Here D must carry the determinantal scheme structure, not merely its reduced support. There is no assertion that B → D is flat or étale, and no assertion that B itself is reduced.

The audit uses the hypotheses and pointwise exclusions in the two supplied proofs. It does not independently reprove their separate theorem that the polar support is finite.

## 1. Constant-rank assertions really hold over nilpotents

A matrix with an invertible r-minor can be reduced by invertible row and column operations to a block matrix diag(I_r,S). If its (r+1)-minors vanish as functions, then every entry of S is zero. Thus its kernel, image, and cokernel are locally free. Merely having rank r on geometric points would not suffice, but the required equations are present here.

For the square rank-five addition map X ⊕ Y → V on B, an invertible 4-minor exists near every point by the pointwise exclusions. Its Schur complement is a single scalar, killed by the defining determinant equation of B. Thus the kernel is a line bundle and the image is a rank-four subbundle H_B. Projection of the kernel into X or Y identifies it with their intersection line h_B. This is a subbundle of V: its vector is nonzero modulo every residue field, hence has a unit coordinate locally. It gives a genuine morphism B → P(V).

Likewise the mixed map X ⊗ U ⊗ Y → J has all 2-minors zero by the defining equations of R. The value f(h,u,h) is nonzero on every geometric fiber and belongs to this image. Locally it supplies an invertible entry after choosing frames, so the image is a line subbundle L_B and f(h,u,h) generates it locally.

The polar map P=f(h,u,-), in local frames for h and u, sends H_B to L_B, since h belongs to both X and Y. Hence P has rank at most two as an actual matrix over the base ring, not only after reduction. Its values on h and u are independent on residue fields, so it has an invertible 2-minor locally. It therefore has rank exactly two as a bundle map. Its 3-minors vanish, giving a factorization B → D on the determinantal schemes.

Finally H_B=P⁻¹(L_B) as subbundles. Indeed, modulo L_B the polar is a split rank-one map, so the inverse image is a rank-four subbundle. The inclusion of H_B in this inverse image is an isomorphism on every residue field, hence is an isomorphism over the local ring. The local choices of frames only multiply the relevant expressions by units and do not affect the construction.

## 2. The scheme-theoretic fiber, not just its points

Fix a closed polar pair (h,u). Its P,L,H,E=H/Ch and β:E×E→J/L are those of `../boundary-rectangle-choice-bound/PROOF.md`. For an arbitrary C-scheme T, a T-point of the fiber of B → D has intersection line equal to the constant h and, by the bundle equality above, sum equal to the constant H. Thus its quotients give a decomposition

    E_T = a ⊕ C,    rank(a)=1, rank(C)=2,    β(a,C)=0.

Conversely any such decomposition gives X and Y by inverse image in H_T. Their intersection is h_T, their sum is H_T, the addition determinant vanishes identically, and their mixed image is contained in the fixed L_T. It contains the fixed nonzero f(h,u,h), so the rectangular equations hold scheme-theoretically. These constructions are inverse and commute with base change.

Choose a nondegenerate scalar member q of β using the maximal-rank argument in the supplied proof. The scalar condition q(a,C)=0 makes C=a^⊥. Because a ⊕ C=E_T, q restricted to a is invertible, so a is nonisotropic. Conversely, on the nonisotropic line locus the orthogonal complement is a rank-two direct complement. Thus the decomposition scheme equals the common-eigenline scheme for the q-selfadjoint operators T_λ, restricted to the nonisotropic open subset.

Every geometric common eigenline is nonisotropic by β(v,v)≠0. Since the eigenline scheme is finite type over C, its intersection with the isotropic closed locus is empty as a scheme if it has no closed points. Therefore restricting to the nonisotropic open loses no part of the eigenline scheme, including nilpotent structure. This verifies the claimed scheme identification.

## 3. Tangent calculation and reducedness

At a common eigenline Cv, write T_λv=μ_λv and q(v,v)≠0. A tangent vector to P(E) can be uniquely represented by w∈v^⊥. Its membership in the tangent space of the common-eigenline scheme says

    T_λw = μ_λw + ν_λv

for suitable scalars ν_λ. Pairing with v and using selfadjointness gives ν_λq(v,v)=0, hence ν_λ=0. Thus w is a joint eigenvector with exactly the same eigenvalue tuple as v.

If w≠0, then v,w are independent. Every vector z in their span has

    λβ(z,z)=μ_λq(z,z) for every λ.

A complex quadratic form on a two-dimensional space has a nonzero isotropic vector z. This would give β(z,z)=0, contradicting the no-projective-zero lemma. Therefore w=0.

All tangent spaces of this fiber vanish. At each closed point, m/m²=0 in its Noetherian local ring, so Nakayama gives m=0. Thus the fiber is reduced. The point classification already proved gives its length 0, 1, or 3.

The tangent calculation does not assume the T_λ commute or are simultaneously diagonalizable. Choose a finite basis of (J/L)* if a finite list of equations is wanted.

## 4. Finite and unramified over the full Artin base

Because B and D are finite C-schemes, every C-morphism B → D is finite. The sheaf Ω_(B/D) is coherent, and its restriction to each geometric fiber is the differential sheaf of that fiber, which is zero. Nakayama at each point gives Ω_(B/D)=0. The morphism is finite type and the residue field extensions are C/C, so it is unramified. Equivalently one can use the standard finite-type criterion that all geometric fibers are zero-dimensional and reduced.

For complete control of lengths, decompose D into its local Artin factors A. The finite A-algebra of B over such a factor decomposes as a product of local Artin rings B_i, one for each point of the geometric fiber. Reducedness of that fiber gives

    B_i / m_A B_i = C,

and in particular m_(B_i)=m_A B_i. To prove A → B_i is surjective, apply Nakayama to the finite A-module

    M = B_i / (A·1).

The residue equality says M=m_A M, so M=0. Therefore B_i ≅ A/I_i as A-algebras. This proof does not require injectivity of A → B_i, flatness, or a splitting of that map.

There are at most three local factors above each point of D, and each has C-length at most length_C(A). Summing proves the stated bound. The description by quotient factors is the precise meaning of nilpotents being inherited from the base; it should not be described as an étale or flat local cover.

## 5. Limits of the conclusion

- Using only #D, rather than length(D), would discard possible base nilpotents and is not justified for scheme lengths.
- It is essential that B is defined by the actual determinant equation. A structure with the same boundary support but weaker equations would not automatically have a line-bundle intersection.
- A local factor A/I is generally not flat over A. Reduced geometric fibers do not imply that the total space is reduced or that the map is étale.
- The statement controls the determinant boundary scheme. It does not bound the full rectangular scheme R or identify its complementary component lengths.



## Status of this record

This is a historical mathematical audit, not a new formal verification or a new execution of tests.
