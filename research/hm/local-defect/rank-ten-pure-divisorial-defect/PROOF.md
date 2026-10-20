# Rank ten: locally free image, pure divisorial defect, and elimination of k=2

## Results

Under the hypotheses of ../global-linear-image-plucker/PROOF.md, assume generic rank(Q)=10. Write G=im(b), F for its saturation in J tensor O on P^4, T=F/G, and R=(J tensor O)/F. Then:

1. G is a vector bundle of rank fourteen, with resolution
   0 -> O(-3) -> O(-1)^15 -> G -> 0,
   where the first map is the canonical square-coordinate inclusion.
2. The defect T is either zero or a pure three-dimensional S2 sheaf. In particular it has no nonzero subsheaf supported in codimension at least two.
3. The previously allowed pair (k,d)=(2,10) is impossible. Only (7,5) and (12,0) remain.
4. For (k,d)=(12,0), F=G and T=0. There is no saturation defect of any codimension. Here c2(F)=69 and c2(R)=75.
5. For (k,d)=(7,5), writing ch2(T)=t h^2, one has
   t in {-53/2, -51/2, ..., 41/2}.
   Equivalently, 1 <= c2(F) <= 48 and 1 <= c2(R) <= 48, with c2(F)+c2(R)=49.

These are necessary conditions, not an exclusion of rank ten. The proof is universal sheaf geometry and the established irreducibility of J. It evaluates no actual source matrix, operation, input, rank instance, polynomial instance, jet, or residue.

## 1. The actual image is locally free

The canonical square relation gives a map O(-3) -> O(-1) tensor Sym^2(V). At every projective point [u], its fiber is the nonzero vector u^2. It is therefore a line subbundle, and its cokernel G0 is locally free of rank fourteen.

The relation makes b factor through a map G0 -> J tensor O. Under the rank-ten hypothesis b has generic rank fourteen. Thus this factor map has generic rank fourteen and its kernel is a torsion subsheaf of the vector bundle G0. The kernel is zero. Consequently G=im(b) is isomorphic to G0, proving the asserted vector-bundle resolution.

Its Chern character begins
   ch(G)=14 - 12h + 3h^2 + ...,
so c1(G)=-12h and c2(G)=69h^2.

## 2. Purity and S2 of the defect

Since R is torsion-free by saturation, F is reflexive: in 0 -> F -> O^20 -> R -> 0 the depth lemma gives depth(F_p)>=min(2,c) at every point of ambient codimension c, and F is torsion-free.

Apply the depth lemma to 0 -> G -> F -> T -> 0. Since G is locally free, at any point p of ambient codimension c>=2,
   depth(T_p) >= min(c-1,2)
whenever T_p is nonzero. Hence T has no associated point of codimension at least two. Since it is torsion, all its associated points have codimension one. Thus any nonzero T is pure of dimension three. At a point of its support of ambient codimension c, its local dimension is c-1; the displayed bound proves S2. At codimension one the S2 requirement is vacuous.

The degree of its effective divisorial cycle is d=12-k. If d=0, purity forces T=0. Equivalently, the two reflexive sheaves G and F agree in codimension one and hence agree everywhere. This proves the zero-defect claim for k=12, including defects that might otherwise have been hidden in higher codimension.

## 3. A section-count obstruction excludes k=2

The equivariant inclusion F -> J tensor O identifies H0(F) with an invariant subspace of the irreducible twenty-dimensional representation J. It cannot equal J: if it did, all constant sections of J tensor O would lie in F, forcing F=J tensor O, contrary to rank(F)=14. Therefore H0(F)=0. The quotient exact sequence gives an injection
   J -> H0(R),
so h0(R)>=20.

Suppose k=2. Then R is globally generated, torsion-free, rank six, and det(R)=O(2). Choose five sufficiently general global sections. The section argument of ../rank-nine-defect-two-sided/PROOF.md, Section 1, gives an exact sequence
   0 -> O^5 -> R -> I_Z(2) -> 0,
where Z has codimension at least two. To recall the torsion-free point: there is no divisorial rank drop, and at every point of codimension c>=2 the depth lemma gives depth of the rank-one quotient at least min(1,c-1)=1. Thus that quotient has no torsion in any codimension and is of the stated ideal-sheaf form.

Since H1(O)=0,
   h0(R)=5+h0(I_Z(2)) <= 5+h0(O(2))=20.
The preceding lower bound forces equality, so H0(I_Z(2))=H0(O(2)). Since all global sections of O(2) generate it at every point, their containment in I_Z(2) forces I_Z=O. Thus Z is empty.

The sequence now splits because Ext1(O(2),O^5)=H1(O(-2))^5=0. Hence
   R = O^5 direct-sum O(2).
Dualizing its quotient map from J tensor O gives the equivariant injection R* -> J* tensor O. Taking global sections produces a five-dimensional invariant subspace H0(R*) inside the irreducible representation J*, a contradiction.

Therefore k=2 is impossible. This argument requires neither a classification of low-Chern-class sheaves nor local freeness of R in advance.

## 4. The surviving divisorial branch

For any k write ch2(T)=t h^2. Its codimension-one character is ch1(T)=(12-k)h, but its ch2 is not the degree of a codimension-two effective cycle: T is divisorial. Chern-character additivity gives
   c2(F)=k^2/2-3-t,
   c2(R)=k^2/2+3+t.

The positivity and zero-c2 arguments of ../rank-nine-defect-two-sided/PROOF.md apply verbatim, with ranks fourteen and six in place of thirteen and seven. Namely, F* is reflexive and generated outside codimension two, while R is globally generated and torsion-free. Both second Chern classes are nonnegative. If c2(F)=0, reflexive zero-c2 splitting gives F=O^13 direct-sum O(-k), whose thirteen constant sections contradict irreducibility of J. If c2(R)=0, applying positivity to R** first shows its codimension-two discrepancy has degree zero, and reflexive zero-c2 splitting gives R*=O^5 direct-sum O(-k). Its five constant sections contradict irreducibility of J*.

Consequently both inequalities are strict:
   -k^2/2-3 < t < k^2/2-3.
For k=7 these become -55/2<t<43/2. Since c2(F) is integral, t lies in 1/2+Z. Thus the allowed list is -53/2,-51/2,...,41/2, or equivalently c2(F) and c2(R) are positive integers summing to 49.

For k=12, Section 2 already gives T=0 and hence t=0; the formulas recover 69 and 75. Positivity does not eliminate this branch.

## Scope

Only the necessary pair (2,10) has been eliminated. The pair (7,5) still permits a pure divisorial defect of degree five; no assertion about existence or absence of an invariant quintic is made. The pair (12,0) has exactly zero saturation defect.
