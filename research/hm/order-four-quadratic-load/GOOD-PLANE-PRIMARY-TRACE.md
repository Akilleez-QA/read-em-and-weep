# A five-dimensional primary trace criterion on a good plane

## Source and notation

Use A_d=H^1(F(d)) exclusively for the primary module of the normalized HM bundle. This is not the Rao module H^1(I_C(d)). The dimensions are dim A_0=5 and dim A_1=dim A_2=10.

Ada Boralevi, The Horrocks–Mumford bundle restricted to planes, arXiv:math/0602002v2, Main Theorem (PDF page 3) identifies a nonempty open plane stratum with resolution

    0 -> 3O_P(-3) -> 5O_P(-2) -> F|P -> 0.               (1)

The notation for resolutions is specified in (1.2); Corollary 2.2 lists the possibilities. Primary source:
https://arxiv.org/pdf/math/0602002

Call a plane with (1) good. Twisting (1) shows that F_P(1) is acyclic and that h^0(F_P(2))=5, H^1(F_P(2))=0.

We also use the verified Banica–Manolache section theorem and stability of HM hyperplane restrictions, as pinned separately in the current proof packet. Thus h^0(F_H(2))>=1 for every hyperplane. No exact generic corank is assumed.

## 1. Good pencils give a direct-sum decomposition of A_1

Let P=H1 intersect H2 be good, with independent equations ell1,ell2. The normalized HM monad is

    5O(-1) -> 2Omega^2(2) -> 5O.

After twisting by -1 all three terms are acyclic: O(-2), O(-1), and Omega^2(1). Splitting the monad into its two short exact sequences proves that F(-1) is acyclic. At twist zero the same argument, with Omega^2(2) acyclic, shows H^2(F)=0. These statements use only Euler/Bott cohomology, not selected monad values.

Split the degree-one Koszul complex into

    0 -> F(-1) -> F direct-sum F -> I_P tensor F(1) -> 0,
    0 -> I_P tensor F(1) -> F(1) -> F_P(1) -> 0.

Both acyclicity assertions just established give an isomorphism

    A_0 direct-sum A_0 -> A_1,
    (x,y) |-> ell1 x + ell2 y.

Consequently

    A_1 = ell1 A_0 direct-sum ell2 A_0.                   (2)

This applies to every basis of the two-dimensional pencil of equations of P. Every nonzero ell in that pencil therefore induces an injective first-primary map A_0->A_1. Equivalently h^0(F_H(1))=0 for every hyperplane H containing P.

## 2. The next Koszul complex is jointly onto

The degree-two Koszul splitting is

    0 -> F -> F(1)^2 -> I_P tensor F(2) -> 0,
    0 -> I_P tensor F(2) -> F(2) -> F_P(2) -> 0.

Use H^0(F)=H^0(F(1))=H^0(F(2))=0, H^2(F)=0, and H^1(F_P(2))=0. The resulting complex on primary cohomology is

    A_0 --(-ell2,ell1)--> A_1 direct-sum A_1
        --(ell1,ell2)--> A_2.

The first map is injective, the last is surjective, and its middle homology is canonically H^0(F_P(2)), of dimension five. In particular

    ell1 A_1 + ell2 A_1 = A_2.                           (3)

The individual middle maps ell:A_1->A_2 are singular by the section theorem. Equation (3) says their images nevertheless span jointly; it does not assert either is invertible.

## 3. Primary product kernels are intersections in a five-dimensional space

For any two distinct hyperplanes H1,H2 in the good-plane pencil, write G_i=F|H_i and

    T_i = image[H^0(G_i(2)) -> H^0(F_P(2))].

Restriction is injective: its kernel is H^0(G_i(1)), which vanishes by (2). Hence dim T_i=b_i=h^0(G_i(2)), with 1<=b_i<=5.

Let Q=H1 union H2. The exact sequence

    0 -> F --ell1 ell2--> F(2) -> F_Q(2) -> 0

identifies H^0(F_Q(2)) with ker(ell1 ell2:A_0->A_2), because the two ambient H^0 groups vanish. The gluing sequence on the union gives

    H^0(F_Q(2))
      = {(s1,s2): s_i in H^0(G_i(2)), s1|P=s2|P}.

Using the two injective restriction maps gives the canonical identification

    ker(ell1 ell2:A_0->A_2) = T_1 intersect T_2

inside H^0(F_P(2)), a five-dimensional space. Therefore

    ell1 ell2 is primary-injective iff T_1 intersect T_2=0,
    dim ker(ell1 ell2) >= max(0,b_1+b_2-5).              (4)

This is a symmetric sharpening of the earlier one-sided product boundary. The trace spaces are fixed by actual bundle restriction; they are not free subspaces to which generic transversality can be applied without proof.

## 4. A new conditional obstruction for all products

Let b be the generic value of h^0(F_H(2)) as H varies. A general hyperplane belongs to a pencil with good base plane, so 1<=b<=5. A general pair of distinct hyperplanes has good intersection plane and both section dimensions equal to b. Equation (4) then gives generic product-primary defect at least max(0,2b-5).

In particular, existence of even one primary-injective product forces b<=2. Indeed if b>=3, a dense open set of pairs gives noninjective products. Rank-deficiency is closed on the irreducible parameter space P(S1) times P(S1), because the entries of product multiplication vary algebraically. A closed subset containing that dense open set is the whole parameter space. Thus, conditionally on b>=3, every product of nonzero linear forms is primary-bad, including squares on the diagonal.

This conditional failure of every product would still not contradict generic primary injection in the full quadratic parameter space: the product locus is proper. Conversely, b=1 or 2 does not prove a good product exists; actual trace intersections remain to be controlled.

## Scope

The new unconditional structure is (2), (3), and the exact five-dimensional trace intersection (4) for good-plane pairs. Generic b is bounded but not determined. No square limit of distinct-hyperplane traces is asserted, and no flatness is assumed. The result concerns primary multiplication, not the ten-dimensional plane-cubic trace space of the Rao residual problem, not the full adjoint boundary, and not Q4 vanishing. No selected matrix, coefficient, plane, or rank was evaluated.

## Subsequent closure within this proof packet

GENERIC-PRODUCT-PRIMARY-INJECTION.md adds a geometric exclusion of common degree-one annihilators and a binary-quadratic relation argument. It proves that general product quadratics are primary-injective and that the actual generic middle corank is one or two. Thus the conditional b>=3 alternative above is excluded by that companion proof. The trace transversality discussed here is no longer an open premise for general PRIMARY products; the separate Rao residual trace problem remains open.
