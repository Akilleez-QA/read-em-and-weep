# Five necessary actual triplet kernels and two full positive endpoint images

## Statement and exact scope

Keep the actual physical G=SL2(F5) line, fixed determinant convention, saturated rank-thirty constant ambient, rank-seventeen source E, and rank-four maximal ordered plateau (1,1) of PR1194 at e4de44641a53b0b3424102cd5fbaf3cf5821996d. Assume its triplet quotient

    A_q=A_std(4)+O(-8),  A_std=Sym2 W.

The actual section gates come first. H0(A_q)=A_std+V+P+D embeds in M2, and H0(A_q(1))=W'+S4+2T6 embeds in M3. PR1194 then forces the actual source

    E=D(-2)+(W'+T6)(-3)+V(-4)+O(-8).

Let K=E^- be its actual kernel. It has rank thirteen, degree -58, top degree at most -3, and endpoint derivative rank at most three. Its only cubic coefficient possibilities are 0 or S4. The complete immutable proofs of PR1194 and PR1185 Section 2 are retained in inputs/. Their actual ambient/source hypotheses remain imported, including the canonical actual derivative and negative-horizontal-subbundle argument.

Then exactly the following five equivariant splittings are necessary alternatives for K:

    K1=(V+P)(-4)+T6(-5),
    K2=(V+2P)(-4)+W'(-7),
    K3=(V+P+D)(-4)+O(-10),
    K4=S4(-3)+(V+P)(-4)+W(-9),
    K5=S4(-3)+(V+P)(-4)+O(-8)+O(-10).

Here 'necessary alternatives' asserts neither existence nor exclusion. For K1 and K2 only, the actual endpoint derivative has the full coherent image

    im beta_K=A_std(2) inside A_q(-2)=A_std(2)+O(-10).

Consequently K^- has rank ten and degree -64, and, writing

    E0=D(-2)+(W'+T6)(-3)+V(-4),

one has actual equalities K^+=E0 and E0^-=K. Thus E0 has rank sixteen and degree -46, with generic derivative rank three. This is not an invocation of any rank-seventeen rank-three classification. No full endpoint image claim is made here for K3,K4,K5. The zero-original-defect lemma is not needed for this theorem.

## 1. Exact kernel cohomology and the near-top coefficient map

PR1194 gives chi_G(E(3))=W'+2T6 and chi_G(E(4))=3V+3P+2D. For the triplet quotient, direct universal characters give

    chi_G(K(3))=-T6,  chi_G(K(4))=V+P,
    H0(A_q(2))=V+2P+2D.

Write an ordinary equivariant Birkhoff splitting

    K=R3(-3)+R4(-4)+N,  top N<=-5,

with R3=0 or S4. Exact Euler characters imply

    H1(N(3))=R3+T6,
    R4=V+P-R3 tensor W+H1(N(4)).

The actual R4 coefficient map into H0(A_q(2)) is injective. A killed coefficient vector would give a saturated direct line O(-4) in K whose own derivative lands in (K/line)(-2), of top degree at most -5. It would therefore be a negative horizontal line in the original constant ambient, impossible. Only R4 injects: this statement does not inject all of H0(K(4)) and does not make a splitting horizontal.

For an irreducible block R(-j) in N, j>=5, the two H1 contributions are

    H1 at twist three: R tensor Sym^(j-5) W,
    H1 at twist four:  R tensor Sym^(j-6) W,

with negative powers zero. Its first dimension is (j-4)dim R. Thus the dimension-six or dimension-ten budgets below bound every atom separately; there is no search of kernel tuples or actual source coefficients.

## 2. Cubic-free kernels

For R3=0 the budget is the irreducible T6. The only individual atoms contained in this budget are

    T6(-5): (T6,0),
    V(-6):  (T6,V),
    W'(-7): (T6,P),
    O(-10): (T6,D),

where each pair records the twist-three and twist-four H1 representations. Completeness follows from (j-4)dim R<=6, parity, and the nine physical irreducibles. Since the first budget is irreducible, exactly one atom occurs. The resulting R4 values are V+P, 2V+P, V+2P, V+P+D. The second has two copies of V and contradicts the single V in H0(A_q(2)). The other three give K1,K2,K3.

## 3. Cubic-S4 kernels

Now R3=S4 and S4 tensor W=A_std+D. The budget is S4+T6, of dimension ten. The bound is 5<=j<=14; after parity and the individual cost constraint, the complete list of allowed atoms is

    S4(-5): (S4,0),
    T6(-5): (T6,0),
    D(-6):  (S4+T6,D),
    V(-6):  (T6,V),
    W'(-7): (T6,P),
    O(-8):  (S4,A_std),
    W(-9):  (S4+T6,A_std+D),
    W'(-9): (S4+T6,D+V),
    O(-10): (T6,D),
    O(-14): (S4+T6,D+P).

This is a fixed universal irreducible-atom table, not a search of bundle tuples. Genuineness of

    R4=V+P-A_std-D+H1(N(4))

requires H1(N(4)) to contain both A_std and D. In the entire atom list, A_std occurs only for O(-8) and W(-9). If W(-9) occurs it already consumes the whole S4+T6 budget, giving K4. If O(-8) occurs it consumes exactly S4, and the remaining T6 atom must supply D. The only such atom is O(-10), giving K5. In each case R4=V+P. This proves the five necessary kernel alternatives without enumerating combinations.

## 4. A universal actual rank-two V image

In every displayed K the coefficient block R4 contains V. By the near-top injection, the actual derivative restricted to this V(-4) block is nonzero. Its O(-10) component is zero by degree. Let

    0 -> W(1) -> A_std(2) -> O(4) -> 0

be the canonical quadratic binary evaluation sequence. The composition V(-4)->O(4) vanishes because Hom_G(V,Sym8 W)=0, with Sym8 W=P+D. Therefore the nonzero V row factors through W(1).

It cannot have generic rank one. Its saturated rank-one image in W(1) would be an equivariant line O(e). Since G is perfect and the ambient has center-even parity, e is even; the ordinary top-degree bound gives e<=1, hence e<=0. But Hom_G(V(-4),O(e))=Hom_G(V,Sym^(e+4) W)=0 for e<=0: symmetric powers through degree four contain no V. This contradicts nonzero rank one.

Thus the row has generic rank two. Its maximal minors have polynomial degree ten, since the source consists of three O(-4) lines and det W(1)=O(2). Their common zero divisor is G-invariant and has degree at most ten. A nonempty invariant divisor on the projective A5 line has degree at least twelve, so this common divisor is empty. The actual row is everywhere onto W(1). In particular the coherent image of beta_K contains this fixed canonical rank-two subbundle of A_std(2).

## 5. Full positive image for K1 and K2

For K1 and K2 all source degrees of K exceed -10, so beta_K has no O(-10) component. It lands in A_std(2), already containing W(1). Consider its composition with A_std(2)->O(4).

The V(-4) row is zero by the preceding section. A P(-4) row, if nonzero, has polynomial degree eight. The T6(-5) row of K1, if nonzero, has degree nine. The W'(-7) row of K2 is zero, because Sym11 W=W+S4+T6 has no W'. These are all rows. Any nonzero P or T6 row is onto O(4): its common zero divisor is invariant and has degree at most eight or nine, below twelve. Hence any nonzero composition to O(4), together with the already-surjective W(1) row, makes the full coherent image exactly A_std(2).

It remains to rule out the identically-zero composition. Then im beta_K=W(1), so F=K^- has rank eleven and degree

    deg F=deg K-deg W(1)=-58-2=-60.

Its actual predecessor quotient is K/F=W(1), of rank two. The same terminating actual kernel filtration as in PR1185 now has at most two columns, with heights h1>=h2>=0 and h1+h2=11. Its coherent-image capacity is

    deg F <= h1+h2-h1(h1+1)-h2(h2+1)
           =-h1^2-h2^2 <=-61.

The final inequality follows from integer h1+h2=11; equality is attained only at (6,5). Thus -60<=-61 is impossible. This checks every height and uses the actual rank-eleven F, not the old rank-thirteen endpoint. Therefore the full positive image is forced in both K1 and K2.

For that image, rank K^-=13-3=10 and deg K^-=-58-6=-64. The negative projection of the original quotient E->A_q comes solely from its source O(-8), with nonzero scalar. Consequently K lies in E0, and E0/K=A_std(4). The saturation of the derivative span K^+ is exactly the preimage of im beta_K tensor T_P1=A_std(4), hence K^+=E0. The derivative of K stays in E0; conversely any derivative-kernel section of E0 is in the original E derivative kernel K. Therefore E0^-=K. These are actual subbundle relations, not connection-compatible Birkhoff splittings.

## Contribution and boundary

This theorem resolves the entire tiny kernel-cohomology ambiguity into five necessary forms and proves an exact actual endpoint image for two of them. It uses only fixed universal representation products, a bounded individual-atom table, invariant divisor minima and symbolic capacity. No selected actual coefficients, parameters, points, jets, tensors, matrices, instance ranks, broad candidate search, historical enumeration or height scan is used. The three other kernels and the triplet quotient itself remain open.
