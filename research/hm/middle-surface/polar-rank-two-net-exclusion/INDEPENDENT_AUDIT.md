# Independent audit of the low-polar-rank net exclusion

## Verdict

PASS. The classification and compatible-locus dimension bound in `PROOF.md` are correct over C as stated. Both classification routes close all indicated cases. I checked the universal polarization lemma and the finite-partner-plane/fixed-factor lemma in their cited files directly. No substantive repair is required.

The conclusion remains restricted to nets with generic polar rank at most two. It does not settle proper surface components of the rank-drop locus for generic-rank-three nets.

## 1. Differential rank and common factors

For the quadratic map q=(q_0,q_1,q_2), the affine differential is 2M(x). Euler gives M(x)x=q(x), so at points where q(x) is nonzero, passing to projective tangent spaces lowers the rank by exactly one. The characteristic-zero generic-rank theorem consequently gives image dimension at most one. A point image or a line image would supply constant linear relations among the independent q_i. Thus the image closure is an integral nondegenerate plane curve.

The common-factor exclusion is exhaustive: a homogeneous common factor of independent quadrics can only have degree one. If q_i=hL_i, independence of q_i implies independence of the three L_i. Their linear map E→C³ is surjective, so their projective map dominates P². Cancelling h contradicts the established curve image. Degree two would make all three quadrics proportional.

Generic polar rank at most one is already ruled out by this projective-image argument. The appendix's separate differential argument is also valid: over C(E), a nonzero dq_0 spans all dq_i, Euler identifies the multiplier as q_i/q_0, and vanishing differential makes that rational function constant in characteristic zero.

## 2. General-line degree argument

No common divisor implies the base locus has codimension at least two in P³. A general line misses such a locus: for a curve the family of lines meeting it has dimension at most three, whereas Gr(2,4) has dimension four; zero-dimensional components pose no problem.

A general line has nonconstant restriction. For example, pairs of general points determine general lines; constancy on a dense open family of lines would make the rational map constant on general pairs of points.

On a base-point-free line the three sections of O(2) generate that line bundle. Therefore the restricted morphism has pullback O_C(1)=O_P¹(2). Its nonconstant image is all of C, and the degree formula is valid whether expressed directly for a finite map of integral curves or via normalization. It gives 2=δ deg C. Nondegeneracy forces deg C≥2, hence C is an integral plane conic and δ=1. Over C that conic is smooth and can be put into the stated standard form.

The final UFD argument has no hidden coprimality assumption: a common irreducible divisor of q_0 and q_2 divides q_1 by q_0q_2=q_1², contradicting the established absence of a common divisor of the three. Coprime q_0,q_2 must therefore both be squares up to constants. Homogeneity and degree two make their square roots linear; independence makes the two roots independent.

## 3. Quadratic-syzygy alternative

At generic rank two, two independent Jacobian columns have a nonzero cross product with homogeneous quadratic entries. It annihilates all columns over C(E), and its polynomial dot products consequently vanish identically. Removing the homogeneous gcd leaves a nonzero syzygy with common entry degree 0, 1, or 2, allowing zero entries without affecting the argument.

Degree zero contradicts independence after integrating the differential relation (or contracting with Euler). For degree one, Euler gives Σr_iq_i=0; differentiating and subtracting the syzygy gives Σq_i dr_i=0. Each coefficient is a constant linear relation among the q_i, so dr_i=0 for every i. Homogeneous linear entries must vanish, a contradiction.

The cited universal polarization lemma is correct. Its two coefficient identities show that Σr_i(x)q_i(y) is symmetric in x,y. Membership in both S⊗W and W⊗S forces membership in W⊗W, and independence then gives r=Cq with C constant symmetric. Euler gives qᵗCq=0. Since r is nonzero, C is nonzero. A rank-one or rank-two ternary quadratic form factors over C, and substitution would force a forbidden constant linear relation among the q_i in the polynomial domain. Thus C has rank three.

For complete independence from the general-line proof, the rank-three relation alone yields the UFD form (q_0,q_1,q_2)=h(a²,ab,b²), with a,b relatively prime homogeneous polynomials of equal degree. Independence forces deg a=deg b≥1, while deg h+2 deg a=2. Hence h is constant and a,b are independent linear forms. This is precisely the argument cited in the appendix, so the second proof does not secretly rely on the first proof's common-factor exclusion.

## 4. Kernel and product locus

The identified W is the full symmetric square of the two-dimensional quotient dual. Its annihilator is exactly ker(Sym²E→Sym²(E/R)), a seven-space equal to RE. The equality ab∈K iff a∈R or b∈R follows from absence of zero divisors in the symmetric algebra of E/R. Likewise, the squares in K are exactly those with factor in R. There is no extra component of the product incidence.

## 5. Finite fully compatible partner planes

The cited parameter locus H⊂P(E)×Gr(3,E) is closed. The condition aU⊂K is a bundle-map vanishing condition; on that closed locus the restriction of v is defined, and the wedge condition is a polynomial identity in b∈U, so its coefficientwise vanishing is closed as well.

If a∈U, choose two vectors b,c∈U independent modulo Ca. Compatibility for a+tb with t≠0 implies v(a²)∈span(a,b) after taking t→0; the second choice gives membership in span(a,c). Their intersection is Ca. Since a²∈K, this contradicts square avoidance. Thus H misses the incidence divisor.

For dim E=4 and dim U=3, the Grassmannian is the dual projective space, and the incidence divisor has ample bundle O(1,1). Any positive-dimensional projective H contains an integral projective curve, on which a nowhere-zero incidence section would trivialize a line bundle of positive degree. Hence H has finite reduced support. The dimensions here are essential to this particular ample-divisor argument and are satisfied.

For a fixed factor a, put M_a={b:ab∈K}. If dim M_a≤3, any two-dimensional component of the compatible locus is dense in the plane P(M_a), and its polynomial identity extends to the plane. If M_a=E, write π:E→E/Ca and T(b)=v(ab) mod Ca. Outside [a], compatibility means (T−λπ)b=0 for a unique λ. The pencil has generic rank three because π has rank three (a suitable minor has nonzero leading coefficient). Thus the generic projective kernel is a point; only finitely many λ can have larger kernels. The pencil can never be zero, since T=λπ would imply T(a)=0 and violate square avoidance. All kernels have projective dimension at most two, and every surface component is one of these kernel planes. Each such plane is recorded by H and avoids [a]. This proves both the universal fiber bound two and finiteness of factors with a surface fiber.

## 6. Final dimension passage

An irreducible component of the ordered compatible locus lies in one of P(R)×P(E) or its transpose. Its corresponding factor image has dimension at most one. A point image gives dimension at most two by the fixed-factor bound. A curve image avoids the finite exceptional factor set generically, so its generic fiber has dimension at most one; the dimension theorem again gives at most two. The argument applies to the locally closed independent-pair locus using its usual constructible dimension, with polynomial closure where needed.

Multiplication on independent pairs is finite-to-one onto its image: a rank-two product over C has exactly its two distinct projective linear factors, up to exchange. Thus passing to compatible projective rank-two tensors preserves the dimension bound.

## Scope of this audit
