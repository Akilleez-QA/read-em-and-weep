# Explicit sparse adjoint grammar for the transition-only scalar solver

## Result

The tensor-homotopy transpose is an explicit chart/exponent filter. It produces at most one input coefficient request per surviving pivot, with a known sign. The entire scalar degree-two-to-one solver can be transposed using finite tuple rules: the standard-cover K term needs at most five triangle requests per edge, and the A h S term has at most 32 unmerged path requests per edge before the carrier projection (at most 16 for pair 12).

These are combinatorial request bounds, NOT polynomial-product counts or a memory certificate. Multiplication by weights and currents can enlarge coefficient support substantially. In particular, the H_rho branch retains unweighted suffix denominators: without the new outer detector's cancellation certificate it must remain a rational demand, not be converted into a fictitious finite Laurent expansion.

No physical source polynomials, partitions, jets, residuals, or coefficients were calculated. This note extends `direct-scalar-free-pairing-reduction.md`, using the same pinned source and N14 scalar solver.

## 1. Coefficient atoms and conventions

Use the common finite frame in every coordinate. A tensor coefficient atom

    eps_(sigma,e)(f) = [x^e] f_sigma

has sigma in {A,B,C}^4, exponent e in Z^4, and Cech degree equal to the number of C entries. A means finite-chart degree zero, B means infinity-chart degree zero, and C means the oriented overlap [0,1].

For twist n_i, an A coefficient is admissible only at e_i>=0; a B coefficient only at e_i<=n_i. C permits any integral exponent. The pair character has n_i=-2 in its pair and n_i=0 otherwise.

A demand record additionally carries its cochain tuple, scalar multiplier/kernel, frame, and an ownership ledger for every denominator. A signed sum merges only genuinely identical records, including ownership and frame. Sorting an alternating tuple contributes its permutation sign; an identical repeated common vertex gives zero. Repeated standard-chart labels alone do not make a general common-cover cochain zero.

Coefficient atoms are used only on certified Laurent-polynomial entries. A rational demand is a distinct record until an exact regularization/cancellation witness lowers it to coefficient atoms.

## 2. One-factor transpose, completely explicit

The scalar contraction on an overlap monomial is

    h_n(x^e C)=-x^e A          if e>=0,
              =+x^e B         if e<0 and e<=n,
              =0              otherwise.

Thus

    h_n^* eps_(A,e) = -eps_(C,e)    if e>=0,
    h_n^* eps_(B,e) = +eps_(C,e)    if e<0 and e<=n,
    h_n^* eps_(C,e) = 0,

with all unmet cases zero. Explicitly, for n=0 the B threshold is e<=-1; for n=-2 it is e<=-2. In particular h_0^* eps_(B,0)=0 and h_0^* eps_(A,0)=-eps_(C,0).

For J_n=i_n p_n:

    J_0^* eps_(A,0)=eps_(B,0),
    J_0^* eps_(B,0)=eps_(B,0),

and every other J_0^* coefficient atom is zero. Both output constants read the SAME input B constant; they are not separate unknown coefficients.

For n=-2,

    J_-2^* eps_(C,-1)=eps_(C,-1),

and every other atom is zero. These rules include the asymmetry of p_0, which reads B rather than A.

## 3. Four-factor transpose, including signs

Write

    h=sum_j J_1 tensor ... tensor J_(j-1) tensor h_j tensor 1_(j+1) ... 1_4.

For an output atom eps_(sigma,e), the j-th adjoint branch survives exactly when:

1. At every i<j with n_i=0, sigma_i is A or B and e_i=0. Replace that prefix state by B, exponent0.
2. At every i<j with n_i=-2, sigma_i=C and e_i=-1. Keep it unchanged.
3. At j, sigma_j=A with e_j>=0, or sigma_j=B with e_j<0 and e_j<=n_j. Replace it by C, keeping e_j.
4. All suffix states/exponents stay unchanged.

Multiply its weight by

    (-1)^(number of C states before j) times
       (-1 if sigma_j=A, +1 if sigma_j=B).

There is no additional transpose sign: these are ordinary duals of already signed linear maps. Every surviving branch increases Cech degree by one. No coefficient exponent changes in h^*.

For a degree-one OUTPUT request in pair12, j=3,4 are impossible: their prefix would require both coordinates1,2 to be C, already giving degree2. Only j=1,2 remain. For pair34 all four pivots are possible, subject to the displayed filters. A single pivot generates one demand, not an exponent interval.

Examples fixing the convention:

- Pair12: an output atom (A,C,B,B) at (e,-1,f,g), e>=0, contributes minus the input (C,C,B,B) at the same exponents through j=1.
- Pair12: an output atom (C,B,A,B) at (-1,e,f,g), e<=-2, contributes minus the input (C,C,A,B), because the B sign is plus and the one-prefix-C sign is minus.
- Pair34: output (A,B,C,A) at (0,0,-1,e), e>=0, contributes plus (B,B,C,C) through j=4: the pivot A minus and prefix-C minus cancel.

## 4. Exact degree-one cover transposes

All rules in this section act in the same finite frame; restrictions change the legal domain, not coefficient exponents. If a different local frame is stored, apply its exact frame-conversion rule first.

### R^*: common edge to standard edge

For a common edge (a0,a1), let e0=r(a0), e1=r(a1). A request on R t becomes a request on t_(e0,e1), sorted with sign. If e0=e1 it is zero. This kills only the two R-mediated branches of T, not H_rho.

### K_cov^*: at most five triangles

For a standard oriented edge sigma=[e0,e1], put b=min(e0,e1) coordinatewise. Let v0=e0 and form a path to e1 by changing coordinates in order 4,3,2,1, skipping unchanged coordinates. Denote its oriented edges [v_(l-1),v_l]. Then the degree-one rectangle-cone formula is exactly

    k[sigma] = [b,e0,e1] - sum_l [b,v_(l-1),v_l].

K_cov^* sends an edge coefficient request to this signed sum of triangle requests with the same exponent. Sort each triangle and kill repetitions. At most five triangles occur before cancellation. The reverse coordinate order follows from the fixed Alexander-Whitney cuts, not a free choice.

Control in two coordinates:

    k[00,11] = -[00,01,11].

The +[00,00,11] and first path triangle vanish; the surviving path is 00->01->11.

### A^*: standard edge to at most four tensor cells

For each active factor d=1,...,4, use A or B state e0,i for i<d, the oriented edge [e0,d,e1,d] at d, and A or B state e1,i for i>d. If the active endpoints coincide, kill the term. If they are (1,0), multiply by -1 and use C=[0,1]. If (0,1), use C with +1. The exponent is unchanged.

This is the degree-one specialization of the cut map and gives at most four tensor degree-one atoms. Apply section3's h^* next.

### S^*: degree-two tensor cell to two paths

A degree-two tensor cell with active coordinates d<e becomes

    request on path changing d then e
       minus request on path changing e then d,

with all inactive coordinates fixed by their A/B states. Both paths have three standard vertices and are increasing. Exponents are unchanged. This is the exact S^* sign, including the control CC -> (00,10,11)-(00,01,11).

Consequently S^* h^* A^* R^* has at most 4*4*2=32 raw triangle requests per common edge, and at most4*2*2=16 for pair12. These are upper bounds before zero filters and duplicate merging, not arithmetic or stored-size bounds.

### Pi^*: standard triple to weighted common triples

For a standard triple (e0,e1,e2), branch over alpha0,alpha1,alpha2, each a carrier/legal-mask label. The common tuple is

    ((e0,alpha0),(e1,alpha1),(e2,alpha2)),

and its multiplier is rho_(e0,alpha0) rho_(e1,alpha1) rho_(e2,alpha2). Sort using SOURCE-FIRST common ordering and retain its sign. Kill identical common vertices. Do not re-evaluate the nonlinear F after sorting; read its fixed alternating extension.

The finite alphabet has at most96 source labels per row before structural zeros. The prescribed partition kills primary carrier j when j exceeds the row's infinity count. Finite coordinates kill mask1. These are exact label filters with no polynomial evaluation.

### H_rho^*: two explicit branches

For a common output edge (a0,a1), with e_l=r(a_l), the degree-two input formula is

    (H_rho f)_(a0,a1)
      = sum_beta0 rho_(e0,beta0) f_(b0,a0,a1)
        - sum_beta0,beta1 rho_(e0,beta0)rho_(e1,beta1)
                                      f_(b0,b1,a1),

where b_l=(e_l,beta_l). Thus an output request becomes precisely these two families of weighted input triple requests. Sort every triple source-first and retain signs. The first branch has at most96 inserted labels; the second at most96^2 before zeros. These fixed finite branching bounds say nothing about the coefficient support of the weights.

Crucially, weights clear inserted-vertex denominators only. The unchanged suffix still owns its carrier/legal denominators.

## 5. E_p^* and derivative composition

For p=(a,b), use currents L_d=A^(-1)V_d(A), U_d=A^(-1)B^(-1)V_d(B)A. A matrix request [x^kappa]tr(W E_p(t)_ijk) becomes four scalar differentiated edge requests:

    +1/2 [x^kappa] tr(W L_b) V_a(t_jk),
    -1/2 [x^kappa] tr(W L_a) V_b(t_jk),
    +1/2 [x^kappa] tr(W U_a) V_b(t_ij),
    -1/2 [x^kappa] tr(W U_b) V_a(t_ij).

The scalar multipliers can still be rational; retain their denominator ownership. This rule fixes the edge choices and all four signs before any source value is constructed.

Once w is certified finite Laurent and the exact stripped derivative is partial_i,

    [x^kappa](w partial_i f)
       = sum_(nu in supp w) (kappa_i-nu_i+1)
                         w_nu [x^(kappa-nu+e_i)]f.

The demand exponent is kappa-nu+e_i. Filter by the certified support of f and kill the zero scalar factor. For an exact local derivative a partial_i+b, first include a and b in the respective multiplier and then apply this rule and ordinary convolution. Never silently replace the physical V_i by partial_i before its frame and character conversion.

On a naked coefficient atom,

    partial_i^* eps_(sigma,kappa)
       =(kappa_i+1) eps_(sigma,kappa+e_i).

For h^* partial_i^*, the h thresholds are tested at the SHIFTED exponent kappa+e_i, not kappa. This handles boundary values and coefficient-zero cases exactly.

## 6. A complementary-derivative intertwining identity

There is an additional useful monomial identity, with a precise change of twist:

    partial_x h_0 = h_-2 partial_x,
    partial_x J_0 = J_-2 partial_x = 0.             (4)

Here partial_x maps the finite-frame Cech complex of O to that of O(-2). On A, differentiation maps nonnegative powers to nonnegative powers, with the constant killed. On B, e<=0 differentiates to e-1<=-2 whenever nonzero. On C, every integral exponent is allowed.

Check on C x^e:

- e>=1: both sides of the first identity are -e x^(e-1) A;
- e=0: both sides vanish;
- e<=-1: both sides are +e x^(e-1) B.

For the J identity, differentiation kills the degree-zero constant inclusion, while the target harmonic coefficient x^-1 of a derivative is always zero. This is an exact identity, not a truncation convention.

In several factors, when n_i=0 and n'_i=-2 with other twists unchanged,

    partial_i h_n = h_(n') partial_i.               (5)

For pivots before i, differentiation commutes with an identity suffix; at i use (4); for pivots after i both sides have the zero composition with J_i. No new Cech Koszul sign arises because partial_i has Cech degree0.

This is relevant precisely to E_p(T_q F_q): p and q are complementary, so the differentiated factor of the q-character has twist0. In the usual elliptic finite chart V_i=y_i partial_(x_i); after stripping the new y_i character, its scalar coefficient is partial_(x_i). At infinity the resulting O(-2) frame conversion must still be applied. Equation (5) may then move the stripped derivative across the tensor h, with the twist changed. It does NOT commute derivatives through Pi or H_rho: those maps have nonconstant weights whose derivatives must be retained. Nor does it authorize differentiating an already absorbed same-coordinate seed as though it were constant.

This intertwining rule is optional for a compiler: the direct shifted-demand rule in section5 is already sufficient and less reliant on frame bookkeeping.

## 7. Known finite supports and the exact stopping boundary

### Known without new polynomial arithmetic

- All tuple alphabets and branches in sections2-4 are finite and explicit.
- The h^* coefficients and exponents are exact filters, not interval estimates.
- Each fixed N14 partition weight is an explicitly finite polynomial formula.
- For a sorted physical source triple, the owned cleared F numerator P has coordinate degrees <=217 in the two pair coordinates and <=210 elsewhere.
- After cancellation of all inserted carrier and pair-legal factors, the local carrier quotients have the existing finite degree bounds: s=0 gives66; s=1 gives335 finite/213 infinity; s=2 gives872/347; s=3 gives1677/481; s=4 gives66 infinity. Pair-legal quotients add at most1 per infinity row and other-coordinate raw legal weights at most2.
- On the Pi branch these yield the existing exact exponent predicate

      p_i + sum_(finite rows) a_(l,i)
          - sum_(infinity rows) a_(l,i) - m_i = kappa_i.

  All p and a variables have finite boxes. This defines support demand without enumerating the boxes.
- Restriction and frame change are finite signed monomial-exponent transformations once frames are specified; A,S,K do not multiply by an unknown polynomial.

### Not yet certified for the new full pairing

- A concrete outer detector Phi on the new refined trace-free representative, with its own coefficient/kernel support.
- Complete denominator cancellation for the products of that detector's weights, the E currents, and the H_rho unchanged suffix. N14 clears the scalar solver's inserted vertices, not arbitrary new outer source/current products.
- Finite Laurent support of a rational intermediate solely because its eventual sum is regular. Individual terms may still have denominators; termwise support must not be guessed.
- The exact support or width of differentiated outer kernels and weight products, and their product count after reuse.
- A certified complete arithmetic and storage schedule.

A sound implementation therefore has three demand types:

1. COEFFICIENT: a certified Laurent atom with explicit finite support bounds.
2. FINITE_SUM: symbolic bounded label/exponent sums with exact weights, signs and predicates; these need not be enumerated.
3. RATIONAL_PENDING: a denominator-owned expression requiring a cancellation/regularization witness before coefficient lowering.

The grammar is mathematically finite through all known maps, but cannot turn RATIONAL_PENDING into COEFFICIENT merely by calling a rational function a Laurent polynomial. A missing outer certificate is an explicit static failure state, not an execution invitation.

## 8. Concrete compiler output required next

Starting with a specified Phi, emit the four E^* edge demands per matrix request. For each, emit the three T^* branches using the exact rules above. Apply derivative shifts and prefix/pivot filters before multiplying any source polynomial. Fuse weights symbolically with their actual owned denominator factors. Where cancellation is certified, produce finite exponent predicates on the P numerators and quotient factors. Otherwise return the precise RATIONAL_PENDING witness.

Only after this closure is complete should the DAG be priced for nonconstant products, coefficient widths, and peak live bytes. The finite branching figures here do not themselves pass that gate.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
