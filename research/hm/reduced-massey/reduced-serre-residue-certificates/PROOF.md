# Exact Serre-dual residue certificates for the reduced algebraic Massey representative

Reused context: the universal normalization, general cup/trace interpretation and boundary identities in §§1–3 occur in [the ordinary trace-residue theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/838dbe4a9ddaee5ca20eae14944e3908ea89079d/research/hm/cubic-loci/foundation-p06/TRACE-RESIDUE.md). This proof retains them and supplies their full application to the reduced formula, together with §§4–5. See [Dependencies](DEPENDENCIES.md).

## 0. Result and scope

Let H be the rank-two bundle on P^4 over C of the prerequisite theorems. Put E_k=End(H)⊗O(k), and use their regular algebraic Thom–Whitney (TW) complex A_k on the ordered standard cover U_i=D_+(x_i), 0<1<2<3<4. All ordered pair vanishings and zero-indeterminacy hypotheses are imported, not proved anew.

For r=1 or 2, set T_r=H²(E_{−r}) and D_r=H²(E_{r−5}). For the lower pattern take b of twist 0 and c of twist −1; for the upper pattern take b,c of twist −1. With a=a_X and all conventions of the algebraic reduction, set

    C_r(X;b,c)=−½B(b,L_Xc)−t_bc a_X+t_ab c,
    t_pq=(K+WhI)(tr(pq)/2).

For every supplied closed η∈A²_{r−5}, the following is an exact scalar certificate:

    R_r(X;b,c;η)
      = [x_0^(−1)x_1^(−1)x_2^(−1)x_3^(−1)x_4^(−1)]
          ∫_[01234] tr(C_r(X;b,c) η).                  (1)

The bracket means the coefficient of that Laurent monomial, not evaluation at a point. This is the normalized Serre pairing of the canonical Massey class with [η]. Thus

    [C_r(X;b,c)]≠0  iff  there exists a closed η with R_r≠0.    (2)

No η representing an actual dual class is constructed here, and neither side is evaluated. The main advance beyond the previous reduction is the explicit exact scalar functional on its finite regular formula, eliminating the need to decide target exactness by solving an End-valued boundary equation. It does not eliminate the separate task of providing dual cocycles.

## 1. Fixed residue and orientation conventions

The scalar Čech differential is the alternating differential of the imported scalar contraction. Its unique degree-four component is indexed 01234. For f∈C⁴(O(−5)) define Res(f) to be the coefficient in (1). Every homogeneous Laurent expression here is a finite sum.

This functional kills Čech boundaries. Indeed each summand of (δg)_01234 is restricted from an intersection missing one index j. Every allowed monomial in that summand has exponent of x_j nonnegative, so cannot be the monomial with all exponents −1. Conversely every monomial of total weight −5 other than that monomial has some nonnegative exponent, hence lies in the image from the corresponding missing-index component, with the appropriate alternating sign. Therefore

    H⁴(O(−5)) ≅ C,   [1/(x_0x_1x_2x_3x_4)] ↦ 1.          (3)

This also proves that Res is a nonzero, fully normalized functional, without invoking a numerical residue computation on any input.

To fix the canonical-bundle identification, use the ordered homogeneous volume expression

    Ω=Σ_(i=0)^4 (−1)^i x_i dx_0∧...∧omit(dx_i)∧...∧dx_4.

The isomorphism O(−5)→K_(P^4) sends f to fΩ. On x_0=1, z_i=x_i/x_0 for 1≤i≤4, Ω becomes dz_1∧...∧dz_4. Thus the generator in (3) becomes dz_1∧...∧dz_4/(z_1z_2z_3z_4). Our Serre trace convention is the residue of this ordered form, normalized to 1, equivalently (2πi)^(−4) times its ordered product-contour integral. No analytic contour calculation is needed for (1). In particular no extra 4!, 1/2, or (2πi)^4 multiplies (1). The factor 1/2 in t_pq is the rank-two scalar splitting, not the Serre trace normalization: the latter uses the ordinary matrix trace tr(Cη).

Orient Δ_[01234] by dt_1∧dt_2∧dt_3∧dt_4, with t_0=1−t_1−...−t_4 and t_i≥0. This is the increasing-vertex orientation used by I in the reduction. If the top component is written universally as

    tr(C_rη)_01234 = Σ_γ f_γ(x) t_0^γ0 ... t_4^γ4
                                  dt_1∧dt_2∧dt_3∧dt_4,

with γ_i nonnegative and f_γ homogeneous Laurent polynomials of weight −5, then (1) is explicitly

    R_r = Σ_γ (γ_0!γ_1!γ_2!γ_3!γ_4!)/( |γ|+4 )!
                   · [x_0^(−1)...x_4^(−1)] f_γ.          (4)

This is an operator formula, not an evaluation of a selected polynomial instance. Expressions using dt_0 are first reduced by dt_0=−Σ_(i=1)^4dt_i, retaining wedge signs. Formula (4) is independent of polynomial presentations modulo Σt_i=1. The Whitney top form has integral 1 with this convention, consistently with IW=id. Changing ordered coordinates or canonical volume must transport both the cover orientation and the O(−5)→K identification; an untransported volume rescaling rescales numerical certificates. The intrinsic Serre pairing does not depend on such a presentation.

## 2. Why this is the Serre pairing

The fiberwise trace pairing End(H)⊗End(H)→O is perfect and identifies End(H) with its dual. Since K_(P^4)=O(−5), the dual bundle to E_{−r}, tensored with K, is E_{r−5}. Serre duality gives the perfect pairing

    T_r × D_r → H⁴(O(−5)) → C.                      (5)

The last arrow is normalized by (3). For the general duality theorem and its cup/evaluation description see Stacks Project, Sections 48.27, especially Remarks 48.27.2 and 48.27.6:
https://stacks.math.columbia.edu/tag/0FVU
The standard projective-space Laurent Čech computation is also recorded in Section 30.8:
https://stacks.math.columbia.edu/tag/01XS
Here (3) directly supplies the needed top-degree calculation and normalization.

The TW product is wedge followed by composition; twists add. Hence tr(C_rη) has degree four and twist −5. It is closed because both factors are closed. Integration I is a chain map and computes the corresponding Čech class. The multiplicative DGA comparisons already proved for algebraic TW identify its product with the sheaf-cohomology cup product. Thus (1) is exactly (5).

Crucially, form the TW product first and only then apply I. No identity I(Cη)=I(C)∪I(η) of cochains is assumed. Nor is any multiplicativity of W used. Degrees two and two give no Koszul minus sign on interchanging the two factors inside the trace.

## 3. Independence of representatives and defining choices

If C is replaced by C+dQ, with |Q|=1 and dη=0, then

    tr((dQ)η)=d tr(Qη).

Its integral is a Čech boundary and has residue zero. If η is replaced by η+dξ, |ξ|=1, then, since |C|=2 and dC=0,

    tr(C dξ)=d tr(Cξ),

again with zero residue. These identities also prove independence when both representatives change, by changing them successively.

The imported algebraic reduction proves that C is the canonical singleton Massey class: changing input representatives, normalized local bundle lifts, or the permitted scalar homotopy choices changes C by a boundary, whenever the input cohomology classes are fixed. The preceding argument therefore proves invariance of (1) under all such changes. In particular independence does not require explicitly constructing Q. A change of model or affine cover is interpreted through the established cohomology comparisons and the normalized canonical trace.

One may take η trace-free without changing its class: H²(O(r−5))=0 for r=1,2, and the trace splitting removes a scalar boundary. However this is unnecessary for (1), and no contraction at twists −4 or −3 is imported from the scalar homotopy proved only at 0,−1,−2. If an ordinary Čech dual two-cocycle η_0 is supplied, η=Wη_0 is a closed regular TW representative. W is defined for all coefficient bundles and twists; its use here needs no scalar contraction at the dual twist.

## 4. Exact detection, finite witnesses, and the cutoff boundary

Perfectness of (5) proves (2). More globally, let F_r be the relevant canonical trilinear operation, identified in its first slot through the KS isomorphism U0≅sl_5. A multilinear map is zero exactly when every decomposable input has zero value. Therefore

    F_r≠0 iff some X,b,c and closed η have R_r(X;b,c;η)≠0.   (6)

This is an existence equivalence, not a produced witness. If a full basis of D_r and regular cocycle representatives for it were supplied, testing all its pairings would decide whether one fixed target class is zero. The imported target dimensions are dim T_1=10 and dim T_2=20, so duality yields the same dual dimensions. These are cohomological dimensions, not newly computed ranks.

Each supplied regular cochain has finite simplex-polynomial support; each scalar coefficient in (1) becomes a finite Laurent sum. The operators in the reduced formula and I preserve finite expressions, as proved in the reduction. Consequently each certificate uses finitely many exact algebraic operations, with no End-valued pair primitive and no solution of dQ=C in the target. Failure to find a nonzero residue in a few tests does not prove vanishing unless the supplied witnesses are known to span the whole dual relevant to the claim.

There is no universal bound here on simplex degree, localization denominator, or base polynomial complexity. A finite subset of cochains chosen by a cutoff need not represent all dual classes and need not inherit a perfect pairing. Existence of finite representatives for a finite-dimensional dual basis does not assert that such representatives have been found or that an arbitrary finite cutoff suffices.

## 5. Exact relation to the four upper and eight lower parameters

Put

    S_2=U0⊗U1⊗U1,   E_2^op=Hom_N(S_2,T_2), dim E_2^op=4,
    S_1=U0⊗U0⊗U1,   E_1^op=Hom_N(S_1,T_1), dim E_1^op=8.

The parameter counts and their chosen character-component parametrizations are those of the two imported multiplicity proofs. Upper coordinates have two symmetric and two alternating last-slot components. Lower coordinates have four symmetric and four alternating first-two-Z-slot components; one must not identify the actual Z-slot flip with a naive flip in the twice-iterated R factorization.

Fix any of those parameter coordinate systems, and write λ_j∈(E_r^op)^* for its coordinate functionals. There is a precise finite-sum residue implementation of every λ_j, independent of inventing actual dual cocycles. The ambient vector space Hom(S_r,T_r) has dual canonically S_r⊗T_r^*. Restriction onto (E_r^op)^* is surjective, because these are finite-dimensional vector spaces. Thus choose any lift of λ_j, and use (5) to write it as

    L_j=Σ_ν s_(jν)⊗d_(jν) ∈ S_r⊗D_r.              (7)

Decompose each s_(jν) into finitely many decomposable source tensors, absorbing their coefficients into d_(jν). Choose TW input representatives for those abstract classes and closed TW representatives η_(jν) for d_(jν). Identify each first-slot U0 class with κ(X_(jν)). Then the exact parameter formula is

    λ_j(F_r)=Σ_ν R_r(X_(jν); b_(jν),c_(jν);η_(jν)). (8)

Equation (8) applies to j=1,...,4 in the upper case and j=1,...,8 in the lower. It is not a claim that (7), its input representatives, or its dual representatives have been computed. It shows rigorously how the abstract character-parameter extraction interfaces with the no-End-primitives regular formula. Different lifts L_j have the same value on every equivariant F_r by definition of restriction. Cohomological representatives are irrelevant by §3. Coordinate changes in the parameter spaces change the list by the corresponding invertible linear transformation.

Consequently all four (respectively eight) expressions in (8) vanish iff the corresponding operation is zero. Any one nonzero parameter expression certifies nonzero operation. A single residue for arbitrary fixed inputs and a witness also certifies nonzero operation, though it need not equal a single selected parameter. By the imported irreducibility the nonzero alternatives have full downstairs images T_2 and T_1. The numbers four/eight here count symmetry-eligible operation parameters; they must not be confused with the retained target dimensions, which are four LOWER and eight UPPER. No actual nonzero expression, retained-span conclusion for the instance, or physical-source verdict is asserted.
