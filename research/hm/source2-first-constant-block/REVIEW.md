# Independent audit: the first constant source2 block

## Verdict and reviewed version

**PASS, conditional on the published actual-source inputs explicitly stated in the proof.** The argument proves a necessary constant, G-equivariant separation of the degree-ten block of every hypothetical actual source2 inclusion satisfying those inputs. It then reconstructs a genuine simultaneous direct summand of the fixed original negative multiplication pencils, not merely an abstract pencil with matching characters. Its added Section 8 correctly combines this normal form with PR789 to give exactly two abstract full constant-gauge orbits over each balanced endpoint.

Reviewed artifact: `PROOF.md` in this directory.

Reviewed proof SHA-256:

`0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4`

No mathematical correction is outstanding in these reviewed bytes. The conclusion remains a necessary condition: neither existence of the asserted idempotents for the fixed HM tensors nor exclusion of source2 is decided. The residual R is not proved to split constantly. This is a written mathematical audit, not proof-assistant certification.

## 1. The actual inputs and the graph description

The pinned PR744 and PR751 statements supply more than numerical splitting data. They provide the genuine invariant constant spaces V0 and V1, the exact intersections with their constant bundles, and the locally free quotients required for both constant projections. The PR751 osculation argument identifies A0 with the actual complete degree-eight second osculating bundle, not just an abstract bundle of the same character and degree. PR758 confirms the corresponding projected backward flag.

Consequently, after choosing an equivariant constant complement Hbar to V0, the inclusion Q*/U projects isomorphically onto its actual image R in Hbar O. Inside

`(H* O)/U = Z direct-sum Hbar O`

it is therefore the graph of a unique bundle map beta:R->Z. This description does not choose a horizontal splitting of the extension R or transport a connection onto an abstract complement. It uses an actual constant representation complement, which is permitted by finite-group semisimplicity.

The apolar conventions are correct. For a parameter line ell,

`ann(ell^(e-j) Sym^j W) = ell^(j+1) Sym^(e-j-1) W`.

Thus ann(U_8^10)=U_1^10=W O(-9), and its dual is

`Z=(V0 O)/U_8^10 = W O(9)`.

Here the invariant symplectic identification of W and W* is used. In particular Z has rank two and degree eighteen. It is not U* and must not be used as the quotient block of Q in the later cohomological reconstruction.

## 2. The coupling space is exactly one-dimensional

The three character identities used in Section 2 are correct. They can be obtained from the binary-icosahedral W-tensor rules and the universal recurrence

`Sym^(n+1) W = W tensor Sym^n W - Sym^(n-1) W`.

In the notation of the proof, the needed W-tensor rules include

`W tensor A = W+S`,
`W tensor S = A+D`,
`W tensor D = S+T`,
`W tensor T = D+P+V`,
`W tensor P = T+W'`,
`W tensor V = T`, and `W tensor W' = P`.

They give Sym^15 W=S+2T and Sym^27 W=W'+2S+3T. Since all the coefficient representations in question are self-dual, there is no W constituent in Sym^27 W and exactly one S constituent in Sym^15 W. Hence

`Hom_G(O(-18),W O(9))=0`,
`Ext^1_G(O(-18),W O(9))=0`,
`dim Hom_G(A O(-6),W O(9))=1`.

The Ext vanishing follows directly from H1(O(27))=0, not from a presumed splitting of R in its constant ambient bundle. Taking G-invariants is exact in characteristic zero for this finite group. The Hom long exact sequence for 0->A0->R->C->0 therefore makes restriction an isomorphism

`Hom_G(R,Z) -> Hom_G(A0,Z)`.

This is the precise reason that killing the coupling on A0 will kill the entire first coupling, including any possible behavior on the final line quotient.

## 3. The five-section jet argument is pointwise and sufficient

The unique D projections of Sym^8 W and Sym^10 W dualize to five-dimensional systems of independent sections. The nonzero projection is surjective onto D, so its dual indeed has dimension five. A nonempty common base divisor would be invariant under the projective A5 action and have degree at least twelve. Its degree is at most eight or ten, respectively, so both systems are basepoint-free.

For a five-section system in O(d), the Wronskian is a nonzero section of a line bundle of degree

`5d + (0+1+2+3+4) deg Omega = 5(d-4)`.

The characteristic-zero independence of the sections guarantees that this Wronskian is not identically zero. At any point, failure of second-jet spanning means a2>=3. Since the vanishing sequence is strictly increasing and starts at zero, its Wronskian weight is at least

`(3-2)+(4-3)+(5-4)=3`.

The failure condition and its weight are invariant. An entire orbit would therefore contribute at least 36, exceeding both possible total Wronskian degrees, 20 and 30. This proves second-jet spanning everywhere, not only at a generic point or outside the exceptional orbits.

It follows that the projected maps U_j^d->D O for j<=2 are fiberwise injective. Their images J_j^d are consequently saturated subbundles, with the stated ranks and degrees. In particular J_2^8 is a rank-three degree-minus-eighteen subbundle, J_1^8 has degree minus fourteen, J_1^10 has degree minus eighteen, and J_2^10 has degree minus twenty-four.

The two Gauss identities used later also follow. For J_2^8, the Wronskian ensures generic independence through third order, so its second fundamental form has generic rank one. Its kernel contains J_1^8. Both are saturated in J_2^8, and their ranks agree, so the kernel equals J_1^8 as a sheaf. Possible third-jet ramification does not add a torsion-supported kernel to a morphism between locally free sheaves. For J_1^10, second-jet spanning everywhere gives its saturated forward transform exactly J_2^10.

These arguments use arbitrary-point vanishing sequences and universal bundle degrees. No representative of an actual source orbit or actual derivative value is needed.

## 4. The nonzero D shear and the annihilator degree signs

The invariant apolar pairing on Sym^10 W restricts nondegenerately to its unique D constituent. Indeed nonisomorphic self-dual irreducibles pair orthogonally, and a degenerate restriction to the unique D would contradict nondegeneracy of the whole pairing. The intersection with U is therefore

`K = D O intersect U_8^10 = ann_D(J_1^10)`.

Since J_1^10 is a saturated rank-two subbundle, the pairing gives an exact sequence

`0 -> K -> D O -> (J_1^10)* -> 0`.

Thus K is saturated of rank three and degree minus eighteen. The sign in the proof is correct: the quotient has degree plus eighteen, so K has degree minus eighteen.

If the constant D-channel map T0 vanished on A0 modulo U, its image I=J_2^8, transported by the nonzero constant D intertwiner, would be contained in K. Both are rank-three subbundles of degree minus eighteen. The quotient of this equal-rank inclusion is torsion of degree zero and is therefore zero. Alternatively their saturation in the same constant bundle already forces equality.

Such equality is impossible. The backward kernel of I has rank two and degree minus fourteen. For K, differentiating the constant pairing shows

`K^- = ann_D((J_1^10)^+) = ann_D(J_2^10)`.

For completeness, if s annihilates J_1^10, then ds annihilates J_1^10 exactly when s also annihilates the derivatives of its local sections. Annihilating that generated sheaf is equivalent to annihilating its saturation: a regular pairing vanishing after multiplication by a nonzero local function already vanishes before multiplication. Hence the identity is valid at ramification points as well as generically. Its right side is rank two and degree minus twenty-four, using the same exact-sequence degree calculation as above. The degrees minus fourteen and minus twenty-four cannot agree.

This proves the required nonzero restriction of T0. It is a geometric nonvanishing argument, not a deduction from the existence of a character channel alone.

## 5. The constant normal form and its dual

Because the nonzero restriction spans the one-dimensional Hom space, beta=c eta for a unique scalar c. The shear

`g(v,h)=(v-cT0(h),h)`

is constant, equivariant, invertible, fixes V0, and acts trivially on its constant quotient. Its action kills the graph map in Z direct-sum Hbar O. The preimage of the resulting zero graph is exactly U direct-sum R, since Q*->R is sheaf-surjective with kernel U. This proves an equality of embedded subbundles after the constant gauge, not just an isomorphism of their underlying bundles.

The constancy of g is essential and present: it commutes with the original flat connection. The dual coordinate change therefore separates

`E0=ann_V0*(U)=W O(-9)`

and the quotient block

`Q0=U*=Sym^8 W O(2)`.

The latter has rank nine, unlike the rank-two Z of Section 2. The proof keeps this distinction correctly throughout the reconstruction.

## 6. Exact recovery of the original two pencils

The original Gauss-gate pin supplies the actual Koszul middle-cohomology realization of H and the actual quotient formula y-zx on the affine chart l=u+zv. Homogenizing gives ay-bx in D_lin(1). A Koszul boundary (A_v n,-A_u n) changes that expression by -(aA_u+bA_v)n, so the quotient formula is well-defined with exactly the original A pencil.

From 0->M2 O(-1)->M3 O->D_lin->0, cohomology gives

`H0(Q(-1))=H0(D_lin)=M3`,
`H0(Q(-2))=H0(D_lin(-1))=M2 tensor H1(O(-2))`.

The final one-dimensional factor is fixed by the determinant convention. Since det L is trivial under the invariant symplectic convention, it introduces no nontrivial G-character.

The two local representatives in equation (21) glue correctly. If e_a=(1,b/a) and e_b=(a/b,1) are the tautological O(-1) frames, then e_b=(a/b)e_a. The relation aA_u+bA_v=0 in D_lin gives

`[A_v n]e_a = [-A_u n]e_b`.

Their connecting class is a generator of the H1(O(-2)) factor times n, up to its one common boundary sign. Multiplication by the symplectically associated linear form t_l=beta a-alpha b gives

`[(beta-alpha b/a)A_v n]=[alpha A_u n+beta A_v n]`.

Thus the reconstructed first map is the fixed original A_l under this same identification of M2 and M3, not just a map between representations with the right dimensions.

For the second map, the ay-bx convention identifies H0(Q) with

`(M3 direct-sum M3)/im(A_v,-A_u)`.

The map (B_u,B_v) descends by the original commutativity identity. Its kernel is exactly the actual H, with the actual inclusion into H0(Q), and it is surjective since B_u is surjective. Negativity gives H0(E)=0, and H1(H O)=0. Therefore the cohomology connecting map identifies H1(E) with M4 so that delta is this descended map. The section t_l m is represented by (alpha m,beta m), which gives

`delta(t_l m)=alpha B_u m+beta B_v m=B_l m`.

Both recovered maps use the same middle identification and the same actual parameter l. There is no independent reparametrization of the second pencil and no unresolved relative gauge. The displayed basis formulas verify natural equivariant maps; the invariant determinant convention ensures G-equivariance. A common choice of the opposite boundary sign only changes a constant gauge.

## 7. Direct-sum functoriality, characters, and complement

The reconstruction uses cohomology, multiplication by sections of O(1), and the connecting map of the original exact sequence. These constructions are functorial for a constant direct-sum decomposition. Consequently the constant block projections induce compatible projectors on all three reconstructed spaces. Transporting them through the exact identifications of Section 6 gives G-equivariant idempotents on the original M2, M3, and M4 satisfying both pencil-intertwining identities for every l.

The block character calculation is correct:

`H0(Q0(-2))=Sym^8 W=P+D`,
`H0(Q0(-1))=Sym^8 W tensor W=W'+S+2T`,
`H1(E0)=W tensor Sym^7 W=V+2P+D`.

For the last equality, Sym^7 W=W'+T, so W tensor Sym^7 W=P+(D+P+V). The dimensions are respectively 9, 18, and 16. Subtraction from the actual pinned source characters yields

`A+2V+2P+3D`, `2W'+2S+4T`, and `V+2P+2D`,

of dimensions 32, 36, and 21. These are genuine complementary representations. Because the maps themselves were recovered, the restricted direct summand is the canonical degree-ten two-pencil system associated with the exact inclusion, not merely a triple of character subspaces.

## 8. The added full-orbit corollary

The revised Section 8 specifies the correct classification problem: full constant embeddings with the exact structural inputs and a balanced endpoint, modulo G-equivariant constant isomorphisms covering the identity of X. It is not a claim that either abstract orbit is realized by the fixed HM module. The earlier shear proof uses only these structural inputs, so its normal form applies to this entire abstract class, not solely to an already constructed actual source.

In the normal form, backward transformation is componentwise. The complete degree-ten block has eighth backward transform U_0^10 and ninth backward transform zero. PR789's residual has third backward transform zero. Hence equation (27) is correct, and the constant span of the eighth backward transform intrinsically recovers V0. This argument does not assume that an arbitrary full ambient equivalence preserves a previously chosen block: preservation follows from the intrinsic Gauss construction. It consequently descends to an equivalence of the genuine residuals.

The same reasoning recovers V1 from the constant span of R^{--}=U_0^8, recovers A0 by intersection, and then recovers the endpoint in the actual constant quotient. If d:F_t->F_s carries its endpoint line subbundle to the other one over the identity of X, the induced isomorphism O(-18)->O(-18) is multiplication by a nonzero constant. Dual evaluation therefore has the same image in H0(O(18)). Since the images are H_t and H_s, their P-multiplicity lines agree and t=s. In particular, no change of ambient coefficient basis can silently change the endpoint parameter.

At fixed t the descended equivalence preserves exactly the vertical data and the quotient endpoint of PR789's full stabilizer. Thus no additional full-space equivalence can merge its zero and nonzero residual coupling classes. Conversely, any residual equivalence extends by the identity on the separated V0. PR789 constructs representatives of both residual classes for every balanced t; adjoining the degree-ten block supplies representatives with the stated full structural inputs. This establishes existence and exhaustiveness of the two abstract full orbits.

The proof correctly limits this to a set-theoretic orbit statement. It claims neither a product moduli scheme, a canonical global nonzero coupling representative, nor actual HM realizability. No additional mathematical defect appears in the added bytes.

## 9. Public source pins and byte integrity

The following public repository files were checked at the stated immutable commits. SHA-256 values refer to the complete UTF-8 file contents. These pins document the exact inputs and the distinct earlier abstract witness; the present verdict remains conditional on the upstream actual-source theorems, as the reviewed proof explicitly states.

- [PR744 constant-span intersection](https://github.com/Akilleez-QA/read-em-and-weep/blob/2348d4b6fb2afd67d66b15aad6037ab92c94f076/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-CONSTANT-SPAN-INTERSECTION.md). SHA-256: `f72531663c01cb681e56500f578d595355cab384c9bb96b1ea120012ff4671b7`.
- [PR751 residual osculations](https://github.com/Akilleez-QA/read-em-and-weep/blob/e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-RESIDUAL-OSCULATIONS.md). SHA-256: `e89dd5169fc0c80360884de045e8d067564be582366e7f9608394d738b200e3f`.
- [PR751 full residual span](https://github.com/Akilleez-QA/read-em-and-weep/blob/e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-RESIDUAL-FULL-SPAN.md). SHA-256: `f7621cc508b76f8c12e52a0c5eddf067e18688a174265d930403fc8a69641026`.
- [PR758 exact residual Gauss flag](https://github.com/Akilleez-QA/read-em-and-weep/blob/063216038f3aefd65617651c2426721efafc7f9b/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-EXACT-RESIDUAL-GAUSS-FLAG.md). SHA-256: `65d1e4132f1be1d2b4323b2160d8562c28c5aa3350153b979a8e740ef40a1722`.
- [Original positive double-hyperplane Gauss gate](https://github.com/Akilleez-QA/read-em-and-weep/blob/063216038f3aefd65617651c2426721efafc7f9b/research/hm/order-four-quadratic-load/POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md). SHA-256: `0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2`.
- [Uniform hyperplane cohomology and actual quotient](https://github.com/Akilleez-QA/read-em-and-weep/blob/063216038f3aefd65617651c2426721efafc7f9b/research/hm/order-four-quadratic-load/UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md). SHA-256: `c7de926d4b63deaa6e36d6ce9b220792cb0a5869ecb557398b381c4cc0dcc3d4`.
- [Actual equivariant source characters and presentations](https://github.com/Akilleez-QA/read-em-and-weep/blob/063216038f3aefd65617651c2426721efafc7f9b/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md). SHA-256: `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`.
- [PR788 universal constant-connection feasibility](https://github.com/Akilleez-QA/read-em-and-weep/blob/941b7b3b77dc8ae8a19b1e000dddeb0438d05db7/research/hm/source2-universal-constant-flag/PROOF.md). SHA-256: `81bb2d40705fa1e35f5719ef59323cd60af675ebe74015651dda9590a2488f29`.
- [PR789 residual coupling normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md). SHA-256: `7eb626caae70e62613e8a3e318ac4c6a858502c4fdecfb44a6693e3ed85635c3`.

## 10. Evidential boundary

The proof and this audit concern universal character identities, exact bundle sequences, invariant orbit sizes, Wronskian weights, and constant-connection duality. No selected actual coefficients, endpoint parameter, source point, derivative value, matrix, source-instance rank, scan, model experiment, or large computation was used.

The new theorem strengthens a necessary actual-source normal form. It does not identify the full actual inclusion with PR788's three-block witness, does not split the remaining residual constantly, and does not establish or refute the required summand in the fixed HM tensors. Those limitations are essential and are correctly maintained.
