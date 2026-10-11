# Independent original-cover obstruction rebuild

## Result

All 15 coefficients of the affine quadratic order-two obstruction were recomputed directly from the complete frozen first Čech cochains. The resulting 16-vector and its 15-vector polynomial preimage agree exactly with the shipped witness. No numerical sampling, producer import, stored quadratic evaluation, or boolean certification flag is used to obtain the result.

The c/d directions disappear only after the appropriate relation and Čech reductions. Their mixed cochains must not be dropped:

| Coefficient | Nonzero raw mixed-BCH terms | Reduced target | Explanation |
|---|---:|---|---|
| c, d | 84 each | zero | Nonzero finite relation primitives; exact projected cancellation |
| ac, ad | 43 each | zero | Nonzero mixed relation correction, then an explicit Čech primitive |
| bc, bd | 41 each | zero | Nonzero mixed relation correction, then an explicit Čech primitive |
| c², cd, d² | 0 | zero | Literally zero in the raw BCH expression |

All constant, linear, and quadratic coefficients, including ab, have exported original-cover primitives modulo the relation. The nonzero reduced coefficients are 1, a, b, a², and b². The matrix preimage is zero for the other ten coefficients; the corresponding Čech primitives need not be zero.

The λ-dependent order-three difference is also checked directly. For κ₂=z⁻¹E₀², the polarized BCH term involving η₁ and λκ₂ has nonzero raw mixed cochains in its 1, a, b coefficients. Each nevertheless reduces to the zero 9-vector in the supplied complete prescribed D₃ target. The certificate exports D₃, its inverse, all five target/preimage vectors, and actual relation/Čech primitives. The c and d coefficients of this bracket are literally zero. This bounded check is not a construction of the entire third jet.

## Replay

Place this directory at `audit_original_cover/` inside the existing PR61 package, leaving its existing files unchanged. From that package root run:

```sh
python audit_original_cover/check_original_cover.py --package . --verify-certificate audit_original_cover/certificate.json
python -O audit_original_cover/check_original_cover.py --package . --verify-certificate audit_original_cover/certificate.json
python -m unittest discover -s audit_original_cover -p 'test_*.py' -v
(cd audit_original_cover && sha256sum -c SHA256SUMS)
```

The same command can run from any directory with an absolute `--package` path. Without `--verify-certificate`, `--output FILE` saves a fresh certificate. Python 3.10+ and the package's SymPy dependency suffice. All substantive checks use explicit exceptions and remain active under `python -O`.

## Input and independence boundary

The checker reads only:

- `data/first_jet.json`: all original-cover origin and a,b,c,d cochains
- `data/order_2.json` and `data/order_3.json`: complete source/target basis labels and maps for comparison
- `certificates/quadratic_certificate.json`: compared only after independently producing the full quadratic vector and preimage

The fixed plane gluing, alpha, alternating form, and coordinate convention are displayed directly in the new checker. Their geometric interpretation and the completeness of the supplied source/target labels remain inputs, as in the original PR61 boundary. The checker itself verifies alpha transport, the alternating-form transport, alpha's radical identity, first-cochain regularity, degrees, weights, and cocycle equations modulo alpha.

The selected D₂ and D₃ entries are rebuilt by multiplying the actual alpha into lifted source-basis representatives and reducing to target coordinates. They agree entry-for-entry with the corresponding supplied maps. Thus neither stored rank flags nor stored selected matrix entries are used to manufacture the obstruction.

## Arithmetic and exactness convention

Each sparse polynomial monomial has exponents `(z,X,Y,W,P,E0,E1,E2)`. The last four positions encode a Hamiltonian, so the bracket is formed independently by polynomial differentiation:

`{p,q} = grad(p)^T Ω grad(q)`.

The coefficient of each parameter monomial is extracted by summing its ordered pairs directly. For a first cochain `(eF,eI,h)` the quadratic BCH components are

- `qF = {eF01,eF12}/2`
- `qI = {eI01,eI12}/2`
- `qH_ij = ({h_i,T eI_ij} - {eF_ij,h_j})/2`

The mixed defect `T qI - qF - δ qH` is divided by alpha and every coefficient of the reconstructed product is checked. The base primitive and ordered plane homotopy give a genuinely closed W-valued representative. Only then is its plane-H² projection reduced to the D₂ target coordinates. Every operation after the brackets is rational-linear and parameter-independent.

For each coefficient the exported fields `original_cover_primitive` certify directly against the raw BCH cochains:

- `qF = δ pF + alpha_F uF`
- `qI = δ pI + alpha_I uI`
- `qH = T pI - pF - δ pH + alpha_F uH`

All these equations are verified coefficientwise. The p and u cochains are checked to be regular on their stated original-cover intersections and to have the correct plane degree and secondary character. Hence zero reduced target is accompanied by an actual original-cover exactness witness, rather than being inferred from a matrix rank alone.

## Why the linear c,d terms reduce to zero

With E₀ denoting the frame variable, the finite relation primitives are

- `vF(c) = 2 E0/(X Y W^4) + 2 z E0/(X^3 Y W^2)`
- `vF(d) = -2 E0/(X Y W^4) - 2 z E0/(X Y^3 W^2)`

Their finite BCH terms vanish, but the corrected finite W terms `-alpha vF` do not. Their plane-H² projections vanish by exact Laurent cancellation. This is compatible with nonzero c,d effects on the chosen second lift, and does not imply any all-order parameter redundancy or carrier invariance.

## λ and normal order

The λ direction is a closed correction in `h² κ₂`. It cannot enter the coefficient of h² in a bracket with `h η₁`; their first possible contribution is order h³. The checker computes exactly that polarized BCH variation, including its normalization. Its vanishing reduced class does not mean the varying third logarithm is zero: the exported nonzero Čech primitives are needed.

For an order-k W coefficient, the finite secondary character is `k-4 + d_i+d_j`, with d=(3,0,2,2), and its plane degree is `p_i+p_j+2-k`, with p=(-3,0,-4,-4). The infinity character uses offset k-8 and weights (3,6,0,2). Analogous U checks use one frame index and plane degree `p_i-4-k`. All raw/corrected λ bracket terms are checked with k=3, rather than relying only on the label “homogeneous.”

## Limits

No parameter-uniform algebraization, global reflexive carrier, hull base change, defect constancy, or zero-defect member is asserted. The fixed geometric model and completeness of its input basis lists are not rederived from a global rank-five presentation here. No high-order expansion is part of this audit.
