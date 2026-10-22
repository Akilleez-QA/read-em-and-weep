# A unique section cubic cannot have identically vanishing square jet

## Result

Let C be a reduced curve in P4 over C, whose general hyperplane sections Z_H are reduced and transverse to C. Assume H0(I_C(3))=0 and, for general H,

h0(I_(Z_H,H)(2))=0, h0(I_(Z_H,H)(3))=1.

Then the first-normal-jet map j_H of the unique section cubic is nonzero for general H. Consequently, under the actual Rao identification of DOUBLE-HYPERPLANE-JET-CRITERION.md, multiplication

ell^2: H1(I_C(1)) -> H1(I_C(3))

is injective for general ell. This closes the square-quadratic residual criterion in the a=0,b=1 branch without proving b=0 or claiming that every later source-lifting obstruction vanishes.

## 1. Suppose the generic jet vanishes and choose double lifts

Use hyperplanes H_t given by

ell_t=X4-sum_(i=0)^3 t_i X_i=0.

A generic zero jet means the nonzero cubic f_t on H_t admits an ambient cubic lift g_t whose restriction to C vanishes to order at least two along Z_t. This is precisely the double-hyperplane criterion. All conditions on coefficients are linear and algebraic in t. After shrinking to a nonempty open with constant ranks, choose a regular algebraic family g(t,X) with g|H_t=f_t nonzero. Such a choice can be made by selecting a local splitting of the surjective linear map from the double-lift space to the rank-one cubic space. No coefficient evaluation is needed.

At a marked point p(t) on a fixed component of C, differentiate g(t,p(t))=0. The derivative dg_t along that component is zero at p, because g_t|C has a double zero there. Thus every parameter derivative partial_i g vanishes at every point of Z_t. Since the cubic ideal on H_t is one-dimensional,

partial_i g = c_i(t) g + ell_t q_i(t,X),             (1)

where q_i is quadratic and c_i is a scalar function. These coefficients can be chosen regularly after shrinking: the equality on H_t determines c_i uniquely, and polynomial divisibility determines q_i.

## 2. The scalar connection has zero curvature

Commuting two parameter derivatives in(1), then reducing modulo ell_t, gives

(partial_j c_i-partial_i c_j) f_t + X_i q_j|H_t-X_j q_i|H_t=0,

up to the simultaneous harmless choice of sign for the antisymmetric pair. Write x_i=X_i|H_t and let a_ij be the scalar curvature coefficients. Wedging the displayed identities with x gives

(x_i a_jk-x_j a_ik+x_k a_ij) f_t=0

for all triples. The polynomial ring of H_t is a domain and f_t is nonzero. The x_i are independent coordinates and the a_ij do not depend on x, so every a_ij=0. Hence the one-form sum c_i dt_i is closed.

On a small simply connected analytic open in parameter space, rescale g by a nowhere-zero analytic scalar solving partial_i u=-c_i u. This makes every partial_i g divisible by ell_t. Working analytically here is sufficient: the final fixed polynomial will vanish on a nonempty analytic family of sections of the algebraic curve, hence on C. No algebraic primitive of the closed one-form is assumed.

## 3. Successive corrections remove all parameter derivatives

We use an elementary polynomial lemma. Suppose a family h(t,X) is homogeneous of degree d and every partial_i h is divisible by ell_t^k, where 1<=k<=d:

partial_i h=ell_t^k a_i, deg_X(a_i)=d-k.

Commutativity of partial_i and partial_j, using partial_i ell_t=-X_i, gives

x_i (a_j|H_t)-x_j (a_i|H_t)=0.                    (2)

If k<d, polynomial coprimality of the independent x_i implies a_i|H_t=x_i b_t for a common homogeneous polynomial b_t of degree d-k-1. Choose its ambient lift b(t,X), with coefficients analytic in t. Then

h_new=h+ell_t^(k+1) b/(k+1)

satisfies partial_i h_new divisible by ell_t^(k+1): differentiating the correction subtracts ell_t^k X_i b, which cancels the quotient modulo ell_t. If k=d, the a_i are scalars, and(2) forces all a_i=0. Thus h is constant in t.

Apply this with d=3, starting at k=1 after section2. A correction divisible by ell_t^2 gives derivatives divisible by ell_t^2; a correction divisible by ell_t^3 gives derivatives divisible by ell_t^3; the terminal scalar argument then makes all derivatives zero. Both corrections preserve the restriction to H_t and preserve vanishing on C intersect 2H_t. We obtain a single ambient cubic G(X) such that

G|H_t = u(t) f_t

throughout the analytic parameter open. It is nonzero, since its restriction is nonzero.

## 4. Contradiction and residual consequence

The fixed cubic G vanishes on Z_t for every t in that open. On each component of C, its intersections with a nonempty open family of transverse hyperplanes range over a nonempty analytic open subset of the component. The restriction of G therefore vanishes identically on each component, so G belongs to H0(I_C(3)), contradiction.

Thus generic j_H is not zero. Its source is one-dimensional, so it is injective. The square-jet exact sequence

0 -> H0(I_Z(2)) -> ker(ell^2:M1->M3) -> ker j_H -> 0

now has both outer spaces zero, proving the claimed injectivity. Here M_d=H1(I_C(d)), and the exact sequence also assumes the established global ideal vanishings in degrees1 and3, both satisfied in the actual HM setting by H0(I_C(4))=0.

## Scope

The proof allows reducible C and does not invoke integral-curve uniform position. It assumes generic transverse sections and uses the double vanishing along the actual components, not arbitrary chosen first-order directions. It establishes the quadratic Rao/residual map in the b=1 alternative. It does not by itself settle the b=2 alternatives, an independent remaining lift boundary, or full Q4. No actual HM coefficients, selected matrix ranks, scans, source evaluations, local-model spike, or consumed experiment were used.

The double-lift equivalence and square-jet exact sequence are from DOUBLE-HYPERPLANE-JET-CRITERION.md at18963f6d45068dd561c63420b9f0135103a9d09b in Akilleez-QA/read-em-and-weep/research/hm/order-four-quadratic-load. The new content is the integrability-and-correction proof forcing an ambient cubic if the unique jet vanished generically.

## Actual generic square-residual conclusion after the section exclusions

The complete section-case reductions now give a=0 and b<=1: quadric lifting at d1cee1b93be80edcced2b84ff7b8ec6b8c27681b and its pinned endpoint dependencies; b=3 closure at1a978bf6a3db59469dff651fd9062b7622bdbde0 with finite/sextic dependencies; b=2 classification at e0d0c123934f06cb63937225881a83e5e5906cfb, small-defect exclusion9b563037147fc62ee5d66b1e5a23dcbc2102ed33, octic exclusion936b652b228d9169a242f962f6053dec00df6382, and nonic exclusion1c0d39586d937ec460a0d0e5dbc1e07f08c366f0. These are all in Akilleez-QA/read-em-and-weep PR543.

If b=0, the jet source is zero, so the square-jet criterion already gives injectivity. If b=1, the theorem above gives it. Thus in the actual generic HM hyperplane family, ell squared is an injective multiplier M_1 -> M_3 of the Rao module. Equivalently the corresponding actual quadratic residual map is generically surjective under the pinned duality identification. This is not a numerical model, a claim about every selected ell, or full quadratic-adjoint invertibility. The separate primary and lift-boundary requirements must still be checked at their own interfaces.
