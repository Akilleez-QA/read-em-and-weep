# Independent audit: universal Heisenberg rank-four bound

## Verdict

The argument in `PROOF.md` is valid. In particular, the alternative Heisenberg subgroup does imply residual rank at least four at the cubic-phase orbit, using the actual operation's twenty-dimensional image and repeated-input injectivity. The conclusion does not depend on evaluating the actual operation or a residual matrix.

The theorem and its application are approved. During the audit, the statement was clarified to say explicitly that `f:V^3→J` is **trilinear**, as required by the universal quotient argument and already true of the standing operation. The final proof contains this clarification and the subgroup normal-form justification.

This audit checked the complete proof and read its cited module, normalizer, order-five-orbit, and six-support synthesis proofs. It accepts their previously established standing hypotheses; it does not replace their geometric or cohomological foundations with new computations.

## 1. Universal quotient and residual rank formula

For a trilinear operation, outer symmetry and the cyclic-zero identity have the stated forty-dimensional universal quotient. One can verify this without importing any source-operation data. Outer symmetry first gives the seventy-five-dimensional space `Sym²V⊗V`; the symmetric-cube relations remove `Sym³V`, of dimension thirty-five. The universal tensor

    F(a,b,c)=a⊗(b∧c)+c⊗(b∧a)

takes values in `T=ker(V⊗Λ²V→Λ³V)`, whose dimension is `50−10=40`. It spans T: every repeated-index block is obtained from `F(a,a,b)=a⊗(a∧b)`, and any two middle-slot choices span each two-dimensional distinct-index block. Thus the induced forty-dimensional quotient map is an isomorphism, proving the required factorization `f=q∘F`.

Repeated-input injectivity is exactly sufficient to give

    K∩{a⊗(a∧b):b∈V}=0,  K=ker q,

for every nonzero a. No uniform lower bound on q outside these subspaces is silently assumed.

For fixed `e0`, the fifteen outer-symmetric quadratic monomials have exactly one universal relation, `e0²`. The nonzero weight-zero part has dimension two, and each other weight has dimension three. Therefore `dim F0=14`. Its repeated subspace has dimension four, and q is injective there. The residual map is the quotient of `q(F0)` by this four-dimensional image, so

    rank Q_e0=14−dim(K∩F0)−4
              =10−dim(K∩F0).

This also verifies that the residual map on `Sym²(V/Ce0)` is well-defined: changing an outer input by a multiple of e0 changes its value by the repeated image.

## 2. Dimension assumption and weight identifications

The image of q is precisely the linear span of the values of f. Hence the hypothesis that this span has dimension at least twenty gives `dim K≤20`.

With `Z ei=ζ^i ei` and `X ei=e_(i+1)`, a degree-three tensor of clock weight j acquires weight `j+3k` under `X^k`. Therefore the correct transfer to weight zero is indeed

    k=−2j=3j modulo 5.

Since K is invariant under both generators, its five weight spaces have equal dimension. Consequently `dim K=5d` and `dim L=d≤4` for `L=K∩T0`. This argument uses the dimension of the actual image, not merely the dimension of an ambient target. The proof correctly distinguishes those issues.

The four repeated vectors `r_a=e_a⊗(e_a∧e_(-2a))`, for nonzero a, are nonzero: the repeated and third indices are distinct. Each forbidden line `Cr_a` is therefore excluded by the stipulated injectivity.

The only distinct-index weight-zero triples are `{0,1,4}` and `{0,2,3}`, giving the asserted direct decomposition `T0=R⊕D`. The displayed t-vectors are independent, two in each of these disjoint blocks.

The five transferred subspaces are exactly the displayed H_j. Specifically, in nonzero weight j, the pair `(0,j)` transfers to `r_(3j)`, the diagonal pair `(3j,3j)` transfers to `−2r_j`, and the remaining pair transfers to t_j. Outer symmetry makes the displayed orders for t3 and t4 immaterial. For each distinct triple, the sum of its three middle-slot choices is zero, giving

    H0=span(t1+t4,t2+t3).

Thus the identity

    dim(K∩F0)=Σ dim(L∩H_j)

is justified weight by weight.

## 3. Independent check of the four-cycle lemma

Every `S_j∩R`, where `S_j=L∩H_j` and `j≠0`, has dimension at most one. If it were the entire two-dimensional edge plane it would contain a forbidden coordinate line. A nonzero vector in a permitted edge line has both of its endpoint coefficients nonzero.

The t-coordinates in a relation among the S_j vanish separately. Relations therefore reduce to the four permitted edge lines of the cycle. Every proper subset of the four edges is a forest, and the leaf-coordinate elimination argument proves independence of its edge vectors. In particular, any three nonzero edge vectors are independent. The space of relations among all four therefore has dimension at most one.

This proves `s=Σ_(j=1)^4 dim S_j≤dim L+1≤5`. If `s≤4`, the two-dimensional bound for H0 gives the required total at most six. If `s=5`, a relation exists and uses all four edges; their span has dimension three and lies in `L∩R`. The projection of L to D then has dimension at most one. Since `H0⊂D`, its intersection with L has dimension at most one, again giving total at most six.

The argument remains valid when `dim L<4`; no equality assumption on the image dimension is needed for the abstract theorem. It also uses only exclusion of the four indicated repeated lines after the four-dimensional repeated-image calculation, not an unstated stronger transversality condition.

Finally, any eigenline of a noncentral Heisenberg element can be made the `e0` line of a standard clock-and-shift basis: adjust its clock eigenvalue by a central scalar and choose a complementary generator with primitive commutator. This does not require K to be invariant under the normalizer of H.

## 4. The alternative subgroup H′

Let `g=X Z³ D³`, with `D ei=ζ^(i²)ei`. On the chosen basis,

    g ej=ζ^(3j+3j²)e_(j+1).

It follows formally that `Zg=ζgZ`. The product of the five cyclic multipliers is one because

    Σ_(j∈F5)(3j+3j²)=0 in F5,

so `g^5=1`; also `Z^5=1`. The commutator supplies the primitive central scalar `ζI`.

These relations give normal forms `ζ^c g^a Z^b` with a,b,c in F5. They are all distinct: the permutation part determines a, and then the diagonal clock entries determine b and c. Thus H′ has order exactly 125 and is an ordinary exponent-five Heisenberg group, not merely a projective group of order 25.

Its action on V is irreducible. Any Z-invariant subspace is spanned by a subset of the five distinct coordinate eigenlines; g permutes those lines transitively. Hence a nonzero subspace invariant under both is all of V.

The matrices X, Z and D are in the original linear normalizer in the standing conventions, so g and H′ are also in it. In particular D has determinant one, since `Σ j²=0` modulo five. Restriction of the actual N-equivariant operation therefore gives the H′-equivariance required by the theorem. H′ need not be conjugate to the original normal Heisenberg subgroup inside N, and no such claim is used.

The preceding order-five classification establishes that the cubic-phase representative is a g-eigenline and belongs to the unique eligible 600-point orbit M. The new theorem applies to this eigenline directly. It does not replace its genuine order-five point stabilizer by a larger one.

## 5. Actual target and image dimension

The target is the actual cohomology module J3, not a freely chosen twenty-dimensional quotient. The cited module proof gives

    J3=J2*≅A*⊗Sym³W.

The independent full-normalizer result establishes that J2 is an irreducible twenty-dimensional N-module; its dual J3 is therefore irreducible as well. This implication does not require irreducibility of J3 after restriction to H′.

Repeated-input injectivity supplies a nonzero value for every nonzero a and any b independent of a, so the actual f is not zero. Its linear image is N-stable by equivariance. Irreducibility of J3 then forces that image to equal J3. Consequently `rank q=20` in the actual application, and `dim L=4`. This establishes the dimension hypothesis structurally, with no evaluation of an operation value or source rank.

## 6. Consequences and scope

The theorem gives residual rank at least four on the cubic-phase representative. N-equivariance gives the same lower bound on all of M, so `M∩Z3=∅`.

Removing this orbit from the audited six-support synthesis leaves exactly the necessary nonempty cardinality list

    1000, 3000, 4000.

The empty alternative is retained. Neither existence, local multiplicities, nor exclusion of the order-three and free-orbit alternatives follows from this proof. Its scope is stated correctly.

No actual operation coefficients, Massey values, source evaluations, residual matrices, or source-rank tests were used in this audit. The work consisted of proof reading, universal tensor and representation arguments, elementary finite-group identities, and this local audit document.
