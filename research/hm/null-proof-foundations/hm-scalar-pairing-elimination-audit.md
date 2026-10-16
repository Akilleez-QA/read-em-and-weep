# Scalar first-lift elimination: exact boundary identity and remaining adjoint term

## Result

The undifferentiated scalar primitives can be eliminated from the complete mixed second-order residual modulo an explicit End Čech boundary. Complementary derivatives of the primitives remain in traceless Maurer–Cartan terms. Cyclic matrix trace kills those terms, but the positive detector is not ordinary matrix trace. A fully specified scalar contraction permits formal elimination of the remaining primitive by transposing that contraction onto the detector; this transfers, rather than removes, the scalar-solving work.

No physical polynomial values, residual evaluation, or jets were computed. This is symbolic algebra only. In particular, no obstruction value or vanishing is asserted.

## 1. Conventions and exact expansion

Use the pinned `hm-pinned-source-formulas.js`, `globalCross`, with p=12 and q=34. On a triangle write A=g_ij, B=g_jk, G=BA=g_ik. Normalize the row residual on the left by G^{-1}. Define

    k_p=-K_p/2,  u_p=g(s_p I+k_p),
    C_p=G^{-1} μ_p(B,A),  c_p=tr(C_p)/2,
    F_p=b_p-c_p,  C_p^0=C_p-c_p I.

All subscripts p may likewise be q. Determinant-one gives tr(k_p)=0. Indeed, with L_a=g^{-1}V_a g, K_p=(-L_a L_b+L_b L_a)/2. The first-order identities are

    δs_p=F_p,   δk_p=-C_p^0,
    (δx)_ijk=A^{-1}x_jk A-x_ik+x_ij.

Let M(s) be the pinned normalized mixed residual, with its fixed ambient terms, and M(0) the algebraic expression obtained by setting both scalar primitives to zero, keeping k, b and ambient terms unchanged. M(0) is not claimed closed or to come from a valid first lift. Put k~_p,jk=A^{-1}k_p,jk A. Direct substitution gives

    M(s)-M(0)
      = (s_p,jk s_q,ij+s_q,jk s_p,ij
         -b_p s_q,ik-b_q s_p,ik) I
        +s_p,jk k_q,ij+s_p,ij k~_q,jk
        +s_q,jk k_p,ij+s_q,ij k~_p,jk
        +(s_q,jk+s_q,ij) C_p+(s_p,jk+s_p,ij) C_q
        +E_p(s_q)+E_q(s_p).

The fixed term -b_p b_q I occurs in both M(s) and M(0), so cancels in this difference. The ambient second jet likewise cancels and has not been omitted from M(0).

For p=(a,b), the remaining derivative operator is exactly

    E_p(s)_ijk = 1/2 [
        (V_a s_jk) A^{-1} V_b A
       -(V_b s_jk) A^{-1} V_a A
       +(V_b s_ij) A^{-1} B^{-1}(V_a B) A
       -(V_a s_ij) A^{-1} B^{-1}(V_b B) A ].

The signs follow directly from μ_p(F,G)=(V_a F V_b G-V_b F V_a G)/2. Each Maurer–Cartan matrix displayed has zero trace, so tr E_p(s)=0. Scalar values and derivatives here are interpreted in the original physical frames; frame factors cannot be frozen before differentiation.

## 2. Exact boundary elimination, including all induced terms

Define the End 1-cochain

    Q_ij=s_p,ij s_q,ij I+s_p,ij k_q,ij+s_q,ij k_p,ij.

Then the exact matrix identity is

    M(s)-M(0)
      = -δQ+F_p k_q,ik+F_q k_p,ik
        +(b_p b_q-c_p c_q)I+E_p(s_q)+E_q(s_p).        (1)

Two explicit product-rule computations verify the signs:

    δ(s_p s_q)
      = -(s_p,jk s_q,ij+s_q,jk s_p,ij)
        +s_p,ik F_q+s_q,ik F_p+F_p F_q,

    δ(s_p k_q)
      = -s_p,jk k_q,ij-s_p,ij k~_q,jk
        +F_p(k~_q,jk+k_q,ij)-s_p,ik C_q^0.

Use s_p,jk+s_p,ij=s_p,ik+F_p and
k~_q,jk+k_q,ij=k_q,ik-C_q^0. The scalar remainder becomes
F_p F_q+F_p c_q+F_q c_p=b_p b_q-c_p c_q.

Thus (1) retains both the quadratic scalar correction and the induced mixed scalar/matrix correction. Dropping either is not justified by gauge invariance.

## 3. What the detector can discard

The complete actual M(s) is closed. Its central part tr(M(s)) I/2 is separately closed because trace commutes with the conjugated Čech differential. In the full-sign character, the scalar summand is O(-2,-2,-2,-2) on (P1)^4, whose cohomology occurs only in degree four. Hence its degree-two cohomology vanishes. The detector of the actual degree-two End class therefore kills this complete central cocycle after regular comparison.

This argument does not permit discarding an arbitrary central summand of an unclosed decomposition. In particular, the displayed quadratic scalar part by itself need not be closed.

Let M^0=M-tr(M)I/2. Projecting (1) to trace zero yields

    M(s)^0 + δ(s_p k_q+s_q k_p)
       = M(0)^0+F_p k_q,ik+F_q k_p,ik
         +E_p(s_q)+E_q(s_p).                         (2)

Important gerbe accounting: M(0) still contains -b_p k_q,ik-b_q k_p,ik-b_p b_q I. Thus +F_p k_q+F_q k_p in (2) is correct only with that definition of M(0). If R_kin is the same k-only residual with all three gerbe terms removed, (2) is equivalently

    M(s)^0 + δ(s_p k_q+s_q k_p)
      = R_kin^0-c_p k_q,ik-c_q k_p,ik
        +E_p(s_q)+E_q(s_p).                         (2a)

The remaining coefficients are minus c, not plus F, in this gerbe-free notation. This explicitly reconciles the independent direct-coefficient reduction with the full-matrix difference identity.

The right-hand side as a whole is closed. Its individual summands need not be. Equation (2) is an authenticated replacement representative for the positive pairing; it eliminates all undifferentiated scalar values but not their complementary derivatives.

The use of scalar H^2=0 is a class-level statement. An executable application still needs a regular comparison on the domain of the new representative; it does not license reusing old pole, feature, or cost bounds without proof.

## 4. Why cyclicity and integration by parts do not finish the job

For a matrix test W, tr(W E_p(s)) is generally nonzero, even though tr(E_p(s))=0. Cyclicity only rearranges the matrices. For example, on the algebraic patch y≠0, take A=diag(y,y^{-1}), B=I, V_a=∂_x, V_b=∂_y, s_jk=x and s_ij=0. Then

    E_p(s)=diag(1,-1)/(2y),
    tr(diag(1,-1) E_p(s))=1/y.

This is a local algebraic control, not a closed global obstruction or a counterexample to gauge invariance. It proves that a purported pointwise cancellation by centrality or cyclic trace is false. Taking s_ik=x makes δs=0 in this example, and a full gauge-covariant global detector would cancel the resulting boundary, as it should.

The sparse positive detector uses selected off-diagonal and weighted diagonal entries of the included/homotopied End matrices; it is not the ordinary rank-two matrix trace. Therefore tr(E)=0 alone cannot remove E from that detector.

Integration by parts moves derivatives to the entire dual density, including coefficient-extraction monomials, physical frame conversion, carrier weights and homotopy matrices. For formal residue pairing Res tr(W V_a s A_a) ω, the adjoint term is

    -Res s [V_a tr(W A_a)+div_ω(V_a) tr(W A_a)] ω.

Ignoring any of these derivatives, or applying residue integration by parts before establishing a regular comparison, changes the functional. A general Laurent coefficient [x^e] is a residue with density x^{-e-1}dx, so its density contributes too. No identity in the supplied notes proves that the resulting adjoint expression vanishes.

## 5. Correct formal adjoint elimination

Let T_p be the fully specified scalar solving operator from `hm-transition-only-first-lift-alternative.md`, including refinement:

    T_p F_p=H_rho F_p+r*(K_cov Pi F_p+A h S Pi F_p).

On the authenticated exact first-order sources, δT_p F_p=F_p. Any old scalar solution differs from T_p F_p by a scalar coboundary, since the pair-character scalar H^1 vanishes. The full induced second-order gauge terms in that note ensure equality of the actual obstruction classes.

Let Φ be a regular, source-authenticated pulled-back linear detector on the appropriate refined End 2-cochains. It is understood to annihilate boundaries and to evaluate the complete closed source. On a common bounded regular domain where every displayed map is defined, equation (2) gives the exact formal identity

    ell(O2_full)
      = Φ(M(0)^0+F_p k_q,ik+F_q k_p,ik)
        +(T_q^* E_p^* Φ)(F_q)
        +(T_p^* E_q^* Φ)(F_p).                       (3)

Here * means algebraic transpose/composition of linear functionals, so there is no additional hidden sign: (T_q^* E_p^* Φ)(F_q)=Φ(E_p(T_q F_q)). Derivative signs are precisely those of E in section 1, or the minus/divergence formula in section 4 if one implements its adjoint by integration by parts.

Equation (3) eliminates the explicit first-order primitive as an input, but still requires constructing/authenticating the adjoint contraction and its finite demands. It is not a proof that either last term is zero, nor a resource saving. The scalar solver's partition derivatives and all new source-domain bounds remain relevant. The old three-carrier-local four-tail feature/cost contract does not automatically apply to the transition-only scalar solver.

## Sources and scope

The pinned closure-and-characters.md was directly fetched and checked at commit 08b73637d4136f91606aad332c46cafd064417f8, blob 946f96670ecb8152eaae16195329f9eb1243b7ae. Section 1 proves ordinary normalized End Čech closure before extraction; section 2 proves that the actual mixed source is pure full sign and retains all three gerbe terms; section 3 explicitly supplies the finite chain inclusion J=(1+h0 δ)^(-1)j; section 4 identifies the deck eigensheaf twist as -2 in every selected factor. Thus for the full-sign scalar direct summand the twist is exactly O(-2,-2,-2,-2). Trace splitting End E=O Id⊕End0 E is equivariant and commutes with the Čech differential in characteristic zero. Künneth then proves the required scalar H² vanishing without using any finite-model rank assertion.

Source: https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md

This derivation uses the pinned source-formula excerpts and their fixed row convention. Its algebra agrees with the trace-free identity in `direct-scalar-free-pairing-reduction.md`. It does not evaluate O2.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
