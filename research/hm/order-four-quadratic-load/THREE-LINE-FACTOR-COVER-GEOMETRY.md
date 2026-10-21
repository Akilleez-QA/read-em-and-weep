# The actual determinant family has a genus-four line-factor cover

## Result

Let T=P(W*) be the actual negative parameter line, and let

    c:T -> P(Sym^3 V*)

be the HM determinant family. The established family theorem identifies c with a rational normal sextic, with c*O(1)=O_T(6). The checked Bănică–Manolache application proves that a general c_t is a product of three distinct lines. Let B be the normalization of the irreducible line-factor incidence, with maps

    pi:B -> T,       f:B -> P(V*),       deg(pi)=3.

Write L=f*O(1). Then:

1. Nm_pi(L)=O_T(6), so deg L=6.
2. B has genus exactly four. The line-factor image is either the invariant conic, covered with degree three, or an integral invariant sextic whose only singularities are six ordinary nodes at the six order-five axis points.
3. The canonical model of B is a smooth A5-invariant (3,3) curve in P(W*) x P(W'^*), where Sym^2 W'=V and W' is the other binary two-space. Its equation spans the unique invariant line in bidegree (3,3).
4. If M,N are the two ruling pencils, with M=pi*O_T(1), then K_B=M tensor N and tau=M tensor N^{-1} has exact order five. In additive notation, L=K_B-tau in the conic case, and L=K_B+2tau or K_B-2tau in the sextic case. The group of degree-zero A5-linearized line bundles is cyclic of order five.
5. The actual direct image is pi_*L=V tensor O_T. Consequently the line-factor incidence itself is smooth and isomorphic to B, every length-three fiber embeds in the dual plane, and no two distinct points of a fiber have the same line factor.
6. There are exactly twelve nonreduced determinant cubics. They occur at the twelve order-five fixed parameters; each is a doubled line times a different line. Every other member is three distinct lines. In particular, there are no triple-line members in this alternative.

These statements apply to the actual determinant family: the reduced-determinant classification excludes the formerly open generic irreducible alternative. They do not determine the vertex-evaluation scalar or the remaining adjoint obstruction maps.

## 1. Established actual inputs

The following source artifacts supply the actual inputs:

- DETERMINANT-CUBIC-FAMILY-RATIONAL-SEXTIC.md: the determinant family is everywhere nonzero, is a rational normal sextic, and has its actual polarization O_T(6). Its representation span is V directsum 4. The genuine A5 three-spaces V and A=Sym^2 W are distinct.
- [REDUCED-DETERMINANT-THREE-CONIC-PENCIL.md, checked pin35fc96](https://github.com/Akilleez-QA/read-em-and-weep/blob/35fc96bebf9c771a4de481c753bb527e510cd8c1/research/hm/order-four-quadratic-load/REDUCED-DETERMINANT-THREE-CONIC-PENCIL.md): the Bănică–Manolache classification applies to each actual hyperplane restriction with reduced determinant; it forces three distinct planes and a general section consisting of three disjoint reduced plane conics. Together with the established generic-reduced dichotomy, this proves the actual generic three-line alternative and excludes the irreducible one.
- DETERMINANT-CUBIC-FACTORIZATION-DICHOTOMY.md: the three-line factor cover is irreducible of degree three; the A5 action lifts to B; and g(B)>=4. There is no equivariantly distinguished line factor.

The representation facts used below are the universal binary-icosahedral decompositions already used in those artifacts: Sym^2 W'=V, W tensor W'=4, and Sym^3 W=Sym^3 W'=the irreducible binary four-space. The only nontrivial genuine irreducible representations of A5 of dimension at most four have dimensions three, three, and four. No actual HM coefficients or evaluated actual matrices enter.

All curves are over C. A5 actions on curves and line bundles mean the actual actions induced from the determinant incidence. G=2.A5 is used when a ruling O(1) needs its binary linearization.

## 2. The norm is the determinant-family polarization

The finite map pi from a smooth irreducible curve to the smooth curve T is flat. A length-three fiber, counted with its scheme-theoretic multiplicities, gives the specialization of the three generic line factors. The product of these factors is therefore c_t, also at ramified fibers.

Here is a line-bundle justification that does not discard ramification. The tautological linear equation on B x P(V) is a section of

    L external-tensor O_P(V)(1).

Take its norm along pi x id. This is a section of

    Nm_pi(L) external-tensor O_P(V)(3).

At every t it is a nonzero cubic: over a finite length-three algebra its norm is the product of the three residue linear forms, each with the corresponding length multiplicity. Thus it gives a base-point-free coefficient map T -> P(Sym^3 V*) with pullback O(1)=Nm_pi(L). This map equals c on the generic point, hence everywhere. Consequently

    Nm_pi(L)=O_T(6).                                      (1)

For a finite map of smooth projective curves, the norm of O_B(D) is O_T(pi_*D); hence degree is preserved by norm, not multiplied by deg(pi). Equation (1) gives deg L=6.

Let Gamma=f(B), of plane degree d, and let e be the degree of B -> Gamma. The map is nonconstant: otherwise the factor incidence would contain a single fixed line, contrary to irreducibility of V. Then

    e d=6.                                               (2)

Gamma is integral and A5-invariant. It cannot be a line, since V is irreducible. It cannot be a cubic: an invariant cubic equation would be an invariant line in Sym^3 V*, but that space is V directsum A directsum 4 and has no invariant line. Thus d=2 or 6. In degree two, the invariant equation is the unique nondegenerate quadratic; in degree six, e=1.

## 3. Both image cases force genus four

### 3.1. Conic image

If Gamma is the invariant conic, identify it with P1. The map (pi,f) is birational onto its image by the definition of B as the normalization of the factor incidence. Both projections have degree three. Its image is therefore an integral (3,3) divisor on P1 x P1, of arithmetic genus four.

Since g(B)>=4, the normalization genus equals the arithmetic genus. The image has no singularities, and (pi,f) identifies B with that smooth (3,3) curve. In particular g(B)=4.

### 3.2. Sextic image

If Gamma is a sextic, f is its normalization, so g(B)<=10. The ramification divisor of pi has degree 2g(B)+4. Its pushforward is a nonzero A5-invariant effective divisor on T. The possible icosahedral orbit sizes are 12,20,30,60. Between degrees 12 and24 the only possible invariant divisor degrees are 12,20,24. Therefore

    g(B) is 4, 8, or 10.                                (3)

Genus eight would make the total delta invariant of the plane sextic equal to two. Its singular points would form an invariant set of at most two points, impossible for the irreducible plane action. Thus g(B) is not eight.

Genus ten would make Gamma a smooth plane sextic. Projection from any of its points is a degree-five morphism B -> P1. Together with pi of degree three, it defines a birational map to P1 x P1: the degree of the joint map divides both three and five. The image would have bidegrees three and five and arithmetic genus eight. Its normalization cannot have genus ten. Thus g(B) is not ten either, proving g(B)=4.

### 3.3. The sextic has exactly six ordinary nodes

For completeness, the minimum size of an orbit in P(V*) is six, and its unique orbit of size six is the axis orbit. Simplicity of A5 excludes a nontrivial action on fewer than five points. An orbit of size five would have stabilizer A4; the restriction of V to A4 is irreducible, since its Klein four subgroup has three distinct nontrivial eigencharacters permuted transitively by an element of order three. Hence A4 fixes no projective point. A stabilizer of index six is the dihedral normalizer of an order-five subgroup. Among the three eigenlines of that subgroup, only its axis is fixed by this normalizer; the other two are exchanged. This gives the six-axis orbit.

The sextic has total delta=10-4=6. Its singular locus must therefore be exactly the six-axis orbit, with delta one at each point. A reduced plane singularity of delta one is a node or a cusp. At an axis, the order-five action on the tangent plane has eigencharacters zeta^a,zeta^{-a}, with a nonzero modulo five. The sextic equation is invariant and its fiber character at the axis is trivial. Its quadratic initial form must consequently be a multiple of xy. A cusp would instead have a rank-one quadratic initial form. Hence all six singularities are ordinary nodes.

## 4. The canonical cover and its two ruling pencils

The curve B is not hyperelliptic. A degree-two map together with pi would give a birational (2,3) curve in P1 x P1, whose genus is at most two.

The quotient B/A5 has genus zero. Indeed Riemann-Hurwitz for a faithful A5 action on a genus-four curve would give, for quotient genus at least one, either a negative ramification requirement or ramification degree six. Every nonzero ramification orbit contributes at least thirty, so the latter is impossible. Thus H0(K_B) has no invariant vectors. Its dimension is four, forcing the genuine irreducible four-space.

The canonical image in P3 has degree six. At least one quadric contains it because h0(2K_B)=9<10. Two independent quadrics cannot contain an integral nondegenerate degree-six curve, so that quadric is unique. Its defining quadratic form is invariant. Its radical is an invariant subspace of the irreducible four-space, so the quadric is nondegenerate and therefore smooth. The canonical curve has bidegree (3,3) on it.

Every degree-three pencil on B gives lines in its canonical model. Indeed its fiber D has h0(D)=2 and h0(K_B-D)=2, so its canonical span is a line. That line lies in the canonical quadric, because the quadric contains a length-three intersection with it. Thus pi is one of the two rulings. Write their line bundles as M,N, with M=pi*O_T(1). Adjunction gives

    K_B=M tensor N.                                    (4)

A5 preserves the two rulings, since it has no nontrivial homomorphism to S2. The second ruling is the other icosahedral projective line: the canonical four-space is W tensor W', whereas W tensor W=1 directsum A is reducible. Thus the canonical quadric is P(W*) x P(W'^*).

The equation of B spans an invariant line in bidegree (3,3). Since both binary cubic spaces are the same irreducible four-space, that invariant line is unique. This identifies the canonical cover intrinsically; it is not an assertion about a chosen equation.

## 5. Exact fifth torsion and the possible polarizations

Each ruling has degree three. Its branch divisor has degree twelve, hence is exactly the twelve-point orbit on its parameter line, with multiplicity one. Its ramification points are simple. Let R_M,R_N be the respective ramification divisors, each of degree twelve. They are disjoint because B is smoothly embedded in the product: both projection differentials cannot vanish at the same point. Riemann-Hurwitz gives

    R_M=K_B+2M,           R_N=K_B+2N.                   (5)

The twelve order-five parameter points pull back under pi to

    12M=2R_M+R_N.                                      (6)

To justify the unramified part of (6), an order-five subgroup fixes each point of a degree-three invariant fiber, since it cannot permute three points nontrivially. The two twelve-point ramification orbits exhaust the order-five fixed points on B. Equations (4)-(6) imply

    5(M-N)=0.

The two pencils are not isomorphic, for otherwise their product map would have graph image rather than a (3,3) image. Thus

    tau=M-N has exact order five.                      (7)

Here M and N individually have center-odd G-linearizations; their ratio tau has a genuine A5-linearization.

We record why there are no other degree-zero A5-linearized possibilities. Riemann-Hurwitz for B -> B/A5 gives the quotient signature (2,5,5): if n_j counts quotient branch points of inertia order j, then

    15 n_2 + 20 n_3 + 24 n_5=63,

whose unique nonnegative solution is (1,0,2). Let D_2,D_5,D'_5 be the three ramification orbits, of degrees 30,12,12, and F a quotient fiber of degree60. Equivariant divisor classes have the presentation

    2D_2=5D_5=5D'_5=F.                                (8)

For justification, an A5-linearized line bundle has a nonzero invariant rational section by descent/Hilbert 90 at the generic point, so it is represented by an invariant divisor. Away from the three branch orbits every invariant prime divisor is a quotient fiber. Any invariant principal divisor comes from an invariant rational function, because A5 has no characters. This gives precisely (8). Its degree-zero subgroup is cyclic of order five, generated by D_5-D'_5. Hence tau in (7) generates the same subgroup.

In the conic-image case, f is the second ruling, since (pi,f) is the smooth (3,3) incidence. The plane conic polarization is its O_P1(2), so

    L=2N=K_B-tau.                                     (9)

In the sextic-image case, the twelve preimages of its six nodes form one A5 orbit, hence are R_M or R_N. Indeed, the dihedral order-ten stabilizer of an axis exchanges its two nontrivial tangent eigenlines, which are exactly the two node branches; transitivity on the six axes therefore gives transitivity on all twelve preimages. Plane adjunction on the normalization gives

    K_B=3L-R_M  or  K_B=3L-R_N.                        (10)

Thus 3(L-K_B)=tau or -tau. The degree-zero class L-K_B is genuinely A5-linearized, so belongs to the order-five group just proved. Inverting three modulo five gives

    L=K_B+2tau  or  L=K_B-2tau.                        (11)

No choice between the two signs in (11), or between the conic and sextic alternatives, is made here.

## 6. The factor polarization has trivial direct image

The three pulled-back plane coordinates inject V into H0(B,L). The line bundle L is not K_B: otherwise this would inject the irreducible three-space V into the irreducible canonical four-space. Since deg L=deg K_B=6, Riemann-Roch gives

    h0(L)=3,            h1(L)=0,            H0(L)=V.   (12)

The rank-three bundle E=pi_*L has degree zero, by Euler characteristic. Write its Birkhoff-Grothendieck splitting in decreasing order. Degree zero and h0(E)=3 allow exactly

    (0,0,0),       (1,0,-1),       (2,-1,-1).          (13)

The first positive Harder-Narasimhan piece in (1,0,-1) supplies a two-dimensional G-stable subspace of H0(E)=V, a contradiction. In the last case all global sections come from the unique O_T(2) piece. G is perfect, so the induced linearization on that line bundle is the standard one; its section representation is Sym^2 W=A, not V. The last case is therefore impossible too. It follows that

    pi_*L=V tensor O_T                                (14)

equivariantly, with the evaluation isomorphism furnishing the canonical trivialization.

Base change for the finite flat map shows that the three plane coordinates are the complete section space on every length-three fiber. This embeds that fiber in the dual plane, including its nonreduced structure. One can see this directly by choosing a section nonzero at all support points: after trivializing by it, the other two sections together with 1 span the fiber algebra and hence generate it as an algebra. The same argument over a neighborhood of the base point proves that (pi,f) is a closed immersion. Its image, the original factor incidence, is consequently smooth and already normalized. Moreover, no nonzero linear equation vanishes on a fiber, because its three coordinate sections are a basis of H0(L|fiber). Thus every length-three fiber spans the whole dual plane. At an unramified fiber the three line equations are linearly independent: the three base lines are nonconcurrent, and the corresponding three planes in the hyperplane share only their vertex, not a line.

## 7. Exact nonreduced members of the actual family

Because g(B)=4, pi has precisely twelve simple branch points. They form the unique twelve-point orbit on T, namely the order-five fixed parameters. An unramified fiber has three distinct points, and (14) makes their three line factors distinct. A ramified fiber has lengths 2+1 at two distinct points; the complete fiber embedding keeps their images distinct. Its norm cubic is therefore a doubled line times a different line.

Thus there are exactly twelve nonreduced members, all of type 2+1, and every remaining member is three distinct lines. This conclusion uses the actual representation distinction A!=V in (14); genus and norm degree alone would not prevent distinct factor points from colliding in the dual plane.

## Boundaries

The use of generic three-line factorization is discharged by the checked Bănică–Manolache application in Section 1, not by an unproved generic-moduli transfer. The argument does not prove that the vertex evaluation is nonzero, does not identify the actual sign in (11), and does not prove any remaining full-adjoint vanishing. The verifier checks only the universal genus, orbit, splitting and torsion arithmetic used above.

The separate NONZERO-VERTEX-EVALUATION.md theorem at c779b2919a36b9d45a6319d46551bd6380154bba resolves the vertex scalar without changing the factor-cover conclusions here.
