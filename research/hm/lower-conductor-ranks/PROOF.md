# Exact lower primary conductor ranks from normalizer multiplicities

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected actual HM/source coefficients, evaluation matrices, numerical rank tests, or large computation is used.

## 1. Inputs and theorem

Let S be the actual primary surface, nu:X->S its normalization, H=nu*O_S(1), and T=nu_*O_X/O_S. Write rho_n:H0(X,nH)->H0(T(n)), r_n=rank(rho_n), H5 for the finite Heisenberg group, Z for its center, and K=N/H5=SL2(F5).

Pinned inputs are:

- PR590, eb236dac3af8adcbc7f2f660b55e9d07904858c6, research/hm/degree-five-invariants/PROOF.md: actual N-linearization of the normalization sequence, node support in the six five-point Heisenberg eigenline orbits, and the actual equivariant conductor multiplication maps.
- PR591, 64a12e00718ec4cb09f17473237e879b08b28e16, research/hm/normalizer-residue-signs/PROOF.md: the order-four lift m=-P2 exchanges the two branches at p=[e0], its O(1) fiber scalar there is -1, the unipotent lift fixes both branches and has fiber scalar 1, and r5=29. Its Section 3 verifies the branch swap both from modular cusp pairing and from the two BHM tangent planes.
- PR588 (quadratic generation), 7547a6a0d84d29478a0bad2d30bda271c37c269e, research/hm/quadratic-conductor-generation/PROOF.md, Sections 3–5: Q2=im(rho2) has dimension five, im(rho_n)=P_(n-2) Q2 for n>=2, r3>=10, r4>=15. Here P_d=H0(P(A),O(d)). PR589, a1c77f791158cc0976df80220c958a50c2217ee3, research/hm/eigenline-postulation/PROOF.md, supplies r_n=30 for n>=6 using the pinned interpolation dependency. The local reviewed quadratic-generation proof also records that conclusion.
- PR574, 3c92fdc469f6870520e7a9d905b5ab9199a5bf37, research/hm/primary-conductor/PROOF.md: r0=r1=0 and h1(O_S)=30. PR592, 1a2822304e0e76d985f8a083fb36548127b881a1, research/hm/normalization-resolution/PROOF.md, Sections 6–7, independently supplies H1(X,nH)=0 for every integer n and the complete normalization Hilbert function; for n>=1 it is h0(X,nH)=5+(15/2)n(n-1). This replaces the older positive-twist vanishing dependency for the numerical consequences below.

Theorem. The complete sequence of nonnegative primary conductor ranks is

(r0,r1,r2,r3,r4,r5,r6,r7,...)=(0,0,5,15,25,29,30,30,...).

The new statements are r3=15 and r4=25. Their structural input is a determination of the full normalizer multiplicity of H0(T(n)) whenever 5 does not divide n. No ambient restriction isomorphism is inferred merely from equality of dimensions.

## 2. The multiplicity representation and its stabilizer line

Let epsilon be the primitive central character on O(1). For 5 not dividing n, let V_n denote the standard five-dimensional N-representation with central character epsilon^n. The subscript denotes central weight, not a tensor power. These representations are the Galois conjugates of the defining Schrodinger representation, including its dual.

All H5-irreducibles with this central character are isomorphic to V_n|H5. Consequently, with T_n=H0(T(n)), there is a canonical evaluation isomorphism

V_n tensor M_n -> T_n,   M_n=Hom_H5(V_n,T_n),   dim M_n=6.       (1)

The action on M_n is g.f=g_T f g_V^(-1); H5 acts trivially, so M_n is a genuine K-representation. This construction needs no choice of a splitting of N over K.

For each direction L in H5/Z, let W_(n,L) be the five-dimensional subspace of T_n supported on its five-node orbit. These subspaces are permuted by N. Let p=[e0] in the diagonal direction and H_p=<tau,Z>, of order 25, its stabilizer in H5. On the fiber F_n=T(n)_p, tau acts as 1 and the center as epsilon^n: the odd-order stabilizer cannot interchange branches, and tau's eigenvalue on e0 is 1. Therefore

W_(n,L)=Ind_(H_p)^H5(F_n).

Frobenius reciprocity or the elementary induced-section construction shows this is one copy of V_n. Thus the six lines Hom_H5(V_n,W_(n,L)) give a direction-indexed direct sum decomposition of M_n. The stabilizer of L in K is the Borel B of order twenty.

Evaluation at p gives the precise B-equivariant identification used to calculate its line character:

Hom_H5(V_n,W_(n,L)) -> Hom_(H_p)(V_n,F_n).                  (2)

For any lift fixing p, equivariance in (2) means the conjugation action g_F f g_V^(-1), not simply the fiber action. The right side is one-dimensional. In the universal Schrodinger coordinates, the unique tau-invariant line of V_n is Ce0, also after any primitive Galois conjugation or dualization. A functional in (2) is supported on that line.

Use the normalizer lifts u(e_i)=zeta^(i^2)e_i and m(e_i)=-e_(2i), allowing inverse index convention. Both fix p; their quotient images generate B. Horrocks–Mumford (1973), equations (1.4)–(1.5), printed pp66–67, give these lifts. On Ce0 in V_n, their eigenvalues are respectively 1 and -1. Galois conjugation preserves both rational scalars.

The actual branch action from PR591 gives u|F_n=1 and

m|F_n=(-1)_(branch) times (-1)^n_(twist)=(-1)^(n+1).

It follows from (2), dividing the fiber scalar by the V_n scalar, that the B-character on the multiplicity line is

lambda_n(u)=1,   lambda_n(m)=(-1)^n.                      (3)

Scalar lift ambiguities cancel in the Hom action. The square m^2 acts positively, so this character factors through B/{+I,-I}=D5. Since K acts transitively on directions, (1)–(3) prove

M_n=Ind_B^K(lambda_n),     5 not dividing n.                (4)

This is an actual target decomposition, not a proposed signed permutation model. The additional division by the standard representation's -1 is essential: the raw fiber sign alone would give the wrong answer in degrees three and four.

## 3. Decomposing the two induced representations

For even n, lambda_n=1. The six-direction action is doubly transitive, since the stabilizer's order-five subgroup acts transitively on the remaining five directions. Thus the unsigned permutation representation is

Ind_B^K(1)=1 + J5,                                        (5)

where J5 is irreducible of dimension five.

For odd n, lambda_n descends to the character of D5 that is +1 on its rotations and -1 on its reflections. Its induction factors through A5. Here is a direct check of its character, independent of a choice of residue coordinates. On A5 classes of orders 1,2,3,5a,5b its values are

(6,-2,0,1,1).                                            (6)

Indeed the identity fixes six directions. An involution fixes two directions, is a reflection in each of their D5 stabilizers, and contributes -1 at each. An element of order three fixes no direction. Each nonidentity order-five element fixes exactly its own Sylow-five direction and contributes +1. The two fixed directions for an involution can also be counted from incidences: there are six D5 stabilizers with five reflections each, and fifteen conjugate involutions, hence two per involution.

The two three-dimensional A5 irreducible characters have values

chi3=(3,-1,0,phi,phi'),    chi3'=(3,-1,0,phi',phi),
phi=(1+sqrt(5))/2, phi'=(1-sqrt(5))/2.

Their sum is (6). These are the two degree-three rows of the character table in Horrocks–Mumford's Appendix, printed p81. Thus

Ind_B^K(lambda_odd)=U3 + U3',                              (7)

with inequivalent irreducible summands. As a verification of multiplicities, the squared norm of (6), using class sizes 1,15,20,12,12, is (36+60+12+12)/60=2; its trivial multiplicity is (6-30+12+12)/60=0.

Combining (1), (5), and (7), the actual primitive-weight targets are

T_n = V_n tensor (1+J5)       for even n,
T_n = V_n tensor (U3+U3')     for odd n.                   (8)

All cited HM identities are from the primary source:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

## 4. Quartic rank

An N-submodule of V_n tensor M corresponds exactly to a K-submodule of M by the Hom_H5 equivalence in (1). Thus (8) in degree four shows the only possible dimensions of an N-stable image in T4 are 0,5,25,30. Since rho4 is N-equivariant and r4>=15, only 25 or 30 remains.

Choose an ambient linear form ell avoiding the thirty nodes. Multiplication by ell induces an isomorphism T4->T5 on section spaces, and takes im(rho4) into im(rho5), by O_S-linearity of the normalization sequence. If r4=30, then r5=30, contrary to PR591's r5=29. Therefore

r4=25.                                                   (9)

More precisely, the image is V4 tensor J5, and the degree-four defect is V4 tensor 1.

## 5. Cubic source and rank

We need the source representation, not only its dimension. Q2 has dimension five and central character epsilon^2, so its restriction to H5 is irreducible. It is the standard extension V2 as an N-module: after choosing an H5 intertwiner with V2, the ratio of the two N-actions is scalar by Schur's lemma, giving a character of K; K=SL2(F5) is perfect, so that character is trivial. The same argument identifies P1 with the standard representation of central character epsilon.

Horrocks–Mumford, Lemma 3.3(ix), printed p70, gives the character identity

h1 times theta(h1) = (chi3+chi2') times theta^3(h1),        (10)

where theta takes the fifth root to its square. The central weights on the left are 1 and 2, summing to 3, the weight of theta^3(h1), since 2^3=3 modulo 5. Apply the appropriate Galois conjugate of (10) so that h1 has weight epsilon. This includes the dual convention. Galois conjugation can exchange the two three-dimensional labels and the two two-dimensional labels, but preserves the dimensions and their central-involution parity. Thus

P1 tensor Q2 = V3 tensor (U + Wspin),                      (11)

where U is one of U3,U3' and Wspin is an irreducible two-dimensional K-representation with the central involution acting negatively. The primary-source derivation of the same identity is Lemma 2.4(ii), printed pp68–69.

Quadratic generation makes im(rho3) precisely the image of the N-equivariant multiplication map

P1 tensor Q2 -> T3=V3 tensor (U3+U3').

The only common multiplicity constituent of (11) and its target is U, occurring once on each side. Schur's lemma forces this image to have dimension either zero or 5 times 3=15. The independent bound r3>=10 excludes zero. Therefore

r3=15.                                                   (12)

The remaining three-dimensional target constituent gives H1(O_S(3)) as V3 tensor the other U3-type constituent. The proof does not require choosing which Galois label is named U3.

## 6. Cohomological consequences and boundary

Together with the pinned values, (9) and (12) give the theorem. For n>=1 the normalization long exact sequence identifies H1(O_S(n)) with coker(rho_n). Therefore

h1(O_S(n))=30,30,25,15,5,1,0,0,... for n=0,1,2,3,4,5,6,7,... .

Also h0(O_S(0))=1 and, for n>=1,

h0(O_S(n))=5+(15/2)n(n-1)-r_n.

In particular the complete section dimensions in degrees zero through five are

1,5,15,35,70,126.

They equal the corresponding ambient polynomial dimensions, but that numerical equality alone does not prove the ambient restriction maps are isomorphisms: a nonzero kernel and cokernel of equal dimension is not excluded by it. No new claim about the ambient ideal, projective normality, or ideal syzygies is made here. For n>=6 the complete section dimension is (15/2)n(n-1)-25.

This resolves the remaining two low primary conductor ranks by genuine normalizer representations and existing nonzero-image bounds. The separate full-adjoint primitive-twist-four/K4 connecting-map problem, prescribed-source membership, higher lifting, and algebraicity remain outside the conclusion.
