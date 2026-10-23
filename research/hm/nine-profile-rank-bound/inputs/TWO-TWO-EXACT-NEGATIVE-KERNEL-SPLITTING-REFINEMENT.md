# Exact negative-kernel splitting refines the (2,2) list

## Checked result and scope

Starting with the 2947 source/target records and35 quotient pairs of TWO-TWO-SYMMETRIC-QUOTIENT-DEFECT-IS-ZERO-OR-TWELVE.md, exact kernel splitting and exact cohomology compatibility leave 1880 records and34 quotient pairs. They use 25 of the 28 primal types and33 of the 37 dual types. There are 1723 defect-zero records and157 defect-twelve records. These are necessary possibilities only, not realizations or sufficient conditions for bundle extensions.

The one eliminated quotient pair has the short independent proof in TWO-TWO-SEVEN-W-QUOTIENT-IS-EXCLUDED-BY-EXACT-COHOMOLOGY.md. Thus this refinement is not merely an individual-block Hom eligibility check. The remaining full profiles and the proven SF/square rank bounds are unchanged.

## 1. Enumerating the full negative kernels

Retain K=E^-, L=(Q*)^-, A=E/K, B=Q*/L. Both kernels have degrees at most -3. For either exact sequence 0 -> N -> F -> C -> 0, with (N,F,C)=(K,E,A) or (L,Q*,B), one has

    H1(N(2)) = chi(C(2)) - chi(F(2)),
    chi(N(3)) = chi(F(3)) - chi(C(3)).

The first equality holds because H0(N(2))=0. Set H to its right side, an actual representation. A negative block R O(-j), j>=4, contributes R tensor Sym^(j-4)W to H. The bound (j-3)dim R<=dim H makes the exhaustive nonnegative block enumeration finite. Here dim H<=30, so j<=33.

Given the high blocks j>=4, their H1(N(3)) contribution is R tensor Sym^(j-5)W for j>=5. Therefore the top coefficient R3 is forced exactly by

    R3 = chi(N(3)) + H1(N(3)).

It must be genuine, center-odd, and contained in H0(C(1)), by the strict-slope derivative injection H0(N(3)) -> H0(C(1)). The verifier exhausts the high-block decompositions, computes this forced top coefficient, and checks the total rank and degree. Every one of the 35 initial quotient pairs has at least one formal K and L splitting at this stage alone. No claim of an additional pair exclusion is made from kernel splitting by itself.

## 2. Enforce the entire exact cohomology sequence

For each resulting splitting N and a specific formal F type, the sequence at twist t requires that the following three representations be genuine:

    X = H0(F(t)) - H0(N(t)),
    Y = H0(C(t)) - X,
    Z = H1(F(t)) - H1(C(t)).

Euler exactness identifies H1(N(t))=Y+Z. Thus these are precisely the character-level necessary image conditions for the six-term cohomology sequence, not just inequalities on total dimensions. They do not assert existence of a sheaf extension or quotient map.

The verifier tests -30<=t<=34. This is exhaustive for these character constraints: for t<-30 all the listed bundles have vanishing H0 and Z=H1(N(t)) is automatically genuine; for t>34 all H1 vanish, because the largest possible negative index is33, and the conditions reduce to exact Euler identities. The source E degrees are between -10 and-2, the source Q* degrees between -28 and-2, and the quotient degree windows were already proved in the previous note.

A primal/dual record survives only if there is at least one kernel splitting satisfying all these conditions on each side. This gives the 1880-record,34-pair result above. No constant multiplicity subspace is presumed horizontal, and no torsion defect is discarded when it equals12.

## Reproduction and files

Run python3 verify_two_two_exact_kernel_splittings.py. It regenerates the full local files two-two-exact-kernel-splittings.json and two-two-exact-kernel-compatible-records.json. The compact distribution and34 pairs are in two-two-exact-kernel-summary.json. The large generated full-record files need not be distributed. The earlier base proof, verifier and summary are unchanged.

All calculations are exhaustive identities for abstract representations and bundle splitting data. No actual HM coefficients, points, matrices, rank tests or scans occur.
