# Exact presentation independent of the historical A certificate

## Conclusion and boundary

The literal homogeneous four-term complex

\[
5\mathcal O(-1)\xrightarrow{\gamma}15\mathcal O\xrightarrow{\delta}10\mathcal O(1)\xrightarrow{\mathrm{ev}}2\mathcal O(2)
\]

has no cohomology outside degree zero, and its degree-zero cohomology is a locally free rank-two normalized Horrocks–Mumford bundle. This conclusion, called **P**, does not require the historical identity
\(\gamma H_0+IP+H_1\delta=1\), called **A**. The proof is by exact identification with the classical monad and the Euler coresolution. All identifications below are explicit; no unverified change of basis is used.

This does **not** establish that the particular rational matrices I, P, H0, H1 in the source satisfy A. P implies existence of local splittings, not correctness of prescribed splittings. Any raw-source statement Q using those particular primitives still needs its relevant primitive identities, including A. No source/model matrix multiplication, rank evaluation, point substitution, jet evaluation, or residual computation was performed for this note.

## 1. Sources and the theorem being imported

- G. Horrocks and D. Mumford, *A rank 2 vector bundle on P4 with 15,000 symmetries*, Topology 12 (1973), 63–81: [author-hosted original](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf), §2, pp.67–69, especially (2.1), (2.3), Lemmas 2.4–2.5.
- E. Lee, *A Modular Quintic Calabi–Yau Threefold of Level 55*, Canadian Journal of Mathematics 63 (2011), 616–633: [published paper](https://doi.org/10.4153/CJM-2011-016-4), §2.1, pp.617–618. This supplies an especially transparent convention check for the two maps f+ and f− and the sign of the right-hand map.
- [Pinned ext-model §1](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md). The definitions below were read from its supplied inert snapshot; the public path and blob identifier were also verified.
- [Literal model](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-operator-compiler/hm-pinned-model.json).
- [Current global Hom argument](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-cm-global-hom/PROOF.md).

The original paper proves that its maps p and q are locally split, with p injective, q surjective, and qp=0; the middle cohomology is locally free of rank two. Lemma 2.5 proves injectivity using the explicitly listed cyclic bivectors, and surjectivity follows by duality. Thus the imported result is global subbundle/quotient-bundle exactness, not generic rank or merely the name “HM.” Lee writes the same construction using the ordered pair (f+,f−); its right-hand map has signs (−f−*,f+*).

## 2. Fixed conventions and the volume identification

Let P(V) parametrize lines in V, dim V=5, with ordered basis e0,...,e4 and volume vol(e0,...,e4)=1. Let Q be the tautological rank-four quotient, so T=Q(1). Put

\[
w_i^+=e_{i+2}\wedge e_{i+3},\qquad w_i^-=e_{i+1}\wedge e_{i+4},
\]

with indices modulo five, preserving the displayed order even when an index wraps around. The maps f± send the i-th source basis vector to w_i±. The five-dimensional source is a separately based copy of V; no representation-theoretic identification with a dual is being assumed.

The classical monad is

\[
5\mathcal O(2)\longrightarrow (\Lambda^2T)^2\longrightarrow5\mathcal O(3).
\]

Twisting by −3 gives 5O(−1) → E0 → 5O, where

\[
E_0=(\Lambda^2T(-3))^2=(\Lambda^2Q(-1))^2=(\Omega^2(2))^2.
\]

The last identification follows from det Q=O(1), the rank-four wedge pairing Λ²Q⊗Λ²Q→det Q, and Ω¹(1)=Q*. With the fixed volume, the embedding of one copy into Λ²V*⊗O sends the class represented by w, with its O(−1) factor v, to

\[
\phi_v(w)(u_1,u_2)=\operatorname{vol}(v,w,u_1,u_2).
\]

It vanishes whenever either u is v and is exactly the volume-dual of v∧w in Λ³V. This is the Euler/Koszul embedding, not an unspecified isomorphism.

Let B=(Λ²V*)²⊗O, and define the constant map b:B→5O by

\[
b(\eta^+,\eta^-)_i=\eta^+(w_i^-)-\eta^-(w_i^+).
\]

Under this volume identification, the left monad map has columns (φ_v(w_i+),φ_v(w_i−)). The right monad map in Lee's convention is −b restricted to E0. Multiplying the last term by −1 is the explicit constant isomorphism between the two conventions; in particular its kernel and surjectivity are unchanged.

### A direct structural check of the global monad hypotheses

The following exterior-algebra argument also spells out the classical exactness mechanism. It concerns formal wedge identities, not products or evaluations of source polynomial matrices. If i≠j, w_i+ and w_j− have a repeated basis vector; their wedge is zero. For i=j,

\[
w_i^+\wedge w_i^-=(-1)^i e_0\wedge\cdots\wedge\widehat e_i\wedge\cdots\wedge e_4.
\]

For formal scalars t_i, put a+=Σt_i w_i+ and a−=Σt_i w_i−. Therefore a+∧a− has the five independent complement-wedge coefficients (−1)^i t_i². If the two classes of a± in Λ²(V/kv) vanish for some nonzero v, then both a± belong to v∧V; their wedge vanishes and all t_i=0. This proves fiberwise injectivity of the left map for every projective point, over every field extension, and hence its subbundle property.

For composition zero, the i,j entry expressed intrinsically is

\[
\operatorname{vol}(v,w_j^+,w_i^-)-\operatorname{vol}(v,w_j^-,w_i^+)=0.
\]

Off the diagonal both wedges have repeated basis vectors; on the diagonal two degree-two exterior factors commute. This is an abstract alternating-form identity, not a multiplication of the literal gamma table.

Finally, at each line kv the form (u,w)↦vol(v,u,w) on Λ²(V/kv) is nondegenerate after trivializing the one-dimensional factors. On its two copies, the cross pairing

\[
((u^+,u^-),(w^+,w^-))\longmapsto
\operatorname{vol}(v,u^+,w^-)-\operatorname{vol}(v,u^-,w^+)
\]

is nondegenerate. The map β is exactly the transpose of α with respect to this pairing and the displayed source/target bases. Thus fiberwise injectivity of α proves fiberwise surjectivity of β, hence sheaf-surjectivity. This gives the needed global monad conditions directly and agrees with the original paper's Lemma 2.5 and duality argument.

## 3. Literal coefficient identification, not just a named bundle

Write a_i=dual(w_i+), c_i=dual(w_i−) in the oriented bivector basis. Set

\[
U_i=(a_i,0),\quad V_i=(0,c_i),\quad Z_i=(c_i,a_i).
\]

Then W=ker b has ordered basis (U0,...,U4,V0,...,V4,Z0,...,Z4). Indeed b kills these vectors, and on the complementary five vectors (c_i,0) it is the identity. This proves both the constant surjection and its exact kernel without any rank computation.

Here is the complete cyclic description of the three literal differential tables after homogenizing the affine coordinates (1,v1,v2,v3,v4) to (v0,v1,v2,v3,v4). Every unspecified coefficient is zero:

\[
\begin{aligned}
\gamma_{U_i,i+2}&=v_{i+1},&\gamma_{U_i,i+3}&=v_{i+4},\\
\gamma_{V_i,i+1}&=-v_{i+3},&\gamma_{V_i,i+4}&=-v_{i+2},\\
\gamma_{Z_i,i}&=v_i.&&
\end{aligned}
\]

These are precisely the coordinates of (φ_v(w_j+),φ_v(w_j−)). For the next table define the symbolic one-form

\[
D_{ab}=v_a e_b^*-v_b e_a^*.
\]

The ten target rows are ordered by the plus copy of (e0*,...,e4*), then the minus copy. The table is

\[
\delta(U_i)=(D_{i+2,i+3},0),\quad
\delta(V_i)=(0,D_{i+1,i+4}),\quad
\delta(Z_i)=(D_{i+1,i+4},D_{i+2,i+3}).
\]

Finally ev is the two-block row evaluation (v0,...,v4), with the other block zero in each row. This exhausts the entries of the pinned gamma, delta and ev by static coefficient inspection. Thus δ is literally paired contraction η↦η(v,−), and ev is literally paired evaluation. No reordering, transpose, inferred basis transformation, or sign normalization of the literal tables is needed.

## 4. Euler cancellation as an exact sheaf argument

The paired Euler coresolution is the exact sequence

\[
0\longrightarrow E_0\longrightarrow B\xrightarrow{d}C\xrightarrow{e}D\longrightarrow0,
\]

where C=(V*)²⊗O(1), D=O(2)², d is contraction and e is evaluation. Let β=b|E0, a surjection by the classical monad theorem. Let A0=5O(−1), and let α:A0→E0 be its subbundle injection. Since βα=0, α factors through W=ker b.

The kernel of d|W is E0∩W=ker β. Also d(W)=ker e: locally take c∈ker e and a lift z∈B; use surjectivity of β to choose t∈E0 with β(t)=b(z). Then z−t∈W and d(z−t)=c. Evaluation e is surjective by Euler exactness. Therefore

\[
A_0\xrightarrow{\alpha}W\xrightarrow{d|W}C\xrightarrow e D
\]

is exact in degrees −1,1,2 and its degree-zero cohomology is ker β/im α, the normalized HM bundle. The monad theorem guarantees this quotient is locally free. Its rank is 12−5−5=2.

This also proves local splitting of the four-term presentation. A bounded complex of vector bundles whose only cohomology is a vector bundle is locally a sum of contractible pairs and that cohomology bundle: successively split the displayed surjections onto locally free images, then the quotient onto the degree-zero bundle. Consequently arbitrary pullback preserves this presentation; no flatness hypothesis on the pullback is needed.

All maps have rational coefficients. The theorem over C descends to Q by faithful flatness (including local freeness of the coherent cohomology), and then extends to any characteristic-zero field by base change. This avoids assuming an arbitrary characteristic-zero field embeds into C.

## 5. What changes in the current global-Hom proof

Replace only the route used to establish P in §2 of the frozen global-Hom proof. Its global lifting arguments in §§3–5 can then use the locally free bundle and globally exact presentation supplied above without invoking the historical A receipt. Their other hypotheses and imported certificates remain separate, in particular the constant-gamma rank-250 result and the physical-bundle identification.

Hence the exact-presentation dependency is independently closed. The raw primitive dependency is not: this proof neither authenticates nor verifies the particular I,P,H0,H1, and must not be represented as a new A receipt or an authorization to evaluate the source.
