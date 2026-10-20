# Two exact structural models for the order-six coefficient quotient

## Statement and contribution

Work over the complex numbers. Put Y = P^4, let F be the normalized
Horrocks–Mumford bundle, and put B = End_0(F). Retain the binary-quartic
invariant sections u = t_2 and v = t_3, of degrees two and three, with
N = V(u,v) the global complete-intersection collision surface. All
restrictions below are scheme-theoretic; no singular or quadruple-root
stratum is removed.

The previously identified order-six quotient is

    Q = H^1(Y,B(6)) / (u H^1(Y,B(4)) + v H^1(Y,B(3))).

The following are new structural descriptions of that quotient, using
only the pinned cohomological inputs recorded below.

1. There is a canonical exact sequence

    0 -> coker(T) -> Q -> H^1(N,B(6)|_N) -> 0,

   where

    T: H^0(N,B(6)|_N) -> H^2(Y,B(1))

   is the composite of the two explicitly specified connecting maps in
   Section 2. In particular Q = 0 if and only if BOTH T is surjective
   and H^1(N,B(6)|_N) = 0. Merely establishing the latter vanishing does
   not, without another argument, settle the degree-six endpoint.

2. Write M = H^1_*(F), and put bar M = M/(u,v)M. A choice of the pinned
   minimal section resolution induces an exact presentation

    35 bar M_2 --bar D--> 15 bar M_3 -> Q -> 0.

   Here bar M_3 = M_3/(uM_1 + vM_0) has dimension at most two. The map
   bar D is induced by the linear block of the first differential of
   that section resolution. It is retained, not evaluated or dropped.
   In particular, 15 bar M_3 surjects onto Q; bar M_3 = 0 is sufficient
   for Q = 0, but is not asserted necessary.

These statements replace an isolated End(F)-multiplication question by
(a) an exact surface restriction/transgression mechanism and (b) an
exact presentation over a quotient of the primary rank-two cohomology
module. They do not prove Q = 0. Neither presentation evaluates an HM
multiplication map or a selected source.

## 1. Exact inputs and elementary consequences

The public primary-cohomology and section-resolution inputs are:

    F^vee = F(1),
    M_s = H^1(F(s)) = 0 for s < 0 or s >= 4,
    (dim M_0, dim M_1, dim M_2, dim M_3) = (5,10,10,2),
    H^2(F(s)) = 0 unless s = -2,
    H^0(F(s)) = 0 for s < 3,

and the exact locally free resolution

    0 -> 2 O(-8) -> 20 O(-6) -> 35 O(-5)
      -> 15 O(-4) + 4 O(-3) -> F -> 0.                 (R)

The numerical dimensions and resolution are imported from PR167, not
obtained here by evaluating their differentials. Serre duality gives

    H^3(F(s)) = M_{-s-4}^vee,
    H^4(F(s)) = H^0(F(-s-4))^vee.

Tensor (R) by F^vee(t), and write the resulting exact resolution of
G(t) = End(F)(t) as

    0 -> E_3(t) -> E_2(t) -> E_1(t) -> E_0(t) -> G(t) -> 0,

where

    E_0(t) = 15 F(t-3) + 4 F(t-2),
    E_1(t) = 35 F(t-4),
    E_2(t) = 20 F(t-5),
    E_3(t) =  2 F(t-7).                               (1)

Tensoring is exact because F^vee is locally free. For an exact
resolution of this length, the groups H^{i+j}(E_j(t)), j = 0,1,2,3,
control H^i(G(t)); their simultaneous vanishing implies H^i(G(t)) = 0.
This follows by splitting the resolution into its three short exact
kernel sequences. No surjectivity on global sections is presumed.

We will use PR167's proved H^2(B(t)) = 0 for t >= 2. We additionally
need the following consequence of (1):

    H^3(B(1)) = 0.                                    (2)

Indeed, at t = 1 the only potentially relevant diagonal terms are

    H^3(E_0(1)) = 15 M_{-2}^vee + 4 M_{-3}^vee = 0,
    H^4(E_1(1)) = 35 H^0(F(-1))^vee = 0.

The remaining groups are H^5(E_2(1)) and H^6(E_3(1)), which vanish on
P^4. Thus H^3(G(1)) = 0. The trace splitting
G(t) = O(t) + B(t) then proves (2).

Vanishing (2) was already included in the broader negative-twist/duality
input used in PR171; this is a direct proof from the narrower PR167
inputs, not a new vanishing theorem.

This does NOT assert H^2(B(1)) = 0. Its known upper bound is thirty,
and it will remain in the exact sequence. No value or vanishing of
H^0(B(3)) is used anywhere.

## 2. The Koszul transgression and surface restriction

Let J = I_N B(6), A = B(1), and P = B(4) + B(3). The regular sequence
(u,v) gives two exact sequences

    0 -> A --(-v,u)--> P --(u,v)--> J -> 0,           (3)
    0 -> J -> B(6) -> B(6)|_N -> 0.                  (4)

The order of the two summands fixes the displayed signs. Since B is
locally free, tensoring the Koszul resolution preserves exactness,
including at the singular locus of N.

Write the relevant maps in the long exact sequences as

    alpha: H^1(P) -> H^1(J),
    beta:  H^1(J) -> H^2(A),
    gamma: H^1(J) -> H^1(B(6)),
    delta: H^0(N,B(6)|_N) -> H^1(J).

The map in the statement is the actual composite

    T = beta o delta.                               (5)

The first long exact sequence, together with H^2(P) = 0, proves

    coker(alpha) = H^2(A),

where the isomorphism is induced by beta. Also H^2(P) = 0 and
H^3(A) = 0 imply

    H^2(J) = 0.                                     (6)

Consequently the second long exact sequence yields

    H^1(J) --gamma--> H^1(B(6))
       -> H^1(N,B(6)|_N) -> 0,                       (7)

and ker(gamma) = im(delta).

The composition gamma o alpha is precisely multiplication by (u,v)
on H^1(B(4)) + H^1(B(3)). Its cokernel is therefore Q, with the SAME
multiplication maps as in the order-six endpoint theorem. Quotienting
(7) by im(gamma o alpha) gives a surjection

    Q -> H^1(N,B(6)|_N).

Its kernel is

    im(gamma) / im(gamma o alpha)
      = H^1(J) / (im(alpha) + ker(gamma))
      = H^2(A) / beta(im(delta))
      = coker(T).

The indicated identifications give a canonical injection of coker(T)
into Q, proving

    0 -> coker(T) -> Q -> H^1(N,B(6)|_N) -> 0.        (8)

No splitting of (8) is asserted. Since all groups are finite dimensional,
this also gives the exact dimension identity

    dim Q = dim H^1(N,B(6)|_N) + h^2(B(1)) - rank(T).

Thus a surface-vanishing argument alone can leave a residual quotient
of H^2(B(1)). Conversely, a proof that T is surjective can still leave
the surface H^1. This identifies two distinct dependencies rather than
silently identifying Q with either one.

One can view T as the two-step connecting operation of the Koszul
complex B(1) -> B(4)+B(3) -> B(6), but equation (5) defines it without
any spectral-sequence convention. Sections of B(6)|_N that already
extend to Y lie in ker(T), since their first connecting map is zero.

## 3. Natural primary-module surjections

Let K(t) = im(E_1(t) -> E_0(t)) and
L(t) = im(E_2(t) -> E_1(t)). The kernel sequences are

    0 -> E_3(t) -> E_2(t) -> L(t) -> 0,
    0 -> L(t) -> E_1(t) -> K(t) -> 0,
    0 -> K(t) -> E_0(t) -> G(t) -> 0.                (9)

For every t >= 3, the following groups vanish:

    H^2(E_1(t)) = 35 H^2(F(t-4)) = 0,
    H^3(E_2(t)) = 20 M_{1-t}^vee = 0,
    H^4(E_3(t)) = 2 H^0(F(3-t))^vee = 0.

The only exceptional H^2(F(s)) twist is -2, which cannot equal t-4
when t >= 3; the other two vanishings follow from the stated degree
ranges. The first two sequences in (9) then give H^3(L(t)) = 0 and
H^2(K(t)) = 0. The last sequence yields a natural surjection

    H^1(E_0(t)) -> H^1(G(t)) = H^1(B(t))             (10)

for every t >= 3. The equality uses H^1(O(t)) = 0 and the trace
splitting, not any assertion about global trace-free sections.

The maps (10) commute with multiplication by every homogeneous
polynomial: they arise from a single graded sheaf resolution and its
twists. In particular they commute with u from t = 4 to t = 6 and
with v from t = 3 to t = 6.

At these three degrees the sources are

    H^1(E_0(3)) = 15 M_0 + 4 M_1,
    H^1(E_0(4)) = 15 M_1 + 4 M_2,
    H^1(E_0(6)) = 15 M_3 + 4 M_4 = 15 M_3.

The four-copy summands map by u or v to M_4 = 0. The two commuting
surjective squares therefore induce a surjection

    15 [M_3/(uM_1 + vM_0)] -> Q.                    (11)

This is already a sufficient-condition reduction involving a primary
top cohomology group of dimension two. It is not an identification of
Q with fifteen copies of that quotient.

## 4. The exact primary-module presentation

We can retain the full kernel in (11). At t = 6 the first sequence in
(9) also gives H^2(L(6)) = 0, because

    H^2(E_2(6)) = 20 H^2(F(1)) = 0,
    H^3(E_3(6)) = 2 H^3(F(-1)) = 2 M_{-3}^vee = 0.

The second sequence in (9) now makes H^1(E_1(6)) -> H^1(K(6))
surjective. The already-proved H^2(K(6)) = 0 and the last sequence in
(9) show that the entire kernel of H^1(E_0(6)) -> H^1(B(6)) is the
image of H^1(E_1(6)). Thus there is an exact sequence

    35 M_2 --D--> 15 M_3 -> H^1(B(6)) -> 0.          (12)

The map D is the cohomology map of E_1(6) -> E_0(6). More explicitly,
it is induced by the linear block 35 O(-5) -> 15 O(-4) of (R); the
other block lands in 4 M_4 = 0. No entries or rank of D are evaluated.

By the commuting squares and surjectivity in Section 3, the inverse
image in 15 M_3 of

    u H^1(B(4)) + v H^1(B(3))

is exactly

    im(D) + 15 (uM_1 + vM_0).

Consequently

    Q = 15 M_3 / [im(D) + 15 (uM_1 + vM_0)].         (13)

Let bar M = M/(u,v)M. Because D is induced by a homogeneous linear
block, its reduction modulo (u,v) factors through 35 bar M_2. Indeed,
D(uM_0) is contained in 15 uM_1 by S-linearity, and M_{-1} = 0,
so the vM_{-1} term in degree two vanishes. Formula (13) proves the
claimed exact presentation

    35 bar M_2 --bar D--> 15 bar M_3 -> Q -> 0.       (14)

A choice of section-resolution bases presents bar D; no preferred
bases or canonical splitting of its image are asserted. The cokernel
is canonically the original Q via the constructed maps.

## 5. Consequences, exact next conditions, and exclusions

Write r = dim bar M_3, so r is 0, 1, or 2. Equations (11) and (14)
imply

    dim Q <= 15r <= 30,
    dim Q = 15r - rank(bar D).

Hence bar M_3 = 0 proves Q = 0. More generally Q = 0 is equivalent
to surjectivity of the induced map bar D in (14); nonzero bar M_3
alone does not imply nonzero Q. If r = 1, the endpoint bound improves
to dim Q <= 15. No value of r or rank(bar D) is supplied.

For a basis-free sufficient test, the dual of bar M_3 is the common
annihilator space

    { lambda in M_3^vee :
        lambda(u a) = 0 for every a in M_1,
        lambda(v b) = 0 for every b in M_0 }.

Its vanishing implies Q = 0; existence of a nonzero functional only
shows that this particular sufficient test fails. Since M_3 has
dimension two, the projective class of a possible nonzero functional lies in
the projective line P(M_3^vee). This is an exact structural criterion, not an evaluated
incidence calculation for the fixed binary-quartic invariants.

Regularity of (u,v) in the polynomial ring S guarantees the sheaf
Koszul resolution used in Section 2. It does NOT say that (u,v) is
regular on the nonzero finite-length module M. In particular it does
not justify setting bar M_3 to zero or deleting an incoming map from
(14). On a nonzero finite-length graded S-module any positive-degree
multiplication is nilpotent and cannot be injective on the whole
module. The ring regular-sequence argument and the primary module
question are different statements.

Under PR439's already-proved identification, the whole paired
order-six coefficient satisfies

    H^2(Z,I_D^6 E)_chi^vee = Q + Q.

Thus the exact presentation gives

    h^2(Z,I_D^6 E)_chi = 2 dim coker(bar D) <= 30r.

Either a proof of both surface conditions in (8), or a proof of
surjectivity in (14), would settle the whole coefficient at order six.
Neither is established here. A nonzero Q would still not establish a
nonzero image in unrestricted cohomology or any nonzero actual source
class. No actual high-order representative, primitive, module lift,
pure-square result, or algebraicity conclusion follows.

## Exact public dependencies and bounded prior-work comparison

- The endpoint being refined is PR439 at commit
  `bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b`:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b/research/hm/paired-collision-endpoint/PROOF.md
  That proof retains the End(F) multiplication quotient Q and does not
  include (8) or the primary-module presentation (14).
- The full paired filtration and the global complete-intersection
  N = V(u,v) conventions are PR437, commit
  `50e82ed233cd7729c38608194f990376eb832418`, proof blob
  `9697423e880070cdf34cbc3548f5a2b32b2a40a0`:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/50e82ed233cd7729c38608194f990376eb832418/research/hm/paired-collision-filtration/PROOF.md
- The section resolution, duality formulas, H^2(B(t)) vanishing for
  t >= 2, and the endpoint upper bounds are PR167, commit
  `063da90fc4543304e87e701cdefcc08225412f17`, proof blob
  `58785a8799c43fd2c7da089d0ddc5e05822132a9`:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md
- The same PR167 commit gives the primary cohomology Hilbert function
  and exact H^2(F) support, proof blob
  `31c7475d89b6c833696b6e915724e5d6d4221e42`:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/PROOF.md
  Its primary reference is Wolfram Decker, *Monads and cohomology
  modules of rank 2 vector bundles*, Compositio Mathematica 76 (1990),
  7–17: https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf

- For comparison, PR171 at commit
  `8236d128910c667610361966011456aa9478747f`, proof blob
  `d450a7e58e0abd39bc0ba88223f2df22b2d4e674`, gives a different
  coordinate-Koszul detector for the degree-minus-one H^2(B) socle:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/8236d128910c667610361966011456aa9478747f/research/conductor-normalization/socle-syzygy-detector/PROOF.md
  Its Section 1 already includes H^3(B(1)) = 0. The quotient and
  transgressions in that paper use all five coordinate sections, not
  the degree-(2,3) regular sequence or the present Q.

The comparison is bounded: the current coordination thread, the
pinned endpoint and filtration proofs, the two pinned PR167 proofs,
and the stated PR171 comparison were inspected. No claim of an exhaustive literature or
repository novelty search is made. The argument is a new structural
refinement relative to these stated inputs, not a resolution of Q.
No HM/source-instance evaluation, multiplication matrix, generator,
checker, or large computation was performed.
