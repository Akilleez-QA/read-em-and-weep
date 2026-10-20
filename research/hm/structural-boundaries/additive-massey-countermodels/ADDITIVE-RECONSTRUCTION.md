# Additive derived reconstruction cannot localize the HM Massey operation

## Main theorem

Let H be the actual rank-two HM bundle on P4 in characteristic zero. There is a sheaf of unital associative algebras B with precisely the same underlying O-module and N-equivariant structure as End H, and therefore precisely the same twisted graded S-derived object, but whose canonical weight-(0,1,1) degree-one triple Massey operation is identically zero.

The replacement algebra is not Azumaya and is not the actual endomorphism algebra. Its trace pairing is degenerate. Thus this theorem excludes only an argument from additive derived reconstruction, underlying S-linear complex, and coordinate-module data. It does not exclude an argument using the actual matrix multiplication, its nondegenerate trace pairing, its inner linear-resolution differential, or its multiplicative reconstruction.

## 1. Construction and exact preservation

Write F=End_0 H. The ordinary trace gives the N-equivariant splitting

End H = O Id direct-sum F.

Define B=O direct-sum F with multiplication

(a,u)(b,v)=(ab,av+bu).

This is the square-zero extension O semidirect F. It is an associative unital O-algebra. Its underlying O-module is IDENTICAL to End H by (a,u) -> a Id+u. The action of the classical normalizer N respects trace, scalars, and F, and therefore preserves this new multiplication. All twisting linearizations are unchanged.

Consequently the objects

C_actual=direct-sum_n RΓ(P4,End H(n)),
C_square=direct-sum_n RΓ(P4,B(n))

are identical as N-equivariant graded S-derived objects, where S=Sym H0(O(1)). This statement preserves every cohomological degree and every coordinate-module map, not only the previously used H1 and H2 rows. Any additive Beilinson reconstruction, exact triangle, extension class of underlying complexes, derived saturation datum, or invariant depending only on this S-derived object is the same. Only multiplication has changed.

## 2. Canonical Massey vanishing

Use a multiplicative Cech resolution, or twisted Dolbeault complexes over C. Since H1(P4,O(n))=0 for every n, all degree-one cohomology classes have F-valued closed representatives. Products of any two F-valued cochains are strictly zero in B. Thus adjacent product primitives may both be chosen to be zero, and the resulting triple cocycle is zero.

Every alternative primitive changes the class by products of degree-one cohomology classes; these products are zero for the same reason. Therefore the Massey set is the singleton {0}. In particular the canonical ordered map with source dimensions 24,5,5 and target dimension 20 is identically zero. This deduction holds for all degree-one triples, not just this weight pattern.

The target remains the actual irreducible twenty-dimensional N-module: its underlying cohomology has not changed. Thus naturality, target irreducibility, and additive reconstruction coexist with the zero alternative.

## 3. Exact losses

The ideal F has square zero in B; its product in End H does not. Therefore B is not the Azumaya algebra End H and cannot be substituted in a theorem requiring an endomorphism-algebra realization.

The functional tr_B(a,u)=2a defines the formal adjugation tau(a,u)=(a,-u), which is an involutive anti-automorphism of this commutative square-zero algebra. On the Dolbeault resolution over C (or a commutative Thom–Whitney model), it has the usual graded anti-automorphism sign. This strict assertion is not made for the ordinary ordered Cech cup product. But the multiplication trace pairing tr_B(xy) annihilates F against all of B, so it is degenerate. Although the underlying vector bundle still admits its original nondegenerate trace bilinear form and Serre pairing, that bilinear form is not obtained from the new product and must not be treated as a cyclic trace pairing for B.

There is likewise no assertion that a chosen resolution of B as an O-module carries the actual End-resolution multiplication, inner differential, or the universal commutator primitive identities. Additive equality does not imply such multiplicative equality.

## 4. Why S-linear nonformality itself does not localize m011

There is also an elementary underlying-module reason for nonformality of C_actual, independent of the actual multiplication. Let Q be exact graded sheafification and R=RΓ_* its derived right adjoint. For a coherent sheaf E on projective space, the counit QR(E) -> E is an isomorphism: sheafification of Γ_*E is E, and every higher graded cohomology module is irrelevant-ideal torsion, hence sheafifies to zero. Thus R is fully faithful on these objects and the adjunction unit C -> RQ(C) is an isomorphism for C=R(E).

Call such C derived saturated. Direct summands of a derived saturated object are derived saturated, by naturality of the unit. A nonzero irrelevant-ideal-torsion module L, in any cohomological shift, is not derived saturated: Q(L)=0, so its unit has zero target.

If R(E) were formal as a graded S-complex, it would be a direct sum of its cohomology modules in their respective shifts. Any nonzero higher cohomology module would then be a nonzero torsion direct summand of a derived saturated object, a contradiction. In particular H1_*(End H) is nonzero, so C_actual is not formal as an S-complex.

Exactly the same statement applies to C_square, since it is the identical underlying S-derived object, while Section 2 proves m011 is zero there. Hence the implication

underlying S-linear nonformality -> nonzero m011

is false even for this exact underlying HM object. The nonformality theorem detects additive extension data among coordinate modules; it does not specify the associative degree-one ternary operation. This observation concerns S-linear formality, not ordinary formality after forgetting S, nor the formality of a single-twist complex.

## 5. What remains a possible structural route

A successful reconstruction argument must use multiplicative information absent from B, for example the actual Azumaya/endomorphism multiplication together with its perfect cyclic trace pairing, or the inner differential of the literal linear resolution. It must additionally prove that the resulting obstruction lies in arity three and weight (0,1,1). Merely showing that some higher associative operation or some coordinate-module extension is nontrivial does not establish that localization.

No claim is made that the Azumaya condition plus the preserved additive data is sufficient, or that this higher multiplicative obstruction has been computed. Actual HM nonvanishing remains undecided by this argument.

## Evidence boundary

This is a sheaf-algebra construction and an adjunction argument. No actual Massey value, source/model matrix product, point, jet, rank, polynomial instance, or residual was evaluated. The construction changes only the hypothetical comparison algebra, not geometric source data.
