# Finite nilpotent transport retains the first-normal error

## Result and limitation

Let `Nhat^2=0`, let `D` be a derivation, and put

    E = H D(Nhat)+[Ahat,Nhat]-Lambdahat Nhat.

For a scalar s, the finite frame change `S=I-s Nhat` has inverse `I+s Nhat` and gives the EXACT identity

    Ahat^S = S Ahat S^(-1)-H (DS) S^(-1)
           = Ahat+(H Ds+Lambdahat s)Nhat+s E+s^2 E Nhat.   (1)

The last two terms disappear on the cone when its preservation equation holds. They do NOT disappear automatically at first normal order. Formula (1) is valid in any commutative coefficient ring with a derivation, including a square-zero normal thickening.

This is a universal local identity. It identifies neither the actual next normal connection nor an extension of the midpoint to `3Q`. In particular it does not turn a previously computed homogeneous cancellation coefficient into the full actual coefficient without comparison of all terms in (1).

## 1. Exact finite calculation

Since `Nhat^2=0`, expansion gives

    Ahat^S = Ahat+(H Ds)Nhat
             +s([Ahat,Nhat]+H DNhat)
             +s^2(-Nhat Ahat Nhat+H(DNhat)Nhat).

Right multiplication of the defining equation for E by Nhat gives

    -Nhat Ahat Nhat+H(DNhat)Nhat=E Nhat.

This proves (1), including the quadratic term. It is not obtained by retaining only the linear part of the gauge change.

Differentiating the square-zero identity also gives

    Nhat E+E Nhat=0.

The transported error therefore satisfies

    E^S=S E S^(-1)=E+2s E Nhat.                       (2)

Both (1) and (2) are exact. No assumption that E is zero in cohomology can replace the matrix identity `E=0` in (1).

## 2. The complete first-normal harmonic coefficient

Use a harmonic splitting with first product correction `B1`:

    L(p)L(r)=L(pr)+q L(B1(p,r)) mod q^2.

Matrix versions of `B1` mean matrix multiplication with this bilinear correction applied to each summand, at its own binary degrees. Suppose

    Nhat=L(n)+qL(T),
    Ahat=L(A)+qL(K),
    Lambdahat=L(lambda)+qL(lambda1),
    Dq=rho q,

and D preserves the harmonic splitting. Suppose also that s is a base scalar, so multiplication by s itself has no positive harmonic correction. Assume the cone equation

    H Dn+[A,n]-lambda n=0.

Then `E=qL(R) mod q^2`, where the FULL first error is

    R=H DT+(H rho-lambda)T+[A,T]+[K,n]-lambda1 n
      +B1(H,Dn)+B1(A,n)-B1(n,A)-B1(lambda,n).          (3)

Write `C=H Ds+lambda s`. Expanding (1), without discarding any first error, yields

    A^S=A+C n,

    K^S=K+B1(C,n)+C T+s lambda1 n+s R+s^2 R n.        (4)

Here `K^S` is the first-normal coefficient of the ENTIRE transformed connection. It is not just conjugation of an isolated old cancellation matrix. The term `B1(C,n)` is required even though s itself is base-only. A nonzero first error contributes both `sR` and `s^2Rn`.

The nilpotence assumption at this order includes the harmonic correction

    nT+Tn+B1(n,n)=0.

The already proved cone equation then implies `nR+Rn=0`. Accordingly (2) gives the first-error transform

    R^S=R+2s Rn.                                     (5)

No second-normal coefficient has been supplied or inferred.

## 3. Consistency with the actual Serre-lift sign

Fix the convention `J=[[0,-1],[1,0]]`, `sigma=(f,g)`, and

    n=sigma sigma^t J,
    tau(V)=sigma V^t J+V sigma^t J,
    w=sigma wedge V=f V2-g V1.

Direct multiplication gives

    nV=-w sigma,
    tau(V)n=w n,
    (I-s n)V=V+s w sigma,
    tau((I-s n)V)=tau(V)+2s w n.                     (6)

Thus if `R=tau(V)`, equation (5) is EXACTLY the vector transport in (6). This independently verifies the positive `+t w` scalar correction in ACTUAL-GLOBAL-SERRE-LIFT-FROM-THE-CONIC-COCYCLE.md, after retaining its convention `N_C=-n` and source-to-target transition `I+tN_C=I-t n`.

For the actual conic coefficient `s=rho_C/z`, `a=z^2`, and `lambda=H rho-u` with `rho=4z`, one obtains

    C=2rho_C H-rho_C u/z.

This is the cone correction already checked in ACTUAL-CONE-OPERATOR-PATCHING-FROM-THE-CONIC-COCYCLE.md. Equations (3)-(4) show precisely what extra information its continuation to first normal order must retain. They do not identify a chosen completion of the actual normal transition.

## 4. Physical equation frames and reproducibility

For a base scalar unit nu, if `q0=nu q`, then `T,K,R,lambda1` and `B1` in the physical splitting are divided by nu. The physical normal derivative is

    rho0=rho+D(nu)/nu.

The extra derivative of nu in `D(T/nu)` cancels its contribution from `rho0 T/nu`. Thus (3)-(4) are compatible with equation-frame transport. In the fixed positive Gram coordinates used in the actual applications, nu is one fixed nonzero constant, not an assigned numerical value.

Run `python verify_first_normal_transport_retains_error.py`. It checks (1)-(2) as full matrix identities with a universally parametrized square-zero matrix and arbitrary connection, derivative, and scalar symbols; checks the noncommutative first-normal coefficient bookkeeping; and checks all four Serre identities in (6). It evaluates no source-instance coefficient, matrix rank, or scan. Existing frozen artifacts are unchanged.
