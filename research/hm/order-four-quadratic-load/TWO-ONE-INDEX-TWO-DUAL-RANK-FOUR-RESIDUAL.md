# Source2 has four residual dual sources and two necessary dual kernels

## Result

For stable ID **G3.21.d610e381ed75**, source index2,

    A=O(-8)+O2+O16,  B=O(-18)+O(-4)+O6,

the published equality theorem forces U=(P+D)O(-2) as a saturated top subbundle of Q*. It splits off equivariantly. Writing Q*=U+R, the two actual cohomology identities leave six possible rank-four residuals; the actual quotient Q*->B eliminates two. The four remaining necessary residuals are

    R1=O(-18)+O(-8)+O(-6)+O(-4),
    R2=O(-18)+O(-8)+W O(-5),
    R3=O(-18)+W O(-7)+O(-4),
    R4=O(-18)+A_std O(-6).

Moreover the same actual quotient forces

    R1 or R2: L=(Wp+T)O(-3)+O(-8)+O(-6),
    R3 or R4: L=(Wp+T)O(-3)+W O(-7),

where L=(Q*)^- is the actual dual Gauss kernel. This is a source/quotient parameterization and necessary-condition reduction, not a quotient-label exclusion or a realization assertion. It is independent of the second primal defect and the previously studied scalar torsion strata.

## 1. Split off the published top osculating subbundle

PR733 at commit3349988b5c3fc82dbca0741fc1b5fe70af1c7d0d proves that this source2 label uses height(8,2,0), not(7,3,0), and contains the saturated eighth osculating bundle of a full degree-ten rational-normal system:

    U=Sym8 W O(-2)=(P+D)O(-2) subset Q*.

The actual profile has k=2, so H0(Q*(1))=0 and top Q*<=-2. Every map from an O(-2) block to a lower-degree block vanishes. Thus U embeds as a constant coefficient subrepresentation of the entire degree -2 block. Finite-group semisimplicity gives an equivariant complement there, proving Q*=U+R without assuming a splitting of its connection.

Since rank Q*=13 and deg Q*=-54, R has rank4, degree -36 and top<=-2. In particular every ordinary residual degree is at least -36-3(-2)=-30.

## 2. Exact, complete residual enumeration

The actual source presentation gives

    H1(Q*(-1))=M3=3Wp+3S+6T,
    H1(Q*)=M2=A_std+2V+3P+4D.

Subtracting the contribution of U gives

    H1(R(-1))=2Wp+2S+4T,
    H1(R)=A_std+2V+2P+3D.                         (1)

A block rho O(e) contributes rho Sym^(-e-1) W to the first character and rho Sym^(-e-2) W to the second, since -30<=e<=-2. Only irreducibles of dimension at most4 can occur. The center-even convention requires even e for even irreducibles and odd e for odd irreducibles.

The checker exhausts exactly these finitely many blocks and all their multisets of total rank4 and degree -36 satisfying (1). Twenty-one blocks survive the componentwise initial character bounds, and there are exactly six full solutions: R1 through R4 above and

    R5=Wp O(-11)+O(-8)+O(-6),
    R6=Wp O(-11)+W O(-7).

No unpublished source list or witness dataset is used. The degree window follows from the rank, degree and top bound, so it is not a heuristic truncation.

The actual surjection Q*->B must project nontrivially onto O(-18). For R5 and R6 every ordinary degree of U+R exceeds -18, so all maps to O(-18) vanish. They are impossible. Each of the four remaining residuals contains exactly one O(-18), which must supply that target with nonzero scalar.

## 3. Equality fixes the top quotient map

Use the actual longest-chain symbols proved in PR733, not merely the existence of an abstract copy of U. Its seventh osculating bundle

    U7=Sym7 W O(-3)=(Wp+T)O(-3)

lies in L. The next highest-line symbol is an isomorphism onto the top O6 quotient of B. Consequently U/U7=O6 maps isomorphically to that summand. Maps from O6 to the lower O(-18),O(-4) summands vanish. Thus the restriction of the actual quotient Q*->B to U is the canonical equivariant evaluation map U->O6, with kernel U7.

Any component R->O6 lifts equivariantly through U->O6. Indeed for every block rho O(e) in the four residuals, e<=-4, so

    Ext1(rho O(e),U7)=H1(Sym7 W tensor rho* O(-3-e))=0,

because -3-e>=1. Taking invariants preserves exactness. A triangular source automorphism therefore removes the R->O6 component. This handles arbitrary scalar choices in that component, including zero; it does not impose an extra condition on the actual connection. The U components to the two negative targets are already zero by degree. Hence

    L is isomorphic to U7 + ker(R -> O(-18)+O(-4)).       (2)

## 4. The two residual kernel types

The O(-18) projection is a nonzero scalar from the unique O(-18) source line; all other source components to it vanish. Its cross-component to O(-4) is also zero because (Sym14 W)^G=0. Remove this matching source/target line. For the remaining rank-three residual R', the map to O(-4) is forced up to a nonzero scalar as follows:

- R1': O(-8)+O(-6)+O(-4). Only O(-4) maps, giving kernel O(-8)+O(-6).
- R2': O(-8)+W O(-5). Only W O(-5) maps, by the degree-one evaluation; its kernel is O(-6), giving O(-8)+O(-6).
- R3': W O(-7)+O(-4). The W component is zero since W is not a constituent of Sym3 W. The kernel is W O(-7).
- R4': A_std O(-6)=Sym2 W O(-6). Its degree-two evaluation to O(-4) has kernel W O(-7).

In each row the relevant equivariant map space is one-dimensional, and global surjectivity forces its scalar to be nonzero. Thus no additional scalar stratum has been discarded. Substitution into (2) proves the two stated actual L splitting types, each of rank10 and degree -38.

## Reproduction and scope

Run `python3 verify_two_one_index_two_dual_rank_four_residual.py` to generate `two-one-index-two-dual-rank-four-residual.json`. The standalone exact-character verifier pins the baseline quotient data, actual source note and published equality theorem. It regenerates the residual list from (1), checks the quotient-support exclusion, symmetric-power identifications, Ext-degree bounds, all lower quotient Hom spaces and the resulting L ranks/degrees.

This result retains four possible Q* splittings and two possible L splittings; it proves no realization and excludes no stable quotient label. There are no selected actual coefficients or points, matrices or actual-instance rank calculations, scans, spikes or consumed experiments. Earlier torsion-stratum files remain unchanged.
