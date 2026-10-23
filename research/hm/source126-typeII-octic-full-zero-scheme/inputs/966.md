# Ten exceptional quadratics in the source2 pure-V image pencil

## Theorem and boundary

In the exact pure-V image pencil of PR792, for a nonzero negative quadratic a,

    T_a: H0(O(4))=D → H0(O(6))/V6=P,  s↦[a s],

has rank four except at exactly ten projective quadratic directions, where it has rank three. The exceptional locus is a reduced orbit of length ten in P(Sym²W). Each exceptional quadratic has two distinct roots: the two fixed points of one cyclic order-three subgroup of the projective icosahedral group. The twenty roots collectively form its orbit of size twenty. In particular EVERY nonzero square quadratic has rank four.

No roots, HM coefficients, parameter values or actual matrices are selected or evaluated. This is a theorem about the full universal image pencil already identified with the fixed negative variables in PR792. It does not assert existence of a Q-compatible pure-V radical. If such a radical exists, PR950 says Q is zero on this image subcomplex; the present result describes its restricted negative quadratic maps, not the full obstruction map. There is no source or pair cut, no generic full-adjoint claim and no complete repair.

## 1. Immutable inputs and natural image identification

INPUTS.json retains exact publicly fetched proofs:

- PR792, commit 2f01f18960ce56b8b2a0c1260c277de3c5f916bf, research/hm/source2-radical-rank-profile/PROOF.md. It proves, for every balanced source2 endpoint and both residual coupling types, that the pure-V radical image is naturally the fixed-variable system

      H0(O4) → H0(O5) → H0(O6)/V6,

  with ordinary linear multiplication and quotient multiplication. Its degree-twelve orbit factor cancels in this genuine image identification. V6 is the unique three-dimensional V constituent of H0(O6), and is basepoint-free. Its proof also records projective orbit sizes12,20,30,60 and perfectness of the binary group.
- PR950, commit 54c7e78bd5351b3ecbdcc4b3b558a0012eb79566, research/hm/source2-radical-image-reduction/PROOF.md. Only the optional Q-compatible application uses this input: it identifies I2=D and I4=P and proves Q|I2=0 under pure-V compatibility. Its quotient problem is not substituted for the image problem here.

Let X=P(W). The projective action is the icosahedral A5 action. Write φ:X→P(V6*) for the morphism defined by V6. It is nonconstant, since its three sections are linearly independent. The notation O(d) denotes the standard degree-d line bundle on X.

## 2. The length-two restriction formula

For nonzero a, let Z_a be its zero divisor, including its scheme structure when a is a square. The usual divisor sequence gives

    0→H0(O4) --a--> H0(O6) → H0(O_{Z_a}(6))→0.

The right space has dimension two. Put r_a=rank[V6→H0(O_{Z_a}(6))]. The kernel of T_a identifies with V6∩aH0(O4), hence has dimension3−r_a. Therefore

    rank T_a = 5−(3−r_a)=2+r_a.

Basepoint-freeness implies r_a≥1, even at a double point (its value quotient is nonzero), so ranks are only3 or4.

For distinct roots p,q, r_a=1 exactly when their nonzero evaluation functionals are proportional, equivalently φ(p)=φ(q). For Z_a=2p, use a local trivialization and divide by a section nonzero at p. Restriction has rank one exactly when the derivatives of all resulting section ratios vanish at p, equivalently dφ_p=0. This uses first jets, not merely evaluation at the support.

## 3. The degree-six map is immersive everywhere

For a three-dimensional subsystem of H0(O6), its Wronskian is the determinant of value, first derivative and second derivative in a local coordinate and local trivialization. The transformation laws give a global section of

    O(6)^3 ⊗ K_X^3 = O(18−6)=O(12).

It is nonzero. To see this directly in characteristic zero, at any point choose a basis of the independent section germs with distinct increasing orders a0<a1<a2 by Gaussian elimination on Taylor coefficients. The leading determinant is the product of the nonzero leading coefficients times the Vandermonde product ∏_{i<j}(a_j−a_i); thus it cannot vanish identically. Its order at that point is exactly a0+a1+a2−3. Basepoint-freeness gives a0=0.

If dφ vanishes at a point, all section ratios have zero linear coefficient, so a1≥2 and a2≥3. The Wronskian weight there is at least2. Its zero divisor is G-stable: changing the section basis multiplies its Wronskian by a nonzero determinant, so the zero set and multiplicities are preserved. Every nonempty projective orbit has at least12 points. A differential-zero orbit would therefore contribute at least24 to a divisor of degree12, impossible.

Thus dφ is nowhere zero. In particular every divisor2p is separated and every square quadratic has rank four. This proves a uniform statement, not just generic separability.

## 4. The bad-pair locus is finite

Let C be the reduced image curve and let X→C_normal→C be the normalization factorization. The first map is finite. Its target has genus zero, since it is dominated by P1 in characteristic zero. If its degree were greater than one, Riemann–Hurwitz would force a ramification point; the derivative of φ would vanish there by the chain rule. Therefore its degree is one and φ is the normalization map of its image.

A birational finite map of curves identifies distinct points only over the finite singular locus. Therefore the unordered distinct pairs with φ(p)=φ(q) form a finite set. Section3 excludes every nonreduced divisor from the rank-drop set. Thus the rank-one locus in the length-two evaluation problem is a zero-dimensional scheme, disjoint from the discriminant conic of square quadratics.

## 5. Its scheme length is ten

Let S=Sym²X=P(Sym²W), with hyperplane bundle O_S(1). The universal degree-two divisor on X×S gives, after tensoring by O_X(6) and pushing to S, the exact sequence

    0→H0(O4)⊗O_S(-1)→H0(O6)⊗O_S→E6→0,

where E6 is locally free of rank two and its fiber is H0(O_{Z_a}(6)). Vanishing of H1(O4) gives exactness after pushforward. Its determinant is O_S(5).

Consider the evaluation map V6⊗O_S→E6. Its rank is at least one everywhere and two generically. Let B be its rank-at-most-one determinantal scheme. Its support is finite by Section4. Near any point of B, a nonzero entry is a unit, and invertible row and column operations reduce the matrix to an identity entry and a row (f,g). Here (f,g) defines a zero-dimensional subscheme on the smooth surface S, so it is a regular sequence. Its relation module is generated by (−g,f). Consequently the kernel of the evaluation map is a line bundle K, and its cokernel is locally O_B up to a line trivialization.

Off B the determinant sequence gives K=det(E6)^(-1)=O_S(-5). Line bundles agreeing off a codimension-two set on the smooth surface agree globally. Therefore the exact sequence has K-theory identity

    [coker]=[E6]−3[O_S]+[O_S(-5)]
           =4[O_S]−5[O_S(-1)]+[O_S(-5)].

A zero-dimensional cokernel has Euler characteristic equal to length, and locally its length is that of B. On P², χ(O(k))=(k+2)(k+1)/2 for every integer k. Thus

    length B=4·1−5·0+6=10.

The scheme B is also exactly the maximal-minor rank-drop scheme of the universal quadratic map T, not just the same point set. Indeed the cokernel sheaves of

    H0(O4)⊗O_S(-1) → (H0(O6)/V6)⊗O_S

and of V6⊗O_S→E6 are canonically the same quotient

    (H0(O6)⊗O_S)/(V6⊗O_S + im[H0(O4)⊗O_S(-1)]).

Their zeroth Fitting ideals therefore agree. These are respectively the ideals of the 4×4 maximal minors of the first presentation and the 2×2 maximal minors of the second. Thus all scheme-length and reducedness conclusions below apply to the actual universal T presentation as well.

This argument does not assume reducedness, an expected-rank guess, or ten ordinary nodes. It establishes the precise scheme length before using symmetry.

## 6. Symmetry makes the ten directions reduced and intrinsic

For an unordered pair of distinct points, its stabilizer H in A5 has a subgroup H0 of index at most two fixing each point. A finite subgroup of PGL2 fixing a point is cyclic: its derivative at the fixed point is injective on that finite stabilizer. The only element orders in A5 are1,2,3,5. Thus |H0| is one of1,2,3,5, and the possible unordered-pair orbit sizes divide into the list

    6,10,12,15,20,30,60.

Every such orbit has size at least six. The scheme B is invariant, and its local length is constant along an orbit. A total length of ten cannot contain two orbits. A single orbit of size six also cannot have total length ten, since its common local length is an integer. Therefore B is exactly one orbit of size ten and every local length is one. It is reduced.

Its pair stabilizer has order six. The pointwise subgroup has order three, since no point stabilizer can have order six. Each pair is therefore the two fixed points of its cyclic order-three subgroup. A5 has twenty elements of order three, hence ten such subgroups. Distinct subgroups cannot share a fixed point, since point stabilizers are cyclic and their only order divisible by three is three. Their twenty fixed points form the orbit of size twenty. The exceptional directions are thus characterized intrinsically without choosing coordinates or roots.

## 7. Conditional formal image complex and scope

If the pure-V radical is Q-compatible, the actual image subcomplex is

    D[[t]] --tT_a--> P[[t]],

by PR950. For each fixed nonzero a, let k=rank T_a. Ordinary constant changes of bases put T_a in rank normal form, so its formal cohomology is

    H0=C[[t]]^(5−k),
    H1=C[[t]]^(4−k) ⊕ (C[[t]]/(t))^k.

Thus away from the ten directions (including every square), the image complex has a free kernel of rank one and four length-one torsion summands in its cokernel. At the ten directions it has free kernel rank two, free cokernel rank one, and three length-one torsion summands. These statements concern only the image complex. Its inclusion into the full obstruction complex need not preserve these groups, and no acyclic cancellation of this image is asserted.

The verifier authenticates both original sources, checks symbolic dimensions, Wronskian weights and orbit-length exclusions, derives the length-ten Euler characteristic, and exhausts the elementary stabilizer/local-length alternatives. It does not select or evaluate actual HM data or the ten roots. The written geometric argument is not proof-assistant certification.
