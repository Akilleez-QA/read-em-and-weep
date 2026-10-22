# Independent review of the third-neighborhood exclusion

Reviewed 2026-10-22. Verdict: PASS under the expressly stated actual-frame and regular-pair hypotheses. The filtered exclusion and scalar-quotient corollary correctly apply the immutable scalar-slope theorem PR729. No additional algebraic gap was found.

## Reviewed versions

SHA-256:

- PROOF.md: `da9b790aafeb51d73d9a263a2f861a147529371698a4dc70dbf996bbb95428ec`
- SCALAR-QUOTIENT-COROLLARY.md: `efdf3aaa589919bd72694fcdd8096a7832f7067b4506d1e6117f97e20d10a344`
- Scalar-slope dependency, PR729 PROOF.md: `3fe0bf356b69647c590b4e779ed7eec1a4194a0a0c40c452233da3e2f72c6a26`
- Actual-frame dependency, PR692 PROOF.md: `aafb8a9c44d538ba99ff67ad184a439b239bed478234818642bcbfd62a1a02a4`

Immutable dependencies, with the content hashes recorded above:

- [PR692 actual frame](https://github.com/Akilleez-QA/read-em-and-weep/blob/858f96ba1539afb1293f31239b8761af08e46f60/research/hm/vertex-scalar-filtration/PROOF.md).
- [PR729 scalar slope](https://github.com/Akilleez-QA/read-em-and-weep/blob/c384ae419983a5031af19c37674df020de1aa5da/research/hm/firstnormal-scalar-slope/PROOF.md).

## Assumptions that must remain explicit

1. Work in characteristic zero over the generic vertex field, with the actual regular completed harmonic frame, not a meromorphic diagonalization or a homogeneous replacement of the actual bundle.
2. In that frame a regular trace-free matrix of weight d has entry degrees d,d−2,d+2, and the relevant weights are even. The actual coefficients have orders at least eight and four, with respective leading terms n8 and T4.
3. The ambient formal coefficient algebra has the indicated q-adic harmonic decomposition; q is a nonzerodivisor before truncation. Thus the kernel of restriction from q³ to q² is q² times the coefficient module modulo q. This is the actual regular endomorphism module in the fixed frame.
4. The fixed class Ns is square-zero modulo q². The leading scalar d2 of its second square is nonzero modulo f for every regular pair, as supplied by PR729. In particular, the theorem must hold for repeated-factor cubics as well as square-free ones.

These are dependency assumptions, not conclusions obtained from weighted degree counting alone.

## Independent filtered check

For trace-free two-by-two matrices over a commutative scalar algebra, the anticommutator is tr(nK) times the identity. Consequently the correction q²H(K) changes the q² square scalar by ordinary tr(n_full K). Harmonic corrections to that product have an additional q factor and vanish modulo q³. The term quadratic in K starts at q⁴ and also vanishes.

The other contributions have orders at least eight:

- T_full²: 4+4;
- B1(n_full,T_full) and its reversal: 8+4−4;
- B2(n_full,n_full): 8+8−8.

Their weight-eight sum uses only n8 and T4 and is precisely d2. No higher filtered actual coefficient enters it.

Regularity does not initially permit assuming K has order zero. Its possible weight−2 term is [[0,0],[c,0]], with c in k. At scalar weight six, no other square contribution is present, and the equation is −u f² c=0. Since u and f are nonzero in the domain S, c=0. Parity then leaves order at least zero.

At weight eight, a potential product of a weight-ten term of n_full with K_(−2) has therefore already disappeared. The only remaining correction is tr(n8 K0). With K0=[[x,0],[z,−x]], x in k and z in S2, it equals u(2fgx−f²z), which belongs to fS5. Thus reduction modulo f forces [d2]=0 and contradicts the stated dependency. This successive elimination, rather than discarding higher terms, is what makes the argument valid for the completed actual frame.

## Bundle and scope checks

A trace-free matrix lift exists locally by lifting three entries and taking the negative of the lifted diagonal for the fourth. This is a local statement on the fixed formal frame, not an assertion that an arbitrary global trace-free section lifts. Conversely any actual bundle extension restricting to this fixed Ns would restrict to one of the regular local matrix lifts excluded here. Therefore the local contradiction rules out such a global extension if that global section and its restriction are the specified ones.

The conclusion concerns this fixed first-normal class. It does not classify all sections of the relevant bundle on 2Q or 3Q, does not assert that every section on 2Q is nonextendible, and does not automatically cover changing Ns or allowing nonregular frame changes. The proof states and establishes the trace-free extension problem; it need not assert a separate result for unrestricted endomorphisms.

There is no contradiction with the multiplied J3. For its leading term P=a²h n8, multiplication by the nonzero quartic increases the leading weight from eight to twelve, and the second correction has weight four rather than weight zero after elimination. Its trace equation has target S12 and the established regular-pair trace map is surjective. The source factor is not being inverted as a regular unit. Nonextendibility of the unmultiplied section cannot be deduced for, or transferred to, the multiplied section by cancellation of h.

## Dependency and conclusion boundary

PR729 supplies nonzero [d2] for every regular pair, lift independence, the affine slope identity, and existence and h-divisibility of the multiplied local solutions. Its cubic-versus-quadratic argument does not require f to be square-free. These are precisely the statements used here. No actual fourth-square value, fourth-Bockstein value, or higher lifting conclusion follows.

## Separate review of SCALAR-QUOTIENT-COROLLARY.md

Verdict: PASS under the stated hypotheses, using PR729 and its existence, h-divisibility and R-independence statements.

For the nonzero cubic f, multiplication S5 → S8 by f is injective. Hence dim (S/(f))8 = 9−6 = 3. The nonzero vector δ spans a one-dimensional subspace, giving a two-dimensional quotient B/kδ.

The slope identity K_(s+λ)=K_s+aλδ, with a nonzero in k, implies that the quotient image is independent of s. R-independence is inherited from the cited dependency. If the quotient image vanishes, K_(s0)=cδ for a unique c in k, and s=s0−c/a gives K_s=0. Conversely K_s=0 plainly gives zero quotient image. If two scalars cancel, their difference times aδ is zero, so they coincide.

The unique object asserted is an abstract scalar, not a unique R, not a canonical global completion, and not the actual geometrically prescribed scalar. Existence of an abstract cancelling scalar occurs exactly when the two-dimensional quotient obstruction vanishes. The corollary supplies neither that vanishing nor the equality of a cancelling abstract scalar with the fixed actual scalar.

All checks above are structural algebra and degree counting. No actual coefficients, selected pair or model, points, derivative values, or actual ranks were evaluated; no large computation was run.
