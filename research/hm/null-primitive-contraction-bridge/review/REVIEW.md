# Independent review: three-identity contraction reduction

## Verdict

Accepted within the explicitly conditional scope. The stated pivot split and identities A, B, C imply all listed contraction identities and both complex identities. The denominator-clearing formula has the correct coefficient placements. The three invented countermodels establish family irredundancy for general matrices of these shapes, not scalar-generator minimality or independence after specialization to the pinned model.

The inspected checker passed in ordinary Python and optimized Python, with identical reports. This verifies static/literal and formal controls only; it is not a certificate for A_pol or C_pol.

## Algebraic verification

Write J = WL = 1 - eta ev. The pivot construction gives LW = 1, ev W = 0, L eta = 0, ev eta = 1 and WL + eta ev = 1 directly, provided the pivot coordinate is invertible. The cyclic ordering of nonpivot coordinates is immaterial as long as W and L use the same order.

For U = (gamma,I,H1 W) and Q = (H0;P;L delta), A and B give UQ = 1. These are square 15-by-15 matrices. Over a commutative field, and also a commutative unital ring, the determinant/adjugate argument gives QU = 1. Thus its nine blocks are exactly those displayed in PROOF.md.

B gives H1 = H1 WL. C gives delta = WL delta. Consequently the zero blocks yield H0 H1 = P H1 = delta gamma = delta I = 0, and the identity block yields delta H1 = W(L delta H1 W)L = WL = 1 - eta ev. The remaining contraction identities are the other blocks of QU or the given split equations. The second complex identity ev delta = 0 is premise C itself; it is not independently inferred from A and B.

The commutative coefficient hypothesis is substantive: a right inverse for arbitrary square matrices over an unrestricted noncommutative ring need not be a left inverse.

## Denominator clearing and literal metadata

Multiplying A - 1 by d_h d_i d_p gives

    d_i d_p gamma N_0 + d_h N_I N_P
    + d_i d_p N_1 delta - d_h d_i d_p Id15 = 0.

In particular, the gamma N_0 and N_1 delta coefficients are both d_i d_p; the N_I N_P coefficient is d_h. All signs and factors in A_pol are correct. This is an equivalence on the stated localization, not a claim at excluded denominator zeros.

Multiplying B by d_h v_p gives N_1 E_p = 0. The checker visits every H1 row and both pivot columns in each chart and demands that their stored numerator lists are literally empty. The rerun reports six checked charts. This proves B_pol for the pinned literal records without evaluating their polynomials.

The ev control checks every entry of the 2-by-10 matrix against the literal constant/coordinate polynomial in its own five-coordinate block and the empty list elsewhere. For k = 0 its generated key is (0,0,0,0), correctly representing v0 = 1 in the finite model. Thus it establishes precisely the finite ev denotation needed by the pivot proof. It does not by itself establish a homogeneous-lift correspondence.

C_pol = ev delta is correctly unchanged and shared across carriers. Its 30 scalar entries and A_pol's 225 scalar entries per carrier remain unevaluated.

## Independence controls

The tiny baseline has gamma = e1, I = e2, H0 = e1^t, P = e2^t, H1 = (e3,0), delta = (e3^t;0), ev = (0,1), eta = (0,1)^t, W = (1,0)^t and L = (1,0). It satisfies the split and A, B, C.

Setting H0 to zero breaks only A. Replacing H1's second column by e1 breaks only B. Replacing delta's second row by e1^t breaks only C and makes delta gamma = eta nonzero. The last modification also preserves every contraction explicitly listed in the historical checker, including delta H1 + eta ev = 1. Hence the listed contractions do not suffice to deduce the missing complex identities on shape grounds alone.

Direct sums with four additional gamma-paired coordinates, seven additional delta-paired coordinates, one cohomology coordinate and one ev-paired coordinate give ranks (5,15,10,2). Reordering coordinates gives the literal two-block split with v0 = 1 and other finite coordinates zero, pivot 0. This justifies the claimed embedding as a shape/splitting counterexample; it is not a specialization claim about the pinned coefficient matrices.

## Exact historical-source boundary

In the pinned inert file inputs/verify_homogeneous_identities.py.txt, lines 31–38 contain the per-carrier contraction checks. These include A, B, and delta H1 + eta ev = 1 but neither ev delta = 0 nor delta gamma = 0. Inspection of the rest of that file found no separate check of those two products. The first-order specification's displayed contraction list likewise omits those two equations.

This supports the narrow wording already used in PROOF.md: those equations are not separately tested by that historical checker or explicitly displayed in that list. It does not establish that the project, its geometric package, or another proof lacks them. Calling the underlying object a complex may itself import them as mathematical hypotheses; such imported evidence must be authenticated separately.

## Execution and evidence scope

check.py was read in full before either run. It imports only standard-library AST, hash, JSON and path utilities. Its model interaction is literal JSON/AST inspection and hashing. Its products are invented free words and tiny invented integer matrices. The historical SymPy checker was read as inert text and never executed or imported.

The original independent review retained identical ordinary and optimized rerun reports. Portable rerun reports are logs/normal.json and logs/optimized.json. Both say PASS, five pins, six charts, six literal-zero H1 pivot checks, and three independence controls. Their equality was verified. Explicit RuntimeError checks remain active under -O.

The checker inserts QU block rules after the corresponding prose theorem; its formal reducer is therefore a consistency/control check, not a replacement for the determinant/adjugate proof. It does not mechanically derive A_pol or evaluate A_pol/C_pol. No original file was changed, no production module or physical source was run, and no deliverable was published.
