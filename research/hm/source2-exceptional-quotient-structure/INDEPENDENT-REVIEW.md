# Independent review: exceptional source2 quotient contraction structure

Reviewed 2026-10-23 UTC, independently of the author's self-check.

## Frozen files

- PROOF.md SHA-256: `dd04970a091598c94350331aae92e24715f611514a1b66ef8527c0c6e1fe826f`
- verify.py SHA-256: `566b4c5caaef55117ec78146dfc692caac3e2feac7b55eb3f580db922f7989ec`
- INPUTS.json SHA-256: `65573e8c9e23f762f894d19f4d5c913297b62a878b0226579111c1b7a4207495`

Verdict: PASS for the conditional exceptional fixed-negative-pencil theorem.

## Independent checks of the new deduction

Read the full proof and checker and compared the imported data with exact
PR794 Sections3–6 and PR795 Sections2–3,7–8, previously read in full.

1. At the exceptional direction PR794 really supplies the split K_z and
   exact sequence0 -> D O -> F -> W'O(-3) + O6 -> 0. The extension
   of W'O(-3) by D O vanishes because H1(O3)=0. Additivity of Ext
   therefore separates that summand. The remaining equivariant Ext group
   is one-dimensional by Schur's lemma. Its class cannot be zero: a split
   O6 would supply nonzero H0(F(-2)), contradicting actual injectivity
   of H0(q(-2)). This uses the actual exceptional map, not only ranks.

2. The twisted complete degree-five evaluation sequence is a nonzero
   representative of precisely that extension class. Thus
   F = T O1 + W'O(-3), equivariantly but not canonically. Its H1 at
   twists -2,-1 is respectively W' tensor H1(O(-5)) and
   W' tensor H1(O(-4)). The other summand contributes no H1.
   The quotient-to-cohomology identifications commute with multiplication
   by every original linear form, by connecting-map naturality. This
   verifies the actual contraction arrows, not just character subtraction.

3. Under Serre duality each contraction is dual to multiplication
   H0(O2)->H0(O3). For nonzero l that map is injective. The span of
   its images as l varies is H0(O3), so the dual contractions have no
   common kernel. With W' multiplicity two, each arrow has rank6 and
   kernel dimension2, while their common kernel is zero.

4. Checked the explicit extension recursion coefficient by coefficient.
   The first equation follows from G_i,j=F_i,j-Hx_i,j. For j<m,
   the recurrence gives F_(i+1),j-G_i,(j+1)=Hy_i,j. The separately
   assigned final column gives the same identity for j=m. This also
   handles m=0 and n=0. Hence the coboundary is onto for all stated
   nonnegative m,n, not only the tested relevant case P4,I2.

5. Constant multiplicity spaces preserve this argument. Averaging a
   section over the finite group is valid even though G acts on the
   arrow space: each conjugate still intertwines the whole fixed
   arrow family, and averaging preserves the section equation. Thus
   the splitting may be chosen G-equivariant without changing variables.

6. In the full three-vertex extension, p4 is an isomorphism because L4=0.
   Its inverse extends the two-arrow section to the second pencil by
   naturality. This proves NR/I = N8 + L. The genuine first-block
   splitting then gives N/I=N0+N8+L, with dimensions(32,42,28).
   The first-arrow rank is9+15+6=30; the common first-arrow kernel is zero.
   No residual horizontal splitting or Q-stable decomposition is inferred.

7. The final distinction about quadratic composites is correct and
   important: L has nonzero first arrows but zero final vertex, so every
   two-arrow composite kills L2. This does not contradict its zero
   common first-arrow kernel. Neither fact asserts Q compatibility or
   existence of an actual compatible exceptional radical line.

## Executed evidence and limits

Ran `python verify.py` and `python -O verify.py`:737 checks pass with
byte-identical JSON. All three exact input SHA-256 and Git blob checks pass.
Inspected the full synthetic checker: it tests an entire basis of each
extension-target space, including the relevant30-dimensional one and all
six multiplicity pairs, independently computes coboundary rank30 with
kernel dimension8, and checks the polynomial contraction minors x^3,y^3.
These symbolic minors cover every nonzero pencil direction, not sampled
actual parameter values. No actual HM/source data is instantiated.

The universal written argument establishes the theorem; finite tests are
supporting diagnostics. This review is not a new deduction, a formal
proof-assistant certificate, source exclusion, or proof of the full repair.
