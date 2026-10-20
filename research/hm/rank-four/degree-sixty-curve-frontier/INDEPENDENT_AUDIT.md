# Independent audit: degree-sixty curve frontier

## Verdict

**PASS, conditional on the explicitly imported group-action and invariant-quintic theorems.** I independently checked `PROOF.md`, its arithmetic, the component-stabilizer argument in the degree-fifty proof, the faithful-genus lower bound, and the scope of the quintic-surface argument and its sectional-genus input. No degree-50/55 exclusion, normality, projective normality, or arithmetic Cohen–Macaulayness is needed. The surviving genus-326 case is not excluded and no existence claim is proved.

## 1. Integrality has no circular degree-55 input

An orbit of 25 curve components costs at least 75. A size-five A-orbit produces six distinct stabilizer-axis orbits, costing at least 90. Thus every component is A-stable, nondegenerate, and of degree divisible by five. A nontrivial SL2(F5)-orbit has at least five elements; its component degree is consequently at most 12 and is either 5 or 10. The imported stabilizer argument applies to both possibilities: Castelnuovo gives normalization genus at most 9; the A-cover possibilities are precisely genus 1 with quotient genus 1 and no branching, or genus 6 with quotient genus 0 and three branch points. In each case the component stabilizer modulo A has order at most 6, forcing at least 20 components and degree at least 100. All components are therefore N-stable. The already established exclusion through degree 45, together with divisibility, gives component degree at least 50. A total degree of 60 permits only one component.

This reasoning neither imports nor implicitly presumes exclusion of integral degree-50 or degree-55 curves.

## 2. Linearization and complete section spaces

The ambient H5-linearization of O(1) restricts to the invariant curve and pulls back functorially to its normalization. Its central character in degrees 1, 2, and 3 is nontrivial. For each such character, clock-and-shift implies that every finite-dimensional module has dimension divisible by five; this applies equally to sections on C and on X. It does not require a full linear lift of the projective normalizer or irreducibility of Sym2(V*).

Every chosen subsystem in the proof contains all ambient sections of the corresponding power of O(1). Consequently it is basepoint free and birational, and its degree is the degree of the line bundle, rather than that degree divided by an unknown mapping degree. Linear independence makes the image nondegenerate. The Castelnuovo checks are:

- degree 60 in P9: 59=8·7+3, giving genus at most 189;
- degree 120 in P19: 119=18·6+11, giving genus at most 336;
- degree 120 in P24: 119=23·5+4, giving genus at most 250;
- degree 180 in P44: 179=43·4+7, giving genus at most 286.

Thus the faithful-genus lower bound 326 proves h0(X,L)=5 and hence h0(C,O_C(1))=5 and H1(I_C(1))=0.

## 3. Cubic equations and the low-degree invariant surface

For a nonzero invariant space of cubics W, its polynomial gcd is semi-invariant. A positive gcd degree at most 3 would have a nontrivial central character, impossible for a one-dimensional H5 representation because the center is the commutator subgroup. Hence the gcd is 1. Avoidance of the finitely many factor-divisibility subspaces gives a genuinely coprime pair f,g.

The degree-nine complete intersection V(f,g) is Cohen–Macaulay and has no embedded associated primes. If V(W) has no surface component, a third member avoids all its surface primes, producing a regular sequence and a degree-27 complete-intersection curve containing C. This contradicts degree 60. This use of Cohen–Macaulayness concerns the complete intersection, not C.

The reduced union T of the surface components of V(W) is N-stable, nonempty, and has degree at most 9. Its component orbits of size 25 or 5 would cost at least 25 or 30 respectively; therefore every surface component is A-stable. For an A-stable integral surface S, the values of its Hilbert polynomial at three sufficiently large consecutive integers congruent to 1,2,3 modulo 5 are divisible by five. Their second difference is deg S. Thus each surface degree is divisible by five, and the degree-nine budget leaves exactly one degree-five surface, necessarily N-stable and nondegenerate.

The imported quintic exclusion has a stated sectional-genus hypothesis, so it is important to include its sectional-genus bridge. That bridge applies here without assumptions peculiar to the original rank locus: the Heisenberg Hilbert congruence for any invariant degree-five surface gives sectional arithmetic genus congruent to 1 modulo 5. Explicitly, write P_S(n)=5 binom(n,2)+(6-g)n+chi; consecutive nonzero central-character residues force 6-g divisible by five. The general-section argument in `../rank-one-middle-quintic-reduction/SECTIONAL_GENUS.md` proves that the section is integral and nondegenerate even for a nonnormal/non-CM surface, and bounds its arithmetic genus between 0 and 5. Hence it is 1. The birational quintic theorem therefore applies to precisely the surface produced here. This is not an illicit invocation of a normal-surface classification.

It follows that I_C(3)=0, and then I_C(2)=0 by multiplication with any nonzero linear form.

## 4. Uniform-position and arithmetic-genus bounds

A general hyperplane section Z consists of 60 distinct points in uniform position. Its linear Hilbert value is 4. The ideal restriction sequence and H1(I_C(1))=0 give h_Z(2)=10.

For clarity, the uniform-position growth rule used is valid for arbitrary nonnegative degrees. One elementary verification is as follows. Put k=h_Z(a), l=h_Z(b). Uniform position makes evaluation on every subset have rank the minimum of its size and the full rank. Choose k-1 points and an a-form vanishing precisely on those points; a nonzero section with any further zero would violate this rank property. Multiplication of the b-forms by this form has rank min(l,60-k+1), and vanishes on the chosen points. On the other hand, multiplying the a-forms by a b-form nonzero at all points gives evaluation rank k-1 on those points. Combining these subspaces yields rank at least min(60,k+l-1). This proves the stated growth inequality.

Iteration gives the first lower-bound sequence

    4,10,13,19,22,28,31,37,40,46,49,55,58,60,

whose deficiencies sum to 368. If h_Z(3)=20, the stronger sequence is

    4,10,20,23,29,39,42,48,58,60,

whose deficiencies sum to 267.

The genus inequality is appropriate for non-ACM curves. If R is the homogeneous coordinate ring and ell a general linear equation, it is a nonzerodivisor on the domain R. Let q_n=dim(R/ell R)_n. Saturation gives q_n>=h_Z(n), and the Hilbert polynomial gives

    p_a(C)=sum_{n>=1}(60-q_n)<=sum_{n>=1}(60-h_Z(n)).

There is no assumption that q_n equals h_Z(n) or never exceeds 60. The normalization genus is at most p_a(C), so the first bound gives 326<=g(X)<=p_a(C)<=368.

## 5. Quotient genus and exclusion of genus 351

The induced SL2(F5)-action on Y=X/A is faithful by the invariant-function-field/deck-group argument. Its genus is at least 14. Riemann–Hurwitz is exactly

    g(X)=25g(Y)-24+10t,

where t counts A-branch points. The bound 368 leaves quotient genera 14 and 15, with t at most 4 and 1 respectively. Finite stabilizers on Y are cyclic, and their orders are at most 10. Each nonempty invariant branch set therefore contains an orbit of at least 12 points. Thus t=0 and the only normalization genera are 326 and 351.

If g(X)=351, twenty sections of L2 would give the contradictory bound 336. Central-character divisibility and the fifteen ambient quadrics force h0(X,L2)=h0(C,O_C(2))=15. Therefore H1(I_C(2))=0. Together with I_C(2)=I_C(3)=0, the restriction sequence now implies I_(Z,H)(3)=0, i.e. h_Z(3)=20, and p_a(C)<=267. This excludes genus 351. The same genus-267 contradiction excludes H1(I_C(2))=0 in the remaining genus-326 case.

## 6. Quadratic and cubic conclusions; nonnormality remains open

For genus 326, twenty-five sections of L2 contradict the bound 250. Thus h0(X,L2) is 15 or 20; the first value would give the excluded vanishing of H1(I_C(2)). Hence h0(X,L2)=20. The intermediate section space on C is likewise 15 or 20, and the same contradiction forces 20. Since there are exactly fifteen independent ambient quadrics,

    h1(I_C(2))=20-15=5.

This proves that C is not ACM. Equality of sections on C and its normalization in degrees one and two does not imply normality: the proof correctly leaves normalization defect between 0 and 42.

The optional cubic statement also checks. At least 35 ambient cubic sections inject. If there were at least 45 normalization sections, the selected subsystem would give the bound 286, contradicting genus 326. Divisibility by five therefore bounds h0(X,L3) by 40. Consequently h0(C,O_C(3)) is 35 or 40, and h1(I_C(3)) belongs to {0,5}. No surjectivity of a multiplication map is inferred.

## Scope of this review

Only local proof documents and abstract mathematical reasoning were used. No actual source-instance evaluation is claimed. The only new artifact is this local independent audit. The main theorem is a necessary-condition result; the degree-60, genus-326, quadratic-deficiency-five branch remains unresolved.
