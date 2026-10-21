# Generic positive section count is now four or five

The actual inversion-even positive multiplication block has source41 and target37. At the invariant cone q0 it has rank33 and kernel A+D5. Its first Bockstein vanishes identically. The second Bockstein vanishes on D5 and is a nonzero multiple of

    A -> P4, h |-> projection_P4(a^2 h),

for a negative quadratic direction a. Nonvanishing is the actual Atiyah/quintic-extension theorem, not a chosen universal coefficient.

This nonzero universal channel has generic rank3. Here is a coefficient-free verification sufficient for that assertion. At any square a=ell^2, a kernel vector would be a nonzero sextic in the complementary V subrepresentation of Sym6W divisible by ell^4. The V linear series has Wronskian degree3(6-2)=12. Such a sextic forces vanishing sequence at least(0,1,4), hence weight at least2. Its G-orbit contains at least12 points, requiring total weight at least24, impossible. Thus the channel is injective on A at every square direction, and hence on an open set of directions. The open set also contains nonsquare directions, yielding smooth quadrics q0+t a for nonzero t.

Consequently the actual positive pencil has generic rank at least36, so its kernel has dimension at most5. Since source dimension exceeds target by4, its kernel has dimension at least4. Upper semicontinuity extends the upper bound to a nonempty open set of inversion-even quadrics. Therefore for a general smooth inversion-even quadric Q,

    h0(B_Q(4))_+ is either4 or5.

The separately proved generic odd vanishing then makes the total section count likewise4 or5. This is a bound with one unresolved rank, not a proof that the count is4.

In a general negative direction, the second-stage surviving source is D5 (dimension5), and the remaining target is one-dimensional. The next obstruction is the third Bockstein into that quotient. If it or a later obstruction is nonzero, the positive rank becomes37; if all higher obstructions vanish, it remains36 on that pencil. No higher nonvanishing is claimed here.

## Checked dependencies

- POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md.
- POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md.
- POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md.
- ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md.
- SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md for generic odd vanishing.

All deductions retain the actual maps. Universal representation geometry is not substituted for their coefficients. No actual HM coefficient, selected actual rank, or consumed experiment is evaluated. The original source/lifting/Weil-class algebraicity problem remains separate and incomplete.
