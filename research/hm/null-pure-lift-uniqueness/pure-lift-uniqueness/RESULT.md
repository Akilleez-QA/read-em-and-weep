# Compact corrected pure lifts: rigidity, compatible boundary, and remaining mixed obstruction

## Conclusion

Let X=P²_z×P²_h, E=m*HM, A=End(E), K_z=pr_z*ω_P², and K_h=pr_h*ω_P². Under the stipulated physical geometric identification and imported Ext¹ character vanishing,

    H¹(X,A⊗K_z)=H¹(X,A⊗K_h)=0,
    H⁰(X,A⊗K_z)=H⁰(X,A⊗K_h)=0.

For a fixed genuine corrected pure-direction algebroid and fixed identification of its reduction with E, the global lift established in ../../null-corrected-pure-lift/corrected-relative-lift/RESULT.md is therefore unique up to unique reduction-preserving isomorphism. The h-direction has the same conclusion by exchanging the factors. This strengthens that report's existence statement using an additional imported global cohomological input. It does not select canonical Čech representatives.

The two pure corrected algebroids can be presented as pullbacks of algebroids on the respective plane factors. Their external tensor product gives one specified genuine two-direction ambient extension. Its boundary admits a unique module lift with fixed reduction E, assembled from the unique pure lifts. Neither this compatible boundary nor its uniqueness proves that its mixed obstruction vanishes. Identifying this corrected ambient extension with a prescribed physical two-jet remains a separate, unproved comparison.

## 1. Exact finite-pushdown identification

Let p:C²→P² be the degree-eight pair quotient from the supplied reports, and let π=p×p:C⁴→X. The physical map factors as f=m∘π. The line twist cancels canonically:

    End(F)=End(N⊗f*HM)=f*End(HM)=π*A.

This cancellation also holds for the stipulated genuine geometric action on endomorphisms. Let χ_z be negative under deck involutions 1 and 2, positive under deck involutions 3 and 4, negative under the inner swap (12), and positive under (34). Its deck weight is two.

On one pair, finite pushdown gives

    full pair deck sign, inner-swap odd: (p_*O_C²)_(11,−)=ω_P²,
    trivial pair deck character, inner-swap even: (p_*O_C²)_(00,+)=O_P².

The first equality follows from the ordinary product-linearized O(−2,−2) summand followed by the symmetric double quotient:

    σ_*O(−2,−2)=O(−2)_(+) ⊕ O(−3)_(−).

The second follows from σ_*O=O_(+)⊕O(−1)_(−). Fixed constant determinant-line conventions in identifying O(−3) with ω_P² do not affect vanishing. There is no extra cohomological permutation sign in this sheaf-level pushdown calculation.

Projection formula, vanishing of higher direct images for the finite map, and exact character projectors in characteristic zero give, in EVERY degree i,

    Hⁱ(X,A⊗K_z) ≅ Hⁱ(C⁴,End(F))_(χ_z).

In particular, this is an actual direct summand of the physical Ext¹ group in deck character (1,1,0,0), rather than a fiberwise approximation or a dimension estimate. Local freeness identifies physical Extⁱ(F,F) with Hⁱ(End(F)). The full deck-character (1,1,0,0) Ext¹ space vanishes by the imported weight-two result; its inner-swap eigensummand vanishes as well. Thus H¹(X,A⊗K_z)=0. Exchange z and h for the other vanishing.

Numerical terminology: the static source closure-and-characters.md calls (79,2,0,0,0) the dimensions PER CHARACTER of weights 0 through 4, not aggregate weight totals. Its total Ext¹ dimension is 79+4·2=87. Only the zero in weight two is needed here, so the terminology does not change the conclusion. No ranks have been recomputed.

## 2. H⁰ and uniqueness as a groupoid statement

The Ext¹ table alone does not give H⁰. Instead use the supplied nonempty dense stable-plane open U⊂P²_h. For h∈U, stability gives

    H⁰(P²_z,End(E_h)⊗ω_P²)=0.

Every global section of the locally free sheaf A⊗K_z consequently vanishes on X_U=P²_z×U. Since X is integral and X_U is dense, it vanishes everywhere. Therefore H⁰(X,A⊗K_z)=0. The same proof gives H⁰(X_U,A⊗K_z)=0 and the h-direction global assertion by exchange.

For a fixed first-order square-zero algebroid with ideal K_z, the isomorphism classes of locally free lifts with a specified reduction E form, when nonempty, a torsor under

    Ext¹_X(E,E⊗K_z)=H¹(X,A⊗K_z).

The reduction-preserving automorphisms of a lift form the additive group

    Ext⁰_X(E,E⊗K_z)=H⁰(X,A⊗K_z).

The first vanishing makes the isomorphism class unique; the second makes the isomorphism between any two lifts unique. The corrected-relative-lift report supplies nonemptiness on compact X for the corrected class

    η_z=(P_z,D_Pz(H_z/2),−2H_z²).

Its factor-exchanged argument supplies nonemptiness for η_h. Thus both fixed pure deformation groupoids are contractible. This means a canonical isomorphism class and unique comparison arrows once the ambient presentations and reductions are fixed. It does not mean a preferred matrix presentation, cocycle primitive, or literal equality of all chosen lifts.

## 3. One genuine mixed ambient extension and its compatible boundary

All three displayed coordinates of η_z are pulled back from P²_z: the canonical-valued biderivation P_z, the derivation-valued Čech class D_Pz(H_z/2), and the scalar Čech class −2H_z². Likewise η_h comes from P²_h. Choose genuine factor algebroid presentations B_z and B_h using the square-zero construction in ../../null-corrected-pure-lift/corrected-relative-lift/RESULT.md on each plane. Pull them to X.

Their external tensor product over C, interpreted sheafwise on product opens and with the product descent data, is a genuine associative algebroid B_zh. Locally its underlying module has the four coefficient pieces

    O_X ⊕ K_z ⊕ K_h ⊕ J,     J=K_z⊗K_h=ω_X.

The factor multiplications define its multiplication, and the external products of the factor gluing maps and coherence units supply its descent. Cross terms, including cross terms of coherence units, are thereby specified; they must not be discarded. Associativity and coherence follow from the factor constructions. The ideal J is square-zero and is annihilated by K_z and K_h. The quotient by J has the fiber-product boundary algebra/algebroid

    B_∂ = (pullback B_z) ×_(O_X) (pullback B_h).

A pair of pure locally free lifts L_z,L_h equipped with their fixed reduction identifications with E determines a module over B_∂ by gluing the pair along E. Locally this is the ordinary fiber product of the two free modules over the common reduction; it is locally free of the same rank. This construction also works with the algebroid descent data because the reductions and coherence are compatible.

Conversely, a boundary lift restricts to the two pure lifts. Thus fixed-reduction boundary lifts are the fiber product of the pure lifting groupoids over their fixed reduction. Their contractibility proves existence and uniqueness up to unique reduction-preserving isomorphism of the boundary lift L_∂. Equivalently, the boundary ideal is K_z⊕K_h with zero cross products, and both its H¹ ambiguity and H⁰ automorphism groups vanish.

This supplies GLOBAL pure boundary compatibility, including exceptional plane parameters, for this specified corrected compact problem. A factor-exchange-compatible presentation also receives the unique boundary comparison induced by exchange; the required coherence follows from uniqueness. This is not an identification with an arbitrary independently prescribed ambient mixed extension, and not a transport theorem for the physical two-jet.

## 4. Why open U retains a torsor of possible pure lifts

On the stable-plane open, the supplied relative calculation gives

    H¹(X_U,A⊗K_z)=H⁰(U,V),
    H⁰(X_U,A⊗K_z)=0,

where V has rank twelve. The restriction of the unique compact lift supplies a distinguished isomorphism class, hence an origin for the open lifting torsor once the compact corrected presentation is fixed. Other open lifts differ by sections of V. They need not extend to X; indeed a lift that extends to this fixed compact problem must have the restricted compact isomorphism class. There is no contradiction between global H¹=0 and potentially nonzero H⁰(U,V): open restriction can create new cohomology classes. Nonzero rank alone does not prove H⁰(U,V)≠0 on the entire U, though sufficiently small nonempty affine opens do have sections.

Accordingly, the earlier statement that an arbitrarily chosen open lift gives a noncanonical torsor origin remains correct without compact rigidity input. With the compact model and imported character vanishing now fixed, its unique global extension class gives a preferred open origin in this precise categorical sense.

## 5. Global scalar freedom and the still-unknown mixed value

For the specified B_zh and its now unique boundary L_∂, the remaining small-extension obstruction is a well-defined class

    c_zh(B_zh,L_∂) ∈ H²(X,A⊗J),    J=ω_X.

The pure uniqueness eliminates a boundary-choice ambiguity; it does not evaluate this class. In particular, a bundle E=m*HM need not be an external tensor-product module merely because the ambient algebroid was constructed by external tensor product. Mixed cross terms remain a genuine lifting problem.

Künneth and the cohomology of ω_P² give

    Hⁱ(X,ω_X)=0 for i=0,1,2,3;    H⁴(X,ω_X)=C.

Thus there is no nonzero global mixed scalar gerbe class in H²(X,J) available to tune the compact obstruction. There is also no scalar H¹ ambiguity. Trace splitting A=O_X·Id ⊕ End₀(E) identifies the entire mixed obstruction target with

    H²(X,End₀(E)⊗ω_X).

The supplied pair-quotient report computes the total target dimension as 62, splitting under block exchange into 32 and 30; its further 2+30 statement concerns the block-even sector with additional projector data. No symmetry of a particular mixed defect, and no vanishing of its value, follows merely from those dimensions.

On X_U, the scalar degree-two group becomes

    H²(X_U,J)=H⁰(U,ω_U),

which need not vanish. But a compact global mixed obstruction has zero trace and therefore restricts with zero scalar component. A nonzero scalar correction available only on U need not extend globally and cannot be invoked as global freedom. The restricted compact obstruction consequently lies in the tracefree recipient H¹(U,V⊗ω_U). Its vanishing still requires an actual argument, and restriction need not detect a global class supported through exceptional-parameter contributions.

For completeness, the same finite-pushdown argument identifies H¹(X,A⊗J) with the full-deck-sign/both-inner-odd part of physical Ext¹. Imported weight-four vanishing makes it zero. H⁰(X,A⊗J)=0 follows from the same dense stable-fiber argument. Hence IF a global mixed lift exists for this fixed mixed ambient and boundary, it too is unique up to unique reduction-preserving isomorphism. This conditional uniqueness is not an existence proof.

The unproved steps remain: evaluating c_zh for the specified corrected mixed ambient; proving a prescribed physical ambient and pure boundary transport to this corrected model; and, when working only on U, controlling restriction kernels and extension across exceptional parameters. No physical mixed value has been computed.

## Inputs and scope

Static inputs: ../../null-corrected-pure-lift/corrected-relative-lift/RESULT.md; ../../null-factor-surfaces/relative-surface-0502/DECK_ADDENDUM.md; ../../null-pair-quotient-bracket/pair-quotient-0512/RESULT.md; and https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md, §4 for imported per-character Ext¹ dimensions. 

Only static reading, finite equivariant pushdown, coherent cohomology, stability, square-zero deformation groupoids, external tensor products, and Künneth were used. No physical source or jet values are evaluated in this argument.
