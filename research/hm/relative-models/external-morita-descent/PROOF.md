> Publication scope: Exact external coefficient square and optional ordinary-sheaf transition obstruction; nontrivial algebroid defects require their supplied complex. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# External products of invariant Morita descent and the mixed coefficient square

## Result, provenance, and the exact advance

For two **supplied independent** finite-group Morita atlases over a common characteristic-zero field, their genuine algebraic external product descends to the external product of their invariant atlases. This statement includes rings, overlap bimodules, the specified balanced compositions, modules with supplied invariant finite-free frames, compatible pure coefficient ideals, and their mixed product. Factorized changes of strictification have the exact finite-average comparison

\[
B_{z,h}=B_z\otimes B_h.
\]

For a mixed lifting problem, the coefficient square, including its mixed kernel, is preserved. The coefficient-module assertions also hold for modules that need **not** themselves be external products, provided they have supplied invariant finite-free frames. An optional explicit square-zero transition-obstruction extension is recorded separately in MIXED_OBSTRUCTION.md and is not needed for the theorem here.

The original sources are [PR 1 comment 6261960300](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6261960300), which already states factorization of root/Morita transport for a genuine external ambient, and [comment 6263380151](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6263380151), which proves the supplied invariant Morita-atlas criterion. The latter source was created and last updated 2026-10-19 at 08:50:01 UTC. The local proofs used here are the separately audited strictification and coherent-choice-comparison results.

**Novelty boundary.** The bare ring factorization and factorized gauge calculation are elementary consequences of the supplied product hypothesis, not a discovery that the physical ambient factors. The additional bounded conclusion is a reduction-compatible external descent theorem preserving the entire coefficient square and the actual mixed coefficient submodule. This discharges an abstract compatibility obligation **conditional on actual external-product data and module frames**. It does not discharge the remaining obligation to construct or identify such data for the physical mixed ambient. None of its actual operations, modules, matrices, obstruction classes, or retained values is evaluated.

## 1. Algebraic hypotheses and the Reynolds identity

Let \(k\) be a characteristic-zero field. In fact, all finite-group assertions require only that the relevant orders be invertible in \(k\). Let \(G_z,G_h\) be finite groups, and let \(D_z,D_h\) be associative unital \(k\)-algebras with strict actions \(\psi_z,\psi_h\) by \(k\)-algebra automorphisms. The two actions are independent: \((g,h)\) acts on

\[
D=D_z\otimes_kD_h
\]

as \(\psi_z(g)\otimes\psi_h(h)\). Put \(A_z=D_z^{G_z}\), \(A_h=D_h^{G_h}\), and \(A=D^{G_z\times G_h}\). All tensor products in Sections 1–6 are algebraic over \(k\) unless a balancing algebra is written.

For any \(k\)-representations \(V,W\) of the respective groups, let

\[
p_z=|G_z|^{-1}\sum_g g,
\qquad p_h=|G_h|^{-1}\sum_h h.
\]

These are linear idempotents with images \(V^{G_z},W^{G_h}\). The Reynolds idempotent for the independent product action is exactly \(p_z\otimes p_h\). Since a vector space splits into the image and kernel of an idempotent, tensoring those direct-sum splittings shows

\[
(V\otimes_kW)^{G_z\times G_h}
 =V^{G_z}\otimes_kW^{G_h}
\tag{1}
\]

as canonically included subspaces. This works for infinite-dimensional vector spaces. Applying it to the underlying vector spaces of the algebras proves the natural algebra isomorphism

\[
\boxed{A_z\otimes_kA_h\ \xrightarrow{\ \sim\ }\ (D_z\otimes_kD_h)^{G_z\times G_h}.}
\tag{2}
\]

The equality is between the images of the canonical injections; it does not depend on choosing vector-space complements. Formula (1) also applies to modules or bimodules regarded as representations and to every invariant subspace in the calculations below.

This is an **external independent-group** statement. It makes no assertion that \(M^G\otimes_{D^G}N^G\to(M\otimes_DN)^G\) is an isomorphism for arbitrary internal tensors. Nor may one replace the product action by a diagonal action: two nontrivial inverse characters can give a nonzero diagonal-invariant tensor while both separate invariant spaces vanish.

## 2. Actual external Morita atlases and module frames

For each factor, supply the data required by the invariant Morita-atlas criterion: actual restriction-compatible algebra sheaves \(D^z_i,D^h_a\), actual equivariant Morita-invertible overlaps \(P^z_{ij},P^h_{ab}\), actual associative compositions, and locally available invariant left generators of the overlaps. Supply the quotient atlases, any restriction/change-of-group data, and effective algebroid descent. One may instead read this section as a purely algebraic assertion on a fixed diagram of rings and bimodules.

On a specified product chart define

\[
D_{ia}=D^z_i\otimes D^h_a,
\qquad P_{ia,jb}=P^z_{ij}\otimes P^h_{ab}.
\tag{3}
\]

These identities must be actual section-level presentations on a product basis, with their restriction compatibilities, or explicitly supplied sheaf external products whose local presentations have these identities. They are not conclusions about sections of arbitrary sheaves on arbitrary product opens.

By (1),

\[
A_{ia}=A^z_i\otimes A^h_a,
\qquad \overline P_{ia,jb}
 =\overline P^z_{ij}\otimes\overline P^h_{ab}.
\tag{4}
\]

External tensor products of invertible bimodules are invertible: tensor their specified inverses and use the canonical interchange isomorphism

\[
(P_z\otimes P_h)\otimes_{D'_z\otimes D'_h}(Q_z\otimes Q_h)
\cong
(P_z\otimes_{D'_z}Q_z)\otimes(P_h\otimes_{D'_h}Q_h).
\tag{5}
\]

On elementary tensors this sends \((p_z\otimes p_h)\otimes(q_z\otimes q_h)\) to \((p_z\otimes q_z)\otimes(p_h\otimes q_h)\). Its inverse is the reverse shuffle; balanced relations verify both maps. There is no permutation sign for these ordinary ungraded modules. For graded variants the usual Koszul sign must be included.

The tensor of invariant left generators is an invariant left generator. Consequently the source's **specific** invariant balanced-composition comparison is available for the product overlaps. Under (4)–(5), the descended composition is the external tensor of the two factor compositions. The associativity and unit diagrams commute because the corresponding diagrams in each factor commute. Thus the product invariant atlas is the external product of the two invariant atlas presentations; the assertion then passes to the stipulated effective descended algebroids.

For supplied factor modules \(M_z,M_h\), equation (1) gives

\[
(M_z\otimes M_h)^{G_z\times G_h}
 =M_z^{G_z}\otimes M_h^{G_h}.
\tag{6}
\]

If the factors have invariant free bases of ranks \(r_z,r_h\), the product basis is invariant and has rank \(r_zr_h\), and the usual extension-of-scalars descent map is an isomorphism in this basis. The product algebra need not be local: no product-locality claim is needed because the frames have already been supplied.

There is also a useful nonfactorized version. For **any** finite-free \(D\)-module \(M\) with a supplied invariant basis \(e_1,\ldots,e_r\),

\[
M=\bigoplus_{\nu=1}^rD e_\nu,
\qquad M^G=\bigoplus_{\nu=1}^rA e_\nu.
\tag{7}
\]

Its chart maps and any supplied equivariant gluing maps descend entry by entry in these frames. This is the version needed for a mixed module problem, and used in the separate optional obstruction addendum. It does not assert that arbitrary equivariant modules possess these frames.

## 3. Weak actions, root transport, and factorized strictification comparisons

Suppose the supplied factor atlases initially have normalized coherent weak actions \((\phi_z,a_z)\) and \((\phi_h,a_h)\). The external weak action has

\[
\phi_{(g,h)}=\phi_z(g)\otimes\phi_h(h),
\quad
 a_{(g,h),(g',h')}=a_z(g,g')\otimes a_h(h,h').
\tag{8}
\]

Its overlap actions and composition are the corresponding external ones. For the comparison assertion, assume each factor has a preserved two-sided ideal \(F^1D_i\), every element of \(1+F^1D_i\) is locally a unit, and the actual strictification systems \(Q_i,R_i\) take values there. The previous strictification theorem supplies such systems under its stated complete or nilpotent hypotheses, but their existence here is supplied. If \(Q_z,Q_h\) are these actual strictification sections in the inverse-gauge convention, then

\[
Q_{(g,h)}=Q_z(g)\otimes Q_h(h)
\tag{9}
\]

strictifies (8), because the transformed coherence equation is exactly the tensor of the two factor equations. The resulting strict action is the independent product of the strictified factor actions. No new inverse-limit construction is needed to prove this assertion once the factor strictifications are supplied.

For a second factorized system \(R=R_z\otimes R_h\), put

\[
u_z(g)=R_z(g)^{-1}Q_z(g),\qquad
u_h(h)=R_h(h)^{-1}Q_h(h).
\]

Then \(u_{(g,h)}=u_z(g)\otimes u_h(h)\). The finite-average comparison is therefore

\[
\begin{aligned}
B&=\frac1{|G_z||G_h|}\sum_{g,h}u_z(g)\otimes u_h(h)\\
 &=\left(\frac1{|G_z|}\sum_g u_z(g)\right)
 \otimes\left(\frac1{|G_h|}\sum_hu_h(h)\right)
 =B_z\otimes B_h.
\end{aligned}
\tag{10}
\]

Each \(u_i(g)\) and its average \(B_i\) lie in \(1+F^1D_i\). The factor unit hypotheses therefore imply that \(B\) is a unit with inverse \(B_z^{-1}\otimes B_h^{-1}\). Hence the comparison of invariant rings and overlaps is literally the external comparison:

\[
\operatorname{Ad}(B)=\operatorname{Ad}(B_z)\otimes\operatorname{Ad}(B_h),
\qquad
p_z\otimes p_h\longmapsto
(B^z_i p_z(B^z_j)^{-1})\otimes
(B^h_a p_h(B^h_b)^{-1}).
\tag{11}
\]

The corresponding concrete left-module invariant comparison is multiplication by \(B\). The coherent witness-change and triple-comparison identities follow factorwise from the earlier coherent-choice theorem.

Root/Morita transport also commutes with the supplied external product. In the source's notation, if the actual ambient overlap maps, coherence units and root lifts satisfy

\[
F=F_z\otimes F_h,\quad C=C_z\otimes C_h,
\quad q=q_z\otimes q_h,
\]

then the formulas

\[
F^L_{ij}=\operatorname{Ad}(q_{ij}^{-1})F_{ij},
\qquad
C^L_{ijk}=q_{ij}^{-1}F_{ij}(q_{jk})^{-1}C_{ijk}q_{ik}
\tag{12}
\]

are exactly the tensor products of the factor formulas, in the same noncommutative order. The Morita bimodules and their inverses factor by (5). Applying strictification and then invariant descent consequently gives the same external descended presentation under the stated hypotheses. This incorporates the source's factorized-ambient observation; it does not prove its premise.

For perspective, if two factor expressions are \(1+sU\) and \(1+tV\), their external product contains \(st(U\otimes V)\). None of (8)–(12) passes to the fiber product that would kill this term.

**Nonfactorized choices.** If another actual strictification \(R\) of the same product weak atlas is not factorized, the general finite-average comparison still identifies its invariant atlas with the factorized one, provided that its comparison average is a unit. A sufficient additional hypothesis is that the common filtration-trivial ideal lies locally in the Jacobson radical, or that the ambient itself is separated complete for the specified multiplicative filtration. It preserves both pure coefficient ideals and their mixed ideal by inner conjugation. Thus arbitrary admissible choice of strictification does not change the coefficient-square theorem up to the earlier coherent equivalences.

One must not obtain this sufficient unit hypothesis merely by tensoring two complete rings algebraically. For example,

\[
1-s\otimes t\quad\text{is not a unit in }k[[s]]\otimes_k k[[t]].
\tag{13}
\]

The natural map to \(k[[s,t]]\) is injective, and an inverse there must be \(\sum_{n\ge0}s^nt^n\). Each algebraic tensor has a coefficient matrix of finite rank, whereas this series has an infinite identity submatrix. Thus the inverse is not an algebraic tensor. Completion and factorwise completeness must be distinguished. The factorized comparison (10) remains invertible without any such inference, since its inverse is already displayed.

## 4. Exact coefficient ideals: sum, intersection, product, and reductions

Let \(I_z\subset D_z\), \(I_h\subset D_h\) be stable two-sided ideals. Set

\[
J_z=I_z\cap A_z,\qquad J_h=I_h\cap A_h,
\]

and define the pure ideals in the full product ambient by

\[
\mathfrak I=I_z\otimes D_h,\qquad
\mathfrak J=D_z\otimes I_h.
\tag{14}
\]

All inclusions in (14) are actual injections because the tensor base is a field. Directly from multiplication and unitality,

\[
\mathfrak I\mathfrak J=\mathfrak J\mathfrak I
 =I_z\otimes I_h.
\tag{15}
\]

Choosing vector-space complements only for the proof gives

\[
\mathfrak I\cap\mathfrak J=I_z\otimes I_h,
\qquad
D/(\mathfrak I+\mathfrak J)
 \cong(D_z/I_z)\otimes(D_h/I_h).
\tag{16}
\]

The subspaces and quotient maps in (15)–(16) are canonical, independent of those complements. Put \(K=I_z\otimes I_h\).

Their actual invariant intersections are

\[
\begin{aligned}
\mathfrak i:=A\cap\mathfrak I&=J_z\otimes A_h,\\
\mathfrak j:=A\cap\mathfrak J&=A_z\otimes J_h,\\
\mathfrak k:=A\cap K&=J_z\otimes J_h,
\end{aligned}
\tag{17}
\]

by (1). Exactness of finite-group invariants, or Reynolds averaging on the equivariant surjection \(\mathfrak I\oplus\mathfrak J\to\mathfrak I+\mathfrak J\), gives

\[
A\cap(\mathfrak I+\mathfrak J)=\mathfrak i+\mathfrak j.
\tag{18}
\]

Combining (15)–(18),

\[
\boxed{\mathfrak i\cap\mathfrak j
 =\mathfrak i\mathfrak j=\mathfrak j\mathfrak i
 =\mathfrak k=J_z\otimes J_h.}
\tag{19}
\]

The pure reductions are

\[
\begin{aligned}
A/\mathfrak i&\cong(A_z/J_z)\otimes A_h
 \cong(D/\mathfrak I)^G,\\
A/\mathfrak j&\cong A_z\otimes(A_h/J_h)
 \cong(D/\mathfrak J)^G,\\
A/(\mathfrak i+\mathfrak j)
 &\cong(A_z/J_z)\otimes(A_h/J_h)
 \cong(D/(\mathfrak I+\mathfrak J))^G,\\
A/\mathfrak k&\cong(D/K)^G.
\end{aligned}
\tag{20}
\]

Here \(G=G_z\times G_h\), and each equality to quotient invariants follows by averaging; no flatness over an invariant ring is assumed.

There is an exact sequence of additive groups (indeed of \(A\)-bimodules)

\[
0\to\mathfrak k\to A
 \to A/\mathfrak i\oplus A/\mathfrak j
 \xrightarrow{\ a-b\ } A/(\mathfrak i+\mathfrak j)\to0.
\tag{21}
\]

Equivalently, as rings,

\[
\boxed{A/\mathfrak k\cong
(A/\mathfrak i)\times_{A/(\mathfrak i+\mathfrak j)}(A/\mathfrak j).}
\tag{22}
\]

The fiber product in (22) describes the two compatible pure reductions. The full ring is \(A\), which still retains \(\mathfrak k\). Replacing \(A\) by that fiber product kills exactly the mixed ideal; such a replacement is not made here.

If the factor ideals are compatible with their Morita overlaps, the pure and mixed ideals in (14)–(15) are compatible with the external overlaps. In an invariant rank-one overlap frame, their descended overlap submodules are precisely multiplication by the ideals (17). Thus all of (17)–(22) are identities of the supplied coefficient ideal data on the Morita atlas, with their specified compositions. The strictification comparisons of Section 3 identify them.

## 5. Reduction on modules, and why inertia remains a separate hypothesis

For \(M\) as in (7), put \(N=M^G\). For each stable ideal \(L\) among \(\mathfrak I,\mathfrak J,K,\mathfrak I+\mathfrak J\), its invariant coefficient submodule is exactly

\[
(LM)^G=(L\cap A)N,
\qquad
N/(L\cap A)N\cong(M/LM)^G.
\tag{23}
\]

Proof: write every vector uniquely in the invariant basis. A vector is invariant exactly when every coefficient is invariant; membership in \(LM\) is coefficientwise membership in \(L\). Quotient invariants then follow by averaging, or directly in the same frame. In particular,

\[
(KM)^G=\mathfrak kN=\mathfrak i\mathfrak jN,
\qquad
\mathfrak iN\cap\mathfrak jN=\mathfrak kN.
\tag{24}
\]

These equations are the precise preservation of mixed coefficient multiplication at the module level. They hold for any module with the supplied invariant frame, whether or not it factors externally. On a covered module problem they hold in the local frames and glue through the supplied transitions.

The frame assumption cannot be removed merely because (19) is true for the algebra. In the already known synthetic double-sign example,

\[
D=k[[u,v]][s,t]/(s^2,t^2),\quad
G=C_2\times C_2,
\]

with the first generator changing both \(u,s\) to their negatives and the second changing \(v,t\), put \(x=u^2,y=v^2,\varepsilon=us,\eta=vt\). The invariant algebra is

\[
A=k[[x,y]][\varepsilon,\eta]/(\varepsilon^2,\eta^2),
\]

so its mixed ideal is indeed \((\varepsilon\eta)\). For a free cover generator \(e\) of double-negative character, however,

\[
(stDe)^G=k[[x,y]]\,st e,
\quad
(\varepsilon\eta)(De)^G=xy\,k[[x,y]]\,st e.
\tag{25}
\]

The algebra theorem retains the ramification defect rather than cancelling it. Such a module has no invariant free frame at the branch intersection. This is a boundary check drawn from the previous example, not a new physical computation.

## 6. The square-zero mixed extension attached to two pure directions

Assume now

\[
I_z^2=0,\qquad I_h^2=0.
\tag{26}
\]

Then \(\mathfrak I^2=\mathfrak J^2=0\), while their mixed product \(K=\mathfrak I\mathfrak J\) is kept. Moreover

\[
K^2=0,\qquad (\mathfrak I+\mathfrak J)K
 =K(\mathfrak I+\mathfrak J)=0.
\tag{27}
\]

The same statements hold for \(\mathfrak i,\mathfrak j,\mathfrak k\). Thus (22) fits into the exact mixed extension

\[
0\to\mathfrak k\to A\to
(A/\mathfrak i)\times_{A/(\mathfrak i+\mathfrak j)}(A/\mathfrak j)
\to0,
\tag{28}
\]

with square-zero kernel annihilated on both sides by the pure augmentation ideal. Its upstairs counterpart has kernel \(K\), and taking invariants identifies the entire extension with (28). Notice the difference between retaining the full two-parameter first-order tensor product and truncating by the total augmentation ideal squared: the latter would kill \(K\), which is expressly retained here.

Equation (26) is a hypothesis on the actual stable factor ideals. It is not licensed by replacing \((I_z^2)^{G_z}\) with \((I_z^{G_z})^2\): that latter comparison can fail for ramified actions. One can apply this section after passing to actual quotients \(D_z/I_z^2,D_h/I_h^2\), but their invariant coefficient ideals must again be the actual invariant intersections in those quotients.

## 7. Completed external products: the topology must be specified

Here is a sufficient formal version with no hidden interchange of arbitrary completions. Let \(D_z,D_h\) carry decreasing \(G_z,G_h\)-stable filtrations by two-sided ideals \(F_z^n,F_h^n\). Define the completed external product **by**

\[
\widehat D
 =\varprojlim_{n\ge1}
 D_n,\qquad
D_n=(D_z/F_z^n)\otimes_k(D_h/F_h^n).
\tag{35}
\]

The diagonal tower is cofinal in the rectangular \((n,m)\) tower. Ring multiplication and the group actions are componentwise continuous. Surjectivity of the quotient transition maps makes the projections from (35) onto its finite-level rings surjective. Completeness of each original \(D_i\) can be assumed if it is desired to identify it with its own completion, but (35) itself is the relevant definition.

Exactness of invariants at each level gives

\[
(D_z/F_z^n)^{G_z}
 =A_z/(A_z\cap F_z^n)
\]

and similarly for \(h\). Since taking invariants is an equalizer, it commutes with inverse limits. Therefore

\[
\boxed{
\widehat D^{G_z\times G_h}
 \cong\varprojlim_n
 \bigl(A_z/(A_z\cap F_z^n)\bigr)
 \otimes_k
 \bigl(A_h/(A_h\cap F_h^n)\bigr).
}
\tag{36}
\]

This is the completed tensor product for the **induced** filtrations. It is not a claim about an unspecified topology or about \(A_z\otimes A_h\) without completion. Finite Reynolds sums commute with the limit. Factorized units and equation (10) consequently pass to this completion.

For coefficient ideals, let \(I_{z,n},I_{h,n}\) be the images of \(I_z,I_h\) in the factor quotients, and use the level ideals

\[
\mathfrak I_n=I_{z,n}\otimes(D_h/F_h^n),\quad
\mathfrak J_n=(D_z/F_z^n)\otimes I_{h,n},\quad
K_n=I_{z,n}\otimes I_{h,n}.
\tag{37}
\]

Define \(\widehat{\mathfrak I},\widehat{\mathfrak J},\widehat K\) to be their inverse limits inside (35). All three towers in (37) have surjective transition maps. The same is true for their sums, and, after averaging, for their invariant ideals. At every level Sections 4–6 apply.

Taking intersections commutes with inverse limits, so

\[
\widehat{\mathfrak I}\cap\widehat{\mathfrak J}=\widehat K.
\tag{38}
\]

The exact sequences

\[
0\to K_n\to\mathfrak I_n\oplus\mathfrak J_n
 \to\mathfrak I_n+\mathfrak J_n\to0
\]

have surjective kernel transitions. The elementary exactness theorem for countable surjective inverse systems (proved by successive correction of lifts) therefore gives

\[
\widehat{\mathfrak I}+\widehat{\mathfrak J}
 =\varprojlim_n(\mathfrak I_n+\mathfrak J_n),
\tag{39}
\]

so the sum is closed. Likewise all pure, sum and mixed quotients commute with these inverse limits. A quick proof of the needed inverse-limit surjectivity is to lift a compatible target sequence inductively; at step \(n+1\), correct any lift by a kernel element whose image removes its discrepancy with the already chosen \(n\)-th lift. Kernel-transition surjectivity provides that correction.

Products require more care. The unconditional topological statement is

\[
\boxed{
\widehat K=\overline{\widehat{\mathfrak I}\,\widehat{\mathfrak J}}
 =\overline{\widehat{\mathfrak J}\,\widehat{\mathfrak I}}.
}
\tag{40}
\]

One inclusion follows by closedness of \(\widehat K\). Conversely, at any fixed level every element of \(K_n\) is a finite sum of products from the two pure ideals; each factor lifts to its inverse-limit ideal by the surjective tower property. The lifted sum approximates the desired element modulo the level kernel. This proves density, hence (40).

The invariant completed ideals satisfy the identical formulas, with \(J_{z,n}=I_{z,n}^{G_z}\), \(J_{h,n}=I_{h,n}^{G_h}\) and \(\widehat A=\widehat D^G\). All towers and the kernels just used remain surjective under invariants. Thus (36) preserves the closed coefficient square and its mixed closed product. No assertion that the **ordinary unclosed** ideal product equals \(\widehat K\) is made without an additional hypothesis ensuring that product is closed. At a fixed nilpotent/artinian coefficient truncation, the algebraic theorem already applies and no such topological issue arises.

For completed modules and overlap compositions require actual compatible finite-free invariant frames of fixed finite rank at every level, with complete separated inverse-limit modules and the stated continuous compositions. Finite direct sums commute with the inverse limit, so (23) holds for the closed coefficient submodules defined levelwise. A completed balanced tensor assertion is used only if that tensor is defined by these levelwise tensors and the finite-frame comparison identifies it with the stipulated complete overlap. This does not establish arbitrary completed tensor exactness, derived completion compatibility, or passage from isolated formal stalks to actual sheaves.

## 8. What is now conditional on what

The proof separates four obligations.

1. **Actual product data.** The mixed ambient, weak action, root/Morita lifts and overlap composition must genuinely be external for independent groups. Equality of pure cohomological classes does not provide these identities.
2. **Actual strictification and descent data.** Strictification sections, unit hypotheses, overlap invariant generators, module invariant frames, quotient atlas and sheaf effectiveness must be supplied. Nontrivial residual inertia is not removed by strictification.
3. **External mixed compatibility.** Under 1–2, the theorem proves exact external invariant descent, factorized comparison, preservation of the full coefficient square, mixed product, and coefficient-module reductions. The separate addendum treats a supplied framed mixed obstruction comparison. No additional arbitrary-invariants-tensor theorem is needed for this step.
4. **Physical value.** Identifying the supplied model with the physical mixed ambient and finding or evaluating its actual module obstruction remain separate. The theorem settles neither and provides no retained-value conclusion.

Accordingly this is a useful conditional closure of the external compatibility step, not a proof of the physical-to-corrected comparison. If the proposed physical presentation is not known to be a genuine independent external product, Sections 1–7 cannot be used to infer that it is one.
