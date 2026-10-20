Historical mathematical review of the source manuscript. Its PASS verdict applies to that source proof under the stated hypotheses; it is not a new review of different proof bytes or a formal verification certificate.

# Independent audit: exceptional fiber cohomology

Verdict: PASS. Reviewed the source EXCEPTIONAL_FIBER_PROOF.md in full, including its precise relative-sheaf conclusion. The standing identification with the pulled-back normalized HM bundle and its natural deck/swap linearization is inherited from the source SOURCE_AUDIT.md, reproduced here as HISTORICAL-SOURCE-AUDIT.md.

## Checks

1. Independently consulted Boralevi, https://arxiv.org/pdf/math/0602002, for the normalized Chern classes, resolution convention and two unstable resolution types. The degree-zero generator and absence of negative generators give h0(E)=1, h0(E(1))=3 and h0(E(t))=0 for t<0. A divisorial zero of the unique section would contradict the last vanishing. Its zero scheme is consequently a regular zero-dimensional section scheme of length four, giving 0→O→E→I_Z(-1)→0. Nonemptiness follows from c2(E)=4.

2. Hom(I_Z(-1),E(t))=H0(E(t+1)) follows by extension into a locally free sheaf across the finite set and uniqueness on a dense open. Maps E→E(t), t<0, annihilate the distinguished section. At t=0 subtract the scalar action on H0(E). The three resulting endomorphisms factor through the section line, square to zero and are tracefree. Thus the claimed negative Hom dimensions and h0(End E)=4 hold uniformly in both unstable strata.

3. The Euler-sequence H0 map sends (a_i) to (sum a_i x_i)u, where u is the nonzero section of End E(-1). It is injective on the integral plane. Serre duality and T(-3)=Omega1 give the identical H2 vanishing for End E tensor Omega1. Riemann–Roch yields chi=2t²+6t-11 and mixed chi=-34; all five displayed cohomology triples follow.

4. Applying the audited finite pushforward decomposition gives End dimensions before trace subtraction. The scalar cohomology removes one (++ ) H0, one H1 from each mixed sector, and one (-- ) H2. This gives (4,128,4), deck H1 dimensions (31,33,33,31), and Euler characteristic -120. The natural product of the two odd cover generators is swap-even, so O(-3) is the odd summand. Its End contribution (0,15,4) loses one scalar H2, giving exactly (0,15,3). The stated upstairs Serre-duality sign is consistent with these splittings.

5. The relative projection is proper and smooth of relative dimension two, and the coefficient is a vector bundle, hence flat over the base. These hypotheses justify top-degree coherent base change: a local finite free cohomology complex can be truncated in degrees 0 through 2, and H2 is a cokernel, which commutes with residue-field tensor. Thus R2 tensor k(b) identifies with H2 of the fiber. Finite-group eigensplitting commutes with this operation in characteristic zero. Nakayama then identifies the set-theoretic support of the retained R2 summand exactly with the exceptional locus, with fiber dimension three there.

## Limits verified

The conclusion does not identify a globally extended R1 fiber with the exceptional H1 dimension 15. It does not determine the exceptional locus, its nonemptiness or dimension, torsion lengths, annihilators, scheme multiplicities, a rank-three bundle on its reduction, or any global/source obstruction value. Extra base and pair-exchange symmetries remain to be imposed. There are no outstanding corrections.
