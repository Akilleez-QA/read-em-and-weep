# Two cubics: the marked carrier is a heptic, octic, or complete-intersection nonic

## Scope and conclusion

Assume the generic actual HM hyperplane section Z=C intersect H consists of 25 reduced spanning points, no three collinear, with h0(I_Z(2))=0 and h0(I_Z(3))=2. Retain the canonical normalizer action on labels and the actual quintic sheaf generation with finite base exactly Z. This note does not assume any unresolved three-cubic case has been closed.

There is a unique marked integral component D of the reduced cubic complete-intersection support containing all 25 points, and those points are smooth on that reduced support. Its possible degrees and arithmetic genera are precisely restricted to:

- degree 7, genus 4 or 3;
- degree 8, genus 7, ACM, with resolution 0 -> 2O(-5) -> 2O(-3) directsum O(-4) -> I_D -> 0;
- degree 9, genus 10, the reduced integral complete intersection of the two cubics.

These are necessary alternatives, not existence claims. In degree seven, the residual curve in the cubic complete intersection is either two skew lines, or a nonplanar double line with conormal quotient O_L(c) for c=0 or 1. The cubic-linkage condition itself excludes all c>=2, not merely numerical genus considerations.

## 1. The marked integral component

Let V=H0(I_Z(3)), of dimension two. Its two independent cubics cannot have a common surface factor. A greatest common factor has degree one or two and is canonical. The generic subset of labels on it is invariant, hence empty or all. If all labels lie on it, a quadric or linear equation contains Z. If none does, dividing both cubics by it supplies equations of degree at most two through Z. Either possibility contradicts h0(I_Z(2))=0.

Thus a basis F,G cuts a complete-intersection curve Y of degree nine, and its reduced support Y_red has degree at most nine. It contains all Z. The finite singular locus of Y_red is canonical. A general quintic from the actual generating system avoids all its components and has total intersection length at most 45. Each singular marked point would contribute at least two: a length-one quotient by a nonzerodivisor would make the maximal ideal principal and the reduced one-dimensional local ring regular. Transitivity makes the generic singular-label subset empty or all; all would contribute at least 50, impossible. Hence Z lies in the smooth locus of Y_red.

Each marked point consequently belongs to exactly one component. The marked subsets on components form a canonical partition. Its equally sized blocks number a divisor of 25, at most nine, hence one or five. Five marked components would each contain five points and could not be lines by no-three-collinear, so their total degree would be at least ten. Thus there is one integral component D containing all Z.

A proper quintic cut gives 25<=5 deg D. The degree-five case is excluded by the reusable constant-Plucker marked-family theorem at c159a09d691605f3254d4d01eca07e042647e6d0. Hence 6<=d:=deg D<=9. Since D contains Z and is contained in both cubics,

h0(I_D(3))=2, and h0(I_D(2))=0.

D spans H, is canonical in the family, and the marked points are smooth on it. Integrality implies D is locally Cohen–Macaulay.

## 2. Residual duality and the genus formula

For d<9 let R be the closed residual curve defined by I_R=I_Y:I_D. It is locally Cohen–Macaulay of degree r=9-d, without any reducedness assumption. Residual duality gives I_D/I_Y=omega_R(-2). Since h0(I_Y(3))=2 and H1(I_Y(3))=0, the equality h0(I_D(3))=2 yields

h0(omega_R(1))=h1(O_R(-1))=0.

Set t=h0(O_R(-1))>=0. Riemann–Roch gives t=1-p_a(R)-r, hence p_a(R)=d-8-t. The (3,3) liaison genus identity gives p_a(D)-p_a(R)=d-r=2d-9. Therefore

p_a(D)=3d-17-t.                         (1)

This formula explicitly retains the possible nonreduced negative-twist sections.

## 3. Degree six is impossible

If d=6, formula (1) gives p_a(D)=1-t<=1. The marked-carrier normalization focal argument applies to this family exactly as to any moving integral sextic with 25 smooth marked points; it does not require three cubics. First, the rank-three characteristic map would have determinant degree at most 30+2p_a(D)-2<=30, but all its maximal minors vanish twice at the 25 marked points. Thus the family cannot dominate P4.

Its canonical swept image cannot be a surface either: incidence dimension and Bertini would make the general D its hyperplane section, giving an invariant surface of degree six, whereas an invariant surface degree is divisible by five. Consequently it sweeps an integral hypersurface. The rank-two gradient-kernel inequality from SEXTIC-FOCAL-GAUSS-EXCLUSION.md, 2f0970771fef9b7f814064929df3a8e0c3d3a837, applies:

25<=4d+2g-2-ramification,

where g<=p_a(D)<=1 is the normalization genus. For d=6 the right side is at most 24, a contradiction. Unlike the genus-two case, no equality or Gauss-series endpoint argument is needed.

The supporting nondominance proof is MARKED-CARRIER-FOCAL-NONDOMINANCE.md at 1dd24cf0361755b13f796d15e5eb7d855b167a63. Its proof uses the marked-family hypotheses and degree six, not the dimension of the cubic system.

## 4. Degree seven: classify the residual double structures and bound their conormal degree

Here R has degree two and h1(O_R(-1))=0. A reduced irreducible degree-two curve is a plane conic, for which h1(O_R(-1))=1, so is excluded. Two reduced intersecting lines are likewise a plane conic and excluded. Two skew lines have the required vanishing and arithmetic genus -1; liaison gives p_a(D)=4.

The remaining possibility is a double structure on a line L. Since R is locally Cohen–Macaulay of degree two, I_L^2 is contained in I_R: its image vanishes generically and a zero-dimensional subsheaf of O_R is forbidden by local Cohen–Macaulayness. The square-zero ideal J=I_L/I_R is rank-one torsion-free on the smooth line, hence J=O_L(c). The conormal quotient

2O_L(-1) -> O_L(c)

is surjective and forces c>=-1. If c=-1 the quotient is given by constants and R is planar, already excluded. Thus c>=0. The sequence 0 -> O_L(c-1) -> O_R(-1) -> O_L(-1) -> 0 gives t=c and p_a(D)=4-c.

We now use the actual cubic linkage to force c<=1. Choose linear equations x,y for L. The conormal quotient is given by two degree-(c+1) forms f,g on L with no common zero. For a cubic P vanishing on R, its first normal part is x*A+y*B with A,B quadratic forms on L. It must satisfy A*f+B*g=0. Since f,g are coprime, such pairs are multiples of (g,-f). If c>=2, their degrees exceed two, and A=B=0. Thus every cubic through R belongs to I_L^2.

In particular F,G would lie in I_L^2. At the generic point of L, the ambient local ring is regular of dimension two and their ideal lies in the square of its maximal ideal. Its quotient then has length at least three, from its constant and two independent linear classes. On the other hand D is an integral degree-seven curve distinct from L, so localization of the residual equality gives I_R=I_Y there. The quotient must have length exactly two, the generic multiplicity of R. This contradiction excludes c>=2.

Hence c=0 or 1, giving p_a(D)=4 or 3 respectively. No assertion that either ribbon actually occurs in the HM family is made.

As an additional cohomological consequence, the deficiency dimensions h1(I_D(n)) for n=1,2,3 are (0,1,0) in genus four and (1,2,1) in genus three. This follows from Riemann–Roch, H1(O_D(n))=0 for n>=1, no equations of degrees one/two, and exactly two cubic equations. Both alternatives are non-ACM.

## 5. Degree eight: the linked-line ACM octic

Here R is a degree-one locally Cohen–Macaulay curve, hence a reduced line. It has p_a(R)=0 and t=0, so p_a(D)=7. Write I_R=(ell_1,ell_2) and

F=ell_1*a+ell_2*b, G=ell_1*c+ell_2*d,

where a,b,c,d are quadrics. The standard residual computation gives

I_D=(F,G,a*d-b*c).

Its two syzygies have total degree five: (d,-b,-ell_1) and (-c,a,-ell_2). The Hilbert–Burch resolution is

0 -> 2O(-5) -> 2O(-3) directsum O(-4) -> I_D -> 0.

Thus D is ACM with h-vector (1,2,3,2), degree eight and arithmetic genus seven. This explicit computation does not presume the original complete intersection reduced.

## 6. Degree nine: no residual scheme remains

If d=9, the complete intersection Y has only D as a component and generic multiplicity one, since their degrees agree. Its Cohen–Macaulay property forbids embedded associated components. Therefore Y is reduced and equals D scheme-theoretically. It is the integral complete intersection (3,3), of arithmetic genus ten, with its usual two-cubic Koszul resolution.

## Boundaries and provenance

Current PR1 was read through comment 6313247316 before this deduction. The marked-label and component arguments are the degree-nine versions of those in THREE-CUBIC-SEXTIC-HEPTIC-DICHOTOMY.md at 435a20fc680c7ccecc3cbfd762a3d5ae97b76299; the residual cohomology is recomputed for two, not three, cubics. The new c<=1 restriction uses cubic normal coefficients and generic linkage multiplicity, not reducedness or a selected matrix evaluation.

No selected coefficient, rank, scan, local-model restart, one-shot experiment, or external write was made. The surviving heptic/octic/nonic configurations are not excluded by this note, and no complete Q4 conclusion is claimed.
