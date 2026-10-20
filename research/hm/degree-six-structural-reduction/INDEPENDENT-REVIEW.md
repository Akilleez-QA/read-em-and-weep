# Independent mathematical review

## Verdict and exact reviewed edition

**PASS within the stated imported hypotheses and exclusions.**

Reviewed file: `PROOF.md`, “Two exact structural models for the
order-six coefficient quotient.”

Reviewed SHA-256:
`3a1550676140a8558c417838a017488bf9d45c100e125f8b487ffadd533df3eb`.

This is an independent mathematical audit, not formal verification.
The complete argument was checked, including all twists, connecting
maps, incoming images, the exact primary-module presentation, and the
scope of the prior-work comparison. The two minor terminology
corrections requested during review are incorporated in the bound
edition. No substantive proof defect remains.

## 1. Input and twist audit

For the normalized rank-two bundle, `F^vee = F(1)` gives

    H^3(F(s)) = H^1(F(-s-4))^vee,
    H^4(F(s)) = H^0(F(-s-4))^vee.

Tensoring the pinned section resolution by `F^vee(t)` produces exactly

    E_0(t) = 15 F(t-3) + 4 F(t-2),
    E_1(t) = 35 F(t-4),
    E_2(t) = 20 F(t-5),
    E_3(t) =  2 F(t-7).

No shift is lost in passing from the section resolution to this
resolution of `End(F)(t)`. Local freeness preserves exactness.

At `t=1`, the groups controlling `H^3(End(F)(1))` are

    H^3(E_0(1)) = 15 M_{-2}^vee + 4 M_{-3}^vee = 0,
    H^4(E_1(1)) = 35 H^0(F(-1))^vee = 0,

followed by groups above degree four. Thus `H^3(B(1))=0` follows.
This does not imply `H^2(B(1))=0`; the latter remains in the theorem.
The trace splitting is valid over the specified field of complex
numbers.

## 2. Koszul and incoming-image audit

The degree-(2,3) regular sequence gives the correctly twisted sequence

    0 -> B(1) --(-v,u)--> B(4)+B(3)
      --(u,v)--> I_N B(6) -> 0.

Its exactness is scheme-theoretic. Neither smoothness of `N` nor
removal of its singular or quadruple-root locus is used.

Writing `J=I_N B(6)`, the established vanishings
`H^2(B(4)+B(3))=0` and `H^3(B(1))=0` imply `H^2(J)=0`.
The first long exact sequence identifies

    H^1(J)/im(alpha) = H^2(B(1)).

The restriction sequence identifies

    ker(gamma) = im(delta)

and makes `H^1(B(6)) -> H^1(N,B(6)|_N)` surjective.
Most importantly, `gamma alpha` is the original map `(u,v)` on
`H^1(B(4))+H^1(B(3))`, not a substitute multiplication map.
Consequently the kernel after quotienting is

    H^1(J)/(im(alpha)+im(delta))
      = H^2(B(1))/im(beta delta).

This proves exactly

    0 -> coker(T) -> Q -> H^1(N,B(6)|_N) -> 0,
    T = beta delta.

The incoming contribution from restricted global sections has not
been discarded. In particular the manuscript correctly refuses the
unjustified equality `Q = H^1(N,B(6)|_N)`. The two stated vanishing
conditions are jointly necessary and sufficient for `Q=0`; no
canonical splitting is claimed.

## 3. Natural primary-module surjections

For `t>=3`, the three groups needed to show `H^2(K(t))=0` are

    H^2(E_1(t)) = 35 H^2(F(t-4)) = 0,
    H^3(E_2(t)) = 20 M_{1-t}^vee = 0,
    H^4(E_3(t)) = 2 H^0(F(3-t))^vee = 0.

The exceptional `H^2(F)` twist is `-2`, corresponding to `t=2`,
which is outside this range. The two kernel sequences therefore
prove the asserted natural surjections at `t=3,4,6`.

All surjections arise from the same twisted resolution and commute
with multiplication by homogeneous polynomials. The source groups
at these twists are correctly

    15 M_0 + 4 M_1,
    15 M_1 + 4 M_2,
    15 M_3.

Both four-copy incoming summands land in `M_4=0`. Hence
`15 bar M_3 -> Q` is surjective, but an isomorphism would require
an additional kernel calculation. The manuscript retains that kernel.

## 4. Exact cokernel and source reduction

At `t=6`, the first kernel sequence also gives `H^2(L(6))=0`,
using precisely

    H^2(E_2(6)) = 20 H^2(F(1)) = 0,
    H^3(E_3(6)) = 2 M_{-3}^vee = 0.

Thus `H^1(E_1(6)) -> H^1(K(6))` is surjective. Combined with
`H^2(K(6))=0`, this proves

    35 M_2 --D--> 15 M_3 -> H^1(B(6)) -> 0.

There is no unmentioned higher-kernel hypothesis. The map is induced
by the linear block `35 O(-5) -> 15 O(-4)`; the other block has zero
target in `H^1`.

Naturality and the degree-three/four surjections identify the full
inverse image of the original denominator as

    im(D) + 15(uM_1+vM_0).

Finally the same linear block is `S`-linear with its degree shift.
It takes `35uM_0` into `15uM_1`; the other possible degree-two
denominator is `vM_{-1}=0`. Thus the source really may be reduced,
and the final presentation is exact:

    35 bar M_2 --bar D--> 15 bar M_3 -> Q -> 0.

The unresolved incoming image of `bar D` is essential. The proof
does not replace its cokernel by its target. Ring regularity of
`u,v` is also correctly distinguished from the impossible
positive-degree regularity of a nonzero finite-length module.

The dimension bounds, the common-annihilator sufficient test, and
the doubled paired-coefficient formula all follow from these exact
statements. Neither `dim bar M_3` nor `rank(bar D)` is computed.

## 5. Exact public pins and bounded comparison

The following immutable repository files were read during review:

- PR439 endpoint proof, commit
  `bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b`,
  path `research/hm/paired-collision-endpoint/PROOF.md`,
  Git blob `8b420be9fd49374981a7dfc59058483a4ae4dbfa`.
- PR437 filtration proof, commit
  `50e82ed233cd7729c38608194f990376eb832418`,
  path `research/hm/paired-collision-filtration/PROOF.md`,
  Git blob `9697423e880070cdf34cbc3548f5a2b32b2a40a0`.
- PR167 strongest-bound proof, commit
  `063da90fc4543304e87e701cdefcc08225412f17`,
  path
  `research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md`,
  Git blob `58785a8799c43fd2c7da089d0ddc5e05822132a9`.
- The same PR167 commit, path
  `research/conductor-normalization/sharper-hm-regularity/PROOF.md`,
  Git blob `31c7475d89b6c833696b6e915724e5d6d4221e42`.
- PR171 coordinate-socle proof, commit
  `8236d128910c667610361966011456aa9478747f`,
  path
  `research/conductor-normalization/socle-syzygy-detector/PROOF.md`,
  Git blob `d450a7e58e0abd39bc0ba88223f2df22b2d4e674`.

PR167's primary resolution and cohomology facts are imported
mathematical inputs. This audit checks their stated consequences,
not a new derivation of the HM monad from explicit matrices.
The source links in the manuscript use the exact commits above.

PR439 already defines `Q` and identifies the doubled paired
endpoint. PR167 already supplies the tensor resolution and endpoint
dimension bound. PR171 already includes `H^3(B(1))=0`, but its
five-coordinate Koszul transgressions concern the degree-minus-one
`H^2(B)` socle, not this quotient. The reviewed contribution is the
explicit two-layer surface description and the exact reduced
primary-module presentation, relative to those inspected inputs.
No exhaustive repository or literature novelty claim is warranted
or made.

## 6. Review boundary

No actual HM or source-instance evaluation, multiplication-matrix
construction, rank calculation, generator, checker, or large
computation was performed. No public repository write was made by
this review. Local hashing binds the reviewed text only.

The proof leaves `Q` unresolved. It supplies no actual source
representative, primitive, ideal-membership certificate, module
lift, pure-square conclusion, or algebraicity result. It correctly
does not infer nonzero ambient cohomology from a hypothetical
nonzero ideal-coefficient group.

## 7. Bound summary check

The accompanying `README.md` was also read in full and passes as a
summary of the bound proof. Its reviewed SHA-256 is
`eb7e2037d6dc18159f91ca4016880c3850c922faac1cdba8699de051509b702f`.

It retains both terms in the surface exact sequence, the incoming
primary differential, the fifteen-copy multiplicity, and the fact
that `Q` is unresolved. It does not identify a two-dimensional
primary group with `Q` or assert vanishing from the regular-sequence
hypothesis.
