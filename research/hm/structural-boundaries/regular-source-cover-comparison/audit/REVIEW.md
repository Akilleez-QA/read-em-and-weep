# Independent audit: actual-source scalar comparison

## Verdict

**Accept the source comparison and its regular source primitive, with the explicitly pinned ordinary comparison as a separate theorem dependency.** The current proof supplies the missing bounded-domain comparison on the actual tagged legal/carrier cover. It does not merely exhibit an abstract quasi-isomorphism or a formal identity in a rational function field.

Reviewed source proof: `../regular-source-cover-comparison-20261018/PROOF.md`, SHA256 `1a4d478d18f564a50f4ccb82bcbdf39461da48b30e4998869a612a024a69b607`.

Ordinary comparison dependency: `../regular-cech-tensor-comparison-20261018/PROOF.md`, SHA256 `7ec48fb142cb5ee319a39507889aa01ed8588549e6af11239024f9ab1628893f`. This audit checked its all-ordered normalization appendix and the source proof's composition with it. It does not replace the companion packet's independent audit of the entire cubical/simplicial construction.

Two small issues found during review were corrected before this verdict:

1. The ownerwise bound packet retained the raw-block and complementary stripped-derivative premises. The source packet now separately pins the later proofs and reviews that discharge both premises, and section 3 cites them explicitly.
2. Restriction from an empty open does not determine a unique regular extension. The domain now explicitly takes empty components and their chosen cleared extensions to be zero. Nonempty principal intersections are dense in the integral standard target, so their extension is genuinely unique.

Final dependency delta accepted: ordinary section 7 now explicitly requires its hypothetical reverse map G to be a regular degree-preserving cochain map, with dG=Gδ, and η to be a regular degree-minus-one operator. This is a wording precision that makes the separate transport corollary's required hypotheses explicit; it does not change J_all, its homotopy or the source construction. The final ordinary independent review, SHA256 `512dbcd60c3a8aa9c9b37a8041ff6b12d43a34d077fdf19b4f7819b73c1f89fc`, accepts that final proof and is now the eighteenth pinned dependency. The source proof remains unchanged at the hash above.

No substantive mathematical defect remains in the reviewed source construction. All 18 pinned dependency files matched their recorded hashes. The producer's invented formal checker and this independent checker both passed normally and with Python optimization, with identical outputs in each pair.

## 1. Scope and evidence

This audit read the mathematical proof packets, their reviews and hash metadata. It independently derived the full ten-term owner ledger, the affine partition construction, the source-domain argument, the chain homotopy sign and the scalar primitive equation. It used only small invented tuple chains, rational partition weights and integer denominator vectors for executable checks.

No frozen source module, model constructor, actual matrix, actual polynomial instance, physical cochain, jet or detector was imported, evaluated or expanded. No Bezout coefficients were computed. 

The conclusions concern the exact frozen rational denotation under its accepted geometric and structural theorem inputs. A static mathematical argument is not a new certification of arbitrary arithmetic software or a successful physical run.

## 2. The full M ledger really includes the scalar first lifts

At each endpoint the established inputs are

    g, g^-1: 2/1; Dg: 3/2; D2g: 4/3;
    k: 6/4; s_raw: 5/2; Dk: 7/5; D s_raw: 6/3.

The derivatives of s_raw used here are complementary to its pair, exactly the scope of the later scalar-derivative theorem. The fixed mixed formula requires only the distinct-coordinate derivatives covered by the transition bounds.

For x=s_raw I+k, the bound is 6/4. Therefore the full lift U=gx has 8/5, while its derivative has 9/6: both (Dg)x and g(Dx) have that allowance. The scalar piece g s_raw has 7/3 and its derivative is no larger than the stated full bound. Thus no first-lift scalar or scalar-derivative contribution has been silently dropped by reusing the earlier scalar-free u=gk notation.

On the original ordered occurrences (i,j,k), the six families, with multiplicities 2,2,2,1,2,1, have:

| Left-normalized family | Carrier vector | Legal vector |
|---|---|---|
| G^-1 U_jk U_ij | (10,16,10) | (6,10,6) |
| G^-1 mu(U_jk,A) | (5,12,11) | (3,8,7) |
| G^-1 mu(B,U_ij) | (11,12,5) | (7,8,3) |
| G^-1 mu_pq(B,A) | (6,8,6) | (4,6,4) |
| G^-1 b U_ik | (10,0,10) | (7,2,7) |
| G^-1 b_p b_q G | (4,0,4) | (4,4,4) |

These are exactly ten slots. The middle charge in the first row is 8+8, not max(8,8). The outer normalizer contributes only at i and k; the scalar b contributes legal (1,2,1). All signs and the internal bidifferential alternatives preserve these upper bounds.

The maxima are carrier (11,16,11) and legal (7,10,7). Trace and division by 2 do not increase them. The full-M closure and full-sign character are separate accepted inputs: neither follows from a denominator estimate or from closure of the trace-free residual. Together with the all-chart membership and direct-summand character extraction, they establish c in S_D^2 and dc=0 for uniform per-occurrence 16/10.

Repeated owner labels are harmless only because occurrences remain distinct. The table is a position-indexed ledger. If several positions carry the same divisor, their divisor multiplicities add; no maximum or label deduplication is allowed.

## 3. Actual cover and existence of the weights

The source indices are the requested triples a=(standard tag A, carrier h, legal mask m). For each fixed A their opens are the principal opens of the actual local functions H_(A,h) times the four legal factors. The root theorem identifies the pullbacks with the actual legal/carrier owner opens on X.

The six homogeneous carrier opens cover over every residue field: simultaneous vanishing of all h_j with product v_j=0 would force every v_j=0; with product v_j nonzero, the auxiliary carrier is nonzero. The product coefficient vector is not zero because it comes from a product of nonzero binary forms. This is an algebraic cover proof rather than a numerical sample of points.

For a legal bit the local factor is 1 or x(x^2-1) on a finite chart, and t or 1-t^2 on an infinity chart. These are the correct homogeneous degree-one/degree-three representatives. The infinity pair has no common zero. Combining carriers with all masks gives a finite principal cover on each whole affine standard chart.

Consequently the ideal generated by C_a=H_a^54 product L_a^29 is the unit ideal in the polynomial ring over Q. Positive powers have not changed the principal opens. Either the maximal-ideal argument or descent along the explicitly free rank-16 curve algebra proves this claim. The argument is over Q; it does not require choosing complex coefficients and subsequently descending them.

Thus polynomial Q_a with sum C_a Q_a=1 exist, and rho_a=C_a Q_a has the exact needed divisibility. A fixed choice for each tag is made once and independently of f. This makes Pi and K linear operators, not input-dependent solvers.

The result is appropriately limited: it supplies existence-backed operator formulas parameterized by chosen witnesses, without computing their coefficients or imposing a degree bound. It does not identify these witnesses with previously prescribed witnesses. The numbers 54/29 here supply divisibility, not a bound on their degrees.

## 4. Actual line transitions and the bounded domain

The full-sign coefficient identification is branch-safe. The curve algebra is free with square-free odd basis, so projection to the full-character summand commutes with invariant localization and clearing. No regular function is divided by a vanishing y or u.

If lambda=tau_B/tau_A on a standard overlap, the full odd basis changes by z_all,B=lambda^2 z_all,A. Equality of the original scalar therefore forces f_B=lambda^-2 f_A. This is the actual O(-2,-2,-2,-2) coefficient law. Conversely z_all,A f_A glue to the full-character scalar on X. Restriction, differential and scalar multiplication all commute with these identifications.

Each source component is an intrinsic L-section on its source intersection. Its product with all occurrence factors D_a=H_a^16 product L_a^10 must extend to the **full intersection of the original standard tags**. That requirement is stronger than ordinary regularity on the source open, and it is what permits averaging.

For heterogeneous tags, each factor D_a is restricted from its own standard chart. Its conversion from a homogeneous common-chart representative differs by a unit on the full tag intersection: both chart equations needed for the change are invertible there. The same is true for the L-frame transition. Hence the all-common-chart bounds imply precisely the mixed-tag clearance required in the definition, without borrowing an absent tag or appending an unexplained infinity factor.

The domain is a subcomplex in every degree. A face's cleared extension is restricted to the smaller full tag intersection and multiplied by the missing occurrence's regular D. Summing faces preserves clearance. This argument uses no closedness assumption. The domain includes all ordered tuples and repeated indices; it is not an alternating subcomplex and does not discard a nonzero repeated component.

## 5. Pi and B have the stated regular targets

For each standard tuple, Pi sums over every choice of source owner with its matching tag. Every input occurrence receives its own weight. A summand is defined by

    product(rho_a/D_a) times the cleared numerator N_a.

Here rho_a/D_a=H_a^38 product L_a^19 Q_a is polynomial on the owner's standard chart. It follows that each summand, and hence Pi f, is regular over the entire standard intersection. There are no unweighted source suffix factors in Pi. Arbitrarily large but finite degrees of Q do not prevent regularity or later finite Laurent splitting.

The cochain identity follows by deleting a face and summing the absent owner's weight to one. Its equality is an identity of intrinsic sections; the unique regular extensions promote the dense-locus calculation to the whole target. This establishes dPi=Pi d on every S_D degree, not merely on c.

B is restriction along the tag map. It lands in S_D since a regular standard section multiplied by all D factors stays regular on that standard intersection. B commutes with d. Summing every weight separately gives Pi B=1, also on nonclosed and repeated-index cochains. No source open or tuple position is replaced by an unrelated tag.

## 6. The prism is regular and has the plus-K convention

The degree-lowering operator is

    (Kf)_(a0,...,a[n-1])
      = sum_i (-1)^i sum_(b0,...,bi) rho_b0 ... rho_bi
          f_(b0,...,bi,a_i,...,a[n-1]),

where b_j has the tag of a_j. The shared a_i is retained after b_i. The full original target source intersection is retained even when an original prefix no longer appears inside the displayed input component.

Its input tuple has the same full standard target as the output tuple: the inserted prefix reproduces the omitted prefix tags, and the seam tag is merely repeated. Its cleared numerator contains D for every inserted occurrence and every suffix occurrence. Multiplying the prism summand by all output D factors gives

    product_(j<i) D_aj times product_(j<=i)(rho_bj/D_bj) times N.

Every factor is regular on that exact full tag intersection. Thus K preserves the same bounded domain S_D. On the original source target, all output D factors are units, so the resulting cochain is regular there. This is not an assertion that the uncleared prism extends to the full standard target: retained suffix denominators are still real until paid by the output D factors.

If b_i equals a_i as an actual owner index, the input still has two occurrences. One is cleared by its weight and the other by the original output D. This correctly handles the repeated seam rather than merging its denominator charges.

For the sign, define p[a] as the weighted average over its tag fiber, and define the chain prism by sum_i (-1)^i[p a0,...,p ai,a_i,...,a_m]. Direct deletion telescopes to

    boundary h + h boundary = Id - p.

In degree zero, boundary sum_b rho_b[b,a]=[a]-sum_b rho_b[b], which unambiguously fixes the direction. Dualizing gives dK+Kd=Id-BPi. No alternating normalization is needed or allowed in this calculation. In particular the source primitive requires **plus Kc**.

## 7. Completion of the scalar primitive and exact limits

The standard ordinary complex receiving Pi is all-ordered. The companion construction explicitly passes to the alternating complex by restriction r to increasing tuples and alternating extension e, retaining the normalization homotopy t with dt+td=1-er. Its ordered operator is H_O=e J r+t. The normalization prism has support in the original vertices; consequently its regular-domain statement includes repeats and is stronger than a merely rational convention change.

The companion identity dH_O+H_Od=1-P_O has P_O supported in degree four. Since Pi(c) is closed of degree two, dH_O Pi(c)=Pi(c). Hence

    b=B H_O Pi(c)+Kc,
    db=B Pi(c)+c-B Pi(c)=c.

Both terms are in S_D^1. Inverting the full-character identification produces a regular scalar primitive beta on the original tagged source cover. The canonical scalar inclusion commutes with the row-End differential even though End(E) need not be a trivial bundle. Combining this with M-R=c I-d_row W yields

    M-R=d_row(beta I-W).

The minus sign before W and the plus sign before K are both required. An End-valued weighted averaging comparison is unnecessary for this source identity, because the scalar primitive was returned to the actual source cover before scalar inclusion was used.

This proves removal of the central difference. It does not prove the trace-free residual exact, determine any obstruction or detector value, construct a higher-order physical lift, or justify executing a formerly prohibited tuple. It also does not identify this tagged-cover primitive with a primitive on a coarser untagged cover without a separate descent assertion.

## 8. Independent controls and their strength

`check_independent.py` reads no input file. It uses two invented tag fibers with rational weights (2,-1) and (3,-2), so each fiber sums to one without positivity. It checks:

- 340 all-ordered source tuple cases through degree three, including 276 cases with repeated indices;
- differential square zero and the full prism identity on each case;
- 30 all-ordered standard tuple cases for the weighted-lift chain map and retraction;
- the independently rebuilt full ten-term ledger and its maxima;
- 42 occurrence-indexed carrier/legal clearance cases;
- active failures for the wrong prism sign, deletion of repeated tuples, and nonunit-sum weights.

The producer's separate checker uses invented symbolic partition variables rather than these numerical invented weights; it also checks omitted prefix weights, shared seams, merged charges and absent-tag/suffix mistakes. The two implementations therefore provide different finite convention controls. Neither computes actual witnesses or proves the imported geometry. The universal arguments in the reviewed proof and this review supply the mathematics; the controls detect the listed implementation or sign mistakes.

`normal.json` and `optimized.json` are identical. `producer-normal.json` and `producer-optimized.json` are identical. `producer-pin-check.json` records the successful 18-file SHA256 check. `reviewed-pins.json` identifies all bytes used for this review.
