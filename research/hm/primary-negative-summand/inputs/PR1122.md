# The actual primary terminal pencil cannot enter the source2 first block

Work over C with the fixed actual normalized HM cohomology module and physical G=SL2(F5) marking of PR1120 and PR1121. Write V for the positive coordinate three-space, W for the negative coordinate two-space, A=Sym2 W, P for the positive four-dimensional irreducible, W' for the other negative doublet, and T6=Sym5 W. Write M4=H1(B(4))_+ and M5=H1(B(5))_-. These are precisely the terminal source and target in PR1072 (through its PR1056 input), not a new truncation or a character-equivalent replacement. All polynomial actions and inclusions below are actual ones. The argument is structural and evaluates no selected coefficient, matrix, tensor, point, parameter, derivative, jet or instance rank.

## 1. Exact inputs and result

The inputs are complete originals in Akilleez-QA/read-em-and-weep:

- PR477, ff87076794e97238150485b12183c3cd0f4711e4, research/hm/adjoint-primary-extension/PROOF.md: actual injective graded polynomial-module map L_j=U tensor H1(F(j-3)) into K_j=H1(B(j-1)). Multiplication is Id_U tensor primary multiplication, not merely a degreewise character comparison.
- PR486, 0de9b4b71cbbf3c4492871d9835952a0dcb41e12, research/hm/level-section-resolution/PROOF.md: Soc(K)=K_6.
- PR1120, 62587a0adde566cac718ee13c28ee13c239389e5, research/hm/scalar-cyclic-module/PROOF.md, and PR1121, 1b1c33a6a348a31e00d7b322a43ecd6d4a8cea7a, research/hm/scalar-channel-projector/PROOF.md: U=P, H1(F(2))=1+A+T6, H1(F(3))=W. In particular the actual positive primary piece in B-degree4 is P tensor (1+A), and its entire terminal primary piece in B-degree5 is P tensor W=W'+T6.
- PR1072, d03beb727c7e778026dcceb3555c899a0808e093, research/hm/terminal-pencil-quotient/PROOF.md: under its retained actual source2 nonzero pure-V Q-compatible radical hypotheses there is a genuine negative splitting through degrees4 and5. Its first-block terminal pencil is

    0 -> W O(-8) -> N0,4 O(-1) -> N0,5 O -> 0,

  where N0,4=V+2P+D and N0,5=W'+2T6. The residual terminal space NR5=T6, and the projectors commute with the actual fixed-parameter negative multiplication. No positive-coordinate or Q preservation of these projectors is assumed.

Conclusion: these actual source2 pure-V compatible-radical hypotheses are impossible for the fixed HM module. The proof needs no R=0 assumption, no residual-large selection, and no fourth/fifth evaluation. It is NOT presently claimed to exclude any source2 formulation outside the full hypotheses supplying PR1072's genuine actual splitting and terminal pencil.

## 2. Levelness forces the full primary terminal evaluation pencil

Let Y=H1(F(2))_+=1+A, and Z=H1(F(3))=W. Both are actual cohomology spaces. Positive coordinates act by zero on Y: multiplication by V preserves physical parity but Z is entirely negative. Let

    c:Y -> Hom(W,Z),   c(y)(w)=w y

be the actual negative-multiplication curry. If c(y)=0, all W coordinates kill y and all V coordinates already kill y. For any nonzero u in U=P, the image of u tensor y in K5 is then an actual socle element by the R-linear injection. Since Soc(K) has no degree5, injectivity gives y=0. Thus c is injective.

Both its source and target have dimension4. Therefore c is an ACTUAL equivariant isomorphism. It is not defined by assigning values to unknown arrow scales; it is the multiplication itself and its invertibility follows from levelness. Under this isomorphism, multiplication is evaluation Hom(W,Z) tensor W -> Z.

Use PR1072's original parameter line T=P(W*). Via its fixed determinant identification, regard this as the line of negative linear forms in W; equivalently pull BOTH the ambient pencil and the primary pencil through the SAME fixed isomorphism to P(W). Denote the tautological line there by O(-1) subset W O. No independent change or rotation of either pencil is made. Evaluation gives an exact sequence

    0 -> Z tensor (W/O(-1))* tensor O(-1)
      -> Hom(W,Z) O(-1) -> Z O -> 0.

Since det W is trivial, W/O(-1)=O(1), so the kernel is Z O(-2). After tensoring with U and identifying by c, the actual primary terminal pencil is

    0 -> (U tensor Z) O(-2)
      -> (U tensor Y) O(-1) -> (U tensor Z) O -> 0.       (1)

The last arrow is onto at every projective parameter because it is evaluation of all Hom(W,Z) maps on a nonzero line. This is a universal proof, not a chosen-direction test. Its source has dimension16, target dimension8, kernel rank8 and degree-16. Both coefficient inclusions into the ambient B-degree4 and5 spaces are injective and intertwine the same actual negative variables by PR477.

## 3. A terminal-pencil Hom vanishing

Lemma. Suppose a two-arrow pencil has an exact bundle sequence

    0 -> A0 O(-2) -> A1 O(-1) -> A2 O -> 0,

and another has exact sequence

    0 -> C0 O(-m) -> C1 O(-1) -> C2 O -> 0,

where m>2 and all Ai,Ci are constant finite-dimensional spaces. Every coefficient-space morphism of these pencils is zero.

Proof. Such a morphism induces a morphism between their kernel bundles. It is zero because Hom(O(-2),O(-m))=H0(O(2-m))=0. The source coefficient arrow f1:A1 O(-1)->C1 O(-1) consequently annihilates the whole first kernel. Exactness makes it factor through A2 O. But Hom(A2 O,C1 O(-1))=0, so f1=0. Commutation and surjectivity of the first pencil's last arrow then force f2=0. This argument keeps both arrows and does not infer preservation of an intermediate positive-coordinate space.

This vanishing also holds for equivariant morphisms, since it holds without imposing equivariance.

## 4. Apply the genuine first-block projector, yielding contradiction

Under the source2 hypotheses of PR1072, compose the actual inclusions in (1) with the genuine negative projectors e0 in B-degrees4 and5. Projector commutation supplies a coefficient-space morphism from (1) to

    0 -> W O(-8) -> N0,4 O(-1) -> N0,5 O -> 0.          (2)

The lemma applies with m=8, proving e0(U tensor Y)=0 and e0(U tensor Z)=0. In particular the actual injection U tensor Z -> M5 lands in NR5.

But dim(U tensor Z)=4*2=8, whereas PR1072 proves dim NR5=6 (indeed NR5=T6). An eight-dimensional vector space cannot inject into a six-dimensional one. Equivalently the actual primary terminal W' constituent would have to embed in the pure T6 residual block, which is impossible by semisimplicity. This contradiction proves the stated conditional exclusion.

No identification of B0 with VR, or E_prim with VC or Vh, was made. Rather, the whole primary terminal pencil is incompatible with the genuine negative separated first block plus six-dimensional residual terminal. The two local repeated-V incidences need not be decided because the common source2 hypothesis furnishing that negative split is already contradictory.

## 5. Boundary and contribution

The new step is the full actual primary terminal pencil (1), obtained from parity, levelness and actual R-linearity, and its Hom obstruction against the genuine long first-block pencil (2). The proof does not repackage the projector algebra or use character equality to identify embeddings. Only its final dimension contradiction uses the character/dimension of the genuinely embedded residual target.

The conclusion is conditional on the complete source2 actual transfer and nonzero pure-V compatible-radical hypotheses already required by PR1072. It does not prove nonexistence of every abstract source2 negative pencil, which exists as a universal model, nor identify what the actual source pair is instead. It makes no full-adjoint invertibility, higher obstruction, original-pair, or algebraicity conclusion.

INPUTS.json authenticates the five complete originals by immutable commit, Git blob, SHA256 and byte length. The bounded checker verifies those hashes, fixed representation identities, the universal evaluation sequence, and the terminal-pencil Hom controls. The actual-module and sheaf-map arguments require the written proof and independent whole-proof reviews; this is not a proof-assistant certificate.
