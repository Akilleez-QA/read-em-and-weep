# A seven-item rank-two overlist excludes index-10 second defect 20

## Claim

For stable ID **G3.21.d41783aef00b**, source index10,

    A=O(-8)+Wp O9,   B=Wp O(-11)+O6,

the profile (2,1) second defect s=20 is impossible. The published rank-eleven theorem gives exactly two alternatives, T_def=O0|D20 or O2|D20. Both are excluded below. This removes a whole defect branch, not the quotient case;143 quotient labels remain.

Write K=E^-, M=K^-, J=K/M and C=A(-2)=O(-10)+Wp O7. Use

    0 -> J -> C -> T_def -> 0.

Here deg K=-64 and maxdeg K<=-3 imply mindeg K>=-64-13(-3)=-25. Every quotient J of K also has mindeg at least -25, since K(25), hence J(25), is globally generated.

At D20 the stabilizer is C6. With O1 weight1 and Wp weights +/-1, C has low weight2 and high weights {0,2}. For either torsion alternative, any nonzero map from the high rank-two summand to T_def is surjective: it has rank one on every point of this reduced transitive orbit.

## A complete small rank-two overlist

Suppose the high summand maps nontrivially, and put

    J'=ker(Wp O7 -> O(k)|D20),   k=0 or2.

It has rank2, degree -6 and maximum splitting degree at most7. Equivariant Birkhoff--Grothendieck splitting gives exactly the following overlist:

    O(-12)+O6, O(-10)+O4, O(-8)+O2,
    O(-6)+O0, O(-4)+O(-2), W O(-3), Wp O(-3).

For completeness, the only irreducibles of dimensions at most2 are1,W,Wp. The effective central character forces even degrees for trivial lines and odd degrees for W,Wp. Two lines have degrees e<=f<=7 and e+f=-6, giving exactly the five even pairs above; a two-dimensional irreducible must have degree -3. Thus this list does not assume a lower degree bound or an unpublished splitting dataset.

The reduced divisor exact sequence gives

    chi(J') = Wp Sym7 W - Sym^k W - Sym^(18-k) W.

Exact character arithmetic gives:

- k=0: chi(J')=-P. Only O(-10)+O4 and Wp O(-3) match.
- k=2: chi(J')=1-D. Only O(-6)+O0 matches.

For k=0, the first candidate cannot embed into Wp O7: its O4 summand has

    Hom_G(O4,Wp O7)=(Wp tensor Sym3 W)^G=0.

Therefore J'=Wp O(-3) when k=0, and J'=O(-6)+O0 when k=2. This argument checks only seven abstract splitting types and one equivariant Hom space, not an actual matrix or selected map.

## The two torsion alternatives

For k=0 the low component is zero by its weight2. Surjectivity forces the high component to be nonzero. Hence J=O(-10)+J', and h0(J(2))=0.

For k=2, if the high component were zero, the low component alone would supply T_def, forcing J=O(-30)+Wp O7. This violates mindeg J>=-25. Thus the high component is nonzero and surjective. Projection to the low summand then gives an exact sequence

    0 -> J' -> J -> O(-10) -> 0.

No splitting of this extension is assumed. Since H0(O(-8))=0, it gives H0(J(2))=H0(J'(2))=H0(O2), of dimension3.

Finally rank M=11 and deg M=-48-2 deg A+s=-48, so Riemann--Roch gives h0(M(4))>=11*5-48=7. The actual derivative M->J(-2) has kernel M^- of maximum degree at most -5, and therefore injects H0(M(4)) into H0(J(2)). Both bounds, zero and three, contradict seven. This proves the claim.

## Reproduction and exact scope

Run `python3 verify_two_one_index_ten_second_defect_twenty_exclusion.py`; output is `two-one-index-ten-second-defect-twenty-exclusion.json`. The standalone checker pins the published frontier144, endpoint alternatives and primal-interior proof, checks the stable ID and A/B, derives the complete seven-item overlist, reproduces both Euler characters and the Hom obstruction using exact Q(sqrt(5)) arithmetic, and verifies the two section contradictions.

This is independent of unpublished E/Q/K/M witness tables and broad first- or second-kernel enumeration. There are no selected actual coefficients or points, matrices or actual rank tests, scans, spikes or consumed experiments. It proves no realization, smoothing or SF claim. Combined with the separately published index10 s=24 exclusion, only second defects {0,12} remain for this quotient label.
