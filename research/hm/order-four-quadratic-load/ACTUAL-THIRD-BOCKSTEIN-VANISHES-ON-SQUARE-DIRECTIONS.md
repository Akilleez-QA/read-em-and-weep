# The actual third Bockstein vanishes on square directions

## Theorem

For the actual positive HM pencil, the restriction of the third Bockstein

    Psi:D5 O_P(A)(-3) -> I_Sigma(6)

to the discriminant conic of square smoothing directions is ZERO.

Equivalently, the actual cubic third gate belongs to the one-dimensional discriminant-divisible channel. This theorem alone does not assert that the remaining channel vanishes or is nonzero, and does not settle generic sections or later Bocksteins.

## 1. Actual class comparison and the detectable input

Fix any point x in the twelve-point C5 orbit on L=P(W), and let y be the other fixed point of its stabilizer. Use abstract eigenlines as in the uniform C5 theorem. Let a=t^2 have divisor2x, and let h=X^4 be the detectable positive-quartic character.

UNIVERSAL-DIVISOR-QUINTIC-TWO-CHART-SHADOW-CANCELLATION.md constructs the ACTUAL divisor-defined meromorphic quintic g0, the exact source relation m,n, the canonical scalar correction u, and the uniquely determined actual Gram primitive. Its full vector-cochain calculation gives

    principal_part_x(R/nu)=alpha Y^2z^(-2)/nu,
    principal_part_y(R/nu)=-4alpha Y^2v^(-4)/nu,
    v=-1/z,  alpha != 0.

ACTUAL-MEROMORPHIC-QUINTIC-SOURCE-CHANGE-PRESERVES-VECTOR-CLASS.md proves the missing geometric comparison: the full finite cocycle identity and exact coefficient-frame covariance show that these principal parts represent the SAME actual normal-operator class as the original orthogonal twelve-pole representative. The m and Gamma affine connection terms, the actual source-versus-target convention, the nonzero Atiyah scalar k, and the physical equation factor nu are retained. This does not assume that local principal parts form a global differential.

Cup by a multiplies the x expression by z^2 and the y expression by1. The x expression becomes regular. The remaining y part is the principal part of the global meromorphic V O_L(-4) section with constant x expression -4alpha Y^2/nu. Hence

    a[R/nu]=0 in H1(V O_L(-4))

for THIS detectable input h=X^4. The established normal-operator/third-Bockstein comparison therefore gives Psi_a(h)=0 in the actual final quotient.

## 2. All other inputs vanish in the final quotient by characters

At this square a, the actual second symbol has rank3. In the binary C5 convention its image has weights2,4,6 in P4, and the final quotient has weight8. The square a has weight2; cubic homogeneity contributes weight6. Thus only a positive quartic h of weight2 can contribute to the final quotient. That input line is precisely X^4, treated above.

Every other h maps to zero in the FINAL QUOTIENT by equivariance. This argument does not claim that every other h has zero cup already in H1(V O_L(-4)); prequotient vanishing has been proved only for the detectable character and is all that is needed.

Therefore the entire map Psi_a:D5->coker beta2_a is zero at this square. The construction is uniform over the stabilizer orbit and uses no selected actual coefficient values or actual-instance rank computation.

## 3. One zero fiber excludes the whole square channel

THIRD-BOCKSTEIN-POLARIZATION-AND-SQUARE-DIRECTION-GATE.md proves that the square restriction lies in the unique equivariant line

    Hom_G(D5,Sym^18 W).

Every nonzero map on this line is basepoint-free. Indeed a common-zero invariant divisor could only have degree12, leaving an impossible injection D5->Sym^6 W=V+P4 after division.

The zero full fiber from Section2 contradicts basepoint-freeness unless the actual square restriction is identically zero. This proves the theorem.

## Scope and reproduction

The discriminant exact sequence identifies the remaining gate as delta times an equivariant D5-valued section of I_Sigma(7). Its coefficient is not evaluated by this theorem. The generic alternatives of four or five sections remain unresolved.

Run the two-chart, finite-source-cocycle and meromorphic-frame verifiers cited in the source notes. The small companion verifier checks the exact detecting character and basepoint obstruction. All computations are universal polynomial identities or representation arithmetic; no actual HM coefficient assignment, matrix/rank evaluation, scan, or local-model replacement is used.
