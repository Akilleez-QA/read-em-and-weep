# The column third-strand jump divisor and its equality-case rigidity

## Scope and pinned dependencies

Work over an algebraic closure of the established characteristic-zero field. All orbit assertions concern geometric points. Write P=P(W*) and A_lambda=S/J_lambda for the projective column family. The numerical statements descend by field extension; no rationality of the exceptional geometric points over the original field is asserted.

The inputs are:

- PR512, commit 26811b53c198879d0c55a2fb9ba75187bee38d9c, [research/hm/column-family-intersections/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/26811b53c198879d0c55a2fb9ba75187bee38d9c/research/hm/column-family-intersections/PROOF.md): the family has A_0=O, A_1=T tensor O, A_2=E tensor O(2), with dim(T)=dim(E)=5, and A_d=0 for d>=3.
- PR513, commit df947c1ce092c0c59dcef187639147da8a7b2873, [research/hm/column-level-resolution/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/df947c1ce092c0c59dcef187639147da8a7b2873/research/hm/column-level-resolution/PROOF.md): u(lambda)=beta_{3,4}(A_lambda) is the remaining resolution parameter and is divisible by five.
- PR517, commit e624a3c4758bd11b2851c2bc52687b32f79215f3, [research/hm/column-third-strand/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/e624a3c4758bd11b2851c2bc52687b32f79215f3/research/hm/column-third-strand/PROOF.md): u(lambda) belongs to {0,5,10,15,20} at every point.
- PR490, commit 1c5ad353bb5f1808150f64cde3c29b92c6e13d91, [research/hm/dual-tensor-bridge/VERIFICATION.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/1c5ad353bb5f1808150f64cde3c29b92c6e13d91/research/hm/dual-tensor-bridge/VERIFICATION.md): the normalizer-equivariant presentation and the binary multiplicity space W=W'.

Repository: https://github.com/Akilleez-QA/read-em-and-weep . The representation source is Horrocks--Mumford, *A rank 2 vector bundle on P4 with 15,000 symmetries* (1973), Sections 1 and 2.2: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf . We use the order-125 Heisenberg subgroup Gamma, its unique five-dimensional irreducible for each nontrivial central character, and the binary normalizer quotient SL(2,F5). Its action on P(W*) is the faithful icosahedral projective action A5.

No generic rank is assumed or computed. No selected source-instance evaluation is used.

## Theorem

Let u_0 be the generic value of u(lambda). There is a unique orbit Omega_5 of size twelve for the projective A5 action, namely the fixed points of the subgroups of order five. Exactly one of the following alternatives holds:

1. u(lambda)=u_0 everywhere;
2. u_0 is in {0,5,10,15}, u(lambda)=u_0+5 on Omega_5, and u(lambda)=u_0 away from Omega_5.

In the second alternative the maximal-rank determinantal divisor of the reduced multiplicity map is precisely the reduced divisor Omega_5, not a multiple of it. In particular, generic u_0=20 implies uniform u=20.

There is also an equality-case constraint: if u_0=15 and the second alternative holds, the multiplicity map factors as

9O -> 6O -> 6O(2) -> 10O(2),

where the first map is a constant surjection, the last map is a constant-subspace inclusion after twisting by O(-2), and the middle map is a square quadratic matrix whose determinant cuts out Omega_5 with multiplicity one at each point. This is a necessary factorization, not an exclusion of that alternative.

## 1. Reduction to a quadratic bundle map

The internal-degree-four Koszul complex is

Lambda^4 T tensor O -> (T tensor Lambda^3 T) tensor O -> (E tensor Lambda^2 T) tensor O(2).

The first map is constant and injective, with image of dimension five. Its cokernel C is a constant vector space of dimension 45. The induced map is

C tensor O -> (E tensor Lambda^2 T) tensor O(2).

Every term has the same nontrivial central character, the fourth power of the central character of T. Let D be the unique five-dimensional Gamma irreducible with that character. Taking Gamma multiplicities, which is exact in characteristic zero, writes this map as identity_D tensor phi, where

phi: 9O -> 10O(2).

The fiber kernel of the displayed 45-to-50 map is precisely the Koszul homology defining u(lambda), since the already-quotiented boundary map has constant rank. Thus dim ker(phi_lambda)=u(lambda)/5. Its generic rank is

r=9-u_0/5, with 5<=r<=9.

Although a normalizer action need not be expressed by a chosen ordinary action on every multiplicity factor, its action on the original family identifies the reduced maps up to invertible source and target transformations. The determinantal ideals of phi are therefore intrinsically normalizer-invariant. Scalar choices of intertwiners for D do not change these ideals.

## 2. A determinantal divisor of degree at most eighteen

At generic rank r, at least one r-minor of phi is nonzero. Every r-minor is a section of O(2r). Their common vanishing ideal on the smooth curve P defines an effective divisor Delta. It is finite, since a nonzero minor is not identically zero, and

deg(Delta)<=2r<=18.

Its support is exactly the locus where the fiber rank falls below r. The construction in Section 1 shows that Delta is A5-invariant.

For clarity, if p is any point, Smith normal form over the discrete valuation ring O_{P,p} gives r nonzero diagonal entries t^{a_1},...,t^{a_r}, with a_i>=0, and zero remaining entries. Consequently

mult_p(Delta)=sum_i a_i,
rank(phi_p)=#{i:a_i=0}.

In particular a coefficient one in Delta means a rank drop exactly one, with no higher-order determinantal multiplicity.

## 3. The orbit restriction, without an orbit table

A finite subgroup of PGL(2) fixing a point is cyclic in characteristic zero. Indeed its tangent character is injective: a finite-order projective transformation fixing a point with derivative one is the identity. A finite subgroup of the multiplicative group is cyclic.

The element orders in A5 are 1,2,3,5. Thus point-stabilizer orders are 1,2,3,5 and orbit sizes are 60,30,20,12. There are six subgroups of order five. Each has two fixed points; two different such subgroups cannot share a fixed point, since that point's stabilizer would be cyclic and contain both. These twelve points form the unique orbit of size twelve. More explicitly, the order-ten normalizer of a subgroup of order five exchanges its two fixed points, for otherwise it would lie in a cyclic point stabilizer; conjugacy of the six subgroups then gives transitivity. Any orbit of size twelve has an order-five stabilizer and is therefore this one.

Every nonempty invariant effective divisor of degree at most eighteen must consequently be Omega_5 with coefficient one. Its coefficient cannot be two, which would already have degree twenty-four. Therefore Delta is either empty or reduced Omega_5.

If Delta is empty, rank and u are constant. Otherwise Section 2 gives rank r-1 at each point of Omega_5 and rank r elsewhere, proving the stated jump of five. If r=5, deg(Delta)<=10 rules out a nonempty Delta. This proves the alternatives.

## 4. Saturation gives an additional rigidity constraint

Let J=im(phi), a rank-r locally free sheaf on P because it is a subsheaf of a vector bundle on a smooth curve. Let I be its saturation in 10O(2). Then I/J is a torsion sheaf. The same local Smith normal form shows that its length is deg(Delta).

The sheaf J is a quotient of 9O, hence is globally generated. Its splitting summands on P1 therefore have nonnegative degree, so deg(J)>=0. The saturated sheaf I is a subbundle of 10O(2); each summand of I has degree at most two, since a line bundle of degree greater than two has no nonzero map to O(2). Hence deg(I)<=2r.

If jumps occur, these facts yield

0<=deg(J)=deg(I)-12<=2r-12.

This is a bound on the image bundle, not only on its determinant. When r=6 it forces deg(J)=0 and deg(I)=12. Global generation then gives J=6O, and the upper bound on the splitting summands of I gives I=6O(2). The quotient 9O -> J is a constant surjection. The inclusion I -> 10O(2) is a constant rank-six matrix after twist. The remaining inclusion J -> I is a square quadratic matrix, with determinant vanishing divisor Delta=Omega_5. It is generically invertible and has corank exactly one at those twelve points. The kernel sheaf of phi is the constant bundle 3O. At the twelve exceptional points, its fiber is strictly smaller than the kernel of the fiber map: the extra one-dimensional fiber kernel comes from the torsion cokernel of J -> I. Thus this constant kernel sheaf does not contradict the asserted rank jump.

For r=7,8,9, the same argument bounds deg(J) by 2,4,6 respectively. Without further representation-theoretic information these bounds do not determine splitting types or rule out jumps.

## Contribution and unresolved questions

This reduces every possible geometric variation of the remaining column Betti parameter to a single known orbit and a single adjacent jump. It also identifies the forced constant-image/saturation factorization at generic u_0=15 if a jump exists. It does not determine u_0, prove that jumps actually occur, or exclude the rank-six equality case.

The proof is authored structural mathematics requiring independent review. It is not formally checked. It makes no first-order, higher-order or algebraicity claim for a selected actual HM/source instance, and uses no selected evaluation, coefficient search or large computation.
