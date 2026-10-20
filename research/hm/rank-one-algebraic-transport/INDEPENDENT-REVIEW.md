# Independent review: good powers and algebraic rank-one transport

## Reviewed bytes and verdict

Reviewed on 2026-10-20. This review binds the following exact SHA-256
digests:

- `PROOF.md`:
  `781f5a0b2d48f86d3120f423bf9eb766dbdbec759849d7810f7e32c42fcc5faf`
- `README.md`:
  `813b53869abcf152552ed4e102d78a2b896935b1ec9c1e4655e5064f6f3a2cea`

**Verdict: no blocking mathematical finding in the stated scope.**
The good-pure-power theorem and algebraic coefficient-family
construction are valid with the displayed hypotheses. The global and
local torsion bounds, exact original special fiber, and first-jet
reconstruction also check.

Two minor statement clarifications were incorporated before this
binding: the finite-dimensionality of V is explicit in the setup,
and the README includes the integer restriction d>=2. They do not
change the argument. This is an independent mathematical proof review,
not a formal verification or a selected HM multiplication computation.

## 1. Pure-power surjectivity

The theorem assumes a polynomial ring in finitely many variables over
C, a finitely generated graded module generated in degree zero, and
dim M_d=2 for d>=2. These hypotheses suffice.

For independent target functionals lambda and mu, the maps

    Phi(ell)(m)=lambda(ell^d m),
    Psi(ell)(m)=mu(ell^d m)

are independent vector-valued homogeneous polynomials. The displayed
polarization identity is correct, and degree-zero generation gives
M_d=S_d M_0, so the map from target functionals to these polynomials
is injective.

The critical point is correctly handled: the derivative rows are
flattened across BOTH linear-variable directions and M_0 generators.
The surjection V tensor M_0 -> M_1 therefore makes their rank exactly
the rank of ell^(d-1):M_1 -> M_d. Rank at most one for every ell makes
all minors vanish identically. It gives one rational scalar a for
all derivative entries, not a separate scalar for each component.

Euler's identity yields Psi=a Phi. Differentiating and comparing with
D Psi=a D Phi gives Phi da=0. A nonzero component of Phi implies
da=0, and the elementary coprime-polynomial argument correctly shows
that the simultaneous constants of C(z_1,...,z_n) are C. This
contradicts the independence of lambda and mu. The minor locus then
proves that good linear forms constitute a nonempty Zariski open.

The argument does not wrongly infer a Veronese intersection from
PR441's good-quadratic open set. It proves the stronger pure-power
claim directly. Characteristic zero is materially used in
polarization, differentiation, Euler division, and rational
constants; the proof does not claim a positive-characteristic
extension or arbitrary-target-dimensional Lefschetz theorem.

## 2. Open intersection and algebraic transport

The imported primary resolution genuinely gives degree-zero
generation, rather than merely the Hilbert function. Its top
dimension two and M_4=0 are used in their proper roles.

Nondegeneracy of U_0 makes

    l |-> l^T U_0^(-1)l

a nonzero quadratic polynomial. Its nonvanishing open intersects
the good-square open by irreducibility. No numerical ell, actual
HM map, or selected source is required.

For D=U_0^(-1)ll^T and alpha=l^T U_0^(-1)l, the identities

    D^2=alpha D,
    D^T U_0=U_0D=ll^T,
    (I+sD)^T U_0(I+sD)=U_0+(2s+alpha s^2)ll^T

are correct. The direct-sum eigenspace argument proves both the
determinant 1+alpha s and the stated inverse. Thus g(s) is a
regular algebraic GL_5 lift on the indicated open, and the cubic
v_0((I+sD)x) is a polynomial family with exactly the original
constant term.

The finite-map statement is properly separated from its restriction:
C[s] is free of rank two over C[t], t=2s+alpha s^2, while the
automorphism locus is finite etale over
Spec C[t,(1+alpha t)^(-1)]. The identity
1+alpha t=(1+alpha s)^2 proves the precise target localization.
No claim that this restricted map is finite over the whole
unpunctured target is needed.

## 3. Global quotient and support bounds

The two-column restriction produces E_t=coker(tI+C), of C-dimension
two, with a surjection E_t -> R_t. Tensoring with the rank-two free
extension doubles C-dimensions. Consequently E_s has length four
and R_s has length at most four.

The natural section-resolution square gives 15R_s -> Q_s after
passing to the quadratic cokernel and then quotienting by the
moving cubic. This does not require the cubic to descend as a
polynomial in t. In particular the proof correctly avoids
identifying Q_s with the base change of a fixed-cubic quotient.
The incoming section-resolution relations remain in the quotient.

It follows that Q_s has total length at most 60, is killed by
f(2s+alpha s^2), and has support at at most four parameters.
The annihilator has degree four because alpha is nonzero and f
is monic quadratic. Cokernel base change is right exact and gives
the stated fibers without any flatness assumption on Q_s.
The original fiber is the actual Q_0 with its original maps.

## 4. Local exponent and first-jet assertions

At b in the automorphism locus, tau(s)-tau(b) is (s-b) times a
unit. Local flat base change carries the e_a composition factors
of the controlling E_t to length-one factors. Thus the local
length bound 15e_a and annihilator exponent e_a are correct,
with e_a<=2.

The singular parameter is not silently included in that etale
bound. There tau(s)+1/alpha=alpha(s+1/alpha)^2, so the possible
exponent doubles to 2e_a<=4 and the local length bound becomes
30e_a<=60. The proof makes no transported-root geometric claim
at this point.

At zero, tau(s)=2s+alpha s^2 is an etale uniformizer change.
Hence the completed Q_s is killed by s^2. Reducing its exact
cokernel presentation modulo s^2 therefore reconstructs the
entire completed module. The coefficients are correctly

    u_0+2epsilon ell^2,
    v_0+epsilon sum_i (Dx)_i partial_i v_0.

The formal comparison with PR442 is literal for the chosen
direction q_1=ell^2: the rank-one square-root formula composed
with t=tau(s) becomes I+sD, using the branch with constant term
one. This is not a claim that every previously arbitrary good
quadratic direction has this particular rank-one algebraization.

## 5. Geometry and retained boundaries

On the allowed base, q_g=g(s) o q_0 is an actual algebraic root-map
family and E_g is its varying pullback coefficient with F held
fixed on the target. The original fiber is exact, and target
isomorphisms transport the regular sequence and all collision
strata. No invariance of the HM bundle under g is assumed.

The PR437/439 endpoint applies fiberwise with the transformed
pair. Away from zeros of the controlling annihilator, primary
surjectivity and naturality give whole-coefficient order-six
vanishing, also over C(s). The proof does not identify Q_s with
a relative R^2 or its ordinary dual.

The final exclusions are necessary and correctly retained:
generic vanishing does not decide Q_0; an annihilator root is
not necessarily a bad endpoint; no actual source membership,
six pure conditions, module lift, or algebraicity of a formal
quantization/module follows. The length 60 is the doubled-base
global bound, not an improvement over PR442's length 30 on
the t-line.

## Public inputs inspected

The coordination discussion was read through the PR442 handoff.
The following immutable public proofs were read for this review:

- PR167, `063da90fc4543304e87e701cdefcc08225412f17`,
  `research/conductor-normalization/sharper-hm-regularity/PROOF.md`.
- PR437, `50e82ed233cd7729c38608194f990376eb832418`,
  `research/hm/paired-collision-filtration/PROOF.md`.
- PR439, `bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b`,
  `research/hm/paired-collision-endpoint/PROOF.md`.
- PR440, `829e03411d04511f6cf04860bf18db4a70b12448`,
  `research/hm/degree-six-structural-reduction/PROOF.md`.
- PR441, `6d81d9500f42ae31bef6d3150cf3ba513c28502b`,
  `research/hm/generic-quadratic-surjectivity/PROOF.md`.
- PR442, `2072baf63868a309366a7d3ae54dc1132e56adb7`,
  `research/hm/endpoint-pencil-torsion/PROOF.md`.

Their exact links and blob identities are recorded in PROOF.md.
The published primary resolution is retained as an imported
mathematical input, not claimed as a fresh matrix or primary-page
verification. No exhaustive novelty or literature conclusion is
made. No selected HM/source-instance evaluation, random sample,
checker, or large computation was performed for this review.
