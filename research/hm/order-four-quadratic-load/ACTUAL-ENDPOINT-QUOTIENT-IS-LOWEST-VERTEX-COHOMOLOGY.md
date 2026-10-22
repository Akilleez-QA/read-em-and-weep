# The endpoint quotient is the lowest vertex cohomology, not full restriction

## Result and correction

Let U=X minus C and retain the actual Serre bundle E=G. The endpoint quotient

    Cplus/J = H1(X,E)_+/D5 = P4

is canonically identified with the LOWEST positive tangent-degree-four vertex cohomology

    H1(L,Wprime O_L(-3)) = Wprime tensor W = P4.   (1)

The map is restriction to U FOLLOWED BY this lowest filtration quotient. Its kernel on the global nine-space is exactly D5.

It is false that this D5 restricts to zero in the full H1(U,E). In fact the full restriction H1(X,E)->H1(U,E) is injective. The discarded D5 survives in higher filtration. Confusing full restriction with its lowest quotient would lose genuine actual extension information.

For the normal-variation trace null-homotopy, the component-constant term alpha cancels identically on U. However the nilpotent term still requires its degree-twelve trace correction. The resulting lowest secondary operation is specified in Section 4; applying the lowest operator to eta without that correction is not the same operation.

## 1. The canonical lowest actual coefficient

Use the actual residue-normalized vertex eigenextension E_v. Its frame lines are O_L(9/2), O_L(-5/2) on the root gerbe. A tangent of diagonal cover degree four would have coefficients

    v1 of degree -1,     v2 of degree 1.

Thus v1 is absent and the coefficient sheaf is exactly

    Wprime O_L(-5/2-1/2)=Wprime O_L(-3).           (2)

The homogeneous transition g->g+p f sends v2 to v2+p v1, so it acts trivially on this lowest coefficient apart from its already displayed line factor. The actual E|U differs from E_v by I+tN_C. Since N_C has weighted tangent-degree shift eight, this correction cannot change (2) or introduce a lower term.

Consequently truncation at the lowest positive tangent degree gives a canonical quotient of the actual filtered sheaf on U, not a claim that E itself splits homogeneously. There is no earlier positive coefficient. Exact tame projection to L therefore produces a well-defined map on H1 into (1).

The wedge map on this piece is v2 |-> f v2. Its image is the degree-four part of I_Z(2). The actual cubic quotient gives

    0 -> Wprime O_L(-3) --f--> D5 O_L
      -> V O_L(2) -> 0.                          (3)

In particular (2) is also identified with the entire lowest ideal coefficient, not merely a subquotient of equal rank.

## 2. The exact global-to-lowest diagram

The actual global Serre quotient identifies

    H1(X,E)_+ = H1(I_Z(2))_+
              = H0(V O_L(2)) = V tensor A=P4+D5,

using the normalized pure-vertex degree-four residue. This normalization retains the conic: global positive quadratics remove the reduced-vertex A and conic D5 components, not the extra pure-vertex D5.

Restricting the Serre quotient to U, then taking its lowest piece, sends such a residue r to its connecting class in (3). Its cohomology sequence is

    0 -> D5 -> V tensor A
      --delta_f--> H1(Wprime O_L(-3)) -> 0,       (4)

because H0(Wprime O(-3))=0 and H1(D5 O)=0. The first arrow is the actual polynomial restriction Q(D5), not an arbitrary D5 embedding. It is exactly the established multiplication subspace J=D5 xi_Q after the actual Serre identification.

The wedge comparison (3) commutes with the actual Serre restriction maps, and the lowest section-line kernel is absent: a scalar multiple of sigma in tangent degree four would require a scalar of cover degree minus four. Hence the lowest E cohomology map is precisely delta_f. Equation (4) proves (1), including its canonical kernel and surjectivity.

This is a filtered statement about the actual E, with its conic correction retained. No splitting of the full H1(U,E) is required.

## 3. Why the full D5 restriction is nonzero

For a locally free sheaf on the smooth stack X, local cohomology sheaves supported on the regular codimension-two conic vanish below degree two. Tame chart descent preserves this statement. Thus

    H1_C(X,E)=0.

The localization sequence gives an injection

    H1(X,E) -> H1(U,E).                           (5)

Consequently its global D5 summand is NOT killed by full restriction. It is killed only by the projection in (1).

There is a concrete compatible higher channel. The cover-degree-four scalar piece of O_U is D5 O_L(-2), with H1=D5. Moreover H0(U,I_Z(2))=0: degrees zero and two contain no ideal, degree four has kernel H0(Wprime O(-3))=0 in (3), and every higher coordinate degree has negative base line degree before taking an ideal subbundle. The local Serre sequence therefore injects H1(U,O_U) into H1(U,E).

Multiplication by sigma sends that scalar degree-four channel to tangent degree twelve. This explains how a D5 can survive actual restriction while being invisible in degree four. This paragraph identifies an available actual higher channel; (5), not an uncomputed comparison of channels, proves the nonzero restriction.

## 4. What the actual trace null-homotopy becomes at the lowest degree

Write the actual shadow as alpha e_v+beta n8, with alpha and beta both nonzero. On U, e_v is the constant one. Choose homogeneous local polynomial lifts n_i of n8, and scalar shadow lifts

    s_i=alpha+beta n_i.

The actual quotient operator is T=H D+u, so T(1)=u. Therefore the previously established scalar subtraction is EXACTLY

    T(s_i)-alpha u = beta T(n_i).                (6)

There is no surviving alpha term even as a local cochain in this choice. This is stronger and more precise than saying an unspecified subtraction is cohomologically exact.

The actual n_i have cover degree eight. For the associated-graded degree-four operator T_4, T_4(n_i) has degree twelve. The ordinary square vertex algebra vanishes in degree twelve, so this is a genuine section of (I_Z^2(4))_12. It need not be zero as an ideal section.

Let L_4 be the lowest degree-four associated-graded part of the ACTUAL adjoint operator L. Let eta_8 be the actual trace-degree-eight leading normal cocycle, normalized compatibly so

    q(eta_8)=beta delta(n_i).

At target trace degree twelve the actual square sequence is

    0 -> Wprime O_L(-3) --tau--> B_(2;12)
      --q--> (I_Z^2(4))_12 -> 0,                 (7)

where B_(2;12) denotes the corresponding adjoint coefficient bundle. Its right term is the entire polynomial degree-twelve piece Sym^12(Wprime) O_L(-2), because the square quotient has no such degree. The kernel is exactly the tangent-degree-four coefficient (2).

Choose local degree-twelve trace lifts K_i with

    q(K_i)=beta T_4(n_i).

Then the LOWEST endpoint cohomology class is represented by

    tau(gamma_4)=L_4(eta_8)-delta(K_i),
    [gamma_4] in H1(Wprime O_L(-3))=P4.           (8)

Equation (8) follows by taking the indicated actual graded pieces of the established commuting trace/operator diagram. Changing the lifts or compatible cochains changes gamma_4 by a coboundary, as in the full diagram. It is therefore an exact secondary-operation formula, not a prescription to choose a favorable lift.

The correction K_i is of precisely the degree that affects (8). It cannot be dropped merely because T kills n8 in the square QUOTIENT. Formula (6) removes alpha; it does not remove this beta-dependent correction.

## 5. The actual degree-four operator IS the homogeneous operator

The independent ACTUAL-CONE-OPERATOR-PATCHING-FROM-THE-CONIC-COCYCLE.md now supplies the required comparison, for the explicitly checked input a=t^2, h=X^2Y^2 and its prescribed symbol and scalar. The explicit formula comparison in this paragraph has that input scope; it is not evidence by itself for h=X^4 or h=XY^3. Its homogeneous cone connection A_hom has weighted diagonal degree four and patches on the actual bundle after adding c_i n, where c_i has positive-cover degree four and n has weighted diagonal degree eight. Thus this actual patching correction has weighted diagonal degree TWELVE.

The patching theorem verifies the complete root-frame transport, physical O(4) operator twist, and trace-free determinant connection. It constructs a genuine actual cone operator, not merely a compatible quotient action. Its section-line action is the prescribed physical scalar determined by the actual u from the Serre/Ext construction; adding c_i n leaves that action unchanged.

Compare it to the fixed actual operator with this SAME symbol and prescribed physical section-line action. Their difference is a global trace-free endomorphism ell n. The twist is important:

    ell n in B(4),     n in B(2),     ell in H0(O_X(2)).

Every global ell has nonnegative positive-cover degree, so ell n has weighted diagonal degree at least EIGHT. There is no negative-cover-degree polynomial sector that could lower this to four. Thus neither the degree-twelve patching correction nor the remaining degree-at-least-eight normalization freedom affects the degree-four part.

The normal-variation operator is NOT merely HD+ad_A. In the fixed actual physical normal-equation convention it is

    L(E)=H D E+[A,E]+H rho E,
    Dq=q rho,     Lambda=H rho-u.

The normal-equation term H rho E is retained unchanged in the comparison. The cone patching theorem does not redefine rho or determine it independently from a choice of normal frame. Here both operators use the same already fixed ambient derivation and natural normal-line action from ACTUAL-NORMAL-VARIATION-TRACE-HAS-A-GLOBAL-NULL-HOMOTOPY.md. A change q0=nu q must transport its equation-unit term as well; the determinant trace subtraction is not permission to omit this normal-equation term.

Consequently the actual L_4 in (8) is precisely

    L_4(E)=H D E+[A_hom,E]+H rho E,               (9)

in those matching coefficient frames. Its quotient operator is the already proved T_4=HD+u. This removes the former operator-identification gap at this degree, while leaving the full actual cone operator and its normal connection distinct from their lowest representatives.

For completeness, the source adjoint has minimum trace degree six. A correction of diagonal degree at least eight sends even that source to trace degree at least fourteen, above the target trace degree twelve in (7). It therefore cannot feed the desired piece through a lower representative. The lowest operator (9) has degree shift four, so source degrees above eight cannot feed it either. The invariant source degree-six cohomology vanishes by the leading-normal-class theorem, allowing that component to be removed compatibly before taking (8).

Thus the endpoint quotient is EXACTLY the homogeneous secondary calculation (8),(9), with the actual eta_8 and its compatible nilpotent scalar lifts. The trace-lift correction K_i remains essential: nothing in this comparison replaces (8) by L_4(eta_8) alone. No value, nonvanishing, or rank of this secondary calculation is asserted here. In particular beta!=0 does not by itself make the resulting map nonzero, and no fourth Bockstein is evaluated.

### General input lemma and its precise hypothesis

The degree argument is not peculiar to h=X^2Y^2. For ANY homogeneous degree-four cone operator with the prescribed actual symbol and actual section-line scalar, already compatible on the vertex eigenextension, finite transport through I-t n has discrepancy

    C n,     C=H Dt+Lambda t.

The conic cocycle t has positive-cover degree zero and physical O(-2), while H and Lambda have cover degree four and operator twist four. Consequently C has cover degree four and physical twist two. Its coefficient bundle is Sym^4(Wprime) O_L(0), whose H1 is zero. Regular local scalar splits c_i therefore exist. Their corrections c_i n start at weighted diagonal degree twelve. Hartogs and the same ell n ambiguity prove exactly the degree-four comparison above for every input satisfying this hypothesis.

This is a general geometric patching proof, not an inference from one tested polynomial formula. The actual scalar u and the natural determinant/normal-line action must belong to the input being considered. A homogeneous formula for a new h must either arise from that natural compatible construction, or have its chart regularity and prescribed section equation verified.

There is a useful uniqueness test for that verification. On a regular chart, two regular trace-free homogeneous degree-four solutions of the SAME prescribed symbol and section equation differ by ell n. Homogeneity would require ell to have cover degree minus four; regular positive-coordinate polynomials contain no such term. Thus the solution is unique. Natural transport preserving the actual determinant-normalized equation must preserve this unique solution, provided the proposed local formulas are regular in the full charts. This supplies a structural covariance proof when those local hypotheses are checked. It does not authorize substituting a meromorphic candidate without its chart regularity, or importing the scalar from a different h.

### The two endpoint inputs satisfy the hypothesis

ACTUAL-TWO-ENDPOINT-INPUTS-HAVE-COMPATIBLE-CONE-OPERATORS.md now checks these hypotheses separately for a=z^2, h=X^4 and h=XY^3. For each input it proves the complete actual source identity, identifies its own actual u by the scalar-cup isomorphism, constructs both regular triangular-chart connections, and verifies their exact section equations and weighted degrees. Natural determinant transport contributes H D(log det P0)=-4zH, canceling the x-chart scalar term 4zH and yielding precisely the y-chart scalar -u. The uniqueness argument above consequently proves full covariance, not merely compatibility of their divisor quotients.

The general conic-cocycle argument therefore applies to BOTH inputs. Equation (9) has no outstanding degree-four operator-identification ambiguity for either one. Equation (8) still contains all trace-correcting K_i and remains unevaluated here. This is a statement about actual input data for the secondary calculation, not its value.

## Sources and verification

The actual nine-space and the polynomial D5 arrow are established in POSITIVE-SERRE-RESIDUE-AND-CANONICAL-CONE-OPERATOR-CORRECTION.md. The actual cubic grade is justified by UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md together with its actual identifications in the Serre-residue sources. The conic extension and degree shift are from ACTUAL-CONIC-RESIDUE-FORCES-VERTEX-SERRE-COCYCLE.md. The normal input is ACTUAL-NORMAL-CLASS-HAS-A-NONZERO-LOWEST-VERTEX-DIAGONAL.md. The full secondary diagram and actual operator conventions are from ACTUAL-NORMAL-VARIATION-TRACE-HAS-A-GLOBAL-NULL-HOMOTOPY.md. The newly established actual-versus-homogeneous operator comparison is supplied by ACTUAL-CONE-OPERATOR-PATCHING-FROM-THE-CONIC-COCYCLE.md, with its complete root-frame verifier.

Run python verify_endpoint_lowest_vertex_cohomology.py. It checks the exact characters, line/degree arithmetic and the regular-pair square Hilbert-series cutoff. The actual sheaf maps and the now-proved operator comparison are supplied by the stated geometric inputs. No actual coefficients or actual-instance ranks are evaluated; frozen sources are unchanged.
