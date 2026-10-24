# Constant self-duality and actual maximal-isotropic top incidence

## Statement and exact conditional scope

Retain the full-positive triplet branch, original t=0, original local delta=12,
residual simultaneous rank-seven k=2 geometry, and remaining original kernel
K1, together with every complete transitive actual-geometric hypothesis of the
three direct originals in Section 1. Work over C on X=P(W*) for the physical
complex determinant-one representation W of G=SL2(F5). This is not a
representation in defining characteristic. Nothing below realizes or excludes
K1, changes the original local defect, or closes an entire profile.

Let S=Z direct-sum C7 be the actual constant eighteen-space, with dim Z=11 and
C7=A+P, where A=Sym^2 W and P is the even four-dimensional irreducible. Put
V=C7*. The actual constant projection of the original degree-eighteen dual
curve is y=(y_Z,y7):O(-18)->S* O. Define Q_r to be the saturation in V O of
its projected intrinsic jets of orders zero through r-1. In particular Q4
has rank four and means saturated THIRD-order jets, not fourth-order jets.
Let x_j be the actual complete order-j jet bundle of the projected original
degree-ten dual curve in Z* O. Let Bhat be the actual lifted rank-nine top,
and set L9=ann_S(Bhat) in S* O.

The new conclusions are:

1. There is a unique projective class of constant equivariant isomorphisms
   h:V->V* carrying y7 to its actual osculating dual line ann(Q6). Its
   associated bilinear form is symmetric and nondegenerate, and

       Q_r^perp=Q_(7-r), 1<=r<=6.

2. The actual constant projection induces an everywhere isomorphism

       L9/x4 -> Q4.

   Inside x5 direct-sum Q4, the quotient of L9 by x4 direct-sum Q3 is the
   graph of an everywhere isomorphism Q4/Q3 -> x5/x4 between degree-zero
   lines. Thus the exact constant-block intersections are

       L9 intersect (Z* O)=x4,   L9 intersect (V O)=Q3.

3. Let B_Z be the complete degree-ten apolar form line on Z*, and B_7 the
   seven-space form line from conclusion 1. Within B_Z direct-sum B_7 there
   is a unique line of block forms whose restriction to L9 vanishes. Every
   nonzero member is a constant invariant nondegenerate symmetric form on
   S*. Consequently L9, and the original Bhat under the dual form, are
   actually maximal isotropic.

4. Under its genuine constant-target embedding, the actual saturated
   third-order jet bundle Q4 has equivariant bundle type P(-6).

The two preparatory unpublished audits are not direct dependencies or
independent review of this proof. All new arguments, including the local
minor lemma, dual-curve construction, constant isomorphism, and rank-nine
graph and form construction, are proved here. No scalar ratio between form
blocks is chosen or evaluated. Uniqueness is asserted only within the two
specified form lines, not among all ambient invariant forms.

## 1. Complete direct originals and assertion provenance

The complete direct originals are:

- PR1239 at 360b7e8f55b05ca5740a10cb3ed844a594766f70,
  research/hm/rankfour-profile11-triplet-stationary-section-kernel/PROOF.md,
  retained as inputs/stationary-section-kernel.md; complete SHA256
  7835e0a0e6769163dca0ad2ed0a62e3c79a491dc6ebc39e5f8c988d9a9ec6de2.
- PR1238 at d259230fbf7259e52db267c56203a29f221da5f0,
  research/hm/rankfour-profile11-triplet-seven-space-ramification/PROOF.md,
  retained as inputs/seven-space-ramification.md; complete SHA256
  25388c411411f7304afc2dc7ad6695af5a931e852ba138c45cfb7a6f708d84e3.
- PR1236 at 092fc5f31dfaa5553ee5ea687f175ecba1878a2a,
  research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md,
  retained as inputs/first-kernel-forward-closure.md; complete SHA256
  90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137.

All three entire originals were freshly fetched through read-only connector
calls at these immutable commits, without line-range limits. Their complete
UTF8 bytes equal the complete originals read for this proof. INPUTS.json
records their exact byte lengths, SHA256 hashes, Git blobs, and immutable
URLs. Full connector responses are retained only in LOCAL-SOURCE-FETCHES.json,
excluded from publication and selected-only replay. No excerpt or audit
substitutes for an entire direct original. All complete transitive
actual-geometric hypotheses remain assumptions of this conditional theorem.

The stationary-section-kernel theorem supplies the fixed universal statement
that the unique G-invariant seven-dimensional subsystem of
H18=H0(X,O(18)) of type A+P, projectively stationary to first order along the
full reduced D12, is the canonical stationary kernel Lambda0=ker(tau).
It also supplies the fixed character facts that A,P,D=Sym^4 W are distinct
self-dual irreducibles. Only this seven-space uniqueness and these fixed
representation facts are used; its additional fifteen-space coefficient
kernel conclusion is not an extra premise needed here.

The seven-space-ramification theorem supplies the actual constant splitting
S=Z direct-sum C7, C7=A+P, and the following actual data:

    y7:L=O(-18) -> V O is saturated and has coefficient span V;
    a=(0,2,3,4,5,6,8) along D12;
    a=(0,1,2,3,4,5,6) off D12;
    Q2 is the actual projected first-jet saturation, of type W'(-11);
    x_j=Sym^j W(j-10), rank x_j=j+1, for 0<=j<=10;
    x_j/x_(j-1)=O(2j-10), with x_(-1)=0;
    y_Z factors through x2, and a_Z:L->x2/x1=O(-6) is nonzero;
    the divisor of a_Z is exactly D12;
    R17=ann_S(x0), and y annihilates R15.

All displayed maps from L are equivariant for its standard linearization.
The complete x0 curve is the projected ORIGINAL degree-ten dual curve;
y is the projected ORIGINAL degree-eighteen dual curve. Neither denotes
an auxiliary primal curve.

The first-kernel-forward-closure theorem supplies the actual forward chain

    Bhat -> R11 -> R13 -> R15 -> R17 -> S O,
    ranks: 9, 11, 13, 15, 17, 18,
    degrees: -54, -52, -46, -36, -10, 0,
    Bhat has equivariant type (D+P)(-6).

Each forward arrow is the saturated span of actual derivatives in the same
constant ambient. These assertions are also compatible with the later
seven-space theorem, but the complete original is retained directly because
the proof uses all stages back to Bhat, not merely its terminal ranks.
The group G has no nontrivial one-dimensional complex characters, as retained
in the complete inputs; hence line bundles of a fixed degree have no hidden
character ambiguity in their indicated equivariant structures.

## 2. Universal jet-minor and saturation lemma

Consider any basepoint-free, linearly nondegenerate characteristic-zero curve
in a constant (n+1)-space. At an arbitrary formal DVR its scalar system has
vanishing sequence 0=a_0<a_1<...<a_n. An adapted constant basis of that scalar
system has formal representatives

    f_i=t^(a_i)(u_i+O(t)), u_i nonzero.

This is a lemma about all filtered scalar systems. It does not select or
evaluate a coefficient, parameter, point, or jet of the actual source.
For k+1 distinct indices i_0,...,i_k, the determinant of derivatives of orders
0,...,k has exact order

    sum_j a_(i_j)-k(k+1)/2.                         (2.1)

Its leading coefficient is a nonzero product of the u_(i_j) and the
Vandermonde product of the distinct integers a_(i_j). Indeed the derivative
coefficients are falling factorial polynomials (x)_r, monic of degree r, so
their determinant is the Vandermonde determinant. Factoring in Laurent
series accommodates zero falling factorial entries when an a_i is smaller
than a derivative order. The final determinant order is nonnegative because
k+1 distinct nonnegative integers have sum at least k(k+1)/2. Higher formal
terms cannot decrease this order, and its displayed leading coefficient
cannot cancel.

The minimum valuation of all maximal minors of the order-k jet map is
therefore

    delta_k=sum_(i=0)^k(a_i-i).                     (2.2)

Smith normal form over a DVR identifies this valuation with the length of
the saturated image modulo the coherent image. Thus (2.2) proves the actual
saturation deficit; saturation is not presumed. Coordinate changes and
changes of the source-line frame act by invertible triangular changes on
jets, so the conclusion is intrinsic. The same determinant with k=n proves
generic independence of all n+1 derivatives of an independent scalar system.
No inverse of a moving map is differentiated or used for this span statement.

## 3. The complete saturated seven-space flag and the dual line

Apply Section 2 to y7, and write

    J_k=P_X^k(O(18))*.

The actual jet map J_(r-1)->V O has saturated image Q_r of rank r, for
1<=r<=7. These are nested equivariant saturated subbundles; Q1=y7(L) and
Q7=V O. The principal-parts filtration gives

    deg J_k=-(k+1)18+k(k+1).

At each point of D12 formula (2.2) has values 0,1,2,3,4,5,7 for k=0,...,6,
and it is zero off D12. Consequently

    r                  1    2    3    4    5    6    7
    deg J_(r-1)      -18  -34  -48  -60  -70  -78  -84
    local deficit      0    1    2    3    4    5    7
    deg Q_r          -18  -22  -24  -24  -22  -18    0.                  (3.1)

The degree increases by the length of the saturation quotient, explaining
the sign. The last row recovers the full Wronskian divisor 7D12 and the
rank-two row recovers the degree of the already known Q2.

Since Q6 is saturated, M=(V O)/Q6 is a line bundle of degree 18. The actual
annihilator line is

    L_dual=M*=ann(Q6) -> V* O, deg L_dual=-18.       (3.2)

Its quotient is Q6*, so this line is saturated. In particular the dual curve
has no basepoints; this was not inferred from differentiating or projecting
a previously saturated curve.

## 4. The osculating dual has the reflected sequence and full span

Continue the universal local lemma with n=6. The signed cofactors of the
six derivative rows of orders zero through five generate their annihilator
over the fraction field. The cofactor omitting component i has exact order

    sum_(j != i) a_j-15.

The minimum, attained at i=6, is sum_(j=0)^5 a_j-15. Dividing by their common
local factor gives a primitive generator of the saturated annihilator line.
Its scalar components have distinct orders a_6-a_i, for 0<=i<=6. Distinct
orders imply independence over C: a nonzero constant combination has the
smallest order among its nonzero summands. They also determine all possible
orders in their span. Hence the exact dual vanishing sequence is

    b_i=a_6-a_(6-i), 0<=i<=6.                       (4.1)

This cofactor argument proves full dual coefficient span V* as well as the
sequence; neither is assumed. Primitive common-factor removal is the local
saturation operation, not a choice of global scalar normalization.
Both supplied sequences are fixed by (4.1). The dual is therefore stationary
to first order along the entire D12 and ordinary off D12.

An independent constant-pairing check of full span is available without any
moving inverse. On the generic locus, let v,z be arbitrary local frames of
the original and annihilator lines. Put c=<z,v^(6)>. Generic independence
of v,...,v^(6) makes c nonzero. Differentiating <z,v^(j)>=0 for 0<=j<=5 gives

    <z^(i),v^(j)>=0 if i+j<=5,
    <z^(i),v^(6-i)>=(-1)^i c for 0<=i<=6.           (4.2)

Induction follows by differentiating the previous zero identity. The pairing
array is anti-triangular with nonzero anti-diagonal; thus z,...,z^(6) are
independent. A constant subspace containing z contains these derivatives,
so it is all of V*. These are universal identities of arbitrary local
frames, not evaluations of an actual frame, point, or jet. The same relations
also show that the bidual line equals the original line generically, hence
everywhere after saturation.

## 5. Stationary uniqueness yields a directed constant self-duality

All constructions in (3.2) are equivariant. The underlying line bundle
L_dual is O(-18). The center acts trivially on the even constant space V*,
and the absence of characters gives the standard equivariant linearization
on L_dual. Thus the isomorphism line Isom_G(L,L_dual) is nonempty, and no
representative in it needs to be fixed or evaluated.

For any theta:L->L_dual in that isomorphism line, write z_theta for its
composite into V* O. The scalar coefficient maps have directions

    alpha:V* -> H18, alpha=y7*,
    beta_theta:V -> H18, beta_theta=z_theta*.

They are both injective by the two full-span proofs. Their images are
invariant seven-dimensional systems of type A+P. Both are first-order
stationary along D12. The complete stationary-section-kernel theorem gives

    im alpha=Lambda0=im beta_theta.                 (5.1)

The inverse of alpha onto its image is a map of FIXED constant vector
spaces. Define, using canonical double-dual identifications only,

    h_theta=(alpha^(-1) beta_theta)*:V -> V*.        (5.2)

This is a constant equivariant isomorphism. Its direction is checked by
transposing the desired identity:

    (h_theta y7)*=alpha h_theta*=beta_theta.

Therefore h_theta y7=z_theta. Varying theta scales h_theta by the same
constant, giving a projective class [h]. Any other constant isomorphism
carrying the full curve to this same dual line induces an automorphism of
L, hence a nonzero constant scalar; full coefficient span then forces the
same scalar multiple of h. Thus this projective class is unique. No equality
of section images has been silently converted into an ambient identification.

The irreducible A is orthogonal: the square of the determinant contraction
on W gives its nondegenerate invariant symmetric form. The irreducible P is
the reduced five-letter permutation representation; restriction of the
sum-of-products form to the coordinate-sum-zero subspace is nondegenerate
and symmetric. This verifies orthogonality by fixed representation theory,
not an actual coefficient computation. Their duals are orthogonal as well.
Since V=A* direct-sum P* is multiplicity-free, Schur's lemma kills cross
blocks and makes every equivariant map V->V* a sum of scalar multiples of
these symmetric forms. In particular h is symmetric and is nondegenerate
because (5.2) is an isomorphism. Let B_7 be the resulting form line.

## 6. Self-duality of every actual saturated jet flag

For any nonzero b_7 in B_7 the primary identity is the intrinsic zero pairing

    b_7:Q1 tensor Q6 -> O_X.

In arbitrary local frames this says b_7(v,v^(j))=0 for 0<=j<=5. Differentiating
these identities, with the bilinear form constant, and inducting on the
first derivative index gives

    b_7(v^(i),v^(j))=0 whenever i+j<=5.            (6.1)

For example, differentiating the already zero pairing with indices
(i-1,j) gives the claim from the zero pairing with indices (i-1,j+1).
The needed total order never exceeds five. Triangular coordinate and frame
changes preserve these zero conditions, so they are intrinsic.

The ordinary jets span the Q_r generically. Equation (6.1) therefore gives
b_7(Q_r,Q_s)=0 for r+s<=7 as a bundle morphism: a generically zero morphism
between vector bundles is zero everywhere. It follows that

    Q_(7-r) subset Q_r^perp.

The two sides have equal ranks and are saturated in V O. Two saturated
subbundles of the same constant ambient that have the same generic fiber
are equal, since each is the intersection of that ambient lattice with its
generic subspace. Thus

    Q_r^perp=Q_(7-r), 1<=r<=6.                      (6.2)

In particular Q3 is maximally isotropic, and Q4=Q3^perp. The radical of the
restriction to Q4 is Q3. It induces a nondegenerate symmetric line form on

    U7=Q4/Q3=O(0),                                 (6.3)

because the two degrees in (3.1) are both -24. The linearization is the
standard one, by the no-character statement. This includes the saturated
fibers over D12; no claim of full ordinary jet rank there is made.

## 7. Actual forward annihilators and the saturated rank-four projection

Set L9=ann_S(Bhat). It is saturated in S* O, has rank nine, and degree -54.
Indeed it is the dual of S O/Bhat, whose degree is 54.
For actual bundles in a constant ambient, if a curve annihilates E^+,
differentiating the zero pairing with local sections of E shows that its
first jets annihilate E. Iterating this elementary rule along the actual
forward chain yields

    x0 annihilates R17,
    x1 annihilates R15,
    x2 annihilates R13,
    x3 annihilates R11,
    x4 annihilates Bhat.

Since y annihilates R15, its intrinsic jets through order three also
annihilate Bhat. There is an actual map

    x4 direct-sum J_3 -> L9.                        (7.1)

Its seven-space projection on J_3 is the third-order jet map of y7 because
the projection is constant. Those four jets are generically independent
by Section 2. The five-dimensional x4 lies entirely in Z*, so (7.1) has
generic rank nine and generically spans L9. Its coherent image need not be
saturated and is not declared equal to L9.

The constant projection L9->V O has generic kernel x4. The latter is
saturated in the whole ambient S* O, hence also in L9. Thus E=L9/x4 is a
vector bundle of rank four, and its induced map E->V O is a sheaf injection.
Its generic image is Q4. The composite to the locally free quotient
(V O)/Q4 is generically zero and hence zero, so it factors through Q4.
The degrees are

    deg x4=5(4-10)=-30,
    deg E=-54-(-30)=-24=deg Q4.

The resulting generic isomorphism E->Q4 has a nonzero determinant of degree
zero, so its determinant never vanishes. Consequently the ACTUAL projection
is an everywhere equivariant isomorphism

    L9/x4 -> Q4.                                  (7.2)

This proves saturation after projection by equal degree; it does not assume
that saturation survives projection.

## 8. The actual top graph and its nonzero quotient-line map

Because y_Z lies in x2, its derivatives through order k lie in x_(k+2).
This follows directly by differentiating arbitrary local expressions in
the actual complete osculating flag, whose derivative raises its index by
at most one. In particular the Z* component of J_3 lies in x5.
The generic generators in (7.1) therefore lie in x5 direct-sum Q4. That is
a saturated subbundle of S* O, so all of L9 lies in it.

Modulo x4, equation (7.2) identifies the actual image of L9 with a graph

    graph(g) subset UZ direct-sum Q4,
    g:Q4 -> UZ=x5/x4=O(0).                         (8.1)

This is an ordinary description of an embedded bundle by an isomorphism;
its inverse is never differentiated. The Z* components of jets through
order two lie in x4. Hence g kills the generic image of J_2, and thus kills
all of Q3, since their generic span is Q3. It descends to a line map

    g_bar:U7=Q4/Q3 -> UZ.                           (8.2)

We prove that this map is nonzero using the ACTUAL quotient row

    a_Z:L -> x2/x1=O(-6)

from the direct original. For every 0<=j<=9, the second fundamental form
of the complete degree-ten flag induces a morphism

    sigma_j:x_j/x_(j-1) -> (x_(j+1)/x_j) tensor Omega_X.                (8.3)

It is well-defined because derivatives of x_(j-1) lie in x_j. The source
and target are line bundles of the same degree 2j-10. Completeness gives
independence of successive complete jets, so sigma_j is generically
nonzero, hence an everywhere isomorphism. This is a symbol map induced
by actual constant-ambient differentiation, not a connection on a quotient.

The principal-parts filtration has

    0 -> J_2 -> J_3 -> L tensor T_X^3 -> 0,
    L tensor T_X^3=O(-12).

The Z* component of J_3 followed by x5->UZ kills J_2. Its top-quotient map
is, up to the nonzero universal factorial in the chosen principal-parts
symbol convention, the composite

    L tensor T_X^3 --a_Z tensor 1--> (x2/x1) tensor T_X^3
        --sigma_2, sigma_3, sigma_4--> x5/x4=UZ.     (8.4)

Each sigma in this display is untwisted once by T_X. Thus the last three
arrows are isomorphisms, and (8.4) is nonzero with divisor exactly D12.
Only its nonvanishing and divisor are needed; no scalar representative or
normalization is chosen.

For clarity, the symbol identity can also be verified for arbitrary local
lifts by the universal Leibniz rule. Write a local section of y_Z as
u0 v+u1 v'+u2 v'', where v is any local lift of the complete curve. Its
third derivative modulo x4 is u2 v^(5): any derivative falling on u2,
or any term starting below v'', has derivative order at most four.
This proves the associated-graded statement (8.4) and involves no evaluation
of actual u_i, v, their derivatives, or any selected point. It does not
assume that a derivative of f12 is nonzero.

The seven-space component likewise gives a top-quotient map

    s:L tensor T_X^3 -> U7,

which is generically nonzero because the generic third-order jets have
rank four whereas the second-order jets have rank three. The graph identity
(8.1) gives g_bar s equal to (8.4), with the same intrinsic symbol convention.
Its right-hand side is nonzero, so g_bar is nonzero. Both U7 and UZ have
degree zero, making g_bar an everywhere equivariant isomorphism.

Finally, for every local section q of Q3 the graph contains (0,q) modulo
x4. A lift in L9 has Z* component in x4; subtracting that component, which
already lies in L9, shows that the actual pure seven-space Q3 lies in L9.
Thus

    L9/(x4 direct-sum Q3)
       =graph(g_bar) subset UZ direct-sum U7.       (8.5)

This equality is everywhere. The map to Q4 has kernel x4, and the graph's
intersection with the pure U7 line is zero because g_bar is an isomorphism.
Consequently

    L9 intersect (Z* O)=x4,
    L9 intersect (V O)=Q3.                         (8.6)

These are identities of actual embedded saturated bundles, not merely
identities of abstract types or generic subspaces.

## 9. The two form lines and the intrinsic graph restriction

Completeness of x0 gives a fixed coefficient-space isomorphism with the
complete degree-ten scalar system. Transport the universal binary apolar
pairing through that CONSTANT isomorphism. Its determinant-contraction
formula defines the line B_Z of nondegenerate invariant symmetric forms
on Z*. Symmetry follows from degree ten being even. No actual coefficient
tensor or normalization is selected.

The pairing of two degree-ten Veronese lifts is the tenth power of the
determinant of their binary arguments. It vanishes to order ten along the
diagonal. Differentiating this universal identity in the two factors gives

    b_Z(x_i,x_j)=0 when i+j<=9.                     (9.1)

This fixed identity implies x4^perp=x5: inclusion follows generically and
saturation gives equality. It also implies x5^perp=x4. Therefore the radical
of b_Z restricted to x5 is exactly x4, and every nonzero form in B_Z induces
a nondegenerate symmetric line form on UZ=x5/x4.

From Section 6 the analogous radical on Q4 for a nonzero b_7 in B_7 is Q3,
and the quotient form on U7 is nondegenerate. Thus x4 direct-sum Q3 is the
common kernel of the two block-form pairings on x5 direct-sum Q4, where
"common kernel" means vectors paired to zero by both forms. Any block form
with two nonzero components has radical exactly x4 direct-sum Q3 on this
bundle. Both forms consequently descend to UZ direct-sum U7.

Restrict these descended forms to the actual graph (8.5), identified with
U7 by its second projection. The resulting linear map is

    rho:B_Z direct-sum B_7 -> H0(X,(U7*)^tensor2)^G,
    rho(b_Z,b_7)=g_bar* b_Z + b_7.                 (9.2)

Here the forms on the right mean their just-constructed quotient-line
forms, and g_bar* denotes pullback in both factors. This notation does
not identify either quotient line with a chosen constant basis. Since
U7 is equivariantly O(0), the target of (9.2) is one-dimensional. Restriction
from B_7 is nonzero by its quotient nondegeneracy. Restriction from B_Z is
nonzero by its quotient nondegeneracy and the isomorphism g_bar. Thus
ker rho is one-dimensional and meets neither coordinate form line
nontrivially.

Every nonzero member of ker rho consequently has nonzero components on
both constant blocks Z* and V. Both block forms are nondegenerate, so their
block-diagonal sum b_S on S*=Z* direct-sum V is nondegenerate, symmetric,
and invariant. Its restriction to L9 vanishes: the common radical
x4 direct-sum Q3 has already been removed, and (9.2) makes the remaining
graph line isotropic. This accounts for ALL actual generators and saturated
fibers, not only a single local top norm. No degree-24 invariant-space or
coordinate-dependent third-derivative norm is required.

Since rank L9=9 and dim S=18, isotropy and nondegeneracy imply

    L9=L9^perp.                                   (9.3)

The kernel line in (9.2) is the unique line with this property within
B_Z direct-sum B_7. There is no assertion about possible other invariant
forms on S*, including additional block or cross-block forms, and no
scalar ratio of the specified two blocks has been evaluated.

## 10. The original top and the actual P-type third-order jet quotient

Let h_S:S*->S be the constant equivariant isomorphism of any nonzero b_S
constructed above. Equation (9.3) gives

    h_S(L9) subset ann_S(L9)=Bhat.

Both sides are saturated of the same rank in S O, so they are equal.
Equivalently, the dual form on S makes the original actual Bhat maximal
isotropic. In particular the equivariant type of L9 is now (D+P)(-6),
not merely a rank-and-degree candidate.

The actual x4 has type Sym^4 W(-6)=D(-6). Under an equivariant bundle
identification L9 isomorphic to (D+P)(-6), its inclusion is a constant
intertwiner D->D+P because H0(O_X)=C. It is nonzero and injective. The
fixed irreducibles D and P are nonisomorphic, so Schur's lemma identifies
its image with the complete D summand. The genuine quotient in (7.2)
therefore has type

    Q4 isomorphic to P(-6).                        (10.1)

This conclusion uses the actual inclusion, actual constant projection,
and actual form isomorphism before taking representation types. It does
not make an abstract splitting horizontal or differentiate one. No further
equivariant classification of Q3 is needed or claimed.

## 11. Verification boundary and contribution

The new result is one chain of necessary actual compatibilities: stationary
uniqueness identifies the original seven-space curve with its actual
osculating dual by a directed constant map; its orthogonal flag then makes
the actual rank-nine top a diagonal graph between two nondegenerate
quotient-line forms; the resulting block form forces actual maximal
isotropy and the precise P(-6) type of the saturated THIRD-order jet bundle.
The degree comparison in (7.2) and the nonzero three-symbol composite in
(8.4) are essential bridges, not presumed projection or saturation facts.

Bounded checks concern only the displayed formal degree and deficit table,
reflection of the two prescribed integer sequences, fixed representation
identities, and the line-degree and dimension arithmetic. They do not
certify any actual source instance. Normal and optimized Python must run
the same explicit runtime checks. The cofactor and constant-pairing proofs
provide independent structural checks of full dual span, not computations
of actual coefficients.

No selected actual coefficient, source parameter, orbit point, eigenline,
jet, tensor, matrix, scalar ratio, normalization, or instance rank is chosen
or evaluated. There is no broad scan, large computation, local Codex use,
quotient connection, derivative of a moving inverse, horizontal Birkhoff
splitting, or silent saturation replacement. Only constant-ambient actual
pairings and universal formal identities are differentiated.

This theorem is conditional on all complete direct and transitive inputs.
It makes no occurrence or exclusion claim for K1, no higher-order matching
of separately proposed branches, and no algebraicity assertion. Exact
algebraic identities of the given actual bundles do not establish
algebraicity of a separate formal deformation. An independent review of
this entire proof and all three complete freshly authenticated immutable
direct originals is required before publication. Neither preparatory
audit nor author self-review substitutes for that review.
