# The sectional-genus-sixteen invariant decic is impossible

## Result

Work over C and retain all conditional hypotheses and notation of /research/hm/middle-surface/decic-middle-surface-constraints/PROOF.md. Its unique hypothetical integral invariant decic surface Y cannot have sectional arithmetic genus 16. Consequently the list there improves from {6,11,16} to

    p_a(C) in {6,11}.

No smoothness, normality, projective normality, or Cohen–Macaulay hypothesis on Y is added. This excludes one genus branch, not all invariant decics. In fact the exclusion only uses H5-invariance, integrality, nondegeneracy, degree ten, and an integral general hyperplane section of arithmetic genus sixteen.

## 1. The general section and an elementary completeness argument

The imported proof establishes that C=Y intersect H is scheme-theoretically integral, spans H=P3, and has degree ten. Suppose p_a(C)=16, and write L=O_C(1).

We first prove h^0(C,L)=4, including when C is singular. The four ambient coordinate sections form a basepoint-free subspace W of H^0(C,L) defining the given closed immersion into P3. If h^0(C,L)>=5, adjoining one independent section produces a five-dimensional basepoint-free subspace W'. Its map f:C→P4 is again a closed immersion. Explicitly, on a chart where one of the original four coordinates is nonzero, it is the graph of the extra regular ratio over the original affine closed immersion; these charts cover C. The image is closed globally because C is projective. Equivalently projection away from the new coordinate point recovers the original closed immersion, and the image avoids that point.

The image is nondegenerate because the five sections are linearly independent. Its hyperplane bundle is still L, so its degree is ten, and it is isomorphic to C, with the same arithmetic genus sixteen. The arithmetic Castelnuovo bound for integral nondegenerate curves in P4 instead gives

    p_a(C) <= pi(10,4)=3 binom(3,2)+3*0=9,
    since 10-1=3*3+0.

This is impossible. Thus h^0(C,L)=4. We use exactly the integral/arithmetic Castelnuovo theorem already checked in the imported proof (Miro-Roig, Theorem/Definition 4.13); no normalization or geometric-genus substitution occurs.

## 2. A maximal-genus degree-ten space curve has a quadric: direct Hilbert-function proof

Let P be a general plane of H=P3 and let Γ=C intersect P. It consists of ten distinct points. The uniform position theorem applies to integral, possibly singular, curves in characteristic zero. In the present case Γ is in linear general position: no three points are collinear.

For completeness, Γ spans P. If a linear form ell on P vanishes on Γ, lift it to H and let h define P. The exact sequence

    0 → O_C --h--> O_C(1) → O_Γ(1) → 0

and H^0(O_C)=C show ell|_C=a h|_C. Since C spans H, ell=a h as ambient forms, and its restriction to P is zero. Hence Γ spans P. There is therefore a noncollinear triple, and uniform position makes every triple noncollinear.

Let h_Γ(n) denote its homogeneous coordinate Hilbert function. For n>=1,

    h_Γ(n) >= min(10,2n+1).

Here is the elementary interpolation proof. Choose m=min(10,2n+1) of the points. For each chosen point p, partition the other m-1 points into at most n pairs and singletons. Each pair determines a line avoiding p, since no three points are collinear; choose a line through each singleton avoiding p. The product vanishes at all the other chosen points and not at p. Multiply by further linear forms avoiding p if needed to reach degree n. These polynomials prove independence of evaluation at the m chosen points.

Now let R=C[x0,x1,x2,x3]/I_C be the homogeneous coordinate ring, and B=R/hR. The integral-domain property of R makes multiplication by h injective. Thus

    dim B_n = dim R_n - dim R_(n-1).

The coordinate ring of Γ is the saturation quotient of B, so there is a graded surjection B→R_Γ and

    dim B_n >= h_Γ(n) >= min(10,2n+1).

These statements do not assume that B is saturated or that C is arithmetically Cohen–Macaulay. Both Hilbert functions are eventually ten. For t sufficiently large, summing the displayed difference gives

    dim R_t = 1 + sum_(n=1)^t dim B_n = 10t + 1 - p_a(C).

Consequently the finite-sum identity is

    p_a(C) = sum_(n>=1) (10-dim B_n).

Some individual summands could be negative; that causes no problem, since the comparison is termwise and both sequences are eventually ten. It follows that

    16 = p_a(C) <= sum_(n>=1)(10-min(10,2n+1))
                  = 7+5+3+1 =16.

Every difference dim B_n-min(10,2n+1) is nonnegative, and their sum is zero. Therefore equality holds termwise. In particular dim B_2=5. Since C spans P3, dim R_1=4, so dim R_2=9. As there are ten quadratic forms on P3,

    h^0(P3,I_C(2))=10-9=1.

This proves the needed quadric assertion without invoking a classification of Castelnuovo curves or assuming C smooth.

## 3. Linear normality of the surface and lifting the quadric

The equation of H is a nonzerodivisor on the integral surface Y. Hence

    0 → O_Y → O_Y(1) → O_C(1) → 0

is exact. Since Y is integral and projective, h^0(O_Y)=1. Section 1 gives

    h^0(O_Y(1)) <= 1+h^0(O_C(1))=5.

Nondegeneracy gives five independent ambient sections, so equality holds and H^0(P4,O(1))→H^0(Y,O_Y(1)) is an isomorphism. The ideal sequence, together with H^1(P4,O(1))=0, gives

    H^1(P4,I_Y(1))=0.

Restriction to H yields the ideal-sheaf exact sequence

    0 → I_Y(1) --h--> I_Y(2) → i_* I_(C/H)(2) → 0.

To justify it without a Cohen–Macaulay assumption: h is a nonzerodivisor on O_Y, so Tor_1(O_Y,O_H)=0. Tensoring 0→I_Y→O_P4→O_Y→0 by O_H identifies I_Y tensor O_H with I_(C/H); multiplication by h is injective on I_Y as well. Twisting gives the sequence above.

The H^1 vanishing makes restriction on quadratic ideals surjective. Its kernel is H^0(I_Y(1))=0 by nondegeneracy. Thus restriction is an isomorphism and Section 2 gives directly

    dim H^0(P4,I_Y(2)) = dim H^0(H,I_(C/H)(2)) = 1.

The nonzero quadric lifts uniquely. The following section gives an independent geometric check of the upper bound; it is not needed for the contradiction.

## 4. There is room for at most one quadric

An integral nondegenerate surface of degree ten in P4 cannot lie in two independent quadrics q1,q2.

Indeed each nonzero quadric containing Y is irreducible: if it factors into linear forms, primality of the homogeneous ideal of Y implies that one factor vanishes on Y, contrary to nondegeneracy. Thus two independent quadrics are coprime. Their intersection is a codimension-two complete intersection of degree four. An integral surface contained in it is an irreducible component and has degree at most four, a contradiction. Thus

    dim H^0(P4,I_Y(2)) <= 1.

Combined with Section 3, that dimension is exactly one.

## 5. Heisenberg symmetry forbids that line

Because Y is H5-invariant, its space of quadratic equations is an H5-subrepresentation of Sym^2(V*) (with the dual convention reversed if P4 was defined using the other convention). Let z generate the center and let ζ be its primitive fifth-root scalar on V. On quadrics it acts by ζ^(-2), a nontrivial fifth root (or ζ^2 in the opposite convention).

But every one-dimensional representation of H5 is trivial on its commutator subgroup, and for the level-five Heisenberg group [H5,H5]=Z(H5). Therefore no H5-stable line in Sym^2(V*) can exist. This contradicts the exactly one-dimensional space of quadrics just obtained.

Equivalently every representation with this nontrivial central character has dimension divisible by five. The line contradiction alone suffices and avoids requiring a full classification of irreducible representations.

## Sources and scope

- Internal established inputs: /research/hm/middle-surface/decic-middle-surface-constraints/PROOF.md, especially Sections 5–6. Its integral-section and arithmetic-Castelnuovo statements are used unchanged.
- Uniform position for integral curves: Paola Bonacini, *On the plane section of an integral curve in positive characteristic*, arXiv:1009.4021, Theorem 2.4 on page 3. This research paper explicitly states the characteristic-zero theorem for an integral curve in P3 and attributes it to J. Harris, *The genus of space curves*, Math. Ann. 249 (1980), 191–204, Section 2. Full Bonacini PDF is in sources/Bonacini-1009.4021.pdf; https://arxiv.org/pdf/1009.4021 . Only this uniform-position input is used from the paper.
- Arithmetic Castelnuovo bound: Rosa M. Miro-Roig, *Complete intersection liaison and Gorenstein liaison: new results and open problems*, Le Matematiche 55, fasc. II, 319–337, Theorem/Definition 4.13, printed page 331. https://lematematiche.dmi.unict.it/index.php/lematematiche/article/download/275/252/1043 . See source inventory for downloaded copy.

All remaining deductions are given explicitly above.
