# Independent audit of the direct scalar dual-fill contract

Reading-order qualification: this contract precedes `owned-denominator-finite-domain-certificate.md` and its independent audit. Those later notes supply the full finite-domain exactness and bounded-primitive comparison at proof level. They do not supply instantiated physical coefficient rows, a practical pivot/factored inverse, or a physical direct-fill residual.

## Verdict

Both graded cup identities and the finite transpose-pivot construction are correct. The originally stated full-regular-complex factorization required an additional domain hypothesis, now inserted explicitly in sections 2-4 and the conclusion of the audited contract: a fixed bounded comparison formula is not automatically a detector on every regular cochain or every regular primitive. Thus the conclusion is conditional on the gauge/comparison domain, exactly as opposed to an unrestricted consequence of scalar H1 vanishing.

## Signs and agreement with the reduction

In the first-endpoint row frame, ell_b cup D_a s contributes L_b D_a s_jk, whereas D_a s cup ell_b contributes D_a s_ij U_b. The antisymmetric cup formula therefore has the reduction's four signs +,-,+,-, with its factor 1/2 and a,b exchange retained.

For delta ell=0 and delta D=D delta, graded Leibniz gives

    delta(ell cup Df)=-ell cup D delta f,
    delta(Df cup ell)= D delta f cup ell,
    delta(ell cup Ds)=-ell cup D delta s,
    delta(Ds cup ell)= D delta s cup ell.

The first two yield E(delta f)=-delta A(f). The latter two yield delta E(s)=-A(delta s). In particular the plus between the two orders in A on degree 2 is necessary. No graded commutativity of cup products has been used.

`test_direct_dual_cup_signs.py` independently expands both identities on a triangle/tetrahedron with a universal additive current cocycle and formal differentiated scalar labels. Both identities pass and the opposite-sign controls fail. This is a formal sign test, not a test of physical frame conversion or pole bounds.

## Finite transpose solve

Write D1:V1->V2, with e a column representing a covector. If e kills ker D1, and B has r columns representing a basis of V1/ker D1, then D1 B has rank r. For an invertible row minor C=(D1 B)_I, the formula

    eta_I=C^(-t) B^t e, eta_outside_I=0

has the stated dimensions and satisfies D1^t eta=e. Agreement on B follows from C^t eta_I=B^t e; agreement on the kernel follows from the compatibility assumption. These two spaces span V1. Conversely, a solution necessarily kills ker D1. D0 and finite H1 exactness are sufficient ways to establish compatibility, but not necessary if kernel annihilation is proved directly. Rank zero is harmless: compatibility then forces e=0 and eta=0 is a filling.

Nonuniqueness is precisely ker D1^t=Ann(im D1). This includes cohomological freedom but is generally larger than dual H2; no preferred coefficients or weight cancellation follows.

## Exact domain conditions still needed

1. Choose an actual scalar subcomplex/gauge domain C0->C1->C2 with the physical character and restriction maps. The complementary derivative must be a compatible map to the appropriate target character, including all frame terms. A statement about stripped coordinate derivatives alone does not suffice.
2. Define Phi on E(C1), and require Phi(delta A(f))=0 for every f in the chosen C0. A sufficient condition is that A(C0) and its boundaries lie in a comparison-compatible regular chain domain on which Phi kills boundaries. Merely having delta A(f) inside a numerical pole envelope does not prove its chosen primitive and chain homotopy are admitted.
3. Require every s in ker(delta1|C1) to have a primitive f admitted by condition 2, or prove e(s)=0 independently. Full-sheaf H1=0 only supplies a primitive in the full regular complex; it does not establish this bounded-domain condition. This is the extra premise needed to pass from section 2's admitted-gauge closedness to section 3's full-complex claim. Alternatively construct a compatible extension of Phi to the full complex and prove it annihilates all regular boundaries there.
4. For a finite model, basis coordinates must represent actual cochains without unidentified relations. Restriction/frame and denominator-alignment operations must land exactly in the chosen target spaces, not in projected/truncated approximations. D1 D0=0 and kernel compatibility must be verified for these actual matrices. If a redundant presentation is used, its relations must also be killed by e and treated consistently by D1.
5. The demanded input s and F=delta s must be included, and the coefficient rows of e must agree with the authenticated, exactly regularized detector formula on all of V1. Source-specific support bounds alone are insufficient to certify e on arbitrary basis vectors introduced by a quotient solve.
6. Supply exact pivot/rank and residual certificates, as well as a valid representation of eta's coefficient functionals on V2. Its extension outside V2 is neither needed for the finite solve nor licensed by it. A rational inverse is mathematically valid but is not a product/byte schedule.

The strongest unconditional audit result is therefore the two formal chain identities and the conditional finite row-space theorem. No physical source polynomial was evaluated, no public post was made, and no resource gate was released.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
