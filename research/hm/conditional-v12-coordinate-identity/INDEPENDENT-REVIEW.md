# Independent mathematical review

## Verdict and exact edition

PASS for the stated abstract coefficient-functional identity and its explicit conditional source-interface boundary.

Reviewed artifacts:

- `THEOREM.md`, SHA-256 `c0cde6780d6df5b73bebbdcdc7e1df7d11aeafc009baee9fc200dc166de31748`.
- `weights.json`, SHA-256 `764ed5d7c1c154a656b20c70b272e1ff185b00e730bbbaabada53d7825a2842f`.

Review date: 2026-10-20 UTC.

The review used direct symbolic reading and rational arithmetic. It did not execute a source generator, checker, selected HM instance, numerical rank computation, or formal verification.

## Independent branch expansion

Write a component key as `(j,n;b)`, with coordinate order in `b` equal to `(v1,v2,v4)`. Direct evaluation of the displayed one-form on the displayed frame gives the following contributions from each input:

- `B2 f0^(0)[1,-3,1]`: `B2` at `(1,0;1,-3,1)`, `(2,0;0,-3,1)`, and `(3,0;1,-4,1)`.
- `B3 f0^(0)[1,-1,0]`: `B3` at `(1,0;1,-1,0)`, `(2,0;0,-1,0)`, and `(3,0;1,-2,0)`.
- `W1 f1^(0)[0,-1,0]`: `-W1` at `(2,0;0,-1,0)`, `(3,0;-1,-1,0)`, and `(4,0;0,-2,0)`.
- `W2 f1^(0)[2,-4,1]`: `-W2` at `(2,0;2,-4,1)`, `(3,0;1,-4,1)`, and `(4,0;2,-5,1)`.
- `W5 f1^(1)[1,-3,0]`: `-W5` at `(2,1;1,-3,0)`, `(3,1;0,-3,0)`, and `(4,1;1,-4,0)`.
- `W7 f2^(0)[-1,-1,0]`: `W7` at `(3,0;-1,-1,0)` and `(4,0;-2,-1,0)`.
- `W8 f2^(0)[1,-4,1]`: `W8` at `(3,0;1,-4,1)` and `(4,0;0,-4,1)`.
- `W9 f2^(1)[-3,1,0]`: `W9` at `(3,1;-3,1,0)` and `(4,1;-4,1,0)`.
- `W11 f2^(1)[2,-4,0]`: `W11` at `(3,1;2,-4,0)` and `(4,1;1,-4,0)`.
- `W12 f3^(0)[-2,-1,0]`: `-W12` at `(4,0;-2,-1,0)`.
- `W13 f3^(1)[-4,1,0]`: `-W13` at `(4,1;-4,1,0)`.
- `W14 f3^(1)[1,-4,0]`: `-W14` at `(4,1;1,-4,0)`.

There are `3+3+3+3+3+2+2+2+2+1+1+1=26` branches. Grouping by their full component/order/coordinate keys gives 18 keys. The six vanishing groups are exactly those in the theorem. The other twelve groups give its conclusion, including the negative signs on the retained `W2` and `W5` terms and the replacement `-W1=-B3` at `(4,0;0,-2,0)`.

This confirms eight central and four first-normal terms. No first-normal input from root 0 occurs, so its otherwise necessary central `a4` coupling contributes no additional term.

## Polynomial weights

Every outer scale in `weights.json` was included. The three arrays for `W1`, `W7`, and `W12` agree, and multiplying them by `-1/4` gives the seven entries of `B3`. The two one-term arrays give `W9=W13=-u6^2 u7 u13/4`.

In the eight-monomial order stated in the proof, direct scaling gives

    B2 = (-1/4,0,0,1/4,0,0,-1/4,1/4),
    W2 = (1/2,3,-6,-1/2,-5/4,17/4,1/2,-1/2),
    W8 = (3/4,3,-6,-3/4,-5/4,17/4,3/4,-3/4).

Thus every coordinate of `B2-W2+W8` is zero.

In the stated four-monomial order, the scaled vectors are

    W5  = (0,3,-5/4,-7/4),
    W11 = (1/2,-33/2,6,10),
    W14 = (1/2,-39/2,29/4,47/4).

Their difference `W11-W14-W5` is zero coordinatewise. The remaining displayed weights are nonzero polynomials in the universal rational polynomial ring. Consequently “exactly six” is valid over that universal ring, not a claim that no additional terms vanish after specialization. The theorem expressly preserves that distinction.

## Derivative and specialization checks

Multiplication by a frame monomial shifts a requested coefficient by minus its exponent, as used throughout the expansion. For a Laurent monomial with exponent `a`, differentiation in coordinate `k` supplies the factor `a_k` and exponent shift `-e_k`, even when `a_k` is negative. This proves the displayed derivative-interface contribution whenever the indicated coefficient product is defined.

The component and frame-monomial product-rule factors add to the original exponent. The warning not to apply this derivative factor twice is therefore correct. The final reviewed edition explicitly requires well-defined coefficient extraction in the source-interface product, for example a finite coefficient convolution. The first-normal coefficient means the coefficient of `t`, not differentiation of a coefficient already restricted to `t=0`.

All identities are polynomial identities over the stated rational ring. Applying a homomorphism to a commutative rational algebra preserves them; it does not preserve a general nonvanishing assertion. No weight has been inverted.

## Scope and publication assessment

The two reviewed artifacts are self-contained for the abstract identity: the theorem specifies the frame, functional, coefficient convention, and exact polynomial arrays. They contain no private filesystem paths, recovery manifests, uncertain-operation narration, or dangling proof references.

The three source-interface requirements remain hypotheses, not conclusions:

1. The exact physical frame, full source field, owner/edge/pivot conventions, and density/derivative conventions must be bound to the source.
2. The entire selected predecessor support and complete cancelling pair must be established, not inferred from selected records.
3. A source-bound DAG/query certificate must identify coefficients, scales, and the same variable namespace.

The historical row counts and pair identifiers in that interface section are not independently certified by this review and are not used in proving the abstract theorem. Publication must not label this as a verified source reconstruction, an exhaustive reconstruction of a historical packet, an actual HM evaluation, or a cohomological/nonvanishing result. Subject to those explicit boundaries, the mathematical payload is suitable as a fresh conditional edition.
