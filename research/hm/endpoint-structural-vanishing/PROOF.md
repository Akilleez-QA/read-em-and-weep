# Structural vanishing of the degree-six Horrocks–Mumford endpoint

Work over C. Let F be the normalized Horrocks–Mumford bundle on Y=P^4, let B=End_0(F), and let M_j=H^1(Y,F(j)). Then

    H^1(Y,B(6))=0.

In particular the fixed quotient Q_0 in PR439/440 is zero, as is the complete paired order-six ideal-coefficient group identified there. The proof below uses published primary cohomology and normalizer representations, but no evaluation of any selected multiplication or section-resolution matrix.

## 1. Pinned inputs

Use the Heisenberg group H and its normalizer N from Horrocks–Mumford (1973), and use E for that paper's bundle. Its normalization is F=E(-3). The following inputs are used:

1. S_1=H^0(O(1))=V^vee, an extending irreducible H-module. This follows from the paper's convention P=P(V) parametrizing lines, Section 1 and printed p. 67.
2. M_3=H^1(E)=W', an irreducible two-dimensional N/H=SL_2(F_5) module, with trivial H-action; this is equation (4.12), printed p. 74, and the appendix p. 81. Its dual is likewise irreducible.
3. The isotypic criterion (2.2), printed p. 67, says that an extending irreducible H-module tensor an irreducible N/H-module is irreducible for N.
4. M is generated in degree zero; dimensions are dim M_2=10 and dim M_3=2. Generation follows from primary equation (4.2), printed p. 72, compatibly with multiplication. The cohomology table is on printed p. 74.
5. F^vee=F(1), H^0(F(-3))=0, and the exact section resolution is

    0 -> 2 O(-8) -> 20 O(-6) -> 35 O(-5)
      -> 15 O(-4) + 4 O(-3) -> F -> 0.                (1)

The resolution is Decker (1990), printed p. 16, Remark 2(ii)-(iii), as pinned in PR167. The cohomology ranges and the kernel-sequence argument of PR440 give the exact presentation

    35 M_2 --D--> 15 M_3 -> H^1(B(6)) ->0.           (2)

Here D is induced by the linear block d:35 O(-5)->15 O(-4) of (1). The other block lands in 4M_4=0. Exactness (2) retains the full incoming differential, not just an upper bound.

Primary sources:
- G. Horrocks and D. Mumford, A rank 2 vector bundle on P^4 with 15,000 symmetries, Topology 12 (1973), 63–81: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
- W. Decker, Monads and cohomology modules of rank 2 vector bundles, Compositio Mathematica 76 (1990), 7–17: https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf

## 2. The top dual multiplication is an isomorphism

Consider the contraction map

    c:S_1 tensor M_3^vee -> M_2^vee,
    c(l tensor lambda)(m)=lambda(l m).               (3)

This is the contraction of the natural module multiplication, not its transpose with an uncontracted S_1^vee factor. Its source contains S_1, not S_1^vee. It is N-equivariant: for g in N,

    c(g l tensor g lambda)(m)
      = lambda(l (g^(-1)m))
      = (g c(l tensor lambda))(m).

It is nonzero because generation in degree zero implies S_1 M_2=M_3, and M_3 is nonzero. Its source is N-irreducible by inputs 1–3. A nonzero equivariant map from an irreducible representation is injective. Both sides of (3) have dimension 10. Therefore c is an isomorphism.

No character comparison with repeated multiplicity spaces is used: irreducibility of this single source forces injectivity, and the independently known dimensions force surjectivity.

## 3. No constant row annihilates the section-resolution linear block

Write U=C^15 and R=C^35 for the multiplicity spaces in (1). The linear block d is an element of Hom(R,U) tensor S_1. Its constant-row map is

    rho:U^vee -> R^vee tensor S_1,
    a |-> a d.                                      (4)

We claim rho is injective. Suppose a d=0. Define the sheaf morphism

    (a,0): U tensor O(-4) + C^4 tensor O(-3) -> O(-4).

It annihilates the full image of R tensor O(-5) in (1), since it ignores the second summand and its composition on the first is precisely a d. Exactness of (1) therefore makes it descend to a morphism

    F -> O(-4).

But Hom(F,O(-4))=H^0(F^vee(-4))=H^0(F(-3))=0. Thus (a,0)=0, and consequently a=0. This proves the claim. Only exactness and a vanishing of global sections are used; no entries of d have been chosen or evaluated.

## 4. Dualizing the retained incoming map

The dual of D in (2) is

    D^vee: U^vee tensor M_3^vee -> R^vee tensor M_2^vee.

By its definition as multiplication by the linear entries of d, it factors as

    U^vee tensor M_3^vee
      --rho tensor id--> R^vee tensor S_1 tensor M_3^vee
      --id tensor c--> R^vee tensor M_2^vee.         (5)

For example the component attached to a relation r is the sum of the functionals m |-> lambda_j(d_jr m), exactly as (3) prescribes. This verifies (5) without any coordinate evaluation of those linear entries.

The first arrow in (5) is injective by Section 3, and the second is an isomorphism by Section 2. Thus D^vee is injective. Finite-dimensional duality implies that D is surjective. The exact cokernel in (2) is zero, proving H^1(B(6))=0.

## 5. Fixed endpoint and subsequent coefficient consequence

For any quadratic q and cubic r, the quotient

    H^1(B(6))/(q H^1(B(4))+r H^1(B(3)))

is zero because its target is zero. This includes the original fixed u_0,v_0 without translating either them or F. Let E_pair=q^*B tensor A^(-2) denote the paired coefficient sheaf called E in PR439, distinct from the primary paper's rank-two E above. In particular PR439 gives

    H^2(Z,I_D^6 E_pair)_chi=0.

Together with PR437's already-established vanishing for every k>=7, the complete paired ideal-coefficient group vanishes for every k>=6. Thus any class represented in I_D^6 E_pair has zero image in the corresponding paired unrestricted cohomology group. This is only a sufficient coefficient-filtration statement: the actual source has not been shown to admit such a representative, and no primitive has been constructed.

The exact quotient presentation in PR440 now also proves that its reduced incoming map is surjective for every pair (q,r). No assumption about the possibly nonzero primary quotient M_3/(qM_1+rM_0) is needed. PR449's classification of that primary quotient's quadratic failure locus remains valid, but primary rank failure does not produce a surviving End(F) endpoint class.

No optimality assertion for order six follows. No conclusion about the six pure diagonal conditions, actual source membership, module lifting, or quantization algebraicity follows.

## Dependencies and comparison

- PR440 exact incoming-map presentation, commit 829e03411d04511f6cf04860bf18db4a70b12448:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/829e03411d04511f6cf04860bf18db4a70b12448/research/hm/degree-six-structural-reduction/PROOF.md
- PR439 complete paired endpoint identification, commit bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b/research/hm/paired-collision-endpoint/PROOF.md
- PR437 coefficient filtration and k>=7 conclusion, commit 50e82ed233cd7729c38608194f990376eb832418:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/50e82ed233cd7729c38608194f990376eb832418/research/hm/paired-collision-filtration/PROOF.md
- PR167 cohomology and section resolution, commit 063da90fc4543304e87e701cdefcc08225412f17:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/PROOF.md
- PR449 normalizer conventions, commit e4b6acdd27d8da8be4052c117ea2dca0f48f46ff:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/e4b6acdd27d8da8be4052c117ea2dca0f48f46ff/research/hm/quadratic-failure-cone/PROOF.md

The proof does not import the computationally obtained tensor-cohomology table in Calvo–Andrade, Corrêa and Fonseca–Quispe, Dimension two holomorphic distributions on four-dimensional projective space, arXiv:2207.08901v5 (https://arxiv.org/pdf/2207.08901v5), Lemma 2/Table 2. That source asserts the same vanishing after normalization. The associated Fonseca–Quispe thesis (https://repositorio.ufmg.br/bitstream/1843/38398/1/Tese_Horrocks%20Mumford%20Holomorphic%20Distributions.pdf), Lemma 4 printed p. 60, attributes this positive-range vanishing to Macaulay2. The present derivation independently supplies the needed structural surjectivity; no source computation was rerun.

Current PR1 and relevant PR439/440/449 were read on 2026-10-20. This is a bounded comparison, not an exhaustive novelty claim. The new contribution relative to these dependencies is Sections 2–4, which force the retained incoming map to be surjective. Mathematical text review is distinct from formal proof verification.
