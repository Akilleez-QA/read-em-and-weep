# An eleven-to-seven section obstruction removes one remaining defect branch

## Claim

For stable ID **G3.21.7d21add56d56**, the profile (2,1) pair

    A=O(-8)+2O(6),   B=2O(-8)+O(6),

has second defect s=0 only. The previously necessary list {0,12} sharpens to **{0}**. This is a new whole-defect exclusion beyond the local module tests: the s=12 torsion quotient is locally possible but incompatible with the actual next derivative.

The quotient case itself is not excluded. The frontier143 count is unchanged, and no realization of the s=0 branch is asserted.

## 1. The global image J is forced

The published rank-eleven endpoint output, source pair index 8, leaves only

    T_def=O(4)|D12

on the s=12 branch. Since C=A(-2)=O(-10)+2O(4), the required image sequence is

    0 -> J -> O(-10)+2O(4) -> O(4)|D12 -> 0.

The O(-10) component cannot contribute to this equivariant quotient. At a point of D12 the C10 stabilizer acts on its fiber with weight -10=0 modulo10, whereas the reduced torsion line has weight4. Therefore the component is zero at every orbit point, hence zero as a map to this reduced sheaf. Equivalently, Frobenius reciprocity gives Hom_G(O(-10),O(4)|D12)=0.

Each map O(4)->O(4)|D12 is an invariant function on the transitive orbit, hence a constant scalar. Surjectivity requires the pair of scalars to be nonzero. A constant GL2 change among the identical O(4) summands reduces every such quotient to restriction from one summand. Its kernel is consequently

    J = O(-10)+O(-8)+O(4),                         (1)

because O(4)(-D12)=O(-8). This is a universal description of every allowed quotient, not a selected map or coefficient evaluation.

As an independent check on the low-component issue, the nonequivariant restriction map from Hom(O(-10),O(4)) onto Hom(O(-10),O(4)|D12) is onto because H1(O(2))=0; an equivariant lift can be obtained by averaging. Thus any such lifted component could also be removed by a triangular source automorphism once a high component is nonzero. In the actual equivariant quotient the stabilizer argument already forces the low component to vanish.

## 2. The endpoint forces eleven sections

Let M=K^- be the second primal kernel. The published profile (2,1) identities and strict top-slope bounds give

    rank M=11,
    deg M=-48-2 deg A+s,
    maxdeg M<=-4,
    maxdeg M^-<=-5.

Here deg A=4 and s=12, so deg M=-44. A rank-eleven split bundle with every ordinary summand degree at most -4 and total degree -44 must have every ordinary summand degree exactly -4. Hence

    h0(M(4))=11.                                  (2)

This uses only rank, degree and the proved slope bound; no endpoint splitting enumeration is necessary. It agrees with the published equivariant endpoint M=(V+2P)O(-4).

## 3. The same J has room for only seven sections

The next derivative of M factors through J(-2), with kernel M^-. Twisting by four and using maxdeg M^-<=-5 gives the necessary injection

    H0(M(4)) -> H0(J(2)).

For the actual image splitting (1),

    J(2)=O(-8)+O(-6)+O(6),
    h0(J(2))=7.                                   (3)

Equations (2) and (3) would require an eleven-dimensional space to inject into a seven-dimensional space, a contradiction.

The earlier endpoint envelope only used H0(M(4))->H0(A); replacing A by the same actual J repairs that lost compatibility and excludes the whole s=12 branch.

## Reproduction and scope

Run `python3 verify_two_one_double_six_second_defect_exclusion.py`.

The small standalone checker pins the published frontier144, rank-eleven endpoint JSON and primal-interior proof, verifies the exact stable ID and unique torsion alternative, checks the stabilizer weights and forced J degrees, and reproduces 11>7. It writes `two-one-double-six-second-defect-exclusion.json` without changing predecessors.

No unpublished same-source datasets are inputs. There are no selected actual points or coefficients, instance matrices or rank tests, scans, spikes, or consumed experiments. The argument concerns universal exact sequences and integer section dimensions only. No global realization, quotient-case exclusion, smoothing or SF claim is made.
