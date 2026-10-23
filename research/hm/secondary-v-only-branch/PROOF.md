# Constant rank and a canonical kernel discriminant in the V-only secondary branch

Work over C with G=SL2(F5), T=P(W*), A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, V the other even three-space, and P=W tensor W'. All equivariant line-bundle twists are retained.

## 1. Exact inputs and new branch

The exact originals in Akilleez-QA/read-em-and-weep are recorded in INPUTS.json:

- FIBER: PR1004, 0b9a8505e71951cf54950f54458c96cae0520146, research/hm/secondary-fiber-completion/PROOF.md. Only its unconditional channel constructions are used here, not its separate two-D-channel hypothesis.
- FORCEDW: PR971, f96962f2219e096821c3dec50712cc0108abea8f, research/hm/forced-secondary-w-extension/PROOF.md. The actual preimage of the canonical W O(-1) summand of Q in K is D O(-4).
- BALANCED: PR976, f23f8b9972d459c7c3ab532937964ef7f543b157, research/hm/balanced-first-cup-kernel/PROOF.md. It proves the actual K=T6 O(-1) plus A O(-2).

Retain the actual square subbundle L=A O(-6), quotient q:K->Q=P O(2) plus W O(-1), and actual reduced secondary boundary

    b:Q -> (V+P+D) O(4).

Its J row has coefficients (a_J,b_J) in the unique P-source and W-source channels i_J,j_J, for J=V,P,D. The A target row of the original beta is zero. All actual quartic transition contributions are retained in these coefficients. This note assumes the previously untreated branch

    a_D=a_P=0,       a_V nonzero.                       (1)

No actual coefficient condition or value is selected by the argument.

## 2. Results

Every fiber rank is constant on T, including the twelve-point orbit:

    b_P != 0:                   rank beta=5;
    b_P=0, b_D != 0:            rank beta=4;
    b_P=b_D=0:                  rank beta=3.            (2)

Consequently the cokernel is locally free and all generic-rank degeneracy schemes are empty. In particular this entire branch has no cokernel torsion.

There is a unique nonzero ratio eta, determined by two actual nonzero channel maps from the canonical A O(-2) summand of K. Put Delta=b_V-eta a_V. Its numerical expression depends on the nonzero channel generators, but the condition Delta=0 is intrinsic: it says the actual V row vanishes on that canonical summand. No numerical value of eta or Delta is computed. The ORIGINAL kernel sheaves are

    b_P != 0:
        A O(-6) plus O(-4);

    b_P=0, b_D != 0, Delta=0:
        A O(-6) plus W O(-3);
    b_P=0, b_D != 0, Delta!=0:
        O(-4) plus S O(-5);

    b_P=b_D=0, Delta=0:
        A O(-6) plus A O(-2);
    b_P=b_D=0, Delta!=0:
        (1+D) O(-4).                                  (3)

These are equivariant isomorphism types, not arbitrarily chosen complements. Thus the branch has a genuine kernel-splitting discriminant even though neither fiber rank nor cokernel torsion jumps.

## 3. The actual V-row kernel and constant rank

The established channels satisfy

    0 -> O(-4) -> P O(2) --i_V--> V O(4) -> 0,

j_P:W O(-1)->P O(4) is everywhere injective, and j_D=v epsilon has rank1 everywhere, with epsilon:W O(-1)->O onto and ker epsilon=O(-2).

Let E be the kernel in Q of the actual V row a_V i_V+b_V j_V. Since a_V is nonzero this row is everywhere onto, and its actual pullback diagram gives

    0 -> O(-4) -> E -> W O(-1) -> 0.                   (4)

The last arrow is onto on every fiber. The remaining P and D rows on E factor through this arrow and are exactly b_P j_P and b_D j_D. Thus the full rank is3 plus the rank of their combined W-source map. This proves (2) on every fiber. More precisely, inclusion of the remaining target rows gives an actual cokernel identification

    coker b = coker[W O(-1) -> (P+D) O(4)].             (5)

It does not require a choice of a splitting or a lift of the V row. Adding the identically zero A target gives the corresponding canonical A O(4) summand of coker beta. Since every rank in (2) is constant, local maximal minors contain a unit at every point, and the cokernels are vector bundles. Thus the assertion about empty degeneracy schemes is scheme-theoretic.

If b_V=0, (4) splits as O(-4) plus W O(-1). If b_V is nonzero, an equivariant splitting of (4) would lift the nonzero map b_V j_V through P O(2), impossible because

    Hom_G(W O(-1),P O(2))=Hom_G(W,P tensor Sym3 W)=0.

Its equivariant Ext space has dimension1: Ext1_G(W O(-1),O(-4))=H1(W O(-3))^G has that dimension by Serre duality. The dual of binary quadratic evaluation, twisted appropriately, supplies the nonzero model

    0 -> O(-4) -> A O(-2) -> W O(-1) -> 0.             (6)

It is nonsplit, as is immediate from its ordinary splitting types. Therefore E=A O(-2) when b_V is nonzero. These are identifications of the actual pullback extension, not replacements by a graded model.

## 4. The canonical actual discriminant

Write K_T=T6 O(-1) and K_A=A O(-2). The BALANCED decomposition is canonical in the equivariant category: Hom_G(K_A,K_T)=Hom_G(A,T6 tensor W)=0 since T6 tensor W=V+P+D, and Hom_G(K_T,K_A)=0 by negative degree. Thus its actual K_A subbundle is intrinsic.

Let q_P and q_W denote the two components of the actual quotient q. The map q_W is onto and vanishes on K_T, so its restriction K_A->W O(-1) is onto. Also q_P|K_A is nonzero. If it were zero, K_A would map into the actual preimage of W O(-1), namely D O(-4), but Hom(K_A,D O(-4))=0 by negative degree.

Consider the two actual maps

    h0=i_V q_P|K_A,       h1=j_V q_W|K_A.

The second is nonzero, since q_W|K_A is onto and j_V is nonzero. The first is nonzero as well: otherwise q_P|K_A would factor through ker i_V=O(-4), yet Hom(K_A,O(-4))=0. Their common equivariant Hom space is one-dimensional:

    Hom_G(A O(-2),V O(4))
       =Hom_G(A tensor V,Sym6 W),
    A tensor V=P+D,       Sym6 W=V+P.

There is therefore a unique eta in C*, with h0+eta h1=0. The actual V row restricted to K_A vanishes exactly when Delta=b_V-eta a_V is zero. The ratio eta is attached to the fixed actual quotient q and the chosen channel generators; it is not asserted to be a universal numerical constant. Rescaling those generators changes its coordinate but preserves this geometric condition. The construction uses the actual quotient maps and their proven nonvanishing; it does not evaluate any selected coefficient or direction.

A second canonical source will detect the same discriminant. Put

    B0=ker[K_A --q_W--> W O(-1) --epsilon--> O].

The composition is onto and is the unique nonzero quadratic evaluation channel, so B0=W O(-3). Moreover Hom_G(W O(-3),K) has dimension1: T6 tensor A=W'+S+2T6 contains no W, whereas A tensor W=W+S contains it once. Thus the inclusion B0->K spans every equivariant map from W O(-3) into K. The restriction h1|B0 is nonzero because q_W(B0)=ker epsilon=O(-2) and j_V is injective. Hence h0+eta h1 vanishes on B0 at exactly the same ratio, with no additional scalar condition. The D row always kills B0.

## 5. Extension facts used for the original kernels

For a reduced kernel Z=ker b, the actual quotient sequence gives

    0 -> L -> ker beta -> Z -> 0,       L=A O(-6).      (7)

The identification of Z below may involve graph lifts in Q; no literal zero P-component is silently assigned.

The needed equivariant Ext dimensions, by Serre duality on T, are

    Ext1_G(O(-4),L)=0,
    dim Ext1_G(O(-2),L)=1,
    dim Ext1_G(W O(-3),L)=1,
    dim Ext1_G(A O(-2),L)=1.                           (8)

For example these are the invariant multiplicities of A, A tensor A, A tensor W tensor W, and A tensor A tensor A, respectively. The named representations are self-dual and the central twists are retained. Equivariant Ext is the invariant part of ordinary Ext in characteristic zero.

The following nonzero extension models fix their middle bundles:

(a) The standard cubic evaluation sequence twisted by O(-5) is

    0 -> A O(-6) -> S O(-5) -> O(-2) -> 0.

(b) Pull (a) back along Euler evaluation W O(-3)->O(-2). It cannot split equivariantly, since a split lift would give a nonzero W O(-3)->S O(-5), forbidden by degree. Its other exact sequence is 0->O(-4)->middle->S O(-5)->0, which splits because H1(S O(1))=0. Thus the nonzero extension of W O(-3) by L has middle O(-4) plus S O(-5).

(c) Start with the dual quadratic evaluation sequence 0->O(-2)->A O->W O(1)->0. Since the kernel is a line, symmetric squaring gives 0->A O(-2)->Sym2(A) O->A O(2)->0. Here Sym2(A)=1+D. Twisting by O(-4) gives a nonzero extension of A O(-2) by L with middle (1+D) O(-4). It is nonsplit because the ordinary middle splitting is different from L plus A O(-2).

These models and the one-dimensional spaces in (8) classify every nonzero equivariant extension in question, up to isomorphism of middle bundles and rescaling of an endpoint.

## 6. Proof of the kernel table

If b_P is nonzero, injectivity of j_P forces the W component of every reduced kernel vector to be zero. The V row then gives Z=ker i_V=O(-4). The first vanishing in (8) proves ker beta=L plus O(-4), independently of b_V and b_D.

Assume b_P=0 and b_D is nonzero. The D row forces the W component into the Euler line O(-2). Thus Z is its pullback in E under (4). If b_V is nonzero, (6) identifies Z=W O(-3): the composite A O(-2)->W O(-1)->O is nonzero quadratic evaluation, whose kernel is W O(-3). The extension (7) splits if and only if some equivariant W O(-3)->K lands in ker beta and projects isomorphically onto Z. There is only the map B0->K from Section4. It lies in the kernel exactly when Delta=0. In that case its projection to Z is nonzero (Hom(W O(-3),L)=0 by degree), hence an isomorphism by Schur's lemma. At any other nonzero b_V the extension is nonzero, so model (b) gives O(-4) plus S O(-5).

If b_V=0 in this same case, Z=O(-4) plus O(-2). Its O(-4) extension component vanishes; its O(-2) component is nonzero, because a splitting would give an equivariant O(-2)->K, while

    H0(K(2))^G=(T6 tensor W+A)^G=0.

Thus model (a) again gives O(-4) plus S O(-5). Since eta and a_V are nonzero, b_V=0 indeed belongs to Delta!=0.

Finally assume b_P=b_D=0. Then Z=E. For b_V nonzero it is A O(-2), and the extension (7) splits exactly when the unique equivariant map A O(-2)->K, namely inclusion of K_A, lies in the V-row kernel. Section4 identifies this condition as Delta=0. Its projection to Z is nonzero by negative-degree Hom to L, so it is an isomorphism. For Delta!=0, model (c) gives (1+D) O(-4).

For b_V=0, Z=O(-4) plus W O(-1). The extension on O(-4) is zero, while the other component is the actual preimage D O(-4) from FORCEDW. Therefore the middle is O(-4) plus D O(-4), agreeing with the Delta!=0 entry. This completes (3).

## 7. Contribution and limits

The new branch (1) has no exceptional rank-drop or torsion locus at all, despite its secondary coefficients remaining unselected. A canonical actual source summand determines one nonzero normalized discriminant ratio. The extension arguments then classify every original kernel sheaf, including its possible splitting-type jump at that ratio. None of this assigns an actual scalar value or asserts occurrence of the branch.

Unlike a rank calculation alone, (7) and Section6 retain actual graph lifts and extension classes. Because ranks are constant here, original kernel fibers agree with the corresponding locally free kernels; the torsion caveat needed in the previous jumping branches does not apply.

No top sigma, vertex delta, opposite C row, source/catalogue pair or global odd-quadric conclusion is selected. No actual HM/source coefficient, point, parameter, derivative, jet, matrix or instance rank is evaluated. Only fixed character arithmetic and universal exact bundle arguments are used.
