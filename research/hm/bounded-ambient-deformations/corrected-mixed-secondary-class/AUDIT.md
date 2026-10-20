> Historical mathematical review, preserved from the original artifact. This is not a new review or formal check of the repackaged text.

# Independent audit of the mixed obstruction counterexample

Status: PASS for the explicitly conditional joint-model theorem, concrete counterexample, and wrong-degree exclusion; imported geometric premises and the actual joint-model comparison remain outside this certification.

All calculations below are over a field of characteristic zero (characteristic different from two suffices for the displayed Maurer–Cartan calculations).

## Concrete DGLA

Let D have degree-one basis A, B, u, v and degree-two basis a, b, w, no other degrees, differential dA = du = a and dB = dv = b, and only nonzero basis brackets [u,v] = [v,u] = w. The degree-two space is central.

This is a DGLA. Graded antisymmetry requires the bracket of two degree-one elements to be symmetric, so the stated brackets have the correct signs. The differential squares to zero. Every term in the derivation identity and graded Jacobi identity vanishes, since all degree-two elements are central. In particular there is no hidden requirement that [u,u] or [v,v] be nonzero.

Project D onto the abelian DGLA h concentrated in degree one with basis Abar, Bbar, sending A and B to their barred counterparts and all remaining elements to zero. Its kernel L has L1 = span(u,v) and L2 = span(a,b,w). Hence

- H0(L) = 0;
- H1(L) = 0, because d: L1 → L2 is injective;
- H2(L) = k[w], because dL1 = span(a,b).

The first-order connecting map H1(h) → H2(L) is zero: its values on the basis are represented by a = du and b = dv. The unique closed degree-one lifts of the ambient basis elements are X = A − u and Y = B − v. Their bracket is

[X,Y] = [A,B] − [A,v] − [u,B] + [u,v] = w.

Thus removing the first-order defects creates a nonzero bracket term even though the original chosen lifts satisfy [A,B] = 0. Dropping the quadratic correction term [u,v] would give the wrong answer.

## Mixed Maurer–Cartan equation

For commuting even formal parameters s,t, the element s Abar + t Bbar is Maurer–Cartan in h. Any lift with zero constant term must have first-order part sX + tY. At bidegree (1,1), write its proposed correction as st Z with Z ∈ L1, since the ambient element is fixed. The Maurer–Cartan equation reads

 dZ + [X,Y] = dZ + w = 0.

The factor is exactly one: one half of the bracket of sX+tY with itself has mixed term st[X,Y], because [X,Y] = [Y,X]. Since dZ lies in span(a,b), no such correction exists. Allowing a degree-one correction in all of D would not help: dD1 has the same image span(a,b).

The argument already holds over k[s,t]/(s²,t²), and therefore also rules out a formal lift over k[[s,t]]. There is no degree-zero gauge freedom in D or L, so gauge equivalence cannot remove this obstruction.

## Pure data, bigrading, and symmetry

Assign weights (1,0) to A,u,a; weights (0,1) to B,v,b; and weight (1,1) to w. The differential and bracket preserve weight. The ambient mixed-weight complex vanishes, so its H1 and H2 vanish in every genuinely mixed weight. The relative mixed-weight H2 does not vanish: it contains [w].

The pure lifts sX and tY separately solve Maurer–Cartan, because [X,X] = [Y,Y] = 0. They are unique among zero-constant-term lifts of the specified pure ambient series: every higher correction lies in L1 and is forced to vanish by the injectivity of d, coefficient by coefficient.

Replacing the bracket by zero leaves the underlying complex, projection, first-order connecting map, pure-weight DGLAs, pure lift solutions, and stated ambient mixed cohomology unchanged. In that replacement, sX+tY lifts jointly. Consequently those data alone cannot distinguish joint existence from joint failure.

The involution A ↔ B, u ↔ v, a ↔ b, w ↦ w is a DGLA automorphism interchanging the two weights. It fixes the obstruction, consistently with the symmetry of the degree-one bracket. Its existence does not impose vanishing.

## Scope and cautions

1. This proves insufficiency of the listed algebraic hypotheses alone. It does not automatically realize this DGLA in a particular geometric deformation problem or rule out extra geometric identities there.
2. Ambient mixed acyclicity is different from relative mixed acyclicity. If H2(L) in the relevant mixed weight were assumed zero, this example would fail that stronger assumption.
3. Independence of chosen closed lifts can be checked directly in a general DGLA extension: when H1(L)=0, differences of closed lifts with a fixed ambient representative are dp with p∈L0, and [dp,Y]=d[p,Y] for closed Y. Simultaneous changes are also exact, including the cross term [dp,dq]=d[p,dq].
4. A globally bilinear secondary pairing requires a fixed complex and compatible linear liftable domain (for instance an abelian quotient). If coefficients, actions, differentials, ambient representatives, or null-homotopy choices vary, additional indeterminacy must be specified. The concrete counterexample makes no such unrestricted claim.

## Review of PROOF.md

The draft was reviewed after the independent calculation above. Its main joint-model theorem and algebraic countermodel pass the audit.

- Section 3: R = ∂y + [x,z] lies in the kernel because its projection is ∂c+[a,b], and is closed by the graded Leibniz rule. Mixed solvability is precisely the vanishing of [R], with correction equation ∂t = −R.
- Section 3.3: the full lift-change expression includes the necessary simultaneous-change term [q,r]. Its displayed primitive has the correct minus sign before [x,V]: ∂[x,V] = −[x,∂V]. The cross primitive ∂[U,∂V] = [∂U,∂V] is also correct.
- Section 3.4: changing c by a closed e changes the relative obstruction by the connecting class [∂E]. The stated distinction between fixed coefficient-action markings and varying positive-coefficient operations is essential and is preserved.
- Section 3.5: the representative-change formulas are correct. With x′=x+∂A and y′=y−[A,z], the two new terms cancel exactly because z is closed. The analogous change of b uses c′=c+[a,β] and y′=y+[x,B], where p(B)=β; the positive signs follow from |x|=1. Successive changes incorporate the cross term.
- Section 4: a closed joint lift of a nonzero ambient cohomology class cannot be exact. It cannot be replaced by an element of the kernel Ext1 group merely because the latter vanishes.
- Section 5: agrees with the independently checked countermodel above.
- Section 6: the plane computation is HH^n(P²,ω)=0 for n≠2 and dimension three for n=2, because the three summands are H^(2−p)(Ω^(2−p)). External Künneth makes the product group nine-dimensional in degree four. Given the imported pure class η with a nonzero canonical component, its external tensor square is nonzero over the ground field. The ordinary characteristic action preserves its degree, so it cannot alone produce the degree-two mixed module obstruction.

Two precision improvements were sent to the author:

1. In a pairing theorem on entire linear spaces, expressly assume existence of c for every pair (for example H2(h_J)=0). Mixed H1 vanishing removes ambiguity but does not itself give existence. The geometric draft already imports H2(h_J)=0; making it explicit prevents an overly general standalone reading.
2. Write the coefficient-valued characteristic composition with its actual twists: applying the second pure direction first gives χ_(E⊗M)(η_z), shifted by two, composed with χ_E(η_h). The latter factor is zero, which proves vanishing without identifying the first factor with χ_E(η_z)⊗M. That identification need not hold for arbitrary coefficient-valued natural transformations.

The geometric premises are imported, not re-proved by this audit. In particular the audit does not certify the model comparison to the physical carrier. The text explicitly leaves that comparison open and does not claim actual mixed vanishing or nonvanishing.

## Final revision and frozen scope

Both precision improvements above have been applied and checked in the final reviewed revision. In particular §6 now explicitly uses the twisted object E⊗M and relies only on the first arrow being zero; no unjustified twist-commutation assertion remains. The external-product assertion uses Künneth on diagonal Ext groups for the two factors. It does not require a multiplicative HKR splitting: the pulled-back factor classes compose externally, and their tensor product is nonzero.

Reviewed file: PROOF.md

SHA-256: f11c6f496158a570dd7b2dfa05f9bcb3601e7374843a9f74eb49cc875d547014
