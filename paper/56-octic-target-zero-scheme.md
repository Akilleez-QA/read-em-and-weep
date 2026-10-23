# The octic target section's length-34 zero scheme

**Craig Ward · 23 October 2026 · Update through PR1000**

**Subsequent update.** PR1005 now computes the whole generator in [chapter 58](58-full-octic-generator-zero-scheme.md): length46, not the target factor’s length34. The target theorem and its historical scope below remain intact; the actual scalar is still unselected.

[PR1000](https://github.com/Akilleez-QA/read-em-and-weep/blob/260cd6a777b23dc7ccd5ed956fcf65e17ff56145/research/hm/source126-typeII-octic-zero-scheme/PROOF.md) studies the universal invariant target section σ:O(-4)→E in the canonical octic generator σψ4. It proves that its zero scheme Zσ is finite of length34, disjoint from the discriminant conic of squares. This σ is **not** the top-polar obstruction in the opposite-bundle/vertex problem. The actual octic scalar remains unselected; four necessary source-dual pairs and three labels remain.

## 1. Exact support and local structure

The scheme consists of the six projective order-five axes, each of length four, and ten simple projective order-three axes. At every order-five axis the completed local ideal is exactly (u²,v²) in stabilizer eigen-coordinates. Thus length34=6·4+10, with scheme structure retained rather than just support counted.

There is no divisorial zero, because dividing out an invariant divisor would produce a forbidden lower-twist invariant section of E. The rank-two section is therefore regular, and its top Chern number gives c₂(E(4))=6+4·3+16=34.

On the square conic, the first-derivative quotient identifies the restricted E with W O(3), and E(4) with W O(11). The section restricts to the nonzero gradient of the squarefree invariant degree-twelve Wronskian, so its two components never vanish simultaneously. This proves absence of all conic zeros, not only generic nonvanishing.

Off the conic, projective stabilizers allow orbit sizes6,10,15,30,60. The unique nonnegative solution of the length equation is 6·4+10·1. At an order-five axis, the two fiber weights allow only u² and v² as quadratic leading terms; indeed every full component lies in (u²,v²). Equality of colength four upgrades containment to equality of completed ideals. The familiar six-axis schemes for other maps are not assumed or counted as newly proved here.

## 2. Minimal saturated ideal resolution

The regular section gives a quotient I_Zσ(7). Pulling back through D O→E and using H¹(O(3))=0 gives the minimal resolution

0→A O(-8)⊕O(-11)→D O(-7)→I_Zσ→0.

There are five degree-seven generators, three linear first syzygies and one degree-four first syzygy. The coordinate-ring Hilbert series is

(1−5t⁷+3t⁸+t¹¹)/(1−t)³.

Its Hilbert function in degrees0 through9 is (1,3,6,10,15,21,28,31,33,34), and it remains34 thereafter. This verifies the full finite scheme rather than an orbit-count heuristic.

## 3. What this says about the octic generator

The generator σψ4 vanishes at every target-factor zero regardless of ψ4. However the theorem does not compute further zeros of the source covector. In particular σ being nowhere zero on the square conic does not alone show that the **whole generator** is nowhere zero there. No nonzero value of the actual octic scalar is selected.

The proof's 92 exact checks authenticate inputs and verify character/Chern arithmetic, finite-group orbit data, local monomial weights and the Hilbert numerator. The global section and scheme arguments remain written mathematics; no actual HM instance is evaluated or full proof-assistant certification claimed.

No pending full-generator zero-scheme theorem is incorporated. The separate source-report chapter55 concerns seven possible types of another bundle, not seven source-dual cases. Actual realization, remaining scalar selection and the original repair remain open.
