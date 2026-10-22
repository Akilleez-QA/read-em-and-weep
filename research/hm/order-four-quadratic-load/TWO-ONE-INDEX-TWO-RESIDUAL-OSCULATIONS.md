# Two residual osculations force a unique source2 dual splitting

## Result

For stable ID **G3.21.d610e381ed75**, source index2, the four necessary dual residual sources of PR738 reduce to the single possibility

    R=O(-18)+A_std O(-6).

Consequently the actual bundles must split as

    Q*=(P+D)O(-2)+O(-18)+A_std O(-6),
    L=(Wp+T)O(-3)+W O(-7).

Inside the genuine constant quotient of PR744, R contains an actual degree-eight line C=O(-8). Its first and second osculating bundles are respectively

    C^+=W O(-7),    C^{++}=A_std O(-6).

This reduces four necessary source types to one, not the number of quotient labels. No realization is asserted, and R^- is not assumed equal to C^+.

## 1. Published geometric input

PR738, commit92c1580998dd5476458e32d8d6c2ca14a9c55edb, proves that R is one of

    R1=O(-18)+O(-8)+O(-6)+O(-4),
    R2=O(-18)+O(-8)+W O(-5),
    R3=O(-18)+W O(-7)+O(-4),
    R4=O(-18)+A_std O(-6).

It also identifies the quotient R->O(-18)+O(-4) with kernel S, where S=O(-8)+O(-6) for R1,R2 and S=W O(-7) for R3,R4.

PR744, commit2348d4b6fb2afd67d66b15aad6037ab92c94f076, proves that this very R is saturated in the genuine constant quotient (H*/V0) tensor O. It proves S is contained in R^-; it does not identify them. Since R/S is locally free, S is saturated in that same constant bundle. These facts, rather than a connection on an arbitrary complement, are essential below.

## 2. S has a forced nonzero derivative and kernel O(-8)

Because S lies in R^-, differentiating its local sections stays inside R. Its own second fundamental form therefore factors through

    S -> (R/S)(-2)=O(-20)+O(-6).                         (1)

The O(-20) component is zero by degree. For S=O(-8)+O(-6), the O(-8) component to O(-6) vanishes because (Sym2 W)^G=0, while the O(-6) component is a scalar. For S=W O(-7), the map to O(-6) is a scalar multiple of the canonical degree-one evaluation. These map spaces are exactly one-dimensional.

In either case the scalar is nonzero. Otherwise S would be a horizontal saturated subbundle of a constant bundle, hence a constant subspace bundle, contrary to deg S=-14. Thus (1) is everywhere onto O(-6). In both cases its kernel is

    C=S^-=O(-8).

The kernel C is saturated in the constant ambient bundle: it is saturated in S, and S is saturated there.

## 3. A universal osculating map excludes the split S

The actual line inclusion C=O(-8)->Hbar tensor O is given by a linear equivariant coefficient map Sym8 W->Hbar, where Hbar=H*/V0. No injectivity of that coefficient map is assumed. In the complete degree-eight system the first osculating bundle is W O(-7), with fiber l^7 W at a parameter line l. Composing its canonical inclusion into Sym8 W tensor O with the coefficient map gives

    W O(-7) -> Hbar tensor O.

Its generic image is the span of C and its first derivative. This has rank2: rank1 would mean the saturated line C is horizontal, impossible for degree -8. Because C=S^-, the image lies generically in S, and hence everywhere in S since S is saturated in the constant bundle.

If S=O(-8)+O(-6), every map W O(-7)->O(-8) is zero by ordinary degree. The resulting map into S would have generic rank at most1, contradicting rank2. This excludes R1 and R2.

For the remaining S=W O(-7), the rank-two osculating map is an isomorphism: its source and target have the same degree -14, so its nonzero determinant is a constant. Thus S is the actual first osculating bundle of C, not merely an abstractly matching splitting.

## 4. The second osculation excludes R3

The complete degree-eight second osculating bundle is Sym2 W O(-6)=A_std O(-6), with fiber l^6 Sym2 W. Composing again with the actual coefficient map gives

    A_std O(-6) -> Hbar tensor O.                      (2)

The image lies generically in R because C and its first derivative span S, and the derivative of S stays in R. Saturation of R makes (2) factor through R everywhere. Its generic rank is3: the nonzero derivative (1) supplies a direction outside S. In particular this conclusion does not require the degree-eight constant polynomial span to be all of Sym8 W; it may a priori be a quotient of dimension4,5 or9.

For R3=O(-18)+W O(-7)+O(-4), ordinary degree forces every map from A_std O(-6) to the first two summands to vanish. Only the rank-one O(-4) summand can receive it, contradicting the generic rank3 of (2). Thus R3 is excluded.

For R4, the O(-18) component vanishes by degree, and the rank-three map into A_std O(-6) is an isomorphism. This identifies the actual second osculating bundle with that direct factor, proving the stated unique residual and dual source splittings.

## Reproduction and boundary

Run `python3 verify_two_one_index_two_residual_osculations.py` to regenerate `two-one-index-two-residual-osculations.json`. The standalone exact-character checker pins both published prerequisites and the stable baseline row. It checks both derivative supports, the universal osculating degrees/representations, the ordinary-degree rank obstructions and the surviving ranks/degrees. The geometric proof above supplies the actual factorization and generic ranks; these are not actual-instance rank evaluations.

No full degree-eight constant span, no equality R^-=S, and no projection of all B/O6 to an arbitrary line quotient is assumed. No selected coefficients or points, matrices, scans, spikes or consumed experiments are used. Earlier frozen artifacts are unchanged. The quotient label remains possible under this result.
