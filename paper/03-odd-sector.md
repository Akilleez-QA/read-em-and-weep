# 3. Odd-sector vanishing by a special octic nonextension

This section records the final exclusion in the odd chain. Its classification and residual-map inputs are the pinned dependencies of the [full source][O]; the local contradiction below is the decisive new boundary calculation.

## 3.1 The section curve and ordinary square

At an order-five hyperplane the section curve is the disjoint union C = Q ∐ Y, with ideal presentations

    I_Q = (z, q_c(y,u)),
    I_Y = (x², xq, q², g),
    g = κxz² − aq,
    a = cy,  q = Ay² + Bu²,  q_c = Cy² + Du².

Here c, κ, A, B, C, D are nonzero and q and q_c have no common root on the projective line. The letters A, B, C, D in this local display are scalar coefficients, not the representations or bundles of Section 1. Inversion fixes x, y, z and negates u. Write

    q₀ = ρx² + σyz,   ρσ ≠ 0,
    R = (u = 0),
    G = g|R / κ.

The relevant assertion is that q₀G² does not extend to a global section of I_C²(8). Throughout, I_C² is the ordinary ideal sheaf square. A symbolic square or an unsaturated polynomial-square substitute would not justify the argument.

## 3.2 Reduction to a quadratic contradiction

Suppose such an extension F exists. Averaging under inversion makes it even without changing its restriction. The even polynomial q₀g²/κ² already lies in I_Y² and has the desired restriction. Hence

    F = q₀g²/κ² + u²H,   deg H = 6.

The divisor u = 0 contains no component of Y. The regular codimension-two geometry makes O/I_Y² Cohen-Macaulay, so u is a nonzerodivisor and the ordinary sheaf colon gives H ∈ H⁰(I_Y²(6)). On the plane x = 0, the proved image ideal is q²(a,q)². The degree-two part of the ordinary square (a,q)² is spanned by a², giving

    H|x=0 = λa²q²,
    F|x=0 = a²q²(σyz/κ² + λu²).

At T = (z,q_c) in this plane, both a and q are units: a = cy does not vanish at either root of q_c, and the quadrics have no common root. Since F belongs to I_Q², the quadratic in parentheses must belong to H⁰(I_T²(2)). The complete-intersection square calculation gives H⁰(I_T²(2)) = C z². This is impossible because yz, u² and z² are linearly independent and σ/κ² is nonzero.

## 3.3 From the local contradiction to generic vanishing

The nonextension gives nonzero actual Cartan boundary on the weight-zero line. The full source proves that the accompanying mixed term extends, so it cannot cancel this contribution. Together with the already established weight-one boundary and the allowed-target classification, the last a = 12 residual branch is eliminated. The residual map has generic rank four; its projected component has rank two. The full first smoothing map from dimension six to dimension ten is injective. The generic odd section space is consequently zero.

The contradiction uses the square scheme at T, not only its reduced support. It also retains the hypotheses that the specified coefficients are nonzero and that q and q_c have no common root. No evaluation of a chosen Horrocks-Mumford instance is needed.

## Pinned source references

[O]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ec080c229105457eafcd2583c8a47b362627a62e/research/hm/order-four-quadratic-load/SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c/research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md
[F]: https://github.com/Akilleez-QA/read-em-and-weep/blob/846968261441fef2cad247d22b66d37aed3f0f8f/research/hm/order-four-quadratic-load/POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md
[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/04fb081d710f1d7e175f252601b96dddcd93106e/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md
[N]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9f28cb10c38d7a0e29c1eb994594325fea7f22bf/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md
[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/72aa6fb732a803eb9201f45f1f82e60f54d296b4/research/hm/order-four-quadratic-load/POSITIVE-GENERIC-FOUR-OR-FIVE-SECTIONS.md
