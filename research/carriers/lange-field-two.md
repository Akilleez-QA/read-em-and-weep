# A field-2 rank-two seed and the transverse deformation gap

Let V be Lange's stable rank-two bundle on Y=P1 x P3. Write u,v for the two hyperplane classes. The cited construction has c1(V)=2u+4v, c2(V)=8uv+6v². Set F=V(-1,-2). Then det F=O and c2(F)=4uv+2v²=2(u+v)², since u²=0.

Let X=C x B with principal product polarization theta=alpha+beta, dim C=1, dim B=3. For m>=3, use generating pairs/four-tuples of sections of m alpha/m beta to obtain finite a:C->P1 and b:B->P3. Existence follows by general linear projection of the very ample systems; finiteness follows from ampleness of the pullback of O(1). E=(a x b)*F is stable: Y is simply connected, the finite map is genuinely ramified, and stable pullback applies. Its determinant is trivial, c2(E)=2m²theta², ch(E)=exp(m sqrt(-2)theta)+exp(-m sqrt(-2)theta). Its Euler characteristics are chi(E)=8m^4 and chi(End E)=128m^4.

This proves existence of a stable bundle with the desired squareclass 2. It proves neither the weak first-order kernel condition nor any higher ambient lift. The factorwise relative construction covers the 7-dimensional polarized product locus A1 x A3, whereas A4 has dimension 10. The three mixed tangent directions remain to be tested.

Sources checked directly:
- https://arxiv.org/pdf/alg-geom/9506021 , section3, Proposition3.1, Chern classes (2),(3).
- https://arxiv.org/html/2203.03246 , Definition2.1, Theorem2.5, pullback polarization convention.

Public mathematical capsule: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6093712738

## Discriminating next test
At a product period matrix, polarized tangent vectors are symmetric 4x4 matrices. The factorwise locus is block diagonal 1+3 (dimension1+6). Choose the three symmetric off-diagonal matrices K_1j, j=2,3,4. For each compute contraction K_1j with At(E) in Ext²(E,E), with determinant fixed. Vanishing is required for the missing commutative polarized directions. The Chern character stays Hodge in these directions, so semiregularity cannot establish that the Ext² class vanishes. Conversely, failure of the factor maps to extend does not itself prove that E fails to extend.

## First-order reduction to three explicit classes
Use the HKR convention ev(eta,kappa,pi)=eta Id+kappa contraction A+(1/2) pi contraction A², with A the normalized Atiyah class. Choose a determinant-compatible Chern connection, so its curvature matrix is trace-free. A matrix of trace-free 2x2 matrices with even-degree form coefficients obeys A²=(tr A²/2)Id. Hence A²=-c2(E) Id in cohomology. If Pi=(pi contraction theta²)/2 and c2=d theta², then ev(d Pi,0,pi)=0. This proves six compensated Poisson directions for any such rank-two bundle; it is not an all-order statement.

The relative product construction proves seven polarized commutative directions. Thus at least thirteen independent directions in the 16-dimensional Chern-character annihilator evaluate to zero. The only missing directions are the three symmetric mixed kappa directions. Since ker ev is contained in the character annihilator by the semiregularity comparison, the full weak condition is equivalent to vanishing of these three Ext² classes. An exact exterior-algebra check in verify_lange_kernel.py confirms character-action rank12, annihilator dimension16 and the 13+3 decomposition. This does not compute any of the three Ext² classes.

## Smaller explicit seed
The m>=3 construction has an explicit m=2 instance on X=C^4 for an elliptic curve C with degree-two map x:C->P1. On the last three factors compose x^3 with Sym^3(P1)=P3. The first factor uses x. This map f:X->P1 x P3 has degree2*(2^3*3!)=96 and pulls O(1,1) back to 2theta. Therefore E=f*F has c2=8theta², chi(E)=128, chi(End E)=2048. It is stable by the same genuine-ramification theorem. The numerical identity gives ext²=2046+2ext¹>=2062 (using the four translation and four Picard directions). The symmetric-product presentation is special, but the general m=2 product construction continues locally in the 7-dimensional product-polarized family: the line bundles 2alpha and 2beta are globally generated and have no higher cohomology, so chosen generating sections extend locally.

## Analytic kernel calculation
The character is 2-d theta²+(d²/12)theta⁴. The (0,2) component of its HH² action is 2eta-2dPi, forcing eta=dPi. The (1,3) component of the kappa action is -2d theta wedge (kappa contraction theta). Multiplication by theta from H^{0,2} to H^{1,3} is injective by hard Lefschetz, so this forces kappa contraction theta=0. These two conditions suffice for all remaining components: contraction by pi sends theta^k to k(k-1)Pi theta^{k-2}, and kappa acts as a derivation. Thus the stated 16-dimensional annihilator is proved for every positive d, not inferred from a single numerical rank.

The semiregularity comparison used for ker(ev) contained in ann(ch) is stated in the proof of Lemma11.3 of [Markman v2](https://arxiv.org/html/2509.23403v2). No surjectivity of ev is asserted.

## Reproduction
Run `python verify_lange_kernel.py` with Python3 and SymPy installed. The exact rational exterior algebra is computed on eight generators, with theta=sum e_i wedge e_{i+4}, i=0,...,3, and d=8. Output: character-action rank12; annihilator dimension16; thirteen independent known directions and three complementary mixed directions. This verifier does not construct Lange transition matrices, compute Ext groups, or evaluate the three mixed Atiyah classes. The stable seed and the thirteen actual vanishing directions use the arguments and primary-source hypotheses above.

## Symmetry reduces the explicit seed to one representative mixed test
For the m=2 seed on C^4 using the same elliptic curve and degree-two map on each factor, the group G=(Z/2)^4 semidirect S3 acts by independent elliptic involutions and permutations of the last three factors. The map f is invariant, so E=f*F carries the canonical G-linearization. Atiyah evaluation is G-equivariant.

Let chi_i denote the sign character of the involution on factor i. This involution acts by -1 on both H0(T_C) and H1(O_C). The symmetric mixed polarized tangent kappa_1j therefore has character chi_1 chi_j. These three characters, j=2,3,4, are distinct. S3 permutes the three classes and their evaluated images. Thus either all three evaluations vanish, or they are all nonzero and lie in distinct character spaces, hence are linearly independent.

Consequently, for this explicit symmetric seed the mixed map has rank either0 or3, never1 or2. The entire HH² evaluation has rank either12 or15, and its kernel dimension is respectively16 or13. Proving vanishing of the single representative kappa_12 contraction At(E) proves the three mixed vanishings; proving it nonzero disproves weak kernel equality for this seed. Neither alternative has been calculated. This representation-theoretic reduction is special to the symmetric seed and is not asserted for arbitrary product maps.
