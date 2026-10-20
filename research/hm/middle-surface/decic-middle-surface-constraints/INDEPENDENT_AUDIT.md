# Independent audit of the decic middle-surface constraints

## Verdict: PASS, conditional on the stated imported hypotheses

I independently checked `PROOF.md`, the relevant local multiplicity and Hilbert-congruence arguments, the rank-at-most-three corollary, and the quintic sectional-genus and birational-exclusion proofs. No correction to the conclusions is required. The result is a necessary constraint on a hypothetical surface component, not an existence theorem or an exclusion of degree ten.

## 1. Component orbits and perfectness

The new orbit argument is valid. A size-five orbit for `A=(F5)^2` has an order-five stabilizer `L`. Because A is abelian, every component in that orbit has exactly the same stabilizer. Normalizer translation takes this orbit to an A-orbit whose stabilizer is the conjugate line. The standard `SL2(F5)` action is transitive on all six lines in A. Distinct stabilizer lines cannot belong to the same A-orbit, so there are at least six disjoint size-five orbits, hence at least thirty components. Positive integral component degrees contradict `deg(W)<=14`.

This is stronger than merely saying the original orbit has a normalizer-invariant stabilizer, which would not be justified when the normalizer permutes several A-orbits. The proof correctly uses the six translated orbits instead.

Every remaining component is individually A-stable, hence H5-stable, and its natural structure-sheaf linearization makes its degree a positive multiple of five. There are at most two components. Their permutation action factors through `SL2(F5)` and has abelian image in S2, so perfectness makes it trivial. The imported elementary verification of perfectness is correct: conjugation by `diag(2,3)` sends an upper unipotent parameter s to 4s, making its commutator parameter 3s; upper and lower unipotents generate the group.

Consequently each component is N-invariant. Excluding invariant quintics leaves exactly one degree-ten component. Reducedness plus irreducibility gives integrality, and irreducibility of the ambient H5 representation gives nondegeneracy.

## 2. Local multiplicities and numerical budgets

The imported local proof is applicable at every residual rank, not only rank one: over the regular local ring of dimension two, the defect has at most six generators and socle dimension `j=10-r`. The resulting bound is `lambda>=max(j,2j-6)`.

For the unique decic, `10m<=delta<=70`. Since `dim Z_3<=1`, its generic rank is four or five. Thus:

- rank five: `m` is in `{5,6,7}`;
- rank four: `m` is in `{6,7}`.

These are necessary lists, with no assertion that every listed pair is realizable. The remainder of the singularity cycle has nonnegative degree divisible by five; its vanishing when `m=7` is correct. Lower-dimensional support is not thereby excluded.

## 3. Hyperplane sections without normality or smoothness

The scheme-theoretic argument is sound. A finite-type integral surface is Cohen–Macaulay at every codimension-zero or codimension-one point, so its closed non-Cohen–Macaulay locus is finite. A general hyperplane avoids that set. Its equation is a nonzerodivisor, and the section is therefore a Cohen–Macaulay curve without embedded points.

The hyperplane linear system satisfies the hypotheses of [Stacks Lemma 37.32.3](https://stacks.math.columbia.edu/tag/0G4C): it is basepoint-free, two general sections have a nonempty zero-dimensional intersection, and a third can avoid a selected intersection point. Irreducibility follows. On the smooth open locus, [Stacks Lemma 33.47.3](https://stacks.math.columbia.edu/tag/0FD4) applies because the hyperplane morphism is an immersion. A general section has its generic point in this locus and is generically reduced. Together with absence of embedded points, this proves integrality. The argument does not claim that the section avoids the entire singular locus or is everywhere smooth.

The exact-sequence proof of nondegeneracy is also correct and does not assume linear normality. It uses only `H^0(O_W)=C` and that W spans P4.

## 4. Arithmetic genus and Hilbert polynomial

Taking the first difference gives exactly

    P_W(t)=10 binom(t,2)+(11-g)t+chi(O_W),
    P_C(t)=10t+1-g.

The proper-support H5 congruence applies to `O_W`, regardless of whether the chosen hyperplane is invariant. It yields `g=1 mod 5` and `chi(O_W)=0 mod 5`.

I independently opened the publisher's [Miro-Roig PDF](https://lematematiche.dmi.unict.it/index.php/lematematiche/article/download/275/252/1043). Theorem/Definition 4.13, printed page 331, explicitly concerns integral nondegenerate curves and their arithmetic genus, not merely the genus of a normalization. The paper works in characteristic zero. At degree ten in P3, the displayed formula gives `g<=16`, so the preliminary list `{1,6,11,16}` is justified for this potentially singular curve.

## 5. The genus-one exclusion genuinely extends to degree ten

No degree-five classification is hidden in the imported exclusion. For a resolution of the normalization, the pullback polarization is nef and globally generated and has square ten. The finite normalization contracts no curve; the resolution's contracted curves map to finitely many points of W. A general hyperplane avoids these points, so its smooth integral pullback maps finitely and birationally to C and is the normalization of C. Therefore its genus is at most `p_a(C)`.

If `p_a(C)=1`, adjunction gives `K_S.L=2g(D)-2-10<0`. Nefness then forbids every effective positive multiple of K. The ruledness implication from vanishing plurigenera is explicitly confirmed in [Beauville's lectures](https://math.univ-cotedazur.fr/~beauvill/conf/Shanghai.pdf), PDF page 26. The moving-fiber intersection argument correctly forces a positive-genus ruled base to have genus at most one.

The group action on the function field is faithful because W spans P4. In the rational case, the nonabelian subgroup `A semidirect C5` of order 125 contradicts the abelianness assertion for all finite 5-subgroups in [Serre, Theorem 5.1(i)](https://www.college-de-france.fr/media/jean-pierre-serre/UPL151543545980010914_9___A_Minkowski_style_bound.pdf), printed page 204, independently checked.

In the elliptic-ruled case, descent to the elliptic base, solvability of its automorphism group, perfectness, and `[SL2(F5),A]=A` force A to act fiberwise. The resulting injection of `C5 x C5` into `PGL2(C(E))` is impossible: over the algebraic closure, the centralizer of an element of order five is a torus and its finite subgroups are cyclic. All these steps are independent of the positive degree.

Thus genus one is excluded and the final arithmetic-genus list `{6,11,16}` is valid.

## Audit boundary

The ambient equivariance, bundle presentation, generic-rank-ten assertions, total singularity-cycle bound, and rank-at-most-three exclusion remain imported conditional inputs. This audit does not establish those inputs for any concrete operation.
