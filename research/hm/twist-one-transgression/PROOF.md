# Twist-one transgressions and the universal cubic obstruction

Work over C on P^4. Let F be the normalized Horrocks–Mumford bundle, B=End_0(F), S=Sym(T), T=H^0(O(1))=V*. This note gives an exact structural obstruction criterion for generation of H^1B(3) from H^1B(2). It reduces H^2B(1) to two scalar intertwiners, but does not prove either scalar nonzero. In particular it does not assert H^2B(1)=0 or universal cubic surjectivity.

## 1. Pinned inputs and notation

Use PR453 at 56516a96a7eacfde0c8e272ca38db415cc7f294b and PR452 at 3b1d18105fa8b8b39bd96d889a34bc81a860f181 for normalizer notation and the equivariant section resolution. Write A=theta V and use the G=SL_2(F_5) representations W,W',U,U',Q,J,R of dimensions 2,2,3,3,4,5,6 as there. In particular Q is the odd four-dimensional representation, not the even section representation T_4.

The section resolution coefficients are

B_3=W', B_2=A tensor Q, B_1=A* tensor (W+J), B_04=V* tensor U, B_03=T_4.

Tensor the resolution by F(t+1), obtaining a locally free resolution of G(t)=End(F)(t), with terms

E_3=B_3 tensor F(t-7), E_2=B_2 tensor F(t-5), E_1=B_1 tensor F(t-4),
E_0=B_04 tensor F(t-3) + T_4 tensor F(t-2).

Put L=im(E_2 to E_1), K=im(E_1 to E_0). The three short exact sequences are

0 to E_3 to E_2 to L to 0,
0 to L to E_1 to K to 0,
0 to K to E_0 to G(t) to 0.

Positive intermediate cohomology of G(t) and B(t) agrees. The primary module M_j=H^1F(j) is A*, A tensor W', V tensor W', W' in degrees 0,1,2,3, respectively, and zero otherwise; H^2F(s) is W at s=-2 and zero otherwise. Serre duality is H^3F(s)=M_{-s-4}*, H^4F(s)=H^0F(-s-4)*. Also H^0F(s)=0 for s<3.

Import H^0B(1)=0 from PR91 at 872aca45943d3758e261a900e5984b981c18b3c4, and H^2B(t)=0 for t>=2 from PR94/167. These are structural dependencies, not tensor-table inputs.

## 2. The two possible twist-one channels

At t=1, H^1E_0=0, H^2E_0=B_04 tensor W, and E_1 is acyclic. Also E_2 has only H^3=B_2 tensor M_0*, while E_3 has only H^3=B_3 tensor M_2*. Thus the three exact sequences identify

H^1K = ker f, H^2K = coker f,
f: B_3 tensor M_2* to B_2 tensor M_0*.

Since H^0E_0=0, the third sequence identifies ker f=H^0G(1)=T, using PR91. The source is V* tensor (1+U'). The target is

A tensor A tensor Q = V* tensor ((U+W') tensor Q)
= V* tensor (W+Q+R+U'+J).

Here A tensor A = V* tensor (U+W') is obtained by dualizing A* tensor A*=V tensor (U+W'); duality does not exchange the primes. Semisimplicity and the known kernel T=V* force the image of f to be exactly the unique V* tensor U' summand. Therefore

H^2K = V* tensor (W+Q+R+J).

The third exact sequence now gives

H^1B(1) to V* tensor (W+Q+R+J) --Delta--> V* tensor (W+Q) to H^2B(1) to 0.

All maps are normalizer equivariant. The four source constituents are pairwise nonisomorphic irreducibles; each of the two target constituents occurs once. Consequently Delta has two possibly nonzero scalar components alpha on W and beta on Q, and vanishes on R and J. Nonvanishing is independent of the scalar choices in abstract representation identifications. Hence

H^2B(1) is one of 0, V* tensor W, V* tensor Q, V* tensor (W+Q),

with dimensions 0,10,20,30. In particular H^2B(1)=0 if and only if both alpha and beta are nonzero. Multiplicity one alone does not establish this condition.

## 3. The exact Koszul obstruction, including the incoming transgression

Put Z=H^2B(1) and
C_3=coker(T tensor H^1B(2) to H^1B(3)).

The coordinate sections of O(1) have no common zero, so their sheaf Koszul complex is exact. After tensoring by B(3), its hypercohomology is zero. Its first page has

E_1^{-p,q}=exterior^p T tensor H^qB(3-p), 0<=p<=5,

and d_r has bidegree (r,1-r). Let

A_2=coker(exterior^3 T tensor H^2B(0) to exterior^2 T tensor Z),
A_3=coker(exterior^5 T tensor H^3B(-2) to exterior^4 T tensor H^3B(-1)).

Then there is a canonical exact sequence

A_3 --d_2--> A_2 --d_2--> C_3 to 0.                 (1)

To check every potentially relevant term, H^2B(2)=0 is imported. At t=0, H^3E_0=0 and H^4E_1=0; the image sequences give H^4K=0, hence H^3B(0)=0. At t=-1,-2, H^4E_0=0, so H^4B(-1)=H^4B(-2)=0.

Thus A_2=E_2^{-2,2} and A_3=E_2^{-4,3}. The term E_2^{0,1}=C_3 has no outgoing differential and can receive only d_2: its d_3 and d_4 sources are zero by H^3B(0)=H^4B(-1)=0. Zero abutment makes that d_2 surjective. The term E_3^{-2,2}, after taking its incoming and outgoing d_2, has no possible further nonzero differential: the only possible higher incoming source is E_3^{-5,4}=0 by H^4B(-2)=0. Zero abutment therefore makes E_3^{-2,2}=0, proving exactness at A_2. This is not an identification of C_3 with A_2 unless the incoming transgression has been controlled.

The outgoing transgression has a concrete cocycle construction. On an affine cover, represent an element of exterior^2 T tensor Z by a Cech cocycle b. Since H^2B(2)=0, the horizontal Koszul boundary of b is a vertical coboundary: choose c in T tensor Cech^1(B(2)) whose vertical boundary is that Koszul boundary. With compatible total-complex signs, the Koszul boundary of c is a cocycle in B(3), defining a class in C_3. Changing the choices produces exactly the equivalences in (1). For the incoming map, start instead with a cocycle in exterior^4 T tensor H^3B(-1), use H^3B(0)=0 to solve its horizontal boundary, and apply the next horizontal boundary.

The unresolved negative group H^3B(-1) has a retained incoming presentation:

H^3B(-1)=coker(B_1 tensor M_1* to B_04 tensor M_0*).

Indeed H^4E_1=0 at twist -1, hence H^4K=0; the third sequence gives H^3G as a cokernel from H^3K to H^3E_0, and H^3E_1 maps onto H^3K since H^4L=0. The latter follows from H^4E_2=B_2 tensor H^0F(2)*=0. This presentation does not assert that the cokernel vanishes. At twist -2, H^4E_2=B_2 tensor H^0F(3)* is nonzero, so the analogous shortcut is not justified. The actual cohomology group H^3B(-2), with its natural multiplication map, is retained in A_3.

## 4. Consequence for universal cubics

The same Koszul argument gives surjectivity T tensor H^1B(t-1) to H^1B(t) for t=4,5: the potential incoming sources are exterior^2 T tensor H^2B(t-2), exterior^3 T tensor H^3B(t-3), and exterior^4 T tensor H^4B(t-4). The first groups vanish since t-2>=2. The second groups vanish because H^3E_0=H^4E_1=0 at twists 1,2. The last groups vanish because H^4E_0=0 at twists 0,1.

Therefore S_2 tensor H^1B(3) maps onto H^1B(5), and there is a natural surjection

S_2 tensor C_3 to H^1B(5)/(S_3 H^1B(2)).            (2)

This is well defined because S_2 T=S_3. Combining (1) and (2) yields a concrete sufficient criterion for universal cubic generation: if the incoming transgression A_3 to A_2 is surjective, then S_3 H^1B(2)=H^1B(5). In particular both alpha and beta being nonzero suffices. Conversely, a failure of universal cubic generation forces C_3 nonzero, forces failure of that incoming transgression to be surjective, and forces at least one of alpha,beta to vanish. None of these implications is reversed without further information: degree-three generator classes may die under all quadratic multiples before degree five.

This excludes diagnosing a universal cubic failure merely from a nonzero H^2B(1), or merely from the two-dimensional/four-dimensional multiplicity alternatives. The exact incoming Koszul transgression and subsequent quadratic multiplication must both be retained.

## 5. Sources and scope

PR453: https://github.com/Akilleez-QA/read-em-and-weep/pull/453
PR452: https://github.com/Akilleez-QA/read-em-and-weep/pull/452
PR451 degree-five presentation: https://github.com/Akilleez-QA/read-em-and-weep/commit/ed8841c18f103e71b84c0e9376e20a2a4ed2ef9c
PR91: https://github.com/Akilleez-QA/read-em-and-weep/commit/872aca45943d3758e261a900e5984b981c18b3c4
PR94: https://github.com/Akilleez-QA/read-em-and-weep/commit/73917b562c26be3c7999b005bf6f2514206eaf43
PR167: https://github.com/Akilleez-QA/read-em-and-weep/commit/063da90fc4543304e87e701cdefcc08225412f17
Primary representations: Horrocks and Mumford (1973), Lemma3.3 and Appendix, https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

This note uses no selected HM/source instance, evaluated differential, numerical rank, generator/checker, or computational tensor table. It does not prove H^2B(1)=0, cubic generation, the fixed-pair order-five quotient vanishing, actual-source membership, a higher-order lift, or algebraicity. The new contribution is the two-channel structural exclusion together with the full exact Koszul transgression criterion and its propagation to universal cubics. Mathematical review is distinct from formal verification.
