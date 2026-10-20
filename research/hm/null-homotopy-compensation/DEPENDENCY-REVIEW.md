# Independent combined-boundary and nonclosed-defect audit

## Verdict and scope

**No correction is required to RESULT.md equations (2) and (3).** The complete boundary is governed by the degree-one operator `K = Qdot T − ΠQ`. Its Hom differential is `δK + KΔ`, not `δK − KΔ`. Both contributions to the remainder therefore have a minus sign: `−δ(pKZ) − pKΔZ`. The endpoint substitution has the four signs `+,−,+,−` and acts on both pieces of K.

This audit starts from the contraction, Leibniz and Čech identities, rather than accepting the normal form. It supplies a shorter proof of the selected chain-map identity, explicit input-degree typing, and an independent free-word operator control. It does not establish a detector value, source-specific cancellation, primitive denotation, or rational-divergence certificate.

## Sources actually read

Under `https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-complete-remainder-normal-form/`:

- `RESULT.md`, especially lines 42–93; `REVIEW.md`.
- `dependencies/hpl.md`, `endpoint.md`, `common-connection.md`, `overlap.md`, `overlap-domain.md`, and `partition-domain.md`.
- The underlying full prism proof at `https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-differentiated-partition-domain/dependencies/partition-prism.md`, especially its equations (3)–(5).

The public bundle's imported geometric premises remain premises. Reading the proofs does not independently authenticate the physical contraction identities or their homogeneous denotations.

## 1. Exact algebraic assumptions and types

Distinguish three complexes: row cochains `(A,Δ)`, source scalar cochains `(B,δ_B)`, and target scalar cochains `(C,δ_C)`. Ambient resolution cochains have commuting differentials `d=d_End` and `δ`; totalization signs are inserted separately. The coefficient derivation is V, and prime denotes differentiation of an operator's coefficients while holding its argument fixed.

Required premises:

1. `d²=δ²=Δ²=0`, `dδ=δd`, and restrictions are actual compatible ambient restrictions.
2. `dH+Hd=1−P`, with `P=jπ` in internal degree zero and `P=0` in negative degrees; `dj=0` and `πδj=Δ` with the actual first-face row transport and exactly one transpose.
3. L is fixed, restriction-compatible, and `Ld=0` on the relevant degree-minus-three maps. Ambient δ is fixed under V. No assumption that the row Δ is fixed under V is made.
4. The common split connection satisfies `H′=−ΓH+HΓ` and `j′=−Γj`; all owner-dependent maps are compared in a common ambient frame.
5. The first-face overlap maps satisfy `C=[δ,Γ]=C0+dR+Rd` and `W=δR+Rδ`, with the internal-degree graded R insertion. Their dependence on the original leading owner is retained.
6. Π is the full ordinary partition comparison, `δ_CΠ=Πδ_B`; its coefficient derivative is `Π′=δ_C Qdot+Qdot δ_B`, with the full differentiated prism and normalized weights. The output staircase and full-sign extraction commute with the appropriate Čech differentials.
7. Multiplication by p is a compatible module map of degree zero. For the formal equality rational coefficients suffice. For killing the boundary by Serre trace, p must be the authenticated global dual section and both boundary summands must have the independently admitted regular sheaf domains.

Input-degree indices, suppressing direction d, are:

- `T_n=LJ2_n : A^n → B^(n+2)`;
- `Q_n=LHRj : A^n → B^(n+1)`;
- `Π_m : B^m → C^m`;
- `Qdot_m : B^m → C^(m−1)`;
- `K_n=Qdot_(n+2) T_n−Π_(n+1) Q_n : A^n → C^(n+1)`.

Thus the boundary uses K_2 on Z, whereas the defect uses K_3 on ΔZ. Direction labels such as K_0,...,K_3 in equation (3) must not be confused with these input-degree subscripts.

## 2. Derive the selected chain map without assuming closed input

Let `U=Hδj` be the unsigned stage-one word and `J2=−HδU`. These words are the same in every input degree; U is not the signed degree-dependent first-stage inclusion.

Line by line:

1. `dU=dHδj=(1−P−Hd)δj=δj−jΔ`.
2. `dJ2=−dHδU=−δU+HδdU` since P vanishes on the degree-minus-one input δU.
3. Substitute step 1: `dJ2=−δU+Hδ(δj−jΔ)=−δU−UΔ`.
4. Put `E=δJ2−J2Δ`. Then `dE=δ(−δU−UΔ)−(−δU−UΔ)Δ=0`.
5. E has internal degree −2. The contraction therefore gives `E=dHE+HdE=dHE`.
6. Apply L: `δ_B T−TΔ=LE=LdHE=0`.

This proof needs neither closed Z nor bottom injectivity in degree −3. Bottom injectivity is relevant to the full HPL chain-map theorem, but is unnecessary for this selected stage-two identity. In particular, dropping `jΔ` at step 1 would invalidate the nonclosed argument.

## 3. Derive the inner overlap correction and its sign

First differentiate the literal words, using fixed δ:

1. `U′=(−ΓH+HΓ)δj−HδΓj=−ΓU−HCj`.
2. `J2′=−H′δU−HδU′=−ΓJ2+HCU+HδHCj`.
3. Therefore `T′=−LΓJ2+LHCU+LHδHCj`.

Now use `C=C0+dR+Rd`. Since RU has internal degree −2 and Rj degree −1, the projections in the following homotopy manipulations vanish:

4. `HCU=HC0U+RU−dHRU+HRδj−HRjΔ`.
5. `HCj=HC0j+Rj−dHRj`.
6. `HδHCj=HδHC0j+HδRj−δHRj+dHδHRj`.
7. Apply L, use `Ld=0` and `Lδ=δ_B L`, and add steps 4 and 6.
8. The middle terms combine as `LHRδj+LHδRj=LHWj`; the remaining two negative terms are `−δ_B(LHRj)−LHRjΔ`.

Consequently, with

`D= LHC0U+LHδHC0j+LRU+LHWj`,

one obtains

`T′=−LΓJ2+D−δ_B Q−QΔ`.

The sign of `−QΔ` comes from the retained projection `jΔ` in `dU`, not from any closure assumption. The first-face insertion R is a graded commutator: it is an anticommutator on internal degree −1. Treating it as an ungraded commutator would invalidate steps 4–8.

For completeness, the supplied overlap construction itself follows from `A_ij=Γ_j−Γ_i=a_ij+dXi_ij`, where `a=j_i(−θ_ij)`, and `R(X)=[Xi,X]_gr`. The graded derivation identity `d[Xi,X]_gr=[dXi,X]−[Xi,dX]_gr` gives `C=C0+dR+Rd`. Alternating first-face cancellation gives `δR+Rδ=W`, with the ambient restriction of Xi_jk, not a replacement by H_i(A_jk).

## 4. Derive the outer identity and fix its orientation

Let `Σ_a ρ_(e,a)=1` and `Σ_a dotρ_(e,a)=0`. The usual two-partition prism between ρ and `ρ+t dotρ` has differential equal to the second comparison minus the first. Differentiating at zero retains only the differentiated duplicated pivot: an undifferentiated duplicated pair has symmetric weight `ρ_aρ_b` and alternating cochain value, so its exchange sum is zero. The resulting full prism has all suffix weights, exactly as in the supplied formula.

The orientation can be fixed without trusting any high-degree sign: on a scalar degree-zero c,

`Qdot_1 δ_B c = Σ_(a,b) ρ_a dotρ_b(c_b−c_a) = Σ_b dotρ_b c_b = Π′_0 c`.

Thus the sign is `Π′=δ_C Qdot+Qdot δ_B`. Interior face cancellation and the normalization identities give the same formula in all degrees. Qdot has degree −1, so its Hom differential indeed has a plus sign. This formula cannot be replaced by a prefix-only prism; that would change both the operator and the domain obligations.

## 5. Operator-level identity, before selecting any input

For a homogeneous map f of degree k, write

`d_Hom(f)=δ_out f−(−1)^k f δ_in`.

T has degree 2 and is closed by §2. Q and K have degree 1; Qdot has degree −1; Π has degree 0. The graded product rule gives directly

`d_Hom(Qdot T)=d_Hom(Qdot)T−Qdot d_Hom(T)=Π′T`,

`d_Hom(ΠQ)=d_Hom(Π)Q+Πd_Hom(Q)=Π(δ_B Q+QΔ)`.

Subtracting yields the requested identity:

**`δ_C K+KΔ=Π′T−Π(δ_B Q+QΔ)`**.

The fully indexed calculation is equally explicit:

`δ_C K_n+K_(n+1)Δ`

`=δ_C Qdot_(n+2)T_n−δ_CΠ_(n+1)Q_n +Qdot_(n+3)T_(n+1)Δ−Π_(n+2)Q_(n+1)Δ`

`=[δ_C Qdot_(n+2)+Qdot_(n+3)δ_B]T_n −Π_(n+2)[δ_B Q_n+Q_(n+1)Δ]`

`=Π′_(n+2)T_n−Π_(n+2)[δ_B Q_n+Q_(n+1)Δ]`.

There is no special input or quotient by exact terms here. Combining with §3, and putting `E_conn=−LΓJ2+D`, gives

`(ΠT)′=δ_C K+KΔ+ΠE_conn`.

A consistency check worth retaining: fixed ambient δ does not imply Δ′=0. Differentiating `δ_B T=TΔ` gives `δ_B T′−T′Δ=TΔ′`; since `d_Hom²Q=0`, the above decomposition implies `δ_B E_conn−E_connΔ=TΔ′`. Thus the derivation does not accidentally assume a globally flat row frame.

## 6. Recover the remainder by Leibniz

The starting coefficient-adjoint remainder retains the full baseline/current-curl R* and differentiates only p and the kernel, holding each Z_d fixed:

`B_p=π15 S[pΠTR*−Σ_d((V_dp)ΠTZ_d+p(ΠT)′_d Z_d)]`.

Insert §5, separately for each direction:

- `−p(ΠT)′Z = −pδ_C KZ−pKΔZ+pΠLΓJ2Z−pΠDZ`.
- Combine the p-derivative and selector terms as `−Π[(Vp)LJ2−pLΓJ2]Z`.
- Restriction compatibility of p and the chain-map identities for S and extraction convert `−pδ_C KZ` to `−π15 δ_tensor[pSKZ]`.

This is exactly RESULT.md (2). The minus sign before both boundary and defect is forced by the original negative kernel derivative. Keeping an earlier inner-HPL boundary as an additional subtraction would process the same inner derivative twice.

## 7. Endpoint defects from ordered cup Leibniz

Write `t_ij(X)=g_ij^−1 Xg_ij`. Differentiating the cocycle `g_ik=g_jk g_ij` gives

`θ_ik=θ_ij+t_ij θ_jk`, hence `Δθ=0`.

For θ and s of Čech degree one, ordered cups with the genuine local-system transport satisfy

`Δ(θ∪s)=Δθ∪s−θ∪δs=−θ∪F`,

`Δ(s∪θ)=δs∪θ−s∪Δθ=F∪θ`.

Therefore

`Δ[(θ∪s−s∪θ)/2]=−(θ∪F+F∪θ)/2`.

On a quadruple the second cup is `F_ijk t_ik θ_kl`, so the transport is g_ik. A direct face expansion gives the same result: putting `x=θ_ij`, `y=t_ijθ_jk`, `z=t_ikθ_kl`, twice the defect equals

`(s_kl y−s_jk z)−(s_kl(x+y)−s_ik z)+(s_jl x−s_ij(y+z))−(s_jk x−s_ij y)`

`=−x(s_kl−s_jl+s_jk)−(s_jk−s_ik+s_ij)z`.

Thus `ΔZ_0=−C_(1,Q)/2`, `ΔZ_1=C_(0,Q)/2`, `ΔZ_2=−C_(3,P)/2`, and `ΔZ_3=C_(2,P)/2`. Multiplication by the common `−pK_d` gives precisely equation (3), with `+,−,+,−`. It is invalid to substitute only inside Qdot T while leaving the ΠQ half of the same defect untreated.

## 8. Independent formal control and what it detects

The companion `dependency_formal_control.py` was written independently for this audit and run under both ordinary Python and `python -O`. Both runs passed. It uses only integer coefficients of noncommuting formal words and these three rewrite identities:

- `δ_CΠ → Πδ_B`;
- `TΔ → δ_BT`;
- `δ_C Qdot → Π′−Qdot δ_B`.

It checks the operator identity in §5 before an input is inserted. Six mutations leave the following residuals (mutated left side minus correct right side):

- Change the inner sign of K: `2Πδ_BQ+2ΠQΔ`.
- Use `δ_CK−KΔ`: `−2Qdot δ_BT+2ΠQΔ`.
- Omit the outer nonclosed term: `−Qdot δ_BT`.
- Omit the inner nonclosed term: `+ΠQΔ`.
- Omit the inner boundary: `+Πδ_BQ`.
- Omit the outer boundary: `−Π′T+Qdot δ_BT`.

These are universal symbolic residuals, not assertions of nonzero physical values. The control does not prove the geometric premises, inspect source matrices, or test cancellation on the actual thirty retained inputs. The independently written arguments above establish why its rewrite relations are the correct ones.

## 9. Domain boundary and unresolved mathematical work

The two summands of KZ have different conditional domain proofs, both needed before Serre trace:

1. Qdot TZ uses the full differentiated prism, the missing-axis character sheaf, endpoint bound 35/15, differentiated-own weight 53/28, and every other own weight 54/29. Every sampled occurrence, including the duplicate pivot's distinct occurrence, is weighted. The normalized derivative restores the missing character, giving the full F-valued coefficient.
2. ΠQZ uses the overlap map's internal-degree-minus-two representation covariance, its 40/16 endpoint envelope, and the full ordinary 54/29 comparison. ΠQΔZ uses the conservative 48/20 bound. Qdot TΔZ uses `δ_BT Z=TΔZ` and the admitted restriction-domain argument, not endpoint closure.

The common F-valued domain allows subtraction. Multiplication by the global dual section p then makes a genuine canonical-valued Čech boundary. Its Serre trace is zero under those geometric premises. This is not a proof that a rational coordinate divergence has been constructed. No independent domain is asserted for individually expanded F-current factors: the scalar-free form inherits domain by equality.

The baseline/current-curl, coupled test/selector, overlap/cohomology corrections, and complete nonclosed defect all remain. The review proves their organization and signs, not their values or cancellation. A source-specific relation among those survivors remains the necessary new mathematical ingredient; repeating CM or discarding nonclosed endpoint defects does not supply it.
