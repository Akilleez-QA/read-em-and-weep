# Sharp abstract minimum genus for the affine normalizer

## Statement and scope

Let A=F₅² and G=SL₂(F₅), with its standard action on A, and let N=A⋊G, of order3000. The smallest genus of a smooth connected complex projective curve carrying a faithful N-action is exactly326.

This is the standing projective Schrödinger normalizer: its splitting is proved in ../rank-three-line-rank-constancy/PROOF.md, Sections 2–3. More generally, the splitting follows directly from the given extension and action. If t lifts central −I, then t² lies in A and is fixed by conjugation by t, which acts as inversion; hence t²=1. All lifts of −I are A-conjugate because conjugation changes their translation part by twice an arbitrary A element. Thus C_N(t) surjects onto G and meets A trivially, yielding N=A⋊C_N(t).

The lower bound imports ../binary-group-genus-thirteen/PROOF.md. The construction below is abstract and uses the Riemann existence theorem. It gives no degree50 embedding into P⁴, no compatible Schrödinger polarization, and no curve in the rank-four locus. Its purpose is to show that a genus obstruction for faithful N-actions alone cannot exclude the surviving genus326 case in PROOF.md.

## 1. Lower bound

Let X carry a faithful N-action, and set Y=X/A. The induced G-action on Y is faithful: an element acting trivially on C(X)^A lies in the Galois deck group A. The imported genus obstruction gives g(Y)≥14. Riemann–Hurwitz then yields

    2g(X)−2 ≥25(2g(Y)−2) ≥650,

so g(X)≥326.

## 2. A generating triple in N

Write elements of N as (u,g), with multiplication

    (u,g)(v,h)=(u+gv,gh).

To avoid confusing the normal subgroup A with a matrix, write

    R = [[0,−1],[1,−1]],
    S = [[0,1],[−1,0]],
    U = RS = [[1,0],[1,1]],

with entries in F₅. Direct multiplication gives R³=I, R≠I, S²=−I, and U=I+J where J≠0 and J²=0. Thus their exact orders are3,4,5.

The matrices R,S generate G. Indeed they generate U=RS, all lower unipotents U^t=[[1,0],[t,1]], and their S-conjugates, all upper unipotents. These elementary matrices generate SL₂(F₅), by ordinary row elimination. More explicitly, row additions first make the upper-left entry nonzero and eliminate the lower-left and upper-right entries; the remaining determinant-one diagonal matrix is also a product of elementary matrices, using

    E₁₂(a) E₂₁(−a⁻¹) E₁₂(a) = [[0,a],[−a⁻¹,0]],

and multiplying by S⁻¹ gives diag(a,a⁻¹).

Fix any v≠0 in A and define

    x=(0,R),   y=(v,S),   w=(xy)⁻¹.

The exact orders of x,y,w are3,4,5. For y this follows from I+S+S²+S³=0 and its order-four projection. The product xy=(Rv,U) has order five because

    I+U+U²+U³+U⁴ = 5I+10J =0

in characteristic five, whereas its projection U has exact order five. By definition xyw=1.

It remains to prove these elements generate N. Put H=⟨x,y⟩. Its image in G is all of G. The subgroup H∩A is an F₅-linear subspace invariant under G, because H surjects onto G and A is abelian. The standard module A is irreducible, so H∩A is either0 or A. If it is A, then H=N.

Suppose instead H∩A=0. Then H is a complement, described by a cocycle c:G→A, so H={(c(g),g):g∈G}. For z=−I, the equality zg=gz and the cocycle identity give

    c(z)−c(g)=c(g)+g c(z),
    2c(g)=(1−g)c(z).

Thus c(g)=(1−g)a for a=c(z)/2. Since x belongs to H, c(R)=0. But det(I−R)=3≠0 in F₅, so a=0. This forces c(S)=0, contrary to y=(v,S) with v≠0. Therefore H∩A=A and H=N. Consequently x,y,w form a generating product-one triple with exact orders(3,4,5).

## 3. The complex curve

The Riemann existence theorem applied to this triple gives a connected N-Galois cover X→P¹ with precisely three branch points and inertia orders3,4,5. Equivalently, send the three standard peripheral loops of the three-punctured sphere to x,y,w. Surjectivity gives a connected regular cover; compactification at the punctures gives the stated inertia indices and a smooth compact Riemann surface, hence a smooth complex projective curve with faithful deck action N.

Riemann–Hurwitz computes

    2g(X)−2
      =3000(−2+(1−1/3)+(1−1/4)+(1−1/5))
      =3000·13/60
      =650.

Hence g(X)=326, attaining the lower bound.

Moreover A acts freely on this constructed X. Inertia of order3 or4 has trivial intersection with A. The order-five inertia subgroup also has trivial intersection with A, because its projection to G has exact order five. All point stabilizers lie in conjugates of these inertia subgroups (and are trivial away from the branch fibers), while A is normal. Thus X→X/A is étale, and its quotient has genus14 by Riemann–Hurwitz.

## 4. What this settles, and what it does not

The abstract faithful-action lower bound326 is sharp. In particular, merely strengthening a statement about genera of faithful N-curves cannot exclude genus326. The projective realization, its degree50 line bundle and Schrödinger representation, or the rank-four equations must supply any further obstruction to the degree50 equality case.

No source tensor, source coefficient, selected source input, or problem-specific operation matrix was evaluated. The finite matrices above belong only to the abstract group SL₂(F₅), and the proof requires no group enumeration or large computation.
