# One fixed Omega specialization — preparation for independent review

**PREPARATION ONLY. No physical execution authority.** Both public `actual` and
private physical-body/child paths refuse before source reads or arithmetic.
There is no release flag, worker, scan, residue schedule, detector, owner
enumeration, historical replay, or old polynomial-store dependency. This is one
normal-paced preparation task; the spike remains closed.

The immutable selection in `spec.json`, published at `4f6fceab9ddddd2c680ad2d9e2193d1e0848c291`, is

- physical vertices `(carrier,legal_mask) = ((0,0),(1,5),(2,10))`, in that order;
- all-finite original physical frame, rational base point
  `x*=(2,13/6,7/3,5/2)`; **no substitute point or adaptive retry**;
- legal bit `i` is exactly `(mask >> i) & 1` and means coordinate `x_i`,
  zero-based (low bit first): mask5
  selects axes0,2, mask10 axes1,3. These are physical labels, not outer owners.
- four cross slots `(02,03,12,13)` (one-based13,14,23,24), signs`(+,-,-,+)`.

## Exact source binding and target

`source-pins.json` and `sources/` contain byte-identical public definitions,
including Git blobs, SHA256s and lengths. The canonical model is
`10810ee877fdaf291399198ad60d7dd0c316a42d:research/hm/null-operator-compiler/hm-pinned-model.json`,
SHA256`635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`.
The same commit's source-formulas.js is SHA256`c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94`.
The physical-source revision is`08b73637d4136f91606aad332c46cafd064417f8`.
The symmetry/second-jet/physical-frame notes are pinned at PR79`5c9705bfcf1cab76ae76885cc8efc56f558d64f2`.
`authenticate_sources` hashes every supplied byte and Git blob; script constants
also bind the selection and pin manifest. No source JavaScript is executed.

The source generator gives `K_ab=(P_a I_b)^t`, `g_ab=D_b K_ab D_a^-1`,
`D_a=diag(nu_a,nu_a^-1)`, `nu_a=product_(selected i)(y_i/x_i)`.
The model's I and P use their OWN `di`/`dp` denominators, without replacement
by a desired homogeneous expression. The single transpose and row order
`g_bc g_ab=g_ac` are retained. No H0/H1/raw scalar/source residual is evaluated.

Put `A=g_ab`, `B=g_bc`, `H_ij=A^-1 V_i V_j A`,
`J_ij=A^-1 B^-1 (V_i V_j B) A`. The target is ONLY

    Omega=([J02,H13]-[J03,H12]-[J12,H03]+[J13,H02])/8.

Trace parts commute. In basis`(h,e,f)` take columns
`((M00-M11)/2,M01,M10)`, form `C=J^t S H` with anti-diagonal entries`(+,-,-,+)`.
Then `8 Omega=(Cef-Cfe)h+2(Che-Ceh)e+2(Cfh-Chf)f`.
The script computes both formulas and requires exact agreement.
This is the second-jet bracket symbol, not the entire M0 or Rsharp.

## Derivations, moving frames and rational stripping

`V_i=y_i partial_x_i` means the **induced elliptic derivation**, with
`V_i(x_i)=y_i`, `V_i(y_i)=(3x_i^2-1)/2`, and other-axis generators fixed.
Equivalently `partial_x_i(y_i)=(3x_i^2-1)/(2y_i)` on this etale locus.
For DISTINCT i,j, `V_i V_j g=y_i y_j partial_i partial_j g`, where the
partials differentiate y inside each moving frame as well.

For the rational core define `Q_a,i=D_a^-1 partial_i D_a`, explicitly
`diag(lambda,-lambda)`, `lambda=mask_i*(x_i^2+1)/(2x_i*(x_i^2-1))`.
This is NOT the stripped old connection `gamma=mask_i/[x_i*(x_i^2-1)]`:
`lambda=gamma+mask_i/(2x_i)`. Old gamma belongs to other source connection
blocks and does not enter this transition-only Omega test. Neither replaces Q.
Define `T_i=K_i+Q_b,i K-K Q_a,i` and
`W_ij=partial_j T_i+Q_b,j T_i-T_i Q_a,j`.
For our distinct axes `partial_j Q_a,i=0`; the code retains both endpoint Qs
and all first/mixed K terms. Use
`Hbar=K_ab^-1 W_ab`, `Jbar=K_ab^-1 K_bc^-1 W_bc K_ab`.

The FIRST route propagates values, first derivatives and six distinct mixed
derivatives through elementary-symmetric substitution, all products and
quotients. This finite derivative algebra is exact for these orders; it does
not expand, truncate or discard source-polynomial coefficients.

The SECOND route differentiates sparse numerators/denominators in the four v
variables explicitly. It computes elementary derivatives independently by
subset formulas, then uses BOTH terms

    partial_ij p(e(x)) = sum_ab p_ab e_a,i e_b,j + sum_a p_a e_a,ij.

A separate four-component product/quotient rule supplies mixed derivatives.
It constructs direct frames from the unit germ

    f_a(x)=nu_a(x)/nu_a(x*)
          =product_selected [sqrt((x_i^3-x_i)/(x_i*^3-x_i*)) * x_i*/x_i].

Equivalently its square is a product of ratios `w(x)/w(x*)`,
`w=(x^2-1)/x`. Solve `f^2=s`, `f(x*)=1` EXACTLY through mixed order:
`f_i=s_i/2`, `f_j=s_j/2`, `f_ij=s_ij/2-s_i s_j/4`.
No numerical square root is used. Value-one normalization retains ALL these
jets; it never freezes a moving frame. Directly differentiate
`g_hat_ab=D_hat_b K_ab D_hat_a^-1` and compare normalized H/J to the first
route. Every core derivative is also compared between routes. The repeated
four component calculations use the SAME fixed point/triple throughout.

Generally `g_ab=D_b(x*) g_hat_ab D_a(x*)^-1`, so normalized second jets are
conjugated by the SAME constant D_a(x*). Our first mask0 gives D_a=I exactly.
Every paired commutator uses all four distinct axes once. Consequently

    Omega_physical(x*,y*)=(y0*y1*y2*y3) Omega_rational(x*).

The same nonzero scalar relates the physical and rational cross-Gram matrices.

## Admissibility without testing actual point values

On the closed rational box `2<=x_i<=5/2`, elementary values obey
`v0=1`, `8<=v1<=10`, `24<=v2<=75/2`, `32<=v3<=125/2`,
`16<=v4<=625/16`. The selected model denominator TEXT is statically checked:

- `d0=v1 v2 v3 v4-1>0`, since `8*24*32*16>1`;
- `d1=v1(v2 v3 v4-v1^4)>0`, since `24*32*16>10^4`;
- `d2=v2(v1 v3 v4-v2^4)<0`, since
  `10*(125/2)*(625/16)<24^4`.

Thus all six I/P input denominators and the selected primary factors
`v_c,F_c` are nonzero. Also `x_i!=0`, `x_i^2-1>=3` and
`c_i=x_i^3-x_i>=6`. The old-gamma and logarithmic-frame denominator factors
are nonzero. Future exact arithmetic records each x, x²-1, c and each di/dp
value and aborts on zero. PI=I, det(K)=1 and the row cocycle are checked in the
full retained derivative germ; directly framed determinant/cocycle germs are
checked too. All matrix inversions use 2x2 adjugate/determinant, with the
unit-determinant checks and scalar inversion guard, never a guessed pivot.
Frame-germ denominators at the point are units. No other source denominator
is inverted. A failed identity or derivative check is an INCONCLUSIVE failure.

Choose any algebraic y_i* with `(y_i*)^2=c_i`. All y_i* are nonzero, so this
rational BASE point lifts to the actual product of elliptic curves over an
algebraic extension. No rational y_i* is assumed. The exact unit germs above
are the etale lifts, valid for either sign. Multiplication by their nonzero
product preserves matrix nonzero. A nonzero rational Omega therefore refutes
the source-specific pointwise symmetry identity on this common open.
**It does not prove a nonzero detector, nontrivial cohomology class, or global
obstruction. Zero at this one point proves none of those or a global identity.**

## Refusal contract and output

`bounded_exact.Meter` counts checked rational constructions and arithmetic,
and numerator/denominator integer primitive operations (including Euclidean
normalization divisions). These are specified software counters, NOT native
bit-work, old polynomial-product units or an aggregate-ledger conversion.
The proposed child cutoffs are2,000,000 rational operations,20,000,000 integer
primitives,4096 numerator/denominator/intermediate bits,256MiB virtual address
space,15 CPU seconds and20 wall seconds. Conservative pre-operation integer
height checks can refuse even a canceling result; refusal is never zero.
A poisoned arithmetic context cannot resume. Literal exponents are capped64.
Inputs are capped128KiB/file; output64KiB. No arbitrary caller source or point
is accepted by the physical entry.

The supervisor has256MiB address-space and15 CPU seconds, allows ONE child,
and kills on wall timeout. The child forbids cooperative subprocess/network
creation and core dumps. Thus the proposed standalone envelope is at most
two simultaneous processes /512MiB combined ADDRESS SPACE /30 combined CPU
seconds, not a measured RAM or historical shared-budget claim. Parent/child
runtime and Python interpreter overhead require review; this is not a hostile
Python sandbox. The supplied arithmetic modules have no subprocess/network
paths. There is NO claim that actual-source calculation finishes under these
caps, and no cap or spent-accounting reset is granted.

`expected-output-schema.json` describes success/refusal records. A successful
future approved run must publish exact H/J, C, all three skews, Omega,
nonzero flag, denominator records, all check outcomes, source/selection hashes,
software counters and process outcome. No partial value is evidence. Any
exception, timeout, kill, cap, nonunit, changed input or disagreement is
INCONCLUSIVE. Physical entry currently returns HELD before launching a child.

Safe preparation replay: `python -B run_artificial_checks.py` runs13
artificial/static controls in each mode. `prepare_omega.py static` only hashes,
parses selected metadata and checks the interval-constant inequalities.
`prepare_omega.py artificial` uses a literal invented model at an invented
point, not the source catalog. The checked controls cover an omitted-Hessian
negative case, nonfrozen frames, old-gamma distinction, both derivative engines,
noncommuting Omega sign/factor, PI/determinant/cocycle, exact arithmetic,
height/count/process refusals, selection/source drift and early physical hold.
No independent reviewer acceptance is claimed for this preparation.

## Exact remaining obligations

Root must independently review the source/formula binding, admissible-open and
elliptic-lift argument, constant frame normalization, derivative engines and
Omega interpretation; and approve or reject the DISTINCT bounded validation
contract, including interpreter/parent-child overhead, counter conventions,
output retention and any applicable resource authority/accounting. Adequate
caps/completion have NOT been established. The physical guard would require a
separate reviewed change before execution; no preparatory flag authorizes it.
The older numerical hold and incomplete historical/aggregate replay are
unchanged. This preparation never supplies an actual Omega or obstruction
value. No workers are active or required.

Preparation failure preserved: `parent-limit-failure.json` records the initial
inherited-hard-limit refusal before any test child could run. Parent and child
now use matching hard limits; the larger combined ceiling is stated explicitly.
