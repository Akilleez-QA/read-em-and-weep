# Audit of the explicit mixed source and a tracefree groupoid reduction

## Historical source audit (Sections 1–3) and distinct lemma (Section 4)

Sections 1–3 audit previously public formulas. They are not additional new claims. Section 4 is the distinct scalar-removal solution-groupoid result.

## Verdict and sources

PASS, within the previously stipulated algebraic-sheaf, marked external-product, and compact Ext-vanishing premises. The comment supplies a useful expanded coordinate formula, not a new obstruction comparison or a vanishing theorem.

Audited source: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716 (2026-10-19 15:38:36 UTC), fetched directly. PR1 remained open at head 2531056eae05fdf31e8fb4ca3affc5907073ad73, updated at that time. Also read the pinned research/hm/second-order-algebroid.md at c8aec970fd65a105f39f4e8aeb8a17f0f0053f89, especially §§4–5, and source comments6260505511 and6260553958 directly.

Local comparisons: actual-joint-deformation-model/PROOF.md; corrected-mixed-secondary-class/PROOF.md; mixed-ambient-rigidity/PROOF.md; mixed-obstruction-transport/PROOF.md; pure-downstairs-identification/PAIR_GAUGE_SOURCE_AUDIT_6270678828.md; pure-deck-structure/INTEGRATION.md.

## 1. Complete source R

Work on an affine acyclic refinement, retaining coefficient-line transitions implicitly. Let z,h,m denote the two pure and mixed weights. Write the actual external-product operations as

    multiplication = μ0 + μz + μh + M,
    Fij = id + zij + hij + wij,
    Aijk = 1 + bijk + cijk + bijk cijk,
    Gij = gij + uij + vij.

Here M and w are the actual external product operations, not arbitrary representatives of a cohomology class. Expand the first factor:

    Fij(Gjk) = gjk + Ujk + Vjk + Wjk,
    Ujk = ujk + zij(gjk),
    Vjk = vjk + hij(gjk),
    Wjk = zij(vjk) + hij(ujk) + wij(gjk).

The mixed component of Fij(Gjk) ⋆ Gij is exactly

    Wjk gij + Ujk vij + Vjk uij
    + μz(gjk,vij) + μz(Vjk,gij)
    + μh(gjk,uij) + μh(Ujk,gij) + M(gjk,gij).

No matrix factors have been exchanged. The mixed component of Aijk ⋆ Gik is

    bijk vik + cijk uik + bijk cijk gik.

Potential terms μz(cijk,gik) and μh(bijk,gik) vanish by complementary-factor support. This is essential: scalarness alone would not justify deletion. Opposite-factor coefficient lines have their canonical relative flat differentiation inherited from the external product; arbitrary coefficient actions are not being allowed.

Subtracting gives exactly the comment's R, term for term. Its b c is the product of two entries of the same triple unit on Uijk. It is not the Čech cup of two degree-two cochains, which would instead have Čech degree four. No mixed factorial appears.

This is precisely the specialization of the finite convolution (1) in actual-joint-deformation-model §3 with its nonzero unary maps retained. That proof's §5A separately treats an F=id source presentation; one must not silently use that ten-term presentation downstairs where F has nonzero pure unary components.

With C=gik inverse R and mixed coefficient Gm=gij xij, the extra residual is gik δx. Hence δx=−C has the stated sign. The ambient pentagon and pure module equations give δC=0 by the already proved quadruple-defect calculation. The normalized ratio is the same complete gerbe cocycle, not merely a detector of its vanishing.

## 2. Gauge Q and the sign

The source uses

    G'ij=Fij(Hj) ⋆ Gij ⋆ Hi inverse,
    Hi=1+ai+di.

This is the inverse-coordinate convention to formula (G) in the delivered joint model. Both are legitimate; the same letter H must not be identified across them without inversion.

Because products of three positive weights vanish,

    Hi inverse=1−ai−di+ai di+di ai.

The first multiplication Fij(Hj) ⋆ Gij has pure parts uij+aj gij and vij+dj gij, and mixed part

    [zij(dj)+hij(aj)]gij + aj vij + dj uij
    + μz(dj,gij)+μh(aj,gij).

Multiplication by Hi inverse adds exactly

    gij(ai di+di ai)
    −(uij+aj gij)di −(vij+dj gij)ai
    −μz(gij,di)−μh(gij,ai).

This reproduces every term and order in Q. Pure transformed transitions are u'=u+aj g−g ai and v'=v+dj g−g di.

For completeness, if D=Fij(Gjk)⋆Gij−Aijk⋆Gik, the transformed defect is

    D'=Aijk⋆Fik(Hk)⋆Aijk inverse⋆D⋆Hi inverse.

D has mixed weight, so all positive factors annihilate it and D'=D. Thus keeping Q preserves the normalized top defect. Removing Q subtracts δq, where qij=gij inverse Qij. Consequently

    C(u',v')=C(u,v)−δq.

The apparent opposite gauge orientation to the earlier proof creates no sign error.

## 3. Choice independence and exact limits

The relevant inputs are COMPACT H¹(Y,End(E)⊗L)=H¹(Y,End(E)⊗M)=0 for Y=P²×P². Source6260553958 derives these from the specifically identified weight-two deck summands via finite pushdown. They are not fiberwise vanishing assertions or statements only on the stable open. H⁰ vanishing there further gives unique reduction-preserving comparison of existing pure lifts.

Therefore every two genuine marked pure lifts in the same fixed pure ambient are related by such pure gauges after local framing. Combining their two gauges into H=1+a+d yields the identity above. The class is independent of these pure choices. Arbitrary cochains not solving the pure equations, changes of coefficient-action marking, unmarked classical automorphisms, or unrelated frozen jets are not covered.

Künneth gives H^i(Y,J)=0 for i=0,1,2,3 and H⁴(Y,J)=C, J=O(−3,−3). Since trace commutes with δ, tr C is closed and admits δk=tr C. Rank E=2 gives

    C−(δk/2)Id = C−(tr C/2)Id = tf(C).

Thus the tracefree representative itself is the canonical cochain projection tf(C); the choice of k certifies its equality of cohomology class with C. The scalar primitive is not a remaining ambient tuning parameter. Nothing supplies a primitive of tf(C).

The full marked ambient and boundary comparisons already established in the cited local proofs remain established under their premises. The source's refusal to identify a frozen raw jet does not reopen those class-level comparisons.

## 4. Complementary bounded lemma: scalar removal is an equivalence of solution groupoids

This strengthens the tracefree representative statement to objects and arrows, without evaluating the source. It is not another assertion of the already known H¹ torsor.

Set F=End(E)⊗J and F0=End0(E)⊗J. For any closed C in Čech²(F), let Sol(C) have objects x in Čech¹(F) satisfying δx=−C. An arrow labeled t in Čech⁰(F) sends x to x+δt; composition adds labels. This convention matches the source's inverse frame convention for mixed gauges.

Projection tf gives a canonical functor

    Sol(C) → Sol(tf C),
    x ↦ tf x,   t ↦ tf t,

where the target uses F0. This functor is an equivalence. More precisely, the trace splitting F=F0⊕J Id gives a literal product decomposition

    Sol(C) = Sol(tf C) × S(tr C/2),

where S(c) has scalar objects s with δs=−c and arrows s→s+δa.

Proof: H²(J)=0 makes S(c) nonempty. If s,s' are objects, their difference is a closed one-cochain. H¹(J)=0 provides a with δa=s'−s. Any two such a differ by a global section of J, and H⁰(J)=0 makes them equal. Thus there is exactly one arrow between any two scalar objects: S(c) is contractible. Projection from the displayed product is fully faithful and essentially surjective, including when the tracefree solution groupoid is empty.

A primitive δk=tr C supplies an inverse on objects by y↦y−(k/2)Id. Changing k changes this inverse by a UNIQUE natural scalar gauge isomorphism. It does not make a literal scalar primitive canonical. The projection functor itself requires no primitive choice.

The construction commutes strictly with restriction to refinements and with coefficient-marked classical conjugation: trace and identity commute with both. If a pure gauge changes C to C−δq as above, translation x↦x+q transports solutions; its tracefree counterpart is y↦y+tf q. The projection square commutes literally. Hence this scalar elimination cannot manufacture a choice-dependent mixed class or an additional scalar modulus during refinement or pure-frame changes.

The uniqueness of arrows in the scalar factor uses H⁰(J), connectedness uses H¹(J), and nonemptiness uses H²(J); H² alone proves only the representative statement. This is the exact additional content of the lemma. No vanishing of H¹(F0), H²(F0), or the actual obstruction is inferred.

## Novelty and stopping boundary

New explicit information in the comment is the expanded external-product R with unary terms and a closed-form Q witnessing pure-gauge covariance. The underlying complete curvature, sign, gerbe identification, H¹ torsor, and class independence were already established in the delivered bounded joint model and secondary/transport proofs. The lemma above adds a small precise solution-groupoid refinement of scalar removal; it does not resolve the central unknown.

The lemma alone decides neither the tracefree obstruction nor existence of a mixed carrier. Historical counts of unresolved coordinates in the audited source are not claims about the current frontier.
