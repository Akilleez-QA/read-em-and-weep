# Finiteness of the entire rank-one (2,3) rectangular incidence

## Theorem and dependencies

Over C, let dim V=5, let J be finite-dimensional, and let f:V^3 -> J be a trilinear map that is outer symmetric and cyclic zero. Assume that every repeated-input map A_a:V/Ca -> J, b -> f(a,a,b), is injective. Then the closed projective determinantal scheme

    R = {([u],X,Y) in P(V) x Gr(2,V) x Gr(3,V): dim f(X,u,Y)<=1}

has finite support, and hence is a finite scheme over C. No reducedness is asserted.

We use two existing results, with exactly these hypotheses:

1. The polar-pair locus D = {([h],[u]): rank f(h,u,-)<=2} has finite support; see /research/hm/middle-surface/extremal-surface-geometry/PROOF.md, Sections 1–3.
2. The complementary triples in R form a finite set; see /research/hm/incidence-foundations/fixed-splitting-curve-exclusion/STRONGER.md, Section 5.1. Its determinant-pole argument applies to any complete curve meeting the complementary open set, including curves whose middle is constant.

The new argument proves that the remaining boundary is finite. In particular the earlier possibility of positive-dimensional vertical boundary fibers is eliminated.

## 1. Pointwise control, including all limits

For independent a,b, A_a(b) and A_b(a) are independent: a dependence A_a(b)=t A_b(a) would give A_(a+t b)(b)=0, contrary to injection. The identity follows by expanding and using f(b,a,b)=-2 A_b(a).

At every rectangular triple, u lies in neither X nor Y. Indeed if u belongs to X, A_u(Y) has dimension at least two and lies in the rectangular image; if u belongs to Y, A_u(X) has dimension two once the first case is excluded.

Also dim(X intersection Y)<=1. Otherwise X is contained in Y. Every nonzero h in X then has

    f(h,u,h)=-2 A_h(u) != 0

in the rectangular image, since u is not in X. That image cannot be zero. A coordinate on its one-dimensional image would give a homogeneous quadratic on the two-dimensional X with no projective zero, impossible over C.

If X intersection Y=Ch, put H=X+Y, of dimension four. Outer symmetry implies

    f(h,u,H) subset f(X,u,Y).

The displayed nonzero value at h proves that the rectangular image is the line

    L=C f(h,u,h).

If u belonged to H, both f(h,u,h)=-2 A_h(u) and f(h,u,u)=A_u(h) would belong to L, contradicting independence. Hence u is transverse to H. The polar P=f(h,u,-) has rank at most two because its restriction to the hyperplane H has image in L. Its values on h and u are independent, so its rank is exactly two. Moreover,

    H=P^(-1)(L).                                           (1)

Indeed the right side has dimension dim ker P+dim L=3+1=4 and contains H.

These assertions hold on all closed points of R, rather than merely on an initially chosen open family.

## 2. The boundary is genuinely closed and projective

Let B be the closed subscheme of R defined by the determinant of the tautological addition map

    X_bundle direct-sum Y_bundle -> V tensor O_R.

Its support is precisely the noncomplementary locus. At every point of B the addition map has rank four by Section 1; intersection dimension two is forbidden everywhere. Therefore B is projective and contains every degeneration of a boundary family. No additional open condition is being tacitly imposed.

Let C be an irreducible component of B with reduced structure. The addition map on C has constant rank four. Its kernel and image are vector subbundles. This remains true if C is singular: locally invert a nonzero rank-four minor, and use reducedness to make the remaining Schur-complement entries vanish. The kernel, projected into X_bundle (equivalently, with opposite sign, into Y_bundle), is the line subbundle

    K=X_bundle intersection Y_bundle subset V tensor O_C.

Thus the intersection line defines a regular morphism C -> P(V), and pairing it with the middle coordinate gives a regular morphism

    C -> D,       ([u],X,Y) -> ([h],[u]).                    (2)

One can work entirely on reduced loci: the minors defining D vanish on every fiber, hence vanish as regular functions on reduced C.

Since D has finite support and C is integral, (2) is constant. Write its values as Ch and Cu. Formula (1) now fixes H as well; neither the line L nor its inverse image depends on scaling the representatives h,u.

## 3. Quotient projectors eliminate all vertical families

On C the subbundles X_bundle and Y_bundle lie in the fixed H and contain the fixed Ch. Their quotients are subbundles of the trivial rank-three bundle

    (H/Ch) tensor O_C.

Their ranks are one and two, respectively. At every point their intersection is zero and their sum is all of H/Ch. Hence the addition map is an isomorphism of bundles:

    (X_bundle/Ch) direct-sum (Y_bundle/Ch)
        isomorphic to (H/Ch) tensor O_C.                    (3)

Projection onto either summand along the other gives a globally regular endomorphism of this fixed trivial bundle. Every matrix entry is a global regular function on the integral projective variety C, hence constant. Thus both quotient subspaces X/Ch and Y/Ch are constant.

A subspace of H containing Ch is uniquely the full inverse image of its quotient subspace in H/Ch. Consequently X and Y are constant. The middle u was already constant. These are all ambient coordinates of C in R, so C is a point.

There are finitely many irreducible components of B. Therefore B has finite support. Combining this with the finite complementary locus proves that R has finite support. Since R is a projective finite-type zero-dimensional scheme over C, its structure morphism is finite. Possible nonreduced infinitesimal structure is not controlled by this proof.

## 4. Boundary and scheme audit

- B is closed before applying completeness; one never applies projective rigidity to an open boundary stratum.
- Intersection dimension is identically one on B, so the intersection-line map is regular, not merely rational.
- The polar map has rank exactly two at every boundary point, including limiting points; h and u cannot collide because u is not in X.
- Fixing the pair fixes the image line L and the hyperplane H by (1). No choice of complement or coordinate normalization enters this step.
- The quotient projectors are regular globally because (3) is an everywhere invertible bundle map, even on a singular reduced component.
- A boundary family cannot acquire intersection dimension two or u in H at its limit, by the global pointwise exclusions. A family inside B cannot acquire a complementary point because B is closed.
- Components meeting the complementary locus are covered by the separate determinant-pole theorem, not by an unjustified extension of quotient projectors across a change in intersection rank.
- All conclusions about individual triples and families are set-theoretic. Finite scheme does not mean reduced, etale, or rigid against infinitesimal deformations.

## 5. Precise consequences for compatible type III scrolls

The normal form and coefficient comparison in /research/hm/middle-surface/squarefree-scroll-middle-families/PROOF.md, Sections 4–5, associate to every compatible ordered type III scroll its intrinsic projection spans:

    X=span{x-mu u, y-nu u},
    Y=span{z-lambda u, y-alpha u, w-beta u}.

Their dimensions are two and three, and ([u],X,Y) belongs to R. It follows that there are only finitely many triples consisting of a middle line and these intrinsic projection spans. This includes complementary and contraction configurations. At a fixed middle, the oriented span choices are finite; swapping the outer factors adds at most the two orientations. On any integral algebraic family where these spans are defined algebraically, the span triple is constant.

There is also a useful fixed-triple geometric statement. Let a triple in R have nonzero rectangular image line M. After choosing its scalar coordinate, write

    f(x,u,y)=beta(x,y) m,       x in X, y in Y.

The rectangular ordered zero locus is the canonical bidegree-(1,1) hypersurface

    Z_beta = {([x],[y]) in P(X) x P(Y): beta(x,y)=0}.          (4)

It depends only on the triple and f, not the choice of m or representative u. For the type III normal form, with p=x-mu u, q=y-nu u, r=z-lambda u, s=y-alpha u, t=w-beta u, coefficient comparison gives the scalar matrix, up to a nonzero overall scalar,

    rows p,q; columns r,s,t:  [[0,0,1],[0,-1,0]].

The scalar is nonzero by the everywhere-rank-one fact on R proved in STRONGER.md, Section 1. Thus beta has rank two. The hypersurface (4) is irreducible and is a P^1-bundle over P(X)=P^1: for each nonzero x, beta(x,-) is nonzero, so its kernel is two-dimensional. In fact it is the Hirzebruch surface F_1 (the kernel bundle is O direct-sum O(-1), up to the projectivization convention). The ordered type III parametrization has dense image in (4), and hence its reduced closure equals (4).

Accordingly, if by an ordered scroll one means precisely its reduced closed ordered-lift image in P(V) x P(V), the above normal form identifies that image with the uniquely determined Z_beta. There are then finitely many such geometric ordered-lift images, with middles recorded. This assertion is separate from finiteness of parametrizations, coordinate frames, correction parameter presentations, or arbitrary scroll embeddings into other ambient spaces, none of which follows automatically. Without making that identification of what is being counted, the unconditional conclusion is the finite set of intrinsic span triples.

The theorem does not classify all residual kernels, does not exclude isolated compatible scrolls, and does not change dimension claims for other independent-zero strata. It strengthens the existing compatible explicit type III analysis by eliminating moving span choices even at a fixed exceptional middle.
