# Generation detects the source126 zero-source radical and removes one Type III direction

## Result and scope

Assume an actual occurrence of source126, with the simultaneous negative-pencil reconstruction and canonical invariant positive quadratic Q of PR944. Write D_Q for its Q-compatible negative-pencil algebra. Then restriction to the first endpoint is injective:

    D_Q -> End_G(N2).

In Type III the radical J=J_X direct-sum J_Y has two one-dimensional arrows. Every nonzero j_X in J_X satisfies

    j_X,2=0, im(j_X,4 Q)=P, rank(j_X,4 Q)=4.

Consequently J_Q intersect J_X=0 and

    Type III: D_Q=C1 plus J_Q, dim J_Q<=1, J_Q squared=0.

If a nonzero compatible radical line exists, its projection to J_Y is an isomorphism. Equivalently, after choosing nonzero generators x,y of J_X,J_Y, it is C(y+t x) for a unique scalar t. Neither existence of that line nor its t is asserted. The old dimension-three compatible algebra is now impossible in Type III; scalarity is not proved. Types I and II retain the previous upper bound dim J_Q<=2, together with the new faithful-first-endpoint restriction.

There is also forced actual support: the Type III X-target projection satisfies

    p_X,4 Q:N2 -> N4_X=V+P is onto,

so its rank is seven. These ranks follow from exact geometry and generation, not from evaluating an actual matrix. Neither source126 pairing nor any stable label is removed.

## 1. Inputs and conventions

INPUTS.json pins four original proof files, with exact Git blob and SHA256 hashes and copied bytes in inputs/.

- PR862 at e103e25456897a1123f9636eb20080e8641ce66a gives the whole covariant fixed-negative-pencil algebra and genuine constant normal form.
- PR944 at 84d7c9b3ee57c0a12c9e99816ec690cd8ea7ffbc proves D_Q=C1 plus J_Q, J_Q subset J, J squared=0, and the reconstructed endpoint characters.
- PR925 at 2be52725fe471efdc64d74bd87702b581f9f6a48, Section 2 ONLY, proves the source-independent actual degree-zero-generation identity N4=im q_+ + im q_-. Its later c-d-f-specific conclusions are not imported.
- PR933 at 804661fb49e245a8df884937bb8d38fb5d0dc17a, Sections 1–4, proves the source-independent equality of actual subspaces im q_+=im Q. Its c-d-f-specific Section 6 is not imported.

Here q_-:Sym2(W) tensor N2 -> N4 is the actual product B_u A_v in the same fixed negative variables. The aggregate q_+ uses all positive-coordinate quadratics; Q uses the canonical invariant one. The actual-image equality does not identify these maps. Together the last two inputs give

    N4=im Q+im q_-.                                      (1)

No direct sum is assumed.

## 2. A zero first endpoint is detected by Q

Let e be any negative-pencil endomorphism with e2=0. Its two intertwining identities imply, for every formal u,v in W,

    e4 B_u A_v=B_u e3 A_v=B_u A_v e2=0.

Thus e4 kills im q_-. Applying e4 to (1) gives the stronger exact image identity

    im(e4 Q)=im e4.                                      (2)

In particular if e is Q-compatible, e4Q=Qe2=0, so e4=0. Merely knowing the kernel and cokernel characters of Q would not give (2); the actual image-sum premise is essential.

## 3. The fourth endpoint faithfully represents the source126 radical

The PR862 constant normal form is

    H=C plus Hbar, E=F plus R,
    F=F0 O(-2), F0=P+2D,
    R=O(-8) plus W O(-9).

An element j_b of J comes from a constant b:Hbar->C with b(R) contained in F and acts by zero on C. Since R spans Hbar, restriction b|R is zero only when b=0. Therefore J injects into Hom_G(R,F).

The natural map

    Hom_G(R,F0 O(-2)) -> Hom_G(H1(R),F0)

induced by H1 is an isomorphism. Indeed equivariant Serre duality identifies H1(R)* with H0(R*(-2)), while H1(F0 O(-2))=F0. Both Hom spaces are therefore naturally (F0 tensor H0(R*(-2)))^G. Under those identifications the induced cohomology map is the same contraction, so this is an isomorphism of maps, not only equality of dimensions. The canonical bundle O(-2) has the trivial determinant linearization for G subset SL2.

By covariant reconstruction, the induced H1 map is precisely j4:N4_R->N4_F, extended by zero on N4_F. Hence

    j4=0 implies j=0 for every j in J.                   (3)

Combining (2) and (3), the first-endpoint restriction is injective on J_Q. It is also injective on D_Q: by PR944, e=lambda1+j; on the nonzero F-source block N2_F, j2 is zero and e2=lambda1. Thus e2=0 forces lambda=0, and then j=0. This proves the first assertion without assuming any full-module extension.

## 4. Type III: a forced rank-four radical channel and a rank-seven target row

In Type III, PR944 gives

    N2_X=0, N4_X=V+P, N4_F=P+2D.

For nonzero j_X, the restricted bundle map X=O(-8)->F is nonzero: its constant map is supported on the span P+D of X, and X spans that space. Section 3 then makes its induced cohomology map nonzero. Equivariance and the displayed endpoint characters permit only the single P-to-P channel. By irreducibility it is an isomorphism on that channel, so im j_X,4=P and its rank is four. The first endpoint j_X,2 is zero because its only source vertex is X.

Equation (2) now forces im(j_X,4 Q)=P, rank four. Thus no nonzero X-arrow can be Q-compatible. Since J_Q is a linear subspace of the two-space J_X plus J_Y disjoint from J_X, its projection to the one-dimensional J_Y is injective. This proves dim J_Q<=1 and the graph-line description in the statement.

The same argument applies to the actual X-vertex projector p_X in the full negative-pencil algebra: p_X,2=0, whereas im p_X,4=N4_X=V+P. Equation (2) proves p_X,4 Q onto V+P, rank seven. The projector itself is not Q-compatible, and no inference of Q-invariance of this vertex splitting is made.

## 5. Why the multiplicity-free Bockstein shortcut cannot replace this argument

For any j in J_Q, its induced endomorphisms of ker Q=A+D and coker Q=P are G-equivariant and square-zero. These representations are multiplicity-free, so their equivariant endomorphism rings are products of copies of C and have no nonzero nilpotents. Both induced maps are therefore zero. An equivariance identity between these endpoint actions is automatically satisfied and does not exclude j. Our contradiction instead uses the represented nonzero j4 and the actual spanning identity (1).

A small synthetic endpoint control shows why image generation cannot be silently omitted. Take domain C, target C^2, Q(1)=(1,0), e2=0, e4(a,b)=(b,0), and q_-=0. Then e4 squared=0, e4Q=Qe2=0, and e4 acts trivially on ker Q and coker Q, but e4 is nonzero. Here im Q+im q_- is only a line, not the whole target. This is solely a counterexample to the weakened endpoint inference, not an actual HM example or a complete negative pencil.

## Verification and remaining work

verify.py authenticates the four inputs, checks the fixed symmetric-power characters used for the X-arrow, exhausts two-parity monomial factorization through a finite range as a regression for the general written proof in PR925, and checks the synthetic negative control and formal two-dimensional graph restriction. These tests support, but do not replace, the mathematical argument; they are not a proof-assistant certificate. No HM coefficient, selected point, chosen actual parameter or actual-instance matrix is evaluated.

The possible mixed radical line remains unresolved. Neither triviality of J_Q nor nontriviality is required for source occurrence by any theorem used here. The four surviving source-dual pairings and three stable labels are unchanged. This is an additional necessary compatibility restriction, not the complete repair.
