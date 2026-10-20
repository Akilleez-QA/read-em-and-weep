# Independent audit of the exact cusp base source

20 October 2026. Formal mathematical record; no obstruction coordinates were evaluated.

## Verdict and source verification

Accepted: all eight terms of equations (2) and (3) in [cusp-base-source-formula.md](cusp-base-source-formula.md) are correct under their stated compatible square-root frames and stipulated pair-character first lift. There is no missing power of F, reversed matrix product, omitted root derivative, incorrect cup endpoint, or extra factor of two to correct. The general ordered-coefficient version of N5 is also correct.

This review directly fetched and read the full pinned PR16 file, not only excerpts or an inherited citation:

- Commit c8aec970fd65a105f39f4e8aeb8a17f0f0053f89.
- Returned blob SHA a58834ab61e18a5dedd8a7bf20bec7121bfa9165.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

I also read the current cusp normalization formula and independent audit, the branch-boundary extension, and the relevant root/frame portions of its independent audit. The earlier first-order cancellation, target representation, polynomial specialization, and six-condition reductions remain imported premises. The present audit establishes the source expansion, not those separate theorems.

One implementation-contract addition is warranted, without changing the mathematical formula: retain PR16 §7's mandatory first-order comparison calibration for N and N^{-1}, giving 16Π = −4[q1∪q2+q3∪q4], as well as zero for E. The five-item contract in the base-source report verifies the E first-order equation but does not explicitly repeat the two line calibration tests. They must not be lost in a later physical implementation.

## 1. Root identities, including the second derivatives

Write A=h_{αβ}, B=h_{βγ}, H=h_{αγ}=BA and g_e=τ_e h_e, where τ_e²=l_e and τ_{βγ}τ_{αβ}=τ_{αγ}. These are actual compatible root transitions. Put

    c_{i,e} = (∂_i l_e)/(2l_e),  ∇_{i,e}=∂_i+c_{i,e}.

The extended derivation on the étale root chart satisfies V_iτ_e=τ_e y_i c_{i,e}. Consequently, for any base matrix Z,

    V_i(τ_e Z) = τ_e y_i∇_{i,e}Z,
    V_i²(τ_e Z) = τ_e[F_i∇_{i,e}²+(F_i'/2)∇_{i,e}]Z.

In particular

    ∇_i² Z = ∂_i²Z + 2c_i∂_iZ + (∂_ic_i+c_i²)Z.

Thus the derivative of the root connection coefficient is present in L_i; it is not permissible to interpret ∇_i² as ∂_i²+2c_i∂_i+c_i². There is no F_i'∂_i term beyond the displayed F_i'/2: V_i is y_i∂_i on base functions, not F_i∂_i.

For r≠s, the logarithmic coefficients have ∂_rc_s=∂_sc_r, so

    V_rV_s(τ_e Z) = τ_e y_ry_s∇_{r,e}∇_{s,e}Z.

For u_e=τ_e y_ry_s U_e, one instead has

    V_ru_e=τ_e y_s[F_r∇_{r,e}+F_r'/2]U_e,
    V_su_e=τ_e y_r[F_s∇_{s,e}+F_s'/2]U_e.

These identities prove the report's L,D operators, including all root contributions. For b=y_ry_sβ the corresponding identity has no τ connection:

    V_rb=y_s d_rβ, V_sb=y_r d_sβ,
    d_iβ=F_i∂_iβ+(F_i'/2)β.

Using D in place of d in the gerbe derivative would be wrong; the report correctly distinguishes them.

PR16 §6's original rational frame q has q²=x(1−t²), not x. Therefore using that frame while setting l=x is invalid unless the explicit unit is absorbed by an actual square-frame change. The audited report does not make that substitution: its étale square-frame hypothesis is exactly what justifies the logarithmic-half formula. The extra transitions within one fixed base chart are ±1 and have zero derivative.

## 2. First-order equation and matrix convention

The source's row equation is

    u_{βγ}g_{αβ}+g_{βγ}u_{αβ}−u_{αγ}
      = b g_{αγ}−μ_p(g_{βγ},g_{αβ}).

With U_e=h_eX_e, its left-hand side is

    τ_{αγ} y_ry_s [B X_{βγ} A + BA X_{αβ} − H X_{αγ}].

After left multiplication by H^{-1} the bracket becomes

    X_{αβ}+A^{-1}X_{βγ}A−X_{αγ}.

The normalized μ_p coefficient is precisely the antisymmetric product of ∇B and ∇A in equation (1), with B differentiated first and A second. Scalar root factors cancel but cannot be cancelled before differentiation. The extraction of y_ry_s coefficients uses the finite-flat odd summand; it is not division by y at a branch point or at the cusp.

## 3. Independent eight-term check

Each expression below is the source term divided by the common scalar τ_{αγ}, before the final left multiplication by H^{-1}. This specifies the matrix order unambiguously.

1. u_{βγ}u_{αβ} gives F_rF_s U_B U_A. Both odd factors occur twice. There is no A or B conjugation to add once U_B=BX_{βγ} and U_A=AX_{αβ} have been used.

2. μ_p(u_{βγ},g_{αβ}) gives

    1/2 [F_s(D_{r,βγ}U_B)(∇_{s,αβ}A)
         −F_r(D_{s,βγ}U_B)(∇_{r,αβ}A)].

The first F_s comes from the two remaining y_s factors, not from D_r. Interchanging F_r and F_s outside the brackets would be wrong.

3. μ_p(g_{βγ},u_{αβ}) gives

    1/2 [F_r(∇_{r,βγ}B)(D_{s,αβ}U_A)
         −F_s(∇_{s,βγ}B)(D_{r,αβ}U_A)].

This is not a reordered copy of term 2; the matrix products remain in the source order.

4. μ_pp(g_{βγ},g_{αβ}) gives

    1/8 [(L_{r,βγ}B)(L_{s,αβ}A)
         +(L_{s,βγ}B)(L_{r,αβ}A)
         −2F_rF_s(∇_{rs,βγ}B)(∇_{rs,αβ}A)].

There are four summands from the square of the antisymmetric pair operator. Its two mixed negative summands coincide because the factor derivations commute, producing −2, while each pure-square term is already encoded in L. The coefficient is 1/8, not the 1/4 belonging to the cross-pair piece in PR16 §8.

5. T_{p,αβ}(g_{βγ})g_{αβ} gives

    λ[a_{r,α}F_sQ_{s,αβ}(∇_{s,βγ}B)
       +F_rQ_{r,αβ}a_{s,β}(∇_{r,βγ}B)]A.

The first scalar a is evaluated at α and the second at β, exactly as required by the Alexander–Whitney cups a_r∪q_s and q_r∪a_s. Both Q values are on αβ; T differentiates B on βγ and is then multiplied by A. These operations are not on the same edge. Since T is a derivation with specified scalar coefficients, it does not differentiate those coefficients while acting on B.

6. −b u_{αγ} gives −F_rF_s β U_H.

7. −b²g_{αγ}/2 gives −F_rF_s β² H/2. The F factors are squared odd generators, not F_r²F_s². Left normalization subsequently makes this term scalar; that does not make b central in the star product.

8. −μ_p(b,g_{αγ}) gives

    −1/2 [F_s(d_rβ)(∇_{s,αγ}H)
          −F_r(d_sβ)(∇_{r,αγ}H)].

The derivative is of H on αγ, not of A or B separately. The sign and derivative order follow from b appearing on the left of g in PR16's triple-unit action. This is precisely the noncentral term lost by commuting that unit across a row transition.

The complete accepted formula is therefore unchanged:

    C_p = H^{-1}(N1+N2+N3+N4+N5+N6+N7+N8),

with Nj exactly as in equations (2) and (3) of the audited report. No separate term is asserted to be a cocycle or a boundary.

For general constant ordered coefficients c_rs,c_sr, direct expansion gives

    s_r=c_rs a_r∪q_s − c_sr q_s∪a_r,
    s_s=c_sr a_s∪q_r − c_rs q_r∪a_s,
    T_p=s_rV_s−s_sV_r.

This verifies every sign and endpoint in the report's replacement N5. The replacement β also uses the correct distinct triangle edges. Changing an ordered representative still requires its actual Čech equivalence.

## 4. Cusp and global-domain checks

At F_i=x_i³ the substitutions F_i'/2=3x_i²/2 in D,L,d are exact. The scalar primitive is a_{i,0}=−x_i/2, a_{i,∞}=0, and δa_i=V_i(y_i/x_i)=x_i/2. Substituting this primitive into term 5 gives the stated −λ/2 times the two ε-weighted summands. Neither summand vanishes uniformly over all overlaps. Simplifying Q_i to 1/x_i is valid only on the oriented standard overlap; reversed and refined edges keep their actual coefficient cochains.

In the infinite chart z=y/x²,t=1/x, direct derivation of the cusp relation gives V(t)=−z and V(z)=−1/2. This confirms the report's regularity check. All operators are regular before rational-coordinate expression. Invariant normalized terms descend by the finite-flat invariant summand, with h,l,X and odd generators transformed together. A coefficient such as 1/x need not be regular on an individual chart, only on its specified overlap.

Compatibility with normalization is also exact: x=w²,y=w³ and V~=(w²/2)∂_w imply V~ν*=ν*V on regular cusp functions. Hence all eight terms pull back before the normalization gauge removes b,T. The gauge also changes the actual first lift. The simpler four-term global-star expression belongs to the transported lift, not to an expression formed by dropping N5–N8 from the cusp source.

## 5. What is and is not established

The full PR16 descent identities and the stipulated first-order equation give δC_p=0, so its cusp specialization represents the claimed pure obstruction. No new denominator or division by F,F',y is introduced by this audit. The passage to the compact six-coordinate target, the identification with v=Q(1,0,0), and injectivity of v↦v+Rv remain the explicitly imported earlier results.

The formula is a complete exact symbolic representative. It does not supply X's actual coefficients, an obstruction coordinate, a cohomological primitive, a proof of vanishing, or a second-order module.
