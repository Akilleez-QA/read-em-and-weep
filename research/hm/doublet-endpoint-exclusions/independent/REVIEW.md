# Independent review: terminal doublet scalar-degree obstruction

## Verdict and frozen scope

PASS for the complete new two-shape exclusion proof, relative to its explicitly pinned actual geometric inputs. No mathematical gap was found. This is a mathematical review with independently reproduced exact algebra controls, not proof-assistant verification and not a complete original proof repair.

Frozen author files in `../`:

- PROOF.md SHA256 `925293b6211d0ad6aa55b62d6de07da78a7509017cab89486791c2bf49e27eb1`
- verify.py SHA256 `52adb9d541df9e5ff0800cceaff3efe3854b471f6d09eb15b652d8d11eddda1d`
- RESULT.json SHA256 `7aed311adac0a8b56c34eb87636e2aa6b6f697fa5e3857ea38bf703a61d08751`

The result excludes A=W' O(-1)+O(e), e=4 or10, for the actual rank-three situation when the backward plateau length is k=1. It therefore applies in maximal profile(1,1). It does not require a condition on B or determinant defect. The general conditional conclusion e>=14 additionally assumes H0(K(3))=W' and absence of W' from Sym^(e+1)W. No conclusion for other e follows merely from this numerical bound.

## Independent source authentication

Eleven complete immutable originals were freshly retrieved through GitHub and authenticated by exact byte length, SHA256 and Git blob SHA1. `INPUTS.json` records the immutable URLs and checksums. They include all ten originals in the author manifest, plus the original physical character reference. Every written geometric source was read in full; the fixed historical JSON was used only to check labels, not regenerate the enumeration. The supplied character module was read and compared against a separately implemented exact character evaluator.

The imported actual HM constructions and their earlier upstream dependencies remain mathematical prerequisites. This review does not claim to re-prove the entire historical dependency graph.

## Critical geometric checks

1. **Correct endpoint direction.** The ACTUAL original, Section4, places E at F_k and its actual derivative kernel at F_(k-1). Section5 says maximal plateau endpoints have derivative rank one or two. Thus k=1 makes K=F_0 the lower endpoint, and rank(beta_K)<=2 is justified. The argument does not accidentally use l=1 or impose rank bounds on later derivatives.

2. **All four source types.** Their rank17, degree−54 and common quartic Euler character 3V+3P+2D agree exactly. The cubic alternatives from PR1140 are respectively 0/S, 0/W', 0, 0. For either target, vanishing cubic kernel implies maxdeg K<=−4; strict-top then injects H0(K(4)) into H0(A(2)). The signed envelopes are −V at e4 and 1+2A_std+D−V at e10. Their negative V multiplicity excludes cubic vanishing for every source. V/Z are eliminated directly. For D, PR1142 forces O2→A in the nonzero alternative, whereas the doublet target is inaccessible by degree and the scalar targets require invariant Sym2 or Sym8, neither present. Therefore only P remains and H0(K(3))=W'.

3. **Top block without horizontality.** Strict-top gives maxdeg K<=−3. Equivariant splitting and its cubic character identify the complete top block C=W'O−3, with lower complement of degrees<=−4. This is only a bundle decomposition. The actual derivative, not a projected connection, lands in A(−2). Its scalar component on C vanishes because W' is absent from Sym5/Sym11. Its doublet component is scalar by Schur. If zero, it contradicts strict-top for K. Hence that component is an isomorphism everywhere.

4. **Exact image and saturation.** The previous isomorphism gives the whole displayed W'O−3 summand in the coherent image. The rank<=2 endpoint bound then forces the scalar projection of the whole derivative to vanish generically, hence identically. Consequently the image is precisely that direct summand, not an unspecified subsheaf with a divisor defect. The resulting exact sequence identifies K/K^-=W'O−3 and makes K^- abstractly the lower complement. No horizontal right inverse is asserted or needed.

5. **The second strict-top step.** The actual derivative of K^- lands in (K/K^-)(−2)=W'O−5. Any degree−4 block maps to zero by ordinary Hom degree−1. Since K^- is saturated in the same constant ambient and has top<=−4, strict-top forbids that killed highest block. Thus maxdeg K^-<=−5. Equivalently, strict-top makes H0(K^-(4)) inject into H0(W'O−1)=0. This does not require the next derivative to have any prescribed rank.

6. **Degree contradiction.** Rank K^-=12 and degree K^-=−46−e. Twelve degrees<=−5 have total<=−60, so e>=14. At e4/e10 the totals are −50/−56, giving strict contradictions. The ambient is the actual constant thirty-space throughout, not the coefficient-presentation space of dimension54.

The stronger initial proposed scalar-row fullness, Euler lifting and explicit whole-kernel splitting are unnecessary in the frozen proof. They were deliberately not used to supply a missing bridge.

## Reproduction and independent controls

The author's verifier passes 400 explicit controls plus81 module controls. Fresh normal and `python -O` executions give output byte-identical to the frozen RESULT.json; the retained production output is `../RESULT.json`.

`independent_check.py` uses exact rational pairs for Q(sqrt5), an explicit closed-binomial formula for symmetric characters rather than the author's McKay recurrence, and conjugacy-class inner products. Its 1601 explicit controls verify orthogonality, all required Hom and Euler identities, complete Sym11, source rank/degree identities, the degree contradiction, source authentication, and all 135 irreducible/symmetric-power products through degree14 against the pinned recurrence. Its normal and optimized output is byte-identical.

- Independent checker SHA256 `f132f9858d5caf601c01072f7d67ac0177503ff63b0f4506ea6e1e2a24853072`
- Independent RESULT.json SHA256 `9079b70c99a5a94d98965162f6d31c51ff81bb1715eefb9c4071923cff81044e`

The fixed original labels are e4:86,87,88,89,96 and e10:116. These are historical identifiers only, not a live or incremental campaign count.

No actual source coefficient, parameter, selected point, jet, tensor, matrix or instance rank was evaluated. No external repository state was changed. No stopped experiment was restarted. Review and arithmetic verification are supporting evidence, not a separate new mathematical progress claim.
