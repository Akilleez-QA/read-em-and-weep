# Formal local rigidity and nonsmoothability of the actual cubic images

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. All calculations below are universal symbolic algebra. No actual HM/source coefficients, matrices, point evaluations, numerical rank tests, scans, or computer algebra are used.

## 1. Inputs, scope, and theorem

The geometric input is Akilleez-QA/read-em-and-weep PR611, commit `12b28d33627cc0e8b283d142dc16439a51bb5e00`, `research/hm/cubic-branch-transversality/PROOF.md`, Sections 1 and 4 ([immutable source](https://github.com/Akilleez-QA/read-em-and-weep/blob/12b28d33627cc0e8b283d142dc16439a51bb5e00/research/hm/cubic-branch-transversality/PROOF.md)). The actual reduced cubic images V=V_51 and T=T_75 are smooth outside sixty points. Their completed local rings at these points are respectively A_4 and A_2, where

    A_d = C[[u_1,...,u_d,v_1,...,v_d]]/(u_i v_j : all i,j).

PR612, commit `799697070309151169a3517d5b0f263766ed0ffc`, `research/hm/cubic-jacobian-singular-schemes/PROOF.md`, proves the intrinsic singular ideal is m^d in these completed rings ([immutable source](https://github.com/Akilleez-QA/read-em-and-weep/blob/799697070309151169a3517d5b0f263766ed0ffc/research/hm/cubic-jacobian-singular-schemes/PROOF.md)). Section 7 below reproves exactly the relative Fitting calculation needed for the smoothing obstruction. No other geometric input is needed.

**Theorem.** More generally, put

    S = C[[u_1,...,u_m,v_1,...,v_n]],
    I = (u_i v_j),   A = S/I,

where m,n >= 2. Then the continuous cotangent deformation module T^1_cont(A/C;A) is zero. Every flat complete local deformation of A over a local Artin C-algebra, with its special fiber identified with A, is isomorphic to the constant deformation, compatibly with that identification. A trivialization over an Artin quotient lifts over any small extension whenever a flat deformation over that extension is already given.

Consequently all sixty completed singular germs of each of V and T are formally rigid. Neither V nor T admits a flat finite-type smoothing over a smooth pointed complex curve, or over Spec C[[t]], with smooth generic fiber of the same pure dimension. This is a statement about these actual cubic images, not about the original HM source, the full-adjoint construction, prescribed-source liftings, or their algebraicity gates. Global rigidity of V or T is not asserted.

## 2. The correct cotangent presentation

Use continuous differentials and continuous derivations for formal power-series rings, with maximal-ideal-adic topologies. The unrestricted algebraic differential module of C[[u,v]] is not used. Since S is formally smooth, the degree-one continuous cotangent deformation module has the presentation

    T^1_cont(A/C;A)
       = coker[Der_cont,C(S,A) -> Hom_A(I/I^2,A)],       (1)
    D |-> (g mod I^2 |-> D(g)).

This is the degree-one cotangent-complex group, not an unjustified substitution of Ext^1_A(Omega_cont,A). The conormal differential I/I^2 -> A^(m+n) need not be injective. Nor is the full cotangent complex asserted to be the two-term conormal complex in all degrees. Its truncation in degrees -1 and 0 suffices for degree-one cotangent cohomology; lower degrees contribute nothing in degree one against the degree-zero target A.

For the ordinary polynomial version of this conormal-cokernel and square-zero-extension description, see the Stacks Project [Deformations of rings and the naive cotangent complex, Remark 91.2.4](https://stacks.math.columbia.edu/tag/08S3). The identification with the degree-one group of the full cotangent complex, and the deformation-torsor interpretation, are in [Deformations of ring maps and the cotangent complex](https://stacks.math.columbia.edu/tag/08SM). Here formal substitutions are continuous; Section 5 supplies a direct complete-local small-extension proof, so the claimed Artin rigidity does not rest on an unproved passage from unrestricted algebraic differentials to continuous ones.

## 3. Every conormal homomorphism is an ambient derivative

Write U=C[[u_1,...,u_m]], W=C[[v_1,...,v_n]]. The ring A is the fiber product U x_C W. Its elements are pairs of series with equal constant term. Equivalently each element has a unique expression c+p(u)+q(v), where p and q have zero constant term.

Let h:I/I^2 -> A be A-linear, and write f_ij=h(u_i v_j). The identities among generators give necessary relations

    u_k f_ij - u_i f_kj = 0,                            (2)
    v_l f_ij - v_j f_il = 0.                            (3)

Let F_ij be the U-component of f_ij. Equation (2) gives u_k F_ij=u_i F_kj. Fix i and choose k different from i. Reduction modulo u_i takes place in the domain U/(u_i), in which u_k is nonzero. It follows that F_ij is divisible by u_i. Write F_ij=u_i a_ij. Substitution in (2) and cancellation in U gives a_ij=a_kj. Thus, for each j, there is a single a_j in U such that

    F_ij=u_i a_j   for every i.                         (4)

In particular all constant terms of f_ij vanish. Applying the same argument to the W-components using (3) and n>=2 gives b_i in W with

    f_ij = u_i a_j(u) + v_j b_i(v) in A.                (5)

The expressions a_j and b_i can have nonzero constants. There is no obstruction to viewing them as elements of A: the inclusion U -> A sends a(u) to the pair (a(u),a(0)), and W -> A is analogous. Define the continuous ambient derivation by

    D(v_j)=a_j(u),       D(u_i)=b_i(v).

Then D(u_i v_j)=u_i a_j(u)+v_j b_i(v)=f_ij. Since the classes of u_i v_j generate I/I^2, D induces h. This proves surjectivity in (1) and hence T^1_cont=0.

There is deliberately no hidden claim that (2)-(3) exhaust the syzygy module: only their necessity was used to bound Hom_A(I/I^2,A), and every resulting homomorphism was then realized by a genuine derivation. In fact this also proves sufficiency for the displayed arrays, because ambient derivatives satisfy every conormal relation, including any further relations. Thus a complete free resolution of I is unnecessary.

The dimension hypothesis matters. For m=n=1, I=(uv) and (1) instead gives T^1=C, represented by the usual node smoothing uv=t. That case is not being included in the theorem.

## 4. Coefficients and the torsor statement

The same calculation applies componentwise with target A tensor_C K for any finite-dimensional C-vector space K. Equivalently, finite direct sums commute with the Hom and derivative spaces in (1). Hence

    T^1_cont(A/C;A tensor_C K)=0.                       (6)

For a small extension B' -> B of local Artin C-algebras, let K be its kernel and assume m_(B') K=0. Given a fixed deformation over B, the classes of its flat lifts, with the identification over B fixed, form a torsor under (6) whenever such lifts exist. In the induction used here, the deformation over B is already trivial, so its constant lift exists. There is therefore exactly one isomorphism class of lifts. This says nothing about uniqueness of the isomorphism: infinitesimal automorphisms may remain. No vanishing of T^2 is claimed or needed.

## 5. Direct complete-local proof over a small extension

Here is a proof of the needed lifting statement without invoking any formal cotangent comparison theorem. A deformation means a Noetherian complete local B'-algebra R', flat over B', together with its closed-fiber identification; no additional chosen section is part of the data. Suppose a specific isomorphism

    R'/K R' = B[[u,v]]/(u_i v_j)

has already been fixed. Lift these coordinate elements to z_i,w_j in the maximal ideal of R'. Their products lie in K R'. Flatness identifies

    K R' = K tensor_(B') R' = K tensor_C A,

with these equalities understood via the injective multiplication map. In this module, multiplication by z_i and w_j acts as multiplication by u_i and v_j. Put h_ij=z_i w_j. The exact identities

    z_k h_ij-z_i h_kj=0,       w_l h_ij-w_j h_il=0

imply (2)-(3) in K tensor_C A. The calculation of Section 3, componentwise in a C-basis of K, therefore gives a_j,b_i in K R' such that

    h_ij=z_i a_j+w_j b_i.

Since K^2=0, replacing z_i by z_i-b_i and w_j by w_j-a_j makes every product zero. The corrections lie in the nilpotent ideal K R', hence the corrected coordinates remain in the maximal ideal and define continuous substitutions. They yield a B'-algebra homomorphism

    phi: B'[[u,v]]/(u_i v_j) -> R'

that induces the prescribed isomorphism modulo K. Both source and target are B'-flat: the source is the constant deformation A tensor_C B', which equals the displayed completed tensor product since B' is finite-dimensional over C.

The map phi is surjective: its cokernel C satisfies C=K C, hence C=K^2 C=0. After surjectivity, tensor the kernel sequence with B=B'/K. Flatness of R' makes the kernel modulo K inject into the source modulo K, where phi is an isomorphism. The kernel L therefore satisfies L=K L, hence L=0. This proves that phi is an isomorphism extending the prescribed trivialization.

Any local Artin C-algebra admits a finite sequence of such small extensions down to C. Induction proves the theorem for every such base. The statement concerns marked special fibers, not pointwise-fixed sections or fixed ambient embeddings; those are different deformation problems with potentially different tangent spaces.

## 6. Compatible formal families

Let R be a Noetherian complete local C[[t]]-algebra, flat over C[[t]], topologically presented using finitely many variables, with R/tR=A. At each stage the kernel of

    C[t]/(t^(r+2)) -> C[t]/(t^(r+1))

is killed by the maximal ideal. Section 5 extends an already chosen trivialization at stage r to one at stage r+1. The resulting isomorphisms are compatible, not merely unrelated isomorphisms at each order. Taking inverse limits gives

    R = C[[t,u,v]]/(u_i v_j)

as complete local C[[t]]-algebras. Here R is also t-adically complete: a Noetherian complete local ring is complete for an ideal contained in its maximal ideal, or one can use its finite power-series presentation and closedness of ideals. The isomorphism is not claimed to converge analytically or to algebraize. The same compatible construction works for a complete Noetherian local C-base through its maximal-ideal-power quotients, provided the family is flat and complete in the indicated sense.

## 7. Why actual algebraic smoothings are excluded

Specialize to m=n=d>=2. Suppose a flat finite-type family over Spec C[[t]], with special fiber one of the actual cubic images, had smooth generic fiber of pure dimension d. Let R_0 be the local ring of its total space at one of the sixty special singular points. Its maximal-ideal completion R is flat over C[[t]] and has special fiber A_d; flatness follows by composition with the flat completion map. Section 6 gives

    R = C[[t,u_1,...,u_d,v_1,...,v_d]]/(u_i v_j).

The completion of the finite relative differential module Omega_(R_0/C[[t]]) is the continuous relative differential module of R. Indeed derivations into finite complete modules are continuous by the product rule and extend uniquely from R_0 to its completion. Its presentation has generators du_i,dv_j and relations

    v_j du_i+u_i dv_j.

Consequently its d-th Fitting ideal is exactly (u_1,...,u_d,v_1,...,v_d)^d. Every d-by-d minor lies in that ideal. Conversely the rows (i_j,j), j=1,...,d, and columns dv_1,...,dv_d give every pure degree-d u-monomial as a diagonal minor; the analogous selection gives every pure v-monomial. Mixed monomials vanish, so these generate the whole indicated power. This calculation is over C[[t]], not just the special fiber.

Write J=Fitt_d(Omega_(R_0/C[[t]])). Smoothness of the generic fiber of pure dimension d makes J[1/t] the unit ideal. Thus t^N belongs to J for some N. Fitting ideals commute with completion, so t^N would lie in (u,v)^d inside R. But reduction modulo (u,v) maps R onto C[[t]] and sends t^N to the nonzero element t^N. This is a contradiction.

A smoothing over a smooth pointed complex curve reduces to this situation by completing the base at the distinguished point and the total local ring at the chosen special singular point. This argument does not need an algebraization of the formal trivializing coordinates, nor an algebraic section of the singular locus. It uses those coordinates only to contradict the vanishing of the relative singular ideal on the generic fiber.

## 8. Algebraic cotangent stalks and the global limitation

For completeness, the algebraic cotangent T^1 stalk of either image also vanishes. Let R_0 be an essentially finite-type complex local ring with completion A_d. Choose a local smooth ambient algebra P surjecting onto R_0, with ideal J. Its algebraic cotangent T^1 is the conormal cokernel

    coker[Der_C(P,R_0) -> Hom_(R_0)(J/J^2,R_0)].

Completing this finite-module presentation commutes with Hom because J/J^2 is finitely presented and completion is flat. The completed ambient smooth local ring is a finite-variable power-series ring, and the completed conormal presentation computes continuous cotangent T^1 of the completion. Invariance under complete-local C-algebra isomorphism identifies this with the zero module calculated above. Faithful flatness of completion therefore gives T^1(R_0/C;R_0)=0. At all other points the images are smooth, so the coherent cotangent T^1 sheaf vanishes everywhere on each image.

Vanishing of this local sheaf is not vanishing of global deformation classes: global degree-one cotangent cohomology can still contain the first sheaf cohomology of the tangent sheaf. No such global cohomology calculation is attempted here.

## 9. Limits and genuine new conclusion

This is stronger than identifying the branch ring, its conductor, depth, or singular Fitting scheme: it computes its degree-one cotangent deformation module and excludes smoothings of these particular image singularities. It does not imply global deformations are constant; globally nontrivial deformations can be locally trivial and can involve gluing or motion of the normalization data. It also does not assert that embedded deformations inside a fixed projective space are stationary.

Most importantly, none of these statements transfers to the original HM source or to any full-adjoint, prescribed-source, or higher-lifting problem without an additional theorem relating that problem to a smoothing of these images. No such theorem is supplied or assumed. No analytic convergence or algebraization of arbitrary formal deformations is proved. The algebraic nonsmoothability assertion in Section 7 is nevertheless valid because every hypothetical smoothing would itself supply the completed flat family to which the contradiction applies.
