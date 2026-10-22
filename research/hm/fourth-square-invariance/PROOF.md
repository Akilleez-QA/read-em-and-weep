# An intrinsic fourth-neighborhood square obstruction

## Fixed data and scope

Work over C on the actual X=P4 with locally free rank-two F and
B=End_0(F). Let Q=(q=0) be the integral invariant quadric and rQ=(q^r=0).
Retain physical-center-even parity and the fixed marking. Fix the permitted
nonzero sources a in Sym^2 W and h in D5, with nonzero restrictions to Q,
the canonical correction b, and the actual cochain U_a.
Here a belongs to Sym^2 W and is center-even; negative coordinate type
does not mean odd center parity. The established identities are

    U_a|Q=aN,        U_a^2=0 on 2Q,
    J3=(ah-qb)U_a-q^2C on 3Q,       J3^2=0,
    J4|3Q=aJ3,      J4|Q=a^3hN.

J3 has twist8 and J4 has twist10. All sections are induced actual bundle
endomorphisms, not arbitrary raw cochain matrices. The actual ladder gives
at least one even J4. PR685 proves that changes of even completion class
give J3' = J3-q^2Ns, with s in H0(O_Q(2))_+=A+D, and a compatible change is

    J4' = J4-q^2 U_a s on 4Q.                         (1)

Here s is lifted to an ambient quadratic. Any other even fourth lift over
that J3 differs by q^3Nt, with t in A+D. We use these classified changes,
not arbitrary changes of a,h,b or the marking.

We prove an intrinsic scalar obstruction and a characteristic-line
criterion. We do NOT prove that the scalar vanishes or compute a fourth
Bockstein value.

## 1. Every allowed fourth lift has the same square

Although U_a itself is an adjoint section only on 2Q, multiplication by
q^2 defines the canonical injection

    B_(2Q)(6) --q^2--> B_(4Q)(10).

Products with its image depend only on the other factor restricted to
2Q. This is a local free-module identity, so also holds where Q is
singular. In particular

    J4|2Q = a(ah-qb)U_a.

For the correction D=-q^2U_a s in (1), D^2=0 modulo q^4 and

    J4 D + D J4 = -q^2s {J4|2Q,U_a}=0,

because U_a^2=0 on 2Q. Thus (J4+D)^2=J4^2. For the remaining change
q^3Nt, the cross term depends only on J4|Q=a^3hN and vanishes by N^2=0;
its own square is zero. These two operations exhaust the even fourth
lifts under consideration. Their common square is independent of both
the completion class and the fourth-lift choice.

## 2. The unique scalar and its forced a-squared factor

For any trace-free rank-two endomorphism over a C-algebra, Cayley-Hamilton
says J^2=(tr(J^2)/2)I. Since J4^2 restricts to a^2J3^2=0 on 3Q, the scalar
restriction sequence gives a UNIQUE positive section

    sigma in H0(O_Q(14))_+,       J4^2=q^3 sigma I.    (2)

The twist is20-6=14. Multiplication by q^3 identifies O_Q(14) with the
last layer in O_(4Q)(20); injectivity uses that q is a nonzerodivisor on X.
Thus sigma, not merely its zero locus or a residue class, is choice-independent.

There is a further forced divisibility. Locally lift J3 to a trace-free
section L of B_(4Q)(8), and write J4=aL+q^3K, K in B_Q(4).
Such local lifts exist because B is locally free. Then

    L^2=q^3 chi I,
    sigma=a^2 chi+a tr((J3|Q)K)
         =a^2[chi+ah tr(NK)].                         (3)

The rank-two polarized identity {L,K}=tr(LK)I supplies the middle equality.
Consequently sigma is locally divisible by a^2. Since Q is integral and
a is a nonzero section, the quotients glue uniquely to

    tau in H0(O_Q(10))_+,       sigma=a^2 tau.         (4)

Neither chi nor K is canonical, but tau is. This argument divides only
after proving regular local divisibility; it does not invert a across
its zero locus. No divisibility by h is asserted.

## 3. Exact local square-zero criterion and absence of a gluing gap

Write I for the actual Serre zero-scheme ideal of N, as used in the pinned
third-square theorem. In particular this is not merely the ideal of its
reduced support. That theorem supplies the exact trace image and vanishing

    im[tr(N-):B_Q(4)->O_Q(6)] = I^2(6),
    H0(I^2(6))_+ = 0.                                 (5)

Any LOCAL trace-free fourth lift of the fixed aJ3 differs from J4 by
q^3K. Its scalar in (2) is sigma+a^3h tr(NK). Therefore local square-zero
extendability is equivalent to

    sigma belongs to a^3h I^2(6),
    equivalently tau belongs to ah I^2(6).             (6)

The corresponding scalar quotient has twist14 before, or twist10 after,
the proved division by a^2. The equivalence uses integrality, not division
by a unit. This is a complete local criterion, but no containment in (6)
is established here.

If (6) holds everywhere on Q, the quotients sigma/(a^3h) glue to a global
section of I^2(6). They are positive because sigma,a,h are positive. The
vanishing in (5) forces sigma=0. Conversely sigma=0 makes the already
existing global J4 square-zero. Hence the following are equivalent:

    local square-zero fourth extensions of aJ3 exist everywhere;
    sigma=0 (equivalently tau=0);
    every classified even global J4 is square-zero.

There is no additional global gluing obstruction for this PROPERTY once
the local scalar containment is known. This does not construct local
extensions or prove their existence.

## 4. Characteristic-line obstruction on the regular nilpotent locus

Let U be the open subset of Q where a^3hN is a nonzero rank-one matrix.
This open is nonempty for the stated nonzero sources. Consider the
corresponding open in 4Q. A J4-invariant line subbundle there has a scalar
action lambda, locally a function after trivializing O(10). From (2),

    lambda^2=q^3 sigma modulo q^4.

Reduction modulo q and reducedness of Q imply lambda=q r. Cancelling q^2
gives r^2=q sigma modulo q^2. Reducing again modulo q gives r=q t, so
lambda belongs to (q^2) and lambda^2=0 modulo q^4. It follows that sigma=0
on that open. This excludes nonzero nilpotent eigenvalues as a way around
the obstruction; it is not merely a statement about a zero-eigenvalue kernel.

Conversely, if sigma=0, J4 has square zero. On U one matrix entry is a
unit. For a local trace-free matrix [[x,y],[z,-x]], a unit off-diagonal
entry, say y, gives a free kernel generated by (y,-x), because x^2+yz=0.
If initially only a diagonal entry is a unit, the same identity makes
both off-diagonal entries units. Thus the kernel is a line direct summand,
and these intrinsic kernels glue. It is J4-invariant and J4 acts by zero.
This kernel is canonical, but other invariant lines can exist over the
nonreduced base; no uniqueness of all invariant lines is claimed.

Accordingly a characteristic line exists on the full regular nilpotent
locus exactly when sigma=0. If sigma is a nonzero global section, it
cannot vanish on any nonempty open of the integral Q; there is then no
J4-invariant line subbundle on any nonempty open of that locus.
No extension across the zero-scheme or source divisors is asserted.

## 5. A sharp nilpotency dichotomy, not a square-zero conclusion

Equation (2) always gives J4^4=0 on 4Q. Its cube is

    J4^3=q^3 sigma a^3hN.

Since B_Q is torsion-free, N is nonzero, and Q is integral, this cube is
nonzero exactly when sigma is nonzero. Also J4 itself is nonzero because
its cone restriction is a^3hN. Thus the global nilpotency index is either2
when sigma=0 or4 when sigma is nonzero, never3. Its cube is also unchanged
under all classified choices, since their differences have q-order at
least2. The unresolved scalar selects the two cases. This is not a claim
about the fourth Bockstein, which is a different boundary obstruction.
In particular nonzero sigma alone does not obstruct extension as an
adjoint section to 5Q, and is not identified with a nonzero beta4.

## Immutable dependencies and verification

- [PR685: classified third and fourth lift changes](https://github.com/Akilleez-QA/read-em-and-weep/blob/449a8df60662bd7a1d93e318ea4f7e6dab28e5ad/research/hm/third-lift-uniqueness/PROOF.md).
- [Actual fourth-neighborhood ladder](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md).
- [Actual third-square theorem and exact square ideal](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md).

This is authored structural mathematics, independently reviewed as recorded
separately. The bounded verifier checks universal rank-two identities,
q-adic orders and twists only. It does not verify actual selected source
coefficients, evaluate sigma, or provide proof-assistant certification.
