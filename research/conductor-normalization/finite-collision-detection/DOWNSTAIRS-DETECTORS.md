# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 05 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# A common degree-84 collision thickening and explicit dual detector modules

This supplements PROOF.md. It gives a common, positive-dimensional finite-order support for all 32 coordinate tests, and hence for the retained thirty, without evaluating any source or detector value.

Write u=t₂,v=t₃ with weights two and three and let N_n=V(K_n)⊂Y, where K_n consists of monomials of weight at least n. The audited regularity theorem says

    H²(B0(r−5)K_n)=0 for n≥r+9, r=0,1,2.

Thus N_9,N_10,N_11 suffice individually for the constant, first and second coordinate. A common choice for all three is T=N_11, giving injective maps

    H²(Y,B0(-5)) → H²(T,B0(-5)|T),
    H²(Y,B0(-4)) → H²(T,B0(-4)|T),
    H²(Y,B0(-3)) → H²(T,B0(-3)|T).

The respective source dimensions 2,10,20 are imported from the paired-coordinate calculation. No claim about target dimensions or surjectivity is needed.

## Explicit finite transverse structure

The divisibility-minimal generators are

    K_10=(u^5,u^4v,u²v²,uv³,v⁴),
    K_11=(u^6,u^4v,u³v²,uv³,v⁴).

For K_11 the weighted degrees are (12,11,12,11,12), and consecutive least-common-multiple degrees are (15,14,15,14). The flat polynomial-base argument already audited in ALL-POWERS.md applies to these ideals. Hence T is Cohen–Macaulay of dimension two; it is not assumed Gorenstein or reduced.

Its associated graded for the finite weight filtration consists of

    O_N(-2a−3b), for 2a+3b<11.

There are fourteen such monomials: six with b=0, four with b=1, three with b=2, and one with b=3. The corresponding generic transverse length is fourteen, and degree(T)=14 degree(N)=84. Similarly N_10 has transverse length twelve and degree72. These are multiplicities along a surface, not counts of sample points. The associated graded gives a filtration, not a canonical direct-sum splitting of O_T or of its cohomology.

## Dualizing module and a complete family of detectors

The explicit global resolution is

    0 → O(-15)^2⊕O(-14)^2
      → O(-12)^3⊕O(-11)^2 → O → O_T → 0.

Equivalently order generators as above and use consecutive syzygies; the ith syzygy has entries v^(b_(i+1)−b_i) and −u^(a_i−a_(i+1)) in adjacent positions. It stays exact over the singular triple-root surface by the already proved flat base change, not by assuming that surface smooth.

Since T has codimension two and is Cohen–Macaulay, its dualizing sheaf is Ext²_Y(O_T,ω_Y). Dualizing the resolution by ω_Y=O(-5) gives

    0 → O(-5) → O(7)^3⊕O(6)^2
      → O(10)^2⊕O(9)^2 → ω_T → 0.

Here the displayed sheaves before ω_T live on Y and ω_T is its extension by zero. The maps are the transposed original maps with the indicated twists. This is a dualizing module presentation, not a claim that ω_T is a line bundle.

Serre duality on the projective Cohen–Macaulay surface T, for the locally free sheaves B0(r−5)|T, gives

    H²(T,B0(r−5)|T)^* = H⁰(T,B0(5−r)|T⊗ω_T),

using trace self-duality B0*=B0. Serre duality on Y gives

    H²(Y,B0(r−5))^* = H²(Y,B0(-r)).

Consequently the duals of the injective restrictions are surjections

    H⁰(T,B0(5)|T⊗ω_T) ↠ H²(Y,B0),
    H⁰(T,B0(4)|T⊗ω_T) ↠ H²(Y,B0(-1)),
    H⁰(T,B0(3)|T⊗ω_T) ↠ H²(Y,B0(-2)).

These are complete families of dual tests for the constant, first-ten and second-twenty coordinate respectively. A detector in the original finite-dimensional dual space admits a representative in the indicated surface section group, generally nonuniquely. Pairing any such section with the restriction of the corresponding obstruction coordinate recovers its original Serre evaluation. This constructs a universal detector recipient and an explicit resolution; it does not produce a preferred basis, solve the Čech equations or evaluate any test.

In particular this is the correct injectivity/surjectivity distinction: original obstruction restriction is injective; the resulting map on dual detector spaces is surjective. Neither assertion is surjectivity of obstruction restriction.

## Relation to the upstairs finite neighborhood

PROOF.md constructs Q_12→B0(r−5)/K_(9+r)B0(r−5). These are its natural quotient maps. One must not replace K_(9+r) by K_11 for r<2 in that construction: I^(12+r) only forces coefficient order K_(9+r), not K_11. The common-T theorem instead restricts the already defined global three coordinate classes. The two versions are compatible after restriction from T to N_(9+r); they are not asserted to be the same chain map out of Q_12 to T.
