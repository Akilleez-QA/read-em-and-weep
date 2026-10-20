# The degree-five defect satisfies ch2(T) <= 25/2

Retain the rank-ten setup of PROOF.md and its surviving branch (k,d)=(7,5). Write ch2(T)=t h^2. Then
   -53/2 <= t <= 25/2,
in half-integer steps. Equivalently,
   9 <= c2(F) <= 48,
   1 <= c2(R) <= 40,
with their sum equal to 49.

## 1. Global generation of G*

Dualizing the square-coordinate bundle sequence gives
   0 -> G* -> O(1)^15 -> O(3) -> 0.
Its global sections are the linear relations among all degree-two monomials. These generate G* everywhere. Here is a direct universal check, involving no actual operation. Choose coordinates with x0 nonzero at a point. Write e_ij for the formal basis vector of the monomial x_i x_j. The linear relations
   x0 e_0i - x_i e_00,
   x0 e_ij - x_i e_0j
(for i>0 in the first list and i,j>0 in the second) span the fiber of the kernel there: their evaluations reduce every basis vector except e_00 to a multiple of e_00, leaving exactly the one-dimensional quotient. There are four plus ten such relations, giving the required fourteen-dimensional kernel. The argument works on every coordinate chart.

## 2. Restriction and duality on a general plane

F is reflexive, so its singular locus has codimension at least three. A general plane L=P^2 in P^4 avoids this locus and is not contained in the divisorial support of T. The restricted map G_L -> F_L is a map of equal-rank bundles with nonzero determinant and is therefore injective. Its cokernel is T_L by right exactness of restriction. Thus
   0 -> G_L -> F_L -> T_L -> 0.

In particular Tor1(T,O_L)=0; the displayed locally free resolution also computes its K-theory class. The sheaf
   E=Ext1_L(T_L,O_L)
is a quotient of G*_L, hence is globally generated. Dualizing the resolution shows
   [E]=[G*_L]-[F*_L],
so E has degree d=5 and ch2(E)=-t. It is a one-dimensional sheaf. Purity also follows from its length-one locally free resolution, although the bound below does not require it.

## 3. Elementary bound for a globally generated curve sheaf

If E is a globally generated sheaf on P^2 with support of dimension at most one and degree d, then
   ch2(E) >= -d^2/2.

For d=0 the sheaf is zero-dimensional and ch2(E) is its nonnegative length. For d>0, remove its maximal zero-dimensional subsheaf A. The quotient E/A is still globally generated and pure one-dimensional, and ch2(E)=length(A)+ch2(E/A). It suffices to bound this pure quotient.

Choose a nonzero global section. Its image is pure one-dimensional as a subsheaf of a pure sheaf, so it is O_D for an effective Cartier divisor D of degree m>=1. (A quotient of O on the smooth surface P^2 with pure one-dimensional support has an unmixed height-one ideal, hence is a divisor structure.) Its quotient Q remains globally generated and has degree d-m. Additivity and induction give
   ch2(E) = -m^2/2 + ch2(Q)
           >= -m^2/2 - (d-m)^2/2
           >= -d^2/2.
This proves the claim, including any zero-dimensional torsion appearing during the induction.

Apply it to the dual defect E of Section 2. Since ch2(E)=-t and d=5, one gets t<=25/2. Combining with the strict positivity lower bound t>=-53/2 from PROOF.md gives the stated interval.

This is universal bundle and sheaf geometry. The monomial calculation verifies only the standard square-coordinate syzygy bundle; it evaluates no actual HM operation, selected input, or actual rank instance.
