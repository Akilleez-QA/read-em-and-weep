# Pure-V source2 compatibility forces the canonical terminal sextet

Work over C with G=SL2(F5), negative coordinate space W, and parameter line T=P(W*) with the determinant identification W≅W*. Write A=Sym2 W, S=Sym3 W, D=Sym4 W and T6=Sym5 W. Retain all actual source2 and nonzero pure-V Q-compatible radical hypotheses of RESIDUAL below. These are conditional hypotheses, not a source realization or an exclusion.

## 1. Exact inputs and result

INPUTS.json pins four complete immutable originals in Akilleez-QA/read-em-and-weep:

- FILTRATION, PR795 at 3f811311d76914a555c7e7d0c5b887b41805aa6c, research/hm/source2-radical-filtration/PROOF.md. Its genuine fixed-variable reconstruction gives E=E0⊕E_R, E0=W O(-9), and the actual kernel sequence

      0 -> E_C=(P+D) O(-2) -> E_R -> E8=T6 O(-3) -> 0.       (1)

  Its exact system 0 NC->N_R->N8->0 has

      NC3=Sym17 W=W'+S+2T6,   NC4=P+D.                      (2)

  The actual inclusion NC4->N4 is H1(E_C)->H1(E), as proved by its evaluation diagram and connecting-map naturality. Its full fixed-pencil radical J has (JN)4=NC4. The actual-source transfer and common-pencil hypotheses of that proof remain in force.
- TERMINAL, PR1052 at 64e4fdd771a14a764c6e119d2eb25b0237d83622, research/hm/negative-string-terminal-gate/PROOF.md. It proves the exact actual Koszul continuation

      0 -> M3 --delta--> W tensor M4 --mu--> M5 -> 0,
      M3=3W'+3S+6T6,  M4=2V+4P+3D,  M5=W'+3T6,            (3)

  with M_i=H1(B(i)) of alternating negative/positive/negative parity. It constructs the coherent canonical string through the marked U4=D_can⊂M4 and its actual next map f5:T6->M5. That map is either zero or injective, and H1(B(6))=0 kills every degree-five descendant under every coordinate.
- SOCLE, PR1056 at 875e86e2eec36a050e9a626735199681762e43ec, research/hm/restriction-socle-kernel/PROOF.md. It identifies the SAME actual source-pencil kernel E in 0 E->M3 O(-1)->M4 O->0 with H1(E)=M4 and H1(E(1))=M5, including actual multiplication and the determinant convention. Its joint-negative kernel is the actual subspace H1(E_{-2})⊂M4, where

      E_{-2}=image[H0(E(2)) tensor O(-2)->E].               (4)

  Also f5=0 exactly when the marked D_can lies in that subspace. Its catalogue-dependent numerical table is not used here.
- RESIDUAL, PR1064 at bfc239e1c8624a0346394e1454b0bea3c976d40d, research/hm/source2-pure-v-canonical-residual-string/PROOF.md. It proves at the level of the actual fixed-variable maps that U=(A_can,S_can,D_can) lies in N_R, projects injectively to N8, and

      pi4(D_can)=D8,      D_can intersect NC4=0.             (5)

  This holds in both remaining generated-endpoint branches. It does not itself identify NC4 with the degree-four joint-negative kernel or make a degree-five claim.

We prove that under these conditional actual hypotheses,

    NC4 = ker[M4 -> W tensor M5]                            (6)

as embedded subspaces, and therefore f5 is necessarily NONZERO. Its image U5≅T6 is canonical, the actual string continues

    W -> A -> S -> D -> T6,

with coherent ordinary symmetric multiplication, and every coordinate kills U5 in degree6. In particular the zero branch of TERMINAL is impossible under these hypotheses, although neither source2 itself nor the9/16 generated-endpoint alternatives is excluded.

There is a further exact-map consequence: every member of the actual fixed-pencil radical J extends uniquely through degree5 as an endomorphism of the alternating negative-coordinate module, and its degree-five component is zero. This is not an extension of the homotopy h or a claim about positive-coordinate commutation.

## 2. The endpoint kernel is intrinsically the maximal slope -2 part

The E in FILTRATION is not identified with SOCLE's E just by its rank or splitting character. FILTRATION constructs its actual negative pencil from evaluation, with N4=H1(E), and states the actual-source transfer to the same fixed original maps. TERMINAL and SOCLE retain precisely that pencil, its M3,M4 and its kernel. One can verify this kernel identification directly, rather than relying on the name E. For an evaluation kernel F here, H0(F)=H0(F(-1))=0 by its negative-degree constituents. Tensor the diagonal sequence on T times T,

    0 -> O(-1,-1) -> O -> O_Delta -> 0,

by p1*F and push along p2. Its cohomology gives the natural exact resolution

    0 -> F -> H1(F(-1)) O(-1) -> H1(F) O -> 0.

For 0 F->H O->Q->0, twisting by-1 identifies H0(Q(-1)) with H1(F(-1)), since O(-1) has no cohomology. Connecting-map naturality identifies the arrow in this diagonal resolution with FILTRATION's reconstructed second pencil r↦delta(l r), under the same determinant convention. Applying this to the evaluation diagram containing E_C,E_R,E0 identifies its kernel inclusions with the inclusions in the original E pencil. Thus (1) is an actual subbundle sequence in this E.

Combine the genuine separation E=E0⊕E_R with (1). It gives the actual quotient sequence

    0 -> E_C -> E -> W O(-9) plus T6 O(-3) -> 0.             (7)

Twisting by2, the right term is W O(-7) plus T6 O(-1), which has no sections. The left term is the constant bundle (P+D)O, whose H1 vanishes. Consequently inclusion gives an isomorphism

    H0(E_C(2)) -> H0(E(2)).                                 (8)

Evaluation commutes with that inclusion, and the constant E_C(2) is generated by all its sections. Its evaluation image in E is therefore exactly (4):

    E_C=E_{-2}                                              (9)

as actual subbundles. This proves the identification without assuming a horizontal splitting of E_R or choosing a degree-2 coefficient subspace by its character.

The right term of (7) also has H0=0. Thus H1(E_C)->H1(E) is injective. FILTRATION's evaluation diagram identifies its image with the actual embedded NC4. SOCLE's natural multiplication theorem identifies the image of H1(E_{-2}) with the actual joint-negative kernel. Equation (9) now proves (6). In particular both negative coordinate maps kill all of NC4, not just the particular marked quartic or the image of one radical element.

## 3. Independent direct verification using only actual arrows

There is a second verification of the containment in (6) that makes clear why a truncated three-degree submodule alone was insufficient. FILTRATION says NC is a submodule for BOTH original negative arrows. The Koszul injection in (3) consequently restricts to

    delta:NC3 -> W tensor NC4.                              (10)

It is injective since the full delta is injective. The two spaces have dimension18 by (2). Therefore (10) is an isomorphism of the actual spaces, not a mere abstract character isomorphism. Exactness of (3) implies that mu annihilates W tensor NC4. This proves that both subsequent negative multiplications kill NC4 in M5, although no such extra arrow was part of the original truncated definition of NC.

For equality rather than containment, (7)–(9) and SOCLE give joint-kernel dimension dim(P+D)=9. The embedded NC4 already has dimension9. Thus this direct verification agrees with the canonical bundle-level identification (6). Neither argument substitutes matching P/D characters for actual containment or naturality.

## 4. Forced nonzero terminal arrow

Let U4=D_can be the particular image of the coherent degree-one-generated string, not an arbitrary D copy in M4. On W tensor U4, actual multiplication factors as

    W tensor Sym4 W -> Sym5 W --f5--> M5.                  (11)

The first map is universal symmetric multiplication. If f5 were zero, every negative coordinate would annihilate U4, so (6) would put U4 inside NC4. This contradicts the actual transversality (5). Therefore f5 is nonzero.

Since Sym5 W=T6 is irreducible, f5 is injective and its image U5 is a selected actual T6 subspace among the three T6 copies in M5. Rescaling the initial coherent identification W->U1 rescales the whole string and does not change U5 or its embedded multiplication system. Thus U5 is canonical in the same sense as U1,...,U4.

The entire H1(B(6)) is zero by TERMINAL, so every ambient linear form, not merely a negative one, annihilates U5. This determines the final nonzero degree of this marked negative-coordinate string under the retained hypotheses.

As a direct geometric consequence, its last universal parameter arrow is the actual subpencil

    0 -> D_can O(-1) -> U5 O -> O(5) -> 0.                  (12)

Indeed the map is the ordinary multiplication Sym4 W tensor O(-1)->Sym5 W tensor O; the binary evaluation sequence proves fiberwise injectivity and its quotient O(5). This statement concerns the selected subpencil. No assertion about splitting the full degree4-to5 pencil or discarding its other actual channels is made.

The conditional Euler-preimage construction in the zero branch of TERMINAL therefore cannot occur with this marked D_can. This does NOT remove the actual unmarked D O(-2) in E_C: that summand's cohomology is a different embedded D subspace, disjoint from D_can by (5). Confusing those two copies would reverse the conclusion.

## 5. Unique radical extension through degree five

Let j=(j2,j3,j4) belong to the actual fixed-pencil radical J from FILTRATION. Since (JN)4=NC4, its image j4(M4) lies in NC4. Equation (6) gives

    m_l j4=0 for every l in W,                             (13)

where m_l:M4->M5 is actual multiplication. Define j5=0. The only new intertwining equation needed to extend j from degrees2,3,4 to degrees2,3,4,5 is

    j5 m_l = m_l j4.

It holds by (13); all earlier equations are those of the given fixed-pencil endomorphism. Thus the extension exists and is equivariant. It is unique, because the complete multiplication W tensor M4->M5 is onto by (3): any intertwining j5 must vanish on that spanning image.

This construction is linear in j and preserves the already satisfied radical product identities. It supplies an extension of the actual radical action to one more degree of the alternating negative-coordinate module. It does not extend h:N4->N2, does not impose arbitrary cross-direction homotopy commutation, and does not assert compatibility with positive coordinates or with the invariant quadratic on additional degrees.

## 6. Contribution and limits

The missing bridge is the actual equality between the source2 endpoint radical image and the degree-four negative socle. Once established by its kernel embedding and independently by the actual Koszul arrows, RESIDUAL's marked transversality decides the previously unselected terminal alternative. This is stronger than noting that T6 occurs in degree5 or that h is invertible on D_can.

All conclusions retain the conditional actual source2 pure-V compatible-radical hypotheses; no actual source is realized or excluded, and neither generated-endpoint branch is chosen. No selected actual HM/source coefficient, point, parameter, derivative, jet, matrix, instance rank or large scan was used. The bounded checker authenticates exact inputs and fixed character/dimension identities; the actual-map conclusions require the written proof and independent mathematical review.
