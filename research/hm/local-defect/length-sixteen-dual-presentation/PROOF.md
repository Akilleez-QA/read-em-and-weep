# The length-sixteen candidate has an explicit dual presentation and Betti table

## Statement and assumptions

Work over C with S=C[x1,x2,x3,x4], or its completion at the homogeneous maximal ideal. Use the abstract module P of `length-sixteen-local-defect/CANDIDATE.md`: four degree-zero generators t_j, indices j in F5*, and the ten linear relations

    x_i t_(3i)=0,
    x_i t_i=lambda x_(-i)t_(3i),
    x_i t_(-i)=-epsilon x_(-i)t_i,

where lambda is nonzero, lambda^4 is not 1, and epsilon is 1 or -1. The last family has two independent members. Retain its full H action and central-character convention. The previously established normal forms give Hilbert function (4,6,4,2), quadratic basis F_j=x_(-j)^2 t_j, and cubic classes G_j=x_j F_j with G_(-j)=-epsilon G_j.

New conclusions are:

1. The entire socle of P is its degree-three pair, with no lower-degree socle.
2. The normalized graded finite dual Q has Hilbert function (2,4,6,4) and the explicit eight-relation presentation below.
3. The minimal graded free resolution of P has terms

    F0=S^4,
    F1=S(-1)^10,
    F2=S(-2)^4 + S(-3)^6 + S(-5)^2,
    F3=S(-4)^4 + S(-6)^4,
    F4=S(-7)^2.

Thus its total Betti numbers are (4,10,12,8,2), and those of its finite dual are (2,8,12,10,4).

These are abstract local-module results, not construction or exclusion of a reflexive rank-two realization. The original candidate's existence and relation-budget equality are premises, not new claims made by this note.

## 1. No socle below the terminal layer

The socle is graded. Degree zero is the four-dimensional irreducible O0, degree one is the sum of the nonisomorphic irreducibles O2 and the opposite clock pair, and degree two is O1. The kernel of the combined multiplication map in each degree is an H-subrepresentation.

Multiplication is nonzero on degree zero, for instance x_i t_i is nonzero. On the O2 part of degree one use U_i=x_i t_i. The existing quadratic identities give

    x_(-i) U_i=-epsilon F_(-i) != 0.

On the clock pair use V_i=x_i t_(-i); then

    x_i V_i=F_(-i) != 0.

Neither irreducible summand can therefore lie in the multiplication kernel. Semisimplicity and their nonisomorphism imply that this kernel is zero. On degree two,

    x_j F_j=G_j != 0,

so the irreducibility of O1 again gives zero kernel. Every variable kills every G_j by the established normal forms. Hence

    Soc(P)=P3,    dim Soc(P)=2.

The opposite B-weights of this socle are (0,+1),(0,-1). For the normalized generator g of C4, gG_j=G_(2j) and g^2G_j=G_(-j)=-epsilon G_j. Its central character is omega^2 when omega is the central character on W and the top has character omega^(-1).

## 2. Dual generators and their actions

Let Q_d=Hom_C(P_(3-d),C), with S action defined by

    (x phi)(p)=phi(xp).

This puts the dual socle in degree zero. Let q1,q2 be the functionals dual to G1,G2. The standard finite-length duality identifies this vector-space dual with Ext^4 up to its uniform determinant-character factor and grading shift. For D(P)=Ext^4_R(P,R), retain the factor det(W)^(-1); it does not change the following module relations or Betti dimensions. In particular no unrecorded character is discarded in the equivariant interpretation.

Since Soc(P)=P3, q1 and q2 generate Q. Indeed the dual of Q/mQ is Soc(P); a proper generated submodule would contradict graded Nakayama. The Hilbert function of Q is consequently the reversed sequence (2,4,6,4).

The quadratic multiplication identities x_iF_j=0 for i not equal to j and x_jF_j=G_j give precisely the four linear annihilators

    x2 q1=x3 q1=x1 q2=x4 q2=0.                    (L)

There are no additional independent linear relations, since dim Q1=4. Dividing the free module by (L) gives

    N=C[x1,x4] q1 + C[x2,x3] q2.

Its degree-two dimension is six, equal to dim Q2, so no quadratic relations remain.

## 3. The four cubic relations

Write t_j^* for the dual basis of P0. Transposing the original candidate's cubic normal forms gives the following complete list on the two polynomial planes:

    x1^3 q1=-(epsilon/lambda)t2^*,
    x1^2 x4 q1=-epsilon t4^*,
    x1 x4^2 q1=t1^*,
    x4^3 q1=(1/lambda)t3^*,

    x2^3 q2=-(epsilon/lambda)t4^*,
    x2^2 x3 q2=-epsilon t3^*,
    x2 x3^2 q2=t2^*,
    x3^3 q2=(1/lambda)t1^*.

For example, the first identity uses the original formula
x_(3j)^3 t_j=-(epsilon/lambda)G_(3j) with j=2; the second uses G4=-epsilon G1. The remaining entries follow in the same way, and all coefficients are nonzero under the stated assumptions.

Thus the cubic kernel has the four independent generators

    x1^3 q1+(epsilon/lambda)x2 x3^2 q2,
    x1^2 x4 q1-lambda x2^3 q2,
    x1 x4^2 q1-lambda x3^3 q2,
    x4^3 q1+(epsilon/lambda)x2^2 x3 q2.           (C)

Their projection onto the first plane is the full cubic monomial basis. Their projection onto the second plane is also a basis, since lambda and epsilon are nonzero. Therefore multiplying (C) by x1,x4 kills every quartic on the first plane: its second-plane part vanishes by (L). Multiplication by x2,x3 similarly kills every quartic on the second plane. All higher degrees vanish as well.

The quotient N/(C) consequently has Hilbert function (2,4,6,4), hence length16. Its natural surjection to Q is an isomorphism. This proves that (L) and (C) are a complete presentation, not just relations that happen to hold.

The four linear relations are minimal. After dividing by them there are no quadratic relations, and the four cubic relations are independent. Thus all four cubic relations are also minimal, with no extra minimal relations of any degree:

    beta_(1,1)(Q)=4,    beta_(1,3)(Q)=4.

This describes the finite dual by two plane generators linked in cubic degree. It does not identify a geometric defect with this dual.

## 4. The full graded Betti table

The original candidate has four degree-zero generators and exactly ten degree-one relations. Its socle has dimension two, concentrated in degree three. The regular-parameter Koszul resolution therefore places its last free module in degree 3+4=7:

    F4=S(-7)^2.

Finite-length graded duality reverses the minimal resolution. With Q normalized as above, its complementary internal degree is 7, so

    beta_(i,j)(P)=beta_(4-i,7-j)(Q).

The newly obtained first syzygies of Q imply

    beta_(3,4)(P)=4,    beta_(3,6)(P)=4.

Finally multiply the known Hilbert polynomial by (1-t)^4:

    (4+6t+4t^2+2t^3)(1-t)^4
      =4-10t+4t^2+6t^3-4t^4+2t^5-4t^6+2t^7.

The alternating Betti numerator is beta0-beta1+beta2-beta3+beta4. All terms except beta2 have now been identified, forcing

    beta2(t)=4t^2+6t^3+2t^5.

This proves the displayed resolution terms. It states their graded ranks, not explicit differentials between them. Completion preserves the minimal Betti numbers and the finite module.

## 5. Consequence for the remaining realization question

If this candidate P is the finite dual of an isolated defect Q=Ext^2_R(M,R) for an equivariantly determinant-trivial reflexive rank-two M, then Q must have precisely the two-generator/eight-relation presentation above, and its minimal Betti numbers must be (2,8,12,10,4). In particular a minimal resolution of M has last free rank two, since the minimal generator number of Ext^2(M,R) equals that last rank.

More generally, if u redundant columns occur in the dual presentation F1^*→F2^* of such an M, the usual minimal-resolution count forces

    rank F2=2,
    rank F1=8+u,
    rank F0=8+u.

These are necessary consequences, not existence claims. The equality-case Tor map for a realization must still be supplied; the finite dual presentation alone is not that map. The concrete presentation and graded Betti data remove missing local input for testing such realization constraints without selecting any actual HM source.
