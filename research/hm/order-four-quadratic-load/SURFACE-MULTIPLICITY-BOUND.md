# Surface-cycle restriction for the new contraction quotient

## Inputs and conclusion

Work over C with the standard projective Schrödinger normalizer N = A semidirect SL2(F5), A = F5^2. Assume the contraction quotient T is N-equivariant, supported in codimension at least two, with effective surface cycle

    [T]_2 = sum lambda_i [Y_i],    delta = sum lambda_i deg(Y_i) in {30,40}.

Here lambda_i is the length at the generic point of the integral surface Y_i. No identification with the older residual map Q is made.

Then every lambda_i is at most 3 if delta=30 and at most 4 if delta=40. More precisely, for each positive integer m let W_m be the reduced union of those Y_i with lambda_i >= m. If W_m is nonempty, then

    deg(W_m) >= 10,    m deg(W_m) <= delta.

This is a bound on generic surface multiplicities, not a bound on local lengths at closed points or embedded components.

## Proof

The abstract normalizer results in PR263 and the sectional-genus bridge explicitly restated in PR266 exclude an N-stable integral quintic surface, including nonnormal surfaces. Their hypotheses are the standard complex Schrödinger normalizer, not the original residual map. The bridge gives an integral general hyperplane section whose arithmetic genus is congruent to 1 modulo 5 and lies between 0 and 5; hence its genus is 1, the input to the birational exclusion.

We first show that every nonempty N-invariant reduced surface W has degree at least 10. Suppose deg(W)<=9. An A-orbit of components has size 1, 5, or 25. An orbit of size 25 already costs degree at least 25. For an orbit of size 5 its stabilizer in A is an order-five subgroup. The normalizer moves that subgroup through all six lines in A. The six A-orbits are disjoint, costing at least 30 components and degree at least 30. Thus every component is A-stable.

Each A-stable component has degree divisible by 5: the H5-linearization of its structure sheaf twists gives Hilbert-polynomial values divisible by 5 in each nonzero central-character residue. Taking a second difference at three sufficiently large consecutive twists with residues 1,2,3 proves divisibility of its degree. A total degree at most 9 therefore leaves exactly one integral degree-five component. It is N-stable, contradicting the abstract quintic exclusion.

Equivariance of T preserves generic lengths, so W_m is N-invariant. The preceding bound gives deg(W_m)>=10, whereas the effective cycle gives delta>=m deg(W_m). Taking m equal to any generic multiplicity proves the conclusion.

## Exact limits of the older surface-section bounds

PR249's quintic theorem applies to a surface scheme Z with a nonzero quintic ideal system having no fixed divisor. At degree at least 17 it gives h0(I_Z(5))<=8 and h0(I_Z(4))<=1. The general degree-d theorem requires a nonzero degree-d ideal system without a fixed divisor and deg(Z)>=(d-1)^2+1. It gives h0(I_Z(d))<=d+3, improved to d+2 when the preceding-degree section dimension is divisible by five.

The historical sheaf applications manufacture Z from a torsion-free sheaf M of positive determinant O(5) or O(6), generated outside codimension two, via a quotient by rank(M)-1 general sections. They also need lower bounds for h0(M). The new T is instead a rank-zero quotient of V* tensor O with det(image)=O. Its effective surface cycle alone supplies none of the required quintic/sextic ideal systems, none of their section counts, and no identification of a scheme degree with delta. In particular the reduced support degree can be strictly smaller than delta. These hypotheses cannot be transferred numerically.

PR266's degree-50/60 results concern N-invariant reduced CURVES, with additional component exclusions or integrality. They do not bound surfaces. A general hyperplane section of an invariant surface is not N-invariant, so the curve genus theorem cannot simply be applied to that section.

No exclusion of delta=30 or 40 follows here. No selected coefficient, source, or rank evaluation was performed.

## Inspected source versions

- PR1 comments read first, including the actual rank-seven stable-kernel and Chern-pair reduction.
- PR249, f8d9a6ee9b11d71cf27b5f3238aea73fcfb121cc: quintic/sextic section bounds and precise generating hypotheses.
- PR263, 75ecdc24934f72dbf2bb3ff274703f37ef4ca27a: birational invariant-quintic exclusion, with explicit sectional-genus hypothesis.
- PR266, d27b39c422bafb09100ee23f8f2b4c3b60a7a0ca: general sectional-genus bridge and component-orbit argument, alongside the distinct curve-only degree frontier.

## Full dependency check: the quintic bridge is independent of the old map

The missing original bridge was subsequently located and read in full:

- PR289 at `057792d7c964d56929f4252b2e2e3ce9f634a862`, `research/hm/middle-surface/rank-one-middle-quintic-reduction/SECTIONAL_GENUS.md`, Sections 1–4 and 6.
- Exclusion: PR263 at `75ecdc24934f72dbf2bb3ff274703f37ef4ca27a`, `research/hm/rank-four/quintic-surface-classification/PROOF.md`, Sections 1–4.

The bridge's wording starts from a surface previously obtained using Q, but its explicitly imported inputs are only: Y integral of degree five over C, standard irreducible H5 action, and the Hilbert congruence. Here those inputs have independent proofs, so the preceding construction of Y is not imported.

For completeness the entire bridge can be compressed as follows. H5 irreducibility makes Y nondegenerate. Its non-Cohen–Macaulay locus is finite: at every codimension-one point an integral surface has a one-dimensional local domain, hence is CM. Choose a hyperplane avoiding that finite locus. Its section C is CM and has no embedded points. Bertini gives irreducibility and generic smoothness, hence C is integral. The exact sequence 0→O_Y→O_Y(1)→O_C(1), together with H0(O_Y)=C, shows C spans its P3. Thus C has at least four linear sections.

Project C from an external point to P2. Fibers are finite, since an infinite fiber would force C to be a line. The degree formula and primality of 5 show that the image is a plane quintic and the map is birational; the alternative image line would make C planar. For this finite birational map f:C→D, the quotient f_*O_C/O_D has length q and p_a(C)=6−q. If q=0, f is an isomorphism respecting O(1), impossible because a plane quintic has exactly three linear sections. Thus 0≤p_a(C)≤5.

Write P_Y(n)=5 binom(n,2)+(6−g)n+chi. For sufficiently large n in each nonzero residue modulo 5, H0(O_Y(n)) is an H5 representation with nontrivial central character, so its dimension, hence P_Y(n), is divisible by 5. Subtract values at consecutive residues 1 and 2: 6−g is divisible by 5. Therefore g≡1 modulo 5, and the interval just proved forces g=1. This argument uses no purity assumption on T and no old Q hypothesis.

The exclusion also needs no embedded quintic classification. Resolve the normalization of Y and put L=pullback O_Y(1). A general pulled-back hyperplane is a smooth integral curve D normalizing C, so g(D)≤1 and L²=5. Adjunction gives K.L=2g(D)−7<0. Nefness of L kills every positive plurigenus; Enriques' ruledness theorem makes the resolution birational to B×P1 with g(B)≤1. The action on the function field is faithful: a projective transformation fixing the integral nondegenerate Y pointwise must be scalar.

If B is rational, N contains the nonabelian order-125 subgroup A semidirect C5, contradicting Serre's theorem that finite 5-subgroups of the complex plane Cremona group are abelian. If B is elliptic, every birational transformation descends to B. Aut(B) is solvable; perfect SL2(F5) acts trivially, and [SL2(F5),A]=A then forces A to act trivially on B too. Faithfulness would embed A=C5² into PGL2(C(B)), impossible even over the algebraic closure: the centralizer of an order-five element is a torus with cyclic finite subgroups.

Primary dependencies reopened and checked directly:

- Stacks, Bertini irreducibility, Lemma 37.32.3: https://stacks.math.columbia.edu/tag/0G4C . The complete hyperplane system is basepoint-free and its image has dimension two.
- Stacks, smooth Bertini, Lemma 33.47.3: https://stacks.math.columbia.edu/tag/0FD4 . Apply on the smooth locus, where the system is an immersion.
- Beauville, Algebraic Surfaces, July 2020, PDF page 26: all plurigenera zero implies ruled; https://math.univ-cotedazur.fr/~beauvill/conf/Shanghai.pdf . The resolution is smooth projective over C, as required.
- Serre, arXiv:0903.0514v1, Theorem 5.1(i), PDF page 13: finite ell-subgroups of Cr(k), ell>3 distinct from the characteristic, are abelian of rank at most two; https://arxiv.org/pdf/0903.0514 . Apply ell=5, k=C.

Finally, no purity of T is necessary: localization at each codimension-two generic point yields a finite-length module; N-equivariance identifies these local modules along component orbits. Thus lengths are orbit-constant, W_m is invariant, and summing the positive codimension-two cycle gives delta≥m deg(W_m). Lower-dimensional associated components contribute nothing to this cycle or argument.

Application pin: FULL-SUPPORT-AND-PURE-CHANNEL.md at 622aebd082db42057cd5b8502e941229ff499e58 of https://github.com/Akilleez-QA/read-em-and-weep/pull/543 supplies this particular equivariant quotient and its degree30/40 cycle. The same group argument applies to its Galois-conjugate Schrödinger coordinate representation.
