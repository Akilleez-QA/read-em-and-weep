# Independent mathematical audit: the quartic endpoint Wronskian map

## Verdict and immutable scope

**PASS. No substantive mathematical defect found. No change to the reviewed proof is required.**

This review applies to `PROOF.md` with SHA-256:

`858a750d6a7c320affc28fcea614164e5c9c40fcf96be687faa1cc9d38af99c0`.

The complete proof was read and its principal arguments independently checked: all-parameter basepoint-freeness, the correctly twisted order-two character calculation, the residual-divisor classification, the degree-sixty invariant pencil, the parameter map's exact degree, the local vanishing lists, the four distinct twelve-orbit parameters, and the sharp jet consequences. This is a written mathematical audit, not proof-assistant certification. No source-instance computation or parameter scan is used in the mathematical verification.

## 1. Source pins, provenance, and the scope of the novelty check

The following supplied source snapshots were read. Their computed hashes agree with the supplied pins:

- PR754: [ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/044add76ebb14043a0edf73171517c90b9ef0c13/research/hm/order-four-quadratic-load/ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md), SHA-256 `26afce66386de77a6ef3b511d9de1b3053b2a885c290bda84dccf4889562d5bc`. The proof cites commit `044add76ebb14043a0edf73171517c90b9ef0c13`.
- PR784: [source2-second-defect-zero/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/66aa488fb10158abcc2d35ce58b05b901d44b81a/research/hm/source2-second-defect-zero/PROOF.md), SHA-256 `b0695ab0fbbfa9a4a4985f29c2818b15a8f6ec1977a5c2eae944d7c3b1bfe766`. The proof cites commit `66aa488fb10158abcc2d35ce58b05b901d44b81a`.
- PR785: [source2-four-jet-rigidity/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/7ec3b8140abe6ee60f9d0dfee657e7b0be022fc3/research/hm/source2-four-jet-rigidity/PROOF.md), SHA-256 `0378cf255b1666f3e8d03f588335a52352ba305d9765cdaea9c4965db8c2792a`. The proof cites commit `7ec3b8140abe6ee60f9d0dfee657e7b0be022fc3`.

This audit checks the immutable source snapshots listed above; it does not assert an independent fresh retrieval of their remote commit bytes.

PR754 supplies the degree-eighteen decomposition, the fixed A and V copies, the two-dimensional P-multiplicity space, and the balanced locus obtained by removing two distinct parameters. Its proof establishes basepoint-freeness on that balanced locus, not a failure of basepoint-freeness at its two omitted parameters. The new proof correctly keeps those two independent ten-section systems in its full parameter family.

PR784 supplies the prior actual-source second-jet and zero-second-defect statements. PR785 supplies the universal four-jet theorem, its degree-ninety Wronskian argument, the order-five fiber twist, and its conditional actual-source Gauss applications. Those inputs are acknowledged rather than presented as new.

Relative to these inspected texts, the genuinely additional conclusions are the all-parameter basepoint-freeness statement, the forced thirty-orbit divisor and resulting four divisor regimes, the invariant residual pencil and degree-four parameter morphism, the reduced four-point twelve-orbit fiber with its four distinct local types, and the exact higher-jet exceptions and sharp upper vanishing bound. This is a comparison with the pinned sources, not an exhaustive repository-wide or literature-wide priority search.

## 2. All-parameter basepoint-freeness and exceptional orbits

Every parameter is a multiplicity line in the P-isotypic summand. Since the fixed irreducible summands and that variable P copy are in direct sum, the subsystem has dimension ten for every parameter, without any balancedness assumption.

Its common base divisor B is invariant. If B is nonempty, its support contains an orbit of size at least twelve, so deg B is at least twelve. Dividing the sections by their common factor gives an injection into H^0(O(18 - deg B)), whose dimension is at most seven. This contradicts dimension ten. The argument therefore proves basepoint-freeness on the entire parameter line and is independent of later ramification arguments.

For the projective A5 action, finite point stabilizers are cyclic, and their possible nontrivial orders are two, three, and five. Each such subgroup fixes two points. A finite point stabilizer cannot contain two distinct maximal subgroups from this list, so the counts of subgroups give respectively thirty, twenty, and twelve distinct fixed points. Their orbit sizes force exactly one exceptional orbit of each size. The use of D12, D20, and D30 as unique reduced divisors is justified.

## 3. Wronskian degree, nonvanishing, and the thirty-orbit sign

The determinant of the order-nine principal-parts map has degree

    10 * 18 - 2 * (0 + 1 + ... + 9) = 90.

For an adapted basis with distinct vanishing orders a_0 through a_9, the coefficient of the lowest Wronskian term is the product of the nonzero leading coefficients and the Vandermonde determinant of those orders, expressed in the falling-factorial basis. It is nonzero in characteristic zero. Therefore the Wronskian is nonzero for every subsystem and its local order is exactly the sum of a_i - i. This also establishes the nonvanishing later needed to rule out common parameter zeros.

The determinant construction is equivariant. Perfectness of the binary group trivializes the determinant character, so the resulting degree-ninety section is invariant, not merely invariant up to a nontrivial character.

The order-two projective stabilizer calculation has the correct fiber sign. For the binary lift with tautological eigenvalue i, the O(18) fiber has character i^(-18) = -1, and the cotangent also has character -1. The order-j jet line therefore has character (-1)^(j+1). The two three-dimensional irreducibles each contribute positive multiplicity one and negative multiplicity two; P contributes two of each. Thus the source has positive multiplicity four and negative multiplicity six, requiring six even and four odd vanishing orders.

The minimum orders are 0,1,2,3,4,5,6,7,8,10, with sum 46 and weight one. Hence the entire D30 is forced in every Wronskian divisor. Discarding the fiber twist would reverse these parity counts and would not prove the stated conclusion; the proof does not make that error.

After subtraction of D30, the effective invariant residual has degree sixty. The orbit equation 12a + 20b + 30c + 60d = 60 has exactly the four listed solutions. If a free orbit appears, it already consumes degree sixty and must be reduced. This proves the four full Wronskian-divisor regimes, including the possibility 3D30 rather than merely D30 plus a disjoint residual.

## 4. The invariant-field proof of the residual pencil

The orbit forms have disjoint zero sets and are invariant by perfectness. Therefore q = F12^5/H20^3 defines a map of degree sixty. The extension C(P1)/C(q) has degree sixty, while the fixed field of the faithful A5 action has index sixty. The inclusion C(q) in the fixed field and the tower formula consequently identify the two fields.

For an invariant degree-sixty form R, the quotient R/H20^3 is a rational function of q. Its only possible poles upstairs lie on D20 and have order at most three. The map q has a pole of exact order three at each point of D20. A pole of the descended function at a finite target point would pull back to a pole outside D20, which is impossible; a pole of order m at infinity would pull back with order 3m, so m is at most one. The descended function is therefore affine linear in q.

This proves that the degree-sixty invariant space is exactly the span of F12^5 and H20^3, without presupposing an explicit invariant-ring relation. T30^2 belongs to this span and has both coordinates nonzero, since its divisor is disjoint from the other two exceptional orbits. The three special target points are consequently distinct.

## 5. Exact degree four and absence of common parameter zeros

The universal basis has six parameter-independent entries and four entries linear in the multiplicity vector. Multilinearity of the Wronskian makes it homogeneous of degree four in that vector. Dividing by the fixed invariant T30 and using the residual pencil gives two homogeneous quartics A4 and B4.

A common projective zero of A4 and B4 would annihilate the entire Wronskian of the corresponding subsystem. The subsystem still has ten independent sections there, so the characteristic-zero Wronskian criterion rules this out. The pair is genuinely basepoint-free.

Two basepoint-free sections of O(4) define a morphism whose pullback of O(1) is O(4). The morphism is thus nonconstant and has degree exactly four. In particular there is no unaccounted common factor lowering the degree. A constant ratio would also contradict the absence of a common zero, since a nonzero homogeneous quartic over C has a projective zero.

Each target fiber has length four with multiplicity. The three distinct special fibers therefore contain at most twelve distinct parameters. Away from them the residual is one reduced free orbit, every ramification point has weight one, and the sequence is 0,1,...,8,10. This proves universal order-eight spanning for those parameters. Surjectivity establishes occurrence of each divisor regime somewhere in the abstract family, not realization by an actual source.

## 6. Completeness of the local vanishing lists

The stabilizer-invariant vanishing filtration has one-dimensional nonzero graded pieces, each with its corresponding graded jet character. Semisimplicity therefore identifies character multiplicities with the numbers of orders in the associated residue classes.

At D12, the fiber character is zeta and the cotangent character is zeta, so order j has character zeta^(j+1). The source has two copies of every character. The baseline orders are 0 through 9. Weight five increases one residue-class sum by exactly five. Only the upper order in that class can be moved by that amount without collision, yielding exactly the five provisional cases indexed by r = 0,...,4.

At D20, each three-dimensional summand contributes eigenvalues 1, omega, omega^2, and P contributes 1,1,omega,omega^2. The fiber of O(18) is trivial. The residue counts are exactly (4,3,3), with baseline 0 through 9. Weight three permits only the replacements 7 by 10, 8 by 11, or 9 by 12.

At D30, the baseline weight is already one. Weight three permits one additional parity-class step of size two: either 10 becomes 12 or 7 becomes 9. These are precisely the two displayed sequences. At weight one the parity-minimal sequence is unique. At a free point of weight one, strict increase likewise forces the unique sequence 0 through 8 followed by 10.

The lists are complete as necessary local possibilities. The proof correctly does not claim that all three D20 candidates or both D30 candidates occur individually.

## 7. The four distinct D12 parameters and the omitted fifth candidate

At an arbitrary point of D12, the family of order-nine jet maps decomposes into five character blocks with target dimension two. The source of the trivial block is fixed of dimension two. Each nontrivial block has one fixed direction and one direction from the variable multiplicity line. Equivalently, its source over the parameter line is O plus O(-1), and its target is O squared.

The full determinant thus factors into one constant determinant c and four linear determinant sections L_r. If any factor vanished identically, every parameter would ramify on D12. The residual-divisor classification would force every residual to be 5D12, contradicting the already established nonconstancy of the degree-four map. Hence c is nonzero and each L_r is nonzero, with one simple projective root.

If two different nontrivial blocks vanished at one parameter, each would have a kernel section with vanishing order beyond the order-nine jet range. In residue class r the largest order would then be at least r+10, increasing that class's minimum sum by at least five. Two such defects contribute at least ten to the local weight, contradicting the allowed D12 weights zero and five. Thus the four roots are pairwise distinct.

At each root the total weight is exactly five, so its defective character determines exactly one of the provisional cases. The trivial character corresponds to residue four because of the fiber twist; its constant invertible block prevents that residue from changing. This excludes replacement of 9 by 14 and leaves exactly the cases r = 0,1,2,3, each realized at its own parameter.

The coefficient cutting out the target value [F12^5] is proportional to this determinant product: at D12 the F12 term vanishes while T30 and H20 do not. Its four roots are simple, proving that the special fiber is reduced and that the parameter morphism is unramified over that target value. No circular assumption of generic D12 nonramification occurs: nonconstancy was established first from the globally nonzero Wronskian family.

## 8. Exact jet exceptions and sharp injectivity

At parameter t_r, the first missing order on D12 is 5+r. All other D12 parameters have the ordinary sequence. The first missing order in any allowed D20 or D30 sequence is at least seven; at a free ramification point it is nine. Consequently jets through order five fail somewhere exactly for t_0, and jets through order six fail somewhere exactly for t_0 and t_1. In each indicated case the failure set is precisely D12.

Every listed sequence begins with 0,1,2,3,4, consistently recovering the previously known four-jet theorem. The largest final order in the refined D12 list is thirteen; at D20 or D30 it is at most twelve, and at a free ramification point it is ten. Thus no nonzero section of any family member can vanish to order fourteen. The order-thirteen jet map is injective everywhere for every parameter.

At t_3 the sequence is 0,1,2,3,4,5,6,7,9,13. An adapted basis therefore contains a nonzero section of exact order thirteen, which is killed by the order-twelve jet map. The uniform order-thirteen injectivity bound is genuinely sharp, not merely the strongest unrefined estimate.

Here an order-m jet records terms through degree m, so it has length m+1. The proof uses this convention consistently.

## 9. Conditional actual-source boundary

The theorem is about the entire abstract degree-eighteen family. It does not identify the parameter of a hypothetical actual source, establish whether that parameter lies in any special fiber, or show that any abstract parameter satisfies all remaining same-source conditions. In particular, inclusion of the two nonbalanced abstract systems in the family does not make them admissible actual endpoints with the required balanced presentation.

No new actual Gauss growth beyond the explicitly applicable jet-spanning hypotheses is asserted, no source label is excluded, and no source realization follows. The source-interface qualifications and the separation between abstract family existence and actual same-source compatibility are mathematically appropriate.

**Final assessment: the pinned draft is sound on its stated assumptions, and all advertised new abstract-family conclusions follow.**
