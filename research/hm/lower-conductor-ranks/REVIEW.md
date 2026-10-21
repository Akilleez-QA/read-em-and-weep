# Independent review: lower primary conductor ranks

Verdict: PASS for the structural mathematical deduction from the pinned actual-geometry inputs, with the bibliographic corrections listed below incorporated. Reviewed 2026-10-21 UTC. This is independent mathematical review, not formal verification or a new verification of every upstream geometric theorem. No selected actual HM/source instance, coefficients, evaluation matrix, numerical rank test, or large computation was used.

## Sources checked

I read the full proposed PROOF.md and independently fetched these immutable repository sources through the read-only GitHub connector:

- PR591, 64a12e00718ec4cb09f17473237e879b08b28e16, research/hm/normalizer-residue-signs/PROOF.md.
- PR590, eb236dac3af8adcbc7f2f660b55e9d07904858c6, research/hm/degree-five-invariants/PROOF.md.
- PR588, 7547a6a0d84d29478a0bad2d30bda271c37c269e, research/hm/quadratic-conductor-generation/PROOF.md.
- PR592, 1a2822304e0e76d985f8a083fb36548127b881a1, research/hm/normalization-resolution/PROOF.md, including the exact Hilbert function and all-twist H1 vanishing in Sections 6–7.

I also inspected the local reviewed primary-conductor, eigenline-postulation and normalization-resolution proofs, and the primary Horrocks–Mumford (1973) text, especially Section 1, Lemma 2.4(ii), Lemma 3.3(ix), and the Appendix on printed p81. The primary source is https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf .

## Actual linearization and the multiplicity character

PR590 provides an actual ambient-pullback N-linearization of the normalization sequence, not just a symmetry of thirty points. Its construction by the unique lift of automorphisms to normalization applies in every degree. Consequently all images used in the proof are genuine N-submodules.

For primitive central weight, the Heisenberg isotypic equivalence is valid: evaluation identifies V_n tensor Hom_H5(V_n,T_n) with T_n. The normalizer acts on this Hom space by conjugation, and H5 acts trivially. Thus the multiplicity space is an honest K-representation, not a projective representation or an arbitrarily chosen Weil extension.

For one five-node orbit, the stabilizer H_p has order 25 and the induced fiber representation has dimension five with the required nontrivial central character. It is therefore the unique irreducible of that character. Evaluation at the fixed node is the appropriate Frobenius reciprocity isomorphism to Hom_Hp(V_n,F_n). It is equivariant for every normalizer lift fixing the point. A direction-stabilizing lift can always be adjusted by H5 to fix the point; the multiplicity action is unchanged by that adjustment.

The two fixed-point scalars must be divided, not merely copied from the branch fiber. The branch quotient contributes -1 under m, while O(n) contributes (-1)^n. The e0 eigenline in the standard five-dimensional representation contributes -1. Hence the multiplicity character is (-1)^(n+1)/(-1)=(-1)^n. The unipotent contributes 1 throughout. Galois conjugation and dualization preserve the rational scalars 1 and -1. Central lift ambiguities cancel between the two factors. This independently verifies the central technical step of the proof.

## Character and source checks

For even n the induced multiplicity is the doubly transitive six-direction permutation representation 1+J5. For odd n it is the induction of the reflection-sign character of D5. I independently checked its A5 character (6,-2,0,1,1): involutions fix two Sylow-five directions and have sign -1 at both, order-three elements fix none, and order-five elements fix one. This is exactly the sum of the two distinct three-dimensional irreducibles. In particular the negative-parity two-dimensional representations do not occur in this target.

Lemma 3.3(ix) really gives h1 theta(h1)=(chi3+chi2') theta^3(h1), where theta squares the primitive fifth root. Central weights add as 1+2=3=2^3 modulo 5. Its Galois conjugates therefore identify the actual P1 tensor Q2 with V3 tensor (one three-dimensional constituent plus one spin two-dimensional constituent). This is not inferred from dimension 25. Identifying Q2 with the standard extension is legitimate: two extensions of the same irreducible H5-module differ by a character of K, and K is perfect. The degree-indexed V_n notation in the draft is explicitly distinguished from HM's Galois indexing.

## Rank and cohomology deductions

The degree-three multiplication image is the actual rho3 image by the pinned quadratic-generation equality. Only one multiplicity constituent is shared between source and target, with multiplicity one on both sides. Its dimension is three, so Schur's lemma allows rank only zero or fifteen. The independent positive lower bound excludes zero.

In degree four the target has two irreducible N-constituents of dimensions five and twenty-five. Semisimplicity permits image dimensions only 0,5,25,30. The prior lower bound removes 0 and 5. A linear form avoiding the finite support propagates full conductor surjectivity from degree four to degree five, so r5=29 excludes 30. Thus r4=25.

The resulting rank sequence is 0,0,5,15,25,29,30,30,... . Normalization cohomology gives h1(O_S(n))=30,30,25,15,5,1,0,... for n=0,1,..., and complete-section dimensions 1,5,15,35,70,126 in degrees zero through five. These arithmetic deductions are correct. The proof expressly avoids inferring ambient restriction isomorphisms from these coincident dimensions. It does not resolve ideal equations or syzygies, projective normality, the separate K4 map, higher lifting, or algebraicity.

## Bibliographic corrections incorporated

The initial draft cited the local folder name low-postulation as the public path at commit 7547a6a0; the correct public path is quadratic-conductor-generation. That commit is PR588, whereas the separate a1c77f79 eigenline-postulation pin should not be labeled PR588. The positive-twist normalization formulas should be attributed explicitly to the separate PR578 input rather than placed under PR574 alone. These were source-label corrections, not mathematical gaps in the argument. The author corrected both public path/PR labels and used the stronger separate PR592 pin for normalization vanishing and the Hilbert function. I read that immutable pin through the connector and checked the corrected draft. All review requests are resolved.
