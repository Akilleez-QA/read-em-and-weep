# No length-two isolated defect on the unique 250-point orbit

## Result

Let G = F5² ⋊ SL2(F5) act on P(V), dim V = 5, through the standard projective Schrödinger normalizer, and let N = H5 ⋊ SL2(F5) ⊂ SL(V) be the stipulated determinant-one lift. Let B be an N-equivariant rank-two reflexive sheaf with equivariantly trivial determinant and isolated singularities. Put T = Ext²(B,O).

At every point p of the unique G-orbit of size 250, a nonzero stalk T_p has length at least three. Thus this orbit, if supported, contributes at least 750 to length(T).

The new assertion is the exclusion of length two. Length one was excluded in ../normalizer-250-simple-defect/PROOF.md. This argument does not exclude canonical local length ten or assert existence of a defect of length three on the 250-point orbit.

## 1. The full linear stabilizer

The established 250-point orbit proof shows that, after conjugation by an element of the projective Heisenberg subgroup and lifting that conjugation to N, the projective stabilizer of p is the subgroup

    L = <a,u> ⊂ SL2(F5),
    a³ = 1, u⁴ = 1, uau⁻¹ = a⁻¹,
    u² = c = -I.

It has order twelve and is Dic3. The point p is the unique L-stable line ℓ in V. The same proof gives

    Spec(a|V) = {1,ω,ω,ω²,ω²},
    a|ℓ = 1,       u|ℓ = -1,

where ω is a primitive cube root of unity.

Let H = N_p. The kernel of N → G is precisely the scalar μ5, and the chosen complement SL2(F5) projects injectively into G. Hence L ∩ μ5 = {1}. Every lift of a projective element of L differs from its chosen lift in L by a scalar in μ5. Since these scalars are central,

    H = μ5 × L.

In particular |H| = 60. This is the full stabilizer, not only a subgroup with the same projective action. Before conjugation, its corresponding conjugate has the same properties.

For every one-dimensional character θ of H, the inversion relation gives θ(a) = θ(a)⁻¹. Together with θ(a)³ = 1, this implies θ(a) = 1. The central μ5 factor can carry arbitrary characters and does not change this conclusion.

## 2. Cotangent weights and length-two finite modules

Set R = O_{P(V),p}, m = m_R, and W = m/m². This is a regular local complex ring of dimension four. The tangent representation is Hom(ℓ,V/ℓ). Since a acts on ℓ trivially and on V/ℓ with eigenvalues ω,ω,ω²,ω², the cotangent representation has precisely the same multiset of eigenvalues after inversion:

    Spec(a|W) = {ω,ω,ω²,ω²}.

In particular W has no a-fixed vector. The scalar μ5 acts trivially on the base and on W; this does not require it to act trivially on an equivariant module fibre.

Let Q be any H-equivariant finite R-module of length two. Since the residue field is C, its complex dimension is two. There are two possibilities:

- mQ = 0, in which case Q is k² as an R-module, with an arbitrary compatible two-dimensional H-representation;
- mQ ≠ 0, in which case mQ and Q/mQ each have length one.

In the second case, Nakayama's lemma shows that m²Q = 0 and that Q is cyclic. Equivalently its annihilator quotient is a local length-two complex algebra, isomorphic to C[ε]/(ε²). The invariant submodule and quotient have characters

    mQ = k_ψ,       Q/mQ = k_χ.

Multiplication induces a nonzero, indeed surjective, H-map

    W ⊗ χ → ψ.

But χ(a) = ψ(a) = 1, whereas W has only the nontrivial a-eigenvalues ω and ω². No such map exists. Therefore every H-equivariant length-two finite R-module is annihilated by m. This assertion includes all central characters and does not assume decomposition into one-dimensional H-representations in the semisimple R-module case.

## 3. Why a semisimple length-two Ext² is impossible

For clarity, the relevant universal algebra bound is reproduced from ../../local-defect/length-two-local-defect/PROOF.md, Section 3. It does not depend on the stabilizer.

Let M be a reflexive rank-two module over a regular local complex ring R of dimension four, free on the punctured spectrum and self-dual. If

    D = Ext²_R(M,R) = k^n,       n > 0,

then n ≤ 1.

Indeed isolated-singularity duality and self-duality give

    A = Ext¹_R(M,R) ≅ Ext⁴_R(D,R) ≅ k^n

as nonequivariant R-modules. Reflexivity gives projective dimension at most two. In a minimal free resolution

    0 → F2 → F1 → F0 → M → 0,

the dual last differential has cokernel D. Minimality gives rank F2 = n and image mR^n. Since μ(mR^n) = 4n, write rank F1 = 4n + t, with t ≥ 0. Splitting off redundant generators of a free cover of mR^n shows

    K := ker(F1* → F2*) ≅ K0^n ⊕ R^t,

where K0 is the kernel of a regular parameter row R⁴ → m. The Koszul resolution gives μ(K0) = 6, so μ(K) = 6n + t. With C = im(F0* → F1*), there is an exact sequence

    0 → C → K → A → 0.

Tensoring with k shows that the image of C/mC in K/mK has dimension (6n+t)-n. Consequently μ(C) ≥ 5n+t. But rank counting gives

    μ(C) ≤ rank F0 = rank F1 - rank F2 + 2 = 3n+t+2.

Thus 2n ≤ 2, as asserted. In particular n = 2 is impossible.

For M = B_p, all assumptions hold: reflexivity and rank two are stipulated; isolated singularities imply local freeness on the punctured spectrum; and the determinant pairing identifies M with M* because det M is trivial. Equivariant triviality makes this identification H-equivariant as well, although the numerical semisimple bound only needs the underlying self-duality. If the global hypotheses initially supply only det B ≅ O on P(V), the perfectness of N established in ../../local-defect/minimal-local-defect-character/PROOF.md, Section 4, gives equivariant triviality for its N-linearization. No triviality of an arbitrary local determinant character is inferred without that global input.

Combining Section 2 with this bound excludes length(T_p) = 2.

## 4. Length one and the resulting orbit contribution

The already proved length-one obstruction states that, for an isolated self-dual rank-two reflexive module with equivariantly trivial determinant and D = k_χ,

    (det W)³ = χ⁻⁴.

At p, the actual element u in N has order four and eigenvalue -1 on ℓ. Since N ⊂ SL(V), the cotangent determinant on an element with line eigenvalue λ is λ⁵. Therefore det W(u) = -1. Evaluating the identity at u contradicts χ(u)⁴ = 1. This independently records why length one is excluded under the same hypotheses.

Hence nonzero T_p has length at least three. Equivariance makes this local length constant on its orbit. The unique 250-point orbit therefore contributes at least 250 × 3 = 750.

This conclusion may be combined with separately audited exclusions on other small orbits. It does not, by itself, establish that every total below 600 has canonical support: that further statement also needs the exclusions for the 300-, 375-, and 500-point orbits and the orbit-size gap. No such outstanding result is assumed here. No canonical local-length exclusion is added by this proof.

## Evidence boundary

Inputs read: ../normalizer-250-simple-defect/PROOF.md; ../../local-defect/length-two-local-defect/PROOF.md; and ../../local-defect/minimal-local-defect-character/PROOF.md. These supply the universal stabilizer spectrum, isolated local duality, and the length-one obstruction. All additional steps use finite-group representations and regular local algebra only. There was no evaluation of an actual physical source, operation, model, rank instance, jet, or residue; no external write, upstream change, installation, subgroup search, or large computation. 
