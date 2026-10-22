# Independent audit: canonical adjoint line and normal-enhanced blowup

Reviewed `CANONICAL-ADJOINT-LINE-AND-NORMAL-ENHANCED-BLOWUP.md` on 2026-10-22. The cited coherence theorem and its nonzero constant are treated as established inputs; this audit checks the subsequent geometry, not the upstream source calculation or normalization.

## Verdict

The stated line construction, Picard obstruction, ordinary-blowup failure, and normal-enhanced resolution are correct. The optional embedding strengthening below is also valid. No source-instance evaluation or numerical computation is used.

## Checked claims

1. **An invertible abstract subsheaf, not necessarily a subbundle.** Reduction of `f n_s=0` modulo the square-zero ideal first gives `f_0 N=0`, hence `f_0=0` by integrality. The remaining equation in that ideal gives `g_0 N=0`, hence `f=0`. This remains valid where N vanishes. The transition is exactly `n_t=(1-2κq/(st))n_s`; it is a unit and reduces to 1. Using the image of the entire family makes the construction independent of the binary basis.

2. **Picard class and sign.** In the explicitly stated frame convention, the class is `-2κ[1/(st)]` in `H^1(Ω,O_Ω(-2))`. The two standard projective opens are affine and the indicated graded Čech quotient computes this cohomology. For `R=(C[V]/(q))[s,t]`, the Laurent monomial `s^-1 t^-1` cannot come from either separate localization. The class is nonzero. Hartogs gives the global reduced units `C*`, which lift, so the map from this H^1 into the infinitesimal Picard kernel is injective.

3. **No invertible extension on X.** An extension would reduce to a line bundle trivial off the codimension-two conic. Normality makes that reduced line bundle trivial on Q. The displayed projective-space sequence proves `H^1(Q,O_Q(-2))=0`, so `Pic(X)→Pic(Q)` is injective. This contradicts the nontrivial class on Ω_X.

4. **Direction of the ratio line.** With opposite affine coordinate `w=s/t`, the corrected coordinate is `w+κq_t`, not `w-κq_t`. The transition of `(p')*O(2)⊗p*O(-2)` is `(z-κq_s)^2/z^2=1-2κq/(st)`. Thus the draft identifies L itself, not its dual.

5. **The multiplier blowup fails.** The relevant ideal is `I=(s,t)`. This is not the ideal `(s,t,q)` of the reduced center inside X. On the ordinary multiplier-blowup chart, `s` is regular but `q` remains nonzero modulo s. Therefore `s^2(g-z)=-κq` is impossible. Any putative extension to P^1 must land in the indicated affine target chart because its reduction is z.

6. **The enhanced blowup works.** For `J=(s^2,st,t^2,q)`, the q-chart is empty because `qT` is nilpotent. More precisely, `D(stT)=D(s^2T)∩D(t^2T)`, so the two square charts cover. Near C the first chart is exactly `C[r,s,z,η]/(η^2)`, with `t=sz` and `q=s^2η`. Its injection into the localization at s proves that η survives and that there are no additional relations. The opposite coordinates satisfy `w=1/z`, `η_t=η/z^2`. The functions `z-κη` and `w+κη_t` are reciprocal, so both projections extend. Reduction gives the ordinary blowup of Q along `(s,t)` because blowing up an ideal and its square is identical.

For terminological precision, it is the **affine chart ring** of the Rees construction that embeds into the localization in item 6.

## Verified strengthening: extend the embedding too

The invertible extension Ltilde embeds canonically as an abstract line subsheaf of `π*B_X(2)`. This does not assert a subbundle.

Locally choose a lift Ñ of N to `B_X(2)` and write

    U_(s²)=s² Ñ+q X_s.

Here X_s is a section on Q; choose any local lift when using it on X. On the enhanced chart set

    ntilde_s=π*Ñ+η π*X_s.

Changing the lift of X_s does not change this expression, since `ηq=s²η²=0`. It satisfies `s²ntilde_s=π*U_(s²)`. Regularity of s makes this quotient unique, independent of the auxiliary choices. Similarly define ntilde_t. Their transition is the same unit `1-2κη/z`, which is the transition of Ltilde.

The identity `s^4 ntilde_s²=π*(U_(s²)²)=0` and regularity of s prove square-zero exactly, without relying on merely topological density. For injectivity, reduce `f ntilde_s=0` to the integral reduced blowup, where the pulled-back N is generically nonzero. Then f lies in the square-zero ideal. That ideal is invertible on the reduced blowup, so the remaining equation again forces f=0. Away from C these are the original generators; near C the chart description proves the required invertibility of the nilpotent ideal.

Thus both the abstract line and its square-zero adjoint embedding extend on Y, but neither a locally free quotient nor a spinor-kernel interpretation follows.
