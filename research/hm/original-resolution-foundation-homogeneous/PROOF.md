# A source-bound homogeneous primitive carrier theorem

## Result

For the exact pinned primitive matrices, interpreted by the homogeneous dictionary explicitly prescribed in the public source, every entry of I, P, H0, H1 is cleared by the square of its OWN carrier section. In fact:

- On primary carrier c, h_c alone clears every such entry.
- On the auxiliary carrier, a² clears every such entry, where a=v0 v1 v3 v4.
- Auxiliary power one is genuinely insufficient. The literal second-row entry P[1,8] is the homogeneous rational section −v1/v0², so its order along the generic divisor v0=0 is two.

This replaces the imported historical 451-entry homogeneous-clearing receipt by a short common-denominator theorem, bound to all literal numerator and denominator records. No primitive matrix product, polynomial expansion or evaluation, physical source, jet, detector, or historical executable checker was run. No external files were changed.

The primitive bound is already global in the prescribed homogeneous model. It is not inferred from finite affine regularity. The finite structural contraction identities also extend to these homogeneous maps by their consistent degrees and uniqueness from the dense v0≠0 chart. This last consequence uses the separately proved structural identities, not a historical A receipt.

## 1. Authenticated convention and exact scope

The pinned model has SHA256 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926 and Git blob fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761. Its finite decoder uses denominator di for I, dp for P, and dh for H0 and H1. The three denominator records coincide on each carrier. All eight input snapshots, their immutable source URLs, SHA256 hashes and Git blobs are listed in source-pins.json.

The following are source DEFINITIONS, rather than premises inferred from a successful run:

1. [Public frames-and-poles, §1](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-support-certificates/frames-and-poles.md) assigns homogeneous weights +1 to gamma, delta, ev; −1 to H0, H1, eta; (0,1) to the two I columns; (0,−1) to the two P rows; and zero to W,L. It explicitly prescribes the homogenization below and the primary/auxiliary carrier factors.
2. The [inert homogeneous source](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-primitive-contraction-bridge/inputs/verify_homogeneous_identities.py.txt) spells out exactly the same rat and primitive conventions. Its model's canonical JSON SHA256, b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2, agrees with the present pinned JSON; this is checked without importing the source. Its test outcomes are not used.
3. The [inert divisor-seed source](https://github.com/Akilleez-QA/read-em-and-weep/blob/dc60a859a0157b1d2d1b57b37324509abc22c600/research/hm/current-scalar-geometric-dependencies/checks/verify_divisor_seeds.py) uses those same degrees, denominator keys and carrier factors. We replace its cancellation-dependent clearance step, rather than replay it or assume its claimed result.
4. The [inert chart source](https://github.com/Akilleez-QA/read-em-and-weep/blob/dc60a859a0157b1d2d1b57b37324509abc22c600/research/hm/current-scalar-geometric-dependencies/checks/verify_chart_and_lines.py) defines the coefficient map by the binary product ∏(1+x_i z), with the factor t_i+z on an infinity chart. Section 5 proves the chart equality directly from those factors, without its expansion-based checker.

The model, public frames-and-poles and refined-domain sources were also read at PR79 head 6b5a14cbc1484c1d638c9d41039807dd8f80d173; their Git blobs are unchanged. This statement concerns those verified files, not any later branch.

The degrees are part of the prescribed bundle model. They cannot be recovered uniquely from finite rational functions alone. We authenticate and use this particular dictionary; we do not claim that an arbitrary physical implementation must use it. Root-line existence, legal-frame identification, transported old connections, exact arithmetic implementation and residual/class comparison remain separate questions.

## 2. Common-denominator homogenization lemma

Let p(u1,...,u4) and nonzero d(u1,...,u4) be polynomials; let D=deg d and n=deg p. For an integer M≥deg p, write

    hom_M(p) = Σ_alpha c_alpha v0^(M−|alpha|) v1^alpha1 ... v4^alpha4.

This is a polynomial homogeneous of degree M. The source's homogeneous rational entry of assigned degree w is

    R_w(p/d) = hom_(D+e+w)(p) / [v0^e hom_D(d)],
    e = max(0,n−D−w).

For p=0 the entry is zero. Suppose a common integer K satisfies K≥D and n≤K+w. Then e≤K−D and

    R_w(p/d) = hom_(K+w)(p) / [v0^(K−D) hom_D(d)].              (1)

Proof: every exponent in hom_(K+w)(p) is nonnegative by n≤K+w. Multiplying the source numerator and denominator by v0^(K−D−e) gives (1), because

    hom_(K+w)(p) = v0^(K−D−e) hom_(D+e+w)(p).

This is a termwise identity of exponent shifts, not an appeal to rational cancellation or a computation of products. The coefficient of each literal monomial is unchanged. Both sides have degree w and specialize to the same p/d at v0=1.

More intrinsically, every homogeneous rational function of degree w is uniquely determined by its v0=1 restriction, since on v0≠0 it is v0^w times that restriction evaluated at u_i=v_i/v0. The assigned w is essential to this uniqueness claim.

## 3. All literal degrees and denominators

The complete records contain 1,710 primitive cells: 451 nonzero and 1,259 zero. There are 619 term records in the nonzero cells. Each term is a coefficient and four nonnegative exponent integers. The metadata checker reads all of them, checks shapes and every denominator record, and tests the inequality n≤K+w separately for every nonzero cell. It creates no polynomial objects and does not evaluate any matrix.

The maximum numerator degrees, in column/row order, are:

| Carrier | I col 0 | I col 1 | P row 0 | P row 1 | H0 | H1 | D | K |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 |
| 1 | 5 | 6 | 5 | 4 | 4 | 4 | 5 | 5 |
| 2 | 5 | 6 | 5 | 4 | 4 | 4 | 5 | 5 |
| 3 | 5 | 6 | 5 | 4 | 4 | 4 | 5 | 5 |
| 4 | 5 | 6 | 5 | 4 | 4 | 4 | 5 | 5 |
| auxiliary | 6 | 4 | 4 | 5 | 4 | 5 | 4 | 6 |
| assigned w | 0 | 1 | 0 | −1 | −1 | −1 | | |

For every primary, the ceilings K+w are (5,6,5,4,4,4). For the auxiliary they are (6,7,6,5,5,5). Thus (1) applies to every primitive cell with the stated common K.

Write Π=v0v1v2v3v4, F_c=v_c^4−∏_(k≠c)v_k and h_c=v_cF_c=v_c^5−Π. The exact denominator records are:

    c=0:       d = u1u2u3u4−1,
    c=1,...,4: d = u1u2u3u4−u_c^5,
    auxiliary: d = −u1²u3u4.

Consequently the common homogeneous denominator in (1) is

    c=0:       v0 hom_4(d) = Π−v0^5 = −h_0,
    c=1,...,4: hom_5(d) = Π−v_c^5 = −h_c,
    auxiliary: v0² hom_4(d) = −v0²v1²v3v4 = −v0v1 a.           (2)

All equalities in (2) are the displayed two-term or one-term denominator identities. They do not require expansion of an actual primitive entry or any matrix product.

The model's gamma, delta and ev have 245 cells in total, of which 75 are nonzero. All their literal numerator degrees are at most one. Their prescribed degree-one lifts are therefore polynomial, as required by the same dictionary.

## 4. Clearing, sharpness, and the false affine shortcut

Let N=hom_(K+w)(p), a polynomial of degree K+w. Equations (1)–(2) give

    primary:   R=−N/h_c,
    auxiliary: R=−N/(v0v1 a).

Thus h_c R is polynomial on a primary. Since

    a²/(v0v1 a)=v3v4,

a²R=−v3v4 N is polynomial on the auxiliary. These are explicit homogeneous polynomial extensions, not merely an inference from absence of detected poles. They clear the same owner's factors; no unrelated carrier or standard-chart equation was introduced.

The primary H²-cleared degree is 10+w; the auxiliary a²-cleared degree is 8+w. Negative entry weights cause no problem, since all displayed numerator degrees after clearing are nonnegative. These are degrees of the prescribed homogeneous sections, not affine numerator-degree substitutes.

The exponent two on the auxiliary is necessary for a uniform bound. At zero-based cell P[1,8], the literal numerator is u1³u3u4 and denominator −u1²u3u4. The finite entry is −u1, but its prescribed degree is w=−1. Formula (1) therefore gives exactly

    P_aux[1,8] = −v1/v0².                                     (3)

At the generic point of v0=0 in P4, v1,v3,v4 are units. The carrier a has order one there, and (3) has order minus two. Hence a·P_aux[1,8] is not regular; a²·P_aux[1,8] is regular. This is a divisor-order argument with one literal monomial, not a point evaluation.

The same failure occurs on the actual product geometry of §5. On the chart with its first factor at infinity and the other three finite, the local product is (t1+z)∏_(i>1)(1+x_i z). Along t1=0 it restricts to z∏_(i>1)(1+x_i z), so v0=t1, v1 restricts to 1, and v3,v4 are units at the generic point of that boundary. Thus the pulled-back entry (3) still has order minus two, while its own auxiliary carrier a has order one.

The independent literal cell I_aux[2,0], numerator u1^4u3² with degree zero assigned to the column, similarly has homogeneous expression −v1²v3/(v0²v4). It exhibits the same double v0 pole.

In particular the tempting auxiliary denominator −v1 a of degree five does NOT work uniformly: the degree-six I column-0 numerator, degree-five P row-1 numerator, and degree-five H1 numerator would require negative powers in their proposed polynomial numerators. The source's actual extra-v0 exponent reaches two. Its public warning that the auxiliary seed can require v0² is explained by these exact cells.

This also rules out the false implication “the finite chart is cleared by a, therefore the prescribed homogeneous entry is cleared by a.” On the finite chart v0=1, the very entry (3) is polynomial. Its assigned negative degree contributes an actual pole on the hyperplane omitted from that chart. The uniform a² theorem includes that hyperplane from the outset.

## 5. Actual product-chart dictionary, without the historical chart receipt

For four projective coordinates (X_i:Y_i), define v_j as the coefficient of z^j in the source-prescribed product

    ∏_(i=1)^4 (Y_i+X_i z).

Each coefficient is a section of O(1,1,1,1). The coefficient vector has no common zero: at every point the four binary linear factors are nonzero polynomials, so their product is nonzero. It therefore defines the usual coefficient morphism to P4. On the finite chart Y_i=1, v0=1 and v_j=e_j(x1,...,x4), matching the pinned source's descending elementary-symmetric update.

For an infinity subset S put t_i=1/x_i and tau=∏_(i∈S)t_i. The source's local product replaces 1+x_i z by t_i+z on S. The factorwise equality

    t_i+z = t_i(1+(1/t_i)z)

gives local_product = tau·finite_product after the coordinate substitution. Equating coefficients proves v_local=tau v_affine on all 16 standard charts at once. No coefficient product was expanded or numerically tested.

For a prescribed degree-w rational entry, homogeneity now gives

    R(v_local)=tau^w R(v_affine).

This is exactly the source-prescribed primitive chart law. A weight-w entry is a rational section of O(w,w,w,w); the I columns and P rows have their distinct weights. The h_c and a clearing sections have multidegrees (5,5,5,5) and (4,4,4,4), respectively. Pulling back the explicit polynomials from §4 proves the bound on every product chart, including their standard boundaries. The factors that vanish at infinity are already charged to the owner’s homogeneous carrier. No unowned v0 inversion and no ad hoc Laurent multiplier is appended.

The elementary maps are equally explicit: eta has entries 1/v_p; W has entries 1 and −v_r/v_p; L is constant. The primary pivot is p=c and the auxiliary pivot is p=0. Since h_c/v_c=F_c and a/v0=v1v3v4 are polynomial, each eta or W entry is cleared by its own carrier to power one. Their degrees are −1 and zero, respectively. The polynomial gamma, delta, ev need no carrier denominator. None of these UNWEIGHTED primitive statements introduces legal-line denominators.

This proves the primitive chart dictionary and its homogeneous pole bound for the actual declared coefficient map. It does not by itself construct or identify physical root-line frames nu, validate their connection transport, or derive physical legal bounds. The public 2d+p=0 relation may be used in that separate frame comparison only with its actual line-frame identification; it is not needed to prove the present primitive result.

## 6. Homogeneous extension of the newly structural contraction

The separate structural-primitive-A proof establishes the full finite contraction for these same decoded records. Exact copies of that proof and its independent review are in dependencies/, with hashes in dependency-pins.json; its full ingredient closure remains in the original structural-primitive-A package. It can now be read as a theorem about the prescribed homogeneous maps, without executing historical homogeneous tests.

A convenient twist convention on P4 is

    K^−1=O(−1)^5, K^0=O^15, K^1=O(1)^10, K^2=O(2)^2,
    C=O ⊕ O(−1).

Gamma, delta and ev have entry degree +1, hence map successive K terms. H0, H1 and eta have entry degree −1 and reverse those arrows. I:C→K^0 has column degrees (0,1), while P:K^0→C has row degrees (0,−1). W,L are degree-zero maps between O(1)^8 and K^1. A simultaneous common twist is harmless; this convention states relative degrees rather than identifying an additional physical root line.

Every finite contraction equation is homogeneous entry by entry in this convention. In particular:

    gamma H0, IP, H1 delta, Id15 all have degree zero;
    delta H1, eta ev, Id10 all have degree zero;
    H0 gamma and ev eta have degree zero;
    (PI)_(i,j) has degree w_j−w_i, where (w_0,w_1)=(0,1).

The off-diagonal entries of the last identity are zero, which is homogeneous of any degree. The side conditions delta I=0, P gamma=0, H0I=0, PH1=0, H0H1=0 and H1eta=0 likewise compare fixed-degree entries. Their dehomogenizations are exactly the already proved finite identities. Uniqueness of fixed-degree rational lifts from §2 therefore gives all these identities over Q(v0,...,v4), on the appropriate carrier localizations, and after pullback to the product charts.

For example the homogeneous A defect has degree zero in every entry and specializes at v0=1 to zero. On v0≠0 it equals that zero specialization at v_i/v0, so it is the zero rational matrix. This is not the invalid claim that a finite pole bound implies a homogeneous bound: identities of fixed homogeneous degree and regularity at a missing hyperplane are different assertions. The latter was proved independently in §§2–5.

No actual matrix multiplication is performed in this extension argument. It transfers a previously proved algebraic identity by a homogeneous type argument, with explicit source-bound degrees.

## 7. Dependency improvement and retained frontier

The cancellation-free raw-domain theorem retained “the same homogeneous primitives have owned carrier bound two” as an imported premise. Sections 1–5 discharge that premise for these exact records and the public dictionary, without the historical 451 cancellation checks. The [refined domain, §4](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-proof-foundations/refined-tracefree-pole-domain.md) uses precisely this conservative bound. Its numerical ledger and the later cancellation-free raw-domain bound 32/18 can retain their existing constants; the sharper primary bound is not needed to change them.

The §6 consequence separately removes the finite-to-homogeneous gap for the newly structural primitive contraction identities. That finite structural theorem has now received independent acceptance; the present packet still requires its own independent review. The pole theorem itself does not depend on A or on any contraction identity.

Still distinct: physical/root-line and old-connection identification, complete scalar and derivative frame comparisons, genuine source implementation semantics, residual closure and geometric class comparison, outer-domain target-tag/partition hypotheses, detector values, and obstruction/algebraicity conclusions. No claim about those follows merely from this denominator theorem, and none was evaluated here.

## Reproducibility and controls

Historical checker results are discussed below; no rerun is asserted here. Both produce the same metadata report. The checker authenticates all eight inert inputs, scans every primitive and regular-map cell, verifies literal denominator patterns, pivots and degree ceilings, and confirms the exact sharpness numerator. Four metadata controls reject the degree-five auxiliary shortcut, an incorrect negative P-row weight, an excessive numerator degree, and a common degree below the denominator degree. The handwritten auxiliary monomial-divisibility exponents are checked as integers.

These controls do not prove arbitrary program semantics or attest prior runs. Hashes identify the records, the complete degree scan supplies finite premises, and the handwritten common-denominator and chart arguments prove the homogeneous assertion. Independent review is requested before treating this packet as accepted.
