Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# The product root line, physical frames, and determinant normalization

## Result and exact model

Let C be the smooth projective completion of y²=x³−x in characteristic zero, O its point at infinity, X=C⁴, and

    Theta_prod = sum_(r=1)^4 pr_r^*(O),
    N = external tensor product O_C(O) = O_X(Theta_prod).

Let q:X→Y=(P¹)⁴ be the product of the x maps. On Y let rho:Y→P⁴ send ((X_r:Y_r)) to the coefficients v_j of

    product_(r=1)^4 (Y_r+X_r Z) = sum_(j=0)^4 v_j Z^j,

and put f=rho q. We prove an explicit isomorphism N²≅f*O_P⁴(1), including its actual legal frames at infinity. The source-prescribed homogeneous complex, pulled back by f and tensored with N, is exactly

    K: N^-1^5 → N^15 → N^3^10 → N^5^2

in degrees (-1,0,1,2). The source's physical splitting factors and reciprocal row transitions follow from these line frames. On the stated legal/carrier cover they are regular, and the previously established oriented primitive determinant normalization agrees with the canonical trivialization of det H⁰(K). This removes the ambient external-product/root-line and physical transition-frame premises for this explicit declared model.

This does not identify an unspecified alternative geometric construction with this model, prove arbitrary software arithmetic or jets correct, evaluate any actual source/residual/detector, or settle an obstruction. No actual matrix products, source evaluation were performed. All matrix formulas below are formal morphism identities deduced from accepted structural contractions and line-frame changes.

## 1. What the sources actually define

Source identity matters here; a squared-line identity alone cannot identify a chosen root, since roots may differ by two-torsion.

1. The [finite Ext model, Statement and §1](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md) explicitly defines N as the exterior product of the four degree-one origin line bundles, q as the product of x maps, rho as the symmetric quotient, f=rho q, and the finite coordinates v_j=e_j(x_1,...,x_4). It displays the four line-bundle terms before and after pullback/twist. We use these definitions, not its numerical Ext calculations or execution claims.
2. The [current scalar proof README, Model provenance](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/README.md) links that exact Ext-model document as its mathematical context. The [ambient second jet, §1](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/ambient-second-jet.md) declares X=C⁴ and the complex with N=O_X(Theta), using the actual matrices and local contractions from the geometric dependency. That document alone does not define an effective representative of Theta. In the explicit product model of item 1, O_X(Theta) means the line N just defined, and Theta_prod is its displayed representative; no equality with an unrelated theta divisor is inferred from notation.
3. The [first-order source, §1](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md) specifies the two one-factor opens and frames, the product ratio nu=product(y_r/x_r)^m_r, the old squared frames and connections, the nu^-2 differential, and the exact column factors of U0 and U1. Thus the source supplies the product cocycle itself, not merely the name N. Its product transition ratios identify the same external-product line and exclude a hidden two-torsion root change.
4. The coefficient product is prescribed literally in the [chart source](https://github.com/Akilleez-QA/read-em-and-weep/blob/dc60a859a0157b1d2d1b57b37324509abc22c600/research/hm/current-scalar-geometric-dependencies/checks/verify_chart_and_lines.py), read here as inert text. The accepted homogeneous proof independently proves its chart law from the factors, without executing that checker. The immutable source-formulas JavaScript and raw-engine snapshots use the same descending elementary-symmetric recurrence. Section 6 binds the displayed frame factors to their exact source text.

Fresh read-only public sources and inherited inert inputs are pinned in source-pins.json. The accepted one-curve proof at [52592f3](https://github.com/Akilleez-QA/read-em-and-weep/blob/52592f30d40fbee055b8b9b513666d0de4082aed/research/hm/null-root-line-geometry/PROOF.md), accepted homogeneous bound, full structural contraction, and determinant-volume proof are dependencies, not historical execution receipts. Their exact local snapshots are pinned separately.

The conclusion is source-bound to this declared product construction and these frames. In particular it does not newly prove the named bundle's identification with every classical Horrocks–Mumford presentation; the theorem below concerns the precise homogeneous matrices already authenticated by the structural proofs.

## 2. The x map and its explicit square root

Write P_a=(a,0), a=0,1,-1. The divisor calculation in the one-curve proof gives

    div(x)=2P_0−2O,
    div(y/x)=P_1+P_-1−P_0−O.

Here y is a uniformizer at each P_a. At infinity use t=1/x and u=y/x², with u²=t(1−t²); u is a uniformizer and ord_O(t)=2. These facts follow from the nonzero partial derivatives in the respective local equations.

The two global sections 1 and x of O_C(2O) have section divisors 2O and 2P_0. They have no common zero. They therefore give a morphism x_C:C→P¹ with coordinates [X:Y]=[x:1] on the finite chart. The associated line isomorphism is

    x_C*O_P¹(1) → O_C(2O),       X ↦ x, Y ↦ 1.                 (1)

This is an actual isomorphism: where Y≠0, its pulled-back frame maps to 1; where X≠0, its pulled-back frame maps to x. Both are nonvanishing local sections. In particular the infinity preimage is the divisor 2O, not O. Multiplication of divisor sheaves gives O_C(O)²=O_C(2O), and (1) fixes the square-line identification, including its scalar convention.

The source's legal opens are

    U0=C minus {O},
    U1=C minus {P_0,P_1,P_-1}.

The sections e0=1 and e1=y/x frame O_C(O) on U0 and U1, respectively. The rational-function pole of e1 at O is absorbed by the divisor O. The old squared frames are ell0=1 and ell1=x, and

    e0²=ell0,     e1²=(1−x^-2)ell1.                            (2)

On U1 the coefficient in (2) is a unit. At infinity put s=1−t². The frame n_infty=1/u of O_C(O) has

    e1=s n_infty,     ell1=s n_infty²,     e1²=s ell1.

Thus the square identification is regular and invertible there. No square-root function of x or t is needed or asserted.

## 3. The product coefficient morphism and global root line

Let M=O_Y(1,1,1,1). Every v_j is a section of M. They have no common zero: the product of four nonzero binary linear forms is nonzero over every residue field. Consequently rho is a morphism, and its basepoint-free section construction gives a specified isomorphism

    rho*O_P⁴(1) ≅ M

sending each coordinate section to its coefficient v_j. This follows from the same local-frame construction used in (1), not just from a numerical multidegree count. Pulling back factorwise and using (1) gives

    f*O_P⁴(1) ≅ q*M ≅ external product O_C(2O) ≅ N².            (3)

The last multiplication map sends the square of the rational reference e_ref=product e0 to L_ref=1. Thus (3) has a fixed normalization. It also proves N=O_X(Theta_prod) directly, since tensoring pullbacks of divisor sheaves adds their divisors.

For an infinity subset A⊂{1,2,3,4}, put tau_A=product_(r∈A)t_r and use on the standard product chart the square-line frame

    ell_A=(product_(r∈A)x_r)L_ref=tau_A^-1 L_ref.

The coefficient vector relative to ell_A is v_A=tau_A v_ref, obtained factorwise from t_r+Z=t_r(1+x_r Z). This is the 16-chart dictionary of the source. The equality is an equality of local sections on overlaps, including the rational extension to their charts; it does not require expanding a product polynomial.

For a legal mask m, let U_m=product U_(m_r) and

    e_m=product e_(m_r)=nu_m e_ref,
    nu_m=product_(r=1)^4(y_r/x_r)^(m_r),
    c_(m,A)=e_m²/ell_A=nu_m² tau_A.                            (4)

On U_m intersected with standard chart A, c_(m,A) is a regular unit, because its numerator and denominator are two frames of the same line. This can also be checked one factor at a time:

    finite chart:    bit 0 → 1,        bit 1 → (x²−1)/x;
    infinity chart:  bit 0 → t,        bit 1 → 1−t².

In the infinity bit-zero case the legal domain excludes O, so t is a unit. In the infinity bit-one case 1−t² is a unit even at O. These four cases cover all legal/product intersections. Formula (4) is the algebraic replacement for the source's formal normalized relation nu_B=tau^(1/2)nu_A: only the squared normalized ratio and its appropriate integral powers are needed below.

The actual sections e_m are retained at infinity. They are not replaced by a formal square root of ell_A or by a function incorrectly declared regular.

## 4. The pulled-back complex and existence of regular physical splittings

Use the source's homogeneous type convention on P⁴:

    L^-1=O(-1)^5, L^0=O^15, L^1=O(1)^10, L^2=O(2)^2.

By (3), f*L tensored with N has exponents 2(-1)+1,2(0)+1,2(1)+1,2(2)+1, namely (-1,1,3,5). Its consecutive maps have coefficients that are sections of N²; in the e_m frames they therefore have coefficient matrices

    c^-1 gamma(v_A),  c^-1 delta(v_A),  c^-1 ev(v_A),           (5)

where c=c_(m,A). On the finite rational reference chart these are nu_m^-2 times the source's unweighted matrices. This derives that scaling from (3), rather than choosing a convenient unrelated gauge.

The accepted homogeneous theorem gives the degrees

    gamma,delta,ev: +1; H0,H1,eta: −1; W,L: 0;
    I columns: (0,1); P rows: (0,−1).

A section of degree d has its coefficient multiplied by c^-d when the square-line frame changes from ell_A to e_m². Hence the actual coefficients of the local inclusion, projection, and homotopies are

    I_m=I(v_A) diag(1,c^-1),       P_m=diag(1,c)P(v_A),
    H0_m=c H0(v_A), H1_m=c H1(v_A), eta_m=c eta(v_A),
    W_m=W(v_A), L_m=L(v_A).                                    (6)

The cohomology coefficient module here is N⊕N^-1, with its chosen local frame (e_m,e_m^-1). Formula (6) describes the images of this chosen frame in the ambient N^15 frame e_m. It does not assert that these local cohomology summands glue separately.

For completeness, these are regular maps on an actual cover. Set Pi=product v_j, h_j=v_j^5−Pi and a=v0v1v3v4. The six opens D(h_j),D(a) cover P⁴: if all h_j vanish and Pi=0 then every v_j=0, impossible; if Pi≠0 then a≠0. The homogeneous primitive theorem makes every primitive regular on its own carrier; its power-two auxiliary clearance already includes v0=0. Intersect their pullbacks with the 16 legal opens U_m and standard product charts. The c factors are units by §3. The accepted homogeneous contraction therefore gives regular local inverses and a splitting onto rank two on every such open. Pullback preserves these explicit split identities without a flatness assumption.

The source's splits become

    U0_m=[c^-1 gamma | I_col0 | c^-1 I_col1 | c H1W],
    Q0_m=[c H0 ; P_row0 ; c P_row1 ; c^-1 Ldelta],
    U1_m=[W | c eta],              Q1_m=[L ; c^-1 ev].          (7)

Extreme split bases are identities. The differential (5) sends the first contractible block identically to the first block of U0_m, sends the last eight U0_m columns to the W columns of U1_m, and sends its last two columns identically to the final term. These assertions use only the accepted contraction equations, not a new matrix product calculation.

Every block of (7) has degree d and factor c^-d. Under A→B, v_B=(tau_B/tau_A)v_A and c_(m,B)=(tau_B/tau_A)c_(m,A). Thus (7) agrees exactly across standard chart changes for fixed actual legal frame e_m. This proves all-chart compatibility without adjoining sqrt(tau), assuming a finite pole bound at a missing divisor, or suppressing a legal-line factor.

Ramification caution: on Y, t_r cuts its boundary to order one; on X, t_r vanishes to order two along the origin divisor. Pullback of an owned-factor power bound stays a power bound in that factor. Numerical valuations must be multiplied by ramification; for example a double v0 pole on Y can become order four on X. No order-one assertion about t at O is used here.

## 5. Common ambient frames give the exact row transitions

Work temporarily in the common rational reference e_ref; this is a legitimate comparison on the dense finite locus, not a claimed regular frame everywhere. A vector in a summand N^k with coefficient z in e_m^k has coefficient nu_m^k z in e_ref^k.

Multiplying each block of (7) by the corresponding ambient factor gives the common-frame split columns

    degree -1: nu^-1 Id5;
    degree  0: [nu^-1 gamma | nu I_col0 | nu^-1 I_col1 | nu^3 H1W];
    degree  1: [nu^3 W | nu^5 eta];
    degree  2: nu^5 Id2.                                      (8)

Each contractible pair has the same factor at its two ends: nu^-1, nu^3, or nu^5. In particular, the actual two cohomology columns in the common ambient frame are

    beta_i = [I_(c_i) D_i],       D_i=diag(nu_i,nu_i^-1),       (9)

where brackets mean classes modulo the image of gamma. The corresponding common-frame projection is D_i^-1 P_(c_i).

For two owners i,j, the accepted quotient-resolution identity gives

    [I_j]=[I_i](P_i I_j).

Applying (9) yields beta_j=beta_i G_ij with

    G_ij=D_i^-1(P_i I_j)D_j,
    g_ij=G_ij^t=D_j(P_i I_j)^tD_i^-1.                         (10)

The diagonal matrices are symmetric. For column coordinates G_ij G_jk=G_ik; for row coordinates g_jk g_ij=g_ik. This is exactly the pinned source's order, not a guessed transpose convention. The actual local construction in §§3–4 gives regular quotient frames, so (10), first compared in a common function field, is their regular transition on every legal overlap. Since X is integral, equality on the dense comparison locus implies equality of these already-defined regular morphisms throughout the overlap. It does not manufacture regularity from a rational equality.

The omitted common ambient nu factors in the raw engine's I_phys/P_phys leaves are now accounted for: the correct common-frame leaves are exactly I D and D^-1 P. The intermediate e_m-frame inclusion and projection in (6) instead have the unequal factors (1,nu^-2) and (1,nu²). These are distinct coordinate descriptions of the same quotient maps.

## 6. Binding to the actual frozen source and old connections

The new static checker reads only source text/AST. It authenticates hashes and exact selected syntax in both implementations:

- raw_engine.nu is the product over legal bits of y_r/x_r; Dframe is diag(nu,nu^-1), with reciprocal inverse option;
- raw_engine.blocks concatenates (gamma,I,H1W) and (W,eta), uses w0=(nu^-2 repeated 5,1,nu^-2,nu² repeated 8), w1=(1 repeated 8,nu² repeated 2), and applies reciprocal inverse-row factors;
- raw_engine.g is D_j transpose(P_i I_j) D_i^-1;
- the source-formulas JavaScript has the same column arrays, inverse rows, left factors (nu_i^-1,nu_i), right factors (nu_j,nu_j^-1), and final transpose;
- both implementations assign weights (-1,1,3,5) in ranks (5,15,10,2).

These are the exact frame scalings derived in (5)–(10). The existing conditional moving-frame implementation bridge can therefore use the actual geometric frame interpretation just proved. A text/AST match is not a proof of arbitrary machine arithmetic or of normalized higher jets. The JS convention nu[0]=1 retains nonzero derivative slots, as its source explains; this packet does not execute or certify that jet implementation.

The square-line frame used for coefficients in (5) is e_m². The old connection is different data: it is the tensor sum of the half-connections flat in

    ell_m=product ell_(m_r),
    e_m²=h_m ell_m,       h_m=product(1−x_r^-2)^(m_r).

Consequently its coefficient in the actual e_m frame is

    alpha_m = (1/2)dlog h_m
            = sum_r m_r dx_r/[x_r(x_r²−1)].                    (11)

This is regular on U_m and is precisely the source's old connection. In the common reference it is alpha_m−dlog nu_m. The one-curve identity, tensored and summed, gives

    (nabla_j−nabla_i)|N^k
       = −(k/2)sum_r(m_jr−m_ir)dlog x_r,
    (nabla_j−nabla_i)(V_r)|N^k
       = −(k/2)(m_jr−m_ir)y_r/x_r.                            (12)

Here V_r(x_r)=y_r and V_r(y_r)=(3x_r²−1)/2. At infinity V_r(t_r)=−u_r and V_r(u_r)=(3t_r²−1)/2; alpha_bit1=−t_r dt_r/(1−t_r²). Thus the source's distinct logarithmic nu derivative, old alpha, and q are geometrically identified on the product. Setting alpha to zero in the retained e1 frame would contradict (11).

For B=−(dU_m)U_m^-1−k alpha_m Id, (7) and (11) give the exact physical split-connection meaning stated in the source. Under common-frame conversion U→nu^k U, the split connection gains −k dlog nu and the old connection gains the same term; their difference B is unchanged. This supplies the frame/old-connection premise to the earlier formal derivative lowering, while keeping arithmetic and derivative-engine correctness separate.

## 7. Determinant line and the specific normalized frames

For the untwisted four-term complex on P⁴, with determinant signs (-,+,-,+),

    det L = det L^-1^(-1) ⊗ det L^0 ⊗ det L^1^(-1) ⊗ det L^2
          = O(5−10+4)=O(-1).

Its alternating rank is −5+15−10+2=2. Therefore

    det K ≅ f*O(-1) ⊗ N² ≅ O_X,                              (13)

where the last isomorphism is precisely (3), not merely vanishing first Chern class. Equivalently the direct N exponent is 5+15−30+10=0.

The local contractions identify det H⁰(K) with det K by cancelling the paired contractible summands. The determinant-volume proof fixes their ordered bases: U=[gamma,I,H1W], V=[W,eta]. It establishes lambda_c=det U/det V=1 for every carrier by sparse oriented minors. The now accepted structural contraction supplies its former A premise. The homogeneous extension supplies the same identity in every square-line frame: numerator and denominator each have homogeneous degree −2, so their ratio has degree zero and is determined by the finite reference.

Thus, before twisting, the ordered carrier cohomology wedge has coefficient exactly one in the O(-1) determinant frame, with the already specified determinant-order convention. Pulling back and tensoring with N multiplies a rank-two cohomology determinant by N². Formula (13) cancels these lines. The legal two-column frame (9) has det D_i=nu_i nu_i^-1=1, so its wedge is that same trivializing volume. It follows structurally that

    det G_ij = det g_ij = 1                                   (14)

on all legal overlaps. This is compatibility of the PARTICULAR stored oriented frames with the canonical determinant trivialization. Triviality of det K alone would not prove (14); a carrier-dependent GL2 regauging could change its volume. The independent sparse normalization and exact factors (9) are both essential.

Consequently rank-two adjugates agree with the actual inverses of these transitions, and for any correctly interpreted derivation D,

    tr(g_ij^-1 Dg_ij)=D(det g_ij)/det g_ij=0.

These are geometric/algebraic consequences for this model. They are not an attestation that an implementation's derivations or inverse routine executes correctly.

## 8. A bounded deck-line consequence

The one-factor map x_C is finite flat of degree two: over the finite chart its algebra is k[x]⊕k[x]y with y²=x³−x; over the infinity chart it is k[t]⊕k[t]u with u²=t−t³. Both are free rank two, and on the overlap

    u=t² y.

The involution sends y,u to their negatives. Hence

    (x_C)_*O_C = O_P¹ ⊕ O_P¹(-2),
    q_*O_X = direct sum_(S⊂{1,2,3,4}) O_Y(-2S).               (15)

The transition of the odd basis is exactly t²=x^-2, the transition of O(-2). This proves (15) directly, rather than importing a deck-character receipt.

A degree-r strict endomorphism of K has line factor N^(2r)=f*O(r), since the common N twist cancels. On Y this is O(r,r,r,r). Its full-sign direct-image component therefore has line

    O_Y(r−2,r−2,r−2,r−2).                                    (16)

More explicitly, write a full-sign coefficient in the finite chart as (product y_r)b_ref and in chart A as (product of u_r for r∈A, y_r otherwise)b_A, multiplying in each case the local degree-r line frame ell_A^r. Equality and u_r=t_r²y_r give

    b_A=tau_A^(r−2)b_ref.                                    (17)

For r=−2 this is tau_A^-4 and O_Y(-4,-4,-4,-4), exactly the source's declared boundary-line dictionary. This is a theorem for any full-sign section of the indicated End-degree, once its membership and degree are established. It does not prove a particular residual/HPL expression lies there, has a particular pole bound, is closed, or represents the desired obstruction. No stronger source attribution is concealed in (17).

## 9. Dependency closure and retained frontier

Closed for the specified construction:

- the actual external-product line and coefficient morphism, with source provenance;
- N²=f*O(1) as an explicitly normalized line isomorphism;
- weights (-1,1,3,5), regular physical local splittings and actual row-frame transitions;
- tensor old connections, common-frame differences and q on all legal charts;
- compatibility of the specific determinant-one normalization with N² cancelling f*O(-1);
- the structural full-sign degree-r chart law, conditional only on membership in that sheaf component.

Still separate: exact implementation/arithmetic semantics; JS normalized jet correctness; identifications with other presentations not fixed by these sources; complete source-generator and residual attribution beyond the displayed geometric leaves; higher pole/regularity and derivative ledgers; HPL/selector/kernel identifications; closedness and class comparison; detector values, the retained dual tests, and obstruction or algebraicity conclusions.

## Verification

Run python check_frame_metadata.py and python -O check_frame_metadata.py. Both authenticate source/dependency bytes and compare selected frozen AST/text contracts. They check integer weight, column, paired-block, determinant, and all 256 legal/standard-chart exponent relations, plus active negative controls. No model is imported, no actual matrix or polynomial product is evaluated, and no source object or jet is constructed. The divisor, basepoint-free, line-gluing, contraction, and determinant arguments above are the mathematical proof; static checks bind them to the displayed source and detect convention changes. Independent verification is recorded separately in REVIEW.md.
