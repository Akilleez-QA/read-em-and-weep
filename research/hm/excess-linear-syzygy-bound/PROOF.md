# A two-valued quadratic-generator ambiguity for the excess factor

Conditional input: PR498 defines the two-step S=Sym(T)-module C with T=V*, C_0=A, C_1=V tensor W, and its unique nonzero normalizer-equivariant multiplication mu:T tensor A -> V tensor W. Here dim A=dim V=5 and dim W=2. The pinned normalizer identity exterior^2 V = A tensor W is used, and W is self-dual. Work over C.

Let b be the number of minimal quadratic generators of the relation module of C. Then b is either 0 or 24.

## Koszul interpretation

Write B=C_1. The degree-two Koszul differential is

D: exterior^2 T tensor A -> T tensor B,
D((s wedge t) tensor a)=t tensor mu(s,a)-s tensor mu(t,a).

Both spaces have dimension50. Koszul homology gives beta_(2,2)(C)=dim ker D and beta_(1,2)(C)=dim coker D. Hence these numbers equal b.

## No invariant kernel

Choose the equivariant identification p:A tensor W -> exterior^2 V. Contraction defines

mu_0(t,a)(w)=i_t p(a tensor w),

with target V tensor W*. This map is nonzero: otherwise all contractions of all two-vectors would vanish. By multiplicity one, after identifying W* with W, it is a nonzero scalar multiple of mu. It therefore suffices to use mu_0.

The dual identification is exterior^2 T = A* tensor W*. Choose a basis a_i of A with dual a_i*. For eta in W*, let alpha_i(eta) be the two-form corresponding to a_i* tensor eta. Then

k(eta)=sum_i alpha_i(eta) tensor a_i

parametrizes all Heisenberg-invariant elements in exterior^2 T tensor A. Under the natural identification T tensor V=End(V), trace the output D(k(eta)) in its T tensor V factors and evaluate the W* factor on w. For a decomposable two-form s wedge t and two-vector beta, the trace of

t tensor i_s beta - s tensor i_t beta

is 2(s wedge t)(beta), with the displayed contraction convention. Therefore

trace(D(k(eta)))(w)
 =2 sum_i alpha_i(eta)(p(a_i tensor w))
 =2 sum_i a_i*(a_i) eta(w)
 =10 eta(w).

Thus D is injective on its entire invariant subspace; a different consistent sign convention merely changes the nonzero factor's sign.

## Orbit multiplicities and exclusion of dimension48

The center of the Heisenberg group acts trivially on both sides of D. The source, restricted to the quotient Heisenberg group, is End(A) tensor W*. End(A) contains each of its25 characters once; W* is trivial on this group. The invariant character therefore occurs twice and each of the24 nontrivial characters twice. The normalizer permutes those24 nontrivial characters transitively. Since ker D is normalizer-stable and has no invariant part, its dimension is 24r with r in {0,1,2}.

The value r=2 would give rank D=2. To exclude it without any matrix or source-instance evaluation, choose t in T and a in A with mu(t,a) nonzero. Let t_1,...,t_4 represent a basis of T/<t>. Modulo <t> tensor B, the four outputs D((t wedge t_i) tensor a) are the four independent tensors t_i tensor mu(t,a), up to a common sign. Hence rank D is at least4. Consequently r is0 or1, proving b in {0,24}.

This argument does not establish b=0. It is a universal contraction and character-orbit argument, not a numerical rank calculation or evaluation of a selected HM/source instance. It determines an actual restriction on minimal syzygies beyond the presentation and Hilbert function. It has independent and root mathematical review, conditional on the pinned inputs; it is not formally checked by a proof assistant.

## Minimal presentation and the pure branch

There are exactly fifteen minimal linear relations, since dim(T tensor A) minus dim C_1 is 25 minus 10. All further defining relations are generated in degree two because C has no higher components. Hence F_1(C)=15S(-1) plus bS(-2), with b in {0,24}.

If b=0, then beta_(2,2)=0. Minimality and exactness exclude all subsequent diagonal terms beta_(i,i): a lowest-degree generator with no possible nonzero differential would be a constant element of a kernel but could not lie in the next minimal image. Regularity is one, and the Hilbert numerator is

5−15t+50t³−75t⁴+45t⁵−10t⁶.

Thus the b=0 branch has the full pure resolution

0 → 10S(-6) → 45S(-5) → 75S(-4) → 50S(-3) → 15S(-1) → 5S → C → 0.

This does not exclude b=24 or select the pure branch. The endomorphism rigidity of C alone does not settle that alternative.

## Pinned dependencies and boundary

- PR498, the actual two-step module, multiplication and character orbit: https://github.com/Akilleez-QA/read-em-and-weep/blob/77018c2e6904a4ef9adfee5f2f48e49894b63fe9/research/hm/determinantal-excess-module/PROOF.md
- PR489, normalizer tensor conventions: https://github.com/Akilleez-QA/read-em-and-weep/blob/5637cdd610fc2ec8ffbbbbfc7627b2d6c54f6873/research/hm/scalar-quartic-generators/PROOF.md
- Horrocks–Mumford, Lemma 3.3 and Appendix: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

No original fixed-pair/source values, higher-order lifting or algebraicity conclusion is asserted. The remaining b alternative is genuine uncertainty. No selected-instance numerical matrices, coefficient search or large computation were used.
