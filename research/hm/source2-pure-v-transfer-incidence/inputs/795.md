# The intrinsic radical filtration and degree-eight core forced by source2

## Result and scope

Work over C. Let G be the binary icosahedral group, W its defining
two-dimensional representation, and X=P(W), using the invariant
symplectic identification W=W*. Put

    A=Sym^2 W, S=Sym^3 W, D=Sym^4 W, T=Sym^5 W,

and write V, P, W' for the other three-, four-, and two-dimensional
irreducibles. All representations here are self-dual. All pencil maps
use the same fixed two-space H^0(O_X(1)); no change of pencil variables
or automorphism of X is allowed.

Let N=(N2,N3,N4; A_l,B_l) be any source2 negative two-pencil system in
the published constant normal-form family, with any balanced endpoint
and either residual quotient coupling class. Let J be the full
Jacobson radical of its degree-preserving G-equivariant fixed-pencil
endomorphism algebra. Define, componentwise,

    (JN)i = sum over j in J of im(ji),
    (Ann_J N)i = intersection over j in J of ker(ji).

These give a canonical filtration by G-equivariant fixed-variable
subpencils

    0 subset JN subset Ann_J N subset N.             (1)

Its exact dimension triples are

    dim N          = (41,54,37),
    dim JN         = (14,18, 9),
    dim Ann_J N    = (32,36,24),
    dim(Ann_J N/JN)= (18,18,15).

The characters of the image, annihilator, and middle quotient are

    JN:
        (P+2D, W'+S+2T, P+D);
    Ann_J N:
        (A+2V+2P+3D, 2W'+2S+4T, 2V+2P+2D);
    Ann_J N/JN:
        (A+2V+P+D, W'+S+2T, 2V+P+D).                (2)

More strongly, as a system with both fixed pencils,

    Ann_J N/JN is isomorphic to N8 plus V[2] plus V[4]. (3)

Here V[i] is the representation V isolated at vertex i, with all
arrows zero. The system N8 is canonically specified by the complete
degree-eight osculating inclusion

    A0=U_2^8=A O(-6) subset Sym^8 W O.

Its dual evaluation sequence and reconstructed spaces are

    0 -> E8=T O(-3) -> (Sym^8 W)* O -> Q8=A O(6) -> 0,
    N8=(A tensor Sym^4 W, A tensor Sym^5 W, T tensor W),
    dim N8=(15,18,12).                              (4)

There is an intrinsic construction of the degree-eight core directly
from the middle quotient K=Ann_J N/JN: remove the common kernel of its
first arrows and restrict its last space to the span of its second
arrow images. This canonical subquotient has fixed-pencil isomorphism
type N8. Neither (3) nor this statement asserts a preferred
scalar-normalized isomorphism to (4), or a constant horizontal splitting
of the original residual bundle.

Conditionally on the actual-source hypotheses and common-pencil
identification of PR790, these are necessary constraints on the fixed
original source2 tensors. No actual instance is evaluated or excluded.

## 1. Exact dependencies and the information beyond individual ranks

The following proofs in Akilleez-QA/read-em-and-weep were retrieved at
their immutable public commits and checked against the local contents:

- [PR791, exact fixed-pencil endomorphism algebra](https://github.com/Akilleez-QA/read-em-and-weep/blob/2cd033a4a5ba549d07330427cd779364cb83c0fb/research/hm/source2-pencil-endomorphism-algebra/PROOF.md),
  commit 2cd033a4a5ba549d07330427cd779364cb83c0fb, proof SHA-256
  8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290.
  We use the full radical, its square-zero property, the genuine first
  constant block, and the fully faithful fixed-variable reconstruction.
- [PR792, V-channel image pencil](https://github.com/Akilleez-QA/read-em-and-weep/blob/2f01f18960ce56b8b2a0c1260c277de3c5f916bf/research/hm/source2-radical-rank-profile/PROOF.md),
  commit 2f01f18960ce56b8b2a0c1260c277de3c5f916bf, proof SHA-256
  0d4eb3e4e9e98dd9ea8202399590f9741c06771411d5ce40e69a139c461b3798.
- [PR793, A-channel image profile](https://github.com/Akilleez-QA/read-em-and-weep/blob/ba9234964af5d879675d19ae97847a9475792f98/research/hm/source2-a-channel-rank/PROOF.md),
  commit ba9234964af5d879675d19ae97847a9475792f98, proof SHA-256
  7a9e75e9f1d22bb058039a94452e6edc1b788faa6e716dc5489f877346ab170a.
- [PR794, complete radical-rank stratification](https://github.com/Akilleez-QA/read-em-and-weep/blob/7fd254100b83bb03f41b776ea3119690aa51f671/research/hm/source2-radical-rank-locus/PROOF.md),
  commit 7fd254100b83bb03f41b776ea3119690aa51f671, proof SHA-256
  a256ec6cc92b1151a6551e6692cfa32cac02bceaad34c60746f51f249256cf4c.
  We use Sections 5 and 6, including their image and row independence
  assertions, not only their final rank stratification.

The first three public Git blob identifiers are, respectively,
5a0d16a2f22032f1a0583b92ad71661b5abab59d,
76bee93507d1a2d0840926d4e4e27edadfebb7d7, and
9fd685d919caf88142441d4788e8ff59ea23fb7a. The fourth public Git blob is
3ad30b9aa1920408cc34778e78405f544b5adc8e; its frozen digest was also
checked directly. No unpublished mathematical dependency is used.

These inputs carry their stated dependence on the arbitrary-coupling
normal form of [PR789](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md)
at 2d1642ad40ae1111b84b50eeaca0426bfbfbb314 and the first constant block
and actual-source transfer of [PR790](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md)
at af0e03d26da5e47d18ae732291aca46f4d448dc5.

Two stronger assertions, not just the individual channel ranks, are
essential here. The first D image of the A channel and the first D
image of the V channel are distinct irreducible subspaces. The two
final P maps on the two-copy P-isotypic domain are linearly independent
in its equivariant Hom space. These are proved in Sections 5 and 6,
respectively, of the full radical-rank dependency. Their use computes
the sum of all radical images and intersection of all radical kernels;
separate rank lists alone would not compute either operation.

## 2. Normal forms and the canonical degree-eight evaluation

Write

    U_j^e=Sym^j W O(j-e) subset Sym^e W O,
    (U_j^e)_[ell]=ell^(e-j) Sym^j W.

The normal form has a genuine constant separated first block

    H*=V0 direct-sum Hbar, Q*=U direct-sum R,
    V0=Sym^10 W=A+V+D, U=U_8^10,
    Hbar=V1 direct-sum F_t, V1=Sym^8 W=P+D.          (5)

Here t remains an arbitrary balanced endpoint. Put

    H_t=F_t*=A18+V18+P_t subset H^0(O(18)),
    C=O(-18), E_C=ker(H_t O -> C*)=(P+D)O(-2).

The residual has genuine intersection and quotient maps

    R intersect V1 O=A0=U_2^8,
    0 -> A0 -> R -> C -> 0.                         (6)

The map to C is induced by the constant projection to F_t O. It is
not an abstract bundle projection introduced by choosing a splitting.
Both residual coupling classes are allowed throughout.

Dualize (5) and set

    E0=ann_V0*(U)=W O(-9), Q0=U*=Sym^8 W O(2),
    E_R=ann_Hbar*(R), E=E0 direct-sum E_R,
    Q=Q0 direct-sum R*.

Thus the natural fixed-pencil reconstruction splits genuinely as

    N=N0 direct-sum N_R.                            (7)

For any evaluation sequence 0 -> E' -> H' O -> Q' -> 0 used here,
the reconstruction is

    N(E',Q')_2=H^0(Q'(-2)),
    N(E',Q')_3=H^0(Q'(-1)),
    N(E',Q')_4=H^1(E'),
    A_l(s)=l s, B_l(r)=delta(l r),                  (8)

where delta is its connecting map. In particular N_C is the
reconstruction of the endpoint evaluation sequence, with spaces

    N_C=(Sym^16 W, Sym^17 W, H^0(O(18))/H_t).        (9)

The inclusion A0 in V1 O has its specified dual exact sequence

    0 -> E8 -> V1* O -> Q8 -> 0,
    E8=T O(-3), Q8=A0*=A O(6).                      (10)

Under apolarity, E8 is the complete subbundle U_5^8, the annihilator
of U_2^8. Thus (10) is the actual complete degree-eight evaluation
sequence, not merely an evaluation with these splitting characters.
Define N8 by (8) applied to (10). This gives (4).

The standard Clebsch rule and the identities in the dependencies give

    A tensor Sym^4 W=Sym^6 W+Sym^4 W+Sym^2 W
                   =A+V+P+D,
    A tensor Sym^5 W=Sym^7 W+Sym^5 W+Sym^3 W
                   =W'+S+2T,
    T tensor W=V+P+D.                               (11)

Also Sym^17 W=W'+S+2T and Sym^18 W=A+V+2P+D. Applying
W tensor Sym^17 W=Sym^18 W+Sym^16 W yields

    Sym^16 W=V+P+2D.                                (12)

These are universal representation identities; no coefficient or
source-instance rank has been chosen.

## 3. The residual evaluation gives a short exact sequence of pencils

Dualizing (6) gives the genuine quotient-bundle sequence

    0 -> C*=O(18) -> R* -> A0*=Q8 -> 0.             (13)

Together with the constant inclusion H_t -> Hbar* and projection
Hbar* -> V1*, it forms a diagram of evaluation sequences

    0 -> E_C -> H_t O   -> C* -> 0
           |       |         |
    0 -> E_R -> Hbar* O -> R* -> 0
           |       |         |
    0 -> E8  -> V1* O  -> Q8 -> 0.                 (14)

The middle and right columns are short exact, with zeros appended
above and below. Their maps commute with evaluation: restriction of
a functional on Hbar to A0 depends only on its V1* component, while
restriction of H_t to R is induced by the quotient R -> C. The
snake lemma therefore gives the left short exact column

    0 -> E_C -> E_R -> E8 -> 0.                     (15)

In particular these are maps of the specified kernels and quotients,
valid for all residual couplings.

Twisting (13) by -2 and -1 yields short exact sequences on H^0,
because H^1(O(16))=H^1(O(17))=0. In degree four, (15) yields

    0 -> H^1(E_C) -> H^1(E_R) -> H^1(E8) -> 0,      (16)

because H^0(E8)=H^0(T O(-3))=0 and H^2(E_C)=0 on X.
Thus the reconstructed spaces are componentwise short exact.

Multiplication by every l commutes with the quotient maps in (13),
so both first-pencil squares commute. Connecting-map naturality in
the two maps of evaluation sequences (14) gives

    H^1(i_E) delta_C=delta_R H^0(i_Q),
    H^1(p_E) delta_R=delta_8 H^0(p_Q).

After composing with multiplication by l, these identities are
exactly the second-pencil squares. Consequently

    0 -> N_C -> N_R -> N8 -> 0                     (17)

is a short exact sequence of G-equivariant systems with the same
fixed pencil variables. We do not assert that reconstruction is exact
for arbitrary bundle sequences; the necessary vanishings have just
been checked for (14).

From (9), (11), (12), and (17), the residual dimensions and characters
are

    dim N_R=(32,36,21),
    char N_R=(A+2V+2P+3D, 2W'+2S+4T, V+2P+2D).     (18)

## 4. Intrinsicness of the radical filtration

PR791 identifies J with the full two-dimensional radical, not a chosen
square-zero subspace of a larger radical, and proves J^2=0. Each of
its elements commutes with every A_l and B_l. An image, sum of images,
kernel, or intersection of kernels of such endomorphisms is therefore
stable under all the arrows. In particular JN and Ann_J N are
G-equivariant subpencils.

For j,j' in J, j j'=0. Thus j kills every im j', proving

    JN subset Ann_J N.                              (19)

The filtration is in fact preserved by every fixed-pencil
endomorphism e, not only by automorphisms. Indeed e j and j e belong
to J because J is a two-sided ideal. Hence e(JN) is contained in JN;
and if x is annihilated by J, then j e(x)=(j e)(x)=0 for every j,
so e(x) lies in Ann_J N.

An isomorphism of fixed-pencil systems conjugates their endomorphism
algebras and their radicals, and therefore transports the entire
filtration. It is independent of channel generators, ambient
complements, and a constant normal-form presentation. We may use (7)
to compute its terms without making their definitions depend on (7).

The duality in PR791 reverses the ambient algebra orientation. On the
reconstructed system, the radical maps go from N0 into N_R and kill
N_R. All computations below use this pencil orientation.

## 5. The full radical image is the non-V endpoint subpencil

Every radical image lies in the embedded N_C of (17). In degree two,
let I_A and I_V be the A- and V-channel images inside Sym^16 W.
PR793 gives I_A=P+D and PR792 gives I_V=D. Section 5 of the full
radical-rank theorem proves that these two D subrepresentations are
distinct. Two distinct irreducible subrepresentations intersect
trivially, and the P image meets neither. Therefore

    I=I_A+I_V has character P+2D and dimension 14.    (20)

By (12) this is exactly the full P- and D-isotypic subspace of
Sym^16 W; its quotient is V. This intrinsic isotypic description in
the endpoint space also shows why neither a choice of D copy nor a
channel normalization remains in (20).

In degree three the A-channel map already fills the entire endpoint
space Sym^17 W. In degree four it fills all H^1(E_C)=P+D. Every
other radical image remains inside those same spaces. Consequently,
inside N_R,

    JN=(I, Sym^17 W, H^0(O(18))/H_t),
    A_l(s)=l s, B_l(r)=[l r].                       (21)

This identifies the actual image subpencil, not only its characters.
Its dimensions and characters are the JN row in (2). In particular

    N_C/JN=V[2]                                    (22)

as a pencil: the middle and final quotient spaces vanish, so both
arrows out of the remaining first space vanish. The assertion (22)
uses the sum of the two D images; it would not follow from the
individual profiles alone.

## 6. The common radical kernel

The separated first system has spaces and characters

    N0_2=Sym^8 W=P+D,
    N0_3=Sym^8 W tensor W=W'+S+2T,
    N0_4=H^1(W O(-9))=W tensor Sym^7 W=V+2P+D.      (23)

Every radical map kills the residual summand N_R. The A-channel
map is injective on N0_2 and an isomorphism from N0_3 onto the
endpoint middle space. Thus no extra common kernel comes from N0
at vertices two or three.

At vertex four write the A and V maps, after their genuine
factorization through H^1(E_C), as

    a,b:V+2P+D -> P+D.

PR793 proves a is onto, with kernel V+P, and its D restriction is an
isomorphism. PR792 proves im b=P. Section 6 of the full radical-rank
theorem proves that a and b have linearly independent restrictions
on the two-copy P-isotypic domain. By Schur's lemma, those restrictions
are two independent linear functionals on its two-dimensional
multiplicity space. Their common kernel there is zero. The A map
has no D kernel, and both maps kill V because their target has no V.
Therefore their entire common kernel is exactly the unique V in
N0_4:

    ker a intersect ker b=V.                        (24)

Since the two channels span J, (24) is the common kernel of the
whole radical on that vertex. The independence of the P restrictions
is essential; their separate surjectivity would not suffice.

In the genuine constant first-block splitting we have, as pencils,

    Ann_J N=N_R direct-sum V[4].                    (25)

There are no incoming arrows from N_R into this extra first-block
V: the entire reconstruction is the direct sum (7), and the
annihilator has no first-block component at vertices two and three.
This proves (25) at the level of arrows, not just of vector spaces.
It does not declare the normal-form complement intrinsic.

Combining (18), (23), and (25) gives all dimensions of N and Ann_J N
stated above, and their characters. For reference the full character is

    char N=(A+2V+3P+4D, 3W'+3S+6T, 2V+4P+3D).

The final quotient N/Ann_J N has dimensions (9,18,13) and characters
(P+D, W'+S+2T, 2P+D); it is isomorphic to the separated first system
N0 modulo its isolated V at vertex four. This last description also
uses the genuine first-block pencil splitting, not a residual bundle
splitting.

## 7. The middle quotient and its pencil splitting

Quotient (17) by JN, using (22), to obtain a short exact sequence
of fixed-variable G-equivariant pencils

    0 -> V[2] -> K_R=N_R/JN --p--> N8 -> 0.        (26)

At vertices three and four, p3 and p4 are isomorphisms. At vertex
two, choose any G-equivariant vector-space section s2 of p2; it exists
because representations of the finite group G over C are semisimple.
Set s3=p3^(-1) and s4=p4^(-1). We verify that s is a pencil section,
not merely a section on the three spaces.

For every fixed linear form l, naturality in (26) gives

    p3 A_l^(K_R) s2=A_l^8 p2 s2=A_l^8.

Since p3 is an isomorphism, this is equivalent to

    A_l^(K_R) s2=s3 A_l^8.

Likewise p4 B_l^(K_R) s3=B_l^8 p3 s3=B_l^8, and invertibility of
p4 gives B_l^(K_R) s3=s4 B_l^8. Thus s commutes with both pencils
for every l, without changing l. Hence

    N_R/JN is isomorphic to N8 direct-sum V[2].       (27)

Different equivariant sections at vertex two differ by a map into
V[2], which is killed by both first arrows. This explains directly
why every such section works and why no canonical section is claimed.

Using JN subset N_R and (25), we obtain

    Ann_J N/JN
       is isomorphic to (N_R/JN) direct-sum V[4]
       is isomorphic to N8 direct-sum V[2] direct-sum V[4]. (28)

Equations (11) and (28) prove the middle dimensions and characters
in (2). The isomorphism type is independent of the balanced endpoint
and of the residual coupling.

The distinction from a horizontal splitting is crucial. We split (26)
only after quotienting by JN, in the category of finite-dimensional
pencil systems. The removed first-space V has zero next space. It
does not reconstruct to one of the negative evaluation bundles to
which the full-faithfulness theorem applies. Consequently (27) gives
no constant splitting R=A0 plus C, and does not turn a nonzero
residual coupling into the zero class. No essential-surjectivity claim
about arbitrary pencil systems is used.

## 8. Recovering the degree-eight core intrinsically

First verify two properties of the specific system N8. Its first
arrows are multiplication

    A tensor Sym^4 W -> A tensor Sym^5 W,

so each A_l^8 is injective for every nonzero l. Twisting (10) by -1,
the acyclicity of V1* O(-1) gives a natural isomorphism

    H^0(Q8(-1)) --delta_8(-1)--> H^1(E8(-1)).

Connecting-map naturality identifies B_l^8 with this isomorphism
followed by multiplication

    H^1(T O(-4)) --l--> H^1(T O(-3)).

By Serre duality, the scalar-factor map is dual to multiplication
H^0(O(1)) --l--> H^0(O(2)), which is injective for every nonzero l.
Thus B_l^8 is surjective for every nonzero l. This proof uses only
universal multiplication and cohomology, with no point evaluation.

Now form K=Ann_J N/JN intrinsically from N and J, and define

    Z2=intersection over l of ker(A_l^K),
    D4=sum over l of im(B_l^K),
    L=(K2,K3,D4), Z=(Z2,0,0).                       (29)

The subspaces are G-stable because the entire arrow families are
G-equivariant. The systems L and Z are subpencils of K, with Z
contained in L. Thus the intrinsic core

    Core_J(N)=L/Z=(K2/Z2,K3,D4)                     (30)

is a well-defined G-equivariant fixed-variable subquotient, without
any channel or normal-form choices. By (28) and the injectivity and
surjectivity just proved,

    Z2 has character V,
    K4/D4 has character V,
    Core_J(N) is isomorphic to N8.                  (31)

In fact every nonzero first arrow has the same kernel Z2, and every
nonzero second arrow has the same image D4. The core therefore has
dimensions (15,18,12), and both pencils have the complete
degree-eight form (10), (8) up to a fixed-variable equivariant
isomorphism.

The isolated source piece Z=V[2] is a canonical subpencil. The isolated
last piece is canonically the quotient K/L=V[4]; a complementary
V[4] subspace of K4 need not be chosen canonically. Likewise the
construction (30) is canonical, but this theorem does not designate
a scalar-normalized identification with the standard model (10).
These distinctions prevent (28) from claiming more canonicity than
the argument supplies.

## 9. Universal and actual-source boundary

The filtration (1), the precise arrow-level identification (28), and
the intrinsic core (30) strengthen the separate radical rank profiles:
they recover a fixed complete degree-eight system as a canonical
subquotient of the whole negative two-pencil system.

All cohomological maps used come from genuine evaluation morphisms
and the actual quotient (6). The only splitting of the original
inclusion used is the published constant separation of the first
block (5). The residual quotient is never treated as horizontally
split. Both coupling classes and every balanced endpoint remain in
the argument.

Under PR790's actual-source hypotheses, PR791's reconstruction and
radical identification transport these intrinsic statements to the
same original fixed negative tensors. They do not calculate that
endomorphism algebra for actual HM tensors, identify an endpoint or
coupling, prove an HM realization, or exclude source2. Nothing is
asserted about endomorphisms of the entire HM module or bundle.

The proof uses exact structural theorems, universal character
identities, natural cohomology, the ideal property of the Jacobson
radical, and semisimplicity of finite-group representations over C.
No actual coefficient, endpoint value, point, derivative value,
tensor, matrix, instance rank, selected model, scan, or large
computation has been chosen or evaluated. This is a written
deductive proof, not proof-assistant certification.
