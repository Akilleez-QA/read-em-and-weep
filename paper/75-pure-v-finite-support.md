# Finite support and ambient-length bounds for the pure-V gate

**Craig Ward · 23 October 2026 · PR1035**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/6effcd9b61b1942447a2c3f136a6776dda213c15/research/hm/source2-pure-v-finite-base-support/PROOF.md).

**Historical necessary bounds, now superseded:** [PR1044](82-pure-v-complete-nonic-classification.md) gives the complete five-stratum scheme classification. No thirty-orbit or ambient double fifteen-axis point occurs; the conic points are ambient-reduced. The nine-length list below records the earlier one-way bounds, not the current possibilities.

Retain the nonzero universal pure-V nonic gate and its finite base scheme B_s. The actual conditional gate could still be zero; no occurrence is selected by these universal restrictions.

## 1. Additional support is tightly bounded

Beyond the six order-five and ten order-three axes already in Z, off-conic support is either empty, the unique fifteen-point order-two axis orbit, or one thirty-point orbit with cyclic order-two stabilizer. The fifteen- and thirty-point possibilities never coexist, two thirty-point orbits cannot occur, and no free sixty-point orbit occurs.

There are fifteen involution-fixed projective lines. Each contains two order-five axes, two order-three axes, two of the fifteen order-two axes, and two points of any thirty-point orbit. Restricting degree-nine components to these lines gives a baseline vanishing order of at least six. Two additional off-conic orbits would raise this to ten and force a common line divisor, contrary to the no-divisor theorem. A free orbit is independently excluded by the global Bézout budget 34+60>81.

On either jet-exceptional line, the prescribed line orders rise to at least eight, so even one extra off-conic orbit is impossible. The only additional support then allowed by PR1035 is the twelve-point conic orbit, and its presence would require that jet line to equal the conic-base line.

## 2. Ambient multiplicity is not conic intersection multiplicity

Off both jet lines, B_s agrees locally with Z at all sixteen prescribed axes, contributing length 34. Two general component combinations have total intersection degree81, leaving at most 47 for additional local lengths.

- A thirty-point orbit must be ambient-reduced, since a local length of at least two would exceed the budget.
- At the twelve conic points, a smooth local component equation follows from the already simple conic intersection. The ambient ideal is curvilinear, of the form (f,w^k), with uniform length 1≤k≤3. This does **not** establish k=1.
- At the fifteen-point orbit, mirror-line degree budgets force a nonzero linear term. The Klein-four characters show that a generator with one mirror character is that mirror equation times a unit, not merely tangent to it. The remaining ideal is (u,v^l), with l=1 or2. No tangent direction or actual double point is selected.

On a jet line, the remaining Bézout budget is at most17. Consequently any conic orbit there, if it were present, would be ambient-reduced. The later line-placement theorem rules out its presence altogether, as stated below.

## 3. Necessary numerical list, not existence

Off the jet lines put k=0 when the conic orbit is absent, l=0 when the fifteen-point orbit is absent, and m=0 or1 for the thirty-point orbit. Then

    0≤k≤3, 0≤l≤2, m∈{0,1}, lm=0,
    12k+15l+30m≤47,
    length(B_s)=34+12k+15l+30m.

The resulting necessary total lengths are

    34, 46, 49, 58, 61, 64, 70, 73, 76.

No entry is asserted to occur for a universal member or an actual source. Potential thirty-point orbit locations and any actual coefficient remain unresolved. These lengths describe the nonic component base scheme, not the lift matrix's degeneracy scheme or the older source126 octic scheme.

## 4. Combined support-only consequence of PR1036

The [four-line placement](76-pure-v-four-lines.md) proves both jet lines distinct from the conic-base line. Combining that published identification with the support exclusions above shows that **each nonzero jet-line gate has support exactly the sixteen prescribed axes**. This combination alone does not determine the exceptional local ideals or total lengths on those lines.

The source reports independent mathematical review and 45 ordinary/optimized checks, including exact A₅ incidence enumeration and integer budgets. The geometric local-algebra arguments retain their written hypotheses. No source, original obstruction value or complete repair is selected.

The subsequent [PR1037 exact-local theorem](78-pure-v-exact-jet-lengths.md) closes this jet-line length gap: ℓ₅ has m³ at six axes and m at ten, total 46; ℓ₃ has the six prescribed length-four ideals and m² at ten, total 54. No actual coefficient is selected.
