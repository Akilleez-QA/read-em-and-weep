# The O(26) branches: eliminate the twelve-point base divisor and force a degree-ten block at the twenty-point divisor

## Result and scope

Consider the three zero-original-defect maximal profile-(1,1) labels

    G3.11.dc58cc54f352:
      A_q=O(-10)+O(-8)+O(26), B_q=O(-28)+O(6)+O(8);
    G3.11.4b6dad66f329:
      A_q=W O(-9)+O(26),     B_q=O(-28)+W O(7);
    G3.11.8ae96830fd21:
      A_q=2 O(-8)+O(26),     B_q=O(-28)+2 O(6).

Let F=R O(-2) be the actual canonical top block of a compatible source E. The positive quotient restricts to a degree-twenty-eight section system on R. Let delta be the degree of its common zero divisor.

Then:

1. delta belongs to {0,12,20}.
2. delta=12 is impossible for every source of all three labels.
3. delta=20 is possible only for the matching E6/E13 sources of the first two labels. In that case there is a genuine invariant constant subspace C of dimension eleven, with

       C=Sym10 W=A+V+D,
       F=U_8^10,
       F^+=U_9^10,
       F^{++}=C O.

Here U_j^e has fiber ell^(e-j) Sym^j W in Sym^e W and is Sym^j W O(j-e). These are actual constant-subspace and osculating-bundle identities, not abstract splittings declared horizontal.

In particular, the third label must have a basepoint-free degree-twenty-eight top system. No delta=0 stratum is excluded by this theorem, and no surviving delta=20 stratum is claimed excluded or constantly separated. Source2 and the original global goal remain open. No selected actual coefficients, parameters, points, derivative values, matrices, source-instance ranks, selected models, scans, or large computation are used.

## 1. Immutable public inputs and exact source overlists

Original actual-bundle, source, quotient, and stable-label data are pinned at

    db51525015bb7c5e825833d550d08dedf6f6ea96

in Akilleez-QA/read-em-and-weep, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact files are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md, one-one-endpoint-necessary-pairs.json, and rank-three-quotient-frontier-144.json.

The source indices are112,115,126. Index112 has exactly

    (0,0,0,0,0,2,0,1), (0,0,0,0,1,1,0,1),
    (0,0,1,0,0,1,0,1), (0,1,0,0,0,1,0,1).

Index115 has those four together with

    (0,0,0,0,0,1,1,0), (0,0,0,0,1,0,1,0),
    (0,0,1,0,0,0,1,0), (0,1,0,0,0,0,1,0).

These give, respectively,

    E0 = (P+2D) O(-2)+2 O(-8)+O(-10),
    U6 = (2P+D) O(-2)+Wp O(-5)+O(-8)+O(-10),
    E3 = (V+P+D) O(-2)+V O(-4)+O(-8)+O(-10),
    E6 = (P+D) O(-2)+T O(-3)+O(-8)+O(-10),

and

    E10 = (P+2D) O(-2)+O(-8)+W O(-9),
    U13 = (2P+D) O(-2)+Wp O(-5)+W O(-9),
    E12 = (V+P+D) O(-2)+V O(-4)+W O(-9),
    E13 = (P+D) O(-2)+T O(-3)+W O(-9).

Index126 has exactly the tuples

    (0,0,0,0,0,2,0,1), (0,0,0,0,0,1,1,0),
    (1,0,1,0,0,2,0,0),

giving E0,E10 and

    E18=2D O(-2)+Wp O(-3)+V O(-4)+2 O(-8).

The labels U6,U13 are local names for the displayed types, not additional catalog indices.

We use the following exact structural dependencies:

- PR796, d2b43060c83328dd5118aee6b9288fcfa0c873ac, research/hm/profile12-quadratic-block-exclusion/PROOF.md: the degree-sixteen top-kernel computations and profile-free quadratic Gauss gap.
- PR797, cdee9396133fb96d4a91babba87b1a7a35903635, research/hm/profile12-tensor-quartic-block/PROOF.md: Sections3-5's small kernel, quotient and constant-span calculations, and Section7's Euler extension. Its interior-stage intersection assumption is not imported.
- PR798, 2bbf244bafc380cf5b0ce1114f86fcd8053e4e55, research/hm/profile12-backward-plateau-exclusion/PROOF.md: generic internal/projected derivative rank additivity and the complete-quartic jet argument.
- PR799, 2172e4a7abbbe232f9f448bea6fa01dee7927460, research/hm/profile11-quadratic-polar-obstruction/PROOF.md: first-polar generation and the two-D-channel contradiction.
- PR804, ae34a9403c0c2abf00516ca35dd494723034c38a, research/hm/profile11-degree28-simple-polar-exclusion/PROOF.md: the simple invariant polar obstruction for a constant fifteen-space with degree-twenty-eight quotient and twelve-point Gauss ramification.

Every path in this list is under the stated repository at its stated immutable commit. Work over C, using the binary-icosahedral notation of these sources. All irreducibles are self-dual. E is saturated in H O, has rank17 and degree-54, and satisfies H0(E(1))=0 and H0(E^-(2))=0. Original defect zero gives the actual saturated derivative image A_q in Q(-2), Q=(H O)/E, and

    E^+/E=A_q(2).                                      (1)

For maximal backward index one, the Gauss rank of E^- is strictly less than three.

## 2. The common divisor and the raw first span

The quotient E->A_q restricts to a map F=R O(-2)->O(26); its negative components vanish by degrees. Strict-top vanishing injects R into H0(O(28)). Its common divisor D_delta is invariant. Dividing by its equation gives an onto map

    pbar:F -> O(26-delta),
    0 -> K0(2) -> R O -> O(28-delta) -> 0.             (2)

Every invariant nonempty divisor has degree at least twelve. Since dim R>=9, the residual section space must have dimension at least nine, so delta<=20. The orbit sizes therefore leave exactly0,12,20. Each nonzero possibility is a single reduced orbit. Its defining semi-invariant is invariant because the binary icosahedral group has no nontrivial one-dimensional characters.

Write J for the internal derivative image of K0 in (E/F)(-2). Let B be the raw sheaf generated by F and its first derivatives, before saturation. Its derivative image I is torsion-free and hence locally free, with exact sequences

    0 -> J -> I -> O(26-delta) -> 0,
    0 -> F -> B -> I(2) -> 0.                           (3)

We do not assume the positive image O(26-delta) is saturated in Q(-2). In particular (3) does not by itself make B saturated.

Let t=length(F^+/B). This is the length of an invariant torsion sheaf, so either t=0 or t>=12. Since F^+ is a subbundle of a constant bundle,

    0 <= t <= -deg B.                                  (4)

The first-polar map R tensor W tensor O(-1)->H O has image exactly B, by the universal value-and-first-derivative identity for quadratic columns. Consequently B(1) is globally generated. Since B injects in a constant bundle, every splitting degree of B is0 or-1. This assertion concerns the image sheaf B; its inclusion into H O need not be fiberwise injective until t=0 is proved.

We repeatedly use the quadratic Gauss gap: if a saturated F=O(-2)^r has Gauss rank one and F^+/F=O(b), then b=2r or b<=r-1. This is profile-free.

## 3. At delta=12, eliminate every top coefficient except P+D

The universal character identities are

    Sym8 W=P+D,
    Sym16 W=V+P+2D,
    Sym28 W=A+V+2P+3D.                                 (5)

At delta=12, equation (2) has target O(16). The top coefficient 2P+D cannot inject into Sym16 W, so U6,U13 are impossible.

For E0,E10, rank K0=13 and deg K0(2)=-16 with all degrees negative. Hence K0 has all degrees at least-6, whereas (E/F)(-2) has degrees at most-10. Thus J=0. Equation (3) gives rank B=15, deg B=-12, and B/F=O(16). By (4), t=0 or12. The case t=0 violates the gap at r14,b16. Therefore F^+ is a constant fifteen-space C, and

    0 -> F -> C O -> O(28) -> 0,
    C=A+V+P+D.                                        (6)

The map C O/F->Q is generically the positive line. It is a nonzero degree-zero map O(28)->O(28), hence an isomorphism onto the saturated positive summand. Inside C O/F(-2)=O(26), the raw derivative image of F is exactly f12 O(14). Thus all hypotheses of PR804's constant-block obstruction hold. Its unique V28=f12 V16 channel has a nonzero projective derivative at every point of D12, whereas the derivative of F is required to vanish there. This excludes (6) for either source, independently of the lower tail.

For E3,E12 the exact kernels from (2) are

    T O(-3)+D O(-4),
    or (S+T) O(-3)+O(-8).

The only apparent internal degree exception is O(-8)->V O(-6), which vanishes because V does not occur in Sym2 W=A. Hence J=0 and rank B=13, deg B=-8. Equation (4) forces t=0, contrary to the gap at r12,b16.

For E18 the exact kernel is

    K0=S O(-3)+V O(-4)+Wp O(-5).

The only internal channel is Wp O(-5)->Wp O(-5), either zero or scalar isomorphism. In the zero case rank B=11 and deg B=-4, so t=0 and the gap at r10,b16 is impossible. In the nonzero case rank B=13 and deg B=-10, so again t=0. The exact characters and first polar then give

    B=F^+=V O+(S+T) O(-1).

PR799's two-D-channel argument applies directly: after the actual constant V projection, independence of the two D rows forces a full S O(-1) inside the projected F, whose first constant span cannot lie in the pure degree-minus-one quotient. That argument uses the saturated B just proved, not saturation of its external positive projection. Thus E18 is also excluded.

It remains only F=(P+D) O(-2) in E6 or E13. The mismatch E6 for the W O(-9) quotient is impossible because only its O(-10) summand maps there, giving image rank at most one. Hence write

    E=F+T O(-3)+L,
    A_q=O(26)+L,
    L=O(-8)+O(-10) or W O(-9),                          (7)

in the matching first or second label, respectively. The third label has no such source.

## 4. The two raw-span alternatives for delta=12 and rank F=9

The complete degree-sixteen top-kernel possibilities are

    (V+D) O(-4),
    S O(-3)+V O(-4)+O(-8),
    T O(-3)+Wp O(-7).

In the first two, the internal map is zero; the apparent O(-8)->T O(-5) channel vanishes because T does not occur in Sym3 W. If J=0 in any case, rank B=10 and deg B=-2, forcing t=0 and contradicting the gap at r9,b16.

Therefore the last kernel occurs and its unique nonzero Wp O(-7)->T O(-5) channel occurs. This is the standard complete quadratic line map tensored with Wp and is saturated. Thus

    J=Wp O(-7),
    rank B=12, deg B=-12,
    0 -> Wp O(-5) -> B/F -> O(16) -> 0.                (8)

First-polar generation gives

    B=(Wp+S+T) O(-1).

Equation (4) leaves exactly two cases: t=0 or12. Both must be treated.

### 4a. Saturation defect twelve gives a forbidden horizontal residual

If t=12, F^+=C O is an actual constant twelve-space. Its map to E^+/E in (1) has no component in L(2), so its image is O(28-D_epsilon). Since B already has image f12 O(16), epsilon is0 or12.

If epsilon=12, N=E intersect C O would have rank11 and degree-16. This is impossible inside E, since every degree of a subbundle of E is at most-2. Hence epsilon=0, and

    rank N=11, deg N=-28.

The raw intersection E intersect B has quotient Wp O(-5) by F, by (8), and already has rank11 and degree-28. It is contained in N, so the two are equal. Thus N/F=Wp O(-5).

The inclusion N/F->E/F=T O(-3)+L has no components into L. Its unique nonzero component into T O(-3) is the Wp-tensor of the quadratic Euler inclusion, with quotient P O(-2). Consequently

    E/N=P O(-2)+L.                                    (9)

Since C O/N maps isomorphically onto the saturated positive O(28) in Q, the sum E+C O is saturated in H O. Equation (9) is therefore an actual saturated subbundle Z of the constant (H/C) O.

The derivative of Z is induced by the original derivative after killing the positive summand, so it factors through A_q/O(26)=L. It kills the top P O(-2) by degrees. The internal derivative of that top into L(-2) also vanishes by degrees. Thus P O(-2) is horizontal in a constant bundle, which is impossible for a negative nonzero bundle. This excludes t=12.

### 4b. Saturation defect zero gives the genuine quartic subsystem

If t=0, B=F^+ is saturated and pure degree-minus-one. The exact quotient classification from PR797 Sections4-5 uses only (8) and this splitting. It gives

    F^+/F=V O(2),
    C0=V tensor Sym4 W, dim C0=15,
    F=V tensor U_2^4,
    F^+=V tensor U_3^4,
    C0 O/F^+=V O(4).                                  (10)

In particular beta_(F^+) induces the isomorphism

    F^+/F=V O(2) -> (C0 O/F^+)(-2).                    (11)

This is an actual constant subsystem. We next recover its endpoint intersections without presuming that E^+ is an interior stage.

## 5. Recover the quartic intersection with its actual twelve-point modification

Set I0=E intersect F^+. Equation (8) gives

    I0/F=Wp O(-5),    F^+/I0=O(16).                    (12)

The image of the final O(16) in E^+/E is f12 O(16) inside O(28).

Since the derivative of E lands in E^+, beta_(E^+) on F^+ kills I0. Equation (11) then implies that C0 O/(E^+ intersect C0 O) has generic rank at most one.

It cannot have rank zero. If C0 O were contained in E^+, its image in E^+/E would have no L(2) component and would contain f12 O(16). Its positive image is therefore O(28) or f12 O(16). The second alternative gives a rank14 degree-16 kernel inside E and is impossible by the degree bound. The first gives a rank14 degree-28 kernel inside E; every degree must then equal-2. But every map O(-2)^14->E lands in its rank-nine top F, again impossible.

Thus the generic rank is one. The kernel of beta_(E^+) restricted to F^+ has rank11 and contains the saturated I0 of that rank, so the two are equal as sheaves. Writing Nplus=E^+ intersect C0 O, (11)-(12) give

    0 -> F^+ -> Nplus -> Wp O(-3) -> 0,
    C0 O/Nplus=O(18).                                 (13)

All degrees of Nplus are at least-3, by twisting the extension by three and using global generation and H1=0. Therefore its map to the negative L(2) vanishes. Its positive image in E^+/E is O(28-D_epsilon), with epsilon=0 or12. Put N=E intersect C0 O. Then rank N=13.

The constant connection gives N contained in Nplus^-. The derivative of Nplus onto (C0 O/Nplus)(-2)=O(16) is already onto on F^+, by (11)-(12). Thus Nplus^- has rank13 and degree-34.

Both N and Nplus^- are saturated subbundles of C0 O. Their equal-rank inclusion is therefore equality. This proves

    N=Nplus^-,    deg N=-34,
    Nplus/N=O(16),                                    (14)

and forces epsilon=12. In particular the image of Nplus in E^+/E really is f12 O(16), not the entire O(28).

The exact Euler-extension argument of PR797 now applies: (12)-(14) give

    0 -> Wp O(-5) -> N/F -> Wp O(-3) -> 0.

The split extension cannot embed in E/F=T O(-3)+L because Hom_G(Wp,T)=0 and all lower components vanish by degrees. The unique nonzero extension is P O(-4). Its unique inclusion into T O(-3) has quotient Wp O(-1). Hence the actual locally free image sheaf of E in (H/C0) O is

    E/N=M+L,    M=Wp O(-1).                            (15)

We do not assume that all of (15) is saturated.

The image of N under the original quotient E->A_q is exactly f12 O(14): differentiation lands in Nplus, whose image modulo E is f12 O(16), and F already maps onto f12 O(14). This explicit factor is essential in the next step.

## 6. The modified projected backward kernel still has generic Gauss rank two

Let K=E^- and let T12=O(26)/(f12 O(14)), a torsion sheaf of length twelve. The quotient diagram for N contained in E gives a surjection

    E/N=M+L -> A_q/(f12 O(14))=L+T12.

Its component to L is zero on M and an isomorphism on L, by degrees and surjectivity. Consequently the projected image of K in (H/C0) O is

    M'=ker(M -> T12),
    0 -> M' -> M -> T12 -> 0.                          (16)

In particular M' is a proper elementary modification of M and has degree-14. It is not being called saturated.

Nevertheless M itself is an actual saturated tautological bundle in a constant P space. Its nonzero equivariant inclusion in (H/C0) O is represented by the nonzero constant map

    Wp tensor W=P -> H/C0.

Since P is irreducible, this constant map is injective. Thus M has Gauss rank two. Over the function field, M' and M are the same embedded plane. Their generic Gauss ranks are therefore equal, so the projected image of K has generic Gauss rank two as well. Possible torsion in (16) does not change this generic statement.

On the other hand, K intersect C0 O=N^-. Indeed the map N->A_q is its internal Gauss quotient N->O(14) followed by multiplication by f12, and multiplication by a nonzero polynomial does not change a kernel sheaf.

For completeness, the quotient C0 O->O(18) in (13) factors through V O(4) and then an onto degree-fourteen three-section system. Multiplication of a local nonvanishing member of that system by complete quartics generates jets through order four at every point. Thus N is its first jet-kernel and N^- its second jet-kernel. The latter has a nonzero rank-one derivative into

    (N/N^-)(-2)=O(12).

This internal derivative is nonzero modulo K because N intersect K=N^-.

At the generic point, project H/K to (H/C0)/M'. The projected derivative of K has rank two, whereas the nonzero internal derivative from N^- lies in the kernel of that projection. Their images are independent, so

    generic rank beta_K >=2+1=3.

This contradicts maximal backward index one. The proof is generic and does not identify M' with M as a sheaf or require saturation of M'. This excludes t=0, and completes the exclusion of delta=12 for all source types.

## 7. At delta=20 the top block is a complete degree-ten osculation

Equation (2) now injects R into Sym8 W=P+D. Among all source tops in Section1, only R=P+D can occur, and the injection is an isomorphism. The quotient after removing f20 is the complete degree-eight evaluation system

    F=(P+D) O(-2) -> O(6).

Its kernel is

    K0=Sym7 W O(-3)=(Wp+T) O(-3).

All its internal components into (E/F)(-2)=T O(-5)+L(-2) vanish by ordinary degrees. Hence J=0, rank B=10, deg B=-10, and B/F=O(8). Equation (4) forces t=0. First-polar generation then makes F^+=B pure degree-minus-one.

Quadratic values and first two derivatives span the full constant coefficient space C. The derivative of F^+ kills F and factors through O(8), so the full constant span has rank at most eleven. It cannot have rank ten, since F^+ has nonzero degree. Hence rank C=11 and

    C O/F^+=O(10).

The nonzero derivative O(8)->O(8) is an isomorphism. Since F^+ is pure O(-1), its H0 and H1 vanish; global sections of the quotient sequence identify C with all H0(O(10))=Sym10 W. Therefore that sequence is the complete degree-ten evaluation sequence, giving

    C=Sym10 W=A+V+D,
    F^+=U_9^10,
    F=(F^+)^-=U_8^10.

The equality in the last line follows from the derivative isomorphism and equality of the saturated rank-nine kernels. These are actual constant embeddings. The incompatible E6 source for the W O(-9) negative quotient is excluded as in Section3, so only E6 for the first label and E13 for the second can carry this stratum.

This is a required subsystem, not a constant-shear separation theorem and not an exclusion of delta=20.

## Contribution and limits

The twelve-point divisor is eliminated without pretending the raw first polar is saturated. Its possible saturation defect is explicitly separated into cases. In the quartic case, the backward projected kernel is kept as the actual length-twelve modification M'; only its generic Gauss rank is used. At the twenty-point divisor, the exact complete degree-eight top system forces a genuine complete degree-ten constant subsystem.

The basepoint-free strata are not decided here. None of these deductions selects an actual source coefficient or evaluates an actual point, derivative, matrix, or rank. All intersection and projection assertions are stated at their proved sheaf or generic level.
