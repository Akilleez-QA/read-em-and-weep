> Publication scope: Reduced flag-incidence isomorphism and improved strata; independent-frame bound eight is an intermediate result superseded by15. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# The global nilpotent incidence and sharp reductions of the large frame strata

## Results

Under the structural hypotheses of the imported proofs, over C, let G=Gr(3,V), dim V=5, and let G_k denote the locally closed locus where dim ker T_W=k. Write q_W(A)=tr(A^2), h_W(A)=det A after a determinant-line trivialization. All assertions below are independent of that trivialization.

1. The reduced quadratic flag incidence B of ../../local-defect/rank-one-quadratic-flag-nef/PROOF.md is canonically isomorphic to the reduced global projective nilpotent-kernel incidence N. Its projection to G is the recovered-three-plane morphism already constructed there. In particular dim N<=3.
2. Let H_d be the locus where the projective nilpotent-kernel fiber has dimension at least d, for d>=0; empty fibers have dimension -infinity. Then H_d is closed and dim H_d<=3-d. In particular the closed locus of three-planes with any nonzero nilpotent in their kernel has dimension at most three, and the locus with a nilpotent curve has dimension at most two.
3. dim G_3<=3 and dim G_4<=2. The singular-net branch G_3 intersect {h_W identically zero} has dimension at most two. More generally the closed locus where K_W contains any determinant-zero three-dimensional subspace has dimension at most two.
4. Independent zero frames over G_3 or G_4 have dimension at most seven. Those over G_2 have dimension at most eight; their h_W-identically-zero branch has dimension at most seven, and their h_W-nonzero branch with a nilpotent kernel point has dimension at most six.
5. The entire independent-frame locus has dimension at most eight. A hypothetical nine-dimensional component would force a generic singular kernel line; the global saturated-kernel line-bundle argument in Section 7 excludes this alternative. Any eight-dimensional independent component must generically come from a five-dimensional spectral base in G_1, or from the nilpotent-free, h_W-nonzero branch of G_2.

These results improve the older four-dimensional bound for G_4 to two. In particular any degree-27 restriction formulated for hypothetical four-dimensional G_4 components has no actual component to which it applies. The universal Chern identities themselves remain valid on their stated bases.

No actual operation matrix, product, selected input, rank instance, residue, jet, or source-model computation is evaluated. Only universal bundle and projective geometry are used. All writes are local proof files.

## Imports

- ../../cubic-loci/global-kernel-incidence/general-three-plane-kernel/PROOF.md: E=sl(S) tensor det S, the global map T:E -> J tensor O_G, rank-one exclusion, k<=4, the spectral incidence, and the degree-two orientation cover followed by a three-dimensional torus bundle.
- ../../local-defect/rank-one-normal-obstruction/PROOF.md, Section 3: the pointwise correspondence between quadratic directions and regular nilpotent kernel tensors.
- ../../local-defect/rank-one-quadratic-flag-nef/PROOF.md: the projective reduced flag incidence B, its global recovered subbundle W, and dim B<=3.
- ../nilpotent-frame-boundary/PROOF.md: every K_4 has a pure one-dimensional nonempty nilpotent locus, h_W is nonzero, and q_W is nonzero; a determinant-zero K_3 has a smooth nilpotent conic.
- ../../cubic-loci/global-kernel-incidence/full-cubic-locus-dimension/PROOF.md: the closed locus dim K_W>=2 is proper in G, hence has dimension at most five; the full zero locus has three coordinate-zero components of dimension ten and no larger components.
- ../../cubic-loci/cubic-component-multiplicities/applications/four-kernel-empty-incidence/PROOF.md: the independent open has dimension at most nine, so exactly those three components have dimension ten. This can alternatively be recovered from the improved estimates below.

## 1. A single projective nilpotent incidence across rank jumps

Let S be tautological on G and D=det S. On P_G(E), with the convention of lines, let R=O(-1). The universal inclusion R -> E yields a twisted traceless endomorphism

    A:S -> S tensor M,       M=R* tensor D.

Define N_0 by the equations

    T(R)=0,   tr(A^2)=0,   det(A)=0,

and set N=(N_0)_red. This is a closed projective G-scheme. Its geometric fiber over W, after reduction, is precisely

    N_W={ [a] in P(K_W) : q_W(a)=h_W(a)=0 }_red.

The projective tensor is nonzero. Cayley-Hamilton says A^3=0. Rank-one exclusion then implies that every geometric point is regular nilpotent: rank A=2 and rank A^2=1.

Because N is reduced, constant geometric ranks give kernel and image subbundles. Indeed locally an appropriate minor is invertible, row and column operations give an identity block, and the remaining block entries vanish at every geometric point and hence vanish on the reduced base. Thus

    F_1=ker A,       F_2=ker A^2

are subbundles of ranks one and two. The twists in A and A^2 do not affect their kernels. They define a morphism

    j:N -> Flag(1,2;V),       (W,[a]) |-> (F_1 subset F_2).

For a regular nilpotent in dimension three, F_2=(im A) tensor M^(-1), viewed as a subbundle of S. The pointwise inverse calculation in the normal-obstruction proof says this flag lies in B. Since N is reduced, the defining equations of B pull back to zero; thus j factors through B_red=B.

## 2. The inverse morphism from quadratic flags

Recall the construction on B. Locally choose u spanning its line L and a lift p of a nonzero frame of P/L, where P is its rank-two flag plane. There is a unique q modulo L with

    f(u,u,q)=f(p,u,p).

Its class modulo P is nonzero. The recovered three-plane W is spanned locally by u,p,q and is a global subbundle. Define the nonzero tensor

    k=2p tensor (u wedge p) - u tensor (u wedge q) in E_W.

It lies in ker T_W. Under the determinant trivialization u wedge p wedge q, its endomorphism sends u to zero, p to u, and q to 2p. Hence it is regular nilpotent and determines a point of N.

This construction is a morphism, not just a pointwise assignment. Changing q by a multiple of u changes nothing. If u'=a u and p'=b p+c u, the recovered class satisfies

    q'=(b^2/a)q+(2bc/a)p modulo L.

Direct substitution into the universal tensor gives

    k'=a b^2 k.

Thus the local tensor lines glue to a line subbundle of E pulled back along the recovered-three-plane map g:B -> G. This supplies a morphism i:B -> P_G(E). Its image lies in N_0 by the tensor identities, and factors through N because B is reduced.

The pointwise correspondence in the normal-obstruction proof shows i and j are inverse on geometric points: j remembers (ker A, im A), and i recovers the unique W and projective tensor. They are inverse as morphisms of reduced schemes. To justify the last step, morphisms from a reduced finite-type C-scheme into a separated scheme that agree on all closed points agree as morphisms: locally the pullbacks of the ideal of the diagonal vanish at every closed point and hence are zero. Apply this to both composites.

Therefore

    B is isomorphic to N,      g corresponds to N -> G.

This explicitly avoids the false general inference that a proper geometric-point bijection must be an isomorphism. The morphism inverse is constructed here. No isomorphism of the unreduced incidence schemes is claimed.

## 3. Fiber-dimension bounds

For d>=0 define H_d={W in G : dim N_W>=d}. Properness of N -> G implies upper semicontinuity of fiber dimension, so H_d is closed; H_0 is simply its closed image. The same assertion follows from the usual proper fiber-dimension theorem with the convention for empty fibers.

If Z is any integral component of H_d, restrict N to Z. At its generic point the fiber has dimension at least d. A component of this restricted incidence dominating Z therefore has dimension at least dim Z+d, by the dimension formula. It is a locally closed subset of N, whose dimension is at most three. Hence

    dim H_d<=3-d.

The argument also bounds any constructible sublocus of H_d and its closure. We use only geometric-fiber dimensions, which are unchanged by reduction.

For k=3, N_W is nonempty: any two homogeneous positive-degree equations q,h on P^2 have a common zero over C; if one or both equations are identically zero, the conclusion is immediate. One can use the projective dimension theorem when both are nonzero. Consequently G_3 lies in H_0 and dim G_3<=3.

For k=4, the imported fixed-kernel theorem gives dim N_W=1. Hence G_4 lies in H_1 and dim G_4<=2. A determinant-zero K_3 has its smooth nilpotent conic, so its base also lies in H_1 and has dimension at most two. If K_W contains a determinant-zero three-dimensional subspace L, rank-one exclusion applies to L and its nilpotents form a conic by the same classification. Thus this entire locus lies in H_1, proving its two-dimensional bound as well.

When k=3 and q,h are both nonzero, their common zero locus has dimension one exactly when they have a common homogeneous factor. Its base is then contained in H_1, of dimension at most two; otherwise N_W is nonempty finite and its base lies in H_0, of dimension at most three. If q=0 and h is nonzero, N_W is a plane cubic support of dimension one and the base bound is two, but there are no independent frames. The q=h=0 alternative would give N_W=P^2 and the abstract bound one; it is actually excluded by the imported constant-rank-net classification, which forces q of rank three when h=0 on K_3.

For k=2, N_W is empty, finite nonempty, or all of P^1. The last case is exactly q=h=0 and gives base dimension at most two, with no independent frames. If h=0 and q is nonzero, N_W is nonempty finite, so that base has dimension at most three. If h is nonzero and N_W is nonempty, the same dimension-three base bound holds. No nilpotent-incidence bound is claimed for the nilpotent-free pencil locus.

For k=1, N_W is either empty or its unique projective point. The latter base has dimension at most three and has no independent frames. These statements also show that generic nilpotence of a line kernel over a dense open in G is impossible.

## 4. Complete dimension bookkeeping for independent frames

Let X_W=V(h_W) minus V(q_W) inside P(K_W). Every nonempty independent-frame fiber over W has dimension dim X_W+3, by the imported orientation-cover and torus-bundle description. On all stated subloci one may use a finite locally closed refinement, or the dimension theorem for constructible loci.

- k=0: no frames.
- k=1: X_W is either empty or a point. The base has dimension at most six, so the contribution is at most nine. The nonempty case is exactly h_W=0 and q_W nonzero.
- k=2, h_W=0, q_W nonzero: X_W is a nonempty open of P^1, so the frame fiber has dimension four. The base has dimension at most three by Section 3, giving total at most seven.
- k=2, h_W nonzero: X_W is finite or empty, so frame fiber dimension is at most three. The established proper rank-drop locus gives base dimension at most five and total at most eight. If N_W is nonempty, its base has dimension at most three, improving the contribution to at most six.
- k=2, q_W=0: no frames, regardless of h_W.
- k=3, h_W=0: the frame fiber has dimension five, and the base has dimension at most two, giving total at most seven.
- k=3, h_W nonzero: X_W has dimension at most one, so frame fiber dimension at most four; the base has dimension at most three, giving total at most seven. If q_W,h_W are both nonzero and share a factor, the base bound improves to two and the contribution to at most six. If q_W=0, there are no frames.
- k=4: X_W has dimension two by the imported density theorem, so the frame fiber has dimension five; the base has dimension at most two, giving total at most seven.

Thus the global independent-frame dimension remains bounded by nine, but only the line-kernel branch can achieve nine. The only other branch capable of dimension eight is the nilpotent-free pencil branch with nonzero restricted determinant.

## 5. Exact generic criterion for a nine-dimensional component

Define the constructible spectral line-kernel base

    U_1={W in G_1 : h_W=0 and q_W nonzero}.

The kernel is a line bundle on G_1, so the conditions define a locally closed subset there. Over U_1 the spectral incidence is simply its unique projective kernel point, and the orientation cover and torus bundle give total frame dimension dim U_1+3. Section 4 shows all other branches have dimension at most eight. Hence the independent open has a component of dimension nine if and only if dim U_1=6.

Since G is irreducible of dimension six, a constructible subset has dimension six if and only if it is dense; every dense constructible subset contains a dense open. Therefore dim U_1=6 is equivalent to the following statement at the generic point of G:

    dim K=1, det|K=0, tr(A^2)|K nonzero.

The last condition is automatic from the first two: otherwise a dense open would have a nilpotent kernel point, contradicting dim H_0<=3. Consequently the criterion reduces to a generic line kernel with identically vanishing determinant.

Finally, a nine-dimensional irreducible subset of the independent open closes to an irreducible component of the full zero locus. Any full component containing it meets that open, so its dimension is at most nine by Section 4; equality of dimensions forces the closure to be that component. Conversely every nine-dimensional full component meeting the independent open has a dense independent part and must have dense line-kernel spectral base by the same estimates. This proves the stated if-and-only-if criterion for actual irreducible components, rather than only for strata.

The imported AP independent-frame existence ensures some independent component exists. The criterion just established is intermediate: Section 7 excludes its generic singular-line alternative. No evaluation of the generic kernel is required for that exclusion.

## 6. Rank-one boundary and limits of the argument

The other projection B -> P(V) has closed image E of dimension at most three, as already proved in the flag-nef argument. Thus the all-inputs-nonzero rank-one portion in the closure of independent frames still has dimension at most six. The two projections have different fibers: H_d concerns varying three-planes, whereas E concerns kernel lines in V. No equality between their images is implied.

The bounds do not assert any G_4, singular net, common-factor net, or nilpotent pencil actually occurs. The incidence argument alone does not improve the total independent-frame bound below nine; Section 7 supplies the additional global line-bundle obstruction and improves it to eight. Neither argument calculates scheme multiplicities or exact component counts.

## 7. The generic singular-line alternative is impossible

The criterion of Section 5 can itself be excluded, without evaluating any operation. Consequently the independent-frame dimension improves from nine to eight.

Suppose for contradiction that the generic kernel of T is one-dimensional and its determinant is zero. Let

    L=ker(T:E -> J tensor O_G)

be the coherent kernel sheaf on all of G, and I=im T. The quotient E/L=I is torsion-free because I is a subsheaf of the vector bundle J tensor O_G. In particular L is saturated in E.

The sheaf L is reflexive. It is torsion-free as a subsheaf of E. At a stalk of dimension at least two, I is a nonzero torsion-free module over a regular local domain, hence has depth at least one. The depth lemma in

    0 -> L -> E -> I -> 0

then gives depth L>=min(depth E,depth I+1)>=2. At smaller-dimensional stalks torsion-freeness gives the required S2 bound. Thus L is torsion-free and S2, which on the normal smooth variety G is equivalent to reflexivity. Since its generic rank is one and G is locally factorial, L is a line bundle.

Set U=L tensor D^(-1). Untwisting its inclusion in E gives a nonzero bundle morphism

    A:U -> sl(S).

At every codimension-one point of G this inclusion is primitive and nonzero on the residue field. Indeed the local ring there is a DVR, and the torsion-free quotient E/L is free, so the inclusion splits locally. This assertion is only needed in codimension one; the inclusion of the line bundle may vanish in higher codimension, and we do not assume otherwise.

The determinant of A is a global section of U^(-3). It is zero at the generic point by hypothesis and therefore zero everywhere. Its trace-square is a global section

    q in H^0(G,U^(-2)).

This section is nonzero: if it vanished identically, the generically nonzero kernel tensor would be nilpotent on a dense open, contradicting dim H_0<=3.

Suppose q has a nonempty zero locus. A nonzero section of a line bundle on the smooth integral G has an effective Cartier zero divisor. If nonempty, it has an irreducible divisorial component Z, of dimension five. At the generic point of Z, primitivity of A makes its value nonzero. Both its determinant and trace-square vanish there, so it defines a nonzero nilpotent tensor in the kernel. Thus the generic point of Z belongs to the closed image H_0 of N. Because H_0 is closed, Z lies in H_0, contradicting dim H_0<=3.

Therefore q is nowhere zero and trivializes U^(-2). The Picard group of Gr(3,5) is Z, generated by the Plucker line bundle, and has no torsion. Hence U is trivial. The nonzero morphism A would then give a nonzero global section of sl(S).

But H^0(G,End(S)) consists only of scalars. Here is an elementary proof. Let p:P_G(S)->G be the projective bundle of lines, and r:P_G(S)->P(V) its map remembering the line in V. The fibers of r are Gr(2,V/line), and r is a relative Grassmannian, so r_*O=O; equivalently it is locally a product with a connected projective Grassmannian, whose only global regular functions are constants. The tautological hyperplane line satisfies

    O_P(S)(1)=r*O_P(V)(1).

The projective-bundle formula for p and projection formula for r yield

    H^0(G,S*)=H^0(P_G(S),O(1))=H^0(P(V),O(1))=V*.

The inclusion S -> V tensor O_G embeds

    H^0(G,End S) -> H^0(G,Hom(S,V tensor O_G))=V tensor V*=End V.

An endomorphism in this image preserves every three-plane W in V. For each line ell, the intersection of all three-planes containing ell is ell, so the endomorphism preserves every line. A linear map preserving every line is scalar: apply this to independent vectors and their sum. Conversely scalar endomorphisms occur. Thus H^0(G,End S)=C and, in characteristic zero, H^0(G,sl S)=0.

This contradicts the nonzero A. The generic singular-line alternative is impossible.

## 8. Strengthened conclusion and the remaining eight-dimensional branch

By Sections 4, 5, and 7,

    dim Z_ind <= 8.

In particular every irreducible component meeting the independent open has dimension at most eight. All other conclusions about the three ten-dimensional coordinate components, the seven-dimensional nonreduced rank-one component, and the existence of at least one independent component remain valid.

There is a useful refinement of the frontier. If G_1 is not dense, its dimension is at most five, so its frame contribution is at most eight. If G_1 is dense, Section 7 says its generic determinant is nonzero; therefore its spectral zero locus has dimension at most five, again giving frame dimension at most eight. In either case an eight-dimensional independent component can still arise from a five-dimensional spectral line-kernel base, or from the nilpotent-free nonzero-determinant pencil branch over a five-dimensional base. The present argument does not exclude either branch or prove that either occurs.

The only possible contributions of dimension greater than seven are now precisely these two types. The line-bundle contradiction used a generic rank-one kernel on the full Grassmannian; it does not apply directly to a kernel line defined only on a divisor, and it must not be silently reused there.
