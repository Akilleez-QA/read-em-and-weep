# The actual fourth value as a fifth-neighborhood adjoint boundary

## Fixed actual input

Use the explicit actual endpoint cochain U_a of
ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md:

    dU_a=q^2 Z_a,       U_a|Q=aN,                     (1)

where q=q0 and Z_a is the fixed closed natural cochain representing zeta_a
in H1(B). U_a is a global degree-zero monad cochain of twist four. Its induced
section on actual2Q is square-zero, but no use of square-zero at a higher
neighborhood is made below. All neighborhoods are restrictions of the ACTUAL
ambient bundle F, not hypothetical higher midpoint extensions.

Fix a direction a, source h in D5, and the same actual Schur/Bockstein choices
as in the canonical corrected-source theorem. Write b=L_can(a,h). The proved
second and third vanishing provide actual classes v_h,w_h in H1(B(2)) with

    q v_h=a h zeta_a,
    q w_h=a(v_h-b zeta_a).                            (2)

Here a,h,b are sections of O(2). This note constructs a global4Q adjoint
section whose5Q boundary represents the fourth value. It does not evaluate
that boundary, and does not identify it with a truncated vertex transport.

## 1. Why global chain primitives exist

Let D_M=Hom^bullet(M,M) be the full monad endomorphism complex, with the fixed
trace-free duality summand. For every t>=2, every sheaf term of D_M(t) has
vanishing positive cohomology. Up to constant representations/determinant
lines the terms are

    O(t-1), O(t), O(t+1), K(t), K(t+1), End(K)(t).

The first five have the usual positive Bott vanishing. For the last, the
identity used in the frozen actual monad-ratio theorem is

    End(K)(t)=Delta^-1 [S_(2,2)Q*(t+1)
                     +S_(2,1,1)Q*(t+1)+Lambda^4 Q*(t+1)].

Each twist t+1>=3 exceeds the largest partition part. Thus the same
Bott-dominance proof given there at t=2 applies to every t>=2. Consequently
H1(B(t)) is computed by GLOBAL cochains. The characteristic-zero fixed-duality
projection retains trace-free primitives; for families one can also apply the
finite-group equivariant projection.

Choose closed global degree-one representatives V_h,W_h of v_h,w_h in
D_M(2). Equalities (2) now give GLOBAL degree-zero cochains C_h,E_h of twist
four satisfying

    dC_h=a h Z_a-q V_h,
    dE_h=a(V_h-b Z_a)-q W_h.                          (3)

These are existence statements justified by actual global hypercohomology,
not claimed explicit evaluations of either primitive.

## 2. Exact normal-neighborhood ladder

Define the global degree-zero cochains

    J3=(a h-q b)U_a-q^2 C_h,       twist eight,
    J4=a J3-q^3 E_h,              twist ten.           (4)

Using (1),(3), with no coordinate division, gives the EXACT identities

    dJ3=q^3(V_h-b Z_a),
    dJ4=q^4 W_h.                                     (5)

Hence J3 induces a global adjoint section on actual3Q and J4 one on actual4Q.
The restricted monad remains a resolution of F on these nonreduced bases:
locally its end sequences split because its cohomology F is locally free.
The induced endomorphisms are trace-free by the retained fixed duality.
Their cone restrictions and normal boundaries are

    J3|Q=a^2 hN,       delta_(q^3)(J3)=v_h-b zeta_a,
    J4|Q=a^3 hN,       delta_(q^4)(J4)=w_h.            (6)

The ambient boundary targets in (6) are H1(B(2)). They use exactly the
published sign convention delta=[d(cochain)/q^r]. No fresh rescaling of N,
Z_a or the Hamiltonian is introduced.

Multiplying J4 by a produces a section of B_(4Q)(12) restricting to a^4 hN.
In the ACTUAL exact sequence

    0 -> B_Q(4) --q^4--> B_(5Q)(12)
         -> B_(4Q)(12) -> 0,                          (7)

the boundary of this particular section is precisely

    partial_5(a J4)=[a W_h|Q] in H1(B_Q(4))_+=P4.      (8)

Its image in the second-symbol quotient is therefore the ACTUAL value

    beta4_a(h)=[partial_5(a J4)] mod im(beta2_a).       (9)

This proves a full actual-neighborhood comparison, not merely an equality
of dimensions or lowest homogeneous residues.

## 3. What the comparison does and does not decide

For these fixed choices, vanishing of (8) is equivalent to extending the
particular section aJ4 from4Q to5Q. Vanishing of (9) is weaker: the boundary
may be a nonzero second-symbol value. These two assertions must not be
silently identified. The usual source corrections and Bockstein quotient
are retained in (9); on the generic rank-three open its target is one line.
No assertion of constant target dimension at the six exceptional axes is
needed for (7),(8).

Changing C_h or E_h by a global closed cochain, with V_h,W_h fixed, does not
change (8), since (5) remains exact. Changing the Bockstein representatives
or source corrections must be tracked by the already established Bockstein
indeterminacy; this note does not declare such changes zero before quotient.

The actual first-normal lift U_a is explicit. The further primitives C_h,E_h
in (3), or equivalent actual geometric data that evaluates (8), remain to be
constructed/evaluated. In particular this ladder is not a substitute for the
missing full-frame comparison of a local next-error coefficient. It supplies
a precise actual target for that comparison without invoking a3Q midpoint.

## Reproduction

Run python verify_actual_fourth_normal_neighborhood_boundary.py. It checks
the full formal differential ladder, every twist and restriction exponent,
and the uniform Bott-dominance inequalities. The actual existence inputs
are the multiplied-lift theorem, the proved second/third Bockstein statements,
and the chain-Hom comparison in ACTUAL-AMBIENT-ATIYAH-MULTIPLIER-IS-THE-MONAD-RATIO.md.
No source coefficient, actual-instance matrix/rank or fourth value is evaluated.
