# Proof audit: degree-sixty frontier

## Verdict

The proposed necessary conditions pass the algebraic and numerical checks below, conditional on the explicitly imported normalizer genus and quintic-surface exclusion theorems. This is an author audit; no independent-review claim is made.

## 1. Arithmetic

Castelnuovo uses d−1=m(r−1)+ε and π(d,r)=(r−1)m(m−1)/2+mε. The four relevant calculations are:

- (d,r)=(60,9): (m,ε)=(7,3), π=189.
- (120,19): (6,11), π=336.
- (120,24): (5,4), π=250.
- Optional cubic bound (180,44): (4,7), π=286.

For the degree-sixty general section with h(1)=4,h(2)=10, the lower-bound sequence through saturation is

    4,10,13,19,22,28,31,37,40,46,49,55,58,60.

Its deficiencies sum to

    56+50+47+41+38+32+29+23+20+14+11+5+2=368.

If h(3)=20, the improved sequence is

    4,10,20,23,29,39,42,48,58,60,

whose deficiencies sum to 267. In the A-cover formula g=25q−24+10t, the bound 368 gives q≤15; at q=14 and q=15, the branch bounds are t≤4 and t≤1 respectively. Neither permits a nonempty orbit of size at least twelve. The resulting genera are exactly 326 and 351.

## 2. Linear-series checks

Choosing 10, 20, or 25 sections is legitimate even if the complete system has more sections: each selected system contains the original five linear sections or all fifteen independent ambient quadrics. Thus it is basepoint free and birational, not merely generically finite of unknown degree. Its image degree is exactly deg L or deg L². The optional 45-section cubic system similarly contains the 35 ambient cubics. Nondegeneracy follows from linear independence of the chosen sections.

For degrees one, two, and three, the central H₅ character is nontrivial. All relevant section spaces on C and X have dimension divisible by five. The character of a quotient has the same property, so there is no issue with taking the Rao dimensions as differences. The proof never assumes that an arbitrary invariant subspace of Sym²V* is irreducible; vanishing of quadrics follows from the separately proved vanishing of cubics.

## 3. Cubic-base-locus checks

The entire nonzero space W of cubics is N-stable. Its gcd is therefore semi-invariant. A positive gcd degree between one and three is impossible under H₅, because every one-dimensional character kills its commutator center. This proves that a coprime pair exists; it does not merely assert that two arbitrary independent cubics are coprime.

The complete intersection of a coprime pair has degree nine and pure dimension two. If the entire base locus had no surface, a third cubic could avoid the finitely many associated surface primes. Cohen–Macaulayness of this complete intersection, rather than any ACM assertion about C, makes the triple a regular sequence. The degree-27 complete-intersection curve cannot contain the integral degree-sixty C.

For the union of surface components of the full base locus, the total reduced degree is at most nine. The union is N-stable even if the chosen pair is not equivariant. An A-orbit of size 25 is too costly; one of size five requires six disjoint such orbits under the quotient action and is likewise too costly. Every surface component is A-stable. Degree divisibility follows by taking a second difference of its Hilbert polynomial at residues 1,2,3 modulo five. A positive degree divisible by five and total degree at most nine means exactly one component of degree five, so it is N-stable. This is precisely the imported forbidden surface, including possible nonnormality.

## 4. Hyperplane and non-ACM checks

The restriction sequence used is

    0→I_C(n−1)→I_C(n)→I_(Z,H)(n)→0.

A general hyperplane avoids the finite singular locus and cuts sixty distinct points in uniform position. Linear normality gives H¹(I_C(1))=0, hence the no-quadrics result on C lifts to the statement h_Z(2)=10. To deduce h_Z(3)=20, one additionally needs H¹(I_C(2))=0; this condition is invoked only in the branch being contradicted. No blanket projective-normality assumption is made.

For an explicit justification of the genus inequality, let R be C's homogeneous coordinate ring and ℓ a general hyperplane equation. Since R is a domain, ℓ is a nonzerodivisor. Put q(n)=dim(R/ℓR)_n. Saturation gives q(n)≥h_Z(n), with equality for large n. Telescoping the graded multiplication sequence gives

    p_a(C)=Σ_(n≥1)(60−q(n))≤Σ_(n≥1)(60−h_Z(n)).

This is valid when q(n)>60 and individual summands are negative. It does not require C to be ACM, and proves an upper bound for p_a(C), hence also for g(X).

Finally h⁰(C,O_C(2))=20 and I_C(2)=0 imply h¹(I_C(2))=5 by the ambient ideal sequence. Equality h⁰(C,O_C(2))=h⁰(X,L²) does not imply normalization is an isomorphism. The only singularity bound asserted is total normalization defect p_a−g≤42.

## Scope

Only local mathematical proof files were inspected or authored. No actual source-instance evaluation is claimed. The genus-326 quadratic-deficiency-five branch remains open.
