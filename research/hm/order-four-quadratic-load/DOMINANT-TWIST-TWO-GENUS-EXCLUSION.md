# Dominant twist-two eigenquotients are impossible

## Statement and inputs

Work over the complex numbers. Let Q be a smooth quadric threefold, V=F|Q, E=V(3), and X=P_Q(E) in the quotient convention. Write H for the pullback of the hyperplane class and L=c1(O_X(1)). Assume the checked evaluation setup: the four evaluation sections of L have exactly fifty reduced simple base points, one over each point of C intersect Q. Blowing up these points gives a smooth fourfold b:Xhat→X, exceptional divisors E_z, and the basepoint-free class

A=b*L−sum E_z,

whose four sections define f:Xhat→P(U*)=P3. The blowup and simple-base-point statement are inputs from the evaluation-basepoint calculation, not genericity assumptions about an endomorphism.

Let ψ be a nonzero primitive trace-free endomorphism V→V(k), for 1≤k≤4. Primitivity means that its entries have no common divisorial zero. Assume H0(V(2))=0, as on the previously established common good open. The checked rank-one-map lemma implies the characteristic polynomial of ψ is irreducible over C(Q). Its eigenquotient divisor T on X is therefore integral: over the generic point of Q it is the irreducible reduced quadratic divisor; any extra divisor would lie over a divisor of Q on which ψ vanishes identically, contrary to primitivity. A Cartier divisor in the smooth X has no embedded components.

Its strict transform That is an integral effective Cartier divisor on the smooth Xhat. If m_z≥0 is the multiplicity of T at the evaluation base point z, then

[That]=2L+(k−5)H−sum m_z E_z.

Here and below L,H on Xhat denote pullbacks. Suppose f|That is dominant onto P3. Then k=2 is impossible.

## An integral Gorenstein curve cut by two evaluation hyperplanes

The proper dominant morphism That→P3 is generically finite, since both spaces have dimension three. In characteristic zero there is a dense open subset of P3 over which it is finite étale. This can be seen by first removing the image of the non-quasi-finite locus and then the branch locus.

Two successive general hyperplane pullbacks give an integral surface and then an integral projective curve Γ. Here are the precise justifications, including the possible nonnormality of That.

For each cut, apply the Bertini irreducibility lemma in the Stacks Project, Lemma 37.32.3. The source is integral over an algebraically closed field and the system is basepoint free. The lemma's codimension-two intersection hypothesis holds on the finite étale open: first the image has dimension three, and after the first cut it has dimension two. Choose two transverse target hyperplanes meeting that open and a third hyperplane avoiding one component of their inverse-image intersection. The base-locus hypothesis is vacuous. Thus each general member is geometrically irreducible.

Both cuts meet the finite étale open densely, so their unique components are generically reduced. That is Cartier in a smooth fourfold and hence Cohen–Macaulay. Each nonzero general section is a nonzerodivisor on the preceding integral scheme, so the cut remains Cohen–Macaulay. Consequently it has no embedded associated primes; generic reducedness then implies reducedness. Thus both successive cuts are integral schemes, not merely irreducible supports. No normality or smoothness of That is required.

Moreover, Γ is the complete intersection of That and two A-divisors in a smooth fourfold. These divisors form a regular sequence, so Γ is a Gorenstein curve and adjunction gives

ω_Γ = O_Γ(K_Xhat+That+2A).

As an integral projective curve over C, Γ has H0(O_Γ)=C and p_a(Γ)=h1(O_Γ)≥0. Therefore deg ω_Γ=2p_a(Γ)−2≥−2.

Bertini source, read directly: https://stacks.math.columbia.edu/tag/0G4C , Lemma 37.32.3. The preceding paragraph verifies its hypotheses in this specific application; smooth-source Bertini is not being applied to That.

## Exact adjunction calculation

Since det E=O_Q(5) and K_Q=O_Q(−3),

K_X=−2L+2H,    K_Xhat=−2L+2H+3 sum E_z.

It follows that

K_Xhat+That+2A = 2L+(k−3)H+sum(1−m_z)E_z.

On X the relation L²−5HL+10H²=0 gives

integral L4=50,    integral H L3=30,    integral H² L²=10.

The exceptional divisors are disjoint. A positive-degree pullback class restricts trivially to each E_z, and integral E_z4=−1 for a point blowup of a smooth fourfold. Hence every mixed pullback/exceptional term vanishes and

deg ω_Γ
 = (K_Xhat+That+2A) A² That
 = [2L+(k−3)H] L² [2L+(k−5)H] + sum m_z(1−m_z)
 = 4·50+(4k−16)·30+(k²−8k+15)·10 + sum(m_z−m_z²)
 = 10k²+40k−130−sum m_z(m_z−1).

This also establishes a new necessary numerical condition for every dominant primitive eigenquotient in this setup:

sum m_z(m_z−1) ≤ 10k²+40k−128.

## Twist two and the remaining scope

For k=2, the displayed dualizing degree is

−10−sum m_z(m_z−1) ≤ −10,

because each m_z is a nonnegative integer. This contradicts deg ω_Γ≥−2. Thus a primitive twist-two eigenquotient cannot dominate P3.

Together with the fixed-Q nondominant exclusion at 44d30ea1cdb8088299411824e0abe6f7cf6cb78f, this removes primitive twist two on the common good open. An independent generic-Q support-dimension exclusion is available at 150b57e90e5898445e08d157bdaafd5934677869. A nonprimitive twist-two section would divide to twist at most one, already impossible by 0c497348c3935ddf4648043f988e1b172c158382. Thus H0(Q,End_0(F|Q)(2))=0 on this open. Primitive twist one was already excluded by nef intersection. The possible primitive twists are consequently three and four. This is not a proof that the actual 20-by-20 boundary is invertible, nor a complete proof repair.

For reference, the new necessary multiplicity bounds for the still possible dominant twists are sum m_z(m_z−1)≤82 at k=3 and ≤192 at k=4. These are constraints, not exclusions.

No selected Horrocks–Mumford coefficients, ranks, numerical samples, or experimental model evaluations are used.

Reproducible universal arithmetic: verify_eigenquotient_intersections.py checks the projective-bundle reduction and exceptional contributions. This is not an actual HM coefficient or rank computation.
