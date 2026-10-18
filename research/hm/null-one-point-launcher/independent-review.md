# Independent review: one fixed Omega specialization preparation

## Status

Accepted as a dormant mathematical preparation at immutable PR90 head `779c1f7604db6fd48ce6e389b30a96f7aebef9f7`. Both derivative routes, source binding, the admissible-open argument, and target interpretation pass independent review. No mathematical correction is required for this preparation. This acceptance does not authorize actual execution, guarantee completion under any limit, or replace the separate resource review.

No physical CLI or physical child was launched, and no source specialization, owner enumeration, or source-jet arithmetic was run. The supplied refusal control invokes the held private body with source readers, arithmetic allocation, and evaluation patched to fail if reached; it confirms immediate refusal.

Selection was frozen at commit `4f6fceab9ddddd2c680ad2d9e2193d1e0848c291` in `Akilleez-QA/read-em-and-weep`. The selected triple is `(carrier, legal_mask) = ((0,0),(1,5),(2,10))`; the rational base point is `(2,13/6,7/3,5/2)` in the all-finite original frame. This review does not select alternatives.

## Source binding checked

All five files in the selection commit's `source-pins.json` match their declared byte lengths, SHA-256 digests, and Git blob SHA-1 digests independently. The original model and formula files were also read at their declared immutable upstream commit and returned the same Git blob IDs. This is a byte-level check, not model evaluation. The physical source revision is pinned as `08b73637d4136f91606aad332c46cafd064417f8`.

The public criterion proves that the correctly transported complete four-slot arrays satisfy `Omega=0` exactly when their traceless-component cross-Gram matrix `J^t S H` is symmetric. It does not assert that the actual source satisfies this condition.

## Mathematical requirements

1. **Curve derivations.** On `y_i^2=x_i^3-x_i`, the invariant derivation is `V_i(x_i)=y_i`, `V_i(y_i)=(3x_i^2-1)/2`. It is not ambient differentiation holding `y_i` fixed. Derivations for different coordinates commute.

2. **Exact rational reduction.** For distinct `a,b`, a physical matrix whose rational representation includes its full moving-frame jets satisfies `V_a V_b G = y_a y_b partial_a partial_b G`. Each of the four complementary products in Omega uses each coordinate once. Consequently `Omega=(y_0 y_1 y_2 y_3) omega`, with `omega` a rational 2 by 2 matrix at the normalized point. Work in any characteristic-zero field containing roots of `y_i^2=x_i^3-x_i`. Here `partial_i=V_i/y_i` is the induced curve derivation, so `partial_i(y_i)=(3x_i^2-1)/(2y_i)`; it is not an ambient derivative. Every selected `x_i` is greater than one, so every `y_i` is nonzero. The common factor is invertible, and zero/nonzero of Omega is equivalent to zero/nonzero of `omega`. No choice of square-root signs changes that conclusion. This argument applies to the displayed cross-coordinate target, not arbitrary repeated-coordinate derivatives.

3. **Moving frames.** For a bit-one finite line frame, `r_i=(x_i^2+1)/(2 x_i (x_i^2-1))=partial_i log(y_i/x_i)`. The normalization `nu(point)=1` sets a frame value, not its germ. With bit vector `m`, `partial_a nu=m_a r_a` and `partial_a partial_b nu=m_a m_b r_a r_b` for distinct coordinates, at the normalized point. Inverse-frame first jets have the opposite sign. Dropping these jets changes the target. Different constant vertex-frame normalizations change both normalized H and transported J by the same conjugation at the first vertex, preserving vanishing.

4. **Masks.** The pinned JavaScript consumes `mask[a]`; the specification supplies integers. The conversion must be explicitly `m_a=(mask >> a)&1`, with zero-based coordinates. Thus mask 5 is `(1,0,1,0)` and mask 10 is `(0,1,0,1)`.

5. **Physical row transitions and transport.** Put `K_ab=(P_a I_b)^t`, `D_a=diag(nu_a,nu_a^-1)`, and `g_ab=D_b K_ab D_a^-1`. With `A=g_01`, `B=g_12`, retain the row-composition convention `g_02=B A`. The required second jets are `H_ab=A^-1(V_a V_b A)` and `J_ab=A^-1 B^-1(V_a V_b B) A`. J must not be left in the intermediate vertex's frame. Transposes, endpoint frame powers, and multiplication order must match these formulas.

6. **Full elementary-symmetric Hessian.** The map is `v_k=e_k(x_0,x_1,x_2,x_3)` with `v_0=1`. For distinct coordinates, `partial_a v_k=e_(k-1)(x excluding a)` and `partial_a partial_b v_k=e_(k-2)(x excluding a,b)`. The chain rule for a source function F contains both the Hessian-of-F term and `sum_k F_k partial_a partial_b v_k`. Omitting the latter evaluates a different source. A correctly implemented square-free jet pullback automatically retains both.

7. **Target and criterion.** The ordered slots are `(02,03,12,13)` and the signs are `(+,−,−,+)` pairing each slot with its complementary slot. Compute all entries of `([J02,H13]−[J03,H12]−[J12,H03]+[J13,H02])/8`. One selected entry is not a complete zero test for a traceless 2 by 2 matrix. The cross-Gram calculation provides a useful independent algebraic cross-check, with all three antisymmetric components retained.

8. **Admissibility.** Nonzero finite line denominators follow from the chosen x coordinates. The final PLAN additionally proves all selected primitive denominators nonzero throughout a rational box containing the fixed point, by exact interval inequalities and authenticated denominator definitions. No actual source denominator was evaluated at the point. A future released evaluator must check every required denominator exactly and refuse on zero. If using an adjugate as the inverse of a transition, determinant one must be checked or independently source-certified for that transition. A refused denominator, failed source identity, or exhausted resource cap is not zero.

## Meaning of a future result

A verified, admissible, exact nonzero Omega at this one point refutes the proposed identity `Omega=0`, equivalently the proposed pointwise cross-Gram symmetry on the actual source domain that contains this triple and point. It does not establish a nonzero detector value, nonzero complete raw obstruction, or nonzero cohomology class.

A zero result establishes only this one specialization. It does not prove any functional or global vanishing identity. No scan, alternative point, alternative triple, or post-result selection follows from this preparation.

## Final implementation review

Reviewed the immutable candidate's `PLAN.md`, `README.md`, `prepare_omega.py`, `bounded_exact.py`, `test_artificial.py`, `run_artificial_checks.py`, result schema, and receipts. All 20 files listed by `preparation-manifest.json` independently match their declared byte lengths and SHA-256 digests. The selection and public-source manifest are also bound by literal SHA-256 constants in the dormant evaluator. Source formulas are read as authenticated text, not executed.

The first derivative route uses the exact square-free degree-at-most-two algebra with value, four first derivatives, and six distinct mixed derivatives. Its subset-convolution product is correct; its geometric-series inverse is exact in this quotient. Coefficients of distinct square-free monomials equal the mixed derivatives without factorials. Descending elementary-symmetric recurrence followed by sparse polynomial evaluation preserves the complete chain rule.

The second route differentiates sparse source numerators and denominators in the four elementary variables explicitly. It computes the elementary values and both derivative orders from a separate subset formula, sums the full ordered Hessian contraction, and includes the gradient times elementary-Hessian term. Its four-component product, quotient, and unit-square-root formulas are correct. Direct frame differentiation is independently based on the germ of `nu^2=product((x_i^2-1)/x_i)` rather than the first route's logarithmic Q formula. The normalized mixed jets agree route by route before Omega is formed.

The core is exactly `(P_a I_b)^t`, retaining each primitive's own denominator. The code checks `P_c I_c=I`, determinant one, and row composition on the entire retained derivative germ, and checks determinant and composition again after direct moving-frame insertion. The covariant route includes both endpoint Q factors with their correct signs and order. The second edge is conjugated into the first vertex's frame before comparison. All four selected cross slots, all four commutator signs, and the factor `1/8` are correct. The cross-Gram route reconstructs both off-diagonal entries as well as the diagonal entry of Omega from all three skews.

### Static admissible-open certificate

The fixed point lies in `2 <= x_i <= 5/2`. On this box the elementary coordinates satisfy `8<=v1<=10`, `24<=v2<=75/2`, `32<=v3<=125/2`, and `16<=v4<=625/16`. The authenticated selected denominator definitions are:

- `d0=v1 v2 v3 v4-1`, positive since `8*24*32*16>1`.
- `d1=v1(v2 v3 v4-v1^4)`, positive since `24*32*16>10^4`.
- `d2=v2(v1 v3 v4-v2^4)`, negative since `10*(125/2)*(625/16)<24^4`.

Both I and P use the corresponding denominator for each selected carrier. These inequalities establish a common legal primary open without evaluating the actual model or any actual point denominator. The line factors and curve right-hand sides are nonzero throughout the box. Hence the chosen base point admits the required elliptic lift over an algebraic extension. The future evaluator still retains exact nonunit checks, so no analytic inference substitutes for an arithmetic guard.

### Independently replayed safe evidence

After reading the test code and confirming its invented-model/static-only scope, the 13 supplied controls passed in normal isolated Python and with `-O` (26 tests total). Their complete logs are `independent-normal.log` and `independent-optimized.log`. The artificial pipeline uses its own literal invented model and its own point; the actual catalog is never supplied to the kernel.

A separate `test_independent_symbol.py` compares the prepared Omega implementation against independent Fraction matrix multiplication on all 144 pairs of single-slot `sl2` basis inputs. It checks all components and equivalence to simultaneous vanishing of the three skews. All 144 pairs passed in each mode. This exhausts the basis pairs of the bilinear symbol, not any family of actual source values. Receipts are `independent-symbol-normal.json` and `independent-symbol-optimized.json`.

### Release boundary and output convention

The physical CLI, private child route, and private body are hard held. Read the separate `resource_review.md` for the independent runtime verdict and its five requirements for any later reviewed release: executable-byte binding, a supervised physical path, truthful partial-evaluation provenance, complete inconclusive failure handling, and an explicit emitted/retained/captured output contract. The present acceptance is of dormant preparation only.

One additional output-clarity requirement applies to a future result: the keys `H` and `J` currently return rational **stripped** jets. Label that normalization explicitly. For slot `(a,b)`, physical `H_ab=y_a y_b H_ab(returned)` and physical `J_ab=y_a y_b J_ab(returned)` in this fixed first frame. Physical Gram and Omega each equal their returned rational version times `y0 y1 y2 y3`. The first vertex has mask zero, so there is no additional constant first-frame conjugation here. This does not change the kernel or its zero test; it prevents rational arrays from being mistaken for unstripped physical values.

No actual Omega value has been produced. Completion within the proposed limits is unproved. The proposed per-attempt ceilings are separate bounded-attempt limits; nothing here resets, extends, or claims consumption from a prior residue-replay budget.
