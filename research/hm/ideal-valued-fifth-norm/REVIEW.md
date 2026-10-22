# Independent deductive review

## Verdict and exact object

**PASS, conditional on the stated pinned geometric inputs.** No blocking
mathematical error was found in the ideal-valued norm construction or its
second-symbol quotient. This is an independent deductive review, not a
proof-assistant check and not an independent reproving of all upstream HM
theorems.

- Reviewed: `PROOF.md`, 7,673 bytes.
- SHA-256: `23794c5f293659d888f7284c7f6e6ee8727ae04175c3bd385594ae0c1afc85e8`.
- Review date: 2026-10-22 UTC.
- The reviewed proof was not modified during this review.

The conclusion is a canonical scalar/ideal-valued shadow of the actual
boundary class, not a nonvanishing theorem, an adjoint extension theorem,
or an algebraicity conclusion.

## Pinned dependency checks

The following exact files were retrieved read-only through the authorized
GitHub connector. The quoted SHA values in this list are returned Git blob
identifiers, distinct from the SHA-256 of the reviewed local proof above.

1. [Actual fifth-neighborhood ladder](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md),
   commit `8d8b5be4ce62c3055bb53be9e16d29cc63072f04`,
   blob `81e4b7ddf79d2c4e26ac0c99517117fe2ca63133`.
   Its section 2 supplies the actual global `J4`, the restriction
   `J4|Q = a^3 h N`, the exact sequence with kernel `B_Q(4)`, the positive
   boundary convention, and the identity modulo `im(beta2_a)`.

2. [Fourth-square invariance](https://github.com/Akilleez-QA/read-em-and-weep/blob/2874402c884a6b426cfd521a674c962a738f84a6/research/hm/fourth-square-invariance/PROOF.md),
   commit `2874402c884a6b426cfd521a674c962a738f84a6`,
   blob `d773154ee28fac80a2f01225fd6c9b3c40e20762`.
   Section 3, equation (5), identifies the image sheaf of `tr(N-)`
   exactly with the square of the actual Serre ideal, `I_Z^2(6)`.
   Thus the map is surjective onto that sheaf, not necessarily on global
   sections or on first cohomology. The proof under review needs only
   sheaf surjectivity.

3. [Third-lift uniqueness and boundary variation](https://github.com/Akilleez-QA/read-em-and-weep/blob/449a8df60662bd7a1d93e318ea4f7e6dab28e5ad/research/hm/third-lift-uniqueness/PROOF.md),
   commit `449a8df60662bd7a1d93e318ea4f7e6dab28e5ad`,
   blob `15757d06b0047aaa42c63608618a810786604ac6`.
   Sections 3 and 4 give zero boundary variation for a change of even
   fourth lift over a fixed third lift and second-symbol variation for
   classified completion changes. These statements hold with
   `a,h,b,U_a` fixed. They do not authorize arbitrary changes of the
   source correction, normalization, or marking. The reviewed proof's
   references to classified changes must, and can, be read in precisely
   this scope. No constant-rank assumption is imported.

4. The further [actual third-square theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md),
   at commit `8d8b5be4ce62c3055bb53be9e16d29cc63072f04`,
   blob `66ad91bc7026203d340a7988f679caa1b98b02ce`, was checked for the
   provenance of the square-ideal image. It states that image directly
   in section 1. The generic Serre-pair trace formula has coefficients
   `2fg`, `g^2`, and `-f^2`; over characteristic zero their generated ideal
   is `(f,g)^2`. This is a universal local identity, not an evaluation
   of an actual HM coefficient or matrix.

These checks verify that the cited files say the inputs used. They do not
claim an independent audit of every geometric theorem on which those
files in turn depend.

## Detailed mathematical checks

### 1. Twists and the q-adic layer

The quadric equation has degree 2. Multiplication by `q^4` adds 8 to a
twist. Thus the adjoint kernel is `B_Q(12-8) = B_Q(4)`, and the scalar
kernel for the norm is `O_Q(24-8) = O_Q(16)`. These are actual sheaf
identifications because `q` is a nonzerodivisor on the ambient space
and `B` is locally free. Smoothness of `Q` is unnecessary.

The complete degree accounting is consistent:

- `J4` has twist 10 and `K=aJ4` has twist 12.
- `f=a^4h` has twist 10, and `fN` has twist 12.
- `n(K)` has twist 24.
- `c_ij` has twist 4, and `tr(N c_ij)` has twist 6.
- `f tr(N c_ij)` has twist 16; multiplication by `q^4` restores twist 24.

The notation `q^4 c_ij` means the canonical last-layer injection, not a
choice of division by a function on `5Q`. Its coefficient on `Q` is
unique. Any extension of that coefficient used to multiply locally
gives the same result modulo `q^5`.

### 2. Norm and polarization factor

For a trace-free rank-two endomorphism, Cayley-Hamilton over a
characteristic-zero algebra gives `L^2 = tr(L^2) Id / 2`. Cyclicity of
trace gives exactly

    n(L+D)-n(L) = tr(LD)+n(D).

There is no missing factor of 2. Inserting `D=q^4 c_ij` makes the
quadratic term a multiple of `q^8`, which is zero on `5Q`. The remaining
product only sees `K|Q`, since `q^4` annihilates one additional factor
of `q`. Consequently equation (5), including its sign, is correct.

### 3. Global scalar lift

The quadric restriction sequence gives

    H^1(P4,O(16)) -> H^1(Q,O_Q(16)) -> H^2(P4,O(14)).

Both outer groups vanish by intermediate line-bundle cohomology on
projective 4-space. The scalar restriction map from `5Q` to `4Q` is
therefore surjective on global sections. This proves existence of `P`
without constructing an adjoint lift or assuming that `Q` is smooth.

The same argument works in the physical-center-even sector: the maps
are equivariant, and taking the even summand is exact in characteristic
zero. In particular `P` can be chosen even.

### 4. Local-to-global construction and sign

An affine cover permits local trace-free lifts because the adjoint
restriction map is a surjective map of coherent sheaves. Both `n(K_i)`
and `P` restrict to `n(K)` on `4Q`, so their difference has a unique
coefficient `w_i` in `O_Q(16)`.

With the stated positive coboundary convention,

    w_j-w_i = f tau(c_ij).

Thus the classes of `w_i` glue in `C_f`. The connecting homomorphism
from `H^0(C_f)` sends that glued section to the same positive cocycle
`f tau(c_ij)`, not its negative. Under the identification of `J_f` with
`I_Z^2(6)`, its class is precisely `tau_*(delta_5 K)`.

### 5. Independence of choices and divisors

Changing a local lift by `q^4 D_i` changes `w_i` by `f tau(D_i)`, so
does not change its quotient section. A change of scalar lift is
uniquely `P -> P+q^4 r` for a global `r` in `H^0(O_Q(16))`. It changes
the quotient section by the negative image of `r`, exactly the
ambiguity divided out in equation (6). Refining the cover changes
neither the glued quotient section nor its connecting class.

Multiplication by nonzero `f` is injective on the ideal sheaf because
`Q` is integral and `I_Z^2` is a subsheaf of `O_Q`. It is therefore an
isomorphism onto `J_f`, including along the zero divisor of `f`. No
inverse of `f` is being asserted in `O_Q`, and no reduced-support or
saturation replacement of `I_Z^2` occurs.

The long exact sequence for `0 -> J_f -> O_Q(16) -> C_f -> 0`, together
with `H^1(O_Q(16))=0`, gives exactly the quotient isomorphism (7).
This makes the construction canonical for fixed `K` and the stated
source data. Under classified completion changes, the further quotient
by `tau_*(V_a)` is essential; the raw norm class need not be invariant.

### 6. Second-symbol quotient and trace kernel

For every linear map `T` and subspace `V`, the map from the source
quotient to the target quotient by `T(V)` is well defined. Applying
this fact to `tau_*` proves equation (9), with no rank condition.
The pinned completion-variation theorem supplies exactly the required
change in `V_a`; neither `tau_*(V_a)=0` nor an inverse of `beta2_a` is
assumed.

The sheaf image theorem gives the short exact trace sequence. Its long
exact cohomology sequence yields

    ker(tau_* on H^1(B_Q(4))) = im H^1(C_N).

In particular the exact kernel of the induced quotient map is

    ker(bar_tau_a) = (im H^1(C_N) + V_a)/V_a.

Equivalently it is `im H^1(C_N)` modulo its intersection with `V_a`.
This confirms the proof's statement: if the shadow vanishes, subtracting
some element of `V_a` leaves a trace-kernel class, not necessarily zero.
The shadow is faithful precisely if `im H^1(C_N)` is contained in
`V_a`. No surjectivity of the trace map on `H^1` is needed.

### 7. Ordinary scalar loss and limited conclusions

The ordinary scalar cocycle lies in `O_Q(16)` and has zero first
cohomology class. This does not force its class in `H^1(J_f)` to be
zero. The nontrivial quotient section measured by (7) is exactly where
this ideal-valued trace information can remain.

For two twist-12 sections, the polarized trace difference also has a
`q^4` coefficient of twist 16; its ordinary scalar first cohomology
vanishes for the same reason. This says nothing about all possible
scalar invariants. A `q^3` norm coefficient and the `q^4` connecting
coset are different data. The proof correctly makes no inference from
nonzero fourth-neighborhood square or nilpotency index to nonzero
fifth-neighborhood adjoint boundary.

## Findings and verification limits

- No blocking correction is required for the reviewed argument.
- The scope of “classified changes” remains the fixed `a,h,b,U_a`
  scope of the pinned theorem, not arbitrary normalization changes.
- The actual value of the norm coset, its class modulo `tau_*(V_a)`,
  and the trace-kernel cohomology remain unresolved.
- Verification consisted of reading the proof and pinned dependencies,
  checking the universal identities, sheaf exact sequences, twists,
  signs, and logical implications, and hashing the reviewed bytes.
- No selected actual HM/source coefficient, point, derivative, matrix,
  or rank was evaluated. No large computation, external write, or
  proof-assistant formalization was performed.
