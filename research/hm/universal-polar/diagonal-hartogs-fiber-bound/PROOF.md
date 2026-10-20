# Diagonal–Hartogs proof of the K7 fiber bound

Work over C. Let E have dimension 4, let K ⊂ Sym²E have dimension 7, and let v:K→E be linear. Assume square avoidance: for every nonzero e with e²∈K, v(e²)∉Ce. An ordered distinct pair ([a],[b]) is compatible if ab∈K and v(ab)∈span(a,b). Then the compatible-pair locus has dimension at most 2.

## Extension lemma

Let Z be an integral projective threefold in P(E)×P(E), whose dense open subset consists of compatible distinct pairs. Suppose dim(Z∩Δ)≤1. Then such Z cannot exist.

Indeed Z meets Δ. The diagonal has class h1³+h1²h2+h1h2²+h2³. Every mixed degree on Z is nonnegative, and at least one is positive because (h1+h2)³ has positive degree. Thus [Z]·[Δ]>0, which excludes disjointness.

Let ν:N→Z be the normalization and set L_i=ν*O(1,0),ν*O(0,1), respectively. The inverse image D of Z∩Δ has dimension ≤1, since ν is finite. On N\D, the two tautological lines are independent. Compatibility on a dense open subset implies compatibility everywhere on N\D: the rank condition a∧b∧v(ab)=0 is closed, and ab∈K is closed. Hence unique regular coefficients α∈H⁰(N\D,L_2), β∈H⁰(N\D,L_1) satisfy v(ab)=αa+βb, as an identity in E⊗L_1⊗L_2. The coefficients are regular because the map from the sum of the two tautological line bundles is a subbundle map wherever the two projective points differ.

Normality and codim_N D≥2 extend both sections uniquely over N. Their identity extends by density. At any point above Δ it gives v(e²)∈Ce, contradicting square avoidance.

The identical extension argument works for a threefold Z⊂P(A)×P(A), dim A=3, when dim(Z∩Δ_A)≤1. Here nonempty diagonal intersection follows by intersecting additionally with h1+h2: Δ_A has class h1²+h1h2+h2², and the resulting degree on Z is 2(deg h1²h2+deg h1h2²)>0 by ampleness.

## Three-dimensional subspace lemma

Suppose K contains Sym²A for a hyperplane A⊂E. There is no compatible threefold in P(A)×P(A).

Let q:E→E/A. If the quadratic form Q(a)=q(v(a²)) is nonzero, every compatible pair satisfies q(v(ab))=0. Thus the diagonal intersection of its projective closure lies in the plane curve Q=0, and the extension lemma applies.

If Q=0 identically, polarization shows v(Sym²A)⊂A. But every homogeneous quadratic map f:A→A has a nonzero eigenvector, including zero eigenvalue. For completeness f modulo the tautological line is a section of Q_A⊗O(2) on P(A)=P², where Q_A is the rank-two universal quotient. Its top Chern class is c2(Q_A⊗O(2))=(1+2+4)h²=7h², so this section has a zero. That zero is a square-compatible point, again impossible.

## Apply the net of annihilating quadrics

Let W=K^⊥⊂Sym²E* have dimension 3. Its projective base locus B consists exactly of [e] with e²∈K.

If the three independent quadrics have no common polynomial factor, B has dimension at most 1. (Any dimension-two component in P³ gives a common irreducible hypersurface factor.) Thus every threefold closure of compatible distinct pairs satisfies the extension lemma.

If they have a common factor, it is linear: a common quadratic factor would make W at most one-dimensional. Write W=zL with z∈E* nonzero and L⊂E* three-dimensional. Put A=ker z.

### Case z∉L

Choose p spanning ker L, normalized by z(p)=1. Then E=Cp⊕A and K=Cp²⊕Sym²A. Write a=xp+u and b=yp+w. The condition ab∈K is xw+yu=0. If x=0 or y=0, either both vanish or one projective vector vanishes. Thus the product incidence is the union of P(A)×P(A) and the graph Γ of the projective involution [xp+u]↦[xp−u].

Any integral threefold outside P(A)×P(A) must be all of Γ. Its compatibility would imply, for all u∈A\{0} and all t≠0,

v(p²−t²u²)∈span(p,u).

Letting t→0 gives v(p²)∈span(p,u) for every u, hence v(p²)∈Cp. This contradicts square avoidance. The three-dimensional subspace lemma excludes threefolds inside P(A)×P(A).

### Case z∈L

Choose L=span(z,ℓ1,ℓ2), and let r span ker L⊂A. The equations for ab∈K are z(a)z(b)=0 and z(a)ℓ_i(b)+z(b)ℓ_i(a)=0 for i=1,2. Consequently the product incidence equals

(P(A)×P(A)) ∪ (P(E)×{[r]}) ∪ ({[r]}×P(E)).

Any integral threefold outside the first component must be one whole star. Compatibility of the first star, evaluated at a=r+tu for arbitrary u independent of r and t≠0, yields

v(r²)+t v(ru)∈span(r,u).

Taking t→0 and intersecting over u gives v(r²)∈Cr, contradiction. The other star is symmetric. Again the three-dimensional subspace lemma handles the first component.

Every possible threefold is excluded, proving the bound. If a component had dimension greater than 3, take an integral three-dimensional section whose dense open remains within the compatible distinct-pair locus; the same argument applies.
