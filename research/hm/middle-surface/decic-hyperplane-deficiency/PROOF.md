# The genus-eleven hyperplane deficiency forces ACM, hence contradiction

## Result and scope

Over C, let Y be an integral H5-invariant decic surface in P4, with the standard primitive central character on linear forms, and suppose its general scheme-theoretic hyperplane section C is integral of arithmetic genus 11. Then Y is arithmetically Cohen–Macaulay.

Consequently, when Y is also invariant under the full normalizer specified in /research/hm/middle-surface/acm-decic-exclusion/PROOF.md, that theorem excludes Y. This eliminates the genus-eleven alternative of /research/hm/middle-surface/decic-middle-surface-constraints/PROOF.md, conditional on its imported hypotheses. The argument neither assumes nor transfers invariants to a resolution, and does not assume Y is locally Cohen–Macaulay or that C is Gorenstein.

The initially proposed non-ACM alternative would force omega_C = O_C(2), with Rao module C concentrated in degree 2. That alternative is indeed the only possible curve deficiency on numerical grounds. But it cannot lift to an H5-invariant Y: it would force the one-dimensional group H^2(P4,I_Y(1)), contradicting its primitive central character.

## 1. Low-degree equations and linear normality

Write I_Y for the saturated ideal sheaf and J_Y for its homogeneous prime ideal. The argument of Section 2 of /research/hm/middle-surface/acm-decic-exclusion/PROOF.md proves

    (J_Y)_1 = (J_Y)_2 = (J_Y)_3 = 0.

For completeness, each nonzero degree-d space for d=1,2,3 has dimension divisible by five. If d=2 or 3 is the smallest equation degree, take independent equations f,g of degree d. A nonconstant common divisor q would, by primeness and the absence of smaller equations, force f/q into J_Y, a contradiction. Thus f,g are coprime, their complete intersection has degree d^2, and cannot contain the degree-ten surface since d^2<10. Degree one is excluded by irreducibility of the five-dimensional representation.

The section C spans its P3. Indeed H^1(I_Y)=0 because Y has only constant global functions, while I_Y(1)=0; the degree-one ideal restriction sequence therefore gives I_C(1)=0.

Put L=O_C(1). We have h^0(C,L)=4. Indeed, if it were at least five, choose five sections including the four defining the given embedding into P3. They define a closed immersion into P4: projection to those first four coordinates is everywhere defined on the image and recovers the original embedding. The image is nondegenerate of degree ten and arithmetic genus eleven. The arithmetic Castelnuovo bound in P4 is pi(10,4)=9, a contradiction. The bound for integral curves, including singular curves, is the one cited in Section 6 of /research/hm/middle-surface/decic-middle-surface-constraints/PROOF.md.

Since Y is integral projective, h^0(O_Y)=1. The restriction sequence

    0 -> O_Y -> O_Y(1) -> L -> 0

therefore bounds h^0(O_Y(1)) by five. The five ambient linear forms inject, so equality holds.

## 2. Riemann–Roch without a Gorenstein hypothesis

Every integral projective curve is Cohen–Macaulay. Its dualizing sheaf omega_C is torsion-free of rank one and degree 2p_a(C)-2=20, with degree defined by Euler characteristic. Tensoring a rank-one torsion-free sheaf by L changes its degree by deg L=10.

A rank-one torsion-free sheaf F of negative degree has no nonzero section: such a section gives an injection O_C -> F with finite-length cokernel, forcing deg F to be nonnegative. If deg F=0 and F has a nonzero section, the same cokernel has length zero, so F is isomorphic to O_C. In particular its section space has dimension one. These statements hold even at non-Gorenstein singularities.

Serre duality and Riemann–Roch now give

    h^0(C,L^2)=10+epsilon,  epsilon in {0,1},
    h^0(C,L^n)=10n-10 for n>=3.

Here epsilon=1 if and only if omega_C tensor L^(-2) is O_C, equivalently omega_C is L^2. In this case C is consequently Gorenstein; that property was not assumed.

Restriction on Y implies h^0(O_Y(2)) <= 5+11=16. The ambient quadrics inject, giving a lower bound fifteen. The center acts on the whole space H^0(O_Y(2)) by the nontrivial degree-two character, so its dimension is divisible by five. Thus

    h^0(O_Y(2))=15.

Similarly, h^0(O_Y(3)) <=15+20=35, and the 35 ambient cubics inject, so

    h^0(O_Y(3))=35.

It follows that H^1(I_Y(t))=0 for t=1,2,3. The hyperplane ideal sequence, exact because the hyperplane equation is a nonzerodivisor on O_Y, then gives

    H^0(P3,I_C(2))=H^0(P3,I_C(3))=0.

Thus the homogeneous coordinate ring R_C has Hilbert function 1,4,10,20 in degrees 0,1,2,3.

## 3. Ten general plane-section points impose independent quartic conditions

Take a further general hyperplane section Gamma of C in P2. It consists of ten distinct points and has the uniform position property. This is the characteristic-zero uniform position theorem for any integral curve; it does not require the curve to be smooth. Joe Harris, “Interpolation,” printed page 168, explicitly states the irreducible-curve version:

https://library.slmath.org/books/Book59/files/60harris.pdf

Linear normality gives H^1(I_C(1))=0. The ideal restriction sequence from C to Gamma therefore gives H^0(I_Gamma(2))=0, because H^0(I_C(2))=0. Consequently h_Gamma(2)=6.

There is some subset of six points imposing six independent conic conditions, by rank of the evaluation matrix. Uniform position implies that every six-point subset has that property. Hence every subset of at most six points imposes independent conic conditions.

Fix p in Gamma, and partition the other nine points into subsets A and B of cardinalities five and four. There is a conic q_A vanishing on A and not at p, because A union {p} imposes six independent conditions. There is a conic q_B vanishing on B and not at p, because B union {p} imposes five independent conditions. The quartic q_A q_B vanishes on Gamma minus {p} and not at p. Doing this for each p proves

    h_Gamma(4)=10, and h_Gamma(n)=10 for all n>=4.

The latter follows by multiplication by a linear form nonvanishing at all ten points. This avoids any unproved assertion about Macaulay growth, decreasing-type Hilbert functions, or saturation of an Artinian reduction.

## 4. The complete possible Rao module of C

Let ell be the linear form cutting Gamma on C. It is a nonzerodivisor on the domain R_C. The quotient R_C/ell R_C surjects onto the saturated homogeneous coordinate ring of Gamma. The kernel may contain finite-length saturation torsion: we do not assume it vanishes. Accordingly,

    dim (R_C)_n - dim (R_C)_(n-1)
      = dim (R_C/ell R_C)_n >= h_Gamma(n).

Since dim(R_C)_3=20, Section 3 gives dim(R_C)_n >=10n-10 for all n>=3. On the other hand the coordinate ring injects into H^0(C,L^n), which has precisely that dimension by Section 2. Equality follows for every n>=3. In particular saturation torsion in the quotient is zero in degrees >=4, but this was a conclusion rather than an assumption.

For n<0 both ambient and curve sections vanish by degree; in degree zero both are constants, and in degree one linear normality applies. Thus the entire Hartshorne–Rao module is

    H^1(P3,I_C(n)) = 0 for n != 2,
    dim H^1(P3,I_C(2)) = epsilon in {0,1}.

If epsilon=1, omega_C is O_C(2). If epsilon=0, C is ACM. The two alternatives cannot be distinguished from curve numerics alone.

## 5. Equivariance rules out epsilon=1

Write D_t=H^1(P4,I_Y(t)) and E_t=H^2(P4,I_Y(t)). We already proved D_1=D_2=D_3=0. The long exact sequence of

    0 -> I_Y(t-1) -> I_Y(t) -> I_C(t) -> 0

gives the exact portion

    D_t -> H^1(I_C(t)) -> E_(t-1) -> E_t.

For t>=3 the middle curve group is zero. Hence E_(t-1) injects into E_t. Serre vanishing for the fixed coherent sheaf I_Y makes E_t=0 for all sufficiently large t. Successive injections therefore give E_2=0.

At t=2, the same exact sequence and D_2=0 now identify

    H^1(I_C(2)) = E_1

as vector spaces. The hyperplane is not invariant and no equivariance of this identification is asserted or needed. It proves dim E_1=epsilon<=1. But E_1 itself carries the H5 action on the invariant ideal sheaf I_Y(1), with the primitive degree-one central character. Every representation of that central character has dimension divisible by five. Therefore E_1=0 and epsilon=0.

This is the crucial additional obstruction: a one-dimensional Rao module at degree two would lift to a forbidden one-dimensional surface cohomology group at degree one.

## 6. ACM lifts from C to Y, in all twists

Now H^1(I_C(t))=0 for every integer t. The same ideal restriction sequence implies D_(t-1) -> D_t is surjective and E_(t-1) -> E_t is injective, for every t. The latter and Serre vanishing give E_t=0 for all t, including negative t.

For every t<0, D_t identifies with H^0(Y,O_Y(t)), which vanishes. One direct justification uses restriction to the integral degree-ten curve C: H^0(C,L^t)=0 for t<0, so H^0(O_Y(t-1)) maps isomorphically to H^0(O_Y(t)) for all t<0; sufficiently negative twists of an ample inverse have no sections. Equivalently, a nonzero section of a negative ample twist on an integral projective variety would have an effective divisor with negative ample degree, which is impossible. Also D_0=0 because global functions are constants. Surjectivity then gives D_t=0 for all positive t as well.

The saturated coordinate ring of Y has no zeroth local cohomology; the groups D_t and E_t measure the next two local-cohomology modules. Their vanishing in every twist is precisely the cohomological ACM criterion for a surface in P4. Therefore Y is ACM. This criterion and its local-cohomology interpretation are also recorded in /research/hm/middle-surface/acm-decic-exclusion/PROOF.md, Section 5.

## 7. Consequence and remaining dependencies

Under full normalizer invariance, the independently established ACM-decic exclusion contradicts Section 6. Thus no full-normalizer-invariant integral decic of sectional arithmetic genus eleven exists.

This proof's non-elementary inputs are: the arithmetic Castelnuovo bound for integral curves; the characteristic-zero uniform position theorem for integral curves; duality/Riemann–Roch for Cohen–Macaulay projective curves; and the standard cohomological ACM criterion. The first and last are sourced in the imported proof files. The uniform position statement was checked directly in Harris's linked text. All further Hilbert-function and representation steps are supplied here.

  The full rank-locus conclusion still depends on the separate separate genus-six and genus-sixteen exclusions and original conditional inputs; this file does not independently audit those.
