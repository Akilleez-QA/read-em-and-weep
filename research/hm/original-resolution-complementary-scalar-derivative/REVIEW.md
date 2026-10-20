# Independent review: raw scalar character and complementary stripped derivative

## Verdict and reviewed version

**ACCEPTED.** For the displayed raw scalar in the declared product-root model, the character coefficient has line O_Y(-2e_a-2e_b), owned carrier vector (5,5), and owned legal vector (2,2). For d outside {a,b}, its invariant derivative has character {a,b,d}; the stripped coefficient is partial_x_d on a finite factor and **minus partial_t_d** on an infinity factor. It glues in O_Y(-2e_a-2e_b-2e_d), with sufficient owned vectors **(6,6)/(3,3)** on every standard product chart.

This closes the complementary-stripping premise for the actual raw scalar derivative slots in the accepted ownerwise pole ledger. No mathematical correction to the producer draft is needed.

The reviewed `PROOF.md` has SHA-256

    ffdcd74399b4265b126ed7ebf5530a369566f6a72d12e2912f3474f20de00601.

The reviewed producer checker has SHA-256

    c7d86675b53e343e1e16d8b16e965b26de4e1561bc53d984edb667ad54447f77.

Exact reviewed copies, source snapshots, accepted dependencies, and their hashes are preserved in this audit. Seven dependency snapshots were compared byte-for-byte with their accepted local originals, including the newly final raw-block review. The raw-block proof hash is 7fe40702b668068a85e3e7639b3c1b99dc80476c0778aa94592df0b516d1add9. The producer's final source-pin file contains seven authenticated snapshots. No fresh remote-source read is claimed.

The mathematical derivation denotation is the invariant field V. This review does not certify an arbitrary field implementation, normalized derivatives, higher jets, or machine arithmetic. It neither assigns the complete residual or terminal lift to a sheaf nor proves closure or an obstruction value. No physical source, model polynomial, actual matrix product, jet, detector, or residue was evaluated. Clearing exponents 54/29 and standard allowance 5251 remain unchanged.

## 1. Exact source leaf and ambient frame weight

I independently inspected the complete frozen raw scalar, its `s_raw` caller, q, `Mat.D`, the `RawSource.T` override, the constructor route into the lift, and the compiler's E and residual wiring. The scalar has four resolution contributions with powers (-1,1,3,5) and signs (-1,1,-1,1). Each contribution contains both ordered wedge traces and all four endpoint-linear trace terms. The outer factor is 1/4, each q-linear term has the additional k/2, and the final term is -15 q_a q_b/8. No endpoint or resolution term is absent.

The source uses `RawSource`, which inherits `SC.Source` but overrides T by the literal raw scalar. `source_and_lift` passes the same raw Mat object to that subclass and to `SC.Lift`, and passes `source.residual` into the lift. It therefore does not use the base compiler's different N14 solver construction for this leaf. `Mat.D` has the entrywise `.V(d)` body; this binds the syntactic operation without proving its backend semantics.

The degree-zero scalar interpretation is justified by the accepted product-root and raw-block theorems. In each fixed resolution degree, the ambient term is one N^k tensored with a constant vector space. Its End bundle consequently has no N-weight. A change from the actual legal frame e_m^k to the common rational frame multiplies every ambient basis vector by the same scalar nu_m^k, so conjugation of an End coefficient is trivial.

There is an inhomogeneous correction for each individual connection, and it must be retained on both sides. Writing U for the split columns and Q for their inverse, the common-frame split coefficient is

    -(V U)Q-k Vlog(nu_m) Id.

The old coefficient in that same frame is

    k alpha_m(V) Id-k Vlog(nu_m) Id.

Their difference is exactly the source block

    B=-(V U)Q-k alpha_m(V) Id.

The common ambient terms cancel; they were not discarded. The accepted product-root theorem also identifies q through the old-connection difference -k q/2. Thus products of the blocks at the two owners and their traces are scalar rational functions in the common ambient description. There is no hidden root-line or square-line weight in the raw scalar.

## 2. B and q each have the required pure character

The accepted raw-block theorem supplies the stronger coefficientwise statement

    B_(o,r)=z_r b_(o,r),   H_o^5 L_(o,r) b_(o,r) regular,

where z_r=y_r on a finite factor and z_r=u_r on an infinity factor. It proves this directly from transported homogeneous primitives and the retained logarithmic and old-connection terms. It does not divide an arbitrary cleared regular block by z_r at a branch point. This is the precise dependency needed here.

Its character is also visible in the source structure: the primitive coefficients depend only on base coordinates, all legal multipliers in the split columns and rows are integral powers of nu_m squared, and V_r of a base coefficient introduces exactly the odd factor in direction r. The old coefficient has the same single-direction character. At infinity the source/standard identity is U_source=c^(-w)U_A, Q_source=c^w Q_A with c=nu_m^2 tau_A. This includes the tau factor and both reciprocal scalings. The raw-block dependency supplies its complete all-chart clearance, so no finite-only block estimate is being promoted to a global one.

For q, the exact source gives delta_r=m_(j,r)-m_(i,r) and

    q_r=delta_r y_r/x_r.

Since u_r=t_r^2 y_r and t_r=1/x_r, its coefficients are delta_r/x_r on the finite chart and delta_r/t_r on the infinity chart. When the endpoint bits agree it is zero. Otherwise precisely one actual endpoint has bit one and the other has bit zero.

The finite pole is paid by the bit-one endpoint's legal factor x_r(x_r^2-1). The infinity pole is paid by the bit-zero endpoint's legal factor t_r. The bit-one infinity factor 1-t_r^2 is a unit at t_r=0 and cannot pay that pole. Multiplying by both endpoint legal factors gives delta_r(x_r^2-1) or delta_r(1-t_r^2), respectively. This is legal-one padding at each actual endpoint, with no carrier charge and no absent owner.

Every one of the seven scalar factor-word types has one odd factor in a and one in b. Since a and b are distinct, no square of an odd basis element occurs in any word. Trace, addition, and the resolution constants preserve character. The scalar therefore belongs to the single {a,b} character summand, allowing the usual possibility that some entries or the complete coefficient vanish.

## 3. Branch-safe coefficient extraction and its line

On a base chart with coordinate ring R, the curve product has coordinate ring

    S=R[z_0,z_1,z_2,z_3]/(z_r^2-f_r).

The four equations are monic quadratic equations in their separate z variables. Successive monic division gives S as a free R-module on the sixteen square-free monomials z_S. This is true at the branch divisors: it does not assume that f_r, y_r, or u_r is invertible. Localizing by the invariant carrier/legal factors preserves that free decomposition. In characteristic zero the {a,b} eigensummand is exactly R z_a z_b, with the same statement after this base localization.

The scalar coefficient is the R-linear projection onto the z_a z_b coefficient. Therefore if an invariant clearing product C makes C s regular, projection makes C sigma regular. This is the valid regularity argument. Literal division by z_a z_b in a branch local ring would not give it.

The raw-block and q formulas already construct sigma by removing the displayed distinct formal basis factors. Its families have bounds

    b_i b_j: (5,5)/(1,1),
    kappa b_i: (5,0)/(2,1),
    kappa b_j: (0,5)/(1,2),
    kappa kappa: (0,0)/(2,2).

Adding powers within each product and taking maxima only across summands gives (5,5)/(2,2). Thus on every chart

    C sigma is regular,
    C=H_i^5 H_j^5 product_r L_(i,r)^2 L_(j,r)^2.

The factors are the actual homogeneous sections with their own chart transitions. Equal carrier labels or coincident prime divisors do not remove either occurrence from this product.

On replacing a finite factor by its infinity chart, the odd frame changes by u=t^2 y. The invariant scalar itself has degree zero, so its coefficient changes by t^-2 in precisely an odd direction. Consequently sigma has line O_Y(-2e_a-2e_b), with weight zero in each complementary coordinate. This is a coefficient line obtained from the actual direct-image eigensummand, rather than a line inferred from affine parity alone.

## 4. Complementarity, the minus sign, and all overlaps

For d outside {a,b}, V_d kills z_a and z_b. On base functions, its expression is z_d partial_x_d on a finite factor and -z_d partial_t_d on an infinity factor. The exact product rule therefore gives

    V_d(z_a z_b sigma)=z_a z_b z_d partial_A,d sigma,

where partial_A,d is partial_x_d or -partial_t_d. This both establishes the new character and defines its coefficient without branch division.

No missing connection term arises: the transition for sigma depends only on a and b, so it is constant under differentiation in d. When switching the d factor itself, sigma_infinity(t)=sigma_finite(1/t) and

    -partial_t sigma_infinity=t^-2 (partial_x sigma_finite)(1/t).

The minus local sign is essential. This gives precisely the new O(-2) transition in d. Switching a or b commutes with the derivative because its transition factor is independent of d; switching the remaining coordinate adds no character factor. These single-coordinate statements generate the full sixteen-chart overlap compatibility, and independent integer controls also checked every ordered pair of charts.

The t^-2 overlap multiplier is not an extra infinity pole to append to the local derivative. It occurs where t is invertible and describes the output line frame. Local regularity on the full infinity chart must instead be proved directly from -partial_t sigma_A, which the next argument does.

If d equals a or b, the odd frame itself is differentiated and its transition is not constant. The displayed complementary rule then fails in general. Both the proof and the controls explicitly exclude that case; none of the actual E scalar slots requires it.

## 5. Owned quotient-rule clearance on the whole infinity chart

Because C sigma is regular on the affine base chart, write it as a polynomial N. Differentiating N/C retains both the numerator derivative and every denominator derivative. For named factors C=product_n F_n^e_n, each denominator-derivative term has the original exponents plus one at its differentiated factor. Therefore product_n F_n^(e_n+1) clears all terms simultaneously.

This statement holds for reducible factors and coincident divisors. The calculation differentiates each named factor with its full exponent; coincident occurrences still contribute additively to a prime-divisor valuation. Constant factors and coordinate-independent legal factors have zero derivative. A missing owner need not be inserted. Carrier factors must be differentiated because they may depend on all four coordinates, even when the character excludes d.

Applying this directly to the local C above gives

    H_i^6 H_j^6 product_r L_(i,r)^3 L_(j,r)^3 partial_A,d sigma regular.

Only the d-coordinate legal factors need their new allowance, but common legal allowance three is valid padding. The result is an upper bound, not a claim that each exponent is attained. There is no extra branch factor, standard infinity equation, affine v0 inverse, or third owner. In particular the named infinity factor t has curve valuation two; the section-power argument preserves that multiplicity rather than treating t as a curve uniformizer.

Together with the overlap computation, this proves the cleared derivative is a global section of its declared cleared output line. The conclusion is stronger than an affine quotient-rule estimate.

## 6. Exact E application and retained scope

The frozen residual uses p=(0,1) and q=(2,3), and includes E(p,q,t) and E(q,p,t). Within E, both T leaves use `solver_pair`, whereas all four scalar derivative slots differentiate in one of the two directions of p. Thus all eight slots across the two E branches are complementary to their scalar pair.

The accepted ownerwise rows (D s_jk)L and (D s_ij)U may consequently use the bound (6,6)/(3,3) on the scalar's original endpoints. The raw-block dependency has separately closed the imported B5/1 premise. Neither replacement changes the residual/lift numerical ledger or its clearing exponents.

The interpretation of V as the mathematical invariant derivative is still distinct from proving exact-field or normalized-jet implementation semantics. Complete residual assigned-sheaf membership, closure, HPL/class comparison, terminal scalar-kernel attribution, and any obstruction or detector values remain outside this scalar theorem. Acceptance here does not silently supply those additional arrows.

## 7. Independent controls and replay

`check_independent_scalar.py` reads only inert text/AST and performs integer or formal-word metadata operations. It authenticates twelve reviewed files, binds six complete function bodies, checks raw-subclass inheritance and the exact Mat/residual/lift route, verifies eight scalar derivative slots.

It separately checks:

- 256 deck-character sign entries and sixteen distinct square-free characters;
- four common-ambient connection cancellations and 64 squared-legal parity entries;
- all 84 scalar word/direction characters;
- all 16,384 q owner/chart/mask/direction cases;
- all 6,144 ordered full-chart overlap cases for complementary triples;
- ten named denominator factors and all eleven quotient-rule term types;
- the scalar and derivative occurrence vectors, including coincident-divisor contributions.

Nineteen active negative controls reject deleted scalar endpoint or qq terms, reversed q orientation, substitution of the base solver, an altered E scalar slot, wrong raw derivative direction, an omitted common-frame old term, branch inversion, wrong scalar character, repeated directions, same-pair differentiation, the wrong infinity sign, a missing line shift, both incorrect local q donors, an absent q owner, both derivative undercharges, and owner merging.

Normal and optimized Python reports are byte-identical. The checker uses explicit exceptions rather than removable assertions. The producer checker was read in full and replayed in both modes after its final dependency addition; those reports are also byte-identical and match its final receipts. Its seven source pins, 16,384 q cases, 384 chart/triple cases, 1,536 single-switch cases, and thirteen rejection controls pass.

These controls authenticate syntax and discriminate bounded metadata mistakes. The free-module, frame, line-transition, and quotient-rule arguments above provide the mathematics. No test evaluates a physical scalar or proves arbitrary software semantics.
