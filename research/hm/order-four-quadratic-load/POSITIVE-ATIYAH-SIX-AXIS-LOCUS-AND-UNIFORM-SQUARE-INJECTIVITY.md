# The six-axis locus and uniform square-direction Atiyah injectivity

## Conclusion

The actual residue-surjectivity theorem identifies the map

    K_a:D5 -> H1(B_Q(2))_+,  h |-> h At_F(D_a)|_Q

with h |-> (1 tensor ad_a)j(h), through an invertible residue pairing, where j:D5->V tensor A is the unique nonzero equivariant embedding and V tensor A=P4+D5.

For every nonzero a, K_a has rank5 except on the six projective C5 axes in P(A), where it has rank4. Those six points are reduced and are disjoint from the discriminant conic. In particular K_(ell^2) is injective for EVERY nonzero square direction ell^2.

This is a geometric rank proof, not an evaluation of an actual HM map. It does not give nonvanishing of the higher secondary operation or improve the original four-or-five section conclusion.

## 1. Reduction to a universal linear bundle map

Every nonzero element a of sl2 has one-dimensional centralizer C a. Hence

    ker K_a = j(D5) intersect (V tensor C a).

Let pi:V tensor A->P4 be the nonzero equivariant projection. The intersection is the kernel of pi(- tensor a). Thus the exceptional directions are the degeneracy locus of

    M:V tensor O_{P(A)}(-1) -> P4 tensor O_{P(A)}.       (1)

The representation decomposition makes this map nonzero, without evaluating any coefficients.

## 2. Generic injectivity without a matrix test

Suppose (1) has generic rank2. Its kernel is a saturated rank-one reflexive sheaf on the smooth plane, hence O(-d). The injection into V O(-1) forces d>=1. Choose any two independent rows over the function field; their cross-product is a nonzero homogeneous quadratic kernel vector. It defines a nonzero section of the kernel twisted by3, so d<=3.

The kernel has an equivariant line-bundle linearization. The binary icosahedral group has no nontrivial characters, so its injection gives a nonzero invariant in

    V tensor Sym^(d-1)(A).

This is impossible: Sym^0 A=1, Sym^1 A=A, and Sym^2 A=1+D5, none containing V.

Generic rank1 is also impossible. A linear space of rank-at-most-one matrices has a common image line or a common kernel hyperplane. Indeed compare two decomposable tensors: their sum has rank1 only if their image factors or their covector factors are proportional; mixing the two alternatives forces one common factor for the entire space. In the present equivariant matrix space that common line/hyperplane would be invariant, contrary to irreducibility of P4 or V. Rank0 contradicts nonzeroness. Thus (1) has generic rank3.

## 3. The determinantal scheme has length six

The four cubic maximal minors give a nonzero equivariant P4 subspace of Sym^3 A. They are linearly independent by irreducibility. Their common divisor, if any, is invariant because the group has no characters. A degree-one common divisor is impossible since A has no invariant. A degree-two or degree-three divisor would put the irreducible four-space of minors inside respectively the three-space of linear forms or the one-space of constants. Thus they have no common divisor.

Absence of a common factor excludes a projective curve component. The six C5 points exhibited in the next paragraph give nonempty projective support, so the maximal-minor ideal has height exactly2 (also the standard maximal-minor height bound excludes a larger height). Hilbert–Burch gives

    0 -> V O(-4) -> P4 O(-3) -> I_D -> 0.

Its Hilbert polynomial gives length(D)=6. This derivation proves expected codimension instead of assuming it.

For any subgroup C5, both A and V have a unique fixed line, whereas P4 has no fixed vector. The tensor of those two lines therefore projects to zero under pi. The corresponding C5 axis in P(A) lies in D. The six order-five subgroups give six distinct axes: distinct cyclic rotation subgroups cannot have the same axis, since rotations about a fixed axis lie in one torus. Equivalently the projective axis stabilizer is the dihedral normalizer of order10 in A5. Thus D already contains six distinct points. Its length proves that these are all of D and that each is reduced.

At each such point M has rank exactly2. If it had rank<=1, local row and column reduction would put all its maximal minors in the square of the maximal ideal, contradicting the reduced length-one local scheme. Therefore dim ker K_a=1 there and is zero elsewhere.

Finally the C5-fixed line in A=Sym^2 W is the weight-zero line xy in a diagonal basis for C5. Its discriminant is nonzero. None of the six axes is a square, proving uniform square injectivity.

## Verification and actual-input boundary

Run verify_positive_atiyah_six_axis_locus.py. It checks only universal characters, dimensions, the Hilbert polynomial, and the degree-zero C5 multiplicities. Actual use of this universal theorem requires ACTUAL-POSITIVE-ATIYAH-MULTIPLICATION-SURJECTS-ONTO-NINE-SPACE.md, including its Serre residue comparison. No actual source coefficients, matrix entries, ranks, or parameter scans enter either argument.
