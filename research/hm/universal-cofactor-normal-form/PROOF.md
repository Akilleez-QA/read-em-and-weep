# Abstract trace-free evaluation and its universal discriminant

## Result and precise scope

Work over C. Let V and U be abstract vector spaces of dimensions five and two, respectively. Define E₀=V⊗sl(U) as the indicated subspace of Hom(U,V⊗U); this is a definition of the model, not an identification of a geometric module. For J∈G=Gr(5,E₀), let β_J:J⊗U→V⊗U be evaluation.

In bases, an ordered five-tuple of operators has matrix

    B = [ P  Q ]
        [ R −P ],                P,Q,R arbitrary 5-by-5 matrices.

Its failure divisor D is nonempty, irreducible, reduced, normal and rational, of class O_G(2). Its smooth points are exactly the corank-one operators. The cokernel-line incidence is a smooth resolution, a Gr(5,13)-bundle over P((V⊗U)*)=P⁹, with fiber P^(c−1) over corank c. Existence of a rank-one output annihilator defines an irreducible closed codimension-five sublocus of G.

No identification with an HM module, scalar-annihilator quotient, or conductor family is assumed or proved. In particular this theorem does not assert the dimension or independence of any geometric family's effective classes.

## 1. Abstract operator space

The trace map End(U)→C has kernel sl(U), of dimension three. Thus dim E₀=15, and E₀ is an actual subspace of Hom(U,V⊗U). No representation-theoretic input or identification U≅U* is needed.

## 2. Exact evaluation formula

For a basis e₁,e₂ of U, every a∈E₀ is uniquely

    a = p⊗H + q⊗E + r⊗F,       p,q,r∈V,
    H=[1 0;0 −1], E=[0 1;0 0], F=[0 0;1 0].

Its evaluation sends x e₁+y e₂ to

    (xp+yq)⊗e₁ + (xr−yp)⊗e₂.                    (1)

In particular the trace-zero condition is on each two-by-two block indexed by a V-coordinate and an input operator; it is not merely a single trace-zero condition on a ten-by-ten square matrix.

## 3. Exact evaluation criteria for arbitrary subspaces

For any subspace J⊂E₀ of dimension d, put

    β_J:J⊗U → V⊗U,    a⊗u↦a(u).

Its cokernel has dimension 10−dim(JU). An ordered tuple of five abstract operators gives an invertible ten-column evaluation map exactly when its span has dimension five and β_J is invertible. If its span has dimension below five, the rank is at most 2d<10.

For a basis a_j=(p_j,q_j,r_j), j=1,…,d, set P=(p_j), Q=(q_j), R=(r_j) as 5-by-d column matrices. Equation (1) gives

    β_J(x,y)=(Px+Qy, Rx−Py).                       (2)

For d=5 this is the displayed block-traceless square matrix. A primal kernel is exactly a pair (x,y) satisfying both equations Px+Qy=0 and Rx−Py=0. A dual kernel is exactly a nonzero pair (s,t)∈V*⊕V* with

    sP+tR=0,       sQ−tP=0.                       (3)

There is also an intrinsic intersection test. For 0≠λ∈(V⊗U)* define

    f_λ:E₀→U*,       f_λ(a)=λ∘a,
    K_λ=ker f_λ.

Then

    β_J fails to be onto  iff  J⊂K_λ for some [λ]∈P⁹.   (4)

For every nonzero λ the map f_λ is onto. Indeed choose v∈V with the row functional λ_v(u)=λ(v⊗u) nonzero. The map sl(U)→U*, A↦λ_v A, is onto: in a basis with λ_v=(1,0), its output is the arbitrary row (a,b) of [a b;c −a]. Thus dim K_λ=13 uniformly. This constant-rank statement is stronger than an ambient relation-space dimension count and makes the following geometry exact.

## 4. The universal discriminant is an irreducible quadratic Plücker divisor

Let G=Gr(5,E₀), of dimension 50, with tautological rank-five bundle T. There is a universal map of rank-ten bundles

    b:T⊗U → (V⊗U)⊗O_G.

Its determinant is a section of (det T*)² tensored with a fixed one-dimensional vector space, since det(T⊗U)=(det T)²⊗(det U)^5. Thus its zero scheme D belongs to |O_G(2)|.

This determinant is not identically zero. For any abstract basis v₁,…,v₅ of V, the five-plane spanned by v_i⊗H has β equal to diag(I₅,−I₅), hence invertible. This is a universal linear-algebra example in E₀, not an evaluation of a geometric family. It lies in E₀ by definition.

The zero locus is nonempty and has a corank-one point: take the five-plane spanned by v_i⊗H for i=1,…,4 and v₅⊗E. Its action is the direct sum of four invertible two-dimensional blocks and one rank-one block, so has rank nine. Again this is an abstract test of the universal operator family only.

Now form

    Z={ (J,[λ])∈G×P⁹ : J⊂K_λ }.

The maps f_λ assemble into a surjective bundle map E₀⊗O_(P⁹)→U*⊗O_(P⁹)(1), with rank-thirteen kernel bundle K. Consequently Z=Gr_(P⁹)(5,K) is smooth and irreducible, of dimension

    9+5(13−5)=49.

Projection π:Z→G is proper and its image is exactly the support of D by (4). Over J its fiber is the projectivization of the annihilator of β_J(J⊗U), hence P^(c−1) if the corank is c≥1. The exhibited corank-one point has a single-point fiber. Thus the image is irreducible of dimension 49, and π is generically one-to-one. Over the corank-one locus the unique cokernel line varies regularly, so π is an isomorphism there, not just a set-theoretic bijection.

We next prove D is reduced, identify its smooth locus, and thereby justify calling π a resolution.

## 5. Smoothness is exactly corank one

At any J with corank one, choose nonzero k∈ker β_J and λ in its one-dimensional dual cokernel. Write k=Σ_j a_j⊗u_j in a basis of J; some u_i≠0. A tangent vector to G is a linear map h:J→E₀/J. The differential of the determinant, up to a nonzero factor, is

    h ↦ λ(Σ_j h(a_j)(u_j)).                         (5)

This expression is independent of the lifts of h(a_j), because λ annihilates J U. The surjectivity of f_λ:E₀→U* lets us choose a variation only of a_i for which λ(h(a_i)(u_i))≠0. Therefore (5) is nonzero, so D is smooth at every corank-one point.

If corank β_J≥2, every nine-by-nine minor vanishes, so the differential of the determinant vanishes even on the full space of ten-by-ten matrices, hence also along G. Such a point is singular on its determinant hypersurface.

The support of D is irreducible and its determinant has multiplicity one at a corank-one point. An effective Cartier divisor on the smooth integral G has no embedded associated components; it follows that D is reduced everywhere. Thus the asserted singular-locus criterion concerns the reduced divisor itself. The smooth irreducible Z, proper birational over D and an isomorphism over its smooth locus, is a resolution, with the exact fibers stated above.

### Normality and rationality

The inverse image of Sing(D) under π is a proper closed subset of the irreducible 49-dimensional Z: the corank-one locus is nonempty. Hence it has dimension at most 48. Every fiber over Sing(D) has dimension at least one, so dim Sing(D)≤47. Thus D is regular in codimension one. Being a Cartier hypersurface in smooth G, D is Cohen–Macaulay and in particular satisfies Serre’s S₂ condition. The regularity-in-codimension-one and S₂ criterion proves that D is normal.

The vector bundle K is trivial on a dense open subset of P⁹. Over that subset Z is a product with Gr(5,13), which has a dense affine cell. Thus Z is rational, and its birational image D is rational as well. These assertions do not assert rational singularities: that stronger singularity property is not established here.

## 6. Rank-one output explanations occupy a much smaller locus

Regard λ∈V*⊗U* as a map V→U*. Its nonzero tensor ranks are one and two. The rank-one projective locus is the closed Segre variety

    Σ=P(V*)×P(U*)⊂P⁹,      dim Σ=5.

Restricting the incidence bundle to Σ gives a smooth irreducible variety of dimension 5+40=45. Its proper image D_rank1⊂G is therefore closed and irreducible of dimension at most 45. The corank-one witness in Section 4 has unique cokernel line generated by v₅*⊗e₂*, which has tensor rank one. Thus this restricted projection has a zero-dimensional fiber, so its image has dimension exactly 45. Consequently D_rank1 has codimension exactly five in G and exactly four in D. In particular the generic corank-one failure has a rank-two cokernel covector; it cannot be explained by a decomposable output functional.

This locus has an exact nilpotent-line criterion. Write λ=ℓ⊗φ with ℓ∈V*, φ∈U* nonzero, and let

    ρ_ℓ:E₀→sl(U),       ρ_ℓ(v⊗A)=ℓ(v)A.

Then J⊂K_λ iff

    ρ_ℓ(J) ⊂ n_φ := {A∈sl(U): φA=0}.              (6)

Here n_φ is a one-dimensional nilpotent line: its endomorphisms have image in ker φ and kill ker φ. In a basis with φ=(1,0), it consists of [0 0;c 0]. Thus the special rank-one explanation requires that some V-direction project the entire operator five-plane into one nilpotent line. Formula (6) gives a concrete geometric obstruction beyond the original generic dimension criterion.

No converse is asserted between corank and tensor rank: a corank-one cokernel may be rank one or rank two, and larger cokernels can contain both types. The codimension bound concerns existence of at least one rank-one output annihilator.

## 7. Boundary of application

The quadratic determinant section is proper in this abstract operator model. An application to another construction requires a separately established map into E₀ and, for the square test, independence of its five operators. No assertion is made that any such family avoids D or the rank-one-annihilator sublocus. No geometric-module identification, conductor rank, or obstruction computation is part of this theorem.
