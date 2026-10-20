# A genuine projective symmetry of the elliptic HM carrier

## Theorem

Work over k=C or Q(i). Let C be the smooth projective elliptic curve y²=x³−x with origin O at infinity, let T=(0,0), and put X=C⁴. Let N=⊠₁⁴ O_C(O), let f:X→P⁴ be the elementary-symmetric map with affine coordinates [1:e₁(x):e₂(x):e₃(x):e₄(x)], and let E=N⊗f*H for the literal normalized HM bundle H. Define a on each factor by

    a(x,y)=(1/x, i y/x²).

The product automorphism, also denoted a, is globally regular and has order four. There is a coherent global regular order-four action on P(E) covering ⟨a⟩. In contrast,

    Hom_X(E,a*E)=0.

More precisely, for the nontrivial two-torsion line bundle

    Q=⊠₁⁴ O_C(T−O),

one has a*N≅N⊗Q and a*E≅E⊗Q. The projective lift is therefore a genuine line-twisted symmetry rather than an ordinary linear bundle lift. It gives no source-star, selector, HPL, or scalar-detector covariance assertion.

## 1. Global extension and group law

Write τ(x,y)=(-x,iy). The elliptic group law gives the rational formula

    t_T(x,y)=(-1/x, y/x²).

Indeed the line through the formal variable point (x,y) and T has slope y/x, and substitution into the algebraic addition law gives x-coordinate y²/x²−x=−1/x and y-coordinate −y+(y/x)(x+1/x)=y/x². These are identities of rational functions, not evaluations at a chosen point. Therefore

    a=t_T∘τ.

Both translation and τ are globally regular automorphisms of the smooth projective curve, so this identity extends the displayed rational formula across its apparent poles. The point T is fixed by τ; consequently t_T commutes with τ. Since T has order two and τ²=[−1],

    a²=[−1],     a⁴=id.

The automorphism [−1] is nonidentity in characteristic zero, so a has order exactly four. On X these statements hold factorwise for simultaneous translation and simultaneous CM. In particular, this a is not the CM map τ alone.

## 2. Compatibility with the target reversal

Let R:P⁴→P⁴ reverse the five coordinates:

    (Rv)_j=v_(4−j),       0≤j≤4.

On the dense open where all x-coordinates are finite and nonzero, the formal elementary-symmetric identity is

    e_j(x₁⁻¹,...,x₄⁻¹)=e_(4−j)(x₁,...,x₄)/e₄(x₁,...,x₄).

Consequently f∘a=R∘f there. Both sides are morphisms on all of the integral variety X and P⁴ is separated, so the equality holds globally. This also proves that zeros or poles of the displayed affine factor e₄ do not obstruct the projective identity.

In the cyclic indexing of the monomial symmetry theorem, the permutation is π(j)=−j+4 in F₅. It belongs to AGL(1,5). Sections 3–4 of [the monomial proof](MONOMIAL.md) explicitly extend its first-differential intertwiner to an invertible chain map through every differential. Therefore there is an isomorphism H≅R*H. This invocation uses the audited full-chain result, not merely a symmetry of γ.

## 3. The scalar-line twist

Since a=t_Tτ and τ fixes T, the scheme-theoretic inverse image of O under a is T. Pulling back the degree-one divisor line gives

    a*O_C(O)≅O_C(T)=O_C(O)⊗O_C(T−O).

The degree-zero line P_T=O_C(T−O) is nontrivial and has order two: under C≅Pic⁰(C), it corresponds to the nonzero two-torsion point T. External tensor product therefore gives a*N≅N⊗Q and Q²≅O_X. The line Q is nontrivial, since restricting to one factor with the other factors fixed gives P_T, up to a constant one-dimensional tensor factor.

Combining target compatibility and H≅R*H yields

    a*E = a*N⊗(f∘a)*H
         ≅ N⊗Q⊗f*R*H
         ≅ E⊗Q.

All these isomorphisms are algebraic over Q(i). There is no requirement to trivialize Q to projectivize this isomorphism. Also a*Q≅Q: pullback sends T−O to O−T, and P_T⁻¹≅P_T. This is consistent with a²=[−1] and cancellation of the twice-applied scalar-line twist.

## 4. Coherent global projective lift, with exact order

Projectivization canonically discards a tensor line, so

    P(E) ≅ P(f*H) ≅ X ×_(P⁴) P(H).

By Section 7 of the monomial proof, P(H) has a coherent action of the monomial projective stabilizer. Let r be its lift of R. In particular r²=id. On the displayed fiber product define

    A(z,p)=(a(z),r(p)).

The identity f a=R f ensures that this is a well-defined global regular automorphism. Its square is

    A²(z,p)=([-1]z,p),

because r²=id and f([-1]z)=f(z). Its fourth power is the identity. Its order is exactly four because the induced base automorphism a has order four. Thus this is an actual coherent cyclic action, not just a separately selected isomorphism of projective bundles. The construction avoids all choices of local frames for N or Q.

For this specific involution one can alternatively check coherence directly in the chain blocks from the monomial proof: the four blocks are P_π, M_π, −I₂⊗P_π, −I₂. Here π²=id, M_π permutes each of U,V,Z by π without signs, and every block squares to the identity. The projective construction above is already sufficient and does not require a general linearization of the entire monomial symmetry group.

## 5. Why the ordinary Hom space is zero

It remains to exclude an untwisted bundle map, rather than merely noting that our construction has a line twist. Use the exact four-term vector-bundle presentation A=N⊗f*L of E from the exact-presentation foundation, pulled back and tensored by N as in P01, with terms in degrees −1,0,1,2:

    5N⁻¹ → 15N → 10N³ → 2N⁵.

It has sole cohomology E in degree zero. The total Hom complex Hom•(A,A⊗Q) computes RHom(E,E⊗Q), and its degree-r terms are sums of N^(2r)⊗Q, for −3≤r≤3.

On every elliptic factor, O_C(2r O)⊗P_T has positive degree when r>0 and negative degree when r<0. Thus by elliptic line-bundle cohomology and Künneth, its external fourth power has cohomology only in q=0 for r>0 and only in q=4 for r<0. For r=0 the nontrivial degree-zero factor P_T has no cohomology at all, so H*(X,Q)=0. Therefore the spectral sequence

    E₁^(r,q)=H^q(X,Hom^r(A,A⊗Q))

has no entries with total degree zero: positive r occurs only at q=0, negative r≥−3 only at q=4, and the r=0 column vanishes. It follows that

    Hom_X(E,E⊗Q)=0.

Together with a*E≅E⊗Q this proves Hom_X(E,a*E)=0. The same argument works directly over Q(i), or the vanishing follows there from faithful base change to C.

There is no contradiction with the CM non-lift theorem. That theorem concerns τ alone, whose target action is the alternating-sign diagonal S and whose pullback fixes N. Here translation by T changes both the target action (to the permitted reversal R) and the scalar line (to Q). Nor does vanishing of ordinary Hom obstruct a projective lift: projective bundle isomorphisms permit tensoring by a line bundle.

## 6. Uniqueness and endomorphism algebras

The projective lift is unique. Over C, a vertical automorphism of P(E) would give E≅E⊗P for a line P. Since det E≅O_X, necessarily P²≅O_X; all such torsion lines on X lie in Pic⁰(X). The same argument as Section 5 applies to every nontrivial P∈Pic⁰(X): Pic⁰(C⁴) consists of external tensor products of degree-zero lines, at least one nontrivial, so its r=0 column is acyclic and the nonzero-r cohomology remains concentrated as above. Thus Hom(E,E⊗P)=0 for nontrivial P. For trivial P the degree-gap argument identifies End(E) with strict constant chain maps; the identity case of the monomial theorem bounds the initial intertwiner space by one and the identity map supplies its nonzero element. Hence End(E)=C, and every vertical projective automorphism is trivial. Two lifts of a differ by such a vertical automorphism, proving uniqueness. Uniqueness over Q(i) follows after base change.

The isomorphism a*E≅E⊗Q also yields an O_X-algebra isomorphism

    End(a*E)≅End(E⊗Q)≅End(E).

Thus this example simultaneously has projective and endomorphism-algebra symmetry while its ordinary Hom space vanishes. These are precisely distinct notions here.

