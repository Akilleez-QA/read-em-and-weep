# Independent review: ramified fourth-neighborhood characteristic lines

**Verdict: PASS.** No blocking mathematical findings.

Reviewed on 2026-10-22. This review is pinned to `PROOF.md` with SHA-256

    c2230371df1f7e90fe857f4331be85f6caf49b601277eddcff7f118a8454d8fe

The review concerns the stated local theorem over the smooth open where the
intrinsic fourth-square scalar is a unit and the reduced matrix is regular
nilpotent. It does not certify unstated global extensions or any Bockstein
conclusion.

## Pinned inputs checked

The two dependency files were read at the exact commits cited in the proof:

- [PR687, fourth-square invariance](https://github.com/Akilleez-QA/read-em-and-weep/blob/2874402c884a6b426cfd521a674c962a738f84a6/research/hm/fourth-square-invariance/PROOF.md), Git blob `d773154ee28fac80a2f01225fd6c9b3c40e20762`. Sections 2 and 4 give the trace-free actual rank-two identity `J4^2=q^3 sigma I`, the scalar twist fourteen, and the nonempty regular-nilpotent locus. The restriction `J4|Q=a^3 h N` and independence under the classified lift changes are stated and proved there.
- [PR766, uniform full-scalar exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/a43b46c98e53716978d0a7750843f2224b4d2408/research/hm/uniform-full-scalar-exclusion/PROOF.md), Git blob `d76e4bc023c6f4544f7b3c5265a9ae7d9096416c`. Section 4 identifies its `S4` with PR687's `sigma`, gives `S4=a^3 h rho4`, and proves that this is a nonzero global section for every permitted nonzero source pair. It does not assert pointwise nonvanishing.

These support exactly the inputs used here. The intersection defining `U` is
nonempty: each constituent is a nonempty open of the integral quadric. No
re-audit of all earlier dependencies is claimed.

## Algebraic checks

1. **The ramified truncation has the asserted filtration.** The monic
   presentation makes `C_e` free over `S`, so `q` is a nonzerodivisor on
   `C_e`. Since `t^e=q`, `t` is a nonzerodivisor as well. Thus
   `t^j C_e/t^(j+1) C_e` is canonically a copy of `R=C_e/(t)`.
   In `B_e=C_e/(t^(4e))`, the nonzero layers are precisely those of
   degrees zero through `4e-1`. The lift of `sigma` is a unit on the
   stated open; changing that lift by a multiple of `q` has no effect
   on `t^(3e)s` in this truncation.

2. **Odd ramification cannot produce an invariant line direct summand.**
   On a trivialization of such a line, invariance gives a scalar `lambda`
   satisfying `lambda^2=t^(3e)s`. A nonzero leading coefficient in `R`
   has nonzero square. Consequently a nonzero square of an element of
   exact `t`-order `r` has exact order `2r`; if `2r>=4e`, the square is
   zero instead. The right side has exact order `3e`, forcing `2r=3e`.
   This excludes every odd `e`, rather than merely excluding a zero
   eigenvalue. After a nonempty étale base change, flatness preserves
   the filtration and its associated graded multiplication, while the
   quotient modulo `t` remains reduced. Reducedness, not integrality,
   is enough for this argument. Localizing to trivialize a line causes
   no problem.

3. **The even-index construction is valid over the nonreduced ring.**
   For `m=3e/2`, the algebra `B'=B_e[u]/(u^2-s)` is finite free of rank
   two and faithfully flat. The root `u` is a unit, so its derivative
   `2u` is invertible; hence this is an étale unit-root cover, not an
   additional normal ramification. The element `lambda=t^m u` has the
   required square. Nonzero rank-one reduction at the chosen point
   ensures a unit matrix entry, and the displayed trace-free identity
   allows a unit off-diagonal entry after a basis interchange if needed.
   Direct multiplication verifies both eigenvectors. Their first
   coordinate is the unit `y`, so they define free rank-one direct
   summands. Solving the first row of `J-lambda I` or `J+lambda I`
   also proves the asserted kernel equalities without division by
   the nonunit `lambda`.

4. **The coalescence and intersection formulas are exact.** Put
   `n=4e`. The normalized slope difference is the unit multiple
   `2t^m u/y`, so the lines agree modulo `t^k` precisely when `k<=m`
   and first differ modulo `t^(m+1)`. Because `t` is a nonzerodivisor
   before truncation,

       Ann_Be(t^m)=(t^(n-m)).

   Flatness gives the same identity after passage to `B'`, and
   multiplication by the units `2`, `u`, and `y` does not change it.
   A common vector in the normalized lines must have the same first
   coordinate in both expressions; that coordinate belongs exactly
   to this annihilator. Therefore

       L_+ intersect L_- = t^(5e/2)L_+ = t^(5e/2)L_-.

   Elementary invertible row and column operations on the two normalized
   generators reduce their matrix to diagonal entries `1` and a unit
   multiple of `t^m`. Thus their sum has quotient exactly

       B'^2/(L_+ + L_-) = B'/(t^(3e/2)),

   up to the stated module isomorphism. No cancellation by a nilpotent
   element has been used.

5. **No other pair of invariant lines can yield a decomposition.** The
   determinant calculation already rules out a decomposition by the
   displayed pair. More generally, a decomposition into two invariant
   line direct summands reduces modulo `t` to such a decomposition over
   the reduced ring `B'/(t)`. Each scalar action has square zero there,
   hence is zero. This would make the entire reduced matrix zero,
   contrary to its regular-nilpotent, nonzero reduction. This argument
   does not rely on exhaustiveness of the two constructed eigenlines.

## Scope and safeguards

- At the minimum index `e=2`, the exact statements are agreement modulo
  `t^3`, separation modulo `t^4`, intersection `t^5L_+=t^5L_-`, and sum
  quotient `B'/(t^3)` in the ring with `t^8=0`.
- The warning about further eigenlines is necessary and correctly retained.
  For example, abstractly replacing the displayed root by
  `lambda+t^(5e/2)c` leaves its square unchanged in `B'` for every `c`.
  This is a universal truncated-ring observation, not an evaluation of
  an actual HM scalar or source.
- The minimum-index conclusion applies to the stated regular normal
  ramification, including `q=v t^e` with `v` a unit. It does not cover
  arbitrary base changes with additional nilpotents.
- The proof neither descends the local root cover nor constructs a global
  ramified cover, a global square-root line bundle, or a global invariant
  line. It does not address the scalar zero divisor, the excluded source
  or nilpotent-zero loci, or the singular locus of `Q`.
- Nothing here extends `J` to the fifth neighborhood or identifies the
  separate `beta4` boundary modulo `im(beta2)`. The stated absence of
  integrability and algebraicity conclusions is appropriate.

This was an independent structural audit of the displayed local algebra
and the exact cited inputs. No selected actual HM/source coefficient,
point, matrix, rank, root, derivative, or scalar value was evaluated. No
large computation, external write, or proof-assistant certification was
performed.
