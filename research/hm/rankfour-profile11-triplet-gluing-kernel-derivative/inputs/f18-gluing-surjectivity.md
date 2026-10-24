# The actual resolved degree-eighteen gluing map is everywhere onto

## Publication input provenance, scope, and conclusion

This is a focused, unpublished proof packet prepared for a new independent
review of the entire frozen proof and all four complete direct originals.
The preparatory draft and its prior map-level checks are not a frozen-packet
review or a mathematical dependency. No publication or upstream submission
has occurred.

Retain the full-positive triplet branch, original t=0 and original local
delta=12, residual simultaneous rank-seven k=2 geometry, remaining original
kernel K1, and every complete transitive actual-geometric assumption of the
direct originals below. Put V=V_alt and H_n=Sym^n W for the physical
determinant-one binary-icosahedral representation W on X=P(W*) over C.

The actual map constructed in PR1207 Section 10 is everywhere onto:

    g:F18=D(-2)+(W'+T6)(-3) -> Q=T6(-1).

Its canonical D(-2) top row is a saturated rank-five inclusion, with
quotient O(4). Consequently the original restriction is onto as well:

    f:E0 -> F10=(P+D)(-2).

The actual kernels of f, g, and the induced quotient row are canonically
identified by the actual quotient maps. We denote this common isomorphism
class, with those canonical identifications, by G7. It has rank seven and
degree -28 and fits into the exact sequence

    0 -> G7 -> (W'+T6)(-3) -> O(4) -> 0.

They are not literally the same embedded subbundle of different ambients.
No splitting type of G7 is asserted. This is a new necessary actual-map
compatibility, not an exclusion or realization of K1 or a branch closure.

## 1. Complete direct originals and actual maps

The complete immutable direct originals, retained without excerpts, are:

- PR1207 at commit af136934955f1bcc700ee768e2debb983e75451d,
  research/hm/rankfour-profile11-triplet-shared-d-gluing/PROOF.md,
  retained as inputs/shared-d-gluing.md: 20,361 UTF-8 bytes,
  SHA256 7043302b3fb672f02777d44aac67e4579ac3421bc9cad66af3655a503d2b6bb7,
  Git blob 3d051410e80a33f1c4d78d3403bb186595bb72c3.
- PR1241 at commit fc43b0a6da1fc5e281284fc3b09e46acb97bec95,
  research/hm/rankfour-profile11-triplet-f18-row-resolution/PROOF.md,
  retained as inputs/f18-row-resolution.md: 15,616 UTF-8 bytes,
  SHA256 cd28b6dba69d23ef905f4816dcd1a7a3165bd8b337169ab0a6acb10a15ac06dc,
  Git blob 429c462fe6ba5f2b99770b9cabb35440130c807b.
- PR1235 at commit 7152e94cedbab18036b5e032d4e97934c4c061b7,
  research/hm/rankfour-profile11-triplet-first-kernel-span/PROOF.md,
  retained as inputs/first-kernel-span.md: 11,977 UTF-8 bytes,
  SHA256 66f8040b87f3d193fbd7e6eecb42a1457a59aa6f2cf3f10f29e7ac7b1aa1b6c9,
  Git blob b846834f8451e7202721d9669b43df294f7a96d3.
- PR1236 at commit 092fc5f31dfaa5553ee5ea687f175ecba1878a2a,
  research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md,
  retained as inputs/first-kernel-forward-closure.md: 18,052 UTF-8 bytes,
  SHA256 90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137,
  Git blob f77cfb52743be86e46e0c40570ec036e69aebaf3.

All four complete proofs were freshly authenticated on 2026-10-24 by
read-only GitHub exact-commit fetch_file calls and separate fetch_blob calls,
without line ranges. Complete path content, blob content, and retained local
bytes agree; both SHA256 and Git blob identifiers were recomputed from the
full retained UTF-8 bytes. All four entire originals were read, not replaced
by summaries or checkers. INPUTS.json records exact request-start UTC times,
method arguments, source URLs, byte counts, hashes, and blob pins;
INPUTS.md and PROVENANCE.md record assertion-level use. Raw responses are
local authentication evidence outside the frozen publication core.

Every complete transitive actual-geometric hypothesis remains an assumption,
not independently re-established or freshly authenticated here. The four
complete direct proofs supply every imported statement used below. No
unrelated extension result, later row exclusion, or additional lead is a
dependency or conclusion of this packet.

The first two give the actual diagram

    0 -> T=V(-4) -> E0 -> F18 -> 0
           |         |f      |g
    0 -> T=V(-4) -> F10 -> Q -> 0,

where the left vertical map is the isomorphism onto the SAME actual T
subbundle of F10. Here

    E0=D(-2)+(W'+T6)(-3)+V(-4),
    F18=D(-2)+(W'+T6)(-3),
    F10=H8(-2)=(P+D)(-2), Q=T6(-1).

The map f is restriction under the constant projection

    p10:C -> V10*,

where the degree-ten curve spans V10 and is complete. The constant kernel
M10=ker p10 has type A+V+P, because C has type 2A+2V+D+P and V10* has
type A+V+D. The symbol M10 in this proof denotes this constant ten-space,
not the rank-two first-jet bundle with similar notation in PR1207.

PR1235 supplies the actual backward kernel

    K=E0^-=(V+P)(-4)+T6(-5).

PR1236 supplies the actual annihilator S0=ann_C*(E0), and the exact sequence

    0 -> L0=O(-10)+O(-18) -> S0 -> A(-6) -> 0.

The original degree-ten first-jet bundle X1=W(-9) lies in V10 O and is
ann_(V10)(F10). Only actual constant-ambient derivatives are used below.

## 2. A universal low-degree lemma inside the physical quartic block

There are canonical complete-jet inclusions

    delta:O(-6) -> H4(-2),
    kappa:W(-5) -> H4(-2),

with delta factoring through kappa. They are the scalar and first-jet
inclusions of the complete quartic curve, tensored by O(-2). Intrinsically
the inclusions are multiplication by the tautological fourth and third
powers. They do not choose a point, polynomial representative, or scalar
normalization.

The equivariant polynomial coefficient space of H4(-2) is H4 tensor H2.
Its fixed physical SL2 decomposition is

    H4 tensor H2 = H6 + H4 + H2.

Let u6:H4(-2)->H6 O be multiplication by the tautological square, and let
u2:H4(-2)->H2 O be the other complete coefficient row. Both are the fixed
universal SL2 maps, up to their harmless constant scalar lines. The H6
component of u6 delta is the complete sixth-power curve O(-6)->H6 O;
the composite u6 kappa is its complete first-jet inclusion W(-5)->H6 O.

These statements are universal multiplication identities: fourth power
times square is sixth power, and third power times a binary vector times
square is fifth power times that vector. They hold at the variable
tautological line and evaluate no selected vector or actual coefficient.

On the other hand u2 kappa is zero. Indeed

    Hom_G(W(-5),H2 O)=Hom_G(W,A tensor H5)=0,
    A tensor H5 = H7+H5+H3 = W'+2T6+S4.

This verifies the needed tensor identity and the actual map directions
without using a coordinate contraction formula.

## 3. The canonical D top cannot lie in the constant kernel M10

Let D0=D(-2) be the canonical top subbundle of E0. Suppose f|D0=0. Then
its actual inclusion in C O factors through M10 O, whose representation
A+V+P has no D constituent.

Identify the coefficient type of D0 with the fixed H4 through its constant
isomorphism line; no representative or normalization is evaluated. The
coefficient-space identity in Section 2 shows that its actual map to
M10 O factors as

    D0 --(u2,u6)--> H2 O direct-sum H6 O
       --(q2,q6)--> M10 O,                         (3.1)

for constant equivariant block maps q2,q6. The H4 coefficient row vanishes
because M10 has no D. The remaining irreducibles A in H2 and V+P in H6
are multiplicity-free, so (3.1) accounts for every possible actual row,
not only a selected universal model.

The map q6 is nonzero: otherwise the rank-five subbundle D0 would map
through the rank-three constant H2 block, impossible for its inclusion
in C O. Since the complete sixth-power curve spans all of H6, the actual
composite scalar map

    z:O(-6) --delta--> D0 -> C O

is nonzero. By Section 2 it equals q6 applied to that complete sixth-power
curve, because u2 delta=0. Its first intrinsic jet image is the image of
the composite through kappa, followed by the actual inclusion of D0 in
C O. The two standard universal descriptions can differ by a nonzero
factor determined by the principal-parts symbol convention; only their
equal image is used. In particular those first jets lie in D0 and hence
in E0.

Thus the actual second fundamental form of E0 kills z: every derivative
of this actual scalar curve still lies in E0. Equivalently z factors
through the actual kernel K=E0^-. This is impossible, since

    Hom_G(O(-6),(V+P)(-4))=((V+P) tensor H2)^G=0,
    Hom_G(O(-6),T6(-5))=(T6 tensor H1)^G=0.

We conclude

    f|D0 is nonzero.                               (3.2)

Notice that no connection on D0 was used. The derivative statement concerns
the actual composed degree-six curve, identified through the fixed universal
map (3.1) and constant maps q2,q6.

## 4. The D row of g is the saturated universal inclusion

The quotient E0->F18 identifies their canonical D(-2) top subbundles:
twisting by two gives an isomorphism on H0, since T(2)=V(-2) has no H0
and H0(E0(2))=H0(F18(2))=D.

If g killed this top, the nonzero map f|D0 would factor through T=V(-4)
in F10. But Hom(D(-2),V(-4))=0 by ordinary degree, contradicting (3.2).
Therefore g's D row is nonzero.

Its equivariant Hom space is one-dimensional:

    Hom_G(D(-2),T6(-1))=Hom_G(D,T6 tensor W)=C,
    T6 tensor W=D+V+P.

The nonzero universal member is the complete degree-five evaluation kernel,
twisted by O(-1):

    0 -> D(-2) -> T6(-1) -> O(4) -> 0.             (4.1)

Hence the actual D row has the same saturated image as (4.1). Denote this
actual rank-five image by D_Q. Its quotient in Q is O(4).

## 5. The remaining quotient row cannot vanish

The induced quotient row is

    h:F18/D(-2)=(W'+T6)(-3) -> Q/D_Q=O(4).        (5.1)

Suppose h=0. Then g maps onto D_Q, because its D row is an isomorphism
onto D_Q. Let B8 be the actual preimage of D_Q under F10->Q. Then

    0 -> T -> B8 -> D_Q -> 0,
    F10/B8=O(4).

The actual image of f is exactly B8, and f is everywhere onto it: its
image contains the whole T by the left isomorphism in the actual diagram,
and maps onto D_Q modulo T. This is a local sheaf-surjectivity argument,
not an identification based only on ranks.

Take the actual rank-three annihilator A3=ann_(V10)(B8) in V10 O.
This notation is local to this argument and does not reuse a backward-flag
label. Dualizing the quotient sequence for B8 inside F10 inside V10* O gives

    0 -> X1=W(-9) -> A3 -> O(-4) -> 0.            (5.2)

Its equivariant extension group vanishes:

    Ext1_G(O(-4),W(-9))
      = (W tensor H1(O(-5)))^G
      = (W tensor H3)^G = 0.

Thus A3 contains an actual equivariant subline O(-4). Because B8 is the
actual image of E0 under constant restriction to V10*, every element of
A3 annihilates E0 when included by the constant map V10->C*. Hence

    A3 subset S0=ann_C*(E0).

But PR1236's exact sequence for S0 gives Hom(O(-4),S0)=0: both
Hom(O(-4),O(-10)+O(-18)) and Hom(O(-4),A(-6)) vanish by degree.
This contradicts the subline just obtained. Therefore h is nonzero.

Every nonzero component of h has entries of degree seven. The common-zero
divisor of all its entries is invariant and has degree at most seven,
bounded by any nonzero entry. The invariant-divisor minimum twelve forces
it to be empty. Thus h is everywhere onto. Together with the saturated
D row this proves that g:F18->Q is everywhere onto.

## 6. The original restriction is onto, and its actual kernel is preserved

The diagram in Section 1 now makes f:E0->F10 everywhere onto: modulo T
it is onto by g, and on T it is an isomorphism. Put G7=ker f, as an actual
subbundle of E0. Its rank and degree are seven and -28. The actual quotient E0->F18 restricts to an
isomorphism from G7 to ker g, by the diagram's left-hand isomorphism.
The quotient F18->F18/D(-2) similarly identifies ker g with ker h.
We use G7 in the following sequences via these canonical actual-map
identifications; these kernels are not literally one embedded subbundle
of three different ambients. We obtain the actual exact sequences

    0 -> G7 -> E0 -> F10 -> 0,
    0 -> G7 -> F18 -> Q -> 0,
    0 -> G7 -> (W'+T6)(-3) --h--> O(4) -> 0.

For the third sequence, g maps its D(-2) top isomorphically onto D_Q, so
subtracting the unique D-top lift identifies ker g with ker h. No splitting
is made horizontal, and no type of G7 beyond rank and degree is claimed.

All conclusions concern the original actual restriction maps and their
coherent kernels, not arbitrary maps between the displayed bundle types.
No actual coefficient, selected point, source parameter, jet, tensor,
matrix, scalar ratio, normalization, or instance rank is evaluated. Only
fixed universal character identities, complete polynomial multiplication
maps, exact diagrams, and degrees are used. No whole-branch exclusion,
higher-order matching, realization, algebraicity, publication, merge, or
upstream submission is claimed.
