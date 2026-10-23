# Removing the marked terminal string leaves the genuine first-block pencil

Work over C with G=SL2(F5), negative coordinate space W, parameter line T=P(W*), and the determinant convention fixed below. Write D=Sym4 W and T6=Sym5 W. Retain all actual source2 and nonzero pure-V Q-compatible radical hypotheses of NONZERO. All decompositions described as genuine are those of the fixed original source presentation, not newly chosen decompositions of its characters.

## 1. Immutable inputs and statement

INPUTS.json authenticates three complete originals in Akilleez-QA/read-em-and-weep:

- FILTRATION, PR795 at 3f811311d76914a555c7e7d0c5b887b41805aa6c, research/hm/source2-radical-filtration/PROOF.md. Its actual evaluation diagram gives E=E0 direct-sum E_R, E0=W O(-9), and 0 E_C=(P+D)O(-2)->E_R->E8=T6 O(-3)->0. The reconstructed module genuinely separates as N0 direct-sum N_R in degrees2–4, with degree-four pieces

      N0,4=V+2P+D,       N_R,4=V+2P+2D.

  Its actual endpoint inclusion is NC4=H1(E_C) inside H1(E_R).
- SOCLE, PR1056 at 875e86e2eec36a050e9a626735199681762e43ec, research/hm/restriction-socle-kernel/PROOF.md. The actual source pencil is 0 E->M3 O(-1)->M4 O->0; H0(E(1))=0, M4=H1(E), M5=H1(E(1)), and these identifications intertwine actual negative multiplication with parameter multiplication after the stated determinant rotation. Here M4=2V+4P+3D and M5=W'+3T6.
- NONZERO, PR1068 at 05e8b33eb87e9f36aa30500145cc42bc0ea00df8, research/hm/pure-v-terminal-nonvanishing/PROOF.md. It authenticates the SAME actual E and E_C embeddings, proves NC4 is the joint-negative kernel, and proves the marked D_can=U4 inside N_R,4 is disjoint from NC4. The coherent next multiplication is nonzero, with marked image U5≅T6 in M5 and exact subpencil

      0 -> D_can O(-1) -> U5 O -> O(5) -> 0.       (1)

We prove that the actual next pencil is onto everywhere with kernel E(1). More importantly, U5 is the entire genuinely separated residual degree-five space N_R,5, not just an unspecified T6 among the three copies. Quotienting that pencil by its marked subpencil (1) leaves exactly the genuine N0 terminal pencil and a zero source summand. Its kernel and cokernel are

      ker = (N_R,4/D_can) O(-1) direct-sum W O(-8),
      coker = 0,        N_R,4/D_can ≅ V+2P+D.      (2)

The zero source summand in (2) is an actual subspace, not an arbitrary representation complement. The result retains both generated-endpoint branches and does not impose any positive-coordinate or Q compatibility on this quotient.

## 2. The full next parameter pencil, with both rotations accounted for

The diagonal sequence on T times T, tensored by the pullback of F=E(1), gives, because H0(F)=H0(F(-1))=0, the natural exact sequence

      0 -> E(1) -> H1(E) O(-1) -> H1(E(1)) O -> 0. (3)

This follows by pushing 0 p1*F(-1) tensor p2*O(-1)->p1*F->Delta_*F->0 along p2. There is no higher direct image of the diagonal term. Thus (3) is exact as bundles, not only at the generic parameter.

It is important that (3) is the actual next pencil on the original parameter line. Write the original pencil as u m_x+v m_y in formal coordinates. SOCLE identifies multiplication by u on H1(E) with m_y, and multiplication by v with -m_x on M4. The diagonal equation is u1 v2-v1 u2, so its cohomology arrow in (3) is

      v H1(mult_u) - u H1(mult_v)
        = v m_y + u m_x.                           (4)

The two determinant rotations therefore cancel. This is the actual u m_x+v m_y map M4 O(-1)->M5 O, with no change of actual parameter or instance evaluation. In particular its kernel is the original E(1), not merely an abstract bundle of the same type or an untracked pullback. Sequence (3) is natural for every actual subbundle and quotient in FILTRATION.

## 3. The selected sextet exhausts the residual degree five

The genuine kernel decomposition and the cohomology identifications extend the separated system naturally to degree5:

      M5=N0,5 direct-sum N_R,5,
      N0,5=H1(E0(1)),       N_R,5=H1(E_R(1)).       (5)

Multiplication respects this decomposition because the bundle inclusions and projections commute with multiplication before taking cohomology. This proves actual compatibility rather than selecting summands by their characters.

Twist the actual residual sequence by1. Its left term E_C(1)=(P+D)O(-1) is acyclic, so the actual quotient induces an isomorphism

      N_R,5 -> H1(E8(1))=H1(T6 O(-2))=T6.         (6)

The marked D_can lies in N_R,4. Hence all its negative descendants lie in N_R,5 by naturality. NONZERO says their image U5 has dimension6 and is nonzero irreducible T6. Equation (6) says N_R,5 has dimension6. The actual containment consequently gives

      U5=N_R,5,       M5/U5 = N0,5.                (7)

In particular the two remaining T6 copies and the W' in M5/U5 are supplied by the genuine first block:

      N0,5=H1(W O(-8))=W tensor Sym6 W=W'+2T6.      (8)

No arbitrary choice among the three T6 copies has occurred.

## 4. Exact quotient pencil and its intrinsic zero-source part

Take the quotient of the actual arrow M4 O(-1)->M5 O by D_can O(-1)->U5 O. Equations (5)–(7) identify this quotient arrow with

      [N0,4 direct-sum Z] O(-1) -> N0,5 O,
      (a,z) |-> m(a),        Z=N_R,4/D_can.         (9)

Indeed the entire residual target has been removed, so all of Z maps to zero. The first-block arrow m is still the actual multiplication. Applying (3) to E0 alone proves

      0 -> W O(-8) -> N0,4 O(-1) -> N0,5 O -> 0.  (10)

Thus (9) is onto at every parameter and (2) follows, naturally relative to the genuine fixed first-block separation. In particular Z has character V+2P+D and dimension16, the same character as N0,4, but these are distinct embedded pieces and are not identified with one another. The quotient has source dimension32, target dimension14, kernel rank18 and degree-32.

There is also an intrinsic characterization that does not use a complement to Z: it is exactly the joint-negative kernel of the quotient degree-four space M4/D_can mapping to W tensor (M5/U5). Indeed twist the exact kernel sequence of (9) by1 and take H0. Its kernel is H0(Z O plus W O(-7))=Z. The resulting coefficient map is simultaneous negative multiplication, up to the fixed invertible determinant rotation. Thus its kernel is exactly Z. Thus the sixteen-dimensional zero-source part is canonical in the marked quotient module itself.

The old nine-dimensional socle NC4 injects into Z, since D_can is disjoint from NC4. Taking the degree-four cohomology of the actual residual sequence, and using the marked isomorphism D_can->D8 from NONZERO, gives

      0 -> NC4 -> Z -> V+P -> 0.                  (11)

The quotient map in (11) is the actual projection N_R,4->N8,4 followed by quotient by the marked D8. Thus removing the terminal string enlarges the degree-four joint-negative kernel by exactly this seven-dimensional residual quotient. Any equivariant vector-space splitting of (11) is unnecessary and is not asserted canonical.

## 5. The retained kernel correction is not discarded

The quotient construction must retain the O(5) cokernel of the selected subpencil. Applying the snake lemma to (1), (3), and (9) gives

      0 -> E(1) -> ker(9) -> O(5) -> 0.           (12)

This is not an isomorphism ker(9)=E(1). Under the genuine separation, its W O(-8) component is the identity, and the residual sequence is

      0 -> E_R(1) -> Z O(-1) -> O(5) -> 0.        (13)

Here E_C(1)=NC4 O(-1) is precisely the part of E_R(1) mapping into NC4 O(-1) inside Z O(-1). To verify this compatibility, use naturality of the diagonal resolution for E_C: it is the identity identification E_C(1)=H1(E_C)O(-1), since H1(E_C(1))=0. Quotienting (13) by that subbundle gives

      0 -> T6 O(-2) -> (V+P) O(-1) -> O(5) -> 0.  (14)

This is the complete binary evaluation sequence, up to an equivariant isomorphism of its coefficient space: twist by1, use H0(T6 O(-1))=H1(T6 O(-1))=0, and conclude that V+P maps isomorphically to H0(O(6))=Sym6 W. In particular (14) is nonsplit. The quotient retains a definite elementary evaluation correction; it does not erase subcomplex cohomology or force the full residual bundle sequence to split horizontally.

## 6. Contribution and limitations

The new determination is map-level: the marked terminal sextet is exactly the residual degree-five block, and the quotient's remaining multiplication is the genuine first-block pencil, with its exact W O(-8) kernel and canonical sixteen-dimensional zero-source part. Equations (12)–(14) account for the selected subpencil's nonzero cokernel. The exact seven-dimensional socle increase (11) is a consequence for the actual marked quotient, not a statement about an artificial three-degree truncation.

All claims remain conditional on the actual source2 pure-V compatible-radical hypotheses; no source or endpoint branch is realized or excluded. No selected actual HM/source coefficient, point, parameter, derivative, jet, matrix or rank is evaluated. The fixed-character checker is only an arithmetic and input-authentication check; the naturality assertions require this proof and independent mathematical review.
