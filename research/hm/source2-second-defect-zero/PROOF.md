# Source2 has zero second primal Gauss defect

## Result and boundary

Fix the hypothetical actual source with stable ID **G3.21.d610e381ed75**, source index 2 and maximal profile (k,l)=(2,1). In the notation of the pinned source papers,

\[
A_{\rm quot}=E/E^-=\mathcal O(-8)\oplus\mathcal O(2)\oplus\mathcal O(16),
\qquad B=Q^*/(Q^*)^-=\mathcal O(-18)\oplus\mathcal O(-4)\oplus\mathcal O(6).
\]

Let K=E^- and M=E^{--}. The second primal injection

\[
J=K/M\longrightarrow A_{\rm quot}(-2)
\]

has **zero torsion cokernel**. Consequently

\[
\deg M=-68,\qquad
J\simeq\mathcal O(-10)\oplus\mathcal O\oplus\mathcal O(14).
\]

In addition, for the genuine constant-quotient residual R of PR751,

\[
R^+\simeq S\mathcal O(-5)\oplus W\mathcal O(-17),\qquad
R^{++}\simeq D\mathcal O(-4)\oplus A_{\rm std}\mathcal O(-16).
\]

Here S=Sym^3 W, D=Sym^4 W and A_std=Sym^2 W. These are isomorphisms of equivariant bundles, not horizontal splittings. Both forward transforms are saturated in the genuine constant ambient bundle; their ranks/degrees are (6,-54) and (8,-68).

This removes every positive second-defect alternative for this source, including the remaining weight-zero length-twelve branch and all sixteen combinations retained under PR736's particular tests. It does **not** remove the source2 quotient label, change the fixed frontier of 23 labels, identify an actual abstract parameter, prove realization, or settle the original rank-three problem. It does not repeat the abstract endpoint-existence theorem: the new input is everywhere second-jet independence and its transfer through the actual constant projections to the second primal defect.

## 1. Immutable inputs and notation

All bundles are on P(W)=P^1 over C. G is the binary icosahedral group. It is perfect, its projective action is A5, and every nonempty invariant effective divisor has degree at least 12. The latter follows because a point stabilizer in A5 is cyclic of order at most 5. Plus and minus denote saturated forward transforms and backward kernels for the original constant connection.

The following are published actual statements, not assumptions about an arbitrarily split connection.

1. [PR744's constant-span intersection](https://github.com/Akilleez-QA/read-em-and-weep/blob/063216038f3aefd65617651c2426721efafc7f9b/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-CONSTANT-SPAN-INTERSECTION.md): there is an invariant constant V0=Sym^10 W of dimension 11 in the actual 30-dimensional constant ambient H*, with
   \[
   Q^*\cap(V_0\otimes\mathcal O)=U_8^{10},\qquad
   U_j^e=\operatorname{Sym}^j W\otimes\mathcal O(j-e),
   \]
   where U_j^e has fiber ell^(e-j) Sym^j W in Sym^e W. Projection to Hbar=H*/V0 gives the saturated actual R, with rank 4 and degree -36. The source explicitly identifies R=Q*/U8^10 and displays its exact constant-quotient inclusion. In particular,
   \[
   0\to U_8^{10}\to Q^*\to R\to0
   \]
   is exact as a sequence of bundles. Thus Q*→R is sheaf-surjective, not a map onto a proper dense subsheaf of R.

2. [PR751](https://github.com/Akilleez-QA/read-em-and-weep/blob/e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-RESIDUAL-FULL-SPAN.md): there is an actual invariant constant V1=Sym^8 W=P+D inside Hbar, with
   \[
   R\cap(V_1\otimes\mathcal O)=U_2^8=A_{\rm std}\mathcal O(-6),
   \]
   and a saturated constant-quotient sequence
   \[
   0\to C=\mathcal O(-18)\to H_{\rm fin}\otimes\mathcal O
   \to(P+D)\mathcal O(2)\to0,
   \quad H_{\rm fin}=Hbar/V_1\simeq A_{\rm std}+V+P.
   \]
   The source explicitly identifies C=R/U2^8 in this sequence. In particular,
   \[
   0\to U_2^8\to R\to C\to0
   \]
   is exact as a sequence of bundles. Thus R→C is sheaf-surjective, not a map whose image still needs saturation, and all stated intersections and quotients are actual ones.

3. [PR754](https://github.com/Akilleez-QA/read-em-and-weep/blob/044add76ebb14043a0edf73171517c90b9ef0c13/research/hm/order-four-quadratic-load/ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md), Sections 1, 3 and 5: the degree-18 subsystem H=Hfin* in H0(O(18)) is basepoint-free, and its unique V copy is
   \[
   V_{18}=f_{12}V_6,\qquad V_6\subset\operatorname{Sym}^6W=V+P,
   \]
   where f12 is a nonzero invariant degree-12 form. This is an identification of invariant subspaces, with no selected coefficients or parameter. Basepoint-freeness also follows directly from the actual saturated line sequence in item 2.

4. [The (2,1) primal interior theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/063216038f3aefd65617651c2426721efafc7f9b/research/hm/order-four-quadratic-load/TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md), Section 1: rank E=17, deg E=-54, rank K=14, rank M=11, and, writing a=deg A_quot and s=length coker(J→A_quot(-2)),
   \[
   \deg M=-48-2a+s.\tag{1}
   \]
   For the source at hand a=10. The plateau gives rank Q*+=16 and rank Q*++=19 by Gauss duality with K and M.

The exact backward residual flag of [PR758](https://github.com/Akilleez-QA/read-em-and-weep/blob/063216038f3aefd65617651c2426721efafc7f9b/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-EXACT-RESIDUAL-GAUSS-FLAG.md) is consistent with these inputs, but is not substituted for any forward projection or jet argument below.

## 2. The V6 plane system is unramified and its Wronskian is f12

The base divisor of the three-dimensional system V6 is G-invariant and has degree at most 6. It is therefore empty. The associated map P^1→P(V6*) is nonconstant, since its three sections are linearly independent.

For a local coordinate z and local trivialization, write its evaluation vector as v(z). The expression v wedge v' is intrinsically a section of

\[
\Lambda^2V_6^*\otimes\mathcal O(12)\otimes\Omega^1
=\Lambda^2V_6^*\otimes\mathcal O(10).
\]

It is not identically zero: otherwise the nonconstant projective map would have identically zero differential in characteristic zero. Its common zero divisor is invariant and has degree at most 10, hence is empty. Thus v and v' are linearly independent at every point.

The plane Wronskian det(v,v',v'') is a section of

\[
\det(V_6^*)\otimes\mathcal O(18)\otimes(\Omega^1)^3
=\mathcal O(12).
\]

Here det(V6) is trivial because G is perfect. The Wronskian is nonzero by the characteristic-zero Wronskian criterion for three independent polynomials. It is invariant. Its divisor is therefore the reduced twelve-point orbit D12, the divisor of f12; equivalently it is a nonzero scalar multiple of f12. No invariant form is assigned coefficients in this argument.

## 3. Every relevant degree-18 system has independent jets through order two

Let H be any basepoint-free G-stable subsystem of H0(O(18)) containing f12 V6. Its evaluation vector projected onto the V6* block is f(z)v(z).

Off D12, the Wronskian of this block is f^3 det(v,v',v''), which is nonzero. Hence the full H system has three independent evaluation/derivative vectors there.

At p in D12, f(p)=0 and f'(p)≠0. The first three projected vectors are

\[
0,\quad f'v,\quad f''v+2f'v'.\tag{2}
\]

The last two are independent because v,v' are independent. The full evaluation vector at p is nonzero by basepoint-freeness and has zero V6* projection. Thus it is independent of the two full derivative vectors: projecting any relation to V6* first kills their two coefficients, then the nonzero full evaluation kills the remaining coefficient. All three are independent at p.

This proves full jets of orders 0,1,2 everywhere. Project the complete degree-18 Veronese osculating bundles

\[
U_k^{18}=\operatorname{Sym}^kW\otimes\mathcal O(k-18),\qquad k=0,1,2,
\]

to H*=Hfin. The proved jet ranks mean these maps are fiberwise injective. Their images are consequently subbundles, rather than merely generically injective subsheaves, and equal the saturated forward osculating bundles of C. In particular,

\[
C^+=W\mathcal O(-17),\qquad C^{++}=A_{\rm std}\mathcal O(-16).\tag{3}
\]

They are generated locally by c,c' and c,c',c'', respectively, without torsion or a saturation correction.

## 4. Forward growth in the actual second constant projection

Apply (3) to the actual sequence R→C from input 2. Fix a local coordinate and a local lift r in R of a generator c of C. A local frame of R consists of a frame of U2^8 and r; this uses only a local bundle splitting, not a horizontal or global splitting.

Differentiation of U2^8 generates U3^8, and two differentiations generate U4^8. The universal leading coefficients are 6 and 5, so these generated sheaves are already saturated subbundles of the constant V1. Locally the first two derivative-generated sheaves for R are exactly

\[
G_1=\langle U_3^8,r,r'\rangle,\qquad
G_2=\langle U_4^8,r,r',r''\rangle.\tag{4}
\]

This description follows from the Leibniz rule applied to the local frame; derivatives of arbitrary coefficient functions add only lower derivatives already displayed. Changing the local lift r changes these generators only by sections and derivatives of U2^8 already included in (4).

Projection to the genuine constant Hfin commutes with differentiation. Therefore the two extra generators in G1 project to the pointwise independent c,c', and the three in G2 to the pointwise independent c,c',c''. Each displayed generating map is fiberwise injective after choosing a frame of U3^8 or U4^8. Thus G1 and G2 have constant ranks 6 and 8 and are subbundles of Hbar tensor O. They are already saturated and are precisely R+ and R++. Their exact intersections with constant V1 are U3^8 and U4^8, and projection is everywhere onto the corresponding C transforms. We have genuine exact sequences

\[
0\to U_3^8\to R^+\to C^+\to0,\qquad
0\to U_4^8\to R^{++}\to C^{++}\to0.\tag{5}
\]

In particular,

\[
\deg R^+=4(-5)+2(-17)=-54,\qquad
\deg R^{++}=5(-4)+3(-16)=-68.\tag{6}
\]

For the stated bundle isomorphisms, the two extension groups vanish: their ordinary twisting differences are both 12, so they are H1 of constant coefficient representations tensored with O(12). Averaging over G gives equivariant splittings. This conclusion is used only to describe the bundles; the connection remains the original one.

## 5. Transfer through the first constant projection without losing saturation

Write p:H* tensor O→Hbar tensor O for the actual constant quotient by V0. The original Q* maps onto R. Because p is constant and R+ is generated without saturation by R and its derivatives, p(Q*+) contains R+ as a sheaf, not just generically. More explicitly, local sections of R lift regularly to Q*, and their derivatives lift to Q*+; the local generators in (4) therefore all lift.

Also Q*+ contains U9^10, the first forward transform of the actual U8^10. This is a saturated rank-10 subbundle inside constant V0. The plateau says rank Q*+=16, while rank R+=6. Thus ker(p|Q*+) has rank 10. This kernel is the intersection of Q*+ with constant V0 and is saturated in V0. It contains the already saturated U9^10 of the same rank, so it equals U9^10. Projection lands in R+ everywhere because it does so generically and R+ is saturated; the preceding local lifts make it surjective. Hence

\[
0\to U_9^{10}\to Q^{*+}\to R^+\to0.\tag{7}
\]

In particular deg Q*+=-10-54=-64, as independently required by deg K=deg E-deg A_quot=-64.

Differentiate (7). The next transform Q*++ contains the full constant V0=U10^10. Every local section of R+ has a regular lift in Q*+, so every generator of R++ also lifts to Q*++. Again projection lands in R++ everywhere by saturation. The plateau ranks are rank Q*++=19 and rank R++=8; the constant kernel V0 has rank 11. Consequently

\[
0\to V_0\otimes\mathcal O\to Q^{*++}\to R^{++}\to0.\tag{8}
\]

Equivalently Q*++ is the full inverse image of R++ under p. This is automatically saturated, since R++ is saturated in the constant quotient. In particular there is no unrecorded torsion defect in (8), and

\[
\deg Q^{*++}=\deg R^{++}=-68.\tag{9}
\]

All projections used here are by the published constant invariant spaces V0 and V1. No connection is imposed on a chosen equivariant complement.

## 6. The actual second defect is zero

For a saturated subbundle F in a constant bundle, duality for the constant derivative gives (F^-)^perp=(F^perp)^+ as saturated bundles. Indeed the annihilator of F+dF consists exactly of the local annihilating sections whose derivatives still annihilate F, by differentiating the pairing. Applying this twice with E^perp=Q* gives

\[
M=E^{--}=\operatorname{ann}(Q^{*++}).
\]

The exact annihilator sequence inside the 30-dimensional constant dual shows that M and Q*++ have the same degree. Thus deg M=-68 by (9). In (1), a=10, so

\[
-68=-48-20+s=-68+s.
\]

Hence s=0. The equal-rank injection J→A_quot(-2) is therefore an isomorphism, giving the claimed J splitting. This is an actual same-source second-fundamental compatibility deduction, not a construction or selection of an abstract endpoint.

## Novelty check and what remains

PR751 establishes the constant quotients and the final balanced line. PR754 proves the abstract balanced locus is a projective line minus two points. PR758 proves the backward residual flag (4,2,1,0). None of those cited proofs gives the everywhere second-jet property (3), the forward exact sequences (5), or the torsion-free second primal injection deduced here. PR736 retains the weight-zero length-twelve branch as three strata and sixteen endpoint/stratum combinations after its tests; this proof excludes that entire branch, not merely another stratum. The fixed source2 label still remains possible with s=0.

The proof neither assigns the P-multiplicity parameter nor evaluates any actual source coefficient, point, derivative, matrix or rank. Formula (2) is a universal local identity, not a selected-instance evaluation. No model experiments or large computations occur. The remaining problem is compatibility with the fixed original source beyond these necessary Gauss conditions; this theorem supplies neither that compatibility nor an exclusion of all source2 realizations.
