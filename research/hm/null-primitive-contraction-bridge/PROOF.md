# Primitive decoder and three-premise contraction bridge

## Result and boundary

The frozen `PhysicalModel.primitive` is a decoder, not a B/C/T split constructor. It reads four stored rational matrices and constructs W, L and eta. Neither the pinned JavaScript formula excerpt nor the first-order specification supplies a B/C/T construction. No such construction is inferred here.

A narrower useful theorem is proved: with the literal evaluation map and pivot split, THREE matrix identities imply the entire moving-frame contraction system and both complex identities. Thus separate checks of every contraction are redundant. These three families are logically independent for arbitrary matrices of these block shapes, in the precise sense explained below. This is not a claim of a minimal generating set of the actual coefficient ideal, nor a proof that the pinned model satisfies these identities.

No production module was imported or run. No actual polynomial product, matrix contraction, physical source, model evaluation, owner, or jet was computed. Only immutable source reads, AST/JSON metadata and literal-shape checks, invented formal words, and three tiny invented integer-matrix countermodels were used. This proof does not grant permission to execute physical polynomial products. Production guards are unchanged.

## 1. Authenticated source and decoder denotation

`pins.json` identifies raw_engine.py at e93cf712f9da4926a8450cc870ed45a7bfc379ab, source formulas and model at 10810ee877fdaf291399198ad60d7dd0c316a42d, and first-order-source.md plus the historical homogeneous checker at 08b73637d4136f91606aad332c46cafd064417f8. The latter was retrieved read-only; its saved 5,050 bytes reproduce Git blob 25816d9ba8699ffaf20c562d9dd8403f049ae383. It is saved with a .txt suffix and never imported or executed.

Assume the scalar API denotes an exact commutative field over Q and each inverse invoked exists. For a record t of pairs (e,c), the `polynomial` loop denotes

    D(t) = sum_(e,c in t) c product_(i=0..3) v_(i+1)^e_i.

Proof: the inner loop invariant is the coefficient times the product over processed indices; the outer invariant is the sum of processed records. The empty list is zero. Fraction conversion gives the stated integer coefficient. `power` has its ordinary binary-power invariant accumulator times current-base^remaining-exponent = original-base^original-exponent; the zero exponent returns 1. No exponent used by the model is negative. `matrix(a,den)` computes D(a_rc)/D(den), with the denominator inverted once. This is an interpretation theorem conditional on exact scalar arithmetic; it does not validate the field implementation.

The inspected model metadata has six charts, rectangular shapes gamma 15x5, delta 10x15, ev 2x10, I 15x2, P 2x15, H0 5x15, H1 15x10. Every literal polynomial record has four nonnegative integer exponents, nonzero integer coefficients and no repeated exponent key. Each denominator di, dp, dh is nonempty. Thus these are nonzero formal polynomials without multiplying or evaluating them. The decoder maps I/di, P/dp, H0/dh, H1/dh exactly. This does not mean denominators are nonvanishing at all points: their invertibility is a localization condition.

The `_build_body` descending update computes the elementary symmetric functions v0=1 and vj=e_j(x1,...,x4): after processing r variables it gives the coefficients of product_(i<=r)(1+x_i z). Descending order prevents overwriting an old coefficient before it is used. Algebraic independence of the elementary symmetric functions over Q means a nonzero polynomial in v1,...,v4 stays nonzero as a rational function after this substitution. This proves formal nonzero denominators, not legal-owner/chart membership or a physical execution admission.

The checker verifies the exact polynomial/matrix AST and literal shape/schema conditions. The earlier moving-frame bridge checks the full primitive AST; this checker additionally binds its denominator-key comprehension. The JS excerpt decodes exactly the same four stored fields with `evm`; equivalence of the JS jet arithmetic is outside this proof.

## 2. Literal ev and the pivot split

Static literal comparison, without evaluating entries, establishes

    ev = diag((v0,v1,v2,v3,v4),(v0,v1,v2,v3,v4)).

Here diag means the 2x10 block-row map, and v0=1 in the finite model. For pivot p and each h=0,1, put eta[:,h]=e_(5h+p)/v_p. W has columns e_(5h+r)-(v_r/v_p)e_(5h+p), r=(p+k) mod 5, k=1,...,4; L selects those same nonpivot coordinates in that order. Assuming v_p is invertible, direct coordinate inspection proves

    L W = Id8, ev W = 0, L eta = 0, ev eta = Id2,
    W L + eta ev = Id10.

This closes the earlier bridge's ev-denotation premise. Define J=W L=Id10-eta ev. In particular every vector z decomposes uniquely into W L z + eta ev z. No relation involving gamma or delta is used here.

## 3. Three sufficient, family-irredundant identities

For each carrier assume exactly

    A: gamma H0 + I P + H1 delta = Id15,
    B: H1 eta = 0,
    C: ev delta = 0.

Set U=(gamma,I,H1 W), Q=(H0;P;L delta). Then

    U Q = gamma H0 + I P + H1 W L delta
        = gamma H0 + I P + H1 delta - H1 eta ev delta
        = Id15.

Only A and B were needed in that calculation. Since U and Q are square over a commutative field, the determinant/adjugate theorem gives Q U=Id15. This implication is an actual mathematical step, not an extra contraction assumption. It is valid over a commutative ring as well when the displayed inverse is a ring matrix.

The checker imports the following QU block consequences after this prose argument. Its formal reducer is a consistency control, not a mechanized determinant/adjugate proof. Reading the nine blocks gives

    H0 gamma=Id5, H0 I=0, H0 H1 W=0,
    P gamma=0, P I=Id2, P H1 W=0,
    L delta gamma=0, L delta I=0, L delta H1 W=Id8.

B and the target decomposition give H1=H1 W L. Hence H0 H1=0 and P H1=0. C and the same decomposition give delta=W L delta. Hence delta gamma=0 and delta I=0. Finally

    delta H1 = W (L delta H1 W) L = W L = Id10-eta ev.

Together with A, B and the split equations, these are every contraction premise of the prior moving-frame proof, plus delta gamma=0 and ev delta=0. In particular the resulting constant differential is genuinely a complex. No rank guess, determinant-one transition, derivative computation, or first-order residual identity was needed.

### Why C must not be silently omitted

The first-order specification lists contraction equations but does not explicitly display ev delta=0 or delta gamma=0 in that list. The historical homogeneous checker likewise tests its listed contraction equations but does not separately test either complex identity. Even all its displayed contractions can hold when delta gamma is nonzero in the eta direction. C therefore records a base-complex premise not established by reading that checker. This is a statement about that exact pinned file and displayed list only; it does not claim the project or other geometric proofs lack a proof of the complex identities.

### Independence and exact meaning of “smallest”

Use invented dimensions (1,3,2,1), gamma=e1, I=e2, P=e2^t, H0=e1^t, H1=(e3,0), delta rows (e3^t,0), ev=(0,1), eta=(0,1)^t. W=(1,0)^t and L=(1,0). This satisfies A,B,C and the pivot split.

- Replace H0 by zero: B,C hold and A fails.
- Replace H1 by (e3,e1): A,C hold and B fails.
- Replace delta's second row by e1^t: A,B hold and C fails; delta gamma=eta is nonzero.

These three tiny controls show no family can be discarded from THIS three-family sufficient system on shape/splitting grounds alone. They embed into the physical ranks by adjoining canonical paired and cohomology summands. They are invented countermodels, not model samples or numerical evidence about the physical matrices.

“Fewest scalar polynomial generators” has no claim here: equations may be grouped into one block equation, actual coefficient specializations may introduce dependencies, and proving ideal-minimality would require additional algebra outside the authorized scope. The result is a three-family irredundant presentation of the remaining checks, not universal scalar minimality.

## 4. Exact remaining polynomial checks, unevaluated

Write stored numerators N_I,N_P,N_0,N_1 and denominators d_i,d_p,d_h, so I=N_I/d_i, P=N_P/d_p, H0=N_0/d_h, H1=N_1/d_h. Let E_p be the 10x2 pivot selector with unit entries at (5h+p,h), so eta=E_p/v_p. Gamma, delta and ev have polynomial entries in the stored model. On the stated localization A,B,C are equivalent to the following polynomial matrix identities:

    A_pol: d_i d_p gamma N_0 + d_h N_I N_P
           + d_i d_p N_1 delta - d_h d_i d_p Id15 = 0,
    B_pol: N_1 E_p = 0,
    C_pol: ev delta = 0.

A_pol has 225 scalar entries per carrier. B_pol has 30 entries per carrier and is just the two selected columns of N_1, so its literal-zero case can be checked without multiplication. C_pol has 30 entries and is common to all carriers. The report deliberately does not expand A_pol or C_pol. It does not count their scalar entries as algebraically independent.

Remaining exact obligations are therefore: authenticate/prove A_pol on each of six stored carriers, authenticate/prove C_pol for the pinned differential, and B_pol if its literal-zero metadata control fails. The supplied checker DOES verify B_pol by inspecting the selected numerator lists are empty; it does not construct H1. Consequently the remaining nontrivial polynomial identity families in this pinned dataset are A_pol (six instances) and C_pol (one instance). The general three-premise theorem and independence controls explain why these are sufficient without claiming the two unevaluated families have been proved.

The historical checker is evidence of the intended tests and formulas, not a newly reproduced certificate: it uses SymPy cancellation of actual products to test A and B and the other listed contractions, and refuses optimized Python. It also uses homogeneous weights and v0 padding. Its previous claimed success is not promoted to a new independent proof here. The present checker uses explicit exceptions and remains active under -O. Finite decoding and homogeneous lift equivalence remain distinct; homogeneous correspondence is imported from the separately reviewed physical-frame bridge, not derived from a finite identity alone.

Other ID0 obligations (exact field implementation, legal localization, transitions/determinants, higher residual terms, HPL, transports, resources and aggregate admission) are unchanged. Neither this theorem nor a zero literal column gives an ID0 value or permission to run the held source.

## Reproduction

Run `python check.py` and `python -O check.py` in this directory. Both are safe static/formal checks and their logs are retained. The historical checker under inputs/ is only inert evidence. A PASS means the source/decoder/schema checks, literal ev and B_pol checks, formal consequences and tiny independence controls passed; it does NOT mean A_pol or C_pol passed.

Inputs may be supplied with --source-root or individual path overrides, as described in README.md. Every override remains subject to immutable hash verification before inspection.
