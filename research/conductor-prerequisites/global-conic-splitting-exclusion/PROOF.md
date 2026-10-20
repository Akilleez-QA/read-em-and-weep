# Finite global exclusion of splitting along a plane conic

## Main result

Let F be the normalized Horrocks–Mumford bundle on Y=P⁴ over C. Let i:W=P²→Y be the square-quadratic surface, so i*O_Y(1)=O_W(2), and put E=i*F. Let C⊂W be the smooth discriminant conic and X_n=nC, with ideal O_W(−2n). Then

    E|X_n does not split as a sum of two line bundles for every n≥9.

More precisely, restriction is an isomorphism of C-algebras

    H⁰(W,End E) → H⁰(X_n,End(E|X_n))             (n≥9).   (A)

This is a universal structural bound for the actual global bundle E. No actual HM matrix, conic splitting type, obstruction coordinate, or selected rank is evaluated. Nine is a sufficient bound; optimality is not claimed.

## 1. Imported bundle and resolution data

The normalized HM bundle has c₁(F)=−H, c₂(F)=4H², and F*=F(1). Pullback gives

    rank E=2,    c₁(E)=−2h,    c₂(E)=16h²,    E*=E(2).

Here every twist in this document is a plane twist unless explicitly stated otherwise. The primary section resolution, established in https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md, pulls back to

    0 → 2O(−16) → 20O(−12) → 35O(−10)
      → 15O(−8) ⊕ 4O(−6) → E → 0.                       (R)

Although pullback is not generally exact, it is exact here: the original resolution resolves a vector bundle by vector bundles, so every successive kernel is locally free and every short exact kernel sequence is locally split. Pullback preserves these sequences.

The square surface and smooth conic geometry are established in https://github.com/Akilleez-QA/read-em-and-weep/blob/21b252420c0011b2cbc119cab2983a6d4ad2e966/research/conductor-normalization/conductor-double-conic-intersection/PROOF.md. The numerical c₂ formula is the ordinary pullback identity 4(2h)²=16h², not a degree-of-image substitution.

## 2. Dimension-two cohomology improves the regularity estimate

For an exact locally free resolution

    ... → A₂ → A₁ → A₀ → G → 0

on P², one has H¹(G)=0 if H¹(A₀)=H²(A₁)=0, and H²(G)=0 if H²(A₀)=0. Indeed let K₁=ker(A₀→G) and K₂=ker(A₁→K₁). The two kernel sequences give H¹(A₀)→H¹(G)→H²(K₁), with H²(A₁)→H²(K₁) surjective because H³(K₂)=0. They also give H²(A₀)→H²(G) surjective because H³(K₁)=0. The kernels need not satisfy an extra vanishing.

Apply this to (R), using H¹(P²,O(k))=0 for all k and H²(P²,O(k))=0 for k≥−2. It gives

    H¹(E(t))=0 for t≥8,
    H²(E(t))=0 for t≥6.                                  (B)

Consequently reg(E)≤9 and reg(E*)≤7. The tempting bound reg(E)≤13 from the maximum of all resolution shifts minus homological degree is valid but wastes the fact that W has dimension two.

Put B=End E. Tensoring (R) by E*(t)=E(t+2) is exact. Its two rightmost terms are

    A₀(t)=15E(t−6) ⊕ 4E(t−4),
    A₁(t)=35E(t−8).

For t≥14, (B) gives H¹(A₀(t))=0 and H²(A₁(t))=0. Hence

    H¹(B(t))=0 for t≥14.                                 (C)

This slightly improves the t≥15 consequence of reg(B)≤reg(E)+reg(E*)≤16. Both imply the same integral conic bound below. No endpoint differential is asserted to be surjective at t=13.

## 3. Negative cohomology and the restriction algebra

The quotient at the right of (R) implies E(8) is globally generated, since its source is 15O⊕4O(2). Therefore E*(6)=E(8) is globally generated as well. Their tensor product B(14) is globally generated.

The trace pairing on End E is nondegenerate, so B*=B. Dualizing an evaluation surjection O^N→B(14) gives an injection of vector bundles

    B → O(14)^N.

Thus

    H⁰(B(−2n))=0 for n≥8.                               (D)

Serre duality on P², with canonical bundle O(−3), gives

    H¹(B(−2n))* ≅ H¹(B(2n−3)).

By (C) this group vanishes for n≥9. Tensor the divisor sequence of X_n with B:

    0 → B(−2n) → B → B|X_n → 0.

For n≥9, (D) and the negative H¹ vanishing show that its restriction map on H⁰ is bijective. Since restriction preserves composition and identity, this is precisely the algebra isomorphism (A). The equality B|X_n=End(E|X_n) follows from local freeness, even though X_n is nonreduced.

## 4. A splitting would give an impossible global idempotent

Suppose E|X_n=L⊕M for line bundles L,M and n≥9. Projection onto L is an idempotent p_n, neither zero nor identity. By (A), p_n has a unique lift p∈H⁰(W,B). Because restriction is injective and p²−p restricts to zero, p²=p. Its image and kernel are locally free direct summands. Their ranks are locally constant; W is connected and their restrictions to C each have rank one. Thus

    E ≅ O_W(l) ⊕ O_W(−2−l)

for some integer l, since Pic(P²)=Z. But then

    16=c₂(E)/h²=l(−2−l)=1−(l+1)²≤1,

a contradiction. Hence E|X_n cannot split. No simplicity or stability theorem for E is needed. In particular the argument does not claim H⁰(End E)=C: indecomposability excludes nontrivial idempotents, not all non-scalar endomorphisms.

## 5. What this bounds among local obstruction layers

The restriction E|C splits by the splitting theorem on P¹. Consequently there is a first nonsplitting order

    n₀=min{n≥2 : E|X_n is not a direct sum of line bundles},
    2≤n₀≤9.                                             (E)

Nonsplitting persists at every higher order: a higher splitting would restrict to a splitting below. In the setting of ../higher-conic-lifting-obstruction/PROOF.md, with even splitting gap d≥8, ε=0 implies splitting on X₂, so (E) sharpens to 3≤n₀≤9.

The first nonsplitting layer is m=n₀−1≤8. When the unique maximal embedded line A_m has been defined, failure of splitting at the next layer can occur in two different ways:

1. Its negative-root obstruction ob_m is nonzero, in H¹(C,O_P¹(−d−4m)); then the line does not lift.
2. The line lifts, but the associated extension class is nonzero. If the preceding bundle is split, the new class lies in

       H¹(C,O_P¹(d−4m))/im(δ_m),

   with δ_m the connecting map from sections of the preceding ratio line bundle.

For even d, the second possibility is excluded whenever d≥4m. Thus, if the first nonsplitting order n₀ satisfies n₀≤floor(d/4)+1, that failure must be a nonzero negative-root obstruction. Outside this range the finite global exclusion alone does not identify which mechanism occurs.

The actual imported conic range d≤20 does not force d≥32, the uniform positive-vanishing condition through X₉. Accordingly this theorem does NOT prove that the maximal line must fail to lift by order nine. It excludes full splitting by order nine. It does not compute actual ob₂, any subsequent ob_m, diagonal Picard parameters, extension classes, or a retained source value. It also does not identify which first nonsplitting order in (E) occurs.

## 6. Scope and source status

The proof uses the previously verified HM section resolution, pullback of locally split exact sequences, elementary projective-plane cohomology, global generation, Serre duality, and the idempotent criterion for vector-bundle decompositions. No actual HM source value or rank is determined. This proof provides global input missing from unrestricted finite-neighborhood countermodels: those local models cannot have arbitrary deep splittings and simultaneously be restrictions of this E.
