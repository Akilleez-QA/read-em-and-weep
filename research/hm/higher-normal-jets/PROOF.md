# Equivariant higher normal thickenings of the twenty-five rank-nine lines

## Scope and dependency

This note concerns the actual primary evaluation degeneracy scheme D in P(A), not the residual beta/lift problem or selected source coefficients. Its input is PR563, commit 56c3c4c37bd51fc710eec4b80662c5506f357f8f, stacked on PR562 and PR561. No actual matrix, coefficient, rank sample, selected HM/source instance, or numerical search is evaluated here.

Fix any one of the twenty-five rank-nine lines L=P(R). Let I=SL2(F5) be its stabilizer complement. PR563 proves that R is a faithful odd two-dimensional representation, that the intrinsic normal derivative has rank two everywhere on L, and that its kernel and cokernel are respectively M=O_L(-5) and C=O_L(1). All these bundles and maps are I-equivariant. The linearized tangent bundle is T0=O_L(2) direct-sum O_L(-5).

We prove that D contains an I-equivariantly embedded split sixth normal thickening of L. This is an existence statement, not a claim that the embedding is canonical. The first possible obstruction to continuing the chosen thickening has order seven and lies in a one-dimensional invariant space. Its nonvanishing is not asserted.

## 1. A global smooth ambient section model

Write the evaluation as e:E -> V0 tensor O on P(A), with E=3Q(-1) of rank twelve and V0 of dimension ten. Set

Y=P(A) times P(V0*), F=pr1*(E*) tensor pr2*O(1).

The annihilator incidence Z is exactly the zero scheme of the section s of F induced by e: the tautological annihilator line composed with e. Thus Y is smooth of dimension thirteen and F has rank twelve. Along the graph C0=L times {k} of the unique rank-nine annihilator,

TY|C0 = O(2) direct-sum 3O(1) direct-sum 9O,
F|C0 = 3O direct-sum 9O(1).

The constant factors can carry nontrivial I representations; only their ordinary bundle splitting is used for cohomology. A rank-nine pivot eliminates nine annihilator variables and identifies Z with D on a neighborhood of C0. Consequently ds has constant rank eleven along C0, its kernel is T0, and its cokernel is C=O(1). This also follows by eliminating the nine invertible linearized annihilator directions and using the normal derivative of PR563.

The exact sequence 0 -> TL -> T0 -> M -> 0 splits since its extension group is H1(O(7))=0. Average a splitting over the finite group I to make it equivariant.

## 2. Inductive lifting lemma with all gluing obstructions included

Define the split truncated normal space

S_n=Spec_L( direct-sum from j=0 to n of M^(-j) ),

with truncated multiplication; equivalently it is the n-th infinitesimal neighborhood of the zero section in Tot(M). Its last ideal J_n=ker(O_Sn -> O_S(n-1)) is M^(-n)=O(5n) and is square-zero.

There is an equivariant map f_1:S_1 -> Z restricting to C0 whose first normal derivative is the chosen splitting M -> T0. Indeed start with S_1 -> L -> Y and add that derivation; s vanishes because ds kills the derivation. This map is a closed immersion.

Suppose an equivariant embedding f_(n-1):S_(n-1) -> Z has been obtained, with n>=2 and the same first normal derivative. Smoothness of Y gives local lifts to Y over S_n. Their differences form a Cech cocycle in TY|C0 tensor J_n. The obstruction vanishes because

H1(TY|C0 tensor J_n)=H1(O(5n+2) direct-sum 3O(5n+1) direct-sum 9O(5n))=0.

Hence a global lift g_n:S_n -> Y exists. All global lifts form a torsor under H0(TY|C0 tensor J_n). Since the preceding map is equivariant, I acts on this affine torsor. Averaging over the finite group in characteristic zero gives an equivariant lift.

The section error g_n*s vanishes modulo J_n and is therefore canonically an equivariant element

a_n in H0(F|C0 tensor J_n).

Here the identification is canonical because J_n is annihilated by the ideal of C0; it does not require trivializing F on S_n. Changing g_n by a derivation v changes a_n by ds(v). The obstruction is thus

o_n=[a_n] in H0(C tensor J_n)=H0(O(5n+1)).

It is I-invariant. If it vanishes, a_n is a section of B tensor J_n, where B=im(ds). The exact sequence 0 -> T0 -> TY|C0 -> B -> 0 and

H1(T0 tensor J_n)=H1(O(5n+2) direct-sum O(5n-5))=0

show that a_n has a global ds-preimage. Average that preimage to make it equivariant and correct g_n. This produces f_n:S_n -> Z. Conversely any lift into Z forces o_n=0. The obstruction class is independent of the ambient lift g_n with f_(n-1) fixed. No independence from an arbitrary change of the preceding embedding is needed or claimed.

Every constructed f_n remains a closed immersion. Locally at a point of L the completed source is C[[t,z]]/(z^(n+1)); the ambient map is surjective on its cotangent space because the first-order tangent directions TL and M are independent. Formal Nakayama therefore makes the completed local-ring map surjective. Since S_n is proper and the reduced map is the closed embedding L -> Y, the morphism is proper with finite fibers, hence finite. Completed local surjectivity then implies surjectivity of its finite structure-sheaf map, giving a closed immersion. Its image lies in the rank-nine open neighborhood and hence identifies with a closed subscheme of D.

This proof includes the global gluing obstruction for ambient lifts and the global correction obstruction. It does not assume a global nonlinear residual equation or an a priori smooth surface containing D.

## 3. Linearizations and invariant-section exclusion

For the action of I on L=P(R), every I-linearization on a fixed O(d) is isomorphic to the standard one: the difference is a character of I, since invertible global functions on P1 are constants, and I is perfect. Thus the central involution acts on O(d) by (-1)^d. In particular every invariant section of odd degree is zero.

For an even degree d, a nonzero invariant section has an A5-stable effective zero divisor on P1. A point stabilizer in a finite subgroup of PGL2 is cyclic: its derivative at the fixed point is faithful in characteristic zero. The possible nontrivial cyclic subgroup orders of A5 are 2,3,5. Therefore orbit sizes are 60,30,20,12. Every invariant effective divisor has degree a nonnegative integral combination of 12,20,30 (including 60 does not enlarge this semigroup).

There is precisely one orbit Omega12 of size twelve: the six cyclic subgroups of order five have disjoint two-point fixed sets, totaling twelve points. Its defining binary form F12 is invariant, not merely semi-invariant, because I has no characters. Likewise the unique size-twenty orbit Omega20 has an invariant defining form F20. The uniqueness follows from the ten order-three subgroups and their two-point fixed sets.

For n=2,4,6 the obstruction degree 5n+1 is odd. For n=3,5 the degrees are 16,26, neither a nonnegative combination of 12,20,30. Therefore all o_n for 2<=n<=6 vanish and the induction constructs an equivariant embedding S_6 -> D.

For n=7 the degree is 36. Its only expression in the orbit-degree semigroup is 3*12. Hence H0(O(36))^I is one-dimensional, generated by F12^3. For any chosen equivariant f_6 the obstruction is

o_7 = lambda F12^3.

No calculation or assertion of lambda is made. If nonzero, its zero divisor is exactly 3Omega12.

## 4. Local intrinsic consequence and multiplicity boundary

At any point of L the rank-eleven derivative of s permits formal elimination of eleven ambient variables, leaving a smooth two-variable formal ring and one residual equation h(t,z). L is z=0. The embedding of S_6 has an invertible first derivative in its surviving normal direction. Reparametrizing the two-variable formal ring therefore identifies the embedded source with z^7=0. Since it maps into Z, h lies in (z^7).

Thus all local residual orders below seven vanish intrinsically, regardless of the noncanonical global embedding choices. If L is a one-dimensional irreducible component and D has no surface component through its generic point, its generic scheme multiplicity is at least seven: over the function field of L the quotient surjects onto C(L)[z]/(z^7). If the residual equation is identically zero, the local scheme instead has dimension two; the multiplicity assertion is intentionally conditional.

The argument is algebraic at every finite truncation and uses completion only for the local elimination description. It does not prove convergence, a full infinite formal neighborhood, a smooth surface, normality, reducedness, higher lifting, source membership, Q4, or algebraicity of the original target. It does not decide lambda. It is a mathematical proof, not machine formal verification.

## Public dependency links

- https://github.com/Akilleez-QA/read-em-and-weep/pull/563
- https://github.com/Akilleez-QA/read-em-and-weep/commit/56c3c4c37bd51fc710eec4b80662c5506f357f8f
- https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6311388937
