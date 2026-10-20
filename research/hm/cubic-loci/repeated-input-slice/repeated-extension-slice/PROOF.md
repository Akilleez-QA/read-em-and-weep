# The scheme-theoretic repeated-input filtered-extension slice

## Statement

Work over C. Let V have dimension five, let J=J3, and let f:V×V×V→J be the established canonical trilinear cubic. Assume the proved identities and structural nonvanishing theorem:

- f(u,u,u)=0 identically;
- f(u,u,w)≠0 whenever u,w are linearly independent complex vectors.

Set X=V_u×V_w, S=C[X], a=(u_1,...,u_5), and

    G(u,w)=f(u,u,w),
    I=(λ(G):λ∈J*),
    D=(u_i w_j-u_j w_i:1≤i<j≤5).

Coordinates here only specify universal ideals; no value or source-model operation is evaluated. Then:

1. Over U=V\{0}, the vector-bundle morphism B:V⊗O_U→J⊗O_U, w↦G(u,w), has constant rank four and kernel L=O_U·u, a line subbundle.
2. Its scheme-theoretic zero locus in U×V is Tot(L), canonically isomorphic to U×A¹ by (u,t)↦(u,tu). These assertions are preserved by arbitrary base change, including nonreduced bases.
3. I:a^∞=D, and √I=D globally. In particular the underlying reduced scheme is the rank-at-most-one locus of the universal two-column array (u,w), irreducible of dimension six.
4. I≠D, both globally and at the origin. Thus the cubic slice is genuinely nonreduced at the origin. Its nonreduced locus is in fact exactly {u=0}; this does not specify its primary decomposition, nilpotence orders, or embedded associated primes.
5. Under the imported framed filtered-extension representation theorem, the repeated-input filtered rank-eight extension functor over U is represented by Tot(L), with an actual universal algebraic filtered bundle. For arbitrary affine bases with u nowhere zero, completion exists if and only if w=tu for a unique regular scalar t. Over bases meeting u=0 the correct condition remains G(u,w)=0, not merely the determinantal equations or fiberwise proportionality.

## Imported inputs and logical scope

Read alongside:

- [the cubic structural nonvanishing manuscript](../../cubic-structural-nonvanishing/cubic-structural-nonvanishing/PROOF.md): universal structural repeated-input nonvanishing and canonicity of f;
- [the cubic filtered extension obstruction manuscript](../../canonical-cubic-extension/cubic-filtered-extension-obstruction/PROOF.md): representability on arbitrary affine complex bases, the actual universal algebraic filtered bundle, and uniqueness up to unique graded-framed filtered isomorphism;
- [the extension locus singularity manuscript](../extension-locus-singularity/PROOF.md): the distinction between homogeneous cubic scheme structure and its reduced support;
- [the cubic explicit weight basis manuscript](../../cubic-witness-detectors/cubic-explicit-weight-basis/PROOF.md): compatible trilinearity, cyclic-zero identity, and actual nonvanishing status.

The dimension twenty of J and the explicit weight basis are not needed for the subbundle or saturation argument. The cyclic-zero identity gives f(u,u,u)=0 in characteristic zero. This is a polynomial identity, not merely a statement after a selected substitution. The formerly conditional nonzero scalar is now discharged by the structural nonvanishing theorem. This proof imports that theorem rather than repeating its geometric or pairing argument.

## 1. From structural nonvanishing to a split bundle inclusion

The universal vector u is nowhere zero on U. Hence O_U→V⊗O_U, 1↦u, is a subbundle inclusion: on D(u_i), the i-th coordinate gives a retraction after division by u_i. Write its image L and its locally free rank-four quotient Q.

Trilinearity gives a bundle morphism B with coefficients quadratic in u. The diagonal identity says B(u)=0, so B factors as

    V⊗O_U → Q →[Bbar] J⊗O_U.

For each complex closed base point u, structural nonvanishing says precisely that the kernel of B on that fiber is C·u. Thus Bbar is injective on every closed fiber. The locus where a map from a rank-four bundle fails to have rank four is closed, defined locally by its maximal exterior-power coordinates. If nonempty on the finite-type complex scheme U, that locus would have a closed complex point. Therefore it is empty. This is a universal degeneracy-locus argument deduced from the proved theorem; it is not a rank calculation at any chosen input.

Locally an invertible maximal minor makes Bbar a split injection: project to its corresponding four target coordinates and invert that isomorphism. Its cokernel is locally free. Hence B has image a rank-four subbundle, kernel exactly L, and remains so under every base change.

## 2. Equality of zero schemes

On a local splitting V⊗O_U=L⊕Q, and after a local splitting of Bbar, the equations B(w)=0 are equivalent as ideals to the four linear fiber coordinates of the Q-component of w. Indeed a left inverse to Bbar recovers those four coordinates from B(w), and B(w) itself is a linear combination of them. The equations therefore cut out Tot(L) exactly, with no infinitesimal thickening.

Alternatively, for every T→U, the kernel of the pulled-back map on sections is L_T, because the displayed split exact sequences survive arbitrary base change. This characterizes the represented zero functor on all test schemes.

Here L is the pullback to U of the tautological line O_{P(V)}(-1) under u↦[u]; it is canonically trivialized on U by the actual vector u. We are not claiming that O_{P(V)}(-1) itself is trivial. Consequently Tot(L)≅U×A¹, with w=tu, and t is unique and regular.

The minors defining D give the same kernel scheme over U. On D(u_i), they are equivalent to

    w_j=(w_i/u_i)u_j for j≠i.

It follows that I S[u_i^{-1}]=D S[u_i^{-1}] for all i.

## 3. Global radical and saturation

We recall the elementary universal determinantal fact: the ideal of 2×2 minors of a generic 5×2 array is prime, and defines the rank-at-most-one scheme. One algebraic proof presents its coordinate ring as the subring of C[z_1,...,z_5,s,t] generated by z_i s,z_i t. The kernel of u_i↦z_i s, w_i↦z_i t is exactly the minor ideal: swapping a u-index and a w-index by the minor relations connects monomials with the same total index multiplicities and the same u/w degrees. Distinct such classes have distinct images. This proves the kernel statement and primality without evaluating any array. The fraction field of this subring has transcendence degree six, as is also seen on D(u_i), where its ring is a polynomial ring in the five u coordinates (u_i inverted) and the ratio w_i/u_i.

The closed complex points satisfying G=0 are exactly the dependent pairs. For u≠0 this is the imported theorem and diagonal vanishing; for u=0 it follows from trilinearity. The dependent-pair set is exactly V(D), including all of {u=0}. Hilbert's Nullstellensatz and primality therefore give √I=D; in particular I⊂D.

For an ideal a generated by the u_i, saturation is the ideal of sections vanishing on the restriction to ⋃D(u_i):

    I:a^∞ = ⋂_i (I S[u_i^{-1}]∩S).

This standard equality can be checked directly: separate powers u_i^{n_i} killing a class imply that a sufficiently large power of a kills it, by the pigeonhole principle on monomials. Section 2 replaces every localized ideal by D. Since D is prime and no u_i lies in D, each contraction D S[u_i^{-1}]∩S is D. Thus I:a^∞=D.

In particular some finite exponent N satisfies a^N D⊂I by Noetherian finite generation. No specific exponent is asserted.

## 4. What happens over the zero vector

The ideal I is homogeneous of bidegree-generated type (2,1), hence lies in the cube of the maximal ideal m of the total origin. The nonzero quadratic minors generate D. Thus I≠D globally. The same strictness holds in S_m: a nonzero quadratic minor has order exactly two, while I S_m⊂m³S_m. As √(I S_m)=D S_m, the local ring (S/I)_m is nonreduced. This uses ideal orders only, not any input or jet evaluation.

There is a slightly stronger structural conclusion. Let p be any complex closed point with u=0 and w≠0. Every generator of I lies in (u)², hence in m_p². Choose an index j with w_j(p)≠0 and i≠j. The minor u_i w_j-u_j w_i has nonzero class in m_p/m_p²: its linear part has u_i coefficient w_j(p)≠0. Therefore D S_p is not contained in m_p², whereas I S_p is. So I S_p≠D S_p and this local ring is nonreduced as well. This is a general order-of-vanishing argument along the universal axis, not a calculation at a selected numerical input. Together with the origin argument and reducedness over U, this identifies the nonreduced locus exactly as {u=0}. Equivalently the coherent nilradical module D/I has support exactly that axis; its support is closed, so checking its closed points suffices.

The scheme-theoretic fiber over u=0 is nevertheless the reduced affine space V_w: putting u=0 kills I, so S/(I+a)=C[w]. A reduced fiber does not imply that its surrounding total space is reduced. The additional structure is transverse to, or interacts with, that fiber.

No primary decomposition, exact nilpotence order, length, multiplicity, or list of associated primes is determined. Nor does this result identify the scheme structure of the full three-independent-input extension locus. Its pullback to this slice can be nonreduced even when properties of the ambient extension locus remain unresolved.

## 5. Filtered extension existence and algebraicity

Let Z_f⊂V³ represent the previously proved graded-framed filtered rank-eight bundle functor. Pull it back along the closed slice map X→V³, (u,w)↦(u,u,w). Functoriality gives precisely Z_G=Spec(S/I), with its full cubic scheme structure and the pullback of the actual universal algebraic filtered bundle.

For an affine complex base T and u:T→U, Section 2 identifies maps T→Z_G with w=tu for a unique t∈Γ(T,O_T), including nilpotent coefficients. The corresponding filtered bundle exists and is unique up to a unique isomorphism preserving the filtration and acting identically on the four framed graded factors. Algebraicity is inherited from the universal bundle; it requires no pointwise choices of primitives or limiting procedure.

Over complex points this says that the repeated-input adjacent classes (u,u,w) admit a completion exactly when u,w are dependent; when u=0 every w is permitted. For a nonreduced base meeting the zero axis, this closed-point criterion is insufficient. The actual representative is the nonreduced cubic scheme Z_G. Replacing it by Spec(S/D) would discard genuine infinitesimal extension families, as I⊊D. No specific infinitesimal family or Massey value is evaluated here.

