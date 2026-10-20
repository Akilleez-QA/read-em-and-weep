> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Intermediate sextic surface obstruction

## Result

The ordered rank-eight Chern pair (14,22) is impossible. Together with the audited sextic bounds, the remaining pairs are (19,17) and (24,12).

More generally, let R be a globally generated torsion-free sheaf on P4 with rank 8, c1=6, c2=22, h0(R)>=20, and uniform Heisenberg central weight 3. These conditions are inconsistent. Only the elementary Heisenberg dimension divisibility is needed, not irreducibility under the full normalizer.

For the other high-degree branch, a rank-12 weight-2 sheaf E generated outside codimension two, with c1=6,c2=24,h0(E)>=20, necessarily has h0(E)=20 and h0(E(-1))=h0(E(-2))=0. This is a constraint, not an exclusion.

All geometry is over C. Sections and schemes below are allowed to be nonreduced; no ACM or reducedness assumptions are imposed.

## 1. Plane liaison fact used

Let D be a zero-dimensional subscheme of a plane complete intersection X of degrees u,v. Let B be its scheme-theoretic residual in X. Put b=uv-length(D). Then length(B)=b and

    h0(I_D(k))-h0(I_X(k)) = h1(I_B(u+v-3-k)).       (1)

Here the residual is defined by I_B=I_X:I_D; zero-dimensional schemes in a smooth plane are locally Cohen--Macaulay. Thus finite complete-intersection linkage applies without extra hypotheses. One way to derive (1) is the ideal residual sequence

    0 -> I_X(k) -> I_D(k) -> omega_B(k+3-u-v) -> 0.

By finite-scheme Serre duality the last term's global sections are dual to H0(O_B(u+v-3-k)). Under projective Serre duality, the connecting homomorphism to H1(I_X(k)) is dual to restriction of plane polynomials of degree u+v-3-k to B. Its kernel therefore has dimension h1(I_B(u+v-3-k)), yielding (1). The assertion also holds for empty B, with both sides zero.

We use only: every length-b plane scheme imposes independent conditions on forms of degree at least b-1. Indeed, choose a linear form avoiding its support, so the first differences of its Hilbert function form the Hilbert function of a standard graded Artinian algebra. Its Hilbert function starts at 1 and increases strictly until it reaches b: a zero first difference would force all later differences zero. Hence it reaches b by degree b-1. This proves the assertion for nonreduced schemes as well.

## 2. Sharp enough plane bounds for lengths 22 through 24

Let D have length a with 22<=a<=24. Suppose its sextic equations have no common curve. Write p_j=h0(I_D(j)).

There is no cubic equation: a cubic and a coprime sextic would contain D in an intersection of length18. Thus p_j=0 for j<=3.

Also p4<=1. For two independent quartics f,g with gcd h of degree t in {0,1,2,3}, residual to h gives

    a <= 6t+(4-t)^2.

The four right sides are 16,15,16,19. To justify the residual bound, choose a sextic coprime to h; the trace on h has length at most6t, while the residual is contained in the complete intersection of the coprime degree-(4-t) factors of f,g.

### Case A: p4=1

Choose its quartic q and a sextic s coprime to q. Then D lies in X=(q,s), a complete intersection of length24. Its residual B has length at most2. Formula (1), with (u,v)=(4,6), at k=5,6 uses residual twists2,1 respectively. Both H1 vanish by the preceding length bound. Therefore

    p5=3, p6=7.                                  (2)

These are exactly the corresponding dimensions of the complete-intersection ideal. For a=24 this also says D=X.

### Case B: p4=0

We claim p5<=2. If p5<=1 this is immediate. Otherwise take the gcd h of the entire vector space I_D(5), of degree t. The divided system has no common curve, so two sufficiently general divided quintics are coprime. Independence ensures 0<=t<=4. The residual D' to h has length at most (5-t)^2; the trace has length at most6t. Hence

    a<=6t+(5-t)^2.

If t=0, choose two coprime quintics and link D in their length25 intersection. Its residual has length at most3. Formula (1) at k=5 uses residual twist2, whose H1 is zero. Consequently p5=2.

If t=1, the bound is22. Necessarily a=22, the trace has length6, and D' has length16, equal to the intersection of the divided quartics. Thus D' is that complete intersection and its quartic ideal has dimension2. Division by h injects I_D(5) into that space, proving p5<=2.

If t=2, the bound is21, impossible.

If t=3, the bound is22. Necessarily D' is a complete intersection of two quadrics of length4, whose quadratic ideal has dimension2. Again p5<=2.

If t=4, D' is nonempty: otherwise h vanishes on D, contrary to p4=0. Division injects I_D(5) into I_D'(1). A nonempty finite scheme imposes at least one condition on linear forms, so the latter space has dimension at most2.

This proves p5<=2 in all cases. Thus the Hilbert function of D at degree5 is at least19. Since a>=22, strict growth until stabilization gives its degree6 value at least20 (if the degree5 value already exceeds19 this conclusion is immediate by monotonicity). Therefore

    p5<=2, p6<=8.                                (3)

## 3. Passing to a surface

Let Z be a surface scheme in P4 of degree a in [22,24] whose sextic ideal has no fixed divisor. Choose successive general regular hyperplane sections C in P3 and D in P2. Their degree/length is a; the restricted sextic system on D has no common curve. The regular flag and absence of fixed curves are justified exactly as in ../sextic-surface-section-bounds/PROOF.md, Section 3; embedded components are allowed.

Put z_j=h0(I_Z(j)) and c_j=h0(I_C(j)). The restriction sequences give

    c_j<=c_(j-1)+p_j,  z_j<=z_(j-1)+c_j.

All these dimensions vanish through degree3. In particular z4<=c4<=p4<=1.

Suppose z5 is divisible by five.

If z4=0 and p4=1, then c4<=1,c5<=4,z5<=4, hence z5=0. Next c6<=4+7=11, so z6<=11.

If z4=0 and p4=0, then c4=0,c5<=2,z5<=2, hence z5=0. Next c6<=2+8=10, so z6<=10.

We conclude

    z4=0 and 5 divides z5  ==> z5=0, z6<=11.      (4)

If z4=1, then p4=c4=1. Multiples of the surface quartic give z5>=5, whereas the restriction inequalities give z5<=1+4=5. Thus z5=5. Finally

    z6<=z5+c6<=5+(4+7)=16.                       (5)

## 4. Excluding degree22 on R

Choose seven general sections of R. The established torsion-free section-quotient lemma gives

    0 -> O^7 -> R -> I_Z(6) -> 0,

with degree(Z)=22 and no fixed divisor in the sextic system. Since H0(O(-j))=H1(O(-j))=0 for j>=1,

    h0(R(-j))=z_(6-j) for j>=1,
    z6=h0(R)-7>=13.

The central weight of R(-1) is4, so 5 divides z5. Its untwisted weight3 also gives h0(R) divisible by5, hence z6 is congruent to3 modulo5.

If z4=0, (4) gives z6<=11, impossible. Therefore z4=1. By (5), z5=5 and 13<=z6<=16. The congruence forces

    z4=1, z5=5, z6=13,
    h0(R(-2))=1, h0(R(-1))=5, h0(R)=20.          (6)

A nonzero section of R(-2) gives an injective sheaf map O(2)->R: R is torsion-free, so a generically nonzero map from a line bundle has zero kernel. Let Q be its coherent quotient. It has rank7 and is globally generated because R is globally generated. Cohomology and H1(O(2))=0 give

    h0(Q)=h0(R)-h0(O(2))=20-15=5.

A globally generated sheaf of rank7 requires at least7 independent global sections, by evaluation at the generic point. This is a contradiction. No torsion-freeness of Q is needed.

Alternatively, if the full symmetry group acts and H0(R)=J is the known irreducible20-dimensional representation, the unique section line of R(-2) is invariant. Multiplication by quadrics gives an invariant15-dimensional subspace of H0(R), also a contradiction. The globally generated quotient argument above does not require this stronger symmetry hypothesis.

Since the ordered pair (14,22) puts degree22 on R, it is excluded.

## 5. Degree24 constraint on E

For E of rank12, weight2, c1=6,c2=24, generated outside codimension two and with h0(E)>=20, choose eleven general sections. Then

    0 -> O^11 -> E -> I_Z(6) -> 0,
    z6=h0(E)-11>=9.

Both h0(E(-2))=z4 and h0(E(-1))=z5 are divisible by5, since their respective weights4 and3 are nontrivial. Since z4<=1, it is zero. Formula (4) gives z5=0,z6<=11. Untwisted divisibility gives z6 congruent to4 modulo5. Therefore z6=9 and h0(E)=20. This proves the constraints stated at the beginning, without excluding (24,12).

## Evidence boundary

This proof uses only universal sheaf geometry, finite plane complete-intersection residual duality, Hilbert functions, and the abstract Heisenberg dimension lemma. It does not evaluate an actual HM source, source matrix, operation value, selected input, rank instance, jet or residue. The sole write is this local proof artifact.
