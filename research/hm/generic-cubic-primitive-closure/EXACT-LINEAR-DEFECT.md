# Exact linear defect: count the contained component lines

## Result

Let C be the reduced disjoint union of the 25 HM component lines in P^4, B=End_0(F), and let ell be a nonzero linear form. Put H=V(ell), Z=C intersect H scheme-theoretically, and let k(H) count the component lines contained in H. Then

dim coker[ell:H^1(B(4)) -> H^1(B(5))]=k(H),
rank[ell:H^1(B(4)) -> H^1(B(5))]=32-k(H).

The residual rank is 24-k(H). This sharpens the already established set-theoretic failure criterion; it makes no assertion about determinantal scheme multiplicities.

Retained premises: the six quintic minors generate the sheaf ideal of the reduced C; C is nondegenerate; proper hyperplane sections (k=0) span their hyperplanes; the actual residue identification; and universal primary linear coverage. These are the inputs established or explicitly retained in PR541 at dac25ba696b20a1965d5b189b141626c2fd9f672. The new step treats sections with exactly one contained component.

## 1. Every hyperplane section spans its hyperplane

The case k=0 is the prior proper-section result. If k>=2, two contained component lines are disjoint, hence skew inside H=P^3, and span H. It remains to prove the assertion for k=1.

Write l_0 for the unique contained component. Each of the other 24 component lines meets H in a reduced point. These points are pairwise distinct and none lies on l_0, because the original component lines are disjoint.

Suppose Z were contained in a plane Pi inside H. Then Pi contains l_0 and all 24 points. No other component line lies in Pi, since none lies in H. Consequently the scheme-theoretic intersection C intersect Pi is exactly the reduced line l_0 together with those 24 reduced off-line points. One can also use only its support and its reduced generic structure along l_0 below.

Restrict the six quintic ideal generators to Pi. Their images generate I_(C intersect Pi,Pi) as an ideal sheaf. This follows by tensoring the generating surjection with O_Pi and then taking the image of I_C tensor O_Pi -> O_Pi; that image, rather than the tensor product itself, is the intersection ideal.

Choose a linear equation t for l_0 inside Pi. Every restricted quintic is divisible by t. Their common divisorial factor is exactly t, with exponent one:

- No other common irreducible factor is possible, because the common zero set is only l_0 and 24 points.
- Near the generic point of l_0, the other component lines are absent. Thus the ideal of C equals the ideal of the reduced l_0 there. Its image in O_Pi is the principal ideal (t), not (t^2). Since the restricted generators generate that ideal, they cannot all be divisible by t^2.

Divide the six restricted quintics by t. The resulting quartic system has no fixed curve and still vanishes at the 24 off-line points. There are two coprime members of this system: choose any nonzero member, then choose a second outside the finitely many proper linear subspaces of members divisible by one of the first member's irreducible factors. This uses only that the complex ground field is infinite and there is no common factor; it is not a coefficient evaluation.

Bézout bounds the intersection length of two coprime plane quartics by 16 (in fact it equals 16). They cannot contain 24 distinct points. This contradiction proves that Z spans H also when k=1.

## 2. The exact residue defect

The single-linear-form residue formula is

dim coker(residual multiplication by ell)
  =h^0(I_Z(1))-h^0(I_C(1))+k(H)-1.

Nondegeneracy gives h^0(I_C(1))=0. The spanning result gives H^0(I_Z(1))=C ell, hence h^0(I_Z(1))=1. The residual defect is therefore exactly k(H).

More intrinsically, write a residue tuple as lambda=(lambda_l), modulo diagonal constants, and choose a global linear form f with f|l=lambda_l ell|l. The vanishing along Z forces f=c ell. Subtracting c from the tuple leaves precisely arbitrary entries on the k(H) contained components and zero entries elsewhere. These supported tuples inject modulo constants because C is not contained in H. Thus the residual dual cokernel is canonically the supported-section space on those components, with the common determinant factor from evaluation duality retained.

Universal primary linear coverage identifies the full and residual cokernels. Since the full target has dimension 32 and its primary part has dimension eight, the asserted full rank 32-k(H) and residual rank 24-k(H) follow.

## 3. Set-theoretic rank strata

For every m>=1, the locus of linear maps of corank at least m is exactly the set of hyperplanes containing at least m component lines. Equivalently it is the union, over m-element subsets of the components, of their common containing-hyperplane loci.

For m=1 this is the already known union of 25 dual planes. For m>=2 it is a finite set: two disjoint component lines span a unique P^3, so their dual planes meet in one point. At such a hyperplane the exact corank is the number of contained components. This does not classify coincidences among those pair-span hyperplanes and does not assign scheme multiplicities.

## Source and boundary

Current PR1 was read first; its latest relevant update is the exact failure-locus statement at dac25ba696b20a1965d5b189b141626c2fd9f672. The new content here is the one-contained-line Bézout exclusion and ensuing exact corank, not the previously published failure support.

PR541: https://github.com/Akilleez-QA/read-em-and-weep/pull/541 .

No selected hyperplane, polynomial coefficients, multiplication rank, or original fixed-pair membership was evaluated. No determinantal multiplicity or full proof-repair claim is made.
