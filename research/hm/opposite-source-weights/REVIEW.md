# Independent review: signed torsion weights and vertex absorption

Verdict: PASS, conditional on the explicitly retained actual-geometric inputs. No substantive mathematical correction is required. This is an independent mathematical and bounded-arithmetic review, not formal proof-assistant certification.

Final reviewed PROOF.md SHA256:

    f4a0156e9445b51e42d8ea281b3309763e81b84ad9b0188b48f025885f441af9

The initial mathematical review covered SHA256 dcf3093833e1001b6b4dea53d3d8f71c66cbfc4668bca185ca098d83c0b00b50. The final bytes differ only in the status sentence recording that review; this exact one-line change was independently verified. The final proof is therefore fully covered by the verdict.

## Input and scope checks

The reviewed copies of the following three inputs agree with INPUTS.json in byte count, SHA256 and Git blob SHA1:

- [PR934, reduced opposite pencil](https://github.com/Akilleez-QA/read-em-and-weep/blob/8c9847612b5f575b987cec9c62b72b099d745e44/research/hm/reduced-opposite-pencil/PROOF.md).
- [PR936, opposite torsion trichotomy](https://github.com/Akilleez-QA/read-em-and-weep/blob/60fd2b9951dd151dfbdff5b09316d05495cca53d/research/hm/opposite-torsion-trichotomy/PROOF.md).
- [PR928, positive factorization, Section 3](https://github.com/Akilleez-QA/read-em-and-weep/blob/1a8fb75aa886f9bb6c07e357759d37630cdd127d/research/hm/profile11-source127-cdf-positive-factorization/PROOF.md).

The primary section-resolution and cohomology assertions used for the new twist were also checked against PR928's exact imported [regularity source](https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md). This review does not independently reprove the imported HM geometry or inspect an actual monad differential.

## 1. Actual source character and all required vanishings

The identity B(2)=Sym2(F_HM)(3) uses det(F_HM)=O(-1), with no extra character because G is perfect. The same equivariant monad class as PR928 therefore gives precisely the displayed twist-three lambda-ring Euler formula. Its smallest and largest line twists are one and seven, so replacing the line Euler characters by ordinary symmetric powers is valid.

For End(F_HM)(2), the resolution has E0=15F_HM(-1)+4F_HM and E1=35F_HM(-2). Its H3 diagonal is controlled by H3(E0) and H4(E1). Serre duality gives H1F_HM(-3), H1F_HM(-4), and H0F_HM(-2); all vanish by the stated primary input. The H4 diagonal reduces to H0F_HM(-3) and H0F_HM(-4). No higher diagonal term is omitted: its cohomological index would exceed four. Together with the imported H0 and H2 vanishings and trace splitting, this justifies H1(B(2))=-chi_G(B(2)).

The arithmetic was independently recomputed using integer cyclotomic group-ring characters, rather than the verifier's symmetric-power plethysm formula. For each of the nine abstract conjugacy classes, the five eigenweights of Hcoord=V+W were used to extract complete symmetric functions through degree seven from the product of five geometric series. Monad coefficient characters and their second Adams operations then reproduced the complete claimed H1 character on all nine classes. Its positive and negative dimensions are 41 and 44. Subtracting the exact source quotient S and H14=W'+2T6 gives E=2W+W'+2S+2T6, of dimension 26.

## 2. The stabilizer orientation is fixed correctly

The character lambda is defined by the actual linearized O(1) fiber, not by an arbitrary choice of generator of the C5 character group. For the quotient W to that fiber, the kernel has character lambda^-1. Consequently the projective tangent is Hom(kernel,quotient)=lambda^2 and the cotangent is lambda^-2. Thus zeta=lambda^2 and tau=zeta^-1 are consistent, and O(10) has trivial K-fiber character.

The signed conclusions would depend on this orientation; the proof does not silently identify zeta with the cotangent character.

## 3. Evaluation-source induction and exhaustive pairings

The complete-evaluation kernel of a globally generated torsion sheaf has only O(-1) summands, so its twist-one H1 vanishes. Taking sections of its twisted evaluation sequence therefore gives the asserted character difference without a correction term. A nonreduced torsion module has a finite equivariant composition series, and twisting multiplies each fiber factor by lambda. Additivity and the tensor-induction identity then give Ind(lambda^(2r-1)) for each factor zeta^r.

The three odd inductions follow from Frobenius reciprocity, including multiplicity two for weight five in T6. The source of the O(2) evaluation kernel is W, while the source of an L O(1) kernel is L. These conventions agree with E=E_Z+E_F.

As an independent exhaustive check, all fifteen unordered pairs from the five C5 weights were tested against both coefficient characters for each of the six quotient bundles. Exactly six matches remain: Type I has {0,4}; Type II has {0,1}; both Type III bundles have {1,4}; both Type IV bundles have {1,2}, with exponents modulo five. This agrees with every signed pairing in (6), without relying only on the prior three absolute-weight patterns.

The reduced-orbit induced sheaves in Section 4 are genuine abstract G-equivariant models. They are globally generated, their evaluation kernels have the required source character, and their section spaces have the required target character. This proves the claimed limitation of the two-character test. It does not prove actual HM occurrence, extend the marked multiplication system, or realize an actual extension scalar. The proof states those boundaries correctly.

## 4. Full equivariant local Ext and absorption check

The completed stabilizer action can be linearized on a uniformizer: averaging an arbitrary lift of the cotangent eigenvector into its tau-eigenspace preserves its nonzero first-order term. The same averaging argument applied to a target-line fiber generator gives an invariant local frame, because its fiber character is trivial. For a cyclic source, averaging a lift of its top eigenvector gives an eigen-generator by Nakayama's lemma. Thus the displayed equivariant free resolutions apply to the full completed modules, not merely to their associated graded representations.

Applying Hom_R(-,R) gives Ext1(k_r,R) of weight 1-r. For a cyclic length-two source with top r, Ext1 is (R/(x^2)) with constant weight 2-r and x-weight 1-r. As an independent character check, local duality gives the same two weights from the vector-space dual of the source, twisted by tau^-1.

It follows that:

- Type I has no invariant extension, whether semisimple or cyclic.
- Every other semisimple case has one invariant extension direction, carried by its unique r=1 factor.
- Cyclic Type II has only the x-direction invariant.
- Cyclic Type IV has only the constant direction invariant.

This also checks that no second invariant direction has been discarded.

For a cyclic module, the relation x^2 y=a e has residual torsion length min(2,ord_x(a)), interpreting a=0 as length two. Changing a by a multiple of x^2 changes the lift, not the extension or this length. Hence the Smith-normal-form argument is valid to all orders, not only after truncating an actual map. A nonzero x-class leaves length one; a unit class leaves zero. For k+k, a nonzero extension functional has one-dimensional kernel and leaves exactly one simple torsion factor. These give every row of (7), including the exclusion of length twelve in cyclic Type IV.

## 5. Global Ext, Type I splitting, and Section 6

The equivariant splitting C=Z+F is supplied by PR936. Each summand of F has degree at most two, so Ext1(F,O(10)) vanishes. Since Hom(Z,O(10)) is zero, the local-to-global sequence identifies Ext1(Z,O(10)) with the direct sum of its local Ext spaces, with no hidden H1 contribution.

Characteristic zero and finiteness of G make invariants exact, so equivariant Ext1 is the invariant part of ordinary Ext1. Transitivity identifies that invariant space with the K-invariants in one arbitrary abstract stalk. A nonzero invariant global class is nonzero at every orbit point. Therefore the global dimensions are exactly zero for Type I and one otherwise, and Type I really splits G-equivariantly, not merely as an ordinary sheaf. The local lengths multiply by twelve exactly as asserted.

For Section 6, splitting the extension over F leaves 0 to O(10) to M to Z to 0. The torsion-free quotient L of M has rank one. The injection O(10) to L has quotient of uniform local length a at the orbit, hence divisor a·Omega and L=O(10+12a). Its equivariant linearization is unique up to a character of G, which is trivial. The extension of L by tors(M) splits because Ext1(L,tors(M))=0, and averaging makes that splitting equivariant. Thus (10) is valid as an existence assertion about summands, not a canonical decomposition.

Consequently, within the explicitly assumed maximal-torsion case, D_vert is locally free exactly for cyclic Type IV with nonzero invariant extension class; then D_vert=F+O(34). No inference is made about the actual class being nonzero.

## Verification and remaining boundary

Both python verify.py and python -O verify.py pass. The independent nine-class cyclotomic calculation and fifteen-pair enumeration also pass. The supplied finite verifier checks character identities and invariant weights, not the geometric vanishings, sheaf exactness, or global splitting; those were reviewed separately above.

No actual HM/source coefficient, selected point, parameter, matrix, derivative, rank or extension scalar was evaluated. No selected source exclusion, frontier change, full-window realization, algebraicity claim, publication or upstream action is part of this review.
