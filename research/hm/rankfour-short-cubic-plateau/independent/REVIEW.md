# Independent review: actual rank-four maximal plateau (1,3)

## Verdict

PASS, conditional on the retained actual-geometric hypotheses. The reviewed proof excludes exactly the ordered maximal rank-four plateau (1,3). It does not exclude all generic rank four, increase the global rank bound by itself, establish surjectivity, or repair the original theorem.

Reviewed author proof SHA256:
`7ec277448b80a3f77300e7c7802b7ea49ef0a742e8a652270f3af9a957010a92`

Reviewed author verifier SHA256:
`1c4ea1db7bbcb7571bd821de308d56d8b108ee3ffb73a3501df1697670eea46f`

The exact reviewed files are retained under `reviewed_author/`. No author import is used by the independent mathematical checker.

## Geometric review

The four complete immutable originals in `INPUTS.json` and the complete final author proof were read. Only their general actual-presentation, ambient-character, Gauss-transform, saturation, equivariant-splitting, and invariant-divisor facts are used. No rank-three theorem, rank-two endpoint exclusion, or historical finite classification is transplanted.

1. The hypothetical actual chain has ranks 13,17,21,25,29 with E=F1. Equal generic rank and saturation give the interior sheaf-kernel and forward-transform identities. Regular derivatives consequently descend between four-dimensional graded bundles. This is valid on the whole parameter curve, not just its generic point.
2. Persistence applies at F0 as well as the interior: dF0 lies in F1 tensor Omega because F0 is the kernel at F1. A section of F0(3) would saturate to a line whose constant coefficient span is reached by at most three derivatives, inside a stage that cannot contain a constant subbundle. The identical reversed-annihilator argument applies to the rank-one upper annihilator. Thus a<=-52 and b<=-4. No rank-one endpoint flag theorem or asserted endpoint differential rank is needed.
3. The rank-four determinant increment is 8, not the rank-two increment 4 or rank-three increment 6. Eliminating c1 from a+c1=-54 and b=a+sum(ci) yields 3a+b=-168+3delta1+2delta2+delta3. The endpoint slack is exactly 8. Every positive invariant effective divisor has degree at least 12; therefore every delta is zero. All endpoint determinant degrees are even because the ambient center acts trivially and the group has no nontrivial characters. Precisely (-52,-12) and (-54,-6) remain. This proves the absence of positive defect, rather than imposing it as an ansatz.
4. Persistence at E forces top degree -3. Its rank/degree deficit is three. The only possible lower blocks are a three-dimensional even coefficient at -4 or one trivial coefficient at -6. The source H1(E(1))=W'+3T6 rejects the latter and forces the former to be V, not A or 3*1. Thus E=(W'+2T6)O(-3)+VO(-4). This is a new short source derivation and does not rerun the historical 28-type classification.
5. With B=E/F0, zero determinant defects imply Li=B(2i-2) as equivariant graded bundles. They do not split the original flag horizontally. Since B(4) is a quotient of globally generated E(4), every ordinary slope is >=-4. Rank four and degree d=-2 or 0 give e<=d+12. These endpoints are sharp within the necessary abstract domain; the checker includes 3O(-4)+O(d+12).
6. For a=-52, F0 is R13 O(-4), giving H1(F0(3))=H1(F0(4))=0. For a=-54, its deficit two gives either X O(-5)+R11 O(-4), X=W or W', or O(-6)+R12 O(-4). Thus cubic H1 is W or W'; quartic H1 is 0 or 1. Treating these quartic corrections as uncorrelated with the cubic excess is a conservative overlist and cannot falsely exclude an actual possibility.
7. The quotient H O/F4 is exactly O(-b), with no hidden one-dimensional coefficient character. Additivity along the actual upper filtration gives [H O]=[E]+[B(2)]+[B(4)]+[B(6)]+[O(-b)]. Taking full equivariant Euler characteristic is legitimate for every twist without global-section surjectivity, H1 vanishing, filtered splitting, or a horizontal direct sum.

## Independent arithmetic result

`independent_check.py` uses exact conjugacy-class values in Q(sqrt5). Symmetric powers are evaluated with the closed binomial character polynomial, not the author's McKay recurrence or its symmetric-power recurrence. Coefficients are recovered by exact character inner products and checked for integrality, orthogonality, dimension, central parity, and the physical W marking.

The necessary domain is independently generated in two ways: ordinary four-line degree multisets with representation decorations at each degree, and irreducible-block recursion with a rank budget. Both agree on all 37 degree-minus-two and 50 degree-zero possibilities. Cubic exactness retains 5 and 8, respectively. Quartic exactness retains 2 and 2. All thirteen cubic candidates, their quartic Euler characters, pass/fail decisions, and four final obstructions agree exactly with the author after only the notation changes D→D5 and P→P4.

The four surviving B and twist-zero full-Euler residuals, in the fixed representation basis, are:

- (-52,-12), B=W'O(-3)+2O(2): 1-A+D5-V.
- (-52,-12), B=VO(-2)+O(4): 1+A-P4.
- (-54,-6), B=W'O(-3)+O(2)+O(4): V-A.
- (-54,-6), B=W'O(-3)+WO(3): V-A.

Every residual is nonzero and has ordinary dimension zero. Thus a scalar dimension check is insufficient. In particular V must not be identified with A, and W' must not be identified with W.

The source contribution at twist zero is chi(E)=-(2V+4P4+3D5), not zero. The independent checker includes all H1 tails by Serre duality at every tested twist. For the final four B, H1(B(2)) happens to vanish; the general necessary domain also permits degree-minus-four blocks, whose B(2) tails are handled with the negative Euler sign. Some final candidates have zero residual at twist three but not twist zero, so a cubic-only full-Euler check would not suffice.

## Reproduction and controls

Run `python3 verify_review.py` from any directory. It verifies the hash manifest, reruns both independent and author checkers in normal and optimized Python modes and from another working directory, compares their stored outputs, and cross-compares all thirteen candidates and final residuals.

Actual fail-closed controls alter copied data/code, then rerun the relevant checker: one-byte corruption of each source, changed immutable source ref, wrong central parity, exchanging A and V while fixing W, discarding H1 tails, omission of a cubic candidate, and replacing a nonzero final obstruction by zero. None modifies the retained author or source files. `CONTROLS.json` records the outcomes. The author's separate internal mutation suite is also rerun.

The implementation uses the standard library only. It selects no actual coefficients, parameters, jets, matrices, or instance ranks and performs no external write. The new finite classification is over necessary abstract bundle data, not actual HM instances or historical search records.

The source hashes authenticate retained bytes, not the truth of their transitive geometric premises. The arithmetic scripts are reproducible checks of the written proof, not proof-assistant certification of its geometry. No broader conclusion is claimed.
