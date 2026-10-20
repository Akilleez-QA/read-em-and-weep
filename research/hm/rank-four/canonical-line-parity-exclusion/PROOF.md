# Canonical reflection lines have residual rank at least four

## Claim and dependencies

Work over C with the setup of ../rank-three-line-rank-constancy/PROOF.md: the five-dimensional Schrödinger space V, its projective normalizer, and the canonical line L=P(W), where W is the two-dimensional negative eigenspace of a normalized reflection R. Write T=V_+ (dimension three), so V=W⊕T. Assume the N-equivariant outer-symmetric cyclic-zero trilinear map f:V³→J and repeated-input injectivity from ../rank-one-middle-curve-exclusion/PROOF.md: f(t,t,a)=0 with t≠0 implies a∈Ct. Set b_u(ab)=f(a,u,b), with rank b_u=4+rank Q_u.

**Theorem.** At every [u] on any of the twenty-five canonical lines, rank b_u≥8 and rank Q_u≥4. Thus none of these lines is contained in Z₃, or even meets Z₃.

Together with the conditional curve classification in ../rank-three-curve-constraints/PROOF.md, this proves that Z₃ is finite as a support, under that classification's stated dependencies. The new line exclusion itself does not require the decic closure, Z₂ finiteness, or the curve classification.

No source tensor or actual operation is evaluated. All calculations below are abstract representation and bundle arguments. The independent audit is recorded in AUDIT.md.

## 1. An honest binary-icosahedral representation

The canonical projective line stabilizer Γ is SL₂(F₅), is perfect, and acts effectively on L as A₅; these facts and the canonical W⊕T splitting were proved in the line-rank-constancy file. We need an honest linear lift with determinant one on W, rather than an unstated projective representation convention.

Let Γhat be the inverse image of Γ in SL(V). It is a finite central extension by μ₅. The character d(g)=det(g|W) satisfies d⁵=1: its fifth power is trivial on μ₅ and descends to the perfect group Γ. Define ρ(g)=d(g)²g. Its restriction to the scalar c∈μ₅ is c⁵=1, so it descends to Γ; moreover det(ρ(g)|W)=d(g)⁵=1. The central involution z of Γ acts as R: R itself lies in SL(V), det(R|W)=1, and thus is unchanged by the normalization. Consequently z is −I on W and +I on T.

For the target it suffices to replace J by the linear span of the values of f. Its action is the quotient action induced from the cubic tensor space on V: equivariance of the original projective map makes its kernel invariant, and the normalized action just constructed induces an honest Γ-action with f exactly equivariant. Equivalently twist the original target lifts by the cube of the scalar used on V. Denote its ± eigenspaces for z by J_±. No irreducibility assertion about J is needed.

## 2. The small representation identities needed below

W is irreducible, and T is irreducible. The prior line proof excludes invariant one-dimensional subspaces in V; this proves both claims by complete reducibility and their dimensions two and three. Since det W=1, Sym²W is an irreducible three-dimensional representation of A₅: it has no invariant vector (an invariant symmetric form on W, together with its invariant alternating form, would contradict Schur's lemma), and A₅ has no nontrivial two-dimensional complex representation.

Put T'=Sym²W. These two three-dimensional A₅ representations T,T' are inequivalent. The operator D e_j=ζ^(j²)e_j from the prior proof has determinant one both on V and on W, hence its normalization above is unchanged. Its traces are

    tr(D|T)=1+ζ+ζ⁴,
    tr(D|T')=1+ζ²+ζ³.

The elementary A₅ character identities are

    T⊗T = 1 ⊕ T ⊕ P₅,
    Sym²T = 1 ⊕ P₅,
    T'⊗T = P₄ ⊕ P₅,                         (2.1)

where P₄,P₅ are irreducible of dimensions four and five. These can be checked directly from the character table on classes of sizes 1,15,20,12,12 (orders 1,2,3,5,5):

    1 : (1, 1, 1, 1, 1)
    T : (3,-1, 0, φ, φbar)
    T': (3,-1, 0, φbar, φ)
    P₄: (4, 0, 1,-1,-1)
    P₅: (5, 1,-1, 0, 0),

where φ=(1+sqrt(5))/2 and φbar=(1-sqrt(5))/2; exchanging the two last columns exchanges T and T'. The symmetric-square formula also follows from χ_Sym²(g)=(χ(g)²+χ(g²))/2.

The six-dimensional Γ-representation W⊗T is irreducible. Indeed End(W)=1⊕T', End(T)=1⊕T⊕P₅, and (2.1) shows that their only common irreducible constituent is 1. Thus dim End_Γ(W⊗T)=1.

Two further consequences we use are

    W⊗W⊗T = T ⊕ P₄ ⊕ P₅,                  (2.2)
    Hom_Γ(W⊗Sym²T,W) = C.                    (2.3)

For (2.2), use W⊗W=1⊕T'. For (2.3), use Sym²T=1⊕P₅ and End(W)=1⊕T'. The unique map in (2.3) is contraction by a fixed invariant nonzero quadratic form q on T. This form is nondegenerate because its radical is a proper invariant subspace of the irreducible T.

## 3. Both parity blocks are constant-rank pencils

For u∈W, z acts by −1 on u. Thus b along L splits into

    b_-: O_L(-1)⊗(Sym²W ⊕ Sym²T) → J_-⊗O_L,
    b_+: O_L(-1)⊗(W⊗T) → J_+⊗O_L.           (3.1)

The source dimensions are nine and six. Each block is Γ-equivariant. Every nonempty finite Γ-invariant subset of L has at least twelve points, by the faithful A₅ action proved in the prior file. If a block has generic rank r>0, the common zero divisor of its nonzero r-minors has degree at most r. Since r≤9 or r≤6, respectively, its invariant support must be empty. If r=0 the block is identically zero. Thus each block has constant rank.

Let I_± be their image subbundles. A constant-rank linear pencil has an image bundle I that is both a quotient of O(-1)^n and a subbundle of a trivial bundle. Birkhoff–Grothendieck and global generation of I(1) and I* give

    I ≅ O(-1)^a ⊕ O^b.                       (3.2)

In particular the constant sections H⁰(I) form a fixed b-dimensional subspace of the target, contained in every image fiber. These spaces and their evaluation subbundles are intrinsically equivariant.

## 4. The even block has rank at least four

Repeated-input injectivity on u and the complementary three-space T gives a rank-three bundle injection

    A_T: O(-2)⊗T → I_+,
    u²⊗t ↦ f(u,u,t).                         (4.1)

Suppose rank I_+≤3. It must equal three by (4.1). Write I_+=O(-1)^a⊕O^(3-a). In the exact sequence

    0→K→O(-1)⊗(W⊗T)→I_+→0,

H⁰(K(1)) is an invariant subspace of the irreducible W⊗T. It cannot be the entire source representation since b_+ is nonzero. Therefore it is zero. All three splitting degrees of K are at most −2, while deg K=−6+a. Hence a≤0 and I_+≅O³.

Its constant three-dimensional image H is a quotient of the span of b_+'s coefficients, which in turn is a quotient of W⊗W⊗T. By (2.2), H must be isomorphic to T. But (4.1), when its target is the fixed H⊗O, corresponds to a Γ-map

    Sym²W⊗T = T'⊗T → H≅T.

This is zero by (2.1), contradicting injectivity. Thus rank b_+≥4.

## 5. The odd block has rank at least four

Restrict f to W³. Outer symmetry and cyclic zero make it factor through the Schur module S_(2,1)W≅W⊗det W≅W. It is nonzero by repeated-input injectivity, hence its two-dimensional image H⊂J_- is isomorphic to W. For every nonzero u∈W, b_u(Sym²W)=H. For an explicit check, after identifying this Schur image with W its formula is a nonzero scalar multiple of

    f(a,u,b)=det(a,u)b+det(b,u)a.

For w independent of u, the values on uw and w² span u and w. Hence H⊗O is a rank-two constant subbundle of I_-.

Suppose rank I_-≤3. By (3.2), h⁰(I_-) is either two or three. The value three is impossible: z acts as −I on H⁰(I_-), so its determinant at z would be −1, whereas every determinant character of the perfect Γ is trivial. Therefore H⁰(I_-)=H. The image modulo H is either zero or a line subbundle isomorphic to O(-1).

Choose a Γ-invariant complement J' to H in J_-. If that quotient line exists, its Γ-linearization is the standard one on U=O(-1): any two linearizations on this line bundle differ by a character, and Γ has no nontrivial characters. Its inclusion in J'⊗O therefore corresponds to a Γ-map W→J'. Its image is a fixed copy H'≅W. Consequently, in both cases, all values of f(t,u,t), t∈T,u∈W, lie in a fixed sum of at most two copies of W, namely H⊕H'.

By (2.3), the Γ-map W⊗Sym²T→H⊕H' must have the form

    f(t,u,t)=q(t) h(u),                       (5.1)

for one fixed linear map h:W→H⊕H'. Over C, the nondegenerate quadratic form on the three-space T has a nonzero isotropic vector t. Choose any nonzero u∈W. Then (5.1) gives f(t,u,t)=0. Outer symmetry and cyclic zero give

    f(t,u,t)+2 f(t,t,u)=0,

so f(t,t,u)=0. Repeated-input injectivity at t forces u∈Ct, impossible because W∩T=0. This contradiction proves rank b_-≥4.

## 6. Conclusion

The targets of the two blocks are complementary reflection eigenspaces. Sections 4 and 5 therefore give rank b_u=rank b_{+,u}+rank b_{-,u}≥8 at every point of L. Hence rank Q_u≥4. Equivariance gives the same statement on all twenty-five canonical lines.

The earlier curve theorem says every nonempty reduced curve part of Z₃ is exactly those twenty-five lines. They have now been excluded, so under that theorem's global hypotheses dim Z₃≤0. Its support is finite by projectivity and noetherianity. This does not classify its isolated points or its determinantal scheme structure.

Using the stronger universal K7 compatible-fiber bound of two from ../diagonal-hartogs-fiber-bound/PROOF.md, independent zero triples over residual-rank-exactly-three middles have affine dimension at most 0+2+3=5 (the last three are the independent nonzero scaling parameters). Thus residual ranks two and three cannot supply an independent component of dimension six. The global bound six remains unchanged; other rank strata retain their separate bounds.
