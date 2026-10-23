# Canonical reduction of the actual opposite-parity pencil

## Theorem

Work over C with the actual normalized Horrocks–Mumford bundle F, B=End₀(F), and G=SL₂(F₅). Write V for the positive coordinate three-space, W for the negative two-space, A=Sym²W, S=Sym³W, and T₆=Sym⁵W. Let R₊ be the positive fixed plane and L=P(W*) the negative fixed line.

Set

    U=H¹(B(2))₋, dim U=44,
    P₃=H¹(B(3))₊, dim P₃=46,
    U₀=ker[U→H¹(B|L(2))₋],
    R=ker[P₃→H¹(B|L(3))₊].

Both restriction maps are onto. Their targets are S and A, respectively, so dim U₀=40 and dim R=43. The second kernel R is also the actual positive-generated middle of PR931.

Let T be the hyperplane-pencil parameter line, identified with L by the actual vertex map. The actual opposite-parity multiplication pencil

    Γ:U⊗O_T(−1)→P₃⊗O_T

restricts to a canonical subpencil Γ₀:U₀⊗O_T(−1)→R⊗O_T. There is an exact sequence of actual sheaves on ALL of T,

    0 → W⊗O_T(−7) → U₀⊗O_T(−1)
      --Γ₀--> R⊗O_T → C → 0,                    (1)

where C is canonically the SAME cokernel sheaf as coker Γ. Thus its rank five, degree 26, and any torsion supported at the twelve exceptional parameters are all retained.

There is a further canonical reduction. Put J=im Γ₀ and C₁₂=H⁰(J)⊂R. Then

    C₁₂≅V+P+D, dim C₁₂=12,

where P is the even four-space and D=Sym⁴W. The inverse image of C₁₂⊗O_T in U₀⊗O_T(−1) is H₁₄⊗O_T(−1) for an actual constant subspace H₁₄⊂U₀, with

    H₁₄≅W⊗Sym⁶W≅W′+2T₆, dim H₁₄=14.

The induced quotient pencil is a canonical SHEAF-INJECTIVE map

    0 → (U₀/H₁₄)⊗O_T(−1)
      --Γ₁--> (R/C₁₂)⊗O_T → C → 0.              (2)

Its source and target have dimensions 26 and 31, and

    R/C₁₂≅1+3A+V+2P+2D.

This is an exact diagrammatic reduction of the actual marked negative map, not merely a character comparison and not an assertion of a chosen direct-sum decomposition of the full pencil.

A geometric consequence is the exact normal-order section formula

    H⁰(P⁴,I_(R₊)^n I_L B(n+3))
       ≅ W⊗H⁰(T,O_T(n−7))       for every n≥0.   (3)

The first nonzero space is the actual W in order seven. No selected actual HM/source coefficients, points, matrices, derivatives or instance ranks are evaluated.

## 1. Immutable inputs

All source paths are in Akilleez-QA/read-em-and-weep. Exact originals and Git blob hashes are recorded in audit-inputs/manifest.json.

- PR931, commit e28d3b74d4288239426ad1e675e806310fadf8be, research/hm/positive-reachable-middle/PROOF.md, blob 060ad3bacb45086349e911265d6c0d6157bef4a0. It identifies R with the restriction kernel, of character 1+3A+2V+3P+3D, and authenticates the actual split F|L=O_L(3)₋⊕O_L(−4)₊ and the needed structural cohomology vanishings.

- EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md, commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/, blob c9af11e07dd1c4535d9afee94a3c134607d534a3. For X=Bl_(R₊)(P⁴), p:X→P⁴ and π:X→T it proves the ACTUAL square-section identification

      π_*p*B(3)=Sym²Y=A⊗O_T(−6),
      Y=π_*p*F(2)=W⊗O_T(−3),                   (4)

  including all parameters. It proves H⁰B(2)=H⁰B(3)=0 and the exact sequence 0→A O(−6)→U O(−1)→P₃ O→C→0. C has rank five and degree 26 including torsion; its torsion is supported at the twelve exceptional parameters, with no claim that it is nonzero or absent.

- NONZERO-VERTEX-EVALUATION.md, commit c779b2919a36b9d45a6319d46551bd6380154bba, in the same directory, blob 335702d20ff8a297050f81c7a2931302241f3ce4. It proves the ACTUAL everywhere-surjective vertex evaluation

      ev:Y=W O_T(−3)→O_T(−2),
      ker ev=O_T(−4).                            (5)

  This is an imported geometric theorem, not a newly evaluated scalar.

- PR167's primary section resolution and regularity theorem at commit 063da90fc4543304e87e701cdefcc08225412f17, research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md, blob 58785a8799c43fd2c7da089d0ddc5e05822132a9.

- The fixed abstract character convention in verify_negative_vertex_scalar.py at commit db51525015bb7c5e825833d550d08dedf6f6ea96, in research/hm/order-four-quadratic-load/, blob 9eb58f03edde15dd612087440d8180e9e16d1755. Only its abstract binary-icosahedral representation conventions are used.

All named representations are self-dual. In particular W′ is the other binary two-space, not the positive three-space V. No c-d-f occurrence is assumed.

## 2. The restriction quotient in the source is actually onto

The line split gives

    B|L(2)=O_L(9)₋⊕O_L(2)₊⊕O_L(−5)₋,
    B|L(3)=O_L(10)₊⊕O_L(3)₋⊕O_L(−4)₊.          (6)

Consequently H¹(B|L(2))₋=H¹(O_L(−5))≅Sym³W=S, and H¹(B|L(3))₊≅A. Equivariant Serre duality uses det W=1.

The ideal Koszul resolution of I_LB(2) has terms

    Λ³V⊗B(−1) → Λ²V⊗B(0) → V⊗B(1).

The resolution diagonal controlling H²(I_LB(2)) consists of H²B(1), H³B(0), H⁴B(−1). The first two vanish by the structural inputs. For the last, the tensor section resolution has rightmost term E₀(−1)=15F(−4)⊕4F(−3); Serre duality gives H⁴E₀(−1)=15H⁰F(0)*⊕4H⁰F(−1)*=0. All other H⁴ resolution-diagonal terms exceed the dimension of P⁴. Hence H⁴B(−1)=0, and H²(I_LB(2))=0.

The restriction long exact sequence therefore makes U→S onto. This proves the exact source row

    0 → U₀ → U → S → 0.                          (7)

PR931 gives the exact target row 0→R→P₃→A→0. Naturality of restriction with multiplication gives a commutative diagram after twisting the source rows by O_T(−1):

    0 → U₀ O(−1) → U O(−1) → S O(−1) → 0
          Γ₀          Γ           β
    0 → R O      → P₃ O      → A O      → 0.       (8)

The map β is the actual multiplication pencil on line cohomology. It is not replaced by an arbitrary equivariant map. We do not identify U₀ with a positive-generated image at the preceding degree; that would be a separate assertion.

## 3. The quotient-pencil kernel and the full naturality diagram

For a parameter t, write H_t for its hyperplane and ν(t)=H_t∩L for the vertex. The map ν:T→L is the canonical annihilator identification for the two-dimensional negative coordinate space. Retaining ν until making this identification avoids changing the negative variables.

Inside P⁴×T, the universal incidence equation gives

    0 → B(2)⊠O_T(−1) → B(3)⊠O_T
      → j_*p*B(3) → 0.                           (9)

Its restriction to L×T remains exact: the restricted equation cuts out the vertex graph, a Cartier divisor of bidegree (1,1), rather than vanishing identically on L×T. Thus the corresponding row is

    0 → B|L(2)⊠O_T(−1) → B|L(3)⊠O_T
      → (graph ν)_*ν*B|L(3) → 0.                 (10)

Restriction defines a morphism from (9) to (10). Their pushforward long exact sequences commute, including their connecting maps. The ambient H⁰ vanishings identify π_*p*B(3) with ker Γ.

On the line, take the physical positive part of the pushed-forward sequence (10). The relevant exact part is

    H⁰(O_L(9))⊗O_T(−1)
      → H⁰(O_L(10))⊗O_T
      → O_T(10)⊕O_T(−4)
      --∂--> S⊗O_T(−1) --β--> A⊗O_T → 0.         (11)

The first source has total positive parity because both H⁰(O_L(9)) and O_T(−1) are negative. The map from H⁰(O_L(10)) is ordinary evaluation along the vertex graph. It is onto the O_T(10) summand and has zero component in O_T(−4). Hence ∂ kills exactly O_T(10) and induces an isomorphism

    O_T(−4) ≅ ker β.                              (12)

This explicitly retains the nonzero H⁰ line contribution. Merely identifying the degree of ker β would not establish (12) or the next step.

By naturality of the connecting maps, the induced map ker Γ→ker β is actual restriction to the vertex followed by ∂. Under (4), ker Γ consists of the actual products Sym²Y. Every section in Y is positive, so its vertex value lies in

    F|L(2)₊=O_T(−2),

not in the negative summand O_T(5). Products therefore evaluate in Sym²(O_T(−2))=O_T(−4), with zero O_T(10) component. Restriction of a product is the product of its restrictions, and Sym²(F(2))=B(3) with the fixed equivariant normalization. Combining this with (12) proves that the induced kernel map is exactly

    Sym²(ev):A O_T(−6)→O_T(−4).                  (13)

Use the same incidence equation and matched connecting-map conventions in both rows. Changing a single boundary convention introduces only a harmless global sign and does not change its kernel or surjectivity.

The identification (13) is an identity of sheaf morphisms on the entire parameter line. It does not discard the twelve exceptional fibers or assume every individual fiber section extends.

## 4. The actual reduced kernel and unchanged cokernel

For any surjection from a rank-two bundle Y to a line bundle Q with line kernel M, multiplication gives an exact sequence

    0 → M⊗Y → Sym²Y → Q² → 0.                    (14)

Locally choose a generator of M and lift a generator of Q; the kernel of the square quotient is generated by their two products with the M generator. This proves injectivity and exactness without choosing a global splitting.

Apply (14) to (5): M=O_T(−4), Y=W O_T(−3), Q=O_T(−2). Thus (13) is onto and its kernel is W O_T(−7). The snake lemma in (8) now gives both

    ker Γ₀=W O_T(−7),   coker Γ₀≅coker Γ=C.

This proves (1) as an exact sequence with the actual maps.

In particular, the presentation computes rank(C)=43−40+2=5 and degree(C)=40−14=26, agreeing with the old presentation. These numerical checks are consequences, not substitutes for the canonical cokernel isomorphism.

For each t the exact base-change sequence is

    0 → (W O_T(−7))⊗k(t) → ker Γ₀(t)
      → Tor₁(C,k(t)) → 0.                        (15)

Thus exceptional torsion is retained. The left term consists of extending square sections with zero vertex value. Extra individual exceptional sections can have a nonzero O_T(10) vertex component, killed by the connecting map in (11). Therefore (15) is not an identification of every reduced fiber-kernel vector with an individually vertex-vanishing hyperplane section.

## 5. A canonical constant subpencil and the 26-to-31 quotient

Let J=im Γ₀⊂R O_T. It is locally free, since a torsion-free coherent sheaf on the smooth curve T is locally free. Sequence (1) gives

    0 → W O_T(−7) → U₀ O_T(−1) → J → 0.

Both H⁰ and H¹ of U₀ O_T(−1) vanish, so the actual connecting map identifies

    H⁰(J)≅H¹(W O_T(−7))
          ≅W⊗Sym⁵W
          ≅V+P+D.                               (16)

Denote this actual space by C₁₂. Its inclusion H⁰(J)→H⁰(R O_T)=R is injective. Evaluation identifies C₁₂ O_T with an actual constant subbundle of J inside R O_T. The quotient J/(C₁₂ O_T) embeds in (R/C₁₂)O_T and is therefore torsion-free. Thus C₁₂ O_T is saturated in J.

Let E be its inverse image in U₀ O_T(−1). There are exact sequences

    0 → W O_T(−7) → E → C₁₂ O_T → 0,
    0 → E → U₀ O_T(−1) → J/(C₁₂ O_T) → 0.        (17)

The latter quotient is locally free, so E is a subbundle. Its rank is 14 and its degree is −14. Hence E(1) is a degree-zero subbundle of the trivial U₀ O_T.

A degree-zero subbundle of a trivial bundle on P¹ is constant: its determinant is O, so its Plücker coordinates are constant global functions and are not all zero. The resulting constant Plücker point specifies one fixed subspace. Applied to E(1), this gives the canonical actual subspace

    H₁₄=H⁰(E(1))⊂U₀,   E=H₁₄ O_T(−1).           (18)

No choice of a direct-sum splitting of Γ₀ is involved.

Twist the first sequence in (17) by one and take Euler characters. Since E(1) is constant, its H¹ vanishes. Equivariant Serre duality gives

    [H₁₄]=[W⊗C₁₂]−[W⊗Sym⁴W]
           =[W⊗Sym⁶W]=[W′+2T₆].                (19)

Here W⊗Sym⁵W=Sym⁶W⊕Sym⁴W, Sym⁶W=V+P, W⊗V=T₆ and W⊗P=W′+T₆ are fixed representation identities. In particular dim H₁₄=14.

Quotient the actual subpencil in (17) by H₁₄ O(−1) and C₁₂ O. By construction its quotient map has zero sheaf kernel and unchanged cokernel C. This proves (2), with dimensions 40−14=26 and 43−12=31. Subtracting (16) from the known character of R gives the displayed target character.

Sheaf injectivity is not fiberwise injectivity at points where C has torsion. Indeed the fiber kernel of Γ₁ is Tor₁(C,k(t)). The construction preserves the complete cokernel sheaf and does not silently saturate away its torsion.

## 6. The actual mixed-ideal section module

Let Z⊂X be the vertex section, so Z=p⁻¹(L) and π|Z is an isomorphism. Left exactness of π_* applied to

    0 → I_Z p*B(3) → p*B(3) → B(3)|Z → 0

identifies π_*(I_Z p*B(3)) with the kernel of actual vertex evaluation on (4). Its evaluation image is exactly the O_T(−4) summand, by (13). Therefore

    π_*(I_Z p*B(3))=W O_T(−7).                  (20)

The higher direct image is deliberately different from the pencil cokernel. If D_vert=(R¹π_*(I_Zp*B(3)))₊, the same long exact sequence and the identity (R¹π_*p*B(3))₊=C give

    0 → O_T(10) → D_vert → C → 0.                (21)

Thus the O_T(10) term cannot be dropped by identifying D_vert with C. The extension implies that tors(D_vert) injects into tors(C), but it does not determine equality or the existence and length of tors(D_vert) when C has torsion.

For n≥0, the blowup identity π*O_T(1)=p*O_P⁴(1)⊗O_X(−E_(R₊)) gives

    H⁰(X,I_Z p*B(3)⊗π*O_T(n))
       =H⁰(X,I_Z p*B(n+3)⊗O_X(−nE_(R₊))).

Since L and R₊ are disjoint, p is an isomorphism near L. Locally near L, and separately away from L, one obtains the canonical ideal identity

    p_*(I_Z O_X(−nE_(R₊)))=I_L I_(R₊)^n.

This uses the standard blowup identity p_*O_X(−nE_(R₊))=I_(R₊)^n for n≥0 and requires no higher-direct-image or exceptional-fiber base-change surjectivity. Projection formula for the locally free B now proves (3) from (20).

The same reasoning for F gives π_*(I_Zp*F(2))=O_T(−4), hence H⁰(I_(R₊)^4 I_L F(6)) is one actual invariant line. Multiplication of that line by the known W=H⁰(I_(R₊)^3 F(5)) identifies it with H⁰(I_(R₊)^7 I_L B(10))=W: this is the global-section map of O(−4)⊗Y→Sym²Y after twisting by seven. Thus the first adjoint survivors in (3) are actual products, not just an abstract W character.

## 7. Contribution and boundary

The earlier actual kernel A O(−6) contained a universally visible line quotient coming from the negative fixed line. The vertex-square comparison removes precisely that quotient and identifies the genuine residual W O(−7) kernel. The canonical constant subpencil then removes its forced constant image, leaving a 26-to-31 sheaf-injective quotient presentation of the same defect C.

These are additional exact constraints on the marked opposite-parity map. They do not choose the remaining quotient arrow, prove C locally free, calculate exceptional torsion lengths, solve all mixed-square equations or establish actual source membership. The construction is global and requires no c-d-f assumption. No source, source-dual pair, stable label or frontier count changes.
