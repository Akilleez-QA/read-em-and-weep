# Combined-inner regularized numerator certificate

## Result and precise scope

This supplies a reusable **explicit numerator identity for the complete inner solver on an arbitrary common edge**, including both signed prism families and the complete standard branch. The identity removes every inserted carrier/legal denominator before forming one derivative. It retains full owner occurrences and gives directly checkable monomial inequalities proving that the resulting numerator is polynomial in the common finite frame.

The new content is the combined formula (3), its owner-sensitive padding, and its exact branch and exponent predicates. The bounds 14/1/5250 and 15/2/5251 were already stated in the refined pole-domain note; they are not newly discovered here. This certificate supplies a reusable implication from the source-clearing identity to those bounds, not an independent verification of that source identity or a physical-source executable lowering.

No physical polynomial is read, expanded, evaluated, or sampled by the tests. Formal arbitrary functions are used only as independent controls of the displayed universal identities. No seed12/30 demand compiler is implemented or imported. No execution or global Laurent-admission flag is changed.

## 1. Source assumptions, with no hidden regularity conclusion

Fix a pair q=(0,1) or (2,3). Its character is n_i=-2 for i in q, zero otherwise. A complete owner is v=(seed, occurrence, carrier, legal_mask, standard_tag). Carrier5 denotes star; source-first sorting places star before primaries0,...,4. Legal bits are low bit i; standard bits are high bit 3-i. Restrict the same fixed partition weights throughout.

Let H_v be the owned carrier equation of degree d_v=4 (star) or5 (primary), and ell_vi the homogeneous legal equation of degree1 (mask0) or3 (mask1). Define

    C_v = H_v^14 product_(i in q) ell_vi.

The essential source input is the identity, for every actual source triple, with the pullback convention below,

    P_[u,v,w] = C_u C_v C_w F_[u,v,w],                  (1)

where P is a polynomial homogeneous section, with coordinate degrees at most217 in q and210 elsewhere. Brackets mean the alternating extension from the fixed source-first order. They do not mean that the nonlinear source is recomputed in a permuted order. There are two distinct zero predicates. A general alternating common-cover cochain vanishes on repeated (carrier,legal_mask,standard_tag). This particular input is the pullback s*F from the source cover and vanishes already on repeated SOURCE labels (carrier,legal_mask), even when standard tags differ. The source-first order makes repeated source labels adjacent; the transition-only proof Section2 establishes their zero value for both C and the gerbe b. The numerator P is then zero too. This stronger predicate is not applied to general common cochains. Neither predicate merges any five-field denominator owner: equal carrier equations at different actual occurrences remain separately owned.

The transition-only first-lift proof and the N14 finite-demand note assert (1), including cancellation of nonpair legal poles. This artifact assumes their source proof; it does not manufacture (1) from a Boolean field or from source hashes. The PR80 finite second-jet contract does not establish (1): it deliberately leaves rational derivatives and localization obligations and rejects infinity charts. Its model-chart index must not be silently reinterpreted as an external carrier ID.

Other imported facts are the fixed cover maps T=H_rho+R(K_cov Pi+A h S Pi), their signs, the polynomial N14 carrier quotient formula, and the standard branch's finite support [-1668,5248]^4. These are explicit mathematical premises. The construction below makes no assumption that individual raw differentiated summands are regular.

## 2. Inserted quotient, with frame conversion exactly once

The scalar partition weight rho_v has twist zero. Write R_v for its carrier factor, and L_vi for its legal factors. In the owner's local standard coordinates,

    R_v = H_v(local)^14 Qcarrier_v,
    Qline_vi = L_vi / ell_vi(local)   for i in q.

These quotients are polynomial definitions, not inversions. In finite coordinates Qline=(1,0). At infinity Qline=(t,1), while the raw nonpair weights are (t^2,1-t^2). Thus even zero finite mask1 branches never divide by a vanishing equation.

In the common finite frame x, define the Laurent polynomial

    Qhat_v = Qcarrier_v(local(x))
             product_(i in q) Qline_vi(local(x))
             product_(i not in q) L_vi(local(x))
             product_(i:e_vi=1) x_i^[-14 d_v-deg(ell_vi)[i in q]].

Then, as an exact identity of restricted rational functions,

    rho_v / C_v = Qhat_v.                              (2)

The monomial multiplier in (2) comes from homogeneous divisor pullback. No pair twist is appended: it is already carried by P and F. No section twist is attached to rho.

### Checkable per-owner reversal bounds

The N14 carrier quotient has infinity coordinate degree at most481. At an infinity coordinate in q:

- mask0: negative exponent magnitude at most 481+1+14*5+1=553;
- mask1: magnitude at most 481+0+14*5+3=554.

At a complementary infinity coordinate the bound is 481+2+14*5=553. Star degree4 only improves these. In finite coordinates Qhat has no negative exponents. These are deliberately conservative; no occupied support is asserted.

Consequently a factor x_i^5250 assigned to the designated output owner clears each inserted Qhat, with at least4696 exponents to spare in the worst pair-coordinate case. This is an explicit integer inequality, not an appeal to eventual regularity of the total answer.

## 3. One numerator for the complete solver

Fix an increasing source-first common output edge (a,b). Define the result on reversed edges by alternating extension of the complete formula, and on repeated common edges by zero. Do not apply the raw ordered prism formula afresh to a reversed edge of an arbitrary input cochain. Put

    Z_ab = product_i Z_(r(a),i)^5250 Z_(r(b),i)^5250,
    D_ab = C_a C_b Z_ab,
    B_ab = [R(K_cov Pi + A h S Pi)F]_ab.

In the common finite chart, Z_(e,i)=1 if e_i=0, and x_i if e_i=1. Let u range over the inserted labels with r(u)=r(a), and v over those with r(v)=r(b). Define the full numerator

    N_ab = C_a C_b Z_ab B_ab
           + Z_ab sum_u Qhat_u P_[u,a,b]
           - C_a Z_ab sum_(u,v) Qhat_u Qhat_v P_[u,v,b]. (3)

Then

    (TF)_ab = N_ab / D_ab.                             (4)

**Proof of equality.** The first prism family is rho_u F_[u,a,b]. Substitute (1) and cancel the matching inserted factor using (2). Its denominator is C_a C_b. The second family is -rho_u rho_v F_[u,v,b]; after the two matching cancellations its only suffix denominator is C_b. Bringing these and B to D_ab gives exactly the two different padding factors Z_ab and C_a Z_ab in (3). All sums retain source-first alternating signs. This proves (4) for arbitrary source numerators satisfying (1), without a physical coefficient calculation.

The identity is valid for full sums; it does not authorize splitting a source numerator into raw rational summands that no longer satisfy (1). In particular the first and second families have different unchanged suffixes, and treating both as if they retained C_a C_b would obscure the C_a padding required in (3).

**Proof that N_ab is polynomial in the common finite frame.** Each P is polynomial. Each inserted Qhat can have negative powers only in coordinates where its designated output owner is an infinity vertex. The corresponding owner's factor in Z_ab clears it by Section2. In the second family u and v have different designated output occurrences, even if their tags coincide, so two negative contributions are cleared by two separate factors. Multiplication by the polynomial C_a introduces no denominator.

For the first term of (3), B is a complete standard-cover cochain on the output standard edge. For each coordinate its monomials satisfy:

- endpoints both finite: exponent >=0;
- endpoints both infinity: exponent <=n_i;
- mixed endpoints: no regularity inequality.

These predicates follow from the actual maps: K's coordinatewise-minimum cone and path vertices use only endpoint bits; S restricts to the same product-cell intersection; h sends C to A only at e>=0 and to B only at e<0,e<=n; J has exactly the constant or harmonic exponent. A and R preserve these domains. Thus no negative exponent occurs without an actual output infinity tag. When one exists, B's lower support bound -1668 is cleared by its x_i^5250. Therefore Z_ab B is polynomial, proving the assertion.

This last conclusion is for the complete B cochain. It does not certify arbitrary pieces obtained by splitting a coefficient projection or replacing a complete coefficient sum by an unconstrained rational leaf.

## 4. Differentiate once, after (3)

Factor D_ab as product_f f^a_f, using the owned factor dictionary. Keep differently owned equal polynomials as separate entries. Let Delta_ab be the product of the factors with a_f>0, each once. Then

    partial_i(TF)_ab =
      [Delta_ab partial_i N_ab
       - N_ab sum_f a_f (partial_i f) Delta_ab/f]
      / [D_ab Delta_ab].                               (5)

Every Delta_ab/f here is the product of the other labelled factors, not a division operation. Its exponents are nonnegative. The numerator is therefore polynomial. Equation (5) proves an increase of at most one on every existing owned factor, and no new factor on an absent owner. It remains valid when different owned factors have the same polynomial value: differentiation counts every occurrence, exactly as the product rule requires.

Inserted denominators do not appear anywhere in (5). Their derivatives are already included in partial_i N through the polynomial quotient functions. For example, the raw pieces partial(rho)F and rho partial(F) can separately contain a new inserted denominator; their cancellation is proved only in their sum by (2). The tests explicitly reject the inference that these raw pieces clear independently.

This gives carrier<=15, legal<=2 and standard<=5251 per actual output owner from (4). In a complementary coordinate the pair-legal factors are coordinate-independent, so their derivatives actually vanish; legal2 is only a safe common allowance. Padding by the unused nonpair legal factors reproduces the compiler's all-coordinate denominator convention without changing (4).

## 5. Physical frames and scalar derivative branch predicates

For a one-coordinate twist n, f_B(t)=t^n f_A(1/t). Direct differentiation gives

    (partial_x f_A)_B = -partial_t f_B + n f_B/t,

where the output twist is n-2. The complementary derivatives used by E have n=0, so the transported stripped operator is exactly -partial_t. This proves that (5) is a geometric O-to-O(-2) derivative, with no omitted connection term or additional arbitrary pole. For n=-2 a connection term would remain; this certificate rejects that case rather than silently applying the complementary rule.

To bound other chart frames, use the existing support and quotient degrees: standard B has pole<=max(1668,5248+2)=5250; a raw rho has local degree<=max(1677+70,481+70+2)=1747. The prism's new boundary factors belong to the designated output tags. Source F itself has only the divisors in (1), in its homogeneous character frame. Hence (4) has the same geometric carrier14/legal1/standard5250 bound, and the complementary derivative raises existing boundary orders by at most one. This frame argument is required: a common-finite polynomial numerator alone would not prove the infinity pole bound.

For coefficient transposition, first apply partial_i^* to kappa: eta=kappa+unit_i with factor kappa_i+1. Kill factor zero. All h predicates are tested at eta, not kappa. For pivot j:

- before j, a zero-twist factor requires state A/B and eta=0, then reads state B;
- before j, a -2 factor requires C and eta=-1;
- at j, A requires eta>=0 with sign -; B requires eta<0 and eta<=n_j with sign +;
- multiply by (-1) to the number of prefix C states; preserve the suffix.

For a Pi input triple with row labels w_0,w_1,w_2, coefficient exponent eta is requested precisely through the finite support predicate

    p_i + sum_(l:e_li=0) a_li - sum_(l:e_li=1) a_li
        - sum_(l:e_li=1) [14 d_wl + deg(ell_wli)[i in q]] = eta_i.

Here 0<=p_i<=14 sum_l d_wl + sum_l deg(ell_wli)[i in q] + n_i. The quotient exponent a_li is nonnegative and bounded by its row's carrier quotient degree, plus1-mask_i for an infinity pair coordinate or2 for an infinity complementary coordinate. Carrier bounds by infinity count s are: s0 finite66; s1 finite335/infinity213; s2 finite872/infinity347; s3 finite1677/infinity481; s4 infinity66. Finite legal factors add zero. Exact coefficients may vanish within these boxes, so this is a finite summation domain with a coefficient equation, not an assertion that every point is occupied. The full Pi value includes the bounded sum and its source-first sign. This predicate is unchanged by restriction and is passed to h at the shifted eta when differentiation is transposed.

The branch predicates additionally require the exact inserted/output tag equalities, distinct source (carrier,legal_mask) labels for the pullback input F (as distinguished from the weaker common-cochain alternation predicate), source-first sorting sign, finite-coordinate mask1 zero, primary carrier index<=number of infinity coordinates, and all-infinity primary index4. Structural survival is not a proof of a nonzero coefficient. The two R-mediated branches vanish for equal standard edge tags, whereas H need not vanish.

## 6. Discharged obligation versus remaining source identity

Discharged: assuming (1), the fixed polynomial quotient definitions and the stated standard-map support, formula (3) is an explicit full-sum polynomial numerator and (5) has no inserted-carrier denominator. Both prism suffix choices, coupled legal/chart reversal, full occurrence ownership, and physical complementary frame transformation are covered for all labels. This is reusable across seeds and is not restricted to the selected seed4 lowering.

Not discharged: the actual-source circuit-to-(1) equality witness, a full executable source numerator circuit for each needed tuple, and executable coefficient realization of B and the bounded partition sums. Precisely, a source adapter must establish that its F_[u,v,w] equals the pinned b_q-tr(G^-1 mu_q(B,A))/2 in the specified homogeneous character frame, and that multiplying that *whole source* by C_u C_v C_w yields its emitted polynomial numerator P. A denominator declaration, hash match, finite second-jet AST, or a test on arbitrary formal functions is insufficient for that implication.

This certificate therefore discharges a general algebraic implication but does not mark any of the compiler's 78 global regularization groups admitted. It proves neither vanishing nor nonvanishing of the obstruction and does not supply an arithmetic cost or live-memory certificate.

## References and replay

- PR79 compiler/foundations pinned at ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18: https://github.com/Akilleez-QA/read-em-and-weep/tree/ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18/research/hm/null-operator-compiler
- PR80 source jet contract read at Git blob c9b88e232d9c113f83d3ef7148ab0a775d39a144; no API from it is reused: https://github.com/Akilleez-QA/read-em-and-weep/pull/80
- Existing notes: refined-tracefree-pole-domain.md; outer-pinned-frames-and-poles.md; transposed-scalar-demand-grammar.md; selected-full-owner-kernel-lowering.md; N14 transition-scalar-finite-demand proof.

Run `python -m unittest discover -s . -v` here with Python3 and SymPy1.14.0. The tests are abstract regression controls supporting the written all-label proof, not a machine formalization of the entire source geometry.

## Review correction

The source input is s*F, so its repeated-source zero predicate is stronger than general common-cover alternation. The implementation separates `source_F_sort` from `alternating_sort`; only the former rejects repeated (carrier,legal_mask) across differing standard tags. Prism source branches use the former. Regression controls check the general common-cochain branch remains nonzero under this distinction, the source branch is zero, and owner-specific denominator clearance still rejects borrowing an equal source factor from another occurrence.
