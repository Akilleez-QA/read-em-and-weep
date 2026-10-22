# The nilpotent trace obstruction lands in a two-dimensional subquotient

## Assumptions

Retain all hypotheses, notation and unit u of [PR717, commit 7362df9da60a3b87b3200078a0145a376cc3056b](https://github.com/Akilleez-QA/read-em-and-weep/blob/7362df9da60a3b87b3200078a0145a376cc3056b/research/hm/nilpotent-trace-lift-invariance/PROOF.md). In addition use the pinned universal first-harmonic product from the dependency cited by PR716:

    B1(p_d,r_e)=tau2(p_d,r_e)/(2(d-1)(e-1)(d+e-1)),       (1)

for the positive even binary degrees used below. Here tau2(p,r)=p_XX r_YY-2p_XY r_XY+p_YY r_XX, with no divided-derivative factors. This normalization is the one in the universal harmonic-product theorem pinned at commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04.

The result is a canonical target reduction

    O_T: K -> f S5/(f² S2+k fg) ⊂ S8/(f² S2+k fg).       (2)

The target in (2) is canonically isomorphic, by division by f, to (S/(f,g))5 and has dimension two. This is not a rank computation or a vanishing assertion for the resulting map between two-dimensional spaces.

## 1. Two universal harmonic expressions

Write T=[[x,y],[z,-x]], with degrees 4,2,6. Put

    c=sc B1(n,n),
    b_ell=sc(B1(n,ell A)+B1(ell A,n)).

The scalar product is commutative, though matrix products are ordered. Thus entrywise expansion gives exactly

    c=u²(tau2(fg,fg)/1470 - tau2(f²,g²)/1350),           (3)
    b_ell=u(tau2(fg,ell f)/462 - tau2(f²,ell g)/550).    (4)

All denominators follow directly from the actual entry degrees: (8,8), (6,10), (8,4), and (6,6), respectively. First-normal nilpotence and the obstruction representative are

    u(2fgx+g²y-f²z)+c=0,                               (5)
    Psi(ell A)=ell(fx+gy)+b_ell.                        (6)

## 2. Polynomial congruences, not point evaluations

For the proof only, make an SL2(k) linear coordinate change so that the new coordinate X does not divide f, which is possible over the infinite field k. This preserves the normalization of tau2 and the harmonic product; it is used solely to prove the coordinate-invariant divisibility statement. Set t=Y/X and write F=f(1,t), G=g(1,t), L=ell(1,t). This is dehomogenization of identities, not an evaluation of an actual source or at a selected point. Primes below are formal differentiation of unspecified polynomials. For arbitrary homogeneous p_d,r_e with dehomogenizations P,R, the chain rule gives

    tau2(p_d,r_e)(1,t)
      =d(d-1) P R'' -2(d-1)(e-1) P'R' +e(e-1) P''R.  (7)

Apply (7) and work in the polynomial quotient k[t]/(F), without assuming F square-free. The product rule gives

    tau2(fg,fg)(1,t) ≡ -98 G²(F')²,
    tau2(f²,g²)(1,t) ≡ 180 G²(F')²,
    tau2(fg,ell f)(1,t) ≡ -42 L G(F')²,
    tau2(f²,ell g)(1,t) ≡ 60 L G(F')².                 (8)

Consequently (3) and (4) become

    c(1,t) ≡ -(u²/5) G²(F')² mod F,
    b_ell(1,t) ≡ -(u/5) L G(F')² mod F.                (9)

Regularity of the homogeneous pair implies gcd(F,G)=1. Reducing (5) modulo F and cancelling the unit G² in k[t]/(F) gives

    y(1,t) ≡ (u/5)(F')² mod F.                        (10)

Equations (6), (9) and (10) now show Psi(ell A)(1,t) is divisible by F. Homogenizing implies f divides some power of X times Psi(ell A). Since X and f are coprime, f divides Psi(ell A) in S itself. The proof remains valid for repeated factors of f. No actual roots, coefficients or derivatives were obtained or evaluated.

## 3. Dimension and canonical reduction

Since every representative Psi(ell A) lies in f S5 and the denominator f²S2+k fg lies in that subspace, O_T factors through (2). Multiplication by nonzero f identifies its reduced target with

    S5/(f S2+k g) = (S/(f,g))5.

The spaces f S2 and k g have dimensions three and one and have zero intersection by regularity. Since dim S5=6, the reduced target has dimension 6-3-1=2. This dimension argument is symbolic and does not evaluate any matrix rank.

The reduced class is explicitly

    Obar_n(ell) = [Psi(ell A)/f] in S5/(f S2+k g).      (11)

By the pinned PR717 lemma, changing the nilpotent T by eta A changes the numerator by f² eta ell/2 and hence changes (11) by f eta ell/2, zero in its target. Thus (11) is independent of T as well. The quotient has no residual source h or scalar first-normal coefficient in its displayed inputs.

## Contribution and next gate

The five-dimensional target of PR716 has a canonical three-dimensional quotient (S/(f))8. Its entire projection of the local variation obstruction vanishes by first-normal nilpotence and the harmonic-product identity. What remains is a canonically defined linear map S1 -> (S/(f,g))5 between two-dimensional spaces. Determining its vanishing or rank is still open here, as is the base fourth-square value. No substitution of a selected regular pair or actual HM/source instance, point evaluation, coefficient extraction or matrix-rank evaluation was used. The only calculation is a fixed four-term universal differential identity.
