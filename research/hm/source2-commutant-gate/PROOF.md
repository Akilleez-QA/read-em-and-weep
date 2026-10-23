# A small linear commutant gate and trace extractor for source2

## Result and boundary

Work over C, with the binary icosahedral group G and its defining
two-dimensional representation W. All endomorphisms preserve the grading,
are G-equivariant, and fix the two pencil variables. Keep the original
negative multiplication tensors fixed. No actual tensor is evaluated here.

The fixed-pencil commutant is the kernel of a linear map

    Delta: C^113 -> C^153.

Conditionally on the actual-source hypotheses and identification in PR790,
source2 requires

    rank Delta = 108 or 109.                         (1)

There is a stronger test that treats both residual coupling classes
uniformly. Append the three ordinary traces at the graded vertices to
obtain a linear map

    Delta_tr: C^113 -> C^156.

For every source2 normal form,

    ker Delta_tr = Jac(ker Delta),
    dim ker Delta_tr = 2,   rank Delta_tr = 111.     (2)

The multiplication on ker Delta is componentwise composition of triples.
Thus (2) recovers its full radical by linear equations alone within the
proved source2 class. For an arbitrary pencil system the common trace
kernel need not be its radical; the conditional scope is essential.

These are necessary tests of the fixed original tensors, not a calculation
of their commutant. In particular, no source2 exclusion, endpoint choice,
HM realization, or conclusion about the full HM module is obtained here.
The contribution is the exact small linear formulation, its dimension
thresholds, and the coupling-independent trace characterization.

## 1. Immutable inputs

All references are in Akilleez-QA/read-em-and-weep.

- [PR789, residual coupling normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md),
  commit 2d1642ad40ae1111b84b50eeaca0426bfbfbb314. Section 2 gives the
  McKay products used below. Sections 5-6 give the two residual classes.
- [PR790, first block and actual tensor identification](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md),
  commit af0e03d26da5e47d18ae732291aca46f4d448dc5, proof SHA-256
  0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4.
  Section 6 identifies reconstruction with the original fixed tensors;
  Section 7 supplies the first-block characters and dimensions.
- [PR791, full fixed-pencil endomorphism algebra](https://github.com/Akilleez-QA/read-em-and-weep/blob/2cd033a4a5ba549d07330427cd779364cb83c0fb/research/hm/source2-pencil-endomorphism-algebra/PROOF.md),
  commit 2cd033a4a5ba549d07330427cd779364cb83c0fb, proof SHA-256
  8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290.
  Sections 2-5 exhaust all constant endomorphisms; Section 6 proves full
  faithfulness; Section 7 records the opposite-algebra orientation.
- [PR795, residual exact sequence and intrinsic core](https://github.com/Akilleez-QA/read-em-and-weep/blob/3f811311d76914a555c7e7d0c5b887b41805aa6c/research/hm/source2-radical-filtration/PROOF.md),
  commit 3f811311d76914a555c7e7d0c5b887b41805aa6c, proof SHA-256
  27a8802a004cb659e1b33cae9aabaca1e8188b1382d8477cac2bb31264c40937.
  Sections 2-3 give the degree-eight and endpoint pencils used in the
  trace calculation. The radical rank-locus theorem is not needed here.

For the feasibility boundary see [PR788](https://github.com/Akilleez-QA/read-em-and-weep/blob/941b7b3b77dc8ae8a19b1e000dddeb0438d05db7/research/hm/source2-universal-constant-flag/PROOF.md):
the abstract normal forms have common commuting pencils, but those
constructed tensors are not identified with the actual HM tensors. Feeding
such an abstract witness into the tests below cannot answer the fixed-HM
question. The actual-source application retains all hypotheses of PR790
and its pinned geometric dependencies; no new identification is assumed.

## 2. The full linear map, with no missing endomorphism channels

Use the irreducible names

    A=Sym^2 W, S=Sym^3 W, D=Sym^4 W, T=Sym^5 W,

with dimensions 3,4,5,6, respectively. The other irreducibles V,P,W'
have dimensions 3,4,2. The actual graded characters are

    M2=A+2V+3P+4D,       dim M2=41,
    M3=3W'+3S+6T,        dim M3=54,
    M4=2V+4P+3D,         dim M4=37.                  (3)

Write the fixed tensors as equivariant maps

    alpha: W tensor M2 -> M3,
    beta:  W tensor M3 -> M4.

Equivalently alpha(l tensor x)=A_l(x) and beta(l tensor y)=B_l(y).
The pencil variables are inputs to these tensors, not additional unknowns
or an automorphism group by which we quotient. Define

    D0 = End_G(M2) plus End_G(M3) plus End_G(M4),
    T0 = Hom_G(W tensor M2,M3) plus Hom_G(W tensor M3,M4),
    Delta(X2,X3,X4)
      = (X3 alpha-alpha(1_W tensor X2),
         X4 beta-beta(1_W tensor X3)).               (4)

The two tensor equations in (4) are exactly

    X3 A_l=A_l X2,   X4 B_l=B_l X3

for every l in W. It suffices to impose them for a basis of W, by
linearity; imposing only one selected l would be a different commutant.
The kernel E of Delta is exactly the algebra of all such triples. It is
closed under composition, since intertwining identities compose, and
contains the simultaneous identity triple. Noninvertible endomorphisms
are included without any extra condition.

For an isotypic decomposition M=sum_r r tensor C^(m_r), Schur's lemma
gives End_G(M)=sum_r Mat_(m_r)(C). Thus every multiplicity matrix is an
unknown in (4), including off-diagonal entries between repeated copies:

    dim End_G(M2)=1^2+2^2+3^2+4^2=30,
    dim End_G(M3)=3^2+3^2+6^2=54,
    dim End_G(M4)=2^2+4^2+3^2=29.

Consequently dim D0=113. There is no assumption that an endomorphism is
scalar on an entire isotypic component.

The products supplied by PR789, together with the ordinary Clebsch
identity for S=Sym^3 W, are

    W tensor A=W+S,       W tensor V=T,
    W tensor P=W'+T,      W tensor D=S+T,
    W tensor W'=P,        W tensor S=A+D,
    W tensor T=D+V+P.                               (5)

They give the entire tensor-product characters

    W tensor M2=W+3W'+5S+9T,
    W tensor M3=3A+6V+9P+9D.

Only matching irreducibles contribute to equivariant Hom. Therefore

    dim Hom_G(W tensor M2,M3)=3*3+5*3+9*6=78,
    dim Hom_G(W tensor M3,M4)=6*2+9*4+9*3=75.        (6)

This proves dim T0=153 and the stated matrix size after choosing bases.
These numbers count scalar coordinates in multiplicity spaces, not the
full vector-space dimensions of the tensors. The target spaces in (6)
include every equivariant channel, so using them loses no equation.

Changes of bases in the exact isotypic identifications or equivariant Hom
spaces induce invertible changes of rows and columns in (4). They do not
alter its kernel dimension. The intrinsic definition (4), rather than a
particular choice of Clebsch coordinates, is the definition of this test.

## 3. The two unaugmented ranks

Under the source2 hypotheses, PR791 proves the entire algebra E is

    zero residual quotient coupling:     C times T(J), dim E=5;
    nonzero residual quotient coupling:  T(J),         dim E=4,

where dim J=2 and J^2=0. The radical is exactly J. PR791's transfer from
the constant inclusion is contravariant before the pencil reconstruction;
its opposite algebra has the same dimensions and radical. No extension
of these endomorphisms to the full HM module is used.

Rank-nullity for (4) now gives, respectively, 113-5=108 and 113-4=109.
This proves (1). Conversely, within this established normal-form family
these two ranks distinguish the residual coupling classes. For arbitrary
fixed tensors a rank of 108 or 109 does not establish membership in the
family or determine a residual geometric coupling.

## 4. The vertex traces detect the whole semisimple quotient

Define the linear map of ordinary vector-space traces

    tau:D0 -> C^3,
    tau(X2,X3,X4)=(Tr_M2 X2,Tr_M3 X3,Tr_M4 X4).      (7)

Every element of J is square-zero as a pencil endomorphism. Each of its
three component endomorphisms is therefore nilpotent and has trace zero.
Hence J is contained in ker(tau|E). To prove equality, it remains to
show that the traces are injective on E/J.

The genuine first constant block gives a direct-sum decomposition of
pencils N=N0 plus NR, with dimensions

    d0=dim N0=(9,18,16),
    dR=dim NR=(32,36,21).                            (8)

In the nonzero residual class, PR791 shows that the residual diagonal
action is a single scalar aR; the first-block diagonal action is a0.
The two radical channels are off-diagonal. Thus, in any constant normal
form, the trace vector is

    tau(X)=a0*d0+aR*dR.

The first two coordinates of d0 and dR have determinant
9*36-32*18=-252, which is nonzero. Therefore tau|E has rank two,
is injective on E/J, and has kernel exactly J in this class.

For zero residual coupling, the residual inclusion splits constantly
into its complete degree-eight block and its degree-eighteen endpoint.
The reconstruction preserves that direct sum. Its pencil dimensions are

    d8=dim N8=(15,18,12),
    dC=dim NC=(17,18,9),      d8+dC=dR.             (9)

These follow from the evaluation sequences in PR795 Sections 2-3:
N8 has spaces A tensor Sym^4 W, A tensor Sym^5 W, T tensor W;
NC has spaces Sym^16 W, Sym^17 W, H^0(O(18))/H_t, with dim H_t=10.
They also sum with d0 to (41,54,37), as required.

PR791's diagonal scalars a0,a8,aC act on these three blocks, while its
radical remains off-diagonal. Consequently

    tau(X)=a0*d0+a8*d8+aC*dC.

The three column vectors are independent:

         |  9  15  17 |
    det  | 18  18  18 | = 180 != 0.                (10)
         | 16  12   9 |

Therefore tau|E has rank three, is injective on E/J, and again has
kernel exactly J. The trace computation is invariant under simultaneous
conjugacy at the three vertices. Thus the use of a normal form in its
proof does not make the resulting kernel depend on chosen complements.
The nonzero-coupling case did not assume a horizontal residual splitting.

This proves in both classes

    E intersect ker tau = J,   dim(E intersect ker tau)=2. (11)

The scalar action used here is the specific exhaustive algebra action
proved in PR791, not an inference from the dimensions of E alone.

## 5. The augmented gate and exact rejection certificates

Define

    Delta_tr=(Delta,tau):D0 -> T0 plus C^3.          (12)

By (11), its kernel is J for either source2 class. Its domain has
dimension 113 and target dimension 156, so rank-nullity proves
rank Delta_tr=111. This proves (2) without computing multiplication in
the commutant or finding idempotents.

For use in multiplicity coordinates, ordinary traces must be weighted
by irreducible dimensions. With X_(i,r) denoting the multiplicity
matrix on the r-isotypic part of Mi, the three rows are

    tau2=3 tr X_(2,A)+3 tr X_(2,V)+4 tr X_(2,P)+5 tr X_(2,D),
    tau3=2 tr X_(3,W')+4 tr X_(3,S)+6 tr X_(3,T),
    tau4=3 tr X_(4,V)+4 tr X_(4,P)+5 tr X_(4,D).     (13)

Unweighted multiplicity traces are not the traces in this theorem.

For authenticated actual tensors, any of the following exact
certificates contradicts the source2 necessary conditions:

- rank Delta at least 110, for example a nonzero 110-by-110 minor;
- six linearly independent exact vectors in ker Delta, proving rank
  Delta at most 107;
- rank Delta_tr at least 112, for example a nonzero 112-by-112 minor;
- three linearly independent exact vectors in ker Delta_tr, proving
  rank Delta_tr at most 110.

The upper-bound alternatives require both exact kernel identities and
independence. A collection of dependent triples or a failed pivot search
is not an upper-rank certificate. Conversely, passing (1)-(2) only passes
these necessary linear conditions. It does not prove the radical is
square-zero for arbitrary tensors, or verify the finer image-pencil and
intrinsic-core constraints of PR792-795, or prove source2 realization.

## 6. Missing actual input and evidential scope

This note provides no authenticated coefficient arrays for alpha and
beta, no characteristic-zero tensor rank, and no modular instance
calculation. An actual test needs a separately authenticated construction
of the fixed HM multiplication tensors with their G actions and exact
bases. It must identify those maps simultaneously with the original
two negative pencils of PR790, rather than merely reproduce characters,
dimensions, commutativity, or an abstract normal-form witness.

SPEC.md records that input contract and the distinction between proof
of an incompatible rank and an inconclusive computation. The argument
here uses only the pinned exact algebra/action theorems, Schur's lemma,
universal representation products, ordinary traces, and rank-nullity.
It is a written conditional proof, not proof-assistant certification or
a performed actual-source evaluation.
