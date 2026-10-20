# Canonical retained filtration and the discriminant-weighted mixed obstruction

> Historical qualification: the filtration and its first quotient remain valid. Statements below denying an unconditional canonical twenty-dimensional projection apply only to the bare filtered bundle, not its additional cubic algebra structure. The later [canonical cubic splitting](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6277692474) resolves that overbroad conclusion; it supplies no vanishing of the thirty conditions.

## Result and exact boundary

There is a canonical first test of dimension ten inside the thirty retained detector conditions. It is not a chosen ten-coordinate block of a Horrocks splitting. Let Y=P⁴, X=P²×P², m:X→Y be multiplication, B₀=End₀(HM), and G=F₀⁺ be the trace-zero even summand of m_*O_X. Define

    W=H⁰(Y,G(1)),
    L=im(W⊗O_Y(−1) → G),    Q=G/L.

Then W is one-dimensional, L=W⊗O(−1) is a line subbundle, and Q is a line bundle of isomorphism type O(−2). There are canonical exact sequences

    0 → D₁₀ → D₃₀ → D₂₀ → 0,
    0 → T₂₀ → T₃₀ → T₁₀ → 0,                    (A)

where D₁₀=H²(B₀⊗L), D₃₀=H²(B₀⊗G), D₂₀=H²(B₀⊗Q), and each T is its perfect Serre dual. The second sequence is the dual of the first, including its order. The actual canonical corrected obstruction C lies in T₃₀ by the previously established alternating transfer.

The first obstruction is the canonical quotient

    C₁₀ = H²(id⊗restriction-to-L)(C) ∈ T₁₀.       (B)

It vanishes exactly when C annihilates the canonical D₁₀ subspace. Only after this vanishing does C have a unique preimage C₂₀ in T₂₀, and then C=0 iff C₂₀=0. There is no unconditional canonical projection of C onto a twenty-dimensional complement.

A new concrete form of (B) is available. A generator of W corresponds to the symmetric bilinear polarization σ of the discriminant of binary quadratics, a section of O_X(1,1)=m*O_Y(1). It is trace-zero. Therefore

    C₁₀(σ) = Tr_m^ω(σ·C_X) ∈ H²(Y,B₀⊗ω_Y(1)), (C)

where C_X is the actual mixed cocycle/class on X and Tr_m^ω:m_*ω_X→ω_Y is the duality trace. Thus the first ten conditions are precisely the vanishing of this discriminant-weighted duality trace. Equivalently, seek a regular Čech one-cochain p with

    δp = Tr_m^ω(σ·C_X).                          (D)

The right side means the actual source of null-mixed-module-equation formula (6), after normalization and the canonical even/retained projection. No physical coefficients have been evaluated.

None of the inspected geometric, pure Atiyah-square, principal-symbol, alternating, or self-duality identities currently proves (D). Below are precise failure checks, rather than a claimed proof of vanishing. In particular this work does not reduce the number of unknown retained values from thirty to twenty.

## 1. Inspected source and admitted premises

https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6274541018

It establishes pr_const(C)=0 for the specified corrected external-product ambient by exact normalized defect transport and pure-boundary rigidity. It explicitly leaves all thirty retained pairings unknown. The argument here retains its admitted algebraic-sheaf, regularity, transition/connection, and Ext-character premises.

Read the pinned ambient source directly:
https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

Dependencies include null-mixed-duality-reversal, null-canonical-alternating-transfer, pair quotient report, null-mixed-module-equation, null-corrected-pure-lift, semiregularity sector report, and null-alternating-primitive/PROOF.md. The imported twist dimensions are h²(B₀(−1))=10 and h²(B₀(−2))=20. Scalars do not contribute these intermediate cohomology groups. No new HM cohomology calculation is claimed.

## 2. Canonical evaluation line, independent of a splitting

The established isomorphism type is G≅O(−1)⊕O(−2). Therefore G(1)≅O⊕O(−1), so dim W=1. Under any such isomorphism the evaluation W⊗O(−1)→G is the inclusion of the first summand: H⁰(O(−1))=0, and the nonzero constant section of O has no zeros. Hence this intrinsically defined map has constant rank one, its image is a line subbundle, and its quotient Q is locally free. The conclusion does not depend on choosing the auxiliary isomorphism used to check it.

More intrinsically Q=det(G)⊗L*, with its actual constant-line factors retained. Its isomorphism type is O(−2). L is the maximal-slope piece of the slope filtration. Thus

    0 → L → G → Q → 0                             (1)

is canonical. It splits abstractly because Ext¹(Q,L)=H¹(L⊗Q*)=0; the latter is H¹(O(1)) times a constant line. But its splittings form a torsor under Hom(Q,L), of dimension five. No preferred sheaf splitting is furnished by the isomorphism type. This statement does not assume that every change of sheaf splitting acts nontrivially on the particular H² groups; that extra claim is unnecessary here.

Tensoring (1) with B₀ and taking cohomology gives the first sequence (A). Exactness with zero connecting homomorphisms follows from the existence of an abstract sheaf splitting, not from an unproved H¹ or H³ vanishing for a twisted HM endomorphism bundle. In particular H²(B₀⊗L) injects and H²(B₀⊗G) surjects onto H²(B₀⊗Q).

Dualizing (1) and tensoring with ω_Y gives

    0 → Q*⊗ω_Y → G*⊗ω_Y → L*⊗ω_Y → 0.           (2)

Again its cohomology sequence is short exact. The trace pairing B₀⊗B₀→O and Serre duality identify it with the vector-space dual of the first sequence (A). Its first term has dimension twenty and its quotient dimension ten. In twist notation they have isomorphism types H²(B₀(−3)) and H²(B₀(−4)), respectively, with the W/determinant lines retained. This is why calling a canonical ten-dimensional obstruction subspace the first test would reverse the correct construction.

## 3. Staged detector criterion, without choosing complements

Write r:T₃₀→T₁₀ and i:T₂₀→T₃₀ for (A). Naturality of Serre duality gives

    <r(C),d> = <C,d>  for d∈D₁₀.                 (3)

Consequently r(C)=0 iff all ten first-subspace pairings vanish. Exactness then supplies a unique C₂₀ with i(C₂₀)=C. For e∈D₂₀ choose any lift ẽ∈D₃₀. Define

    <C₂₀,e> = <C,ẽ>.                             (4)

The value is independent of the lift exactly because C annihilates D₁₀. These twenty second-stage pairings are therefore canonical after, and only after, stage one passes. Equations (3)–(4) give a complete necessary and sufficient criterion for C=0.

For cochain use, (2) also provides an explicit staged lift of a primitive. If r(c)=δp for a cocycle c representing C, locally lift p to a one-cochain p̃ with values in B₀⊗G*⊗ω. Then c−δp̃ is valued in B₀⊗Q*⊗ω and represents C₂₀. Its class is independent of all choices: all cohomological connecting maps of (2) vanish. Its vanishing gives a primitive of c and hence the mixed module correction, with the sign chosen according to δx=−C. This is an exact staged construction, not a proof that the required p exists.

## 4. A universal explicit generator and weighted-trace target

Let V be the two-dimensional binary-form vector space, so P²=P(Sym² V) and P⁴=P(Sym⁴ V), with dual conventions adjusted consistently. The symmetric sections of O_X(1,1) are Sym²(Sym² V*). Multiplication pulls back the five-dimensional space of quartic linear coordinates. The elementary binary-quadratic decomposition is

    Sym²(Sym² V*) ≅ Sym⁴ V* ⊕ (det V*)².         (5)

The second summand is the polarization of the discriminant. It is symmetric in the two quadratics and nonzero. Concretely, fix Δ(ax²+bxy+cy²)=b²−4ac and set σ(q,r)=[Δ(q+r)−Δ(q)−Δ(r)]/2=bb′−2(ac′+a′c). Rescaling this convention rescales C₁₀(σ), but does not change its vanishing. Its determinant-line qualification matters if no volume form on V is fixed; choosing one merely chooses a nonzero generator σ of a one-dimensional space.

Algebra trace is equivariant for changes of binary coordinates. After restricting to SL(V), the discriminant line is trivial whereas Sym⁴ V* has no invariant vector. Thus trace sends σ to zero in H⁰(Y,O(1)). Alternatively trace/6 composed with pullback is identity on quartic linear coordinates, and the equivariant decomposition (5) identifies its kernel as exactly the discriminant line. It follows that W is precisely this line inside H⁰(X,O(1,1)). This argument is universal binary-form algebra, not a value at a factorization or a physical-model computation.

Finite duality identifies m_*ω_X with Hom(m_*O_X,ω_Y), and its trace is evaluation at the unit. For λ in this Hom sheaf and a local section s of m_*O_X, module multiplication satisfies

    Tr_m^ω(sλ) = (sλ)(1) = λ(s).                 (6)

Twisting (6) by O(1), restricting λ to G, and taking s=σ proves (C). No étale restriction, inverse Jacobian, or division by a branch equation is involved. The same formula works on an affine cover of Y, whose inverse image under finite m is affine, and hence gives the regular cochain equation (D). If representatives first live on an E-trivializing refinement, pass through the ordinary common-refinement comparison; finite pushforward and the coefficient maps themselves remain canonical.

For the actual source, let c be the normalized tracefree mixed defect tf(g_ik⁻¹R_ijk), with R precisely formula (6) of null-mixed-module-equation. The unprojected normalized defect has exact trace by mixed-module §7; subtracting half that scalar coboundary times the identity therefore preserves its cohomology class. One may canonically project c to its block-even retained coefficient summand after pushforward; the preceding transfer says this projection represents the entire class. The map (6) annihilates the constant-dual summand because Tr(σ)=0 and ignores the block-odd summand. Thus (C) is independent of these representative adjustments as well as of pure-gauge choices. A pure-gauge change c→c+δq changes its weighted trace by δTr_m^ω(σq).

## 5. Three specific failed vanishing arguments

### A. Multiplying the known alternating primitive

The known theorem is e_sign(R_raw)=δP, equivalently the unweighted duality trace of C is zero in cohomology. To get (D), one needs the weighted average, not σ times the unweighted average. The section σ depends on the chosen quadratic partition: it is invariant under its inner swaps and block exchange, but is not pulled back from a section of O_Y(1). Indeed, if σ=m*a, then trace-zero would give 6a=0, contradicting σ≠0.

Therefore the necessary commutation with full permutation averaging fails. One cannot replace the weighted average of transported σ·R by σ times e_sign(R). Multiplying the displayed primitive only proves exactness of σ·e_sign(R), in the relevant pulled-back coefficient line; it says nothing by itself about the different weighted expression e_sign(σ·R). This is a concrete failure of the proposed proof step. It does not disprove (D).

### B. Pure Atiyah-square scalarity or principal-symbol order

The corrected pure argument proves the cohomological identities for the normalized relative Atiyah class and supplies solutions u,v of the two pure module equations. The actual mixed source still contains the cross products U_jk v_ij+V_jk u_ij, the four mixed bidifferential interactions, the overlap-composition term w(g_jk), the external-product M term, and the triple-unit interactions −bv−cu−bcg. Its scalarity is not an instance of the pure rank-two square identity.

The map in (C) is a finite coefficient evaluation on this entire closed source. It is not a principal-symbol projection on a differential operator. Knowing M's highest symbol, or knowing the pure characteristic classes vanish, does not identify Tr_m^ω(σc) with a scalar Atiyah expression or provide its primitive. In particular, discarding the terms involving chosen pure primitives would change the secondary obstruction being tested. The mixed-module gauge identity proves independence of those choices in cohomology; it does not allow setting them to zero when their pure equations have nonzero right sides.

Thus a new chain-level weighted transgression identity, or a genuine comparison identifying (C) with an already vanishing characteristic class, is needed. No such identity was found in the inspected sources. This is a source-specific gap, not a theorem that all possible Atiyah-based approaches must fail.

### C. Existing symmetry and ordinary semiregularity

Block-evenness, zero constant projection, and the rank-two inverse-adjoint identity allow every vector of T₃₀. The quotient r:T₃₀→T₁₀ is surjective, so these established linear constraints cannot force r(C)=0. This is a structural insufficiency argument, not a construction of a nonzero actual mixed obstruction or a modification of its fixed ambient.

The existing semiregularity report proves that its ordinary linear target has no retained U22 isotype, so that map annihilates the whole retained space. A map already zero on T₃₀ cannot distinguish its first-stage quotient. There is no additional automatic ten-dimensional vanishing supplied by that report.

## 6. Remaining mathematical target

The next well-posed universal target is (D): derive a regular primitive for the discriminant-weighted finite trace of the complete specified mixed source. It is a canonical ten-dimensional obstruction test, with an explicit geometric coefficient σ and an exact coefficient-sheaf destination. If established, it would canonically leave only T₂₀; until then all thirty conditions remain open.

Only static source/file reading and universal sheaf, representation, cohomology, and duality algebra were used. 
