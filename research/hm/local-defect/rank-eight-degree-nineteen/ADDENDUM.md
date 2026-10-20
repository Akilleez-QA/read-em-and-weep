> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# The unique-plane-quartic case: coprime exclusion and the surviving cubic gcd

This addendum uses PROOF.md, including the verified generation by J*. Suppose h0(E)=25, so z6=14, and suppose the general plane section D has p4=1. The argument below excludes the coprime quartic/quintic alternative, but does not exclude all of p4=1.

## 1. Equality of the low-degree bounds

Link D in CI(4,6) using its unique quartic and a coprime sextic. The residual B has length5. Plane liaison gives

    p4=1+h1(I_B(3)),
    p5=3+h1(I_B(2)),
    p6=7+h1(I_B(1)).

Thus H_B(3)=5. The scheme B cannot be collinear, since a length5 collinear scheme has H_B(3)=4. Consequently H_B(1)=3; also strict Hilbert-function growth gives H_B(2)>=4. Therefore p5<=4 and p6=9. Restriction now gives

    14=z6<=c6<=c5+9<=c4+p5+9<=1+4+9=14.

Every inequality is an equality:

    c4=1, c5=5, c6=14, p5=4, p6=9.

Let h be the unique quartic equation of C. Its four independent linear multiples occupy four dimensions of I_C(5), so an additional quintic g exists outside h*S1.

As proved in the degree24 purity argument, reflexivity of E makes Z pure with at most finitely many non-Cohen--Macaulay points, and its general hyperplane section C is a pure Cohen--Macaulay curve.

## 2. The coprime alternative is impossible

If h and g are coprime, C lies in CI(4,5), of degree20. Complete-intersection linkage of the locally Cohen--Macaulay curve C gives a locally Cohen--Macaulay residual curve of degree1, necessarily a line. A line is arithmetically Cohen--Macaulay, and complete-intersection liaison preserves arithmetic Cohen--Macaulayness for locally Cohen--Macaulay curves. Hence C is ACM.

The pure-surface lifting argument in intermediate-sextic-surface-obstruction/ADDENDUM.md, Section7.3, applies: ACM implies surjectivity of ambient polynomial sections onto O_C(t) for every t and negative-twist vanishing. Purity gives H0(O_Z(t))=0 for t sufficiently negative. Induction in the regular hyperplane sequence then gives H1(I_Z(t))=0 for all t. The quartic h lifts to Z, contradicting z4=0.

## 3. The only possible gcd has degree3

Let a=gcd(h,g), with degree t. Since g is not a multiple of h, t<=3. Restrict to a sufficiently general plane, where the gcd remains of degree t and the two divided forms remain coprime. The sextic system has no common curve; its trace bound and the residual complete intersection give

    19<=6t+(4-t)(5-t).

For t=0,1,2,3 the right-hand sides are respectively20,18,18,20. The coprime case t=0 was excluded above. Thus any surviving unique-quartic case has t=3. Write

    h=a*l, g=a*q,

where a is cubic, l is linear, q is quadratic, and l does not divide q.

## 4. The residual to the cubic is a plane conic

Put C'=C:a. Multiplication by a identifies O_C'(-3) with a coherent subsheaf of O_C. Since C is pure, C' is pure as well. Also C' lies in CI(l,q), a plane conic. Its degree is at least1: the trace of C on a has degree at most18 by intersection with a sextic coprime to a. Thus deg C' is1 or2.

If deg C'=1, purity implies C' is a line. Its two independent linear ideal equations, multiplied by a, would produce two independent quartics on C, contradicting c4=1. Hence deg C'=2. The inclusion in the pure degree2 complete-intersection curve CI(l,q) is consequently equality scheme-theoretically: the kernel of O_CI(l,q)->O_C' would have finite support, impossible in the pure source. Therefore

    C:a = CI(l,q).

This reasoning allows reducible or nonreduced conics.

## 5. Exact remaining gap

Choose a sextic s in I_C(6) coprime to a; the sextic system has no fixed divisor. Since I_C is contained in I_C:a=(l,q), write s=l*A+q*B, with deg A=5 and deg B=4. The ideal

    K=(a*l, a*q, s)

has height2, and its Hilbert--Burch resolution is

    0 -> O(-6) direct-sum O(-9)
      -> O(-4) direct-sum O(-5) direct-sum O(-6)
      -> K -> 0.

The two syzygies are (q,-l,0) and (A,B,-a). Their maximal minors are the three indicated generators, up to signs; height2 follows because the first two generators have gcd a, whereas s is coprime to a. Its curve is ACM of degree

    (6^2+9^2-4^2-5^2-6^2)/2=20.

It contains C of degree19. This is not a complete intersection, so the residual-line liaison argument from Section2 cannot simply be applied. No proof here shows that removing the degree1 discrepancy preserves ACM, and no full unique-quartic exclusion is asserted.

The proved additional necessary structure is: if h0(E)=25 and p4=1, then C has a unique quartic a*l, its extra quintic is a*q, the residual C:a is the plane conic CI(l,q), and C is contained in the degree20 ACM Hilbert--Burch curve just described.

All claims use abstract sheaf and scheme geometry only. No actual source, matrix, operation, selected input, rank instance, jet or residue is evaluated.
