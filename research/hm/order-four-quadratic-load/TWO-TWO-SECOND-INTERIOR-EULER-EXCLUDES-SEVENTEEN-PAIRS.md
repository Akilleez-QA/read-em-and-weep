# Second-interior Euler constraints exclude seventeen further (2,2) pairs

## Result and scope

The original full derivative determinant in the (2,2) profile has no torsion: A is isomorphic to B*(-2). This follows directly from the second interior quotient degrees, without enumeration. Exact Euler characters of the same second quotient injections then reduce the frozen 24 pairs / 1221 records to seven pairs / 723 records. All survivors have original determinant defect zero. These are necessary possibilities, not realizations. The (2,2) profile itself is not excluded, and no global SF or square-rank bound changes.

## 1. Profile convention and saturation

Use the maximal plateau convention of ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, Section 4. In (2,2), the central bundle is F2=E, and F1=K=E^- is an interior stage. Thus its derivative has rank three and its saturated kernel is F0=K^- of rank 11. The dual reversed plateau has central bundle Q*, rank 13; its first negative transform L has rank 10 and is again interior, with derivative rank three and endpoint L^- of rank 7. No assertion is made that either endpoint K^- or L^- has derivative rank three.

Set A=E/K, B=Q*/L, J=K/K^-, and J'=L/L^-. The actual derivatives induce equal-rank sheaf injections

    J -> A(-2),       J' -> B(-2).

Their cokernels may have torsion; neither is presumed an isomorphism. Derivative kernels are saturated in their source and hence in the constant ambient bundle: the successive ambient quotient is an extension of locally free sheaves. Thus J,J' and both endpoint kernels are bundles.

Both E and Q* have rank-degree data (17,-54),(13,-54) and all degrees at most -2. The strict-top-slope lemma applied twice gives maxdeg K^- and maxdeg L^- at most -4. Write a=deg A, b=deg B. Consequently

    -10-a <= deg J <= a-6,
    -26-b <= deg J' <= b-6.

The lower inequalities use deg K=-54-a, deg L=-54-b and deg K^-<=-44, deg L^-<=-28. Hence a>=-2 and b>=-10. The original transpose injection A -> B*(-2) has invariant determinant length

    t=-6-a-b,       0<=t<=6.

A nonzero invariant effective divisor on the icosahedral projective line has degree at least 12. Therefore t=0 and A=B*(-2). In particular -2<=a<=4 and b=-6-a. This conclusion keeps all three determinant defects distinct.

## 2. Exact second-interior Euler envelope

Let (N,C) be either (K,A) or (L,B), let M=N^-, and let d be the positive index of the actual highest splitting degree of N. Thus N has highest degree -d. Write J_N=N/M and T_N=coker(J_N -> C(-2)). Since N is an interior rank-three stage, J_N and C both have rank three and T_N is torsion. The two exact sequences give

    chi_G(C(d-2))-chi_G(N(d))
      = H0(T_N(d)) + H1(M(d)).                       (*)

Here H0(M(d))=0 by strict decrease of the top slope, and H1(T_N(d))=0 because T_N is torsion. Both terms on the right are genuine representations, so every irreducible multiplicity on the left is nonnegative. This is stronger than the former H0(C(d-2)) top-coefficient bound. In particular negative H1 contributions of C are now retained. Equation (*) neither assumes zero second determinant torsion nor substitutes a formal map for the actual derivative.

Apply (*) to every frozen K and L candidate, retaining a record only when each side retains at least one candidate. Exact abstract character arithmetic gives 723 records and seven ordered quotient pairs. The 17 discarded pairs each have a negative multiplicity on at least one side for every candidate there. The compact summary supplies all their envelope characters as independent certificates.

## 3. Seven remaining pairs and the second determinant lengths

Each pair is determined by A because B=A*(-2). The remaining A are:

1. O(-8) + O(2) + O(4).
2. O(-8) + W O(3).
3. O(-8) + O(2) + O(6).
4. W' O(-1) + O(2).
5. O(-8) + O(4) + O(6).
6. O(-8) + W O(5).
7. W' O(-1) + O(4).

Their degrees a are respectively -2,-2,0,0,2,2,2. All surviving K,L candidates have top index d=3. If s and s' are the lengths of the two second-interior cokernels, the same degree calculation gives

    0<=s<=2a+4,        0<=s'<=2b+20=8-2a.

Each is the degree of an invariant effective determinant divisor. Thus s=0 in all seven pairs: J=A(-2) exactly. Also J'=B(-2) except possibly in the two a=-2 pairs, where s' may be 0 or 12. In that remaining s'=12 branch, its determinant divisor is the reduced twelve-point orbit, the cokernel has length one at each point, and L^- has degree -28 and rank 7 with maxdeg<=-4. Hence L^- is an equivariant coefficient representation of dimension 7 tensored with O(-4). The branch is retained, not discarded.

## Reproduction and limitations

Run python3 verify_two_two_second_interior_euler.py. Add --full to regenerate the separately named survivor records. The compact output is two-two-second-interior-euler-summary.json; full output is two-two-second-interior-euler-records.json. The frozen input is two-two-kernel-top-multiplicity-records.json, SHA-256 ecb306e613b55076416f6682f205174ee88eb166dda0c007c141b92f01a86d15. The verifier imports only the read-only abstract character ring from verify_negative_vertex_scalar.py and confirms that its record input is unchanged.

The verifier checks bounded hypothetical splitting characters and integer degrees only. It does not evaluate any actual coefficient, point, polynomial instance, map, matrix, or rank, and performs no rank scan or consumed experiment. The geometric rank-three statement concerns interior stages only; the exact-sequence proof, not hypothetical map realizability, justifies the filter. Earlier files are left unchanged.
