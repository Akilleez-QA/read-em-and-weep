# Endpoint rank drop excludes the last three (2,2) pairs

## Result and scope

The three necessary quotient pairs in TWO-TWO-ENDPOINT-TOP-SLOPE-LEAVES-THREE-PAIRS.md are all impossible. Therefore the (2,2) maximal rank-three plateau profile is excluded. This proof uses only the dual negative endpoint and, in one branch, one further negative transform. It never assumes rank three at an endpoint and never applies a rank-two degree bound obtained from rank-one curves.

No conclusion about other profiles, a new global SF bound, maximal rank, or the generic section count is made here. There are no actual coefficients, selected points, actual-instance matrices, rank evaluations, scans, or experiments.

## 1. Input and a backward rank-one lemma

Retain the established exact sequences

    0 -> L -> Q* -> B -> 0,
    0 -> N=L^- -> L -> B(-2) -> 0.

Here rank N=7, maxdeg N<=-4, and deg N=-48-2b, where b=deg B. Its derivative factors through B(-4). All these are actual bundle statements, with the second determinant torsion already proved zero in the preceding note.

We need only the backward half of RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md. If a negative saturated bundle F of rank r in a constant bundle has derivative rank one, successive negative kernels give an equivariant flag

    0=F0 < F1 < ... < Fr=F,  rank Fi=i.

Indeed every subsequent derivative factors through the preceding line quotient. Its rank is at most one and cannot be zero: a saturated derivative-invariant subbundle of a trivial bundle is constant, whereas every positive-rank subbundle of F has negative degree and no global sections. All kernels are saturated in the constant ambient bundle. This induction requires no assertion that F spans that whole ambient bundle.

Write di=deg(Fi/F(i-1)). The induced nonzero equivariant line maps give invariant effective divisors of degrees

    delta_i = d_(i+1)-d_i-2 >= 0,  1<=i<r.

Thus

    deg F = r*d_r-r*(r-1)-sum_(i=1)^(r-1) i*delta_i.       (1)

Every nonzero invariant effective divisor on the icosahedral projective line has degree at least 12. Consequently each delta_i is zero or at least 12. This also applies to the divisor of any nonzero equivariant map between line bundles. The binary icosahedral group has no nontrivial one-dimensional representations, so no untracked character changes this assertion.

If beta_F reaches a sum of line bundles of degrees at most c, its last quotient line Fr/F(r-1) has d_r<=c: at least one component of its regular nonzero map is nonzero. If the only reachable target is O(c), the divisor of that map has degree c-d_r and is invariant as well.

## 2. Exhaustive necessary endpoint splittings

Use A3=Sym^2 W, V for the other even three-space, and P4 for the even four-space. The three cases and their necessary dual endpoint splittings are:

1. A=O(-8)+O(2)+O(6), B=O(6)+O(-4)+O(-8), deg N=-36:

       N=V O(-4)+W' O(-5)+W O(-7),                 (2a)

   or

       N=V O(-4)+W' O(-5)+O(-6)+O(-8).           (2b)

2. A=O(-8)+O(4)+O(6), B=O(6)+O(-6)+O(-8), deg N=-32:

       N=V O(-4)+W O(-5)+W' O(-5).                (3)

3. A=O(-8)+W O(5), B=O(6)+W O(-7), deg N=-32:

       N=V O(-4)+W O(-5)+W' O(-5),                (3)

These are necessary splitting overlists, not assertions of realizability or compatible actual maps.

Here is the exhaustive bounded procedure, reproduced in the verifier. Write N=sum Rj O(-j), j>=4, with center parity (-1)^j on Rj. The excess sum (j-4)dim Rj is 8 in case 1 and 4 in cases 2 and 3. Thus every block has j<=12, respectively j<=8. Enumerate all irreducible blocks with j>=6 within that excess. The two exact Euler identities at twists four and five uniquely determine R4 and R5 for each such choice. Keep only genuine representations, correct parity, rank seven and the stated degree.

The Euler character at twist four is V-1-A3 in case 1, and V in cases 2 and 3. Using both twist-four and twist-five Euler identities, case 1 gives exactly (2a),(2b). In cases 2 and 3 the same two-twist procedure gives (3) and one further type

       O(-4)+V O(-4)+W' O(-5)+O(-6).

The strict-top-slope lemma injects H0(N(4)) into H0(B). For cases 2 and 3, H0(B)=Sym^6 W=V+P4 has no trivial constituent, excluding that further type. The same injection leaves both case-1 types. The verifier checks the Euler class for every surviving L candidate in all 354 frozen records; it is identical for a fixed pair. The procedure does not need to enumerate or assert actual extension realizability.

## 3. Both degree-minus-32 endpoints are impossible

For (3), all source summands have degree -4 or -5. Its derivative target B(-4) is respectively

    O(2)+O(-10)+O(-12),  or  O(2)+W O(-11).

Ordinary Hom-degree vanishing kills every component except O(2). Hence its derivative has rank at most one. Rank zero would make N constant, impossible. Its rank is exactly one.

Apply (1) with r=7, deg N=-32 and d7<=2. Then

    0 <= sum i*delta_i = 7*d7-10 <= 4.

Every nonzero delta_i is at least 12, so all vanish. This gives 7*d7=10, impossible for an integral degree. Both pairs are excluded.

## 4. The degree-minus-36 endpoint: rank one is impossible

For (2a) and (2b), the derivative target is

    B(-4)=O(2)+O(-8)+O(-12).

The O(-12) component always vanishes. For (2a), the O(-8) component also vanishes, so the derivative is rank one. For (2b), its rank is at most two.

Any rank-one branch is impossible by (1): r=7, deg N=-36, and the last quotient still has d7<=2. Thus

    0 <= sum i*delta_i = 7*d7-6 <= 8.

All delta_i vanish, forcing 7*d7=6, impossible. Hence only (2b) with derivative rank two could remain.

## 5. The sole rank-two branch has no determinant torsion

Let C=O(2)+O(-8), and put P=N^-. In this branch the derivative is a generically surjective morphism N -> C, with saturated kernel P of rank five. The induced equal-rank injection N/P -> C has torsion cokernel of length t>=0. Its determinant divisor is invariant, so t=0 or t>=12.

Since deg C=-6,

    deg P = -36-(-6-t) = -30+t.

The strict-top-slope lemma for N, whose highest degree is -4, gives maxdeg P<=-5. Thus deg P<=-25, so t<=5. Therefore t=0, and

    0 -> P -> N -> O(2)+O(-8) -> 0                 (4)

is exact. No torsion-free assumption was imposed in deriving this result.

## 6. Its next endpoint is rank one and also impossible

From (4), P has rank five, degree -30, and highest degree at most -5. Its excess above -5 is five. The same bounded character procedure, now at twists five and six, gives exactly two necessary splittings:

    P=(1+P4) O(-6),

or

    P=W' O(-5)+O(-6)+W' O(-7).                    (5)

The exact Euler characters used are chi_G(P(5))=0 and chi_G(P(6))=1+P4. Enumeration allows every j<=10 and every parity-compatible irreducible; none is silently omitted.

Because P is the derivative kernel of N, its derivative factors through

    (N/P)(-2)=O(0)+O(-10).

Both splittings in (5) have all source degrees strictly larger than -10. Thus the O(-10) component vanishes, and only O(0) is reachable. Again rank zero is impossible, so the derivative rank is exactly one.

Apply (1) with r=5, deg P=-30, d5<=0. It gives

    0 <= sum i*delta_i = 5*d5+10 <= 10.

All internal gaps vanish, hence d5=-2. But the last quotient maps nontrivially and equivariantly to O(0), giving an invariant effective divisor of degree 2. This contradicts the minimum invariant divisor degree 12. The last branch is excluded.

## Reproduction

Run python3 verify_two_two_endpoint_rank_drop_exclusion.py. The compact output is two-two-endpoint-rank-drop-summary.json. The input SHA-256 is recorded in that output. It reads the frozen 354-record file and the read-only character-helper definitions; earlier proof, verifier, and record files are not modified. All rank assertions above are geometric consequences of regular Hom-degree vanishing and negativity, not actual-map rank tests.
