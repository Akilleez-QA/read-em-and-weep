# The fourth-detecting input's endpoint from two universal tensors

## Exact endpoint result, not a fourth value

For the actual input a=t^2, h=X^2Y^2, the normalized lower endpoint has canonical P4 Serre residue

    E(t^2,X^2Y^2)=ke/(3Bc) s(AX^2s+2BY^2t).          (1)

For the actual normal generator multiply (1) by the SAME unknown nonzero c_eta as in the two previously computed endpoint values. In particular this endpoint is nonzero. This is not a fourth Bockstein value or the next ambient normal division. It does not evaluate the full higher-normal lift or replace it by its endpoint component.

All A,B,c,e,k remain unassigned nonzero parameters. Independence below is an exact universal tensor identity with nonzero symbolic determinant, not an actual-instance rank test. No frozen endpoint-package artifact is edited.

## 1. The actual two-dimensional family space

The actual corrected endpoint is G-equivariant, quadratic in a in A=Sym^2(W), and linear in h in D5=Sym^4(Wprime), by ACTUAL-ENDPOINT-NORMAL-VARIATION-IS-NONZERO.md. Its target is the canonical P4 complement in V tensor A, where V=Sym^2(Wprime).

The relevant multiplicity is

    dim Hom_G(D5 tensor Sym^2 A,P4)=2.

One exact character check uses A5 class sizes (1,15,20,12,12) and characters

    D5=(5,1,-1,0,0),
    P4=(4,0,1,-1,-1),
    Sym^2 A=(6,2,0,1,1).

Their product has character inner product 120/60=2. These are even representations, so the same multiplicity holds for the binary group. The scalar summand of Sym^2 A cannot map D5 to P4. Thus using the ordinary quartic a^2 loses no possible endpoint family.

This dimension statement alone evaluates nothing. We now construct TWO equivariant tensors, prove their independence, and calibrate them against both already computed actual values.

## 2. Equivariant tensors and the actual orthogonal projection

Retain the actual invariant cubic tensor

    f=AX^2Y s^3+BY^3s^2t+AcX^3st^2-BcXY^2t^3.

For bihomogeneous polynomials define the UNNORMALIZED product transvectant

    (p,q)_(r,j) = sum_(i=0)^r sum_(l=0)^j
       (-1)^(i+l) binom(r,i) binom(j,l)
       (partial_X^(r-i) partial_Y^i partial_s^(j-l) partial_t^l p)
       (partial_X^i partial_Y^(r-i) partial_s^l partial_t^(j-l) q).

It is contraction with the two invariant alternating tensors, hence equivariant. This fixes all factorial conventions used below. Put H=(f,f)_(1,1) and define

    U(a,h)=pr_P4((h a^2,f^2)_(4,4)),
    V(a,h)=pr_P4((h a^2,H)_(3,3)).                 (2)

Both expressions have bidegree (2,2), are quadratic in a and linear in h, and are G-equivariant because f and the apolar projection carry their actual invariant markings.

The projection is onto the ACTUAL complement of Q(D5), not an abstract isomorphic four-space. Let Q_i=Q(X^(4-i)Y^i), with all five actual formulas from ACTUAL-NONZERO-ENDPOINT-HAS-AN-EXPLICIT-P4-SERRE-RESIDUE.md. Under the product degree-two apolar pairing, the exact universal Gram identity is

    <Q_i,Q_j> = (3e^2/8) (-1)^i/binom(4,i)
                   if i+j=4, and 0 otherwise.     (3)

Thus Q(D5) is nondegenerate. The canonical equivariant projection is explicitly

    pr_P4(p)=p-sum_i <p,Q_(4-i)>/<Q_i,Q_(4-i)> Q_i. (4)

Equations (3),(4) are exact formal identities in unassigned parameters. They avoid any chosen-instance rank computation. The verifier checks every Gram identity and all projected orthogonality identities.

## 3. Universal independence on the two abstract kernel inputs

Set a=t^2 and introduce nonzero symbolic output directions

    O1=B t(2AX^2s-BY^2t),
    O2=A^2 X(cXt^2+2Ys^2),
    O3=A s(AX^2s+2BY^2t).

Direct universal differentiation and the projection (4) give the COMPLETE identities

    U(t^2,X^4)=-552960 O1,
    V(t^2,X^4)=-995328 O1,

    U(t^2,XY^3)=-3870720 O2,
    V(t^2,XY^3)=-248832 O2,

    U(t^2,X^2Y^2)=2764800 O3,
    V(t^2,X^2Y^2)=497664 O3.                       (5)

The determinant of the two universal coefficient rows for the first two inputs is

    (-552960)(-248832)-(-995328)(-3870720)
       = -3715041853440 != 0.                     (6)

This is a polynomial certificate that the two equivariant MAPS in (2) are independent: any linear relation between the maps would give a relation on each of the two entire symbolic output directions O1,O2, and (6) forces both coefficients to vanish. It is not a rank evaluation at a selected actual source coefficient or bundle instance.

By Section1 these two maps are a basis of the entire quadratic endpoint-family space. Consequently two correctly marked actual evaluations determine every input. The fixed source identification I_f is retained through h: X^4 and XY^3 are precisely the previously checked kernel lines, not newly substituted negative-coordinate quartics.

## 4. Calibration against BOTH actual corrected values

The proved actual endpoint values, with the common c_eta temporarily factored out, are

    E(t^2,X^4)=0,
    E(t^2,XY^3)=-keA/(Bc)(XYs^2+(c/2)X^2t^2).    (7)

The second is the exact canonical P4 residue, not an arbitrary representative modulo Q(D5). Its connecting sign and factor 2/3 were independently checked in the residue audit described below.

Writing E=c_U U+c_V V, equations (5),(7) uniquely yield

    c_U=ke/(7464960 ABc),
    c_V=-ke/(13436928 ABc).

Thus the COMPLETE normalized quadratic family is

    E(a,h)=ke/(ABc) [U(a,h)/7464960
                         -V(a,h)/13436928].       (8)

This formula is in the stated unnormalized transvectant convention. A different factorial convention changes the two tensor coefficients, not the calibrated endpoint.

Substitution of the third row of (5) into (8) gives exactly (1). Its X^2s^2 coefficient is keA/(3Bc), nonzero in the formal coefficient field. The verifier also checks that (1) is orthogonal to all five Q_i. It is therefore a nonzero canonical P4 vector, not merely a nonzero representative killed by the endpoint quotient.

Restoring the actual normal generator multiplies (8) and (1) by c_eta, without determining that scale. No numerical normal-coordinate normalization is imposed.

## 5. Short independent audit of the calibration residue

The exact cubic sequence is

    0 -> Wprime O(-3) --f--> D5 O --Q--> V O(2) -> 0.

The regular local quartic lifts

    p_x=-BY^4-AcX^3Yz+BcXY^3z^2,
    p_y^x=AX^2Y^2/z

satisfy p_y^x-p_x=fY/z and Q(p_x)=Q(p_y^x)=-(eA/2)XY. D5 O has coefficient transition one, and p_y^x becomes -AX^2Y^2w under w=-1/z, so both are regular with the stated connecting orientation.

The actual product apolar orthogonal projection sends

    XYs^2 -> (2/3)(XYs^2+(c/2)X^2t^2),

as follows from the exact decomposition

    XYs^2=(2/3)(XYs^2+(c/2)X^2t^2)
                      +(2B/(3eA))Q(Y^4).

Multiplying by the actual endpoint coefficient 3k/(Bc) gives exactly the second value in (7). Its sign, degree-zero transition and projection factor are therefore fixed before calibrating (8).

## Reproduction and boundaries

Run python verify_endpoint_two_tensor_reconstruction.py. It reruns the explicit residue check, proves the invariant Gram identities, calculates both universal tensor maps at all three abstract inputs, certifies their independence by (6), checks the character multiplicity, calibrates BOTH actual values, and checks the result (1).

The previously established actual filtered-operator comparisons and trace-corrected endpoint calculations supply (7); they are not replaced by these tensor calculations. The result concerns only the lower endpoint normal variation at the fourth-detecting input. No higher Bockstein, next ambient normal division, or generic Smith exponent follows from it.
