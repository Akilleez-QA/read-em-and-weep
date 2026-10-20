# Independent zeros over residual-rank strata

## Result and scope

Work over C, with dim V = 5, and assume the following symbolic hypotheses: a trilinear map f with values in J, outer symmetry, the cyclic-zero identity, and the repeated-input injection. Retain also the previously established statement that the projective residual-rank-drop locus has codimension at least two in P(V). No rank instance is evaluated here.

The main conclusion is as follows. Over the residual-rank-exactly-nine middle stratum, let T be the locus where the unique projective kernel tensor has rank exactly two. There is a canonical rank-two bundle W on T, a canonical compatibility locus C in T, and a finite étale ordered-factor cover of degree two

    C_ordered → C.

The scheme of ordered, separately projectivized, linearly independent zero triples over the rank-nine stratum is canonically isomorphic to C_ordered, with the precise scheme structures specified below. In particular, its reduced locus has dimension at most two. The corresponding all-inputs-nonzero affine independent-zero locus has dimension at most five. A component of that affine locus of dimension greater than five must lie over middle residual rank at most eight.

More generally, on a locally closed constant-rank-r middle stratum S_r, with r ≤ 9,

    dim(projective independent-zero locus over S_r) ≤ dim S_r + 9 − r,
    dim(affine independent-zero locus over S_r) ≤ dim S_r + 12 − r.

Thus the rank-eight part has affine dimension at most six, and every affine independent-zero component of dimension at least seven lies over middle residual rank at most seven.

All dimensions are Krull dimensions of finite-type schemes, equivalently of their reductions. Empty loci are allowed throughout. No conclusion asserts nonemptiness, transversality, expected codimension of compatibility, or occurrence of any rank value.

## 1. Projective bundles and the necessary twists

Write B = P(V), using the convention that projective space parametrizes lines. On B put

    U = O_B(−1) ⊂ V ⊗ O_B,
    E = (V ⊗ O_B)/U.

Thus E has rank four. The cyclic-zero identity implies f(u,u,u) = 0. Consequently the repeated-input map is intrinsically a bundle map

    A: U^⊗2 ⊗ E → J ⊗ O_B.

The repeated-input injection hypothesis makes its image F a rank-four subbundle; A identifies U^⊗2 ⊗ E with F. Outer symmetry makes the residual map symmetric in its outer variables. Changes of lifts from E to V contribute only to F, giving the well-defined map

    Q: Sym² E → (J ⊗ O_B/F) ⊗ U^∨.

At a chosen nonzero generator u of U, this is the familiar residual map Q_u. Its source has rank ten. We use the symmetric-algebra convention p ⊙ q = p q, with the associated symmetric bilinear map sending p q to f(p,u,q). Equivalently, in a tensor-square realization, p q corresponds to (p ⊗ q + q ⊗ p)/2. No factor of two is hidden in later formulas.

For scheme-level assertions, S_r may be the determinantal rank-exactly-r stratum of Q, or its reduction, or any locally closed base change on which Q has algebraic constant rank r. Here “algebraic constant rank” means that the (r+1)-minors vanish and locally an r-minor is invertible, so that kernel, image, and cokernel are vector bundles. In particular, the reduced locus on which the geometric rank is r has this property. On S_r put

    K_r = ker(Q|S_r),     rank K_r = 10 − r.

The rank-ten stratum has no independent zeros, by the argument recalled in Section 8.

## 2. The rank-two kernel-tensor parameter space

First take r = 9. Then K = K_9 is a line subbundle of Sym² E. Its contraction map is

    K ⊗ E^∨ → E.

Let T be its determinantal rank-exactly-two stratum inside S_9: impose the rank-at-most-two minors and remove rank at most one. This scheme structure, which need not be reduced, is intentional. On T the image

    W = im(K ⊗ E^∨ → E)

is a rank-two subbundle of E. The symmetric tensor K lies in Sym² W, and its induced contraction K ⊗ W^∨ → W is an isomorphism. These statements hold over the scheme T, not just at its geometric points: locally split E by the image of the constant-rank contraction; symmetry removes every component outside Sym² W, and the remaining contraction is invertible.

For arbitrary r ≤ 9, replace S_9 by the projective bundle

    H_r = P_{S_r}(K_r),

with tautological line K = O_{H_r}(−1) ⊂ Sym² E. Define T_r inside H_r by exactly the same determinantal rank-exactly-two construction. The notation U, E, K, W below always means their pullbacks to the relevant parameter space. The rank-nine construction is the special case H_9 = S_9.

## 3. The finite étale ordered-factor cover

On any T = T_r just constructed, every geometric fiber of K ⊂ Sym² W is a nondegenerate binary symmetric tensor. Over an algebraically closed field of characteristic zero it is the product of two distinct lines in W.

Here is a scheme-theoretic construction that does not choose those lines. On π: P_T(W) → T let L = O(−1) be the tautological line. Define D by the vanishing of

    π* K → Sym²(π* W/L).

A line L lies in D precisely when it divides the binary tensor K. Since W/L is a line bundle and W/L ≅ π*(det W) ⊗ L^∨, this is the zero scheme of a section of

    π*(K^∨ ⊗ (det W)^⊗2) ⊗ O(2).

The nondegeneracy of K makes this a relative degree-two divisor with invertible discriminant. Consequently D → T is finite étale of degree two. For example, étale locally on T the binary tensor factors into two distinct lines, and the divisor is the disjoint union of the two corresponding sections. Alternatively, on an affine root chart its quadratic equation has invertible discriminant, so its degree-two algebra is étale; the projective divisor has degree two and is finite over T.

The discriminant and its twist can be written without trivializing them globally. If k is a local generator of K and e_1,e_2 a local basis of W, write formally

    k = a e_1² + b e_1 e_2 + c e_2².

Then

    δ(k²) = (b² − 4ac)(e_1 ∧ e_2)²

defines a canonical isomorphism

    δ: K^⊗2 → (det W)^⊗2.

Its invertibility is exactly nondegeneracy. Let N = K ⊗ (det W)^∨. The factor cover is equivalently the square-root cover with algebra O_T ⊕ N, whose multiplication N^⊗2 → O_T is induced by δ. This gives another direct proof that it is finite étale of degree two, since 2 and δ are invertible.

The map D → T carries a canonical fixed-point-free involution τ exchanging the two factors. More explicitly, D parametrizes ordered pairs (L_1,L_2) of line subbundles of W with

    W = L_1 ⊕ L_2,
    multiplication L_1 ⊗ L_2 → K an isomorphism.

The first line is the tautological divisor point; the second is the uniquely determined other factor. For k = p q, the ordered pair gives the square root k ↦ p ∧ q of δ, and reversing the order negates that square root. Thus τ exchanges L_1 and L_2 and acts by −1 on N in the cover algebra. The cover need not split globally; no choice of a global square root, orientation, or ordering is assumed.

## 4. Complement-independent compatibility

Choose locally a splitting s: E → V ⊗ O and a nonzero local generator u of U. For k ∈ K ⊂ Sym² E, define B_{s,u}(k) using the symmetric bilinear map

    p q ↦ f(s(p),u,s(q)).

Because Q(k) = 0, this lies in F. Invert A_u: E → F to define

    v_{s,u}(k) = A_u^−1 B_{s,u}(k).

For a factorization k = p q, replacing the lifts by

    s(p) + αu,     s(q) + βu

changes v by

    v ↦ v + βp + αq.

This follows directly from trilinearity, outer symmetry, and f(u,u,u) = 0. It lies in W. More generally, a change of splitting contributes the contraction of k with the splitting difference and therefore has image in W. It follows that the class of v in E/W is independent of the splitting.

Replacing u by λu changes v to λ^−1 v. Hence the invariant compatibility map, with its full twist, is

    ψ: K → U ⊗ (E/W),
    k ↦ u ⊗ [v_{s,u}(k)].

Equivalently it is a map U ⊗ K → U^⊗2 ⊗ (E/W). It is a section of the rank-two vector bundle

    K^∨ ⊗ U ⊗ (E/W).

Define C = Z(ψ) as its scheme-theoretic zero locus in T, and put

    D_C = D ×_T C.

Then D_C → C is finite étale of degree two, including when C is nonreduced. Nothing here says that the two compatibility equations are independent or that C is nonempty.

## 5. Recovering the unique outer directions

Work on D_C, choose u and local nonzero frames p ∈ L_1, q ∈ L_2, and use s to regard p,q as lifts in V. Since multiplication L_1 ⊗ L_2 → K is an isomorphism, p q generates K. Compatibility says exactly that

    v = A_u^−1 f(p,u,q) ∈ W.

There are unique coefficients ν, μ with

    v = νp + μq.

Set

    x = p − μu,     z = q − νu.

The exact expansion gives

    f(x,u,z) = A_u(v − νp − μq) = 0.

Their residual images p,q are independent, so x,u,z are linearly independent and in particular nonzero.

These formulas define algebraic line subbundles in V and are independent of every auxiliary choice:

- If the lifts p,q change to p+αu,q+βu, then ν,μ change to ν+β,μ+α. The displayed vectors x,z do not change.
- If p,q,u change to ap,bq,λu, with a,b,λ units, then v changes to (ab/λ)v. Consequently ν changes to (b/λ)ν, μ changes to (a/λ)μ, and x,z change to ax,bz. Their lines do not change.
- These statements also apply on nonreduced test schemes, since all decompositions use direct summands and invertible functions.

Thus there is a canonical morphism

    Φ: D_C → (P(V) × P(V) × P(V))_ind,
    (middle line, kernel line, ordered factors) ↦ ([x],[u],[z]),

where the subscript means the open locus of three linearly independent lines. The middle factor is the given line in S_r. The involution τ corresponds exactly to interchanging the first and third factors.

For fixed u,p,q, this is also the uniqueness statement: writing x=p+a u and z=q+c u, the zero equation is

    c p + a q + v = 0.

Since p,q are independent, it holds precisely when v ∈ W, and then uniquely a=−μ and c=−ν. There is no residual affine family of outer directions after separate projectivization.

## 6. Exact scheme correspondence and reductions

Let Z_ind be the zero scheme of the trilinear section on the open independent locus in P(V)^3. Its defining section has target J tensored by the duals of the three tautological lines, so its vanishing is well-defined without choosing representatives. Let Z_ind,r be its base change along the middle projection to S_r.

We claim that Φ is an isomorphism

    D_C ≅ Z_ind,r.

To construct the inverse, on an arbitrary test scheme carrying an independent triple let P,Q ⊂ E denote the residual first and third tautological lines. Independence means that P ⊕ Q → E is a rank-two subbundle inclusion. Multiplication gives a line subbundle

    P ⊗ Q → Sym² E.

The full zero equation implies Q(PQ) = 0, so this line lies in K_r and defines a point of H_r = P(K_r). Its symmetric contraction has rank exactly two and image P ⊕ Q, not merely at geometric points but as a split bundle calculation. All rank-at-most-two minors therefore vanish identically. Consequently the map factors scheme-theoretically through T_r with the determinantal scheme structure used in Section 2. The pair (P,Q) supplies its ordered factors and hence a point of D.

Choose local lifts and write the outer vectors as p+a u,q+c u. The full equation yields v=−c p−a q. Therefore ψ vanishes scheme-theoretically and the map factors through D_C. The unique-coefficient calculation of Section 5 makes these two constructions mutually inverse on every test scheme. This proves the isomorphism, including nilpotents.

In rank nine H_9 = S_9, so this is exactly the asserted degree-two cover of the compatibility locus in the middle rank-nine, rank-two-kernel stratum. For smaller ranks, the compatibility locus lives in the rank-two part of the projectivized kernel bundle, rather than solely in the middle base.

A safe reduced-only formulation is also available. Start with the reduced rank-r middle stratum and the reduced rank-two kernel-tensor locus; take the reduced compatibility locus. Its ordered-factor cover is canonically the reduction of Z_ind,r. Finite étale covers of reduced schemes in characteristic zero are reduced. One must not, however, replace the determinantal rank-two locus by its reduction and then claim to have retained the full original nonreduced independent-zero scheme. The exact nonreduced assertion above uses the indicated determinantal locus.

## 7. Scaling, dimensions, and the meaning of projectivization

“Projectivized triples” here means separate projectivization of the three inputs: a locus in P(V)^3. It does not mean projectivization by only one common scalar in V^3.

The all-inputs-nonzero affine independent-zero scheme maps to Z_ind as the product of the punctured first, middle, and third tautological line bundles. It is a Zariski-locally trivial (G_m)^3-torsor. Thus it has dimension exactly three greater on every nonempty component. These three free scales are the two outer scales and the additional middle scale. Fixing an actual middle vector removes the middle factor but leaves the two independent outer scales. There is no assertion that these torsors, or the factor double cover, are globally trivial.

On rank nine, the cover D_C → C is finite and surjective, so, when nonempty,

    dim Z_ind,9 = dim C ≤ dim S_9.

The given codimension-at-least-two bound for the rank-drop locus in P(V)=P^4 implies dim S_9 ≤ 2. Hence

    dim Z_ind,9 ≤ 2,
    dim(affine independent-zero rank-nine part) ≤ 5.

For r ≤ 9, H_r → S_r is a projective bundle of relative dimension 9−r. The rank-two compatibility locus C is locally closed in H_r, and its finite étale cover has the same dimension. Therefore

    dim Z_ind,r ≤ dim S_r + 9−r,
    dim(affine independent-zero rank-r part) ≤ dim S_r + 12−r.

Every S_r with r ≤ 9 lies in the same rank-drop locus, so dim S_r ≤ 2. In particular, the affine rank-eight part has dimension at most six. These are upper bounds only; no subtraction of two for the two compatibility equations is justified without further information.

If one instead quotients affine triples by a single common scalar, the rank-nine upper bound would be four, not two. This distinction does not affect the affine bound five.

## 8. Consequences for components and precise stopping point

At a rank-ten middle line the residual map is injective. An independent triple has independent residual vectors p,q, so p q is a nonzero rank-two tensor. Its residual equation Q_u(p q)=0 is impossible. Thus the entire independent-zero locus lies over residual rank at most nine.

Let Y be an irreducible component of the reduced all-inputs-nonzero affine independent-zero locus. If Y meets rank nine, its rank-nine part is a nonempty open subset of Y, because no point of this independent-zero locus has rank ten. Its dimension is therefore dim Y and is at most five. Consequently, if dim Y > 5, then every point of Y has middle residual rank at most eight.

For such a component lying over rank at most eight, any nonempty rank-eight part is open in Y and has dimension dim Y. The rank-eight bound is six. Hence a component of dimension at least seven lies entirely over rank at most seven. More generally the constant-rank bounds may be applied to the largest middle rank occurring on an irreducible component; the closedness of the lower-rank determinantal loci makes that largest-rank part nonempty and open.

These conclusions concern the independent, all-inputs-nonzero locus. They make no assertion about dependent triples, coordinate-zero strata, their boundary germs, or the full vertex. 
