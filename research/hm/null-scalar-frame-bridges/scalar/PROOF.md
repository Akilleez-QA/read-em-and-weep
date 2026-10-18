# Narrow raw-scalar implementation bridge

## Result and boundary

For legal inputs consisting of exactly four square blocks per endpoint and direction, the frozen `raw_scalar_formula` computes exactly the pinned unsymmetrized four-block endpoint/supertrace/gerbe polynomial. No coefficient, endpoint, weight, or sign mismatch was found. This discharges only the scalar-combination implementation sub-obligation, conditional on the supplied blocks and q having their stated denotations and on the exact field primitives.

This is not a proof of the complete physical model, scalar source exactness from first principles, mixed residual implementation, transport, HPL, aggregate admission, or ID0=0. No production module was imported; no physical model, owner, source, field, or jet was executed. The only executable algebra is an invented free trace-symbol polynomial ring interpreting the restricted AST. 

The package-level `pins.json` gives exact SHA-256 values and all available original commit/path URLs. The principal frozen raw-engine pin is `e93cf712f9da4926a8450cc870ed45a7bfc379ab`, SHA-256 `c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9`.

## Mathematical expression checked

For block index l=0,1,2,3 set

- ranks n=(5,15,10,2), weights k=(-1,1,3,5), signs e=(-1,1,-1,1);
- Ai=B_i,a, Bi=B_i,b, Aj=B_j,a, Bj=B_j,b;
- theta_a=qa/2 and theta_b=qb/2.

Then the expression is

s = sum_l e_l/4 [tr(Ai Bj)-tr(Bi Aj)]
  + sum_l e_l k_l/8 [qa tr(Bi)+qa tr(Bj)-qb tr(Ai)-qb tr(Aj)]
  - 15 qa qb/8.

The source `first-order-source.md` at `08b73637...`, §§2 and 4, gives
T_ij = -str(B_i wedge B_j + k theta_ij wedge (B_i+B_j))
and s = -(1/4) iOrd_pi T - (15/8) r.
Thus the plus 1/4 in the implementation is the product of these two minus signs, not a change of transgression convention. Both endpoint traces are necessary. This uses the pinned source's ordinary coefficient contraction and unsymmetrized endpoint formula, not a cyclic trace assertion on Cech cochains. In particular the rank-weight check is
sum_l e_l n_l k_l^2 = -5+15-90+50 = -30.
The -15/8 edge correction is the source's conversion to the ordered gerbe representative; it is not the 15/4 triangle gerbe coefficient.

The pinned JavaScript excerpt at `10810ee.../research/hm/null-operator-compiler/hm-pinned-source-formulas.js`, `globalBuild2.first`, states precisely this same expression, with `Ai.k` and `Ai.sign` populated by the displayed four-block list. Its SHA-256 matches raw-engine's declared source pin `c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94`. The BI denotation JSON supplies an independently readable identical expression; equality is established by the expanded formula, not inferred solely from hashes.

## Exact Python lowering

`raw_engine.py:76–83` is the checked function. Expanding the two starred endpoint tuples in `zip` produces rows `(k,e,Ai,Bi,Aj,Bj)` in that order. Lines 80–83 give exactly the displayed polynomial. `Mat.mul` at 55–62 computes ordered matrix multiplication and `Mat.trace` at 65 computes its diagonal sum. Therefore `trace(mul(A,B))[0][0] = sum_rs A_rs B_sr`, exactly JavaScript `mtraceProduct(A,B)`. The 1x1 wrapper is unwrapped once. All rational factors use `Fraction`; no floating-point approximation is introduced here.

The caller `PhysicalModel.s_raw` at 157–159 passes `(blocks(i,a),blocks(i,b))`, `(blocks(j,a),blocks(j,b))` and q in precisely that order. `blocks` at 153–155 returns four blocks of the stated ranks. The generic function itself does not validate arity: malformed short tuples would silently truncate `zip`. This is a precondition of the narrow theorem, not a mismatch on the concrete four-block caller. The matrices must also have the legal square shapes; the scalar helper is not a general input-validation boundary.

## Physical-frame and mixed-derivative bridge, with explicit premises

Read-only inspection of `blocks` shows `U0=(gamma,I,H1 W)`, `Q0=(H0;P;L delta)`, `U1=(W,eta)`, `Q1=(L;ev)`, and column weights
w0=(nu^-2 I5,1,nu^-2,nu^2 I8), w1=(I8,nu^2 I2).
Rows of Q receive reciprocal weights *before* `D(U,d) Q` is multiplied. The result is negated, and the k gamma identity term is subtracted. The extreme blocks are zero before that subtraction. This is the correct literal placement of the moving-frame derivative; it is not differentiation of a constant normalized nu.

Let U,Q denote the unweighted rational-x matrices, W a diagonal matrix of invertible scalar weights, and D any derivation. Independently of UQ=1,

-D(UW) W^-1 Q = -(DU)Q - U diag(Dw_j/w_j)Q.

This identity follows by Leibniz and W W^-1=1. It shows why the value of a constant frame normalization cancels, while its logarithmic derivative remains. It does not independently prove that the supplied Q is the geometric inverse of U; that is a pinned primitive/model premise.

On the finite curve y_i^2=x_i^3-x_i, define V_i x_j=delta_ij y_i and V_i y_j=delta_ij(3x_i^2-1)/2. These formulas preserve the curve relation, since
V_i(y_i^2-x_i^3+x_i)=2y_i(3x_i^2-1)/2-(3x_i^2-1)y_i=0.
Consequently they extend as derivations to the relevant localization. Derivations for different factors commute. For nu=product_i (y_i/x_i)^m_i, quotient differentiation gives

V_i nu/nu = m_i y_i (x_i^2+1)/(2x_i(x_i^2-1)).

That is y_i times the source's rf, whereas the separately coded q is `(m_j,i-m_i,i)y_i/x_i` and the connection coefficient is `m_i y_i/[x_i(x_i^2-1)]`. Confusing these three quantities would be a defect; the inspected code keeps them distinct.

After cancellation of W values in the displayed moving-frame identity, every block coefficient in direction a is y_a times a rational-x expression Bhat_a. Likewise qa=y_a qhat_a. For a != b the checked scalar identity is therefore

s_physical(a,b) = y_a y_b s_stripped(a,b).

For a complementary direction c not in {a,b},
V_c s_physical = y_a y_b y_c partial_c s_stripped.
For distinct complementary c,d, a second derivative similarly yields
V_d V_c s_physical = y_a y_b y_c y_d partial_d partial_c s_stripped.
No factorial occurs for distinct-axis jets. Crucially, this conclusion does not apply to repeated directions: those require V_a(y_a) terms. The exact field representation's `Element.V` at 426–442 explicitly includes those terms by differentiating rational coefficients and adding `(3x_i^2-1)/2` when the basis mask contains i. Its `jet` applies V in sequence without discarding directions. Correctness of the underlying rational partial/arithmetic implementation is still an imported premise, not an audit performed here.

The frozen Source.E at 214–219 differentiates its scalar T only along the pair p; residual at 230–231 invokes E(p,q) and E(q,p) with p=(0,1), q=(2,3). `RawSource.T` delegates to s_raw and `Mat.D` at 72 differentiates each resulting exact element. Thus the complementary-direction hypothesis holds at these scalar E calls by source inspection. Differentiating the rational scalar polynomial propagates through *both* endpoints and all four blocks by Leibniz; there is no frozen scalar-jet lookup in this path. This does not prove all other residual mixed jets or all downstream differentiated values.

## Reproduction and strength of checker

Run:

    python scalar/check.py --source-root SOURCE_ROOT

The checker first verifies all six file hashes in `pins.json`, reads raw-engine with `ast.parse`, and interprets only the scalar function's restricted expression/loop AST in a newly invented formal ring. No `exec`, `eval`, importlib, production import, or physical constructor is used. It compares with a separately written, fully expanded 25-monomial mathematical formula. Six semantic coefficient/endpoint mutations are rejected. An additional reversed-word mutation is rejected in the stricter ordered-trace-symbol representation; that last check is only source-word preservation, since ordinary matrix trace does permit cyclic rotation. It must not be advertised as a numerical counterexample to tr(AB)=tr(BA).

The checker does not parse or execute JavaScript or mechanically verify prose. The source-to-formula comparison and conditional differential argument above are the mathematical review; hashes preserve precisely the inputs reviewed. Normal and optimized passing runs are recorded in the package `logs/` directory. This is a bounded implementation bridge suitable to cite for ID0's scalar-combination sub-obligation, not a closure of ID0 or authorization to run it.

## Portable checker note

The packaged checker uses explicit runtime checks rather than removable Python assertions. Its normal and `python -O` runs enforce the same controls. Source locations are supplied by command-line arguments; `pins.json` is read-only and preserved. The checker writes only its JSON report to standard output.
