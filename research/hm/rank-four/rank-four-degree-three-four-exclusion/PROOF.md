# No cubic or quartic components of the rank-four curve

## Statement and hypotheses

Work over C, with the projective Schrödinger normalizer N=A⋊G, A=F5² and G=SL2(F5), acting on P(V)=P4. Import from ../rank-four-line-component-exclusion/PROOF.md the N-invariance and bounds dim Z5≤1 and deg Γ4≤125, where Γ4 is the reduced curve part of Z4, and the honest G-representation V=T⊕W with irreducible summands of dimensions three and two. The central involution acts by +1 on T and −1 on W. The representation T factors through the irreducible three-dimensional icosahedral representation of A5.

**Theorem.** Γ4 has no integral curve component of degree three or four. Together with the no-line theorem and ../rank-four-canonical-conic-exclusion/PROOF.md, every irreducible component of Γ4 has degree at least five.

In fact the argument excludes degree-three/four components in any N-invariant reduced curve of total degree at most125. It requires no rank calculation beyond this degree bound. A component here is reduced and integral; singular curves are included.

## 1. Preliminary facts about spans and normalizations

Let C have degree d=3 or4, and let P(U) be its span, of projective dimension r. Then 2≤r≤d. The upper bound follows from h0(ν*O_C(1))≥r+1 and h0(L)≤deg L+1 for a positive-degree line bundle on the smooth normalization ν:X→C. An integral curve spanning a line is that line, so r≥2.

If r≥3, Castelnuovo's bound gives genus g(X)≤1: for r=3 and d=3,4 the bounds are respectively0,1; for r=4,d=4 the bound is0. In particular a nondegenerate quartic in P4 has rational normalization.

A group of projective transformations preserving C acts faithfully on X if its restriction to P(U) is faithful. Indeed a transformation fixing C pointwise has C contained in the union of the projectivized eigenspaces of a linear representative. Integrality puts C in one eigenspace; its span is U, so the representative restricts to a scalar on U. Normalization preserves this faithfulness assertion.

We will use two low-genus facts.

(a) C5² cannot act faithfully on P1. The centralizer in PGL2(C) of an element of order five is a torus, whose finite subgroups are cyclic.

(b) An automorphism of order five of a genus-one curve is a nontrivial translation. Indeed its image in the automorphisms fixing an origin, a cyclic group of order2,4, or6, is trivial. A translation t_p by a point p of order five cannot preserve a line bundle L of degree3 or4: under Pic0(E)≅E, t_p*L⊗L^−1 corresponds up to sign to (deg L)p, which is nonzero. Thus a faithful order-five automorphism preserving a degree-three/four polarization is impossible in genus one. This applies to the pullback of O_C(1), whether or not C is smooth or linearly normal.

## 2. A component fixed by all of A is impossible

If A_C=A, its span is invariant under the irreducible Heisenberg representation and therefore U=V. Necessarily d=4, and X≅P1 by §1. The A-action on X is faithful because C spans P(V). This contradicts §1(a).

## 3. A component with trivial A-stabilizer

Suppose A_C=1. Put K=N_C and let H be its image in G. Then K≅H and

    |N·C|=25[G:H].

The degree bound d|N·C|≤125 gives [G:H]≤1 for either d=3 or4. Thus H=G, and K is a complement to A. As recalled in the line-exclusion proof, a cocycle c:G→A is a coboundary: if z is the central involution, then 2c(h)=(1−h)c(z), so c(h)=a−ha for a=c(z)/2. After A-conjugation, K=G.

Now U is G-invariant. Complete reducibility and the inequivalent irreducibles T,W show that U is T or V, since dim U≥3.

### 3.1 The plane case U=T

The equation of the integral plane curve spans a G-invariant line in Sym^d(T*). Since G is perfect, this line must be the trivial representation. The dimensions of the invariant cubic and quartic spaces are respectively0 and1, and the latter is spanned by q², where q is the invariant quadratic form. For completeness, average the characters over A5. Its conjugacy-class sizes are1,15,20,12,12, and the eigenvalues on T at an element of rotation angle θ are1,e^{iθ},e^{−iθ}. The characters of Sym³T and Sym⁴T, in the identity/order2/order3/two order5 classes, are

    Sym³T: (10, −2, 1, 0, 0),
    Sym⁴T: (15,  3, 0, 0, 0).

Their averages are0 and1. The two choices of the three-dimensional icosahedral representation exchange the order-five classes and give the same result. The nonzero invariant q supplies q² in degree four. There is therefore no invariant cubic equation and no integral invariant quartic equation.

### 3.2 The full-span case U=V

Here d=4 and X≅P1. The G-action on X is faithful by §1. But G cannot embed in PGL2(C). To see this without classifying finite subgroups, its nontrivial central involution would have image an involution whose centralizer is the solvable group G_m⋊C2. All of the embedded G would lie in this centralizer. This is impossible because G is nontrivial and perfect. Thus this case also fails.

## 4. Axis-stable planar components

Suppose |A_C|=5 and r=2. Conjugate its axis to <Z>, where Z e_j=ζ^j e_j, j∈F5. The span U is the span of a three-element subset S of these five eigenlines.

The N-orbit of this plane has exactly60 planes. For a fixed axis, A-translations and the diagonal torus induce all affine transformations j↦aj+b. These act transitively on the ten three-element subsets: complements are two-element subsets and the affine group is transitive on unordered pairs. There are six axes, and their sets of invariant proper subspaces are disjoint, since invariance under two distinct axes would give invariance under all of A and contradict Heisenberg irreducibility. Every translate of U is invariant under a conjugate axis, so the count is exactly6·10=60.

Each plane in this orbit is the span of at least one translate of C, and distinct spans give distinct curves. Thus d|N·C|≥3·60=180>125. No such planar component occurs.

## 5. Axis-stable hyperplane components

Continue with |A_C|=5, now r=3. The span U is generated by four Z-eigenlines. Its orbit has exactly30 hyperplanes: five choices of missing eigenline for each of the six axes, by the same argument as §4.

The diagonal normalizer element

    D e_j=ζ^{j²}e_j

fixes each such span and commutes with Z. The projective group B=<Z,D> is C5², and its restriction to P(U) is faithful. In fact Z^aD^b restricts to a scalar only if the polynomial aj+bj² takes a constant value at the four distinct indices spanning U. A polynomial of degree at most two cannot have four roots unless it is zero, so a=b=0.

If D fixed C, the faithful B-action would lift to X. When g(X)=0 this contradicts §1(a). When g(X)=1, even the subgroup <Z> contradicts §1(b), since it acts faithfully and preserves ν*O_C(1), of degree3 or4. Hence D does not fix C. Its order is five, so C,DC,...,D⁴C are five distinct orbit curves with the same span.

Conjugating this construction to every one of the30 orbit hyperplanes produces at least five curves over each. Consequently |N·C|≥150, contradicting the degree budget.

## 6. Axis-stable full-span quartics

The only remaining case has |A_C|=5, U=V and d=4. Its normalization is P1. Let K=N_C, and let H be its image in G. Since A_C is normal in K, H preserves its axis and lies in the axis stabilizer B_G⊂SL2(F5), of order20.

We claim that 5 does not divide |H|. Otherwise Cauchy's theorem gives an element u∈H of order five. Such an element of B_G is nontrivial unipotent, fixes the axis pointwise, and satisfies (u−1)²=0 on A. Choose a lift k=(a,u)∈K in A⋊G. Then

    k^5=(Σ_{i=0}^4 u^i a,1)=(5a+10(u−1)a,1)=1.

Thus k has order five, centralizes A_C, and is not in A. The group <A_C,k> is therefore C5². Since C spans P(V), it acts faithfully on its rational normalization, contradicting §1(a). This proves the claim.

As |H| divides20 and is prime to5, |H|≤4. Therefore

    |K|=5|H|≤20,
    |N·C|=3000/|K|≥150.

This again violates the degree budget. Notice that the lift k need not be the particular diagonal D, and may carry a nonzero translation part. The order-five calculation is essential to covering those stabilizers.

## 7. Conclusion and scope

The possibilities |A_C|=1,5,25 and r=2,3,4 have all been exhausted. No integral cubic or quartic is a component of Γ4. The earlier audited exclusions of lines and conics therefore imply that every irreducible curve component of Γ4 has degree at least five, and in particular Γ4 has at most25 irreducible curve components.

This does not prove Γ4 empty, does not exclude degree-five or higher curves, and says nothing new about isolated points of Z4. The no-conic input uses the actual operation's structurally proved image dimension20; the cubic/quartic exclusion itself only uses the normalizer representation and degree budget. No actual source tensor, source coefficient, selected source input, or operation matrix was evaluated.
