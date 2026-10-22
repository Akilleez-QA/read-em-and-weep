# The actual Atiyah correction has an absolute double-cubic representative

## Result

Use the fixed normalization ζ_a=k At_G(D_a), k≠0, and the actual Serre pair σ=(f,g), with f of positive cover degree3 and g of degree5. Write z for an oriented base coordinate, a=a(z) for a negative binary quadratic, and

    D_a=2a ∂z+(a_z/2) Euler_positive.

The FULL class t(a)=a ζ_a in Cminus, not merely its effective twelve-dimensional quotient, is the global defect boundary of the absolute section with vertex coordinate

    r_t/g² on 2D,
    r_t=k a [D_a(fg)−2a_z fg].                         (1)

Since fg has positive Euler degree8, equivalently r_t=2k a ∂z(a f g). The line on 2D is O_(2D)(−2,10). The global boundary is the one identifying H0(M_-)/A with Cminus. This provides the full correction needed to subtract b ζ_a when the actual canonical third correction b is proportional to a. It does not compute the endpoint normal-variation P4 or the fourth Bockstein.

All arguments are identities of derivations, regular pairs and line bundles. No actual coefficient value or instance matrix is selected or evaluated.

## 1. Tangency and the actual boundary

In a determinant-compatible frame put

    n=[[fg,−f²],[g²,−fg]],
    R_t=k a[D_a n−2a_z n].                             (2)

The natural action on the physical O(2) line is −2a_z. Thus (2) is the tensor derivative of the actual section N, using the local trivial connection on the bundle and the natural action on its twisting line. It is not an arbitrary subtraction of a scalar term. Since n²=0, differentiation gives

    n R_t+R_t n=0.

The diagonal of (2) is (1). Hence (2) defines the tangent-modulo-conjugation defect section.

For a change of bundle frame P, the difference of the local tensor derivatives, after transport to the target frame, is

    [k a D_a(P) P^−1,n].                               (3)

Scalar determinant factors in D_a(P)P^−1 do not affect the commutator. We use the positive Atiyah cocycle D_a(P)P^−1 throughout. The exact tangent/commutator diagram therefore identifies the global boundary of (2) with k a At_G(D_a)=t(a), with no normal-division factor ν. Choosing the opposite Čech convention changes both boundaries together, not their relative subtraction.

On the conic, the negative quadratic a vanishes and D_a is tangent to the negative block. Thus this derivative has zero conic defect. Its vertex representative lies in the degree-eight coefficient bundle M_-. The already-proved global quotient, rather than an assumed extension of a chosen homogeneous polynomial lift, identifies its boundary in Cminus.

## 2. Full finite quintic-source covariance

Let g'=g+p f and put r_t' equal to (1) with g'. Treat D_a as a derivation; it differentiates p as well. Direct expansion gives the exact identity

    r_t' g²−r_t(g+p f)²
      =f² {k a[g²(D_a p+2a_z p)−2p g D_a g]−p²r_t}.   (4)

Consequently r_t'/g'² and r_t/g² agree on the double cubic. This is the finite canonical-module comparison, not just equality on D and not equality after a cup product. In actual regular target frames the numerator is regular because it is obtained by differentiating regular f,g and a.

## 3. Base frames and determinant term

For the oriented opposite chart w=−1/z, the actual coefficient frames satisfy

    f_y=z^−3 f_x,   g_y=z^5 g_x,   a_y=z^−2a_x.

The positive-cover Euler degree of fg is8. Since ∂w=z²∂z and

    (a_y)_w=a_z−2a/z,

one obtains

    D_(a_y)(f_y g_y)=z²D_a(fg)−4az fg.

Substitution into (1) gives EXACTLY r_t,y=r_t,x. The quotient r_t/g² therefore acquires the required factor z^−10. Omitting the determinant term −2a_z fg would leave an erroneous −4a²fg/z. This checks the root-line/base-frame action, rather than only triangular changes.

## 4. Full midpoint corrected source for the detecting square

For a=t²,h=X²Y², the canonical correction theorem proves b=γa with a fixed nonzero γ. Retain its already-fixed normalization and sign, rather than assigning a new invariant numerical value.

Let r_mid be the explicit absolute numerator in ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md. That numerator was obtained by division by the cover equation, so its physical section is r_mid/(νg²). In contrast (1) is an Atiyah derivative and has no such division. The complete MIDPOINT projection of the corrected source is therefore represented by

    [r_mid/ν−γ r_t]/g².                                (5)

Its global boundary is [v_h]_minus−b ζ_a. Formula (5) retains every polynomial-nine direction; no splitting of the effective quotient has been chosen. The class of b ζ_a lies in Cminus because the Serre involution fixes At(D_a) and negates a. The actual endpoint can still carry its residual Cplus/J=P4 contribution.

The published actual third-zero theorem implies that multiplication by a kills the boundary of (5). This is a check on its lower multiplication, not the next ambient division and not a value of β4.

## Verification and dependencies

Run python verify_absolute_atiyah_double_cubic.py. The verifier checks the complete derivation identity (4), the full tangent equation, and the exact base-frame computation with arbitrary symbolic a,a_z and a degree-eight Euler eigenvector. It does not substitute actual HM coefficients.

The geometric inputs are the actual Atiyah normalization, the complete tangent/commutator presentation, the corrected physical determinant action, the actual double-cubic/global-boundary quotient, the nonzero canonical square-source correction, and the absolute midpoint section theorem. The verifier checks the displayed universal identities; it does not independently establish those pinned geometric inputs.
