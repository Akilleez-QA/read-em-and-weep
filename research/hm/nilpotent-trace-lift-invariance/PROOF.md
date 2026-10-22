# First-normal nilpotence makes the trace-obstruction map independent of the lift

## Assumptions and scope

Work over k=C(L) in precisely the fixed actual harmonic frame and weighted grading of [PR716, commit 2a602d811b904def02bd56518fb0549e2911ff3e](https://github.com/Akilleez-QA/read-em-and-weep/blob/2a602d811b904def02bd56518fb0549e2911ff3e/research/hm/firstnormal-trace-variation/PROOF.md). Let S=k[X,Y], let f=f3 and g=g5 be its regular homogeneous pair of degrees 3 and 5, and retain the nonzero coefficient unit u=u0 in k. Thus

    n = u [[fg,-f²],[g²,-fg]].

A trace-free matrix of weight d has entry degrees d,d-2,d+2. Keep the ordered first harmonic product B1 from PR716. Assume at least one regular trace-free weight-four T exists for which N=n+qT is first-normal nilpotent in the transported harmonic algebra. Explicitly its weight-twelve first square coefficient vanishes:

    {n,T}+B1(n,n)=0.                                      (1)

For a full filtered first-normal nilpotent lift, (1) is its leading weight-twelve equation: the lower bounds ord(n_full)>=8 and ord(T_full)>=4 exclude higher terms from this weight. We do not assume nilpotence follows from coherence alone.

Actual nonemptiness is supplied by the pinned dependencies, not an extra conjecture. The [canonical square-zero lift theorem, section 4, equation (11)](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md) proves U_a²=0 on 2Q. The [coherence theorem, section 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md) defines N_s=U_(s²)/s² on the negative chart where s is invertible (and similarly for t). Hence N_s²=0 there. Finally, [the corrected third-neighborhood theorem, section 2](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md) identifies the actual harmonic coefficients by N_s=L(n_full)+qL(T_full). Taking the leading weight gives (1). This uses the exact chart definition, not an assertion that N_s equals U_a/a for every source a.

Put A=[[f/2,0],[g,-f/2]] and K={ell A: ell in S1}. PR716 proves K is the entire weight-four trace kernel of n and defines

    O_T(D) = [tr(TD)+sc(B1(n,D)+B1(D,n))]

in Q8=S8/(f²S2+k fg), for D in K. Here sc=tr/2. This paper proves that O_T is independent of every choice of T satisfying (1). It does not compute this common map or assert its rank or vanishing.

## 1. The nilpotent-lift space is an affine copy of K

If T and T' satisfy (1), subtraction gives {n,T'-T}=0. Trace-free rank-two polarization over S gives {n,E}=tr(nE)Id. Thus T'-T belongs to K by the regular-pair syzygy of PR716. Conversely adding any E in K to a solution preserves (1). Consequently, whenever it is nonempty, the solution set of (1) is exactly T+K. The common unit u cancels from this kernel equation; there is no normalization or division by f or g.

## 2. Its action on the obstruction map is zero

Take E=eta A and D=ell A, with eta,ell in S1. Direct matrix multiplication, independent of any coefficients of f and g, gives

    A²=(f²/4)Id,
    tr(ED)=(eta ell/2) f².                               (2)

Only the ordinary T term in the displayed formula for O_T changes when T is replaced by T+E. Therefore

    O_(T+E)(D)-O_T(D)=[tr(ED)]=[(eta ell/2)f²]=0 in Q8.  (3)

The degrees are correct: eta ell is a quadratic. No unit u occurs in (2), since the kernel was parametrized without a unit; the trace-image ideal is unchanged by multiplying it by u in k^×.

There is also an explicit compatible correction at the lift level. Suppose a weight-zero D1 satisfies

    tr(nD1)=-tr(TD)-sc(B1(n,D)+B1(D,n)).

For T'=T+eta A, set

    D1'=D1+[[0,0],[eta ell/(2u),0]].                     (4)

Since the trace of n times the added matrix is -f² eta ell/2, equations (2) and (4) show D1' solves the corresponding equation for T'. Thus liftability, and not merely a necessary quotient test, is invariant under the whole affine nilpotent-lift space. This is a local statement, not a realization of these choices as global completions.

## 3. Contribution to the preceding vertex gate

Under the hypotheses of PR716, the variation of the leading fourth-square class along D is a O_T(D). If first-normal nilpotence is available, the resulting linear map K -> Q8 is determined by n and the fixed harmonic product, not by the first-normal coefficient T or its choice in the nilpotent-lift space. In particular, the unknown map cannot be changed by choosing another nilpotent first-normal lift. Its two-dimensional source and five-dimensional target remain exactly those of PR716.

This removes the first-normal lift as a dependency of that local variation gate. It does not eliminate the base value of the vertex fourth-square scalar, determine the common map, assert global realizability of D, or identify it with a Bockstein. No actual HM/source-instance coefficients, points, derivatives or matrix ranks are evaluated, and no large computation is involved.

## 4. Boundary against a false stronger argument

The scalar harmonic product is defined on even binary forms, the Veronese algebra k[X²,XY,Y²], rather than on all of k[X,Y]. Its normal deformation corresponds to the quadric relation xz-y²=q. A formal splitting argument for a deformation of the polynomial algebra k[X,Y] is therefore not available here: the odd forms f3, g5 and ell have no scalar harmonic lifts supplied by the inputs. This lemma deliberately does not infer universal vanishing from such a splitting.
