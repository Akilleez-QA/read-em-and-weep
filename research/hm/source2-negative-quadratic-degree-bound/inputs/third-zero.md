# The actual positive third Bockstein vanishes identically

## Theorem and exact frontier

For the actual positive HM pencil, the cubic third gate

    Psi:D5 O_P(A)(-3) -> I_Sigma(6)

is ZERO. The specialized third Bockstein also vanishes in every projective smoothing direction, including the extra A-kernel line at each of the six second-symbol axes.

Thus the remaining generic finite positive Smith exponent, if it exists, satisfies

    4 <= e <= 31,

rather than the previous lower bound3. Generic total sections remain four or five. No fourth or later Bockstein value, generic surjectivity, or complete original proof repair is asserted.

## 1. The square channel is zero

ACTUAL-THIRD-BOCKSTEIN-VANISHES-ON-SQUARE-DIRECTIONS.md proves the exact restriction Psi|Delta=0. Its input is the full actual source-change/two-chart comparison, not a local residue heuristic:

- the actual divisor-defined quintic gives a global meromorphic source;
- the uniquely fixed scalar correction and Gram primitive are retained;
- the complete finite cocycle and affine coefficient-frame identities identify the resulting principal parts with the actual normal operator;
- the detectable C5 square input has zero cup already in H1(V O_L(-4));
- the other inputs vanish in the final quotient by characters;
- basepoint-freeness of the unique nonzero square channel forces that entire channel to vanish.

Only the detectable square input was claimed to vanish before the final quotient. The stronger all-input prequotient assertion is neither used nor implied.

The discriminant exact sequence therefore gives

    Psi=delta Psi1,   Psi1:D5 -> H0(I_Sigma(7)).          (1)

## 2. The actual fibers at the six semisimple axes are zero

ACTUAL-SEMISIMPLE-C5-AXIS-VECTOR-CUP-VANISHES.md treats an arbitrary order-five stabilizer axis a=st, with detectable input h=XY^3. The same actual meromorphic source is used, but its scalar correction and Gram primitive are recomputed for this input. In particular the primitive is A/(Bc)z^(-4), not zero.

With the oriented opposite chart v=-1/z, the complete cochain has

    principal_part_x(R)=alpha1 XYz^(-6)+alpha2 XYz^(-1),
    R_y regular.

Cup by a=z leaves only alpha1 XYz^(-5) as a pole. Its y-frame expression in V O_L(-4) is -alpha1 XYv, which is regular. Thus the actual cup is exact before the connecting D5 and second-symbol quotients. The normalizer supplies the other detectable input h=X^3Y.

The actual second-symbol cokernel at the axis consists of characters4,6, so every other D5 input is zero there by equivariance. This proves zero in the ACTUAL fiber

    I_Sigma(6)/m_p I_Sigma(6)=coker(beta2_p),

not merely ordinary evaluation of a polynomial vanishing on Sigma. The independent scalar/primitive audit checks the actual inverse u, oriented Gamma, and primitive uniqueness without relying only on the Laurent expansion.

## 3. The residual discriminant channel is zero

THIRD-GATE-VANISHING-AT-SIX-AXES-KILLS-RESIDUAL-CHANNEL.md proves the following actual geometry.

The second symbol has rank2 at every C5 axis. The normalizer permits rank0 or2; rank0 at six axes would force local length at least6 at each, contradicting total length24. The derivative from its weight0 kernel to its weight4,6 cokernel has no tangent weight2,8. Consequently

    I_Sigma,p is contained in m_p^2.

In fact Sigma is exactly the six length-four complete intersections locally given by (x^2,y^2), but the displayed inclusion suffices.

Since delta is a unit at every semisimple axis, the ACTUAL fiber vanishing from Section2 and(1) put each degree-seven component of Psi1 in

    m_p I_Sigma,p, hence in m_p^3.

The six axes have no three collinear and lie on no conic. For each axis omit that point and take the irreducible conic through the other five. A septic with triple zeros at all six points intersects each of these six distinct conics at least15 times, exceeding degree14. Each conic must therefore be a component. Their total degree12 exceeds7, so the septic is zero. Applying this to every component of Psi1 proves Psi1=0 and therefore Psi=0.

## 4. Specialization has one additional kernel line to check

The global D5 family alone does NOT automatically exhaust the kernel of the specialized second Bockstein at a rank-drop point. Away from the six axes, the rank is3 and its kernel is exactly D5, so the preceding result is the whole third Bockstein.

At an axis a=st, rank2 leaves the extra A-kernel line of C5 weight0. The direction a itself also has weight0, while the specialized target coker(beta2_a) has only weights4,6. The specialized third differential is equivariant, with cubic direction weight0. It therefore vanishes on this extra weight0 line. Equivariant lift choices exist by averaging over the finite stabilizer, so no choice breaks this weight argument.

There are no other rank-drop points, by the exact length-four description of Sigma. This proves the claim about EVERY specialized third Bockstein without assuming that kernel formation commutes with base change.

## 5. What remains unresolved

For a general direction, the positive pencil still has33 unit Smith factors and three factors of valuation2. Its last row either vanishes identically, giving generic positive kernel dimension5, or has finite valuation e. The present theorem gives e>=4. The linear-pencil maximal-minor degree bound gives

    6+e <= 37,

so e<=31. Thus fourth through thirty-first correctly iterated higher obstructions remain a finite unresolved gate. The proved third vanishing does not choose between generic section dimensions4 and5.

All source calculations used universal identities in arbitrary nonzero tensor-line symbols, exact geometry, or representation arithmetic. No selected actual HM coefficients, actual-instance map/rank evaluations, scans, or substitute local-model experiments were used.

## Reproduction

Run python verify_actual_third_vanishing_frontier.py. It reruns the finite-source, full-frame, square, semisimple and six-axis checks, then checks the specialized extra-kernel character and Smith bounds. The actual geometric comparisons and exact-sequence arguments are supplied by the named proofs, not certified solely by symbolic test output.
