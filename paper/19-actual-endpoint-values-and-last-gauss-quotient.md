# 19. Actual endpoint values and the last Gauss quotient

The lower endpoint contribution is now evaluated on two canonical inputs: one gives zero and the other gives a nonzero global cohomology class. This proves that the actual invariant normal line maps injectively into the two-dimensional space of quadratic endpoint families. It does not evaluate a fourth Bockstein. Separately, four of the five rank-two Gauss quotient shapes are excluded; the last shape has eleven necessary splittings left after a further nine-case exclusion.

This chapter records the published results through 22 October 2026, 06:18 UTC. It supersedes the endpoint and Gauss frontiers of Chapters 17 and 18 without changing their historical proofs. The generic section count remains four or five.

## 19.1 Which endpoint is being computed

Write T=H¹(B_Q(−2))^G for the one-dimensional invariant normal space. The actual endpoint is the quotient of the positive part of the lower source,

    Cplus/J = P4 = H¹(L,Wprime O_L(−3)).

The last identification is restriction to the vertex open followed by the lowest filtration quotient. It is not full restriction: full H¹ restriction is injective, and the discarded D5 survives in higher filtration. Omitting the lowest projection would therefore change the mathematical map. [Endpoint quotient][QUOTIENT].

This lower P4 is distinct from the copy P4=H¹(B_Q(4))₊ used in the third obstruction. The actual third Bockstein remains identically zero. A nonzero lower endpoint need not survive the next ambient division and final fourth quotient.

## 19.2 Actual comparison and the retained corrections

The nonzero nilpotent trace and lowest diagonal from Chapter 18 identify the actual normal input with c_eta times an explicit invariant apolar cocycle at its lowest relevant degree, where c_eta is nonzero but not assigned an absolute numerical value. The cocycle has diagonal class 4/z in its apolar normalization and comes with compatible scalar trace lifts. [Apolar representative][APOLAR].

The two input operators are compared separately with the actual cone operators, on both complete regular charts and under the physical determinant-normalized root transport. Conic corrections and section-preserving ambiguities start too high in the filtration to change this degree-four operation. This is an actual operator comparison, not an inference from the dimension of an equivariant Hom space. [Compatible operators][OPERATORS].

The corrected secondary formula retains both the equation-unit term and the trace-lift subtraction:

    τ(γ₄) = L₄(η₈) − δK,
    q(Kᵢ) = T₄(nᵢ),
    L₄(E) = H DE + [A,E] + HρE,
    T₄(s) = H Ds + us.

The component-constant shadow cancels against the scalar null-homotopy. The nilpotent shadow does not disappear: its degree-twelve trace lift contributes to the degree-four tangent class. Dropping Kᵢ would compute a different operation.

## 19.3 The two actual values

For the canonical square a=t², use z=t/s and the normalized abstract C5 eigenvectors X,Y. The [integrated endpoint theorem][ACTUAL] gives

    q_eta(t²,X⁴)  = 0,
    q_eta(t²,XY³) = c_eta · (3k/(Bc)) [Y/z] ≠ 0.

Here B,c,k and c_eta are nonzero symbolic quantities in the fixed actual conventions. No coefficient instance or parameter point is selected, and the formula does not choose an absolute scale for the normal generator.

For X⁴ the full corrected cochain is a regular O(−3) coboundary. For XY³ the exact cochain identity is

    γ₄ = 3kY/(Bc z) + z⁻³ γ_y(−1/z) − γ_x,

with regular γ_x and γ_y on their respective complete charts. The global dual section Y*⊗1 has residue 3k/(Bc), which is nonzero. Thus the second assertion is nonvanishing in global cohomology, not just the appearance of a nonzero local term. [Square cancellation][ZERO]; [nonzero residue][NONZERO]; [independent comparison audit][AUDIT].

## 19.4 Fixed source identification and the kernel theorem

The positive source must be transported by the already fixed identification I_f, not silently replaced by a binary-quartic model. Its exact values are

    I_f(X⁴)  = 20736 B²c s t³,
    I_f(XY³) = 5184 ABc² t⁴.

Both lie in K_a at a=t². They give the mixed and pure square-kernel lines, respectively. A zero on the mixed input alone does not identify a vanishing named symmetric or alternating channel.

The construction is linear in η, quadratic in a and linear in the source h. The target family space has dimension two, with decomposition

    Sym²A ⊗ D5 = 1 ⊕ A ⊕ V ⊕ 2P4 ⊕ 3D5.

The second value in Section 19.3 proves that the actual map

    T → Hom_G(D5, P4 ⊗ Sym²A)

is nonzero. Since T is a line, its kernel is zero. This is a kernel theorem for the lower endpoint family, not for the fourth obstruction.

## 19.5 No whole endpoint fiber vanishes

Mr. Slop's [PR662 theorem][BASELOCUS] proves the structural whole-fiber detection statement. The new [actual corollary][DIRECTIONS] discharges its previously unevaluated hypothesis: for every nonzero invariant normal direction η and every nonzero parameter a, the entire map q_eta(a,−):D5→P4 is nonzero.

Indeed, polarization identifies the family with a nonzero equivariant map from D5_parameter into Hom(D5_source,P4). Irreducibility makes that map injective. The trace-free tensor (a⊗a)₀ is nonzero for a≠0: otherwise the rank-one endomorphism aaᵗ would equal a scalar identity of rank zero or three. This argument includes isotropic a.

Combining the actual nonzero family with Mr. Slop's [PR661 square-secant detection][SQUARE] also proves that its restriction to K_a is nonzero at every nonzero square. Neither assertion says that each individual source vector has a nonzero value. No all-direction nonsquare secant nonvanishing, actual fourth value or full-normal-connection determination follows.

## 19.6 Four quotient shapes excluded

The separate extremal (3,1) Gauss rank-two dual-image branch previously had five possible first-quotient shapes. The complete [new exclusion][SIXTWO] rules out (n,e)=(6,2), in addition to (4,2),(6,4),(8,4). Only (8,2) remains in that branch.

The argument follows actual saturated Gauss kernels inside the constant ambient thirty-space. A nonzero negative-degree saturated subbundle cannot have zero derivative, because its Grassmann classifying map would then be constant in characteristic zero and the bundle would have degree zero. Exact Hom supports force successive complete evaluation kernels until a nonzero negative-degree core has no allowed derivative, a contradiction.

At a nonzero map supported on a source line, the next quotient is that actual source line even if the map has zeros. Replacing it by the saturation of its image in the displayed target would give an incorrect next derivative target. No rank-three condition is imposed after the plateau has ended.

## 19.7 Eleven necessary splittings in the last shape

For (8,2), the [positive-tail reduction][TWENTY] leaves twenty possible splittings of K, of rank fourteen and degree −58. These are K splittings, not the same objects as the earlier quotient/type pairs. The prior sequence 140→77→73→63→42→21 therefore must not be continued as a single same-unit count by appending twenty and eleven.

Let b be the multiplicity of Wprime in H⁰(K(3)); this is the integer called a in the Gauss source, not the quadratic parameter a above. Eleven splittings have b=1 and nine have b=2. The [doubled-sector exclusion][DOUBLED] removes all nine b=2 cases. Their actual next kernels have four shapes, organized as

    Qalpha = (V⊕P4)(−4) ⊕ Wprime(−5) ⊕ L,
    Qbeta  = T6(−3) ⊕ Wprime(−5) ⊕ L ⊕ O(−10),
    L = O(−8)⊕O(−10) or W(−9).

The low Wprime map is an isomorphism. The high-map cases then descend through forced evaluations to negative-degree cores with zero allowed derivative. In Qbeta, the established H⁰(E^{---}(3))=0 forces the quintic component to act; no horizontal splitting is assumed.

Eleven b=1 candidates remain necessary, not realized. The full (8,2) shape, the rank-one dual-image branch and the entire (3,1) profile remain unresolved. Generic SF≥3 and positive-square rank≥27 are unchanged.

## 19.8 Evidence and the remaining task

The endpoint proof is supported by explicit regular cochains, the actual filtration and operator comparisons, a global dual residue, and the fixed source identification. The integrated verifier reruns the two secondary computations and actual two-input comparison, then checks both source identities and canonical kernel equations. The no-direction verifier checks universal trace-free tensor identities. The Gauss verifiers check exact characters, Hom supports, kernel degrees and lift ranges; the saturated-kernel and invariant-divisor arguments remain geometric proofs.

The remaining task is the actual next ambient division, with its compatible normal-coordinate scale and lift data, or a dual certificate retaining that information. The fourth obstruction has not been evaluated. The four-or-five section theorem, finite exponent range 4–31 or permanent cokernel, and the unresolved original source-recovery, lifting and algebraicity goals are unchanged. No formal proof-assistant certificate is claimed.

Public supplementary checks:

- [Integrated actual endpoint verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/verify_actual_endpoint_normal_variation_nonzero.py).
- [Whole-direction tensor verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/229e621948e9f6d80902080ad227993da3f0dced/research/hm/order-four-quadratic-load/verify_actual_endpoint_no_direction_zero.py).
- [Complete (6,2) exclusion verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/verify_extremal_31_first_remaining_quotient_exclusion.py).
- [Doubled-sector exclusion verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/229e621948e9f6d80902080ad227993da3f0dced/research/hm/order-four-quadratic-load/verify_extremal_31_doubled_gauss_exclusion.py).

## Pinned sources

[ACTUAL]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/ACTUAL-ENDPOINT-NORMAL-VARIATION-IS-NONZERO.md
[QUOTIENT]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/ACTUAL-ENDPOINT-QUOTIENT-IS-LOWEST-VERTEX-COHOMOLOGY.md
[APOLAR]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/ACTUAL-LOWEST-NORMAL-CLASS-HAS-AN-APOLAR-REPRESENTATIVE.md
[OPERATORS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/ACTUAL-TWO-ENDPOINT-INPUTS-HAVE-COMPATIBLE-CONE-OPERATORS.md
[ZERO]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/UNIVERSAL-HOMOGENEOUS-ENDPOINT-SECONDARY-SQUARE-CANCELLATION.md
[NONZERO]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/UNIVERSAL-HOMOGENEOUS-ENDPOINT-SECONDARY-XY3-NONVANISHING.md
[AUDIT]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/ACTUAL-TWO-INPUT-ENDPOINT-VALUES-INDEPENDENT-AUDIT.md
[DIRECTIONS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/229e621948e9f6d80902080ad227993da3f0dced/research/hm/order-four-quadratic-load/ACTUAL-LOWER-ENDPOINT-HAS-NO-WHOLE-DIRECTION-ZERO.md
[SIXTWO]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/EXTREMAL-31-FIRST-REMAINING-QUOTIENT-EXCLUSION.md
[TWENTY]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/EXTREMAL-31-LAST-REMAINING-QUOTIENT-REDUCTION.md
[DOUBLED]: https://github.com/Akilleez-QA/read-em-and-weep/blob/229e621948e9f6d80902080ad227993da3f0dced/research/hm/order-four-quadratic-load/EXTREMAL-31-DOUBLED-GAUSS-EXCLUSION.md
[BASELOCUS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/f75a18fd411350adda35dedf18751eee002a39bc/research/hm/endpoint-base-locus-exclusion/PROOF.md
[SQUARE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/1325647fd916bf2daa71b11efeae6d52cfefa2cd/research/hm/endpoint-square-reconstruction/PROOF.md
