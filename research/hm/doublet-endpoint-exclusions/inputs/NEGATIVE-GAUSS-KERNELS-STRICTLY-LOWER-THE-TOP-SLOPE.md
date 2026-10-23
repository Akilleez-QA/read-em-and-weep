# Negative Gauss kernels strictly lower the highest splitting degree

## Lemma

Let F be a saturated subbundle of a constant bundle H tensor O on P1 over C. Suppose every ordinary splitting degree of F is at most -d, where d>0. Let Fminus be the kernel of its second fundamental form for the constant connection. Then

    H0(Fminus(d))=0,

so every splitting degree of Fminus is at most -d-1. A zero kernel is allowed. No constant-rank plateau or equivariance hypothesis is needed.

**Proof.** If a nonzero section of Fminus(d) existed, regard it in H0(F(d)). Every summand of F(d) has nonpositive degree, so this section is a nonzero constant vector in the degree-zero summand. It gives a nowhere-vanishing direct bundle summand C=O(-d) of F. In particular F/C is locally free, and C is saturated in H O because both F/C and H O/F are locally free.

Since the second fundamental form of F kills C, the second fundamental form of C takes values in (F/C) tensor Omega1, not just in the whole ambient quotient. All degrees of (F/C) tensor Omega1 are at most -d-2. Thus

    Hom(O(-d),(F/C) tensor Omega1)=0.

C is therefore horizontal in the constant ambient bundle. Its Grassmannian classifying map has zero differential and is constant in characteristic zero. Saturation then makes C a constant line subbundle, of degree zero, contradicting d>0. This proves the lemma. No splitting of the connection has been assumed.

## Iteration and the actual new constraint

Every successive Gauss kernel is saturated in the same constant ambient bundle. Indeed the derivative kernel is saturated in its source, and its quotient and the earlier ambient quotient are locally free. Iterating the lemma gives

    max degree(F^(-r)) <= -d-r

for every existing backward transform, without assuming that later ranks equal any prescribed plateau rank.

In the actual proof-repair setup, E is saturated in the constant thirty-space and the independently proved GLOBAL input is H0(E(1))=0. Hence its degrees are at most -2. Consequently

    H0(E^-(2))=0,
    H0(E^{--}(3))=0,
    H0(E^{---}(4))=0,

and, generally, H0(E^(-r)(r+1))=0. These constraints apply even when the maximal forward length is one. They are stronger than using only the endpoint-length persistence bound in those branches.

This is a new application to the remaining Gauss profiles, not a claim that the second-fundamental-form argument is historically new. It neither excludes every remaining profile nor proves SF>=4. The remaining profile list and generic positive-square bound are unchanged until the new constraints are applied completely.

For example, write K=E^- and A0=E/K. The actual derivative K -> A0(-2) has kernel E^{--}. The new H0(E^{--}(3))=0 therefore gives the ONE-step representation bound

    H0(K(3)) injects into H0(A0(1)),
    chi_G(K(3)) <= H0(A0(1)).

No extra H0(A0(-1)) term is needed for this bound. The second inequality follows because H1(K(3)) is genuine. This statement is valid for the actual E with its global degree input, not for an unrelated bundle lacking that input.

## Equivariant multiplicity bottleneck

More generally suppose C=R tensor O(-d) is a nonzero direct summand of F at its highest degree, and the derivative of F kills C. The same proof, now for a higher-rank constant-coefficient summand, makes C horizontal and contradicts its negative degree. Thus no nonzero constant multiplicity subspace of the top splitting block can be annihilated identically.

If a derivative of F is known to land in a bundle T, the induced map

    H0(F(d)) -> H0(T(d))

must be injective. With a finite group action this is an injective map of representations, so each source multiplicity is bounded by the corresponding target multiplicity. It is NOT fiberwise injectivity of F -> T: a polynomial map may be injective on global sections while having a lower generic fiber rank.

A useful special case is F=C O(-d)+N with every degree of N at most -d and beta_F(C O(-d))=0. Its internal second fundamental form takes values in N(-2), so that top summand is already horizontal. No long descent through all lower summands is required. The saturated-image convention remains essential.

## Sources and reproduction

The actual inclusion, global H0(E(1)) input and ordinary splitting are in ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md and POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md. The recursive saturated-kernel principle is Section1 of EXTREMAL-31-FIRST-REMAINING-QUOTIENT-EXCLUSION.md. This proof strengthens the available backward degree input without changing those files.

Run python3 verify_negative_gauss_strict_top_slope.py. It checks the universal degree inequalities, iteration and the resulting actual three vanishings, and the twist of the one-step target. The saturated-line and characteristic-zero argument above is the mathematical proof; the elementary arithmetic is not a substitute for it. No actual coefficient, point, instance matrix, rank experiment or scan is used.
