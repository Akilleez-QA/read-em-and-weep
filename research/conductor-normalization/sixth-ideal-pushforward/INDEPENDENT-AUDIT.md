# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: sixth triple-diagonal ideal power

## Verdict

PASS in characteristic zero, with the natural ungraded descent linearization and the fixed one-dimensional normalization lines used in the fourth-power proof.

Put Z=(P1)^4, Y=Sym^4(P1)=P4, q:Z→Y, A=q*O_Y(1), I=I_D for the reduced union of the four triple diagonals, and N=q(D) with its reduced structure. Let v be the Vandermonde section of A^3 carrying sign. In the full rank-six trace normalization, the proposed identities hold globally:

    J3 := (q_*I^3)^S4 = (t3,t2^2),
    (q_*I^6)_sign = J3 tensor O_Y(-3).

For EA=q*B0 tensor A^(-1), they give

    (q_*(I^6 EA))_sign = B0(-4) tensor J3.

These are equalities of subsheaves under the established Vandermonde identification, including over quadruple collisions. The ideal J3 defines a degree-(3,4) complete intersection of degree 12, supported on N. Its nilradical is a square-zero invertible O_N-module O_N(-2). Thus “double N” is valid as a scheme-theoretic description, with the qualification that no splitting of the square-zero extension is asserted.

No physical-source value, source order, obstruction coordinate, cohomology rank, or induced cohomology image is evaluated by these statements.

## 1. Inputs independently checked against the fourth-power proof

The files fourth-ideal-pushforward/PROOF.md and fourth-ideal-pushforward/INDEPENDENT-AUDIT.md establish the following ingredients:

1. I is locally a two-generator regular-sequence ideal, also at the quadruple diagonal.
2. The three weight values σ1,σ2,σ3 sum to zero. Their differences generate I after trivializing A.
3. Their difference product is a nonzero constant times v.
4. Every regular alternating section is v times a regular invariant section, with the A^(-3) line twist.
5. The reduced triple-root surface has ideal I_N=(t2,t3), where t2 and t3 have degrees 2 and 3 downstairs, and form a regular sequence.
6. For every k≥3, the local ordinary-power colon formula is (I^k:v)=I^(k-3).

For the regular-sequence hypothesis, the preceding independent audit gives explicit common-affine-root equations

    I=(a(c-b), b(c-a)),

with a=x1-x4, b=x2-x4 and c=x3-x4. This is a reduced codimension-two complete intersection, including a=b=c=0. The argument below uses this I-adic regular-sequence structure. It does not replace it by smoothness of D or by maximal-ideal order at a quadruple collision.

The prior nullcone proof establishes the scheme equality I_N=(t2,t3), rather than merely its radical. This scheme equality is essential when expressing an arbitrary invariant coefficient by the two generators downstairs.

## 2. Exact leading form of t2

Choose a local frame of O_Y(1) and its pullback frame of A. Set

    x=σ1-σ2,    y=σ1-σ3.

The trace-zero identity gives the exact formulas

    σ1=(x+y)/3,
    σ2=(y-2x)/3,
    σ3=(x-2y)/3.

Consequently, in the stated trace normalization,

    t2=2(σ1^2+σ2^2+σ3^2)
      =(4/3)(x^2-xy+y^2),

and

    t3=2(σ1^3+σ2^3+σ3^3)
      =(2/9)(x+y)(y-2x)(x-2y).

In particular q*t2 lies in I^2 and q*t3 lies in I^3.

At any point of D, write R for the local ring upstairs. Since x,y are a regular sequence,

    gr_I R = (R/I)[X,Y].

The degree-two initial form of t2 is

    Q=(4/3)(X^2-XY+Y^2).

Multiplication by Q is injective over every coefficient ring R/I: after multiplication by the unit 3/4, it is monic in X over (R/I)[Y]. This does not require R/I to be a domain, and thus applies at intersections of the triple-diagonal components. For the degree-zero calculation actually needed here, one can simply inspect the X^2 coefficient.

It follows that

    t2 a ∈ I^3  implies  a ∈ I

for every regular local a upstairs: taking the degree-two class gives (a mod I)Q=0. The reverse implication is immediate. Thus the relevant local colon identity is

    (I^3:t2)=I.

Away from D both sides are the unit ideal. A change of frame multiplies the relevant sections by units, so this local assertion is compatible with the line-bundle conventions. The useful algebraic property is the unit leading coefficient; a bare assertion of nondegeneracy of a quadratic would not substitute for this argument over a general coefficient ring.

## 3. Invariant contraction in degree three

Work locally downstairs, trivializing O_Y(1), and let f be a regular invariant coefficient whose pullback belongs to I^3.

First, I^3⊂I implies f∈I_N, by the already audited contraction equality (q_*I)^S4=I_N. Since I_N=(t2,t3) as an ideal sheaf, there are regular local coefficients a,b downstairs such that

    f=t2 a+t3 b.

Here a and b have the corresponding degree -2 and -3 twists if frames are not suppressed. Pulling back, the second summand lies in I^3. Hence t2 a lies in I^3 upstairs. Section 2 forces q*a∈I, so invariant contraction gives a∈I_N downstairs. Write a=t2 c+t3 d. Then

    f=t2^2 c+t3(b+t2 d),

and hence f∈(t3,t2^2).

Conversely, q*t3∈I^3 and q*(t2^2)∈I^4⊂I^3, so every local section of (t3,t2^2) pulls back into I^3. Therefore

    (q_*I^3)^S4=(t3,t2^2).

The proof is local in the appropriate quotient neighborhoods, and all its expressions have the required line twists. The right side is the globally defined ideal sheaf which is the image of

    O_Y(-3) direct-sum O_Y(-4) → O_Y,
    (b,c) ↦ t3 b+t2^2 c.

It therefore glues without a choice of generator scalars or local coefficient decomposition. The nonuniqueness of a,b is harmless: the argument proves the requisite property for any such local decomposition.

No extension-contraction equality q*I_N=I is used or true in general. In particular, one must not replace this calculation by the assertion that ordinary ideal powers commute with the ramified quotient.

## 4. Sixth-power sign pushforward and coefficient twist

The general Vandermonde colon lemma gives

    (I^6:v)=I^3.

Indeed the degree-three initial form of v is a unit times XY(Y-X), and multiplication by that polynomial is injective in gr_I R. This remains valid at quadruple collisions and uses ordinary ideal powers.

A regular sign section is uniquely v times an invariant section of A^(-3). Such a section belongs to I^6 precisely when its invariant quotient belongs to I^3 tensor A^(-3). Finite pushforward and the projection formula therefore identify

    (q_*I^6)_sign
      = (q_*I^3)^S4 tensor O_Y(-3)
      = (t3,t2^2) tensor O_Y(-3).

For EA=q*(B0(-1)), a second application of projection formula yields

    (q_*(I^6 EA))_sign = B0(-4) tensor (t3,t2^2).

The inclusion into the unrestricted sign coefficient B0(-4) is the usual ideal inclusion. If “sign summand” denotes the literal equivariant isotypic sheaf, the one-dimensional sign representation remains an explicit factor; suppressing it gives the multiplicity sheaf displayed here. Restoring the fixed binary determinant normalization lines does not change the ideal calculation or the degree shifts.

## 5. Complete intersection and exact double structure

Let C=V(t3,t2^2). Its reduced support is N because

    radical(t3,t2^2)=radical(t3,t2)=I_N.

As t2,t3 form a codimension-two regular sequence in the smooth ambient P4, t3,t2^2 also form a regular sequence at every point of their common zero scheme. Equivalently, t2 is a nonzerodivisor modulo t3, and therefore its square is too. Thus C is a codimension-two complete intersection of degrees 3 and 4. It is Cohen–Macaulay, has no embedded associated components, and has degree 12.

There is more information than generic multiplicity two. Its nilradical is

    I_N/J3=(t2,t3)/(t3,t2^2).

Multiplication by t2 induces an isomorphism

    O_N(-2) ≅ I_N/J3.

To check the kernel locally, if t2 h∈(t3,t2^2), reduce modulo t3. Since t2 is a nonzerodivisor modulo t3, this forces h∈(t2,t3). Surjectivity is immediate. The induced multiplication on I_N/J3 is zero, because t2^2 vanishes in O_C. Consequently there is a canonical exact sequence

    0 → O_N(-2) → O_C → O_N → 0,

whose first term is the square-zero nilradical. This proves that C is a double structure with an invertible nilradical everywhere on N, including the quadruple-root curve. It does not assert that this exact sequence splits as modules or algebras, and does not assert that N is smooth.

The sixth-power sign condition is strictly stronger as a sheaf condition than the common fourth-/fifth-power sign condition. The exact difference is

    0 → J3 → I_N → O_N(-2) → 0.

After inserting the coefficient bundle,

    0 → B0(-4) tensor J3 → B0(-4) tensor I_N
      → B0(-6)|_N → 0.

This strictness at the sheaf level does not determine strictness of an induced H^2 image.

## 6. Koszul resolution and regular coefficient criterion

The complete-intersection resolution of J3 is

    0 → O_Y(-7) → O_Y(-3) direct-sum O_Y(-4)
      → J3 → 0.

For the generator order (t3,t2^2), the first map is c↦(-t2^2 c,t3 c), and the second is (b,c)↦t3 b+t2^2 c. Tensoring by the locally free B0(-4) gives

    0 → B0(-11) → B0(-7) direct-sum B0(-8)
      → (q_*(I^6 EA))_sign → 0.

Thus, on a quotient-adapted local chart, a regular sign coefficient written as v f lies in I^6 EA exactly when

    f=t3 b+t2^2 c

for regular local coefficient sections with the displayed twists. This criterion concerns local regular coefficients. It neither provides individually closed choices b,c for a closed cochain nor evaluates the map from this sheaf into the global obstruction cohomology.

## 7. Scope and sources

Audited local inputs:

- fourth-ideal-pushforward/PROOF.md
- fourth-ideal-pushforward/INDEPENDENT-AUDIT.md
- prerequisite weighted-koszul-cohomology, document PROOF.md (see the unit INPUTS.md), especially sections 1 and 6

This audit is a bounded independent algebraic check of the proposed sixth-power invariant contraction, sign pushforward, and scheme structure. It performs no physical-source evaluation, no rank computation, no external app write, and no large computation. Its conclusion retains the inherited coefficient and linearization hypotheses of the cited audited inputs.

## 8. Additional check of PROOF.md section 6: formal duality criterion

The optional cohomological criterion in the sixth-power proof also passes, under its stated self-duality hypothesis B0≅B0∨ and the separately admitted dimension of the ambient H^2 target.

The local-complete-intersection surface M=C above is projective, Cohen–Macaulay and Gorenstein even though it is nonreduced. Adjunction gives

    ω_M = (ω_Y tensor O_Y(3+4))|_M = O_M(2).

For F=B0(-4), Serre duality on Y identifies H^2(Y,F)^∨ with H^2(Y,B0(-1)). Serre duality on the Gorenstein surface M identifies H^2(M,F|_M)^∨ with H^0(M,B0(6)|_M). Thus the dual of the restriction map has exactly the proposed source and target.

The Koszul resolution, tensored by B0(6), breaks into

    0 → B0(-1) → B0(3) direct-sum B0(2)
      → B0(6) I_M → 0,
    0 → B0(6) I_M → B0(6) → B0(6)|_M → 0.

The composition of their connecting homomorphisms is

    δ_M : H^0(M,B0(6)|_M) → H^2(Y,B0(-1)).

This is the dual restriction/Gysin map under the Koszul adjunction identifications, up to the overall sign convention for the two-step boundary. Such a sign leaves its image, annihilator, and rank unchanged. Consequently

    im[H^2(B0(-4) I_M) → H^2(B0(-4))]
      = (im δ_M)^perp.

If the inherited value h^2(B0(-4))=10 is used, the image dimension is 10-rank δ_M. No value of rank δ_M follows from this duality statement, and no positivity vanishing or source membership is silently used.

## Appendix A. Targeted audit of the proposed all-powers extension

This appendix checks the precise local-flatness and associated-graded steps proposed by the author. It does not evaluate any source or cohomology rank.

### A.1 Local base and miracle flatness

Fix y∈N and trivialize O_Y(1) near y. Put R=O_Y,y and let t2,t3 denote the resulting regular functions. The map

    A0=k[u,v]_(u,v) → R,    u↦t2, v↦t3,

is well-defined and local: polynomials nonzero at (0,0) map to units in R, while both t2,t3 lie in the maximal ideal. The target is a regular, hence Cohen–Macaulay, Noetherian local ring, and the map is essentially of finite type. The source A0 is a regular local ring of dimension two. Since t2,t3 form a regular sequence at y,

    dim R/(t2,t3) = dim R-2.

These are the standard local miracle-flatness hypotheses, so R is flat over A0. The assertion applies to arbitrary scheme points y of N, not just closed points; their residue fields need not be k. The dimension formula uses Krull dimensions of the corresponding local rings. No global smoothness of N is needed.

### A.2 Weighted filtration and its exact graded algebra

Define L_n in A0 to be the ideal generated by u^a v^b with 2a+3b≥n, and K_n=L_n R. Flatness preserves the inclusions and the successive quotient sequences for the L_n. Since the weighted associated graded of A0 is k[U,V] with deg U=2 and deg V=3, and every graded piece is annihilated by (u,v), this gives

    gr_K R = (R/(t2,t3))[U,V],
    deg U=2,    deg V=3.

There is no appeal here to a formal completion or to convergence of an expansion. Localizing k[u,v] at (u,v) does not change this graded algebra: every inverted denominator has nonzero degree-zero initial term.

### A.3 Injectivity into the upstairs associated graded

For a clean stalkwise statement, use the finite semilocal algebra S=(q_*O_Z)_y and the ideal I_S=(q_*I)_y. The weight differences x,y in the chosen frame generate I_S. Their regular-sequence property can be checked at all maximal ideals of S, where it is the already audited local property on Z. Hence

    gr_I S=(S/I_S)[X,Y].

The invariant-contraction identity yields an injection

    R/(t2,t3) → S/I_S.

The proposed graded map sends U to Q2=(4/3)(X^2-XY+Y^2) and V to the corresponding homogeneous cubic Q3. The universal map

    k[U,V] → k[X,Y],    (U,V)↦(Q2,Q3),

is injective. To verify this without a generic-point or representation-theoretic shortcut, express the three σ values as the indicated k-linear combinations of X,Y. They satisfy the monic cubic

    T^3-(Q2/4)T-Q3/6=0.

Thus they, and therefore X,Y, are integral over k[Q2,Q3]. The polynomial ring k[X,Y] is finite over that subalgebra, so dim k[Q2,Q3]=2. A k-algebra generated by two elements and of dimension two has no algebraic relation between its generators. This proves the injection.

Tensoring this injection with S/I_S over the field k preserves injectivity. Combining it with the coefficient injection above proves that the natural graded map

    (R/(t2,t3))[U,V] → (S/I_S)[X,Y]

is injective. Using the semilocal pushforward stalk avoids any need to infer injectivity from a single selected branch of D.

### A.4 Frames and the finite-order argument

A change of frame of O_Y(1) multiplies t2 and t3 by the corresponding unit powers 2 and 3. Every weighted monomial ideal K_n is therefore unchanged. Globally it is the ideal sheaf generated by the images of O_Y(-(2a+3b)) under t2^a t3^b, for 2a+3b≥n. The upstairs variables change by the common degree-one frame factor, so the graded map is compatible with the same weighted gluing.

Every K_n pulls back into I^n. Conversely, if f∉K_n, choose the largest integer r<n for which f∈K_r. Its degree-r graded class is nonzero. The graded injectivity just proved implies that its pullback is not in I^(r+1), and hence is not in I^n. This is a finite argument involving only the filtration through degree n. It needs neither separatedness of an infinite filtration nor completion.

Accordingly the proposed flatness-and-graded-injectivity chain is valid and establishes the local contraction formula

    (q_*I^n)^S4 = (t2^a t3^b : 2a+3b≥n),    n≥0,

with the stated global ideal-sheaf interpretation. Outside N both ideals are the unit ideal for positive n, so there is no additional gluing issue there. The sixth-power result is its n=3 case and does not depend on this more general argument.

## Appendix B. Audit of ALL-POWERS.md: finite resolution and eventual H^2 vanishing

The actual ALL-POWERS.md text was read after Appendix A was prepared. Its sections 1–3 agree with the audited flatness, graded injection, and finite-order argument. Sections 4–5 also pass the following checks.

### B.1 The finite adjacent-generator resolution

For n≥1, the divisibility-minimal exponent pairs for 2a+3b≥n can be ordered with a strictly decreasing and b strictly increasing. The pure-power endpoints are exactly u^ceil(n/2) and v^ceil(n/3). For neighboring minimal generators

    m_i=u^(a_i)v^(b_i),    m_(i+1)=u^(a_(i+1))v^(b_(i+1)),

their least common multiple is u^(a_i)v^(b_(i+1)), of weighted degree e_i=2a_i+3b_(i+1). The relation is

    v^(b_(i+1)-b_i) m_i - u^(a_i-a_(i+1)) m_(i+1)=0.

Thus both the signs and the source/target line degrees in the proposed map are correct.

These adjacent relations generate the entire syzygy module over k[u,v]. In each monomial multidegree, the minimal generators dividing that monomial form a consecutive interval: the u-exponent inequality selects a final interval and the v-exponent inequality selects an initial interval. Consecutive differences span all coefficient vectors with sum zero on their intersection. Polynomial relations decompose into these finitely many multidegrees. Independence of the adjacent syzygies follows successively from the first, second, and later components in the polynomial domain. This gives the exact two-term free resolution of the monomial ideal.

At y∈N, the flatness already checked preserves this resolution after substitution u=t2,v=t3. Outside N one of t2,t3 is a unit. The polynomial resolution localized at the corresponding variable resolves the unit ideal and is a split exact sequence of modules, since its final module is free. Substitution into any target algebra therefore preserves exactness there as well. Hence the global sequence

    0 → direct-sum_i O_Y(-e_i)
      → direct-sum_i O_Y(-d_i) → K_n → 0

is exact everywhere, with d_i=2a_i+3b_i and the displayed homogeneous maps. No global flatness away from N is required.

For a minimal generator with a_i>0, removing one u proves d_i-2<n, hence n≤d_i≤n+1. At the pure-v endpoint, removing one v proves d_i-3<n, hence n≤d_i≤n+2. The common stated bound n≤d_i≤n+2 is therefore correct. Each neighboring least common multiple has weighted degree at least that of either generator, so e_i≥n. These are uniform lower bounds on every summand in the resolution as n grows.

### B.2 Eventual H^2 vanishing and the threshold inequality

After tensoring by B0(-4), the long exact cohomology sequence has

    H^2(F0) → H^2(B0(-4)K_n) → H^3(F1),

where F0 is a sum of B0(-4-d_i) and F1 is a sum of B0(-4-e_i). Trace self-duality and ω_Y=O_Y(-5) give exactly

    H^2(B0(-4-d))^∨ = H^2(B0(d-1)),
    H^3(B0(-4-e))^∨ = H^1(B0(e-1)).

Serre vanishing supplies some integer T such that H^1(B0(t)) and H^2(B0(t)) both vanish for all t≥T. For every n≥max(1,T+1), the inequalities d_i,e_i≥n put all the dual twists in this range. Both outer groups in the displayed exact sequence vanish, so

    H^2(Y,B0(-4)K_n)=0.

With n=k-3, the equivalent sufficient condition is k≥max(4,T+4). This proves existence of an eventual vanishing threshold and its formal dependence on a Serre bound. It does not compute T, an effective numerical k, or the least possible threshold. The number of summands may grow with n; that causes no issue because every individual finite sum has all its summands in the vanishing range.

A closed sign two-cochain that actually takes values in I_D^k EA determines a class in this coefficient H^2. Therefore sufficiently large ordinary collision-ideal membership is indeed a universal sufficient condition for its ambient obstruction class to vanish. The proof does not establish that a particular physical source has that membership, or confuse this collision-ideal exponent with a deformation expansion order.

### B.3 Extended verdict

PASS for the all-powers invariant-contraction formula, its sign-pushforward consequence, the adjacent-generator resolution, and eventual H^2 vanishing, with the hypotheses and scope stated in ALL-POWERS.md. No further geometric or numerical hypothesis is needed beyond the audited regular-sequence/weight/trace inputs, characteristic zero, locally free self-dual B0, and standard local flatness and Serre-duality/vanishing results.
