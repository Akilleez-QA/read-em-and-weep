# The (n,e)=(6,4) first quotient is impossible

## Result and scope

In the hypothetical rank-three Gauss plateau (k,l)=(3,1), with rank-two dual cubic image, the first quotient

    A0 = E/K = O(4) + W' O(-3)

is impossible. This excludes the entire (n,e)=(6,4) case, including all ten primal types retained by the section envelopes. Together with the separate smallest-quotient exclusion, this leaves the three quotient shapes (6,2), (8,2), (8,4) in the rank-two dual-image branch. No conclusion about existence in those cases or about the rank-one dual-image branch is asserted. The established bounds SF >= 3 and positive-square rank >= 27 remain unchanged.

Inputs are EXTREMAL-31-FIVE-QUOTIENT-SECTION-ENVELOPES.md and the actual Gauss-kernel/persistence statements used in EXTREMAL-31-SMALL-QUOTIENT-EXCLUSION.md. The argument uses no actual coefficients, points, matrices, rank experiments, or parameter scans. No frozen file is modified.

## 1. Universal splitting overlist

Write K2=E^{--}, F0=E^{---}. Their ranks are 11 and 8; K has rank 14 and degree -52. Global H0(E(1))=0 implies every splitting degree of K is at most -2. The section envelopes give

    H0(K(2)) = d D5,                 d in {0,1},
    T6 <= X := H0(K(3)) <= T6+S4,
    chi_G(K(3)) = T6-W'.

Thus X=T6 or T6+S4, and H1(K(3))=W' or W'+S4, respectively. The degree -2 coefficient is d D5. The degree -3 coefficient is X-d(D5 tensor W), necessarily genuine; D5 tensor W=T6+S4. In particular d=1 forces X=T6+S4 and leaves no degree -3 coefficient.

Let R be the genuine, otherwise unrestricted degree -4 coefficient. Every degree -j block C O(-j) with j>=5 contributes C tensor Sym^{j-5} W to H1(K(3)). Positivity, not cancellation, governs these contributions. The rank and degree give j<=26: the other thirteen line degrees are at most -2.

For 5<=j<=26 and the required central parity, the only irreducible blocks whose contributions are bounded by W'+S4 are

    W' O(-5),     S4 O(-5),     O(-8),

with respective contributions W', S4, S4. Consequently the tail is exactly W' O(-5), together with no optional block when X=T6, or exactly one of S4 O(-5), O(-8) when X=T6+S4. These are necessary splitting overlists; impossible rank/degree or coefficient choices may safely remain in an overlist. The companion exhausts the finite abstract character assertion, not maps or parameter values.

## 2. Isolate the actual low-target isomorphism

The actual derivative has generic rank three:

    delta: K -> A0(-2) = O(2) + W' O(-5),
    ker(delta)=K2.

All degree -2, -3, -4 blocks have zero map to W' O(-5) by degree. The optional S4 O(-5) has zero map by irreducibility. The optional O(-8) also has zero map because

    Hom_G(O(-8), W' O(-5)) = Hom_G(W', Sym^3 W) = 0.

Therefore the sole possible contributor to the rank-two low target is the unique W' O(-5) block. Generic rank three forces its scalar endomorphism to be nonzero, hence an isomorphism of bundles.

This block can have a nonzero component to O(2). Remove that graph component by the target automorphism (a,b) -> (a-h(b),b), where h is that component composed with the inverse low-target isomorphism. This is an actual equivariant bundle automorphism, and it leaves all other blocks' O(2) components unchanged, because their low components are zero. The kernel is therefore exactly the kernel of the remaining map to O(2).

The optional tails have zero component to this line as well:

    Hom_G(S4 O(-5), O(2)) = Hom_G(S4, Sym^7 W) = 0,
    Hom_G(O(-8), O(2)) = (Sym^{10} W)^G = 0,

using Sym^7 W=W'+T6 and the absence of the trivial representation in Sym^{10} W.

## 3. Evaluation, and the missing lifting justification

### Case d=1

The D5 O(-2) component to O(2) is nonzero, because otherwise its twist-two section representation D5 would lie in H0(K2(2)), which persistence makes zero. Its Hom space is one-dimensional, since D5=Sym^4 W. It is the nonzero scalar multiple of the complete quartic evaluation, hence everywhere surjective, with kernel

    0 -> S4 O(-3) -> D5 O(-2) -> O(2) -> 0.

The degree -3 coefficient is zero, so all other non-tail source blocks are R O(-4). Every map R O(-4) -> O(2) lifts to D5 O(-2): its obstruction lies in

    Ext^1(R O(-4), S4 O(-3))
       = R^* tensor S4 tensor H1(O(1)) = 0.

A lift can be made equivariant by averaging over the finite group. Subtracting it by a triangular source automorphism eliminates the corresponding component of delta. Thus

    K2 is isomorphic to S4 O(-3) + R O(-4) + optional tail.

### Case d=0

Now the degree -3 coefficient is T6 or T6+S4. The T6 O(-3) component to O(2) is nonzero. Indeed the next derivative and H0(F0(3))=0 inject H0(K2(3)) into H0((K/K2)(1)), which embeds in

    H0(A0(-1)) = S4.

A zero T6 component would put T6 inside H0(K2(3)), which is impossible. Since T6=Sym^5 W, its one-dimensional Hom space gives complete quintic evaluation:

    0 -> D5 O(-4) -> T6 O(-3) -> O(2) -> 0.

Every map from R O(-4) to O(2) lifts, since its obstruction is R^* tensor D5 tensor H1(O)=0. The possible additional S4 O(-3) component actually vanishes because Hom_G(S4,Sym^5 W)=0. Even without this character vanishing, the lifting obstruction would vanish by H1(O(-1))=0. Equivariant averaging and a triangular source automorphism again compute the actual kernel:

    K2 is isomorphic to D5 O(-4) + R O(-4)
                       + (X-T6) O(-3) + optional tail.

In both cases the optional tail is absent, S4 O(-5), or O(-8), as prescribed in section 1. Both evaluation maps and the low-target isomorphism are everywhere surjective, so delta is surjective as a sheaf. Therefore

    K/K2 is isomorphic to O(2) + W' O(-5).

None of these isomorphisms is asserted horizontal. They are legitimate kernel computations for actual bundle maps. The subsequent Hom vanishing applies to every equivariant bundle map, so it survives all source and target coordinate changes.

## 4. Contradiction at the next Gauss stage

The next derivative would have generic rank three:

    K2 -> (K/K2)(-2),
    (K/K2)(-2) is isomorphic to O + W' O(-7).

Every possible degree -3, -4, or -5 block in the displayed actual kernels has zero map to W' O(-7) by degree. The only possible deeper block is O(-8), and

    Hom_G(O(-8),W' O(-7)) = (W' tensor W)^G = (P4)^G = 0.

Thus the derivative factors through a line and has generic rank at most one, contradicting the plateau rank three. This excludes (n,e)=(6,4) universally.

## Reproduction

    python3 verify_extremal_31_middle_quotient_exclusion.py

The verifier imports and executes the existing section-envelope certificate; checks the Euler characteristic, section envelope, complete tail enumeration, evaluation characters, all special Hom vanishings, and the line-cohomology inequalities guaranteeing lifts. The sheaf, averaging, and actual-kernel arguments are supplied above rather than inferred from arithmetic alone.
