# Conditional moving-frame block implementation bridge

## Result and precise boundary

The frozen `PhysicalModel.blocks(o,d)` implements the pinned split-connection definition

    B_l(V_d) = -(V_d U_l^phys)(U_l^phys)^-1 - k_l alpha_o(V_d) Id,

in block order ranks `(5,15,10,2)` and line weights `(-1,1,3,5)`. The extreme split bases are identities. No indexing, column-weight, inverse-row, or sign defect was found. This closes the moving-frame *lowering* obligation conditional on the explicit coefficient-field, localization, matrix-shape, contraction, and primitive-denotation premises below. It does not certify those premises from the actual model entries, establish ID0, or authorize execution.

No production module was imported. No actual model matrix, physical source, owner, or jet was evaluated. Only source text, ASTs, invented noncommutative formal words, and integer index/exponent arithmetic were inspected/executed. This proof concerns source inspection and formal controls only.

The exact source pins and original URLs are in `pins.json`: frozen raw_engine.py at e93cf712f9da4926a8450cc870ed45a7bfc379ab; source-formulas JavaScript at 10810ee877fdaf291399198ad60d7dd0c316a42d; first-order-source.md at 08b73637d4136f91606aad332c46cafd064417f8. The latter §§1–2 is the mathematical specification. This result concerns these frozen bytes, not an unverified current working branch.

## Premises

Work over the localized commutative exact coefficient field with a derivation D=V_d. Assume the implemented scalar arithmetic, `power`, and entrywise `Mat.D` denote their usual operations. In particular D satisfies Leibniz, and the localization includes every denominator used. Let nu and the pivot coordinate v_p be invertible. Directions d and mask bits must be legal; carrier data must have the pinned denotation. Matrix operations must receive rectangular, correctly shaped matrices, with no malformed ragged rows.

Use gamma:15x5, delta:10x15, I:15x2, P:2x15, H0:5x15, H1:15x10, ev:2x10, W:10x8, L:8x10, eta:10x2. The name gamma here is the differential matrix; below alpha denotes the old line connection, avoiding the implementation's reused local variable name `gamma`.

A sufficient contraction system, as specified by first-order-source.md §1, is

    gamma H0 + I P + H1 delta = Id15,
    H0 gamma = Id5, P I = Id2, delta H1 = Id10 - eta ev,
    H0 I = H0 H1 = P gamma = P H1 = delta I = H1 eta = 0,
    L W = Id8, W L + eta ev = Id10, ev W = L eta = 0, ev eta = Id2.

The complex identity delta gamma=0 is used for the optional direct Q0U0 block calculation and constant-differential interpretation. It is not an extra premise needed for the minimal inverse argument: the first resolution identity, H1 eta=0, and W L + eta ev=Id already prove U0Q0=Id; a square right inverse over a commutative field is a two-sided inverse. Thus there is no hidden dependence on verifying delta gamma separately merely to conclude Q0=U0^-1. The `check.py` direct-left-inverse control declares delta gamma=0 explicitly.

These premises are mathematical identities, not numerical witnesses. This report does not promote hashes or prior prose to a fresh proof that the model entries satisfy them.

## Kernel basis indexing and shapes

For h=0,1 and k=1,...,4, the code sets r=(p+k) mod 5 and column c=4h+k-1. Then

    W[:,c] = e_(5h+r) - (v_r/v_p)e_(5h+p),
    L[c,:] = e_(5h+r)^t,
    eta[:,h] = e_(5h+p)/v_p.

All four nonpivot positions occur exactly once in each five-coordinate summand, for every p in 0,...,4. If ev is the two block-row evaluation map with coefficients (v0,...,v4), these definitions give the four W,L,eta,ev contraction equations above entrywise. That identification of ev is an explicit model-denotation premise; it is not inferred just from the variable's name. The checker verifies the exact primitive AST and all five combinatorial pivot-index cases, without assigning coordinate values.

Consequently `zip(gamma,I,H1 W)` concatenates three blocks with the same 15 rows and widths 5,2,8. U0 and Q0 are 15x15. U1=(W,eta) and Q1=(L;ev) are 10x10. On these shapes zip does not truncate. Malformed dimensions are outside the theorem.

## Inverses and split differentials

With unweighted frames

    U0=(gamma,I,H1 W), Q0=(H0;P;L delta),
    U1=(W,eta), Q1=(L;ev),

one obtains

    U0Q0 = gamma H0 + IP + H1 WL delta
          = gamma H0 + IP + H1 delta - H1 eta ev delta = Id15,
    U1Q1 = WL + eta ev = Id10.

The direct 3x3 Q0U0 block multiplication has diagonal blocks Id5, Id2, and L(delta H1)W=Id8; the off-diagonal blocks vanish by the displayed premises and delta gamma=0. Likewise Q1U1 has diagonal Id8,Id2 and zero off-diagonals. These formal word reductions are checked without actual matrix construction.

Define diagonal column weights

    S0=diag(nu^-2 Id5, 1, nu^-2, nu^2 Id8),
    S1=diag(Id8,nu^2 Id2).

Then U0phys=U0 S0, U1phys=U1 S1, with inverses S0^-1 Q0 and S1^-1 Q1. The two cohomology columns have DIFFERENT weights: first 1, second nu^-2. Replacing them with a common weight would change the connection.

For the scaled differentials nu^-2 gamma, nu^-2 delta, nu^-2 ev, the first is the first five columns of U0phys. The second sends the last eight columns of U0phys to the first eight columns W of U1phys and kills the other columns. The third sends the last two columns nu^2 eta of U1phys to Id2 and kills W. Thus the splitting differential is constant under these same premises, with extreme frames Id5 and Id2.

## Differentiation and exact block formulas

Lines 147–149 multiply columns of U by w[j], divide rows of Q by w[i], differentiate the weighted U, multiply in the order D(Uphys)Qphys, and negate. They do not differentiate Q and do not use Q D(U). For any diagonal S with invertible scalar entries,

    -D(US) S^-1 Q = -(DU)Q - U diag(Dw_j/w_j)Q.

This is a Leibniz identity, independent of UQ=Id. Invertibility is used only to identify Qphys as the geometric inverse. It follows that the resulting connection is flat in the split basis: D(Uphys)+[-D(Uphys)Qphys]Uphys=0. Subtracting the old connection gives B, rather than the split connection itself.

Write rho=D(nu)/nu and alpha=alpha_o(D). Let E22=diag(0,1) in the two cohomology coordinates. The literal output is

    rank 5,  k=-1: B_-1 = +alpha Id5;
    rank 15, k= 1: B_0 = -(DU0)Q0
                           +2rho gamma H0 +2rho I E22 P
                           -2rho H1 W L delta -alpha Id15;
    rank 10, k= 3: B_1 = -(DU1)Q1 -2rho eta ev -3alpha Id10;
    rank 2,  k= 5: B_2 = -5alpha Id2.

By H1 eta=0, H1WLdelta=H1delta, so the rank-15 formula admits that simplification. No derivative is omitted from DU0 or DU1: in particular D(H1W) and D(eta) retain their product/quotient contributions. The rank-5 plus sign is forced by subtracting k alpha with k=-1; the rank-2 term is not zero merely because its moving basis is the identity.

On the finite curve y_i²=x_i³-x_i, V_d x_i=delta_di y_i and V_d y_i=delta_di(3x_i²-1)/2. For mask m and nu=product_i(y_i/x_i)^m_i,

    rho = m_d y_d (x_d²+1)/(2x_d(x_d²-1)),
    alpha = m_d y_d/(x_d(x_d²-1)).

The former is the logarithmic derivative of nu, the latter the old connection from first-order-source.md §1. Their distinct numerators are essential. The code's line 151 equals alpha; it does not erroneously substitute rho. At infinity this statement refers to the same rational connection after authorized coordinate transport, not to a newly zero connection; this report does not audit that transport.

## Relation to the pinned JavaScript

The exact JS excerpt has the same unweighted U0,Q0,U1,Q1, the same column weights and reciprocal rows, the same negative derivative, and the same four (rank,k) choices. JS evaluates a normalized nu jet whose constant coefficient is 1, with logarithmic derivative rf=(x²+1)/(2x(x²-1)); raw_engine uses the actual physical nu and V_d. The displayed Leibniz identity proves independence from multiplying nu by a nonzero constant while retaining its logarithmic derivative. Since V_d=y_d partial_d on rational-x primitives, the Python block coefficient is y_d times the corresponding stripped JS first-direction coefficient. The old-connection coefficient similarly gains y_d. Equality of higher/repeated jets is not asserted here. This is the missing conditional moving-frame refinement of the earlier raw-scalar bridge, not an independent audit of JS jet arithmetic.

## Controls and reproducibility

Run `python frame/check.py --source-root SOURCE_ROOT`.

It verifies three pinned SHA-256s; compares the exact blocks, primitive, and nu ASTs against the reviewed contract; checks ranks and five pivot-index cases; checks 13 formal left-inverse subblocks plus two right-inverse expressions; and checks the Leibniz exponents for all 25 weighted columns. Eight static mutation controls reject wrong derivative sign, inverse scaling, cohomology column order, old-connection sign, extreme weight, middle-block order, and each of two matrix word orders. The package `logs/` directory records normal and optimized PASS runs.

The AST equality is an exact source-contract control, not an AST interpreter proving arbitrary program behavior. The mutation controls demonstrate static discrimination, not numerical counterexamples. The formal ring is noncommutative and applies only the declared equations; it never loads model data. The mathematical reasoning above supplies the semantic bridge. Remaining obligations include actual primitive contraction/denotation authentication, exact-field correctness, owner legality/localization, transport, other residual terms, HPL, and aggregate admission.

## Portable checker note

The packaged checker uses explicit runtime checks rather than removable Python assertions. Its normal and `python -O` runs enforce the same controls. Source locations are supplied by command-line arguments; `pins.json` is read-only and preserved. The checker writes only its JSON report to standard output.
