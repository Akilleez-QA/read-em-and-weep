# Common-radical nets with generically full ternary polar rank

## Statement

Work over C. Let dim E=4, dim K=7, and v:K→E be linear and square-avoiding: v(a²)∉Ca whenever 0≠a and a²∈K. Suppose W=K⊥ has a common radical line Ce. Suppose its polar evaluation M(x):E→W* has generic rank three. Then the compatible rank-two locus in P(K) has dimension at most two.

This excludes the entire specified common-radical, generic-rank-three branch. It does not address nets with generic polar rank at most two, or nets without a common radical line.

Dependencies: the universal fixed-factor/finite-partner-plane results in /research/hm/universal-polar/rank-three-compatible-fiber-structure/PROOF.md, Sections 1–2, and the square-avoiding K6 theorem in /research/hm/universal-polar/rank-four-compatible-fiber-bound/PROOF.md. No restricted subspace is assumed to remain a full residual kernel.

## 1. Quotient and preliminary reductions

Put V=E/Ce, dim V=3. The forms in W descend to independent symmetric forms B1,B2,B3 on V. In bases, their polar evaluation is a 3×3 matrix N(x) whose ith row is Bi(x,−). Its determinant is a nonzero homogeneous cubic by hypothesis. The original evaluation M(a) is N(a mod Ce) after quotienting its domain.

There is no nonzero common radical vector in V. Indeed such a vector t would give N(x)t=0 for every x, contrary to generic invertibility. In particular N(x)≠0 for every nonzero x∈V.

It suffices to exclude an integral ordered compatible threefold Z. Multiplication ([a],[b])↦[ab] is finite onto the rank-at-most-two product locus, so this excludes compatible rank-two dimension at least three. Take closures of ordered loci throughout; compatibility away from the diagonal is the closed polynomial identity v(ab)∧a∧b=0, together with ab∈K.

By the universal finite-partner-plane lemma, neither factor image of Z has dimension zero or one. A three-dimensional first image is impossible: wherever M(a) has rank three its kernel is exactly Ce, so the second factor is [e]. This would give a three-dimensional fixed-e compatible locus, whereas every fixed-factor compatible locus has dimension at most two. The same argument applies to the other projection.

Thus both factor images are surfaces. Let A be the first image. Its general fiber in Z has dimension one, so rank M(a)≤2 generically on A. Since the rank-zero locus is only [e], the remaining cases are generic rank two and generic rank one.

## 2. Generic rank-two surface images are impossible

The rank-drop locus D={rank M≤2} is the hypersurface det N(a mod Ce)=0 in P(E), a cone with vertex [e]. Every irreducible surface contained in D is an irreducible component of D and therefore contains [e]. Thus [e]∈A.

At a general a∈A of rank two, the projectivized partner space P(ker M(a)) is a projective line containing [e]. The one-dimensional fiber of Z over a fills this line. Consequently the entire line satisfies the compatibility identity, and in particular (a,e) is compatible. Closedness extends this identity over A. Its rank-two part identifies A as a surface in the fixed-e compatible locus.

Every surface component of a fixed-factor compatible locus is a plane avoiding that fixed factor, by Sections 1–2 of the cited universal lemma. Since A itself is an integral surface, it must be such a plane and must avoid [e]. This contradicts [e]∈A.

## 3. Ternary rank-one curves are lines

Let R⊂P(V) be the locus rank N≤1. Any irreducible curve C⊂R has degree at most two: all 2×2 minors vanish on C and at least one such minor is a nonzero quadratic, since det N≠0. The defining irreducible polynomial of C divides every minor.

Suppose C is an irreducible conic with equation q. All cofactors are scalar multiples of q, so adj(N)=qC0 for a constant matrix C0. Since N is generically invertible, so is adj(N), and C0 is invertible. The identity N adj(N)=det(N) I yields

    N C0 = ℓ I

for a nonzero linear form ℓ (the diagonal entries give the same polynomial quotient det(N)/q). Thus N=ℓ C0⁻¹.

For each row i, the associated symmetric bilinear form has the shape Bi(x,y)=ℓ(x)ri(y), where ri is the ith row of C0⁻¹. Symmetry implies ri is proportional to ℓ: choose x with ℓ(x)≠0 and compare Bi(x,y)=Bi(y,x). All rows of C0⁻¹ are consequently proportional, contradicting invertibility. Hence every irreducible curve in R is a line.

## 4. A rank-one line is totally isotropic for the net

Let P(U)⊂R be a line, dim U=2. The linear pencil {N(u):u∈U} consists of nonzero rank-one matrices, and its vector-space dimension is two because N has no nonzero zero.

Elementary rank-one-pencil fact: a two-dimensional space spanned by rank-one maps R=r⊗α and S=s⊗β consists entirely of rank-at-most-one maps only if either r,s are proportional or α,β are proportional. Otherwise choose domain vectors on which α,β give independent coordinates; R+S has rank two. Thus the pencil has either a common one-dimensional image or a common two-dimensional kernel.

The common-image case is impossible here. If all N(u) have image in a line L⊂W*, the two-dimensional annihilator L⊥⊂W consists of symmetric forms vanishing on U×V. Each such form descends to V/U, which is one-dimensional; the space of these forms has dimension at most one. This contradicts dim L⊥=2 and the independence of W.

Hence all N(u) have a common two-dimensional kernel H⊂V. If H≠U, choose nonzero t∈H∩U. Because t∈U, H⊂ker N(t). Because t∈H, symmetry of every Bi implies U⊂ker N(t). Therefore H+U=V lies in ker N(t), giving N(t)=0, impossible. Thus H=U.

It follows that Bi(U,U)=0 for all i. Moreover ker N(u)=U for every nonzero u∈U, since each N(u) has rank one.

## 5. Generic rank-one surface images reduce to K6

If rank M is generically one on A, its image under projection P(E)\{[e]}→P(V) lies in R. A cannot map to a point because a projection fiber is only a line. Its image is therefore a curve C, and A is the full cone over C. Section 3 shows C=P(U) is a line. Hence A=P(F), where F⊂E is the three-dimensional inverse image of U and contains e.

Section 4 gives Sym²F⊂K. At every a∈P(F)\{[e]}, the partner kernel is exactly F. Thus the dense open of Z over such a lies in P(F)×P(F), and closedness places all of Z there. Every product ab from Z belongs to the six-dimensional subspace K0=Sym²F⊂K.

The restriction v|K0 remains square-avoiding. Multiplication is finite, so Z supplies a compatible rank-two threefold in P(K0). This contradicts the K6 theorem, including its ternary-support case. No compatibility-preserving projection of v to F is used or needed.

This exhausts all possible factor images and all generic polar ranks on a surface image, proving the statement.

## Audit

The argument uses abstract symmetric bilinear forms, projective dimensions, elementary rank-one pencils, and the already established K6 theorem. There are no remaining cases within the stated common-radical-line and generic-rank-three hypotheses.
