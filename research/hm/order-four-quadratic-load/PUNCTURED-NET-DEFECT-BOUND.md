# A bounded primary defect on a two-parameter net

## Theorem

For every nonzero quadratic q0, there is a projective plane T=P2 in P(S2) through p=[q0] such that every point of T other than p induces an injective primary multiplication M0 -> M2. On this plane let

    phi : M0 tensor O_T(-1) -> M2 tensor O_T

be universal primary multiplication, with dim M0=5 and dim M2=10. Let Z be the closed subscheme defined by its maximal-minor ideal sheaf, and let C=coker(phi). Then:

1. Z is empty or zero-dimensional, with support contained in {p}, and length(Z)<=25.
2. There is an exact locally free resolution

       0 -> 5O_T(-1) -> 10O_T -> C -> 0.

   Thus C has rank five, has local projective dimension at most one, and is locally free away from p.
3. Writing sheaf Ext rather than global Ext,

       E = sheaf Ext^1_T(C,O_T)
         = coker(10O_T -> 5O_T(1)),

   one has I_Z E=0 and

       length(E) <= 15,

   and also length(E)<=5 length(Z).

   Higher sheaf Ext groups vanish.
4. If q0 is primary-good, then Z and E are empty/zero, and C is a vector bundle on all of T.

The theorem does not require determining whether q0 is primary-good.

## 1. Choice of the plane and the actual universal resolution

The codimension-at-least-three theorem for the primary-bad locus B in P(S2)=P14 supplies T through every p with T intersect B contained in {p}. Its proof is projection from p to P13: the image closure of B minus {p} has dimension at most eleven, and a general projective line avoids that closure. The corresponding plane through p has the required property.

On T the universal map phi is generically injective, because it is injective on every fiber away from p. Its sheaf kernel is therefore a torsion subsheaf of the locally free source. Since T is integral, that kernel is zero. This gives the displayed exact resolution, not merely a complex exact on the punctured plane.

At any point where a maximal minor is a unit, phi is a split inclusion over the local ring. Consequently C is locally free there. Set-theoretically, the maximal-minor locus is precisely the locus where fiber rank is below five, so Supp(Z) is contained in {p}.

## 2. A complete intersection containing Z

The maximal minors of phi are homogeneous quintic forms on T. Their common zero scheme has no positive-dimensional component. In particular they have no common irreducible polynomial factor.

Let V5 be their linear span. Choose any nonzero f in V5. There are finitely many irreducible factors of f. For every such factor h, the subspace of V5 consisting of multiples of h is proper, since h is not a common factor of all the minors. Over the infinite ground field C, finitely many proper linear subspaces cannot cover V5. Choose g outside their union. Then f and g are coprime quintics.

The plane complete intersection Y=V(f,g) is zero-dimensional and has scheme length 5 times 5=25 by plane Bezout. Since f and g belong to the maximal-minor ideal, there is a closed inclusion Z into Y, or equivalently a surjection O_Y onto O_Z. Hence length(Z)<=25. This argument uses the actual ideal sheaf, including any nonreduced structure at p, rather than only its reduced support.

If Z is empty the same bound is automatic. No chosen minor or coefficient is evaluated.

## 3. The exact annihilator argument

Applying sheaf Hom(-,O_T) to the length-one locally free resolution gives

    10O_T -> 5O_T(1) -> E -> 0,

and sheaf Ext^i_T(C,O_T)=0 for i>=2.

Work on an affine neighborhood trivializing O_T(1). The dual map is represented by a 5-by-10 matrix A over the coordinate ring. Choose any five of its columns, obtaining a 5-by-5 submatrix B. Its determinant is, up to sign, the corresponding maximal minor of phi. For every vector y in the free target module of rank five,

    det(B) y = B adj(B) y.

The right side lies in the image of A, since every column of B is a column of A. Thus det(B) annihilates coker(A). This holds for all five-column choices. Therefore the full maximal-minor ideal annihilates E locally, and the statement glues to I_Z E=0 on T. No assertion that the annihilator equals I_Z is needed.

At the sole possible support point p, E_p is a quotient of a free module of rank five over O_{T,p}, and I_{Z,p} annihilates it. Hence there is a surjection

    (O_{Z,p})^5 -> E_p.

Taking lengths gives length(E)<=5 length(Z)<=125. Twisting the target by O_T(1) does not affect this local argument or the length.

In fact the supports of E and Z agree: at a local point, E vanishes exactly when the dual map is surjective, equivalently when its five-by-five minors generate the unit ideal. Only support equality, not equality of the two schemes, is asserted.

## 4. The sharper bound: length(E)<=15

We now improve the elementary adjugate estimate. The resolution gives depth(C_p)>=1 at the only possible nonfree point p by the depth lemma over the regular local ring O_{T,p} of dimension two. Any torsion subsheaf of C is supported at p, because C is a bundle elsewhere. Such a subsheaf would be finite-length and contradict depth at least one. Therefore C is torsion-free.

Set F=C** and D=F/C. A reflexive sheaf on the smooth surface T is locally free, so F is a rank-five vector bundle. The sheaf D has finite length and is supported at p. The ten original sections generate F away from p, since F and C agree there. We do not assert that they generate F at p.

Choose four general linear combinations of these ten sections. They are independent outside a finite set: on T minus {p}, evaluation is surjective, and the rank-at-most-three locus of a general map from a four-dimensional space to a five-dimensional fiber has expected codimension two, or is empty. This dimension bound follows from the incidence of dependent four-tuples in the globally generated fibers. Adjoining the point p still leaves no divisorial dependence. Thus we obtain an injective map O_T^4 -> F that is a direct-summand inclusion at every codimension-one point.

Its cokernel is torsion-free. To justify the possible issue in codimension two, a local section of F lying in the generic span of these four sections has unique rational coefficients. At every codimension-one point those coefficients are regular, because the inclusion is a direct summand there. Normality of the local rings implies the coefficients are regular throughout the local neighborhood. Hence O_T^4 is saturated in F, which is precisely the torsion-freeness of the quotient.

The rank-one torsion-free quotient is therefore I_W(5) for a zero-dimensional subscheme W. Here det(F)=det(C)=O_T(5), obtained directly from the resolution; a rank-one torsion-free sheaf on a smooth surface equals its double dual line bundle tensored with a finite-colength ideal. Consequently

    c2(F)=length(W)>=0.

Meanwhile the resolution gives c(C)=(1-h)^(-5), hence c1(C)=5h and c2(C)=15h^2. From 0 -> C -> F -> D -> 0, additivity of the Chern character yields

    length(D)=c2(C)-c2(F)=15-length(W)<=15.

Finally, applying sheaf Hom(-,O_T) to this sequence gives E=Ext^1(C,O_T) isomorphic to Ext^2(D,O_T), since F is locally free. Over a regular local ring of dimension two, Ext^i of a finite-length module into the ring vanishes for i<2, and Ext^2 preserves length. One can see the length statement without a duality normalization: the Koszul resolution gives Ext^2(k,R)=k and lower Ext zero; induction on a composition series gives the assertion for every finite-length module. Thus

    length(E)=length(D)=15-length(W)<=15.

This proves the sharper bound. The auxiliary W need not be supported at p. Neither global generation of F at p nor local freeness of C at p was assumed.

## 5. Scope and dependency

The only HM-specific input beyond the actual primary multiplication is the established codimension-three bound in PRIMARY-BAD-CODIMENSION-THREE.md. The remaining proof is the general geometry of a generically injective linear 5-to-10 map on a projective plane, plane Bezout, and the adjugate identity.

The bounds quantify a possible primary specialization defect on a two-parameter net. They do not assert flatness of a family across p, invertibility of full adjoint multiplication, residual surjectivity, vanishing of Q4, or primary goodness of the original prescribed quadratic. The construction does not identify a new net member with the original source pair. These are uniform bounds, not selected-instance rank computations.
