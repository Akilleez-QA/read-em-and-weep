# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent formal audit

## Verdict

The proof in `PROOF.md` passes the formal audit, conditional on the geometric and representation-theoretic inputs explicitly inherited there. The construction gives a canonical invariant trilinear operation, the rank-two argument gives outer reversal, and the actual deformation family gives the polarized cubic relation. These two relations permit the stated abstract representation channel. The proof correctly stops short of claiming a nonzero geometric value or completeness of the listed identities.

This audit is a symbolic check of the draft. It does not independently verify the earlier geometric input files, construct or evaluate a geometric instance, or establish that a nonzero abstract tensor is realized by a rank-two bundle.

## 1. Defining systems and representative changes

The sign convention is consistent: for degree-one representatives and primitives,

    d(α hβγ+hαβ γ)=−αβγ+αβγ=0.

A primitive change adds the cohomology class a[v]+[u]c. Both closed correction classes belong to K because all defining cochains are invariant; K·K=0 therefore kills the indeterminacy. The warning against unrestricted primitives is necessary and correct.

The three representative-change formulas are correct, including their signs:

- α→α+dx, hαβ→hαβ+xβ gives d(x hβγ).
- β→β+dy, hαβ→hαβ−αy, hβγ→hβγ+yγ gives zero change.
- γ→γ+dz, hβγ→hβγ−βz gives −d(hαβ z).

These moves can be applied successively, so they prove independence under simultaneous representative changes as well. Linear choices of representatives and of a section of the differential on boundaries prove trilinearity; their subsequent removal by independence is valid. Naturality under DGA morphisms and quasi-isomorphisms follows from transporting defining systems.

Minor wording improvement: Section 2 should say “choose a linear right inverse of d:A¹→B²(A)” rather than “choose a linear right inverse d:A¹→B²(A).” The section itself has direction B²(A)→A¹.

## 2. Rank-two identity

Adjugation is linear only in rank two, and its graded anti-multiplicativity has exactly the sign displayed. It commutes with the Dolbeault differential and the finite-group action. H¹ of the invariant scalar complex vanishes, so subtracting one half of an exact scalar trace produces trace-free closed representatives.

For such representatives, τ(βα)=−αβ. Consequently the symmetrized bilinear primitive in Section 4 has the required differential and satisfies τh(a,b)=−h(b,a). Applying τ to the defining cocycle yields minus the reversed cocycle. Since the trace contribution vanishes on H², τ acts there as −id. Thus M(a,b,c)=M(c,b,a).

The distinction between trace-free representatives and possibly non-trace-free primitives is essential and is respected. The equivalent assertion about symmetric trace-free and antisymmetric scalar parts of h is also correct.

## 3. Smooth-family implication

The argument requires a family of integrable holomorphic structures on the fixed space, with tangent a, not merely a family of underlying smooth bundles. This is the inherited meaning of the family in the draft. Three formal orders suffice.

The first derivative of a deformation is a closed representative of a. A first-order change of smooth trivialization, equivalently a gauge change with a prescribed degree-zero first-order term, can replace it by the desired invariant representative. This gauge change preserves the full Maurer–Cartan equation. Once α is invariant, averaging b and c separately preserves db=−α² and dc=−(αb+bα), because the latter expression is linear in b. There is no need to assert that averaging the entire nonlinear family produces another integrable family.

Taking h(a,a)=−b gives M(a,a,a)=[dc]=0. Polarization over C gives the six-term sum, and reversal identifies its terms in three pairs. The resulting cyclic sum vanishes. This does not imply pointwise vanishing of every ordered value.

## 4. Source quotient

The one-copy Schur-functor statement is correct in characteristic zero. In the Schur–Weyl decomposition of K^⊗3, imposing reversal retains the symmetric multiplicity space, kills the alternating one, and retains one dimension of each two-dimensional standard multiplicity space. The cyclic-sum relation kills the symmetric piece and is already zero on a standard multiplicity space. The remaining polynomial functor is one copy of S_(2,1)K.

The quotient need not carry the original full argument-permutation S3 action: the reversal relations are not a submodule for every argument permutation. The draft explicitly makes this qualification and correctly distinguishes argument S3 from geometric S4.

## 5. Eligible geometric representation channel

Under the stated action, the [22] summand of (C²)^⊗4 has multiplicity space det². J therefore acts there by +1, and the coordinate reversal R supplies three positive copies. Removing a trivial positive line does not change [22]. The stated twelve remaining positive trivial copies also follow from the displayed eigenspace dimensions.

Assuming the inherited target contains the stated positive [22] copies, semisimplicity supplies ℓ, P, and φ. Since the trivial and [22] representations are inequivalent, P(t)=0 and ℓ(u)=0 for u in U. The displayed F consequently has F(t,t,u)=φ(u), is nonzero, and satisfies both reversal and cyclic-zero by direct symbolic cancellation. It establishes nonzero equivariant Hom from the source quotient to that target sector.

This is an abstract compatibility witness only. It proves that the two established argument identities do not themselves eliminate this channel; it neither realizes F as a geometric Massey operation nor rules out additional geometric identities. The draft's limits are appropriately explicit.

## 6. Assumptions retained

The reasoning uses characteristic zero, finite-group averaging, vanishing H¹ and H² of the invariant scalar complex, invariant ordered cup-product vanishing, the actual integrable family, and the stipulated geometric actions and target decomposition. In particular, for a general non-linearly-reductive group, vanishing of invariant scalar cohomology alone would not justify invariant primitives. No such generality is claimed here.

The rational descent paragraph is formally sound provided its stipulated algebraic DGA and multiplicative comparison exist as stated. The audit does not independently construct those models or verify the preceding geometric inputs.

## 7. Sign-valued Serre pairing and retained-sector projection

The corrected final paragraph of Section 6 is consistent with the stipulated sign-valued pairing. If B has value character ε on D8, a physical vector of character ε can pair nontrivially with a detector vector of character χ only when εχ=ε, hence χ=1. Equivalently, the pairing-dual character is ε⊗ε^∨=1. Projecting the detector to the ε character instead would give the wrong pairing sector.

With the stated restriction [22]|D8=1⊕ε and positive multiplicity twelve, the full [22]-positive isotypic target has dimension twenty-four, while its D8-trivial projection has dimension twelve. The average e_D8,triv=(1/8)∑g is the correct canonical projector. Nondegeneracy of the inherited pairing identifies this projected sector with the pairing dual of the retained physical ε sector, but gives no nonvanishing or spanning assertion about the image of the Massey map. The updated paragraph preserves this distinction.
