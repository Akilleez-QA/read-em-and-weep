# Independent review: explicit central-scalar contraction

## Verdict and scope

**ACCEPTED at the stated conditional-comparison scope.** The one-factor Laurent split, signed four-factor homotopy, full mixed-defect character ledger, and comparison-transport formulas are correct. This constructs an explicit operator on the regular standard tensor Čech complex. Applied to an admitted full comparison of the actual scalar cocycle, it gives its compared primitive. It does **not** supply that actual comparison, a primitive on the original source cover, or evaluated coefficients of the actual primitive.

The exact reviewed producer proof is preserved as `reviewed-PROOF.md`; its SHA-256 is recorded in `reviewed-version.json`. The independent checker is `check_independent.py`, with byte-identical normal and optimized reports. No actual source, model, matrix, polynomial, jet or residual was evaluated. No source module was imported.

The prior abstract scalar H²-vanishing and identity R=tf(M)+dW already exist. The increment here is the complete operator with signs and domain, a full-M character argument using its actual first lifts, and precise comparison formulas with their missing inputs exposed. It is not a new proof of vanishing of the remaining trace-free mixed class.

## 1. The actual scalar input: full M, not its baseline or projection

The supplied accepted structural-closure dependency gives more than the displayed conclusion d_row R=0. In §§7–8 it defines the full ten-term D using U_r=g(s_raw,r I+k_r), normalizes M=g_ik⁻¹D, and derives

    0 = −g_il d_row M + A_ijkl.

The actual complementary product-factor support kills every summand of A. Hence d_row M=0 before trace-free projection. The dependency also establishes regularity on the original common intersections, including invariance of local rings under the stated regular vector fields. Its proof identifies all first-order lifts, source frames, inverse convention and derivative denotation. These are the needed inherited premises.

It would be invalid to infer d tr(M)=0 merely from dR=0 and R=tf(M)+dW: the latter only forces tf(dM)=0. For example a wholly central nonclosed cochain has zero trace-free part. The stronger unprojected anomaly identity is what avoids that error here.

The full-M character argument is independently correct. Write a=w_ij, b=w_jk, g=w_ik=a XOR b, p=3, q=12. The inherited actual scalar and transition-only pieces have character r, so the **whole** first lift has character

    char(U_r,ij)=w_ij XOR r.

Each of the two U_p U_q products has character g XOR 15. Each of the four first bidifferential slots has that same character, since the bidifferential adds its pair character. This includes derivatives of the scalar part of U. The mixed bidifferential adds all four bits. The three negative gerbe slots also have character g XOR 15, including the fully scalar −b_p b_q G term. Left normalization by G⁻¹ adds g and leaves character 15 in every slot. Thus this argument accounts for scalar-quadratic terms that are absent after trace-free projection; purity of R alone would not have established their purity.

The physical owner cohomology frame has the same deck character in its two columns, so its scalar sign cancels in End. Trace is invariant under owner-frame conjugation. Consequently c=tr(M)/2 is intrinsically a full-character scalar cochain; characteristic zero permits division by two. Trace commutes with the row Čech differential, and therefore dc=0 by full-M closure.

For the coefficient line, the finite-flat algebra has the square-free monomials as a free basis, including at ramification. Extracting the coefficient of z_0z_1z_2z_3 is a regular linear projection, not division by a possibly vanishing branch function. With z_all,A=τ_A²z_all,ref, equality of scalar sections gives a_A=τ_A⁻²a_ref. This is the O(−2,−2,−2,−2) coefficient convention used by the contraction. The actual deck-stable source restrictions retain this character extraction. They do not turn source functions with additional carrier/legal denominators into regular sections on standard tensor intersections.

## 2. One factor: the signs and the exceptional monomial

For the fixed convention

    d(a,b)=x⁻²b(1/x)−a(x),

write a finite Laurent polynomial f=Σ c_n xⁿ. The proposed map

    h(f)=(−Σ_(n≥0)c_n xⁿ, Σ_(n≤−2)c_n t^(−n−2))

has regular polynomial components in their respective affine charts. Substitution gives

    dh(f)=f−c_(−1)x⁻¹.

Conversely d(a,b) has disjoint exponent ranges for its two components: nonnegative from −a and at most −2 from x⁻²b(1/x). Hence hd(a,b)=(a,b). With P(f)=c_(−1)x⁻¹ and P=0 in degree zero, this proves the full operator identity dh+hd=1−P. The nonnegative part of h needs its minus sign, and the sole harmonic exponent is −1, not −2.

The relations dP=Pd=0, P²=P and h²=hP=Ph=0 follow on the same two degree groups. In particular no degree-zero harmonic piece has been suppressed.

## 3. Four factors: graded action and telescoping

For a homogeneous simple tensor, the total differential has the sign (−1) to the sum of preceding cochain degrees. The proposed operator is

    H = h⊗1⊗1⊗1 + P⊗h⊗1⊗1
        + P⊗P⊗h⊗1 + P⊗P⊗P⊗h,

using the graded tensor action. Thus its i-th term carries precisely the same preceding-degree sign, because h has degree −1. P is an operator of degree zero, even though its image is in factor degree one. Treating its operator degree as one would be an error.

For each summand, cross-factor differential terms cancel by the odd degrees of d and h. The remaining anticommutator is

    P^⊗i ⊗(dh+hd)⊗1^⊗(3−i),    i=0,1,2,3.

Substituting 1−P and telescoping proves dH+Hd=1−P^⊗4. Each factor P is zero in degree zero, so the tensor projector is supported only in total degree four. Its image there is the single all-x⁻¹ monomial. It follows for every **closed** degree-two c_std that

    d(Hc_std)=c_std.

For nonclosed degree-two inputs the omitted term would be Hdc_std, and degree alone does not remove it. The top-degree harmonic monomial is also not a boundary by this contraction. The stated side relations H²=0 and HP_top=P_topH=0 are valid but are not needed for the degree-two primitive.

The operator is finite and explicit on its stated Laurent-polynomial input. This does not mean the actual c has been evaluated or its Laurent coefficients have been supplied.

## 4. Three distinct cochain complexes and exact transport requirements

The tensor Čech total complex is not literally the ordinary Čech complex of the sixteen product opens. For example its degree-two group has 24 tensor-chart summands, while the normalized ordinary sixteen-open complex has 560 triple-intersection summands. They have standard comparison constructions, but an abstract equivalence is not a supplied algorithm on this source. The actual carrier/legal source cover is a third complex, with its own regular section domains and restrictions.

Accordingly the producer correctly requires a degree-preserving scalar cochain map Π:S→T with the actual coefficient-line identification included and values in regular tensor-intersection sections. A finite detector, selector on one component, rational expression with interior poles, or unsupported identification of those complexes is insufficient. Given this map and dc=0, HΠ(c) is the promised compared scalar primitive.

To compare M and R as End-valued cochains, a second chain map Π_End and a target scalar inclusion j_T must satisfy

    Π_End(f I)=j_T Π(f).

They must be defined on the relevant cochains and differentials. Then, without requiring an End trivialization,

    Π_End(M−R)=d(j_T HΠ(c)−Π_End(W)).

If one computes the scalar by tracing the target image, trace naturality is an additional needed compatibility. It is not needed when scalar Π is directly applied to the already extracted c. A chain map alone establishes this boundary identity in its target; a zero chain map illustrates why it need not reflect a source class identity.

For an actual source primitive, the stronger supplied data are chain maps A:S→T, B:T→S and a degree-minus-one K on S with

    dK+Kd=1−BA.

The exact formula is

    b_source=BHA(c)+Kc.

Indeed dAc=0, P_top Ac=0 in degree two, and therefore

    d b_source = BA(c)+(1−BA)c=c.

The plus sign before K is forced by the displayed homotopy convention. A target homotopy for AB is unnecessary for this implication; the source homotopy is essential. Regularity of these maps on the admitted source domain is necessary for a regular source primitive. None of A, B or K is constructed in this packet. In particular the notation BHA(c)+Kc must not be reported as an evaluated or already available original-cover primitive.

The common-refinement alternative is equally correct: if dη+ηd=ρ−rΠ, then b_Q=rHΠ(c)+ηc satisfies db_Q=ρc. This gives a refinement primitive and does not descend it without further transport.

## 5. Sign of the central removal and limitation of the result

From the inherited convention R=tf(M)+d_rowW and c=tr(M)/2 one obtains

    M−R=cI−d_rowW.

Thus any scalar primitive db=c produces exactly

    M−R=d_row(bI−W).

The sign before W is minus. This uses the scalar inclusion as a chain map and does not require bI and W to be individually global sections. Reversing the inherited convention for R would change the formula, but no such convention change is made here.

This removes only the central part of the full mixed defect and compares the full defect to the known trace-free representative. It proves neither that R is exact nor that the obstruction vanishes. It also provides no higher-order correction, source-value certificate, new pole/complexity bound, or detector value.

## 6. Independent invented controls

The independently written checker uses only small integer dictionaries of invented monomials and finite formal generators. It imports no producer/source/model code and reads no source coefficients. Its checks cover:

- 12 one-factor atoms in both degrees, both affine charts and all three Laurent ranges;
- 52 four-factor atoms across all 16 degree masks, with separate examples activating each summand of H;
- d²=0, H²=0 and the full dH+Hd identity on those controls;
- an invented closed degree-two cochain with six terms and its explicit four-term degree-one H-primitive;
- a toy source S=T⊕[k e→k f], with |e|=1, |f|=2 and de=f, where A and B are projection/inclusion and Kf=e;
- all ten full-M slot characters for the 256 possible ordered edge-character pairs, giving 2,560 integer checks.

The toy source verifies dK+Kd=1−BA and shows concretely that omitting K loses the f component. It is solely a formal control, not a claimed actual cover comparison.

Eight active negative controls reject the wrong positive Laurent-split sign, wrong harmonic exponent, omitted Koszul sign, omitted prefix projectors, omitted closedness hypothesis, false top-degree exactness, omitted K and wrong sign before W. All tests use explicit exceptions and pass under normal Python and python −O with byte-identical reports. Their finite success controls conventions; the universal written arguments above establish the identities.

I additionally inspected the producer checker before independently replaying it normally and under optimization. Both reports are byte-identical and confirm its nine inert proof pins, 10,000 selected tensor atoms, 1,536 invented degree-two controls and 40,960 full-M integer character checks. All four accepted dependency snapshots now match their current reviewed originals byte-for-byte; see `dependency-comparisons.json`. An initially stale closure-review snapshot was refreshed before final pinning, with no change to the mathematics.
