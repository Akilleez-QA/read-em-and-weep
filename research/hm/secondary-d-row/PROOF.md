# Canonical geometry of the D row of the actual secondary boundary

Work over C with G=SL2(F5), W its faithful two-space, T=P(W*), A=Sym2 W, D=Sym4 W, P the even four-space, and V the other even three-space. Retain the actual secondary map and the canonical source Q6=P O(2) plus W O(-1) from the exact immutable QUOTIENT, SQUARE and SECOND inputs in INPUTS.json. All linearizations are retained. No actual coefficient is selected.

The target representation is actual: SQUARE identifies H1(End(F_R)(-2))=Hom(D,A), with the scalar H1(O_R(-2)) zero. Trace self-duality and equivariant Serre duality give H1(B_R(-1))=H1(B_R(-2))*, hence A tensor D=A+V+P+D. No determinant character is lost since G is perfect. A final kernel corollary also uses BALANCED, PR976 at f23f8b9972d459c7c3ab532937964ef7f543b157, research/hm/balanced-first-cup-kernel/PROOF.md, which proves the actual K=T6 O(-1) plus A O(-2). Its exact bytes are likewise pinned in INPUTS.json.

## 1. Statement

The D-isotypic row of the actual secondary boundary has the form

    b_D = (a i, b j): P O(2) plus W O(-1) -> D O(4),

for two actual but unselected scalars a,b after choosing nonzero generators of its two one-dimensional equivariant Hom spaces. There are canonical exact maps

    0 -> P O(2) --i--> D O(4) --q--> O(12) -> 0,       (1)
    W O(-1) --epsilon--> O --v--> D O(4),   j=v epsilon,
    q v = c f12,   c nonzero,                          (2)

where epsilon is Euler evaluation, v the quartic Veronese section, and f12 a nonzero invariant of degree12, with reduced divisor the unique twelve-point orbit Omega. The relevant subbundles and maps up to nonzero scalar are canonical.

Consequently, without choosing which case occurs:

- a=b=0: the D row is zero.
- a nonzero, b=0: the D row has rank4 everywhere, kernel W O(-1), and cokernel O(12).
- a=0, b nonzero: the D row has rank1 everywhere, kernel P O(2) plus O(-2).
- a and b nonzero: the D row has rank5 off Omega and rank4 on Omega; its kernel sheaf is the canonical Euler O(-2) inside W O(-1), and its cokernel is O(12)|Omega. Its maximal-minor ideal is the reduced ideal of Omega.

This classifies a canonical row of the actual quartic boundary, not the rank of the entire boundary and not the values of a,b.

## 2. The degree-eight D linear system and its evaluation kernel

The fixed decompositions are

    Sym7 W=W'+T6,   Sym8 W=P+D,
    D tensor W=S+T6,   Sym9 W=S+T6,
    Sym10 W=A+V+D,   D tensor A=A+V+P+D.

Let D8 be the unique D-isotypic subspace of Sym8 W. It has no basepoint on T. Indeed a nonempty base divisor would be G-invariant and have degree at most8. The projective action factors through A5; a point stabilizer is cyclic and has order at most5. Hence every orbit has at least12 points. This rules out such a divisor. Evaluation therefore gives

    0 -> M -> D O -> O(8) -> 0,                        (3)

with rank M=4 and degree M=-8.

We claim H0(M(1))=0. This is the kernel of multiplication D8 tensor W -> Sym9 W. Binary Koszul exactness embeds that kernel equivariantly into Sym7 W. It is also a subrepresentation of D tensor W. The only common irreducible in their displayed decompositions is T6, so a nonzero kernel would have dimension6. But the kernel has dimension at most5: after choosing an abstract basis x,y of W, any relation x f+y g=0 in D8 tensor W is determined by f, since the polynomial ring is a domain. Projection to that D8 coordinate is injective. Thus the kernel is zero.

Birkhoff–Grothendieck now forces every splitting summand of M to have degree at most -2; its rank and degree force all four to equal -2. Therefore M=U O(-2) for a four-dimensional coefficient representation U. The canonical evaluation identification U=H0(M(2)) makes this equivariant. Since H1(M(2))=0, (3) twisted by2 gives

    U = (D tensor A) - Sym10 W = P.

Twisting (3) by4 proves (1). The Hom space Hom_G(P O(2),D O(4)) has dimension1, since P occurs once in D tensor A. Thus this constructed injection is the unique nonzero possible P-to-D channel of the actual secondary boundary.

## 3. The W channel and the invariant twelve-form

The quartic Veronese map v:O -> D O(4) is nowhere zero: it is the equivariant section corresponding to the invariant nondegenerate pairing D tensor D -> C. The Euler map epsilon:W O(-1)->O is onto with kernel O(-2). Their composite j is nonzero. Since Hom_G(W O(-1),D O(4)) has dimension1 (D occurs once in W tensor Sym5 W=V+P+D), j is the unique nonzero W-to-D channel.

The composition q v is an invariant section of O(12). We must prove it is not zero, rather than infer this from invariant multiplicity alone. The fixed character calculation gives dim(Sym12 W)^G=1. Choose a nonzero invariant f12. The ordinary polarization map

    Sym12 W -> Sym8 W tensor Sym4 W

is SL2-equivariant, and multiplication composed with it is a nonzero scalar times the identity in characteristic zero. Its value on f12 is therefore nonzero. In (P+D) tensor D the unique invariant summand is the invariant line D8 tensor D. Thus polarization of f12 spans that line. The product of the invariant pairing that defines q v is consequently a nonzero multiple of f12. This proves (2).

Its divisor is G-invariant of degree12. Every orbit has at least12 points, so the divisor consists of one orbit of12 distinct points with multiplicity one. Because G is perfect, any invariant orbit divisor has an invariant defining form, not merely a semi-invariant one. The uniqueness of the invariant line therefore gives uniqueness of this orbit as a divisor. No selected parameter or exceptional point has been evaluated.

## 4. Exact row kernels, cokernels and determinantal scheme

The first three cases follow from (1), the Euler sequence and the nowhere-zero Veronese map. In the fourth case quotient the D target by the everywhere-injective P channel. The remaining map is

    W O(-1) --b c f12 epsilon--> O(12).

Its kernel sheaf is ker epsilon=O(-2), since multiplication by f12 is injective on O. Its cokernel is O(12)|Omega. In the full row, a section in the kernel must have W-component in ker epsilon; its j image is then zero, so its P-component is zero. This proves the asserted canonical kernel, not merely its degree.

Locally make the P channel a four-by-four identity block. The remaining row is f12 times the two coordinates of epsilon; at least one coordinate is a unit at each point. Hence the ideal of five-by-five minors is exactly (f12). Thus the maximal-rank failure scheme is reduced Omega, and the rank is exactly4 there. This retains scheme multiplicities, not merely support or generic rank.

## 5. A conditional criterion for the full secondary kernel

Suppose both D-row coefficients a,b are nonzero. Let u_V and u_P be the actual coefficients of the W O(-1) channels to V O(4) and P O(4), respectively. Their Hom spaces are one-dimensional, since W tensor Sym5 W=V+P+D. Then the full reduced secondary map is sheaf-injective (equivalently, generically rank6) if and only if at least one of u_V,u_P is nonzero. If both vanish, its kernel sheaf is exactly the Euler O(-2).

Indeed its kernel is a subsheaf of the D-row kernel, which is precisely the Euler line, with zero P-source component. A nonzero map W O(-1)->J O(4), for J=V or P, restricts nontrivially to this line. Otherwise the Euler exact sequence would make it factor through O, but Hom_G(O,J O(4))=Hom_G(J,Sym4 W)=0 since Sym4 W=D. The descended morphism would be equivariant by uniqueness of descent, so this contradiction applies in the equivariant category. A nonzero map from a line bundle to a vector bundle is injective as a sheaf on the integral curve T. Thus any nonzero u_V or u_P kills the entire kernel sheaf. Conversely when both vanish the Euler line maps to zero in every row; the A row is zero because its two Hom spaces vanish, as follows from A tensor A=1+A+D and W tensor Sym5 W=V+P+D.

This is a conditional criterion for the actual coefficients, not a selection of their values. Sheaf injectivity does NOT assert injectivity on every fiber. In fact any nonzero restriction O(-2)->J O(4), J=V or P, is nowhere zero: a common-zero divisor of its degree-six coefficient forms would be G-invariant of degree at most6, impossible because every orbit has at least12 points. Off Omega the D row has one-dimensional fiber kernel equal to the Euler line, so the full reduced map has fiber rank6 there. Any fiber rank drop is therefore confined to Omega; its rank on Omega requires further analysis. If u_V=u_P=0 under the same hypothesis, the full map has generic rank exactly5.

## 6. The corresponding original kernel is determined conditionally

Retain the hypothesis that both D-row coefficients are nonzero. For the original boundary beta:K->target, the always-surviving square subbundle is L=A O(-6). If either u_V or u_P is nonzero, Section 5 gives ker beta=L exactly. If u_V=u_P=0, its kernel E fits into

    0 -> A O(-6) -> E -> O(-2) -> 0.                   (4)

This extension is nonzero in the equivariant category. Indeed a splitting would give a nonzero equivariant O(-2)->E->K. But the actual BALANCED splitting gives

    Hom_G(O(-2),K)=H0(K(2))^G
       =(T6 tensor W + A)^G=(V+P+D+A)^G=0.

Furthermore Ext1_G(O(-2),A O(-6))=H1(A O(-4))^G has dimension1, since by equivariant Serre duality on T this is the invariant multiplicity of A tensor Sym2 W=A tensor A, which is1. In characteristic zero the equivariant Ext group is the invariant part of ordinary Ext. The standard binary cubic evaluation sequence, twisted by O(-5), is

    0 -> A O(-6) -> S O(-5) -> O(-2) -> 0.             (5)

It represents a nonzero class: a splitting would contradict the displayed ordinary splitting type. All nonzero classes in this one-dimensional Ext space give isomorphic middle bundles up to rescaling an endpoint. Thus in this conditional case

    ker beta = S O(-5),

equivariantly up to isomorphism. In the other conditional case ker beta=A O(-6). These are kernel SHEAVES; exceptional fiber kernels may be larger because tensoring an exact sequence need not preserve left exactness. No value of a,b,u_V,u_P is selected.

## 7. Contribution and limits

The source and target Hom dimensions alone leave six scalar channels for the secondary map. This result gives exact geometric normal forms for both channels of its canonical D row, proves a forced reduced twelve-point determinant divisor if both are present, and supplies uniform lower bounds for the full map: rank at least4 everywhere if a is nonzero; rank at least5 away from Omega if a and b are nonzero. These conclusions keep the actual quartic corrections encoded in the unselected a,b. Together with Sections 5 and 6 they identify both reduced and original kernel sheaves conditionally on the stated D-row hypothesis, but do not choose any actual coefficient case. No top sigma, vertex delta, or global quadric-section conclusion is made.

Only fixed abstract character arithmetic, binary polynomial identities and universal bundle arguments are used. No selected actual HM/source coefficient, point, parameter, derivative, jet, matrix, or instance rank is evaluated.
