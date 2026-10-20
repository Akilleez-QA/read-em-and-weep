# Good-fiber deck decomposition and the rank-12 gluing summand

## Result

Over the good base B° for the projection r:C⁴→C² onto factors 3,4, let G=End₀(F). The rank-120 bundle R¹r_*G decomposes under deck involutions of fiber factors 1,2 with ranks

    character (00,10,01,11):  (27,33,33,27).

On the fiber-full-sign rank-27 summand, the inner swap (12) has eigensubbundle ranks

    swap-even: 15,     swap-odd: 12.

Consequently a global full-deck-sign class which is also odd under (12) restricts, via the Leray identification, to H¹(B°,V₁₂), where V₁₂ is this rank-12 vector bundle. If the stipulated D8 character ε is the restriction of permutation sign, its classes have precisely this necessary inner-swap parity. The remaining base deck and base-swap characters impose further eigenspace conditions. Pair exchange exchanges the two fibrations and is a separate compatibility condition.

This does not reduce the dimension of the global thirty-dimensional obstruction space to twelve: vector-bundle rank is not a cohomology dimension. Nor does it remove possible contributions associated with exceptional fibers. No actual obstruction value or model matrix is evaluated.

## 1. Plane endomorphism cohomology

Let E=HM|Λ be any stable normalized plane restriction. Then rk(E)=2, c1(E)=-H, c2(E)=4H². Write A=End(E). Its Chern character is

    ch(A)=4−15H².

Riemann–Roch on P² gives

    χ(A(t))=2t²+6t−11.

Since E is stable, H⁰(A)=C and H⁰(A(t))=0 for all negative t. The trace pairing gives A*=A. Serre duality therefore gives

    H²(A(t)) ≅ H⁰(A(-t-3))*.

The dimensions for t=0,-1,-2,-3 are respectively

    h¹(A)=12,   h¹(A(-1))=15,   h¹(A(-2))=15,   h¹(A(-3))=12.

Among these four twists, the only nonzero H⁰ is h⁰(A)=1, and the only nonzero H² is h²(A(-3))=1.

The Euler sequence supplies an injection A⊗Ω¹→A(-1)^3, hence H⁰(A⊗Ω¹)=0. In dimension two, T_P²(-3)≅Ω¹_P², so Serre duality and A*=A give H²(A⊗Ω¹)=H⁰(A⊗Ω¹)*=0. Finally

    χ(A⊗Ω¹)=3χ(A(-1))−χ(A)=-34,

and therefore h¹(A⊗Ω¹)=34.

These statements hold for *every stable plane restriction*, including special stable resolution strata. They do not require a generic-resolution hypothesis.

## 2. Fiber deck characters

Use the proven pushforward decomposition from RESULT.md, but retain the two fiber deck characters:

    00: σ_*O = O⊕O(-1),
    10: σ_*O(-2,0)=Ω¹,
    01: σ_*O(0,-2)=Ω¹,
    11: σ_*O(-2,-2)=O(-2)⊕O(-3).

Projection formula gives H¹(C²,End(F_b)) character dimensions

    00:12+15=27,
    10:34,
    01:34,
    11:15+12=27.

The scalar H¹(O_(C²)) has one dimension in character 10 and one in 01, and none in 00 or 11. Trace splitting therefore gives End₀ ranks (27,33,33,27), totaling 120.

The finite-group idempotents define coherent direct summands of R¹r_*G. Their fiber dimensions are constant on B°, and R¹r_*G is locally free and base-change compatible there, so these are locally free eigensubbundles of the stated ranks.

## 3. Why the swap signs really are (+,-)

The deck-full-sign line on P¹×P¹ is O(-2,-2), with its product linearization: a local generator y₁y₂ is invariant under exchanging factors. This line is σ*O_P²(-2), with the ordinary descended linearization, not a sign-twisted one. The two equal-degree line factors are degree-zero sheaves; their exchange introduces no Koszul sign.

The finite double quotient σ:P¹×P¹→P² has

    σ_*O = O_P² ⊕ O_P²(-1),

with the first summand invariant and the second anti-invariant for the sheet-exchange involution (12). Equivariant projection formula consequently yields

    σ_*O(-2,-2)
        = O(-2)_(swap +) ⊕ O(-3)_(swap −).

The plane map i_h and the bundle E_h factor through the symmetric quotient. Thus the induced swap action on the pulled-back End(E_h) is trivial on its base factor; the line N cancels canonically in End(F). Taking cohomology preserves the indicated (+,-) eigenspaces. Hence the fiber-full-sign H¹(End₀F_b) splits as

    H¹(P²,A(-2))_(+) ⊕ H¹(P²,A(-3))_(-),

of dimensions 15 and 12.

There is no extra cohomological sign to insert here. The action has been computed from an equivariant finite pushforward, so its induced action on cohomology already is the actual geometric action. As a consistency check, equivariant Serre duality on the abelian surface does carry swap sign in the canonical two-form; it exchanges the complementary ± counts rather than changing this decomposition.

## 4. The remaining gluing target

Let V₁₂⊂R¹r_*G be the simultaneous summand with fiber deck character 11 and swap (12) eigenvalue -1. It is a rank-12 locally free sheaf on B°. Since r_*G=R²r_*G=0 there, Leray gives naturally

    H²(r^(-1)B°,G) ≅ H¹(B°,R¹r_*G).

This isomorphism is equivariant for all group elements preserving the fibration. Fiber deck involutions and (12) act trivially on B°, so their projectors commute with the right-hand cohomology. Therefore the simultaneous full fiber deck/inner-swap-odd subspace is exactly

    H¹(B°,V₁₂).

For a class originally full-sign under all four deck involutions, retain the odd character under base deck involutions 3 and 4 on this H¹ group as well. For ε=permutation sign restricted to D8, retain the appropriate base-swap parity. The exchange (13)(24), however, exchanges r with the other factor projection; it cannot be imposed as an additional pointwise endomorphism of this single rank-12 bundle without an explicit comparison between the two fibrations.

On an affine open U⊂B°, H¹(U,V₁₂)=0, confirming the earlier restriction vanishing. Over the full good base B°, this H¹ need not vanish. Restriction of the global thirty-dimensional sector to the good locus need not be injective, and even its image dimension is not bounded by the sheaf rank twelve. These distinctions prevent a false claim that any global obstruction coordinate has been eliminated.

All statements retain the physical-bundle identification and equivariance premises from RESULT.md and the supplied deck-character report. Only static geometry, Riemann–Roch, stability, and equivariant pushforward are used.
