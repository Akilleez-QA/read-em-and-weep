# The exact equivariant endomorphism algebra forced by source2

## Result and boundary

Work over C. Let G be the binary icosahedral group, W its defining
representation, and X=P(W), with the invariant symplectic identification
W=W*. Put A=Sym^2 W and D=Sym^4 W; let V and P be the other three- and
four-dimensional irreducibles. All maps below are over id_X. The negative
two-space, and hence both pencil variables, remain fixed throughout.

Conditionally on the actual-source hypotheses and first constant block
theorem specified in Section 1, the entire algebra of degree-preserving
G-equivariant endomorphisms of the fixed source2 negative pencil system
has one of exactly two abstract algebra types:

    residual quotient coupling zero:       C times T(J), dimension 5;
    residual quotient coupling nonzero:    T(J),         dimension 4.

Here J is a two-dimensional vector space, and T(J) is the algebra whose
underlying vector space is C plus C plus J, with multiplication

    (a,d,b)(a',d',b') = (aa',dd',a b' + d' b).          (1)

In both cases the Jacobson radical is J, of dimension two and square
zero. The semisimple quotient is C^3 in the zero-coupling case and C^2
in the nonzero-coupling case. T(J) is the two-vertex triangular algebra
with two parallel arrows; its opposite is isomorphic to itself.

This is an exact necessary algebra constraint, not just the existence of
a projector or a lower bound on the endomorphism dimension. It holds for
every balanced endpoint and every residual coupling in the stated normal
forms, including noninvertible endomorphisms. It does not calculate this
algebra for the actual HM tensors, determine their residual class, or
exclude source2. The algebra concerns these two negative multiplication
pencils only, not the endomorphisms of the full HM module or HM bundle.

## 1. Exact dependencies and the normal forms

The repository is Akilleez-QA/read-em-and-weep. The direct published inputs
were read at the following immutable pins:

- [PR788, universal constant flag and common-pencil reconstruction](https://github.com/Akilleez-QA/read-em-and-weep/blob/941b7b3b77dc8ae8a19b1e000dddeb0438d05db7/research/hm/source2-universal-constant-flag/PROOF.md),
  commit 941b7b3b77dc8ae8a19b1e000dddeb0438d05db7, especially Section 6.
- [PR789, residual coupling normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md),
  commit 2d1642ad40ae1111b84b50eeaca0426bfbfbb314, especially Sections 2–6.

- [PR790, first constant block and fixed-pencil summand](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md),
  commit af0e03d26da5e47d18ae732291aca46f4d448dc5, proof SHA-256
  0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4.

PR790, Sections 1–5, gives the full constant splitting and restriction
nonvanishing used below; its Section 6 identifies the canonical
reconstruction with the original actual tensors, not merely their
characters. Its Section 8 establishes the intrinsic full backward flag.
The present theorem is conditional on the actual-source hypotheses
explicitly stated there; no unpublished mathematical dependency is used.

The earlier actual-source inputs of that dependency are PR744 at
2348d4b6fb2afd67d66b15aad6037ab92c94f076, PR751 at
e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169, and PR758 at
063216038f3aefd65617651c2426721efafc7f9b, in
research/hm/order-four-quadratic-load/. Their exact source paths are,
respectively, TWO-ONE-INDEX-TWO-CONSTANT-SPAN-INTERSECTION.md;
TWO-ONE-INDEX-TWO-RESIDUAL-FULL-SPAN.md and
TWO-ONE-INDEX-TWO-RESIDUAL-OSCULATIONS.md; and
TWO-ONE-INDEX-TWO-EXACT-RESIDUAL-GAUSS-FLAG.md. The actual common-pencil
origin at the PR758 pin is the one in
POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md, together with
UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md and
ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md.

We state all the normal-form data used, so the conditional theorem also
makes sense directly for any abstract inclusion with these data. Write

    U_j^e = Sym^j W O(j-e) subset Sym^e W O,
    (U_j^e)_ell = ell^(e-j) Sym^j W.

For every balanced endpoint t of PR754, let

    Hcal_t=A+V+(P tensor t) subset H^0(O(18)),
    F_t=Hcal_t*,  C=O(-18),  c_t:C -> F_t O.

The endpoint has full constant span F_t and F_t=A+V+P. The balanced
locus is the one at PR754, commit
044add76ebb14043a0edf73171517c90b9ef0c13,
research/hm/order-four-quadratic-load/ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md.
No value of t is chosen.

The first block theorem puts the full inclusion into the genuine constant
normal form

    H*=V0 direct-sum Hbar,       Q*=U direct-sum R,
    V0=Sym^10 W=A+V+D,           U=U_8^10,
    Hbar=V1 direct-sum F_t,      V1=Sym^8 W=P+D.        (2)

Here R is a saturated subbundle, and

    R intersect V1 O = A0=U_2^8,
    0 -> A0 -> R -> C -> 0                             (3)

is induced by the genuine constant projection to F_t O and c_t.
Set

    K=(V1 O)/A0,       Z=(V0 O)/U=W O(9).

PR789 represents R/A0 as the graph of an arbitrary

    alpha in Acoup=Hom_G(C,K),       dim Acoup=2.

The injective restriction map

    sigma_t:Hom_G(F_t,V1) -> Acoup,
    sigma_t(p)=(p c_t mod A0)                         (4)

has one-dimensional image L_t. The invariant residual datum is
[alpha] in Acoup/L_t; its zero/nonzero status is independent of the
constant complement. If [alpha]=0, a constant shear permits alpha=0.

For all alpha the exact backward flag is

    R^-=U_1^8,       R^{--}=U_0^8,       R^{---}=0.

Consequently in (2),

    (Q*)^{(-8)}=U_0^10,       (Q*)^{(-9)}=0.            (5)

Finally the first block theorem gives

    Hom_G(C,Z)=0,
    Hom_G(R,Z) -> Hom_G(A0,Z) is an isomorphism,
    dim Hom_G(R,Z)=1,                                  (6)

and the restriction, modulo U, of the constant D-channel map

    V1 -> D subset V0

is nonzero. This last assertion is geometric: it is proved there by
universal jet spanning and backward-degree incompatibility, not inferred
from a character multiplicity. It is indispensable below.

The annihilator E=ann(Q*) in H O and Q=(Q*)* have all splitting degrees
of E and Q* at most -2, as required by PR788. In fact

    E=W O(-9) plus Sym^5 W O(-3) plus (P+D)O(-2),
    Q*=Sym^8 W O(-2) plus A O(-6) plus O(-18)

as equivariant bundles. These abstract splittings are not declared
horizontal; only the displayed constant splitting (2) is used as such.

## 2. Noninvertible endomorphisms preserve the intrinsic constant flag

Let S be a subbundle of a constant bundle V O, and let f:V->V be constant
with f(S) contained in S. The second fundamental form is the composite
of the constant connection with projection to (V O)/S. Since

    d(f s)=f(ds)

for every local section s, f carries the kernel S^- into S^-.
Repeating proves preservation of every backward transform. No inverse,
constant-rank hypothesis on f, or preservation of a chosen complement is
used. This argument is for the actual kernel sheaves, so it does not
ignore special-point behavior.

We will also use a simple scalar lemma. If a line subbundle L subset V O
has full constant span and a constant map f preserves L, then f is scalar.
Indeed f|_L is multiplication by an element of H^0(O_X)=C, possibly zero.
Subtracting that scalar from f kills L and hence its full constant span.
This proves the statement for arbitrary endomorphisms, not just units.

Let

    E_Q= {f in End_G(H*): f(Q*) is contained in Q*}.     (7)

By (5) every f in E_Q preserves U_0^10. Its full constant span is V0,
so f preserves V0 and acts on it by a scalar a0. Thus f has a unique
form

    f(v,h)=(a0 v + b(h), d(h)),
    b in Hom_G(Hbar,V0),  d in End_G(Hbar).             (8)

Preservation of Q* in its constant splitting (2) is equivalent to

    d(R) contained in R,       b(R) contained in U.     (9)

In particular a nonzero map from V0 into the residual quotient is
impossible, even if f kills the eighth backward line: in that case it
kills all V0. This excludes additional lower off-diagonal ambient
channels without assuming invertibility.

For d in (9), the same argument using R^{--}=U_0^8 shows that d preserves
V1 and is scalar a1 on it. Its induced map on F_t preserves the endpoint
line C, so the scalar lemma and the full span of c_t give a scalar a2
on F_t. Therefore

    d(v1,z)=(a1 v1 + p(z), a2 z),
    p in Hom_G(F_t,V1).                                (10)

This is the full set of possible shapes, not a restriction to a preferred
subgroup. The entire constant flag is recovered from the inclusion.

## 3. The residual algebra, including its singular endomorphisms

Modulo A0, formula (10) sends the graph point
(alpha(c),c_t(c)) to

    (a1 alpha(c)+sigma_t(p)(c), a2 c_t(c)).

Its membership in the same graph is equivalent to the linear equation

    (a1-a2)alpha + sigma_t(p)=0 in Acoup.               (11)

There is no division by a1 or a2. Thus the equation covers all
noninvertible residual endomorphisms, including zero diagonal scalars.
Conversely (11), together with (10), suffices to preserve the inverse
image of the graph and hence R itself.

If [alpha]=0, first make the permitted constant shear with alpha=0.
Equation (11) and the injectivity in (4) then force p=0, while a1 and
a2 are arbitrary and independent. Hence in a split residual gauge

    End_G(Hbar;R)=C id_V1 plus C id_F_t.                (12)

If [alpha] is nonzero, reduction of (11) modulo L_t forces a1=a2.
Then (4) forces p=0. Therefore in every such graph chart

    End_G(Hbar;R)=C id_Hbar.                           (13)

Equations (12)–(13) are exhaustive algebras, not just classifications of
the invertible stabilizer. The proof allows alpha to vary arbitrarily
over both classes and t to vary over the entire balanced locus.

## 4. Exactly two upper off-diagonal channels survive

Schur's lemma and the characters in (2) give the direct sum

    Hom_G(Hbar,V0)=Dchannel plus Achannel plus Vchannel, (14)

each channel one-dimensional. The D channel is supported on the unique
D in V1; the A and V channels are supported on F_t and vanish on V1.
There is no P channel into V0.

The condition on b in (9) is the kernel of the linear restriction

    r:Hom_G(Hbar,V0) -> Hom_G(R,Z),
    r(b)=(b mod U)|_R.                                 (15)

By (6) this map is nonzero on the D channel. For a map in the A or V
channel, its restriction to R factors through the quotient R/A0=C,
because it vanishes on V1. Its composite with Z is therefore in
Hom_G(C,Z)=0. These two channels lie in ker r. They are independent
constant maps, so (14)–(15) show exactly

    ker r=J=Achannel plus Vchannel,      dim J=2.        (16)

In particular there is no cancellation that would allow a D component:
the other two channel images in the one-dimensional target are zero,
while the D image is nonzero. Notice that the factorization used is
through R/A0=C, not a claim that the maps vanish on C in V0 O. Their
images on C can be nonzero sections of U.

Extend b in J by zero on V0, giving an endomorphism n_b of H*. It sends
the residual space to V0 and kills V0, so

    n_b n_b'=0 for all b,b' in J.                     (17)

All these maps preserve Q*. They are genuine independent endomorphisms,
not extra choices of a parameter or changes in the pencil variables.

## 5. Multiplication, radical, and abstract algebra type

In the zero-coupling gauge of (12), every element of E_Q is specified
uniquely by (a0,a1,a2,b), with b in J. Composition, with the rightmost
factor acting first, is

    (a0,a1,a2,b)(a0',a1',a2',b')
      =(a0a0',a1a1',a2a2',a0 b' + a2' b).             (18)

The reason the right scalar is a2' rather than a1' is that every b in J
vanishes on V1 and is supported on the endpoint space F_t. Thus (18)
identifies E_Q with C times T(J), with the separate C acting on V1.
Its dimension is 5.

In the nonzero-coupling case (13), a1=a2 and every endomorphism is
specified by (a0,a2,b). Its multiplication is precisely (1). Hence
E_Q=T(J) and its dimension is 4.

In either case J is a two-sided ideal with J^2=0, and the quotient is
the product of three or two copies of C, respectively. A nilpotent ideal
of a finite-dimensional algebra lies in its Jacobson radical; the
semisimplicity of the displayed quotient forces the reverse inclusion.
Therefore J is exactly the radical, not merely a square-zero subideal.

These statements describe the whole constant ambient algebra. No
independent action on a repeated ambient irreducible has been omitted:
Section 2 forces scalar actions on the intrinsic full-span blocks, and
Sections 3–4 test every remaining channel permitted by their characters.

## 6. Full faithfulness of the common-pencil reconstruction

We now establish the morphism statement needed to transfer the exact
algebra, rather than just selected projectors, to the fixed pencils.

Consider G-equivariant exact sequences on the same X

    0 -> E -> H O -> Q -> 0,                           (19)

with every splitting degree of E and Q* at most -2. A morphism from
(19) to another such sequence is a G-equivariant constant linear map
h:H->H' satisfying h(E) contained in E'. It induces a quotient map
q:Q->Q'. All maps cover id_X and use the same linear forms.

PR788 reconstructs

    N2=H^0(Q(-2)),  N3=H^0(Q(-1)),  N4=H^1(E),
    A_l(r)=l r,    B_l(s)=delta(l s),                  (20)

where delta:H^0(Q)->H^1(E) is the connecting map. A pencil morphism is a
triple (e2,e3,e4) satisfying

    e3 A_l=A'_l e2,    e4 B_l=B'_l e3                 (21)

for every l in the fixed two-space of linear forms. Naturality of
cohomology and multiplication sends a morphism h to such a triple and
preserves addition and composition.

We prove this functor is fully faithful, allowing arbitrary morphisms.
Fix independent basis symbols u,v of the same two-space; this is only a
universal verification, not a chosen actual parameter. PR788 gives

    H = ker(B_u,B_v)/im(A_v,-A_u),                     (22)

by identifying the class of a cycle (x,y) with the unique h whose
Q-section is u x+v y. Both assertions needed for this identification
hold: H^0(E)=0 makes H->H^0(Q) injective, and H^1(Q(-2))=0 makes every
Q-section expressible as u x+v y via the sheaf Koszul sequence.

Given any triple satisfying (21), the maps e2, e3 plus e3, and e4
form a map of the complexes in (22), so they induce a constant map
h:H->H'. Also (21) for A gives a map of the natural evaluation sequences

    0 -> N2 O(-1) -> N3 O -> Q(-1) -> 0.             (23)

Here the first map at the point where l vanishes is multiplication by
l, with the fixed determinant convention. Consequently e2 and e3
induce a unique bundle map q:Q->Q'. Since Q(-1) is globally generated,
(23) further gives

    H^0(q(-1))=e3.                                    (24)

For a cycle (x,y), the section of Q' determined by h is
u e3(x)+v e3(y), while applying q to its original section gives the
same expression by (24). Thus

    q composed with (H O -> Q)
      = (H' O -> Q') composed with h.                 (25)

This proves h(E) contained in E' as a bundle map, not just away from
exceptional parameters. It also identifies q as its actual quotient map.

The induced N2 map is e2: multiplication by any nonzero formal l is
injective on H^0(Q'(-2)), and the two candidates have the same composite
with A'_l by (21), (24), and multiplication naturality. The induced N4
map is e4 as well. Indeed every section of Q is u x+v y, and

    delta'(q(u x+v y))
      = B'_u e3(x)+B'_v e3(y)
      = e4(B_u x+B_v y)
      = e4 delta(u x+v y).                            (26)

The connecting map delta is surjective because H^1(H O)=0. Equation
(26) and the natural cohomology sequence therefore identify the induced
H^1(E) map with e4. This proves fullness.

For faithfulness, a morphism's quotient q is determined by e3 through
the globally generated evaluation (23). Its constant h is then determined
by (25), since H'->H^0(Q') is injective. Equivalently (22) reconstructs
it uniquely. The two procedures are inverse on all Hom spaces, are
G-equivariant, and respect composition. Hence the reconstruction is fully
faithful on these constant inclusions, not just injective on automorphism
groups or a map from one endomorphism algebra to another.

No assertion of essential surjectivity onto arbitrary commuting pencil
systems is needed. PR788 applies to all the normal forms here, and
Section 6 of the first block dependency identifies the reconstruction
of the actual inclusion with the fixed original actual pencils under
its published common-Koszul/Gauss origin. Thus the fully faithful Hom
identification applies to those fixed pencils conditionally on source2.

## 7. The opposite algebra and the fixed-tensor necessary condition

Let E_P denote the algebra of all degree-preserving G-equivariant triples
(e2,e3,e4) on the original M2,M3,M4 satisfying

    e3 A_u=A_u e2,   e3 A_v=A_v e2,
    e4 B_u=B_u e3,   e4 B_v=B_v e3.                   (27)

This definition fixes the two negative variables: no change of basis of
the parameter line is part of an endomorphism. Section 6 gives a covariant
algebra isomorphism from endomorphisms of E subset H O onto E_P.

Duality is contravariant. Explicitly, f in E_Q induces f*:H->H preserving
E=ann(Q*), and every constant map preserving E arises this way. Since
(f g)*=g* f*, it follows that

    E_P is isomorphic to E_Q^op.                      (28)

This orientation must not be suppressed. It changes the displayed arrow
direction, but not the result's abstract algebra types. The map

    (a,d,b) -> (d,a,b)

is an anti-isomorphism of T(J), as a direct check of (1) shows. Therefore
T(J)^op is isomorphic to T(J), and the same holds after multiplying by C.
Equations (18), (28) prove exactly the two types and radical assertions
stated at the start.

Consequently, if the fixed actual source2 pencils exist with the stated
source geometry, their full algebra (27) must have dimension 5 or 4,
and its multiplication must have the corresponding stated radical and
semisimple quotient. Within the proved normal-form class, dimension 5
is equivalent to zero residual quotient coupling, while dimension 4 is
equivalent to nonzero residual quotient coupling. Dimension alone is not
asserted sufficient for an arbitrary pencil system to lie in this class.

The endpoint t does not vary inside this algebra: endomorphisms are maps
of one fixed inclusion over id_X. Any ambient maps that could have mixed
its quotient constituents were already exhausted by (10)–(11). Allowing
base automorphisms or a change in the negative variables would be a
different symmetry problem and is expressly outside (27).

## Method and evidential scope

Only the pinned structural normal forms, functoriality of the original
constant connection, character multiplicities, exact sequences, natural
cohomology, and finite-dimensional algebra are used. All scalars and
bundle maps above are universal variables; no value of an actual endpoint,
coefficient, point, derivative, tensor, matrix, or source-instance rank
has been selected or evaluated. No scan, selected model, or large
computation was performed. The proof neither computes the actual HM
endomorphism algebra nor identifies an HM realization. It is a written
structural proof, not proof-assistant certification.
