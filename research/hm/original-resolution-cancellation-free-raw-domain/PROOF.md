Editorial source note: filenames such as source-pins.json and inputs/ in the historical text refer to the original source edition. This mathematical edition records original and staged SHA256 values in SOURCE-BINDINGS.json; unavailable supporting source bindings remain explicit publication prerequisites, not asserted included files. Historical audit runs are not new checks.

# Cancellation-free raw-domain theorem

## Result

The literal frozen raw residual has the same carrier/legal bound **32/18** without using the historical complete-curvature bound **F <= 14/1**, without using transition-cocycle cancellation, and without identifying the implemented adjugate with a genuine inverse. Its literal J0–J3 lifts therefore retain **36/20, 42/23, 48/26, 54/29** and the existing cleared-suffix extension.

This is a new dependency elimination from the conditional raw-domain theorem, not a proof of all its geometric premises. Determinant one, the transition cocycle, complete raw closure, and contraction/HPL identities are still required wherever one identifies these literal expressions with geometric inverse transitions, a closed obstruction cocycle, or its cohomology class. They are not needed for the pole-counting argument below.

No production source or actual model arithmetic was executed. The accompanying checker uses only invented integer bound pairs.

## 1. Exact frozen expressions

All references in this note use immutable commit `491306fd2f7f8a04c29784afa48a6cb8a467f154` of `Akilleez-QA/read-em-and-weep`.

- [Raw engine](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-raw-regular-extension/inputs/raw_engine.py.txt): `Mat.inverse` returns the 2-by-2 adjugate, with no determinant division. `RawSource.T` returns the literal `s_raw` and inherits the other source methods unchanged.
- [Compiler, lines 178–197](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-raw-regular-extension/inputs/compiler.py.txt#L178-L197): the exact definitions of k, mu, mixed mu2, b, and F. In particular F is b minus one half the trace of the left-normalized mu term.
- [Compiler, lines 214–232](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-raw-regular-extension/inputs/compiler.py.txt#L214-L232): both E endpoint currents, all seven kinetic terms, all three negative gerbe terms, left normalization, both Fk branches, and both E branches.
- [Direct raw-domain proof, sections 2–4](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-raw-regular-extension/PROOF.md): the conditional direct raw block/scalar bounds and inclusion/HPL/outer-suffix ledger.
- [Independent review](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-raw-regular-extension/REVIEW.md): per-occurrence ownership, all-chart qualification, and exact suffix limitation.

Set A = g_ij, B = g_jk, G = g_ik. Throughout this proof write M# = adj(M), including where the frozen source spells the operation `inverse`. No equation G = BA or M# M = Id is imposed. Matrix words remain in their source order.

For a direction pair r = (a,b), the literal definitions are

    mu_r(B,A) = ((D_a B)(D_b A) - (D_b B)(D_a A))/2,
    k_r(M) = -((D_a M#)(D_b M) - (D_b M#)(D_a M))/4,
    u_r(M) = M k_r(M),
    F_r = b_r - tr(G# mu_r(B,A))/2.

Here b_r is the source's ordered scalar product (15/4) q_(a,ij) q_(b,jk). The E currents are L_d = A# D_d A and U_d = A# B# (D_d B) A. These formulas remain meaningful even before proving determinant one.

## 2. Retained premises and owner semantics

The precise pole inputs are as follows.

1. Each entry of the same literal g has the all-chart homogeneous carrier/legal bound **4/2**. Its first derivative has **5/3**, and its distinct-coordinate second derivative has **6/4**, in the correctly transported local frames. The geometric/homogeneous interpretation of these inputs is retained; a finite affine estimate alone is insufficient.
2. Each normalized q has **0/1**, with its legal factor owned by an endpoint actually present. The literal raw scalar has **10/2**, and its complementary derivative has **11/3**. The direct proof derives these from block **5/1**. That derivation still needs homogeneous primitive carrier bound 2, owned pivot divisibility, the physical U/Q denotations, complete log-frame and old-connection terms on all charts, and exact complementary-direction stripping. This note does not authenticate or reprove those premises.
3. Entries of the expression denote rational homogeneous sections of the assigned sheaves on all charts, with the stated ordinary sum, ordered product, trace, adjugate, and derivative semantics. Constants introduce no poles. Derivatives of a product obey the complete Leibniz rule. The all-chart derivative certificates apply to the products used below. In particular the raw scalar pair directions and the E derivative directions are disjoint.
4. The same literal original-resolution inclusion adds at most **4/2**. Each undifferentiated End homotopy adds at most **6/3**. Restrictions retain every previously selected owner and add no poles. These are retained bounds on the literal operations; their identification as a homological contraction is a separate semantic obligation.
5. For the final global extension, the assigned J_s coefficient twist is **-s-2 in each coordinate**. The carrier/legal sections have their actual homogeneous multidegrees. The target-tag correspondence and local partition factorizations used in section 5 are retained.

Rank-two adjugation preserves these local entrywise pole bounds, but under general GL2 changes of frames it also carries determinant-line factors. Local pole bookkeeping alone therefore does not prove that arbitrary adjugate residuals glue in the assigned sheaf. Actual all-chart assigned-sheaf compatibility is an independent retained premise of the global extension. Removing determinant one from the local arithmetic argument does not remove that compatibility requirement.

A pair (h,l) is a uniform bound **per owner occurrence**, not a maximum over different owners. For a tuple T, an entry is cleared by the product over v in T of H_v^h times the relevant legal factors ell_(v,i)^l. Equivalently, the pole allowance at a prime divisor is the sum of the multiplicity-weighted allowances of all these factors. Addition takes maxima within the same owner coordinate; multiplication adds allowances after owner lists have been aligned. A missing owner can be padded with allowance zero. Distinct occurrences remain distinct even if their labels or divisors coincide.

The scalar pair raw bounds and transition bounds may be padded to the full residual triple. Every source factor then has the indicated uniform allowance on that same tuple. This deliberately conservative convention justifies the simple pair arithmetic below.

## 3. Bound every literal branch, without cancellation

For a 2-by-2 matrix, the adjugate merely permutes and negates its four entries. Hence g# has bound **4/2**, Dg# has **5/3**, and distinct D2g# has **6/4**. This uses no determinant identity.

Consequently k has **10/6**. A complementary derivative of k differentiates one of its two first-derivative factors; it has **11/7**. Thus u = gk has **14/8**, and Du has **15/9** by either Leibniz summand. Equivalently the latter follows from the retained quotient-rule certificate on the combined product. Only distinct second derivatives are needed by the frozen mixed formula.

The entire integer ledger is:

| Literal expression | Carrier | Legal |
| --- | ---: | ---: |
| g or g# | 4 | 2 |
| Dg or Dg# | 5 | 3 |
| distinct D2g or D2g# | 6 | 4 |
| k | 10 | 6 |
| u = gk | 14 | 8 |
| Du | 15 | 9 |
| b = constant times qq | 0 | 2 |
| L = A# DA | 9 | 5 |
| U = A# B# (DB) A | 17 | 9 |
| F = b - tr(G# mu(B,A))/2 | 14 | 8 |
| Each Fk branch | 24 | 14 |
| E summand using L | 20 | 8 |
| E summand using U | 28 | 12 |
| Each normalized u-u kinetic term | 32 | 18 |
| Each normalized first-bidifferential kinetic term | 24 | 14 |
| Normalized mixed-second-bidifferential term | 16 | 10 |
| Each unsimplified normalized b-u gerbe term | 18 | 12 |
| Unsimplified normalized b-b-G gerbe term | 8 | 8 |

In detail, F is bounded directly by

    max((0,2), (4,2) + (5,3) + (5,3)) = (14,8).

Therefore Fk <= (14,8)+(10,6) = **24/14**, already below 32/18. The historical finer F14/1 certificate is unnecessary.

The literal transported current U has **17/9** without substituting any cocycle identity; multiplied by the raw complementary derivative **11/3**, it gives **28/12**. The untransported L summands give **20/8**. No current-difference cancellation is needed.

All seven kinetic terms and all three gerbe terms remain present before trace-free projection. Their normalized bounds are, respectively,

    u-u:    (4,2) + (14,8) + (14,8) = (32,18),
    D-u:    (4,2) + (15,9) + (5,3)  = (24,14),
    D2-D2:  (4,2) + (6,4) + (6,4)   = (16,10),
    b-u:    (4,2) + (0,2) + (14,8)  = (18,12),
    b-b-G:  (4,2) + (0,2) + (0,2) + (4,2) = (8,8).

The seven kinetic slots consist of two u-u slots, four first-bidifferential slots, and one mixed-second slot. The three gerbe slots consist of two b-u slots and one b-b-G slot. Neither G#G=Id nor any trace cancellation is used. Trace and trace-free projection do not increase these entrywise bounds. Taking the maximum across the entire five-branch residual gives **R <= 32/18**.

This is an upper bound, not a claim that the actual expression attains either exponent, and not a claim that individual residual branches are closed.

## 4. Literal lift and homogeneous extension

The retained inclusion and undifferentiated homotopy bounds yield

    J_s <= (32,18) + (4,2) + s(6,3),   s = 0,1,2,3.

Thus the four certificates remain **36/20, 42/23, 48/26, 54/29**. The recurrence's pole count does not itself use its contraction identities or raw closure. Those remain necessary to derive the usual coboundary/class equations from the recurrence.

For each occurrence v put

    C_v = H_v^54 product_i ell_(v,i)^29,
    D_v = C_v product_i Z_(r(v),i)^5251.

The product over all occurrences of D_v clears every certified divisor of J3. No N14-generated standard denominator was used in this proof, so retaining standard exponent 5251 is conservative padding. Adding these regular clearing sections cannot invalidate the extension. The cleared degree in coordinate i is

    sum_v (54 deg_i H_v + 29 deg_i ell_(v,i) + 5251) - 5.

This is a sheaf degree derived from the assigned twist and every clearing section, not an affine rational numerator degree. Under the all-chart homogeneous premise, the cleared rational section has no divisorial pole. Normality of (P1)^4 extends it regularly. J3 uses six occurrences; its Cech boundary uses seven, retaining deleted-face owners and harmless additional padding. No six-owner bound for that boundary is asserted.

## 5. Exact retained suffix consequence

Let B be the inserted occurrences and A the original suffix occurrences of a prism term; all products count multiplicity. Suppose each inserted partition weight factors on its own standard chart as rho_b = C_b Q_b with Q_b regular. Put N = (product_(v in B union A) D_v) J3, now a regular homogeneous section by section 4.

Use the target intersection of the **full original input tuple**, including original prefix entries removed from the displayed suffix. The retained regular-cover construction gives every inserted b_i the standard tag r(a_i) of an original input entry. Consequently every inserted and retained-suffix Z factor is a unit on that target. The exact identity there is

    (product_(a in A) C_a)(product_(b in B) rho_b) J3
      = N (product_(b in B) Q_b)
          / product_(v in B union A, i) Z_(r(v),i)^5251.

Its right side is regular on that target. This proves the same **cleared suffix extension**, also for J0–J2 and restrictions. Inserted weights cancel only inserted carrier/legal factors. The original suffix factors must still be supplied. It does not extend an uncleared prism to the entire standard target. Standard tags cannot be borrowed from absent vertices.

## 6. What was removed, and what was not

Removed from this literal-domain proof:

- the historical complete F14/1 certificate;
- the cocycle simplification U = G^-1 DG - A^-1 DA;
- the normalized gerbe cancellations;
- determinant one as a requirement for bounding the implemented adjugate operation.

Retained: the same literal source formulas and exact arithmetic denotations; the all-chart homogeneous primitive, transition, q, raw-scalar and derivative inputs; physical moving frames and old connections; occurrence ownership; inclusion/homotopy bounds; assigned twists; partition divisibility and full-target tag correspondence.

Not established here: the primitive bound-2 certificate or actual contraction equations, actual all-chart model identity, determinant one, genuine inverse semantics, the transition cocycle, raw closure, HPL identities, geometric source/class comparison, any physical computation or detector value. A structural determinant-one theorem can independently close its geometric semantic obligation, even though this weaker bound proof does not need it.

The accompanying arithmetic mutations reject an unsupported substitution of the finer F14/1 certificate into this coarse ledger, omission of outer normalization, and a larger input for which 32/18 no longer follows. The first control does not refute F14/1 when separately proved; it confirms that this ledger neither proves nor needs that sharper certificate. These controls test finite integer bookkeeping only. They are not a program verifier, actual-model counterexamples, or evidence that the retained geometric premises hold.
