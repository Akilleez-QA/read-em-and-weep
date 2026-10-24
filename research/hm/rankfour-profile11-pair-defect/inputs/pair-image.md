# The two decomposable top-four quotients have the same kernel and full positive endpoint image

## 1. Statement and precise actual setting

Work over C on the original physical line T=P(W*) with G=SL2(F5), its fixed determinant identification, and the constant connection on the original rank-thirty ambient H O. Retain the actual saturated inclusion E in H O, with rank E=17, degree E=-54, S=Q* of rank13 and degree -54. Suppose the actual derivative has generic rank four and maximal ordered profile (1,1). Set K=ker beta_E and A_q=E/K. Thus rank K=13 and the actual endpoint beta_K has rank at most three.

The preceding top-degree-four reduction leaves three necessary source-D forms. This theorem treats exactly two of them:

    A_q=F+O(-8),
    F=2O(4)+O(2),       or       F=O(4)+W O(3).        (1)

The third form A_std O(4)+O(-8) is outside this theorem. All original determinant defects are retained. Write A_std=Sym2 W, S4=Sym3 W, D=Sym4 W and T6=Sym5 W; V is the other three-space, W' the other doublet and P the even four-space. All representations are self-dual. The actual source is

    E=E_D=D(-2)+(W'+T6)(-3)+V(-4)+O(-8).              (2)

Then the actual kernel necessarily has the ordinary equivariant splitting

    K=S4(-3)+2V(-4)+W'(-5)+O(-10).                    (3)

More strongly, the ACTUAL endpoint derivative has image

    im beta_K = F(-2) inside A_q(-2)=F(-2)+O(-10),    (4)

as a sheaf equality, not just an equality of generic rank or saturation. Its negative O(-10) component is zero. Consequently

    rank K^-=10,       degree K^-=-60,
    K^+=E0=D(-2)+(W'+T6)(-3)+V(-4),
    rank E0=16,        degree E0=-46,
    E0^-=K,            generic rank beta_E0=3.        (5)

The adjacent graded derivative is an isomorphism

    K/K^- -> (E0/K)(-2).                             (6)

Only generic rank three is asserted for beta_E0 itself. No ordinary source or kernel splitting is assumed horizontal; no flat quotient connection is put on K/S4(-3). Neither (1) nor (3) is asserted realized, and neither configuration is excluded by this theorem.

## 2. Inputs and scope of verification

INPUTS.json retains complete originals with file identities. ACTUAL at db51525015bb7c5e825833d550d08dedf6f6ea96 gives the actual presentations and physical marking. PR1123 at 504b7eb800407dfc7e6340c98c72cdd553939f54 gives the four sources. PR1140 at 7a2488bcd36d95f79b5198001111b1a31fe5c3ba gives the cubic-kernel alternatives; in source D, H0(K(3)) is 0 or S4. PR1185 at236e0a3723c3d73ea7fb9e549376540a8e70508b supplies the actual endpoint construction and its retained geometric hypotheses. PR1194 at e4de44641a53b0b3424102cd5fbaf3cf5821996d supplies the preceding complete three-shape reduction, retained as inputs/top-four-reduction.md with SHA25656bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0. Its actual near-top coefficient injection is recalled and reproved where needed below.

The original actual-geometric/source premises remain imported, including saturation in the original rank-thirty constant ambient. The 54-dimensional coefficient presentation is not substituted for that inclusion. The proof uses neither a rank-three source ledger nor any later top-three image theorem: the earlier degree-three actual antecedent is already excluded and is not a live frontier.

The only arithmetic is fixed universal characters, an eight-dimensional genuine-cohomology atom table, and rank/degree arithmetic. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank, global bundle search, or historical enumeration is evaluated.

## 3. The same eight-dimensional tail budget forces the same kernel

Both forms in (1) have rank four and degree two, so rank K=13 and degree K=-56. Strict top for the actual derivative gives top K<=-3. Choose an ordinary equivariant Birkhoff splitting

    K=R3(-3)+R4(-4)+N,        top N<=-5.

This is not a connection-compatible splitting. Direct Euler-character calculation gives, for both forms,

    chi_G(K(3))=S4-W'-T6,
    chi_G(K(4))=A_std+2V,
    H0(A_q(1))=S4+2T6,
    H0(A_q(2))=D+2V+2P.                              (7)

For example, chi_G(E(3))=W'+2T6 and chi_G(E(4))=3V+3P+2D. In computing the quotient Euler characters, the O(-8) tail contributes minus S4 at twist three and minus A_std at twist four. It must not be discarded merely because it has no sections.

The positive S4 coefficient in the first Euler character of (7) forces R3 to contain S4. Since PR1140 permits only 0 or S4 in source D, necessarily R3=S4, and then

    H1(N(3))=W'+T6.                                  (8)

An irreducible block R(-j) in N contributes R tensor Sym^(j-5) W to (8), and has dimension (j-4)dim R<=8. Central parity is (-1)^j. The complete individual-block list inside this genuine budget is

    block          H1(block(3))       H1(block(4))
    W'(-5)         W'                 0
    T6(-5)         T6                 0
    V(-6)          T6                 V
    W'(-7)         T6                 P
    O(-10)         T6                 D
    P(-6)          W'+T6              P
    O(-12)         W'+T6              V+P.             (9)

This is a small irreducible atom calculation with its dimension bound proved first, not a kernel-bundle enumeration. All other parity-compatible irreducibles either exceed dimension eight or contribute W or S4, absent from (8). The exact decompositions of (8) are W'(-5) plus one of the four pure-T6 rows, or one of the last two rows.

Taking quartic Euler characters and using S4 tensor W=A_std+D yields

    R4=2V-D+H1(N(4)).                                (10)

For the six alternatives just described, H1(N(4)) is respectively 0,V,P,D,P,V+P. Only D makes (10) a genuine representation. Therefore N=W'(-5)+O(-10) and R4=2V, proving (3). No derivative-image claim is inferred solely from this character computation.

## 4. The actual top source row identifies one saturated Euler line

Let p:E->A_q be the actual quotient. Projection to its O(-8) summand receives only the displayed O(-8) source row, by degree, and surjectivity makes that scalar nonzero. Hence

    E0=ker(E -> A_q -> O(-8))
      =D(-2)+(W'+T6)(-3)+V(-4)

in the chosen source splitting, and restriction is an actual exact sequence

    0 -> K -> E0 -> F -> 0.                           (11)

This is elementary block cancellation in p, not a horizontal decomposition. Intrinsically E0 is the displayed kernel and is saturated in E and the constant ambient.

The top subbundle U=S4(-3) from (3) can project into E only through D(-2): every other source-row Hom is zero by degree or irreducible inequivalence. Moreover Hom_G(S4(-3),D(-2)) has dimension one, because D tensor W=S4+T6. Its image is therefore the canonical binary evaluation kernel

    0 -> S4(-3) -> D(-2) -> O(2) -> 0.                (12)

Since p kills U, the ACTUAL D-row factors through (12):

    D(-2) -> O(2) --j--> F.                           (13)

It is nonzero, since a zero D-row would place D(-2) in K and contradict strict top. The O(-8) component of this row is zero by degree.

For F=2O(4)+O(2), equivariance gives Hom_G(O(2),O(4))=0, so j is a nonzero scalar into the displayed O(2). For F=O(4)+W O(3), the O(4) component is again zero and Hom_G(O(2),W O(3)) is one-dimensional. It is the nonzero standard Euler injection. Thus in either case j is a saturated injection and its actual quotient is

    0 -> O(2) --j--> F -> R -> 0,
    R=2O(4).                                        (14)

For the second case, this uses 0->O(2)->W O(3)->O(4)->0 with the same fixed determinant identification. No independent parameter change or unproved equality of source connections is made.

## 5. The actual cubic kernel row fills that Euler line

The actual derivative of K factors through A_q(-2), because beta_E kills K. Its restriction to U has no O(-10) component by degree. The space Hom_G(S4(-3),F(-2)) is one-dimensional in each case: its section character is H0(F(1))=S4+2T6. The nonzero canonical map

    S4(-3) -> O -> F(-2),                            (15)

given by cubic evaluation followed by j(-2), spans this Hom space.

The ACTUAL beta_K restriction to U is nonzero. More precisely, the coefficient map H0(K(3))->H0(A_q(1)) is injective: a killed coefficient line O(-3) is a saturated direct line in K, and its derivative then lands in (K/line)(-2), of top degree at most -5. The Hom vanishes, making a negative saturated line horizontal in the original constant ambient, a contradiction in characteristic zero.

Hence the actual restriction is a nonzero scalar multiple of (15). Cubic evaluation is onto O everywhere, and j is saturated, so

    im(beta_K|U)=j(-2)O                              (16)

as an exact sheaf image. This identifies the same actual j from (13), up to its harmless nonzero scalar, not a second freely chosen graph direction.

## 6. The two quartic V rows fill the entire remaining positive quotient

The actual coefficient map on the R4=2V block is likewise injective:

    2V -> H0(A_q(2)).                                (17)

Indeed a killed coefficient line O(-4) is saturated in K, and its derivative would land in (K/line)(-2) of top degree at most -5. The same negative-horizontal contradiction proves (17). This concerns only the R4 coefficient space, not all of H0(K(4)).

Twist (14) by two. Since H1(O(4))=0, its section sequence is exact:

    0 -> D -> H0(F(2)) -> H0(R(2)) -> 0,
    H0(R(2))=2 Sym6 W=2V+2P.                         (18)

The first term D has no V, and (7) says the V multiplicity of H0(F(2)) is exactly two. Therefore composing (17) with the quotient in (18) is an isomorphism on the V multiplicity spaces. This is still the composition of ACTUAL derivative rows with the ACTUAL quotient by the line j; no quotient connection is introduced.

The corresponding bundle map is

    2V(-4) -> R(-2)=2O(2).                           (19)

Every Hom_G(V(-4),O(2)) is one-dimensional, corresponding to the unique V in Sym6 W=V+P. Let nu:V(-4)->O(2) be any nonzero such universal row. It is onto at every parameter. Indeed its common zero divisor is G-invariant and has degree at most six. Projectively the group is A5. A finite stabilizer of a point of P1 is cyclic; its possible orders in A5 are 1,2,3,5, so every orbit has size at least twelve. Thus a nonempty invariant effective divisor has degree at least twelve. The common zero divisor must be empty. This argument applies to all nonzero rows and selects no actual parameter or coefficient.

By the one-dimensional row Hom, (19) is nu tensored with the induced map of the two-dimensional multiplicity spaces. That multiplicity map is an isomorphism by (18). Consequently (19) is onto R(-2) everywhere.

The U row fills the kernel j(-2)O by (16), while the two V rows fill the quotient R(-2) by (19). Therefore the actual image of U+2V(-4) is exactly all of F(-2). Both these blocks have zero O(-10) component by degree.

## 7. Rank at the endpoint forces the complete image and the exact adjacent flag

The actual beta_K has generic rank at most three by maximal profile (1,1). Section 6 already puts the entire rank-three positive subbundle F(-2) in its actual sheaf image. If any remaining row had nonzero O(-10) component, its generic image together with F(-2) would have rank four. Hence the entire O(-10) component is zero. The image equals F(-2), proving (4), with no passage to a saturation needed.

Taking ranks and degrees in

    0 -> K^- -> K -> F(-2) -> 0

gives rank K^-=10 and degree K^-=-56-4=-60, since rank F=3 and degree F=10. The positive F is saturated in A_q=F+O(-8); its inverse image E0 in E is saturated in the original constant ambient. By (4) the actual forward transform K^+ is precisely this inverse image, proving the formula for E0 in (5). Its rank and degree are 16 and -46.

The same image equality says beta_E0 kills K. Conversely, after projecting H O/E0 onto H O/E=Q, the derivative beta_E0 on E0 becomes beta_E|E0. The latter factors through the surjection E0->F and the original coherent injection A_q->Q(-2), hence has generic rank three. Thus beta_E0 has generic rank at least three. Because K of rank thirteen is in its kernel and rank E0=16, its generic rank is at most three. It is exactly three, and its coherent kernel is K: the induced map from the bundle E0/K=F is generically injective and therefore has zero sheaf kernel on the smooth curve.

Finally, the quotient K/K^- is the actual image F(-2), while E0/K=F. This proves the actual graded isomorphism (6). It does not assert that the next derivative image of E0 is saturated or that the original rank-four determinant defect vanishes.

## 8. Contribution and unresolved part

For the two decomposable positive parts in (1), the proof determines the same necessary kernel and the full actual positive endpoint image, including every parameter. It also identifies the correct next rank-sixteen saturated bundle and its precise predecessor. These are structural actual-map conclusions, not only character necessities.

The triplet-positive quotient A_std(4)+O(-8) remains outside this result. The two configurations treated here are not excluded or asserted realized. No rank-seventeen rank-three theorem is transferred to E0, and no horizontal Birkhoff decomposition or descended flat connection is assumed. The original full rank-four profile, higher top degrees, square-surjectivity, full-adjoint invertibility, smoothing, algebraicity and original repair remain unresolved by this theorem.
