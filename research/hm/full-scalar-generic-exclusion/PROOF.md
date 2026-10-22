# Generic positive sources have no full fourth-square exceptional negative direction

## Statement and immutable dependencies

Work over C in the actual canonical marked HM family. Let A=Sym^2 W be the irreducible three-dimensional negative-coordinate representation, H=D5 the five-dimensional positive-source representation, and T=Sym^8 U tensor Sym^2 W the 27-dimensional full scalar target. The two three-dimensional representations Sym^2 W and Sym^2 U are not identified.

**Theorem.** There is a nonempty Zariski-open subset U_good of P(H) such that for every [h] in U_good and every nonzero a in A, the actual intrinsic fourth-square scalar rho4(a,h) is a nonzero global section. In addition, for every nonzero a in A the linear map h↦rho4(a,h) is nonzero.

The second assertion is proved first; the first assertion then follows by resolving both alternatives of the existing modular-gate dichotomy. Neither assertion evaluates a selected actual source or negative direction.

The exact inputs are:

1. [PR696, polynomial parameter descent](https://github.com/Akilleez-QA/read-em-and-weep/blob/958244d6d9d3b326f66c073a9d669717c953ec32/research/hm/scalar-parameter-descent/PROOF.md), commit 958244d6d9d3b326f66c073a9d669717c953ec32, sections 1–3: the ACTUAL intrinsic rho4 is a Gamma-equivariant polynomial map A×H→T, of bidegree (3,1). A is irreducible. This is stronger than merely listing the possible equivariant families. Fixed Reynolds-averaged linear splittings construct actual polynomial lifts; PR687's choice independence makes their last-layer square intrinsic; unique division by the universal source multiplication gives the equivariant polynomial rho4 without source denominators.
2. [PR747, actual source-family exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/0a0ee30a5142477e54245b7c6f22d561abb4f5f1/research/hm/source-family-fourth-square-exclusion/PROOF.md), commit 0a0ee30a5142477e54245b7c6f22d561abb4f5f1, sections 1–3: in one fixed rational negative frame, with k=C(P1), a fixed k-vector space V, d≠0 in V, and gamma≠0,

       K_actual(a,h)=a^2 Phi_h(a),
       Phi_h(a)=a K_h−gamma S_h(a)d.

   K:H→V is C-linear, and h↦S_h identifies H with the trace-free self-adjoint endomorphisms of A for its invariant nondegenerate apolar form B. For every h≠0, Phi_h:A→V is a NONZERO C-linear map. Write E_h=ker_C Phi_h.
3. [PR713, leading-vertex obstruction](https://github.com/Akilleez-QA/read-em-and-weep/blob/5b3943980ecaef78ee7f56fbc015d40955fb24f0/research/hm/leading-vertex-obstruction/PROOF.md), commit 5b3943980ecaef78ee7f56fbc015d40955fb24f0, sections 2 and 4, as imported in PR747: nonzero K_actual implies nonzero actual global rho4. Thus rho4(a,h)=0 implies Phi_h(a)=0 for nonzero a,h. The converse is NOT an input.
4. [PR760, rational pole strata](https://github.com/Akilleez-QA/read-em-and-weep/blob/d798dceb77b94b5dbb9457fb303984e595ce1874/research/hm/rational-pole-strata/PROOF.md), commit d798dceb77b94b5dbb9457fb303984e595ce1874, sections 2–3: either Y_K={ [h]:E_h≠0 } is a proper closed subset of P(H), or there is a unique [a0] such that a0∈E_h for all h. In the latter branch the sources with dim E_h=2 are exactly the smooth plane conic X=j(P(a0^perp)), and outside X one has E_h=C a0. Its pinned dependencies are PR752 at e0d0cb31fbef5c7d6f1148e2278fbce115239dcf and PR759 at 8688c748e3a655a6db793c4b96504aaafb55cbc9.

No Gamma action on the chosen quotient V=(k[X,Y]/(f3))_8, and no equivariance of K, Phi, or the modular gate, is assumed.

## 1. No universal full-scalar exceptional negative direction

**Lemma.** For every a0≠0 in A, rho4(a0,−):H→T is a nonzero linear map.

**Proof.** Linearity follows from bidegree (3,1). Suppose instead that rho4(a0,h)=0 for all h. For any g∈Gamma and any h∈H, full-scalar equivariance gives

    rho4(g a0,h)=g rho4(a0,g^{-1}h)=0.

Fix any h≠0, without selecting or evaluating an actual instance. Every g a0 is nonzero; input 3 and cancellation of the nonzero element (g a0)^2 in k imply

    Phi_h(g a0)=0  for every g∈Gamma.

The C-linear span of the orbit Gamma a0 is a nonzero Gamma-stable subspace of the irreducible A, hence is all of A. Because Phi_h is C-linear, it must therefore vanish on all of A. This contradicts input 2 for h≠0. The assumption was impossible. ∎

The argument transports full-scalar zeros before passing to the modular gate; it never transports a modular zero by a presumed quotient action. It also never claims rho4 itself is linear in a: only Phi_h is used for the orbit-span step.

Consequently, for every fixed [a]∈P(A), the source locus where the full scalar vanishes is the proper projective linear subspace P(ker rho4(a,−)), possibly empty. This is a new exclusion in the opposite quantifier order from PR747.

## 2. Excluding all negative exceptions for a general positive source

Apply input 4.

If Y_K is proper, then for [h] outside Y_K no nonzero a belongs to E_h. Input 3 gives rho4(a,h)≠0 for EVERY nonzero a. Thus P(H)\Y_K is a nonempty open good-source set.

Otherwise let [a0] be the unique common modular direction, and let X be the conic in input 4. By the lemma the linear map L0:H→T, L0(h)=rho4(a0,h), is nonzero. Thus P(ker L0) is a proper closed projective linear subspace of P(H). Define

    U0=P(H) \ (X union P(ker L0)).

This is nonempty: P(H)=P4 is irreducible, X has dimension one, and P(ker L0) is proper, so their union cannot be all of P4. For [h]∈U0, any full-scalar exceptional a would belong to E_h=C a0 by input 3 and the conic exclusion. Write a=c a0 with c≠0. Homogeneity then gives

    rho4(a,h)=c^3 rho4(a0,h)=c^3 L0(h)≠0,

a contradiction. Hence every [h]∈U0 has no full-scalar exceptional negative direction. This proves the theorem in both alternatives, without deciding which alternative the actual modular map K occupies. ∎

The modular common-direction certificate of PR761 may therefore remain unevaluated without blocking this full-scalar conclusion. In its common-direction branch, the bad full-scalar source locus is contained in the union of that conic and a proper linear subspace.

## 3. Intrinsic closed bad-source locus

The bidegree (3,1) of rho4 makes

    Z_full={([a],[h])∈P(A)×P(H):rho4(a,h)=0}

a closed incidence locus. Projection P(A)×P(H)→P(H) is proper. Therefore its image B_full, the set of sources admitting at least one full-scalar exceptional negative direction, is closed. Section 2 shows it is proper. One may thus take the intrinsic maximal good-source open set

    U_good=P(H)\B_full.

Full-scalar equivariance also makes Z_full and B_full Gamma-stable. This conclusion again uses only the full scalar, not equivariance of the modular quotient. The statement holds over C at the family level; no coordinates of a good h or exceptional direction have been produced or evaluated.

## 4. Conditional dimension bound in the common-direction branch

**Corollary.** If the modular common-direction branch of PR760 holds, then dim B_full≤1 (allowing the empty locus).

**Proof.** Section 2 gives B_full⊂P(ker L0) union X, where X is a conic and ker L0 is proper. Section 3 makes B_full Gamma-stable. Suppose an irreducible component C of B_full had dimension at least two. For every g∈Gamma, the irreducible set gC is contained in P(ker L0) union X and cannot be contained in the one-dimensional X. Thus gC⊂P(ker L0). The nonzero vector subspace spanned by C is consequently contained in

    intersection_{g∈Gamma} g^{-1}(ker L0).

This intersection is Gamma-stable and proper, since it is contained in ker L0. But H=D5 is irreducible, as in the representation inputs of PR696, so the intersection is zero. This contradicts the nonempty projective component C. ∎

This bound is conditional only on the common modular branch; it neither selects that branch nor computes any actual source value. It strengthens the properness of B_full to dimension at most one in that branch.

## 5. Contribution, verification, and strict scope

The first step rules out a negative direction at which the full scalar vanishes for every positive source. The second combines this with PR760's sharp modular dichotomy to prove a uniform conclusion over ALL negative directions at each general positive source. Merely interchanging the quantifiers in PR747 would not justify this: the orbit-span lemma and the common-direction theorem supply the missing argument.

Here “nonzero scalar” means a nonzero global section in T, not a section without zeros at physical points of Q. The result concerns the actual fourth-square scalar of the classified canonical lift family, independent of the allowed completion/lift choices. It is not a claim about every arbitrary fourth-neighborhood endomorphism.

The separate beta4 fifth-neighborhood adjoint boundary modulo im(beta2) is not identified with rho4. No beta4 value, higher-order integrability, first-order obstruction, or algebraicity claim follows here. The physical-center-even and extra Serre involutions remain distinct.

Verification is deductive: exact parameter descent, orbit-span irreducibility, the one-way modular implication, the complete two-branch argument, and proper projective projection. No selected actual HM coefficient, point, derivative, source pair, matrix rank, model scan, or large computation is used. This is a written proof, not a proof-assistant formalization.
