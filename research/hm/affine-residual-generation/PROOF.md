# Actual residual basepoint-freeness from the twelve pentagons

Status: authored structural proof, independently mathematically reviewed in REVIEW.md; not formally checked. Work over C. No selected source point, coefficient matrix, rank, or hyperplane is evaluated.

## Immutable inputs and exact dictionary

Use PR569 at 3c79994aac419f7c963b06df52e0e330929318a2 for the primary integral surface S, its 25 pairwise disjoint Cartier lines L_v indexed by G=F_5^2, and its cyclic-block hyperplanes. Use PR570 at e5e55594ef2b99cefb81c4c02b22cb45e1ff0025 for the exact primary S15 identification: the normalization ν:X=S(5)→S identifies the distinguished lines with all 25 torsion sections and gives H=I+2F and C=sum_v L_v=5I. Thus ν^*(5H-C)=10F and H^2=15. The normalization is an isomorphism near the distinguished lines. This is an exact coordinate-copy identification, not an identification with the separate fixed-beta surface lane.

The projective translation groups also match. The coordinate pin in PR562 at 86b643fe2adecbd321d1c8f98be84fe2082bcd10, §§1 and 6, uses the actual Schrödinger basis e_i, the universal formula φ(e_i wedge e_j)=v_(i+j) tensor w_(j-i), and identifies the primary module A=V_3 as the third Galois transform of the standard HM module. In these coordinates the standard generators are the cyclic permutation e_i→e_(i-1) and diagonal e_i→ζ^i e_i. Their primitive Galois transforms replace the second generator by e_i→ζ^(a i)e_i, where 5 does not divide a, and leave the permutation matrix unchanged. The resulting generated projective subgroup is exactly the same: the new diagonal generator is a primitive power of the old one. Dual conventions merely invert these generators and again do not change the subgroup.

BHM §3.1 gives these same cyclic-permutation and diagonal coordinate generators for its Schrödinger module; §4.2 identifies their quotient G with translations by the torsion sections. PR570 copies the BHM coordinates x_i into the primary e_i coordinates. Thus on the identified surface it is the same projective G that translates the actual lines and the modular torsion sections. Choosing a different origin or generator convention changes their labels by an affine automorphism of F_5^2, which preserves affine lines and parallel classes. No equality of the linear central characters of A and the other incidence ambient module is asserted or required.

The public source is Barth–Hulek–Moore, “Shioda’s Modular Surface S(5) and the Horrocks–Mumford Bundle,” in Vector Bundles on Algebraic Varieties (TIFR):
https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

Its §3.1 gives the coordinate generators, §4.2 gives the translation and compatible SL2(F5) actions, disjoint torsion sections and five sections per pentagon component, and §4.3 gives the twelve I5 fibers and component self-intersection -2. The remaining fibers are smooth elliptic curves. The exact primary identification and polarization are supplied by PR570, using BHM §4.5, rather than inferred from numerical similarity.

## 0. Constructing all thirty affine-block divisors

For a direction U⊂G, PR569 proves that the five lines indexed by U span a unique ambient hyperplane Π_U. For any affine coset A=v+U, translate this hyperplane by v to obtain Π_A. This does not depend on the representative v: any element of U permutes the five lines in the block, and hence preserves their unique spanning hyperplane. Translation is projective linear, so Π_A is the unique hyperplane spanned by the five lines indexed by A. This constructs all thirty hyperplanes without evaluating any selected source coefficients.

The surface S spans its ambient P4, so no Π_A contains S. Its hyperplane section contains the five Cartier lines in A. Subtracting them gives the effective Cartier residual R_A=H-C_A, where C_A=sum_(v in A)L_v. For each direction U, choose nonzero equations ℓ_A of its five coset hyperplanes and let q_U=product_(A parallel U)ℓ_A. Since those cosets partition G, restricting q_U to S and dividing by the canonical section of C gives a nonzero section s_U of M=5H-C with divisor sum_(A parallel U)R_A. Choices of equations change only its nonzero scalar. These constructions supply the six actual residual sections used below; no unpublished affine-block lemma is needed.

## 1. Two pentagons for each direction

Translations preserve every fiber. On the dual graph of a pentagon they give a homomorphism G→D10. Since G has odd order, its image is either trivial or the rotation group of order five. It is not trivial: translation acts transitively on the 25 torsion sections, and each of the five components meets exactly five of them. Consequently translation acts transitively on the five components. Its kernel U is a subgroup of order five, hence a direction in G. The sets of section labels meeting the individual components are exactly the five affine cosets of U.

The assignment of this direction U to a singular fiber is equivariant for SL2(F5). That group acts transitively on the six directions in G. Therefore all six directions occur with equal multiplicity among the twelve singular fibers, so each occurs exactly twice. Denote the two fibers belonging to U by F_U^+ and F_U^-.

This argument uses only the group action and incidence counts. It requires neither coordinates for the cusps nor an evaluation of a selected source instance.

## 2. Exact multiplicities in an affine residual

Pull back R_A to X and retain the notation R_A. The divisor is effective. Since M=10F and

M.R_A=M.H-sum_{v in A}M.L_v=50-50=0,

every component of R_A is vertical. Let A be a coset of direction U.

For any pentagon component E, one has C.E=5 and F.E=0. Hence H.E=I.E=1. If its pentagon has direction U, exactly one component E_0 meets the five sections in A; the others meet none. Thus

R_A.E_j=1-5δ_{j0}.

If its pentagon has direction different from U, its five section-label cosets each meet A once, so R_A.E_j=0 for all j.

Write the coefficient vector of R_A on a U-pentagon as (a_0,...,a_4), with adjacent cyclic indices and E_0 the component just specified. Since different fibers are disjoint, the intersection equations are

-2a_j+a_{j-1}+a_{j+1}=1-5δ_{j0}.

Their integer solutions are

(a_0,...,a_4)=(3,1,0,0,1)+t(1,1,1,1,1), t∈Z.

Indeed the displayed vector satisfies the equations, and the kernel of the cycle Laplacian consists precisely of the constant vectors. Effectivity forces t≥0 because two coordinates of the displayed vector vanish. Its minimum H-degree is therefore five.

There are two U-pentagons. Together their compulsory minimal contributions already have H-degree ten. But H.R_A=H.(H-C_A)=15-5=10. Every additional effective vertical component has positive H-degree: each pentagon component has degree one, and a smooth fiber has degree five. Hence there can be no additional contribution. In particular t=0 on each U-pentagon, and R_A has no support on any other fiber.

Therefore R_A is exactly the sum of the two divisors with cyclic coefficient vector (3,1,0,0,1), centered at the components met by the five sections in A, one on each of F_U^+ and F_U^-.

Checks: each vector has degree five and self-intersection -10, so the complete residual has degree ten and square -20, in agreement with PR569 at d=15.

## 3. Divisors of the six residual product sections

For each U, summing over its five cosets centers the vector successively at all five components of each associated pentagon. Each component consequently has total coefficient 3+1+0+0+1=5. Thus the section s_U of M defined by the product of the five affine-block hyperplanes, divided by C, satisfies

 div_X(ν^*s_U)=5(F_U^++F_U^-).

The six unordered cusp pairs are disjoint and partition the twelve cusps. Therefore any two sections belonging to different directions have disjoint zero divisors on X. In particular the six pulled-back sections have no common zero.

Basepoint-freeness descends to S: for any point x∈S and any y∈ν^{-1}(x), the value of a section of an invertible sheaf is zero at x if and only if its pulled-back value is zero at y. Since ν is surjective, a common zero on S would give a common zero on X. Thus the six sections globally generate M on the actual possibly nonnormal S.

## 4. Consequences and limits

The morphism S→P5 defined by these sections is genuine and basepoint-free. On the normalization its pullback line bundle is O_X(10F), and its defining sections come from degree-ten sections on the base P1, with zero divisors five times the six cusp pairs. Its image is a curve whose normalization is P1. In fact the image has degree ten. To see this, let e be the degree of the induced finite map from the elliptic base P1 to the normalization of that image, and let m be the image degree. Then em=10. The system is normalizer-stable, so this map is A5-equivariant. The A5 action on the elliptic base is faithful, also seen by restricting the fibration to any chosen torsion section and using its faithful stabilizer action. The ramification divisor has degree 2e-2 and is A5-invariant. As in the companion proof, the point-orbit sizes are 12,20,30,60; for e dividing ten, the possible nonzero degrees 2,8,18 cannot occur. Therefore e=1 and m=10.

This does not by itself assert that the elliptic fibration X→P1 descends as a morphism S→P1. Nor does the divisor calculation alone assert that the restricted six sections are linearly independent, or determine the scheme structure of any nonnormal identifications. Those are separate questions.

## Verification boundary

The source passages and cited repository proofs are the inputs. The component-action argument, cycle-Laplacian calculation, degree exhaustion, descent of basepoint-freeness, and degree-ten image argument are structural deductions proved above. No computer-algebra test or formal proof assistant is claimed. This note does not identify the whole primary degeneracy scheme with S away from the locus covered by PR570, and does not establish the original generic-section goal.
