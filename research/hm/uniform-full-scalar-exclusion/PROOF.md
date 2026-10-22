# Uniform nonvanishing of the actual fourth-square scalar

## Statement and exact dependencies

Work over C in the actual canonical source family, with the physical-center-even convention of the cited papers. Put

    A=Sym^2 W, H=D5=Sym^4 U,
    rho4:A x H -> T=Sym^8 U tensor Sym^2 W.

Here H is the irreducible five-dimensional positive source representation. The theorem is

    rho4(a,h) != 0 for every a != 0 and every h != 0.       (1)

The inequality means a NONZERO GLOBAL SECTION, not a section that is nowhere zero on the physical quadric Q. The full scalar, rather than only its modular leading class, is essential to the proof.

The exact dependencies are:

1. [PR696, 958244d6d9d3b326f66c073a9d669717c953ec32](https://github.com/Akilleez-QA/read-em-and-weep/blob/958244d6d9d3b326f66c073a9d669717c953ec32/research/hm/scalar-parameter-descent/PROOF.md): the ACTUAL intrinsic rho4 is a Gamma-equivariant polynomial of bidegree (3,1) with values in T. The representation H=D5 is irreducible. This is an actual-family statement, not merely the description of a space of possible equivariant families.
2. [PR747, 0a0ee30a5142477e54245b7c6f22d561abb4f5f1](https://github.com/Akilleez-QA/read-em-and-weep/blob/0a0ee30a5142477e54245b7c6f22d561abb4f5f1/research/hm/source-family-fourth-square-exclusion/PROOF.md): in one fixed rational source frame, let k=C(L), V=(k[X,Y]/(f3))_8 and d=[d2]!=0. The map K:H->V is C-linear and extends k-linearly to all positive quartics. For every source pair,

       K_actual(a,h)=a^2(a K_h-L_can(a,h)d).             (2)

   The pair, first-normal lift, V and d stay fixed as a and h vary. All global a are represented in the same rational trivialization, and nonzero a is nonzero in k.
3. [PR713, 5b3943980ecaef78ee7f56fbc015d40955fb24f0](https://github.com/Akilleez-QA/read-em-and-weep/blob/5b3943980ecaef78ee7f56fbc015d40955fb24f0/research/hm/leading-vertex-obstruction/PROOF.md), sections 2 and 4, as used in PR747: K_actual is a further modular reduction of the actual fourth-square scalar class. Thus rho4(a,h)=0 implies K_actual(a,h)=0. The reverse implication is NOT used or asserted.
4. [PR764, 961202467b714be787811f331534659122f761fe](https://github.com/Akilleez-QA/read-em-and-weep/blob/961202467b714be787811f331534659122f761fe/research/hm/noncube-source-exclusion/PROOF.md): for every regular leading pair and every first-normal nilpotent lift, K(H) subset k d forces the leading cubic f3 to be geometrically a pure cube. Its passage from H to all quartics is justified by k-linearity and the fact that H spans that space over k.
5. [PR765, ba8d389d56aee132a196c6f749de097323879d74](https://github.com/Akilleez-QA/read-em-and-weep/blob/ba8d389d56aee132a196c6f749de097323879d74/research/hm/actual-cubic-noncube/PROOF.md): the ACTUAL cubic is not geometrically a pure cube over k. Its section 1 suffices here; its stronger fiberwise and discriminant conclusions are unnecessary. This uses the actual cubic relation subbundle and the inequivalence of Sym^2 W and Sym^2 U, rather than an actual coefficient or source evaluation.

## 1. Every full zero pair must lie over a proper linear source space

By dependencies 4 and 5,

    K(H) is not contained in k d.

Consequently

    H0={h in H : K_h belongs to k d}

is a proper C-linear subspace of H. Indeed k d is a C-linear subspace of V and K is C-linear. Neither finite C-dimension of V nor Gamma-stability of H0 is needed.

Suppose a and h are nonzero and rho4(a,h)=0. Dependency 3 and (2) give

    a^2(a K_h-L_can(a,h)d)=0 in V.

Cancellation of the nonzero element a of the field k yields

    K_h=(L_can(a,h)/a)d in k d.                       (3)

Therefore every full zero pair has its positive source h in H0. The quotient in (3) is a rational function in k; no claim that it is constant is needed.

## 2. Equivariance and irreducibility exclude every full zero pair

Suppose, for contradiction, that rho4(a,h)=0 for some nonzero a and h. For every g in Gamma, actual-family equivariance gives

    rho4(g a,g h)=g rho4(a,h)=0.

Both g a and g h remain nonzero. Applying section 1 to EACH transformed pair, in the SAME fixed rational frame and with the SAME K and d, gives

    g h belongs to H0 for every g in Gamma.

Since H0 is C-linear, it contains span_C{g h : g in Gamma}. That span is a nonzero Gamma-subrepresentation of H. Irreducibility of H makes it all of H, contradicting the properness of H0. This proves (1).

Only the full global scalar is transformed equivariantly. We never transform K, d or V, never assert equivariance of reduction modulo f3, and never require H0 itself to be Gamma-stable. Reapplying the universal fixed-frame necessary condition to each transformed full zero pair is sufficient.

Equivalently, the full bad-positive-source locus in P(H) is Gamma-stable and contained in P(H0). A nonempty invariant projective subset of an irreducible representation spans the whole representation, so such a subset cannot be contained in a proper projective linear space. The direct orbit argument above avoids any need for a closedness or proper-projection argument.

## 3. Injectivity for every nonzero negative direction

For every nonzero a in A, dependency 1 makes

    H -> T, h |-> rho4(a,h)

C-linear. The theorem says its kernel contains no nonzero h. Hence this map is injective, with image dimension five, for EVERY nonzero a. This is a uniform structural consequence, not a selected actual matrix-rank test. No individual negative direction or positive source has been substituted or evaluated.

## 4. Every classified fourth lift has nilpotency index four

[PR687, 2874402c884a6b426cfd521a674c962a738f84a6](https://github.com/Akilleez-QA/read-em-and-weep/blob/2874402c884a6b426cfd521a674c962a738f84a6/research/hm/fourth-square-invariance/PROOF.md), sections 2 and 5, gives for every classified even fourth lift

    J4^2=q^3 S4 Id,    J4|Q=a^3 h N,
    J4^3=q^3 S4 a^3 h N,    J4^4=0 on 4Q.

Here S4 is the section denoted sigma in PR687. By PR696's pinned scalar factorization, S4=a^3 h rho4. The nonzero source restrictions and (1), together with integrality of Q, give S4!=0. Since N is nonzero and B_Q is torsion-free, S4 a^3 h N is nonzero. The last-layer injection into the locally free module on 4Q therefore makes J4^3 nonzero. Thus EVERY classified even fourth lift at EVERY nonzero source pair has exact nilpotency index four. This resolves the index-two-or-four alternative of PR687 uniformly within the stated family, without evaluating a source instance. It does not address arbitrary unclassified changes of sources, marking or correction, and does not imply a nonzero beta4.

## Contribution and limits

This removes the exceptional positive sources left by the generic full-scalar conclusion of [PR762](https://github.com/Akilleez-QA/read-em-and-weep/blob/31f480f16257b2a512633034cb0b6ade215acf35/research/hm/full-scalar-generic-exclusion/PROOF.md). The full zero-pair locus in P(A) x P(H) is empty. The modular zero-pair locus need not be empty: vanishing after reduction is only a necessary, not sufficient, condition for full scalar vanishing.

The result concerns the fourth-square scalar of this actual canonical source family. It does not identify the separate fourth Bockstein beta4, whose fifth-neighborhood adjoint boundary has a further quotient modulo im(beta2). It proves neither a first-order obstruction nor a higher-order integrability or algebraicity conclusion. Nor does it assert that rho4(a,h) has no zeros as a section on Q.

This is an authored deductive proof, with independent review recorded separately, not a proof-assistant certification. It uses no selected actual coefficient, source pair, point, derivative, root, discriminant value or matrix, and no computation or scan. All nonvanishing and the fixed-a injectivity conclusion follow from the pinned structural inputs and the orbit-span argument.
