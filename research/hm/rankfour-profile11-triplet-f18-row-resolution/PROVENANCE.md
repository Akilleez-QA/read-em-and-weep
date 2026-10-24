# Assertion provenance and verification boundary

## Complete source authentication

The only direct originals are the entire PR1239 and PR1207 PROOF.md files
listed in INPUTS.md and INPUTS.json. Each was read completely and freshly
retrieved through both a commit-pinned repository-path call and a returned
blob call. The two complete responses and retained local bytes agree.
Authentication establishes exact file identity, not truth of an imported
theorem or independent certification of its transitive geometric hypotheses.

## Imported facts and their exact use

1. PR1239, Sections 2-4 and 10, supplies the physical representation facts,
   invariant orbit lengths and unique reduced Z12, the canonical line L_A,
   torsion quotient tau, P target T_P, and tau's injectivity on f12 H6.
   Section 5 supplies the intrinsic first-order stationarity criterion.
   Sections 6-7 supply the nonzero Wronskian and local weight formula.
   The new proof's Sections 1-6 use only these fixed universal facts.
2. PR1239, Sections 8-9, supplies the actual scalar-section injection
   j18:V18* -> H18 and embedded identity Lambda15=ker gamma. This is used
   only in the conditional actual application, Section 7. No actual
   coefficient space is identified with its dual by representation type.
3. PR1207, Section 2, supplies the standard complete first-jet identity
   and physical small representation identities. Section 3 proves the
   actual everywhere-surjective partial first-jet evaluation. Section 6
   supplies its induced complete-versus-partial kernel sequence, exactly
   two possible F18 splittings, and H0/H1 at twist two. Sections 7-8 supply
   the actual E0 extension and its equivariant splitting in the first case.
   The new proof's Sections 6-7 identify the exact map before selecting
   the alternative. No rank or completeness property is transported from
   an unrelated actual bundle.

## New deductions proved here, not imported

- Section 1: P0 itself is basepoint-free. A fixed Z12 would force
  P0=f12 H6[P], contradicting tau's injectivity there. Its first-jet image
  is then exactly L_A, proving its first-order projective stationarity.
  Section 5 cites this present deduction, not an unstated prior theorem.
- Section 2: the forced V_alt quadratic syzygy is an everywhere bundle
  isomorphism V_alt(-2) -> M_S. Lower generic ranks are excluded by degree
  and fixed representation constraints; equal determinant degree proves
  no residual torsion defect.
- Section 3: the four-section degree-six Wronskian has divisor precisely
  Z12. Its weights force the exact sequences (0,1,2,4) there and
  (0,1,2,3) elsewhere. Thus second-jet evaluation is everywhere onto with
  kernel O(-12).
- Section 4: the canonical Hom line B=Hom_G(E*,V_alt) and the syzygy
  construct q:B O(-18) -> S O, nowhere zero. Its adjoint proves that its
  scalar system is the nonzero P component Q of ordinary H2 times E.
  The naturally directed row-column identity pq=0 uses no chosen form.
- Section 5: exact successive principal-parts factors have Hom degrees
  22 and 20. First-order stationarity would force the degree-20 factor
  to vanish on Z12, then identically; q would factor through O(-12),
  contradicting H6 invariants being zero. This proves Q is not P0.
- Section 6: the standard complete-jet inclusion is multiplication by
  the square of the variable vanishing linear form. Nondegenerate
  determinant-square contraction equates vanishing of its V_alt row with
  gamma(H2 times E)=0. The preceding contradiction proves that row nonzero.
- Section 7: combining the exact actual maps from the two originals now
  removes only the D+V_alt twist-two kernel alternative. The first F18
  splitting and its actual equivariantly split E0 extension remain.

## Mathematical and computational boundaries

The draft used to prepare this packet had SHA256
34f76d25931425ad9bb027afa0a6182e0741122cbb06982fe28e778d789e085e.
Only its status/source-provenance introduction and the Section 5
attribution to the present Section 1 were changed for publication
preparation; no mathematical argument or map direction was changed.
That draft and its earlier audit are preparation, not inputs or a new
review. The prior orthogonal-top packet was inspected only as a packaging
example; its mathematical conclusions are unnecessary here.

The bounded checker authenticates whole selected files and checks fixed
small character identities, degree sums, and cohomology dimensions.
It does not establish source sufficiency, actual-map directions, saturation,
Wronskian nonvanishing, the formal differentiation lemma, or the
determinant contraction. Those require review of the entire proof and
both complete freshly authenticated immutable originals.

No actual HM/source coefficients, parameters, selected points, eigenlines,
jets, tensors, matrices, instance ranks, invariant polynomial representatives,
P representative, or scalar normalizations are evaluated. There is no
broad scan, large computation, historical enumerator, local Codex task,
GitHub write, merge, upstream submission, quotient connection, horizontal
splitting, or differentiation of a moving inverse. Higher principal parts
are only a universal obstruction to first-order stationarity, not a proof
of higher-order branch matching or algebraicity. No realization or
exclusion of the full K1 branch follows.
