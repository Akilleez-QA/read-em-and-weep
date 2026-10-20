# Independent review of the bounded joint model and its public dependency bindings

## Verdict and exact scope

**PASS for the two manuscripts at their stated mathematical scope and for the exact public theorem-binding closure.**

The first manuscript proves the conditional joint-DGLA secondary-class theorem, its formal countermodel, and the separate wrong-degree exclusion. The second proves a direct bounded equation model and its marked module-lifting groupoid comparison. The latter does not require, and does not establish, strict-DGLA rectification.

The closure resolves the former missing-public-reference hold. It is not an unconditional certification of every recursively inherited source premise. Source denotation, localization, characteristic-zero, coefficient-action marking, genuine equivariance and the specified external-product presentation remain exactly as required by the cited theorems. No selected source instance, historical checker, matrix, jet, detector or obstruction value was evaluated.

This is a current review of the following exact files, not reuse of the historical reviews embedded in the manuscripts.

| File | SHA256 |
| --- | --- |
| Unit 01, `corrected-mixed-secondary-class/PROOF.md` | `e6736426507ab8c0ab6fabeaa099dc08acd7f27b94149e43c7f0dc2bc91019d9` |
| Unit 02, `actual-joint-deformation-model/PROOF.md` | `2b3bac4150bc53a63ddfcd99351f38cdd5253d4c124b9a97fc820ba2e2f0d47f` |
| `JOINT-DEPENDENCY-CLOSURE.md` | `f48afab2ec4d427862d1638abadf1c2082627e37d320d41c78be02105800005c` |
| `JOINT-PUBLIC-PINS.json` | `a6f203e3ca9983491fadd30893a2c111eb3510b042e0c52a37c38d999e5679ba` |
| Replacement Unit 01 `DEPENDENCIES.md` | `36e1cf76c690a8099301b15092b342711dfeb41ef4a1fff84270c560541b79f8` |
| Replacement Unit 02 `DEPENDENCIES.md` | `3b2d740cc8dd566b1aa432cee87c4398c7496f180fb75aee3728f12111c8ba5c` |

## 1. Independent checks of the secondary theorem

In the stipulated DGLA extension, put \(R=\partial y+[x,z]\). Projection gives
\(p(R)=\partial c+[a,b]=0\), while the graded derivation identity and closedness of \(x,z\) give \(\partial R=0\). The mixed correction equation is consequently \(\partial t=-R\). Since \(x,z\) have degree one, their bracket is symmetric, and the two mixed contributions to \(\tfrac12[x+z,x+z]\) sum to \([x,z]\), not half that expression.

For simultaneous pure changes \(x\mapsto x+q\), \(z\mapsto z+r\), the complete change is

\[
[q,z]+[x,r]+[q,r].
\]

If \(q=\partial U\) and \(r=\partial V\), its primitive is

\[
[U,z]-[x,V]+[U,\partial V].
\]

The minus sign is forced by \(\partial[x,V]=-[x,\partial V]\). Thus pure kernel \(H^1\)-vanishing removes this ambiguity without removing \(R\). A closed change \(e\) of the ambient correction changes the class by the connecting class \([\partial E]\), for a lift \(E\) of \(e\). Ambient \(H^1\)-vanishing removes this ambiguity, whereas ambient \(H^2\)-vanishing supplies existence of ambient primitives. These are different assertions, and the manuscript preserves the distinction.

The representative change \(x'=x+\partial A\), \(y'=y-[A,z]\) preserves \(R\) literally. The corresponding statement for the second variable has the opposite displayed primitive sign, as required by its degree. The family-level bilinear conclusion retains the compatible fixed model and primitive-existence hypotheses; it is not deduced from rigidity alone.

The countermodel is a genuine DGLA: every nonzero bracket lands in central degree two, so Jacobi and the differential derivation identity hold. The pure kernel differentials are injective, the mixed kernel class \(w\) is not a boundary, and the unique pure closed lifts are \(A-u\), \(B-v\). Their bracket is \(w\). Setting only \([u,v]\) to zero preserves all stated linear/cohomological data but changes mixed solvability. This proves precisely the claimed formal insufficiency, not a realization on the geometric carrier.

For the independent degree exclusion, the three plane terms
\(H^{2-p}(\Omega^{2-p}_{\mathbf P^2})\), \(0\leq p\leq2\), are one-dimensional and all have Hochschild degree two. External Künneth therefore puts the nonzero tensor square of the corrected direction in degree four. Its characteristic image vanishes because the first arrow
\(E\to E\otimes M[2]\) is zero. The second arrow is correctly the action on \(E\otimes M\); no unsupported commutation of characteristic actions with tensoring by a line is needed. This degree-four class is not the degree-two mixed module obstruction.

## 2. Independent checks of the bounded equation model

The four ambient equations include multiplication associativity, overlap multiplicativity, the inner composition relation and the pentagon. The module equation has the correct row-left order

\[
F_{ij}(G_{jk})\star G_{ij}=A_{ijk}\star G_{ik}.
\]

Changing local row coordinates by \(v\mapsto v\star H_i\) gives
\(G'_{ij}=F_{ij}(H_j)^{-1}\star G_{ij}\star H_i\). This follows by substitution, without commuting coefficients.

The finite weight convolution retains every multiplication and overlap operation, including those acting on positive inputs. In mixed weight, either exactly one index is mixed or there is one index of each pure weight. Three positive indices cannot survive. The stated decomposition into the mixed module-linear term, the mixed ambient-linear term and the pure cross term is therefore exact.

Writing \(G^m_{ij}=g_{ij}x_{ij}\), left normalization gives

\[
\delta x=x_{ij}+g_{ij}^{-1}x_{jk}g_{ij}-x_{ik}.
\]

The coefficient transport in the middle term is retained. The ambient contribution has signs \(+\mu^m,+F^m,-A^m\), and the correction equation is \(\delta x=-R\).

The joint derivative has ambient components
\((b\mu,\delta\mu-bf,\delta f+ba,\delta a)\).
For an algebra gauge \(e\), its module gauge component is
\(\xi_{ij}=-g_{ij}^{-1}e_i(g_{ij})\).
Expanding \(be\) and \(\delta e\) makes the corresponding ambient contribution before normalization

\[
g_{jk}e_i(g_{ij})-e_i(g_{ik})+e_j(g_{jk})g_{ij}.
\]

Its normalized negative is exactly \(\delta\xi\). For an edge scalar gauge, \(\xi=b_{\rm edge}\operatorname{Id}\), while the triple-unit contribution is
\(-\delta b_{\rm edge}\operatorname{Id}\). Frame gauges contribute \(-\delta h\), whose next differential is zero. This checks \(d^1d^0=0\) independently of the nonlinear substitution argument.

At fixed genuine ambient, local finite free frames lose no module-action data. Every local module map is determined by its frame images; every locally free marked lift admits such frames. With the entire boundary fixed, frame-change arrows consequently give the claimed fully faithful and essentially surjective descent-groupoid comparison. This does not identify an unspecified simultaneous deformation 2-groupoid.

For \(L=F_{ij}(G_{jk})\star G_{ij}\), \(W=A_{ijk}\star G_{ik}\), the complete boundary equation makes \(D=L-W\) mixed-valued. Since the positive ideal annihilates that layer,

\[
W^{-1}\star L=1+g_{ik}^{-1}D
\]

holds literally. The quadruple comparison uses both the inner composition equation and the pentagon before reducing the four failures to their additive Čech sum. Thus \(\delta R=0\) requires no existing global mixed module. This proves equality with the complete gerbe representative in the fixed presentation, not just coincidence of zero sets.

Finally, the actual ambient correction solves an inhomogeneous equation. Only differences of genuine mixed extensions are ambient cocycles. Hence the cited \(HH^2(J)=0\) cannot justify deleting the actual correction or treating the pure cross term as separately closed.

## 3. Checked theorem-binding composition

The public bindings supply the exact strength used in the manuscripts:

- PR130, PR232 and PR404 supply effectiveness for supplied genuinely equivariant locally free objects with trivial root-transported classical inertia. PR404 uses invariant frames and finite quasi-coherent layers, not flatness of the covering algebra over its invariants. Arbitrary ramified equivariant modules remain excluded.
- PR131 supplies actual pair chart, overlap and scalar gauges, including existence of its unevaluated scalar primitive. PR235, PR131 §6 and PR404 §§4,7 retain the full external-product mixed multiplication, overlaps and triple units. Matching pure HKR classes alone is not substituted for this comparison.
- PR239 treats the complete prescribed transition \(U_r=g(s_{\rm raw,r}\operatorname{Id}+k_r)\). PR237 supplies finite-group effectivity only for a nonempty marked lifting problem; PR250 supplies the necessary pair-character rigidity. PR120 and PR121 supply corrected pure existence and marked uniqueness. Their comparisons agree on the fixed classical reduction and therefore assemble on the full boundary.
- PR252's structural appendix and corrected PR351 contain the same complete source residual and normalization. The corrected first-order equation includes the essential \(+U_{r,ik}\) term. PR351's erratum rejects the old omitted-term display. The common raw-engine and compiler hashes bind the mathematical denotation, not its execution.
- Complementary-factor support in PR79 and PR351 kills exactly the mixed weighted scalar-derivative terms. Substitution gives two ordered \(U\)-products, four pure multiplication/\(U\) terms, one mixed multiplication term and three negative gerbe terms. Their left normalization is the full \(M\), and \(R_{\rm raw}=\operatorname{tf}(M)+\delta W\). No isolated summand is used as the obstruction.
- PR123 supplies literal normalized root cancellation on the mixed defect. PR134 §4 then uses deck-equivariant pure-boundary rigidity and extension of a boundary gauge through the nilpotent ideal to identify the full obstruction classes. This proves \([R_{\rm raw}]=j(C)\), not equality of chosen raw and corrected cochains.
- The coefficient inverse \(j^{-1}\) uses \(\tfrac1{64}\operatorname{Tr}\) after multiplication by the two volume forms. The finite degree-six constant projector in PR133 and PR134 instead uses \(\tfrac16\operatorname{Tr}\). Neither is an endomorphism trace. PR134 transfers the alternating primitive on the geometric endomorphism cohomology, without requiring an \(S_4\)-action on the fixed paired ambient.
- PR402 and PR406 support the stated comparative limitations of ordinary traces and coefficient-free Atiyah commutators. They are not premises for the conditional DGLA algebra or its countermodel.

The foundation editions referenced through PR314, PR317, PR321, PR322, PR333, PR351 and PR362 keep their distinct roles. In particular contraction is not a determinant-one certificate, character membership is not cocycle closure, and a source registry is not a mathematical or runtime proof.

## 4. Edition verification and accepted publication changes

The revised registry contains **47 distinct commit/path/blob bindings**, with no duplicates. Each declared Git blob ID was independently reproduced from its materialized source content using the Git blob header and SHA1. Forty-six materializations had exactly one added terminal newline; removing that one byte reproduced the declared blob. PR404 matched without normalization. All 29 immutable links in the closure document occur in the registry.

Two precision issues found during review were corrected before the hashes above were frozen: duplicated PR132/PR237 registry entries, and a PR404 section pointer that now refers to §§4,7 for external products rather than §5's invariant-frame theorem. Neither required a mathematical change to either manuscript.

The accepted publication changes are the closure and pin appendices and the two precisely scoped dependency-page replacements. The two `PROOF.md` byte sequences remain unchanged. Historical audit hashes are historical and are not represented as hashes of these repackaged proofs.

No mathematical blocker remains for that bounded publication scope. The review does not release a strict-DGLA comparison, a family-wide secondary pairing, raw-cochain equality, source execution, a new obstruction value or vanishing theorem, a mixed primitive, pure diagonal conditions, higher-order quantization or algebraicity.
