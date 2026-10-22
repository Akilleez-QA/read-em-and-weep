# Complete exclusion of the (6,2) rank-two dual-image quotient

## Result and source boundary

The hypothetical maximal rank-three plateau (k,l)=(3,1), with rank-two dual cubic image, cannot have first quotient

    A0=E/K=O(4)+W'(-1).

This is the entire (n,e)=(6,2) case. Combined with the three earlier exclusions, only (8,2) remains in that rank-two branch. The rank-one dual-image branch is not settled. The lower bounds SF>=3 and positive-square rank>=27 are unchanged.

The complete eight-type reduction is EXTREMAL-31-FIRST-REMAINING-QUOTIENT-REDUCTION.md. The universal irreducible sextic kernel lemmas are proved in EXTREMAL-31-LAST-LOW-QUOTIENT-EXCLUSION.md. We use their actual-map conclusions, not a realization assumption about abstract bundle splittings. Write S=S4, T=T6, P=P4, D=D5. All displayed summands are equivariant bundles; all Hom spaces below are equivariant.

The actual ambient input has been checked in POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md: its exact sequence embeds E as a subbundle of the constant thirty-space H tensor O. The Gauss derivative there is the actual second fundamental form of that inclusion. ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md explicitly retains this constant ambient realization for the saturated Gauss flags. No abstract multiplication-pencil kernel is substituted for this ambient subbundle.

## 1. A recursive actual-kernel principle

For a saturated subbundle G of H tensor O, put F=ker(beta_G). The derivative target is locally free, so G/F, being its image sheaf, is torsion-free and hence locally free on P1. Consequently F is saturated in G and in H tensor O. Differentiation of F lies in G, so its actual next derivative factors as

    beta_F: F -> (G/F) tensor O(-2).

Its kernel is again an actual saturated ambient subbundle. This remains true after leaving the rank-three plateau; no constant-rank-three condition is imposed on subsequent derivatives.

If beta_F=0, the Grassmann classifying map of F has zero differential, hence is constant in characteristic zero. Its tautological subbundle F is then trivial, of degree zero. Thus EVERY nonzero negative-degree bundle encountered below must have nonzero actual derivative. This is the only nonvanishing principle used after the plateau ends.

An important image convention: if the only potentially active source block is a line L and its derivative is nonzero, the map L into the target is injective as a sheaf. Therefore the actual quotient by the derivative kernel is isomorphic to L, even if the map has zeros and its image is not saturated in that target. The next target is L(-2), not the saturation of that image. The ambient saturation of the kernel, proved above, is unaffected.

## 2. The three explicit Q shapes

The reduction supplies the following possibilities for Q=E^{--}:

    Q1=(D+V)(-4)+W'(-5)+O(-10),
    Q2=S(-3)+V(-4)+W'(-5)+O(-8)+O(-10),
    Q3=S(-3)+V(-4)+W'(-5)+W(-9).

In each case K/Q=O(2)+W'(-3), so beta_Q has target O+W'(-5) and generic rank three. Exact Hom calculations show that the only block mapping to the low target is W'(-5), by its scalar endomorphism. The only block mapping to O is D(-4) in Q1 and S(-3) in Q2/Q3; their Hom spaces have dimension one. Rank three forces these maps nonzero. They are complete quartic/cubic evaluation, hence surjective, and the low map is an isomorphism. Thus the ACTUAL next kernel F0 and quotient are

    Q1: F0=S(-5)+V(-4)+O(-10),
    Q2/Q3: F0=(A+V)(-4)+L,
       L=O(-8)+O(-10) or W(-9),
    Q/F0=O+W'(-5).

The next derivative target is O(-2)+W'(-7). It has no low component in all three cases. The complete Hom supports and ensuing kernels are as follows. Each arrow is the actual nonzero derivative onto its indicated scalar target. All other blocks have zero Hom to that target.

First case:

    S(-5)+V(-4)+O(-10) -> O(-2),
    A(-6)+V(-4)+O(-10) -> O(-4),
    W(-7)+V(-4)+O(-10) -> O(-6),
    O(-8)+V(-4)+O(-10) -> O(-8),
    V(-4)+O(-10) -> O(-10),
    V(-4) -> O(-12).

The first five maps must be nonzero by Section 1; the first three are complete evaluations, and the next two are scalar isomorphisms on the active line. Their kernels are exactly the subsequent displayed sources. The last Hom space is zero, a contradiction.

For the second/third cases the initial chain is

    (A+V)(-4)+L -> O(-2),
    W(-5)+V(-4)+L -> O(-4),
    O(-6)+V(-4)+L -> O(-6),
    V(-4)+L -> O(-8).

Again the first three are forced complete evaluations (including the degree-zero line evaluation). If L=O(-8)+O(-10), only O(-8) maps at the fourth step. If L=W(-9), the fourth step is complete linear evaluation with kernel O(-10). Both yield

    V(-4)+O(-10) -> O(-10),
    V(-4) -> O(-12),

the same contradiction. All stages have positive rank and strictly negative degree.

## 3. Complete solution of the residual high-map problem

The remaining reduction is the actual high map

    f:J=(2V+P)(-4)+W'(-5) -> O(2),

with at least one sextic component on 2V+P nonzero. Every nonzero irreducible sextic or septic series is basepoint-free: its common-zero divisor would be invariant of degree at most seven, whereas a nonempty icosahedral invariant divisor has degree at least twelve. Thus f is surjective. The original delta is also surjective and K/Q=O(2)+W'(-3).

A multiplicity-space automorphism of 2V makes at most one V component active. The established universal sextic lemmas, twisted down by two, give

    ker(V(-4)->O(2))=W'(-7),
    ker(P(-4)->O(2))=V(-6).

There are exactly four possible Q=ker f:

    R1: V(-4)+(T+W')(-5),
    R2: 2V(-4)+V(-6)+W'(-5),
    R3: (V+P)(-4)+P(-6),
    R4: (V+P)(-4)+W'(-5)+W'(-7).

Here are all lifting and extension details.

If V and P components are both nonzero, they comprise the complete sextic series Sym^6 W=V+P after independent scalar changes. Its kernel is T(-5). The W'(-5) component lifts through that evaluation: the obstruction is in T tensor W' tensor H1(O(0))=0. Subtracting the lift gives R1.

If only P is nonzero, its kernel is V(-6). The W'(-5) high component lifts because its obstruction has line factor H1(O(-1))=0. Thus R2 holds.

If only V is nonzero, let J' be the kernel on V(-4)+W'(-5). It sits in

    0 -> W'(-7) -> J' -> W'(-5) -> 0.

If the W' high component is zero this splits and gives R4. If it is nonzero, the extension cannot split: a splitting would lift that high map to V(-4), but Hom(W'(-5),V(-4))=0. Its invariant extension space is

    (End(W') tensor H1(O(-2)))^G = C.

All nonzero classes have the same equivariant middle bundle, namely W' tensor W(-6)=P(-6), by the tensor Euler sequence. This gives R3. Every lift above may be averaged over the finite group. Such lifts and source automorphisms compute actual kernels; none is assumed horizontal for the ambient connection.

## 4. Excluding the four residual kernels

The next derivative has target O+W'(-5) and generic rank three.

For R1 the only high contributor is T(-5), and the only low contributor is W'(-5). They are forced complete quintic evaluation and scalar isomorphism. Consequently

    F0=D(-6)+V(-4),       Q/F0=O+W'(-5).

Its next derivative has no component to W'(-7), and the forced scalar chain is

    D(-6)+V(-4) -> O(-2),
    S(-7)+V(-4) -> O(-4),
    A(-8)+V(-4) -> O(-6),
    W(-9)+V(-4) -> O(-8),
    O(-10)+V(-4) -> O(-10),
    V(-4) -> O(-12).

Every nonterminal map is complete evaluation, while the terminal Hom is zero. Section 1 excludes both that terminal map and any earlier zero map.

For R2 the only high contributor is V(-6), and only W'(-5) reaches the low target. Rank three forces both. The sextic lemma gives

    F0=2V(-4)+W'(-9),     Q/F0=O+W'(-5).

In the next map to O(-2)+W'(-7), only W'(-9) has any Hom, and only to O(-2). This is the unique nonzero septic pair, forced nonzero and basepoint-free. Its kernel is O(-16), so the ensuing source is 2V(-4)+O(-16), with target O(-4). Only O(-16) can map to O(-4). If zero, the actual ambient derivative is zero, impossible. If nonzero, the ACTUAL quotient is O(-16), including at zeros of that degree-twelve scalar map. Its kernel 2V(-4) has next target O(-18) and no Hom to it, again impossible.

For R3 only P(-6) can map to either target block. Its nonzero low map is tensor Euler

    0 -> W'(-7) -> P(-6) -> W'(-5) -> 0.

Rank three forces the high restriction on W'(-7) nonzero; otherwise the total map has rank at most two. That restriction is a basepoint-free septic pair with kernel O(-14). Thus the full map is surjective and

    F0=(V+P)(-4)+O(-14),  Q/F0=O+W'(-5).

For R4 the low map is the scalar isomorphism on W'(-5), and the high map is the septic pair on W'(-7); all other Hom spaces vanish. Rank three forces both, giving the same F0 and quotient.

For this common F0 its next map to O(-2)+W'(-7) is supported ONLY on O(-14). Both target components may occur; no ratio or saturation is assumed. If the map is zero, Section 1 contradicts negative degree. Otherwise the line maps injectively as a sheaf, so the ACTUAL quotient is O(-14) and its kernel is (V+P)(-4). The next derivative then has target O(-16), inaccessible by degree. This is the final contradiction.

## Verification and limits

Run python3 verify_extremal_31_first_remaining_quotient_exclusion.py. It reuses the frozen reduction's exact representation ring, checks every displayed Hom support, evaluation character, extension dimension, and lifting inequality, and checks the ranks and negative degrees of the kernel chains. The geometric saturation and constant-Grassmann argument, basepoint-free divisor argument, and actual-image sheaf arguments are supplied here rather than inferred from arithmetic.

No actual coefficients, points, matrices, rank experiments, or scans occur. Only new proof/verifier files were written. No conclusion about the remaining (8,2) quotient or the rank-one branch is claimed; global bounds remain unchanged.
