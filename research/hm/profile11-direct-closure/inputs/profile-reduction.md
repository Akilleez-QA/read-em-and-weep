# Direct coverage reduction from the canonical primary four types

## 1. Result and exact scope

For the ACTUAL saturated HM Gauss inclusion E in the constant plane-section bundle, use the same fixed parameter and group marking throughout. The primary-terminal theorem PR1123 forces one of these four necessary equivariant splitting types:

    D-type: D O(-2)+(W'+T)O(-3)+V O(-4)+O(-8),
    P-type: P O(-2)+(W'+T)O(-3)+V O(-4)+W' O(-5),
    V-type: V O(-2)+(W'+T)O(-3)+2V O(-4),
    zero-top type: (W'+2T)O(-3)+V O(-4).             (1)

None is asserted realized. Under the original profile-specific necessary quotient theorems, the following conclusions hold without the subsequent 182-to23 exclusions, same-source witness relation, or four-pair ledger:

1. The maximal generic-rank-three profile (1,2) is impossible.
2. For maximal profile (2,1), E must have the exact D-type in (1). Exactly eight of the original thirteen ordered quotient rows survive the necessary conditions proved here, listed in Section 5.

This does not exclude profile (2,1) or (1,1), and therefore is not COV and not a global generic-rank-three exclusion. It is a shorter independent resolution of the profile-(1,2) coverage branch and an actual-source restriction in profile (2,1).

All nine full immutable public inputs and their byte/Git-blob identities are in INPUTS.json. The original ten-pair (1,2) theorem is at 857cd414252618a53a79ddce72982c6d91341db9; the thirteen-pair (2,1) theorem is at f7071d29886c83151028576bf32e001c347cafc9; PR1123 is at 504b7eb800407dfc7e6340c98c72cdd553939f54; PR1124 is at 48396766d4e61a9de2455b1d068ba8abe09e05f3. Exact repository paths and full URLs are in the manifest. The earlier geometric proofs of necessity remain imported theorems, not inferred from JSON. The original rows are used only to identify the listed quotient shapes and stable identities.

## 2. Two direct necessary conditions on the actual quotient

Put K=E^- and A_q=E/K. This is the actual locally free quotient by the derivative kernel, not an arbitrary bundle with the same character. Its induced map into Q(-2) need not be saturated.

### 2a. Canonical cubic visibility

This is the actual-embedding visibility theorem of PR1129 at d1238732f42df5c70ba4430e230428d2cf699bbe, research/hm/primary-gauss-visibility/PROOF.md, freshly authenticated here. Its short argument is recalled to keep the orientation explicit.

PR1124 constructs the saturated actual primary block C=(W'+T)O(-3) inside this E and proves all degrees of E/C are at most-2. For any nonzero coefficient line L in C, the quotient E/L also has all degrees at most-2: it is an extension of E/C by the other O(-3) lines. If beta_E killed L, its internal derivative would land in (E/L)(-2), whose top degree is at most-4. Hom(O(-3),(E/L)(-2))=0 would make the negative saturated L horizontal, impossible in a constant bundle over C. Consequently

    W'+T embeds in H0(A_q(3)).                     (2)

This is coefficient-space injection, not fiberwise injection of the rank-eight block. It retains the actual original ambient inclusion and chooses no horizontal complement.

### 2b. Iterated section envelope, including rank-drop endpoints

Let F_0=E and F_{i+1}=F_i^- be its successive actual Gauss kernels. They remain saturated in the same constant bundle. The strict-top theorem gives maxdeg F_i<=-2-i, allowing zero kernels. Put J_i=F_i/F_{i+1}, so J_0=A_q. Differentiation of a kernel section shows that the derivative of F_i lands in (F_{i-1}/F_i)(-2). Thus for every i>=1 there is a sheaf injection

    J_i -> J_{i-1}(-2) -> A_q(-2i).

This does not presume that later derivative ranks equal three. For any integer r>=2, H0(F_{r-1}(r))=0. Telescoping the exact kernel-quotient sequences and using finite-group semisimplicity gives the necessary character inequality

    H0(E(r)) <= sum_(i=0)^(r-2) H0(A_q(r-2i)).     (3)

The right side minus chi_G(E(r)) is consequently genuine as well. We only use r=4 and r=10 below, not an uncontrolled twist search.

The exact ACTUAL presentation gives

    chi_G(E(4))=3V+3P+2D.                          (4)

In particular H0(E(4)) contains at least three V copies for every type in (1).

## 3. Exclude profile (1,2) directly from its original ten shapes

The original necessary theorem leaves precisely the following A_q shapes, with B_q=A_q^*(-2):

    old0:  O(-10)+O(-8)+O(14),
    old2:  O(-10)+O(2)+O(4),
    old4:  O(-10)+2O(4),
    old6:  2O(-8)+O(14),
    old7:  O(-8)+O(2)+O(4),
    old8:  O(-8)+O(2)+O(6),
    old12: W O(-9)+O(14),
    old14: W' O(-3)+O(4),
    old20: O(-10)+W O(3),
    old21: O(-8)+W O(3).                           (5)

These are the original old IDs, not newly numbered survivors. The argument below exhausts (5).

Every degree in (1) is at least-8. Hence no type has a nonzero map to O(-10) or W O(-9). The quotient projection onto such a summand would have to be onto. This excludes old0,2,4,12,20.

Only the D-type has a degree-at-most-minus-eight summand, and it is a single O(-8). Consequently no type can surject onto 2O(-8), excluding old6. This is a rank-one-to-rank-two quotient obstruction, not merely a nonzero-Hom test on each target line separately.

For old8, H0(A_q(3))=Sym5 W+Sym9 W=S+2T contains no W'. Equation (2) excludes it.

For the three remaining shapes, compute the r=4 target in (3):

    old7 and old21:
      H0(A_q(4))+H0(A_q(2))+H0(A_q)
        = A_std+2V+3P+3D;

    old14:
      H0(A_q(4))+H0(A_q(2))+H0(A_q)
        = V+3P+2D.

Their V multiplicities are two and one, respectively, smaller than the at-least-three in (4). All are impossible. This proves conclusion1, including all original second-dual-defect alternatives: the proof used neither a value nor vanishing of that separate defect.

## 4. Profile (2,1): eliminate all but the D-type

The original thirteen rows have the following eleven distinct A_q shapes; the two marked shapes occur with both original determinant defects 0 and12:

    O(-10)+2O(6);
    O(-8)+O(2)+O(6);
    O(-8)+O(2)+O(16);
    O(-8)+O(4)+O(6) [two rows];
    O(-8)+O(4)+O(16);
    O(-8)+W O(5) [two rows];
    O(-8)+2O(6);
    O(-8)+O(6)+O(16);
    O(-8)+W' O(9);
    W' O(-5)+O(16);
    W' O(-1)+O(6).                                (6)

O(-10)+2O(6) is excluded by the quotient degree obstruction already used. Equation (2) excludes the second, seventh and last shapes in (6), whose cubic sections are respectively S+2T,2S+2T,S+2T, all missing W'.

Every remaining shape containing O(-8) forces E to be the D-type: all three other sources in (1) have degrees greater than-8 and admit no map to that quotient line.

It remains to exclude A_q=W' O(-5)+O(16). The V-type and zero-top type have degrees greater than-5, so cannot supply its negative summand. The D-type has only one lower summand O(-8); but

    Hom_G(O(-8),W' O(-5))=(W' tensor Sym3 W)^G=0,

since W' tensor Sym3 W=V+D. All its other summands have degree greater than-5. Therefore this quotient shape forces the P-type in (1), and the W'(-5) quotient is supplied by its displayed W'(-5) summand.

Apply (3) at r=10. Every summand of this E(10) is nonnegative, and its trivial-section multiplicity is four: P tensor Sym8, W' tensor Sym7, T tensor Sym7, and V tensor Sym6 each contribute one; W' tensor Sym5 contributes zero.

The right side of (3) has trivial multiplicity only three. Indeed its W' part has symmetric indices5,3,1 (the others negative), none containing W'. The scalar O(16) part has symmetric indices

    26,24,22,20,18,16,14,12,10.

Only degrees24,20,12 have a trivial constituent, once each; exact universal character arithmetic verifies these nine fixed values. Thus (3) would require four trivial copies to inject into three, impossible.

This excludes the final non-D possibility. No identification of separate primal and dual existential witnesses is used: each map and section argument concerns the same actual E and its actual quotient A_q.

## 5. Exact remaining profile-(2,1) dependency

The retained original source indices and original defects are:

    2: A_q=O(-8)+O(2)+O(16), defect0;
    3: A_q=O(-8)+O(4)+O(6), defect12;
    4: A_q=O(-8)+O(4)+O(6), defect0;
    5: A_q=O(-8)+O(4)+O(16), defect0;
    6: A_q=O(-8)+W O(5), defect12;
    7: A_q=O(-8)+W O(5), defect0;
    9: A_q=O(-8)+O(6)+O(16), defect0;
    10: A_q=O(-8)+W' O(9), defect0.

Every one now requires the same exact D-type in (1). In defect-zero rows B_q=A_q^*(-2). The two defect-twelve rows both have B_q=O(-18)+O(-8)+O(6), as in the original theorem. The exact stable IDs and ordered pairs are retained in RESULT.json.

These are necessary leftovers of this proof, not realizations and not a claim they are live in later historical ledgers. To close the profile with this route, it remains to exclude these actual D-type quotient cases. No later source2 transfer, rank-one endpoint classification or original182-to23 reduction has been silently imported.

## 6. Verification and boundary

The new checker verifies the complete immutable inputs, all ten and thirteen original ordered rows, the4 source degree/multiplicity facts, the fixed representation identities used above, and the exact residual row list. It does not rerun historical enumeration or evaluate a selected HM/source instance.

The argument resolves two narrow coverage steps without a composite ledger. The separate profile(1,1) branch, remaining profile(2,1) cases and earlier maximal-profile exhaustiveness still matter for a global rank-three claim. No maximal-rank, square-rank, obstruction value, full-adjoint invertibility, smoothing, algebraicity, or original theorem repair is claimed.
