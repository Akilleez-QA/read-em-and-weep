# Incidence derivations

This file preserves three successive derivations. Part A is the corank-two local model; Part B proves smoothness of the full two-plane incidence directly; Part C proves the simultaneous all-corank resolutions using PROOF.md. Statements of limitations in the earlier parts describe what that component alone proves and do not negate the later extension.

## Part A

# Corank-two geometry of the universal quartic cofactor divisor

## Result and scope

Work over C. Let dim V=5, dim U=2, E=V⊗sl(U), G=Gr(5,E), and let b:T⊗U→(V⊗U)⊗O_G be evaluation. Write D={det b=0} and S={rank b≤8}, with S given its reduced structure unless explicitly stated otherwise.

Then S, the reduced singular locus of D, is irreducible of dimension 46, hence codimension four in G and codimension three in D. Its corank-exactly-two locus is nonempty, dense, and smooth. At EVERY corank-exactly-two point, the analytic germ of D is the product of the three-dimensional ordinary quadratic node {x11 x22−x12 x21=0} with a smooth 46-dimensional germ. In particular this describes the generic singularity of D.

The two-plane cokernel incidence has a 46-dimensional irreducible general stratum and a 39-dimensional special stratum. The exceptional base planes are exactly W=ℓ⊗U* for [ℓ]∈P(V*). Even these special cokernel planes do not obstruct transversality at corank exactly two.

All assertions concern the universal operator family. They do not evaluate, or establish a rank for, any actual conductor/HM/cofactor instance.

## 1. Audited starting point

The proof and audit in ../universal-cofactor-normal-form define the abstract operator space E=V⊗sl(U) and its evaluation operator b, and establish the following geometry: dim G=50; D is a reduced irreducible normal rational divisor of class O_G(2); its smooth points are exactly the corank-one operators; its resolution is the cokernel-line incidence. We use those results, not any evaluation of the actual conductor family.

For J∈G put B_J:J⊗U→V⊗U, R_J=ker B_J, and C_J=coker B_J. Its dual cokernel C_J* is naturally a subspace of (V⊗U)*.

## 2. Rank of evaluation against a two-plane

Put H=(V⊗U)* and take W∈Gr(2,H). Define

    f_W:E→Hom(U,W*),     f_W(a)(u)(w)=w(a(u)),
    K_W=ker f_W.

Identify Hom(U,V⊗U)* with V*⊗End(U) via the trace pairing. The annihilator of V⊗sl(U) is V*⊗C·Id_U. The dual map f_W* is restriction of this pairing to W⊗U. Consequently

    ker f_W* = (W⊗U) ∩ (V*⊗C·Id_U).                 (1)

If a nonzero ℓ⊗Id_U lies in W⊗U, contracting its U factor against all of U* shows ℓ⊗U*⊂W. Both have dimension two, so W=ℓ⊗U*. Conversely such a W contains the full tensor ℓ⊗Id_U. In this case the intersection in (1) is exactly its one-dimensional span: another independent ℓ' would force the four-dimensional (span(ℓ,ℓ'))⊗U* into W.

Thus

    rank f_W = 4 and dim K_W = 11, if W is nonspecial;
    rank f_W = 3 and dim K_W = 12, if W=ℓ⊗U*.

The special planes form a closed copy of P(V*)=P^4 inside Gr(2,H), which has dimension 16. Closedness follows, for example, from the rank-drop condition in (1), and the inverse to [ℓ]↦ℓ⊗U* is regular onto its image.

## 3. Incidence and exact dimension

Consider the projective incidence

    I₂={(J,W)∈G×Gr(2,H): J⊂K_W}.

Its image under p:I₂→G is exactly S: a two-plane of annihilators exists precisely when corank B_J≥2. The fiber is Gr(2,C_J*).

Over the nonspecial open base B°, the kernel K is a rank-eleven vector bundle. Therefore I₂°=Gr_B°(5,K) is smooth and irreducible, of dimension

    16+5(11−5)=46.                                  (2)

Over the special base, K is a rank-twelve vector bundle, so the closed special incidence I₂^sp is smooth irreducible of dimension

    4+5(12−5)=39.                                   (3)

In particular dim S≤46. There is a corank-exactly-two point in the image of I₂°: choose a basis v1,…,v5 of V and the usual matrices H0=diag(1,−1), E0=[0 1;0 0] in sl(U). Take

    J=span(v1⊗H0,v2⊗H0,v3⊗H0,v4⊗E0,v5⊗E0).

The direct sum evaluation has rank 2+2+2+1+1=8. Its dual cokernel is span(v4*⊗e2*,v5*⊗e2*), which is nonspecial. This is an abstract universal example, not a selected actual conductor evaluation. Since corank exactly two is open within S, a nonempty open subset of I₂° has singleton fibers. Hence its image closure S₀ is irreducible of dimension 46.

## 4. Irreducibility: ruling out lower-dimensional extra components

We record the dimension argument rather than assume that special incidence points deform to nonspecial ones.

On an affine chart of G trivializing the rank-ten domain bundle, b is a matrix-valued regular function B:X→Mat10. The rank≤8 matrix variety Y⊂Mat10 is irreducible of codimension (10−8)^2=4, thus dimension 96. In the smooth 150-dimensional variety X×Mat10, its product X×Y has dimension 146 and the graph Γ_B has dimension 50. Every irreducible component of their intersection therefore has dimension at least

    146+50−150=46.

This is the intersection dimension inequality in a smooth ambient variety (equivalently, the diagonal has codimension 150 and is locally cut out by 150 equations). The intersection identifies with S∩X. Thus every irreducible component of S has dimension at least 46.

The special incidence is projective, so its image S_sp=p(I₂^sp) is closed and has dimension at most 39. The closure of the image of I₂° is S₀. Since I₂=I₂°∪I₂^sp and p(I₂)=S,

    S=S₀∪S_sp.

An irreducible component of S not contained in S₀ would be contained in S_sp, contradicting its dimension lower bound. Therefore S=S₀, proving irreducibility and dim S=46. This argument establishes the reduced image's irreducibility; it does not assert that the entire incidence I₂ is irreducible or make an unnecessary scheme-theoretic reducedness claim for the determinantal ideal.

## 5. Normal-map transversality at every corank-two point

Fix J with corank B_J=2; write R=R_J, C=C_J, W=C*. Both R and C have dimension two. A tangent vector h∈T_JG=Hom(J,E/J) induces the normal map

    ν:Hom(J,E/J)→Hom(R,C),
    ν(h)(Σ a_j⊗u_j)=Σ [h(a_j)(u_j)] in C.          (4)

The expression does not depend on lifts: elements of J map into im B_J. Let F:E/J→Hom(U,C) be the map induced by evaluation and projection to C. It is the descended f_W.

If W is nonspecial, F is onto by Section 2. Thus Hom(J,E/J) maps onto Hom(J,Hom(U,C))=Hom(J⊗U,C). Restriction to the subspace R is onto Hom(R,C). Therefore ν is onto.

Now suppose W=ℓ⊗U*. Projection V⊗U→C can be identified with ℓ⊗Id:V⊗U→U, identifying C with U. Under this identification the image of F is precisely sl(U). Surjectivity onto sl(U) follows by choosing v with ℓ(v)=1. Since J⊂K_W, this map indeed descends to E/J.

Suppose a functional on Hom(R,C) annihilates im ν. Under the trace pairing it is a map q:C→R. Composing with R↪J⊗U and choosing a basis a1,…,a5 of J, write

    q(c)=Σ a_j⊗Q_j(c),        Q_j∈Hom(C,U).

The variations h(a_j) are independent, and each F(h(a_j)) ranges over all sl(U). The annihilator condition is therefore

    tr(A Q_j)=0 for every A∈sl(U), for every j.

With C=U, the trace-orthogonal complement of sl(U) is C·Id. Hence Q_j=t_j Id and q(c)=a⊗c, where a=Σ t_j a_j∈J. But q(C)⊂R forces B_J(a⊗c)=a(c)=0 for every c∈U. The space E embeds faithfully in Hom(U,V⊗U), so a=0 and q=0. Thus the dual of ν is injective, proving that ν is onto in the special case too.

## 6. Local analytic model

Near the fixed corank-two point, choose an invertible eight-by-eight minor. Holomorphic invertible row and column operations reduce b to a block diagonal matrix with an invertible eight-by-eight block and a two-by-two Schur complement A, with A(J)=0. The derivative of A at J identifies with ν (up to invertible source and target coordinate changes). Since ν is onto, the four entries of A are part of a holomorphic coordinate system on the 50-dimensional smooth G.

The determinant differs from det A by an invertible function. Completing the four entries to coordinates z1,…,z46 gives

    (D,J) ≅ ({x11 x22−x12 x21=0},0) × (C^46,0).

The quadratic form x11 x22−x12 x21 is nondegenerate on its four-dimensional variable space. Thus its hypersurface is the three-dimensional ordinary quadratic node. In these coordinates S is exactly {x11=x12=x21=x22=0}; the reduced singular locus is smooth of dimension 46 there. In fact the local determinantal scheme agrees with this smooth reduced locus, and the local Jacobian singular scheme of D also agrees with it.

Corank exactly two is nonempty by Section 3 and open within the irreducible S, hence dense. This proves the asserted generic singularity and the stronger local statement at every corank-two point. The corank-at-least-three locus is a proper closed subset of S, so has dimension at most 45; no sharper bound is needed or claimed here.

## 7. Scope of this component

The corank-two derivation above proves the ordinary-node model and rules out additional components from the special cokernel-plane locus. Global scheme structure and higher coranks are addressed in PROOF.md and Part C below, not inferred from the incidence dimension alone.


## Part B

# Addendum: the two-plane incidence resolves the singular locus

This part uses the notation and results of Part A above. Its conclusion is independent of any actual conductor evaluation.

## Statement

The full incidence

    I₂={(J,W)∈Gr(5,E)×Gr(2,(V⊗U)*): f_W(J)=0}

is smooth and irreducible of dimension 46. Its proper projection onto the reduced corank-at-least-two locus S is a resolution, is an isomorphism over corank exactly two, and has fiber Gr(2,C_J*) over J, where C_J=coker B_J. No Gorenstein, canonical-divisor, or crepancy assertion for S is made here.

## 1. The twenty equations

Let Q=Gr(5,E)×Gr(2,(V⊗U)*), a smooth variety of dimension 50+16=66. Use T for the tautological rank-five bundle from the first factor and W for the tautological rank-two bundle from the second. Evaluation defines a section

    s of Hom(T⊗U,W*),

a rank-twenty vector bundle, whose scheme-theoretic zero locus is I₂. We show that its differential is onto at every zero. This proves that I₂ is smooth of dimension 46, including along the special-base stratum.

At a zero (J,W), variation of J is an arbitrary h:J→E/J. Its contribution is f_W∘h, since f_W vanishes on J. When W is nonspecial, E/J→Hom(U,W*) is onto by Part A Section 2. The J variations alone therefore span all twenty components Hom(J,Hom(U,W*)).

## 2. Differential over a special plane

Now W=ℓ⊗U*. Choose V=V₀⊕Cv₀ with V₀=ker ℓ and ℓ(v₀)=1. Then

    K_W=V₀⊗sl(U),       W*=U,

and f_W(a) is contraction of a by ℓ, with image sl(U). The J variations therefore span exactly Hom(J,sl(U)), of dimension fifteen, inside Hom(J,End(U)). The quotient is J*, using trace on each End(U) coefficient. It remains to show that W variations span this five-dimensional quotient.

The tangent space to Gr(2,(V⊗U)*) at W is

    Hom(W,(V⊗U)*/W) = Hom(U*,V₀*⊗U*).

Encode a tangent vector by a linear map T:V₀→End(U) as follows: for w∈U*, its variation δw is the covector on V₀⊗U given by

    (δw)(v⊗u)=w(T(v)u).

For a=Σ_i v_i⊗A_i∈K_W, with v_i∈V₀ and A_i∈sl(U), differentiating evaluation in the W direction yields, under W*=U,

    δf_W(a)=Σ_i T(v_i)A_i.

Consequently its image in the trace quotient is the functional on J

    a ↦ Σ_i tr(T(v_i)A_i).                         (1)

The trace pairing End(U)×sl(U)→C is onto the dual of sl(U), with kernel C·Id in its End(U) factor. Thus the space of all T induces all of K_W*=(V₀⊗sl(U))* through (1); its kernel is V₀*⊗C·Id, the tangent space to the special P(V*) locus. Restricting arbitrary functionals on K_W to its subspace J is onto J*. Hence W variations supply all five missing directions. The full section differential has rank 15+5=20.

This proves global smoothness of I₂. It also explains why the rank jump of f_W does not create a singularity of the total incidence: motion of W compensates for the lost J-variation directions.

## 3. Irreducibility and resolution

The nonspecial-base open I₂° is irreducible of dimension 46. The complement I₂^sp has dimension 39 by Part A Section 3. Every irreducible component of the now-proven smooth I₂ has dimension 46, so none can lie in its 39-dimensional complement. Hence the dense irreducible open I₂° has closure all of I₂, proving irreducibility.

The projection p:I₂→G is projective and its image is S. It factors through reduced S since I₂ is reduced. Over a point J of corank c≥2, the defining equations in W say exactly that W is a two-plane in C_J*, so the scheme-theoretic fiber is Gr(2,C_J*), of dimension 2(c−2).

Over the nonempty dense corank-exactly-two open of S, the rank-eight image of B_J is a vector subbundle locally. Its annihilator is a rank-two subbundle, supplying the regular inverse J↦(J,C_J*). Thus p is an isomorphism there. It is consequently a proper birational morphism from a smooth variety to S, and hence a resolution.

No assertion here requires S to be normal or Gorenstein, and no canonical-class inference is made. Higher-corank dimension estimates, if independently established, can separately decide whether this resolution is small.


## Part C

# All-corank incidence resolutions and their canonical bundles

## Scope and dependencies

This part extends Parts A and B above. Work over C with dim V=5, dim U=2, E=V⊗sl(U), G=Gr(5,E), and evaluation b:T⊗U→(V⊗U)⊗O_G. Let D_c be the corank-at-least-c locus and S_c=D_c∖D_(c+1).

We import from PROOF.md its all-corank transversality theorem and exact dimension/irreducibility results: for 1≤c≤6, D_c is irreducible of dimension 50−c², S_c is nonempty smooth dense, and D_7 is empty. At J∈S_d the entire family of determinantal loci is analytically the corresponding rank loci in Mat_d times a smooth factor of dimension 50−d². These are substantive dependencies, subject to that proof's independent audit. The normal/Cohen–Macaulay determinantal-ring input needed for the target-canonical conclusions is verified against the primary source in Section 5. All D_c are normal Cohen–Macaulay Gorenstein, and every π_c is small and crepant with canonical line O_(D_c)(2c−15).

## 1. The simultaneous family of incidence resolutions

Put H=(V⊗U)* and define, for 1≤c≤6,

    Z_c={(J,W)∈G×Gr(c,H): W annihilates b_J(J⊗U)}.

Use its scheme structure as the zero locus of the evaluation section of

    F_c=Hom(T⊗U,W*)

over G×Gr(c,H), where W denotes the rank-c tautological subbundle on the second factor. The rank of F_c is 10c. Projection π_c:Z_c→G is projective and has image D_c. At a point J of corank d≥c, its scheme-theoretic fiber is

    Gr(c,C_J*),        C_J=coker b_J,

of dimension c(d−c).

## 2. Smoothness everywhere, not just over S_c

Fix J∈S_d and any W∈Gr(c,C_J*). On a neighborhood of J, invertible row and column operations reduce b to an invertible (10−d)-block and its d-by-d Schur complement A. The all-corank transversality theorem says A is a submersion at J, with A(J)=0. Consequently analytic coordinates identify this neighborhood with a neighborhood of (0,0) in Mat_d×C^(50−d²).

Under the same output basis changes, every annihilating W has zero component against the invertible block, and the incidence condition becomes

    W∈Gr(c,(C^d)*),        W·A=0.

For the full matrix family this incidence is the total space, over Gr(c,(C^d)*), of the vector bundle

    Hom(C^d,ann(W)),

whose rank is d(d−c). Its base has dimension c(d−c), so the total space is smooth of dimension d²−c². Taking the product with C^(50−d²) proves that Z_c is smooth of dimension 50−c² at every point over S_d. Since these strata exhaust Z_c, this proves global smoothness. The calculation applies to the actual incidence scheme and thus excludes nonreduced structure.

There is also an algebraic étale version, useful for scheme properties. On the invertible-minor open, the entries of A are regular functions. Their differentials are independent at J by transversality. Choose 50−d² additional regular functions whose differentials complete a basis of the cotangent space of smooth G at J. The combined map

    (A,z):G_open→Mat_d×A^(50−d²)

is étale on a neighborhood of J by the Jacobian criterion. Schur reduction identifies every relevant ideal of minors with the exact pullback of the corresponding generic determinantal ideal. The incidence itself is the same étale pullback of the standard matrix incidence, using the invertible output basis changes above. Thus the local assertions admit algebraic étale models, not just complex-analytic or completed-local ones.

In particular the section of F_c is regular: its zero locus is smooth of codimension 10c in the smooth ambient variety of dimension 50+c(10−c).

## 3. Irreducibility, resolution, and smallness

Over S_d the kernels C_J* form a rank-d vector bundle, and π_c^−1(S_d) is its relative Grassmannian of c-planes. Therefore

    dim π_c^−1(S_d)=50−d²+c(d−c).

For d=c the fiber is a point and π_c is an isomorphism over S_c: the inverse sends J to its full dual cokernel, which varies regularly on this constant-rank stratum. For d>c the dimension difference from Z_c is

    (50−c²)−[50−d²+c(d−c)]=d(d−c)>0.              (1)

Every component of the smooth Z_c has dimension 50−c², so no component is contained in the finite union of these smaller strata. The open π_c^−1(S_c)≅S_c is irreducible; hence Z_c is irreducible. Thus π_c:Z_c→D_c is a projective resolution.

Equation (1) is at least c+1≥2 when d>c. Hence there are no exceptional divisors. The stronger dimension-theoretic smallness inequality also holds on every nontrivial-fiber stratum:

    codim_(D_c)(S_d)=d²−c² > 2c(d−c),

because the difference is (d−c)²>0. Finite unions of these strata give the same strict inequality for each locus where fiber dimension is at least any fixed positive integer. Consequently π_c is a small resolution in both the no-exceptional-divisors sense and the strict fiber-dimension sense.

For c=6 there are no higher strata at all: Z_6→D_6 is an isomorphism and D_6 is smooth of dimension 14.

## 4. Canonical bundle of the smooth resolution

Let p and q be the projections from G×Gr(c,H). Determinants below are considered up to fixed one-dimensional vector-space factors, which do not affect their line-bundle classes or the resulting isomorphisms. The canonical line bundles of the two Grassmannians give

    ω_(G×Gr(c,H))=(det T)^15⊗(det W)^10.

For F_c=(T⊗U)*⊗W*, of rank 10c,

    det F_c=(det T*)^(2c)⊗(det W*)^10.

Adjunction for the regular section established in Section 2 therefore yields

    ω_(Z_c)=[(det T)^(15−2c)]|_(Z_c)
           =π_c* O_(D_c)(2c−15).                  (2)

Here O_(D_c)(1) is the restriction of the Plücker line from G. The cancellation of the Gr(c,H) determinant factors is exact. In particular c=1 recovers O(−13), c=2 gives O(−11), and c=6 gives O(−3).

Formula (2) is unconditional relative to the imported all-corank local-model/dimension theorem. It does not by itself assert a canonical or Gorenstein property of the possibly singular target; that step requires the normal and Cohen–Macaulay input below.

## 5. Target canonical sheaf and crepancy: verified standard input

The standard determinantal-ring theorem required here is:

    The coordinate ring of a generic m-by-n matrix of rank at most r,
    over C, is an integral normal Cohen–Macaulay ring.

This input is verified in the author-hosted [Bruns–Vetter, Determinantal Rings](https://www.home.uni-osnabrueck.de/wbruns/brunsw/detrings.pdf): Corollary 5.17 (printed page 60, PDF page 68) proves Cohen–Macaulayness; Theorem 6.3 (printed page 65, PDF page 73) proves normality and integrality. Their general notation includes the ordinary rank-bounded matrix rings, as stated explicitly on printed page 70. Corollary 8.9 (printed page 98, PDF page 106) additionally confirms Gorensteinness for square matrices, independently checking the conclusion below. The zero-rank case is a point and needs no theorem. These statements were opened and read, not inferred from search summaries.

By that theorem and the algebraic étale models proved in Section 2, every D_c, with its determinantal scheme structure, is reduced, normal, and Cohen–Macaulay: these properties hold for the generic model times its smooth factor and transfer under étale morphisms. In particular the reduced support used in the incidence arguments agrees with the actual scheme of the appropriate minors.

Because D_c is normal Cohen–Macaulay it has a rank-one reflexive dualizing sheaf ω_(D_c). On its dense smooth open S_c, π_c is an isomorphism, so (2) identifies

    ω_(D_c)|_(S_c)≅O_(D_c)(2c−15)|_(S_c).

The complement has codimension at least (c+1)²−c²=2c+1 whenever nonempty. Both sheaves are reflexive on the normal D_c, so this identification extends uniquely to

    ω_(D_c)≅O_(D_c)(2c−15).                        (3)

Thus ω_(D_c) is invertible and D_c is Gorenstein. Pulling (3) back and comparing with (2) proves crepancy. More intrinsically, the canonical identification over S_c extends across its inverse-image complement, of codimension at least two in the smooth Z_c, so the equality is crepancy of canonical divisors and not merely equality of abstract line-bundle classes.

No terminal-singularity or rational-singularity extension is asserted here. Those would require separate use and checking of the relevant discrepancy or vanishing theorems, beyond the canonical-bundle calculation.

## 6. Boundary

These are universal operator-family statements; no application-specific identification or rank evaluation is used.
