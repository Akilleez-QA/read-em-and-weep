Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Heisenberg Hilbert congruences for proper-support sheaves

## Result

In the established rank-nine branch, let G=im(b), let F be its saturation in J tensor O, and put T=F/G. Write a=degree([T]_2). Then

    a belongs to {25,30,35}.

More generally, every H5-equivariant coherent sheaf M on P(V)=P4 whose support has dimension at most three satisfies

    chi(P4,M(m)) is divisible by 5 for every integer m.

All coefficients of its Hilbert polynomial in the integral binomial basis are divisible by five. Its top-dimensional cycle degree is also divisible by five. The general statement does not require a uniform central character, purity, reduced support, local freeness, or a Cohen--Macaulay condition.

## 1. Conventions and representation lemma

Use the established defining action of the order-125 Heisenberg group H5 on V. Write c for its central generator, acting on V by a primitive fifth root zeta. On P(V), c acts trivially on the base. The standard linearization of O(-1) has central character zeta, so O(m) has central character zeta^(-m).

Every finite-dimensional complex H5-module on which c acts by a nontrivial scalar zeta^j has dimension divisible by five. Here is a direct proof. Choose standard generators sigma,tau with sigma tau sigma^(-1)=c tau. The operator tau is diagonalizable, since it has finite order. Conjugation by sigma cycles its eigenspaces through multiplication of the eigenvalues by zeta^j (or its inverse, depending on direction). Since j is nonzero modulo five, every such cycle has length five. Its eigenspaces have equal dimension. Summing over cycles proves the claim.

This uses only the abstract group relation and evaluates no operation or matrix instance.

## 2. Uniform central weight

First suppose c acts on M by zeta^w. Then it acts on M(m), and hence on every cohomology group H^i(P4,M(m)), by zeta^(w-m). Consequently

    chi(M(m)) = 0 modulo 5 whenever m is not w modulo 5.       (1)

Let P(m)=chi(M(m)) be the Euler characteristic polynomial. Its degree is at most three because the support dimension is at most three. As an integer-valued polynomial, P has an integral binomial expansion

    P(m)=b0+b1 binom(m,1)+b2 binom(m,2)+b3 binom(m,3),

with integers b_i; omit terms above its degree. In particular 6P(m) belongs to Z[m]. Reduce this polynomial modulo five. By (1), its reduction vanishes on the four distinct residue classes other than w. A polynomial of degree at most three over F5 with four roots is identically zero. Thus every coefficient of 6P is divisible by five.

Since 6 is invertible modulo five, P(m) is divisible by five for every integer m, including m=w modulo five. Taking finite differences at m=0 gives

    b_i = Delta^i P(0) = 0 modulo 5

for every i. This proves both asserted Hilbert-polynomial congruences.

Equivalently, one may use the eventual Hilbert polynomial and sufficiently large integers in each residue class to obtain the same polynomial identity. No vanishing theorem for individual cohomology groups is needed.

## 3. Arbitrary central action

For a general H5-equivariant coherent sheaf M, the center acts O-linear because it acts trivially on P(V). Its finite-order action splits M into coherent eigensheaves using the usual idempotents

    M = direct sum over w in Z/5 of M_w.

Centrality makes each summand H5-equivariant. Each has support dimension at most three and uniform central weight w. Apply Section 2 to each summand and add. This establishes the result without a uniform-weight hypothesis.

If the support dimension is r, its top-dimensional cycle has degree delta and the leading Hilbert coefficient is delta/r!. In the integral binomial expansion this means b_r=delta. Hence 5 divides delta. The zero sheaf is harmless; all these assertions are then zero identities.

The proper-support hypothesis matters: a degree-four polynomial can vanish at four residues without vanishing identically modulo five. For example O on P4 is equivariant and chi(O)=1.

## 4. Application to the rank-nine saturation defect

The rank-nine kernel theorem and addendum establish

    0 -> O(-3) direct-sum O(-8) -> O(-1)^15 -> G -> 0,
    T=F/G is supported in codimension at least two,
    [T]_2 = a h^2.

The two-sided positivity argument in ../rank-nine-defect-two-sided/PROOF.md sharpens the necessary interval to

    22 <= a <= 36.                                          (2)

All these constructions are equivariant: b is equivariant, its image G is equivariant, and the uniquely defined saturation F is preserved by the group action. Thus T is H5-equivariant. Moreover it has uniform central weight three, since it is a subquotient of J tensor O and c acts on J by zeta^3. This convention and character are explicitly recorded in Section 2 of ../rank-four-global-determinant/PROOF.md. Therefore c acts on T(m) by zeta^(3-m).

The general lemma applies since dim supp(T)<=2. Its top-dimensional cycle degree is a, and (2) ensures this cycle is nonzero, so

    5 divides a.

Combining this with (2) proves precisely

    a in {25,30,35}.

For reference, the established second Chern identities then reduce to the three ordered possibilities

    (c2(F*),c2(R)) = (12,4), (7,9), or (2,14),

using c2(F*)=37-a and c2(R)=a-21.

This is a necessary condition for rank nine, not its exclusion, realization, or an identification of the defect support.

## Evidence boundary

The argument reads only existing local proof texts and uses universal group representations, coherent-sheaf cohomology, and Hilbert polynomials. No actual HM source, operation matrix, product, selected input, rank instance, polynomial instance, jet, or residue is evaluated. Only this local proof file is written.
