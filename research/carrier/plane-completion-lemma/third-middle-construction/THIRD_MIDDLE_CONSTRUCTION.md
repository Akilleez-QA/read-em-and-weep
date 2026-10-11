# Complete third-middle construction on the fixed completed plane

## Result and scope

The full third-middle cochain is constructed over Q[a,b,c,d,lambda] in the specified gauge. All 40 possible parameter coefficients are exported: the 35 monomials of total degree at most three in a,b,c,d and lambda times 1,a,b,c,d. There are 13,547 quadratic-tensor terms in the finite, infinity and mixed primitives, with 28 nonzero parameter coefficients. Including relation primitives gives 19,375 terms.

This supplies the middle-bundle transition logarithm through h³ on the previously constructed symplectic completion. It does not yet supply an order-three section, identify an ancestor, or establish a carrier or defect conclusion.

## Inputs and gauge

All repository inputs are pinned to commit `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb` of `Akilleez-QA/read-em-and-weep`, under `research/carrier/formal-five-parameter-chart/`:

- `data/first_jet.json`: literal first-order tensors eta.
- `audit_original_cover/certificate.json`: literal `original_cover_primitive` second-order tensors kappa, plus lambda z^-1 E0² in the mixed component.
- `data/order_3.json`: complete source and target labels and the supplied relation-map entries.
- `audit_original_cover/check_original_cover.py`: retained verbatim as `pinned_contraction.py`; its geometric relation, transport, ordered Laurent Čech homotopy, and exact primitive construction are used.

The chosen gauge is the unique inverse preimage in the regenerated prescribed 9×9 D3 block, followed by the pinned ordered homotopy. No free higher-order gauge adjustment is added. D3 is regenerated from the line relation, compared entrywise with the supplied block, and inverted over Q. Its determinant is 1. This is a finite construction on explicitly checked right-hand sides, not an inference from matrix rank.

## Cubic equations and direction conventions

Use j-to-i transitions

    g_ij(h) = exp(-h A_eta_ij - h² A_kappa_ij - h³ A_nu_ij) g_ij(0).

The tensor bracket is the pinned Poisson bracket. The dictionary rho=-A is anti-Lie, so vector composition corresponds to reversed tensor BCH. Write [u,v] for the tensor bracket and N(u,v)=[u,[u,v]]+[v,[v,u]]. On either plane chart, the raw third-order right-hand side is

    delta nu = 1/2([eta01,kappa12]+[kappa01,eta12]) - 1/12 N(eta01,eta12).

For a mixed edge ij, put F=etaF_ij, I=T etaI_ij, hi=etaH_i, hj=etaH_j, and KF,KI,ki,kj for the corresponding second-order tensors. The raw mixed right-hand side is

    T nuI - nuF - delta nuH
      = 1/2([hi,KI]+[ki,I]-[F,kj]-[KF,hj])
        + 1/12(N(hj,F)-N(I,hi)).

This follows from BCH(Hj,F)=BCH(TI,Hi). Both orders of the eta–kappa product and both nested-bracket terms are retained. Lambda enters through kappa only at this order.

## Exact construction

For each parameter coefficient, form the raw finite/infinity/mixed tensors q0,qi,qh. Their total defect T qi-q0-delta qh is divided by the actual line relation alpha, with exact reconstruction. Split its projected relation quotient between the two base charts, then use the ordered plane homotopy to obtain a closed W-valued total cocycle.

Project its finite representative to plane H², reduce to the supplied target coordinates, and solve with the regenerated D3 inverse. Subtract alpha times the resulting compatible source representative. Both plane projections now vanish. The ordered homotopy produces finite and infinity primitives; a final homotopy produces the mixed primitive.

The exported relation primitives witness the RAW equations, including the original uncorrected cubic tensors. Every coefficient is rational, every denominator is a permitted geometric-coordinate monomial, and there is no division by a deformation parameter. This construction includes coefficients whose obstruction projection or entire primitive is zero.

## Verification

`construct_third_middle.py` uses the pinned eight-variable polynomial-Hamiltonian contraction. Its exact primitive routine reconstructs the raw finite/infinity/mixed equations and verifies grading and regularity. The driver records 163 named checks in addition to the contraction's internal exact checks.

`verify_third_middle.py` does not import the generator or contraction. It uses separate symmetric-slot tensor arithmetic and geometric transition formulas in `tensor_slot_support.py`, independently rebuilds all cubic right-hand sides, compares them with the exported raw tensors, and checks all primitive equations modulo the actual relation. It checks every W term's degree, character, base regularity and plane poles. All five lambda coefficients agree exactly with the previously supplied partial lambda slice. A deliberate change to the actual origin finite01 primitive by X^-1 Y^-1 W E0² is rejected with exactly that nonzero quotient residual.

The separate verifier passes 2,253 exact checks. Generator and verifier both run normally and under Python -O; final byte-comparison results are recorded in the accompanying run receipt. SymPy is used only by the generator's exact rational finite matrix solver. The separate verifier uses Python's standard-library Fraction arithmetic.

An independent review checked the universal cubic signs using truncated exponential/logarithm arithmetic in a free associative Q-algebra, inspected the implemented cubic formulas, and independently audited all 19,375 W/relation primitive terms. That review is separate from the raw-equation verifier described above.

## Output and next bounded step

`THIRD_MIDDLE_COCHAINS.json` contains all parameter exponents, original-cover primitives, relation witnesses, raw stages, target coordinates and inverse preimages. `THIRD_MIDDLE_CHECKS.json` and `THIRD_MIDDLE_INDEPENDENT_CHECKS.json` record checks and pins. `SHA256SUMS` freezes the package.

With these actual third-middle tensors available, the next bounded question is whether the section extends through h³ with its prescribed pairing, using all cubic exponential cross terms and the already fixed first- and second-order section gauges. That question is not answered by the middle construction alone.
