# PH-R independent review of PH01 — 2026-10-16

**Disposition: ACCEPT the narrow physical homogeneous-source identification for F12 and F34, conditional on the explicit pinned source premises below. No global geometric, coefficient-program, or arithmetic admission follows.** No producer correction is required for this theorem.

Only `test_independent.py` and this report were written in the review directory. Read all five producer files and the marker, including the complete parsed certificate, and checked its complete reconstruction. Read the pinned physical frame/character notes, physical-current binding and source excerpt, primitive shape/exponent metadata, finite whole-source proof and independent/degree reviews, and null's complementary-pair proof and independent review. Source code and stored physical coefficients were not executed. No physical polynomial coefficient was multiplied, differentiated, expanded, evaluated or specialized. No physical scan, resource-budget change, commit or post was performed.

## Explicit premises and provenance

Acceptance imports the authenticated primitive/contraction identities and the specified physical bundle model; it does not reprove their historical polynomial checkers. In particular:

- `08b73637d4136f91606aad332c46cafd064417f8`, `frames-and-poles.md` §§1–2 supplies honest weighted homogeneous primitives, `v_local=tau*v_finite`, the coherent common line transition `nu_local=tau^(1/2)*nu_finite`, and the actual source splitting dictionary. `closure-and-characters.md` §2 supplies the physical deck linearization and cancellation of central E-frame signs.
- `ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18`, `physical_current_source_binding.py`, `hm-pinned-model.json` and `hm-pinned-source-formulas.js` specify `g_ab=D_b*(P_a I_b)^t*D_a^-1`, the absolute owner constants, logarithmic jets, both endpoint connections, bit conventions, and ordered source orientation. Constants fixed at a frozen source point do not make moving frames constant functions.
- `82a8785d0a23e8d4e44e9ca4f52c8bb24fdadbdc` supplies the reviewed **actual finite** whole-F12 identity `P=(product C)F`, with the per-tuple degree bound and uniform 217/210 bound, conditional on its authenticated contraction identities.
- `02d0e727ffb95dfd9281906cc284c56e8bffd018` supplies null's finite F34 polynomial/degree property on a fixed ordered triple. It permits an unsorted inverse image to establish the property for the freshly evaluated increasing target triple. It supplies no identity between two sorted alternating cochains.

All nine direct source SHA256 pins and the five finite producer hashes are authenticated from local Git objects by the producer authentication path. The independent suite separately checks all nine direct digests and compares the **entire** certificate to reconstruction. The finite marker's Git blob pin is checked as well. These are byte/provenance checks; the mathematical premises remain explicit. Acceptance-comment URLs in the certificate are references, not independently fetched evidence in this review.

## Physical identification audited independently

The chart identity is a coefficientwise identity of the elementary multilinear lifts: invert any subset of coordinates and each term acquires the same `tau`. Therefore I column r has weight r, P row s has weight -s, and transposition gives K entry `(r,s)` weight `r-s`. For `sigma_rr=1-2r`, the common D transition contributes `(sigma_rr-sigma_ss)/2=s-r`. It cancels the K weight exactly. Owner constants remain fixed throughout. The physical transition matrix thus agrees with its pulled-back finite matrix **before differentiation**. The splitting dictionary has `2d+p=0` in every listed block; physical I and P have opposite residual half-weights, cancelling in End normalization. These conclusions use the pinned construction, rather than inferring a frame from a desired output degree.

The actual finite square line ratios are constant multiples of `((x²-1)/x)^m`. Multiplication by the common t after inversion gives t for mask0 and `1-t²` for mask1. Half logarithmic differentiation gives

    Q_t = [1/(2t) - m*t^-2*rf(1/t)] sigma,
    Q_t(mask0)=sigma/(2t), Q_t(mask1)=-t*sigma/(1-t²).

The mask0 term is mandatory. In `partial K+Q_b K-K Q_a`, the derivative of `tau^(r-s)` is cancelled by precisely the common part of **both** endpoint Q's. What remains is `tau^(r-s)*(-t^-2)*T_x`. The independent controls cross multiply the actual rf formula against artificial Laurent K entries for all matrix indices and endpoint mask bits. They detect omission of the common Q term.

The invariant vector is `-z*partial_t` and `y=z/t²`. Stripping the new local z therefore supplies a second minus, leaving the positive `t^-2` factor per inverted pair direction. Separately, `dlog x=-dt/t` combined with that invariant-vector minus gives `q_local=deltaMask/t`. This q is the gerbe coefficient, not rf. Consequently both the ordered gerbe `(15/4)q01,p*q12,q` and the normalized trace correction with coefficient `-1/4` have the same pair character. Closed matrix-index cycles telescope the K weights. Matrix multiplication order and source-slot order remain fixed.

Thus the physical source, before introducing any candidate numerator, obeys

    F_pair,local = product_(i in pair, inverted) t_i^-2 * F_pair,finite(pullback).

The pair character is `(-2,-2,0,0)` or `(0,0,-2,-2)`. The completed scalar's separate `tau^-4` transition is not substituted for this first pair-source character. Central deck signs cancel in the normalized trace by the imported source linearization; the stripped pair retains precisely its pair deck character.

## Hidden v0 factors, divisor degrees and fixed owners

This is the critical primitive bridge. The ordinary affine denominator degree is **4** for both carrier0 and auxiliary5, and 5 for carriers1–4. For auxiliary5, with homogeneous `a=v0*v1*v3*v4`,

    hom_4(d) = -v1²*v3*v4 = -v1*a/v0.

It is not the degree5 expression `-v1*a`. Starting from the canonical weighted rational expression, multiplying by `a²` yields `-v0^(2-e)*v3*v4*hom_(4+e+w)(num)`, hence `-v3*v4*hom_(6+w)(num)`. The exponent bound ensures `e<=2`. Using denominator degree5 would lose the required padding at the boundary. Carrier0 similarly has `hom_4(d)=-H0/v0` and padding `1-e`; primaries1–4 have e=0. The independent metadata check visits all 161 nonempty I/P entries and verifies the canonical padding is nonnegative without coefficient arithmetic. Zero entries remain zero.

H has assigned degree5 for primary carriers and4 for auxiliary5. Legal sections are Y of degree1 and `X(X²-Y²)` of degree3; their infinity coefficients are t and `1-t²`. Thus each fixed C owner has per-axis degree `14d + 1_(axis in pair)*deg(ell)`. Original owner standard equations remain Y or X, with local coefficients `(1,t)` or `(x,1)` as appropriate. A representation chart is not a new owner standard tag. Its common overlap still requires those original standard equations and owned carrier/legal sections to be units. Occurrences are never merged.

Combining these independently identified physical transitions with the imported finite identity yields `product C_local * F_local = t^(D_C+n_pair)*P_finite(pullback)`. The finite degree theorem makes every reversed exponent nonnegative. This is exactly the polynomial candidate's chart expression, and proves the claimed physical numerator equality. Polynomiality on the full representation chart concerns the cleared numerator; division recovers F only on the stated overlap. The argument works directly for both ordered pairs without renaming or sorting owners.

## Verification and retained boundaries

The independent stdlib suite has **10 tests**. It covers exact elementary lifts on all16 charts; literal primitive exponent/padding metadata; actual infinity rf/Q and ordinary tangents; formal half-weight D cancellation and chain balances; artificial noncommutative matrix/gerbe transport on all16 charts for both pairs; legal sections, C degrees, fixed tags and monomial reversal; order-boundary examples; and mutation rejection. The artificial gerbe is nonzero for both pairs. Negative controls distinguish dropped endpoint terms, lost signs, reversed matrix products, wrong coefficients, changed divisor degrees, reassigned tags and sorted source slots. These artificial controls support the universal algebra and do not replace the pinned physical-source premises. Two initial negative controls were vacuous (a zero omitted endpoint and an unchanged assigned value); these reviewer-only controls were corrected before the final runs.

Final commands, from the repository root:

    python -B -m unittest discover -s research/codex-swarm/physical-homogenization -p 'test_*.py' -v
    python -B -O -m unittest discover -s research/codex-swarm/physical-homogenization -p 'test_*.py' -v

Both pass **20/20**, comprising producer10 and independent10. Unittest checks remain active under `-O`.

The five producer SHA256 values matched the marker before review and after the final runs, and the marker bytes were unchanged:

| File | SHA256 |
|---|---|
| PROOF.md | `73896848cf224631578aa71b765a51f43c97ac1541e8d56ec1d146ad448ac1ab` |
| README.md | `883ad5dbb103d425a054d60bef639b3568fe3b9121f0a7e4f880d697d5559beb` |
| frames.py | `841b8ebd342ae0c45d92499fc712d94051729d27e8137279fb14e09710246c6e` |
| physical-source-certificate.json | `945551c886bd399bfa6cab8f1bc6bd144059dc2656ada5dfb546ce6b71a2a3c5` |
| test_frames.py | `1cad972ca549e7df43bc0dc096249fd87361014bad3126b10caf54c31a78b58e` |

Accepted scope is the actual pair-source homogeneous/infinity equality and cleared numerator identification under the listed premises, for the intended fresh source order and its alternating extension. Repeated-source zeros retain null's imported convention. This supplies one missing input to the combined-pole implication. It does not instantiate complete standard-B/inner or weighted standard-target coefficient programs, source payloads or supports; identify historical order or sorted renamed cochains; reprove first-current tracelessness; assemble a detector; compute an obstruction; or release arithmetic/resource gates. All producer global gates remain false.
