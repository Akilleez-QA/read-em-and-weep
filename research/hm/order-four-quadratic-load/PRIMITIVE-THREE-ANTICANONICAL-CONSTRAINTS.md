# Anticanonical constraints on a primitive twist-three eigenquotient

Let Q be a smooth complex quadric threefold, V=F|Q, E=V(3), X=P_Q(E) with the quotient convention, and H,L the hyperplane and tautological classes. Assume the checked common-open inputs H0(V(2))=0, c1(E)=5H, c2(E)=10H². A primitive trace-free ψ:V→V(3) defines an integral eigenquotient divisor

T∈|2L−2H|=|−K_X|.

Integrality follows from the already checked irreducible characteristic polynomial and absence of a divisorial zero of ψ. In this note T is not assumed normal, smooth, canonical, or to have isolated singularities.

## 1. Exact direct images despite the exceptional eigenquotient fibers

Write π:T→Q and N=(L−H)|T. The morphism π is proper and generically finite of degree two but need not be finite: over a zero of ψ its fiber is the full projective line. Applying the projective-bundle direct-image formulas to

0→O_X(−2L+2H)→O_X→O_T→0

gives

0→O_Q→π_*O_T→O_Q(−3)→0,   R^iπ_*O_T=0 for i>0.

Here R¹p_*O_X(−2L+2H)=O_Q(−3); all other contributions are zero. The extension splits because H1O_Q(3)=0. In fact the splitting is canonically the trace splitting, since π has generic degree two and the characteristic is zero. Hence

π_*O_T=O_Q⊕O_Q(−3).

The algebra structure is the spectral double-cover algebra defined by ψ. Thus the Stein factorization T→Y→Q has the actual integral sextic spectral cover Y, and ρ_*O_T=O_Y, R^iρ_*O_T=0 for i>0. The latter follows from the displayed vanishing and the finite, hence exact and faithful, pushforward from Y to Q. These statements do not assume Y normal.

The two analogous restriction sequences for N and −N give the exact bundle-valued identities

π_*O_T(N)=V(2),          R^iπ_*O_T(N)=0 for i>0,
π_*O_T(−N)=V(−4),        R^iπ_*O_T(−N)=0 for i>0.

For the first, O_X(N−T)=O_X(−L+H) is relatively acyclic. For the second, both direct images of O_X(−L+H) vanish, whereas

R¹p_*O_X(−3L+3H)=E*⊗O_Q(−2)=V(−4).

Consequently h^i(O_T(N))=(0,5,0,0). Indeed the actual primary injection q:H1F(0)→H1F(2) has dimensions5→10, and the restriction sequence gives h1V(2)=5 and all other cohomology of V(2) zero. Gorenstein duality on T then gives h^i(O_T(−N))=(0,0,5,0).

Thus N is the restriction of the ambient half-anticanonical class and is positive on the projective-line fibers with no global section, not an effective divisor whose cube can be subjected to positivity without justification.

## 2. Virtual intersection numbers and the smooth alternative

Adjunction gives ω_T=O_T. The sequence above gives h^i(O_T)=(1,0,0,1). These assertions hold for the integral Gorenstein T without smoothness.

The relative tangent sequence of the smooth projective bundle gives

c2(X)=6LH−11H²,       c3(X)=8LH²−18H³.

For the Cartier divisor T, its virtual tangent class is T_X|T−O_T(T). Since T=−K_X, its virtual Chern classes satisfy

c2^vir(T)=c2(X)|T,
c3^vir(T)=[c3(X)−c2(X)T]|T.

Using integral L4=50, HL3=30, H²L²=10, H³L=2, one obtains

integral c3(X)T = 56,
integral c2(X)T² = 24,
integral c3^vir(T) = 32.

Also N³=−36 and c2^vir(T)·N=12, consistent with χ(O_T(N))=−5. These are virtual intersection computations and are NOT identified with the topological Euler number when T is singular.

If T is smooth, its genuine topological Euler number is therefore32. Hodge symmetry, the previously computed O_T cohomology, and trivial canonical bundle imply

32=2(h11(T)−h21(T)),

so h11(T)≥16. As h20(T)=0, the exponential sequence and Lefschetz (1,1) identify its Picard rank with b2=h11. The ambient X has Picard rank two. Therefore any smooth primitive twist-three eigenquotient must possess at least fourteen independent divisor classes beyond the image of Pic(X) in Pic(T).

In particular, smoothness together with an inherited Picard group is impossible. This is a conditional constraint, not an assumption that an actual eigenquotient is smooth or has inherited Picard group. A singular eigenquotient is not excluded by it.

If T is smooth, the Stein map ρ:T→Y also gives a resolution with R^iρ_*O_T=0; Y is normal because ρ_*O_T is integrally closed on each open subset. Thus its spectral cover has rational singularities. This is another consequence of smoothness, not a claim that the actual cover is normal or has rational singularities.

## Scope

The new unconditional content is the exact derived pushforward description of both half-classes and the resulting cohomology. The new numerical restriction is the Picard-rank minimum16 in the smooth alternative. Negative N³ alone does not imply a contradiction: N is neither asserted nef nor effective, and no positivity theorem for singular varieties is used. These deductions do not exclude primitive twist three, and no full-boundary invertibility or complete proof repair is claimed.

No selected coefficients, rank samples, experiments, or external writes are used.
