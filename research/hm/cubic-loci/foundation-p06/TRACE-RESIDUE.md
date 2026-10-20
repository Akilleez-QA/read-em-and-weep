# Normalized trace residue for an ordinary cubic

For any closed degree-two C of twist −r and closed degree-two η of twist r−5 in the regular model of TW-MODEL.md, put

    R(C,η)=[x_0^-1 x_1^-1 x_2^-1 x_3^-1 x_4^-1] integral_[01234] tr(Cη).

This is the perfect normalized Serre pairing. The proof below applies in particular to r=3 and the ordinary canonical cubic C=a h_bc+h_ab c supplied by the canonical-operation theorem. No orbit-reduced formula, scalar-contraction recipe, dual representative or value is supplied.

## 1. Fixed residue and orientation conventions

The scalar Čech differential is the alternating differential of the ordinary alternating Čech complex. Its unique degree-four component is indexed 01234. For f∈C⁴(O(−5)) define Res(f) to be the coefficient in R(C,η). Every homogeneous Laurent expression here is a finite sum.

This functional kills Čech boundaries. Indeed each summand of (δg)_01234 is restricted from an intersection missing one index j. Every allowed monomial in that summand has exponent of x_j nonnegative, so cannot be the monomial with all exponents −1. Conversely every monomial of total weight −5 other than that monomial has some nonnegative exponent, hence lies in the image from the corresponding missing-index component, with the appropriate alternating sign. Therefore

    H⁴(O(−5)) ≅ C,   [1/(x_0x_1x_2x_3x_4)] ↦ 1.          (3)

This also proves that Res is a nonzero, fully normalized functional, without invoking a numerical residue computation on any input.

To fix the canonical-bundle identification, use the ordered homogeneous volume expression

    Ω=Σ_(i=0)^4 (−1)^i x_i dx_0∧...∧omit(dx_i)∧...∧dx_4.

The isomorphism O(−5)→K_(P^4) sends f to fΩ. On x_0=1, z_i=x_i/x_0 for 1≤i≤4, Ω becomes dz_1∧...∧dz_4. Thus the generator in (3) becomes dz_1∧...∧dz_4/(z_1z_2z_3z_4). Our Serre trace convention is the residue of this ordered form, normalized to 1, equivalently (2πi)^(−4) times its ordered product-contour integral. No analytic contour calculation is needed for R(C,η). In particular no extra 4!, 1/2, or (2πi)^4 multiplies R(C,η). The Serre trace normalization uses the ordinary matrix trace tr(Cη), with no rank-two scalar-splitting factor.

Orient Δ_[01234] by dt_1∧dt_2∧dt_3∧dt_4, with t_0=1−t_1−...−t_4 and t_i≥0. This is the increasing-vertex orientation used by I in TW-MODEL.md. If the top component is written universally as

    tr(Cη)_01234 = Σ_γ f_γ(x) t_0^γ0 ... t_4^γ4
                                  dt_1∧dt_2∧dt_3∧dt_4,

with γ_i nonnegative and f_γ homogeneous Laurent polynomials of weight −5, then R(C,η) is explicitly

    R(C,η) = Σ_γ (γ_0!γ_1!γ_2!γ_3!γ_4!)/( |γ|+4 )!
                   · [x_0^(−1)...x_4^(−1)] f_γ.          (4)

This is an operator formula, not an evaluation of the user's polynomial instance. Expressions using dt_0 are first reduced by dt_0=−Σ_(i=1)^4dt_i, retaining wedge signs. Formula (4) is independent of polynomial presentations modulo Σt_i=1. The Whitney top form has integral 1 with this convention, consistently with IW=id. Changing ordered coordinates or canonical volume must transport both the cover orientation and the O(−5)→K identification; an untransported volume rescaling rescales numerical certificates. The intrinsic Serre pairing does not depend on such a presentation.

## 2. Why this is the Serre pairing

Write E_k=End(H)⊗O(k), T_r=H²(E_{−r}), and D_r=H²(E_{r−5}).

The fiberwise trace pairing End(H)⊗End(H)→O is perfect and identifies End(H) with its dual. Since K_(P^4)=O(−5), the dual bundle to E_{−r}, tensored with K, is E_{r−5}. Serre duality gives the perfect pairing

    T_r × D_r → H⁴(O(−5)) → C.                      (5)

The last arrow is normalized by (3). For the general duality theorem and its cup/evaluation description see Stacks Project, Sections 48.27, especially Remarks 48.27.2 and 48.27.6:
https://stacks.math.columbia.edu/tag/0FVU
The standard projective-space Laurent Čech computation is also recorded in Section 30.8:
https://stacks.math.columbia.edu/tag/01XS
Here (3) directly supplies the needed top-degree calculation and normalization.

The TW product is wedge followed by composition; twists add. Hence tr(Cη) has degree four and twist −5. It is closed because both factors are closed. Integration I is a chain map and computes the corresponding Čech class. The multiplicative DGA comparisons in TW-MODEL.md identify its product with the sheaf-cohomology cup product. Thus R(C,η) is exactly the displayed Serre pairing.

Crucially, form the TW product first and only then apply I. No identity I(Cη)=I(C)∪I(η) of cochains is assumed. Nor is any multiplicativity of W used. Degrees two and two give no Koszul minus sign on interchanging the two factors inside the trace.

## 3. Independence of representatives and defining choices

If C is replaced by C+dQ, with |Q|=1 and dη=0, then

    tr((dQ)η)=d tr(Qη).

Its integral is a Čech boundary and has residue zero. If η is replaced by η+dξ, |ξ|=1, then, since |C|=2 and dC=0,

    tr(C dξ)=d tr(Cξ),

again with zero residue. These identities also prove independence when both representatives change, by changing them successively.

For the ordinary defining-system cubic, the canonical-operation theorem proves that changing representatives or adjacent primitives changes C by a boundary, whenever input classes are fixed. The preceding argument therefore proves invariance of R(C,η) under all such changes. In particular independence does not require explicitly constructing Q. A change of model or affine cover is interpreted through the established cohomology comparisons and the normalized canonical trace.

One may take η trace-free without changing its class: H²(O(r−5))=0 for r=1,2,3, and the trace splitting removes a scalar boundary. However this is unnecessary for R(C,η), and no contraction at twists −4 or −3 is imported from the scalar homotopy proved only at 0,−1,−2. If an ordinary Čech dual two-cocycle η_0 is supplied, η=Wη_0 is a closed regular TW representative. W is defined for all coefficient bundles and twists; its use here needs no scalar contraction at the dual twist.

