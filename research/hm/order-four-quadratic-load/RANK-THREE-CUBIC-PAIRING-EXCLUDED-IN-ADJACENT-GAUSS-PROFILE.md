# The cubic pairing cannot have rank three in the adjacent Gauss profile

## Result

In the hypothetical generic-rank-three Gauss profile (k,l)=(3,2), the restricted cubic pairing

    B:R O -> T6 O(3),    R=H0(E(2)),

has rank at most two. Thus its only possible nonzero image from the established small-image list is Wprime O(1). This excludes both rank-three image possibilities simultaneously, without enumerating the remaining primal splitting types.

It does not exclude the entire (3,2) profile or generic SF rank three. The numerical square-endpoint bound remains 27.

## Inputs

Use the actual bundles E of rank17 and degree minus54, Q=H O/E, and the plateau

    F0 < F1=K2 < F2=K < F3=E < F4 < F5.

Here K=E^- has rank14 and K2=E^{--} has rank11. The next derivatives have rank three, and persistence gives

    H0(K2(3))=0,    H0(F0(4))=0.                      (1)

The actual character identity gives H0(E(3)) containing Wprime+2T6. The dual cubic evaluation is T6 O(-3) inside Q*. Its paired derivative produces the map B above. The established image list is

    V O,    Wprime O(1),    V O(2),

and each such image is saturated in T6 O(3). These are the exact inputs of the [adjacent-profile theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/7d4e3e6d960438e3000f33d0e68b9e2b970129fa/research/hm/order-four-quadratic-load/ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md), Sections1 and5.

## 1. A rank-three pairing determines the full derivative image

Suppose B has rank three. Let J be the image of the restricted derivative R O->Q and let I be the image of the full derivative E(2)->Q. Both are locally free image sheaves on the parameter line. Their ranks are three, since the full derivative has rank three and its projection already has that rank.

The projection Q->T6 O(3) maps J onto im B, with a torsion kernel; that kernel is zero since J is torsion-free. The projected image of I contains im B with the same rank. Because im B is saturated in T6 O(3), it cannot admit a larger subsheaf of the same generic span inside that bundle. Thus the projected image of I is also im B. Its kernel is again zero. Consequently

    I=J,    I is isomorphic to im B,
    E/K=I(-2).

No saturation of I in Q has been assumed here. Saturation is used only for the previously proved projected image in T6 O(3).

## 2. Exclude im B = V O

This case gives E/K=V O(-2), of degree minus6. Hence deg K=minus48. The next derivative is

    K(3) -> (E/K)(1)=V O(-1),

with kernel K2(3). Its target has no sections, whereas Riemann--Roch gives

    h0(K(3)) >= chi(K(3)) = -48 + 14(3+1) = 8.

This contradicts (1).

## 3. Exclude im B = V O(2)

Now E/K=V O and deg K=minus54. The exact quotient sequence, twisted by three, maps H0(E(3)) to

    H0(V O(3))=V tensor S4=Wprime+S4+T6.

The source contains at least two copies of T6, while the target contains one. Therefore H0(K(3)) contains a copy of T6. This uses an actual cohomology-character lower bound, not a dimension assumption about a chosen derivative.

The next derivative has target

    K(3) -> V O(1),    H0(V O(1))=V tensor W=T6.

By (1) it is injective on sections. The preceding T6 inclusion forces this section map to be an isomorphism. Its restriction to the canonical evaluation bundle T6 O is therefore the complete evaluation of V O(1), up to an automorphism of its section space. Since V O(1) is globally generated, the derivative is surjective as a bundle map. Hence

    K/K2=V O(-2),    deg K2=-48.

The next required derivative is

    K2(4) -> (K/K2)(2)=V O,

with kernel F0(4). Its source satisfies

    h0(K2(4)) >= chi(K2(4)) = -48 + 11(4+1) = 7,

whereas the target has only three sections. This contradicts the second vanishing in (1).

Both rank-three possibilities are excluded. The result applies also when R=0, in which case B=0 from the outset. It leaves rank-two and zero pairings as genuine remaining cases.

## Verification and limits

Run verify_adjacent_cubic_pairing_rank.py. It checks the two representation identities, all degree/rank/Riemann--Roch counts, and the persistence indices. The projection-saturation and complete-evaluation arguments are proved above. No actual coefficients, matrices, rank evaluations, parameter scans, or local-model experiments are used.
