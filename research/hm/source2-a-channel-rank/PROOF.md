# The universal A-channel radical image profile for source2

## Result and boundary

Work over C. Let G be the binary icosahedral group, W its defining
two-dimensional representation, and X=P(W). Use the invariant symplectic
identification W=W*. Put

    A=Sym^2 W, S=Sym^3 W, D=Sym^4 W, T=Sym^5 W,

and let V, P, W' be the other three-, four-, and two-dimensional
irreducibles. All these representations are self-dual.

For every balanced degree-eighteen endpoint and both residual coupling
classes in the source2 constant normal forms, a nonzero A-channel
element of the exact radical induces a square-zero degree-preserving
endomorphism (n2,n3,n4) of the fixed negative two-pencil system with

    (im n2, im n3, im n4) = (P+D, W'+S+2T, P+D),
    (rank n2, rank n3, rank n4) = (9,18,9).             (1)

The claim is uniform over that entire normal-form family. It is not a
rank calculation for a selected HM/source instance. Conditionally on
the actual-source inputs of PR790, it is a necessary constraint on the
fixed actual source2 tensors, not an evaluation or exclusion of them.

There is also a precise description of the image pencils. Let

    H_t=A18+V18+P_t subset H^0(O(18))

be the endpoint section space. There is a fixed, endpoint-independent
nine-dimensional subspace I_A of H^0(O(16)), with character P+D,
defined intrinsically in Section 5, such that the image system is

    I_A -> H^0(O(17)) -> H^0(O(18))/H_t,
    s |-> l s,       r |-> [l r],                     (2)

for each of the same fixed pencil variables l in H^0(O(1)). Both maps
have the required injectivity and surjectivity, respectively, for every
nonzero l. The description is uniform, but no claim is made that the
whole image system is independent of t up to pencil isomorphism.

In particular, (2) is not the full endpoint evaluation system: its first
space has dimension 9, not h^0(O(16))=17. An isomorphism in its middle
space does not remove this distinction.

## 1. Exact published inputs

The following sources in Akilleez-QA/read-em-and-weep were read at their
stated immutable pins:

- [PR789, residual coupling normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md),
  commit 2d1642ad40ae1111b84b50eeaca0426bfbfbb314. We use its arbitrary
  residual graph, genuine endpoint quotient, and exact annihilator
  sequence, including both coupling classes for every balanced endpoint.
- [PR790, first constant block](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md),
  commit af0e03d26da5e47d18ae732291aca46f4d448dc5. We use its constant
  splitting and its Section 6 identification of the natural
  reconstruction with the original actual pencils.
- [PR791, exact endomorphism algebra](https://github.com/Akilleez-QA/read-em-and-weep/blob/2cd033a4a5ba549d07330427cd779364cb83c0fb/research/hm/source2-pencil-endomorphism-algebra/PROOF.md),
  commit 2cd033a4a5ba549d07330427cd779364cb83c0fb. Sections 4-7 identify
  the A and V constant channels as the full square-zero radical and
  establish the contravariant transfer to the fixed pencils.
- [PR786, endpoint Wronskian](https://github.com/Akilleez-QA/read-em-and-weep/blob/575c0720268af5bb4b305e29284f65614ba9f9ca/research/hm/source2-endpoint-wronskian/PROOF.md),
  commit 575c0720268af5bb4b305e29284f65614ba9f9ca, Sections 1 and 3.
  We use the projective orbit sizes 12,20,30,60, the unique degree-twelve
  orbit, and perfectness of G. No endpoint Wronskian value is used.

These sources supply all the structural inputs stated below. The
universal A-subsystem and cohomological image arguments are proved here.
The proof does not depend on a rank assertion for the V channel.

## 2. Normal forms, orientation, and characters

Write

    U_j^e=Sym^j W O(j-e) subset Sym^e W O,
    (U_j^e)_[ell]=ell^(e-j) Sym^j W.

For an arbitrary balanced endpoint t, put

    H_t=A18+V18+P_t subset H^0(O(18)),
    F_t=H_t*, C=O(-18), c_t:C -> F_t O,
    E_C=ker(H_t O -> O(18))=(P+D)O(-2).              (3)

The relevant constant normal form is

    H*=V0 direct-sum Hbar, Q*=U direct-sum R,
    V0=Sym^10 W=A+V+D, U=U_8^10,
    Hbar=V1 direct-sum F_t, V1=Sym^8 W=P+D,
    R intersect V1 O=A0=U_2^8,
    0 -> A0 -> R -> C -> 0.                          (4)

The final map in (4) is the genuine constant projection to F_t O,
followed by identification with its saturated endpoint. R is allowed
to have either residual quotient coupling class. No constant splitting
of its last exact sequence is assumed.

Dualizing the separated first block gives

    E0=ann_V0*(U)=W O(-9), Q0=U*=Sym^8 W O(2),
    E_R=ann_Hbar*(R), E=E0 direct-sum E_R,
    0 -> E_C -> E_R -> T O(-3) -> 0.                 (5)

For these actual constant evaluation sequences, reconstruction is

    N2=H^0(Q(-2)), N3=H^0(Q(-1)), N4=H^1(E),
    A_l(s)=l s, B_l(r)=delta(l r).                   (6)

Here Q=Q0 direct-sum R*, and delta is the connecting map. PR790 identifies
(6) with the fixed original tensors under its actual-source hypotheses.

Let b:Hbar->V0 be a nonzero A-channel constant map. Thus b vanishes on
V1 and on the V and P constituents of F_t. PR791 gives b(R) contained
in U. Extend b by zero on V0 to obtain n:H*->H*. Then n is a nonzero
radical element and n^2=0. The pencil endomorphism is induced by

    h=n*:H=V0* direct-sum Hbar* -> H,

which maps V0* into the A18 constituent of H_t subset Hbar* and kills
Hbar*. This reverses the ambient arrow direction. The algebra transfer
is contravariant, as in PR791; the reconstruction (6) after dualizing
is covariant. No opposite-algebra direction is silently interchanged.

We record the universal character facts used. The Clebsch recurrence

    W tensor Sym^m W = Sym^(m+1) W + Sym^(m-1) W

and the standard G-products quoted in PR789 give

    Sym^6 W=V+P, Sym^7 W=W'+T, Sym^8 W=P+D,
    Sym^10 W=A+V+D,
    Sym^18 W=A+V+2P+D,
    Sym^19 W=W+S+W'+2T.                             (7)

For the specific middle character,

    (P+D) tensor W=(W'+T)+(S+T)=W'+S+2T.            (8)

Also W tensor Sym^18 W minus Sym^19 W gives

    Sym^17 W=W'+S+2T.                               (9)

Indeed W tensor A=W+S, W tensor V=T, W tensor P=W'+T,
and W tensor D=S+T, so that subtraction is explicit. In particular A18
is a unique irreducible subspace. These are universal representation
identities, not evaluations of an actual tensor or parameter.

## 3. The unique A18 subsystem and its kernel

First A18 is basepoint-free. Its common base divisor B is G-invariant.
If nonempty, deg B is at most 18. The projective orbit sizes are exactly
12,20,30,60, so necessarily B is the unique reduced orbit D12. The
lower bound 12 alone would not justify this conclusion; the full list
of orbit sizes is what rules out intermediate possibilities.

Let f12 be any nonzero form with divisor D12. Its line is G-stable and
G is perfect, so f12 is invariant. Dividing A18 by f12 would then embed
the representation A into Sym^6 W=V+P, contradicting (7). Therefore B
is empty, and there is an exact sequence

    0 -> E_A -> A18 O --ev_A--> O(18) -> 0.          (10)

Thus E_A has rank two and degree -18. Its sections vanish because A18
consists of three independent sections. Hence its ordinary splitting
has two strictly negative degrees.

## 4. The A-channel map of kernels is an isomorphism

Let p:V0*->A18 be the nonzero constant A projection determined by h.
Factor h through p and the constant inclusion of A18 in H_t. Since h
preserves E and vanishes on Hbar*, its restriction to E0 lies in
E_R intersect A18 O. The genuine surjection R->C identifies this
intersection with the kernel of endpoint evaluation on A18, namely
E_A. We obtain a morphism
of exact sequences

    0 -> E0  -> V0* O -> Q0    -> 0
         |g        |p      |q_A
    0 -> E_A -> A18 O -> O(18) -> 0.                 (11)

All these are actual bundle maps induced by constant ambient maps;
no abstract splitting is being treated as horizontal.

We prove that g has generic rank two. Under the invariant apolar
pairing E0 is the complete first osculating bundle U_1^10. The dual
of projection onto the unique A in V0* is the unique three-dimensional
subsystem A10 of H^0(O(10)). Projection of U_1^10 onto that A
constituent is dual to the value-and-first-jet evaluation of A10,
under the natural osculating/jet identifications and the same
symplectic point convention. Thus their generic ranks agree. In
particular the generic rank of this jet evaluation is that of g.

The subsystem A10 is basepoint-free, since any invariant base divisor
would have degree at least 12, exceeding 10. Its independent sections
define a nonconstant morphism X->P(A10*). In characteristic zero the
differential of this morphism is nonzero generically: otherwise every
nonconstant affine coordinate ratio would have zero differential in
the characteristic-zero function field of X and hence would be
constant, a contradiction. Therefore value and first derivative span
two dimensions generically. This is a universal separability argument,
not a computation at a chosen source point.

Both E0 and E_A have rank two and degree -18. Hence det(g) is a nonzero
section of a degree-zero line bundle on P1. It has no zeros, so

    g:E0 -> E_A is an isomorphism everywhere,
    E_A=W O(-9) equivariantly.                       (12)

No separate splitting argument or syzygy calculation is required: (10)
and generic rank already suffice. The determinant identifies both the
particular channel map and the equivariant coefficient representation.

## 5. The first and middle cohomological image spaces

The middle vertical map in (11) is onto with kernel (V+D)O. The left
vertical map is an isomorphism by (12). The snake lemma therefore gives
the exact sequence

    0 -> (V+D)O -> Q0 --q_A--> O(18) -> 0.           (13)

After twisting by -2, H^0((V+D)O(-2))=0. Thus

    H^0(q_A(-2)):Sym^8 W -> H^0(O(16))

is injective. Define

    I_A=im H^0(q_A(-2)).                             (14)

It has dimension 9 and character P+D. It is a proper subspace of the
17-dimensional full section space. The map q_A is determined, up to a
nonzero scalar, by the constant A projection and the unique A18 system,
so I_A is independent of t and of the residual coupling.

After twisting (13) by -1, both cohomology groups of (V+D)O(-1) vanish.
Consequently

    H^0(q_A(-1)):H^0(Q0(-1)) -> H^0(O(17))

is an isomorphism. Its dimension is 18 and its character is W'+S+2T
by (8)-(9). Multiplication is natural in (13); in particular

    I_A tensor H^0(O(1)) -> H^0(O(17))

is an isomorphism as well, because the corresponding multiplication
from H^0(Q0(-2)) tensor H^0(O(1)) to H^0(Q0(-1)) is an isomorphism.

The genuine quotient R->C in (4) dualizes to a bundle inclusion

    O(18)=C* -> R*.                                 (15)

It remains injective on global sections after either twist. The
quotient map induced by h from Q0 into R* is exactly q_A followed by
(15). Therefore (14) and the middle isomorphism compute precisely the
first two images of the full endomorphism, not merely candidate image
representations. The endomorphism is zero on the residual domain
summands in these degrees.

## 6. The final cohomological image and both couplings

Since evaluation by A18 already surjects everywhere, inclusion of the
evaluation sequence (10) into the endpoint evaluation sequence (3)
has identity right vertical map on O(18). Its snake sequence is

    0 -> E_A -> E_C -> (H_t/A18)O -> 0,
    H_t/A18=V+P.                                    (16)

This is a sequence of the specified kernels, not a chosen complement.
Since H^1((V+P)O)=0, it gives a surjection

    H^1(E_A) -> H^1(E_C) -> 0.                       (17)

The target has dimension 9 and character P+D by (3). The endpoint
cohomology sequence also canonically identifies it with

    H^1(E_C)=H^0(O(18))/H_t.                         (18)

The exact residual annihilator sequence in (5) has H^0(T O(-3))=0.
Consequently it gives an injection

    H^1(E_C) -> H^1(E_R).                            (19)

Together (12), (17), and (19) factor the degree-four endomorphism as

    H^1(E0) --isomorphism--> H^1(E_A)
            --surjection--> H^1(E_C)
            --injection--> H^1(E_R).                 (20)

Thus its image is exactly the embedded P+D in (19). Its rank is 9.
The source character is W tensor Sym^7 W=V+2P+D; the kernel of (17)
has character V+P, consistently with (16), but no character count is
used as a substitute for the surjectivity and injectivity proofs.

Nothing in (15)-(20) splits the residual sequence constantly. The maps
are induced by its genuine quotient and the exact annihilator sequence,
which hold for every residual coupling. This is why the conclusion
survives the nonzero coupling class as well as the split class.

## 7. Identification of the image pencils

The full constant map is

    V0* --p--> A18 -> H_t -> Hbar*,

and its kernel and quotient maps are the maps used in (11), (15), and
(20). Naturality of multiplication identifies the first restricted
pencil on the images with s->l s from I_A to H^0(O(17)). Naturality
of the connecting maps identifies the second one with

    H^0(O(17)) -> H^0(O(18))/H_t, r -> [l r].         (21)

This proves (2) as a system with the same pencil variables, not only
as a triple of representations. Multiplication by nonzero l is
injective on homogeneous forms. The subspace l H^0(O(17)) is the
hyperplane of degree-eighteen sections vanishing at the zero of l.
Basepoint-freeness of A18, hence of H_t, says that H_t is not contained
in that hyperplane. Therefore

    l H^0(O(17))+H_t=H^0(O(18)),

which proves surjectivity in (21) for every nonzero l.

The image description is cohomological: in degree two it retains only
I_A, while in degree three it fills H^0(O(17)), and in degree four it
passes from H^1(E_A) to the quotient H^1(E_C). One must not replace
these three images by the full reconstruction of (10) or of (3).
The full endpoint evaluation system has first space H^0(O(16)) of
dimension 17; the A18 evaluation system additionally has final space
H^1(E_A) of dimension 16. Neither is the (9,18,9) image system here.

Equations (14), (18), and (20), together with the middle isomorphism,
prove (1). Square-zero and commutation with every fixed pencil are
already ensured by the radical construction and naturality in (6).
Changing the nonzero generator of the one-dimensional A channel only
rescales its maps and changes none of these image spaces.

## 8. Immediate generic-middle-rank corollary

For a fixed endpoint and either residual class, let J be the full
two-dimensional radical of PR791. Every element of J, after duality,
kills Hbar* and maps the separated V0* block into Hbar*. Its map in
degree three therefore factors through the 18-dimensional space
H^0(Q0(-1)), so its middle rank is at most 18.

The A element attains 18 by the theorem. Nonvanishing of the eighteenth
exterior power is a Zariski-open condition on J, and it is nonempty.
Hence a Zariski-open dense subset of J has middle rank exactly 18.
This corollary does not determine any other radical direction, compute
a rank-drop locus, or assert the existence of an additional exceptional
direction.

## Evidential scope

The arguments use only pinned normal forms, universal representation
identities, invariant orbit sizes, characteristic-zero separability,
determinants of bundle morphisms, and natural exact/cohomology sequences.
No actual HM/source coefficient,
endpoint value, point, derivative value, matrix, instance rank, selected
model, scan, or large computation has been chosen or evaluated.

The result is a necessary universal radical profile over every balanced
endpoint and both residual coupling classes. It does not calculate the
actual source algebra, identify its endpoint or coupling, prove an HM
realization, or exclude source2. This is a written structural proof,
not proof-assistant certification.
