# An actual rank-two opposite core and its Euler-branch companion

Work over C on T=P(W*) with standard G=SL2(F5) linearizations and current labels W,W',A=Sym2 W,S=Sym3 W,D=Sym4 W,T6=Sym5 W,V=Sym2 W',P. No selected actual HM/source coefficient, point, parameter, matrix, jet or instance rank is evaluated.

## 1. Immutable interfaces and statement

INPUTS.json authenticates two originals in Akilleez-QA/read-em-and-weep.

- NONSPLIT is PR1090 at 0bbb6529ababc4a92cceacd1e4db2a0bac10d759, research/hm/nonsplit-quartic-extension/PROOF.md. It supplies the actual presentation

      0 -> O(-8)+L3 --u--> Z9 -> C -> 0,         (1)
      0 -> F:=J tensor W' O(5) -> Z9 -> B7 -> 0,
      0 -> B4 -> B7 -> J_r tensor A O -> 0,      (2)

  where B4 has type S O(1), J and J_r are one-dimensional trivial multiplicity spaces, and all kernels and quotient maps in (2) are canonical. The source L3 has

      0 -> M0 tensor W O(-1) -> L3
           -> M1 tensor O(-2) -> 0,             (3)

  for trivial multiplicity lines M0,M1; its splitting exists but is not canonical. The composite Z9->J_r A O->J_r O(2) is the actual canonical quotient of C, and its kernel in C is the actual Q of rank4 and degree24.
- RESIDUAL is PR1002 at b691ab014afa0c546894dba5bcec396ed6694d5d, research/hm/canonical-residual-pencil/PROOF.md. Sections1–4 establish that this same canonical Q is globally generated, with its actual complete-evaluation presentation

      0 -> E24 O(-1) -> H28 O -> Q -> 0,
      E24=W+W'+2S+2T6,
      H28=1+2A+V+2P+2D.                         (4)

  Its invariant complete-coefficient gate lambda is a map between two one-dimensional spaces. Dual evaluation identifies the invariant cokernel with Hom_G(Q,O)*. Thus lambda is nonzero exactly when Hom_G(Q,O)=0, and zero exactly when that space is one-dimensional. This is an actual-map statement, not an abstract character criterion.

We construct a canonical rank-six bundle Y6, an extension

      0 -> F -> Y6 -> B4 -> 0,                  (5)

and an inherited map mu between multiplicity lines. If mu is nonzero, there is an actual fiberwise-injective rank-two core

      0 -> O(-8)+M1 tensor O(-2) -> Y6 -> Q -> 0. (6)

If mu is zero, there is an actual companion

      0 -> O(-8)+M0 tensor W O(-1) -> Y6
           -> Q -> J_r tensor O -> 0.          (7)

In (7) the final quotient is unique up to scalar. Its kernel Q3 therefore has the rank-three-source presentation obtained by replacing Q with Q3 and removing the terminal O. The target Y6 has isomorphism type W' O(5)+S O(1), but no splitting is chosen. The alternatives mu=0 and lambda=0 agree through the same actual Q; we do not identify their numerical values or choose either branch.

## 2. Take the actual kernel of the degree-two quotient

Let Y8 be the kernel of the composite Z9->J_r O(2) in the NONSPLIT interface. The composite kills the source in (1), since it factors through C. Taking kernels of the two surjections to J_r O(2) gives

      0 -> O(-8)+L3 -> Y8 -> Q -> 0.           (8)

In particular this is the canonical Q defined by the actual quotient of C, not merely a bundle with the same character.

The usual complete quadratic evaluation has sequence

      0 -> W O(-1) -> A O -> O(2) -> 0.

Apply it to the canonical quotient Z9->J_r A O from (2). The induced map

      r:Y8 -> J_r tensor W O(-1)                (9)

is onto. Its kernel Y6 is precisely the preimage of B4 in Z9, so (5) follows. The definition uses kernels of existing maps, not any section of a target extension.

Since B4 has type S O(1), Ext1_G(B4,F)=0 by H1(O(4))=0. Thus Y6 has the indicated isomorphism type, with multiplicity lines retained. Its splitting is not canonical: Hom_G(B4,F) has dimension one, because W' tensor Sym4 W=S+T6. We use only the actual extension (5).

## 3. The inherited scalar and the forced nonzero full projection

Compose the source of (8) with (9). The O(-8) summand has zero projection, since

      Hom_G(O(-8),W O(-1))
        =Hom_G(W,Sym7 W)=0,
      Sym7 W=W'+T6.                            (10)

Write h:L3->J_r W O(-1) for the remaining actual map. It is nonzero. Otherwise (9) would descend through (8) to a surjection Q->J_r W O(-1). A quotient of a globally generated bundle is globally generated, but W O(-1) has no sections and positive rank. This contradicts RESIDUAL's global generation of the actual Q.

Restrict h to the canonical subbundle M0 W O(-1) in (3). By Schur's lemma it is

      mu tensor id_W,   mu:M0 -> J_r.           (11)

This map between actual multiplicity lines is intrinsic; no complement in (3) is chosen to define it. Its value remains unevaluated.

If mu is nonzero, the restriction in (11) is an isomorphism of bundles. Therefore h is onto and its kernel L1 maps isomorphically under (3) to M1 O(-2). This is a canonical identification induced by the actual kernel diagram: it does not use a preselected splitting of L3. Since the separate O(-8) source has zero projection by (10), the full kernel of the source projection is the actual direct sum O(-8)+L1.

Taking kernels in (8) and (9), with h onto, proves (6). Its source map is inherited from u, and its quotient is the same actual Q. No target splitting or matrix cancellation is used.

If mu is zero, h factors through the quotient M1 O(-2) in (3). The factor is nonzero, because h is nonzero, and

      Hom_G(O(-2),W O(-1))=C.

Its nonzero generator is Euler inclusion. After the nonzero multiplicity identification determined by h, its sequence is

      0 -> M1 tensor O(-2) -> J_r tensor W O(-1)
           -> J_r tensor O -> 0.               (12)

Thus ker h=M0 W O(-1) and coker h=J_r O. The kernel-cokernel exact sequence for (8) and the surjection (9) gives exactly (7). In particular it constructs an actual surjection Q->J_r O; it does not append a freely chosen trivial factor.

Let Q3 be the kernel of this quotient. It is locally free, and (7) gives

      0 -> O(-8)+M0 tensor W O(-1) -> Y6 -> Q3 -> 0. (13)

Both (6) and (13) inject on every fiber because their quotients are locally free. The weighted map F into their quotients is the restriction of the inherited F->C, through Q or Q3: the canonical degree-two quotient kills F by degree, and the trivial quotient kills F as well. All actual embeddings are retained.

## 4. Compare with the old gate through actual Q, not labels

The target Y6 is an extension of positive-degree bundles, so Hom(Y6,O)=0 even without equivariance. In the nonzero-mu branch, (6) therefore gives Hom_G(Q,O)=0 by precomposition with its surjection Y6->Q.

In the zero-mu branch, apply Hom(-,O) to the right part of (7). Since Hom(Y6,O)=0, every map Q->O factors uniquely through its displayed quotient J_r O. Hence

      Hom_G(Q,O)=J_r*,   dimension one.         (14)

Its kernel Q3 is consequently intrinsic and independent of the scalar used to identify J_r with C. Also Q3 is a quotient of the positive bundle Y6 and is ample on P1. Global generation of Q implies that Q->J_r O splits equivariantly: global sections map onto its constant target because they generate Q fiberwise, and averaging supplies an invariant section. No splitting of Q is needed to construct (13).

Now apply RESIDUAL's dual complete-evaluation identification to the very same Q identified in Section2. It gives

      mu=0  if and only if  lambda=0,
      mu≠0  if and only if  lambda≠0.           (15)

The bridge is the actual quotient of C, its actual kernel Q, and the functorial Hom(Q,O) obstruction. No comparison of abstract C/Q characters is used to deduce (15). We do not assert a canonical identification of the two gate source and target lines or an equality of their scalar coordinates.

The older reductions through the unique W source and the earlier rank-three core used different intermediate actual embeddings and targets. The present result does not identify those source subbundles by their representation labels. Its new content is the actual rank-two presentation (6) and the companion (13) with the common intrinsic target (5), obtained from the new nonsplit graph quotient. Equation (15) retains an old distinction rather than claiming a new branch exclusion.

## 5. Choices, invariants and scope

Y6 has rank6 and degree14. The source in (6) has rank2 and degree-10, giving Q rank4 and degree24. The source in (13) has rank3 and degree-10, giving Q3 rank3 and degree24. Before branching, Y8 has rank8 and degree12, and the source in (8) has rank4 and degree-12, again giving Q rank4 and degree24.

The nonzero-mu source line L1 is defined by h, not by an arbitrary complement to M0 in L3. In the zero branch the source M0 W O(-1) is the canonical subbundle from (3). All target extensions and actual maps remain intact. No value of mu or lambda, actual C row, source pair, top obstruction, vertex extension or initial marked-line position is selected. Work stops at this common-target core.

verify.py authenticates the immediate originals and checks only bounded fixed-character Hom tests, universal Euler balances and the final ranks/degrees. REPRODUCE.md reconstructs omitted audit originals. REVIEW.md binds independent whole-proof review to the final author bytes; neither proof-assistant certification nor any actual-instance evaluation is claimed.
