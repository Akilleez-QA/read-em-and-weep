# The exceptional source2 radical quotient has a universal contraction summand

## Theorem and boundary

Over C retain the balanced-endpoint, arbitrary residual-coupling source2
normal form of the exact PR790, PR794 and PR795 inputs in INPUTS.json.
Let j be the unique exceptional mixed radical direction of PR794 and
I=im(j), vertexwise. No scalar coordinate is assigned to this direction.
With the ORIGINAL pencil variables, there is a G-equivariant isomorphism

    N/I ≅ N0 ⊕ N8 ⊕ L,
    L=(W'⊗H¹(O(-5)), W'⊗H¹(O(-4)), 0).

The first arrows of L are multiplication by the same linear forms on H¹;
its second arrows vanish. Thus L has characters (V+D,T,0) and dimensions
(8,6,0), but is NOT the direct sum of isolated vertex pieces. Every nonzero
first arrow in L is surjective, with two-dimensional kernel; their common
kernel is zero. The complete quotient dimensions are (32,42,28).
Its first arrows have rank30 for EVERY nonzero linear form, and common
kernel zero. This contrasts with the regular quotient's isolated initial
8-space, without asserting or using a regular-direction theorem here.

This is a new arrow-level normal form, uniform for both residual coupling
classes and every balanced endpoint. It needs no Q compatibility. If j
commutes with actual Q, the statement describes the negative arrows of the
conditional 32-to-28 reduction, NOT a Q-stable direct sum. No compatible
line is asserted to exist, no source or catalogue pair is excluded, and no
complete proof repair is claimed. No selected HM coefficient, parameter,
point, matrix or rank is evaluated.

## 1. Exact imported geometry

The three exact originals are copied into inputs/, with immutable commit,
public URL, Git blob and SHA256 in INPUTS.json.
PR790 gives the genuine fixed-pencil split N=N0⊕NR. PR795 Sections2–3 give

    0 → NC → NR → N8 → 0,
    NC=(H⁰(O16), H⁰(O17), H⁰(O18)/H_t),
    N8_2=A⊗H⁰(O4),  N8_3=A⊗H⁰(O5),

with first arrows given by multiplication. Here N8 has dimensions(15,18,12)
and N0 has dimensions(9,18,16). These are arrow systems, not just characters.
PR794 gives I⊂NC, dimensions(9,12,9), and surjective exceptional quotient
map q:Q0=Sym⁸(W)O(2)→O(18). Its kernel F sits in

    0 → D O → F → EV ⊕ O(6) → 0,       EV=W'O(-3).       (1)

Indeed PR794 Section4 equations(23)–(26) identify the exceptional split
extension K_z=EV⊕O6 and supply (1). Its Section5 proves H⁰(q(-2)) injective.
No residual endpoint enters q or (1).

## 2. The exceptional kernel bundle and endpoint quotient

Ext¹_G(EV,D O)=0: its underlying H¹ consists of copies of H¹(O3)=0,
and taking finite-group invariants over C is exact. The EV part of (1)
therefore splits off equivariantly. The other extension has class in

    Ext¹_G(O6,D O) = (D⊗H¹(O(-6)))^G = (D⊗Sym⁴W)^G ≅ C.

This class cannot vanish. Otherwise F would contain an O6 summand and
H⁰(F(-2)) would contain H⁰(O4), contrary to the imported injectivity of
H⁰(q(-2)). A standard equivariant evaluation sequence supplies a nonzero
class in this one-dimensional space:

    0 → Sym⁴W O → Sym⁵W O(1) → O(6) → 0.             (2)

To see (2), twist the complete degree-five evaluation sequence by O1.
It is nonsplit because Hom(O6,Sym⁵W O1)=0. Rescaling its kernel or quotient
identifies every nonzero class with (2). Consequently, as an equivariant
bundle (with no chosen preferred splitting),

    F ≅ T O(1) ⊕ W'O(-3).                           (3)

For k=1,2 the exact sequence 0→F(-k)→Q0(-k)→O(18-k)→0
has H¹(Q0(-k))=0. Its connecting homomorphism identifies

    NC_2/I_2 = H¹(F(-2)) = W'⊗H¹(O(-5)),
    NC_3/I_3 = H¹(F(-1)) = W'⊗H¹(O(-4)).             (4)

The T terms are acyclic in these H¹ degrees. Naturality makes the induced
first arrows in (4) exactly H¹ multiplication by l, for EVERY l in the
original pencil. Since I4=NC4 by containment and equal dimension, NC/I=L
as an arrow system. Its characters V+D and T also follow by subtraction
of the imported actual image characters. This proves the arrow description,
not merely a character identity.

Under Serre duality these first arrows are W' tensored with the duals of
H⁰(O2) --l--> H⁰(O3). The latter are injective for every nonzero l, and
their images as l ranges over the pencil span H⁰(O3). Hence every L arrow
is onto and their common kernel is zero.

## 3. An elementary two-arrow splitting lemma

Let P_m be the two-arrow system H⁰(Om)→H⁰(O(m+1)) with multiplication,
and let I_n be H⁰(O(n+1))*→H⁰(On)* with dual multiplication. Every
extension of P_m by I_n splits, for all nonnegative m,n.
Here is a direct proof, without importing a classification theorem.
Choose monomial bases solely for this universal linear-algebra proof.
The P_m arrows Mx,My insert a length m+1 column in the first or last
m+1 coordinates of length m+2. The I_n arrows Cx,Cy discard the last
or first coordinate of a length n+2 column. To remove arbitrary extension
cross terms Hx,Hy of size (n+1) by (m+1), it suffices to solve

    Cx F - G Mx = Hx,       Cy F - G My = Hy.        (5)

Let F have size(n+2)×(m+1), G size(n+1)×(m+2), with zero-based indices.
Set F_0,j=0 and F_i,m=0 for i≥1. Recursively, for i=0,...,n and
j=0,...,m-1, set

    F_(i+1),j = F_i,(j+1) + Hy_i,j - Hx_i,(j+1).

Then put G_i,j=F_i,j-Hx_i,j for j≤m and
G_i,(m+1)=F_(i+1),m-Hy_i,m. These identities verify both equations(5),
including their final columns. Thus the extension-coboundary map is onto.
This is universal coefficient algebra, not evaluation of any actual pencil.

The assertion persists with constant multiplicity spaces by applying the
same construction to every entry of the multiplicity Hom space. If all
extension data are G-equivariant, average the resulting section over G.
The group acts simultaneously on vertices and the two-dimensional arrow
space; conjugating an intertwining section therefore remains an intertwining
section for the SAME full arrow family. The average is equivariant and
still a section. No pencil-variable change is made to the original system.

## 4. Splitting the exceptional residual extension

Quotienting the imported exact sequence by I gives

    0 → L → K=NR/I --p--> N8 → 0.                   (6)

On the first two vertices, N8=A⊗P4 and L=W'⊗I2. Section3 therefore
supplies a G-equivariant section(s2,s3) commuting with every first arrow.
At vertex four p4 is an isomorphism, so take s4=p4^(-1). Naturality gives

    p4 B_l^K s3 = B_l^8 p3 s3 = B_l^8,

and hence B_l^K s3=s4 B_l^8. Thus the section extends to BOTH pencils,
and K≅L⊕N8. The genuine first-block splitting N=N0⊕NR now proves the
theorem. This stronger splitting argument works despite p3 NOT being an
isomorphism; it does not reuse the regular quotient's invalid exceptional
section argument.

Every first arrow of N0 is injective: its first two spaces are
Sym⁸W⊗H⁰(O0) and Sym⁸W⊗H⁰(O1). The same holds for N8 by multiplication.
Their ranks are9 and15. L contributes rank6, proving rank30 and common
kernel zero for the whole quotient. In particular there is no nonzero
isolated initial-vertex subpencil of this exceptional quotient. Nevertheless
all two-arrow composites vanish on L2 because L4=0; linear-arrow and
quadratic-arrow common kernels must not be confused.

## 5. Scope of verification

verify.py authenticates every exact input by SHA256 AND Git blob, checks
character/dimension identities and cohomology vanishings, and solves (5)
for every elementary cross term of the relevant scalar 30-dimensional
extension-target space. It checks arbitrary linear combinations symbolically
through this basis, the complete 30×38 coboundary rank, its eight-dimensional
kernel, the six multiplicity pairs, and polynomial full-rank minors and
common-kernel identities of the contraction pencil. These are synthetic
universal checks, not actual-source samples or proof-assistant certification.
The written argument, rather than bounded testing, establishes universality.
