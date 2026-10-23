# Source2: full residual span, unique primal source and a final line system

## Result and dependencies

For **G3.21.d610e381ed75**, source index2, combine the exact constant-span intersection of PR744 (commit2348d4b6fb2afd67d66b15aad6037ab92c94f076) with `TWO-ONE-INDEX-TWO-RESIDUAL-OSCULATIONS.md`. Use its actual inclusions in the genuine constant quotient Hbar:

    0 -> R -> Hbar tensor O -> E'^* -> 0,
    R=O(-18)+A_std O(-6),
    C=O(-8), C^+=W O(-7), C^{++}=A_std O(-6).

Here rank Hbar=19, and E' has rank15, degree -36 and all degrees in [-8,-2]. We prove three successive necessary reductions:

1. The constant polynomial span of C is the full V1=Sym8 W=P+D, not P or D alone.
2. The actual primal source is forced to

       E=W O(-9)+T O(-3)+(P+D)O(-2).

3. There is a genuine final saturated line system in a constant quotient Hfin=Hbar/V1 of rank10:

       0 -> O(-18) -> Hfin tensor O -> (P+D)O2 -> 0,
       Hfin is isomorphic as a representation to A_std+V+P.

These are necessary structural constraints, not a label exclusion or a realization. In particular the final line system is not declared impossible.

## Step 1. Exclude both proper constant spans

The coefficient map of the actual line C is Sym8 W->Hbar. Since Sym8 W=P+D is multiplicity-free, its nonzero constant polynomial span is P, D or P+D. Write A0=C^{++}=A_std O(-6). It is a saturated subbundle of R (quotient O(-18)), hence of Hbar tensor O. If V is the constant span of C, then A0 lies in V tensor O and is saturated there. Let

    Z=ann_V*(A0) subset V* tensor O.

Projection of the actual E' into V* factors through Z, because E' annihilates R. Its annihilator in V is exactly R intersect (V tensor O).

If V=P, Z is the equivariant line O(-18): dualizing A0 gives a rank-three degree18 quotient of the rank-four constant bundle. There are no nontrivial one-dimensional coefficient characters. Every degree of E' is at least -8, so Hom(E',O(-18))=0. Therefore all of V lies in R. This contradicts negativity of R.

If V=D, Z has rank2 and degree -18. Moreover H0(Z)=0: the induced global map D->H0(A_std O6) is nonzero, hence injective by irreducibility of D. Its exact H1 character is

    H1(Z)=A_std tensor Sym6 W - D = V+2P+D.             (1)

Center-even equivariant splitting and top Z<=-1 give a complete rank-two overlist: four even line pairs of total degree -18, and W O(-9), Wp O(-9). The exact checker applies (1), leaving precisely

    Z=W O(-9),    or    Z=O(-10)+O(-8).

In the first case Hom(E',Z)=0 by the minimum source degree -8, again forcing D inside R. In the second case every component to O(-10) is zero, and any map to O(-8) is a constant coefficient map from degree -8 blocks. Thus the image of E' in Z is either zero or exactly its O(-8) summand, everywhere. The zero case is already impossible. In the other case its annihilator in D is a saturated rank-four degree -8 bundle, contained in R. Both this annihilator and R are saturated in the same constant bundle and have rank4, so they are equal. But deg R=-36, not -8. This excludes V=D.

Consequently the span is the full invariant constant subspace V1=P+D of dimension9. No assumption of a full polynomial span was made in deriving the preceding osculating bundles.

## Step 2. The actual E' has only four possibilities, then only one

The unique W O(-9) block in E was proved in PR744, and E' is its actual projection kernel. Subtracting that block from the two actual E cohomology identities yields

    H1(E'(-1))=2Wp+2S+4T,
    H1(E')=V+2P+2D.                                   (2)

All ordinary degrees lie in [-8,-2]. The checker enumerates irreducible blocks in this complete window, with center parity, rank15, degree -36 and both identities (2). Exactly twelve blocks meet the componentwise preliminary bounds; the complete multiset enumeration gives exactly four solutions:

    E'1=O(-8)+(P+2D)O(-2),
    E'2=Wp O(-5)+(2P+D)O(-2),
    E'3=V O(-4)+(V+P+D)O(-2),
    E'4=T O(-3)+(P+D)O(-2).

In the complete degree-eight system the apolar annihilator of A0, whose fiber is l^6 Sym2 W, has fiber l^3 Sym5 W. Thus

    ann_V1*(A0)=T O(-3).

The actual projection E'->V1* factors through this rank-six bundle. Its image must have generic rank at least5: otherwise its annihilator in the nine-dimensional constant V1 has rank at least5 and would lie in rank-four R.

Every degree -2 block has zero map to T O(-3). The first three candidate sources therefore have projection rank at most1,2,3 respectively, so are impossible. For E'4 the projection is a nonzero scalar isomorphism on T O(-3), since T is irreducible; it is zero on (P+D)O(-2). This proves the unique E' and E splittings stated above, as well as the exact actual projection sequence

    0 -> E''=(P+D)O(-2) -> E' -> T O(-3) -> 0.          (3)

## Step 3. The genuine final rank-one residual

The surjectivity in (3) means the annihilator of its image in V1 is exactly A0. Therefore

    R intersect (V1 tensor O)=A0.

Dualizing (3) shows that (Hbar tensor O)/(R+V1 tensor O)=E''* is locally free. Hence projection to the genuine constant quotient Hfin=Hbar/V1 yields

    0 -> R/A0=O(-18) -> Hfin tensor O -> E''*=(P+D)O2 -> 0.

This proves saturation of the final line, not just a generic projection. Since rank Hbar=19 and rank V1=9, rank Hfin=10.

Dualizing this last sequence and taking cohomology gives

    0 -> Hfin* -> Sym18 W -> P+D -> 0.

The exact decomposition Sym18 W=A_std+V+2P+D therefore forces Hfin*=A_std+V+P, and all these representations are self-dual. In particular the final degree-eighteen system is a ten-dimensional equivariant subsystem of Sym18 W with this character. Its realization and syzygy conditions remain open here; this is not a classification of all embeddings of the original source.

## Reproduction and scope

Run `python3 verify_two_one_index_two_residual_full_span.py` to generate `two-one-index-two-residual-full-span.json`. It pins the prerequisite notes and baseline stable row; derives the two H1 targets; enumerates all four E' types and the complete rank-two annihilator overlist; checks the rank-support obstructions, degrees, symmetric powers and final constant representation.

The proof uses only actual projection/annihilator exact sequences and universal osculating geometry. It assumes neither R^-=C^+ nor a projection of B to an arbitrary bundle complement. No selected coefficients or points, actual-instance matrices/ranks, scans, spikes or consumed experiments are used. No prior frozen files or label counts change.
