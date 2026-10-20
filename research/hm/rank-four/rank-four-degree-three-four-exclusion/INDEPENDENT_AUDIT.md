# Independent audit: cubic and quartic component exclusion

## Verdict

**PASS, conditional on the explicitly imported normalizer representation and degree/invariance hypotheses.** The argument excludes integral degree-three and degree-four components of any reduced N-invariant curve of total degree at most 125. No correction to the mathematical argument is required.

This audit independently checks PROOF.md rather than treating the author's AUDIT.md as independent certification. The line-exclusion and canonical-conic proofs were read to check the stated interface with prior work; the underlying rank/degree and image-dimension theorems were not re-proved. No actual source operation, source tensor, source coefficient, selected source input, or operation matrix was evaluated.  

## 1. Scope, degree accounting, and exhaustive case division

The group has order |N|=25·120=3000. For a degree-d integral component C of an invariant reduced curve, its distinct N-translates are distinct components, all of degree d. Hence d[N:N_C]≤125. This does not count embedded structures, multiplicities, or intersections as additional components.

An A-stabilizer is a subgroup of the elementary abelian group of order 25, so its order is 1, 5, or 25. An integral curve spanning a line is that line, excluding span dimension one for d=3,4. If L is the pullback of O_C(1) to its normalization, then deg L=d and the independent ambient linear forms inject into H⁰(L). The elementary inequality h⁰(L)≤d+1 gives r≤d. Thus the only spans are planes, hyperplanes, and (only for d=4) all of P⁴. These are precisely the cases treated.

## 2. Genus and faithfulness checks

For a nondegenerate integral degree-d curve in P^r, Castelnuovo's arithmetic-genus bound also bounds the genus of the smooth normalization. Writing d−1=m(r−1)+ε gives the bound (r−1)m(m−1)/2+mε. The relevant values are:

- (d,r)=(3,3): 0;
- (d,r)=(4,3): 1;
- (d,r)=(4,4): 0.

Thus every use of rationality or genus at most one is valid for singular as well as smooth curves. No genus bound is incorrectly applied to plane quartics.

If a projective transformation fixes C pointwise, each vector representing a point of C is an eigenvector of a representative linear map. The eigenvector locus is a finite union of linear eigenspaces. Irreducibility puts C in one of these, and spanning implies that the map is scalar on the entire span. Consequently a group acting faithfully on the span acts faithfully on C and its normalization. Normalization also gives an honest group action by uniqueness of lifting automorphisms. This verifies the faithfulness assertions wherever invoked.

The two low-genus obstructions are correct:

- In PGL₂(C), the centralizer of a nonidentity element of order five is the diagonal torus. A commuting elementary abelian group of order 25 cannot embed in that torus, whose finite subgroups are cyclic.
- On an elliptic curve, the quotient of the automorphism group by translations has order 2, 4, or 6. A nonidentity order-five automorphism is therefore translation by a nonzero five-torsion point p. The polarization kernel for a degree-d line bundle is E[d]: translation preserves it only if dp=0. Neither d=3 nor d=4 satisfies this. Pullback of the ambient hyperplane bundle is invariant under the lifted curve action and has degree d even for a singular or non-linearly-normal curve.

## 3. Stabilizer A_C=A

An A-invariant span lifts to an invariant subspace for the irreducible Heisenberg representation. It is therefore V. The degree/span bound forces d=4, with rational normalization. Since N is a projective transformation group and C spans P(V), A acts faithfully on the normalization. The elementary abelian order-25 obstruction applies. There is no omitted smaller-span possibility.

## 4. Trivial A-stabilizer and the full G action

For A_C=1, projection identifies K=N_C with H⊂G and gives [N:K]=25[G:H]. The degree bound yields [G:H]≤5/d<2, hence H=G for both degrees.

The complement conjugacy calculation is valid in characteristic five: the central involution z acts by −1 on A, and equality of c(zh) and c(hz) gives 2c(h)=(1−h)c(z). Since 2 is invertible, c(h)=a−ha with a=c(z)/2. Conjugation by a translation therefore reduces K to the canonical G. No unjustified coprime-order splitting assertion is needed.

In V=T⊕W, inequivalent irreducibility and multiplicity one imply that every invariant subspace is a sum of these summands. With dimension at least three, U is T or V. In particular there is no invariant hyperplane.

### Plane equations

A plane degree-d integral curve is cut out by one irreducible homogeneous polynomial, unique up to scalar. Setwise preservation gives a one-dimensional representation on its equation line. Since SL₂(F₅) is perfect, that character is trivial; since T factors through A₅, invariant forms can be counted there.

The displayed symmetric-power characters check directly from the generating function

    Σ χ(Symⁿ T)(g)tⁿ = 1/((1−t)(1−e^{iθ}t)(1−e^{−iθ}t)).

At orders 2 and 3 the denominators specialize to (1−t)(1+t)² and 1−t³. At either order-five class the degree-three and degree-four coefficients vanish. With class sizes 1,15,20,12,12, the averages are (10−30+20)/60=0 and (15+45)/60=1. Dualizing does not change these values. The invariant nonzero quadratic q has nonzero square, so the unique invariant quartic line is spanned by q². It cannot define a reduced integral quartic. This checks both degrees and both three-dimensional icosahedral representations.

### Full span

The full-span case forces a rational quartic. The action of G on its normalization is faithful, including the central involution: on V that involution acts with opposite signs on T and W, so it is not projectively scalar. An embedded G in PGL₂(C) would lie in the centralizer of its central involution. That centralizer is the torus normalizer C*⋊C₂ and is solvable. A nontrivial perfect group cannot be its subgroup. This excludes the full G action, not merely its A₅ quotient.

## 5. Axis-stable planes and hyperplanes

A subspace stable under an axis generator with five distinct eigenvalues is the span of a subset of its eigenlines. Distinct axes cannot stabilize the same proper nonzero subspace: they generate A projectively, and their Heisenberg lifts would preserve that subspace, contradicting irreducibility.

The six axes are G-conjugate. For one fixed axis, Heisenberg translations give j↦j+b on eigenline labels, and the split torus in SL₂(F₅) supplies every nonzero multiplier. Thus the full affine group acts. It is transitive on unordered pairs and hence on their three-element complements, as well as on single omitted labels. Therefore the plane orbit has exactly 6·10=60 members and the hyperplane orbit exactly 6·5=30. Disjointness across axes justifies these products rather than merely upper bounds.

Sixty distinct spans imply at least sixty distinct curve translates, so planar components of either degree exceed the budget.

For a four-eigenline hyperplane, D=diag(ζ^{j²}) belongs to the Schrödinger normalizer and has projective order five. Z and D commute and generate C₅² projectively. A scalar restriction of Z^aD^b would require aj+bj²=c at four distinct indices. A degree-at-most-two polynomial with four roots is zero, forcing a=b=0 (and c=0). Thus the restriction is faithful.

If D preserved C, both Z and D would act faithfully on its normalization. Genus zero contradicts the elementary abelian group obstruction; genus one is already contradicted by the nontrivial order-five subgroup generated by Z and the degree-three/four polarization. Hence the D-orbit contains exactly five distinct curves with this one span. Conjugating to every hyperplane produces five distinct curves over each of thirty distinct spans, so there are at least 150 translates. There is no overcount between spans.

## 6. Axis-stable full-span quartics and translated lifts

Here C has rational normalization. Since K∩A=A_C is normal in K, its image H in G lies in the axis stabilizer of order 20.

If 5 divides |H|, Cauchy's theorem supplies u∈H of order five. In the axis stabilizer such an element is a nonidentity unipotent: its diagonal eigenvalues are 1, it fixes the axis pointwise, and (u−1)²=0 on A. Every lift k=(a,u) in K satisfies

    k⁵=(Σᵢ₌₀⁴uⁱa,1)=(5a+10(u−1)a,1)=1.

Both integer coefficients vanish in F₅. The nontrivial projection u ensures that k has exactly order five. Conjugation on A is u regardless of the translation a, so k centralizes A_C. Its subgroup meets A_C trivially because its nontrivial powers have nontrivial projection. Consequently ⟨A_C,k⟩≅C₅², and full span makes its action on the rational normalization faithful. This is impossible.

Thus |H| divides 20 and is prime to five, so |H|≤4, |K|=5|H|≤20, and the component orbit has at least 150 members. The lift argument genuinely covers all translation parts; it does not assume that the stabilizer contains a specially chosen diagonal representative.

## 7. Conclusion and dependency boundary

Every stabilizer/span case is exhausted and each contradiction is valid. The cubic/quartic exclusion itself depends only on the stated projective normalizer representation, curve invariance, and total degree bound. It requires neither the prior no-line/no-conic conclusions nor any actual-operation evaluation.

Combining it with those separately imported exclusions gives minimum component degree five and at most 25 irreducible curve components. The claim remains conditional on those earlier inputs. It does not establish that the curve is empty, exclude degree-five components, or constrain isolated rank-locus points beyond the existing results.
