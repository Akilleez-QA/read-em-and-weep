# Exterior shadows sharpen the coupled column-cycle bounds

## Dependencies and scope

Work over characteristic zero with S=Sym(T), dim T=5, dim U=10, dim G=2, P=P(G*), and the moving quadratic column U tensor S(-2) tensor O(-1) -> S tensor O. Let K denote its Koszul complex, and Z_(p,d) its cycle sheaf in homological degree p and S-degree d.

The only actual-family inputs used below are:

1. The syzygy bundle L=Z_(1,3) is 10O(-2) direct sum 5O(-6), from PR511 at commit 55bc80b2cb660edd741c93747df7304ee51a061e, research/hm/binary-symmetric-propagation/PROOF.md.
2. The actual complementary generalized Eagon--Northcott duality, from PR507 at 87c9b317bd4b1116e63212a6d7ec2730486b2032 and PR508 at a59d3dbfdad8b5516cd17c91890b669f2567bdb7, identifies the residual dimensions with x=h^0(Z_(3,7)(8)) and y=h^0(Z_(2,5)(8)). The direct low-degree hypercohomology argument proving these identities is in PR549 at commit eaebbcad2b1cf0ad1e83e12bb33c380bae00a0fb, research/hm/column-koszul-bridge/PROOF.md (reviewed local proof SHA256 7b388da8bffd768a79e74eb73c7d1c89669f04a0cdcbd256d7282db556b76c3c).
3. That same bridge establishes E:=Z_(2,5) -> 100O(-3) direct sum 50O(-7). In particular every splitting summand O(b) of E has b<=-3.

These inputs gave y<=700, x<=2475 and 3x<=25y. The new argument uses the alternating exterior shadow, not merely the ambient tensor injection. It proves

             y<=315,       x<=610,       9x<=20y.

All are necessary conditions, not determinations of x or y. No selected actual coefficients, matrices, ranks, or numerical evaluations are used.

## 1. Linear exterior-shadow inequality

Let B and U be finite-dimensional vector spaces, with dim U=N. Suppose W_p is a subspace of B tensor Lambda^p U and W_(p-1) is a subspace of B tensor Lambda^(p-1) U containing every contraction i_f(W_p), f in U*. Then

             p dim W_p <= (N-p+1) dim W_(p-1).

Proof. Choose ordered bases of B and U. Order the basis vectors b_a tensor u_I first by a and then lexicographically by the indicator vector of I. Use the same convention in each exterior degree. If two sets of the same size both contain j, deleting j preserves their relative order. Consequently, if a vector w has leading monomial b_a tensor u_I and j belongs to I, contraction by u_j* has leading monomial, up to nonzero sign, b_a tensor u_(I minus j): all larger terms were absent, smaller terms containing j remain smaller, and terms not containing j vanish.

Let A_p be the set of possible leading monomials of W_p, so |A_p|=dim W_p by row reduction. Let partial A_p be the colored lower shadow, consisting of all (a,I minus j) for (a,I) in A_p and j in I. The preceding paragraph shows partial A_p is contained in the leading-monomial set of W_(p-1).

Count edges (a,I)->(a,I minus j). There are p|A_p| edges. Any lower monomial has at most N-p+1 preimages, one for each element not already in its set. Hence

p dim W_p = p|A_p| <= (N-p+1)|partial A_p| <= (N-p+1) dim W_(p-1),

as asserted. This argument is a finite-dimensional structural inequality, not a computation of any actual matrix. It works over any field.

Iterating, for contraction-closed spaces W_1,...,W_p,

             dim W_p / binom(N,p) <= dim W_1 / N.

## 2. Correct fixed-coefficient spaces for the column family

For an integer n>=0 define

             W_p(n)=H^0(P,Z_(p,2p+1)(n+p)).

The ambient Koszul term becomes

K_(p,2p+1)(n+p) = T tensor Lambda^p U tensor O(n),

so W_p(n) is naturally a subspace of B_n tensor Lambda^p U, where B_n=T tensor Sym^n G. Contraction in U changes p to p-1 but leaves B_n unchanged. Since contraction anticommutes with the Koszul differential, it maps W_p(n) into W_(p-1)(n). This fixed coefficient degree is essential: using the same line-bundle twist at consecutive p would not give the required common B_n.

In particular W_1(n)=H^0(L(n+1)), and the actual splitting gives

             dim W_1(n)=10 max(n,0)+5 max(n-4,0).

For N=10, the exterior-shadow inequality now yields

             2 dim W_2(n) <= 9 dim W_1(n),
             3 dim W_3(n) <= 8 dim W_2(n).

## 3. The two independent upper bounds

The defect y is dim W_2(6). Here dim W_1(6)=60+10=70. Therefore

             2y <= 9*70,   hence y<=315.

The defect x is dim W_3(5). Here dim W_1(5)=50+5=55. Iterating the normalized shadow inequality gives

             x <= [binom(10,3)/10]*55 =12*55=660.

Equivalently, 3x<=8 dim W_2(5) and 2 dim W_2(5)<=9*55 yield x<=660.

The colored vertex shadow sharpens this last bound further. Apply the proof of Section 1 repeatedly, and for each basis color a of B_5 let r_a be the number of degree-one leading monomials of W_1(5) of that color. Then 0<=r_a<=10 and sum_a r_a=55. Every degree-three leading monomial of W_3(5) has all three of its vertices among those r_a vertices, because all iterated contractions remain in W_1(5). Thus

             x <= sum_a binom(r_a,3).

The discrete function f(r)=binom(r,3), with f(0)=f(1)=f(2)=0, has nondecreasing first differences f(r+1)-f(r)=binom(r,2). Hence transferring one unit from a smaller positive r to a larger r<10 never decreases the sum. Iteration concentrates the total 55 in five entries equal to ten and one entry equal to five. Consequently

             x <= 5 binom(10,3)+binom(5,3)=610.

This argument uses only leading-monomial dimensions, not a splitting of the actual cycle space into coefficient colors. The extremal monomial pattern is an upper-bound device, not an asserted actual family.


## 4. The sharpened coupled inequality

Since W_2(5)=H^0(E(7)), the degree-three shadow inequality gives

             3x <= 8 h^0(E(7)).

Write E as a sum of O(b_j) on P^1. Input 3 implies b_j<=-3. For each such b,

             h^0(O(b+7)) <= (5/6) h^0(O(b+8)).

Indeed these dimensions are max(b+8,0) and max(b+9,0), and the latter argument is at most six. Summing proves h^0(E(7))<=(5/6)y. Thus

             3x <= (20/3)y,   or 9x<=20y.

This improves the old tensor-contraction coefficient by the factor 4/15. It also retains y=0 => x=0, without proving the converse.

## 5. Open dependency and verification boundary

The exact alternating cycle spaces remain to be determined. The new bounds rule out larger residual defects without assuming relative homology is flat, a relative perfect pairing, generic perfection, or numerical ranks at a selected column. They do not establish a geometric lifting or algebraicity statement.

The exterior-shadow lemma and its substitutions are mathematically reviewed in the accompanying review files, conditional on the pinned actual-family inputs. No formal verification is claimed. This is a column-cycle statement, not a conclusion about the residual quadratic or full adjoint map.

## Public dependency links

- Actual cycle interpretations and splitting-degree bound, PR549:
https://github.com/Akilleez-QA/read-em-and-weep/blob/eaebbcad2b1cf0ad1e83e12bb33c380bae00a0fb/research/hm/column-koszul-bridge/PROOF.md
- Actual syzygy bundle, PR511:
https://github.com/Akilleez-QA/read-em-and-weep/blob/55bc80b2cb660edd741c93747df7304ee51a061e/research/hm/binary-symmetric-propagation/PROOF.md
- Complementary generalized EN duality, PR507 and PR508:
https://github.com/Akilleez-QA/read-em-and-weep/blob/87c9b317bd4b1116e63212a6d7ec2730486b2032/research/hm/generalized-en-defects/PROOF.md
https://github.com/Akilleez-QA/read-em-and-weep/blob/a59d3dbfdad8b5516cd17c91890b669f2567bdb7/research/hm/middle-defect-duality/PROOF.md
