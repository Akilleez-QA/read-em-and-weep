# Exact local contractions and SL₂ frame normalization

Status: explicit matrices generated and all stated algebraic identities executed exactly. The second-order obstruction value remains uncomputed.

This extends the carrier atlas and supplies local data for comparison with the four-term line-bundle model. The executable certificate is verify-hm-contractions.js; run it with Node.js. It has no dependencies, reconstructs all matrices from wedge products, checks safe integer arithmetic, and asserts each polynomial identity after clearing denominators.

## The three-term monad contraction

Work on either pivot chart from the atlas. Write the monad as A→B→C, with matrices α,β, and let I,Jc,P,U be that chart's index lists.

Define:
- j:C→B by j_I=β_I⁻¹ and j_{Jc}=0;
- h:B→A by h=A_P⁻¹ pr_P pr_{Jc}, where A=α_{Jc};
- i:E→B by i=S, the atlas frame;
- p:B→E by p=R pr_{Jc}, the atlas coordinate map.

Then hα=1, βj=1, αh+jβ=1−ip, pi=1, hj=hi=pj=0.
These identities are checked after multiplying by the displayed pivot determinants. Thus h and j give the degree−1 homotopy of a strong deformation retract of the monad onto its cohomology E.

## The four-term comparison

In the local v₀=1 chart let v=(1,a,b,c,d), η=e₀*, and
W=(Λ²V*)².
Let C_v:B→W be the isomorphism onto the kernel of contraction with v:
C_v(w)(u₁,u₂)=vol(v,w,u₁,u₂), separately in each half.

Define the constant map
b(ζ⁺,ζ⁻)_a=ζ⁻(w⁺_a)−ζ⁺(w⁻_a).
Its kernel K₀ has the following ordered basis, where stars denote the dual oriented bivectors:
U_a=(w⁺*_a,0), V_a=(0,w⁻*_a), Z_a=(w⁻*_a,w⁺*_a).

Let i_K:K₀→W be this inclusion, and let p_K:W→K₀ read the coefficients of, respectively, the top w⁺* basis, bottom w⁻* basis, and bottom w⁺* basis. Thus p_K i_K=1; on ker b, i_K p_K is the identity.

Let p_M:W→B read the coefficients with both dual indices in {1,2,3,4}, then apply the six-dimensional wedge pairing matrix S from the atlas, in each half. Then p_M C_v=1.

The local four-term complex is
A --γ→ K₀ --δ→ (V*)² --ε→ C²,
where
γ=p_K C_v α,  δ=ι_v i_K,  ε=ev_v.

Its contraction onto E has the following matrices:
I=p_K C_v i,
P=p p_M i_K,
H₀=h p_M i_K,
H₁=p_K(1−C_v j b)(η∧−),
H₂=(η·−).

Here H₀ maps K₀→A, H₁ maps (V*)²→K₀, and H₂ maps C²→(V*)².

The certificate checks:
- δγ=0 and εδ=0;
- H₀γ=1;
- γH₀+H₁δ=1−IP;
- δH₁+H₂ε=1;
- εH₂=1;
- PI=1, H₀H₁=0, H₁H₂=0, H₀I=0, PH₁=0.

After pullback and twisting, this is exactly the local contraction for
5N⁻¹→15N→10N³→2N⁵
in degrees −1,0,1,2. The other primary charts are obtained by cyclic relabeling. Both the primary and auxiliary pivot choices are executed by the certificate.

## Rational symplectic normalization

For the atlas frame S, the O(−1)-valued pairing has scalar
σ=1 on each primary chart,
σ=−a²/d on the auxiliary chart.

The certificate checks these equalities as polynomial identities. Thus the auxiliary second column can be rescaled by −d/a² to give pairing scalar1. No square root is needed.

For the determinant-trivial bundle E=f*H⊗N, choose a local N frame n and write z_j=f*v_j/n². The scalar of the induced ordinary symplectic form is σ/z_j. Therefore rescale the second frame column by z_j/σ. The resulting transition matrices lie in SL₂.

Conjugate the coordinate projection by the inverse diagonal rescaling; the homotopy H is unchanged. All strong-deformation-retract identities persist.

## Remaining computation

These are local contractions. A global Čech comparison still needs the homotopy-corrected inclusion and the exact cover-refinement comparison described in the second-order algebroid document. Neither a framewise inclusion alone nor these identities calculate the obstruction class.
