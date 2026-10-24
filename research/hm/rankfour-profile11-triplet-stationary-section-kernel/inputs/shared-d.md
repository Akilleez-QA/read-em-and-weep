# The two positive-triplet scalar curves must share the actual D block

## 1. Statement and retained boundary

Work over C on the physical binary-icosahedral line P(W*), with G=SL2(F5) and the fixed determinant convention. Retain the original actual rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

Use the conclusions of PR1205 at immutable commit 97dad5c307a04f61d850e8a4211559e97ed4c2fd. In its genuine constant ambient C of dimension21, the actual bundles are

    E0=D(-2)+(W'+T6)(-3)+V(-4),
    S0=ann(E0) in C* O,  L0=S0^-=U+T,
    U=O(-10),  T=O(-18),  S0/L0=A(-6),
    M=L0^+=W(-9)+W(-17),  S0/M=O(6).

The intrinsic first-jet map identifies P^1(L0*)* with the actual saturated M. Let C10 and C18 be the actual constant coefficient spans of U and T in C*. The preceding theorem proves

    C*=C10+C18=2A+2V+P+D,
    C10=A+V or A+V+D,
    C18=A+V+P or A+V+P+D.

The two copies of A and the two copies of V are independent, and at least one curve retains D. If both retain D their intersection is exactly that common D; otherwise the two constant spans are disjoint. No individual completeness was assumed in obtaining these alternatives.

Then necessarily

    C10=A+V+D,  C18=A+V+P+D,
    C10 intersect C18 = D.

In particular the degree-ten curve has a complete coefficient system, and the degree-eighteen curve has fifteen-dimensional coefficient span, losing exactly one P copy. Both previously permitted disjoint-span alternatives are excluded. Equivalently the D part of the actual coefficient kernel in Sym10 W+Sym18 W projects isomorphically to each of the two D summands; it is not supported on either one alone. The P part remains a four-dimensional kernel inside the two-copy P isotypic component of Sym18 W.

This does not exclude or realize the whole full-positive-image branch, any whole K splitting, the triplet quotient or the maximal profile. The other coherent endpoint images of PR1199 remain separate. The original defect t=0 is unchanged.

## 2. Inputs and the missing actual-subbundle bridge

INPUTS.json records complete freshly fetched immutable sources, including their Git blobs, byte lengths and SHA256 hashes. The principal input is the complete PR1205 proof. The retained PR1199 proof supplies the universal principal-parts identity, and ACTUAL supplies the physical representation and equivariant splitting conventions. Their transitive actual-geometric hypotheses remain assumptions; no rank-seventeen theorem is transferred to E0.

Set

    F=ann(M) in C O.

All annihilators here use the actual constant perfect pairing C x C*. Since M is a saturated subbundle of S0 with quotient O(6), duality in the actual constant ambient gives an exact sequence of bundles

    0 -> E0 -> F -> O(-6) -> 0.                    (1)

The extension group is

    Ext1(O(-6),E0)=H1(E0(6))=0,

because E0(6)=D(4)+(W'+T6)(3)+V(2). Averaging a splitting over G yields the equivariant bundle isomorphism

    F=D(-2)+(W'+T6)(-3)+V(-4)+O(-6).             (2)

More importantly, the actual inclusion E0 in F is canonical: it is exactly the Harder-Narasimhan subbundle F_{>=-4}. Indeed the summands of degree at least -4 in (2) map to zero under the actual quotient F->O(-6), by ordinary degree. That quotient is onto, so its scalar map on the remaining O(-6) is nonzero. Its kernel is therefore precisely F_{>=-4}. This argument identifies the actual kernel, not an arbitrarily chosen extension splitting.

Neither (2) nor equivariant Birkhoff splitting declares a connection horizontal. The constant-span decompositions used next are genuine decompositions of constant vector spaces. Only after deriving (1)-(2) will they imply a decomposition of E0 in a particular case.

## 3. What disjoint coefficient spans actually split

Let M10 and M18 denote the actual first-jet subbundles of U and T. The intrinsic identification already proved for M gives

    M=M10+M18,
    M10=W(-9),  M18=W(-17).

The two jet maps are everywhere injective and their direct sum is the actual M. Each Mi is saturated in its constant coefficient span: it is saturated in C* O, hence in Ci O. Define

    F10=ann_(C10)(M10) in C10* O,
    F18=ann_(C18)(M18) in C18* O.

Here the subscript specifies the smaller constant ambient; in particular these are not automatically annihilators of summands of S0.

If C10 intersect C18=0, the actual constant decomposition C*=C10 direct-sum C18 gives

    C=C10* direct-sum C18*,  F=F10 direct-sum F18. (3)

The first-jet degrees give

    rank F10=dim C10-2,  deg F10=-18,
    rank F18=dim C18-2,  deg F18=-34.             (4)

These statements follow from the exact quotient onto Mi*; no completeness of either individual system is being assumed. The Harder-Narasimhan graded representations of an equivariant direct summand of F are direct summands of the corresponding graded representations in (2).

## 4. Degree-ten alone retaining D is impossible

Suppose C10=A+V+D and C18=A+V+P. Then their spans are disjoint, dim C10=11 and F10 has rank9, degree-18. Every ordinary degree of F10 is at most-2 because it is a direct summand of (2). The sum of its nine ordinary degrees is-18, so all nine must equal-2. But F has only five ordinary degree-minus-two summands, namely D(-2). This contradicts (3).

One can also see the representation obstruction directly: dim Sym10 W=11, so the surjective degree-ten coefficient map to C10 is now an isomorphism. Its complete first-jet annihilator is

    F10=Sym8 W(-2)=(P+D)(-2),

which cannot be a direct summand of F because (2) contains no P(-2). Completeness is deduced in this case, not presumed before it.

## 5. Degree-eighteen alone retaining D is impossible

Suppose C10=A+V and C18=A+V+P+D. Again their spans are disjoint. Now F10 has rank4, degree-18. By (2)-(3), its slope-graded coefficient representations are direct summands of exactly

    D at -2,  W'+T6 at -3,  V at -4,  1 at -6.

The irreducible D and T6 have dimension five and six, so neither fits in rank four. The single W' has dimension two, but the remaining available V and 1 have dimensions three and one, with no second scalar or doublet: it cannot be completed to rank four. The unique possibility is consequently

    F10=V(-4)+O(-6),
    F18=D(-2)+(W'+T6)(-3).                       (5)

This is a direct-summand argument involving four fixed irreducible blocks, not a bundle-candidate search. The degrees in (5) are respectively-18 and-34, as required.

Use the actual identification E0=F_{>=-4} from Section2. Harder-Narasimhan truncation respects the genuine direct sum (3). Write E10=(F10)_{>=-4}=V(-4), as its actual subbundle of C10* O. Equation (5) therefore forces the actual equality

    E0=E10 direct-sum F18

inside the constant decomposition C10* direct-sum C18*. Taking annihilators in that same decomposition gives

    S0=S10 direct-sum M18,
    S10=ann_(C10*)(E10) in C10 O.                (6)

The actual U lies in S10 and the actual T lies in M18: this follows from U+T=L0 subset S0 and their distinct constant supports. Thus the actual quotient by L0 in (6) is

    S0/L0=(S10/U) direct-sum (M18/T).            (7)

The intrinsic principal-parts exact sequence for T=O(-18) is

    0 -> O(-18) -> P^1(O(18))* -> O(-16) -> 0.

Its identification with the actual first-jet map gives M18/T=O(-16). Consequently (7) makes O(-16) a direct summand, in particular a quotient, of S0/L0=A(-6). But

    Hom(A(-6),O(-16))=A* tensor H0(O(-10))=0.

This contradiction excludes the second disjoint-span alternative. No claim about second jets is required; the given actual L0 and first-principal-parts sequence suffice.

## 6. Consequence for the actual coefficient kernel

At least one D is retained, and Sections4-5 rule out either one alone. Hence both are retained and the actual constant-span intersection is exactly D. Since

    Sym10 W=A+V+D,
    Sym18 W=A+V+2P+D,

the degree-ten coefficient map is an isomorphism to its eleven-dimensional span. On the D isotypic part, the joint coefficient map has the form D direct-sum D -> D, with both scalar entries nonzero. Its kernel is therefore the graph of a nonzero equivariant isomorphism between the two source D summands. This is a coordinate-free nonvanishing and incidence statement; no actual scalar, coefficient, tensor or relative normalization is chosen or evaluated.

The degree-eighteen map still has a P kernel and is not complete. The theorem has established a necessary shared-D compatibility, not actual higher-order realization or algebraicity. No horizontal Birkhoff splitting, connection on a nonconstant quotient, saturation replacement of a coherent image, selected actual instance calculation, broad scan, or large computation occurs.
