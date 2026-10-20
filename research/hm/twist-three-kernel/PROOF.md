# Twist three: semistable evaluation kernel and no surface defect

## Theorem and scope

Retain the conditional nonzero branch of [the twist-three reduction](../twist-three-reduction/PROOF.md): on complex P4,
T=H0(End_0(F)(3)) is the irreducible fifteen-dimensional normalizer representation of central weight zeta^2. Evaluation has generic rank three and no divisorial defect. Write

0 -> K -> T tensor O -> B(3) -> D -> 0,

where B=End_0(F), K is reflexive of rank12, c1(K)=-9H and ch2(K)=(3/2+t)H^2; the effective codimension-two cycle of D has degree t in 5Z_{>=0}.

Then t=0 and K is slope-semistable. Moreover K* is globally generated. Thus D is supported in codimension at least three. Nevertheless D is nonzero: B(3) is not globally generated. Consequently, in the nonzero fifteen-section branch the evaluation fails on a nonempty locus of dimension at most one.

This does NOT prove H0(B(3))=0. It proves semistability and excludes the previously open positive surface-defect alternative without any selected HM matrix or polynomial evaluation. The logical order is first t=0 without semistability, then semistability from dual evaluation and negative-twist vanishing.

## 1. Central-character Riemann–Roch lemma

For any N-equivariant torsionfree sheaf E of rank r with scalar central weight zeta^2, every cohomology group of E(m), when m is not 2 modulo5, is a sum of nontrivial-central-character Heisenberg representations, each of dimension5. Hence its Euler polynomial P(m) vanishes modulo5 at 0,1,3,4.

Riemann–Roch on P4 uses

Td(P4)=1+(5/2)H+(35/12)H^2+(25/12)H^3+H^4.

All denominators of ch(E) and Td(P4) are prime to5. Therefore RR can be reduced coefficientwise modulo5. Its leading coefficient is r/24=-r modulo5, giving

P(m)=r[1-(m-2)^4] modulo5.

Comparing the m^3 and m^2 coefficients gives

c1(E)=3r modulo5,
ch2(E)=2r modulo5.

If c1(E)=-aH, this is equivalent to

a=2r modulo5,
c2(E)=2r(r-1) modulo5.

No local-freeness assumption is used: coherent Chern characters and RR apply to the torsionfree HN quotients as well. Higher-coefficient congruences are unnecessary here.

## 2. The maximal HN piece and two elementary exclusions

If K is unstable, let A be its first slope-Harder–Narasimhan piece, of rank r and determinant O(-a). HN uniqueness makes A N-equivariant. A is saturated in K, and K is saturated in T tensor O because its quotient is the torsionfree evaluation image. Thus A is saturated in T tensor O. In particular A is reflexive, and Q=(T tensor O)/A is torsionfree and globally generated.

The determinant inclusion gives a>=0; destabilization gives a/r<3/4. The span of the generic fibers A_x is a nonzero N-submodule of the irreducible T, hence equals all T. If a=0, its Plucker map is constant, contradicting full span. If a=1, its rational Plucker map has image a projective linear space P^s, s<=4, in Gr(r,T). The Grassmannian linear-space lemma proved in [PLUCKER-LEMMA.md](PLUCKER-LEMMA.md) bounds the total fiber span by r+s. The only degree-one arithmetic candidates below have r=3 or8, and both give r+s<15. They are excluded.

The complete first-piece arithmetic list after a=0,1 exclusion is

(r,a)=(6,2),(7,4),(9,3),(10,5),(11,2),(11,7).

Indeed these are exactly 1<=r<=11, 0<a<3r/4 and a=2r modulo5 with a!=1. This is a small integer check, not a geometric rank computation.

### Globally generated torsionfree quotient positivity

For any globally generated torsionfree sheaf Q of rank q on P4, c2(Q)>=0. Choose q-1 general global sections. They are independent away from codimension at least two, and inject O^{q-1} into Q. The quotient has no codimension-one torsion. At a point of codimension at least two, the depth lemma gives quotient depth at least

min(depth Q, depth O-1)>=1.

Thus the quotient is torsionfree everywhere. It is rank one, hence I_Z tensor det Q for a subscheme Z of codimension at least two. Its second Chern class is the effective codimension-two cycle [Z]. The case q=1 is direct. Therefore c2(Q)>=0.

Applied to 0->A->T tensor O->Q->0, this gives

c2(A)<=a^2.

Meanwhile A is semistable, so Bogomolov gives

c2(A)>=(r-1)a^2/(2r).

For r=6 or11 and a=2, the central congruence is c2(A)=0 modulo5, while the Bogomolov lower bound is strictly positive. Therefore c2(A)>=5, contradicting c2(A)<=4. This genuinely excludes the rank-six determinant-minus-two rival; irreducibility alone did not do so.

Only (7,4),(9,3),(10,5),(11,7) remain for the first HN piece.

## 3. A precise equality-case exclusion

For (r,a)=(9,3), Bogomolov and the central congruence give c2(A)>=4 and c2(A)=4 modulo5. The value4 would give

Delta(A)=2*9*4-8*3^2=0.

It cannot occur. The equality theorem for a slope-semistable reflexive sheaf on a smooth compact Kahler manifold gives a filtration with projectively flat quotients of the same slope. A precise primary reference is Chen, arXiv:2205.12305, Theorem1.14 and Proposition5.2; take X=P4, its hyperplane Kahler metric, and the identity resolution. Since P4 is simply connected, the projectivization of every such quotient is trivial; a vector bundle with trivial projectivization is O(k)^{direct sum rank} for an integer k. Its slope is integral, whereas the slope of A is -1/3. Contradiction.

Hence for this case c2(A)>=9. A is reflexive by Section2, so the theorem's reflexivity hypothesis is satisfied. No unproved general-plane semistability is invoked.

## 4. Complete residual HN arithmetic proves t=0

All HN slopes are at most the first, which is strictly negative; write each HN quotient E_i with rank r_i and c1=-a_iH. Thus every a_i is a positive integer. They satisfy

sum r_i=12, sum a_i=9, a_i=2r_i modulo5,
a_1/r_1<a_2/r_2<...,
c2(E_i)>= (r_i-1)a_i^2/(2r_i),
c2(E_i)=2r_i(r_i-1) modulo5.

The increasing-ratio convention is precisely decreasing HN slope. For torsionfree quotients the ordinary Bogomolov inequality applies; reflexivity of later quotients is not needed.

After the first-piece exclusions, the complete possible profiles and lower second-Chern numbers are:

- ranks (7,4,1), a=(4,3,2), c2 lower bounds (9,4,0).
- ranks (7,5), a=(4,5), c2 lower bounds (9,10).
- ranks (9,3), a=(3,6), c2 lower bounds (9,12); the first9 uses Section3.
- ranks (10,2), a=(5,4), c2 lower bounds (15,4).
- ranks (11,1), a=(7,2), c2 lower bounds (25,0).

Exhaustiveness can be checked by taking the remaining totals after each allowed first piece. For first (11,7) only (1,2) remains. For (10,5), remaining (2,4) cannot split into increasing slopes because the only positive rank-one a<=4 is2, giving equal ratios. For (9,3), remaining totals (3,6) likewise allow only a single factor: rank1 needs a=2 and rank2 needs a=4, all ratios equal2. For (7,4), remaining totals (5,5) allow either the single factor (5,5), or (4,3) followed by (1,2); other partitions violate the congruence or strict ratio ordering.

In each of the five rows,

sum ch2(E_i) <= sum (a_i^2/2 - lower_bound_i)=3/2.

Since ch2 is additive and ch2(K)=3/2+t with t>=0, this proves t=0 when K is unstable.

If K is semistable, its discriminant 45-24t is nonnegative. Since t is a nonnegative multiple of5, again t=0. This finishes the theorem without assuming semistability of K.

The five rows give additional exact constraints if instability occurs: every displayed lower bound must be attained, since their upper sums already equal3/2. These are necessary alternatives only, not realizability statements.

## 5. Evaluation still must fail somewhere

The Chern classes of B(3) are c1=9H, c2=42H^2, c3=72H^3. If this rank-three bundle were globally generated, the tautological line bundle on the quotient projective bundle P(B(3)) would be globally generated, hence nef. Its sixth power would have nonnegative degree. The projective bundle formula instead gives

integral_{P(B(3))} c1(O(1))^6
= integral_{P4} (c1^4-3c1^2*c2+c2^2+2c1*c3)
=6561-10206+1764+1296=-585.

Contradiction. Thus D is nonzero. Section4 says it has no surface component, and the imported divisor theorem says it has no divisor component. Its support is therefore a nonempty union of curves and/or points. Nothing here shows that a curve rather than only points must occur.

## Sources, audit boundary, and computation scope

- Imported geometry and normalizer representation: [the twist-three reduction](../twist-three-reduction/PROOF.md) and its [primary-source input derivation](../twist-three-reduction/INPUTS.md).
- Grassmannian linear-space lemma: [PLUCKER-LEMMA.md](PLUCKER-LEMMA.md), proved there by elementary linear algebra.
- Chen, Admissible Hermitian-Yang-Mills connections over normal varieties, arXiv:2205.12305, Theorem1.14 printedp9 and Proposition5.2 printedpp31–32: https://arxiv.org/pdf/2205.12305 . Opened 2026-10-20. The present application only uses the smooth projective equality case.
- Bertone–Roggero, Splitting type, global sections and Chern classes for torsion free sheaves on P^N, arXiv:0804.2985, Theorem3 printedp7: https://arxiv.org/pdf/0804.2985 . The c2 lower-bound inequality corroborates Section2's positivity; no stronger equality clause is needed.

The supplied short arithmetic script enumerates only ranks, determinants and congruence-rounded Bogomolov bounds. It does not compute an HM map, source, pairing, polynomial, or selected instance. The proof's five-row residual enumeration is hand-checkable and independent of the script.

## 6. New upgrade: the kernel is in fact slope-semistable

Import the independently audited HM vanishing

H1(B(u))=0 for every u<=-2,

proved by the unnumbered proposition on printed p.218 of Decker–Schreyer, Pullbacks of the Horrocks–Mumford bundle, J. reine angew. Math. 382 (1987), 215–220. [Primary page](https://gdz.sub.uni-goettingen.de/id/PPN243919689_0382?tify=%7B%22pages%22%3A%5B222%5D%2C%22view%22%3A%22info%22%7D); [article record](https://eudml.org/doc/152990). The proposition states the vanishing for End(F); its proof explicitly normalizes c1(F)=-1. This is the classical complex HM bundle, not an assertion for arbitrary pullbacks or positive characteristic. Trace splitting transfers the stated End(F) vanishing to B. Only u=-4,-5 will be needed.

Section4 established codim Supp(D)>=3. On the regular ambient P4, a sheaf supported in codimension at least three has sheaf Ext^j(D,O)=0 for j<3. Write I=im(evaluation). Dualizing 0->I->B(3)->D->0 gives I*=B(-3) and Ext^1(I,O)=Ext^2(D,O)=0. Dualizing 0->K->T tensor O->I->0 therefore gives a short exact sequence

0 -> B(-3) -> T* tensor O -> K* -> 0.

Consequently for m>0,

H0(K*(-m))=0,

because H0(O(-m))=0 and H1(B(-3-m))=0. In particular K admits no nonzero morphism to either O(-1) or O(-2).

Suppose K were unstable. In each of the five exhaustive profiles of Section4, the final HN quotient E has one of these invariants:

- rank1, c1=-2;
- rank5, c1=-5, c2=10;
- rank3, c1=-6, c2=12;
- rank2, c1=-4, c2=4.

The rank-one case has E**=O(-2). In the other cases E is semistable and Delta(E)=0. Its reflexive hull E** remains semistable, and the codimension-two defect cycle of E**/E is effective. Hence Delta(E**)<=Delta(E)=0. Bogomolov forces equality, and Chen's reflexive equality theorem applies to E**. On simply connected P4, its projectively flat factors are sums of O(-1) in rank5 case or of O(-2) in ranks2,3 cases. All extensions between copies of the same line bundle split since H1(O)=0. Thus

E**=O(-1)^5, O(-2)^3, or O(-2)^2,

respectively. The surjection K->E followed by E->E** and a suitable summand projection gives a nonzero map K->O(-m), m=1 or2. This contradicts the preceding vanishing.

Therefore K is slope-semistable. The final unconditional conclusion within the nonzero15branch is:

K is reflexive, slope-semistable, rank12, c1=-9H, ch2=(3/2)H^2, Delta=45H^2;
K* is globally generated;
D is nonzero and supported in dimension at most one.

Logical order matters: codimension-two defect vanishing was proved first without assuming semistability. Only then was dual evaluation exactness used to rule out the residual unstable profiles. This is not a circular Bogomolov argument.

Twist-three section vanishing remains unproved.
