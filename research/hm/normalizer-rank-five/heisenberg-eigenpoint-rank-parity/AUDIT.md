# Independent audit: even residual ranks at least four at Heisenberg eigenpoints

## Verdict

**PASS, including the strengthened Section 7.** Under the full hypotheses stated in `PROOF.md`, the residual rank belongs to {4,6,8,10} at each of the thirty canonical Heisenberg eigenpoints. The parity conclusion alone does not require repeated-input injectivity; the stronger lower bound does. No mathematical flaw was found, and no existence of an allowed rank is claimed.

This audit uses only abstract representation identities, invariant kernels, and finite-group actions. It contains no evaluation of an actual source operation, source matrix, or geometric rank instance.

## 1. Residual descent, kernel equivariance, and twists

Outer symmetry gives f(v,u,u)=f(u,u,v). The cyclic identity with all three arguments equal gives 3f(u,u,u)=0, hence f(u,u,u)=0 over C. Consequently the composite of the middle-input map Sym²V → J with J → J/R_u kills uV and descends to Sym²(V/Cu). This establishes exactly the residual map used in the argument.

For a lift g fixing u, natural equivariance gives preservation of R_u and preservation of the residual kernel. This remains valid if equivariance for that chosen lift includes a nonzero scalar: the scalar does not affect whether the residual image is zero. More explicitly, replacing an equivariant lift by a scalar multiple rescales the trilinear output uniformly and does not change the subspace R_u or the vanishing condition. Thus the proof needs an honest action on the input kernel, not an independently chosen honest action on J/R_u.

Each of Z,D,T fixes e_0 as a vector. Therefore the tautological factor U and its dual have trivial action for these chosen lifts. No missing tautological character changes the kernel calculation. This reasoning depends on the stated natural homogeneous equivariance; it does not assert equivariance for an arbitrary nonequivariant operation.

## 2. Exact matrix relations and normalizer membership

On basis vectors, direct universal representation calculations give

- D X D⁻¹ e_i = ζ^(2i+1)e_(i+1), hence D X D⁻¹ = ζ X Z²;
- T X T⁻¹ = X² and T Z T⁻¹ = Z³, since 2⁻¹=3 in F_5;
- T D T⁻¹ e_i = ζ^(9i²)e_i = ζ^(4i²)e_i, hence T D T⁻¹=D⁴=D⁻¹.

The other listed relations follow immediately from diagonality and the order of 2 in F_5×. The induced label transformations of D and T have determinant one. Both normalize the projective Heisenberg group, as required.

The restriction of ⟨Z,D⟩ to E is faithful: its values at indices 1 and 4 give a+b=0 and −a+b=0, implying a=b=0. Nontrivial powers of T are nontrivial permutations of the four basis vectors of E and cannot belong to this diagonal subgroup. Hence the generated group really is C_5² ⋊ C_4 of order 100; there is no overlooked central scalar relation affecting the claimed module action.

## 3. Character separation and the multiplier action

The B-character of e_i e_j is (i+j,i²+j²). These two entries determine i+j and ij, and therefore the unordered multiset {i,j}, including repeated indices. Thus the ten monomials have pairwise distinct characters. For s=0, j=−i and t=2i² is nonzero, excluding the trivial B-character.

For an independent check, the three ordered T-orbits have the following character lists, with entries taken in F_5:

- Squares: (2,2), (4,3), (3,2), (1,3).
- Adjacent pairs: (3,0), (1,0), (2,0), (4,0).
- Opposite pairs: (0,2), (0,3).

These are ten distinct pairs. The transformation is (s,t) ↦ (2s,4t). This correctly uses inverse conjugation to compute the character on Tv; it is consistent with T Z T⁻¹=Z³ and contains no inversion error.

## 4. Orbit decomposition and parity

The explicit monomial orbits in `PROOF.md` are correct and have sizes 4,4,2. Because B is finite abelian over C and these characters are distinct, every B-invariant subspace is a sum of the corresponding individual character lines. T-invariance then forces its character support to be a union of the three whole orbits.

Applied to the residual kernel, its dimension is a subset sum of 4,4,2, hence one of 0,2,4,6,8,10. Subtracting from dim Sym²E=10 gives precisely the claimed possible even ranks. The irreducibility and absence of diagonal mixing asserted in the proof follow from the same character-support argument.

The separate rank-one argument is also sound: a one-dimensional quotient has Z and D eigenvalues constrained by conjugation to be trivial, while no trivial B-character occurs in the source. Semisimplicity of the B-action justifies passing from absence in the source to absence in any quotient.

## 5. Transport to thirty eigenpoints

I checked the specific canonical-orbit claim used from `../normalizer-minimal-point-orbit/PROOF.md`, independently of its stronger minimum-orbit and orbit-gap claims. Each of the six lines L in F_5² determines five distinct Heisenberg eigenlines. A Weyl operator with nonzero pairing cycles the five eigenvalues, giving transitivity within that five-point set. Eigenlines belonging to two different L cannot coincide, since independent Heisenberg operators have nontrivial scalar commutator. Finally SL_2(F_5) is transitive on the six labels L. These observations establish a single orbit of exactly thirty points containing [e_0].

Equivariance transports residual kernels and ranks along this orbit. Rescaling a representative u rescales the middle-input map by a nonzero scalar and does not change R_u as a subspace, so the rank is well-defined on projective points. Therefore the local parity conclusion transports to all thirty points.

## 6. Audit of the strengthened lower bound and scalar cancellation

The character disjointness argument is exact: equality (i+k,i²+k²)=(j,j²) forces 2ik=0 in F_5, impossible for nonzero i,k. Hence no B-character of E occurs in Sym²E or in its B-submodule K_u. This establishes Hom_B(K_u,E)=0; the passage to a submodule is valid by character decomposition over C.

The chosen complement span(e_1,e_2,e_3,e_4) is B-stable, so the unreduced map b_u on Sym²E is unambiguous here. For q in K_u its image lies in R_u by definition. Repeated-input injectivity makes A_u:E→R_u an isomorphism, so the correction v_u=A_u⁻¹b_u|K_u exists uniquely and is linear.

The scalar cancellation is valid even without assuming that the chosen target operators themselves form an honest representation. For each g in B, put L_g=c_gρ_g. Since g fixes u exactly and both maps arise from the same cubic operation, b_u(gq)=L_g b_u(q) and A_u(gv)=L_g A_u(v). Consequently

    A_u(v_u(gq)) = b_u(gq) = L_g A_u(v_u(q)) = A_u(g v_u(q)).

Injectivity of A_u gives v_u(gq)=g v_u(q). Thus v_u is an honest B-intertwiner between the specified input modules, every target scalar cancels, and character disjointness forces v_u=0. No extra twist survives. In particular b_u vanishes on K_u.

If a square e_i² were in K_u, this vanishing and the cyclic identity would give 0=f(e_i,u,e_i)=−2f(e_i,e_i,u). The final term is nonzero by injectivity of A_(e_i) on V/Ce_i, since u=e_0 is independent of e_i. This is an abstract contradiction from the hypotheses, not a computation or evaluation of any actual operation. It uses the stated injectivity for all nonzero repeated inputs, not merely injectivity at u=e_0.

Therefore the entire square module survives in the residual quotient. The kernel is a sum of a subset of the remaining modules of dimensions 4 and 2, so its possible dimensions are exactly the necessary list {0,2,4,6} and the residual rank is constrained to {4,6,8,10}. The already verified rank transport extends this stronger assertion to all thirty canonical eigenpoints.

## Scope checks

- No classification of other point orbits is needed for this theorem.
- No claim about global emptiness of a low-rank locus follows without additional support information.
- Section 7 excludes ranks zero and two using repeated-input injectivity; together with parity, it excludes every rank at most three at the canonical eigenpoints.
- This is a necessary representation-theoretic constraint, not a realization theorem.

The proof states all these boundaries correctly. No correction is required.
