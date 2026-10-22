# The cubic evaluation image is a smooth projected Veronese surface of degree nine

## Theorem

Let R=P(V) be the actual positive HM plane and let

    L=q0 V* directsum H0(I_Z6(3))
      subset H0(R,O_R(3))

be the seven-dimensional span of the invariant-hyperplane determinant cubics. The actual evaluation morphism

    Phi:R -> P(L*)=P6

is a closed embedding. Its image is therefore a smooth nondegenerate surface isomorphic to P2, of degree nine. It is the projection of the cubic Veronese surface in P9 away from the omitted irreducible three-dimensional coefficient space.

The image is not linearly normal: its missing linear sections form precisely the other irreducible A5 three-space A. No statement about individual members of the determinant-cubic family being smooth follows from this surface theorem.

## 1. The immediate finite-birational consequence

The determinant-family theorem proves that L is base-point-free and has dimension seven. Hence Phi is everywhere defined, its image T spans P6, and

    Phi*O_T(1)=O_R(3).

Every fiber is zero-dimensional. A positive-dimensional projective fiber would contain a curve, on which this pullback has degree zero, contradicting ampleness of O_R(3). Properness therefore makes Phi finite onto T.

Let e be its degree. The intersection formula gives

    e deg(T)=c1(O_R(3))^2=9.

A nondegenerate integral surface in P6 has degree at least codimension plus one, namely five. Thus e=1 and deg(T)=9. Already at this point R is the normalization of T. This argument does not yet show that T is smooth; that stronger assertion uses the actual Steiner tensor below.

## 2. The projection center is the other three-space

Use the convention that P(V) parametrizes lines. The full cubic Veronese map is

    v3:R -> P(Sym^3 V),  [v] |-> [v^3].

The actual cubic coefficient decomposition is

    Sym^3 V*=V* directsum A directsum 4,
    L=V* directsum 4.

All these A5 representations are self-dual. The kernel

    C=ker(Sym^3 V -> L*)

is therefore the irreducible three-space A, different from V. The morphism Phi is linear projection from the projective plane P(C), provided this center is disjoint from the Veronese. Base-point-freeness already gives that disjointness. We prove the stronger disjointness from the secant variety.

## 3. The actual Steiner injection excludes binary cubics from the center

The actual Steiner presentation of E=F_R(2) is

    0 -> A O_R(-1) --M--> D O_R -> E -> 0,
    D=5.

Its coefficient tensor is

    t:A tensor V -> D.

Because this is a subbundle injection, t(a,v) is nonzero whenever a and v are nonzero: at every point [v] the fiber map A->D is injective.

Now contract a symmetric cubic in the center by a constant covector:

    partial:C tensor V* -> Sym^2 V.

This equivariant map is nonzero, since in characteristic zero a nonzero homogeneous cubic cannot have all first derivatives zero. The representation decompositions are

    C tensor V*=4 directsum 5,
    Sym^2 V=1 directsum 5.

Thus contraction lands in the five-dimensional constituent and is the unique nonzero map between these coefficient spaces, up to scalar. Using the invariant self-duality of V, an equivariant identification C=A, and the unique five-dimensional target, it is a nonzero scalar multiple of the ACTUAL tensor t.

Consequently

    partial_xi(f) != 0
    for every nonzero f in C and nonzero xi in V*.     (1)

This is a transfer of the actual fiber-injectivity theorem through a multiplicity-one representation interface. It is not an evaluation of a selected presentation or a rank test.

In particular no nonzero cubic in C belongs to Sym^3 U for a two-dimensional subspace U of V. Every such cubic is annihilated by every covector vanishing on U, contradicting (1).

## 4. The center avoids all secant and tangent lines

The locus of cubics belonging to Sym^3 U for some two-space U is closed: it is the image of the projective bundle P(Sym^3 U_univ) over Gr(2,V). Every secant line to v3(R) lies in this locus, since the line joining v^3 and w^3 lies in Sym^3(span(v,w)). This closed locus therefore contains the entire secant variety, including tangent-line limits.

Section 3 proves that P(C) is disjoint from this closed binary-cubic locus. In particular it is disjoint from the secant variety of the cubic Veronese.

Explicitly, let xi be any length-two subscheme of R, reduced or nonreduced. It is contained in a line P(U), with dim U=2, and its cubic-Veronese span lies in P(Sym^3 U). A nonzero covector annihilating U annihilates every tensor in that span. Section 3 therefore shows that the projection center misses the span. Dually, restriction L->H0(xi,O_xi(3)) is onto. Thus L separates every length-two subscheme, and the very-ampleness criterion makes Phi a closed embedding. This argument includes tangent directions and does not rely only on pointwise injectivity.

This completes the upgrade from finite birational normalization to a smooth embedded P2. The hyperplane pullback remains O_R(3), so its degree is nine as in Section 1.

## 5. The exact linear-normality defect

Since Phi is an embedding,

    H0(T,O_T(1))=H0(R,O_R(3))=Sym^3 V*,

of dimension ten, whereas ambient linear forms restrict to the seven-space L. The image T is nondegenerate, so H0(I_T(1))=0. The restriction sequence yields

    H1(I_T(1))=Sym^3 V*/L=A,

of dimension three. This identifies the failure of linear normality with the actual omitted representation, without asserting further equations or a full resolution of T.

## Dependencies and boundary

DETERMINANT-CUBIC-FAMILY-RATIONAL-SEXTIC.md supplies the actual seven-dimensional base-point-free linear system and its coefficient decomposition. INVARIANT-CONIC-SECOND-NORMAL-COLLAPSE.md supplies the actual distinction between the two three-spaces. The stable Steiner presentation and its fiber injectivity are the only additional geometric inputs.

No selected HM/source coefficients, evaluated actual matrices or ranks, scans, or experiments are used. The surface theorem does not establish mixed-root section compatibility, smoothness of individual plane cubics, or an outstanding adjoint-vanishing gate.
