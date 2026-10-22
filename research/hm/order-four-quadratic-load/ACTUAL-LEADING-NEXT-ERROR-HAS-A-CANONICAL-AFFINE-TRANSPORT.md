# Canonical leading affine transport of the next error

## Conclusion and scope

The weight-four coefficient of the next error has two indispensable affine transition terms:

`R2,j = Ad(P) R2,i + F_P(R1,i) + L2,j(Z_ij,0)`,                 (1)

where

`F_P(R)=B1(P,R)P^-1+B1(PR,P^-1)`,

`L2(Z)=H0 DZ+[A0,Z]+(2H0 rho-Lambda0)Z`.

The second term is harmonic transport of `q R1`. The third comes from the second-normal mismatch of the locally truncated nilpotent. Neither can be discarded. The mismatch has the exact nonzero cohomology class

`[Z0]=-(B lambda/4)[eta_ap]`,                                  (2)

in the same q and apolar marking as the preceding normalization proof. Relative to `q0=nu q`, its scalar coefficient is divided by `nu²`.

Regular choices of second-normal bundle transitions cannot change (1). Its leading trace-compatible affine gluing problem has a unique solution, because its tangent coefficient is `Wprime O(-1)` with H0=H1=0. This conclusion uses the full affine cocycle and trace compatibility proved below, not acyclicity alone. It is a statement about the weight-four coefficient only, not about weight eight, an ambient third-neighborhood midpoint, a global square-zero N2, or beta4.

## 1. Conventions and fixed actual inputs

First work in a common physical normal-equation frame on an overlap. All determinant and coefficient-line transports are included before writing matrices. We use the harmonic products B1,B2 from the preceding nilpotence proof. Let

`N_i=L(n_i)+q L(T_i)`,

`E_i=Hhat D N_i+[Ahat_i,N_i]-Lambdahat N_i`

`   =q L(R1,i)+q² L(R2,i) mod q³`,

and `Dq=rho q`. The relevant weights are

`n:8`, `T:4`, `H0,A0,Lambda0:4`, `R1:8`, `R2:4`.

The actual lowest first-normal connection and its harmonic affine transition have already been checked in `ACTUAL-LOWEST-NORMAL-CONNECTION-HAS-AN-EXPLICIT-NEXT-ERROR-TERM.md`. This supplies compatibility at the weights used here. It does not assert compatibility of every higher term. In particular, unknown higher first-normal connection discrepancies start too high to alter (1). The present proof does not set the complete R1 to zero.

For the genuine midpoint first-normal pair, and an ordered transition i→j, write P for its leading marked matrix and define the literal mismatch

`N_j-Ad(P_hat)N_i=q² Z_ij mod q³`.                           (3)

This is a definition of the midpoint mismatch, not a global second-normal nilpotent or an actual endpoint adjoint lift. At an actual endpoint there is additionally a q-order mismatch whose leading weight is eight. Its first error contribution has weight twelve, and its second error contribution starts at weight eight, so it cannot change the weight-four law proved here. Equation (3) is not asserted literally for that endpoint pair; those higher-weight first-order terms must be retained in the subsequent weight-eight problem. In the conventional two-chart Cech frame, with everything transported back to x, it reads

`Z_xy=N_y^x-N_x`, `delta s=s_y^x-s_x`.

Reversing the arrow reverses this transported mismatch. This is important when using an explicit P_y→x formula.

## 2. The second coefficient of harmonic conjugation

A leading marked transition is a diagonal base transition followed by a lower triangular transition whose off-diagonal entry has cover degree two. Its harmonic inverse is exact: products of two nonconstant lower entries contain E21²=0, and all products with base scalars have no positive harmonic correction.

In this convention,

`Ad(P_hat)(L(n)+qL(T))`

`=L(PnP^-1)+q L(PTP^-1+F_P(n))+q² L(U_P(n,T)) mod q³`,

where the complete coefficient is

```
U_P(n,T) = F_P(T)
           + B2(P,n)P^-1
           + B1(B1(P,n),P^-1)
           + B2(Pn,P^-1).
```                                                     (4)

For the marked triangular transition the two B2 terms vanish, since the only nonconstant entries of P and P^-1 have degree two. The iterated B1 term does not vanish in general. If the target N_j is its fixed first-normal truncation, (3) gives `Z_ij,0=-U_P(n_i,T_i)` for this ordered arrow.

For `P=[[1,0],[p,1]]`, the complete expression is particularly transparent:

```
U11 = -B1(p,T12),       U12=0,       U22=-U11,
U21 = 2B1(p,T11)-p B1(p,T12)-B1(pT12,p)
      -B1(B1(p,n12),p).
```

It has entry degrees `(0,-2;2,0)`, with the upper entry absent. Thus it lies in the actual weight-zero, physical-twist-minus-two coefficient bundle, not an unmarked scalar line.

## 3. Derive the affine error law

For a compatible connection, conjugating the operator and the nilpotent conjugates its error. Harmonic transport of `qR1` has second coefficient `F_P(R1)`. Replacing the transported nilpotent by the target truncation adds `q²Z`. Applying the error operator to this difference gives

`q²[H0 DZ+[A0,Z]+(2H0 rho-Lambda0)Z] mod q³`,

because `D(q²)=2rho q²`. This proves (1).

Unknown second-normal connection coefficients contribute commutators with n, and unknown second-normal symbol/scalar coefficients contribute their ordinary action on n. Their weight bounds below exclude them from (1). No global third-neighborhood connection or bundle has been presumed.

## 4. Which transition choices can enter this weight?

Normalize an extra first-normal transition as `I+qQ`. A regular adjoint coefficient Q has minimum weight minus two: its lower entry can be cover-degree zero, but no regular upper or diagonal entry permits a smaller weight. Its effects on Z are of types `[Q,T]`, B1-products with n, and quadratic Q-products with n. Their minimum weights are respectively two, two, and four. Its effect on R2 through `[Q,R1]` starts at weight six.

An extra second-normal transition `I+q²C` has the same regular lower bound, minus two. It changes Z by `[C,n]`, of weight at least six. Thus it cannot change Z0. Unknown regular second-normal connection coefficients similarly affect R2 through a commutator of weight at least six; scalar/symbol terms have minimum weight zero and contribute only weight at least eight.

Leading homogeneous triangular/root transitions have exact harmonic products, as explained above. More generally, arbitrary lifts of the actual first-normal transitions can fail the triple cocycle by `I+q²C_ijk`. Such a regular C_ijk again has weight at least minus two. Its action on n starts at six, so it does not spoil the cocycle law for Z0. Its induced error action starts above four. These statements permit a leading affine cocycle even when the actual midpoint bundle has no global third-neighborhood extension.

Conic and higher stabilizer corrections remain in the full transport; their already established positive weight raises place them above the coefficients isolated here. None is silently removed from the full problem.

## 5. Identify the actual mismatch class

The coefficient bundle of Z0 is

`0 -> V O_L(-10) -> J_eta -> O_L(-2) -> 0`,

with the already proved identification `J_eta=P4 O_L(-8)`. The weights follow directly: a diagonal coefficient has O(-2), and a lower degree-two coefficient has O(-7-2-1)=O(-10). Its trace map is the injection

`J_eta -> Sym8(Wprime) O_L(-4)`

whose image is the degree-eight square relation. There is no regular tangent of weight zero, so this trace map has zero kernel.

Squaring (3), with trace-free local lifts, gives

`tr(n Z_xy)=chi_y^x-chi_x`.                                  (5)

The preceding normalization theorem proves

`chi_bar=-(B lambda/4)n_ap`,

and the fixed apolar cocycle satisfies `tr(n eta_ap)=delta n_i`. Taking the connecting class of the exact trace sequence proves (2), with the Cech sign fixed above.

There is also a regular X-chart certificate, not only a cohomological dimension argument. The previous theorem gives

`chi_x+(B lambda/4)n_x=Q f²+a f g_x`,

with its explicit regular Q,a. Define

`S_x=[[a/2,0],[-Q,-a/2]]`.

Then `tr(nS_x)=chi_x+(B lambda/4)n_x`. Choose the compatible local certificates on the remaining charts. Injectivity of the weight-zero trace map gives

`Z0+(B lambda/4)eta_ap=delta S`.                             (6)

This identifies the surviving affine mismatch with the normalized apolar class. It neither assigns the independent actual displacement scale c_eta nor constructs a global N2.

## 6. Scalar compatibility and the canonical affine correction

Put

`C(n,T,R1)=tr(TR1)+tr B1(n,R1)`.

Exact harmonic conjugation and cyclicity of the scalar matrix trace give

`C(n_j,T_j,R1,j)-C(n_i,T_i,R1,i)
 =-tr(n_j F_P(R1,i))`,                                     (7)

with all ordinary line transports understood. Also the cone equation gives the exact identity

`tr(n L2 Z)=[H0 D+2(H0 rho-Lambda0)]tr(nZ)`.                 (8)

The verifier checks (7) for unrestricted abstract homogeneous coefficients in every matrix entry of the required degrees, and checks (8) algebraically using `H0Dn+[A0,n]=Lambda0n`.

Together with (5), these identities show that (1) preserves the full scalar constraint

`tr(nR2)=H0Dchi+2(H0rho-Lambda0)chi-C(n,T,R1)`.              (9)

In particular, it preserves the **affine** trace datum, not an unjustified assertion `tr(nR2)=0`.

The leading triple compatibility established in Section 4 makes the affine correction in (1) a genuine coefficient cocycle. The coefficient theorem supplies

`0 -> Wprime O(-1) -> E4 -> Sym12(Wprime) O -> 0`.

Locally choose any lift of (9), which is possible by its surjective trace map. The difference between its transitions and (1) then lies in `Wprime O(-1)`. It is a cocycle by (1) and (7)–(9). Its H1 is zero, so it has a correcting local cochain. Its H0 is zero, so the resulting affine-compatible family satisfying (9) is unique.

This is the precise sense in which the known leading trace and the complete affine law give a canonical weight-four correction. It is not a claim that the raw local R2 matrices are zero, nor that one may discard the nonzero Z0. It also does not compute the higher-weight actual error or its final obstruction class.

## 7. Normal-line covariance

The formulas above were written only after choosing a common physical-q frame. On an overlap with `q_j=u_ij q_i`, normal coefficient r acquires the inverse factor `u_ij^-r`, in addition to the ordinary tensor/frame transition of the quantity being expanded. Thus Z has the appropriate inverse-square normal factor in addition to N's own twist, and R1/R2 have inverse first/second normal factors in addition to E's twist.

Furthermore

`rho_j=rho_i+D log u_ij`.

For a pure normal-equation frame change, with other tensor frames held fixed,

`[H0D+2H0rho_j-Lambda0](u^-2 Z)
 =u^-2[H0D+2H0rho_i-Lambda0]Z`.

The commutator term transports in the usual way. This explicitly explains why the `+2H0rho` in (1) cannot be dropped. Choosing a local equation with a convenient derivative is not the same as annihilating the globally fixed normal section. The physical conversion `q0=nu q` and its factor `nu^-2` in (2),(5),(6) remain as in the preceding normalization proof.

## Verification and limits

Run `python verify_leading_next_error_affine_transport.py`.

It checks universal homogeneous harmonic formulas, the full scalar compatibility, normal-line covariance, the regular apolar cochain sign, and all choice-degree bounds. No actual coefficient values or instance rank tests occur. All earlier frozen files remain unchanged. Weight-eight effects and beta4 remain uncomputed.
