# Three component alternatives remove index-5 second defect 20

## Claim and published inputs

For stable ID **G3.21.ed1df480d8d2**, source pair index5,

    A=O(-8)+O4+O16,   B=O(-18)+O(-6)+O6,

the profile (2,1) second defect s=20 is impossible. This is a whole-defect exclusion, not an exclusion of the quotient label. It is separate from the index5 s=24 section obstruction.

Use the actual stages K=E^-, M=K^-, J=K/M and the exact sequence

    0 -> J -> C=O(-10)+O2+O14 -> T_def -> 0.

The published rank-eleven theorem allows exactly T_def=O2|D20 for s=20 and lists four possible M endpoints. Every one contains V O(-4), so H0(M(4)) contains V. The actual derivative M->J(-2), with kernel M^- of maximum degree at most -5, therefore requires an injection H0(M(4))->H0(J(2)). We distinguish the high, middle and low summands of C.

## High component nonzero

A nonzero equivariant component O14->O2|D20 is nonzero everywhere on this reduced transitive orbit. Its restriction is invertible. After twisting by two, its section map from H0(O16) is injective because 16<20. The low summand has no sections. Projection to the middle summand consequently embeds H0(J(2)) into H0(O4)=Sym^4 W=D.

But D contains no V, whereas H0(M(4)) contains V. The required injection is impossible.

## High zero, middle nonzero

The restriction of the middle O2 summand is invertible. The low component can be removed by an equivariant triangular source automorphism, as follows. The space of equivariant maps O(-10)->O2|D20 is one-dimensional: O12 has trivial C6 fiber weight, and equivariant sections on a transitive reduced orbit are determined by their invariant fiber. The invariant section defining D12 has degree12 and is nowhere zero on the disjoint orbit D20. Its restriction spans this space. Thus the low component lifts to a global equivariant map O(-10)->O2. Subtract that lift from the middle coordinate. This does not alter the zero high component.

The resulting kernel is therefore equivariantly

    J=O(-10)+O(-18)+O14.

Now H1(J(2))=Sym^6 W+Sym^14 W contains D. On the other hand maxdeg K<=-3 gives H0(K(2))=0, and the actual presentation

    0 -> E -> M3 O(-1) -> M4 O -> 0,
    M3=3Wp+3S+6T,  M4=2V+4P+3D,

combined with 0->K->E->A->0 gives

    H1(K(2))=chi(A(2))-chi(E(2))=A_std+3V+3P.

Here A_std is the three-dimensional irreducible, not the quotient bundle A. This representation has no D. Since H1(K(2))->H1(J(2)) is onto (H2(M(2))=0), the D multiplicity gives a contradiction.

## High and middle both zero

Only the low summand supplies the quotient, forcing

    J=O(-30)+O2+O14.

But rank K=14, deg K=-54-deg A=-66 and maxdeg K<=-3 imply mindeg K>=-66-13(-3)=-27. Hence K(27) is globally generated, as is its quotient J(27). The displayed O(-30) summand contradicts this. These three exhaustive cases prove the claim.

## Reproduction and scope

Run `python3 verify_two_one_index_five_second_defect_twenty_exclusion.py` to generate `two-one-index-five-second-defect-twenty-exclusion.json`. The standalone checker pins the published frontier144, endpoint list and primal-interior constraints, checks the exact stable ID and unique torsion alternative, checks V in all four published endpoints, reproduces the character arithmetic over Q(sqrt(5)), and verifies the degree bound.

The degree12 lift uses only the standard invariant orbit divisor D12: its defining section is invariant because the binary icosahedral group has no nontrivial one-dimensional characters. No selected points, coefficients, actual matrices, actual rank tests, scans, spikes or consumed experiments enter. There is no first-kernel or J-splitting enumeration, unpublished witness-table dependency, quotient-case exclusion or realization claim. Frontier143 remains unchanged. Combined with the separate s=24 exclusion, index5 has only second defects {0,12} left.
