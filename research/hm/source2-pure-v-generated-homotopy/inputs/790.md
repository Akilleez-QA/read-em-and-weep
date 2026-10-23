# Source2 forces a constant degree-ten block and a fixed-pencil summand

## Result and boundary

Work over C. Let G be the binary icosahedral group, W its defining two-space,
A=Sym^2 W, S=Sym^3 W, D=Sym^4 W, T=Sym^5 W, and V, P, W' the other
three-, four-, and two-dimensional irreducibles. All these representations
are self-dual. Use the invariant symplectic identification of W with W*.

Conditionally on the published actual-source conclusions of PR744, PR751,
and PR758 for source2, every actual constant inclusion has a G-equivariant
constant ambient normal form

    (H*, Q*) = (Sym^10 W, U_8^10) direct-sum (Hbar, R),       (1)

where U_j^e has fiber ell^(e-j) Sym^j W and is Sym^j W O(j-e).
The assertion is about a constant change of ambient coordinates preserving
the original connection. It is not a bundle splitting declared horizontal.

Consequently the fixed actual negative multiplication tensors on
M2 -> M3 -> M4 admit a simultaneous G-equivariant direct summand with
characters

    (P+D, W'+S+2T, V+2P+D)                                (2)

and dimensions (9,18,16). The complementary dimensions are (32,36,21).
The summand is the canonical two-pencil system associated with
U_8^10 in Sym^10 W, not merely a triple with these dimensions.

This is a necessary condition on the fixed HM tensors. No test of this
condition is performed. The residual R is not asserted to split constantly,
no endpoint parameter is selected, and no source label is excluded.

## 1. Pinned inputs

The repository is Akilleez-QA/read-em-and-weep. The following original paths
are under research/hm/order-four-quadratic-load/:

- PR744, commit 2348d4b6fb2afd67d66b15aad6037ab92c94f076:
  TWO-ONE-INDEX-TWO-CONSTANT-SPAN-INTERSECTION.md.
- PR751, commit e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169:
  TWO-ONE-INDEX-TWO-RESIDUAL-FULL-SPAN.md, with the preceding
  TWO-ONE-INDEX-TWO-RESIDUAL-OSCULATIONS.md.
- PR758, commit 063216038f3aefd65617651c2426721efafc7f9b:
  TWO-ONE-INDEX-TWO-EXACT-RESIDUAL-GAUSS-FLAG.md.
- At the PR758 pin: POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md,
  UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md, and
  ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md.

PR788, commit 941b7b3b77dc8ae8a19b1e000dddeb0438d05db7,
research/hm/source2-universal-constant-flag/PROOF.md, supplies the abstract
common-pencil reconstruction and the independently feasible split witness.
The argument below proves a new necessary partial splitting for every
actual inclusion satisfying the earlier exact inputs. Section 6 verifies
that reconstruction recovers the original tensors, rather than only their
characters. It does not identify the full actual inclusion with PR788's
three-block witness.

For the bounded orbit corollary in Section 8 only, we additionally use
PR789, commit 2d1642ad40ae1111b84b50eeaca0426bfbfbb314,
research/hm/source2-residual-coupling-normal-form/PROOF.md. It classifies
residual inclusions with the exact structure (3), proves two residual
constant-gauge classes over each balanced endpoint, and constructs both
as abstract residual inclusions. Its full stabilizer and its exact
backward flag are the particular inputs used below.

The needed earlier conclusions are as follows:

    V0=Sym^10 W is a genuine invariant constant subspace of H*;
    Q* intersect (V0 O) = U=U_8^10;
    R=Q*/U is saturated in (H*/V0) O;
    V1=Sym^8 W is a genuine invariant constant subspace of H*/V0;
    R intersect (V1 O) = A0=U_2^8;
    0 -> A0 -> R -> C=O(-18) -> 0.                         (3)

The final line C is saturated in its genuine constant quotient. The
constant quotient characters are

    H*/V0 = V1 + F,    V1=P+D,    F=A+V+P.

Choose arbitrary equivariant constant splittings of these representation
quotients, allowed by finite-group semisimplicity. Thus

    H*=V0 direct-sum Hbar,    Hbar=V1 direct-sum F.

All ensuing assertions hold for any such initial choice. This choice
introduces no connection on an abstract bundle complement: every chosen
summand is an actual constant subspace.

## 2. The only possible first coupling

Apolar duality gives

    Z=(V0 O)/U = W O(9).                                  (4)

For clarity, Z is the quotient by U, not the block of Q dual to U.
Quotient the actual inclusion by U. Its projection onto Hbar O identifies
it with R, so it is the graph of a unique equivariant bundle map

    beta:R -> Z.                                         (5)

The following are universal character identities:

    Sym^15 W = S+2T,
    Sym^27 W = W'+2S+3T,
    A tensor W = W+S.

They imply

    Hom_G(C,Z) = (W tensor Sym^27 W)^G = 0,
    Ext^1_G(C,Z) = H^1(W O(27))^G = 0,
    dim Hom_G(A0,Z)
      = dim (A tensor W tensor Sym^15 W)^G = 1.            (6)

Here equivariant Ext is ordinary Ext followed by invariants because G is
finite in characteristic zero. Applying Hom_G(-,Z) to (3) proves that
restriction is an isomorphism

    Hom_G(R,Z) -> Hom_G(A0,Z),                            (7)

and both spaces have dimension one. This does not assume that (3) splits
compatibly with its constant embedding.

There is a nonzero constant equivariant map

    T0:Hbar -> V0                                        (8)

supported on the unique D constituent of V1 and the unique D constituent
of V0, and zero on the other constituents. The crucial issue is whether
its composite A0 -> V0 O -> Z is nonzero. Characters alone do not decide
that restriction. We prove it geometrically next.

## 3. A universal five-section jet lemma

For d=8 or d=10, let p_d:Sym^d W -> D be the projection onto its unique
D constituent. Under an arbitrary nonzero equivariant identification of
these D spaces, consider the projected Veronese curve

    O(-d)=U_0^d -> D O.

Its dual is a five-dimensional invariant linear system in H^0(O(d)). The
system has no base points. Indeed a nonempty base divisor is invariant
under the projective A5 action, every orbit has at least 12 points, and its
degree is at most d<12.

The characteristic-zero Wronskian of five independent sections is nonzero.
Its divisor has degree

    5(d-4),

which is 20 for d=8 and 30 for d=10. At an arbitrary point let
0=a0<a1<a2<a3<a4 be its vanishing sequence. Failure to span second jets
means a2>=3. Strict increase then gives a3>=4 and a4>=5, so the Wronskian
weight sum_i(ai-i) is at least 3. The failure locus is invariant. If it
were nonempty, one entire orbit would contribute weight at least 3*12=36,
contradicting the total Wronskian degree in either case.

Therefore both systems span second jets everywhere. In particular, for
j=0,1,2, the projected complete osculating morphism

    U_j^d -> D O

is fiberwise injective. Its image J_j^d is a saturated rank-(j+1) subbundle
isomorphic to U_j^d, with

    deg J_j^d = (j+1)(j-d).                              (9)

These conclusions are pointwise-universal. No orbit representative,
coefficient, actual point, or derivative value has been chosen.

Two differential consequences will be used. First,

    (J_2^8)^- = J_1^8,     degree -14.                   (10)

The inclusion of J_1^8 in the backward kernel is immediate from the
osculating construction. The generic third jet is independent, since the
five sections have nonzero Wronskian. Hence the second fundamental form
has generic rank one. Its kernel is saturated, and J_1^8 is also saturated
in J_2^8, so the equal-rank inclusion is equality. Possible third-jet
ramification does not change this kernel sheaf.

Second, the saturated forward transform satisfies

    (J_1^10)^+ = J_2^10.                                (11)

Indeed the second jets are independent everywhere. This also follows
by taking the saturated sheaf generated by the first-jet bundle and its
derivatives.

## 4. The D shear cannot vanish on A0 modulo U

Equip Sym^10 W with its invariant nondegenerate apolar pairing. Distinct
irreducible summands are orthogonal, and its restriction to the unique D
summand is nondegenerate. The apolar annihilator of U_8^10 is U_1^10.
It follows that

    K = (D O) intersect U_8^10 = ann_D(J_1^10).           (12)

Because J_1^10 is saturated, K is a saturated rank-three subbundle of
D O. Dualizing its defining sequence shows

    deg K = deg J_1^10 = -18.                            (13)

The sign in (13) is important: D O/K=(J_1^10)*, so deg K is the
negative of the positive degree of that quotient.

Suppose, contrary to the desired nonvanishing, that T0(A0) is contained
in U_8^10. The image of A0=U_2^8 under its D projection is

    I=J_2^8.

By Section 3 it is saturated, of rank three and degree -18. Under the
nonzero constant D intertwiner in (8), the supposed containment says
I is contained in K. Both have the same rank and degree, so I=K as
subbundles of the same constant D space. Equivalently, their torsion
quotient has length zero. Saturation also gives this equality directly.

Their backward Gauss kernels would then be equal. But (10) gives

    rank I^- = 2,     deg I^- = -14.

On the other hand, constant-pairing annihilator duality and (11) give

    K^- = ann_D((J_1^10)^+)=ann_D(J_2^10),
    rank K^- = 2,     deg K^- = deg J_2^10 = -24.         (14)

To see the duality without imposing an extra hypothesis, differentiate
<s,t>=0 for sections s of ann(J_1^10) and t of J_1^10. The condition
that ds still annihilate J_1^10 is exactly that s annihilate its first
forward transform. Saturation gives the same annihilator. Thus (14)
is an identity for the original constant connections.

The degrees -14 and -24 are incompatible. Therefore

    A0 --T0--> V0 O --> Z

is nonzero. By (7), the restriction eta=(T0 mod U)|_R spans Hom_G(R,Z).

## 5. Kill the entire first coupling by a constant automorphism

There is a unique scalar c such that beta=c eta. Its existence is all
that is used; its value is neither selected nor computed. The constant
G-equivariant shear

    g(v,h)=(v-c T0(h),h),    v in V0, h in Hbar,           (15)

is invertible, is the identity on V0, and induces the identity on the
constant quotient Hbar. It therefore leaves the actual projected R
unchanged and transforms the graph (5) into the zero graph. Taking the
preimage before quotienting by U yields the equality

    g(Q*)=U direct-sum R

inside V0 O direct-sum Hbar O. This proves (1). Because g is constant,
it preserves the ambient flat connection and all its Gauss constructions.

Dually the actual annihilator inclusion splits as

    E=E0 direct-sum ER in V0* O direct-sum Hbar* O,
    E0=ann_V0*(U)=W O(-9).                              (16)

The corresponding quotient block is Q0=U*=Sym^8 W O(2). In particular
Q0 is not Z from (4).

## 6. The reconstruction recovers the fixed actual pencils

Write L for the actual negative two-space. The original actual maps are

    A_l:M2 -> M3,    B_l:M3 -> M4,

with A_l injective and B_l surjective for every nonzero l, and
B_u A_v=B_v A_u. The original Gauss gate identifies the actual constant
plane-section space with

    H=ker[(B_u,B_v):M3+M3 -> M4]
        / im[(A_v,-A_u):M2 -> M3+M3].                    (17)

It also identifies the actual quotient Q with D_lin(1), where

    0 -> M2 O(-1) --A--> M3 O -> D_lin -> 0,             (18)

and the quotient map from (17), at the formal parameter [a:b], is

    [(x,y)] -> [a y-b x] in D_lin(1).                   (19)

The following verification uses arbitrary basis symbols u,v and arbitrary
homogeneous variables a,b. It is an identity on the parameter line, not
an evaluation at a selected source parameter.

Define the reconstructed spaces and maps by

    N2=H^0(Q(-2)), N3=H^0(Q(-1)), N4=H^1(E),
    A_rec,t(n)=tn,   B_rec,t(s)=delta(ts),               (20)

where delta is the connecting map of 0->E->H O->Q->0. Formula (18)
gives canonical isomorphisms N3=M3 and N2=M2, up to the fixed determinant
convention for L. The symplectic identification associates

    l=alpha u+beta v    with    t_l=beta a-alpha b.

This section of O(1) vanishes at the parameter [alpha:beta].

Here is an explicit universal verification of the first map. Under
N2=M2, an element n has local representatives

    [A_v n] tensor (1,b/a) on a!=0,
    [-A_u n] tensor (a/b,1) on b!=0                     (21)

in D_lin(-1). They agree because a A_u n+b A_v n=0 in D_lin. Formula
(21) realizes the connecting isomorphism arising by twisting (18) by
O(-1); H^0 and H^1 of M3 O(-1) vanish. Multiplication by t_l gives, on
a!=0,

    [(beta-alpha b/a) A_v n]=[alpha A_u n+beta A_v n].

Thus, under N2=M2 and N3=M3,

    A_rec,t_l = A_l.                                    (22)

For the second map, take global sections of (18) twisted by O(1).
Using (19) to fix the coordinate convention gives

    H^0(Q)=(M3+M3)/im(A_v,-A_u).                        (23)

The map (B_u,B_v) descends to (23) by commutativity. Its kernel is
exactly the actual H in (17), with precisely its actual map to H^0(Q)
by (19). It is surjective because, for example, B_u is surjective.
Since H^0(E)=0 and H^1(H O)=0, the actual cohomology sequence therefore
identifies N4=H^1(E) with M4 so that delta is this descended map.
The section t_l m is represented in (23) by (alpha m,beta m). Hence

    B_rec,t_l(m)=alpha B_u m+beta B_v m=B_l(m).           (24)

Equations (22) and (24) prove simultaneous identification with the fixed
original tensors. They do not rely on independently chosen isomorphisms
between representations. The construction is equivariant; the displayed
basis expressions just verify the natural maps. A common sign change in
boundary conventions only changes constant gauges, not the conclusion.

## 7. The forced tensor idempotents

The reconstruction (20) commutes with constant direct sums. Apply it to
(16) and Q=Q0 direct-sum QR. The degree-ten block is

    N2,0=H^0(Q0(-2))=Sym^8 W=P+D,
    N3,0=H^0(Q0(-1))=Sym^8 W tensor W=W'+S+2T,
    N4,0=H^1(E0)=W tensor Sym^7 W=V+2P+D.                (25)

Its dimensions are (9,18,16). The canonical block is determined by the
exact constant inclusion

    0 -> W O(-9) -> Sym^10 W O -> Sym^8 W O(2) -> 0

and (20). Thus the actual tensors admit G-equivariant idempotents e2,e3,e4
satisfying

    ei^2=ei,
    e3 A_l=A_l e2,
    e4 B_l=B_l e3                                       (26)

for every l in the same actual negative two-space, with image characters
(25). In fact their restricted pencil system is isomorphic to the stated
canonical degree-ten block. The weaker condition consisting only of
(25)-(26) is already a necessary fixed-tensor condition.

Subtracting (25) from the original characters

    M2=A+2V+3P+4D,
    M3=3W'+3S+6T,
    M4=2V+4P+3D

gives complementary characters

    A+2V+2P+3D,    2W'+2S+4T,    V+2P+2D,

of dimensions (32,36,21). No existence or nonexistence of the idempotents
for the fixed HM tensors has been decided here.

## 8. Corollary: two full constant-gauge orbits over each balanced endpoint

Let B be the balanced endpoint locus of PR754, and let

    H_t=A+V+(P tensor t) subset H^0(O(18)),
    F_t=H_t*,    c_t:O(-18) -> F_t O,    t in B.

Here t is a line in the two-dimensional P-multiplicity space. Consider
full 30-dimensional G-equivariant constant inclusions with the exact
structural inputs of Section 1 and this balanced endpoint, up to
G-equivariant constant ambient isomorphisms covering the identity of X.
This is an abstract constant-embedding problem containing every
hypothetical actual source2 inclusion with those inputs; it is not the
problem of realizing a prescribed HM module.

Together with PR789, the theorem gives exactly two such full gauge
orbits over each t: residual coupling zero and residual coupling
nonzero. Different values of t cannot be identified by the allowed
constant equivalences. This is a statement about a set of gauge orbits,
not a product moduli scheme, a canonical family of representatives, or
a choice of a global nonzero coupling.

To prove that no extra full ambient equivalence identifies the two
residual classes, put an inclusion into (1). Constant direct sums
commute with backward Gauss transforms. The complete block identities
and PR789's residual flag give

    R^- = U_1^8,    R^{--}=U_0^8,    R^{---}=0,
    (Q*)^{(-8)}=U_0^10,    (Q*)^{(-9)}=0.                (27)

The full constant span of U_0^10 is V0=Sym^10 W. Thus V0 can be recovered
intrinsically from the full inclusion as the constant span of its eighth
backward transform. Every constant equivalence commutes with these
transforms, so it must carry V0 onto the corresponding target V0 and
therefore descend to an equivalence of the genuine residual inclusions.
In the residual, the constant span of R^{--}=U_0^8 intrinsically recovers
V1 inside H*/V0. Its intersection with R recovers A0=U_2^8. The final
constant quotient then recovers the endpoint c_t.

If an induced constant endpoint isomorphism d:F_t -> F_s sends c_t(C)
to c_s(C), its restriction gives an automorphism of C=O(-18), hence a
nonzero scalar lambda. Consequently

    d c_t = c_s lambda.

Dualizing and taking global sections shows that the two embedded
section spaces H_t and H_s in H^0(O(18)) are equal: their evaluation
maps differ only by an invertible change of domain and multiplication
by lambda. Since their P-isotypic parts are P tensor t and P tensor s,
this forces t=s. For this fixed endpoint the descended residual
isomorphism preserves V1, A0, and the quotient endpoint, so it belongs
to precisely the full stabilizer treated in PR789. Its zero/nonzero
coupling distinction therefore cannot be erased by a larger full
ambient equivalence.

Conversely, every residual equivalence extends by the identity on the
separated V0 block. PR789 constructs a residual in each of its two
classes for every balanced t, and adjoining U_8^10 produces full
constant inclusions with all the exact structural data and the forced
bundle splittings used here. Sections 2–5 put every full inclusion in
this class into such a form. This proves existence and exhaustiveness
of the two abstract full gauge orbits.

Neither orbit is asserted to occur for the fixed actual HM tensors.
For an actual source the endpoint and residual zero/nonzero class
remain undetermined; the fixed-pencil idempotent condition (26) is
still only a necessary condition, not a performed tensor test.

## Scope of the new reduction

The theorem strengthens the structural necessary form of an actual
source2 inclusion: its entire degree-ten block can be separated by a
constant equivariant shear. It does not constantly split R into its
rank-three osculating part and final degree-eighteen line, and it does
not turn PR788's abstract split witness into an HM realization.

Only published exact bundle inputs, universal characters, invariant
orbit-size bounds, arbitrary-point Wronskian arguments, constant
annihilator duality, and natural exact sequences are used. No actual
coefficients, parameters, points, derivatives, matrices, source-instance
ranks, scans, selected models, or large computations were evaluated.
This is a written structural proof, not proof-assistant certification.
