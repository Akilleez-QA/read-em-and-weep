# Universal constant-connection feasibility of the source2 flag

## Result and precise boundary

Work over C. Let G be the binary icosahedral group, W its defining
representation, A=Sym^2 W, S=Sym^3 W, D=Sym^4 W, T=Sym^5 W,
and let V, P, W' denote the other three-, four-, and two-dimensional
irreducibles. All coefficient representations used below are self-dual.
Write X=P(W); the invariant symplectic identification W=W* identifies the
dual parameter line when necessary.

Let B be the entire balanced open locus of PR754: the projective line of
P-multiplicity lines in Sym^18 W, with its two nonbalanced points removed.
For every t in B there is a genuine G-equivariant saturated inclusion

    Q_t* ⊂ H_t* ⊗ O_X

with the original trivial connection on its stated constant representation,
whose annihilator E_t simultaneously satisfies the following data:

1. The source2 ambient character, source splittings, ranks and degrees,
   negativity, full constant spans, and both prescribed linear presentations.
2. The two genuine constant projections and exact intersections of
   PR744/751, including the balanced final degree-eighteen endpoint.
3. The exact residual backward flag of PR758, the maximal rank-three profile
   (2,1), both source2 first quotients, and zero second primal defect.
4. All four-jet flag statements of PR784/785 and the actual ramification of
   its own endpoint described by PR786.
5. A common pair of commuting multiplication pencils of dimensions
   41→54→37 whose Koszul middle cohomology is H_t and whose actual Gauss
   derivative is the quotient map from the kernel to the cokernel, exactly
   as in the abstract form of the published double-hyperplane interface.

Thus these listed abstract constant-connection and common-pencil conditions
are jointly feasible, not merely separately feasible bundle splittings.
None can exclude source2 by themselves.

This is NOT an HM realization theorem. The constructed pencils are not
identified with multiplication on the fixed actual HM adjoint cohomology
module. In particular, neither its actual endpoint parameter nor its actual
embedding into the plane section space is determined. No stable label is
excluded; the frontier remains 23=19/3/1. The result concerns the remaining
label G3.21.d610e381ed75 only at the explicitly listed abstract level.

## 1. Pinned sources and novelty boundary

All named paths in this paragraph except the separate PR784–787 directories
lie under research/hm/order-four-quadratic-load/ in
Akilleez-QA/read-em-and-weep.

- PR744, origin 2348d4b6fb2afd67d66b15aad6037ab92c94f076:
  TWO-ONE-INDEX-TWO-CONSTANT-SPAN-INTERSECTION.md. Its unchanged version at
  063216038f3aefd65617651c2426721efafc7f9b is also the input to PR784.
- PR745 at 8f4298bfd92fdf9bdbe3827dd82a0a137b91b024:
  PRIMAL-EQUALITY-RESIDUAL-FILTRATIONS-REMOVE-BOUNDARY-STRATA.md and its
  source kernel classification were checked. Its extra cuts concern the distinct labels
  G3.11.942927348917, G3.12.8e9af2d08af9, G3.21.45ca6278cbfc, not source2.
  Its ordinary filtered witnesses explicitly do not construct a constant
  ambient connection.
- PR751 at e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169:
  TWO-ONE-INDEX-TWO-RESIDUAL-FULL-SPAN.md, with the preceding
  TWO-ONE-INDEX-TWO-RESIDUAL-OSCULATIONS.md. These force exactly the E and Q*
  splittings reproduced below, rather than a weaker numerical overlist.
- PR754 at 044add76ebb14043a0edf73171517c90b9ef0c13:
  ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md proves the balanced family B.
- PR758 at 063216038f3aefd65617651c2426721efafc7f9b:
  TWO-ONE-INDEX-TWO-EXACT-RESIDUAL-GAUSS-FLAG.md.
- At the same PR758 pin, ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md,
  POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md, and
  UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md provide the original source
  characters, linear presentations, and exact common Koszul/Gauss origin.
- PR784 at 66aa488fb10158abcc2d35ce58b05b901d44b81a,
  research/hm/source2-second-defect-zero/PROOF.md.
- PR785 at 7ec3b8140abe6ee60f9d0dfee657e7b0be022fc3,
  research/hm/source2-four-jet-rigidity/PROOF.md.
- PR786 at 575c0720268af5bb4b305e29284f65614ba9f9ca,
  research/hm/source2-endpoint-wronskian/PROOF.md.
- PR787 at 19ec11c934cbba7be18dd1f465ba0d0cc547dcf8,
  research/hm/source2-fifth-sixth-conditional/PROOF.md was supplied and read
  during this proof. Its conditional fifth/sixth branches are compatible
  with (12), including their endpoint saturation corrections.

The checked sources prove successive necessary constraints or the final
endpoint's abstract feasibility. They do not assert the simultaneous
constant-connection construction or its common-pencil reconstruction below.
Those are the new assembly and limitation statement here. The endpoint
classification and jet theorems themselves are credited inputs.

## 2. The construction over every balanced parameter

For t in B, write Hcal_t=A+V+P_t ⊂ Sym^18 W for its ten-section system and
F_t=Hcal_t*. PR754 supplies the exact sequence

    0 → C_t=O(-18) → F_t⊗O → (P+D)O(2) → 0.       (1)

For e≥0 and 0≤j≤e, let

    U_j^e = Sym^j W⊗O(j-e) ⊂ Sym^e W⊗O,
    (U_j^e)_ell = ell^(e-j) Sym^j W.               (2)

These are the complete Veronese osculating subbundles. Define

    H_t* = Sym^10 W ⊕ Sym^8 W ⊕ F_t,
    Q_t* = U_8^10 ⊕ U_2^8 ⊕ C_t.                 (3)

Each summand in (3) is saturated in its own constant block, so Q_t* is
saturated in the direct sum. Its rank is 9+3+1=13 and its degree is
9(-2)+3(-6)-18=-54. The ambient rank is 11+9+10=30. Moreover

    Sym^10 W=A+V+D,  Sym^8 W=P+D,
    H_t* = 2A+2V+2P+2D.                           (4)

Set E_t=ann(Q_t*) inside H_t⊗O. The apolar pairing in Sym^e W identifies
the annihilator of ell^(e-j)Sym^j W with ell^(j+1)Sym^(e-j-1) W. Applying
this to the two complete blocks and dualizing (1) gives

    E_t = W O(-9) ⊕ T O(-3) ⊕ (P+D)O(-2).        (5)

It has rank 2+6+9=17 and degree -18-18-18=-54. Thus (5) is exactly the
forced source2 splitting of PR751, and (3) is its forced Q* splitting.
Both bundles have H0(F(1))=0 and contain no nonzero constant subbundle.
Both span their whole constant ambient spaces: a missing constant direction
would be a nonzero constant section of the annihilator, which is impossible
by the negativity of the other bundle.

No parameter is selected in this construction. Over B, the P_t factor is
the tautological multiplicity line tensored with P. Hence (1)–(3) are an
algebraic family, constant in the X direction; the constant vector space
F_t may vary as a vector bundle in the parameter direction. One need not
choose a global trivialization in t, identify coefficients, or set a value
of t to state or prove any assertion.

The displayed coefficient-representation identifications in (1) and (5)
are fiberwise in t. Over B their multiplicity spaces are vector bundles;
they are not asserted to have canonical global trivializations. In
particular F_t has relative P multiplicity O_B(1). The relative ambient
bundle is pulled back from the parameter base, and its connection is only
in the X direction. Identifying a fiber with a fixed abstract A+V+P is a
constant equivariant gauge choice, not selection of an actual HM parameter.

Crucially, (3) is a decomposition of constant representations and their
subbundles before differentiating. The connection preserves these ambient
constant blocks. It is not an arbitrary bundle splitting later declared
horizontal.

## 3. The genuine constant quotients

Projection by V0=Sym^10 W has exact intersection and quotient

    Q_t* ∩ (V0⊗O)=U_8^10,
    R_t=Q_t*/U_8^10=U_2^8⊕C_t
       ⊂ (Sym^8 W⊕F_t)⊗O.                        (6)

Projection of R_t by V1=Sym^8 W gives

    R_t ∩ (V1⊗O)=U_2^8,
    R_t/U_2^8=C_t ⊂ F_t⊗O.                       (7)

All arrows are sheaf-surjective onto their displayed targets, with locally
free quotients. Equations (6) and (7) reproduce the precise saturation and
intersection hypotheses of PR744/751, not just their generic ranks. Their
annihilator projection kernels are respectively
T O(-3)⊕(P+D)O(-2) and (P+D)O(-2), as required.

The degree-eight line U_0^8 has full constant span Sym^8 W, and its first
two forward transforms are U_1^8 and U_2^8. Likewise the degree-ten block
comes from the full Sym^10 W system. The endpoint C_t has full span F_t
because its ten defining sections are independent.

## 4. Exact Gauss flags and the source2 quotient pair

Write F^+ for saturated forward transform and F^- for backward derivative
kernel. In a genuine constant direct sum these operations commute with
direct sums: differentiation and the quotient map are componentwise, and
saturation is componentwise because the quotient module is a direct sum.
For the nonconstant complete blocks, 0≤j<e,

    (U_j^e)^-=U_(j-1)^e,
    (U_j^e)^+=U_(j+1)^e,                            (8)

with U_-1^e=0 and U_e^e=Sym^e W⊗O. The constant top block is fixed by
both forward and backward transformation; the backward formula in (8)
is not asserted at j=e. Further forward transforms remain constant.
One universal leading-symbol identity proves (8): for a local line
ell=x+zy, differentiation of ell^(e-j)y^j modulo U_j^e is
(e-j)ell^(e-j-1)y^(j+1), nonzero for j<e. No source point is evaluated.
The consecutive quotient is

    U_j^e/U_(j-1)^e = O(2j-e).                      (9)

A negative line in a constant bundle has zero backward kernel. Therefore

    R_t^- = U_1^8,  R_t^{--}=U_0^8,  R_t^{---}=0,  (10)

giving exactly ranks (4,2,1,0), degrees (-36,-14,-8,0), and the residual
quotients O(-18)+O(-4), O(-6), O(-8) of PR758.

For n≥1 the complete backward flag is

    (Q_t*)^(-n)=U_(8-n)^10 ⊕ U_(2-n)^8,            (11)

with negative indices zero. For j≥0 put C_t^(j)=(C_t)^(j+), saturated at
each step. The complete forward flag is

    (Q_t*)^(j+) = U_min(8+j,10)^10
                  ⊕ U_min(2+j,8)^8 ⊕ C_t^(j).    (12)

Formula (12) remains valid at all higher endpoint ramification. It is a
statement about this constructed split constant system, not a statement
that the fixed actual source's higher extensions split horizontally.

PR785 gives C_t^(j)=U_j^18 projected injectively into F_t for 0≤j≤4, with
no saturation corrections. Annihilator duality and (9) therefore yield

    A_t=E_t/E_t^- = O(-8)⊕O(2)⊕O(16),
    B_t=Q_t*/(Q_t*)^- = O(-18)⊕O(-4)⊕O(6),
    J_2=E_t^-/E_t^{--} = O(-10)⊕O⊕O(14),
    J_3=E_t^{--}/E_t^{---} = O(-2)⊕O(12),
    J_4=E_t^{---}/E_t^{----} = O(-4)⊕O(10).       (13)

The maps A_t→B_t*(-2) and J_2→A_t(-2) are isomorphisms: their component
symbols are the nonzero complete-block coefficients and the everywhere
independent first two endpoint jets. Thus both central torsion defects
are zero. The maps involving J_3 and J_4 have exactly the top-two-summand
image and the isomorphism stated in PR785.

Through j=4, the residual forward ranks/degrees are

    (4,-36), (6,-54), (8,-68), (10,-78), (12,-84).

The corresponding E backward ranks/degrees are

    (17,-54), (14,-64), (11,-68), (9,-78), (7,-84). (14)

The characteristic-zero Wronskian of ten independent sections is nonzero.
Thus the generic ranks of C_t^(j) are min(j+1,10). Formulae (11)–(12) give
the complete saturated rank flags

    E backward: 17,14,11,9,7,5,3,2,1,0;
    E forward:  17,20,22,24,25,26,27,28,29,30.      (15)

Hence precisely two rank-three blocks lie below E and one above it;
the adjacent outward increments are two. The maximal rank-three profile
is exactly (2,1), not an assumed numerical label. Higher backward E
degrees may depend on the endpoint's ramification and are not declared
uniform here. PR786's endpoint types apply to each t on their stated
parameter loci; no identification of balanced exceptions with jet
exceptions is made.

The same formula (12) realizes each conditional fifth/sixth branch of
PR787 whenever its parameter lies in B. Its conclusion that at least one
of the two low-jet exceptional parameters is balanced therefore also
applies to this abstract constant-connection family. We do not choose
which exceptional parameter lies in B or identify an actual HM branch.

## 5. The original source characters and both linear presentations

The exact actual source data are

    M2=A+2V+3P+4D,
    M3=3W'+3S+6T,
    M4=2V+4P+3D.                                   (16)

The splittings (3) and (5) give

    H1(E_t(-1))=M3,  H1(E_t)=M4,
    H1(Q_t*(-1))=M3*,  H1(Q_t*)=M2*.               (17)

For clarity these are exact identities, not just dimension matches.
For E_t(-1), its three contributions are each W'+S+2T, using
W⊗Sym^8 W=Sym^9 W+Sym^7 W and T⊗A=Sym^7 W+Sym^5 W+Sym^3 W.
For E_t, the contributions are V+2P+D, V+P+D, P+D. For Q_t*(-1), the
contributions are W'+S+2T, W'+S+2T, Sym^17 W=W'+S+2T. For Q_t*, they are
P+D, A+V+P+D, Sym^16 W=V+P+2D. These sum to (17).

Any equivariant bundle F on P1 with all splitting degrees at most -2 has
the natural linear presentation

    0 → F → H1(F(-1))⊗O(-1) → H1(F)⊗O → 0.       (18)

The map is induced by multiplication with the variable linear form. On a
summand O(-d), it is the dual of the full degree-(d-1) evaluation sequence,
twisted by O(-1), so it is surjective and its kernel is O(-d). Tensoring by its
coefficient representation and taking sums proves (18); the invariant
identification W=W* fixes the parameter convention. Applying (18) to
E_t and Q_t* proves precisely the two abstract source presentations

    0 → E_t → M3 O(-1) → M4 O → 0,
    0 → Q_t* → M3* O(-1) → M2* O → 0.             (19)

In particular the known Euler-character and section-envelope conditions
derived from these presentations are satisfied. The next section shows
that their middle representations can be identified compatibly, rather
than merely choosing two unrelated maps with the right characters.

## 6. A canonical common commuting-pencil reconstruction

This section is a general lemma. Suppose

    0 → E → H⊗O → Q → 0                            (20)

is exact on P1 and both E and Q* have all degrees at most -2. Let

    N2=H0(Q(-2)), N3=H0(Q(-1)), N4=H1(E),
    δ:H0(Q)→H1(E)

be the connecting map. Since H⊗O(-1) is acyclic, its twisted sequence
canonically identifies N3 with H1(E(-1)). For any linear form l define

    A_l:N2→N3,       r↦lr,
    B_l:N3→N4,       s↦δ(ls).                      (21)

Then A_l is injective for every nonzero l. Under the connecting
identification, B_l is multiplication H1(E(-1))→H1(E), which is
surjective by 0→E(-1)→E→E|_(l=0)→0. Naturality and commutative polynomial
multiplication give the exact identity

    B_u A_v = B_v A_u                               (22)

for every u,v. Thus this is a common commuting pair of pencils, not
independent presentations whose compatibility is assumed.

For independent u,v, form the constant complex

    N2 --(A_v,-A_u)--> N3⊕N3 --(B_u,B_v)--> N4.    (23)

Its first map is injective, its last map surjective, and its middle
cohomology is canonically H. To prove the last assertion, send a cycle
(x,y) to the unique h in H whose section of Q is ux+vy. Such h exists
because δ(ux+vy)=0, and is unique because H0(E)=0. The Koszul sequence

    0 → Q(-2) --(v,-u)--> Q(-1)^2 --(u,v)--> Q → 0

shows that its kernel on cycles is exactly the first image in (23).
It also gives surjectivity onto H because H1(Q(-2))=0, so every section
of Q, including the image of every h, can be written ux+vy.

Let l=u+zv. If k∈ker B_l, the cycle (k,zk) represents the section lk of
Q, which vanishes at p=(l=0). Its class is therefore in E_p⊂H. Conversely
any h∈E_p has its Q-section divisible by l, giving a unique k∈N3 with
B_l k=0. Consequently this identifies the kernel fibers with precisely
the original inclusion E⊂H⊗O, with the usual tautological O(-1) factor.

Dually the evaluation presentation of Q(-1) is

    0 → N2⊗O(-1) --A--> N3⊗O → Q(-1) → 0,         (24)

as follows either from the same division argument or summandwise from
the full evaluation kernel. Thus (20), both pencils, and their common
constant Koszul space are one compatible construction. In the affine
frames of the published Gauss gate, the quotient is represented by
[(x,y)]↦[y-zx] modulo A_l N2; differentiating [(k,zk)] gives [k]. This
is the same universal negative-transpose/Gauss comparison, up to its
harmless common boundary sign.

For (3)–(5), the representations N2,N3,N4 are M2,M3,M4 by Serre duality,
(17), and the connecting isomorphism. Their dimensions are 41,54,37.
Their common middle cohomology has character

    M3⊗W - M2 - M4 = 2A+2V+2P+2D,

agreeing with (4). This proves item 5 in the result. Merely imposing
commutativity of two linear multiplications, the Koszul formula, or the
two exact presentations is therefore not an additional exclusion of
the constructed family.

The common-pencil square-rank condition is also satisfied. For an
injective A_l and surjective B_l, the exact kernel/cokernel comparison
identifies the map ker B_l→coker A_l with the Gauss map above and gives

    rank(B_l A_l)=24+rank(SF_l).

Here all three central component symbols are everywhere nonzero, so the
constructed SF has rank three at every point. Thus the constructed square
multiplication has rank 27 everywhere, agreeing with the frozen lower
bound. This is a universal rank deduction from the proved exact sequences,
not an actual-instance evaluation or a new assertion about the fixed HM
square map.

## 7. Exactly what remains outside this theorem

The fixed original problem has B_HM=End_0(F_HM), prescribed spaces
H1(B_HM(2))_+, H1(B_HM(3))_-, H1(B_HM(4))_+, and prescribed
multiplications by the negative linear forms. Its constant H_HM is the
actual plane section space H0(B_HM|_R(4)), identified with their Koszul
middle cohomology by the published geometric vanishing theorem.

Sections 2–6 construct a family with the same representations, bundle
splittings, and displayed abstract interfaces. They do not produce
equivariant isomorphisms identifying the constructed A_u,A_v,B_u,B_v
with those fixed HM multiplication tensors, nor an identification of
the resulting constant inclusion with E_HM⊂H_HM⊗O. They do not extend
the constructed three graded pieces to the fixed full ambient adjoint
module, its multiplication in the other coordinate directions, its
algebra structure, or its geometric origin from the HM bundle.

Even equality of an abstract endpoint parameter with a hypothetical
actual endpoint would not by itself identify these constant inclusions.
The actual source need not be horizontally split into the three blocks
of (3); no such assertion is made. The family is a witness that the
listed necessary axioms are consistent, not a classification of all
constant embeddings having those axioms.

Accordingly, further exclusion must use information not implied solely
by those realized axioms: for example a constraint on the fixed original
multiplication tensors or on their extension to the full actual module.
This theorem does not assert which extra constraint succeeds or fails.
It neither constructs an HM realization nor proves that none exists.

## Method restrictions and evidential scope

The proof is universal over B. No endpoint parameter, invariant-form
coefficients, actual source point, source derivative, matrix, or rank
was selected or evaluated. The derivative formula is a universal
identity for complete osculating bundles. No model experiment, scan,
large computation, or source-instance calculation was run. This is a
written structural proof, not proof-assistant certification.
