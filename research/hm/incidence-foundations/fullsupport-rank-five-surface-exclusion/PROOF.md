# Full-support rank-five surfaces: exclusion of two surface factor images

Over C, let E have dimension four and K be a full-support five-dimensional subspace of Sym²E. Let v:K→E be linear. Assume square avoidance: v(e²) is not proportional to e whenever 0≠e²∈K. Then no integral ordered rank-two factor surface X, densely satisfying v(ab)∈span(a,b), can have both factor images surfaces.

## Proof and dependencies

If both factor images are planes, the distinct-plane classification and coincident-plane exclusion in `/research/hm/middle-surface/linear-graph-surface-exclusion/PROOF.md` and `/research/hm/middle-surface/linear-graph-surface-exclusion/COINCIDENT_PLANES.md` give a contradiction. If exactly one is a plane, the pure-span theorem in `/research/hm/incidence-foundations/one-planar-factor-exclusion/PROOF.md` applies.

Suppose both are nonplanar. The theorem in `/research/hm/incidence-foundations/nonplanar-factor-degree-bounds/PROOF.md` shows that both images equal an integral quadric Q, both projections are birational, and the symmetric annihilator evaluation matrix M has ambient generic rank four. Its maximal-minor gcd g is the irreducible equation of Q. Dividing the quartic minor vector by g gives a primitive quadratic left syzygy of five independent quadrics q_i spanning K-perp.

The polarization lemma in `/research/hm/incidence-foundations/quadratic-gradient-syzygy/PROOF.md` writes that syzygy as Cq for a nonzero constant symmetric matrix C and yields q^t Cq=0. Rank C is at least three. Rank three forces the kernel image into a fixed projective line, contradiction. Rank four forces the kernel map on Q to be the restriction of a balanced ambient projective involution. Dense compatibility and square avoidance exclude this by `/research/hm/incidence-foundations/nonplanar-linear-correspondence-exclusion/PROOF.md`.

Finally rank five is impossible by `/research/hm/universal-polar/rank-five-quadric-maps/PROOF.md`: restriction to any source plane and the ranks 3,4,6 of ternary Veronese relations force a product partner for every linear form in W=span(q_i). Applying the previously established pure incidence lemmas to this dual five-space gives W=eE*+Ch. Its Jacobian minor gcd is e², contradicting the irreducible g. This also treats a cone Q, since the argument does not require smoothness of the source quadric.

All ranks are exhausted, proving the theorem.

## Stronger pure-K classification of the nonplanar subcase

Without v or square avoidance, the same reasoning leaves only rank C=4. Hence every such both-nonplanar factor surface is the graph on a common integral quadric of a balanced ambient linear involution. The nonlinear involutions previously left open are now excluded purely by K. The smooth-quadric bidegree bounds in the cumulative packet remain valid intermediate results but are superseded for this incidence problem.

## Scope

This theorem concerns full-support rank-five kernels and compatible ordered rank-two surfaces. It does not by itself exclude point- or line-factor surfaces, ternary-support kernels, or all lower-rank cases. It makes no claim about actual mixed quantum obstruction values, higher-order module existence, or algebraicity.
