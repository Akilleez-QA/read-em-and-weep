# Exact original torsion characters do not prune the 159 shortest-profile pairs

## Result and scope

The 159 necessary pairs of ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md all satisfy the exact original torsion-character condition. Counts remain 80,61,5,13 at original defect t=0,12,20,24. This is a negative result for this particular proposed pruning method, not a realization theorem or exclusion of any profile. The new information is the exact stabilizer character of each possible cokernel, and an exhaustive equivariant length-two local classification that retains the tangent character.

All 66 positive reduced-orbit pairs determine one unique possible orbit-line parameter k. All thirteen doubled-orbit pairs determine exactly two possible sheaf types: one cyclic module and its semisimple associated graded. Their Euler characters agree at every twist. Even the stronger source/target stabilizer-fiber and Tor compatibility condition below prunes neither pairs nor alternatives.

We use the previous 159-pair list as a necessary overlist; its degree bounds and geometric derivation remain inputs. The new verifier independently checks its counts, ranks, degree identity, center parity, character-ring orthogonality and all new arithmetic. It does not rerun or overwrite the predecessor verifier or dataset.

## 1. Exhaustive original torsion possibilities

Write C=B*(-2) and T=coker(A->C), where both bundles have rank three. The invariant determinant divisor has degree t. For t=12 or20 it is the single reduced orbit D_t. For t=24 it is 2D_12. Local length equals determinant order, so the latter case has length two at each of the twelve orbit points, not length one at an invented orbit of size24.

Let H be the binary point stabilizer. It is cyclic of order10 on D_12 and order6 on D_20. The O(1) fiber generates its character group. Equivariant sheaves supported on one transitive orbit are equivalent to H-equivariant modules on a local infinitesimal neighborhood of one point. Since the center acts trivially on A and C, T is center-even. Thus reduced orbit lines are precisely

    O(k)|D_12, k=0,2,4,6,8;
    O(k)|D_20, k=0,2,4.

For t=24, let R be the local DVR and m its maximal ideal. An R-module of length two is either R/m^2 or (R/m)^2, by the elementary-divisor theorem. The alternatives cannot vary along the transitive orbit.

In the cyclic case, the one-dimensional quotient T/mT is an H-character. A generator with exactly that character exists: average any lift against that character using the Reynolds projector. Its residue is nonzero, so it generates by Nakayama, giving the H-equivariant identification with R/m^2 tensored by that character. Such a character is the fiber of O(k); global transport over the orbit identifies T with O(k)|2D_12. There is no additional infinitesimal linearization parameter, since the eigen-generator already yields the full equivariant module isomorphism. The allowed k are even modulo10.

In the semisimple case mT=0. The two-dimensional H-representation is a direct sum of any two even characters, allowing equal or distinct characters. Consequently the complete alternatives are

    cyclic: O(k)|2D_12, k=0,2,4,6,8;
    semisimple: O(k)|D_12 + O(l)|D_12,
                0<=k<=l<=8, k,l even.

There are five cyclic and fifteen semisimple isomorphism classes. These are possibilities for sheaves only; we have not proved the existence of a global quotient C->T with kernel A.

## 2. Tangent character and exact Euler signatures

The divisor equation of D_s is invariant: its defining line is stable and the binary icosahedral group has no nontrivial one-dimensional characters. Thus

    H0(O(k+r)|D_s)=chi(O(k+r))-chi(O(k+r-s)).

For 2D_12 replace s by24. Crucially, the conormal character is not trivial. The canonical filtration gives

    0 -> O(k-12)|D_12 -> O(k)|2D_12 -> O(k)|D_12 -> 0.

At the stabilizer this conormal shift is -12=-2 modulo10; the tangent character is its inverse. Therefore the cyclic signature equals the semisimple signature for the unordered pair {k,k-2 mod10}. This equality holds for every twist, not just at the untwisted representation level. It does not assert an isomorphism of the two sheaves: the cyclic module has nonzero maximal-ideal action and the semisimple one has zero action.

Exactness of 0->A->C->T->0 requires

    chi(C(r))-chi(A(r))=H0(T(r)).

This is tested against the entire sheaf list above, not merely against the cone of effective characters. Two consecutive twists determine the full Euler signature: tensor the standard equivariant Euler sequence on P1 to obtain

    chi(F(r+1))=W chi(F(r))-chi(F(r-1)).

It applies to these torsion sheaves as well, because the Euler sequence is locally split and its terms are locally free. We test r=0,1, then redundantly verify -32<=r<=32. The redundant interval is not an assumed completeness cutoff.

## 3. Stronger stabilizer-fiber compatibility

The exact local sequence, tensored with the residue field, yields

    0 -> Tor1(T,k_p) -> A_p -> C_p -> T/mT -> 0.

For a reduced orbit line of parameter k, the final character is k and the initial Tor character is k-s, with s=12 or20. For a cyclic doubled-orbit module they are k and k-24. For a semisimple pair they are {k,l} and {k-12,l-12}. The differences are conormal shifts, not arbitrary parity choices.

Accordingly we require that the final characters occur in C_p, the Tor characters occur in A_p, and the residual H-representations agree. This retains multiplicities, including coincident semisimple characters. Restriction to H is computed by exact cyclic Fourier decomposition in the cyclotomic field, not by numerical eigenvalues or selected points. A block R O(e) has fiber Res_H(R) shifted by e modulo |H|. All irreducibles are self-dual, so choosing the opposite eigenline does not alter the restriction calculation after consistently naming O(1)'s character.

Every surviving Euler alternative also passes this stronger necessary condition.

In fact this condition is sufficient for abstract completed-local equivariant Smith compatibility. Choose an H-eigenparameter x by averaging a lift of a generator of m/m^2; its nonzero linear term makes it a formal parameter. Its character is the conormal character -s modulo |H|. Likewise, averaging fiber eigenbases gives equivariant free bases of the completed source and target modules, by Nakayama. Identify the matching residual free characters by units. For a reduced length-one factor, send a source eigen-generator of character k-s to x times a target generator of character k. For a cyclic length-two factor use x^2 and source character k-2s. For a semisimple length-two module use two independent length-one factors. These are abstract module constructions, not evaluations of the actual map or a selected source point. They produce the stated cokernel and determinant order. Thus no further purely completed-local equivariant Smith obstruction can discard these alternatives based only on the given source/target fiber characters. This does not construct a global bundle map with the required splitting types or the actual Gauss derivative; global realization remains entirely open.

## 4. Concrete output

Pair IDs are zero-based row numbers in one-one-endpoint-necessary-pairs.json. Every pair survives. Each defect12 or20 pair has precisely one possible k; all are in the compact output. At defect24 the list is:

- IDs 8,15,19,20: cyclic k=4 or semisimple {2,4}.
- IDs 9,10,11,12,13,14,16,17,18: cyclic k=6 or semisimple {4,6}.

Thus cyclicity cannot be inferred, nor can one discard the semisimple case on the ground that its two fiber characters are distinct. Euler signatures alone cannot choose between these alternatives. Any successful further pruning needs a condition beyond these original exact Euler signatures and local fiber/Tor compatibility, such as global quotient realization or additional endpoint geometry.

## Reproduction and boundaries

Run python3 verify_one_one_exact_torsion_characters.py. It writes only the new compact one-one-exact-torsion-characters.json and pins source hashes. The character calculation is exact in Q(sqrt(5)); local Fourier calculations use exact cyclotomic polynomial reduction. The finite sheaf lists are exhaustive by the preceding local geometric argument.

No actual selected coefficients or points, instance matrices, actual-map rank experiments, scans, spikes, or consumed experiments are used. No predecessor is edited. The original profile remains open, and no SF or smoothing bound is improved.
