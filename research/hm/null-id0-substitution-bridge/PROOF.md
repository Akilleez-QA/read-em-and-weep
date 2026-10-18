# Bounded integrated ID0 denotation and terminal-interface theorem

## Result

The checked pieces compose to a **conditional raw-scalar denotation theorem**, not yet a whole-ID0 correctness theorem. In the primitive portion, the only remaining model-identity family is A: B and C have structural proofs on the same pinned model. Accepting A's historical computation receipt, exact field/derivation semantics, and legal localization closes decoder → contractions → moving-frame blocks → raw scalar. It does not close raw scalar → complete residual → HPL → outer transport → terminal input.

A new source-bound substitution theorem below closes propagation of an equal raw-scalar denotation through the frozen Source.E/residual, HPL recurrence, selector and entire weighted outer sum, with all other leaves and contexts held fixed. This is a concrete congruence theorem for the actual pinned implementation; it does not assert that the fixed context already has the intended global geometric denotation.

There is also an exact, strictly weaker interface condition than equality of the entire transported scalar: once both complete inputs are authenticated Laurent representatives in the same frame, their ID0 terminals agree if and only if their difference belongs to the kernel of the three-coefficient functional below. This gives a precise replacement target for a future downstream proof without pretending that upstream scalar correctness implies it.

All claims concern the supplied local public artifacts and their source pins. `cb452046675d5c74c403d781898f679f429ffae4` is the parent-supplied current public head label; this note does not independently bind that remote tree. Implementation theorems concern raw-engine/source pin e93cf712f9da4926a8450cc870ed45a7bfc379ab, model/formula pin 10810ee877fdaf291399198ad60d7dd0c316a42d and historical theorem/checker pin 08b73637d4136f91606aad332c46cafd064417f8. Public packaging at a later head is not a new production implementation.

## 1. Common mathematical interpretation

Let K be an exact commutative characteristic-zero field carrying the four curve derivations V_i and the required localized rational functions. Require all invoked inverses to exist; all arrays to have their stated rectangular shapes; directions/masks to be legal; and field, rational, matrix and derivative operations to denote their mathematical counterparts. In particular the curve relations are y_i^2=x_i^3-x_i, V_i x_i=y_i, V_i y_i=(3x_i^2-1)/2. This is a semantic premise, not proved by 42 finite arithmetic controls.

The decoder sends a literal record t to sum_(e,c) c product_i v_(i+1)^e_i and a stored matrix numerator N with denominator d to N/d. Its elementary-symmetric loop sets v0=1 and v_j=e_j(x1,...,x4). Schema checks and algebraic independence establish nonzero *formal* denominator polynomials, not pointwise invertibility on every chart or legal-owner domain.

The same model bytes appear in primitive identity and contraction packages (SHA256 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926). Both contraction and frame/scalar packages bind the same raw_engine, source-formulas and first-order-source bytes. This makes the middle arrows genuinely composable rather than similarly named theorems about unrelated inputs.

## 2. Primitive-to-scalar composition

For each of six carriers assume

    A: gamma H0 + I P + H1 delta = Id15.

The historical receipt reports 1350 E_identity entry checks. Its inert source tests that expression, and its homogeneous-to-finite specialization at v0=1 gives this finite A on the stated localizations **if the computation report is accepted**. Neither its execution, arithmetic correctness, nor its truth was freshly established. It is not an independently reproduced proof or a signature.

The following two model identities have a different evidence class:

    B: H1 eta = 0.
    C: ev delta = 0.

B follows from the literal empty selected numerator columns and eta's pivot-selector definition. C follows universally from the literal skew-column form: (v_r,v_s) paired against (epsilon v_s,-epsilon v_r) gives zero by commutativity. The C static proof checks 20 paired and 10 zero block columns, shared across all six carriers, in finite and homogeneous interpretations. No actual polynomial product is required. Thus the older contraction report's unresolved C obligation has been discharged by the newer structural C report; its historical wording must not be copied as today's gap.

The literal pivot split gives LW=Id8, ev W=0, L eta=0, ev eta=Id2, WL+eta ev=Id10. Put U0=(gamma,I,H1W), Q0=(H0;P;L delta), U1=(W,eta), Q1=(L;ev). A and B give U0Q0=Id15; square-matrix inverse theory over K gives Q0U0=Id15. B yields H1=H1WL; C yields delta=WLdelta. Reading Q0U0's blocks then gives every required contraction, delta gamma=0 and delta I=0, including delta H1=WL. This imports no separate inverse or rank oracle.

Set S0=diag(nu^-2 Id5,1,nu^-2,nu^2 Id8), S1=diag(Id8,nu^2 Id2), with nu invertible. The frame proof establishes the frozen lowering

    B_l(V)= -V(U_l S_l) S_l^-1 Q_l - k_l alpha(V) Id,
    ranks (5,15,10,2), k=(-1,1,3,5),

with identity extreme frames. The two cohomology columns have distinct weights. The formula uses alpha, not rho=V(nu)/nu. Constant normalization cancels by Leibniz; repeated directions still require derivatives of y_i.

For signs epsilon=(-1,1,-1,1), Ai=B_i,a, Bi=B_i,b, Aj=B_j,a, Bj=B_j,b, the scalar proof establishes

    s = sum_l epsilon_l/4 [tr(Ai Bj)-tr(Bi Aj)]
      + sum_l epsilon_l k_l/8 [qa tr(Bi)+qa tr(Bj)-qb tr(Ai)-qb tr(Aj)]
      - 15 qa qb/8.

The concrete caller supplies exactly four square blocks and both endpoints; general malformed tuples are outside this theorem. For distinct a,b, s_phys=y_a y_b s_stripped. Complementary derivatives give the further y_c and y_d factors without factorials. Static inspection establishes the complementary directions for the scalar E calls only. This closes the primitive-to-scalar denotation; section 3 propagates equality through the unchanged downstream context. Neither result independently audits all other physical leaves or identifies the whole R with its intended geometric class.

## 3. Newly closed arrow: raw-scalar substitution through the frozen full pipeline

This result reads the exact compiler.py SHA256 28e95b87adefaba0d4ec886a7ab272f252f376bbb1fc26e0a387bc05f896a386, pinned by the frame/scalar package; raw_engine and inert program are already pinned above. The lift_schema.py SHA256 3de33f88790e46bb62d4c400143ef62dea8b0b15d51bd18a4fb70689e3261f31 is bound by the inert patch's frozen-source list. These files are read as text only.

**Substitution theorem.** Fix a legal finite owner/index domain and the exact pinned downstream context: g, q, all other source leaves, lift I/P/H0/H1/eta, schema, owner order/parity, outer weights, staircase orientations, frame conventions and deck stripping. Require exact matrix/field/derivation semantics, valid shapes/inverses, fresh/equivalent caches, and compare successful mathematical results. Replace every scalar leaf s(p,i,j) by s'(p,i,j), with equality as elements of the differential field for every call in this domain. Then the entire preterminal stripped rational is unchanged. Thus its certified ID0 value, if defined, is unchanged. This is equality in the differential field, not agreement at finitely many sampled points or agreement of zero-order jets.

Here is the sharper error-propagation identity proved by source inspection. Put epsilon=s'-s. For a triple (i,j,k), p=(a,b), complementary solver pair q, write

    L_a = g_ij^-1 V_a(g_ij),
    T_a = g_ij^-1 g_jk^-1 V_a(g_jk) g_ij,

and similarly for b. The exact Source.E return expression implies

    Delta E(p,q;i,j,k) = (1/2) [
        V_a(epsilon(q,j,k)) L_b
      - V_b(epsilon(q,j,k)) L_a
      + V_b(epsilon(q,i,j)) T_a
      - V_a(epsilon(q,i,j)) T_b ].

The matrix multiplication order is exactly the displayed order, and the signs are +,-,+,-. RawSource inherits Source and overrides only T, wrapping s_raw as a 1x1 matrix. Static inspection finds the only self.T calls in Source are the two endpoint calls in E. Source.residual uses E((0,1),(2,3)) and E((2,3),(0,1)); its seven kinetic terms, three negative gerbe terms, tracefree baseline and both Fk terms contain no T. Hence exactly

    Delta R(t) = Delta E((0,1),(2,3);t)
               + Delta E((2,3),(0,1);t).

This proves both endpoint derivatives propagate and no unseen T-dependence is discarded. It does not replace the actual baseline or Fk terms by zero: they cancel only in this difference because they are identical on both sides. Mat.inverse is an adjugate without determinant division; interpreting it as g^-1 still requires the determinant-one premise. Even without that geometric premise, its unchanged literal value suffices for the congruence result.

The fixed Lift methods yield the exact error recurrence, with all owner references as in the code:

    Delta J0(t)_(1,1) = I_(t0) (Delta R(t))^transpose P_(t0),
    (delta Delta J_(s-1))(t) = sum_j (-1)^j Delta J_(s-1)(t with vertex j deleted),
    Delta J_s(t) = sigma_s H_(1-s,t0) (delta Delta J_(s-1))(t),
    (sigma_1,sigma_2,sigma_3)=(1,-1,1).

The block homotopy is linear because it adds H_v F_(u,v) into block (u,v-1) when v>0, and (-1)^r (IP) F_(u,1) H_(u+1) into (u+1,1) when u<3. It never multiplies two residual-dependent blocks. The first owner is chosen in each recursive tuple before subsequent deletions; no additional row-End conjugation is inserted. Cache keys and supports are identical in the two semantic runs; finite-stage induction proves this recurrence and congruence for stages 0 through 3. It does not prove the separate closure equations for J3.

Define ell(J2)=J2_(3,1)[5,0]+J2_(2,0)[1,3]+J2_(2,0)[4,2]. The exact weighted_assignment and complete preterminal loop imply the further identity

    Delta F = pi15 sum_stair sum_owners orientation(stair) parity(owners)
              [product_(original owners o) outer_weight(o)]
              ell(Delta J2(canonical owners)).

Here pi15 is coefficient projection onto deck mask15 in the same exact field representation. It is additive and Q-linear; all fixed outer factors are multiplied before projection. No assertion that these factors commute with pi15 is used. Original unsorted owners supply weights; canonical owners supply the lift; the entire sum precedes mask extraction. A parity-zero branch contributes zero on both sides. This is a literal denotational identity of the frozen context, not a new domain or transport theorem.

Combining the displayed identities gives an explicit linear differential response operator epsilon -> Delta F with fixed coefficients. In particular epsilon=0 implies Delta F=0, since V(0)=0, and then the exact terminal theorem applies. This **closes the implementation substitution arrow** from the newly proved raw scalar through the actual full residual/HPL/outer computation. It does not identify that computation with the intended geometric class unless its other leaves, domain, transport and global comparison are authenticated. In particular replacing raw s by an N14 solver would require equality or an adequate global comparison theorem; raw-scalar correctness by itself does not assert raw s=N14 T.

## 4. Explicit remaining geometric interface

Name the mathematical complete residual R*, its accepted HPL lift J*, and the complete transported/weighted, original-frame, deck-stripped scalar F*. Name the inert candidate's corresponding denotations R_c, J_c and F_c. These are denotational variables, not evaluated physical objects.

To conclude F_c=F*, it suffices to establish all of the following commuting interfaces (or a proved weaker terminal-kernel condition from section 5):

1. **Whole residual interface:** R_c denotes the full R*, including seven kinetic terms, three negative gerbe terms, tracefree baseline, both Fk terms and both E terms, with the correct transitions, old connections, ordering, derivatives and global raw/N14 comparison. The proven raw s is only a leaf used in E; its equality does not establish the other leaves or enclosing operations.
2. **Lift interface:** original-resolution inclusions, homotopies, ordered Cech faces, degrees and signs (1,1,-1,1) give J_c=J*. J2 supplies the selector but J3 and delta J3=0 remain required for the asserted cocycle/class interpretation. The selector is X13[5][0]+X02[1][3]+X02[4][2].
3. **Outer/domain interface:** full owner equality, occurrence distinctions, stable sort parity, unsorted-owner weights, every assignment and staircase orientation are preserved; common carrier/legal/standard bounds 54/29/5251 and owned suffix divisors support whole-coefficient regular extension. The displayed degree formula alone does not prove clearing. Authenticate original-frame transport, internal-degree -2 tau^-4 conversion (finite tau=1), and one full deck-product removal via mask15. Mask15 is not the S4 sign projector. Authenticate the corrected common-frame alternating theorem and retained-sector identification for this actual global class.

Seed30→0 injective relabeling and the candidate's identical preterminal AST reduce avoidable reimplementation differences. They do not discharge the imported semantic interfaces or all transitive dependencies. A cache/source call must not secretly depend on seed/history, and guards/admission are not a proof of source semantics. The existing packages explicitly retain these conditions.

These three interfaces are a bounded logical factorization, not a claim that three scalar identities are mathematically independent or the unique minimal geometric proof. At the terminal boundary they can be weakened exactly as follows.

## 5. Exact terminal-interface theorem and shortcut countermodel

Let S=Q[x1^±1,...,x4^±1]. Put

    e1=(-3,-3,-1,-1), e2=(-2,-2,-2,-2), e3=(-1,-1,-3,-3),
    lambda(F)=[x^e1]F+2[x^e2]F+[x^e3]F.

Suppose a single immutable complete candidate rational F_c=A/B is certified Laurent: B=x^d C with no coordinate variable dividing C, and exact full division certifies A=CQ. Suppose F* is the authenticated geometric scalar in the same coordinates/frame and belongs to S. Under correct certificate/terminal arithmetic and successful execution,

    candidate mathematical terminal = lambda(F_c)
      = Q[d+e1]+2 Q[d+e2]+Q[d+e3].

Therefore

    candidate terminal = intended ID0
      iff lambda(F_c-F*)=0,

provided the retained pairing theorem identifies intended ID0 with lambda(F*). Proof: exact division gives F_c=x^-d Q; Laurent coefficient extraction is Q-linear, so subtract the two terminal expressions. No linearity assumption about source construction or HPL is needed for this final equivalence.

Consequently equality of full scalars is sufficient, but unnecessary; even equality of the three target coefficients individually is stronger than necessary. The target-space kernel is precisely {(a,b,c):a+2b+c=0}, with basis (2,-1,0), (1,0,-1). For example the nonzero formal Laurent discrepancy 2x^e1-x^e2 is invisible to this one terminal. An error x^e1 changes it by 1. All off-target monomials are also invisible to lambda. This is the exact weakest equality condition at this authenticated Laurent interface, not an admission shortcut: proving or checking only three apparent zeros before Laurent certification is invalid, and one invisible error says nothing about other detectors or whole cohomology.

**Countermodel to the implied raw-scalar shortcut.** Consider an abstract interface with fixed raw-scalar component s=0 and an unspecified downstream scalar contribution z. Let completion one output F=0; completion two output F=x^e1. Both completions satisfy identical information about s, both outputs are Laurent and accept the same frame-label strings, and both can satisfy a correct shared-division API. Their terminals are 0 and 1. This is a formal information-loss countermodel, not a claim that either completion is realizable by the pinned physical model. It proves that any argument using only raw-scalar equality, Laurentness and labels is missing a downstream hypothesis. The pinned whole-source closure would rule out arbitrary z; it must actually be proved rather than inferred from the leaf theorem.

## 6. Certificate controls, operational semantics and release

The retained certificate theorem proves the universal algebraic terminal above. The candidate proposes one exact division followed by weighted reads in the same Execution, identity-bound rational/context, and poison checks. Its labels are declarations, not provenance certificates. The 42/42 extracted invented-input controls support these retained arithmetic paths on the pinned candidate; they are not a proof of full field, Element.V, physical jets, production importability, source correctness, or resource bounds. This integration did not replay that extraction or import its candidate.

The actual candidate entry starts with an unconditional RuntimeError before reading arguments. Under ordinary unchanged Python semantics its current operational denotation is **refusal**, not lambda(F_c). The above expression is the unreachable specification's successful mathematical value under stated premises; there is no claim of a successful execution today. Applying/activating anything would need separate authorization and reviewed source changes, authenticated transitive dependency closure, new source-bound admission, and cost/peak-lifetime bounds covering all live numerators, denominators, quotient/remainder, native scratch, lookups and final output. Old receipts cannot be silently relabeled.

Thus D0 remains unknown. Even an authenticated D0=0 would not prove vanishing; an authenticated nonzero D0 proves nonvanishing only with the retained/global identification premises.

## 7. Reproduction boundary

Public-bundle clarification: the check_static.py shipped beside this copy is the self-contained narrow section-3 checker described in README.md. It verifies four bundled inert source texts, method patterns and formal response controls; it does not rerun the 88-input integration checks described in the historical paragraph below. Primitive/frame/terminal package results remain cited premises. The original integrated proof and full checker remain unchanged.

The following describes the original full integration checker, not this public bundle's narrower checker.

`python check_static.py` and `python -O check_static.py` verify pinned local input bytes, cross-package source identities, inert candidate AST terminal/refusal structure and the tiny formal coefficient-kernel controls. They perform no polynomial products, no physical source/model/owner/jet construction, no production imports, no candidate compilation/execution, no patch application and no external writes. PASS does not mechanically prove the prose mathematics or discharge its premises. The input digest manifest preserves the exact review snapshot, not an independent trust anchor.
