Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# Full character and ambient degree of the exact raw residual and lift

## Result and limits

For the exact frozen raw route, the complete residual R is a meromorphic row endomorphism of the physical rank-two cohomology bundle, of pure full deck character. The precise strict-resolution statement starts at

    J0=I_phys R^t P_phys.

For s=0,1,2,3, every block of the literal Js is a meromorphic section of End^(-s)(K) of pure full deck character. On Y=(P1)^4 its branch-safe character coefficient consequently lies in a multiplicity copy of

    O_Y(-s-2,-s-2,-s-2,-s-2).

The respective coefficient multidegrees are (-2,-2,-2,-2), (-3,-3,-3,-3), (-4,-4,-4,-4) and (-5,-5,-5,-5). R itself is an endomorphism of cohomology and is not silently substituted for a strict End(K) block. Its matrix entries in each specified physical owner frame are full-character meromorphic scalar functions; intrinsically its endomorphism bundle need not be trivial.

This closes the rational sheaf/character/degree membership premise explicitly retained by the product-root, legal-free-homotopy and ownerwise residual packets. It does not prove raw closure, HPL class identities, selector attribution, a Ward or Serre pairing, detector values, or an obstruction. Pole clearance is a separate input, and arbitrary software arithmetic or jet correctness remains separate. No numerical value, actual source or primitive matrix/polynomial, physical constructor, or source import is evaluated. 

## 1. Existing result checked and exact source

The accepted product-root proof, section 8, establishes the degree-r full-character line O(r-2,r-2,r-2,r-2) only once membership is known. Legal-free-homotopy section 3 also explicitly conditions its full-character consequence on the input. The ownerwise proof retains assigned-sheaf attribution in its hypotheses. These do not already prove the theorem here.

The newer [inner-boundary domain proof at 4c0e965](https://github.com/Akilleez-QA/read-em-and-weep/blob/4c0e965b4de72e43c39ba863f9aa8eea15571851/research/hm/null-inner-boundary-domain/PROOF.md), read afresh, proves covariance of a particular differentiated boundary word, then projects that word to full character. Its section 3 expressly needs no purity of unselected entries. The present theorem instead checks purity of every literal raw residual family and the complete undifferentiated J0-J3. No novelty is claimed for the general full-character line dictionary or for that differentiated boundary theorem.

The inherited inert sources are:

- [Raw engine](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-realization/raw_engine.py), SHA256 c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9.
- [Compiler](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-raw-regular-extension/inputs/compiler.py.txt), SHA256 28e95b87adefaba0d4ec886a7ab272f252f376bbb1fc26e0a387bc05f896a386.

The mathematical denotation is the actual raw route: source_and_lift constructs RawSource(model.M), whose T is the raw scalar s_raw, and passes its residual to the frozen Lift. Mat.inverse is the rank-two adjugate, not an independently normalized inverse expression; Mat.D denotes the exact invariant curve derivation V_d entrywise. The proof is about this rational denotation. AST authentication cannot by itself certify a field engine.

Pinned dependencies provide the explicit model X=C^4, C: y^2=x^3-x; N=external product O_C(O); the normalized identity N^2=f*O(1); and

    K^j=N^(2j+1)^(d_j), j=-1,0,1,2, (d_j)=(5,15,10,2).

They also provide the physical quotient frames and original-resolution homotopies. The scalar dependency proves that each raw s_(a,b;ij) is a genuine meromorphic scalar of character {a,b}, with its correct all-chart old-connection interpretation. Only that scalar typing and character result is needed below, not its numerical pole bound.

## 2. Deck characters and differentiation

Let G=(Z/2)^4 act by independently negating the four y coordinates. A subset is encoded by a four-bit mask; character addition is XOR, written + below. Let e_d be the single-bit mask in direction d. A rational function F has character a if sigma(F)=chi_a(sigma)F for every sigma in G; zero is allowed in any stated character space.

The source's primitive entries are rational functions of the coefficient coordinates v, hence are G-invariant. Its actual legal ratio

    nu_m=product_d(y_d/x_d)^(m_d)

and its inverse both have character m. Both diagonal entries of D_m=diag(nu_m,nu_m^-1) and of its inverse therefore have the same character m. The source formula gives

    g_ij=D_j(P_i I_j)^t D_i^-1,  character(g_ij)=m_i+m_j.

Every entry of the rank-two adjugate is a signed entry of g, so its character is also m_i+m_j. This does not use determinant one, inverse cancellation or a transition cocycle.

The invariant differential satisfies

    sigma V_d sigma^-1=chi_(e_d)(sigma)V_d.

On the finite chart this follows directly from V(x)=y and V(y)=(3x^2-1)/2. At infinity, with t=1/x and u=y/x^2, it follows from V(t)=-u and V(u)=(3t^2-1)/2. Both preserve their regular curve algebras. By the derivation and quotient rules this identity holds on the rational function field. Consequently V_d sends character a to a+e_d, even if direction d was already present. This is stronger and safer than assuming every derivative simply appends an odd factor. Second derivatives flip both specified bits.

Matrix composition adds characters; transpose, trace, entry selection and scalar multiplication preserve them. Addition preserves a character when every summand has it. These operations act entrywise in the displayed, fixed frames; the geometric frame interpretation is proved in sections 5-6.

## 3. Complete residual character ledger

For a distinct pair p=(a,b), use p also for e_a+e_b. Set p=(0,1), q=(2,3), so p+q=15. Write A=g_ij, B=g_jk, G=g_ik, and w_ab=m_a+m_b. The exact definitions give:

| source object | character |
|---|---|
| g_ab and its adjugate | w_ab |
| k_p(ab)=-((V_a g#)(V_b g)-(V_b g#)(V_a g))/4 | p |
| u_p(ab)=g_ab k_p(ab) | w_ab+p |
| mu_p(B,A) | character(B)+character(A)+p |
| each mu2(B,A) summand | character(B)+character(A)+15 |
| q_(ij,d) | e_d |
| b_p(ijk) | p |
| F_p=b_p-tr(G# mu_p(B,A))/2 | p |
| s_(p;ij), from the raw override | p |
| L_d=A# V_d A | e_d |
| U_d=A# B# (V_d B) A | e_d |

For k, the owner characters cancel twice. For F, w_ik+w_jk+w_ij=0. The raw B blocks and q each have the single character of their derivative direction, so the exact four-block scalar trace polynomial has character p; this is also the scalar dependency's branch-safe, all-chart theorem. The four fixed mu2 derivative tuples are (0,2;1,3), (0,3;1,2), (1,2;0,3), (1,3;0,2). Each uses all four bits once; their signs do not affect character.

Now retain every literal residual slot:

| family after its literal normalization | source slots | character |
|---|---:|---|
| G# u_p(jk)u_q(ij), and swapped p,q | 2 | 15 |
| G# mu_p(u_q(jk),A), and swapped p,q | 2 | 15 |
| G# mu_p(B,u_q(ij)), and swapped p,q | 2 | 15 |
| G# mu2(B,A) | 1 | 15 |
| G# b_p u_q(ik), and swapped p,q | 2 | 15 |
| G# b_p b_q G | 1 | 15 |
| F_q k_p(ik), F_p k_q(ik) | 2 | 15 |
| (V_a s_(q;jk))L_b, (V_b s_(q;jk))L_a | 2 | 15 |
| (V_b s_(q;ij))U_a, (V_a s_(q;ij))U_b | 2 | 15 |
| preceding four E slots with p and q exchanged | 4 | 15 |

The first ten slots are the seven kinetic and three gerbe slots inside the source's G# normalization. The next two are its Fk slots. The final eight are exactly E(p,q) and E(q,p). A representative E character is (q+e_a)+e_b=p+q; no scalar derivative is omitted. The whole baseline tracefree projection preserves character: tr(M0)Id has character 15, just as M0. Therefore the complete R has character 15, with no cancellations or dropped source families. In particular the proof does not require R to vanish or to be closed.

## 4. The exact lift preserves character and lowers degree

The raw leaf dispatcher supplies

    I_phys=I D_m, P_phys=D_m^-1 P,
    H(1)=H0, H(2)=H1, H(3)=eta.

Both physical inclusion/projection matrices have character m, so I_phys R^t P_phys has character m+15+m=15. The projector E=I_phys P_phys has character zero. Every H leaf is an unweighted primitive, hence invariant. Each literal homotopy branch

    h_v F_(u,v),
    (-1)^r E F_(u,v) h_(u+1)  (v=1, u<3)

therefore preserves character. Alternating restrictions do also: each underlying owner legal/carrier open is deck-stable, the action does not relabel an owner, and restriction commutes with the action. The scalar stage signs have no effect.

The block key (u,v) denotes Hom(K^(u-1),K^(v-1)), of degree v-u. J0 has key (1,1). Both homotopy branches lower v-u by one. Iterating the exact source predicates gives:

    J0: (1,1),                 degree  0;
    J1: (1,0), (2,1),          degree -1;
    J2: (2,0), (3,1),          degree -2;
    J3: (3,0),                 degree -3.

These are possible supports, not nonvanishing claims. Zero branches or accidental cancellations do not affect the theorem. Face deletion retains the original occurrence labels and frames. Nothing here asserts the recurrence is a lift of a cohomology class; it is a typed sequence of rational cochains regardless of closure.

## 5. Actual all-chart frame membership, without formal square roots

Parity on one affine chart alone would not supply this section. Fix a standard product chart A, with tau_A=product_(r in A)t_r, square-line frame ell_A=tau_A^-1 ell_ref, and v_A=tau_A v_ref. For legal owner i the product-root bridge fixes the ACTUAL frame e_i=nu_i e_ref and the integral ratio

    c_iA=e_i^2/ell_A=nu_i^2 tau_A.

On the legal/standard intersection c_iA is a unit, including the permitted branch points. The actual cohomology inclusion/projection in the e_i-power frames are

    I_iA^legal=I_i(v_A) diag(1,c_iA^-1),
    P_iA^legal=diag(1,c_iA)P_i(v_A).

These are supplied by the normalized root/frame bridge, not inferred from deck parity. They are matrices of genuine regular quotient maps on the owner open, extended meromorphically as needed.

The g_ij in the residual is the scalar matrix of a transition between two such FIXED physical quotient frames. Changing a standard representation chart does not replace those physical frames. Therefore g, its adjugate and its invariant derivatives are the same meromorphic scalar matrices after coordinate substitution. The old-connection comparison in the raw-block/scalar proofs likewise shows that B and q, and hence s_raw, are the same meromorphic functions: both split and old connection receive the same common ambient derivative term. Differentiation is by the same global V_d, not by a reset finite-chart derivation. Thus every ingredient of R, and R itself, agrees across standard representations in its fixed first-owner frame.

Every 2-by-2 rational matrix in that fixed frame gives a meromorphic endomorphism of the cohomology bundle. This is a local cochain component on its owner intersection; it is not an assertion that different Čech tuples glue to one global section or satisfy a cocycle equation. The product-root bridge gives the required frame, so the assignment is geometric and unambiguous.

Now the literal j has the following actual standard-chart coefficient in End^0(K):

    J0,A=I_i(v_A) diag(1,c_iA^-1) R^t
                         diag(1,c_iA) P_i(v_A).             (1)

At the rational reference chart c_i,ref=nu_i^2. Conjugation by diag(1,nu_i^-2) is the same as conjugation by D_i=nu_i diag(1,nu_i^-2), since the common scalar cancels. Formula (1) is consequently exactly the source expression I_i D_i R^t D_i^-1 P_i, not a new operator.

On A to B put lambda=tau_B/tau_A. Homogeneous column/row degrees give

    I_B=I_A diag(1,lambda),
    P_B=diag(1,lambda^-1)P_A, c_iB=lambda c_iA.

Substituting in (1) proves J0,B=J0,A. This is the degree-zero strict End chart law on every overlap, without adjoining sqrt(tau), dropping an ambient factor, or claiming a rational frame is regular where it is not.

The original-resolution homotopies are actual degree-minus-one maps. The legal-free-homotopy theorem proves, using the same integral root bridge,

    h_B=lambda^-1 h_A, E_B=E_A.

If F_B=lambda^r F_A, both literal homotopy branches obey the law lambda^(r-1). Since lambda depends on the representation charts, not on the selected owner, it commutes with the cochain restrictions. Induction now proves

    Js,B=lambda^-s Js,A.                                    (2)

This identifies each Js with the actual strict degree-minus-s ambient sheaf, on every standard chart and overlap. It does not use differentiated homotopies or derivative-anomaly cancellation.

For equivariance, use the natural deck linearization of the divisor line N=O(Theta_prod), with invariant rational section e_ref=1. The two columns of the physical quotient frame have the same character m_i, because their common-reference coefficients are I_i D_i. Thus conjugation in its endomorphism bundle cancels that frame character; the matrix character 15 of R is exactly its intrinsic endomorphism character. Equivalently formula (1) uses invariant primitives and invariant c, so J0,A has character 15 directly in the strict End frame ell_A^0. Each h_A and E_A is invariant and (2)'s line frames descend from Y. The strict equivariant character assertions of section 4 are therefore valid in these actual bundles, not merely for unrelated finite scalar formulas.

## 6. Branch-safe coefficient extraction and the line

On a standard base chart let R_A be its polynomial coordinate ring and let z_r=y_r or u_r according to its finite or infinity factor. Its pulled-back curve algebra is the free rank-16 module

    S_A=R_A[z_0,z_1,z_2,z_3]/(z_r^2-f_r),
    S_A=direct sum_(S subset {0,1,2,3}) R_A z_S.

Here f_r=x_r^3-x_r or t_r-t_r^3, and z_S is the square-free product. Freeness follows from the monic quadratics even at every branch divisor. Localizing in invariant base equations preserves the direct sum. Every rational function has such an expression over Frac(R_A): the iterated quadratic extension has the displayed 16 characters, or equivalently localization of the free finite-flat algebra gives its generic algebra. There is no need to invert a branch coordinate as a regular function.

Each strict degree-r block has the factor N^(2r)=q*O_Y(r,r,r,r). By sections 4-5, a full-character Js coefficient in its local line frame ell_A^r is uniquely z_all b_A, with r=-s. Extract b_A by the free-module coefficient projection. If an invariant clearing factor C_A makes C_A Js,A regular, the same projection makes C_A b_A regular. This is a base-linear direct-summand argument, not division by the possibly vanishing product z_all.

On finite-to-infinity changes z_A=tau_A^2 z_ref and ell_A^r=tau_A^-r ell_ref^r. Equality of the already identified meromorphic section gives

    b_A=tau_A^(r-2)b_ref.

For an arbitrary A-to-B overlap this is b_B=lambda^(r-2)b_A. Hence the coefficient line is O_Y(r-2,r-2,r-2,r-2), and substituting r=-s proves the announced four lines. Coefficientwise invariant clearing bounds from the other packets may now be applied to these actual lines. This theorem supplies membership; it neither derives those bounds merely from parity nor grants regularity to an uncleared expression.

## 7. Static verification and remaining frontier

The checker authenticates all inert input/dependency bytes, binds complete selected source ASTs and the exact raw override, and inspects the seven/three/two/eight slots and homotopy predicates. Its computations are limited to integer character masks, block degrees, formal frame exponents and local overlap metadata. It verifies all 4096 legal-mask triples, all 256 standard-chart pairs and the four stages. Active negative controls reject omitted normalization, wrong pair, missing derivative flip, wrong physical leaf character, an odd homotopy, wrong block degree, a missing c chart multiplier, omitted odd-basis transition and branch-unit division.

No original source is imported. These finite checks bind conventions and detect mutations; sections 2-6 supply the mathematical proof. Normal and optimized runs are recorded. This packet closes complete R/Js rational ambient character membership for the frozen raw denotation. Full-source closure, cohomological/obstruction attribution, terminal scalar selectors, arbitrary implementation arithmetic remain separate.
