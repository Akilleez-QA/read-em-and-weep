# Independent audit: the two actual endpoint values

## Conclusion and scope

The established actual filtration/operator comparison promotes the fully trace-corrected homogeneous secondary calculations as follows, in the normalized lowest cocycle convention:

    a=z^2, h=X^4:   endpoint class = 0;
    a=z^2, h=XY^3:  endpoint class = (3k/(Bc)) [Y/z].

For the fixed actual normal generator these expressions are multiplied by its common, UNKNOWN NONZERO normalization c_eta. Thus the first actual P4 endpoint value is zero and the second is nonzero. The displayed nonzero scalar is a normalized coefficient, not an absolute numerical value for the actual normal generator.

This is an endpoint normal-variation result. It is not a fourth Bockstein evaluation, does not determine a full normal connection, and does not infer all representation channels from either input. In particular the two independent inputs must remain distinguished: their source identifications I_f(X^4) and I_f(XY^3) need not belong to the same test line.

## 1. Audit of the physical twists

The physical normal input is B(-2), and its leading trace degree is eight. Its diagonal/lower matrix entries have cover degrees zero/two. The scalar shadow has physical twist zero and cover degree eight, so its coefficient line is O_L(-4). Consequently its opposite regular lift obeys

    n_y = z^4 n_y^x.

The operator has physical twist four and degree shift four. Its output is B(2); the relevant trace degree is twelve. The diagonal, upper and lower matrix entries have cover degrees four, two and six. Combining the actual vertex frame lines O(9/2), O(-5/2) with the physical twist gives their respective coefficient lines

    O(0), O(8), O(-8).

The scalar trace output has physical twist four and degree twelve, hence line O(-2). Therefore the correct operator transport is

    F_y = z^2 T(n_y^x),

exactly as checked by both endpoint verifiers. These are not the transformation factors of an untwisted ordinary two-by-two matrix.

The kernel in this degree is the lower tangent coefficient of cover degree one, namely Wprime O_L(-3). The upper tangent coefficient would have degree minus one and is absent. Multiplication by the cubic f gives the matrix diagonal and respects the coefficient lines O(3) times O(-3)=O(0).

## 2. Orientation and complete trace lifts

Both computations use the oriented base coordinate w=-1/z and the same regular targets as the independently checked actual operators. Transporting the y trace-lift matrix to x first multiplies upper/lower entries by z^8/z^-8, and then conjugates by P(p_x-p_y^x). This is the correct marked target change, since p_y^x=z^-8 p_y.

Both verifiers construct complete regular matrices K_x,K_y and check q(K_i)=T(n_i). The base poles from their temporary rational construction are removed by explicit tangent additions. The additions are retained in the secondary difference, not thrown away as zero trace. The square input uses tangent corrections 4kY/(Ac^2 z^2) and -4kY/(Ac^2 w); the XY^3 input uses 5kY/(Bc z) and zero.

Every final matrix entry is checked to be polynomial in the chart coordinate AND both positive variables. Consequently localization in a positive variable during the polynomial-remainder construction does not leave an unverified pole in the final trace lifts.

Both computations include the equation-unit term in

    L(E)=H DE+[A,E]+H rho E,   rho=4z,
    T(s)=H Ds+u s.

They verify the cone-preservation identity and exact trace diagram. The resulting FULL difference

    L(eta)-K_y^x+K_x

has upper entry zero, diagonal f gamma and lower entry 2g_x gamma, hence is precisely tau(0,gamma).

## 3. Exact coboundary and nonzero residue

For X^4 the entire gamma equals

    z^-3 gamma_y(-1/z)-gamma_x

with the displayed gamma_x,gamma_y regular on their charts. This is an exact O(-3) coboundary, stronger than merely observing two absent Laurent coefficients.

For XY^3 the entire gamma equals

    3kY/(Bc z) + z^-3 gamma_y(-1/z)-gamma_x,

again with explicitly verified regular cochains. H1(O(-3)) is represented by the two Laurent powers z^-1,z^-2. The surviving class is therefore exactly (3k/(Bc))[Y/z]. It is detected by the GLOBAL dual section Y* tensor 1 of Wprime* O(1): its residue pairing is 3k/(Bc), nonzero because all source parameters remain unassigned nonzero constants. A local functional outside the dual section space is not being used.

## 4. Why these are actual endpoint values

ACTUAL-TWO-ENDPOINT-INPUTS-HAVE-COMPATIBLE-CONE-OPERATORS.md proves the actual source identity and scalar inverse separately for EACH input. Its verifier checks both complete regular charts and the full physical determinant-normalized root transport. The actual scalar is fixed by the scalar-cup isomorphism, rather than chosen to make the endpoint simplify.

The general conic-cocycle comparison in ACTUAL-ENDPOINT-QUOTIENT-IS-LOWEST-VERTEX-COHOMOLOGY.md then identifies the actual degree-four operator with this homogeneous operator. Actual conic patching corrections begin at weighted diagonal degree twelve. Remaining global fixed-symbol/fixed-section-action ambiguity is ell n with ell in H0(O_X(2)), beginning at degree eight. Neither can change the target degree-four operation. The equation-unit term H rho and all K_i remain in this comparison.

The same endpoint theorem identifies the actual endpoint quotient Cplus/J with H1(Wprime O(-3)). The actual normal generator has a nonzero lowest piece, and the apolar reconstruction identifies it with c_eta times the cocycle used here, with c_eta nonzero. Linearity scales the shadow lifts, trace lifts and endpoint class by this same factor. The actual component-constant term is canceled exactly by the global scalar subtraction, not discarded by a support argument.

Thus no additional unevaluated comparison scalar can change zero to nonzero or vice versa. The second input proves a nonzero actual endpoint class. It does not identify any subsequent higher obstruction with that class.

## Independent reproduction

The audit reruns the two frozen secondary verifiers and the actual two-input operator verifier, without assigning any source parameter or evaluating an instance rank. The exact secondary identities are in:

- UNIVERSAL-HOMOGENEOUS-ENDPOINT-SECONDARY-SQUARE-CANCELLATION.md;
- verify_homogeneous_endpoint_secondary_square_cancellation.py;
- UNIVERSAL-HOMOGENEOUS-ENDPOINT-SECONDARY-XY3-NONVANISHING.md;
- verify_homogeneous_endpoint_secondary_xy3_nonvanishing.py.

The companion XY^3 proof records the same normalized nonzero class. Frozen sources were not modified by this audit.

Run python verify_actual_two_input_endpoint_audit.py to rerun the three universal verifiers and independently check that the actual-compatible regular operators are entrywise IDENTICAL to those used in the two secondary calculations, with the same full normal cocycle and shadow lifts. It also checks the physical line arithmetic and the effect of an arbitrary nonzero actual normal scale.
