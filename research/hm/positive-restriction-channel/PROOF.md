# The positive restriction defect is the canonical last vertex jet

## Result

Use the smooth weighted stack X=P(1,1,2,2), physical O(1)=O_wt(2), the actual rank-two Serre bundle G, regular zero scheme Z, and physical inversion-even parts (+). Write E=pi*F_Q(2), S=O_wt(1), so G=E S^(-1). Let J=(a,b) be the ideal of the stack vertex line, not the coarse vertex ideal. Let

 V_sec=H0(G|Z(4))_+,  K=im[H0(G(4))_+ -> V_sec].

The preceding positive-boundary theorem establishes dim V_sec=35, dim K=31 and V_sec/K=P4 via the actual boundary d. There is a canonical subspace

 T=H0(J^4(G|Z(4)))_+ = P4

and

 V_sec=K direct-sum T.                                           (A)

In particular d|T:T->H1(B(4))_+=P4 is an isomorphism. This is a canonical LAST-JET identification, not the choice of one of four abstract P4 copies. It identifies the defect with the deepest quintic odd Loewy layer. It does not evaluate the specified actual operator residue.

For any v in V_sec there is a unique k in K with the same image as v modulo J^4; its actual boundary is the image under d|T of v-k. A lift of k to a global G(4) section need not be unique, but its restriction to Z is unique. Thus this prescription has no splitting or global-section-lift ambiguity.

## Pinned inputs

The preceding theorem is [PR648's positive-boundary theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/83eb365e87fe3aef3488aa339b73636fa845f630/research/hm/positive-boundary-duality/PROOF.md). Its V_sec/K statement uses the following cone files at 8c26de8e5e68fd41945373ac1f6ee280f109d716, under research/hm/order-four-quadratic-load/:

- [WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md): H1(G(2))=0; actual global odd vertex Loewy layers W'O_L(2), A O_L(2), W'O_L(2); E|L=O_L(5) plus O_L(-2); after tensoring by E(1), the positive layers are W'O_L(1), A O_L(8), W'O_L(1). The conic contribution is entirely odd.
- [VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md), Sections 1--2: the cubic relation is the actual global subbundle K3=O_L(-2) in Sym^3 W' O_L(1), and the degree-three quotient is A O_L(2). The regular initial (3,5) pair is uniform at all points. The odd grades are cover degrees 1,3,5.
- [INVARIANT-CONE-SPINOR-FILTRATION-AND-NILPOTENT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/INVARIANT-CONE-SPINOR-FILTRATION-AND-NILPOTENT.md): the stack coordinate model and G=E S^(-1).

The primary support input H1(F(t))=0 outside 0,1,2,3 and H2(F(t))=0 outside -2 is Section 1 of [the actual primary-image extension proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d5d9bd997145b0ecf7d7bd659a19fb7845afb75f/research/hm/actual-primary-image-extension/PROOF.md). Normalization is F*=F(1).

These inputs describe actual sheaves and maps, not only characters. The distinction between stack stabilizer invariants and physical inversion is retained throughout.

## 1. Uniform lifting through the third transverse cover degree

The fourth power of the ideal of the regular coordinate pair a,b has its universal Hilbert--Burch resolution

 0 -> Sym^3(W') tensor S^(-5)
   -> Sym^4(W') tensor S^(-4) -> J^4 -> 0.         (1)

An inessential determinant representation is trivial for the stated binary group. Tensor (1) by G(4). Since S^2=O(1), the result is

 0 -> Sym^3(W') tensor E(1)
   -> Sym^4(W') tensor G(2) -> J^4 G(4) -> 0.      (2)

We have H1(G(2))=0 by the pinned positive Serre-bundle theorem. Also H2(E(1))=H2(F_Q(3))=0. For the latter use

 0 -> F(1) -> F(3) -> i_*F_Q(3) -> 0:

H2(F(3))=0 by primary support, and H3(F(1))=H1(F(-5))*=0 by Serre duality and the same support statement. Exact tame coarse pushforward justifies computing stack E(1) on Q. Thus (2) gives

 H1(J^4 G(4))=0.                                  (3)

In particular global sections of G(4) surject onto G(4)/J^4G(4), in both physical parities. This is a uniform sheaf-cohomology assertion, with no chosen vertex point or coefficient evaluation.

## 2. Passing from the full third-jet neighborhood to truncated Z

Set U=G|Z(4)/J^4(G|Z(4)). There is a natural surjection

 G(4)/J^4G(4) -> U.                               (4)

One must not infer surjectivity on sections of (4) from sheaf surjectivity alone. Its kernel is controlled explicitly by the cubic relation.

On the stack, G(4)=E S(3). Equivalently it is E(1) tensor S(2). After exact coarse pushforward, only odd transverse cover degrees occur in the S(2) factor. Modulo J^4 they are degrees one and three. The actual ideal of Z has no relation below degree three and its degree-three relation is K3=O_L(-2). Multiplying that relation by a positive transverse degree gives degree at least four, already zero in this truncation. Consequently the coarse kernel of (4) is exactly

 E|L(1) tensor K3 = E|L(-1)
                  = O_L(4)_+ plus O_L(-3)_-.       (5)

This identification is intrinsic: it uses the canonical cubic relation subbundle, not a choice of a quintic generator or a splitting of E over a thickening. Only E|L is needed because the kernel is annihilated by J after this truncation. The physical signs in (5) are those of O_L(4) and O_L(-3) with their inherited binary-group linearizations. Equivalently E(1)|L has positive O_L(6) and negative O_L(-1), while K3=O_L(-2) is physical even. Physical O_X(1)|L=O_L(1) is not treated as parity-trivial.

In particular the positive H1 of this kernel is zero, since H1(O_L(4))=0. Combining (3)--(5),

 H0(G(4))_+ -> H0(U)_+ is onto.                   (6)

The negative O_L(-3) cohomology is not silently discarded: it is irrelevant only because we take the physical positive part. The theorem does not assert the analogous negative surjectivity onto U.

## 3. Canonical deepest layer and exact dimensions

The three odd transverse degrees of the actual vertex module are 1,3,5. Thus J^4 retains precisely the last, degree-five odd layer after coarse pushforward. The pinned global Loewy theorem, tensoring by E(1), gives

 p_* pi_*(J^4(G|Z(4))|Z_vertex)_+ = W' O_L(1).                   (7)

Here p is the finite negative projection from the vertex-supported scheme to L. There is no conic contribution to the positive cohomology: away from the vertex J is the unit ideal, but G|Z(4) has only physical odd sections on the disjoint conic. For precision, (7) denotes the positive summand after the negative projection on the vertex component; the conic has zero positive H0 and H1. All the relevant positive vertex line degrees are 1 or 8, so H1 vanishes for the deepest layer and for U. Consequently

 T=H0(J^4(G|Z(4)))_+=W' tensor H0(O_L(1))=P4,

 0 -> T -> V_sec -> H0(U)_+ -> 0,

 H0(U)_+=P4 + A tensor Sym^8 W
         =A+2V+3P4+2D5, of dimension31.            (8)

Here V in the character formula is the established three-dimensional irreducible; V_sec denotes the section space.

By (6), the actual image K surjects onto H0(U)_+. The preceding theorem proves dim K=31, and (8) proves the target has dimension31. Hence this actual restriction map K->H0(U)_+ is an isomorphism. Therefore K intersects T trivially, and dim K+dim T=35 proves (A). The established kernel equality ker d=K now proves d|T is an isomorphism.

## 4. What the result does and does not determine

The new canonical projection V_sec->T is formed by subtracting the unique actual global-restriction image having the same lower jets. It is not the projection attached to an arbitrary decomposition into irreducibles. In particular it need not kill a chosen homogeneous middle P4 summand: a lower-jet class can acquire an actual highest-jet correction when globally lifted. The actual global image determines that correction.

The transpose d* therefore restricts perfectly to the dual of the last-jet subspace. This strengthens its earlier containment in conormal cohomology by proving that its last-jet projection is an isomorphism. It does not identify d* with a chosen inclusion of the dual last grade into the full filtered dual space.

For the actual specified operator class v(a,h), its absolute value remains d(v(a,h))=(d|T)(v(a,h)-k(a,h)), where k(a,h) is the unique actual restriction matching the lower jets. Computing this actual remainder, and then passing to the second-symbol quotient, remains open. No selected actual HM/source coefficients, matrices, point ranks, scans, large computation, or operator evaluation were used.
