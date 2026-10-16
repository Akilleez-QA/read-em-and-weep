# Independent audit: a finite-jet dual contraction

## Verdict

The proposed jet construction is a valid CONDITIONAL dual-fill certificate. It is not yet an instantiated compression of the authenticated detector. Exact factorization of the actual detector row and sufficient descent of boundary annihilation are indispensable. The existing denominator/pole envelope proves neither. A checked small counterexample below separates both obligations even when the original owned-denominator complex has H1=0.

## Local frames and chain maps

Choose a point p and a standard affine chart containing p. Trivialize F and every L_v separately on that chart, and trivialize each summand F tensor product_(v in I)L_v by the PRODUCT of these frames. Although the degrees vary with I, these product frames make the numerator differential literally signed multiplication by the local polynomial d_v. Independent frames without their transition factors do not have this property.

Choose one finite local algebra J=O_(X,p)/a, for an m_p-primary ideal a. Let Wq be the direct sum of one copy of J for every (q+1)-vertex tuple, and let q_q send a global numerator to its local jet in that summand. Give W the signed multiplication differential Dbar by the local jets of d_v. Then

    q_(q+1) D_q = Dbar_q q_q

holds in every degree, including augmentation if it is used. The same quotient ideal must be used throughout, or a separate containment proof must show multiplication carries each discarded source ideal into its target discarded ideal. Clipping each cochain degree independently is not automatically compatible.

For rectangular jets J=k[t_1,...,t_4]/(t_i^(r_i+1)), standard chart monomials show that q0 is onto precisely when each vertex numerator degree m_(v,i) is at least r_i in every coordinate. This statement is about surjectivity onto the FULL W0, independently in each vertex component. Translation to a different point in that chart is triangular and preserves the degree condition. General local trivializations or nonrectangular ideals require their own jet-generation proof.

## Descent and adjoint signs

Require an exact identity e=e_J q1 on the ENTIRE full numerator V1. Equivalently e annihilates ker(q1); merely fitting within a rational pole envelope does not imply this. With e D0=0 and q0 onto,

    e_J Dbar0 q0 = e D0 = 0

implies e_J Dbar0=0. Onto q0 is sufficient; the weaker direct assertion e_J Dbar0=0 would also suffice if checked independently. Onto q1 is not required for the theorem, although a compiler must explicitly choose and certify e_J when extensions are nonunique.

The actual cover supplies a vertex w with d_w(p) nonzero. Write its jet as c(1+u), where c is nonzero and u is nilpotent. Its exact inverse is c^(-1) sum_(j=0)^(N-1)(-u)^j for any certified u^N=0. For rectangular jets N=1+sum_i r_i suffices. Coefficients may be symbolic only if c is certified invertible in their coefficient ring, or that ring is explicitly localized.

Define h_q:Wq -> W(q-1) by inserting w and dividing by its unit jet: on output tuple I not containing w, take the coefficient of input tuple sorted(I union {w}) with sign (-1)^(position of w), divided by d_w; on tuples already containing w, use zero. The wedge/contraction identity is

    Dbar_(q-1) h_q + h_(q+1) Dbar_q = id_Wq.

In degree one, define eta_J=e_J h2 and eta=eta_J q2. Then

    eta D1 = e_J h2 Dbar1 q1
            = e_J (id-Dbar0 h1) q1 = e.

For column covectors, eta_J=h2^t e_J and eta=q2^t eta_J. There is no extra negative sign. All signs are inherited from the increasing tuple convention above.

## H0, H1, and owner scope

The AUGMENTED jet Koszul complex J -> W0 -> W1 -> ... is contractible. The nonaugmented jet complex has H0=J and positive cohomology zero. It therefore need not preserve global H0 or H2: the full owned-denominator model here has H0=0 and H2=k. The maps q are chain maps, not asserted quasi-isomorphisms. Only the certified factorization and descent identities justify pulling this particular dual filling back.

The division by d_w occurs solely in the finite local jet algebra. It must not be reinterpreted as a global rational scalar primitive or as permission to add an apex denominator to an absent owner. q2 evaluates numerators with their original owner tuples; eta is a linear functional on the original V2. This dual-only use introduces no new rational cochain or pole transfer. Any implementation that converts h into a global primal contraction needs a separate ownership/domain proof and is outside this certificate.

## Checked obstruction: both hypotheses matter

The independent test reuses the abstract P1xP1 example in test_owned_denominator_complex.py: F=O(-2,-2), four denominators 1,y²,x²,x²y² in a standard chart, and full global numerator degrees (0,0), (2,2), (4,4), (6,6) in degrees 0,1,2,3. Its H1 is zero.

Take eta to select numerator x³ on triple (0,1,2). Then e=D1^t eta selects exactly numerator x on edge (0,1), and eD0=0.

1. For J=k[x,y]/(x²,y), e factors exactly through q1. Chain compatibility holds. But q0 has rank4 into an 8-dimensional W0. Since d0=1 and all other denominator jets vanish, e_J Dbar0 is nonzero on vertex1 numerator x. Global boundary annihilation therefore does NOT descend.
2. For constant jets J=k, q0 IS onto. But the edge (0,1) numerator x lies in ker(q1) and has e-value1. Exact factorization therefore fails.

Both checks pass in test_jet_dual_independent.py. This is a counterexample to deducing a usable jet certificate solely from finite pole bounds, global exactness, and a unit denominator. It is not a counterexample to the conditional theorem.

## Compression obligation remains open

At a standard point, arbitrary full numerator rows can always be recovered by jets through their full multidegrees. Those orders can exceed the degree-zero numerator jet-generation ceiling: edge numerator degrees add TWO vertex denominator degrees, whereas degree-zero spaces add only ONE. Thus choosing sufficiently many jets to guarantee arbitrary-e factorization does not automatically preserve q0 surjectivity. Choosing smaller jets makes surjectivity easier but demands a genuinely special factorization of the authenticated e. Its derivative/coefficient construction and finite Laurent envelope alone are not that factorization.

To claim an actual compressed certificate, provide the point and frames, quotient ideal, all-degree chain compatibility, q0 surjectivity OR direct e_J Dbar0=0, exact actual-e factorization, and the adjoint residual. Separately give a representation and operation/storage schedule. No physical source evaluation was performed in this audit.

## Review of the completed proposal

Independently read jet-quotient-direct-dual-certificate.md and reran test_jet_quotient_dual_certificate.py. Its general tensor quotient, unit-ideal contraction, exact binomial coefficient factorization criterion, and conditional residual agree with this audit. The abstract example reports full dimensions (16,150,256), quotient dimensions (16,24,16), and exact intertwining/contraction/lifted residual. The 134-versus-12 closed-row dimension distinction accurately prevents treating its successful example as a universal compression theorem. No correction to the mathematical conditional claim was required.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
