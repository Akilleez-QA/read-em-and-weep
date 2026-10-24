# Both actual lower gluing rows are nonzero, and the gluing kernel has type H_6(-4)

## Statement, conditional scope, and publication boundary

Retain the full-positive triplet branch, original t=0, original local
delta=12, residual simultaneous rank-seven k=2 geometry, remaining original
kernel K1, and every complete transitive actual-geometric hypothesis of the
four direct originals in Section 1. Work over C on X=P(W*) for the physical
determinant-one representation W of G=SL2(F5). Write V=V_alt throughout;
V is not the seven-space denoted V in the PR1240 original.

The actual quotient gluing row supplied by PR1243 is everywhere onto:

    h:(W'+T6)(-3) -> O(4).

We prove that both its W' and T6 components are nonzero. Consequently the
actual kernel G7=ker(f:E0->F10) has equivariant bundle type

    G7 isomorphic to H_6(-4)=(V_alt+P)(-4).

The actual quotient maps canonically identify G7 with ker(g:F18->Q) and
with ker h. These are isomorphisms between kernels in different ambients,
not literal equality of their embeddings. No identification of G7 with
the same-typed top of K1 is asserted.

The necessary intermediate lemma identifies the rank-five saturated
FOURTH-order jet bundle Q5 of the projected seven-space curve y7, and the
actual intersection with the constant seven-space:

    Q5 isomorphic to V(-4)+W'(-5),
    R13 intersect (C7 O)=b7(Q5),
    b7:C7* -> C7.

Here b7 belongs to the already established constant nondegenerate form
line. Q5 is not the fourth-order jet bundle of the original curve in its
full degree-eighteen ambient, nor of an auxiliary curve. Its definition
uses the actual constant seven-space projection and saturation there.

This is a focused unpublished packet, frozen for a NEW independent review
of the entire proof and all four complete direct originals. The preparatory
draft, preparatory audit, author verification, and bounded checker do not
replace that review. The checker authenticates bytes and checks only fixed
small character and degree identities; it does not prove geometry or test
actual maps. No branch closure, full ten-dimensional constant-span claim,
new derivative-fullness claim, higher-order matching, realization, exclusion
of K1, or algebraicity statement follows here.

## 1. Four complete immutable direct originals and imported actual data

All four sources are in Akilleez-QA/read-em-and-weep. Each complete proof
was freshly fetched by an exact-commit read-only GitHub fetch_file request
without line limits and a separate fetch_blob request. Decoded path bytes,
blob bytes, and the retained UTF-8 bytes agree exactly. SHA256 and Git blob
identifiers were recomputed from those full bytes. All four entire originals
were read. INPUTS.json records exact requests, UTC timestamps, URLs, lengths,
hashes, and assertion provenance; INPUTS.md and PROVENANCE.md explain their use.

- A, PR1242, commit 66ef0616fdd0607272b8bbd23892bc33120ac7f2:
  research/hm/rankfour-profile11-triplet-r13-extension-incidence/PROOF.md;
  retained as inputs/r13-extension-incidence.md; 19,230 bytes;
  SHA256 4819cebda47b3ef7a48ecbcb1fe01295a3a3a7ea7986df540421e1433d547b21;
  Git blob 5ac2f53aec71adda224d3578fb6e871ac6a8fecb.
- B, PR1243, commit dde84900cd6f9ad117800c39042844bb897a2f79:
  research/hm/rankfour-profile11-triplet-f18-gluing-surjectivity/PROOF.md;
  retained as inputs/f18-gluing-surjectivity.md; 12,798 bytes;
  SHA256 3919909cd67055e266299a0841e4642c465185eba28500a3b00b4a284f93693a;
  Git blob 700257a6d8f41f9cfbae7fdf8d78d77795a07bb9.
- C, PR1240, commit 3fbaa182b1aceb6915be88088ef158d6d15e34fb:
  research/hm/rankfour-profile11-triplet-orthogonal-top-incidence/PROOF.md;
  retained as inputs/orthogonal-top-incidence.md; 28,094 bytes;
  SHA256 407d35049bb17ab4b8f4e270627adb416fc5601eab1445a21685f2cc27bcb637;
  Git blob f00b059695615d9b8ab6d315798940e3ab0a58d4.
- D, PR1236, commit 092fc5f31dfaa5553ee5ea687f175ecba1878a2a:
  research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md;
  retained as inputs/first-kernel-forward-closure.md; 18,052 bytes;
  SHA256 90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137;
  Git blob f77cfb52743be86e46e0c40570ec036e69aebaf3.

Historical publication-status wording inside these retained originals is
preserved unchanged. Their earlier dependencies are transitive assumptions,
not additional freshly authenticated direct sources. In particular no fifth
source is needed for P tensor W: it is derived below from identities in A
and B. Neither preparatory text is a mathematical premise of this proof.

Put H_n=H^0(X,O(n))=Sym^n W for n>=0. Superscripts H^i always denote
sheaf cohomology and are not symmetric-power indices. Serre duality gives
H^1(O(-n-2))=H_n* with the retained determinant convention. Fixed
representation types are self-dual where used; this does not choose a
pairing or a representative of any actual scalar-map line. The fixed
low-degree identities retained in A and B are

    H_0=1, H_1=W, H_2=A, H_3=S4, H_4=D, H_5=T6,
    H_6=V+P, H_7=W'+T6,
    D tensor W=S4+T6,
    T6 tensor W=D+V+P,
    W' tensor W=P,
    W' tensor H_3=D+V.

The displayed named irreducibles are distinct, with dimensions indicated
by their subscripts or by dim W=dim W'=2, dim A=dim V=3, dim P=4.
There are no nontrivial one-dimensional characters. Every nonempty
invariant effective divisor has degree at least twelve. In particular A
first occurs in H_2 and W' first occurs in H_7.

A supplies the actual E0 and its canonical subbundles

    E0=D(-2)+(W'+T6)(-3)+V(-4),
    D0=D(-2), N=W'(-3),
    R13=E0 intersect (S O),
    R13 isomorphic to T6(-3)+(V+P)(-4), R13^+=R15.

Here plus denotes saturated forward span in the original constant ambient
C O, dim C=21. D0 is the maximal-degree top. N is the unique nonzero
W'(-3) image in E0, not a freely chosen splitting summand: its other
possible components vanish by Hom_G(W',D tensor W)=0,
Hom_G(W',T6)=0, and ordinary degree. The canonical top of R13 has type
T6(-3). D supplies the actual second fundamental form beta_E0 whose
coherent image is saturated of type A(4). B supplies its actual kernel

    K=K1=(V+P)(-4)+T6(-5).

B supplies the actual commutative diagram with exact rows

    0 -> T=V(-4) -> E0  -> F18 -> 0
           |         |f      |g
    0 -> T=V(-4) -> F10 -> Q   -> 0,

where the left vertical arrow is an isomorphism onto the same actual T
subbundle of F10. Here

    F18=D(-2)+(W'+T6)(-3), F10=(P+D)(-2), Q=T6(-1).

Both f and g are everywhere onto. The map f is induced by the actual
constant restriction p10:C->V10*, where the original degree-ten scalar
curve spans V10 in C*. Its constant kernel M10 has type A+V+P. The actual
D0 row maps isomorphically onto a saturated D_Q=D(-2) in Q, and Q/D_Q=O(4).
It induces the actual onto quotient row

    h:F18/D0=(W'+T6)(-3) -> Q/D_Q=O(4).          (1.1)

The quotient E0->F18 restricts to a canonical isomorphism ker f->ker g:
the diagram's map on T is an isomorphism. Likewise F18->F18/D0 restricts
to an isomorphism ker g->ker h because g|D0 is an isomorphism onto D_Q.
The reverse identification uses the unique D0 correction of a lift; it
introduces no horizontal splitting and is never differentiated.

C supplies the actual constant splitting S=Z direct-sum C7 with C7=A+P,
dim Z=11. The original degree-ten curve restricted to S* is complete in
Z*, and has actual complete osculating flag x_j of rank j+1; x2 annihilates
R13. The restriction y=(y_Z,y7):O(-18)->S* O of the original degree-eighteen
dual curve annihilates R15. In C7* O, Q_r is the saturated image of the
intrinsic jets of y7 of orders zero through r-1. Thus Q2 is the rank-two
first-jet saturation, Q4 is the rank-four third-order jet saturation, and
Q5 is the rank-five fourth-order jet saturation. C proves

    Q4 isomorphic to P(-6), deg Q5=-22,
    Q5/Q4=O(2), Q2^perp=Q5.                     (1.2)

The last equality uses C's constant nondegenerate symmetric form line on
C7*. As a directed isomorphism a nonzero member is b7:C7*->C7. We never
equate bundles in these opposite ambients without applying this map.

## 2. The actual W' row of h cannot vanish

The map E0->F18 carries N isomorphically onto its canonical W'(-3)
subbundle. It cannot kill N because its kernel is T=V(-4) and Hom(N,T)=0.
Its components in D(-2) and T6(-3) vanish by the fixed identities above,
so its only nonzero component is the W' coefficient isomorphism. Passing
to F18/D0 preserves it. These are properties of the actual quotient map,
not a choice of splitting normalization.

The restriction beta_E0|N is nonzero: otherwise N would map into K, whereas
Hom(N,K)=0 by ordinary degree. Its generic rank is two. To see this, suppose
its nonzero coherent image had rank one and saturate that image in the
actual saturated target A(4). The saturation is an equivariant line O(a),
with standard linearization because there are no characters. A nonzero
inclusion O(a)->A(4) requires A in H_(4-a), hence a<=2. The nonzero map
N=W'(-3)->O(a) requires W' in H_(a+3), hence a>=4. These inequalities are
incompatible. The coherent image and its saturation are distinguished here;
only their common generic rank is used.

Now suppose h's W' row is zero. The actual map N->Q then lands in D_Q.
But Hom_G(N,D_Q)=Hom_G(W',D tensor W)=0, so this map is zero. In the actual
diagram N->F10 therefore factors through T and is zero by ordinary degree.
Thus N lies in the constant bundle M10 O.

For precision, the constant coefficient map of this inclusion has direction

    M10* -> H^0(N*).

Its dual H^0(N*)*->M10 has image equal to the constant coefficient span of
N. The representation type H^0(N*)=(W')* tensor H_3 is D+V; its dual has
the same type, without choosing a duality. Since M10=A+V+P is
multiplicity-free, this actual coefficient span lies in the constant
V-isotypic three-space of M10. Derivatives of sections of N stay in this
same constant three-space. Its intersection with E0 already contains the
rank-two N, so those derivatives modulo E0 have generic rank at most one.
This contradicts the generic rank two of beta_E0|N. We conclude

    h|W'(-3) is nonzero.                          (2.1)

## 3. The actual rank-five projected jet bundle Q5

The saturated inclusion Q4 in Q5 and (1.2) give the actual extension

    0 -> P(-6) -> Q5 -> O(2) -> 0.               (3.1)

Its class e is nonzero: an equivariant splitting would put a positive-degree
line O(2) in the constant bundle C7* O, impossible. The equivariant Ext
space is

    Ext^1_G(O(2),P(-6))=(P tensor H^1(O(-8)))^G,

and has dimension one, since H^1(O(-8))=H_6* and H_6=V+P contains P once.
Serre duality identifies e, without choosing a self-duality of P, with a
nonzero invariant functional

    e_tilde:P* tensor H_6 -> C.                  (3.2)

After twisting (3.1) by three, the connecting map is

    delta_e:H_5 -> P tensor H^1(O(-3)).          (3.3)

Its complete Serre-dual identity is

    <delta_e(s), lambda tensor t>
       = e_tilde(lambda tensor (t s)),
    s in H_5, lambda in P*, t in H_1.            (3.4)

The left pairing is the natural perfect pairing with
P* tensor H_1, using H^1(O(-3))=H_1*. A compatible Serre-duality convention
is understood; changing it by an overall sign does not affect nonvanishing.
The section representation H_1 is not being identified notationally with
the cohomology group H^1(O(-3)). If delta_e were zero, (3.4) would make
e_tilde vanish on the image of

    id_(P*) tensor multiplication:
    P* tensor H_1 tensor H_5 -> P* tensor H_6.

Ordinary binary polynomial multiplication H_1 tensor H_5->H_6 is onto:
each degree-six monomial is a variable times a degree-five monomial.
Consequently that tensor map is onto and e_tilde would be zero, contrary
to (3.2). Thus delta_e is nonzero. This argument tests every lambda in P*,
not only the polynomial factor.

Derive the remaining required fixed identity from the direct inputs.
By reciprocity and self-duality at the level of representation types,
W' occurs once in P tensor W because W' tensor W=P; T6 occurs once because
T6 tensor W=D+V+P. Their dimensions 2+6 exhaust dim(P tensor W)=8. Hence

    P tensor W=W'+T6.                            (3.5)

Since H_5=T6 is irreducible, the nonzero equivariant map (3.3) is injective
onto the T6 constituent of its target, whose type is (3.5). The cohomology
sequence of (3.1)(3), including H^0(P(-3))=H^1(O(5))=0, therefore gives

    H^0(Q5(3))=0, H^1(Q5(3)) has type W'.        (3.6)

Every ordinary splitting degree of Q5 is at most -4. Its rank five and
degree -22 leave only two possible degree lists:

    (-6,-4,-4,-4,-4), or (-5,-5,-4,-4,-4).

In the first alternative the canonical rank-four top, after twist three,
has zero cohomology; the bottom quotient is the standard equivariant
O(-6), since there are no nontrivial characters. It would give
H^1(Q5(3))=H^1(O(-3)), of type W rather than W', contradicting (3.6).
This uses the canonical bottom quotient, not a uniquely embedded bottom
line. The second degree list is therefore forced. Its bottom coefficient
representation is W' by (3.6), since H^1(O(-2)) is trivial.

At twist four, additivity of equivariant Euler characteristic in (3.1)
gives

    chi_G(Q5(4))=H_6-P=V.                        (3.7)

The bottom block W'(-5) has no cohomology at this twist; the top coefficient
block is therefore V. The ordinary extension of the bottom block by the
top block splits, since H^1(O(1))=0, and a splitting can be averaged over
the finite group to be equivariant. Thus

    Q5 isomorphic to V(-4)+W'(-5).               (3.8)

This classifies the actual projected saturated jet bundle. It does not
extend any unramifiedness, jet-rank, or coefficient-span conclusion to a
different curve or to the unprojected original degree-eighteen system.

## 4. The exact actual seven-space intersection of R13

The original degree-ten curve spans V10 in C*. Its constant restriction
to S* is the complete curve spanning Z*. The restriction image of V10
is therefore exactly Z*. Taking annihilators in S gives

    S intersect M10=ann_S(Z*)=C7.                (4.1)

This uses the original coefficient span and its actual constant restriction;
it is not a transfer of the span of an auxiliary curve.

Let L5=ann_S(R13), a rank-five subbundle of S* O. It contains x2, of rank
three in Z* O. It also contains y and its first intrinsic jets: if e is a
local section of R13, then de lies in R15 tensor Omega_X, and y(R15)=0.
Differentiating the actual constant pairing y(e)=0 gives dy(e)=-y(de)=0.
The constant projection of these first jets to C7* O is precisely the
first-jet map of y7, with generic rank two and saturated image Q2.

The projection of L5 to C7* O consequently has generic rank at least two.
Its kernel contains x2, so its rank is at most two. Its generic image is
exactly the generic fiber of Q2. Taking annihilators in the actual primal
seven-space yields, first generically,

    R13 intersect (C7 O)=ann_(C7)(Q2).           (4.2)

Both sides are saturated in C7 O. On the left, the kernel description of
the map C7 O->(C O)/R13 gives a quotient embedded in a locally free sheaf;
it is torsion-free and hence locally free on X. The right side is the
annihilator of a subbundle. Equal generic fibers of saturated subbundles
therefore give (4.2) everywhere, including the invariant divisor.

For a nonzero member b7:C7*->C7 of the fixed constant form line, the
orthogonality Q2^perp=Q5 means exactly

    b7(Q5)=ann_(C7)(Q2).

Scaling b7 changes no image. Combining with (3.8) and (4.2) gives

    R13 intersect (C7 O)=b7(Q5),
    R13 intersect (C7 O) has type V(-4)+W'(-5).  (4.3)

The first equality concerns actual subbundles in C7 O. The type assertion
uses a constant isomorphism from the opposite ambient C7* O; it does not
confuse the two embeddings.

## 5. A zero T6 row would force an impossible common octic image

Suppose h's T6 row vanishes. Its W' row is nonzero by (2.1) and is
everywhere onto: the common-zero divisor of its degree-seven entries is
invariant and has degree at most seven, smaller than the minimum twelve
for a nonempty invariant effective divisor. Its kernel is a line of degree
2(-3)-4=-10, with standard linearization. Thus

    ker h isomorphic to T6(-3)+O(-10),           (5.1)

and the actual canonical T6(-3) constituent in F18/D0 lies in ker h.
Transport it by the canonical actual-map isomorphism ker h->ker f from
Section 1. It gives an actual subbundle J6 in E0, of type T6(-3), contained
in M10 O because f is induced by p10. Independently the canonical top of
R13 supplied by A gives an actual subbundle J6' in E0 of type T6(-3),
contained in R13.

For either inclusion J6 or J6' in E0, its map to E0/D0 lands in the
canonical degree-minus-three top: there is no map T6(-3)->V(-4).
Its W' component is zero by irreducibility. Its T6 component is nonzero,
since otherwise a rank-six subbundle would lie in rank-five D0. That
component is consequently an isomorphism on the irreducible coefficient
representations. Both inclusions therefore project onto the same canonical
T6(-3) constituent in E0/D0.

There is a unique one-dimensional scalar-map space

    Hom_G(O(-8),T6(-3))=C,                       (5.2)

because H_5=T6. A nonzero member is the universal complete fifth-power
inclusion tensored by O(-3); it is everywhere a line inclusion. This is a
universal map line at the variable tautological point, not a selected
representative or an evaluated scalar.

The induced map of fixed equivariant Hom spaces

    Hom_G(O(-8),E0) -> Hom_G(O(-8),E0/D0)        (5.3)

is injective, since

    Hom_G(O(-8),D0)=(D tensor H_6)^G=0.

The scalar-map lines induced from (5.2) through J6 and J6' have the same
nonzero quotient line under (5.3): the scalar-map line in the canonical
T6(-3) constituent. Injectivity of (5.3) forces the two lifted Hom lines
to coincide. Equivalently the four blocks of E0 contribute 0,0,1,0 to
dim Hom_G(O(-8),E0), so that dimension is one. No relative scalar
normalization of the two inclusions is chosen or evaluated.

The resulting common actual image is a nonzero line subbundle of E0;
both compositions are everywhere injective. Its image lies in both R13
and M10 O, hence by R13 subset S O and (4.1) lies in

    R13 intersect (C7 O).

But (4.3) gives

    Hom_G(O(-8),R13 intersect (C7 O))
      = (V tensor H_4)^G + (W' tensor H_3)^G
      = 0,                                      (5.4)

because H_4=D and H_3=S4. This contradicts the nonzero common image.
Therefore

    h|T6(-3) is nonzero.                         (5.5)

The contradiction is between actual incidences and fixed Hom spaces. It
does not arise by identifying two subbundles merely because their types
match, and does not differentiate the inverse of a moving bundle map.

## 6. Complete degree-seven evaluation and the precise endpoint

The decomposition H_7=W'+T6 is multiplicity-free. Each component space in
Hom_G((W'+T6)(-3),O(4)) is one-dimensional. Both components of the actual
h are nonzero by (2.1) and (5.5). The complete degree-seven evaluation has
nonzero components on both summands, so h differs from that evaluation
only by an invertible constant coefficient automorphism, one scalar line
on each block. This is an existence statement about constant automorphisms,
not a chosen or evaluated scalar ratio.

The universal complete evaluation sequence, twisted by O(-3), is

    0 -> H_6(-4) -> H_7(-3) -> O(4) -> 0.       (6.1)

For completeness, its kernel at the variable tautological line consists
of degree-seven forms divisible by the vanishing linear form; multiplication
identifies it with H_6 tensor O(-1) before the twist. The determinant
convention provides the equivariant identification. This is a universal
binary-polynomial identity, with no selected point or polynomial evaluation.
The constant automorphism above therefore identifies the type of ker h
with H_6(-4). Using only the canonical actual quotient-map isomorphisms
from Section 1 proves

    G7=ker f isomorphic to ker g isomorphic to ker h
       isomorphic to (V_alt+P)(-4).              (6.2)

Their ranks and degrees are seven and -28, as already required by B.
No equality with the same-typed top of K1, equality across distinct kernel
ambients, new derivative-fullness, or full ten-dimensional constant span
of G7 is asserted. The new contribution is exactly the nonvanishing of both
actual lower rows and the resulting gluing-kernel type, with the Q5 and
actual-intersection lemma needed to prove the second row nonzero.

All statements remain conditional on the four complete direct originals
and their transitive geometric assumptions. They do not exclude or realize
K1, close a branch, change original t=0 or local delta=12, prove higher-order
matching of separately proposed data, or establish algebraicity. Actual
fourth-order jets appear only in the already defined projected seven-space
flag Q5; no corresponding assertion is transferred to the full original
degree-eighteen curve or an auxiliary curve.

No selected actual HM/source-instance coefficient, source parameter, point,
jet, tensor, matrix, eigenline, scalar value, normalization, or instance
rank is evaluated. There is no broad scan, large computation, historical
enumerator, quotient connection, horizontal splitting, moving inverse
derivative, rank-seventeen transfer, local Codex operation, GitHub write,
merge, or upstream submission. Independent review of the entire frozen
proof and all four complete authenticated originals remains required.
