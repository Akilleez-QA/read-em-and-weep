# Orbit torsion and the regular block of the actual opposite pencil

Status: authored structural proof with independent mathematical review recorded in REVIEW.md; not formally checked. Work over C. No actual HM/source coefficient, parameter, point, matrix, derivative, rank or instance is evaluated.

## Inputs and notation

The exact input is PR934, commit 8c9847612b5f575b987cec9c62b72b099d745e44, research/hm/reduced-opposite-pencil/PROOF.md. Write G=SL2(F5), W for its binary two-space, A=Sym2 W, V for the other three-space, P for the four-space and D for the five-space. Its actual reduced pencil on T=P(W*) is

    0 -> E O(-1) --gamma--> H O -> C -> 0,
    dim E=26, H=1+3A+V+2P+2D, dim H=31.

C has rank five and degree 26. Its torsion is supported in the exceptional twelve-point set. Every sheaf and map is G-equivariant; the center acts trivially on C. The projective action is the faithful A5 action. The elementary orbit proof is included below, so no new geometric classification or exceptional-fiber result is imported. All earlier actual-geometric dependencies of PR934 remain in force.

Let Z=tors(C), F=C/Z, and let Omega denote the unique twelve-point orbit of the projective A5 action. If Z is nonzero, its support equals Omega and the exceptional twelve-point set, as proved below. Let f12 be any scalar section of O(12) with reduced zero divisor Omega; its normalization is irrelevant.

## Theorem

1. There is an integer m in {0,1,2} such that length(Z)=12m and length(Z_t)=m at every t in Omega. F is globally generated, of rank five and degree 26-12m. In particular the ideal I_Omega squared annihilates Z. If m=1, I_Omega itself annihilates Z. At an exceptional point the fiber-kernel dimension of gamma is at most two; it is one when m=1, and is either one or two when m=2, uniformly on the orbit.

2. The reduced pencil is the complete evaluation presentation of C. The inclusion Z->C canonically defines a square linear subpencil of size 12m, whose determinant divisor is m Omega; the quotient pencil is the complete evaluation presentation of F and has dimensions (26-12m)->(31-12m). There exists a G-equivariant constant source/target change splitting the original pencil into these two blocks. The complement and the block splitting are not canonical.

Thus nonzero torsion forces a regular 12->12 or 24->24 block, with determinant a nonzero scalar multiple of f12 or f12 squared. The complementary bundle pencil is respectively 14->19 or 2->7. This is not a choice of numerical normal form or an evaluation of the actual arrow.

3. Suppose m=2. Choose a generator zeta of the character group of an abstract point stabilizer C5 such that

    A|C5 = 1 + zeta + zeta^(-1).

Write I0=Ind(1)=1+A+V+D, I1=Ind(zeta)=Ind(zeta^(-1))=A+P+D, and I2=Ind(zeta^2)=Ind(zeta^(-2))=V+P+D. Exactly one of the following necessary character patterns holds:

    H0(Z)=I0+I1,  H0(F)=A+P;
    H0(Z)=2I1,    H0(F)=1+A+V;
    H0(Z)=I1+I2,  H0(F)=1+2A.

The corresponding possibilities for F as a G-bundle are, respectively:

    O(2) + P O,                 or W' O(1) + A O;
    O(2) + (1+V) O,             or W O(1) + V O;
    O(2) + (1+A) O,             or W O(1) + A O.

Here W' is the other binary two-space. These are necessary possibilities, not claims that all occur for the actual bundle.

In the middle pattern, every Z_t is annihilated by its maximal ideal and has vector-space dimension two. In particular the reduced pencil has fiber kernel exactly two there, and I_Omega Z=0 despite the determinant divisor being 2 Omega. The middle pattern cannot be cyclic length-two torsion. In either other pattern both the cyclic and the two-generator alternative remain undecided by this theorem.

## Proof of 1: global generation and the orbit budget

C is a quotient of H O, so it is globally generated; the quotient F is therefore also globally generated. On a smooth curve F is locally free. Its splitting on P1 has only nonnegative degrees, proving deg F>=0 and length Z<=26.

A finite subgroup of PGL2 fixing a point is cyclic: the tangent character is injective for a finite-order automorphism in characteristic zero. A5 has cyclic subgroups only of orders 1,2,3,5, so its orbit sizes are 60,30,20,12. There is exactly one twelve-point orbit: A5 has six subgroups of order five, each with two fixed points, and distinct such subgroups cannot share a fixed point because its stabilizer is cyclic. These twelve points form an invariant set and hence one orbit. If Z is nonzero, its support is G-invariant and contained in the exceptional twelve-point set; the orbit-size list forces that support to equal the unique twelve-point orbit Omega, and hence to equal the exceptional set. This argument does not need a separate invariance assumption on the exceptional set. Equivariance identifies all twelve nonzero stalk lengths, hence length Z=12m with 0<=m<=2. For Z=0 take m=0. A module of length m over a DVR is annihilated by the m-th power of its maximal ideal. For m=1 it is the residue field; for m=2 its underlying module is either R/(x^2) or k+k. The fiber Tor1 dimension is respectively one or two. These statements are uniform by equivariance. They prove the asserted annihilation and fiber-kernel bounds without assuming cyclicity or reading off length from fiber dimension.

## Proof of 2: complete evaluation and its functorial torsion block

Cohomology of the given exact presentation identifies H canonically with H0(C), since H0(O(-1))=H1(O(-1))=0. Thus its last map is actual complete evaluation. Its kernel K is the actual bundle E O(-1), and E=H0(K(1)). This is the intrinsic meaning of the source coefficient space; no unsupported identification of a chosen source basis with H0(C(-1)) is needed.

For every globally generated coherent sheaf M on P1, its evaluation kernel K_M is locally free, with H0(K_M)=H1(K_M)=0. The first vanishing follows because evaluation is the identity on global sections; the second follows by the same long exact sequence. As a locally free subsheaf of a trivial bundle, every line summand has degree at most zero; the H0 and H1 vanishings then force every summand to have degree exactly minus one. Thus K_M=H0(K_M(1)) O(-1). Its rank is h0(M)-rank(M). This also applies to a torsion sheaf, whose evaluation kernel is locally free although the evaluation quotient is not.

Apply this to Z,C,F. Because H1(Z)=0, the exact sheaf sequence gives exact global sections 0->H0(Z)->H0(C)->H0(F)->0. The evaluation diagram and the snake lemma give

    0 -> K_Z -> K_C -> K_F -> 0.

All three kernels are sums of O(-1), so twisting by one yields the exact coefficient-space sequence. This canonically places the evaluation pencil of Z inside that of C, with quotient the pencil of F. Its size is length Z, since h0(Z)=length Z. The determinant divisor is the local length divisor by Smith normal form; it is m Omega. Riemann--Roch and global generation give h0(F)=rank F+deg F, hence the claimed complementary dimensions.

Finally Ext1(F,Z)=H1(F* tensor Z)=0. Thus 0->Z->C->F->0 splits as sheaves. Averaging a splitting over finite G makes it equivariant. Functoriality of complete evaluation then produces compatible constant equivariant splittings of both coefficient sequences. This proves existence, not a canonical complement.

## Proof of 3: the degree-two quotient and stabilizer characters

The filtration of each length-two torsion stalk by powers of its maximal ideal has two one-dimensional composition factors, counted with multiplicity, as a representation of C5. Its global-section character is the sum of their inductions to A5. This uses composition factors, not an assumption that the stalk is reduced. The central involution acts trivially, so C5 rather than its binary lift suffices here.

The restrictions to C5 of the five A5 irreducibles are

    1: {0}; A: {0,1,-1}; V: {0,2,-2};
    P: {1,-1,2,-2}; D: {0,1,-1,2,-2}.

Frobenius reciprocity proves the displayed I0,I1,I2. Thus H0(Z) is one of the six unordered sums I_i+I_j. Subtracting each from H0(C)=1+3A+V+2P+2D gives:

    2I0:    -1+A-V+2P;
    I0+I1:  A+P;
    I0+I2:  2A-V+P;
    2I1:    1+A+V;
    I1+I2:  1+2A;
    2I2:    1+3A-V.

A genuine representation cannot have a negative irreducible multiplicity. This proves precisely the three stated patterns.

Since F is globally generated of rank five and degree two, its ordinary splitting type is O(2)+4O or 2O(1)+3O. Its degree filtration is G-invariant. The extensions between successive decreasing-degree pieces split equivariantly: the relevant H1(O(d-e)) vanish for d>=e, and a splitting can be averaged. A linearized O(2) factor has trivial multiplicity character because G has no nontrivial one-dimensional characters. Its global sections are A. In the second splitting type the two-dimensional O(1) multiplicity is center-odd and hence is W or W'. Their global-section characters are W tensor W=1+A and W' tensor W=P. Subtracting these characters from the three allowed H0(F) characters gives exactly the six bundles listed above. No other degree partition or multiplicity character is possible.

It remains to distinguish cyclic length two. The cotangent character at a C5-fixed point is zeta or zeta^(-1): the projective action comes from W, and its two eigenlines have eigenvalue ratio equal to one of the nontrivial weights of Sym2 W=A. For a cyclic length-two stalk, multiplication by a local parameter identifies its two composition-factor characters up to this cotangent twist. Their exponents therefore differ by 1 or -1 modulo five. In the middle pattern both factors belong to {1,-1}; two elements of this set differ by 0,2 or -2, never by 1 or -1. The cyclic alternative is impossible. The only length-two DVR module left is k+k, proving the final assertion.

## Contribution and boundaries

PR934 retained all exceptional torsion but neither bounded its length nor described an actual regular block. Here the orbit budget restricts it to two possible nonzero lengths, the canonical evaluation functor isolates its regular linear subpencil, and the maximal length case admits only three global character patterns and six quotient bundles. One of those patterns forces reduced support-module structure even though its determinantal multiplicity is two. This separates torsion length, fiber defect and nilpotence.

No choice among m=0,1,2 is made. Nothing proves local freeness of C, actual occurrence of a maximal pattern, a source exclusion, a frontier decrement, mixed-map solvability or algebraicity. This is authored structural mathematics, not formal proof-assistant verification.

## Further consequence: torsion cannot all disappear in the vertex-ideal extension

Retain the additional exact geometric input from PR934 Section 6:

    0 -> O(10) -> D_vert -> C -> 0.

In the middle maximal-torsion pattern above, tors(D_vert) has total length either twelve or twenty-four. In particular D_vert is not locally free, and at least one copy of the residue field survives at each exceptional point. This is stronger than the general inclusion tors(D_vert)->tors(C).

Indeed tors(D_vert) injects into Z since a line bundle has no torsion. At an exceptional stalk R, pull the extension back to Z_t=k^2 and call its middle module M. The quotient of D_vert,t by M is the free module F_t, so the torsion of D_vert,t equals that of M. Every extension 0->R->M->k^2->0 is classified by Ext1_R(k^2,R)=k^2. A zero class gives M=R+k^2. A nonzero class can be transformed to (1,0) by a change of basis of k^2, and then M=R+k, with R included into the free summand by multiplication by a uniformizer. These changes of basis are only a proof of the local module classification, not chosen actual evaluations. Therefore its torsion length is respectively two or one. Equivariance and transitivity make the same alternative hold at all twelve points. Outside Omega there is no torsion. Summing proves the assertion, without asserting which extension class occurs.
