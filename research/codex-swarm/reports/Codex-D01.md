> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-D01 — **certificate specification; obstruction undecided.**

At pin `08b73637d4136f91606aad332c46cafd064417f8`, let \(Q^\bullet\) be the characteristic-zero full-sign finite complex in `research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js`, with
\[
B:Q^1\to Q^2,\quad C:Q^2\to Q^3,\qquad
(\dim Q^1,\dim Q^2,\dim Q^3)=(2560,6560,4080).
\]
Assume the geometric stabilizer/choice-independence hypotheses of comments **6130306841/6130352358** and dimension certificate **6130391535**. Then the corrected \(R^\sharp\) represents a class in \(H^2(Q)[\varepsilon]\), of dimension **32**. This makes no characteristic-three claim.

**New hand-derived rank obstruction.** Write the genuine transferred action and projector as
\[
R_g=P_A\rho(g)I_A,\qquad
E=\tfrac18\sum_{g\in D_8}\varepsilon(g)R_g.
\]
For every boundary-annihilating row \(\ell\),
\[
[(\ell R_g)E]=\varepsilon(g)[\ell E]
\]
as functionals on cohomology. Thus the D8 translates of the known detector have restricted rank **at most one**, regardless of their cochain support. The 78 staircase seeds in **6205341120** expand that single functional; they supply no additional independent rows. Its restricted rank is currently **0 or 1**, not established here.

A useful failure control: the witness in **6104478488**, supported on constant positive coordinates \(z[7],z[23],z[50]\), is permutation-invariant. Indeed its harmonic inclusion has Čech degree zero, so \(H\Delta i=0\), and factor permutations fix its coefficient matrices and constant sections. Its nonzero pairing proves the detector nonzero on the **trivial** component; it does not prove nonzero restriction to ε.

**Complete-dual acceptance contract.** Supply exact rational cycles \(Z=(z_1,\ldots,z_{32})\) and rows \(F=(f_1,\ldots,f_{32})^t\), satisfying
\[
CZ=0,\qquad EZ-Z=BU,\qquad FB=0,\qquad FZ=I_{32}.
\]
Under the stated dimension premise these identities prove that the rows separate every ε class. For an authenticated finite representative \(v\) of the **complete corrected** \(R^\sharp\), require \(Cv=0\) and \([Ev]=[v]\). Then
\[
[v]=0\iff Fv=0.
\]
Any nonzero entry of \(Fv\) gives a boundary-annihilating nonvanishing certificate. An explicit boundary alternative is \(v=Bx\), checked in both negative and positive blocks, including the length-five contribution.

**Minimal missing executable inputs.**

- Signed factor permutations \(\rho(a),\rho(b),\rho(c)\), with \(a=(12),b=(34),c=(13)(24)\), on the genuine regular tensor Čech model, including Koszul signs.
- Correct perturbed maps
  \(I_A=(1+H\Delta)^{-1}i\), \(P_A=p(1+\Delta H)^{-1}\), and their authenticated coordinate binding. Comment **6140937153** supplies the convention; the inspected oracle exports transfer maps, not instantiated D8 actions.
- Checks that these are chain maps and induce the group laws/projector on cohomology. Strict cochain idempotence must not be assumed.
- The 32-cycle/dual certificate and authenticated source-to-\(v\) comparison retaining owners, frames, and the corrected gerbe baseline (**6205127744/6205660472**).

Old published results supply dimension32 and one detector. The orbit-rank bound, witness-sector distinction, and acceptance contract above are this report’s deductions. No oracle, physical coefficients, or matrix calculations were run. Independent review remains **Codex-D02/Codex-V07**. Next step: authenticate the action interface before requesting any restricted-rank computation.