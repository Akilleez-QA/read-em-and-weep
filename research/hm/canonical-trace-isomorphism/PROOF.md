# A canonical nilpotent lift forces the reduced obstruction to be a scalar isomorphism

## Statement and dependencies

Work over k=C(L), in the fixed binary harmonic frame of these pinned dependencies:

- [PR716, first-normal trace variation, commit 2a602d811b904def02bd56518fb0549e2911ff3e](https://github.com/Akilleez-QA/read-em-and-weep/blob/2a602d811b904def02bd56518fb0549e2911ff3e/research/hm/firstnormal-trace-variation/PROOF.md).
- [PR717, nilpotent trace lift invariance, commit 7362df9da60a3b87b3200078a0145a376cc3056b](https://github.com/Akilleez-QA/read-em-and-weep/blob/7362df9da60a3b87b3200078a0145a376cc3056b/research/hm/nilpotent-trace-lift-invariance/PROOF.md).
- [PR718, target reduction, commit 2411fcd92acd738d0d8af7bebc79ee9191b276ef](https://github.com/Akilleez-QA/read-em-and-weep/blob/2411fcd92acd738d0d8af7bebc79ee9191b276ef/research/hm/trace-obstruction-target-reduction/PROOF.md).
- [PR721, Jacobian nonvanishing, commit 53a2d26279bdafe258b6d7ce201f5d633f7e893e](https://github.com/Akilleez-QA/read-em-and-weep/blob/53a2d26279bdafe258b6d7ce201f5d633f7e893e/research/hm/trace-obstruction-jacobian-nonvanishing/PROOF.md).

Put S=k[X,Y], deg f=3, deg g=5, with (f,g) regular, u∈k×, A=S/(f,g), and J=f_Xg_Y-f_Yg_X. The dependencies prove Soc(A)=A6=k[J] with [J]≠0, dim A5=2, and a reduced map O:S1→A5 independent of the nilpotent first-normal lift T. They establish the normalized Jacobian identity Y O(X)−X O(Y)=(u/15)[J].

Let V=S1 and ω(X,Y)=1. The multiplication pairing V×A5→A6 is perfect: if h∈A5 multiplies to zero by both X and Y, it lies in the socle, which is concentrated in degree six, so h=0. Equal dimensions then give perfection. Define the resulting isomorphism i:V→A5 by

    m i(v)=ω(v,m)[J],       ω(X,Y)=1.

This note proves the stronger universal identity

    O=(u/30)i.                                           (1)

Consequently O is always an isomorphism under these hypotheses. This is a derivation from the precise harmonic expressions, not an assumption of rank two or an evaluation of the distinguished actual pair.

For any homogeneous h write Hess(h)=h_XX h_YY-h_XY², and let τ2 denote the undivided second transvectant. The proof constructs a canonical nilpotent lift and proves the stronger polynomial identity

    ell Ψ(ell)/f
      =u(f D_ell²g/40-g D_ell²f/12),                      (2)

where D_ell=α∂Y−β∂X for ell=αX+βY, and Ψ(ell)=ell(fx+gy)+b_ell for this canonical lift. Both sides of (2) are homogeneous degree six. The sign of D_ell has no effect on its square. Formula (2) immediately makes the quadratic q(ell)=[ell O(ell)]/[J] vanish identically.

## 1. Universal canonical first-normal nilpotence

Define a trace-free weight-four matrix T_can with entries

    x=u τ2(f,g)/112,
    y=−u Hess(f)/20,
    z=u Hess(g)/144.

The entry degrees are 4,2,6, respectively, as required. The nilpotence scalar from PR718 is

    C=u²(τ2(fg,fg)/1470−τ2(f²,g²)/1350).

We claim the polynomial identity

    u(2fgx+g²y−f²z)+C=0.                                (3)

Here is a direct formal verification, valid for arbitrary unspecified forms. Dehomogenize at X=1 with t=Y/X and use F,G and formal derivatives. The general transvectant identity is

    τ2(p_d,r_e)(1,t)
      =d(d−1)P R''−2(d−1)(e−1)P'R'+e(e−1)P''R.

It gives

    x/u=(6FG''−16F'G'+20F''G)/112,
    y/u=(F')²/5−3FF''/10,
    z/u=5GG''/36−(G')²/9,

and

    C/u²=F²(2GG''/63−(G')²/9)
            +F(2F'GG'/7−2F''G²/35)−(F')²G²/5.

Substitution cancels every term in (3). All terms of (3) are homogeneous of degree twelve; injectivity of dehomogenization on this space proves the homogeneous identity. No roots, square-free hypothesis, selected coefficients or points enter. This constructs a nilpotent T for every pair of forms, and lift invariance permits using it to compute the given O whenever the regular-pair hypotheses hold.

## 2. The quadratic multiplication pairing vanishes

With T_can the numerator is

    Ψ(ell)=ell(fx+gy)+u(τ2(fg,ell f)/462−τ2(f²,ell g)/550).

For L=ell(1,t), use L''=0 and the same transvectant identity. Direct product-rule simplification yields

    Ψ(ell)(1,t)/(uF)
      =L(FG''/40−F''G/12)+L'(−FG'/5+F'G/3).            (4)

The displayed equality is a polynomial identity after multiplying by F; it does not require choosing or evaluating any root. It follows also from the preceding target-reduction theorem that Ψ(ell)/f is a homogeneous degree-five polynomial.

Take ell=X, so L=1 and L'=0. Homogenization of (4), now to degree six, gives

    X Ψ(X)/f=u(f g_YY/40−g f_YY/12).                    (5)

In particular X O(X)=0 in A6. The factor X in (5) is essential: the right side has degree six, while Ψ(X)/f has degree five. No cancellation by X in A is used.

For completeness, the passage from (5) to every ell is justified by polynomial covariance, not by assuming that one vanishing diagonal entry proves q=0. Under any determinant-one linear change of binary variables, τ2 transforms equivariantly: it is contraction of two second-derivative tensors using two copies of the preserved alternating tensor. The same holds for Hess, since τ2(h,h)=2Hess(h). Products transform equivariantly as well. Therefore all three entries of T_can, both terms of b_ell and Ψ(ell) transform by substitution, with the same displayed constants. The binary-variable change does not mix the matrix entries: it preserves each entry's homogeneous degree. Thus the construction is equivariant as a map of the forms and the linear input ell.

For any nonzero ell=αX+βY, select a second linear coordinate m=γX+δY with αδ−βγ=1. Such a choice exists over k. In the coordinates (ell,m), differentiation in m with ell held fixed is −β∂X+α∂Y=D_ell. Apply (5) in that frame and pull back to the original frame. Equivariance gives precisely (2). The zero linear form satisfies (2) trivially. Both sides of (2) thus agree for every ell, without any selected actual-source or point evaluation.

The right side of (2) belongs to (f,g). Hence

    ell O(ell)=0 in A6 for every ell∈V.                 (6)

In particular the full quadratic q, not just one diagonal value, vanishes.

## 3. Identification of the entire map

Let M=i^(-1)O. By the defining pairing,

    (tr M)[J]=Y O(X)−X O(Y)=(u/15)[J].

Since [J]≠0, tr M=u/15. Also

    ω(Mell,ell)=0 for all ell.

For M=[[p,r],[s,t]], this quadratic is −s x²+(p−t)xy+r y². Therefore s=r=0 and p=t. Since k has characteristic zero,

    M=(u/30)Id.

This proves (1), including its normalization and sign. Equivalently the multiplication pairing is completely determined:

    m O(ell)=(u/30)ω(ell,m)[J].                         (7)

In particular Y O(X)=(u/30)[J] and X O(Y)=−(u/30)[J], consistent with the prior alternating identity. Its determinant under socle identification is u²/900, nonzero. This determinant is derived universally, not computed at an instance.

## 4. Consequences and remaining gate

There is no nonzero weight-four tangent D=ell A0 with a first-normal trace-orthogonal lift: PR716's obstruction criterion is O(ell)=0, and (1) forces ell=0.

Set Q8=S8/(f²S2+kfg). Multiplication by f induces an injection j:A5→Q8: cancellation of f in S identifies its image with fS5/(f²S2+kfg). Reduction modulo f then gives the exact sequence

    0 → A5 --j--> Q8 --π--> (S/(f))8 → 0.

The quotient has dimension three. PR716 gives the affine local leading fourth-square family r(ell)=r0+a j(O(ell)), with a∈k×. Its base r0 is assumed defined as in that dependency, including its divisibility hypotheses. By (1), j(im O)=ker π, so local cancellation is possible if and only if

    π(r0)=0 in (S/(f))8.

When this holds, let b=i^(-1)(j^(-1)(r0)). Its unique cancelling direction is

    ell=−30b/(au).

The rank-one possibility allowed by the alternating Jacobian identity alone is excluded by the exact harmonic identities. The only local existence gate is the three-dimensional immutable quotient of the base class. Neither that quotient for the actual base nor the base class itself has been evaluated or proved zero here. Local cancellation remains distinct from actual global completion changes, which do not move R4 under the preceding dependencies.

This theorem uses only fixed-size universal differential identities and equivariance. It makes no model substitutions, actual-instance evaluations, or broad computations.
