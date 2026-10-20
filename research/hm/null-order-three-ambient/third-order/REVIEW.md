# Independent audit: third-order ambient extension and total de Rham lift

## Verdict

The displayed construction passes the four required identities modulo h^4: local associativity, overlap algebra preservation, triple-inner gluing, and the scalar pentagon. Its product coefficient and overlap map are explicit; its scalar unit coefficient c is existential. The existence conclusion requires the stated regular equivariant acyclic Čech model on X=C^4, and is not a consequence of the universal differential relations alone. No module or period identification follows.

Audited files: `RESULT.md` in this directory; [RESULT.md](../total-de-rham/RESULT.md); and the scalar pentagon proof and pinned source copied in `the scalar-pentagon packet (see README sources) `.

Only universal tensor, derivation, and cochain identities were used. No actual rational function, jet, module matrix, finite model, or repository experiment was evaluated.

## 1. Product correction and its sign

For one factor pair (r,s), on an overlap i,j, write

T_ij = λ(a_r,i q_s,ij V_s + q_r,ij a_s,j V_r).

Factor support, the dual frame, and dq_r=(δa_r)ω_r imply

L_T(V_r∧V_s) = −λ[(δa_r)_ij a_s,j + a_r,i(δa_s)_ij] V_r∧V_s.

The bracketed scalar is precisely δ(a_r a_s)_ij, including its literal Alexander–Whitney endpoints. Cross-pair derivatives vanish. Therefore the proposed

ρ_i = λ(a_1,i a_2,i π12 + a_3,i a_4,i π34)

satisfies δρ=−L_Tπ with no sign or factor discrepancy.

For the coefficient convention in the draft, P=−W^(-1). Differentiating this inverse convention at W in the direction −Z yields −P Z P. Thus ρ=−P Z P corresponds to the formal two-form ω−h²ζ. It would have the opposite sign for ω+h²ζ. The draft states the correct sign explicitly.

## 2. All four ambient identities

### Local associativity

The common Moyal coefficients are associative because the V_r commute. Adding h³ρ/2 changes the associator through h³ only by the ordinary Hochschild differential of this new bidifferential operator. A bivector defines a biderivation and hence a Hochschild two-cocycle. No condition such as [π,ρ]=0 is required at this order; that would enter a later order. Normalization preserves the unit.

### Overlap algebra preservation

With F_ij mapping the j algebra to the i algebra, direct expansion gives at h³

μ3,j−μ3,i + T_ij μ1 − μ1(T_ij−,−) − μ1(−,T_ij−)
= δμ3 + L_Tμ1
= (δρ+L_Tπ)/2 = 0.

The h² term is the ordinary derivation identity. Thus F3=0 is valid. The inverse id−h²T is valid modulo h^4.

### Triple-inner gluing

For A=1+hb+h²b²/2+h³(b³/6+c), symmetry of μ2 gives

[A,f]_⋆ = h²{b,f}+h³{b²/2,f}
= h²{b,f}+h³b{b,f}.

Multiplying on the right by A^(-1)=1−hb+O(h²) cancels the displayed cubic term. Star-derivative corrections in that final multiplication start at h^4. The new μ3 and c likewise cannot contribute through h³. Consequently Ad(A)=id+h²H_b modulo h^4, and triple gluing is exactly the input equation δT=H_b. There is no missing h³ condition.

### Pentagon

The h³ scalar equation is precisely

δc = Ψ,
Ψ_ijkl = {b_ijk,b_ikl}/2 − {b_jkl,b_ijl}/2 − T_ij(b_jkl).

The sign of δc agrees with the declared ordinary Čech differential. Higher product coefficients do not enter: their normalized evaluation on the two units requires nonconstant inputs, each already divisible by h. The previously supplied universal proof of δΨ=0 applies unchanged to these chart-dependent products.

## 3. Existence, regularity, and explicitness

The a_r coefficients are regular on their respective prescribed charts; the q_r coefficients are regular on the prescribed overlaps. The V_r are regular global derivations. Hence ρ, the local μ3, F, and Ψ have the required regularity. This does not claim globally regular a_r.

The source's original charts arise as inverse images of affine charts under the finite map C→P¹; their finite intersections, and products thereof, are affine. They are preserved by the deck involutions. Accordingly the original product affine cover provides the regular equivariant acyclic model required for the existence argument; no passage to a rational-function complex is necessary.

For the actual scalar cochain action, b and π have pair-sign characters P or Q, while T is invariant. Thus Ψ has only characters P or Q. H³(C^4,O) has only triple-sign characters, by Künneth and the sign action on H¹(C,O). The class of Ψ therefore vanishes in the regular Čech complex. A regular primitive c exists and can be projected onto P/Q characters. This supplies existence, not a formula or evaluated cochain for c. Without these geometric/cohomological hypotheses, the correct conclusion is only the obstruction equation δc=Ψ.

## 4. Companion total de Rham calculation

The total signs and all four components are consistent:

dζ=0, δζ=dα, δα=−db, δb=0,

with α=ι_Tω. The displayed η_r=a_rω_r+q_r is D-closed because the Čech degree-one term contributes −dq_r. The expansion of η_rη_s uses the correct negative sign when a form passes a Čech one-cochain and retains the correct asymmetric endpoints.

The ordinary-nerve commutativity homotopy is also correct. For c_rs,ij=q_r,ij q_s,ij, one has δc_rs=−(q_r∪q_s+q_s∪q_r) and the mixed-form component of η_rη_s+η_sη_r is dc_rs. Hence η_rη_s+η_sη_r=−Dc_rs. The subsequent antisymmetrization and scalar Π representative comparisons have the stated signs and factors.

The companion document properly distinguishes its chosen total de Rham lift Π_dR from the original H²(O) class Π. Its abstract exterior-algebra contraction is expressly distinguished from geometric contraction on total cochains. Therefore neither the identity [β]=−4λΠ_dR nor the formal inverse calculation above identifies an actual central period or proves a module lift.

## Final assessment

No mathematical correction is needed to the audited construction at the claimed truncation. It establishes a regular third-order ambient extension, with explicit μ3 and F3 and an existential regular c, under the stated X=C^4 cover and character hypotheses. The result is not an explicit complete set of unit coefficients and does not settle any module obstruction or all-orders extension.
