# The complete universal projective radical rank stratification for source2

## Result and scope

Work over C. Let G be the binary icosahedral group, W its defining
two-dimensional representation, and X=P(W), with W=W* through the
invariant symplectic form. Put

    A=Sym^2 W, S=Sym^3 W, D=Sym^4 W, T=Sym^5 W,

and denote the other three-, four-, and two-dimensional irreducibles by
V, P, and W'. All maps cover id_X and keep the same two pencil variables.

For every balanced degree-eighteen endpoint and every residual coupling
in the source2 constant normal forms, let J be the two-dimensional
square-zero radical of its fixed-pencil endomorphism algebra. Its
projective line has exactly the following rank strata:

    the V-channel direction:           (5, 6, 4);
    one additional direction:          (9,12, 9);
    every other direction:             (9,18, 9).

The additional direction is different from both the A and V directions.
Under the universal A/V channel identifications, it is independent of
the balanced endpoint and of the residual coupling. It is characterized
intrinsically by the splitting of an equivariant extension constructed
below. No scalar coordinate or actual-source parameter is assigned to
it. Independent rescalings of channel generators change a coordinate
description, not the distinguished projective direction.

The corresponding image characters are respectively

    (D,T,P),
    (P+D,W'+S+T,P+D),
    (P+D,W'+S+2T,P+D).

This is the complete set-theoretic projective rank stratification over
the entire stated normal-form family. It is not a calculation at an
actual HM/source instance or a selected member of that family. Its
transfer to the original actual source2 tensors remains conditional on
the actual-source hypotheses and reconstruction theorem of PR790.

## 1. Exact dependencies and universal data

The following published proofs in Akilleez-QA/read-em-and-weep were read
at the specified immutable commits:

- [PR791, exact pencil endomorphism algebra](https://github.com/Akilleez-QA/read-em-and-weep/blob/2cd033a4a5ba549d07330427cd779364cb83c0fb/research/hm/source2-pencil-endomorphism-algebra/PROOF.md),
  commit 2cd033a4a5ba549d07330427cd779364cb83c0fb, proof SHA-256
  8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290.
- [PR792, degree-six V-channel image pencil](https://github.com/Akilleez-QA/read-em-and-weep/blob/2f01f18960ce56b8b2a0c1260c277de3c5f916bf/research/hm/source2-radical-rank-profile/PROOF.md),
  commit 2f01f18960ce56b8b2a0c1260c277de3c5f916bf, proof SHA-256
  0d4eb3e4e9e98dd9ea8202399590f9741c06771411d5ce40e69a139c461b3798.
- [PR793, universal A-channel radical image profile](https://github.com/Akilleez-QA/read-em-and-weep/blob/ba9234964af5d879675d19ae97847a9475792f98/research/hm/source2-a-channel-rank/PROOF.md),
  commit ba9234964af5d879675d19ae97847a9475792f98, proof SHA-256
  7a9e75e9f1d22bb058039a94452e6edc1b788faa6e716dc5489f877346ab170a.
  Sections 3-6 are the A-channel inputs below.

The first two public contents were also checked against local Git blob
identifiers 5a0d16a2f22032f1a0583b92ad71661b5abab59d and
76bee93507d1a2d0840926d4e4e27edadfebb7d7, respectively. The frozen
A-channel digest was checked directly. These proofs carry their stated
dependencies on [PR790](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md)
at af0e03d26da5e47d18ae732291aca46f4d448dc5 and on the arbitrary-coupling
annihilator sequence of [PR789](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md)
at 2d1642ad40ae1111b84b50eeaca0426bfbfbb314.

Here are the precise data used. There is a genuine constant separated
first block with evaluation sequence

    0 -> E0 -> V0* O -> Q0 -> 0,
    V0*=Sym^10 W=A+V+D,
    E0=W O(-9), Q0=Sym^8 W O(2).                    (1)

The arbitrary balanced endpoint has section space and kernel

    H_t=A18+V18+P_t subset H^0(O(18)),
    E_C=ker(H_t O -> O(18))=(P+D)O(-2).             (2)

The unique A18 subsystem is basepoint-free, and V18=f12 V6, where
f12 is a nonzero invariant orbit form, with no chosen coefficients or
normalization. The subsystem V6 in Sym^6 W is basepoint-free. Write

    0 -> E_A -> A18 O -> O(18) -> 0,
    0 -> E_V -> V6 O -> O(6) -> 0.                  (3)

The A and V constant projections of V0* induce morphisms from (1) to
the two sequences (3), with kernel maps and quotient maps

    g_A:E0 -> E_A,        q_A:Q0 -> O(18),
    g_V:E0 -> E_V,        q_V:Q0 -> O(6).            (4)

The A theorem proves g_A is an isomorphism, E_A=W O(-9), and

    0 -> (V+D)O -> Q0 --q_A--> O(18) -> 0.          (5)

Thus H^0(q_A(-2)) is injective with image P+D, while H^0(q_A(-1))
is an isomorphism. PR792 proves

    E_V=W' O(-3),
    0 -> E0 --g_V--> E_V -> T12 -> 0,               (6)

with T12 a torsion sheaf, and proves that H^0(q_V(-2)) and
H^0(q_V(-1)) are onto H^0(O(4)) and H^0(O(5)). In particular the
middle V-channel image has dimension six. Set

    q_V'=f12 q_V:Q0 -> O(18),
    r=g_V g_A^(-1):E_A -> E_V.                      (7)

For every residual coupling there are genuine inclusions

    O(18) -> R*,       E_C -> E_R,
    0 -> E_C -> E_R -> T O(-3) -> 0.                (8)

They are injective on H^0 after twists -2 and -1, and on H^1,
respectively. PR792 further proves the inclusion E_V->E_C, induced
by V6->V18 and multiplication by f12, is injective on H^1 for every
balanced endpoint. These are assertions about the actual maps, not
about abstract bundle complements.

The reconstruction spaces are H^0(Q(-2)), H^0(Q(-1)), H^1(E), with
Q=Q0 plus R* and E=E0 plus E_R. Each radical endomorphism kills the
residual domain, and its quotient map from Q0 factors through O(18)
in (8). Its last map factors through H^1(E_C) in (8). Consequently
we may compute all three images in these smaller spaces without any
loss from the residual coupling. PR791 supplies the entire radical
J=Achannel plus Vchannel and the correct contravariant duality to the
original pencil algebra.

## 2. A multiplication test for the two needed nonvanishings

Let delta_A and delta_A(1) denote the connecting maps of (3) and its
twist by one. Define

    beta = H^1(r) delta_A : H^0(O(18)) -> H^1(E_V),
    beta_1 = H^1(r(1)) delta_A(1)
                         : H^0(O(19)) -> H^1(E_V(1)). (9)

The universal characters supplied by the dependencies are

    Sym^6 W=V+P, Sym^7 W=W'+T,
    Sym^8 W=P+D, Sym^17 W=W'+S+2T,
    Sym^19 W=W+S+W'+2T,
    A tensor W=W+S, V tensor W=T,
    P tensor W=W'+T, D tensor W=S+T.                (10)

In particular

    H^1(E_A(1))=W tensor Sym^6 W=W'+2T,
    H^1(E_V(1))=W'.                                 (11)

The twist of (6) still has torsion cokernel, whose H^1 vanishes, so
H^1(r(1)) is onto. By (11) it is therefore nonzero on the unique W'
in its source. The twisted A evaluation sequence has H^0(E_A(1))=0
and H^1(A18 O(1))=0. Hence delta_A(1) is onto, with kernel exactly
the image of A18 tensor W, whose character is W+S. It follows that

    beta_1 is nonzero on the unique W' in Sym^19 W.  (12)

Here and below a statement about the unique W' means its intrinsic
isotypic subspace; no vector or point is selected.

For any subspace L of H^0(O(18)), naturality of connecting maps,
multiplication, and the O-linear map r implies

    beta(L)=0  =>  beta_1(L W)=0,                    (13)

where L W denotes the image of multiplication L tensor H^0(O(1)).
Indeed for every formal linear form l and s in L,
beta_1(l s)=H^1(m_l) beta(s). Thus (12) obstructs vanishing in (13)
whenever L W contains a nonzero W' subrepresentation.

First apply this with L=f12 Sym^6 W. Ordinary multiplication
Sym^6 W tensor W -> Sym^7 W is onto, and multiplication by the
nonzero form f12 is injective. Thus L W=f12 Sym^7 W contains its
nonzero W' summand, giving

    beta(f12 Sym^6 W) is not zero.                  (14)

Second apply it with L=P_t. Balancedness in (2) makes E_C(1)
acyclic, so its evaluation sequence gives an isomorphism

    H_t tensor W -> H^0(O(19)).                     (15)

By (10) the unique W' in its domain comes from P_t tensor W, not
from A18 tensor W or V18 tensor W. Its image is nonzero by (15),
and therefore

    beta(P_t) is not zero for every balanced t.     (16)

Both conclusions are uniform structural statements. They use neither
a chosen endpoint nor a calculation of a derivative, coefficient, or
rank at a point.

## 3. The universal extension and its nonzero pushout

Identify V18 with V6 as a constant representation via f12, and put

    E_AV=ker((A18 plus V6)O -> O(18)),
    (a,v) |-> ev_A(a)+f12 ev_6(v).                   (17)

This evaluation is onto because A18 is basepoint-free. The map

    E_AV -> O(6), (a,v) |-> ev_6(v)

is onto: locally lift a section of O(6) using ev_6 and then cancel
its f12 multiple using ev_A. Its kernel is exactly E_A plus E_V.
We have an exact sequence of vector bundles

    0 -> E_A plus E_V -> E_AV -> O(6) -> 0.         (18)

Let eta_A and eta_V be the extension classes of the evaluations (3).
With the displayed sign convention, (18) is the pullback of their
direct sum by O(6)->O(18) plus O(6), s|->(-f12 s,s). Its components
are consequently

    xi_A=-f12^* eta_A,       xi_V=eta_V.             (19)

The equivariant extension space relevant to the second component is

    Ext^1_G(O(6),E_V)
      = H^1(E_V(-6))^G
      = (W' tensor Sym^7 W)^G,

which is one-dimensional by (10). Taking G-invariants is exact over C,
so this is also the extension group in the equivariant category. The
class xi_V is nonzero: a splitting of its evaluation sequence would
give a nonzero map O(6)->V6 O, whereas Hom(O(6),V6 O)=0.

The pushout r_*xi_A is nonzero as well. Its connecting map on H^0
is, by (19), the negative of beta composed with multiplication by
f12 on H^0(O(6)). This is nonzero by (14); a zero extension class
would have zero connecting map. Therefore

    r_*xi_A is a nonzero element of C xi_V.          (20)

This is the crucial nonvanishing. It does not follow merely from the
one-dimensional extension space, and (14) proves the missing geometric
content without computing its scalar of proportionality.

## 4. The exact middle-rank locus

To analyze all mixed directions, choose arbitrary nonzero generators
of the two one-dimensional channel spaces, and use a formal variable
z for their relative coefficient. No value is evaluated. Write

    q_z=q_A+z q_V',       z nonzero.                 (21)

The corresponding constant map is

    p_z:V0* -> A18 plus V6, v |-> (p_A(v),z p_V(v)).

It is onto with kernel D, since the two projections have different
irreducible supports. Its kernel map from (1) into (17) is

    E0 -> E_A plus E_V -> E_AV,
    e |-> (g_A(e),z g_V(e)).                         (22)

Using g_A, the first arrow is the graph of z r. Its quotient inside
E_A plus E_V is E_V through (x,y)|->y-z r(x). Thus the graph is
saturated there, notwithstanding the torsion cokernel of g_V alone.
Define its quotient in E_AV by K_z. Sequence (18) yields

    0 -> E_V -> K_z -> O(6) -> 0.                   (23)

In particular K_z is locally free: locally an extension of locally
free sheaves splits. Hence the graph is also saturated in E_AV.
By pushout, the exact extension class of (23) is

    xi_V-z r_*xi_A.                                 (24)

Both terms are nonzero in the same one-dimensional space by (20).
It follows that there is exactly one mixed projective direction for
which (24) vanishes. This direction is not either coordinate axis.
We use only its intrinsic vanishing characterization, not a scalar
coordinate for it.

At that direction the equivariant extension splits, giving

    K_z=E_V plus O(6).

At every other mixed direction its class is a nonzero multiple of
xi_V. Rescaling the kernel or quotient identifies every such nonzero
extension with the degree-six evaluation extension (3). Consequently

    K_z is equivariantly isomorphic to V6 O

at all those directions. This conclusion concerns the extension
classification; it does not presume that an arbitrary rank-three
degree-zero bundle is trivial.

Apply the snake lemma to the morphism from (1) to the evaluation
sequence defining E_AV, with maps (22), p_z, and q_z. Since p_z is
onto and (22) is injective, it proves q_z is onto and gives

    0 -> D O -> ker q_z -> K_z -> 0.                (25)

After twisting by -1, D O(-1) is acyclic, so

    H^0(ker q_z(-1)) = H^0(K_z(-1)).                (26)

For a nonsplit extension the right side is zero. For the split
extension it is H^0(O(5))=T, of dimension six, since E_V(-1) has
no sections. The domain H^0(Q0(-1)) has dimension eighteen. Thus
the mixed middle rank is twelve at the single split direction and
eighteen everywhere else. In representation terms the corresponding
images have characters W'+S+T and W'+S+2T.

The pure A direction has middle rank eighteen by (5), and the pure
V direction has middle rank six by PR792. This accounts for every
point of the projective radical, including the direction not covered
by the affine expression (21).

## 5. Every non-V direction has first rank nine

Put I_A=im H^0(q_A(-2)) and I_V=im H^0(q_V'(-2)). They have
characters P+D and D, respectively. Their D subrepresentations are
distinct. Suppose instead that those subrepresentations were equal.
Schur's lemma would give

    H^0(q_V'(-2))=H^0(q_A(-2)) L0,

where L0 is the equivariant endomorphism of Sym^8 W=P+D which is
zero on P and a nonzero scalar on D. A map from the trivial bundle
Q0(-2)=Sym^8 W O is determined by its map on constant sections.
The asserted equality therefore gives the bundle identity

    q_V'=q_A L,

with L=L0 tensor id_O(2). On sections after twist -1 the map q_A
is an isomorphism, while L has image D tensor W, of dimension ten.
This would make H^0(q_V'(-1)) have image dimension ten, contradicting
its proven dimension six. The D subrepresentations are distinct.

As irreducible subrepresentations, two distinct copies of D have
zero intersection, and neither meets the P image. Therefore any
linear combination with a nonzero A coefficient is injective on
the source P+D: it cannot cancel on D, and it is nonzero on P.
Its first rank is nine and its image character is P+D. The pure
V direction has first rank five. This argument does not choose
coordinates in a multiplicity space or form any rank matrix.

## 6. Every non-V direction has final rank nine

Use g_A to identify H^1(E0) with H^1(E_A). Let

    a:H^1(E_A) -> H^1(E_C)

be induced by the inclusion E_A->E_C, and let

    b:H^1(E_A) --H^1(r)--> H^1(E_V) -> H^1(E_C)

be the V-channel map. The A proof and the evaluation exact sequences
identify

    H^1(E_A)=H^0(O(18))/A18=V+2P+D,
    H^1(E_C)=H^0(O(18))/H_t=P+D,
    ker a=delta_A(V18 plus P_t)=V+P.                (27)

The map a is onto, while b has image the unique P in the target;
the last arrow defining b is injective by PR792. By (16), b is
nonzero on the P summand delta_A(P_t) of ker a. Hence the restrictions
of a and b to the P-isotypic part of H^1(E_A) are linearly independent.
In particular every linear combination with a nonzero coefficient
of a remains nonzero on that isotypic part: otherwise it would give
a proportionality contradicting the nonzero restriction of b to
ker a. Such a nonzero equivariant map onto the irreducible P is onto.

On D the map b is zero by Schur's lemma, and a is an isomorphism
onto the target D by (27). Thus every combination with nonzero A
coefficient has image P+D and final rank nine. The pure V direction
has final image P and rank four. The injection H^1(E_C)->H^1(E_R)
from (8) preserves these images for every residual coupling.

## 7. The reduced middle comparison operator and determinant divisor

There is also a coordinate-free refinement of the middle-rank locus.
Put U=H^0(Q0(-1)) and B=H^0(O(17)), and denote the A and V maps
between them by u_A and u_V. The A map is an isomorphism, so the
comparison operator

    s=u_A^(-1) u_V : U -> U

is defined after choosing nonzero channel generators. Its image is
an irreducible T of dimension six. By Schur's lemma its restriction
to its image is a scalar c, and therefore s^2=c s. The scalar cannot
be zero: otherwise id_U+z s would have inverse id_U-z s for every
formal z, contradicting the mixed singular direction proved above.
Thus s/c is a projector with image dimension six and kernel dimension
twelve.

Taking determinants in the reduced family of maps U->B now shows
that its determinant divisor on P(J) is exactly

    12 [V-channel direction] + 6 [additional direction].

Indeed the family acts by its A coefficient on the twelve-dimensional
kernel of s, and by a nonzero linear functional vanishing at the
additional direction on the six-dimensional image of s. This gives
the displayed multiplicities without computing a coefficient or
assigning a numerical coordinate to either direction.

This comparison projector is not an element of the square-zero
radical and does not describe multiplication in J. The determinant
here is only that of the reduced eighteen-dimensional map U->B,
not that of the full radical endomorphism in degree three. The latter
is always singular, since a radical endomorphism is square-zero.

## 8. Universality and the actual-source boundary

The extension (18), the maps q_A, q_V, g_A, g_V, and the split-class
condition (24) involve only the fixed first block, the unique A18
and V18 subsystems, and the degree-six evaluation. None involves
P_t or a residual graph. They therefore define the same additional
projective direction under the A/V channel identifications throughout
the entire normal-form family. Changing either nonzero channel
generator merely changes its coordinate description. No numerical
coordinate has been assigned, and this radical direction is not
identified with a choice of the endpoint t.

The sole endpoint-dependent nonvanishing needed for the other two
ranks is (16), proved for all balanced endpoints by the acyclicity
of E_C(1). The residual maps used in (8) are injective in exactly
the three required cohomological degrees for both coupling classes.
Consequently there are no additional rank strata depending on the
endpoint or coupling.

PR791 identifies these channels with the full radical, not a chosen
two-dimensional subspace of a larger radical. Its fully faithful
reconstruction, together with PR790 under the latter's actual-source
hypotheses, transfers the result to the same fixed original pencils.
Duality reverses multiplication but preserves these ranks and the
square-zero property. No change of pencil variables is used.

All arguments are structural: equivariant evaluation sequences,
saturation and locally free quotients, one-dimensional extension
classes, natural multiplication and cohomology, and Schur's lemma.
No actual HM/source coefficient, endpoint value, point, derivative
value, tensor, matrix, instance rank, selected model, scan, or large
computation has been chosen or evaluated. No realization or exclusion
of source2 is claimed. This is a written deductive proof, not
proof-assistant certification.
