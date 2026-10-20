# Independent audit: six pinned primitive retractions

## Verdict

The pinned model satisfies the rational identities

    H0_i gamma = Id5, H0_i I_i = 0, H0_i H1_i = 0

on all six stated denominator localizations, without assuming primitive A. This is a structural proof from a sparse four-cycle inverse (five primary carriers), a triangular inverse (the auxiliary carrier), and literal zero support. It does not use the determinant-volume theorem or its conclusion, the historical primitive receipt, physical matrix products, source execution, or polynomial expansion.

The independent static comparison passed in both ordinary Python and `python -O`, with byte-identical receipts. It compares all 450 stored H0 cells, the 150 selected gamma cells, all six homotopy denominator records, and the 360 relevant I/H1 zero cells against the formulas below. The implementation only encodes signed factor labels into exponent metadata and compares inert JSON records. The mathematical elimination is in this note; the checker is not an arithmetic proof engine.

The source bytes are the previously authenticated model copy at `../determinant-volume-20261018/inputs/hm-pinned-model.json.txt`, SHA256 `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`. This audit verifies that pin locally; it does not establish a new remote provenance claim. The decoder interpretation is H0 = stored H0/dh, with v0=1.

## 1. Universal sparse inverse, derived without contractions

Work over a commutative ring localized at

    Delta = t*a*b*c*d - t^5 = -t*(t^4-a*b*c*d).

Here t and h=t^4-a*b*c*d are units, since their product is a unit. Consider the five equations

    yA = b*x3 + t*x4,
    yB = t*x1 + c*x2,
    yC = -d*x1 - t*x3,
    yD = -t*x2 - a*x4,
    yE = t*x0.

Starting from yC, then yA, then yD gives

    t*x3 = -yC-d*x1,
    t^2*x4 = t*yA+b*yC+b*d*x1,
    t^3*x2 = -t^2*yD-a*t*yA-a*b*yC-a*b*d*x1.

Substitution into yB gives one cycle-closure equation,

    h*x1 = a*c*t*yA+t^3*yB+a*b*c*yC+c*t^2*yD.

It uniquely determines x1; the preceding equations uniquely determine x2,x3,x4, and yE determines x0. The resulting numerators over the single denominator Delta are

    x0: (a*b*c*d-t^4)*yE,
    x1: -a*c*t^2*yA-t^4*yB-a*b*c*t*yC-c*t^3*yD,
    x2: a*t^3*yA+a*b*d*t*yB+a*b*t^2*yC+t^4*yD,
    x3: a*c*d*t*yA+d*t^3*yB+t^4*yC+c*d*t^2*yD,
    x4: -t^4*yA-b*d*t^2*yB-b*t^3*yC-b*c*d*t*yD.

This proves that the displayed linear map is the inverse of the five-equation map. It uses only elimination on an invented universal sparse pattern; it does not compute a product of the actual source matrices. No determinant theorem is needed. In particular there is no dependency on A, exactness, quotient volume, or physical-frame identification.

For primary carrier j, let

    (t,a,b,c,d) = (v_j,v_(j+1),v_(j+2),v_(j+3),v_(j+4))

with all variable and domain indices taken modulo five. The selected ambient rows in the equation order (A,B,C,D,E) are

    (j+1, j+4, 5+(j+2), 5+(j+3), 10+j),

where each entry inside a five-row block is reduced modulo five. The output coordinates (x0,...,x4) in the universal equations mean the actual domain coordinates (j,j+1,j+2,j+3,j+4). The literal selected gamma records match these equations, and the literal dh is exactly Delta with v0=1. Every stored H0 numerator matches the displayed inverse after this index renaming and deletion of the inert v0 factors. All its other ambient-coordinate coefficients are empty records. Thus

    H0_j = (gamma restricted to F_j)^(-1) R_Fj,

where R_Fj selects the five rows in any consistently chosen order. Consequently H0_j gamma=Id5 for j=0,...,4.

No homogeneity of an unexamined source entry is assumed: the comparison covers each of the five actual stored H0 arrays and all selected gamma records.

## 2. Auxiliary triangular inverse

Write a=v1,b=v2,c=v3,d=v4, with v0=1. The selected rows F5=(4,7,8,10,11) give

    y4 = x1+c*x2,
    y7 = -d*x1-x3,
    y8 = -x2-a*x4,
    y10 = x0,
    y11 = a*x1.

They solve successively as

    x0 = y10,
    x1 = y11/a,
    x2 = y4/c-y11/(a*c),
    x3 = -y7-d*y11/a,
    x4 = -y8/a-y4/(a*c)+y11/(a^2*c).

The stored denominator is Delta5=-a^2*c*d. It makes a,c,d units. In that normalization, the five numerator rows are

    -a^2*c*d*y10,
    -a*c*d*y11,
    -a^2*d*y4+a*d*y11,
    a^2*c*d*y7+a*c*d^2*y11,
    a*d*y4+a*c*d*y8-d*y11.

All 75 stored auxiliary H0 cells and all 25 selected gamma cells match these formulas literally. Therefore H0_5 gamma=Id5 independently of A. The apparent extra d in dh is a common normalization factor; the triangular inverse itself needs only a and c to be units.

## 3. Support consequences and unconditional A-row reduction

In increasing order the selected sets are

    F0=(1,4,7,8,10),
    F1=(0,2,8,9,11),
    F2=(1,3,5,9,12),
    F3=(2,4,5,6,13),
    F4=(0,3,6,7,14),
    F5=(4,7,8,10,11).

Literal inspection establishes I_i[F_i,:]=0 and H1_i[F_i,:]=0. Since H0_i is supported precisely on F_i, this proves H0_i I_i=0 and H0_i H1_i=0 by disjoint support, without multiplying any polynomials.

Put R_i=gamma H0_i+I_i P_i+H1_i delta-Id15. Then the retraction identities give H0_i R_i=0 as a formal consequence. More directly, the rows in F_i vanish: gamma_F H0=R_F, I_F=0 and H1_F=0. Thus the five F_i rows of A, totaling 75 of its 225 displayed scalar entries per carrier, are already proved. The unproved A obligation may be stated as the other ten rows, 150 entries per carrier. This is a row-count reduction, not a claim of algebraic independence or an A proof.

## 4. Optional stronger block reduction, with its extra metadata premises exposed

The following refinement is algebraically valid if the additional literal support/normalization premises below are checked. They are not part of this audit's minimal checker; the producer's broader review may certify them separately.

Choose the existing coordinate pair D and complementary eight-set S, and suppose

    I_F=0, I_D invertible, H1_F=H1_D=0,
    P_S=0, P_D=I_D^(-1).

The support identities then give PI=Id2, PE_S=0 and PH1=0. The basis N=[gamma,I,E_S] is invertible solely because its block lower-triangular matrix in row order (F,D,S) has invertible diagonal blocks gamma_F,I_D,Id8. This argument is independent of A and of determinant normalization.

Assume the already structural C: ev delta=0 and the pivot splitting W L+eta ev=Id10. Let

    T=H1[S,:] W, M=L delta E_S.

Then direct abstract block algebra gives

    N^(-1) R N =
        [ 0              0           0       ]
        [ P gamma        0           0       ]
        [ T L delta gamma T L delta I T M-Id8 ].

In particular the independent inverse formula does not silently identify the middle row of N^(-1) with the stored P: that equality would already require P gamma=0. The displayed computation instead uses N^(-1)I as the canonical middle inclusion, so it is noncircular.

The displayed residual has at most 130 scalar positions per carrier: 10+40+16+64. If the direct sparse matching proof of det M is used, that minor's invertibility is an independent support fact; no theorem about det(P_i I_j), split-frame volume, or contraction may be imported here. All four residual blocks still need proof. This refinement does not certify them.

## 5. Scope and reproduction

Historical checker results are discussed below; no rerun is asserted here. Neither imports nor executes any production or historical source. There is no actual polynomial multiplication, matrix multiplication, field evaluation, specialization, owner, source jet, or transition calculation. The script uses explicit exceptions rather than assertions.

The newly proved statement is the retraction identity and its two zero-support consequences on all six pinned rational carriers. It reduces the remaining A obligation; it does not remove A, establish a complete contraction, prove delta gamma=0 or delta I=0, establish legal-owner regularity, authorize physical execution, or decide a global obstruction.

## 6. Review of the producer's completed artifact

I also read `../primitive-retraction-20261018/PROOF.md` after completing the independent inverse derivation and literal checks. Its Sections 2–5 agree with the inverse formula and support reasoning here. Its Section 6 correctly gives an unconditional four-block, 130-position coordinate defect, using the additional P/H1 metadata checks supplied with that package. Section 7 correctly conjugates the defect by N and uses the independent invertibility of M to obtain the stated four remaining families. In particular it does not assume P gamma=0, identify Q with P prematurely, or infer delta gamma=0 from the A-dependent contraction theorem. Accepted on those stated source and scalar premises. The new PR-head provenance statement in that artifact is not independently re-fetched by this local audit; the source model's exact bytes are independently hash-checked here.
