# Exact image and radical of the actual middle homotopy pairing

## Theorem

Retain the conditional actual source2 nonzero pure-V compatible-radical
hypotheses. Let Y_n:M3->M4 be the same negative multiplication, h:M4->M2
the canonical homotopy, and I2=im j2. Put

    J3=ker j3,       A_h:J3 -> W* tensor I2,
    A_h(v)(n)=h Y_n v.                                  (1)

Then A_h is well-defined and onto. Its exact kernel character is

    ker A_h = 3W'+2S+4T.                                (2)

This holds in both cases h|NC4=0 and h|NC4 nonzero, without selecting
which occurs.

Put K3=ker Q3 intersect ker j3 and F3=W im h. The actual induced map

    bar A_h:K3/F3 -> W* tensor I2

has image the UNIQUE S summand of W* tensor I2=S+T and exact sequence

    0 -> R_pair -> K3/F3 --bar A_h--> S -> 0,
    R_pair has character 2W'+2S, dimension12.            (3)

Its source has dimension16. Here R_pair means the actual joint radical
of the pairing v,n -> hY_n v on this quotient, not a selected sum of
isomorphic copies. Moreover the marked canonical S_can=U3 supplies an
ACTUAL canonical complement after passage to the quotient:

    K3/F3 = R_pair direct-sum bar S_can.                  (3a)

This is a degree-three quotient splitting selected by the coherent marked
string, not an arbitrary choice of an S multiplicity direction.

The quotient (K3/F3)/R_pair is an actual S coefficient space; its
uncurried multiplication into I2 gives the parameter subpencil

    0 -> ((K3/F3)/R_pair) tensor O(-1)
      -> I2 tensor O -> O(4) -> 0.                       (4)

This is ordinary binary cubic-to-quartic multiplication up to an
unselected nonzero scalar. Neither surviving endpoint16 mechanism,
source realization, transfer value nor positive-variable action is chosen.

## 1. Immutable inputs and exact domains

INPUTS.json pins seven complete public proofs: PR1019 for the actual
endpoint homotopy identities and im h intersect ker Q2=I2; PR1064 for
h(NR4)=I2, its marked nonzero quotient-D comparison, and the actual
coherent S_can-to-D_can string with h|D_can an isomorphism onto I2; PR1068 for the
actual isomorphism delta:NC3->W tensor NC4; PR795 for the genuine exact
residual negative system NC->NR->N8 and j3(NR3)=0; PR792 for coherent
I2=f12 Sym4 W and I3=f12 Sym5 W; PR1054 for F3=W'+2T and F4 subset ker h;
and PR1089 at f8dfebc8c12cbefd3b17422fa1220629e90af78e, the global
alternating-vanishing theorem, for

    K3=3W'+3S+2T, F3 subset K3,
    K3/F3=2W'+3S,
    (K3)_T=(F3)_T.                                    (5)

The latter equality means equality of the ACTUAL T-isotypical subspaces:
it follows from inclusion and equal multiplicities, not a new choice
of their positions. Its rank-four proof and alternating-transfer
vanishing are inputs, not reproved here.

All spaces and arrows are actual inherited spaces. The central parities
of M2,M4 are positive and of M3 negative; W is negative and h preserves
positive parity. Thus the currying (1) is an equivariant map of the
stated odd representations. The letter J3 denotes only ker j3, not the
full radical algebra.

## 2. Values and surjectivity when h is nonzero on NC4

For v in J3, radical intertwining and Q2 h=j4 give

    Q2 hY_n v=j4 Y_n v=Y_n j3 v=0.

The value hY_n v already lies in im h. Thus it lies in
im h intersect ker Q2=I2, proving (1) is well-defined.

The actual NR3 lies in J3. If h|NC4 is nonzero, it kills I4 and is onto
I2 by PR1064: NC4/I4 and I2 are irreducible D and the induced map is
nonzero. PR1068's actual coefficient isomorphism is

    delta(v)=x tensor Y_yv-y tensor Y_xv,
    delta:NC3 -> W tensor NC4.

Composing with Id_W tensor h gives an onto map to W tensor I2. This
is A_h|NC3 after the fixed invertible determinant rotation W*≅W.
It follows that A_h is onto W* tensor I2 in this case.

## 3. Zero restriction: the full universal quotient pairing

Suppose h|NC4=0. Exactness and PR1064 give the unique descended map
hbar:N8,4->I2. It is nonzero on the actual D8 because h is an
isomorphism on the marked D_can projecting isomorphically to D8.
No splitting NR=NC plus N8 is used.

The fixed-variable quotient is

    N8,3=A tensor Sym5 W,
    N8,4=(A tensor Sym6 W)/Delta(Sym8 W).

Its realization by transvectants is C=(C1,C2) with

    Ck(a tensor f)=(a,f)_k,
    (a,f)_k=sum_j (-1)^j binom(k,j)
        (partial_x^(k-j) partial_y^j a)
        (partial_x^j partial_y^(k-j) f).

C identifies N8,4 with Sym6 W plus Sym4 W=(V+P)+D. If i2(f)=f12 f
is the coherent inclusion of PR792, then Schur's lemma gives

    hbar([a tensor f])=lambda i2((a,f)_2), lambda nonzero. (6)

The scalar remains unselected. Actual quotient naturality now identifies
A_h|NR3 with the pullback, through the onto pi3, of lambda times

    U:A tensor Sym5 W -> W* tensor Sym4 W,
    U(u)(ell)=C2(ell u),                              (7)

followed by i2 on the target. Multiplication by ell in (7) affects ONLY
the second polynomial factor, not the first A coefficient factor.
The zero restriction on NC4 makes this descent valid for the actual
maps, not only the characters.

The map U is onto, with exact kernel Delta_2,5(Sym7 W). Here complete
polarization sends the monomial x^(7-k)y^k to the tensor with coefficients

    binom(7-k,2-j) binom(k,j)

at row j*6+(k-j), whenever 0<=k-j<=5. Multiplication back is21 times
the identity, so this inclusion is injective. The checker proves U kills
its whole image. In monomial order, U is a10-by18 matrix; columns

    (1,2,3,4,5,7,8,9,10,11), numbered from zero,

have determinant70808371200. Thus its rank is10 and the displayed
eight-dimensional kernel is exact. This is a universal representation
map certificate, not the evaluation of an actual source map or parameter.

The two channels also have direct polynomial explanations. Alternating
multiplication of the outputs gives

    x C2(yu)-y C2(xu)=2(a,g)_1,  u=a tensor g,         (8)

which is onto the irreducible T=Sym5 W. For the other channel use formal
first-factor variables X,Y and epsilon=Xy-Yx. The embedding

    Sym3 W -> A tensor Sym5 W,  g -> epsilon² g

is equivariant and nonzero. Direct differentiation gives, for every
formal negative linear form ell and cubic g,

    C2(ell epsilon² g)=84 ell g.                     (9)

Thus the S channel is nonzero as well. Neither identity evaluates ell
or g at a selected point. Equations(8)–(9) agree with the full rank
certificate and fix their universal constants only; lambda in(6) is
not assigned any value. This proves A_h onto also when h|NC4=0.

Since M3=3W'+3S+6T and im j3=I3=T, one has
J3=3W'+3S+5T. Subtracting the now-proved target S+T gives (2).
This character subtraction is used only after the actual surjection.

## 4. Restriction to the simultaneous odd kernel

First A_h kills F3. Indeed Y_n F3 is contained in the generated F4,
and PR1054 proves F4 subset ker h. Thus A_h descends on K3/F3.

All S-isotypical vectors of M3 lie in K3: the targets of Q3 and j3
have characters W'+3T and T and hence no S. Equivalently, J3/K3 identifies with im(Q3|J3), a subrepresentation
of the3T image of Q3, and contains no S. In particular all three
S copies in J3 are retained in K3. The surjection A_h:J3->S+T proved
above is onto the S summand, which can only be supplied by those S
copies. Its restriction to K3 therefore still maps onto S.

On the other hand, every W' maps to zero because Hom_G(W',S+T)=0.
By (5) the entire T-isotypical part of K3 is contained in F3 and is
already killed. Thus A_h(K3) is exactly S, with no T image. From the
actual quotient in(5), the kernel on K3/F3 has character2W'+2S and
dimension12. This proves (3), including the exact actual radical.

For (4), let L=(K3/F3)/R_pair. The induced map L->W* tensor I2 identifies
L with the unique S summand there. Uncurrying gives a nonzero map
W tensor S->D. That equivariant Hom space is one-dimensional, because
W tensor Sym3 W=Sym4 W plus Sym2 W. Hence it is ordinary polynomial
multiplication up to a nonzero scalar, with the coherent I2 quartic
identification retained. For every nonzero ell, multiplication by ell
on cubics is injective. The standard binary evaluation sequence then
gives (4) with quotient O(4). This assertion is about the actual pairing
quotient L, not a chosen complementary S subspace of K3/F3. It is not identified
with any separate S-to-D channel in an opposite-pencil construction.

## 5. The marked string canonically splits the pairing quotient

PR1064 retains the actual marked subspaces S_can=U3 and D_can=U4,
with coherent isomorphisms f3:Sym3 W->S_can and f4:Sym4 W->D_can
satisfying

    Y_n f3(s)=f4(ns),        h|D_can:D_can->I2 is an isomorphism.

Both are the specific canonical string images, not arbitrary S or D
copies. The targets of Q3 and j3 contain no S, so S_can is contained
in K3. Since F3=W'+2T contains no S, its image bar S_can in K3/F3 is
isomorphic to S_can.

On this actual marked subspace the pairing is literally

    A_h(f3(s))(n)=h f4(ns).                            (10)

Multiplication W tensor Sym3 W->Sym4 W is nonzero and h f4 is an
isomorphism. Therefore A_h|S_can is a nonzero equivariant map from
irreducible S onto the unique S image established in Section4. It is
an isomorphism after currying. Thus bar S_can is an actual section of
(3), proving (3a), without selecting any complement independently.

If a denotes bar A_h and b its restriction to bar S_can, the canonical
projector on K3/F3 is

    p=inclusion_(bar S_can) b^(-1) a.

It satisfies p²=p, has image bar S_can and kernel R_pair. Rescaling the
coherent f3,f4 identifications does not change their actual images or
this projector; the inverse and forward scalar factors cancel.
The quotient space in (4) is consequently canonically identified with
bar S_can. This strengthens the quotient-only statement. It does not choose a
complement to F3 inside the pairing kernel or supply any
negative-horizontal, Q-module or positive-module splitting. The marked S_can is not identified with any
separate S-to-D channel in an opposite-pencil construction.

As a cross-check on surjectivity, (10) supplies the S channel directly.
The T channel is also onto by PR1089's actual map theta=X(Id_W tensor h)
delta:NR3->I3; it is the determinant rotation of A_h followed by binary
multiplication W tensor I2->I3, which kills the S summand. This gives an
independent actual-map channel explanation consistent with both cases
and the universal rank-ten calculation in Sections2–3.

## Verification and boundaries

Run python verify.py and python -O verify.py. Both reproduce RESULT.json.
The checker authenticates seven immutable inputs, reconstructs (7) and
its exact polarization kernel, verifies the fixed10-by10 determinant,
checks (8)–(9) on all formal coefficients, and checks the stated character
and dimension consequences, together with the scaling-invariant projector
identity. The actual-map arguments and quotient
choices remain essential and are given above.

No actual HM coefficient, direction, point, jet, matrix or instance rank
is evaluated. The theorem sharpens the actual mixed homotopy pairing;
it does not impose a new source cut, select a remaining branch, extend h
to a module homomorphism, or supply positive/full-adjoint conclusions.
