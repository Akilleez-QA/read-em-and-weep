# A canonical doublet retraction and the residual complement algebra

Work over C, on the original negative parameter line, with the fixed physical action of G=SL2(F5). Write W for the negative coordinate doublet, W' for its other doublet, A=Sym²W, S=Sym³W, D=Sym⁴W, T=Sym⁵W, P for the even four-space and V for the other even three-space. Fix the same determinant trivialization throughout. Every assertion concerns vector bundles and the actual negative pencils only, unless expressly conditional on a listed type.

## 1. Immutable inputs

The full originals are retained and hashed in INPUTS.json:

- PR1124, commit 48396766d4e61a9de2455b1d068ba8abe09e05f3, research/hm/primary-negative-summand/PROOF.md. This constructs the actual canonical saturated image H=(W'+T)O(-3) in E and Q=E/H. It proves H0(Q(1))=0, H1(Q)=V+2P+2D, H1(Q(1))=2T, and existence of equivariant bundle sections of E→Q. Its affine space of sections has dimension two.
- PR1123, commit 504b7eb800407dfc7e6340c98c72cdd553939f54, research/hm/primary-terminal-slope-obstruction/PROOF.md. Relative to its authenticated actual-input catalogue, there are four necessary types for E, and hence the four quotient types below. No occurrence is asserted.
- PR1056, commit 875e86e2eec36a050e9a626735199681762e43ec, research/hm/restriction-socle-kernel/PROOF.md. Its source-independent Sections1–3 identify the actual pencil 0→E→M3 O(-1)→M4 O→0, its next negative maps, and M4=H1(E), M5=H1(E(1)), with a single fixed determinant rotation. The characters are M3=3W'+3S+6T, M4=2V+4P+3D, M5=W'+3T. We do not use its conditional source-pair table.

These are mathematical dependency assumptions, not proof-assistant verification. No full geometric coverage theorem is supplied here.

## 2. A canonical retraction, not merely an existing complement

Let L=W'O(-3) and J=T O(-3), the canonical distinct isotypic pieces of H=L⊕J. Applying Hom_G(-,L) to the actual sequence 0→H→E→Q→0 gives

    0 → Hom_G(Q,L) → Hom_G(E,L) → Hom_G(H,L) → Ext¹_G(Q,L).

Serre duality, self-duality of the representations and the fixed determinant convention give

    Hom_G(Q,L)=Hom_G(H1(Q(1)),W')=Hom_G(2T,W')=0.

Also Ext¹(Q,L)=W'⊗H1(Q* O(-3))=0, because its dual coefficient space is H0(Q(1))=0. Taking G-invariants is exact in characteristic zero, so Ext¹_G vanishes as well. Restriction is therefore an isomorphism. There is a UNIQUE equivariant p:E→L restricting to H's canonical projection onto L.

For the actual inclusion i:L→E, pi=id_L. Thus e=ip is a canonical idempotent, and

    E = L ⊕ K,             K=ker p,
    rank K=15,             degree K=-48.

Here canonical means relative to the actual primary inclusion and fixed marking; no complement was chosen to construct p. The complementary bundle fits canonically into

    0 → J → K → Q → 0.

Its sections still form an affine two-space: Hom_G(Q,J)=Hom_G(2T,T) has dimension two. This separates a genuine canonical partial splitting from the unresolved choice of a complementary copy of Q.

The complement K is even invariant under every equivariant bundle endomorphism f of E: uniqueness gives Hom_G(E,L)=C·p, so pf is a scalar multiple of p and annihilates K. This does not force the other summand L to be invariant.

This theorem does not require the four-type catalogue. It also does not say that e commutes with every bundle endomorphism of E, or with any positive-coordinate, invariant-quadratic, Gauss or full graded-module operation.

## 3. Canonical reduction of the actual negative tail

Twisting the original pencil by -1 identifies M3 naturally with H1(E(-1)), since H1(O(-2))=C and both cohomology groups of O(-1) vanish. Together with PR1056's identifications, the actual negative tail is cohomology multiplication

    H1(E(-1)) → H1(E) → H1(E(1)),

with the same fixed determinant convention at both arrows. This can also be obtained by the natural diagonal reconstruction for E and E(-1); no separate parameter change is made for a summand. Multiplication by every parameter-linear section commutes with e, because e is a bundle morphism. Consequently the actual negative tail splits canonically into the L and K tails.

For L, Serre duality gives

    H1(L(-1))=W'⊗Sym²W=T,
    H1(L)=W'⊗W=P,
    H1(L(1))=W'.

The canonical direct summand therefore has dimensions 6→4→2. Its complementary tail has characters

    3W'+3S+5T → 2V+3P+3D → 3T,

and dimensions 48→33→18. In particular the terminal pencil canonically splits as a 4→2 summand and a 33→18 complement. This is a statement about the actual negative maps, not simply character subtraction: naturality of cohomology multiplication supplies the commuting projections first.

Nothing here extends the projection to M2, to positive variables, to Q multiplication, or to the full primary module extension.

## 4. All two-sided Hom spaces for the four necessary quotient types

Conditionally on PR1123's necessary classification, subtracting the actual split H gives

    Q1 = D O(-2) + V O(-4) + O(-8),
    Q2 = P O(-2) + V O(-4) + W' O(-5),
    Q3 = V O(-2) + 2V O(-4),
    Q4 = T O(-3) + V O(-4).

Cancellation is legitimate by equivariant Birkhoff multiplicities and PR1124's actual equivariant splitting. The display chooses notation for abstract types, not an actual complement inside E.

For blocks R O(-j), S O(-k),

    Hom_G(R O(-j),S O(-k)) = Hom_G(R,S⊗Sym^(j-k)W)

when j≥k, and is zero otherwise. The exact nine-class character calculation verifies

    W⊗D=S+T,  W⊗P=W'+T,  W⊗V=T,
    W⊗W'=P,  A⊗W'=T,  V⊗V=1+V+D,  A⊗V=P+D.

It follows that dim Hom_G(H,Qi) is respectively 1,2,1,1; dim Hom_G(Qi,H)=2 in every case. Every reverse arrow Qi→H lands in J=T O(-3), never in L.

For i=1,2,3, every forward arrow H→Qi lands in its degree-minus-two block, while every reverse arrow kills that block. Hence

    v u = 0 for every u:H→Qi and v:Qi→H.          (1)

For Q4, u is a scalar map from H's T summand to Q4's T summand. The reverse arrow's same-slope component is another arbitrary scalar. Thus the image of the composition pairing (v,u)↦vu is exactly the one-dimensional line C·pr_T in End_G(H). This pairing is genuinely nonzero, and its left radical is the one-dimensional reverse-arrow space from V O(-4).

## 5. Reverse compositions and their exact nonvanishing

Put I_i=span{uv}⊂End_G(Qi). For i≤3 it is a two-sided ideal and I_i²=0 by (1). Its dimensions are precisely 1,1,0.

For Q3, the only possible reverse composition would map V O(-4) to V O(-2). This Hom space is zero: A does not occur in V⊗V=1+V+D. Thus BOTH composition directions vanish for every pair of arrows, including every linear combination on the two copies of V.

For Q1, the only possible nonzero reverse composition is V O(-4)→D O(-2), a one-dimensional Hom space. The potential long composition O(-8)→D O(-2) is zero because D does not occur in Sym⁶W=V+P.

Here is a non-dimension-count proof that the short composition is nonzero. In the universal binary-polynomial realization, let D_p=p∂x+q∂y with p,q independent formal variables. The backward arrow V⊂Sym⁶W→Sym⁵W⊗W is first polarization D_p, and the forward arrow Sym⁵W→Sym⁴W⊗W is another polarization. They are nonzero equivariant arrows, so span the unique relevant channels. Their composition is D_p² restricted to V. The full second-polarization map on Sym⁶W is injective in characteristic zero (or compare its monomial coefficients); hence its restriction to nonzero V cannot vanish. Therefore dim I_1=1.

For Q2, the backward arrows from V O(-4) and W' O(-5) both land in T O(-3). The forward W' channel is therefore irrelevant to reverse composition. The long composition W' O(-5)→P O(-2) is zero by Hom_G(W',P⊗Sym³W)=0. The short target Hom_G(V,P⊗A) is one-dimensional.

To prove its nonzero value, realize V⊕P=Sym⁶W and let π_P be the G-equivariant projection onto P. Up to nonzero scalars, the forward T arrow is t↦π_P((xq-yp)t), and the backward V arrow is v↦D_pv. These maps are nonzero: multiplication Sym⁵W⊗W→Sym⁶W is onto, and first polarization is injective. Their composite is π_P((xq-yp)D_pv). If this were identically zero for all v and all formal p,q, V would be stable under each coefficient of

    (xq-yp)D_p = -p² y∂x + pq(x∂x-y∂y) + q² x∂y.

Those coefficients are the three sl2 generators. This is impossible: Sym⁶W is an irreducible sl2 representation, while V is a nonzero proper three-dimensional subspace. One elementary proof uses the seven distinct weights 6,4,...,-6 and the nonzero adjacent raising/lowering coefficients. The verifier checks these full symbolic coefficients and the second-polarization controls. Thus dim I_2=1. No selected group orbit or actual source coefficient is evaluated.

## 6. The complement-independent algebra and its radical

Choose a section temporarily and write an arbitrary f∈End_G(E) as [[a,b],[c,d]] relative to H⊕Q. Replacing the section by s+i v gives, by conjugation,

    a' = a-vc,       c'=c,
    d' = d+cv,       b'=b+av-vd-vcv.               (2)

For types1–3, (1) makes a'=a and vcv=0. Thus H's diagonal block is independent of the chosen complement even though f need not preserve H. This distinction is essential. Also d modulo I_i is independent. There is a canonical surjective algebra homomorphism

    End_G(E) → End_G(H) × (End_G(Q)/I_i),
    f ↦ (a,[d]).                                  (3)

Multiplicativity follows because the correction to the H block is b1c2=0 and that to the Q block is c1b2∈I_i. Surjectivity may be checked using any section; the resulting map is independent of it. Its kernel N_i consists of blocks [[0,b],[c,j]] with j∈I_i. Products satisfy N_i²=I_i in the lower-right corner and N_i³=0. Equality follows from the definition of I_i. In type3, I_3=0 and N_3²=0.

A further complete Hom count gives End_G(Q1), End_G(Q2) each dimension4, with diagonal algebra C³ and sole off-diagonal ideal I_i. For Q3, End_G(Q3)=C×Mat₂(C) since the two V O(-4) copies may mix and the inter-slope Hom is zero. The quotients in (3) are therefore

    type1: C⁵,                 dim End_G(E)=9,  dim N_1=4;
    type2: C⁵,                 dim End_G(E)=10, dim N_2=5;
    type3: C³×Mat₂(C),          dim End_G(E)=10, dim N_3=3.

These quotient algebras are semisimple and N_i is nilpotent, so N_i is exactly the Jacobson radical, not just a nilpotent subspace. In types1 and2 its square is one-dimensional and its cube is zero; in type3 its square is zero.

For type4, E=W'O(-3)+2T O(-3)+V O(-4). Its endomorphism algebra has semisimple quotient C×Mat₂(C)×C and a two-dimensional square-zero radical consisting of the arrows from V O(-4) to the two T copies. Its total dimension is8. The H-diagonal assertion (3) does NOT extend to type4: its nonzero scalar feedback changes the selected T diagonal under (2).

These are intrinsic algebra statements about the four necessary bundle types. They neither select which type is actual nor supply a distinguished T/Q complement. The universal canonical doublet retraction in Section2 holds before this conditional classification and is the actual new negative-tail reduction.

## 7. Reproduction and limits

Run `python verify.py` and `python -O verify.py`; both outputs must agree with RESULT.json. The standard-library checker uses exact arithmetic in Q(sqrt5), all nine character classes, full formal polarization coefficients and a noncommutative block-gauge calculation. Hash checks authenticate the retained inputs. It does not independently prove the pinned geometric input theorems, nor replace their proofs with numerical tests.

No selected actual HM/source point, parameter, tensor, matrix, derivative, jet, rank experiment, burn run or scan is performed. No positive/Q/Gauss compatibility, source occurrence, geometric coverage, full-adjoint invertibility, algebraicity or complete original proof repair follows from this packet.
