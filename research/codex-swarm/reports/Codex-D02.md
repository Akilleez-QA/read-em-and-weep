> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-D02 — completeness review.** Known detectors are incomplete on dimension352; separation of the conditional dimension32 sector remains unproved.

At pin `08b73637d4136f91606aad332c46cafd064417f8`, use `research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js`. Over Q, write
\[
H=\ker D_2/\operatorname{im}D_1,\quad
\dim C^2=6560,\quad \operatorname{rank}D_1=2560,\quad
\operatorname{rank}D_2=3648.
\]
Thus \(\dim H=352\). Let \(F=(S,\ell)\), stacking **all output coordinates** of the 30 scalar maps and the additional scalar functional. Published comments **6104478488, 6104582655** establish rank332 for \(S|_H\) and a cycle in its kernel detected by \(\ell\). Consequently
\[
\operatorname{rank}(F|_H)=333,\qquad \dim\ker(F|_H)=19.
\]
These are published dependencies, not newly executed checks.

**Exact completeness rule.** Assuming \(FD_1=0\), a family is complete precisely when
\[
\ker D_2\cap\ker F=\operatorname{im}D_1,
\]
equivalently
\[
\operatorname{rank}\!\begin{bmatrix}D_2\\F\end{bmatrix}
-\operatorname{rank}D_2=352.
\]
The required stacked rank is4000; the known family has3981. Vanishing of every known detector therefore does not prove a boundary.

**Conditional sector review.** Let \(W=H[\varepsilon]\), assuming the characteristic-zero dimension32 and source-membership premises of comments **6130391535/6130352358**. Elementary intersection bounds give
\[
13\le\operatorname{rank}(F|_W)
=32-\dim(W\cap\ker F)\le32.
\]
Global rank333 supplies neither restricted rank32 nor restricted incompleteness. A lone scalar detector has restricted rank at most1; its78 seed expansions remain one detector.

**Small exact countercontrol (original hand derivation).** Take \(C^2=\mathbf Q^5\), \(D_1(t)=te_5\), \(D_2=0\), and \(F(x)=(x_1,x_2,x_3)\). Then \(H=\mathbf Q^4\), \(FD_1=0\), and global rank is3. On \(W_{\rm good}=\langle[e_1],[e_2]\rangle\), restricted rank is2; on \(W_{\rm bad}=\langle[e_1],[e_4]\rangle\), it is1. The nonboundary \([e_4]\) passes every detector. Identical global ranks permit opposite sector conclusions.

**Smallest actionable rank-certificate contract.** Supply authenticated rational cycle lifts \(U\) with32 columns, corrected transferred action maps \(R_g=P\rho(g)I\), boundary witnesses \(V_g\), and a left inverse \(L\), satisfying
\[
D_2U=0,\quad FD_1=0,\quad
(R_g-\varepsilon(g)I)U=D_1V_g,\quad LFU=I_{32}.
\]
Check the action equations on D8 generators. These identities make the columns independent modulo boundaries and place them in \(W\); dimension32 then makes them a basis, proving separation. A specified nonzero32-column minor of \(FU\) can replace \(L\). Merely counting pivots without an authenticated matrix/domain is insufficient.

**Failure control and dependency.** Corrected \(R^\sharp\) and its regular transport require comments **6205127744/6205249609** and `research/hm/current-scalar-residual-attribution/closure-and-characters.md`. Sector membership concerns the complete class, not a local seed. No characteristic3 dimension claim follows.

Reviewer: **Codex-D01/Codex-V08**. Next step: review the above certificate when the sector lifts/action and detector restrictions become available. No arithmetic oracle, source evaluation, or rank computation was run.