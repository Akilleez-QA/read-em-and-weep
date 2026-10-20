# Structural twist-one vanishing and cubic generation

Work over C on P^4. Let F be the normalized Horrocks–Mumford bundle and B=End_0(F). We prove H^2B(1)=0 without evaluating a Horrocks–Mumford differential. Consequently S_3 H^1B(2)=H^1B(5).

## Inputs

Use the normalized monad A⊗O(-1) → 2Ω²(2) → C⊗O, with dim A=dim C=5, exact at its ends and middle cohomology F. Here C=A* in the normalizer notation of PR454, and its Heisenberg central weight is 3; T=H^0O(1)=V* has central weight 4. This is Horrocks–Mumford (1973), §2, sequence (2.3), twisted by −3, using Λ²T_{P4}(-3)=Ω²(2).

Import from PR454 at 2124f284c3bc488bd0c666c61d4347e3b8950f08 its exact Koszul transgression sequence, the alternatives dim H^2B(1)∈{0,10,20,30}, and its generation in twists 4,5. Import the primary module generation in degree 0 and dim H^1F(1)=10 from the primary resolution. The section-resolution surjection p_3:H^1E_0(3)→H^1B(3) is the pinned structural input of PR440, also used in PR454. None of these inputs is a computational tensor table.

## 1. A universal exterior-image estimate

Let C,T be five-dimensional vector spaces and R⊂C⊗T a 15-dimensional subspace. Then the map

C⊗R → Λ²C⊗T,  c⊗(c'⊗t) ↦ (c∧c')⊗t

has rank at least 30.

Choose bases of C,T and a one-parameter diagonal subgroup whose 25 weights on C⊗T are pairwise distinct. The Grassmannian limit R_0 of R exists and is invariant under that subgroup. Since all its weight spaces are one-dimensional, R_0 is a coordinate subspace. If r_j basis vectors occur over the j-th T-basis vector, then Σr_j=15 and 0≤r_j≤5. Its exterior image in Λ²C⊗t_j has dimension

10−binom(5−r_j,2)=r_j(9−r_j)/2 ≥2r_j.

Summing gives rank at least 30 for R_0. The exterior map is equivariant under this subgroup, so its rank is constant on the nonzero points of the degeneration and cannot increase at the limit. This proves the assertion for R. This is a universal linear-algebra estimate, not an evaluation of any particular bundle map.

## 2. The symmetric-square monad

Put K=Ω²(2). In characteristic zero the graded symmetric square of the monad is a complex in degrees −2,…,2,

Λ²(A⊗O(-1)) → (A⊗O(-1))⊗2K → Sym²(2K)⊕(A⊗C⊗O(-1)) → 2K⊗C → Λ²C⊗O,

quasi-isomorphic to Sym²F=B(-1). This follows locally by splitting the monad into F in degree zero and contractible complexes; symmetric squaring preserves the resulting quasi-isomorphism.

First, H^3B(-1)=0. Indeed every term on total degree 3 of its hypercohomology spectral sequence vanishes. The only non-immediate central term is H^3 Sym²(2K). The exterior Euler resolution

0→K→Λ²T⊗O→T⊗O(1)→O(2)→0

when tensored by K resolves K⊗K by copies of K,K(1),K(2). These have no higher cohomology by Bott, hence H^i(K⊗K)=0 for i≥3. Since Sym²(2K) is a direct summand of 4(K⊗K), its H^3 vanishes. The other total-degree 3 terms are H^5(10O(-2)), H^4(10Ω²(1)), H^3(25O(-1)), H^2(10Ω²(2)), and H^1(10O), all zero by dimension or Bott.

Next twist the symmetric-square complex by 1. Every term now has vanishing positive cohomology. For the central term, write Q for the rank-four universal quotient, so K=Λ²Q*. The elementary Schur decompositions are

Sym²K=S_(2,2)Q* ⊕ Λ⁴Q*,  Λ²K=S_(2,1,1)Q*.

Bott makes S_(2,2)Q*(1) and S_(2,1,1)Q*(1) acyclic; Λ⁴Q*(1)=O. Explicitly the shifted Bott weights are (5,5,4,1,0) and (5,5,3,2,0), each having repeated entries. This proves the assertion for Sym²(2K)(1), and the remaining terms O(-1),10K,25O,10K(1),10O(1) are immediate.

It follows that H^2B is the cokernel of the final map of global sections:

H^0(2K(1))⊗C → Λ²C⊗T.

If R is the image of H^0(2K(1))→C⊗T from the original monad, this is exactly the exterior image of C⊗R (up to an irrelevant nonzero scalar). Twisting the monad by 1 shows coker(H^0(2K(1))→C⊗T)=H^1F(1): the left term is 5O and has no higher cohomology. Thus dim R=25−10=15. Section1 gives h^2B≤50−30=20.

## 3. Heisenberg symmetry improves the bound to two

The target Λ²C⊗T has trivial central character. Since C has central weight 3, Λ²C has central weight 1 and dimension 10. The Heisenberg irreducibility theorem therefore identifies Λ²C with 2V as an H_5-module. Consequently

Λ²C⊗T ≅2End(V) as H_5-modules.

The conjugation representation End(V) is the regular representation of H_5/Z(H_5): its 25 characters each occur once. Thus the invariant part of the target has dimension 2. The normalizer quotient SL_2(F_5) acts transitively on the 24 nontrivial characters. Any normalizer-equivariant quotient with a nonzero nontrivial-character part therefore has dimension at least 24. Since H^2B is such a quotient and has dimension at most 20, that part is zero. Exactness of invariants in characteristic zero now yields

h^2B(0)≤2.

This bound is obtained from a universal exterior-image estimate and symmetry, not from a numerical tensor-cohomology table or a selected matrix.

## 4. The dimension gap forces twist-one vanishing

Let Z=H^2B(1) and C_3=coker(T⊗H^1B(2)→H^1B(3)). PR454 gives an exact sequence

A_3 → coker(Λ³T⊗H^2B(0)→Λ²T⊗Z) → C_3 →0,

where A_3 is a quotient of Λ⁴T⊗H^3B(-1). Section2 makes A_3=0, so the displayed cokernel is isomorphic to C_3. Hence

dim C_3 ≥10 dim Z−10h^2B(0) ≥10 dim Z−20.

On the other hand, the section-resolution map p_3 is surjective, with source

H^1E_0(3)=B_04⊗M_0 ⊕ T_4⊗M_1.

Primary generation gives M_1=T M_0. Naturality of p_t therefore puts the entire second summand into T H^1B(2). Thus C_3 is a quotient of B_04⊗M_0, which has dimension15·5=75.

If Z were nonzero, PR454's irreducible-channel alternatives would give dim Z≥10. The lower bound would then give dim C_3≥80, contradicting dim C_3≤75. Therefore Z=0. In the notation of PR454, both twist-one scalar components alpha and beta are nonzero.

The exact sequence for Delta in PR454 also identifies H^1B(1)=V*⊗(R⊕J), of dimension 55: its W and Q components map isomorphically to the target, while its R and J components are the kernel.

The exact Koszul sequence gives C_3=0. Combining this with the already proved surjectivity of multiplication in twists4 and5 gives

S_3 H^1B(2)=H^1B(5).

## 5. The canonical defect supplies the non-primary target

Use PR452's canonical splitting H^1B(2)=I_2⊕j(C_2) and let L=S_3I_2. Universal cubic generation gives

H^1B(5)=L+im[S_3⊗C_2→H^1B(5)].

Thus the canonical defect cubic map surjects onto H^1B(5)/L. PR453 identifies L as H_5-trivial and defines the canonical N-stable summand K_nontriv as the sum of the nontrivial H_5/Z-character spaces of H^1B(5). Projection kills L, so the composite

S_3⊗C_2→H^1B(5)→K_nontriv

is surjective. In particular the full canonical defect, not merely the primary image, supplies the entire nontrivial character orbit whose dimension is at least 24. This settles the universal missing-orbit question of PR453. No assertion is made that a single canonical channel suffices, or that multiplication by one fixed cubic is surjective.

## Scope

This proves universal cubic generation, not vanishing of the quotient for one fixed cubic v, nor vanishing of the fixed-pair order-five quotient. It does not prove actual-source membership, a higher-order lift, or algebraicity. No selected HM/source-instance map, numerical rank, generator/checker, or large computation is used. Mathematical review is distinct from formal verification.

## Public dependencies

- Horrocks and Mumford (1973), §2: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
- PR454, exact transgressions and channels: https://github.com/Akilleez-QA/read-em-and-weep/blob/2124f284c3bc488bd0c666c61d4347e3b8950f08/research/hm/twist-one-transgression/PROOF.md
- PR440, natural primary surjections: https://github.com/Akilleez-QA/read-em-and-weep/blob/829e03411d04511f6cf04860bf18db4a70b12448/research/hm/degree-six-structural-reduction/PROOF.md
- PR167, primary module and section resolution: https://github.com/Akilleez-QA/read-em-and-weep/commit/063da90fc4543304e87e701cdefcc08225412f17

The comparison is bounded to these pinned dependencies and current coordination, not a claim of priority over the full literature.

- PR452, canonical defect splitting: https://github.com/Akilleez-QA/read-em-and-weep/blob/3b1d18105fa8b8b39bd96d889a34bc81a860f181/research/hm/cubic-defect-channels/PROOF.md
- PR453, canonical non-primary summand: https://github.com/Akilleez-QA/read-em-and-weep/blob/56516a96a7eacfde0c8e272ca38db415cc7f294b/research/hm/cubic-invariant-target/PROOF.md
