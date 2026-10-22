# Binary-pencil relation bundles bound generic section quadrics and cubics

## New conclusion

Let C be the 25 disjoint HM lines in P4 and R_d=H1(I_C(d)). Assume the established H0(I_C(d))=0 for d<=4, H2(I_C(d))=0 for d>=-1, and the six-dimensional saturated quintic ideal, whose six sections generate I_C(5) as a sheaf. Then for a general proper hyperplane H, Z=C∩H satisfies

    a=h0(I_(Z,H)(2)) <= 3,
    b=h0(I_(Z,H)(3)) <= 7.

These are upper bounds, not vanishing assertions. They do not prove injectivity of a generic quadratic R1→R3. The new input beyond the earlier plane-cubic trace criterion is a low-degree binary relation presentation with no syzygies through degree four, followed by determinant-degree bounds on its relation bundles.

No selected HM/source matrices, coefficients, planes, ranks, or parameter experiments are used.

## 1. Binary generation and low-degree Koszul homology

Choose any plane P avoiding C, cut out by independent linear forms x,y. Put B=C[x,y]. Because P misses C, I_C restricted to P is O_P and the Koszul restriction complex is exact:

    0→I_C(d-2)→I_C(d-1)^2→I_C(d)→O_P(d)→0.

This can also be checked locally: near P the ideal I_C is O, and away from P one of x,y is a unit. Split at J_d=I_P I_C(d)=I_(P union C)(d). The second short exact sequence is

    0→J_d→I_C(d)→O_P(d)→0.

For 1<=d<=4, H0(I_C(d))=0 and H1(O_P(d))=0 give

    0→H0(O_P(d))→H1(J_d)→R_d→0.

The first short exact sequence, using H2(I_C(d-2))=0, gives

    R_(d-2)→R_(d-1)^2→H1(J_d)→0.

Consequently the last map in the binary Koszul complex

    R_(d-2) --(-y,x)→ R_(d-1)^2 --(x,y)→ R_d

is onto, and its middle homology is H0(O_P(d)), of dimension binom(d+2,2). This proves generation from R0 through the degrees used below. In fact the same surjectivity proves binary generation in all nonnegative degrees, since H1(O_P(d))=0 and the stated H2 vanishing persist; nonzero H0(I_C(d)) at higher degrees only changes middle homology.

The first map is injective for d<=4: its kernel is the image of H0(J_d), and H0(J_d) is a subspace of H0(I_C(d))=0. Negative R degrees are zero for this union of lines. Thus

    Tor_2^B(R,C)_d=0 for d<=4,
    dim Tor_1^B(R,C)_d=binom(d+2,2) for d=1,2,3,4.

Equivalently there are no common x,y annihilators in R0,R1,R2. This differs from the primary argument: here the absence of low global ideal equations supplies the condition for every avoiding plane, with no section-plane incidence needed.

Using R0=24, R1=45, R2=60, R3=65 gives minimal relation counts 3,6,10 in degrees 1,2,3. In particular R2 is 60, not 55.

## 2. Truncated relation bundles

Choose minimal homogeneous generators of the binary relation module of the surjection

    B tensor R0 → R.

Through degree three the free relation modules are

    F2 = 3B(-1) directsum 6B(-2),
    F3 = F2 directsum 10B(-3).

Their sheaf maps on P1=P(span(x,y)^*) are

    phi2: 3O(-1) directsum 6O(-2) → 24O,
    phi3: 3O(-1) directsum 6O(-2) directsum 10O(-3) → 24O.

Neither map is assumed injective. Write K2,K3 for their kernel bundles and E2,E3 for their image sheaves. On the smooth curve P1 the images and kernels are locally free, giving short exact sequences 0→Ki→Fi→Ei→0.

There are no polynomial syzygies among these minimal relations of total degree <=4: such a syzygy would be an element of the second syzygy module, whose minimal generators in these degrees are excluded by the Tor_2 vanishing. Consequently H0(Ki(4))=0. By splitting bundles on P1, every summand of Ki has degree at most -5.

## 3. Generic ranks and the degree inequalities

For a general pencil member ell, set

    a=dim ker(ell:R1→R2),
    b=dim ker(ell:R2→R3).

The ideal restriction sequence identifies these with the quadric and cubic ideal-section dimensions of Z=C∩V(ell), since all global ideal spaces in the relevant degrees vanish.

Choose a second pencil coordinate nonzero at p=V(ell) in P1. Modulo ell, the binary presentation identifies the cokernel of evaluation of phi_d at p with (R/ell R)_d. Hence

    rank(phi2)_generic = 24 - (60-45+a) = 9-a,
    rank(phi3)_generic = 24 - (65-60+b) = 19-b.

Thus rank(K2)=a and rank(K3)=b.

Because Ei injects into 24O, deg(Ei)<=0: its determinant has a nonzero map into an exterior power of 24O. The source bundle degrees are -15 and -45, respectively. Since deg(K2)<=-5a and deg(K3)<=-5b, degree additivity gives

    0 >= deg(E2) = -15-deg(K2) >= -15+5a,
    0 >= deg(E3) = -45-deg(K3) >= -45+5b.

Therefore a<=3 and b<=9. Choosing P general ensures the generic pencil member is also a general ambient hyperplane, giving the announced bounds.

### 3.1 The six quintics improve b<=9 to b<=8

In total degree five, the degree-zero ends of the first Koszul short exact sequence still vanish: H0(I_C(3))=H0(I_C(4))=0. Therefore

    Tor_2^B(R,C)_5 = H0(I_(P union C)(5)).

This space has dimension at most six, because I_C(5) has dimension six. Since no lower-degree syzygies exist, all degree-five syzygies are minimal. The syzygies of either truncated relation map form a subspace of this same degree-five space. Thus h0(K3(5))<=6. If b=9, the degree calculation forces K3=9O(-5), giving nine such sections, a contradiction. Hence b<=8. This argument expressly permits nonzero degree-five syzygies; their vanishing is NOT assumed.

The sheaf-generation input gives the stronger bound

    h0(I_(P union C)(5)) <= 3.                          (*)

Indeed the six quintics restrict to a basepoint-free system in H0(O_P(5)), because P misses C. Such a positive-degree system on P2 must have dimension at least three: one section has zeros, and two have a common zero by Bezout (or a common curve). Its kernel inside the six-dimensional space therefore has dimension at most three.

If b=8, write K3 as a sum of O(-e_i), with all e_i>=5. At most three e_i equal five by (*), and sum e_i<=45 by the image-degree bound. The only possibility is

    K3=3O(-5) directsum 5O(-6),    deg(E3)=0.

Thus E3 is a constant rank-eleven subbundle of 24O, and equality must hold in (*): the six global quintics restrict to an exactly three-dimensional basepoint-free system on P. Likewise a=3 forces K2=3O(-5), a constant rank-six image E2, and exactly the same restriction-rank-three condition. These are necessary equality configurations, not contradictions.

### 3.2 Actual Plücker geometry forces quintic restriction rank at least five

The actual four global sections of E=F(3) have rank-two evaluation away from C; their six maximal minors are the six saturated quintics. Thus on any plane P avoiding C there is a surjection 4O_P→E_P and its classifying map

    f:P2→Gr(2,4)⊂P5,    f*O_Gr(1)=O_P(5).

The rank-two universal quotient pulls back to E_P, whose Chern numbers are c1=5 and c2=4+3(-1)+9=10. The map f is finite onto its image because its pulled-back ample line bundle is ample. Let r be the dimension of the span of the six restricted quintics. Their basepoint freeness implies r>=3.

If r=3, the image is the full linear P2 spanned by it, contained in the Grassmannian. The degree of f onto that plane is 25. Pullback of the second Chern class of the universal quotient restricted to that plane would make c2(E_P) divisible by 25, contradicting c2(E_P)=10. No classification of Grassmannian planes is required.

If r=4, the image spans P3. The Plücker quadric is the smooth quadric defined by the nondegenerate wedge pairing on Lambda²(C4); a totally isotropic vector subspace has dimension at most three, so no projective P3 is contained in it. The image is therefore a surface component of its quadratic intersection with this P3. A plane component would contradict the span dimension. The only remaining possibility is an integral degree-two quadric surface, but the degree formula would give 25=2 deg(f), impossible. Consequently

    rank[I_C(5)→H0(O_P(5))]>=5,
    h0(I_(P union C)(5))<=1.                          (**)

This holds for every avoiding plane, and uses the actual evaluation/minor identification, not an arbitrary sheaf with the same Chern classes. All the geometry precedes any selected evaluation.

By (**), at most one summand of K3 is O(-5); every other summand has degree at most -6. For b>=1 this gives deg(K3)<=-6b+1. The source/image degree bound now gives 6b<=46, hence b<=7. Similarly a=3 would require K2=3O(-5), contradicting (**), so the binary argument alone also improves a<=2. The separate symmetry/Bezout argument in RAO-SECTION-QUADRICS.md improves this further to a<=1.

The earlier b<=8 deduction is retained above to isolate exactly what follows from six-dimensional quintic saturation alone; the stronger b<=7 uses the actual four-section Grassmannian map. Neither bound assumes degree-five syzygies vanish.

## 4. What remains unresolved

The earlier exact product criterion remains

    0→A1 directsum A2→ker(ell1 ell2:R1→R3)→T1∩T2→0,

where Ai are the section-quadric systems and Ti the section-cubic traces in the ten-dimensional plane-cubic space. The new bounds do not force Ai=0 or T1∩T2=0. In particular the primary proof with five generators and five quadratic relations cannot be imported: the Rao module has 24 degree-zero generators, three linear relations, six new quadratic relations, and ten new cubic relations. Its truncated relation kernels can have positive rank while respecting the established absence of degree<=4 syzygies.

This is a new upper-bound deduction, not a rebranding of the trace criterion or a proof of generic quadratic residual surjectivity. No claim about squares, the original selected quadratic, full adjoint lifting, Q4 vanishing, or Mr. Slop's derived-excess maps follows.

## Input comparison

Read before deriving: PR543's plane-trace criterion, local source Q4-QUADRATIC-PLANE-TRACES.md. Its dimensions and global ideal vanishings are retained. Only elementary Koszul cohomology, graded minimal resolutions over C[x,y], and bundle splitting on P1 are used after those inputs. No integral-curve uniform-position or disconnected-curve lifting theorem is invoked.

## Exact source pins

- Actual low-degree Rao dimensions and I_C(4)=0: PR543, `f4e61e37e8be9ad32936baa7c69a3433efdc8c2a`, `research/hm/order-four-quadratic-load/PROOF.md`, Sections 1–3.
- Earlier trace criterion: same commit, `research/hm/order-four-quadratic-load/PLANE-TRACE-CRITERION.md`.
- Actual four-section degeneracy construction, Eagon–Northcott minors and the saturated six-dimensional quintic result: PR538 refinement at `3d0b833b1a22680a4ac1ea793fdeec378730de21`, as explicitly cited by PR543's pinned PROOF.md. Here C must be this actual degeneracy locus, not merely an abstract union with matching numbers.
- Normalized F has c1=-1,c2=4, and h0(F(3))=4. These are the primary HM bundle inputs used by the same actual evaluation construction. H2(I_C(d))=0 for d>=-1 also follows immediately from H1(O_C(d))=0 for a disjoint union of lines and intermediate cohomology vanishing of O_P4(d).
