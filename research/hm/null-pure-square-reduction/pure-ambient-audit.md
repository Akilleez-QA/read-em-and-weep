# Independent audit: pure obstruction and ambient second-jet freedom

## Verdict

Accepted, with the first-order identification and fixed-module-boundary qualifications retained. For the actual carrier E=f*H⊗N on X=C⁴, the characteristic morphism is zero on HH²(X)⁰. Thus arbitrary valid changes of the ambient second jet cannot alter the deck-invariant component of its second-order module obstruction. This is an independence theorem, not a computation or vanishing theorem for the pure obstruction.

The report `[pure-square-next.md](pure-square-next.md)` correctly states this distinction. Its existential conclusion is also valid: for this fixed first-order boundary, once the imported mixed vanishing is admitted, allowing arbitrary second-order ambient choices yields no additional diagonal existence cases beyond the original ambient two-jet. This does not say that every alternative ambient admits a lift when the original does; alternatives can introduce other character obstructions.

## 1. Full Hochschild space and conventions

Use the full global Hochschild deformation complex appropriate to algebroids, including its arity-zero/curvature part. Its degree-two HKR decomposition is

HH²(X)=H⁰(∧²T_X)⊕H¹(T_X)⊕H²(O_X).

Under the independent elliptic involutions, V_i and H¹(O_Ci) both have character χ_i. Consequently the first and third summands have only χ_iχ_j with i≠j. The middle summand has the sixteen lines V_i⊗ε_j; exactly the four lines with i=j are invariant. There is no omitted invariant scalar-gerbe class and no invariant bivector class. Computing only global bidifferential products would miss H¹(T_X), and omitting curvature would wrongly omit H²(O_X), but neither omission occurs in the supplied proof.

HKR sign or normalization choices cannot change the asserted zero evaluations. On this abelian fourfold T_X is trivial, so Todd-class modifications of HKR introduce no nontrivial correction. No canonical-bundle or determinant character twist enters HH² or End(E). A line twist of E can change its characteristic map, so the proof must, and does, extend the actual N rather than work only with End(E).

## 2. Nonzero moduli directions, including j=1728

The family y²=x(x−1)(x+1−t), with its infinity section, is smooth formally around t=0 and retains the degree-two x-map. The ordered branch cross-ratio has nonzero derivative. A trivial deformation of the pointed elliptic curve would make its complete linear series |2∞| constant up to a PGL₂ change. Such an infinitesimal change fixing 0,1,∞ is zero and cannot move the fourth branch point. Hence the Kodaira–Spencer class is nonzero and spans H¹(T_C).

Forgetting the origin does not invalidate this assertion: infinitesimal changes of a single marked point on an elliptic curve are absorbed by translations; the pointed-to-unpointed deformation tangent is an isomorphism. Extra finite automorphisms at j=1728 ramify the coarse j-coordinate, not the deformation tangent of this branch-marked family. Testing only the derivative of j would have given a false negative.

Varying the four factors independently supplies precisely the four diagonal classes, with nonzero scalar normalizations immaterial.

## 3. Actual root line and characteristic evaluation

The pinned carrier is E=f*H⊗O_X(Σ∞_i), not merely a bundle with matching Chern classes. Each infinity section is a relative Cartier divisor. Their sum defines an actual relative line bundle N_t, with N_t²=f_t*O(1), because each x-map has pole divisor 2∞. Thus no unproved square-root extension, root-gerbe trivialization, or formal choice of half a Chern class is needed.

The four relative x-maps, followed by multiplication of binary linear forms, give f_t to the same P⁴. The actual vector bundle f_t*H⊗N_t extends E. Therefore the obstruction At(E) contracted with each Kodaira–Spencer class is zero in full Ext²(E,E), not only after trace. By linearity the characteristic map vanishes on all HH²(X)⁰.

## 4. Exact scope of the ambient comparison

Two valid second-order algebroid structures with an explicitly identified common first-order structure differ, modulo second-order gauge, by a total Hochschild two-cocycle η. With the first-order module lift transported through that identification and then fixed, the difference of module obstruction classes is ev_E([η]). This uses the undeformed characteristic map: multiplying the square-zero second-order difference by a first-order term would have order three.

Equivariance of ev_E gives pr₀ ev_E(η)=ev_E(pr₀η)=0, even for non-equivariant η. This accounts for product, overlap, and triple-unit corrections together, not only separately chosen sheaf-algebra coefficients. Additional locality restrictions merely reduce the allowable corrections and cannot weaken the conclusion.

It does not authorize changes of the first-order module Ext¹ class, identify two unspecified first-order presentations, eliminate the actual quadratic source, or produce a physical/regular cochain primitive. A geometric family proving ev_E=0 need not reproduce the prescribed quantization jet: only its tangent and the extension of E are used here. Thus the strongest proposed rival, missing source-jet binding, is neutralized for the characteristic-map claim but remains a genuine barrier to any stronger claim of quadratic vanishing by substitution of another ambient family.

For the actual pair-character boundary the residual has only pure invariant and mixed full-sign components. Given the accepted mixed result, the remaining diagonal condition is [C_PP+C_QQ]=0; the full two-parameter condition requires both pure classes to vanish separately. All noncentral terms in PR16 remain part of these classes. No new vanishing is established.

## Sources directly inspected

- PR16 full source, §§1, 5, 8–9: https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md
- Actual carrier and root line: https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md
- Exact source characters and first-order-identification warning, §§2, 5: https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md



## Conditional extension: arbitrary first-order module choices

An additional imported hypothesis strengthens the conclusion: assume there is an actual smooth ordinary deformation family of E whose Kodaira–Spencer map surjects onto Ext¹(E,E). A smooth parameter space of dimension 87 alone is not enough; the tangent-surjectivity is essential. This audit has not independently inspected a source proving that hypothesis.

Under it, every z∈Ext¹(E,E) extends as an ordinary module deformation through second order. Therefore its Yoneda square vanishes in Ext². This follows by taking an arc with prescribed tangent in the smooth family; it is not an inference from dimensions alone.

Here is a full-source justification of the variation formula. Let Z be an unnormalized homogeneous first-order transition correction representing z, and replace u by u+λZ in the complete PR16 source. The normalized residual is

C(u+λZ)=C(u)+λL_u(Z)+λ²Q(Z),

where the unnormalized linear numerator is

Z_jk u_ij + u_jk Z_ij + μ₁(Z_jk,g_ij) + μ₁(g_jk,Z_ij) − b_ijk Z_ik,

and the quadratic numerator is Z_jk Z_ij. Normalize both by g_ik⁻¹. The latter represents the ordinary Yoneda square with the declared row convention. The ambient μ₂, T, b², and μ₁(b,g) terms remain in C(u), but are independent of u and hence cancel from the difference.

For every λ, u+λZ solves the complete first-order equation. Full descent therefore implies δC(u+λZ)=0 polynomially in λ. Comparing coefficients proves that L_u(Z) and Q(Z) are each cocycles. This avoids attributing classes to individual, possibly nonclosed summands of the displayed formula.

Choose the original baseline u=u_P+u_Q with its authenticated pair characters. Both u and the first-order ambient operations have precisely these character shifts. Thus L_u maps the z-character S to S⊕P and S⊕Q. Its invariant projection can receive only pair-character z. Those Ext¹ groups vanish by the imported pinned rank result. For the remaining weight-zero and singleton classes, pr₀[L_u(z)]=0. The smooth tangent-surjective family gives [Q(z)]=0 for every z, including sums of distinct character components.

Finally an exact first-order difference is removed by the reduction-preserving local gauge in the pinned closure-and-characters source §5; retaining its induced second-order term preserves the obstruction, and discarding that term changes it only by a Čech boundary. Consequently no cochain representative loophole remains.

Subject to the extra smoothness/tangent premise, the invariant quadratic obstruction is independent of every first-order module choice as well as every second-order ambient choice, after fixing and identifying the first-order ambient deformation. Its value is still unknown. This strengthens, rather than contradicts, the fixed-boundary result proved above.

## Branch-square addendum audit

The author's branch identity is correct. With e₁=x₁+x₂, e₂=x₁x₂ and a_odd=(x₁−x₂)y₁y₂, one obtains a_odd²=(e₁²−4e₂)e₂[(1+e₂)²−e₁²]. Homogenizing through q=aX²+bXY+cY² gives Δ=(b²−4ac)ac[(a+c)²−b²]. The second factor is the product q(1,0)q(0,1)q(1,1)q(1,−1), hence the asserted resultant with XY(X²−Y²), subject only to the fixed resultant normalization.

The coefficient is anti-invariant under factor swap, while its square descends. The identity de₁∧de₂=(x₁−x₂)dx₁∧dx₂ confirms the sign; a sign-twisted or parameter-compensated presentation is essential before interpreting a_odd downstairs.

Under (a,b,c)↦(ζ⁴a,b,ζ⁻⁴c), discriminant and ac are fixed, while a², 2ac−b², c² have weights 3,0,2 modulo five. All three resulting polynomial components are nonzero. Hence Δ is not invariant under that torus action. This rules out naively extending the same unmodified mixed D5 action while preserving this fixed branch-dependent multiplication. It neither excludes every possible compensated action or equivalent presentation nor implies that the full pure residual factors through multiplication by Δ. Derivative and noncentral source terms remain to be controlled.
