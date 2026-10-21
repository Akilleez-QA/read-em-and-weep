# Exceptional hyperplane characters do not determine the jump

## Checked conclusion

The actual equivariant K-class determines all order-five weight multiplicities in the ambient hyperplane map, without evaluating that map. It yields no dimension-forced exceptional adjoints beyond the three known squares. Moreover the largest allowed local torsion length j=2 remains compatible with both local order-five characters and the full global A5 section character.

Thus character defects alone do not decide the exceptional jump or its elementary divisors. This is a precise boundary of the representation-only argument, not an assertion that a chosen compatible model is the actual cokernel.

## 1. Actual K-class and cohomology support

Use U=V directsum W for the actual ambient five-space, A=Sym^2 W, and W' for the other binary two-space, so Sym^2 W'=V. Put N=A directsum W'. The actual equivariant normalized monad gives

    [F]=W' [Omega^2(2)]-N[O(-1)]-N[O],
    [Omega^2(2)]=Lambda^2 U[O]-U[O(1)]+[O(2)].

Since det F=O(-1),

    [B(t)]=[F]^2 [O(t+1)]-[O(t)].                    (1)

For t=2,3 every line-bundle twist occurring in the expanded right-hand side is at least t-1>=1. Its equivariant Euler characteristic is therefore obtained directly from symmetric powers of U; no differential rank occurs in this calculation.

The established actual ambient cohomology is concentrated in H1 at these two twists: h1(B(2))=85 and h1(B(3))=100. This support, from the actual exterior-symmetric resolution and the PR167/PR463 vanishing inputs, is needed to turn the Euler character into H1, rather than infer a representation from an Euler character alone. The resulting dimensions and central traces reproduce the independently proved parity dimensions (41,44) and (46,54).

## 2. Exact order-five multiplicities

Choose an order-five generator for which W has weights1,4 modulo five. Then V has weights0,1,4, A has weights0,2,3, and W' has weights2,3. The genuine spaces are center-even and the binary two-spaces are center-odd.

Expanding (1) gives, in weight order0,1,2,3,4,

    H1(B(2))_+ : 7,9,8,8,9,
    H1(B(2))_- : 8,9,9,9,9,
    H1(B(3))_+ : 10,8,10,10,8,
    H1(B(3))_- : 12,9,12,12,9.                        (2)

At the fixed parameter whose hyperplane equation has weight1, the actual even hyperplane map therefore has source and target multiplicities

    source H1(B(2))_- tensor <ell>: 9,8,9,9,9,
    target H1(B(3))_+            : 10,8,10,10,8.       (3)

The only positive source-minus-target defect is one copy of weight4. The actual two section weights of F_H(2) are4,2, so their three squares have weights3,1,4. They already contain that forced copy. There is no further dimension-forced kernel weight in (3).

If the fiber has only its three squares, its H1 cokernel character is consequently

    1,1,1,2,0.                                       (4)

The opposite fixed parameter has all weights negated, as required.

## 3. A length-two jump is still character-compatible

The all-parameter section-bundle theorem gives the global cokernel C_lin rank five, degree26, and the jump theorem bounds its uniform local torsion length by j<=2. If j=2, its torsion-free quotient has rank five and degree two.

We exhibit compatibility data for j=2, not an actual identification. At the parameter of (3), the cotangent character is weight2: the tautological equation line has weight1 and the other binary line has weight4, so the tangent character is3. Let the local torsion be O/(z^2) with generator weight0. Its fiber character is0 and its Tor_1 character is4. The free quotient fiber character required by (4) is therefore

    (1,1,1,2,0)+weight4-weight0 = (0,1,1,2,1).        (5)

This is exactly the fiber character of

    O_T(2) directsum P4 tensor O_T,

where P4 is the genuine irreducible four-space. Indeed O_T(1) has fiber weight4 at this parameter, so O_T(2) has weight3, and P4 has weights1,2,3,4.

The full global characters also agree. The actual K-class calculation gives

    H1(B(2)) = A+2V+3P4+4D5 +2W+2W'+3S4+4T6,
    H1(B(3)) = 1+4A+2V+3P4+3D5 +3W'+3S4+6T6,

where S4=Sym^3 W and T6=Sym^5 W are binary irreducibles. The exact kernel A O(-6) gives

    H0(C_lin)=1+3A+V+2P4+2D5.                         (6)

Here H1(A O(-6))=A tensor D5=A+V+P4+D5, which is subtracted from the even H1(B(3)) representation.

The twelve-point orbit has stabilizer C5. A length-two module with the chosen generator has successive weights0,2, so its global section character is

    Ind_C5^A5(chi0+chi2)=1+2A+V+P4+2D5.

The candidate free quotient O(2) directsum P4 O has global section representation A+P4. Their sum is exactly (6). Thus neither the local characters nor the complete global section character rules out j=2.

The alternative local torsion type k directsum k, with possibly different stabilizer characters, must likewise be distinguished from O/(z^2); equal length does not mean equal fiber excess. The accompanying verifier lists the elementary character-compatible degree-two free splitting possibilities, without selecting one as actual.

## 4. What remains to be determined

The actual maps, not their characters, determine whether the torsion exists and which elementary divisors occur. The verified data permit the three-square fiber and also permit length-two torsion data. No matrix rank or determinant scalar has been evaluated here.

The verifier uses only the actual equivariant K-class, universal symmetric-power characters, and finite cyclic character bookkeeping. Its full-group check reuses verify_negative_vertex_scalar.py in the same directory. It performs no selected HM/source coefficient calculation or rank scan.
