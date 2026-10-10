# First-order matrix lift: proof and exact regression scope

The companion transgression proof gives an explicit first-order lift from constant-differential local splittings of the determinant-trivial Horrocks–Mumford pullback. The executable certificate tests the instantiated splitting and transition formulas at rational points. Its 6,864 exact zero residuals are regression evidence; they do not replace the coefficientwise proof.

## Data and frames

The self-contained script embeds sparse polynomial matrices for the six carrier charts, expressed in the common basis of
K = [5 N^{-1} → 15 N → 10 N^3 → 2 N^5].
Each polynomial is an array of exponent/coefficient pairs in (a,b,c,d); each rational matrix has its displayed common denominator. Charts 0–4 are cyclic primary charts and chart 5 is the auxiliary chart. These are the globally homogenized contraction matrices, not unconverted projective-chart matrices.

For pivot j, form W from the eight vectors e_k−(v_k/v_j)e_j, in cyclic order in each five-dimensional half, and η=e_j/v_j in each half. Let L read the nonpivot coordinates. The splitting matrices and inverses are
U0=[γ,I,H1 W], Q0=[H0;P;L δ],
U1=[W,η], Q1=[L;ε].
The script checks Q0 U0=1 and Q1 U1=1 at each tested point. It differentiates every rational matrix exactly and uses B_r=−(dU_r)Q_r. The normalized column transition is P_i I_j; the left-row transition is its transpose.

On a fixed line chart the scalar correction is
s_ij=(1/4)ιπ str(B_i∧B_j).
Writing K(g)=μ1(g^{-1},g), use u_ij=g_ij(s_ij 1−K(g_ij)/2).
The test evaluates u_jk g_ij+g_jk u_ij−u_ik+μ1(g_jk,g_ij).

## Executed fixed-chart tests

All six carrier charts, all 216 ordered triples, and all six coordinate bivectors are tested at each of
(a,b,c,d)=(1,1,1,2), (1,2,3,4), (2,3,4,5).
This gives 3,888 exact rational zero residuals.

## Mixed line charts

The line chart mask records which factors use the frame q_i=y_i/x_i instead of 1. At a tested point, a constant change of frame normalizes each q_i value to 1. This leaves d log q_i unchanged and keeps the matrix evaluation rational. The logarithmic derivatives used are
∂_x log q=(x²+1)/(2x(x²−1)),
γ_old=1/(x(x²−1)) dx.
The latter is one half of d log(1−x^{-2}). The implementation also includes the diagonal line-frame changes of U0 and U1 and the old connection weights (−1,1,3,5).

The scalar transgression includes the old-connection terms and the shorter-gerbe correction −15 r/8. For a coordinate bivector ∂_xa∧∂_xb, the shorter gerbe is (15/4) times the product of the corresponding overlap mask differences divided by xa xb. Multiplying by the values of ya yb gives the actual invariant-vector-field bivector at that point; first-order equations involve no derivative of π.

The three mixed-chart runs are:
- x=(2,−2,3,4), vertices (0,0),(1,3),(5,12),(2,15): 384 equations.
- x=(2,3,4,5), vertices (0,0),(1,3),(2,5),(3,10),(4,12),(5,15): 1,296 equations.
- x=(3,4,5,6), vertices (0,15),(1,12),(2,10),(3,5),(4,3),(5,0): 1,296 equations.

All 2,976 mixed-chart residuals vanish exactly. The tested points lie in the required overlaps.

## Reproduction and remaining scope

Run the companion JavaScript file with Node.js. It uses BigInt rational arithmetic, prints each report, and throws if any residual is nonzero. It requires no external packages.

The coefficientwise proof additionally uses the exact splitting and determinant-one identities established in the atlas and contraction certificates. The point tests specifically guard their implementation and the cross-line signs. No second-order residual, finite cohomology projection, or solution of the original Weil-class problem is asserted here.

Run from the repository root: `node research/hm/verify-first-order-regression.js`.
