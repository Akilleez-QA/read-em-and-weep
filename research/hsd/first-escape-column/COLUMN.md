# First-escape column

Documentation only. This file records routes already stated in the public route register and in the public thread of pull request 1. It does not compute a class, run a computer-algebra session, or certify that a Weil component is nonzero.

The starting checkout `add03476d9055aa00e1e00778eea6332cf8e01cc` does not contain the register. The live public copy is `research/history/route-register.md` at commit `1e3b5369ce21510f2d621d09b5cc27ca032f5961`. The checked update in that file (2026-10-10, 03:41 UTC) controls the Ext count and the ordinary Yoneda-square status. The 03:35 snapshot below it is history.

Pinned hypercohomology limit, from the public assertion on pull request 76 at commit `80ea7e98a09ef6c3f10285cb6d0eedc8bc7f979c`: the twist −2 differential \(d_5\) on the pinned four-term perfect complex

\[
C=[5\mathcal{O}(-1)\to 15\mathcal{O}\to 10\mathcal{O}(1)\to 2\mathcal{O}(2)]
\]

establishes \(a_2=0\) for the hypercohomology of \(\mathrm{End}(C)(-2)\). That assertion does not identify \(a_2\) or \(h^2\) with groups of \(\mathrm{End}(H)\). It is not a Weil-class certificate.

`excluded` means the stated construction or inference fails. It does not mean that a Weil class is non-algebraic. `unresolved` means the sources used here do not supply that cell.

Status of this file: amend applied; awaiting re-review.

## Caveats

**D1.** A Lefschetz projector is not the Chern character of a derived summand. Beauville eigen-components, isotypic projectors for finite groups of homomorphisms, and the Fourier transform on cycle classes stay inside the divisor-generated closure when they are induced by Lefschetz correspondences. Applying such a projector to a total Chern character does not compute the Chern character of an arbitrary derived summand.

**D2.** The Horrocks–Mumford carrier lives on an abelian fourfold. The Weil class lives on an eightfold. No fourfold-to-eightfold bridge and no class formula are supplied. This column does not assign a transported-hyperplane zero test to that carrier, and it does not tag the carrier with the specialization-deformation escape that would require that bridge.

**C1.** Chern-character closure under tensor, dual, and Hom holds for vector bundles and for derived or perfect \(K\)-operations. Underived coherent functors drop Tor and Ext. On a smooth surface, \(\mathrm{ch}(I_p)=1-[p]\), and the underived dual of \(I_p\) is \(\mathcal{O}\). The derived dual \(\mathrm{RHom}(I_p,\mathcal{O})\) keeps the \(\mathcal{O}_p\) partner that the underived dual loses.

**C2.** Missing transport between the fourfold and the eightfold remains unresolved.

An earlier escape list was not accepted as exhaustive. This column does not use that list as a set of row tags.

## Schema

Each entry is one audited route or operation.

| Field | Meaning |
|---|---|
| input variety | where the object lives before the step |
| output variety | where the object lives after the step |
| object | bundle, sheaf, complex, correspondence, or class |
| first uncontrolled operation | the first step not forced by Lefschetz correspondences or by a published theorem cited for that step |
| smallest nonzero-Weil certificate | what would prove that a nonzero Weil component escapes |
| status | `excluded`, `open`, `conditional`, or `n/a` |
| notes | short source limit; unresolved stays unresolved |

### Output-certificate row

Any independently justified nonzero Weil projection of the actual output class qualifies as a nonzero-Weil certificate. The positive scalar below, the Mr. Slop test **C**, is a useful sufficient test under its stated hypotheses. It is not an exclusive oracle.

At a very-general polarized split-Weil period with \(\mathrm{Hdg}^8(A,\mathbb{Q})=\mathbb{Q}\theta^4\oplus W\) and \(\theta W=0\), let \(V=\int\theta^8\) and let \(\alpha\) be the class of the actual selected algebraic output. Its Weil component \(w\) satisfies

\[
\Delta=V\int\alpha^2-\Bigl(\int\alpha\,\theta^4\Bigr)^2=V\int w^2.
\]

Hodge–Riemann positivity on primitive rational \((4,4)\) classes gives \(\Delta>0\) exactly when \(w\neq 0\). For an actual perfect complex \(E\) on this \(A\) with \(\mathrm{ch}(E)=P(\theta)+w\), take a line bundle \(L\) with \(c_1(L)=\theta\), or with \(c_1(L)\) a known nonzero multiple of \(\theta\), in this normalization. Nine distinct values of \(\chi(E\otimes L^m)\) then determine \(P\) and are blind to \(w\). The class-sensitive scalar is

\[
\chi(E,E)-\int P(-\theta)P(\theta)=\int w^2,
\]

with positive dual sign in degree eight. At a special period with extra primitive Hodge classes, \(\Delta\) needs a separate Weil projection before it is read as \(w\). A formal polynomial or a synthetic test vector is not this certificate.

An explicitly algebraic transport of a known special seed, together with a nonzero final Weil projection of the transported class, is another sufficient certificate. A row below supplies a certificate only when that row says so. Otherwise the certificate cell is `unresolved`.

### Mr. Slop audit labels

- **A.** Extraction universality. On a projective variety with an ample line bundle \(L\), every coherent sheaf admits a two-term presentation by finite sums of negative powers of \(L\) (Stacks tag `01QB`). On a smooth projective eightfold the same ampleness continues through nine terms in degrees \(-8,\ldots,0\). For \(K=H^{-8}(C)\) the truncation triangle is \(K[8]\to C\to F\to K[9]\), and the connecting class lies in \(\mathrm{Ext}^9(F,K)\). That group vanishes by amplitude: coherent Ext on a smooth projective eightfold vanishes in degrees above 8, so \(C\simeq F\oplus K[8]\). That splitting is the nine-term case. A two-term presentation has truncation triangle \(K[1]\to C\to F\to K[2]\), with connecting class in \(\mathrm{Ext}^2(F,K)\), which need not vanish. The relation used for that presentation is K-theory additivity \([C]=[F]-[K]\). The vanishing used above is the dimension bound. It is not Stacks tag `0FY7`, which is a Serre-functor example. Unrestricted extraction starts from an arbitrary \(F\) and manufactures no exceptional object. A proposal has to constrain the differential or the idempotent by a geometric condition independent of the desired class, and then compute the selected output's class.
- **B.** Split-Weil seeds on \(J\times J\). See the row with that label. A special-fiber divisor class is not a family class.
- **C.** The \(\Delta\) / \(\chi(E,E)\) scalar above. It is a sufficient test under the stated hypotheses, not a construction and not an exclusive oracle.

## Index

| Id | Status | Smallest nonzero-Weil certificate |
|---|---|---|
| Lefschetz closure | excluded | n/a inside the closure |
| A extraction | n/a | unresolved |
| B seeds on \(J\times J\) | conditional | unresolved for escape off \(A_0\) |
| C certificate template | n/a | sufficient \(\Delta\) / \(\chi(E,E)\) test |
| G1 net-count repair | excluded | unresolved |
| G2 ordered index 2 | excluded | unresolved |
| G3 essential-circle surgery | open | unresolved |
| G4 orientation cover | excluded | unresolved |
| G5 genus-two product | excluded | unresolved |
| G6 one gluing locus | excluded | unresolved |
| G6 graph columns | open | unresolved |
| A1 cyclic secant | excluded | unresolved |
| A2 invariant \(\mathrm{Ext}^1\) | excluded | unresolved |
| A3 line cones | conditional | unresolved |
| A4 literal secant sheaves | excluded | unresolved |
| A5 proportional-canonical ideals | excluded | unresolved |
| A6 Schoen ideal | excluded | unresolved |
| A7 line-power complexes | excluded | unresolved |
| A8 Horrocks–Mumford pullback | open | unresolved |
| A9 semiregularity shortcut | excluded | unresolved |
| Lange pullback | excluded | unresolved |
| Lange ribbon boundary | open | unresolved |
| Finite abelian covers of \(Q^4\) | excluded | unresolved |
| Primitive triple | excluded | unresolved |
| \(\tau=1\) maximal direction | excluded | unresolved |
| \(\tau=1\) quotient image | open | unresolved |
| Direct cycle families | open | unresolved |

## Rows

### Lefschetz closure

- **input variety.** A very-general polarized split-Weil eightfold \(A\) with Hodge group \(\mathrm{SU}(4,4)\), and powers of \(A\) and of its dual.
- **output variety.** The same powers.
- **object.** Classes generated from divisor classes by rational sums, cup products, exterior products, and pullback or Gysin pushforward along correspondences invariant under the Lefschetz group.
- **first uncontrolled operation.** None while the output stays in this closure. An uncontrolled extraction or a special-fiber deformation is not guaranteed to remain in the divisor-generated closure, and it does not necessarily leave it. No such step is carried out in this row.
- **smallest nonzero-Weil certificate.** n/a inside the closure. The Weil projection of every class that stays in the closure is zero. A nonzero certificate for an uncontrolled extraction or a special-fiber deformation is unresolved.
- **status.** excluded
- **notes.** Complexified Hodge group \(\mathrm{SL}_8\). Divisor classes have weight 0 for the central circle acting by \(z\) on an 8-plane and by \(z^{-1}\) on its dual; the Weil lines have weights \(\pm 8\). The public thread records this as a special case of Milne, Duke Mathematical Journal 100 (1999), Theorem 3.2, including the dual abelian variety, the Poincaré bundle, Beauville eigen-components, isotypic projectors, and Fourier–Mukai, because those operations preserve Lefschetz classes. The Todd class of an abelian variety is 1, so Grothendieck–Riemann–Roch stays in the closure when the Chern characters and the correspondence kernels do. **D1.** The row leaves a non-tautological producer untouched.

### A — extraction universality

- **input variety.** A projective variety with an ample line bundle; the nine-term form uses a smooth projective eightfold.
- **output variety.** The same variety.
- **object.** An arbitrary coherent sheaf \(F\), presented by a bounded complex of negative line-bundle powers, together with the accompanying syzygy or truncation kernel.
- **first uncontrolled operation.** Selecting one cohomology sheaf, a stable summand, or a projector without a geometric constraint on the differential or the idempotent that is independent of the desired class.
- **smallest nonzero-Weil certificate.** unresolved. The presentation manufactures no exceptional \(F\).
- **status.** n/a
- **notes.** Audit label **A**. Stacks tag `0ESY` gives Chern-character additivity on a distinguished triangle, \(\mathrm{ch}(E_2)=\mathrm{ch}(E_1)+\mathrm{ch}(E_3)\), and the termwise formula \(\mathrm{ch}(E^\bullet)=\sum_n(-1)^n\mathrm{ch}(E^n)\), so a shift contributes \(\mathrm{ch}(K[n])=(-1)^n\mathrm{ch}(K)\). A two-term presentation need not split as \(C\simeq F\oplus K[1]\). Its truncation triangle is \(K[1]\to C\to F\to K[2]\) (Stacks tag `08J5`); the connecting class lies in \(\mathrm{Ext}^2(F,K)\) and need not vanish. K-theory additivity on that triangle gives \([C]=[F]-[K]\) (Stacks section `0FJG`). When the presentation terms have zero exceptional part, \(w(F)=w(K)\), equivalently \(\mathrm{ch}_{\mathrm{exc}}(F)=\mathrm{ch}_{\mathrm{exc}}(K)\). For the nine-term complex in degrees \(-8,\ldots,0\), \(\mathrm{Ext}^9(F,K)=0\) by amplitude on the smooth projective eightfold (\(\mathrm{Ext}^{>8}=0\)), so \(C\simeq F\oplus K[8]\). The shift is even, and zero exceptional part on the terms gives \(\mathrm{ch}_{\mathrm{exc}}(F)=-\mathrm{ch}_{\mathrm{exc}}(K)\). That isomorphism makes \(F\) a derived retract of \(C\). The vanishing is amplitude, not Stacks tag `0FY7`. Two-term presentations are Stacks tag `01QB`.

### B — split-Weil seeds on \(J\times J\)

- **input variety.** A polarized abelian fourfold \(J\).
- **output variety.** The decomposable eightfold \(A_0=J\times J\).
- **object.** For \(K=\mathbb{Q}(s)\) with \(s^2=-d\) and \(d>0\) squarefree, the Rosati-skew map \(q(x,y)=(-d\, y, x)\) and the divisor polynomials \(R=D^4-6d\, D^2 P^2+d^2 P^4\) and \(I=4D^3 P-4d\, D P^3\), with \(P=m^*\theta_J-\theta_1-\theta_2\) and \(D=\theta_1-d\theta_2\). The polarization \(\theta_1+d\theta_2\) makes the signature \((4,4)\).
- **first uncontrolled operation.** Algebraic transport of \(R\) and \(I\), or of a divisor class that remains Hodge on the whole target family, from this decomposable \(A_0\) to a very-general simple split-Weil eightfold.
- **smallest nonzero-Weil certificate.** unresolved for escape off \(A_0\). On \(A_0\) itself, \((D+sP)^4=R+sI\) is recorded as a nonzero class in the eigen determinant line, and \(R,I\) span the Weil plane of this special fiber. That special-fiber statement is not the escape certificate.
- **status.** conditional
- **notes.** Audit label **B**. An isogeny does not carry this decomposable \(A_0\) to a very-general simple target. Individual divisor factors of \(R\) and \(I\) need not remain Hodge on a general Weil deformation. **C2.** A special-fiber divisor class is not a global rejection rule and is not a family algebraicity theorem.

### C — output-certificate template

- **input variety.** A very-general polarized split-Weil eightfold, under the Hodge hypothesis in the schema.
- **output variety.** The same eightfold.
- **object.** The actual selected algebraic output, or an actual perfect complex on that eightfold.
- **first uncontrolled operation.** n/a. This row is the certificate. Treating \(\Delta>0\) at a special period, or substituting a synthetic vector, is a misuse of the test.
- **smallest nonzero-Weil certificate.** Any independently justified nonzero Weil projection. Under the hypotheses in the schema, including \(c_1(L)=\theta\) or a known nonzero multiple of \(\theta\), the positive scalar \(\Delta=V\int w^2\), equivalently \(\chi(E,E)-\int P(-\theta)P(\theta)=\int w^2\), is a sufficient test. An algebraic transport of a known special seed with nonzero final Weil projection is another sufficient certificate.
- **status.** n/a
- **notes.** Audit label **C**. The displayed scalar is not an exclusive oracle. No row below supplies a computed value of this scalar.

### G1 — net-count repair

- **input variety.** unresolved as a named algebraic variety. The recorded object is the stabilization trace in the withdrawn eightfold argument.
- **output variety.** The same trace after a proposed change of Euler characteristic, including connected sum with \(S^3\times S^5\).
- **object.** The ordinary forward trace and its signed double-point count.
- **first uncontrolled operation.** Repairing only the net index count. The cited cancellation theorems do not remove the bad local generator at an interior maximum of a nonempty compact superlevel.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** Register G1, retired for this trace construction. Foundations recorded there: Eliashberg–Murphy, Theorem 2.3, and the EEMS stabilization lemma. The original sign correction remains the withdrawal notice: each reverse trace contributes \(-1\), and the count is \(-2m\), not zero.

### G2 — no ordered index 2

- **input variety.** unresolved as a named algebraic variety. The recorded object is the ordinary-ball trace.
- **output variety.** The same trace.
- **object.** A bounding cochain for the graded trace. For \(n=8\) the forward cusp indices are \(\{2,6\}\).
- **first uncontrolled operation.** A local implementation that would remove ordered index 2. Global regrading does not change self-intersection indices.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** Register G2. The abstract zero-bounding-cochain criterion is a valid gate under its stated Calabi–Yau hypotheses. The ordinary-ball implementation fails. Source recorded in the register: Akaho–Joyce, Propositions 12.2 and 13.10. Different geometry is not ruled out by this row.

### G3 — essential-circle surgery

- **input variety.** unresolved as a named algebraic variety. The recorded local model is essential-circle Lagrangian surgery.
- **output variety.** unresolved. A global finite-area surgery neighborhood was not constructed.
- **object.** An embedded surgery neighborhood compatible with the immersion, the grading, the homology, and the periods.
- **first uncontrolled operation.** Supplying that neighborhood. A thin isotropic core with formal framing does not supply it.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** open
- **notes.** Register G3. After the branch-label correction, the local index matches the forward cusp; the alleged action-order mismatch is withdrawn. A blanket placement principle is not promoted to a no-go here. Source recorded in the register: Hicks, Lagrangian cobordisms and Lagrangian surgery.

### G4 — orientation cover

- **input variety.** unresolved as a named algebraic variety. The recorded construction is a nonorientable surgery followed by its orientation cover.
- **output variety.** A torus, via an invariant composite map.
- **object.** The top class and the required nonzero \(\nu\alpha\).
- **first uncontrolled operation.** Using the orientation-reversing deck involution to produce \(\nu\alpha\). The rational pushforward of the top class is zero.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** Register G4. The obstruction is homological and applies to this escape only.

### G5 — genus-two product

- **input variety.** A genus-two building block.
- **output variety.** The product of four copies of that surface.
- **object.** The product class, compared with the target class \(\Omega\).
- **first uncontrolled operation.** Placing the full target \(\Omega\) inside the product's contraction kernel by a real linear change, a scaling, or an isogeny.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** Register G5. The embedded spin Maslov-zero genus-two block is recorded as genuine. The product has Euler characteristic 16, first Betti number 16, and \(b_2=b_6=100\), with contraction-kernel dimension 20, against a target specification of 16. Sources recorded in the register: Abouzaid–Smith, and Hicks, Examples 4.2.5 and 4.2.9.

### G6 — one clean gluing locus

- **input variety.** The product class of the preceding row.
- **output variety.** The same ambient manifold after one codimension-two gluing.
- **object.** The resulting \(H^2\) restriction and the \(H_6\) kernel.
- **first uncontrolled operation.** Killing the required \(H^2\) classes with one connected gluing locus. Killed classes lie in the span of the gluing-divisor classes.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** Register G6, for one connected locus. The recorded count asks for at least eight independent divisor classes, and the natural splitting asks for twelve cross-factor directions. Mak–Wu, Corollaries 2.22 and 4.13, grade an existing clean pair; they do not construct this configuration.

### G6 — graph columns

- **input variety.** The same product class.
- **output variety.** unresolved. Simultaneous plumbing was not constructed.
- **object.** Proposed graph columns in one model of degree 1.
- **first uncontrolled operation.** Overlapping supports, simultaneous plumbing, grading, and unobstructedness. The register records that the columns span the required directions in that one model, and records the rest as open.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** open
- **notes.** Register G6. No same-sign graph-orientation no-go is claimed.

### A1 — corrected cyclic secant

- **input variety.** The polarized abelian variety of the literal cyclic secant complex.
- **output variety.** The same variety.
- **object.** The corrected partial-normalization object. The recorded character uses \(\mathcal{O}(3\Theta)\). The literal \(\mathcal{O}(\Theta)\) printed in the cited secant section is the line bundle that correction replaces.
- **first uncontrolled operation.** Deforming that corrected object. The character correction itself is a change of line bundle. The recorded node calculation is a further research test: a class \(\xi=\pi+d\Pi\) annihilates the Chern character, while its evaluation at a normalized isolated node is nonzero.
- **smallest nonzero-Weil certificate.** unresolved. A nonzero evaluation on a tangent is not the output-certificate row.
- **status.** excluded
- **notes.** Register A1, for this corrected object and this symmetry architecture. For odd \(d\ge 3\), the recorded \(h^2\) bounds are greater than 28 and reject full semiregularity. They do not by themselves reject the weak image criterion. Orlov transport of the paired class is recorded as producing a polarized Weil tangent with nonzero evaluation. New objects and unrelated autoequivalences are outside this exclusion. Source recorded in the register: Markman, version 2, section 12.

### A2 — invariant Ext¹ as translations and Picard twists

- **input variety.** The cyclic-curve smoothing of the secant object.
- **output variety.** The same variety.
- **object.** The claim that invariant \(\mathrm{Ext}^1\) is exhausted by translations and Picard twists.
- **first uncontrolled operation.** That exhaustion. A global cyclic-curve smoothing tangent has nonzero local \(T^1\). The recorded local model is the Hilbert–Burch deformation of the ideal \((ac,bc,bd)\).
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** Register A2, retired. First-order lifting of the local model was recorded as checked. All-order global gluing was not, and this row does not promote the tangent to a carrier.

### A3 — ample-line cones

- **input variety.** The obstructed secant object.
- **output variety.** The same variety, after a line-bundle cone or a finite tower of such cones.
- **object.** Cones on the literal Orlov normalization.
- **first uncontrolled operation.** A cone orientation, or an extension, whose relevant Ext groups do not vanish. In the tested orientations the evaluation is controlled by naturality.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** conditional
- **notes.** Register A3. Sufficiently negative line additions split for the literal Orlov normalization. Sufficiently positive, correctly \(B\)-twisted additions in the tested triangle orientation preserve the nonzero evaluation, and the same bounds propagate through finite towers. Other orientations remain open. The preserved evaluation is not a Weil-class certificate.

### A4 — literal secant sheaves

- **input variety.** The abelian variety carrying the free-point ideal family, and the theta-supported example.
- **output variety.** The same variety.
- **object.** The literal sheaves of Markman, Example 8.2.3 and Example 8.2.4.
- **first uncontrolled operation.** A Poisson deformation of the free-point ideal, which would deform the skyscraper quotient, and star-composition of the local resolution in the theta-supported example.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** Register A4, for these literal carriers. The partial-normalization alternative is the node obstruction of A1. The theta-supported star-composition is recorded as a nonzero constant degree-two class with vanishing boundaries at the point. Other point-modified or divisor-supported sheaves are outside this exclusion. Source: Markman, version 2, those two examples.

### A5 — proportional-canonical surface ideals

- **input variety.** The polarized abelian variety with polarization \(\theta\).
- **output variety.** The same variety.
- **object.** \(I_Z(a\theta)\) for \(Z\) a complete intersection of \(b\theta\) and \(c\theta\), and more generally a tested smooth-surface ideal whose canonical class is proportional to \(\theta\) restricted to the surface.
- **first uncontrolled operation.** Matching the required character. The recorded numerical conditions force \(b=c\) and \(d=-b^2/4<0\), or \(a^2+9d=0\).
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** Register A5. Neither family realizes \(d>0\). Smooth surfaces with an independent canonical class are outside these tests.

### A6 — Schoen-surface ideal

- **input variety.** The ambient variety in which the Schoen surface is a holomorphic Lagrangian for a nonzero holomorphic two-form \(\Omega\).
- **output variety.** The same variety, including isogeny pullbacks of this realization.
- **object.** The proposed ideal-carrier cycle.
- **first uncontrolled operation.** The cycle identity that would identify the class with a positive multiple of \(\theta^2\).
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** Register A6. The integral of \(\Omega\wedge\overline{\Omega}\) vanishes, while the proposed positive multiple of \(\theta^2\) has positive integral. This excludes the ideal-carrier realization, not every use of Schoen classes. Source recorded in the register: Ciliberto–Mendes Lopes–Roulleau, On Schoen surfaces.

### A7 — signed-twist monad and three-term line powers

- **input variety.** The polarized abelian variety with one ample line bundle \(L\).
- **output variety.** The same variety.
- **object.** The numerical monad \(L^{-1}{}^{\oplus 8}\to \mathcal{O}^{\oplus 18}\oplus L^2\oplus L^{-2}\to L^{\oplus 8}\), and nonzero complexes in three consecutive degrees whose terms are powers of one ample line bundle with \(\mathrm{Pic}^0\) twists, after constant-block cancellation.
- **first uncontrolled operation.** Compensated Poisson evaluation on the maximal \(L^2\) summand, and, in the three-term family, survival of \(H^2(\mathcal{O})\) on that summand. Numerical character matching was not an exact-ended construction. An incoming lower-power differential in a fourth column is outside the three-term family.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** Register A7, within the stated amplitude. Equal maximal summands are not acyclic, and their relevant \(d_2\) vanishes. Longer complexes and non-line middle bundles remain outside this exclusion and are not given a construction here.

### A8 — Horrocks–Mumford pullback

- **input variety.** \(\mathbb{P}^4\), carrying the normalized Horrocks–Mumford bundle \(H\), with \(c_1=-h\) and \(c_2=4h^2\).
- **output variety.** An abelian fourfold. The explicit seed is a product of elliptic curves. The register's Chern-character statement uses a finite map given by five sections of \(\mathcal{O}(2m\Theta)\).
- **object.** The rank-two bundle \(E=f^*H\otimes\mathcal{O}(m\Theta)\). The register records \(c_1=0\), \(c_2=15m^2\theta^2\), and \(\mathrm{ch}(E)=2\operatorname{Re}\exp(i\sqrt{15}\, m\theta)\), over \(\mathbb{Q}(\sqrt{-15})\). The separate elliptic-product seed used for the Ext count is \(f^*H\otimes N\) on the product of the curve \(y^2=x^3-x\). This row does not identify that twist with \(\mathcal{O}(m\Theta)\).
- **first uncontrolled operation.** Transport from this fourfold carrier to an eightfold object and its class formula. No such formula is supplied. On the fourfold, the ambient second-order obstruction remains uncomputed; that gap is separate from the Weil certificate.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** open
- **notes.** Register A8, active as a fourfold carrier with restricted first-order success. The checked register update records Ext dimensions \((1,87,7372,87,1)\) and vanishing of ordinary fixed-base Yoneda squares, given the smooth 87-dimensional fixed-base family and its Kodaira–Spencer isomorphism. That vanishing is not ambient all-order unobstructedness. **D2** and **C2:** no transported-hyperplane zero test, and no specialization-deformation tag. The \(d_5\) assertion at `80ea7e98` is \(a_2=0\) for \(\mathrm{End}(C)(-2)\) on the pinned complex, not for \(\mathrm{End}(H)\). Stability and simplicity of the pullback are cited from Biswas–Das–Parameswaran, Theorem 2.5. The classical bundle is the Horrocks–Mumford construction.

### A9 — semiregularity and hyperholomorphic shortcuts

- **input variety.** The fourfold of the normalized Horrocks–Mumford seed.
- **output variety.** The same fourfold.
- **object.** \(\mathrm{End}(E)\) for the simple normalized seed, and the literal Orlov self-pair.
- **first uncontrolled operation.** Invoking ordinary semiregularity, an unchanged hyperholomorphic theorem for stable or reflexive sheaves, or the sufficient base-dimension criterion recorded in the register. The recorded numbers put \(\chi(\mathrm{End})=7200\) and \(h^2=7198+2h^1\), above the fourfold target dimension 28, and the literal Orlov self-pair has cohomology in more than one degree.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** Register A9. These shortcuts are unavailable as stated. Failure of a sufficient criterion is not an obstruction theorem, and it does not close A8.

### Lange pullback

- **input variety.** \(\mathbb{P}^1\times\mathbb{P}^3\), with classes \(u=c_1\mathcal{O}(1,0)\) and \(v=c_1\mathcal{O}(0,1)\).
- **output variety.** An abelian fourfold admitting a finite map to \(\mathbb{P}^1\times\mathbb{P}^3\). The explicit seed is a product of a principally polarized elliptic curve and a principally polarized abelian threefold.
- **object.** \(E=f^*F\) with \(F=V(-1,-2)\), where \(V\) is the rank-two bundle with \(c_1(V)=2u+4v\) and \(c_2(V)=8uv+6v^2\). Then \(\det F=\mathcal{O}\) and \(c_2(F)=2(u+v)^2\). For \(m\ge 3\), the product seed has \(\det E=\mathcal{O}\), \(c_2(E)=2m^2\theta^2\), and Chern character \(\exp(m\sqrt{-2}\,\theta)+\exp(-m\sqrt{-2}\,\theta)\).
- **first uncontrolled operation.** Extension off the 7-dimensional product polarized locus in the three transverse polarized directions. Existence of the finite product maps and \(\theta\)-stability on that locus are the cited theorems. The transverse mixed Atiyah evaluation is the research calculation.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** [Pull request 21](https://github.com/Akilleez-QA/read-em-and-weep/pull/21) records the field-two seed. [Pull request 26](https://github.com/Akilleez-QA/read-em-and-weep/pull/26) excludes every finite abelian-fourfold pullback of an original Lange bundle: evaluation rank 15, kernel dimension 13, against a 16-dimensional character annihilator. [Pull request 28](https://github.com/Akilleez-QA/read-em-and-weep/pull/28) is the independent exact re-verification of that rank. Isogeny pullback and descent preserve that obstruction, as stated with the exclusion. The product seed changes the discriminant square class from 15 to 2 and still lies under the full-semiregularity exclusion. Sources: Lange, Proposition 3.1; Biswas–Das–Parameswaran, Theorem 2.5. This row does not evaluate the Horrocks–Mumford ambient obstruction. **C2.**

### Lange ribbon boundary

- **input variety.** \(\mathbb{P}^1\times\mathbb{P}^3\), on the vertical boundary of the stable ribbon component.
- **output variety.** unresolved
- **object.** unresolved. The recorded remaining case is a constant double-line ruling together with a generically curvilinear vertical plane of multiplicity four.
- **first uncontrolled operation.** unresolved
- **smallest nonzero-Weil certificate.** unresolved
- **status.** open
- **notes.** Leftover case in Mr. Slop's carrier note on pull request 1: a constant double-line ruling together with a generically curvilinear vertical plane of multiplicity four ([comment 6094109126](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6094109126)). No full component classification was claimed. This row is that leftover case, not a new construction.

### Finite abelian covers of \(Q^4\)

- **input variety.** The smooth quadric fourfold \(Q^4\), where the spinor or Cayley bundle lives.
- **output variety.** An abelian fourfold \(A\), where that bundle would be pulled back.
- **object.** The spinor or Cayley bundle on \(Q^4\). Pullback along a finite map \(A\to Q^4\) would place it on \(A\).
- **first uncontrolled operation.** n/a. The route stops at existence of the finite morphism.
- **smallest nonzero-Weil certificate.** unresolved. No object on \(A\) is produced.
- **status.** excluded
- **notes.** Two directions. The bundle starts on \(Q^4\) and would be pulled back to \(A\) along \(A\to Q^4\). The finite morphism in the other direction, from the abelian fourfold onto \(Q^4\), is excluded by Demailly–Hwang–Peternell, Theorem 1.1 ([arXiv:0707.0581](https://arxiv.org/abs/0707.0581)). The exclusion at morphism existence is the statement in Mr. Slop's carrier update on pull request 1 ([comment 6094109126](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6094109126)). This row is not the Horrocks–Mumford deck cover of projective space.

### Primitive triple

- **input variety.** \(\mathbb{P}^1\times\mathbb{P}^3\).
- **output variety.** The same variety. The embedded primitive triple on the fixed support was not obtained.
- **object.** An embedded ribbon on the graph Segre \(\mathbb{P}^1\times\mathbb{P}^1\subset\mathbb{P}^1\times\mathbb{P}^3\) with conormal \(\mathcal{O}(-2,1)\), proposed as a \(c_2=3(u+v)^2\) Serre construction.
- **first uncontrolled operation.** Extension of that ribbon to an embedded primitive triple. The abstract triple-extension obstruction group vanishes, so the vanishing is not the embedded obstruction. The recorded obstruction is a nonzero binary quintic read from the ambient coordinate transition.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** [Pull request 24](https://github.com/Akilleez-QA/read-em-and-weep/pull/24), for this fixed graph Segre support. Other supports, and other rank-two bundles with those Chern classes, stay outside. The row does not evaluate the Horrocks–Mumford ambient obstruction.

### \(\tau=1\), maximal direction

- **input variety.** \(\mathbb{P}^1\times\mathbb{P}^3\).
- **output variety.** unresolved. The mixed-Atiyah and finite-pullback test was not reached.
- **object.** A charge-three non-instanton monad with one minimal middle-type jump \(\tau=1\), moving-plane quotient \(U=\mathcal{O}(2)\oplus\mathcal{O}(1)^2\), and constant symplectic coefficient \(W=\mathcal{O}^2\), in the case where the exceptional section lies in the canonical maximal-degree line of \(U\).
- **first uncontrolled operation.** Nonsplit central gluing and isotropy, including the quadratic symplectic transition correction and the doubled exceptional ideal. A genuine local \(\tau=1\) smoothing is recorded, and a globally split rank-six middle cannot compactify it with these twists. Solving only the linear column-gluing stage is not the full gate.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** excluded
- **notes.** [Pull request 53](https://github.com/Akilleez-QA/read-em-and-weep/pull/53) records the corrected central criterion and this maximal-direction exclusion. [Pull request 59](https://github.com/Akilleez-QA/read-em-and-weep/pull/59) reviews the \(164\times 138\) matrices of rank 137. The exclusion is for every actual primitive presentation in this maximal direction. Restriction to \(\mathbb{P}(\mathcal{O}(1)^2)\) forces a constant common factor of the two intrinsic quadrics, and ordinary surjectivity fails. Replacing the doubled ideal by its radical loses conditions. The quotient-image direction is the next row.

### \(\tau=1\), quotient image

- **input variety.** \(\mathbb{P}^1\times\mathbb{P}^3\).
- **output variety.** unresolved
- **object.** The same charge-three family with exceptional section of nonzero image in \(U_0/\mathcal{O}(2)_0\).
- **first uncontrolled operation.** unresolved as a global monad. Full central compatibility, ordinary rank, and exceptional-fiber rank were left as gates for this quotient-image direction.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** open
- **notes.** The maximal-direction rank is not a classification of this direction. No Weil projection is supplied. Boundary, omitted from this column rather than promoted: formal construction and algebraization near \(D\) have been recorded, while the actual global \(R\) presentation, identification, and defect remain unresolved ([comment 6117584496](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6117584496)). That partial result is not a global certificate.

### Direct algebraic-cycle families

- **input variety.** unresolved
- **output variety.** unresolved
- **object.** unresolved. The register names moduli, Prym or cyclic-cover, direct Kuga–Satake, determinant-cycle, and arithmetic routes only as a class of missing families.
- **first uncontrolled operation.** unresolved. A genuinely dominating family was not supplied. Density of special or CM points, and algebraicity on a special fiber, are recorded as insufficient for spreading or lifting.
- **smallest nonzero-Weil certificate.** unresolved
- **status.** open
- **notes.** Register, open branch on direct algebraic cycle families. No construction is added here. **B** remains the only explicit special seed in this column, and its transport is unresolved.

## What stays out

Longer line complexes, non-line middle bundles, nonexternal Fourier–Mukai kernels, several clean Lagrangian loci, tropical or generating-family geometry, filtered Maurer–Cartan proposals, and a \(\tau=2\) quotient are named in the sources as outside the exclusions above or as separate unfinished work. They are not given rows in this column. That omission does not cover the recorded boundary near \(D\): formal construction and algebraization near \(D\) have been recorded, and the actual global \(R\) presentation, identification, and defect remain unresolved ([comment 6117584496](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6117584496)). That partial result stays omitted from this column and is not a global certificate.

The ordinary fixed-base Yoneda-square vanishing for the Horrocks–Mumford seed is a fourfold statement from the checked register update. It is not a value of \(\int w^2\) on an eightfold.
