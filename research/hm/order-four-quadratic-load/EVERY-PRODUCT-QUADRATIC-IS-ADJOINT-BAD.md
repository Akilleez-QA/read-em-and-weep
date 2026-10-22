# Every product quadratic is full-adjoint bad

## Checked input and scope

Let F be the normalized Horrocks–Mumford bundle on P4, with determinant O(−1), and B=End0(F). The established ambient vanishings are H0(B(2))=H0(B(4))=0, so for every nonzero quadric equation q,

H0(B_Q(4)) = ker[q:H1(B(2))→H1(B(4))].

The two cohomology spaces have dimension85. Here Q=V(q) is allowed to be reducible or nonreduced; restriction remains exact because B is locally free and q is a nonzerodivisor on P4.

The verified hyperplane-section theorem gives

H0(H,F_H(2))≠0 for EVERY hyperplane H.

The source roles are separate. Banica–Manolache, INCREST preprint104 (1981), Section1, Lemma1, printed pp.3–4, proves this section nonvanishing for a stable rank-two bundle on P3 with c1=−1 and c2=4. Boralevi, The Horrocks–Mumford bundle restricted to planes, arXiv:math/0602002, printed p.6, supplies stability of every HM hyperplane restriction; it is not cited as independently proving the section nonvanishing. Their combination applies to F_H. The exact lemma and proof, including its identified Gruson–Peskine dependency, were previously checked and recorded in PR543's MIDDLE-LINEAR-DETERMINANT-ZERO.md; PRODUCT-PRIMARY-BOUNDARY.md records the resulting scope. The present note uses that checked dependency and does not claim a new independent proof of the Banica–Manolache lemma.
https://imar.ro/~increst/1981/104_1981.pdf
https://arxiv.org/pdf/math/0602002

The result below concerns full adjoint multiplication. It does not contradict generic product injection on the primary submodule or a good residual quotient.

## 1. A forced nilpotent adjoint section on every hyperplane

For a rank-two bundle G in characteristic zero there is a canonical identification

End0(G) ≅ Sym²(G)⊗det(G)^−1.

For G=F_H, twisting by three gives

B_H(3) ≅ Sym²(F_H)(4).

Choose any nonzero section s of F_H(2). Its symmetric square is nonzero at the generic point of the integral hyperplane, and therefore defines a nonzero global section

alpha_s∈H0(B_H(3)).

Explicitly its bundle map is the composition G→det(G)(2)→G(3), where the first arrow is v↦s∧v and the second multiplies by s. Its square is zero, since s∧s=0; it is trace-free. No assumption about the zero locus of s is required.

Consequently

a_H:=h0(B_H(3))≥1

for every hyperplane. More precisely, multiplication by a fixed nonzero s injects H0(F_H(2)) into H0(Sym²(F_H)(4)), so a_H≥h0(F_H(2)).

This disproves the proposed prerequisite H0(B_H(3))=0 for injective full-adjoint plane traces. Unlike primary traces, the full-adjoint restriction always has a nonzero kernel.

## 2. Two independent supported sections on a reduced product

Let q=ell1 ell2 with distinct hyperplanes H1,H2 and P=H1∩H2. Their gluing sequence is

0→B_Q(4)→B_H1(4)⊕B_H2(4)→B_P(4)→0.

For every alpha∈H0(B_H1(3)), multiplication by the nonzero linear form ell2|H1 gives a section ell2 alpha of B_H1(4) vanishing on P. Thus (ell2 alpha,0) glues to a global section on Q. The analogous sections (0,ell1 beta) from H2 have disjoint component support and are linearly independent from the first family. Multiplication by either nonzero equation on its integral hyperplane is injective. Hence

h0(B_Q(4))≥a_H1+a_H2≥2.

Equivalently every reduced product quadratic gives a full eighty-five-by-eighty-five multiplication map of corank at least two.

## 3. Squares and the full rank-at-most-two locus

For Q=2H the exact sequence

0→B_H(3)→B_(2H)(4)→B_H(4)→0

already yields a nonzero full-adjoint kernel. The stronger corank-at-least-two bound follows from specialization: reduced products are dense in the irreducible variety of symmetric quadrics of rank at most two, and the corank-at-least-two locus of the actual multiplication matrix is closed. Thus

corank[q:H1(B(2))→H1(B(4))]≥2

for EVERY nonzero quadric q of rank at most two, squares included.

No statement about all singular quadrics of ranks three or four follows. Products form a proper eight-dimensional locus in the fourteen-dimensional projective space of quadrics. Failure there does not contradict possible generic invertibility on smooth quadrics.

## 4. Exact correction to a product-plane strategy

If T_i denotes the image of H0(B_Hi(4)) in H0(B_P(4)), the gluing sequence gives

0→H0(B_H1(3))⊕H0(B_H2(3))→H0(B_Q(4))→T_1∩T_2→0.

Therefore even complementary trace images cannot make the product map invertible: the two supported nilpotent families survive independently of their intersection.

In particular, under the additional hypothesis that ell:H1(B(3))→H1(B(4)) is onto, h0(B_H(4))=15 but its plane trace image has dimension15−a_H≤14, NOT15. A proposed reduction to two complementary fifteen-dimensional planes inside H0(B_P(4)) is invalid before any transversality question is posed.

The same observation forces the lower linear multiplication ell:H1(B(2))→H1(B(3)) to have nonzero kernel for every ell. Its generic injectivity cannot be an available premise.

## 5. Determinant consequence

Let D(q) be the degree85 determinant polynomial of full quadratic multiplication, without assuming it is nonzero. On the rank-at-most-two locus, not only D but every first derivative of D vanishes: at a matrix of corank at least two, every eighty-four-by-eighty-four cofactor is zero, and differentiation of the determinant along any quadratic direction is a linear combination of those cofactors.

Thus any eventual nonzero full determinant hypersurface is singular along the entire rank-at-most-two quadric locus. Equivalently its vanishing order at the generic smooth point of that locus is at least two. This is a necessary algebraic constraint, not a proof of an additional global factor or of identical vanishing.

## 6. Comparison with the earlier Segre failure family

PR543's PRIMARY-INJECTION-AND-FAILURE.md, Sections3–4, had already proved corank at least four on the representation-theoretic Segre variety Sigma=P(A0)×P(U′) inside P(S2), using S2=A0⊗U′ with dimensions5 and3. This has dimension six. It is not the ordinary locus of rank-at-most-two quadratic forms, which has dimension eight. The new family is therefore not a weaker restatement of that earlier bound.

In fact every point of the old Sigma is primary-bad, whereas GENERIC-PRODUCT-PRIMARY-INJECTION.md proves that a general ordinary product is primary-good. Thus a general point of the new family lies outside the old one. We make no assertion about their full intersection.

## 7. A sharper section-dependent bound and the actual lift boundary

Put b_H=h0(F_H(2)). The multiplication pairing of global sections of F_H(2) into Sym²(F_H)(4) has no zero divisors: at the generic point it is multiplication of two nonzero degree-one elements of a symmetric algebra over the function field, which is a polynomial domain. The elementary Hopf lemma therefore gives

a_H=h0(B_H(3))≥2b_H−1.

For clarity, the lemma follows because the projectivized kernel of a bilinear map without zero divisors misses the Segre P^(b_H−1)×P^(b_H−1); the projective dimension inequality forces image dimension at least2b_H−1. Consequently, for distinct hyperplanes,

corank(ell1 ell2)≥2b_H1+2b_H2−2.

The established generic primary value is b_H∈{1,2}. If the generic value is two, the generic product corank is at least six and closedness gives corank at least six on the entire rank-at-most-two locus. If it is one, the unconditional bound here remains two. No exact value of b_H is asserted.

Finally, both actual quadratic flanks are good on a general product. The primary assertion is the published generic-product theorem. Residual surjectivity holds at a general square by UNIQUE-CUBIC-SQUARE-JET-INJECTIVITY.md, hence its pullback to the irreducible parameter space of pairs of linear forms is a nonempty open; it therefore holds at a general product too. Intersecting these two opens is legitimate.

On this generic product open, the actual rank-twenty snake boundary delta has kernel equal to the full adjoint kernel. Thus its rank is at most eighteen, despite both flanks being good. If the generic b_H is two, its rank is at most fourteen. This is an actual compatibility obstruction to treating the lift boundary as a free generic twenty-by-twenty map on products; it does not bound its rank at general smooth quadrics.

## Boundary and provenance

The new deduction closes the proposed full-adjoint product-quadratic escape route negatively. It leaves the smooth-quadric rank-twenty boundary and the rank-twenty-five conductor-kernel splitting unresolved. Current PR1 and the existing primary/residual product notes were read first. No chosen coefficients, rank sample, experiment, or external post was used.
