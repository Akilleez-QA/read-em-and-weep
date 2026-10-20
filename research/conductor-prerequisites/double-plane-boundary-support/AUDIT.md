> Historical mathematical review retained with the source. This is not a new independent review or a formal verification certificate.

# Independent audit of the double-plane support exclusion

## Verdict

The argument in PROOF.md is valid under its stated hypotheses over C. I independently checked the rational division, every local valuation and contact assertion, globalization in a fixed quotient, and both compatible-square contradictions. No computational experiment or physical/source instance is used in this audit.

## Checks

1. Away from [x], the five-plane incidence forces equality with the five-dimensional restricted kernel. The regular proportionality and exact bundle-division argument from the cited rank-one proof applies there. Both a and lambda transform with L, so their divided covector ell is a rational section of the trivial E* bundle. Its only possible poles lie over [x].

2. The local chart a(z)=1 is permitted at every point over [x]. Nonconstancy makes b nonzero in the function field, and the local DVR therefore gives a finite contact order k. In the polynomial convention used, comparison of the xH and H-squared coefficients gives exactly (2) and (3), hence (4), with no missing polarization factor.

3. A primitive B has primitive square in the polynomial ring over the residue field. Thus val(c b-squared)=val(c)+2k. When P=0, (4) forces val(c)>=-k; cb and d are regular. When P is nonzero, its constant coefficient vector cannot cancel against terms divisible by the uniformizer, giving val(c)=-2k and a unit u. These arguments divide only by a uniformizer in the fraction field and by explicitly verified units.

4. The strengthened contact estimate is essential and correct. In the constant basis B0 plus a complement, P has only a B0-squared component. The mixed coefficients in u(s B0+D)-squared congruent to -P modulo tau^k are exactly 2usD. Since 2us is a unit, D is divisible by tau^k. Therefore b modulo the fixed B0 direction vanishes to order 2k, enough to cancel the pole of c. Merely knowing the initial square direction would not have sufficed; the proof establishes the stronger estimate.

5. Every exceptional preimage produces the same line C B0, because a nonzero square polynomial P determines its linear-factor line uniquely. The calculation is performed separately on each normalized branch with its own k and uniformizer, so neither transversality nor unramified parametrization is assumed. The image of ell in the fixed quotient E*/D is consequently regular everywhere and hence constant on the complete integral curve.

6. Restriction is made to the full ambient polynomial identity, not to an unsupported claim that Sym-squared W lies in every moving K_t. Since W annihilates D, the remaining rational shear vanishes there; the resulting regular identity implies F(Sym-squared W) lies in the common support intersection I.

7. The first nonzero local jet of a-x belongs to the constant linear span J of the support covectors. Thus B0 belongs to J, and in the nonzero-P case I lies in W. This follows by dividing an identity in J tensor R and taking its residue, or equivalently by testing every constant linear equation of J. No derivative or first-order contact assumption is involved.

8. In the zero-P case, at most two ternary quadratics have a nonzero common zero by the height bound. In the nonzero-P case, F maps Sym-squared W to the binary plane W, and the homogeneous binary cubic e wedge F(e-squared) has a projective zero. Each produces exactly the compatible square forbidden in the statement. The no-exceptional-preimage case is correctly handled by the previously proved global regularity argument.

## Scope

Together with the independently stated irreducible-quadric and distinct-factor arguments, this excludes complete nonconstant support curves for all nonzero scalar annihilator quadrics under the five-plane incidence and square-avoidance hypotheses. It makes no claim about classifying all rank-five tensors or proving a global rank bound.

## Separate audit of the corrected conditional integration section

The appended conditional corollary is valid with its explicitly imported geometric premises. This audit checks the deduction from those premises, rather than independently re-proving the rank-two finite-support theorem or every application-specific source hypothesis.

The corrected notation agrees with the full-flag proof: the global support graph has target P(V*) for the five-dimensional ambient V, h is the middle hyperplane pullback, and n is the support class. The rank-one exclusion is applied separately in each four-dimensional local middle space. A positive-dimensional projective support fiber contains an integral complete curve, so the local exclusion suffices to make rank-one fibers finite.

Properness and finite fibers imply that the support graph is finite over B. The graph is integral and birational to B. Their common function field and the integral-closure characterization of normalization identify the normalization of this finite graph with B's normalization. Thus its second projection extends H to B's normalization. The original support map on Y and the pullback of this extension agree on a dense open; the target is separated and Y is integral, so they agree everywhere. This proves descent of n, rather than assuming it. Descent of h already follows from the middle map.

With both classes descended, every curve contracted by f has zero intersection with their sum. Proper pushforward of A is an effective Weil divisor cycle on the normalized surface, possibly with contracted components discarded. The projection formula for the descended Cartier class preserves the given intersection number, which is at least degree(B)>0. Therefore this pushed-forward divisor cannot vanish. Its support lies over the bad locus, and finiteness of the normalization map implies that its curve image in B is also a curve. No Cartier assertion about the pushed-forward Weil divisor, classification of all rank-five types, existence assertion, or universal dimension bound is needed or implied.

Final status: the main theorem and the corrected conditional integration deduction are accepted. No outstanding mathematical gap was found in these arguments.
