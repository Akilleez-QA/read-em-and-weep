# Independent review: the stored quotient projections

## Verdict

Accepted. On all six pinned denominator localizations,

    P_i=J_i^-1 E_Di^t(Id-gamma H0_i),
    P_i gamma=0.

This uses the separately proved, source-bound identity H0_i gamma=Id5 and a fresh literal identification of every stored P entry. It does not use primitive A, the historical receipt, transition determinant normalization, or a source evaluation. The 120-position remaining-A normal form is also correct. Full A remains unproved by this package.

Reviewed producer PROOF.md SHA256:

    bd746d262cfa8172e6988e9ad459a8a60f29c365eb2fbdf5157793b4c6a70f39

The included retraction proof has SHA256 `c4ac035e0a50bcb449e0ee151910c1ffa3bda9b297e38d95dd63ab5e8ea84841`, the final version independently reviewed in the prior package. Thus the new projection argument is based on the proved retraction, not on an A-dependent consequence that happens to have the same name.

## 1. Independent derivation of the primary normalization

Use the primary inverse with denominator D=t(abcd-t^4), in the exact cyclic domain and selected ambient orders of the retraction proof. For a general ambient vector u, set x=H0u. In the two selected D coordinates, the source gamma rows are

    (gamma x)_D0=a x2+d x3,
    (gamma x)_D1=-c x1-b x4.

Therefore the normalized coordinates of u-gamma x are necessarily

    q0=z0-a x2-d x3,
    q1=(z1+c x1+b x4)/t.

The factor 1/t in q1 is essential because I_D=diag(1,t); it cannot be discarded merely because the finite chart0 has t=1.

I derived the numerator coefficients independently from the already proved inverse recurrence. For each row below, list the four F-cycle coefficients in order (yA,yB,yC,yD), with common denominator D. The result is

    q0: -(a^2 t^3+ac d^2 t),
        -(a^2 b d t+d^2 t^3),
        -(a^2 b t^2+d t^4),
        -(a t^4+c d^2 t^2).

    q1: -(ac^2 t+b t^3),
        -(c t^3+b^2 d t),
        -(ab c^2+b^2 t^2),
        -(c^2 t^2+b^2 c d).

The selected D coefficients are D for q0 and D/t=abcd-t^4 for q1. All coefficients at the fifth F coordinate and at S vanish. These are exactly the producer's formula (2), including every sign, exponent of t, and ordering. This derivation is a short symbolic elimination on the universal sparse pattern, not a multiplication or expansion of the actual source arrays.

The checker maps the formal labels (t,a,b,c,d) to the five cyclic source labels, removes v0 factors, and compares signed exponent records independently for each carrier. It checks the two selected gamma rows as well as I_D and the denominators. In particular it does not assume a cyclic action on the full stored I or P arrays: it checks the actual P arrays in all five cases.

## 2. Independent auxiliary calculation

Write a=v1,b=v2,c=v3,d=v4 and D5=-a^2cd. From the triangular inverse,

    x1=y11/a,
    x4=-y4/(ac)-y8/a+y11/(a^2c).

The two selected source gamma rows are -c x1-b x4 and d x4. Since J=diag(1,-d/a^2), the normalized coordinates are

    q0=z0+c x1+b x4,
    q1=-(a^2/d)z1+a^2x4.

Over D5, q0 has F coefficients abd at y4, abcd at y8, and -ac^2d-bd at y11; q1 has a^3d, a^3cd, and -a^2d in those same positions. The D coefficients are D5 and a^4c. There are no other coefficients. This independently agrees with every term in producer formula (4) and with its literal template.

The auxiliary diagonal sign is consequently fixed by J, not guessed from the primary pattern. Inverting the stored denominator already makes the required a,c,d units, so this proof introduces no extra localization beyond the chart being used.

## 3. Scope of the source checks

I read the complete static checker and reran it under normal and optimized Python. The outputs agree byte-for-byte. The checker compares:

- all 180 stored P cells, including empty entries;
- all 60 entries in the selected gamma_D blocks;
- 24 entries in I_D and 18 denominator records;
- 60 literal-zero I_F cells and 420 literal-zero H1_(F union D) cells.

It hashes the exact source before interpreting it. The model SHA256 is `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`, already bound to Git blob `fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761`. The current-head provenance of these same bytes was established in the preceding package; this review makes no new remote-fetch claim.

The function named term only encodes a fixed list of inert variable labels as an exponent tuple. No source polynomial is used as an operand of a multiplication, cancellation, inverse, derivative, or evaluation. No production code is imported. The run checks source binding and literal agreement; the handwritten derivation supplies mathematical correctness of the expected template.

I also inspected and reran the separate invented-control script in normal and optimized modes. Its unrelated 3-dimensional rational example verifies the exact case and isolates each of the three remaining defect families while preserving the new retraction/projection identities. Both runs pass identically. Its matrices have no source inputs, so this is a control of the abstract block theorem, not a physical sample. The retained source-byte negative controls reject in both modes.

## 4. Formal consequences and precise remainder

The now established equality P=J^-1 E_D^t(Id-gamma H0) immediately gives Pgamma=0 by the retraction identity. The support facts give PI=Id2, PH1=0, H0I=0 and H0H1=0. Therefore gamma H0+IP is an idempotent with image im(gamma) direct-sum im(I).

The kernel statement is equally direct: H0u=0 forces u_F=0 because gamma_F is invertible; then Pu=J^-1u_D. Thus

    ker H0 intersect ker P = span(E_S).

This justifies the displayed complementary projection and the full inverse of N=[gamma,I,E_S]. Unlike the preceding H0-only result, it is now legitimate to identify P with N inverse's middle block row; this identification is the conclusion of the new projection proof, not a premise.

With R=gamma H0+IP+H1delta-Id and H=E_S^tH1, applying R to the three column blocks of N gives

    Rgamma=H1delta gamma,
    RI=H1delta I,
    RE_S=H1delta E_S-E_S.

Since H1 is supported on S, this gives exactly the producer's lower-row normal form. Under the already structural pivot identities and C, it is

    N^-1 R N =
      [0,0,0; 0,0,0; T Ldelta gamma,T Ldelta I,TM-Id8].

The direct sparse-minor proof makes M invertible independently of A. Consequently TM=Id8 makes T invertible, and A is equivalent to

    Ldelta gamma=0,  Ldelta I=0,  TM=Id8.

Their shapes are 8x5, 8x2 and 8x8, giving 120 scalar positions per carrier. This is an exact equivalent presentation, not a minimality assertion and not a proof that the remaining entries vanish.

C is sufficient for inserting WL into delta as written. Alternatively literal B alone suffices for the displayed normal form by inserting WL into H1, as in the prior package. C is required for identifying the two Ldelta conditions with the full equations delta gamma=0 and delta I=0. Nothing here obtains either equation from the A-dependent contraction theorem.

## 5. Remaining boundary

The quotient annihilation family has genuinely been removed from the unresolved A system by a source-specific structural proof. A complete contraction, the complementary inverse, the inclusion cycle equation, and the common complex equation are not supplied by this package alone. The prior transition-determinant theorem still retains its remaining A premise.

The distinction from physical execution is unchanged: no physical matrix product, actual source polynomial expansion, source point, source jet, owner, detector, or obstruction value was computed. No GitHub write or publication action was taken in this review.
