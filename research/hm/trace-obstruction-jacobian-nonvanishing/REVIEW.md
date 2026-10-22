# Independent review of the Jacobian nonvanishing lemma

## Verdict

PASS for the exact identity, nonvanishing, and rank-at-least-one conclusion, conditional on the stated upstream hypotheses and the target-reduction lemma now pinned as PR718, commit 2411fcd92acd738d0d8af7bebc79ee9191b276ef. No actual HM/source-instance evaluation was performed. The standalone PROOF.md incorporates the elementary full-socle justification supplied below.

Reviewed the standalone PROOF.md and verify.py against [PR717 at commit 7362df9da60a3b87b3200078a0145a376cc3056b](https://github.com/Akilleez-QA/read-em-and-weep/blob/7362df9da60a3b87b3200078a0145a376cc3056b/research/hm/nilpotent-trace-lift-invariance/PROOF.md) and [PR718 at commit 2411fcd92acd738d0d8af7bebc79ee9191b276ef](https://github.com/Akilleez-QA/read-em-and-weep/blob/2411fcd92acd738d0d8af7bebc79ee9191b276ef/research/hm/trace-obstruction-target-reduction/PROOF.md). This review does not independently certify the geometric input or actual nonemptiness supplied by the pinned upstream theorems.

## Exact harmonic normalization and sign

For n=u[[fg,-f²],[g²,-fg]] and D=ell[[f/2,0],[g,-f/2]], expanding the scalar trace of the two ordered harmonic products gives precisely

    sc(B1(n,D)+B1(D,n))
      = u(B1(fg,ell f)-B1(f²,ell g)).

The two diagonal half-factors and the two ordered products cancel the scalar-trace half-factor. Entry degrees (8,4) and (6,6) give denominators 462 and 550 respectively. Thus there is neither an extra factor two nor a missing unit u.

In the formal dehomogenized product, the coefficient of L' is u F(F'G/3-FG'/5). Consequently t b_X-b_Y is its negative, equal to u F(3FG'-5F'G)/15. Euler's identities identify the parenthesis with the specified orientation J=f_X g_Y-f_Y g_X. The result is therefore +u fJ/15, not its negative. The ordinary T contribution cancels before any quotient is taken. All terms are homogeneous of degree nine, so dehomogenization is injective on the relevant homogeneous component and rehomogenization is valid.

The reviewed tiny script was run once and passed all four formal checks. It manipulates only free formal jets and an unspecified two-by-two matrix; it substitutes no actual pair, coefficients, roots, derivatives, or rank instance.

## Division by f and quotient

The target-reduction proof establishes actual polynomial divisibility of each Psi(ell A0) by f, not merely a fraction-field representative. Since S is a domain and f is nonzero, cancellation in the polynomial identity is valid. Multiplication by f identifies S5/(f S2+k g) with the stated subquotient. Multiplication by X or Y then gives well-defined classes in (S/(f,g))6. No inversion of f in the Artinian quotient is being attempted.

## Koszul/Ext nonvanishing

The comparison map K(f,g) -> K(X,Y) lifting A -> k has degree-one matrix M transpose with the usual column convention and top component det(M)=J/15. Dualizing reverses the arrow and sends the generator of Ext²(k,S) to [J/15] in Ext²(A,S), with the same determinant sign when both Koszul complexes use their displayed ordered sequences.

Finite-length modules supported at (X,Y) have Ext⁰ and Ext¹ into S equal to zero: this follows from the explicit Koszul resolution of k and induction on a composition series. In particular Ext¹(mA,S)=0. The long exact sequence for 0 -> mA -> A -> k -> 0 therefore makes Ext²(k,S) -> Ext²(A,S) injective. This establishes [J/15] nonzero. Grading shifts do not alter the ungraded injectivity argument. The adjugate identity also proves that both X and Y annihilate [J/15]. No step assumes f or g square-free or the Artinian quotient reduced.

## Small full-socle clarification

The Hilbert series alone proves dim A6=1 and A_d=0 for d>6, but does not alone exclude a socle in lower degrees. The claim that A6 is the entire socle is correct for this regular pair and can be made self-contained as follows.

Let a homogeneous class [h] of degree r<6 be killed by X and Y. Write

    Xh = af+bg,       Yh = cf+dg.

Regularity and the unique regular-pair syzygy imply

    Ya-Xc = e g,      Yb-Xd = -e f.

Homogeneity gives deg(e)=r-6<0, hence e=0. Since X,Y are coprime, a=Xv, c=Yv and b=Xw, d=Yw for polynomials v,w (including zero when the relevant degree is negative). Cancelling X from Xh=X(vf+wg) yields h in (f,g). Thus no lower-degree socle exists. Together with the Hilbert series and the nonzero degree-six Jacobian, this proves Soc(A)=A6=k[J]. This short addition closes the only expositional omission found.

## Scope of the conclusion

Because u is a nonzero scalar in characteristic zero, the displayed alternating multiplication identity rules out the zero map. Source and reduced target have dimension two, so only rank in {1,2} follows. Nonzero alternating multiplication does not imply rank two. The argument neither calculates the actual rank nor evaluates the base fourth-square scalar, beta4, or any distinguished actual lift. Its final local-variation consequence remains conditional on the variation formula and unit a from PR716; it does not establish global realizability of local directions.

## Standalone finalization

The finalized standalone PROOF.md pins PR717 and PR718 by immutable commit, includes the lower-degree socle exclusion, and uses the left-adjugate identity in its natural order. verify.py is unchanged from the independently inspected and executed formal checker.

## Frozen reviewed artifacts

SHA256 hashes of the final proof and formal verifier:

- PROOF.md: d097fbb0dbd7abb0820c6c6e4c56a9b2133a5fff1488ee1d12330e0d7d666360
- verify.py: df581f2c3c3a7047085fbba2a158d4b489e7f49ff8251eb27f8a231a7a138933
