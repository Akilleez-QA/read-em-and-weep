# Abstract operator spans of every dimension: sharp ranks and exact root causes

## Scope and theorem

Work over C. Define the abstract operator space E=V⊗sl(U), with dim V=5 and dim U=2, as in ../universal-cofactor-normal-form/PROOF.md. The square-case transversality argument in ../universal-cofactor-higher-coranks/PROOF.md motivates the rectangular derivation below, which is included in full. No geometric-module identification is used.

For 1≤d≤5 and J∈G_d=Gr(d,E), let β_J:J⊗U→V⊗U be evaluation, W=JU its image, r=dim W, and P⊂V its minimal V-support, of dimension s. Then:

1. Exactly the ranks ceil(2d/3)≤r≤2d occur. Thus the rank ranges for d=1,2,3,4,5 are respectively 1–2, 2–4, 2–6, 3–8, 4–10.
2. For any W⊂V⊗U of dimension r and support dimension s, the space E(W) of traceless operators whose image lies in W has dimension 2r−s. In particular d≤2r−s, and s≥ceil(r/2).
3. Each nonempty exact-rank stratum S_(d,r) is smooth and irreducible, of dimension

   D(d,r)=d(15−d)−(2d−r)(10−r).

   The closed rank-at-most-r locus R_(d,r) is irreducible of the same dimension. The generic support dimension on either locus is min(5,2r−d).
4. At any exact-rank-r point, the local analytic matrix family is a generic (10−r)-by-(2d−r) matrix at zero, together with a smooth factor of dimension D(d,r). This statement applies to the actual ideals of minors, not only to reduced sets.
5. The minimum-rank cases admit the exhaustive, intrinsic parametrizations in Section 5. In particular d=3, r=2 holds exactly for J=v⊗sl(U); d=4, r=3 means support dimension two and complete saturation J=E(W); and d=5, r=4 splits exactly into support dimensions two and three.

These results apply before any assertion that five original operators are independent. Section 6 separates loss of effective span from additional evaluation syzygies exactly.

## 1. The image-support lemma

For a subspace W⊂V⊗U, define

   P(W)=span{(id_V⊗φ)(w): w∈W, φ∈U*}⊂V.

It is the unique minimal P with W⊂P⊗U. View Hom(U,W)=W⊗U* as a subspace of V⊗End(U). The vector-valued trace map τ:V⊗End(U)→V has kernel E. Its restriction to W⊗U* sends w⊗φ to (id_V⊗φ)(w). Its image is therefore exactly P(W), not merely a subspace thereof. Rank-nullity gives

   E(W):=E∩Hom(U,W)=ker(τ|_(W⊗U*)),
   dim E(W)=2r−s.                                      (1)

For W=JU, every operator in J belongs to E(W), so d≤2r−s. Since W⊂P⊗U, r≤2s. Consequently

   d≤2r−ceil(r/2)=floor(3r/2),
   r≥ceil(2d/3).                                       (2)

The upper bound r≤2d is the source-dimension bound. More precisely, every actual image has

   ceil(r/2)≤s≤min(5,2r−d).                            (3)

The minimal support of J itself in V⊗sl(U) equals P(W): an operator lands in P⊗U if and only if all its V-coefficients are in P. Thus s is intrinsic to the operator span and can be tested without choosing a larger image space.

## 2. Every intermediate rank occurs

Fix independent vectors v_1,…,v_5 in V. In a basis e_1,e_2 of U use H=diag(1,−1), E_+=(e_2↦e_1,e_1↦0), and E_-=(e_1↦e_2,e_2↦0).

For d≤r≤2d, take independent generators v_i⊗A_i, 1≤i≤d, with exactly r−d choices A_i=H and the remaining choices A_i=E_+. Their evaluation images lie in disjoint V-slots and have dimensions two or one, hence total rank r.

The only allowed cases with r<d are (d,r)=(3,2),(4,3),(5,4). They are realized respectively by

   v_1⊗sl(U),
   (v_1⊗sl(U)) ⊕ C(v_2⊗E_+),
   (v_1⊗sl(U)) ⊕ C(v_2⊗E_+) ⊕ C(v_3⊗E_+).

This proves both sharp bounds and absence of gaps. All witnesses lie in the abstract operator space.

## 3. Rectangular transversality for every effective span

The proof in the five-plane packet extends without a square-matrix assumption; here are all details needed for the extension. Put T=V⊗U, R=ker β_J, Q=coker β_J, and p:T→Q. Then dim R=2d−r and dim Q=10−r. The normal derivative is

   ν:Hom(J,E/J)→Hom(R,Q),
   ν(h)(Σ_j a_j⊗u_j)=p(Σ_j δa_j(u_j)),                 (4)

where a_1,…,a_d is a basis of J and δa_j lifts h(a_j). The expression is independent of the lifts.

Suppose q:Q→R annihilates the image of ν under the perfect trace pairing. Regard q as a map into J⊗U and write its components q_j:Q→U. Independent variations δa_j∈E imply that q_j p:T→U annihilates E under the trace pairing between Hom(U,T) and Hom(T,U). The annihilator of V⊗sl(U) is exactly V*⊗id_U, hence

   q_j p=ℓ_j⊗id_U,  ℓ_j∈V*.

Because q lands in R, β_J q=0. Precomposing with p gives

   0=Σ_j a_j∘(ℓ_j⊗id_U)=Σ_j ℓ_j⊗a_j

under Hom(T,T)=V*⊗Hom(U,T). The actual operators a_j are linearly independent. Thus every ℓ_j is zero, and surjectivity of p gives every q_j=0. Therefore q=0, and ν is surjective.

Near J, choose an invertible r-by-r block A of the universal 10-by-2d matrix. Its Schur complement F is a (10−r)-by-(2d−r) matrix with F(J)=0 and differential ν. By the holomorphic submersion theorem its entries are part of a local coordinate system, with D(d,r) additional coordinates. Invertible row and column operations reduce β to diag(I_r,F). The ideal of (t+1)-minors, for r≤t<2d, then equals the ideal of (t−r+1)-minors of F. This follows by adjoining the full identity block for one inclusion, and expanding larger minors for the other. Thus the claimed local models are scheme-theoretic in analytic coordinates. In particular S_(d,r) is smooth, of pure dimension D(d,r), including the maximal-rank case when the normal matrix has zero columns.

## 4. Support incidences and global irreducibility

Fix r and s satisfying (3). Choose P∈Gr(s,V), then W∈Gr(r,P⊗U) of full support P. The full-support condition is open: it is the rank-s condition on W⊗U*→P. The parameter space is consequently either empty or a smooth irreducible open subset of a relative Grassmannian, of dimension

   s(5−s)+r(2s−r).

On it the trace kernels E(W) form a vector bundle of rank 2r−s by (1). Choose J∈Gr(d,E(W)), and impose the open condition JU=W. Call the resulting incidence I_(d,r,s). When nonempty it is smooth irreducible of dimension

   I(d,r,s)=s(5−s)+r(2s−r)+d(2r−s−d)
           =D(d,r)+(5−s)(s+d−2r).                     (5)

Its map to G_d identifies it with the exact-rank-r, exact-support-s stratum: W=im β_J and P=P(W) are unique and vary regularly on these constant-rank loci. The latter statement follows from the image subbundles of β and of the contraction map W⊗U*→V.

By (3), the correction term in (5) is nonpositive. Equality occurs at precisely one allowed value,

   s_*=min(5,2r−d).                                   (6)

The nonempty S_(d,r) is smooth of pure dimension D(d,r) by Section 3, and is the finite union of these support strata. Therefore some support stratum must have dimension D(d,r); (5) forces it to be the s_* stratum. Every other support stratum has strictly smaller dimension. Taking closures within S_(d,r), the single irreducible s_* stratum has closure equal to all S_(d,r): otherwise another component of the smooth pure-dimensional variety would have to lie in a finite union of lower-dimensional closed subsets. Thus S_(d,r) is irreducible and its maximal-support stratum is dense. It is also open, since support dimension is a matrix-rank condition.

For completeness, the passage to the closed rank-at-most-r locus does not silently discard extra components at lower ranks. On a smooth affine chart X⊂G_d, intersect the graph of the universal matrix with X times the generic rank-at-most-r determinantal variety. The latter has codimension (2d−r)(10−r). The intersection dimension inequality in a smooth ambient space gives every irreducible component of R_(d,r) dimension at least D(d,r). One can prove that inequality by expressing the intersection using the diagonal of the smooth ambient space and applying the principal ideal theorem to its regular sequence of defining equations. Meanwhile R_(d,r) is the union of finitely many S_(d,t), t≤r. For allowed consecutive ranks,

   D(d,t+1)−D(d,t)=2d+9−2t>0.

Thus all lower-rank strata have strictly smaller dimension than D(d,r). No component can be supported entirely in their union. The closure of the irreducible S_(d,r) is therefore all R_(d,r), proving irreducibility and dimension. This argument does not rely on a generic-matrix assumption for the original family; its transversality was proved directly.

### Singular loci of the proper rank loci

For each feasible r<2d, the singular locus of R_(d,r) is exactly R_(d,r−1), with the latter empty below the minimum feasible rank. At an exact-rank-r point the local residual bound is zero, giving a smooth coordinate subspace. At a point of rank t<r, the local residual bound is k=r−t with 0<k<min(10−t,2d−t). The residual determinantal variety has positive codimension, but all its defining (k+1)-minors have zero linear term at the zero matrix. It is therefore singular there. This also shows that every minimum-rank locus is smooth. The exception r=2d is the whole smooth Grassmannian and is not covered by the singular-locus formula.

## 5. Complete minimum-rank equality classifications

The descriptions here are exhaustive and have converses. The support P and evaluation image W are unique, so these are intrinsic parameterizations, not merely selected normal-form examples.

### d=1, r=1

Here s=1 and W=P⊗L with lines P⊂V and L⊂U. Equation (1) gives dim E(W)=1, hence J=E(W)=P⊗n_L, where n_L is the line of endomorphisms with image in L and killing L. Equivalently J=C(v⊗N) with N nonzero nilpotent. The parameter space has dimension 4+1=5, agreeing with D(1,1).

### d=2, r=2

There are exactly two support possibilities.

- s=1: W=P⊗U, and J is any two-plane in P⊗sl(U). Every such J has rank two, since rank one would contradict (2). This support stratum has dimension 4+dim Gr(2,3)=6.
- s=2: choose P∈Gr(2,V) and any W∈Gr(2,P⊗U) of full support. Then J=E(W), which has dimension two. Its rank is exactly two by (2) and containment in W. This stratum has dimension 6+4=10 and is dense in S_(2,2).

Thus evaluation rank two for an effective pencil need not mean that all operators have one common V-factor.

There is a finite orbit refinement under changes of V coordinates and conjugation on U. In support one, the orthogonal line to J inside sl(U), for the nondegenerate trace pairing, is either nilpotent or semisimple, giving two types. In support two, the projective line P(W) meets the determinant quadric in P(P⊗U) in the whole line, two distinct points, or one double point. Full P-support excludes the ruling with fixed P-factor. The remaining three normal forms for W are

   P⊗Ce_1;
   span(p_1⊗e_1,p_2⊗e_2);
   span(p_1⊗e_1,p_1⊗e_2+p_2⊗e_1).

Indeed a nonzero binary quadratic over C has either two distinct roots or a double root; an identically zero determinant gives a line on the smooth rank-one quadric, hence one of its two rulings. Elementary changes of the two factor bases give the displayed secant and tangent forms. Thus the minimum-rank effective pencil has exactly five abstract orbit types. These coordinate equivalences do not posit additional geometric symmetries of a separate geometric construction.


### d=3, r=2

Inequality (3) forces s=1. Then E(W)=P⊗sl(U) has dimension three, and

   rank β_J=2  iff  J=P⊗sl(U) for a line P⊂V.

The equality locus is Gr(1,V)=P^4, dimension D(3,2)=4. This gives a particularly rigid root-cause criterion for a three-dimensional effective span.

### d=4, r=3

Now (3) forces s=2, and dim E(W)=4. Choose any support plane P⊂V and any hyperplane W⊂P⊗U; its support is automatically P, because a support line would allow dimension at most two. Then

   J=E(W)

has dimension four and evaluation image exactly W by (2). Conversely every minimum-rank four-plane is obtained in this way. Its parameter space is a P^3-bundle over Gr(2,5), dimension 9=D(4,3).

There are two intrinsic compression types. The defining covector λ∈P*⊗U* of W has tensor rank one or two. Rank one means W contains a full factor p⊗U: in suitable bases J=(Cp⊗sl(U))⊕(Cq⊗n_L). Rank two means W contains no full factor p⊗U. Indeed a full factor occurs exactly when λ(p⊗−)=0, and a rank-two map P→U* is injective. These exhaust the two orbits of hyperplanes under GL(P)×GL(U); the GL(U) action on operators is conjugation. The rank-one locus has fiber dimension two and total dimension eight, while rank-two compressions form the open dense dimension-nine stratum.

### d=5, r=4

There are exactly two support possibilities.

- s=2: W=P⊗U, and J is an arbitrary hyperplane in P⊗sl(U), a six-dimensional space. Its evaluation rank is four by (2). These form a P^5-bundle over Gr(2,5), of dimension eleven.
- s=3: choose any three-plane P⊂V and any W∈Gr(4,P⊗U) of full support P. Then J=E(W), of dimension five, and its rank is exactly four by (2). This stratum is an open subset of a Gr(4,6)-bundle over Gr(3,5), of dimension fourteen, and is dense in S_(5,4).

The second case has an equivalent dual criterion that can be used without a normal form. Put C=W^⊥⊂P*⊗U*, a two-plane. Full support means that C contains no full factor ℓ⊗U* for nonzero ℓ∈P*. Then

   J={a∈P⊗sl(U): λ∘a=0 for every λ∈C}.

Thus support-two minimum rank is a hyperplane inside a full two-slot operator space, whereas support-three minimum rank is the complete solution space of a two-dimensional output compression. Neither should be conflated with mere effective dependence of the five original operators.

## 6. Exact diagnosis for an original ordered five-tuple

Let A=C^5 index an ordered five-tuple of abstract operators and let α:A→E be their linear map. Put J=im α, d=rank α. The original ten-column operator factors as

   B:A⊗U → J⊗U → V⊗U,

with the first map α⊗id_U onto and the second β_J. Hence rank B=r and there is a canonical exact sequence

   0→ker α⊗U→ker B→ker β_J→0.                        (7)

In particular

   dim ker B=10−r=2(5−d)+(2d−r).                     (8)

The first summand counts relations among operators; the second counts genuine evaluation syzygies remaining after all those dependencies are removed. Equation (8) is a dimension decomposition; no canonical splitting of (7) is asserted. The cokernel also has dimension 10−r. No interpretation in a geometric graded module is asserted.

For d=1,2,3,4,5, the possible kernel and cokernel dimensions are respectively 8–9, 6–8, 4–8, 2–7, 0–6, with every integer in the stated interval possible universally. If d=0 all operators vanish, B=0 and both kernel and cokernel have dimension ten.

This supplies an exact sequence of questions before any actual rank-instance evaluation: determine d; determine the intrinsic support s; use r≥max(ceil(2d/3),ceil((d+s)/2)); then distinguish evaluation saturation J=E(W) from a proper subspace of that compression space. The equality classifications above give exact structural diagnoses when the minimum rank occurs. No assertion is made here about which case the actual conductor construction occupies.

## Boundary

All conclusions concern abstract operator spans in E. Applying them to effective classes in a geometric construction requires a separate identification. No such identification, effective-span dimension, or actual conductor rank is asserted here.
