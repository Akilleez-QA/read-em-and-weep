# Independent review of the supplied-source membership sector

Date: 2026-10-23. Verdict: PASS for the bounded written theorem and universal
diagnostics described below, relative to the authenticated prior mathematical
inputs. This is not a proof-assistant certificate or a physical-instance test.

## Frozen artifact binding

The reviewer independently recomputed these SHA256 hashes after the final
freeze notification:

- PROOF.md: `74d801f850d281658955f7583a838c90ff49fa2f9122dea8a2391e01a71dcc0b`
- verify_source_membership.py: `c1ea8a33e60d26b0f702311380e280ea9c7dff3c8ffa9eddeb01019ead0f7ce6`
- SOURCE-MANIFEST.json: `442d709dab1e69db3fc8629765d563746f81d50a41a961419831b642db304e5f`
- README.md: `45cbb98f9e68459027af410d0fb7cbba19215d8e0c89f827b4304036037a9f8c`

All seven source copies match their manifest byte counts and SHA256 digests.
For each copy, recomputing Git SHA1 on `blob <byte count>\0<content>` also
matches its recorded immutable Git blob. The review read the six initial
inputs and the subsequently added central-parity premise. It uses those
prior geometric/cohomological results as inputs, not as conclusions proved
by the present character checker.

## Mathematical findings

1. **Correct source convention.** The positive binary representation is
   U=Wprime, with V=Sym^2 U, whereas A=Sym^2 W is the distinct negative
   three-dimensional irreducible. The proof does not interchange A and V.
   Its source is R=Sym^3 A tensor D5=3A+3V+3P4+4D5, of vector dimension 50.
   The newly authenticated central-parity input explicitly identifies the
   center of SL2(F5) with HM inversion. Thus R-equivariant cohomology maps
   land in the physical positive sector; a separate cone Serre involution
   is not being silently identified with that center.

2. **Global sufficiency, not just pointwise solvability.** The complete
   fixed-duality trace-free complex has the positive-twist termwise
   acyclicity supplied by global_complex Section 1. Consequently its global
   cochains compute H^1(B(t)) at t=2,4. Exactness of Hom_G(R,-) over C makes
   vanishing of the entire coefficientwise class equivalent to a single
   equivariant polynomial primitive in C^0_4. This is not a gluing claim
   inferred from separate pointwise choices. H^0(B(4))=0 also correctly
   gives uniqueness only modulo d C^-1_4, not literal cochain uniqueness.

3. **Exact arithmetic.** Applying equivariant Hom from R to the actual
   q kernel/image/cokernel sequence gives dimensions
   0 -> 7 -> 34 -> 30 -> 3 -> 0. In particular the image dimension is
   34-7=30-3=27. Independently counting isotypical multiplicity slots gives
   6 for V, 9 for P4, and 12 for D5. These are scalar coefficient counts,
   not representation-vector dimensions or an evaluated physical rank.

4. **No circular E or W existence assumption.** The natural fixed Z and
   preceding division q[v]=a h zeta_a are explicit hypotheses in the final
   Result. Their full-family existence follows from the cited D5
   multiplication inclusion, an equivariant section of q onto its image,
   and the global-cochain comparison. Independence under a change of v by
   a K-valued family follows from aK being contained in im(q). The prior
   canonical raw-cubic sheaf factorization, not the desired equation dE=T
   or the later J4 ladder, removes the quotient obstruction. The proof does
   not silently transport the canonical correction to an arbitrary Schur
   gauge.

5. **Sharp 27-sector for canonical b.** Once the preceding V and canonical
   correction are fixed, [a(V-bZ)] belongs to Hom_G(R,I). As [W] varies
   over Hom_G(R,M2), the defect [a(V-bZ)]-q_*[W] is an affine surjection
   onto Hom_G(R,I). Every cohomology-family W has a closed global
   representative, so this surjectivity applies to precisely the
   unrestricted closed equivariant families asserted in the theorem.
   Its fibers are torsors for Hom_G(R,K), of dimension seven. The theorem
   correctly makes no claim that every such family is produced by an
   additional fixed physical algorithm. Quotient-P4 tests cannot separate
   these residual defects, because they all vanish on I.

6. **Sharp 28-sector when b varies.** The correction family space
   L=Hom_G(A tensor D5,A) has dimension one. Its map to Hom_G(R,P4) is
   composition with the actual second-symbol sheaf injection. A zero
   composite therefore forces the whole sheaf map b to vanish, despite
   exceptional fibers where the second symbol has lower fiber rank.
   The resulting quotient line has dimension one. Varying b covers that
   line and varying W covers the 27-dimensional kernel of the quotient,
   so the combined residual image has dimension 28. Its linear kernel
   has zero b-component and dimension seven. Full membership forces
   b=b_can, followed by the 27 compatibility conditions on W.

7. **Conditional ten-channel detector corollary.** A linear map defined
   on the full 27-dimensional defect space with values in PR889's
   ten-dimensional trace-family space has a kernel of dimension at least
   seventeen. Sharpness supplies nonzero defects in this kernel, so such
   a detector cannot certify membership for every allowed W. The proof
   explicitly requires independent existence and factorization of that
   detector. It does not extend an eta or trace response defined only on
   im(d) to inputs outside that domain. It also does not exclude nonlinear
   observations or stronger hypotheses restricting the W-family.

## Issues raised and resolved before freeze

- The initial six inputs did not explicitly identify the positive sector
  with the central-even sector. Adding the immutable central_parity input
  and the corresponding dependency statement resolves that point.
- Closedness and bidegree alone do not suffice for the preceding V: taking
  V=0 while retaining the nonzero canonical b would leave a nonzero quotient
  obstruction. The final Result now expressly requires the fixed canonical
  Z and full-family preceding division q[v]=a h zeta_a. The README agrees.

No unresolved defect was found in the final bounded theorem.

## Reproduction and scope

The reviewer independently executed both:

    python verify_source_membership.py
    python -O verify_source_membership.py

Both exited successfully and reported 127 exact character/multiplicity
checks and seven negative controls. The checker uses explicit failure
branches, so optimization does not remove its checks. Inspection confirms
that its slot labels describe an abstract split multiplicity model, not
chosen actual HM coefficients or a sampled q-matrix. Its diagnostics are
consistent with, but do not establish, the geometric source theorems or
the global factorization and acyclicity arguments.

This review does not certify an actual supplied W, physical contraction,
primitive, trace row, normalization comparison, calibration, or the original
global proof repair. It authorizes no publication or branch operation.
