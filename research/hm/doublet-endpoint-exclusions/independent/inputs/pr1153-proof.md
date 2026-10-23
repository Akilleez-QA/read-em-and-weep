# A P-type cubic Gauss kernel forces an Euler doublet image

## Statement and scope

Work over C on the fixed physical binary-icosahedral line P(W*), with G=SL2(F5), the determinant convention, and the ACTUAL saturated inclusion E in the constant thirty-dimensional plane-section bundle H O. Write beta_E:E -> (H O/E)(-2), K=ker beta_E, and A=E/K. Thus A is the actual locally free quotient, not the saturation of its image in the ambient derivative target. Assume the P-type source

    E=P O(-2)+(W'+T)O(-3)+V O(-4)+W' O(-5).

All notation uses the pinned physical representation marking: dim(P,W',T,V)=(4,2,6,3), W is the standard two-dimensional representation, P=W' tensor W, and P tensor W=W'+T.

We prove the following necessary conditions for this actual source, without assuming a rank for beta_E or its next derivative.

1. If H0(K(3)) is nonzero, it is exactly the W' constituent from the top P O(-2). The actual top row factors nontrivially through its Euler quotient W' O(-1).
2. This factorization is equivalent to the nonzero cubic-kernel alternative. Its coherent image in A is either W' O(-1), with top-row kernel W' O(-3), or a line O(e) with e even and e>=6, with top-row kernel noncanonically equivariantly isomorphic to W' O(-3)+O(-e-2). These are coherent images, not their saturations in A.
3. Consequently, if Hom_G(W' O(-1),A)=0, then H0(K(3))=0 and

       H0(A(2)) + chi_G(A(4)) - chi_G(E(4))

   is a genuine representation. Here chi_G(E(4))=3V+3P+2D.

No upper bound on the degrees of A is required in item3. This is a new P-type actual-map criterion, not a claim that a particular quotient shape is newly excluded, that an abstract image occurs for the actual map, or that the original repair is complete.

## 1. Exact inputs and geometric distinction

INPUTS.json authenticates five complete immutable public originals by URL, byte count, SHA256 and Git blob ID. PR1140 at 7a2488bcd36d95f79b5198001111b1a31fe5c3ba supplies the actual cubic-kernel alternatives and the graph argument. PR1129 at d1238732f42df5c70ba4430e230428d2cf699bbe supplies the near-top visibility lemma. The strict-top theorem and physical character source are pinned at db51525015bb7c5e825833d550d08dedf6f6ea96. PR1142 at df2fd3d35dac577d7f1e1c4d51fe68b1fcc824ad is the analogous D-type theorem and provides context, not a proof of this P-type assertion. The actual source and embedding hypotheses above are explicit: we do not derive them from a historical enumeration. Their construction is recorded in the dependencies cited by PR1140.

The coefficient-presentation space of dimension54 is not the constant Gauss ambient H of dimension30. All derivatives below are for the latter actual inclusion. Splittings used below are equivariant ordinary Birkhoff splittings, never horizontal or quotient-compatible connection splittings.

The near-top fact needed here can also be seen directly. If L=U O(-3) is a saturated subbundle of E, E/L has degrees at most -2, and beta_E kills L, then the actual derivative of L lands in (E/L)(-2). But Hom(L,(E/L)(-2))=U* tensor H0((E/L)(1))=0. Thus L is horizontal in the constant ambient. Its classifying map has zero derivative and is constant over C; saturation makes it a constant degree-zero subbundle, contradicting its negative degree. This applies to saturated graphs as well as displayed summands.

## 2. Localizing the cubic kernel, including mixed cancellations

Let F=P O(-2) be the top block and C=W' O(-3) the displayed cubic W' block. Strict-top gives H0(K(2))=0, so the top row p|F:F -> A is nonzero. PR1140 proves

    H0(E(3))=(W'+T) + (W'+T),
    H0(K(3)) is either zero or W'.

The two T channels are independent in the quotient. Suppose the cubic kernel is W'. Its inclusion into the cubic source has only two possible isotypic components: the top W' in H0(F(3)), and H0(C(3)).

If its projection onto H0(C(3)) were nonzero, it would be an isomorphism by Schur's lemma. Normalizing that projection to the identity, its top component corresponds under

    Hom_G(W' O(-3),F)=Hom_G(W',P tensor W)

to a bundle map g:C -> F. Equality of cubic coefficient maps is equality of these bundle morphisms. The kernel then evaluates to the graph c -> (g(c),c) inside F+C. This is a saturated direct summand C of E, with quotient isomorphic to the sum of all other displayed blocks, hence with maximal degree -2. Its p-row vanishes because all its coefficient sections belong to H0(K(3)); equivalently beta_E kills the whole graph. This contradicts Section1.

The displayed projection must therefore vanish. The nonzero kernel W' is exactly the unique top W' constituent. In particular there are no hidden cancellations mixing the displayed and top W' copies. This strengthens the abstract kernel alternative of PR1140 by locating its sole possible nonzero constituent in the actual top row.

## 3. Unique Euler factorization

The evaluated top W' gives a nonzero equivariant morphism j:W' O(-3) -> P O(-2), unique up to scalar because W' has multiplicity one in P tensor W. Since P=W' tensor W, this is the standard Euler inclusion tensored by W' and twisted:

    0 -> W' O(-3) --j--> P O(-2) --q--> W' O(-1) -> 0.     (1)

For completeness, before tensoring, in homogeneous coordinates the two maps are the column (x,y) and the row (-y,x). Their product is zero. On the x-chart normalize x=1: the maps are (1,t) and (-t,1), whose kernel and image agree and whose ranks are one everywhere. On the y-chart use (s,1) and (-1,s), with the same conclusion. Thus (1) is exact and saturated globally; no evaluation of an actual source coefficient is involved. The determinant marking identifies the standard dual convention.

Section2 says p|F kills j. Hence (1) gives a unique factorization

    p|F = f q,       f:W' O(-1) -> A.

It is nonzero because p|F is nonzero. This is an actual morphism into the actual quotient A, not merely a character possibility. Conversely, if the actual top row factors through q, it kills j. Twisting (1) by three, the Euler kernel supplies a nonzero W' in H0(K(3)). The PR1140 alternative then makes the whole cubic kernel exactly W'. Thus factorization of the actual row through this Euler quotient is equivalent to the nonzero cubic-kernel alternative; abstract existence of some nonzero map W' O(-1) -> A is not sufficient.

## 4. Coherent-image dichotomy and the line-degree threshold

Let I be the coherent image of f in A. It is torsion-free on a smooth curve, hence a vector bundle, and f surjects onto I as a sheaf. Its rank is one or two.

If its rank is two, the kernel of the surjection W' O(-1) -> I has rank zero. As a subsheaf of a bundle it is torsion-free, so it is zero. Thus I is equivariantly isomorphic to W' O(-1). This is a sheaf injection of the doublet into A, not necessarily a saturated subbundle.

If its rank is one, I=O(e) with the standard equivariant linearization: G is perfect, so no character twist is available. There is a nonzero equivariant map W' O(-1) -> O(e), requiring

    Hom_G(W',Sym^(e+1) W) != 0.                         (2)

A negative exponent contributes zero. The first occurrence of W' in Sym^n W is n=7; the exact lower sequence is

    Sym0=1, Sym1=W, Sym2=A_std, Sym3=S,
    Sym4=D, Sym5=T, Sym6=V+P, Sym7=W'+T.

Thus e>=6. Central parity in (2) also requires e even. In particular, when maxdeg A<=5, the rank-one alternative cannot occur, and a nonzero cubic kernel would force an actual sheaf injection W' O(-1) -> A. Without that extra degree assumption, the nonzero map f still always exists, which is enough for the Hom-vanishing criterion.

Write K_F=ker(p|F). In the rank-two image case, f is a sheaf injection, so K_F is exactly j(W' O(-3)). In the rank-one case, the surjection W' O(-1) -> O(e) has line kernel O(-e-2), by additivity of degree. Its equivariant linearization has no character ambiguity because G is perfect. Pulling this line kernel back through q gives

    0 -> W' O(-3) -> K_F -> O(-e-2) -> 0.

Its ordinary extension group is W' tensor H1(O(e-1))=0 since e>=6. A splitting can be averaged over the finite group, so

    K_F is equivariantly isomorphic to W' O(-3)+O(-e-2).

This splitting is noncanonical and is not asserted horizontal. It is the kernel of the restricted top row, not the entire Gauss kernel K. The image alternatives and kernel descriptions are necessary conclusions, not assertions of actual realizability. No sufficiency for an actual Gauss image is claimed.

## 5. Strengthened quartic envelope

If Hom_G(W' O(-1),A)=0, the map forced by Section3 cannot exist. Therefore H0(K(3))=0. Since K is a bundle on P1, every ordinary degree of K is then at most -4. K is saturated in E and in the constant ambient. Apply strict-top to K: its own Gauss kernel Kminus has all degrees at most -5, so H0(Kminus(4))=0.

The actual derivative of K lands in (E/K)(-2)=A(-2), because beta_E vanishes on K. Its kernel is Kminus. Consequently

    H0(K(4)) embeds in H0(A(2)).

The exact sequence 0 -> K -> E -> A -> 0 gives chi_G(K(4))=chi_G(E(4))-chi_G(A(4)). Thus the character in the statement equals

    [H0(A(2))-H0(K(4))] + H1(K(4)),

which is genuine by semisimplicity and the injection. There is no additional H0(A) error term. The same conclusion holds whenever the cubic kernel vanishes for another reason.

For this P source, the last block twists to W' O(-1), with Euler characteristic zero. The other contributions give

    chi_G(E(4))=P tensor Sym2 W +(W'+T) tensor W +V
              =(V+P+D)+(P+D+V+P)+V
              =3V+3P+2D.

This identity and the forced first W' occurrence are checked exactly by the accompanying character verifier.

## 6. Reproduction and open boundary

The checker authenticates all inputs, verifies the physical character orthogonality and tensor identities, all symmetric characters through degree7, the P-source quartic Euler character, and polynomial Euler exactness on both formal charts. It runs without assertions and gives identical output with Python optimization enabled. These are universal algebra controls supporting the written geometric proof; they do not prove the geometry by themselves.

No historical profile enumeration is rerun, and no actual source coefficient, parameter, point, jet, tensor, matrix, instance rank, or scan is selected or evaluated. No new live case count, actual profile closure, rank-four theorem, full-adjoint invertibility, smoothing, algebraicity, or complete original proof repair follows here. Applying the criterion to a complete current actual-source frontier remains separate work.
