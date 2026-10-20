# Universal Heisenberg rank-four bound and exclusion of the cubic-phase orbit

## 1. Precise statement

Work over C. Let H be the order-125 Heisenberg group acting irreducibly on a five-dimensional space V, with central character a primitive fifth root. Let f:V^3→J be trilinear, H-equivariant, outer-symmetric and cyclic-zero. Suppose:

1. the linear span of its values has dimension at least 20;
2. for every nonzero a, the map V/Ca→J, b↦f(a,a,b), is injective.

For a nonzero u, let Q_u:Sym²(V/Cu)→J/R_u be the residual middle map, where R_u={f(u,u,v):v∈V}. Then at every eigenline of a noncentral element of H,

    rank Q_u ≥ 4.

The proof actually needs repeated-input injectivity only to exclude the repeated tensors appearing below. No operation value, coefficient, or source input is evaluated. The dimension assumption is essential to the stated argument and must not be omitted when applying it.

For the actual normalizer-equivariant operation of the standing problem, the target is the irreducible 20-dimensional N-module J3=A*⊗Sym³W. Repeated-input injectivity implies f is nonzero, so its N-stable image is all of J3. Thus assumption 1 holds by the previously established representation theorem, not by a rank evaluation.

## 2. Universal tensor quotient

Put

    T = ker(V⊗Λ²V → Λ³V),    dim T=40,
    F(a,b,c)=a⊗(b∧c)+c⊗(b∧a).

The values of F span T, and F is outer-symmetric and cyclic-zero. This is the universal Schur_(2,1) quotient, so f=q∘F for an H-equivariant linear map q:T→J. Write K=ker q. Repeated-input injectivity gives

    K ∩ {a⊗(a∧b): b∈V} = 0 for a≠0.

The center acts on T by the cube of its input character, still primitive. Every irreducible H-module of this central character has dimension five, and the clock eigenspaces of T have dimension eight. Shift identifies the five clock eigenspaces of K. Consequently

    dim K=5d,    dim(K∩T_0)=d≤4,

since rank q≥20.

Choose a standard Heisenberg eigenbasis e_i, i∈F5, with clock e_i↦ζ^i e_i and shift e_i↦e_(i+1). Let

    F_0 = span{F(x,e_0,z):x,z∈V}.

The map Sym²V→F_0 has kernel Ce_0² and hence dim F_0=14. Its repeated-input subspace has dimension four and meets K trivially. Thus

    rank Q_e0 = 10 − dim(K∩F_0).

It remains to bound the latter dimension by six.

## 3. Five weight spaces in one eight-dimensional space

Let T_0 be the clock-weight-zero space. It has the direct decomposition

    T_0 = R ⊕ D,
    R = span(r_1,r_2,r_3,r_4),
    r_a = e_a⊗(e_a∧e_(-2a)).

The remaining summand D is the sum of the two two-dimensional distinct-index blocks belonging to the triples {0,1,4} and {0,2,3}. These are the only three-element subsets of F5 with sum zero. Set

    t_1=F(e_0,e_3,e_2),   t_4=F(e_3,e_2,e_0),
    t_2=F(e_0,e_1,e_4),   t_3=F(e_1,e_4,e_0).

The first two form a basis of the {0,2,3} block, the latter two of the {0,1,4} block. In particular all four t_j are independent.

Let L=K∩T_0, so dim L≤4. By repeated-input injectivity, L contains none of the four lines Cr_a.

The weight-j component of F_0 is shifted into T_0 by X^(3j): because a degree-three tensor's weight increases by 3k under X^k, and j+3(3j)=0 mod 5. Since K is shift-invariant, this preserves its intersection dimension with K. The resulting five subspaces are

    H_0 = span(t_1+t_4, t_2+t_3),
    H_1 = span(r_1,r_3,t_1),
    H_2 = span(r_2,r_1,t_2),
    H_3 = span(r_3,r_4,t_3),
    H_4 = span(r_4,r_2,t_4).

To verify these without any operation evaluation, the weight-j quadratic monomials for j≠0 are e_0e_j, e_(j/2)², and the remaining distinct nonzero pair with sum j. Their universal tensors shift respectively to nonzero multiples of r_(3j), r_j, and t_j. The weight-zero monomials are e_1e_4 and e_2e_3; their tensors lie in the two distinct-index blocks. The cyclic identity gives the displayed H_0 (individual signs do not affect its span).

Therefore

    dim(K∩F_0) = Σ_(j=0)^4 dim(L∩H_j).

## 4. The four-cycle intersection lemma

The following elementary argument is independent of representation theory. Keep R,D,H_j as above, and suppose dim L≤4 and L∩Cr_i=0 for every i. Put S_j=L∩H_j for j=1,2,3,4, and s=Σ dim S_j.

The four planes H_j∩R are the edges of a four-cycle on the coordinate lines r_1,r_2,r_4,r_3. Each S_j∩R has dimension at most one; otherwise it would be the entire edge plane and contain a forbidden coordinate line. Any nonzero vector on such a one-dimensional intersection has both endpoint coefficients nonzero.

Consider the addition map ⊕S_j→L. In a relation Σv_j=0, the t_j-coordinates vanish separately because t_1,…,t_4 are independent. Hence each v_j lies in S_j∩R. Any three nonzero edge vectors are independent: a proper subgraph of the cycle is a forest, and a leaf coordinate occurs in exactly one edge vector, forcing that coefficient to vanish; remove that edge and repeat. Thus the space of relations has dimension at most one. It follows that

    s≤dim L+1≤5.

If s≤4, adding dim(L∩H_0)≤2 proves the desired bound six.

If s=5, the addition map has a nonzero relation. It uses all four edges, and any three of their vectors are independent. Consequently dim(L∩R)≥3. Since dim L≤4, its image in D under projection along R has dimension at most one. But H_0⊂D, so dim(L∩H_0)≤1. Again the total is at most six.

This proves dim(K∩F_0)≤6 and therefore rank Q_e0≥4. For any eigenline of a noncentral H-element, choose that element as clock, multiply it by a central scalar so its chosen eigenvalue is one, and choose a complementary Heisenberg generator as shift. This gives precisely the standard eigenbasis used above, proving the theorem.

## 5. Apply to the alternative Heisenberg subgroup

Retain the original normalizer coordinates X e_j=e_(j+1), Z e_j=ζ^j e_j, D e_j=ζ^(j²)e_j. Set

    g=X Z³ D³.

Then g^5=Z^5=1 and Zg=ζ gZ. Thus the linear subgroup generated by g and Z is an order-125 Heisenberg subgroup H′ contained in the original linear normalizer. More explicitly, the 125 normal forms ζ^c g^a Z^b are distinct: if such a form is the identity, its permutation part forces a=0, and its diagonal entries then force b=c=0. It acts irreducibly on V by the finite Stone–von Neumann argument (or directly: g is a five-cycle monomial matrix and its five eigenlines are transitively permuted by Z).

The cubic-phase representative of the unique eligible 600-point orbit is a g-eigenline, as already established in ../order-five-rank-three-classification/PROOF.md. The actual f is H′-equivariant, its image has dimension 20 by irreducibility of its actual N-target, and global repeated-input injectivity is a standing hypothesis. The theorem therefore gives residual rank at least four at that line. N-equivariance transports the result to its entire 600-point orbit M:

    M ∩ Z3 = ∅.

No value of f, no chosen source-operation coefficient, and no rank matrix at a source input was computed. The universal Schur tensor calculation identifies subspaces by group characters and symbolic tensor identities only.

Combining this with the audited six-support synthesis, the remaining nonempty reduced support cardinalities are restricted to

    1000, 3000, 4000.

The empty alternative remains possible. This is a necessary list, not an existence statement. The proof gives no multiplicity claim and does not exclude the remaining order-three or free orbits.

## 6. Why the earlier stabilizer shortcut was insufficient

The alternative Heisenberg subgroup alone does not enlarge the cubic-phase point's stabilizer in the original normalizer: it remains C5. The argument above instead uses the coupling of all five clock eigenspaces by the shift and the global 20-dimensional image. Neither a pointwise disjoint-character claim nor an imported order-100 stabilizer is used.

## Dependencies and verification

- ../../cubic-loci/canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md, Sections 2–3: universal Schur symmetry and actual 20-dimensional irreducible target.
- ../../full-hm-image-symmetry/PROOF.md: irreducibility of the relevant 20-dimensional target and its dual.
- rank-two-structural-countermodel/PROOF.md, Sections 1–2: the universal tensor model and repeated-tensor interpretation (also rederived here).
- ../order-five-rank-three-classification/PROOF.md: cubic-phase eigenline and unique 600-point orbit.
- rank-three-six-support-alternatives/PROOF.md: current six-cardinality synthesis.

An independent audit has verified the weight decomposition, four-cycle lemma, subgroup H′, and use of the actual target image dimension. See AUDIT.md for its complete report.
