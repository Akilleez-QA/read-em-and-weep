# Independent algebra audit

## Verdict and reviewed version

**PASS: no blocking mathematical defect found.** The first-subleading exact sequence, the exact formal normal form in §6, and the first-subleading norm integration in §7 follow under the hypotheses stated in `PROOF.md`.

- Reviewed file: `PROOF.md` in this directory.
- Frozen SHA256: `e8aa520d4d55be47ac6c9e5467d21d86e57a5ba0052aac0a5991aeb5ba2c7d25`.
- Review date: 2026-10-22.
- Method: independent universal algebraic derivation. No actual model coefficients, points, derivatives, selected matrices or ranks were evaluated; no model scan or large computation was used. The source file was not modified.

This review verifies the self-contained algebra and checks the §7 integration against the supplied local first-subleading norm proof and its fixed harmonic conventions. It does not re-audit that work's earlier geometric inputs or supply any missing geometric descent hypotheses.

## 1. First-subleading theorem

The weighted degrees are consistent throughout: the perturbation has entry degrees 12,10,14, while a weight-four trace-free gauge has entry degrees 4,2,6.

The polarization equation is

    2fg x + g² y - f² z = 0.

Coprimality implies f divides y and g divides z, including when f has repeated factors. Consequently the parametrization

    y=-2fp, z=2gr, x=gp+fr

is both exhaustive and unique. Direct multiplication independently gives the gauge action

    (p,r) -> (alpha f+beta g, gamma f-alpha g).

There is no sign or factor-of-two error in this formula.

The map S_4 direct-sum S_2 -> S_7 defined by (alpha,beta) -> f alpha+g beta is injective: f divides beta in any syzygy, and deg beta=2<3. Its domain and codomain each have dimension eight, so it is an isomorphism. Eliminating p therefore leaves precisely the quotient S_9/fS_6. Multiplication by g identifies this quotient with (S/(f))_4 because g is a nonzerodivisor modulo f and both graded pieces have dimension three over k.

For D=vn, the parameters are p=vf/2 and r=vg/2; eliminating p leaves vg. Thus nu(vn)=[v], with no missing factor of u or two. The kernel and injectivity statements follow from the same decomposition, and formula (9a) reconstructs the unique gauge for a chosen representative v. Independently checking (10) gives [X_ell,n]=f ell n, exactly the stated ambiguity and sign.

The order calculation in (11) is correct: conjugation by 1-X removes [X,n], while X²n and XD begin at weight 16. The universal realization with F=f+p and G=g+r has the required tangent term and is exactly square-zero.

## 2. Exact formal corollary

The additional full factorization (12) is essential to the stated corollary and is explicitly assumed rather than inferred from the first tangent equation. The proof stays inside this factored class.

### Pair reduction and determinant orientation

The Koszul resolution for the regular binary pair of degrees 3 and 5 gives an Artin quotient with top degree six. Hence every higher component of F and G lies in (f,g), with the coefficient degrees needed for the allowed gauge M. All corrections have positive transverse degree, so M is formally invertible. The physical matrix grading is closed under products and formal inversion.

For s=(f,g)^t and r=(g,-f), the independent alternating-form identity is

    n_0(Ms)=det(M) M n_0(s) M^(-1).

Thus conjugation by M^(-1) produces the scalar a=(U/u)det(M), not its inverse. The proof uses the correct determinant orientation.

### Removal of scalar units trivial in the quotient

Completion preserves the finite-length quotient, and its degrees divisible by four are exactly degrees zero and four. Choosing v_4 from the degree-four residue of a-1 gives b=a/(1+v_4) in 1+(f,g)R.

Writing b-1=g w_1-f w_2 degreewise is valid. Its degrees force w_1 to start in degree three and w_2 possibly in degree one. Therefore every entry of T-I_2=w(g,-f) has the required positive matrix weight, including the degree-one w_2 case. Since T s=s and det(T)=b, direct conjugation gives

    T n T^(-1)=n/b.

This establishes the exact normal form by a regular formal frame change, rather than by an unsupported rescaling of the fixed coefficient.

### Uniqueness and completeness

If Q conjugates a n to c n, its action preserves the fraction-field image line, so Qs=lambda s. Integrality of lambda is justified: k[[X,Y]] is a factorial regular local domain, and the finite-colength ideal (f,g) cannot have a common nonunit divisor. Applying the same argument to Q^(-1) makes lambda a unit.

The regular-pair syzygy gives Q=lambda I_2+w r, and hence

    det(Q)=lambda²+lambda r w,
    Q n Q^(-1)=(lambda²/det(Q)) n.

The scalar multiplier is one modulo (f,g). This proves necessity of the stated residue equality under all allowed gauges. Conversely, the pair-fixing construction above realizes every physical scalar ratio in 1+(f,g), proving completeness as well as uniqueness.

The first-order normalization agrees with nu explicitly: if the first terms of M are alpha_4,beta_2,gamma_6,delta_4 and h_4=u_4/u, then the tangent parameters are

    p=f_7+(h_4/2)f,
    r=g_9+(h_4/2)g.

Eliminating p leaves, modulo f, the scalar residue [alpha_4+delta_4+h_4], which is [a_4]. This independently confirms the normalization claimed at the end of §6.

## 3. Integration with the first-subleading norm formula

The §7 application is a first-order ambient frame change, not an assumption that the harmonic lift is multiplicative. Every entry of X has even cover degree, so the entrywise harmonic lift is available without lifting the odd factors f and g. All lifted entries have positive transverse order; 1-H(X) is therefore formally invertible.

Conjugation gives K'_[16]=K_[16]+[K_[12],H(X)] with the stated sign. Restricting to harmonic order zero gives

    B'_0=sD+[sn,X]=s(D-[X,n])=v_4 A_0.

Expanding each ordered product H(A_i)H(X) and H(X)H(A_i) gives exactly the sum in (19), with harmonic index j-i and the stated ranges. All resulting coefficients have matrix weight 16-4j. In particular the changes in B_1, B_2 and B_3 cannot be omitted.

Before harmonic extraction, the change of the cross pairing is tr(K_[12][K_[12],H(X)]), which is zero by cyclicity. Thus the entire fourteen-term norm sum is unchanged by this gauge; no individual-term invariance is needed or asserted. Removing B'_4 by a separate local q^4 correction changes the raw norm representative only through the actual source-multiplied relation image described in the norm proof. It does not establish global removability of B_1 through B_3. The scalar-reference subtraction and final global quotient remain necessary, as §7 states.

The application correctly distinguishes H(v_4 A_0) from H(v_4)H(A_0), and it does not transport the full ordinary-cover normal form to the ambient harmonic algebra without the additional normal terms.

## 4. Scope of the accepted result

The dimension three is over k=C(L), not a global three-dimensional complex parameter space. The conclusions are in a fixed regular adapted frame on the ordinary binary cover and, in §6, its formal transverse completion.

This review does not infer a global choice of f,g, regularity of the gauges at every point of L, compatibility on overlaps, analytic or algebraic convergence, extension of the actual full factorization, a normalization of other normal coefficients or the whole K_[16], an actual residue or beta4 value, a beta2-image statement, further-neighborhood existence, or algebraicity. These exclusions are correctly preserved in the proof.

No correction or additional hypothesis is required for the stated algebraic results.
