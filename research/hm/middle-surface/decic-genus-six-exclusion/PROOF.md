# Exclusion of sectional arithmetic genus at most six for the invariant decic

## Statement and scope

Work over C. Put A=(F_5)^2 and G=A semidirect SL_2(F_5), with its standard action on A; |G|=3000. Let Y be an integral projective surface of degree ten, acted on faithfully by G. Suppose Y has an ample globally generated line bundle O_Y(1), with self-intersection O_Y(1)^2=10, defining a birational morphism onto its image, and a general scheme-theoretic hyperplane section C is integral with p_a(C)<=6. Then Y does not exist.

In particular this excludes the genus-six alternative in /research/hm/middle-surface/decic-middle-surface-constraints/PROOF.md. The other alternatives there reduce to {11,16}. No normality, smoothness, Cohen–Macaulay hypothesis, or equality between the sectional arithmetic genus and the genus on a resolution is needed. This statement uses the standard classification/minimal-model theorems for smooth complex projective surfaces, and the explicitly cited finite-group facts below.

## 1. Elementary facts about G

Write H=SL_2(F_5). Its upper and lower elementary unipotents generate H and have order five. H is perfect: for d=diag(2,3), conjugation multiplies the upper elementary parameter by 4, so [d,u(t)]=u(3t). Thus all upper unipotents belong to [H,H], and so do the lower ones by conjugation. They generate H.

Moreover [H,A]=A: the central element -I of H acts as -1 on A, so its commutators with A run through A, because -2 is invertible modulo five. Therefore G is perfect. In particular every homomorphism from G to a solvable group is trivial.

The standard H-module A is irreducible, so any G-normal subgroup of A is either 0 or A. Also C_G(A)=A, because the conjugation representation of H on A is faithful.

The subgroup P=A semidirect <u>, for a nonidentity upper elementary unipotent u, has order 125 and is nonabelian. It is a Sylow five subgroup.

## 2. The resolution and its moving section

Normalize Y, then take a smooth projective resolution f:S->Y. Set L=f^*O_Y(1). It is globally generated and nef, with L^2=10, hence big. A general D in the pulled-back hyperplane system is smooth and integral by Bertini. Resolution-exceptional curves lie over finitely many points of the normalization and therefore finitely many points of Y. A general hyperplane avoids these points. Thus D->C is finite birational: normalization is finite, and the resolution has no exceptional curve above C. It follows that D is the normalization of C.

Write g=g(D). Then 0<=g<=p_a(C)<=6 and adjunction gives

    K_S.L = 2g-2-L^2 = 2g-12 <= 0.

The action on Y induces a faithful birational action on S. We do not need to choose an equivariant resolution or an equivariant sequence of contractions.

## 3. The birationally ruled case

Suppose S is birationally ruled over a smooth projective curve B of genus b. If b>0, its ruling is birationally intrinsic: rational curves map constantly to B, and the induced base is unique up to isomorphism. The ruling map extends to S, either by resolving the map or using the fact that rational exceptional curves cannot map nontrivially to B. A general D is horizontal. Indeed, a vertical irreducible curve has nonpositive self-intersection, whereas D^2=10. The resulting nonconstant morphism D->B and Riemann–Hurwitz give b<=g<=6.

If b=0, S is rational. The faithful birational action embeds P in Cr_2(C). Serre's Theorem 5.1(i) says finite l-subgroups of Cr_2 over characteristic different from l are abelian of rank at most two when l>3. This contradicts the nonabelian P of order 125.

If b=1, Aut(B) is solvable: translations form an abelian normal subgroup, and automorphisms fixing the origin form a cyclic group of order 2, 4, or 6 in characteristic zero. Perfectness makes G act trivially on B. Then A acts faithfully on the geometric generic rational fiber, giving A inside PGL_2(overline{C(B)}), which is impossible. For an elementary proof, diagonalize an element of order five; its centralizer in PGL_2 is a torus, whose finite subgroups are cyclic. Every element of A centralizes it.

If 2<=b<=6, let K be the kernel of G->Aut(B). The intersection K cap A is G-normal in A, hence 0 or A. If it is A, the same generic-fiber argument gives the impossible embedding A inside PGL_2(overline{C(B)}). Hence K cap A=0. For k in K and a in A, the commutator [k,a] lies in both K and A; it is therefore trivial. Thus K is contained in C_G(A)=A, and K=0. So G acts faithfully on B. Hurwitz gives

    3000 = |G| <= 84(b-1) <= 420,

again impossible. This excludes every ruled case compatible with the section.

## 4. Reduction of the nonruled case to Kodaira dimension zero

Assume S is not birationally ruled. The classification/ruledness theorem gives kappa(S)>=0. Contract exceptional (-1)-curves to the unique smooth minimal model q:S->M. The standard minimal-model theorem for surfaces gives K_M nef and says every birational self-map of M is regular. Thus G acts faithfully by automorphisms on M.

The blowup formula gives K_S=q^*K_M+E, with E effective and q-exceptional. Both q^*K_M and L are nef, and E.L>=0. Consequently

    0 >= K_S.L = (q^*K_M).L + E.L >= 0.

Equality holds throughout, in particular g=6 and (q^*K_M).L=0. By the Hodge index theorem, the intersection pairing is negative definite on the orthogonal complement of L, since L^2>0. A nef divisor has nonnegative square. Therefore q^*K_M is numerically zero, and hence K_M is numerically zero.

No appeal to a general abundance conjecture is needed. Since kappa(M)>=0, some positive multiple mK_M has a nonzero section, with effective divisor F. Numerical triviality gives F.H=0 for an ample H; thus F=0. Hence mK_M is linearly trivial, so kappa(M)=0. The classification leaves exactly K3, Enriques, abelian, or bielliptic surfaces.

## 5. A small symplectic obstruction on a K3 surface

There is no faithful symplectic action of A=C_5 x C_5 on a complex K3 surface X.

Choose nonidentity a in A. A symplectic automorphism of order five on a K3 surface has exactly four fixed points (Nikulin; explicit statement in Garbagnati–Sarti, section 1). Since A commutes with a, it permutes these four points. A five-group has trivial image in S_4; therefore all of A fixes each of them. Fix one such point x.

A finite group fixing a smooth complex point acts faithfully on the tangent space if its action on the variety is faithful. This can be seen by analytic linearization: average local coordinates against the inverse tangent representation to obtain an equivariant coordinate map with invertible derivative. An element acting trivially on the tangent then acts trivially on a neighborhood and hence on the irreducible variety.

Thus A embeds in SL(T_xX)=SL_2(C), because the action preserves the nowhere-vanishing holomorphic two-form. Commuting finite-order matrices are simultaneously diagonalizable, so its image lies in {diag(t,t^-1)}. This torus has only a cyclic subgroup of elements of exponent five, of order five, contradicting |A|=25. No classification of finite subgroups of SL_2 is required.

If M itself is K3, G acts trivially on the one-dimensional space H^0(M,K_M), because G is perfect. Therefore its A subgroup is symplectic, and the preceding obstruction applies.

## 6. Enriques surfaces

Let pi:X->M be the canonical K3 double cover, with deck involution epsilon. Every automorphism of M has two lifts to X, and all lifts of G form a finite group Gtilde fitting into

    1 -> <epsilon> -> Gtilde -> G -> 1.

The extension is central, since the deck group has order two. More importantly, the abelianization of Gtilde is a quotient of C_2: the image of [Gtilde,Gtilde] in G is [G,G]=G, so Gtilde is generated by its commutator subgroup and the kernel C_2. The character of Gtilde on H^0(X,K_X) therefore has image of exponent at most two.

Let Ptilde be a Sylow five subgroup of Gtilde. Its projection to G is injective (the kernel has order two) and has order 125, hence identifies it with a Sylow five subgroup P of G. Since A is a normal five subgroup of G, A lies in P. The inverse image of A inside Ptilde is consequently a subgroup isomorphic to A. Every element of Ptilde has odd order, so the preceding character is trivial on Ptilde. This gives a faithful symplectic A-action on X, contradicted by Section 5.

Verified stronger alternative: perfectness makes the action on H^0(M,2K_M) trivial, i.e. semi-symplectic. Mukai–Ohashi, Proposition 4.2 and Corollary 4.3 of the current arXiv version, show that each such automorphism has a unique symplectic lift and that the whole lifted group is G x C_2. These are numbered 3.2 and 3.3 in an older version. The extension argument above does not require choosing this splitting.

## 7. Abelian surfaces

Write M=V/Lambda with V=C^2 and Lambda a lattice of rank four. Every automorphism is a translation followed by an origin-preserving group automorphism. Its linear part on V gives a homomorphism rho:G->GL_2(C). Perfectness implies det rho=1.

Let s in G have order five. If rho(s) is nontrivial, its eigenvalues are zeta^a,zeta^(-a) for a=1,2,3,4, where zeta is a primitive fifth root. The real-linear transformation preserves Lambda, so its real trace is an integer. On the other hand that trace is

    2(zeta^a+zeta^(-a)) = 4 cos(2 pi a/5),

which is either sqrt(5)-1 or -sqrt(5)-1 and hence irrational. This contradiction shows rho(s)=1 for every order-five element.

The group G is generated by A and the upper/lower elementary unipotents of H, all of order five. Therefore rho is trivial. All of G acts by translations, an abelian group. Since G is perfect, this action is trivial, contradicting faithfulness.

## 8. Bielliptic surfaces

A complex bielliptic surface has its intrinsic Albanese morphism M->B with B elliptic and smooth geometric generic fiber an elliptic curve. Automorphisms preserve this fibration and act on B, allowing translations on the Albanese torsor. Since Aut(B) is solvable and G is perfect, G acts trivially on B.

Faithfulness then embeds G into the automorphism group of the geometric generic genus-one curve over overline{C(B)}. Choose an origin on that curve. Its automorphism group is the extension of its abelian translation group by a finite cyclic origin-fixing group (characteristic zero), so is solvable. A perfect group has trivial image in a solvable group. This contradicts faithfulness and eliminates the last case.

## 9. Conclusion and exact dependencies

All birational possibilities are excluded. Thus no such decic has sectional arithmetic genus at most six. Applied to the established candidate set {6,11,16}, the surviving list is {11,16}.

There is no unresolved mathematical gap in the proposed argument after making the following points explicit: pull back the hyperplane system through normalization; use geometric, not arithmetic, sectional genus on S; do not assume contractions are equivariant; use uniqueness of the nonruled minimal model to descend the birational action; use Hodge index on q^*K_M, not an unproved pushforward-nef claim for L; and use the positive plurigenus already supplied by nonruledness to turn numerical triviality of K_M into torsion.

This proof does not exclude genus eleven or sixteen, nor assert the existence of an invariant decic. It does not transfer chi(O_Y) or p_a(C) to a resolution. It does not use any selected source matrix, numerical source computation, or external application mutation.

## Verified references

1. J.-P. Serre, “A Minkowski-style bound for the orders of the finite subgroups of the Cremona group of rank 2 over an arbitrary field,” Theorem 5.1(i), PDF p. 12 / printed p. 204. The theorem states that finite l-subgroups for l>3 are abelian of rank at most two. https://www.college-de-france.fr/media/jean-pierre-serre/UPL151543545980010914_9___A_Minkowski_style_bound.pdf
2. A. Garbagnati and A. Sarti, “Symplectic automorphisms of prime order on K3 surfaces,” arXiv:math/0603742v2, Section 1, pp. 2–3. Explicitly states four fixed points for symplectic order five and attributes it to Nikulin (Theorem 4.5 and section 5 of their reference Ni1). https://arxiv.org/pdf/math/0603742
3. S. Mukai and H. Ohashi, “Finite groups of automorphisms of Enriques surfaces and the Mathieu group M_12,” arXiv:1410.7535v2, Section 4, p. 15, Proposition 4.2 and Corollary 4.3. Explicitly verifies the two lifts, the unique symplectic lift for semi-symplectic automorphisms, and the group splitting. https://arxiv.org/pdf/1410.7535
4. G. Martin, “Automorphism group schemes of bielliptic and quasi-bielliptic surfaces,” arXiv:2008.11679, Introduction p. 2. Explicitly describes the bielliptic quotient and its Albanese morphism to an elliptic curve, with elliptic fibers. https://arxiv.org/pdf/2008.11679
5. R. Vakil, Complex Algebraic Surfaces, Class 19: direct author lecture notes giving the four Kodaira-zero classes. This is an authoritative exposition, rather than the original historical classification research. https://math.stanford.edu/~vakil/02-245/sclass19B.pdf . Course materials: https://math.stanford.edu/~vakil/02-245/index.html . Standard background used here also includes resolution, Bertini, adjunction, Hodge index, ruledness for kappa=-infinity, uniqueness/nefness of nonruled minimal models, Hurwitz, and the structure of genus-one automorphisms.
