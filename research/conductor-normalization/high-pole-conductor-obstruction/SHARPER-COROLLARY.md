# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 06 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# Sharper cohomology: both retained coordinates admit simple poles

This corollary uses the separately proved positive-twist theorem in ../sharper-hm-regularity/SHARPEST-BOUND.md, with its primary-source verification and independent proof audit in ../sharper-hm-regularity/AUDIT.md:

    H1(B(t))=0 for t≥7,  H2(B(t))=0 for t≥2.

It does not rederive or independently source-audit that theorem; its cited companion audit supplies that verification. The original PROOF.md remains valid with its expressly weaker or conditional inputs; this corollary states the strengthened conclusions from the established sharper thresholds.

## 1. Universal pole bound one in both coordinates

F1=W*⊗B(−4) and F2=(W²)*⊗B(−3) satisfy

    F1(D)=W*⊗B(2),  F2(D)=(W²)*⊗B(3).

Both H2 groups vanish. On a compatible finite affine Čech cover, every regular two-cocycle in either coefficient therefore has a compatible meromorphic primitive with at most a SIMPLE pole along D. This is an existence theorem for all classes, not construction of the actual retained source primitives.

Moreover H1(F_i(kD)|D)=0 for each k≥2. Indeed its hypersurface sequence has outer groups H1(F_i(kD)) and H2(F_i((k−1)D)); for k=2 these are H1(B(8)),H2(B(2)) in the first coordinate and H1(B(9)),H2(B(3)) in the second, all zero. Larger k also vanish. Consequently EVERY given k-pole primitive with k≥2 can have its top layer removed by a Čech coboundary, keeping its differential fixed, until only a simple pole remains. This is stronger than merely selecting some simple-pole primitive.

## 2. The complete retained obstruction survives simple-pole principal parts

Let P_i,k=F_i(kD)/F_i. For k=1 the exact sequence is

    H1(F_i(D)) → H1(P_i,1) --∂→ H2(F_i) → 0.

Thus precisely

    H1(P_1,1)/im[W*⊗H1(B(2))] ≅ H2(F1),
    H1(P_2,1)/im[(W²)*⊗H1(B(3))] ≅ H2(F2).

The inherited ten and twenty retained conditions remain intact. Neither H1(B(2)) nor H1(B(3)) is known to vanish from the stated thresholds. These are image subspaces of the specified maps, not automatically injected copies of the groups.

At the common double-pole bound, both H1(F_i(2D)) and H2(F_i(2D)) vanish, so

    H1(P_1,2) ≅ H2(F1),  H1(P_2,2) ≅ H2(F2).

Naturality makes H1(P_i,1)→H1(P_i,2) surjective, with kernel exactly the corresponding image above. Thus moving to the double-pole presentation removes only the closed-meromorphic-cochain ambiguity. It does not remove any actual retained obstruction.

## 3. Sharpened conductor thresholds, with the endpoint distinction retained

Use the normalization resolution and notation in PROOF.md. Its controlling groups show

    H1(T,ν*(B(t)|D))=0 for t≥8,
    H1(D,B(t)|D)=0 for t≥8.

For the first assertion the middle H1 groups have twists t,t−1≥7, and the left H2 group has twist t−2≥2. For the second, H1(B(t))=0 and H2(B(t−6))=0 when t≥8.

Hence every global conductor section lifts to a global normalized section at t≥8, and every such high layer is cohomologically removable. This includes the first coordinate's second-pole layer at t=8 and the second coordinate's second-pole layer at t=9.

The more specific four-global-generator statement requires H1(B(t−2))=0, so its guaranteed range begins at t=9. In that range,

    im[H0(T,ν*B(t))→H0(Q_t)]
      =im[H0(B(t−1))^4→H0(Q_t)]=H0(Q_t),

and the exact global presentation is

    0→H1(B(t−6))→V_t→H0(Q_t)→0,
    V_t=coker[H0(B(t−2))^5→H0(B(t−1))^4].

The extra relations vanish for t≥13, so only there is V_t unconditionally equal to H0(Q_t) by these bounds. At t=8 the normalized-image statement is valid but the four-global-generator shortcut is not established. This endpoint distinction matters for the first second-pole layer and must not be silently erased.

There is a precise replacement at t=8. Let

    u=H1(j⊗B(8)):H1(B(2))→H1(B(6))^5,

where j:O(−6)→O(−2)^5 is the leftmost map of the Q resolution. Its quartic entries are, up to compatible signs and a common nonzero scalar, the five maximal minors of A generating the downstairs conductor ideal. The two kernel sequences, using H1(B(7))=0 and H2(B(2))=0, give

    0→ker(u)→V_8→H0(Q_8)→coker(u)→0.

Thus the missing four-generator sections at this endpoint are exactly coker(u), while all Q_8 sections still lift to global normalized sections. The stated thresholds do not decide whether u is surjective; no value or rank of this map is evaluated.

## 4. Remaining mathematical boundary

Both retained simple-pole layers are below these high-twist thresholds: they have t=2 and t=3. Removing them is precisely the original retained-class vanishing problem, modulo the closed simple-pole ambiguity described above. Normalization, conductor support or the existence of a simple-pole primitive provides no vanishing test for those classes by itself.

No minimality of the universal simple-pole bound is asserted for a specific source; a source with zero retained class has a regular primitive. No actual source, polynomial instance, selected rank or obstruction coordinate was evaluated.
