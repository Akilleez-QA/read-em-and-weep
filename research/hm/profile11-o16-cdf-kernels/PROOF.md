# Three necessary high-P kernels remain for the c-d-f source127 edge

## Result and boundary

Consider the original zero-defect source edge

    G3.11.cce6e3ba4eeb, source_index127,
    (0,0,1,1,0,1,0,0),
    E=(P+D) O(-2)+(V+P) O(-4)+O(-8),
    A_q=O(-8)+O(2)+O(16).

PR859 proves that the high-only P O(-2) subsystem in this exact source has no common divisor. Its actual external derivative is therefore onto O(16), and its exact kernel is necessarily one of

    A O(-8);
    W O(-7)+O(-10);
    Wp O(-3)+O(-18).                              (1)

The proof first classifies five possible exact kernels, then excludes two entire kernel branches using saturated internal images and first-polar characters. The remaining forms in (1) are necessary, not asserted realizable. No entire source edge or stable label is excluded. The basepoint-free input is the explicit immutable PR859 dependency below, rather than an unstated assumption.

No selected actual HM/source coefficients, parameters, points, derivative values, matrices, source-instance ranks, selected models, scans, or large computation are used. The attached verifier performs only a fixed thirteen-candidate abstract representation check and reads original pinned source data.

## 1. Pinned actual input

PR859, commit 6129e92a26572779003f3295227f688b77ed881c, proves that this exact source's high-P system is basepoint-free. It excludes the only possible common-divisor degree twelve without assuming a saturated external O(16) image in that branch. Its conclusion is used only to obtain the onto map (2):

https://github.com/Akilleez-QA/read-em-and-weep/blob/6129e92a26572779003f3295227f688b77ed881c/research/hm/profile11-o16-high-p-divisor/PROOF.md

All original actual source, strict-top, quotient and stable-label data are at commit db51525015bb7c5e825833d550d08dedf6f6ea96, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact files are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, one-one-endpoint-necessary-pairs.json and rank-three-quotient-frontier-144.json. The accompanying manifest records immutable URLs and Git blob hashes. Applying the original decoder to the displayed tuple gives exactly the displayed rank17, degree-54 E.

The actual E is saturated in a constant bundle H O and H0(E^-(2))=0. Original defect zero identifies the actual raw derivative quotient A_q with a saturated subbundle of (H O/E)(-2). Thus its O(16) summand is saturated there.

We use the saturated internal/external derivative-image lemma from PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac, Section3:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

If F has saturated external derivative image U and the actual internal image J from ker(F->U) into (E/F)(-2) is saturated, then the full raw derivative image I is saturated, with 0->J->I->U->0, and the actual first span M=F^+ satisfies 0->F->M->I(2)->0.

First-polar generation and the needed representation identities are in PR802, commit e484640a6565c278321bf6557860262c1ac1b7df, Sections3 and5:

https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

For a quadratic F=R O(-2) whose raw first span is saturated, the canonical polar map R W O(-1)->F^+ is onto. Hence F^+ has splitting degrees0 and-1, because F^+(1) is generated and F^+ lies in a constant bundle. No no-section condition on E^+ is used.

Work over C with the binary icosahedral group G and the notation W,Wp,A,V,P,S,D,T from those sources. Their dimensions are2,2,3,3,4,4,5,6 respectively, with A=Sym2 W, S=Sym3 W, D=Sym4 W and T=Sym5 W. G is perfect and all irreducibles are self-dual. Every bundle map below uses the actual ambient connection; equivariant splitting is not treated as horizontal splitting.

## 2. Exact kernel classification from two small characters

Let F=P O(-2), a saturated direct summand of E. Its components to O(-8) and O(2) vanish by degree and P not occurring in Sym4 W=D. By the cited basepoint-free theorem its external map gives

    0 -> K -> P O(-2) -> O(16) ->0.              (2)

Strict-top makes the map on twist-two sections injective. Consequently every ordinary splitting degree of K is at most-3. Its rank is3 and degree-24. The exact character constraints are

    H1(K(2))=Sym18 W-P=A+V+P+D,
    chi_G(K(3))=P W-Sym19 W=-(W+S+T).            (3)

Here Sym18 W=A+V+2P+D, Sym19 W=W+Wp+S+2T and P W=Wp+T.

The small rank makes the possibilities exhaustive without a large search. A rank-three equivariant bundle is of exactly one of these forms:

- one dimension-three irreducible block, A O(-8) or V O(-8);
- one dimension-two odd block U O(-j), U=W or Wp, together with a scalar O(-k), where 2j+k=24, j>=3 odd and k>=4 even;
- three scalar even-degree blocks O(-j1)+O(-j2)+O(-j3), with j1+j2+j3=24 and each ji>=4.

These alternatives use the complete irreducible dimensions and central parity; there are no other rank-three coefficient combinations. The first character in (3) has no invariant constituent. Thus a scalar degree-four block is impossible. In the two-space case the possible pairs (j,k) are precisely (3,18),(5,14),(7,10),(9,6). In the three-scalar case the possible sorted degree triples are precisely (6,6,12),(6,8,10),(8,8,8).

For an atom R O(-j), j>=4, its contribution to H1(K(2)) is R Sym(j-4) W. A j=3 atom contributes its coefficient to chi(K(3)); a j>=5 atom contributes -R Sym(j-5) W, while a j=4 atom contributes zero. Applying these formulas gives:

    candidate                        H1(K(2))                 chi(K(3)) when first matches
    A O(-8)                          A+V+P+D                  -(W+S+T)
    V O(-8)                          A+V+P+D                  -(Wp+S+T)
    W O(-3)+O(-18)                   A+V+P+D                  -(Wp+S+T)
    Wp O(-3)+O(-18)                  A+V+P+D                  -(W+S+T)
    W O(-5)+O(-14)                   1+2A+V+D                 not needed
    Wp O(-5)+O(-14)                  A+V+P+D                  -(Wp+S+T)
    W O(-7)+O(-10)                   A+V+P+D                  -(W+S+T)
    Wp O(-7)+O(-10)                  2V+P+D                   not needed
    W O(-9)+O(-6)                    A+V+P+D                  -(W+S+T)
    Wp O(-9)+O(-6)                   2A+P+D                   not needed
    O(-6)+O(-6)+O(-12)               2A+P+D                   not needed
    O(-6)+O(-8)+O(-10)               A+V+P+D                  -(W+S+T)
    O(-8)+O(-8)+O(-8)                3D                       not needed

Thus the complete necessary kernel list before further geometry is exactly

    A O(-8);
    W O(-7)+O(-10);
    W O(-9)+O(-6);
    Wp O(-3)+O(-18);
    O(-6)+O(-8)+O(-10).                          (4)

No item is being chosen as an actual instance, and matching these characters does not prove realizability.

## 3. Exclude W O(-9)+O(-6) through its actual saturated line image

The actual internal target for (2) is

    (E/F)(-2)=D O(-4)+(V+P) O(-6)+O(-10).        (5)

For K=W O(-9)+O(-6), its only possible component is

    W O(-9) -> D O(-4).                          (6)

Indeed W does not occur in V Sym3 W=Wp+S+T or P Sym3 W=S+2T, so the degree-three channels to V/P vanish. The O(-6) same-degree V/P components vanish by irreducibility; its D component would require D in Sym2 W=A. Every component to O(-10) vanishes by degree.

The equivariant Hom space in (6) is one-dimensional. Its universal nonzero map factors as

    W O(-9) -> O(-8) -> D O(-4).                (7)

The first arrow is the Euler surjection, with kernel O(-10). The second is the everywhere-injective tautological fourth-power line. At an arbitrary line l in W it sends the line generator to l^4 in Sym4 W. The composite is nonzero, so uniqueness identifies every nonzero map in (6) up to scalar. This argument evaluates no selected point or coefficient. Its image is the saturated O(-8) subbundle of D O(-4).

Thus the actual internal image J is either0 or O(-8), with no torsion modification. The external O(16) is saturated. The actual-image lemma yields a saturated M=F^+ of degree

    deg M=-8+18=10            if J=0,
    deg M=-8+18-6=4          if J=O(-8).

Both are positive, impossible for a subbundle of a constant bundle. This excludes the entire third kernel branch of (4).

## 4. Exclude O(-6)+O(-8)+O(-10) with every scalar-row alternative retained

For this kernel and target (5), the only nonzero possible components are

    O(-8) -> D O(-4),
    O(-10) -> O(-10).                            (8)

To check every apparent extra component, the scalar maps to V/P would require either a trivial equal-degree map or V/P in Sym2 W or Sym4 W, all impossible. The other D components would require D in Sym2 W or Sym6 W=V+P, also impossible. The lower target admits only the indicated same-degree scalar.

A nonzero first map in (8) is the saturated tautological fourth-power line O(-8); a nonzero second map is an isomorphism to the scalar target. Since they land in different direct summands, their direct sum is saturated as well. Consequently the four exhaustive internal images are

    0, O(-8), O(-10), O(-8)+O(-10).             (9)

The first three give degree M equal to10,4,2 respectively, already impossible. In the final case the actual-image lemma gives rank M=7 and degree M=-4. First-polar generation forces splitting degrees0 and-1. If C and L are its constant and linear coefficient representations, then C=chi_G(M) and C W+L=chi_G(M(1)). The exact sequences give

    C=-P+Sym18 W-Sym4 W-Sym6 W=A,
    C W+L=Sym19 W-Sym3 W-Sym5 W=W+Wp+T.

Since A W=W+S, this would require

    L=Wp+T-S.

The negative S multiplicity is impossible in a genuine representation. Thus the final alternative in (9) is also excluded. This removes the fifth kernel branch of (4) without discarding either internal row.

## Conclusion and next unresolved interfaces

Removing the two excluded branches from the complete list (4) leaves exactly (1). This does not imply that any remaining kernel exists in the actual problem.

The remaining internal targets are not empty. For example A O(-8) has a nonzero possible map to D O(-4); W O(-7)+O(-10) has both a D component and a scalar lower component; and the O(-18) in the final branch can map to D O(-4) and P O(-6). None of those channels is assumed zero. Their compatibility with the actual connection and the complementary endpoint rows remains a separate problem.

The verifier checks the thirteen candidates, the complete internal Hom vanishings used for the two exclusions, the multiplicity-one universal maps, source identity, and polar characters. It does not replace the actual saturation and connection arguments. This is a written branch reduction, not Lean certification, a whole-source exclusion, or a global result.
