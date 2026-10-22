# Actual fifth lifts coexist with the nonzero fourth-square scalar

## Statement, scope and pinned inputs

Work over C with the actual marked rank-two bundle F, B=End_0(F), and the
integral quadric Q=(q=0). Write nQ=(q^n=0). Retain the physical-center-even
summand, not the extra Serre-involution grading. Let A=Sym^2 W and H=D5.
Fix any nonzero a in A. No particular a or positive source h is evaluated.

The assertion is an actual-family coexistence theorem: there is a nonzero
h in H for which a classified K=aJ4 extends to a global trace-free section
on 5Q, although its fourth-square scalar is nonzero. Every such fifth lift
has exact nilpotency index four. More precisely, every nonzero source in
ker(beta4_a) admits such a classified K, and

    dim ker(beta4_a) >= 1 + dim im(beta2_a).                  (1)

The kernel bound itself is elementary and is not claimed as new. The new
conclusion is its conjunction with uniform scalar nonvanishing in the
ACTUAL family, including realization by classified completion changes.
Thus nonzero rho4 cannot be an obstruction to fifth adjoint lifting even
within this actual family, rather than merely in an abstract countermodel.

We use these immutable results:

- [PR696, 958244d6d9d3b326f66c073a9d669717c953ec32](https://github.com/Akilleez-QA/read-em-and-weep/blob/958244d6d9d3b326f66c073a9d669717c953ec32/research/hm/scalar-parameter-descent/PROOF.md), section 1: fixed equivariant linear splittings give a polynomial actual J4(a,h) of bidegree (3,1). In particular it is linear in h for fixed a; it belongs to H0(B_(4Q)(10))_+ and restricts on Q to a^3 h N.
- [PR766, a43b46c98e53716978d0a7750843f2224b4d2408](https://github.com/Akilleez-QA/read-em-and-weep/blob/a43b46c98e53716978d0a7750843f2224b4d2408/research/hm/uniform-full-scalar-exclusion/PROOF.md): for every nonzero a,h, rho4(a,h) is a nonzero global section; every classified J4 has J4^2=q^3 S4 Id with the same S4=a^3 h rho4 !=0.
- [PR685, 449a8df60662bd7a1d93e318ea4f7e6dab28e5ad](https://github.com/Akilleez-QA/read-em-and-weep/blob/449a8df60662bd7a1d93e318ea4f7e6dab28e5ad/research/hm/third-lift-uniqueness/PROOF.md), sections 2--4: all s in A+D are realized by completion changes, and compatible fourth lifts J4'=J4-q^2 U_a tilde(s) satisfy delta5(aJ4')=delta5(aJ4)-beta2_a(s), in the ladder-compatible q-t a convention. Even fourth-lift changes with the third completion fixed have zero fifth boundary.
- [The actual fifth-boundary ladder at 8d8b5be4ce62c3055bb53be9e16d29cc63072f04](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md): beta4_a(h) is delta5(aJ4) modulo V_a=im(beta2_a).
- [PR770, b242300110c33627eb77ee5ab36cc81fffa359e4](https://github.com/Akilleez-QA/read-em-and-weep/blob/b242300110c33627eb77ee5ab36cc81fffa359e4/research/hm/faithful-fifth-norm/PROOF.md): E=H1(B_Q(4))_+=P4 has dimension four, and its faithful ideal-valued norm identification is tau_*:E -> H1(Qsq)_+, where Qsq=pi_*(I_Z^2(6)) is the ordinary square on the smooth weighted stack, not the square of a coarse annihilator ideal. For fixed K, nu(K)=tau_*(delta5 K), and raw zero is equivalent to a global fifth lift.

All completion changes below keep a,h,b=L_can(a,h),U_a and the marking fixed.

## 1. A raw-zero source exists for every negative direction

Choose once the polynomial actual family supplied by PR696. Since a is
fixed, the map h -> K(a,h)=aJ4(a,h) in H0(B_(4Q)(12))_+ is linear.
The exact sequence of locally free restrictions is

    0 -> B_Q(4) --q^4--> B_(5Q)(12)
      -> B_(4Q)(12) -> 0.                               (2)

Its connecting homomorphism is linear. Consequently

    T_a:H -> E,       T_a(h)=delta5 K(a,h)               (3)

is a linear map from a five-dimensional space to a four-dimensional one.
Thus dim ker(T_a)>=1. For every nonzero h in that kernel, exactness of
(2) supplies a global K5 in H0(B_(5Q)(12)) restricting to K(a,h).
The lift can be made physical-even by averaging. This is existence of an
actual adjoint section, not just vanishing of a scalar necessary test.

No source in this kernel is specified or evaluated. The conclusion holds
for every nonzero a, including second-symbol rank-drop directions. The
choice-dependent raw kernel need not be canonical; only its nontriviality
is required here.

## 2. The entire quotient kernel is geometrically realized

Let p_a:E -> E/V_a be the quotient. The published boundary interpretation
identifies beta4_a=p_a T_a, hence this is linear in h and (1) follows from
dim(E/V_a)=4-dim(V_a).

If beta4_a(h)=0 then T_a(h) lies in V_a. By the definition of this image
and the full A+D range in PR685, there is an s with

    beta2_a(s)=T_a(h).

Realize s by the classified third-completion change and choose its
compatible fourth lift J4'=J4-q^2 U_a tilde(s). PR685 gives

    delta5(aJ4')=T_a(h)-beta2_a(s)=0.                   (4)

Thus aJ4' extends to 5Q. Conversely a fifth lift of any classified fourth
choice has raw boundary zero; choice invariance modulo V_a forces
beta4_a(h)=0. We therefore obtain the precise equivalence

    h in ker(beta4_a)
    iff some classified aJ4 at that h extends globally to 5Q. (5)

This is not an assertion that the original fixed polynomial representative
has raw zero for every quotient-zero h. The completion correction is
essential in (4). In PR770's notation, the same correction subtracts
tau_*(beta2_a(s)) from nu(K), so it annihilates the faithful norm class as
well. No inverse or generic-rank assumption for beta2_a has been used.

## 3. Every resulting fifth lift has exact index four

Let h!=0 and let K5 be ANY global fifth lift of any classified K=aJ4
whose boundary vanishes. For a trace-free rank-two endomorphism the
Cayley--Hamilton identity reads

    K5^2=n(K5) Id,             n(K5)=-det(K5).

This identity is valid for line-bundle-valued endomorphisms, with powers
interpreted in their corresponding twists. On 4Q its scalar is

    n(K5)|_(4Q)=q^3 c,        c=a^2 S4 in H0(O_Q(18)).  (6)

The section c is nonzero: a and S4 are nonzero on the integral Q. Thus
n(K5) belongs to (q^3), and its associated-graded coefficient at order
three is c. It is not in (q^4). This is a global nonzero coefficient,
not a claim of a unit at every point of Q.

The cube restricts on 4Q to

    K5^3|_(4Q)=q^3 c a^4 h N !=0.                      (7)

Indeed a^4h is nonzero on integral Q, N is a nonzero section of the
torsion-free B_Q(2), and the q^3 last-layer injection on 4Q preserves
nonzero sections. On the other hand

    K5^4=n(K5)^2 Id=0 on 5Q,

because n(K5)^2 belongs to (q^6), which vanishes modulo q^5. Equations
(7) and this vanishing prove exact nilpotency index four, independently
of all fifth-lift choices. In particular none of these fifth lifts is
square-zero, despite being a genuine global adjoint lift.

## 4. Conditional index law on every higher thickening

There is a further consequence without any higher existence assertion.
Suppose n>=4 and a trace-free K_n in H0(B_(nQ)(12)) restricts to one of
the classified K=aJ4 in H0(B_(4Q)(12)). The twist remains twelve; this
is not a claim about later ladder steps with further multiplications by a.
Then

    nilpotency index(K_n)=2 ceil(n/3).                 (8)

To prove this, let s=n(K_n). As above, s has exact q-adic order three with
nonzero leading coefficient c=a^2 S4 on Q. Also K_n|Q=a^4hN!=0.
The q-adic graded pieces of a locally free sheaf on nQ identify with its
appropriate Q twists because q is a nonzerodivisor on the ambient smooth
space. For each k with 3k<n, s^k has leading coefficient c^k!=0, and
s^k K_n has leading coefficient c^k a^4hN!=0. These nonvanishings use
integrality of Q and torsion-freeness, and do not require c to be a unit.
Cayley--Hamilton therefore gives

    K_n^(2k)=s^k Id,       K_n^(2k+1)=s^k K_n,

both nonzero when 3k<n. They vanish when 3k>=n since they are divisible
by q^(3k). The first zero exponent is exactly (8). For n=4,5,6 the index
is four; for n=7,8,9 it is six.

## Contribution and limits

The raw dimension argument and the quotient dimension bound alone are not
new obstruction computations. Combining them with PR766 proves something
stronger than the previously stated logical caution: every nonzero
negative direction has ACTUAL nonzero positive sources whose globally
extendible fifth adjoints still have nonzero fourth-square scalar. The
classified realization (5) and the index law make that coexistence precise.

This does not determine beta4_a on any selected h, prove it identically
zero, prove higher lifts beyond 5Q exist, or give first-order obstruction,
higher integrability or algebraicity conclusions. Nonzero scalar means a
nonzero global section, not nowhere-zero. No actual coefficient, point,
derivative, source, matrix or rank is evaluated. The proof is deductive;
independent review is recorded separately, not proof-assistant certification.
