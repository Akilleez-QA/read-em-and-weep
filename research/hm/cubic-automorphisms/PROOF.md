# Recovering the blowdown and the full polarized automorphism group

Status: authored mathematical proof; independently reviewed. Not formally machine-checked. Work over C. No selected HM/source coefficient, point, derivative, matrix, or numerical rank is evaluated. The Fourier identities below are universal identities for the order-five character table.

## 1. Inputs and result

Pinned dependencies in Akilleez-QA/read-em-and-weep:

- PR611, 12b28d33627cc0e8b283d142dc16439a51bb5e00, research/hm/cubic-branch-transversality/PROOF.md: the canonical cubic image V=V_51 in P9 has normalization nu:M->V, where M=Bl_Z P4 and Z is the thirty reduced Heisenberg eigenlines. The polarization pulls back to D=3H-E, with E the sum of the thirty exceptional divisors. The conductor consists of sixty reduced double values, with 120 reduced preimages in M.
- PR610, e4898406ed2552dd40e9695f9fda3d9f1d270301, research/hm/cubic-joint-characters/PROOF.md: for each eigenline pentad, its twenty exceptional marks (i,j), i!=j in F5, pair by (i,j)<->(2i-j,3i-2j). These are all the conductor pairs.
- PR615, 24bc9b741c287f8ac207bd9df4de4c07c50bea2f, research/hm/cubic-polarized-deformations/PROOF.md: H0(V,O_V(1)) is the complete ten-dimensional cubic section space S defining V.
- PR617, 7f240b04bc4f03cfe73ffd64cae17c453dd895e6, research/hm/cubic-scalar-constraints/PROOF.md, Section6: for U=F5^2 acting projectively in its five-dimensional irreducible Heisenberg representation, its full projective normalizer Gamma has order3000 and exact sequence 1->U->Gamma->SL2(F5)->1. The six pentads are indexed by the six directions in U.

- PR622, c6a7c691f8ecd8562505546f993c755fb03b24fb, research/hm/cubic-embedded-rigidity/PROOF.md: the PGL10 orbit of [V] is open in its Hilbert component, and the Hilbert germ at [V] is smooth of dimension99. This dependency is used only in Section6.

We prove

    Aut(V,O_V(1)) = Stab_(PGL5)(Z) = Gamma.                 (1)

The first equality is a canonical identification through the recovered blowdown. The second is a new classification of the full configuration stabilizer, not an assumption that a transformation preserving Z already normalizes U. In particular the full polarized automorphism group has order3000.

The embedding of V by its complete section space identifies this group with its projective stabilizer in PGL10. This result does not classify automorphisms that change the polarization, or automorphisms of the other HM surfaces.

## 2. Intrinsic recovery of the original hyperplane bundle

On the blowup of a smooth fourfold at reduced points,

    K_M = -5H+3E,      D=3H-E,

and therefore

    K_M+3D=4H.                                           (2)

The exceptional coefficient3 can also be read directly in a blowup chart: writing four affine coordinates as t,t a_2,t a_3,t a_4 gives Jacobian factor t^3. All thirty centers are disjoint, so these contributions add.

The Picard group of M is free on H and the thirty exceptional classes E_z. Indeed a line bundle away from the exceptional divisors corresponds to a line bundle on P4 minus finitely many points, which extends uniquely as a divisor class on smooth P4. Subtract its multiple of H; the remaining divisor class is supported on the exceptional divisors. Independence follows by restricting to a line in each E_z=P3, where H and the other exceptional classes restrict trivially while E_z restricts as O(-1), and then restricting a relation with all exceptional coefficients zero to a line avoiding Z. In particular Pic(M) has no torsion.

Every polarized automorphism f of V lifts uniquely to an automorphism f_tilde of its normalization M. It preserves D=nu*O_V(1) and the canonical class. By (2), it preserves 4H. Torsion-freeness then forces it to preserve H itself. Thus H is intrinsically the unique fourth root of K_M+3D in Pic(M).

The complete system |H| recovers the original morphism pi:M->P4. Explicitly pi_*O_M=O_P4 and projection formula identify H0(M,H) with H0(P4,O(1)); hence |H| is the original blowdown. Its positive-dimensional fibers are exactly the thirty E_z. It follows that f_tilde permutes these divisors and descends to a projective transformation a of P4 preserving Z.

Conversely, every a in Stab_(PGL5)(Z) lifts to M, preserves D and acts on its complete cubic section space. The cubic morphism is equivariant for this action, so a induces a polarized automorphism of its scheme-theoretic image V. These constructions are inverse: they agree on the dense open where the birational maps are isomorphisms. This proves the first equality in (1).

Finally every polarized automorphism of V induces a projective transformation of P(H0(V,O_V(1))*), because the section space is complete. Conversely a projective transformation stabilizing V restricts to one. This restriction is faithful: V is integral and nondegenerate, and a projective transformation fixing it pointwise would have V contained in a single projectivized eigenspace of a linear lift, forcing that lift to be scalar. Thus the identification with the PGL10 stabilizer is exact.

## 3. The conductor intrinsically recovers the six pentads

Form a graph whose vertices are the thirty exceptional divisors recovered by |H|. For each conductor value, put an edge between the two divisors containing its two normalization preimages. These divisors are distinct by the pinned pairing formula.

Within one pentad, the paired mark (i,j) has its other branch based at k=2i-j. Conversely every unordered pair {i,k}, i!=k, arises uniquely from the two marks (i,2i-k) and (k,2k-i). Consequently that pentad contributes exactly its ten edges, the complete graph K5. There are no edges between different pentads and no further conductor pairs. The full graph is therefore the disjoint union of six copies of K5.

Normalization and conductor are intrinsic, and the divisors were recovered from the polarization. Every polarized automorphism preserves this graph, so it permutes its six connected components. Through Section2, every projective transformation preserving Z therefore permutes the six eigenline pentads. This conclusion is not inferred merely from the cardinality30 or from an abstract permutation of points.

## 4. A universal two-eigenbasis rigidity lemma

Let e_i, i in F5, be an eigenbasis for one Heisenberg direction. An independent direction has an eigenbasis whose lines, after rescaling and relabeling, are the Fourier lines

    f_j = sum_(i in F5) zeta^(ij) e_i,    j in F5.

To see this without choosing actual eigenvector coordinates, choose lifts g,s with g s=zeta s g. Cycling a g-eigenvector by s gives the basis e_i; diagonalizing this cyclic shift gives exactly the displayed universal character sums. Any original choice only changes nonzero scales and labels.

Suppose a projective transformation preserves each of these two pentads setwise. A linear lift T has

    T e_i=d_i e_(pi(i)),       T f_j=c_j f_(tau(j)),

for permutations pi,tau of F5 and nonzero complex d_i,c_j. Comparing the coefficient of e_(pi(i)) gives

    d_i zeta^(ij)=c_j zeta^(pi(i) tau(j)).                  (3)

Divide (3) by its instance at j=0, then divide the resulting identity by its instance at i=0. The nonzero scalars cancel, leaving

    zeta^(ij)=zeta^((pi(i)-pi(0))(tau(j)-tau(0))).           (4)

Since zeta is primitive, the exponents agree in F5. Put a=pi(1)-pi(0), which is nonzero. Taking i=1 in (4) gives tau(j)-tau(0)=a^(-1)j. Then taking j=1 gives pi(i)-pi(0)=a i. Finally the j=0 instance of (3) gives

    pi(i)=a i+b,       tau(j)=a^(-1)j+c,
    d_i=c_0 zeta^((a i+b)c).                              (5)

Thus T is, up to scalar, a product of a Heisenberg diagonal character, a Heisenberg cyclic translation, and the index dilation e_i->e_(a i). Each normalizes U. Therefore every projective transformation preserving these two pentads belongs to Gamma. The calculation also shows the ordered-pair stabilizer has exactly25*4=100 elements.

No value of a cubic map, derivative, or source coefficient occurs here. Equations(3)–(5) prove a universal rigidity property of a Fourier pair for arbitrary nonzero scalars.

## 5. Full automorphism classification

Gamma acts transitively on ordered pairs of distinct directions in U. Indeed SL2(F5) does: choose nonzero vectors on the two source lines and scale one to give determinant1; do the same for the target lines, then map the resulting determinant-one bases. Hence it is transitive on ordered pairs of distinct pentads.

Let a be any projective transformation preserving Z. By Section3 it permutes the six pentads. Fix an ordered pair of distinct pentads. Compose a on the left with an element of Gamma sending its image pair back to the fixed pair. The composite preserves each of these two pentads, and Section4 puts it in Gamma. Therefore a itself belongs to Gamma.

Conversely Gamma preserves U and its eigenlines, so it preserves Z. This proves the second equality in (1). In particular there are no additional complex-linear projective symmetries of the canonical cubic image beyond the full Heisenberg normalizer.

As an intrinsic consequence, U is normal in the recovered full automorphism group, and the six pentads and thirty exceptional divisors are recovered without retaining the original coordinates. The group acts transitively on the thirty divisors: its quotient is transitive on directions and U is transitive on each pentad. The stabilizer of any divisor consequently has order100.

## 6. The open Hilbert orbit has an explicit finite cover

Use PR622 only for this consequence. Write G=PGL10 and let O=G.[V] be the open Hilbert orbit. Its scheme-theoretic stabilizer is the projective stabilizer classified above. In characteristic zero an algebraic group scheme of finite type is smooth; alternatively PR622 gives zero stabilizer Lie algebra directly, so its finite stabilizer is reduced. It is therefore the constant finite group Gamma of order3000.

The orbit is the homogeneous space

    O = PGL10/Gamma.

The right action of Gamma on PGL10 is free. The quotient map is a Gamma-torsor for the étale topology, hence a finite étale map of degree3000. It follows that the smooth99-dimensional open Hilbert orbit has this explicit finite étale homogeneous cover. This identifies the finite ambiguity in moving the embedded model by projective coordinates: any two transformations carrying V to the same embedded image differ by exactly an element of Gamma.

This assertion is confined to the open orbit. It does not assert that the entire Hilbert component is homogeneous, that the orbit is closed, or that its boundary is smooth.

## 7. Boundary

The theorem concerns the polarized canonical cubic image V_51. It does not classify all unpolarized automorphisms, all abstract deformations, the degree75 surface, or the original full-adjoint/source/algebraicity problem. It is independent of any numerical obstruction calculation and does not identify a Galois-semilinear symmetry with a complex-linear automorphism. The latter distinction is essential: only the complex-linear normalizer Gamma occurs in (1).
