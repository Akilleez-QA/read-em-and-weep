# The detecting semisimple C5-axis vector cup vanishes

## Scope

This is a separate deduction from the square calculation. It uses the same actual divisor-defined meromorphic quintic and the independently checked full-frame/source-change theorem. Its algebra is universal in arbitrary nonzero A,B,c,lambda,k; no actual coefficient values, source-instance matrices, or ranks are evaluated.

For an arbitrary order-five stabilizer, take the semisimple smoothing line a=st. For the two positive-quartic characters which can contribute modulo the actual second symbol at this axis, the actual third cup vanishes already in H1(V O_L(-4)). The input h=XY^3 is proved explicitly; the other is its normalizer transform. This is a statement in the actual cokernel fiber, not mere vanishing of a polynomial at a point of Sigma.

The passage from these six fibers to a global third-gate conclusion is a SEPARATE geometric theorem. No complete original repair is asserted.

## 1. Keep the exact actual source

Use all notation and the actual meromorphic generator g0 from UNIVERSAL-DIVISOR-QUINTIC-TWO-CHART-SHADOW-CANCELLATION.md. Thus on s=1,

    f=A X^2Y+BzY^3+Ac z^2X^3-Bc z^3XY^2,
    g0=-lambda/(2Ac)(B XY^4z^(-3)+A X^3Y^2z^(-4)).

The regular targets and their source-to-target p_x,p_y are exactly those in that note. The opposite chart is v=-s/t; use its actual coefficient frames, not the raw derivative in s/t. The physical equation normalization is the same fixed nonzero nu.

Now let a=st, locally a=z, and h=XY^3. The exact source relation

    h f_z = m f+n g0

has

    n=A/(B lambda)[Ac X^2z^2+A XY+Bc^2 XYz^5+3Bc Y^2z^3],
    m=XY^2(AX+5BcYz^3)/(2Bc z^4).                       (1)

These follow by reducing h times the actual kappa=(d_L f)/g on D; the displayed polynomial identity also checks them directly. Equality on D alone is not used to discard a multiple of f: m is the exact source quotient in(1).

## 2. The actual scalar correction and primitive

The actual socle pairing gives, with one nonzero common scalar e,

    Q(XY^3)=e[-(A/B)X^2s^2+Y^2st]/4,
    Q(X^3Y)=e[X^2st+(B/A)Y^2t^2]/4.

The Hamiltonian derivation for a=st is t partial_t-s partial_s. Therefore the actual equation Q(u)=k a Lie_(D_a)(Qh), and the isomorphism on global sections Q(2), give

    u=(kA/B)X^3Y s^2-k XY^3st.

On s=1 the effective correction is

    Gamma=(kA/B)X^3Y+k XY^3z.                            (2)

The actual meromorphic Gram primitive is

    v0=A/(Bc) z^(-4).                                   (3)

Indeed the regular target values are exactly

    v0+tau(p_x,n)=-3cz,
    v0_y+tau(p_y,n_y)=-13A/(Bc) v^2,
    v0_y=z^2v0.

These are regular on both charts and realize the required transition cocycle. H0(O_L(-2))=0 makes this primitive unique. In particular setting v0=0 would give a FALSE nonzero residue; (3) is essential.

At the opposite chart a_y=-v and

    Gamma_y=z^(-2)Gamma-4kz^(-1)h
           =(kA/B)X^3Y v^2+3kXY^3v.

Both the affine connection term and the orientation are retained.

## 3. Complete cochain cancellation

Substitute (1)-(3), the same actual p_x,p_y, and these frames into the FULL canonical vector formula R. The companion symbolic verifier proves

    principal_part_x(R_x)=alpha1 XYz^(-6)+alpha2 XYz^(-1),
    R_y is regular,
    alpha1=3k lambda/(10Bc^2),  alpha2=-k lambda/(2A).    (4)

There are no other polar terms. The regularity statements include all source-m, scalar-extension, derivative, and Gram-primitive contributions.

The finite-source and full-frame identities in ACTUAL-MEROMORPHIC-QUINTIC-SOURCE-CHANGE-PRESERVES-VECTOR-CLASS.md identify these with the actual vector-class principal parts, not a substitute local model.

Cup by a=z at x and a_y=-v at y leaves only alpha1 XYz^(-5) as a possible polar part. But the meromorphic section of V O_L(-4) with x expression alpha1 XYz^(-5) has y expression

    z^4 alpha1 XYz^(-5)=-alpha1 XYv,

which is regular. Thus this pole is globally removable, and

    a [R/nu]=0 in H1(V O_L(-4)).                         (5)

This is before quotienting by the connecting D5 or by im beta2_a. It does not require a guessed value of the final annihilator.

For an independent final-test check, the P4 complement of Q(D5) in V tensor H0(O_L(2)) has the character-six vector

    i^t c proportional to Y^2t^2-(2A/B)X^2st.

Tensor-product apolar orthogonality to Q(XY^3) proves the ratio. Hence the test a i^t c has only X^2,Y^2 components, while both polar terms in(4) are XY. Their scalar pairings are zero as expected.

## 4. Which fiber has been killed

At a=st the C5 weights of A are8,0,2 and those of P4 are2,4,6,8. The actual quadratic second symbol has rank2 there, with image the weights2,8; an independent geometric proof appears in THIRD-GATE-VANISHING-AT-SIX-AXES-KILLS-RESIDUAL-CHANNEL.md. Its cokernel therefore has precisely weights4,6.

The third symbol is cubic in a, and this a has weight0. Only h=XY^3 and h=X^3Y can contribute to the cokernel. Equation(5) treats the first. An element of the normalizer interchanges s,t and X,Y up to nonzero factors, takes a to a nonzero multiple of itself, and interchanges these two input lines. Equivariance therefore gives zero for the second as well. All remaining input characters are zero in the cokernel by weights.

Consequently the entire map on this actual cokernel fiber is zero. By the universal orbit argument, the same is true at all six C5 axes. Since formation of a cokernel commutes with tensoring by the residue field, this means zero in

    coker(beta2) tensor k(p)=I_Sigma(6)/m_p I_Sigma(6),

not merely zero under the inclusion I_Sigma(6)->O(6). This distinction is necessary for the later multiplicity argument.

## Reproduction and limitations

Run python verify_semisimple_axis_vector_cup_cancellation.py. It imports only the preceding UNIVERSAL symbolic setup, retains every formal parameter, checks the exact relation and regular primitives, and verifies every polar coefficient and the global removal after cup. No selected HM coefficient, actual matrix/rank evaluation, or scan is used.

The third fiber vanishing is licensed by the exact normal-operator, finite-cocycle and coefficient-frame comparisons, not by the polynomial checks alone. It does not say the lower R class is zero. Indeed its surviving order-one term is generally nonzero before cup. It does not settle any fourth or later Bockstein.
