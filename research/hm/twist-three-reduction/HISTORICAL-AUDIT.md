# Historical mathematical review receipt

This receipt describes the original proof at its original hash below. It is preserved as historical evidence, not represented as a review of the normalized publication bytes. See PUBLICATION-CHECK.md for the independent final-publication review and its exact proof hash.

# Independent audit of the twist-three reduction

## Frozen artifact and verdict

Audited file: PROOF.md in this directory.
SHA256: 7f016e9e092e94d0f6f27bc39de2d5e367a4bfeb866bd72e74994f55fd6a18e7
Audit date: 2026-10-20.

PASS, relative to the explicitly imported, previously audited HM resolution, cohomology table, and twist-two vanishing. The new argument proves H⁰End₀F(3)=0 or V₁⊗χ₃, with dimensions 0 or 15. Under the nonzero alternative, evaluation has generic rank three and no divisorial cokernel support, and the codimension-two defect degree is divisible by five. It does not prove which alternative occurs, nor kernel semistability.

The audit independently derived the spectral page and geometric congruences before reading the draft; checked the original HM PDF and its printed p.81 character table; and checked the final frozen Plücker argument. The auditor contributed a possible Plücker exclusion during drafting, so independence does not mean absence of collaboration on that step. Final verification below concerns the exact hash, not an earlier draft.

## Checks

1. Coefficient recovery. Twisting the section resolution by one leaves precisely W′⊗H⁴O(-7) in column -3 and D⊗H⁴O(-5) in column -2. Equivariant Serre duality gives H⁴O(-7)=Sym²V and H⁴O(-5)=C. Their kernel and cokernel are H¹F(1)=V₁⊗W′ and H²F(1)=0. Thus D=V₁⊗χ₄# follows from an actual exact sequence, not dimension matching.

2. Primary characters. HM Lemma 3.3(v),(vi) and the Appendix support Sym²V=V₁⊗χ₃′, S₃=V₁⊗(χ₅⊕W′), W′⊗χ₃′=W′⊕χ₄#, and W⊗χ₄#=χ₃⊕χ₅. All nine columns of the two Appendix tensor identities agree. In particular the spinorial χ₄# is not the coefficient χ₄ of O(-3). The χ₃ versus χ₃′ designation is correct. Irreducibility of V₁ tensored with each quotient irreducible follows from the H₅-isotypic equivalence, or Schur's lemma for H₅ followed by quotient equivariance.

3. Spectral indices. Tensoring by F*(3)=F(4) gives terms F(-4), F(-2), F(-1), and F⊕F(1), with the stated coefficients. The only E₁ entries are (-3,3) of dimension 10, (-2,2) of dimension 40, and (0,1) of dimension 115. In particular H⁴F(-4)=H⁰F(0)*=0 and the omitted rows contribute nothing. There are no incoming differentials to the two total-degree-zero terms. The only outgoing possibilities are d₂ from (-2,2) and d₃ from (-3,3), both into the stated degree-one position or its quotient.

4. Scalar permanence. The proof correctly uses the associated graded, not a nonexistent canonical embedding of hypercohomology into the direct sum of its E₁ entries. Finite-group semisimplicity makes constituent multiplicities additive across the filtration. The scalar V₁⊗W′ occurs only in the ten-space and the scalar V₁⊗χ₅ only in the forty-space, each once. Their known presence in H⁰End(F)(3) forces both to survive. Therefore d₃=0 and d₂ can act only on the irreducible V₁⊗χ₃. Trace splitting then identifies the trace-free sections with its kernel. No assumption about the unknown coefficient P or target multiplicities is needed.

5. Cohomology arithmetic. Only total degrees zero and one survive. The Euler characteristic of End(F)(3) is 10+40-115=-65, and removing χO(3)=35 gives χB(3)=-100. Thus the two (h⁰,h¹) pairs are (0,100) and (15,115), with higher cohomology zero.

6. Rank congruences. For the saturated evaluation image, det I=O(a) has a≥0 and a≡3r mod5. The central character comparison is valid because characters of N are trivial on its μ₅ center. The determinant inclusion extends across the complement of the codimension-one locally free locus. H⁰B(2)=0 implies vanishing in every lower twist by multiplication by a nonzero polynomial. Rank one would require a≤0 and a≡3 mod5, impossible. Rank two requires exactly a=1. The congruence alone does not exclude rank two, and the frozen proof does not claim it does.

7. Plücker exclusion. With a=1, wedge evaluation gives global linear forms, so its rational projective image has linear closure P^s, s≤4. The dense evaluation image consists of decomposable bivectors; closedness of the Grassmannian puts the entire closure inside it. The proof of the elementary linear-space classification is valid: pairwise intersecting planes either all contain one fixed line or all lie in one fixed three-space. Their total span has dimension at most s+2, hence at most six here. The annihilator of that span in the fifteen-dimensional section space would consist of sections vanishing on the dense full-rank locus. Such sections are zero, a contradiction. This argument does not require globally locally free I, a base-point-free linear system, or an unjustified choice of an equivariant common line.

8. Divisorial defect. Generic rank three makes the maximal minors nonzero sections of O(9). Their common divisorial factor is N-invariant and of degree at most nine. Since N has no characters, a defining equation is invariant, so its positive degree must be five. HM Theorem 3.5 excludes an N-invariant quintic. At each codimension-one DVR, absence of a common maximal-minor factor implies surjectivity; hence the cokernel really has codimension at least two, including scheme-theoretic generic lengths.

9. Kernel and numerical boundary. K is rank twelve and reflexive: its quotient in the trivial bundle is torsion-free, so the depth lemma gives S₂. The Chern character calculation yields c₁K=-9H and ch₂K=(3/2+t)H², where t is the nonnegative integer degree of the cokernel's leading codimension-two cycle. Therefore Δ(K)=c₁²-24ch₂=45-24t. If K is semistable, Bogomolov forces t≤1. The proof correctly leaves semistability unproved and makes no claim that this inequality forces vanishing.

10. Defect divisibility. The new final paragraph is valid. The cokernel inherits central character ζ²; after twist m every cohomology group has character ζ^(2-m). For four residues modulo five these groups have dimension divisible by five by the H₅ representation classification. The Euler characteristic is an integer-valued polynomial of degree at most two, with coefficient t in the binomial basis. Since its only possible denominator is two, reduction modulo five is well-defined and has four roots. Thus it is zero and 5 divides t. Combining this with conditional t≤1 forces t=0 if K is semistable; conversely positive codimension-two defect implies instability. Neither direction asserts semistability.

## Scope and remaining gap

The outstanding issue is whether the explicitly isolated irreducible δ₃ is nonzero. The evaluation restrictions constrain the zero-map alternative but do not contradict it. No selected HM/source instance, matrix rank, cofactor, pairing, polynomial value, or large computation was used in this audit. No external service was changed.
