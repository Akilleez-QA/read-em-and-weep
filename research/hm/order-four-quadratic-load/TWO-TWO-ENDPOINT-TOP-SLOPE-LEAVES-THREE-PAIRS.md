# Endpoint strict top slope leaves three (2,2) quotient pairs

## Result

The seven pairs / 723 records of TWO-TWO-SECOND-INTERIOR-EULER-EXCLUDES-SEVENTEEN-PAIRS.md reduce to three pairs / 354 records. The same negative V multiplicity excludes each of the four removed pairs. This is a necessary-character restriction, not an exclusion of (2,2) or a realization assertion.

## 1. The actual endpoint derivative, without a rank assumption

Retain K=E^-, M=K^-=E^{--}, and A=E/K. The preceding proof establishes that the second interior quotient is exactly

    J=K/M=A(-2)

in all seven remaining pairs; its determinant torsion has been proved zero, not assumed away. Since M is the kernel of the derivative of K, its own derivative factors through

    beta_M: M -> J(-2)=A(-4).

M is saturated in the constant ambient bundle and all its degrees are at most -4. The strict-top-slope lemma gives H0(M^-(4))=0. Consequently

    H0(M(4)) -> H0(A)

is an injection of representations. This assertion remains valid if M has no degree -4 summand, in which case its source is zero. No hypothesis about the generic derivative rank of the endpoint M is used.

The exact sequence 0 -> M -> K -> A(-2) -> 0 gives

    chi_G(M(4))=chi_G(K(4))-chi_G(A(2)).

Since H0(M(4))-chi_G(M(4))=H1(M(4)) is genuine, a necessary condition is

    H0(A)+chi_G(A(2))-chi_G(K(4)) >= 0.            (1)

## 2. Exact certificates for all seven pairs

The expression in (1) depends only on the equivariant Euler class of K, so all candidate splittings for a given pair give the same result. Exact abstract character arithmetic gives:

- A=O(-8)+O(2)+O(4): expression -V.
- A=O(-8)+W O(3): expression -V.
- A=W' O(-1)+O(2): expression A3-V-P4.
- A=W' O(-1)+O(4): expression D5-V.

Here A3 denotes the three-dimensional irreducible Sym^2 W, to distinguish it from the quotient bundle A; P4 and D5 denote the four- and five-dimensional irreducibles. Each displayed virtual representation has V multiplicity -1, proving that its pair is impossible.

The remaining A and their expression in (1) are:

- O(-8)+O(2)+O(6): A3.
- O(-8)+O(4)+O(6): P4+D5.
- O(-8)+W O(5): P4+D5.

In all three, B=A*(-2). Their degrees a are 0,2,2. The second-interior determinant bounds proved previously are now strictly below 12 on both towers. Thus both exact quotient identifications hold:

    K/K^-=A(-2),       L/L^-=B(-2).

No original or second-interior determinant torsion remains in the three-pair overlist. This follows after the four exclusions; the earlier length-twelve dual branch was retained until its primal partner was independently excluded by (1).

## Reproduction and scope

Run python3 verify_two_two_endpoint_top_slope.py, with --full for the separately named full survivor file. Outputs are two-two-endpoint-top-slope-summary.json and two-two-endpoint-top-slope-records.json. The verifier reads the frozen 723-record file and only the character-helper definitions of the prior verifier, without executing its file-producing section. All earlier files remain unchanged. The compact summary includes the input SHA-256 and every exact certificate.

Only abstract characters and hypothetical bundle splittings are used. There are no actual coefficient or point choices, no actual map or matrix evaluations, no rank tests or scans, and no experiments. In particular the argument does not extend the rank-three plateau assumption to an endpoint. The full (2,2) exclusion remains open.
