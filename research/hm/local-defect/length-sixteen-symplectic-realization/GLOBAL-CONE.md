# Homogenization: a stable charge-four cone, not the HM kernel

## Statement

For the same epsilon=-1 and lambda in C* with lambda^4 !=1, homogenize the preceding matrices on P4 with coordinates [y:x1:x2:x3:x4]. Their middle cohomology is an H-equivariant rank-two reflexive sheaf F, nonfree exactly at v=[1:0:0:0:0], with equivariantly trivial determinant and

    Ext^1(F,O) at v = P,
    Ext^2(F,O) at v = D(P).

It is slope-stable and has

    c1(F)=0, c2(F)=4H^2, c3(F)=0, c4(F)=-86H^4.

On every hyperplane not containing v it restricts to a stable rank-two bundle E on P3 obtained from the charge-four linear symplectic monad. In particular this is NOT the hypothetical actual HM rank-eight kernel, which has c2=5 and full projective-normalizer equivariance. The construction realizes local data globally only after changing those required global inputs.

## Construction and local properties

Let A=O(1) tensor T and E0=O tensor V. The same linear L and constant J give

    O(-1) tensor T* --J L^t--> O tensor V --L--> O(1) tensor T.

The action on the five homogeneous coordinates is the given H action on x1,...,x4 and the trivial action on y; the representation factors T,V are those of the local proof. The O(1) convention is chosen so its coordinate sections have this displayed representation. Thus the maps are genuinely H-equivariant.

The candidate presentation has finite-length cokernel over C[x1,...,x4], so its homogeneous rank-drop locus is the origin. Consequently on P4 the cokernel Ptilde of L is supported only at v, with stalk the original length-sixteen module. The first map is injective, and the middle cohomology F is a vector bundle of rank two off v. In the affine chart y=1 its stalk at v is defined by the same matrices over C[x1,x2,x3,x4]_(x1,x2,x3,x4); its completion, not the uncompleted stalk itself, is the formal local module of PROOF.md. The same depth, torsion-freeness, orthogonal-complement and Ext arguments work over this algebraic regular local ring. Alternatively completion is faithfully flat and preserves the finite-length defects, so the local depth and nonfreeness conclusions descend. Thus reflexivity, self-duality and both defect identifications hold algebraically, with no additional singularities.

## Restriction and stability

A hyperplane avoiding v is the graph y=linear(x1,...,x4), so its x coordinates identify it with P3. On it the displayed complex is a monad with both endpoint exactness conditions everywhere. Its middle cohomology E is a rank-two bundle with c1=0.

The ten relation columns of L are linearly independent in degree one, by the independent candidate presentation. Thus the map on global sections C^10 -> H0(O_P3(1) tensor T) is injective, giving H0(ker L)=0. Since H1(O_P3(-1))=0, the first exact sequence of the monad then gives H0(E)=0. More generally H0(E(-d))=0 for d>=0: for d>=1 the middle O(-d)^10 has no sections, and H1(O(-d-1))=0 on P3.

A saturated rank-one destabilizing subsheaf of E would be O(d), d>=0. It would yield a nonzero section of E(-d), contradiction. Hence E is slope-stable. The identical argument on P4 proves H0(F(-d))=0 for d>=0, using H1(O_P4(-d-1))=0. A saturated rank-one subsheaf of the reflexive F is reflexive by the depth lemma with torsion-free quotient; on P4 it is O(d). Thus F is also slope-stable.

The instanton-type vanishing H1(E(-2))=0 also follows directly: the endpoint bundles of the twisted monad are O(-3)^4, O(-2)^10, O(-1)^4, all acyclic on P3. This observation is not needed for stability or the Chern calculation.

## K-class and Chern classes, including the singular correction

Taking Euler classes of the three-term complex gives

    [F] - [Ptilde] = 10[O] - 4[O(-1)] - 4[O(1)].

The plus sign for Ptilde when solving for F is essential. Because length(Ptilde)=16,

    ch(F) = 10 - 4 exp(-H) - 4 exp(H) + 16H^4
          = 2 - 4H^2 + (47/3)H^4.

Therefore c1=0, c2=4H^2 and c3=0. For c1=c3=0,

    ch4=(c2^2-2c4)/12.

Equating this with (47/3)H^4 gives c4=-86H^4. Higher Chern classes need not vanish for a reflexive coherent sheaf merely because its rank is two. Omitting the finite-length correction would incorrectly compute the K-class of a vector-bundle monad instead of this singular sheaf.

The global Euler characteristic provides an independent sign check:

    chi(F)=10 chi(O)-4 chi(O(-1))-4 chi(O(1))+16
          =10-0-20+16=6.

The hyperplane restriction has c2=4, exactly as the nonsingular charge-four monad. Thus neither a twist preserving c1=0 nor reinterpretation of the vertex defect turns this into the required c2=5 HM kernel. Moreover the singleton singular locus prevents full irreducible projective H5 equivariance: a unique singular point would have to be fixed, contradicting the absence of an invariant projective point. The H action used here is only the local stabilizer action extended with a fixed vertex.

## Scope

This is an explicit abstract algebraic construction, not an evaluation of a selected source/model instance. It establishes global realizability after relaxing the actual global Chern and symmetry constraints, and isolates exactly why those remaining constraints are indispensable. It does not alter the existing global rank-eight contradiction or prove any mixed/pure obstruction vanishing.
