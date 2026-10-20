> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Cubic section schemes: a necessary non-ACM obstruction

This is a reduction, not an exclusion of determinant degree three.

Assume the stated rank-seven branch: E=F* has rank 11, R has rank 9, both have c1=3, h0 at least 20, positive c2, and c2(E)+c2(R)=9. Their general-section sequences give schemes Z_E and Z_R with

    h0(I_Z_E(3)) >= 10,    h0(I_Z_R(3)) >= 12.

Both cubic systems have no fixed divisor, since their originating sheaves are generated outside codimension two. Their codimension-two degrees equal the respective second Chern classes.

## Two quadrics force degree at most four

Let Z be a codimension-at-least-two scheme in P4 whose cubic ideal has no fixed divisor. Suppose its ideal contains two independent quadrics q1,q2.

If the quadrics are coprime, their complete intersection contains Z and has degree four; hence the codimension-two degree of Z is at most four.

Otherwise write q1=l a and q2=l b, where l,a,b are linear and a,b are independent. Choose C in I_Z(3) not divisible by l. The scheme cut out by (la,lb,C) contains Z. Its codimension-two cycle is supported on V(l,C), of degree three, and possibly the plane V(a,b), of degree one. Multiplicities are controlled as follows. Away from V(a,b), the ideal is (l,C), so its cycle multiplicities are precisely those of that complete intersection. If V(a,b) is not contained in V(l), then at its generic point l is a unit, and the ideal contains (a,b), so any additional multiplicity is at most one. If V(a,b) is contained in V(l), choose local transverse parameters l,b at its generic point. The ideal (la,lb) is then (l^2,lb). Since C is not divisible by l, V(l,C) has some finite local multiplicity m there. Modulo C, the extra annihilator l contributes at most the residue field: equivalently the exact sequence for multiplication by l on the quotient by (l^2,lb,C) shows length at most m+1. Thus the total cycle degree is at most 3+1=4 in this case also. Therefore deg_2 Z <=4.

## Consequently one section scheme is non-ACM

Since the two degrees sum to nine, at least one is at least five. Call that scheme Z. By the preceding argument,

    h0(I_Z(2)) <= 1.

In particular it has no linear equation. If Z were arithmetically Cohen--Macaulay, its homogeneous coordinate ring, of dimension three, would have a nonnegative Artinian-reduction h-vector. Its first entries would satisfy

    h_0=1, h_1=2, h_2>=2.

The Hilbert function in degree three would therefore satisfy

    H_Z(3)=10 h_0+6 h_1+3 h_2+h_3 >=28,

and hence h0(I_Z(3))<=35-28=7. This contradicts either required cubic-section bound. Therefore at least one of Z_E,Z_R has codimension-two degree at least five and is not ACM.

This does not prove that either scheme is locally non-Cohen--Macaulay: local Cohen--Macaulayness and arithmetic Cohen--Macaulayness are different conditions. Nor does reflexivity of E supply the missing arithmetic vanishing.

## Remaining gap

To exclude the rank-seven branch by this method, one needs an additional theorem ruling out the requisite non-ACM scheme: degree at least five, at most one quadric, at least ten cubics (at least twelve on the R side), and no fixed divisor in its cubic ideal. The section-count argument alone has not supplied that theorem.

Only universal sheaf geometry and Hilbert functions were used. No operation, source matrix, input, rank instance, product, jet, or residue was evaluated.
