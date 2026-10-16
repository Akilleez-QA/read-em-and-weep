# Independent audit: scalar adjoint cover grammar and proposed new domain

## Outcome

No sign/order error was found in `transposed-scalar-demand-grammar.md` sections 1–6. The proposed conservative carrier54/legal29 outer domain also follows from a new ledger for the reduced representative, using the exact refinement and ownership construction below. The primitive-map premise has been checked directly against the pinned homogeneous-frame certificate, as detailed in section8. This is a formula-domain certificate, not a coefficient evaluation or an execution-cost certificate.

## 1. Exact finite-map checks

The standalone standard-library script `test_scalar_cover_adjoint.py` performed 150,453 successful checks:

- 120 standard edges: the AW cut chain equals the path changing coordinates 4,3,2,1.
- 120 edges: the rectangle-cone triangle chain has boundary edge minus that path.
- 120 edges: at most five nonzero triangles; five is attained.
- 150,000 pair12/pair34 edge-and-exponent cases: the stated raw path bounds 16/32 hold.
- 69 coefficient entries: the weighted prism identity δH+Hδ=1-r*Pi on a source-first ordered toy common refinement.
- 24 coefficient entries: the degree-two prism is exactly its displayed positive first branch and negative second branch.

Results are in `scalar-cover-adjoint-test-results.json`. Both scripts involved here reject Python -O/-OO before running assertions.

The exponent representatives -3,-2,-1,0,1 cover all distinct threshold/equality behaviors of h* and J* (the outer classes mean <=-3 and >=1). The tested unmerged path maxima over the deliberately enlarged formal request domain are 6 for pair12 and 12 for pair34. The bound test does not filter every suffix chart/exponent admissibility, so these are valid conservative upper bounds, not a claim that both are attained by admissible nonzero coefficient atoms. These stronger bounds concern finite map branching only; they do not bound multiplier support, polynomial products, or storage. They do not require changing the already safe 16/32 statements.

## 2. Why the cover formulas are correct

For an edge (e0,e1), the AW term active at d fixes coordinates before d at e0 and coordinates after d at e1. Its oriented edge therefore occurs in the reverse-coordinate path from e0 to e1, including every reversal sign. The degree-zero k is zero, so the rectangle-cone recurrence specializes to

    k[e0,e1]=[b,e0,e1]-sum_l[b,v_(l-1),v_l],

where b is the coordinatewise minimum. There are at most four path edges plus the original cone triangle. The two-coordinate diagonal control is -[00,01,11].

The q=2 prism recurrence has pivots0 and1, giving

    +sum rho0 f(b0,a0,a1)
    -sum rho0 rho1 f(b0,b1,a1).

All raw tuples are then alternated with their sorting sign. SOURCE-FIRST common ordering is particularly important for reading the nonlinear F via its fixed alternating pullback: do not re-evaluate its nonlinear formula on an arbitrary permutation. Repeated standard labels alone are not zero. Identical common vertices are zero, and a pullback specifically from F also vanishes if its physical source labels repeat.

The finite bound32 is four AW terms times four possible h pivots times two staircase paths; pair12 excludes pivots3,4, giving16. These are valid even without exploiting the additional mutually exclusive filters.

## 3. Scalar finite-frame and standard-boundary bounds

The previously authenticated N14 scalar finite-demand note gives input numerator degree at most217, quotient degree at most1677 in a finite coordinate and481 in an infinity coordinate, legal quotient/raw-weight degree at most2, and a finite-frame denominator shift at most73 per row. Its exact exponent equation therefore implies the conservative envelope

    -1668 <= e_i <= 5248,
    -1668=-3(481+2+73),  5248=217+3*1677.

This combines separate maxima, which only enlarges the bound. It does not assert simultaneous attainment or occupied support. K, S and h preserve exponents in the fixed finite frame. The tensor h's J-prefix only inserts constants or exponent -1, already within the envelope.

Changing to a pair-character standard infinity frame adds at most2 to a boundary pole, because the factor twist is0 or-2. Thus5250 is a safe chart-boundary pole envelope for the standard-cover part of the scalar solver. One local derivative raises the envelope by at most1, so5251 is safe after a complementary derivative. All physical frame and character conversions must remain explicit.

For a raw rho weight, the worst finite-coordinate degree is1677+70=1747 and its finite legal weight has degree0. An infinity-coordinate degree is bounded by481+70+2=553; the endpoint bounds are smaller. Thus1747 is a safe uniform raw-weight degree bound. One must not incorrectly append a further legal degree2 to the already maximal finite-coordinate case.

The H_rho branch has at most two such polynomial weights. Its inserted carrier/legal denominators are canceled by the prescribed weights. Its unchanged suffix retains carrier14/legal1; a derivative raises these safe bounds to15/legal2. The derivative also differentiates the weights, as required by Leibniz. No global commutation of derivatives with T is used.

## 4. New carrier ledger for the reduced representative

Write k=-K/2 and use the closed representative

    Rsharp=M(0)^0+F_p k_q,ik+F_q k_p,ik
                 +E_p(T_q F_q)+E_q(T_p F_p).

M(0) retains the three gerbe terms. Equivalently one may use the gerbe-free R_kin notation with coefficients -c instead of +F. The bounds below apply to either complete expression, without assuming cancellations between its summands.

The physical seed bounds give carrier orders g,g^-1<=4, k<=10, and u^k=gk<=14. Consequently:

- Normalized u^k u^k:4+14+14=32.
- Normalized μ(u^k,g):4+15+5=24.
- Normalized μ2(g,g):4+6+6=16.
- Gerbe terms have no larger bound.
- Fk:14+10=24.

For E use L_d=A^-1 V_d A and U_d=A^-1 B^-1(V_d B)A. The exact product derivative identity is

    U_d=(BA)^-1 V_d(BA)-A^-1 V_d A.

Therefore both currents have carrier bound9, not the unreduced17. The differentiated scalar H_rho branch has suffix bound15, so E has carrier bound24. The scalar standard-cover branch has only standard-boundary poles, with no carrier divisor, and hence is no worse in the carrier ledger.

Thus Rsharp has carrier bound32. Inclusion I(-)^t P adds4. Each undifferentiated End homotopy adds at most6. The four full-lift bounds are

    J0:36, J1:42, J2:48, J3:54.

This is a new ledger; it does not import the original source's62 bound or its four-tail feature representation.

## 5. Independent coarse legal ledger

The pinned local physical-frame estimates used in the original transport note are g,g^-1<=2 in legal order, k<=6, and u^k<=8. Thus M(0) has legal bound18, from2+8+8 in the normalized quadratic term. Its derivative and gerbe terms are no larger.

The new scalar H_rho branch has legal bound1, hence a conservative derivative bound2. The current identity above gives L,U legal bound5 (2+3), so its E term has bound7. The standard-cover scalar branch has no legal-divisor poles beyond standard boundaries; multiplying currents does not exceed the same envelope. Fk is bounded by1+6=7.

Consequently18 remains a valid coarse legal bound for Rsharp. Inclusion adds2 and each End homotopy adds3, giving

    J0:20, J1:23, J2:26, J3:29.

Carrier54 therefore also dominates this legal bound if one chooses a single powered partition parameter. Sharper legal partitions may be used only with their own explicit certificate.

## 6. Ownership and the essential refinement condition

The scalar solver lives on B=(standard label e, physical source label alpha). Its inner inserted vertices keep the standard label of the associated original vertex. The outer weighted projection must use the SAME r:B->U: on target tuple (e0,...,eq), its inserted vertices are (ei,alpha_i).

Under precisely this construction, every old standard-boundary denominator belongs to one of the target standard opens and is a unit on their intersection. It needs no additional outer carrier/legal weight. This statement would not be justified for a projection that forgets/replaces those standard labels or introduces an independent standard cover without a new compatibility proof.

Source-first sorting only permutes the common-vertex owners and contributes a sign; it does not transfer any denominator to an absent carrier or mask. Inner scalar inserted denominators are canceled locally; unchanged suffix denominators stay owned by original edge vertices. Currents involve only the original triangle endpoints. The inclusion and homotopy add their own prefix-vertex owners. Repeated physical carrier labels across different common vertices remain separately charged.

No physical source polynomial, residual, jet, sample, partition expansion, or obstruction coefficient was evaluated in this audit. A usable detector-demand compiler and cost/memory certificate are still separate obligations.

## 7. Audit of the proposed homogeneous outer envelope

A standard boundary owner with tag e_i=0 contributes the homogeneous divisor Y_i=0, while tag e_i=1 contributes X_i=0. Define B_(e,i)=Y_i or X_i respectively. Both have homogeneous degree1, and B_(e,i) dehomogenizes to1 in its owner's own standard chart. In the common finite trivialization, the infinity owner's X_i becomes x_i and the finite owner's Y_i becomes1.

For a J_s component, s=0,1,2,3, there are m=s+3 common vertices and internal degree r=-s. Clearing each actual occurrence with its own carrier54, legal29 and standard-boundary5251 factors gives a global homogeneous numerator with coordinate degree at most

    54*5*m +29*3*m +5251*m +(r-2)
      =5608*m-s-2.

At m=6,s=3 this is33643. This is an upper envelope, not a numerator construction. The regular extension follows because the stated factors clear every codimension-one pole of the rational section on the normal variety (P1)^4, including both standard boundary divisors when different owners require them. Factors on absent owners are not borrowed.

The retained5251 standard-boundary bound is stable under inclusion and End homotopies for a precise reason: the authenticated physical local I,P,H maps are regular sheaf maps on their carrier/legal opens, with the specified carrier/legal pole bounds in homogeneous local frames. They introduce no additional coordinate boundary pole except those already included in those divisors. Their bundle degree changes the final twist r-2 and hence the cleared numerator's degree. It is not an additional meromorphic standard-boundary factor. Cech restrictions only retain owners from the tuple. This reasoning would fail if one used affine-frame entries and then appended unaccounted transition ratios instead of the authenticated local homogeneous maps.

For the N54 outer carrier partition, M=107, threshold535 and L_s=(s+1)*534+1. The quotient bounds are independently checked:

- s=0: finite266;
- s=1: finite1335, infinity853;
- s=2: finite3472, infinity1387;
- s=3: finite6677, infinity1921;
- s=4: infinity266.

For the legal29 partition, M=57. The mask-zero infinity quotient has degree at most2M-29=85; the mask-one quotient has degree at most2M-2*29=56. Thus85 uniformly suffices. Finite-chart legal quotients have degree0 (mask one vanishes).

On the outer Pi term, the exact finite-frame exponent equation is the same homogeneous-denominator reversal rule as for the scalar solver. Each infinity-row shift now includes its carrier degree, legal degree, and its standard-boundary5251. This shift is at most5608. Its local quotient exponent is at most1921+85=2006. Therefore a conservative all-component exponent envelope is

    -45684 <= e_i <=73705,
    -45684=-6*(2006+5608),
    73705=33643+6*6677.

The twist is already included once in the cleared numerator degree5608m-s-2. Appending an additional frame exponent to this reversal equation would double count it. Actual component-specific and owner-specific bounds can be smaller.

These calculations establish a finite regular domain/envelope for the proposed full comparison, which uses the same r:B->U and the authenticated homogeneous local maps described above. They establish neither occupied support nor a practical product/storage bound.


## 8. Checked primitive-map premise under the source pullback

This premise is checked against `hm-full-sign-legal-line-bound.md` and `hm-regular-cover-transport.md`. The first note's section1 states the homogeneous primitive certificate entrywise: every bare I,P,H0,H1,eta,W,L entry belongs to the local coordinate ring with precisely its tuple's owned carrier factors inverted, for primary and auxiliary carriers. Section5 checks the local infinity frames explicitly and explains that the covariance tau^(r-2) is already implemented, with no extra tau pole appended. Section6 identifies the common-original-frame H and E=IP as carrier-only matrices, independent of the line mask.

The regular-cover note section6.1 supplies the conservative physical-frame charges used here: I/P/H carrier2 each, inclusion legal2, and End-homotopy legal3. Its domain argument shows that restrictions and the regular internal differential introduce no new divisor. Pullback along s:B->V is ordinary restriction to U_e intersect V_alpha. Restriction cannot add a divisor pole. Accordingly the same local primitive-map regularity and owned carrier/legal bounds hold on the new source-first common refinement. Neither sorting nor the extra standard label changes a primitive matrix.

This directly verifies the only potential source of an extra standard-boundary charge in the inclusion/homotopy stages. There is none. The retained5251 allowance therefore remains sufficient through J0,J1,J2,J3; the changing internal line degree is accounted for by r-2 in the cleared numerator, not by another transition factor. The stronger original full-source legal-one result is NOT imported for the new derivative-of-partition source; only the primitive facts and the explicitly recomputed coarse legal ledger are used.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
