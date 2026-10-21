# Necessary geometry at the no-quadric five-cubic endpoint

Assume the established generic HM section premises, a=0 and b=5. FINITE-CUBIC-BASE-RIGIDITY.md supplies a canonical reduced cubic base curve D containing all 25 section points Z. The existing quintic cut gives deg D>=5 and I_D(2)=0. This note proves that D is an integral quintic and that two independent global E=F(3) sections vanish along D. It does NOT exclude that configuration without a separate family-incidence argument.

## 1. A six-point cubic lemma

Six distinct plane points impose six independent conditions on cubics unless five are collinear. If there are no five collinear, fix a target point p. Partition the other five by the lines they determine with p; each class has size at most three. Two disjoint pairs can be chosen from different classes (a matching of size two in the complete multipartite graph). Their joining lines avoid p. A third line through the remaining point and avoiding p completes a cubic vanishing at the other five but not p. This separates every target point.

Consequently if a set Gamma of at least six distinct points has h_Gamma(3)<=5, all but at most one lie on one line. Indeed some six points have five on a line L. If a point outside L exists, any further outside point, together with four points on L, would form six points with no five collinear. The line L is unique, since it contains at least five points whereas the complement has at most one.

## 2. Passing from generic plane points to curve components

Let D be any reduced curve in P3, with I_D(2)=0 and h0 I_D(3)>=5. For a general linear nonzerodivisor L on its homogeneous coordinate ring R,

    dim R2=10, dim R3<=15,
    h_(D intersect V(L))(3)<=dim(R/LR)3<=5.

If deg D>=6, the preceding lemma puts all but at most one point of its general reduced plane section on a unique line.

This forces D to be contained in a quadric, as follows. Work over the function field of the dual plane parameter space, with D fixed over C. For each irreducible component D_i, the incidence variety of pairs (p,H), p in D_i and p in H, is irreducible: it is a P2-bundle over D_i. Thus the points of its generic plane section form a single Galois orbit. The unique heavy line is defined over the parameter function field, so either all or none of those points lie on it. Components off the line therefore have total degree at most one. The remaining union D' has degree at least five and its general plane section is collinear.

The elementary noncollinearity lemma in NO-QUADRIC-CUBIC-BOUND.md says a reduced nonplanar curve of degree at least five has noncollinear general plane section. Hence D' is planar. D is thus a planar curve together with at most one line, and is contained in the union of that plane and a plane containing the remaining line. This contradicts I_D(2)=0.

Therefore deg D<=5. Applying the earlier lower bound gives deg D=5 at the HM endpoint.

## 3. Integrality and the fixed two-section kernel

Choose a quintic from the six generators avoiding every component of D. Its Cartier intersection with D has length25 and contains the reduced length25 scheme Z; hence it equals Z scheme-theoretically. At a singular point of a reduced curve, a nonzerodivisor Cartier quotient cannot have length one (a one-dimensional local ring with principal maximal ideal is regular). Thus Z avoids singularities and intersections of components of D.

Each component D_i consequently contains exactly 5 deg(D_i) of the 25 points. These subsets give a canonical partition of the section labels. The generic semilinear normalizer action preserves the partition, and transitivity on labels forces equal block sizes, hence equal component degrees. Their degrees sum to the prime number five. Either D is integral or it has five line components. Each line in the latter case would contain five section points, contrary to the established absence of three collinear points. Thus D is integral.

Every one of the six quintics vanishes on Z. On D, divide its restriction by the chosen quintic whose divisor is exactly Z. The quotient is a global regular function on the integral projective curve D, hence a constant. Thus all six restricted minors are proportional.

Outside Z, the actual evaluation U tensor O→E has rank two, and its Plücker coordinates on D are the proportional minors. Its quotient two-plane is therefore constant on D minus Z. The complementary fixed two-dimensional kernel W⊂U consists of actual global sections vanishing on that dense open subset of D. Their restrictions to D vanish everywhere, since E|D is locally free and D is reduced. This gives two independent global E sections vanishing along the integral quintic D.

## Boundary

No generic-plane uniform-position theorem for integral curves was used. Irreducibility of each incidence cover supplies only transitivity of its generic points, exactly what the unique-heavy-line argument needs. No selected coefficients or matrices were evaluated. Excluding the final two-section configuration requires a further geometric argument; this note does not claim b<=4.
