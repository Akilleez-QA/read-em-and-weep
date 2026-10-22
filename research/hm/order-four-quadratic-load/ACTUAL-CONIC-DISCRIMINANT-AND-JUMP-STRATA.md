# The actual conic pencil is an isomorphism

## Statement

Let R=P(V) be the positive fixed plane of HM inversion, with its actual irreducible three-dimensional A5 representation V. Let F_R be the normalized HM restriction and put A=H1(F_R). The established stable Steiner resolution is

       0 -> A tensor O_R(-3) --M--> D tensor O_R(-2) -> F_R -> 0,
       dim A=3, dim D=5.

The actual symmetric conic-multiplication pencil is an A5-equivariant linear isomorphism

       mu:Sym^2 V* -> Sym^2 A,
       q |-> [q:H1(F_R(-2))=A* -> H1(F_R)=A].

Both its invariant channel and its five-dimensional channel are nonzero. Consequently:

1. The actual jumping-conic scheme is an irreducible reduced cubic hypersurface J in P(Sym^2 V*), projectively isomorphic to the symmetric determinant cubic.
2. Its scheme-theoretic singular locus is the inverse image under P(mu) of the rank-one Veronese surface. Thus it is a smooth degree-four Veronese surface in the conic parameter space.
3. For a smooth domain conic C_q, the precise splitting is determined by the actual rank:

       rank mu(q)=3:  F_C = O(-1) directsum O(-1);
       rank mu(q)=2:  F_C = O(0) directsum O(-2);
       rank mu(q)=1:  F_C = O(1) directsum O(-3).

   All degrees in this list are on P1. Rank zero is impossible for nonzero q, so O(2) directsum O(-4) never occurs on a smooth conic in R.
4. The unique A5-invariant conic in R is smooth and balanced.

The cubic J is not identified with the separate cubic discriminant of singular conics in the source parameter space. No assertion is made that every target rank stratum meets the smooth-domain-conic open. These intersections require their own proof.

## 1. Actual equivariance and the two channels

FIXED-PLANE-CONIC-BALANCE-AND-FOURTH-JETS.md proves that A is an irreducible three-dimensional A5 module, verifies the actual Serre-duality identification H1(F_R(-2))=A*, and proves symmetry of mu. The symmetry comes from cancellation of the alternating rank-two pairing sign with the degree-one cup-product sign. It also proves that mu is not the zero map.

These are genuine A5 representations: inversion acts trivially on F_R, as follows from the actual standard U=H0(F(3)) and its surjective evaluation on R. Both symmetric squares have multiplicity-free decomposition

       Sym^2 V* = 1 directsum 5,
       Sym^2 A  = 1 directsum 5.

Thus mu acts by one scalar on each of the two isotypic channels, after choosing equivariant identifications. Their values are not selected or evaluated below.

## 2. The five-dimensional channel cannot vanish

Twisting the Steiner sequence by minus two gives the canonical injection

       j:A*=H1(F_R(-2)) -> A tensor H2(O_R(-5))
                                      = A tensor Sym^2 V.

The multiplication pencil is exactly contraction of j with q in Sym^2 V*. The following Steiner cohomology differential is

       d_M:A tensor Sym^2 V -> D tensor V,

induced by the same linear presentation M. Its composite with j is zero.

Suppose the five-channel of mu were zero. Since mu is nonzero, it then has only its invariant scalar channel. Therefore

       j(a)=T(a) tensor r,

where T:A*->A is a nonzero invariant symmetric isomorphism and r in Sym^2 V is the nondegenerate invariant quadratic tensor. Nondegeneracy follows because the radical of an invariant form is an invariant subspace of the irreducible V.

Intrinsically M is a coefficient map A->D tensor V*. On the subspace A tensor r, the differential d_M is this coefficient map followed by contraction with r,

       A -> D tensor V* --id_D tensor r_sharp--> D tensor V.

A harmless common nonzero scalar depends on symmetric-tensor normalization. Since r_sharp is an isomorphism, d_M(T(a) tensor r)=0 for every a forces the entire coefficient map M to be zero. That contradicts its rank-three subbundle inclusion. Hence the five-channel is nonzero.

This uses the actual kernel relation d_M j=0. Nonzero abstract equivariance by itself would not exclude a scalar-only pencil.

## 3. The invariant channel cannot vanish

Let q0 span the invariant line in Sym^2 V*. Its form is nondegenerate, so C0=V(q0) in R is a smooth invariant conic. Suppose mu(q0)=0. The actual conic restriction sequence and H0(F_R)=0 give

       H0(F_C0)=ker mu(q0),  dim H0(F_C0)=3.

Since deg(F_C0)=-2, Birkhoff–Grothendieck then forces

       F_C0=O_P1(2) directsum O_P1(-4).

The maximal subline is unique, hence A5-stable. Its lower quotient is therefore a genuinely A5-linearized line bundle. After twisting by the ambient degree-three line bundle, whose degree on C0 is six, it gives an equivariant quotient

       F_C0(3) -> O_P1(2).

The A5-linearization on this degree-two line bundle is the standard one from O_R(1)|C0: any two linearizations differ by a character, and A5 has no nontrivial characters. Consequently its global sections are the irreducible three-dimensional module V*.

But the actual U=H0(F(3)) is the irreducible four-dimensional A5 module, and evaluation U tensor O_C0 -> F_C0(3) is everywhere onto because R is disjoint from the HM degeneracy lines. Composing with the displayed quotient produces a surjection onto O_P1(2), hence a nonzero equivariant map U->V*. This is impossible between inequivalent irreducibles. Therefore mu(q0) is nonzero. It is then an isomorphism A*->A by irreducibility.

Both channels are now nonzero. Their multiplicities are one, so mu is an isomorphism of six-dimensional vector spaces. No actual coefficient value or matrix-rank evaluation is involved.

## 4. An additional coefficient-representation consequence

In fact D is the irreducible five-dimensional A5 module. The coefficient map

       A tensor V -> D

is onto. Otherwise a nonzero constant functional D->C annihilating its image would descend through the Steiner presentation to a nonzero quotient F_R->O_R(-2). Such a homomorphism belongs to

       H0(F_R* (-2))=H0(F_R(-1))=0,

a contradiction. For irreducible three-dimensional A and V the tensor product is 1 directsum 3 directsum 5 when the representations agree, or 4 directsum 5 when they differ. Its only quotient of dimension five is therefore the irreducible 5.

This gives a second check of Section 3. Under its hypothetical splitting, F_C0(2) has the canonical equivariant quotient O_C0. The globally generating D tensor O_R->F_R(2), restricted to C0, would induce a nonzero map from irreducible D=5 to the trivial one-dimensional representation, again impossible.

## 5. Determinantal geometry and splitting strata

The actual restriction sequence identifies H0(F_Cq) with ker mu(q) for every nonzero conic equation, including singular conics. Stability and Serre duality also give H2(F_R(-2))=H2(F_R)=0. The universal restriction sequence therefore has the actual derived direct-image presentation [A* tensor O_P5(-1) --mu--> A tensor O_P5], in degrees zero and one. Its degree-one cokernel has zeroth Fitting ideal generated by det mu. Thus the natural jumping-conic determinant scheme is exactly this determinant, not a polynomial inferred from a matching Hilbert function. Since mu is a linear isomorphism, it pulls back the classical symmetric three-by-three determinant hypersurface.

That hypersurface is irreducible: matrices of rank at most two form the closure of the image X->X X^t for three-by-two matrices X, an irreducible parameter space. Its generic rank-two points are smooth, because their adjugates are nonzero; hence the determinant is reduced. The determinant gradient consists of the three diagonal cofactors and twice the three off-diagonal cofactors. Its singular scheme is therefore the rank-at-most-one symmetric determinantal scheme, namely the Veronese surface. The factors of two are units over C, and Euler's relation makes adding the cubic equation unnecessary.

For a smooth conic write F_C=O(a) directsum O(-a-2), a>=-1. Then h0(F_C)=0 if a=-1, and h0(F_C)=a+1 otherwise. Since mu(q) is nonzero for every nonzero q, its corank is at most two. This gives precisely the three splitting types in the statement and excludes a=2 everywhere on the smooth-conic open.

The projective singular surface is exact even if part or all of it consists of singular domain conics. Its intersection with the smooth-domain open, when nonempty, is precisely the O(1) directsum O(-3) splitting locus. Likewise the smooth-domain part of J outside that surface is precisely the O directsum O(-2) locus. No unproved incidence statement between the two distinct cubic discriminants is used.

## 6. Uniform second normal jets

Let Q be any smooth inversion-even quadric, let C=Q intersect R, I=I_(C/Q), and G=B_Q(4). Such C is smooth. The previous uniform conic analysis allowed a up to two. The new theorem removes that last possibility, so always -1<=a<=1.

The second normal graded piece is B_C(2) tensor Sym^2 W, where W is the two-dimensional odd equation space of R. Its three line degrees before the multiplicity-three factor are

       4, 2a+6, 2-2a.

All are now nonnegative. Therefore this piece has H1=0, h0=45, and even parity for every smooth even Q. Together with the previously established first two layers of dimensions27 and42 and their H1 vanishings, the ideal-power sequences prove

       H1(G/I^3G)=0,
       h0(G/I^3G)_+=72,  h0(G/I^3G)_-=42.

This is a uniform statement about sections on the second infinitesimal normal neighborhood, not a global extension theorem. The global adjoint restriction need not be onto these114 sections. Exact twist-four corank and the actual odd and positive boundary maps remain open.

## Dependencies and limits

The actual representation and pencil interfaces are proved in FIXED-PLANE-CONIC-BALANCE-AND-FOURTH-JETS.md and INVERSION-EVEN-TWIST-THREE-VANISHING.md. The uniform ideal-power and parity identities are in FIXED-CONIC-PARITY-JETS-AND-POSITIVE-GATE.md. All arguments concern the actual maps. No selected HM coefficients, actual rank tests, scans, or experiments are used.
