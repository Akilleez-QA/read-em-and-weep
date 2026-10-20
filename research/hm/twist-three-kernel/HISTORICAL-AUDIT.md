# Historical mathematical review receipt

This receipt describes the original proof at its original hash below. It is preserved as historical evidence, not represented as a review of the normalized publication bytes. See PUBLICATION-CHECK.md for the independent final-publication review and its exact proof hash.

# Independent frozen-artifact audit

## Verdict

PASS for final PROOF.md SHA-256 `c28cbf3c492e82da32e38fd1c465ddcf848fe80f3c2b2ddc31378dd186cdb86a`. The earlier Sections1–5 draft was separately checked at SHA-256 `37d6807b934070de99c8a23b32700f9379b4fccfc094628dc1ae5508008bc0ed`.

Under the imported nonzero fifteen-section branch, the final proof establishes t=0, slope-semistability of K, global generation of K*, and a nonempty evaluation defect supported in dimension at most one. It does not establish section vanishing. The baseline proof SHA-256 was independently verified as `7f016e9e092e94d0f6f27bc39de2d5e367a4bfeb866bd72e74994f55fd6a18e7`.

## Checks

1. **Riemann–Roch:** Td(P4) reduces to 1+H^4 modulo 5, not merely 1. All relevant denominators (2,6,12,24) are invertible. The four roots of the Euler polynomial, its rank/24 leading coefficient, and comparison of its cubic and quadratic terms give a=2r and ch2=2r modulo5, hence c2=2r(r-1). This works for torsionfree HN factors without local freeness.
2. **HN geometry:** Uniqueness makes the first and all successive HN pieces equivariant. The center acts by the same scalar on their subquotients. Saturation is transitive here because both successive quotients are torsionfree. A saturated subsheaf of a locally free sheaf is reflexive on the smooth base. Later HN quotients need only be torsionfree. Once the first slope is strictly negative, all determinant numbers a_i are positive.
3. **Degree-one exclusion:** The elementary Grassmannian linear-space lemma in the elementary proof reproduced as [PLUCKER-LEMMA.md](PLUCKER-LEMMA.md) was read and checked. Its span bound excludes ranks3 and8 with a=1. Constant Plucker image excludes a=0. No assertion of global local freeness or everywhere-defined Plucker map is required.
4. **Quotient positivity:** Q=15O/A is genuinely globally generated and torsionfree. The general-section/depth argument in the proof establishes c2(Q)>=0. Independently, Bertone–Roggero arXiv:0804.2985, Theorem3, gives the needed inequality for torsionfree sheaves; nonnegative general-line splitting type yields c2(Q)>=0. Its stronger equality/splitting clause is not used. Thus c2(A)<=a^2 excludes both rank6 and rank11 with a=2.
5. **Equality theorem:** Chen arXiv:2205.12305 v4, Theorem1.14 (printed p9) and Proposition5.2 (printed pp31–32), were independently opened and checked. The theorem covers semistable reflexive sheaves; the identity resolution is applicable on P4. The filtration in its proof has equal slope. Projectively flat quotients on the entire smooth simply connected P4 have trivial projectivization, so are sums of a single line bundle and have integral slope. This excludes rank9, c1=-3, c2=4, whose slope is -1/3. No semistability of a general plane restriction is assumed.
6. **Exhaustiveness:** An independent combinations-based enumeration, rather than the author's recursive enumeration, gives precisely15 raw strictly ordered HN profiles. After the degree-one exclusions, the only profiles allowing positive defect before the later refinements are (11,2)+(1,7), with ch2 upper bound43/2, and (9,3)+(3,6), with upper bound13/2. The quotient positivity and equality exclusions leave exactly the five rows printed in Section4. Each has ch2 upper bound3/2, attained only at all the listed minimum c2 values. The independent script is audit_arithmetic.py. No selected HM computation is involved.
7. **Global-generation exclusion:** c(B(3))=(1,9,42,72) is correct. With the quotient projective-bundle convention, the top tautological intersection is c1^4-3c1^2c2+c2^2+2c1c3=-585. A globally generated tautological line bundle is nef and cannot have negative top self-intersection. This proves D is nonzero, not that it has a curve component.

## Sources reopened

- https://arxiv.org/pdf/2205.12305
- https://arxiv.org/pdf/0804.2985

## Separate audit of Section6 semistability upgrade

PASS. The negative-twist input has now been independently read directly on the primary page cited below: the unnumbered Decker–Schreyer proposition on printed p218 states H1(End(F)(k))=0 for all k<=-2, and its proof explicitly normalizes c1(F)=-1. Trace splitting supplies the B vanishing. Thus the m=1 concern in the preliminary audit is resolved by an actual theorem, not an assumption about a spectral-sequence map.

On regular P4, codimension at least three gives sheaf Ext^j(D,O)=0 for j<3. The two dual exact sequences therefore genuinely give 0->B(-3)->15O->K*->0. It follows both that K* is globally generated and that H0(K*(-m))=0 for m>0.

The final HN factors in all FIVE residual profiles were checked, including the rank3 final factor in the (9,3)+(3,6) profile. Rank1 has hull O(-2); the rank5, rank3 and rank2 cases have discriminant zero and slopes -1,-2,-2 respectively. Taking their reflexive hulls preserves semistability, decreases the discriminant by an effective codimension-two defect contribution, and hence still gives zero discriminant by Bogomolov. Chen's equality theorem gives line-bundle factors of the same integral slope; H1(O)=0 splits their extensions. A nonzero projection of K onto one of these line bundles contradicts the previously proved vanishing. This excludes every unstable profile and proves slope-semistability.

There is no circularity: t=0 is proved without semistability, which then permits dual exactness and the last-factor contradiction. The stopping boundary is respected: neither stability nor H0(B(3))=0 is asserted.

Additional primary source inspected as a saved page image:
https://gdz.sub.uni-goettingen.de/id/PPN243919689_0382?tify=%7B%22pages%22%3A%5B222%5D%2C%22view%22%3A%22info%22%7D

## Final presentation freeze

The final proof was reread at the hash in the verdict after presentation-only cleanup of dependency references and provisional delivery wording. The mathematical statements, bounds, all five HN profiles, dual-sequence argument, and conclusion are unchanged. No absolute workspace paths are used in this audit.
