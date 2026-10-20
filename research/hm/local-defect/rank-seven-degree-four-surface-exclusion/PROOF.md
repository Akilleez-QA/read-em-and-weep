> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Rank seven is excluded by its degree-four surface section

## Result

Under the established equivariance, irreducibility, saturated-image, and determinant hypotheses, generic rank(Q)=7 is impossible.

The universal geometric input is this statement:

> Let Z be a closed subscheme of P4 of dimension two and degree four, possibly nonreduced, with embedded or lower-dimensional components. If the complete cubic system H0(I_Z(3)) has no fixed divisor, then h0(I_Z(3)) <= 10.

No arithmetically Cohen--Macaulay assumption is made. This statement and the established rank-seven determinant k=3, together with the full-support Heisenberg Chern congruences, prove the exclusion.

## 1. Noncollinear plane schemes of length four

Let D be a zero-dimensional subscheme of P2 of length four, not contained scheme-theoretically in a line. Its saturated homogeneous coordinate ring A has Hilbert function

    H_A(0)=1, H_A(1)=3, H_A(t)=4 for t>=2.

Here is a proof that covers nonreduced schemes. Choose a linear form l avoiding the finitely many support points of D. It is a nonzerodivisor on A: the associated primes of a saturated zero-dimensional projective scheme's coordinate ring are the homogeneous primes of its support, and the irrelevant ideal is not associated. Alternatively saturation and multiplication by a section invertible along D prove this directly.

The exact sequence for multiplication by l shows that the first differences of H_A are the Hilbert function of the standard graded Artinian algebra A/lA. Thus H_A is nondecreasing, is eventually four, and its first differences cannot become zero and later positive: an algebra generated in degree one has every later graded piece zero once one graded piece is zero.

If H_A(2)=3, its first difference at degree two is zero, forcing the eventual value to remain three. This contradicts length four. Since H_A(2)<=4, it follows that H_A(2)=4, and monotonicity gives all later values. Therefore

    h0(I_D(1))=0,
    h0(I_D(2))=2,
    h0(I_D(3))=6.                                (1)

## 2. Taking general sections without a Cohen--Macaulay assumption

Let Z satisfy the geometric statement. Choose a general hyperplane H=P3, and then a general hyperplane L=P2 inside H. Put C=Z intersect H and D=C intersect L, with scheme-theoretic intersections.

The first hyperplane equation can be chosen to avoid every associated point of O_Z. The second can be chosen to avoid every associated point of O_C. Consequently both are nonzerodivisors on the corresponding structure sheaves. There are only finitely many associated points at each step. Possible zero-dimensional associated points are avoided by choosing the hyperplanes not to pass through their supports.

The intersections are proper: C has dimension one, and D is zero-dimensional of length four. One way to verify the length, including all embedded components, is to take successive differences of the Hilbert polynomial using these nonzerodivisor sections. The quadratic leading term of P_Z is 4t^2/2; its second difference is the constant four. Lower-degree terms disappear. Thus length(D)=4.

Let B be the base scheme of the complete cubic system of Z. The no-fixed-divisor hypothesis means dim(B)<=2; in particular the system is nonzero. A general plane L meets B in a finite set or is disjoint from it. The plane may be chosen with this property simultaneously with the preceding regular-section properties: each condition holds on a dense open set of the appropriate flag parameter space.

We claim D is noncollinear. If it lay in a line ell inside L, any cubic section vanishing on D would restrict to zero on ell. Indeed D, considered as a subscheme of the smooth curve ell=P1, is an effective divisor of length four. A section of O_ell(3) cannot vanish on it unless it is zero. Every member of H0(I_Z(3)), restricted to L, vanishes on D. Hence every such restriction would vanish identically on ell. This would place ell in the base locus B intersect L, contrary to its finiteness. Thus D is noncollinear, and (1) applies.

## 3. The cubic bound

The nonzerodivisor choices yield exact ideal-sheaf restriction sequences

    0 -> I_Z(t-1) -> I_Z(t) -> I_{C,H}(t) -> 0,
    0 -> I_{C,H}(t-1) -> I_{C,H}(t) -> I_{D,L}(t) -> 0.

These are sheaf sequences; their exactness does not require vanishing of any intermediate cohomology. They follow by tensoring the structure-sheaf sequences with the hyperplane quotient and using the nonzerodivisor condition to kill Tor_1.

Taking global sections gives upper bounds, with no surjectivity assumption. Since Z and C are nonempty, h0(I_Z)=h0(I_C)=0. Starting with (1), we obtain

    h0(I_C(1)) <= 0,
    h0(I_C(2)) <= h0(I_C(1))+h0(I_D(2)) <= 2,
    h0(I_C(3)) <= h0(I_C(2))+h0(I_D(3)) <= 8,
    h0(I_Z(1)) <= h0(I_Z)+h0(I_C(1)) = 0,
    h0(I_Z(2)) <= h0(I_Z(1))+h0(I_C(2)) <= 2,
    h0(I_Z(3)) <= h0(I_Z(2))+h0(I_C(3)) <= 10.

This proves the geometric statement.

## 4. Application to rank seven

Suppose generic rank(Q)=7. By ../rank-seven-cubic-plucker-obstruction/PROOF.md, the remaining determinant branch is k=3 and has no divisorial defect. In the saturated-image sequence

    0 -> F -> J tensor O -> R -> 0,

F has rank eleven and first Chern class -3, while R has rank nine and first Chern class 3. Both have H5-central weight three. The congruences of ../full-support-equivariant-chern-congruences/PROOF.md give

    c2(F)=0 modulo 5,
    c2(R)=4 modulo 5.

The strict second-Chern positivity argument established in ../rank-nine-defect-two-sided/PROOF.md applies to these ranks: F* is reflexive and generated outside codimension two, R is globally generated and torsion-free, and a zero class would contradict irreducibility of J or J*. Combined with c2(F)+c2(R)=3^2, this forces

    c2(F)=5,  c2(R)=4.                              (2)

The space H0(F) is an invariant subspace of the irreducible twenty-dimensional representation J. It cannot be all of J because rank(F)=11. Thus H0(F)=0, and the global-sections sequence injects J into H0(R). In particular h0(R)>=20.

Choose eight sufficiently general global sections of R. The torsion-free section-quotient argument in ../rank-nine-defect-two-sided/PROOF.md, Section 1, gives

    0 -> O^8 -> R -> I_Z(3) -> 0

for a closed subscheme Z of codimension at least two. This argument is valid for a torsion-free R, without assuming local freeness: generic sections have no divisorial rank drop, and the depth lemma excludes torsion of the rank-one quotient at higher-codimension associated points.

By (2), the surface cycle of Z has degree four. Thus Z has dimension two and degree four. Since R is globally generated, its quotient I_Z(3) is globally generated. Its complete cubic system therefore has base scheme exactly Z and in particular has no fixed divisor. The geometric statement applies and gives

    h0(I_Z(3)) <= 10.                               (3)

On the other hand H1(O)=0, so the last exact sequence gives

    h0(I_Z(3))=h0(R)-8 >= 12,                       (4)

contradicting (3). Hence generic rank seven is impossible.

## Evidence boundary

Only existing local proof statements and universal equivariant Riemann--Roch, elementary projective Hilbert-function arguments, hyperplane restriction sequences, and sheaf geometry were used. No actual HM source, operation matrix, product, selected input, polynomial instance, rank instance, jet, or residue was evaluated. The argument allows nonreduced schemes and lower-dimensional or embedded components, and assumes neither local freeness of R nor arithmetic Cohen--Macaulayness of Z. Only this local proof deliverable was written for the exclusion.
