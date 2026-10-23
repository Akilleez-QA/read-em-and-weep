# The separated terminal graph has two distinct symmetric gate channels

## Statement

Retain the actual source2 nonzero pure-V compatible-radical hypotheses,
and assume the canonical P_h has nonzero projection to the genuine
separated block N0,2. In the fixed PR1031 basis R=alpha R1+beta R2,
the two separated terminal channels correspond to the lines

    Sym5 terminal channel:       R1-4R2,
    T in Sym7 terminal channel:   3R1+2R2.                 (1)

They are independent. The actual gate has the unique form

    R=A (R1-4R2)+B (3R1+2R2),                            (2)

where A,B are the two coherently normalized components of the actual
terminal functional pulled back along the actual graph. Both may be
zero. In particular R=0 iff both components vanish. Neither component,
the graph, nor realization of any gate is selected.

The new content is the precise correspondence (1), not the tautological
fact that any two independent vectors span a plane. The separated
terminal graph, unlike the residual one-channel quotient, imposes no
linear relation on R by itself: its two formal functional components
map isomorphically onto the full symmetric gate plane. This is NOT an
assertion that arbitrary functional components occur in actual HM.

## 1. Pinned actual quotient and graph

INPUTS.json retains exact public originals: PR1081 at
411b644cdc12938c35b7fedac5bb92664bfc1a47, PR1094 at
79b84d3b21cdbc76bb19d3a973e09981936dda32, PR1031 proof and model at
7150cf97eeebe473bcd7c61c1f968c73625d92ef, and PR1036 proof and verifier
at bb22e239e9423b54487236dba8c4f70f9e6b738f. Paths and byte digests
are recorded there. The historical PR1036 verifier is read as a pinned
normalization source, not executed. No actual source data is evaluated.

PR1081 derives, with the genuine multiplication projectors, the actual
quotient

    N0,5=(Sym3 W tensor Sym8 W)/(W Delta_2 Sym10 W)
         --C--> Sym7 W plus Sym5 W,
    C(c tensor f)=((c,f)_2,(c,f)_3).                    (3)

The relation space has dimension22 and is exactly ker C. Its proof
tracks actual Koszul determinant conventions, not only characters.
The cubic descendants of the unique P8 in Sym8 have rank12, with
kernel S and image T7 plus T5, the full T-isotypical part of (3).
Here T7 is the unique T constituent of Sym7=W'+T, and T5=Sym5.
The actual projection

    e5:F5 -> T7 plus T5

is an isomorphism. Write g for its inverse, including its actual graph
into NR5=T. We do NOT identify g with the zero graph or replace it
by an arbitrary equal-character inclusion.

PR1094 supplies the actual functional ell:im Q3=3T -> I3 and the
Spencer identity

    ell(c s(p))=i3(D(U_p)(c)),
    D(U)(c)=xU(yc)-yU(xc),  R(a)p=i2(U_p(a^2)),        (4)

where s:I4->P_h is the actual inverse of Q2, and i2,i3 are the coherent
f12 multiplication identifications with Sym4,Sym5. Spencer has kernel
C Id on End(Sym4). It is therefore injective on equivariant P-families:
Hom_G(P,1)=0. In fact it is an isomorphism onto the two-dimensional
space Hom_G(Sym3 W tensor P,T). This also follows from its full rank24
and the source decomposition Sym3 W tensor P=S+2T.

## 2. Coherent universal channel representatives

Use unnormalized transvectants

    (f,g)_k=sum_j (-1)^j binom(k,j)
           partial_x^(k-j)partial_y^j f
           partial_x^j partial_y^(k-j) g.

Let Pi:Sym6->P and E:P->Sym6 be the exact apolar orthogonal projection
and inclusion of PR1031, Pi E=Id. Let F12 be the invariant Wronskian
of ker Pi, with the precise normalization in PR1036:

    F12=-2x^12-(44sqrt5/5)x^10y^2+66x^8y^4
        +(88sqrt5/5)x^6y^6+66x^4y^8
        -(44sqrt5/5)x^2y^10-2y^12.

This is universal representation data, not the coefficient of an
actual HM instance. Define

    f_p=(F12,E p)_5 in Sym8,
    J7(v)=(F12,v)_7 in Sym5.                          (5)

These maps are equivariant because F12 is invariant. Exact full-matrix
checks show that p->f_p has rank4 and J7 has rank6. Since Sym8 has
P multiplicity one, the former is precisely its P8 inclusion up to
coherent nonzero scalar. Since Sym7=W'+T, J7 kills W' and is an
isomorphism on T7. Define the two cubic families

    C5(c,p)=(c,f_p)_3,
    C7(c,p)=J7((c,f_p)_2).                            (6)

Each has rank6, and their stacked coefficient matrix has rank12.
Thus these are independent maps, not two names for the same T row.

There is an unselected nonzero scalar eta such that e2 s(p)=eta f_p.
Naturality of the genuine separated projection then gives

    c s(p)=g(eta ((c,f_p)_2,(c,f_p)_3)).               (7)

Both sides are actual elements of F5; its projection is an isomorphism.
Write the actual row i3^-1 ell g on T7 plus T5 as

    lambda7 J7 plus lambda5 Id.

The scalars lambda7,lambda5 include every effect of the actual graph;
we do not discard its residual component. Equations (4) and (7) give

    D(U_p)=eta lambda5 C5(-,p)+eta lambda7 C7(-,p).    (8)

## 3. Exact Spencer inverses and gate lines

For every cubic c and octavic f, the full polynomial identity is

    x(yc,f)_4-y(xc,f)_4=-20(c,f)_3.                  (9)

Hence U5_p(v)=-(v,f_p)_4/20 is the inverse of C5. In the fixed
apolar conventions of PR1031 the checker proves, with all three
quadratic coordinates and all four P coordinates formal,

    U5_p(a^2)=k5 (R1(a)-4R2(a))p,
    k5=6131220480 sqrt5.                             (10)

For C7 let U7_p be its unique trace-zero Spencer inverse. Existence
and uniqueness follow because D induces an isomorphism from the
trace-zero complement of C Id to Hom(Sym3,Sym5). This complement is
G-stable under conjugation. The inverse therefore gives an equivariant
P-family, rather than a collection of unrelated column choices.
The exact coefficient solve verifies all Spencer equations and gives

    U7_p(a^2)=k7 (3R1(a)+2R2(a))p,
    k7=-78316384529940480000.                        (11)

The proof does not infer either line from characters alone. The
bounded verifier reconstructs the complete 24-by25 Spencer matrix,
solves all four families, removes the scalar trace, and compares all
quadratic coefficients with the pinned R1,R2 matrices.

Spencer uniqueness on P-families applied to (8) now proves (2), with

    A=eta lambda5 k5,   B=eta lambda7 k7.             (12)

A scalar-identity correction cannot remain, since it would be a
G-map P->1. The determinant of the channel-coordinate matrix
[[1,3],[-4,2]] is14. Consequently the correspondence from the two
functional components to the full gate plane is an isomorphism.
Equivalently alpha=A+3B, beta=-4A+2B, and

    A=(2alpha-3beta)/14,   B=(4alpha+beta)/14.

Thus vanishing of the Sym7 functional component is exactly the linear
condition beta=-4alpha; vanishing of the Sym5 component is exactly
2alpha=3beta. These conditions include the zero gate; for nonzero gates
the corresponding projective ratios are1:-4 and3:2, respectively.
Simultaneous vanishing is precisely ell(F5)=0, consistent with PR1094.
No further linear restriction follows solely from the graph description.

## Scope and verification

Run python verify.py and python -O verify.py; both reproduce RESULT.json.
The full-coefficient calculations use only fixed universal representations.
There are no actual HM coefficients, selected directions, points, jets,
source-instance matrices or ranks. Written actual-map naturality in
Sections1-2 is essential and is not replaced by the universal solves.
The theorem is conditional on the nonzero N0 mechanism and does not
transfer its two-channel conclusion to the residual-large mechanism.
It does not address the opposite pencil, source occurrence, or gate
nonvanishing. In particular the actual terminal row is not freely chosen
merely because its ambient equivariant Hom space has dimension two.
