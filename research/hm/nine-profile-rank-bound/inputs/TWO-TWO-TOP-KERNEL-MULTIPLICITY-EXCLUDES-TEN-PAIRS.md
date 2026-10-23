# Top kernel multiplicity excludes ten more (2,2) quotient pairs

## Result

The exact-kernel refinement left 1880 records and 34 quotient pairs. Applying the strict-top-slope lemma at the *actual top degree of each candidate kernel*, on both derivative towers, leaves 1221 records and 24 quotient pairs. The remaining defect distribution is 1064 records of defect zero and all 157 records of defect twelve.

This excludes ten quotient pairs, not the entire (2,2) profile. Surviving formal splittings are only necessary possibilities. No existence of a bundle extension or realization of a formal derivative is asserted.

## 1. Necessary injection at the kernel's own top degree

Use K=E^-, L=(Q*)^-, A=E/K, and B=Q*/L. Both E and Q* and their saturated Gauss kernels are subbundles of constant bundles. The actual second fundamental forms of K and L factor as

    beta_K: K -> A(-2),
    beta_L: L -> B(-2).

Let N be either K or L, with its corresponding quotient C=A or B. Write its equivariant splitting as

    N = direct sum over j >= d of R_j tensor O(-j),
    R_d nonzero, d >= 3.

The strict-top-slope lemma applied to N itself gives H0(N^-(d))=0. Equivalently the induced map

    R_d = H0(N(d)) -> H0(C(d-2))

is injective as a representation. Therefore, for every irreducible R,

    multiplicity_R(R_d)
      <= sum over (e,S) in C, e+d-2 >= 0
           multiplicity_R(S tensor Sym^(e+d-2) W).

Here repeated blocks of C are counted with repetition. The cotangent twist is -2 and is retained on each tower. All irreducibles involved are self-dual, as checked in the character model.

For completeness, why is a killed coefficient impossible? A nonzero vector in the kernel on global sections selects a negative line O(-d) in the top splitting block of N. It is a saturated direct summand of N. Its derivative modulo N is zero; its derivative within N modulo this line lands in (N/O(-d))(-2), whose degrees are at most -d-2. Thus this derivative is also zero. The line is horizontal in the constant ambient bundle, so has constant Grassmannian map and degree zero, a contradiction. This is a statement about constant top coefficients and global-section injectivity, not fiberwise injectivity of the derivative.

The earlier exact-kernel verifier imposed the special case at twist 3. That constraint is empty when R_3=0. The present test also imposes the necessary injection at d=4 or any larger actual top index. This is the source of the new exclusions.

## 2. A common certificate for the ten excluded pairs

For each of the ten pairs below, every exact-cohomology-compatible L splitting has top degree -4 and contains exactly two copies of V in H0(L(4)). However H0(B(2)) contains exactly one V. Hence beta_L cannot satisfy the necessary injection. Some splittings have an additional trivial-coefficient obstruction, but it is unnecessary.

All ten have defect zero, so B=A*(-2). They can be listed by A alone:

1. O(-10) + O(2) + O(4).
2. O(-10) + O(2) + O(6).
3. O(-10) + W O(3).
4. O(-10) + 2 O(4).
5. O(-10) + O(4) + O(6).
6. O(-10) + W O(5).
7. O(-10) + 2 O(6).
8. W' O(-3) + O(4).
9. W' O(-3) + O(6).
10. V O.

For the first seven, H0(B(2))=Sym^10 W. For the next two it is W' tensor Sym^3 W. For the last it is V. The exact character identities give V multiplicity one in each of these three representations. The compatible-kernel enumeration supplies the two V copies on the source side. The verifier separately checks this common certificate for every candidate L splitting in all ten pairs, not just an example splitting.

## 3. Record and splitting accounting

All 659 eliminated records fail the L-side condition. No record is eliminated solely by K, but K is not ignored: across the full input record list, 160 K candidates are removed (5478 to 5318), and 1811 L candidates are removed (4266 to 2455). These are candidate occurrences before discarding entire failed records, not counts of distinct bundle types. A record is retained only if at least one K and at least one L splitting pass. The compact output records the remaining 24 pairs and the ten eliminated pairs with explicit multiplicity certificates.

## Reproduction and scope

Run:

    python3 verify_two_two_kernel_top_multiplicity.py

Add --full to regenerate the separately named survivor file two-two-kernel-top-multiplicity-records.json. The compact output is two-two-kernel-top-multiplicity-summary.json. Inputs are the frozen exact-kernel-compatible record file and the read-only abstract character ring in verify_negative_vertex_scalar.py. The verifier records the input SHA-256 and checks that input content is unchanged.

Sources: TWO-TWO-EXACT-NEGATIVE-KERNEL-SPLITTING-REFINEMENT.md and NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md. The executable checks exact abstract character multiplicities and finite splitting identities only. It uses no actual HM coefficient, point, matrix, map evaluation, rank test, rank scan, or experiment. There is no rank-two degree argument via rank-one curves. The geometric injection lemma, rather than formal-map realizability, is the necessary-condition justification.
