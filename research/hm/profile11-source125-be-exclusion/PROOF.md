# The be source of G3.11.ea6bced3bddf is impossible

## 0. Scope and fixed dependencies

The single original source is tuple (0,1,0,0,1,0,0,1), source index125, label G3.11.ea6bced3bddf:

    E=2P O(-2)+T O(-3)+Wp O(-5)+O(-10),
    A_q=O(-10)+O(4)+O(16),
    B_q=O(-18)+O(-6)+O(8),

with original determinant defect zero. The source catalog commit is db51525015bb7c5e825833d550d08dedf6f6ea96. The two catalog paths under research/hm/order-four-quadratic-load are one-one-endpoint-necessary-pairs.json and rank-three-quotient-frontier-144.json, with Git blobs fe0afa410d89340d3082dc814277f89fbb582c19 and 8b5971092f9ef762584912609fd5e9301c4e271d.

Conventions and actual-bundle lemmas are as in the cf proof, PR882 at ef8ed8d457494608472a2c07de776e9162b2c20f, research/hm/profile11-source125-cf-exclusion/PROOF.md. In particular G is binary icosahedral, W its defining two-space, Wp the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P the other even irreducibles. All are self-dual. Every nonempty invariant effective divisor has degree at least12. The rank17 degree-54 source is saturated in a constant thirty-space, H0(E(1))=0, and strict-top says H0(E^-(2))=0. Original defect zero makes A_q saturated in Q(-2), Q=H O/E.

We use the actual internal/external image lemma and quadratic first-polar generation recorded in that proof and PR875, commit01f835fda6e771351555f0af1fa11647c27eb01e. A quadratic first span has only degrees0 and-1. For a quadratic rank-r block with saturated rank-one first increment O(b), the constant second span gives b=2r or b<=r-1. All constant projections below use actual ambient constant subspaces.

The two-P high-system kernels are the universal result in PR846, commit1644b5221fe6f8c23f30401fd6f2dc64230c0f5f, restated below. No other source exclusion is assumed to exclude be.

## 1. The lower P row is nonzero

Let G0=2P O(-2) be the full top. If its O(4) derivative row vanished, its high degree18 system would be onto: strict-top gives eight independent sections, whereas a nonempty invariant divisor would leave at most seven. The complete kernel list is

    Wp O(-3)+V O(-4)+W O(-7),
    Wp O(-3)+V O(-4)+O(-6)+O(-8).

The internal target is T O(-5)+Wp O(-7)+O(-12). Every Hom from either kernel to this target is zero. Thus the saturated first increment is O(18), and the first span has degree -16+18=2, impossible in a constant bundle.

Consequently the lower P row is nonzero. Its kernel on the two-dimensional P multiplicity space determines a genuine saturated top copy

    F=P O(-2)

which maps only to the high O(16). The other P direction maps onto O(4), by its degree6 basepoint-free covariant.

The high row on F is nonzero by strict-top. It cannot have an invariant base divisor. The only possible divisor degree is12, leaving a degree6 P system with raw image O(4) and kernel V O(-4). This kernel has zero internal Hom to

    P O(-4)+T O(-5)+Wp O(-7)+O(-12).

Hence the whole raw derivative has rank one and abstract image O(4). Write its saturation as O(4+delta), with delta an invariant divisor degree. Its saturated first increment has degree b=6+delta. The rank4 quadratic gap forces b=8, because b>=6>3, and hence delta=2. This contradicts invariance. Thus F maps onto O(16) everywhere.

The full top G0 therefore maps onto the saturated positive pair O(4)+O(16).

## 2. The complete high-P kernel list

For any onto high system P O(-2)->O(16), let K be its kernel. Then

    rank K=3, degree K=-24,
    H0(K(2))=0,
    H1(K(2))=A+V+P+D,
    chi_G(K(3))=-W-S-T.

The complete necessary list is

    K_A=A O(-8),
    K_W=W O(-7)+O(-10),
    K_U=Wp O(-3)+O(-18).                         (1)

Here is a bounded completeness proof. Every summand R O(-j) has j>=3 and central parity (-1)^j. A rank-three irreducible must have degree-8; A and V both meet the first cohomology budget, but A Sym3=W+S+T while V Sym3=Wp+S+T, so only A survives. A rank-two odd irreducible plus a line has degree pairs (j,k)=(3,18),(5,14),(7,10),(9,6), with total2j+k=24. The cohomology budget leaves W(-3)+O(-18), Wp(-3)+O(-18), Wp(-5)+O(-14), W(-7)+O(-10), W(-9)+O(-6). The first and third have the wrong twist3 character, leaving the other three. For three lines, no O(-4) is allowed by the trivial constituent in H1; the only possible sorted degree triples are (6,6,12),(6,8,10),(8,8,8), and only (6,8,10) meets the budget. Finally O(-6) cannot inject into P O(-2), since P is absent from Sym4 W. This removes W(-9)+O(-6) and the remaining three-line case, proving (1).

## 3. The full positive kernel splits and forces a constant V

Let Kfull be the external kernel of G0->O(4)+O(16). There is an exact sequence

    0 -> K -> Kfull -> V O(-4) ->0,             (2)

because the high row on F is onto and the low row on the complementary P has kernel V O(-4). Every equivariant extension in (2) splits. Explicitly the relevant Ext1 groups vanish by

    A V=P+D,   V W=T,   T W=D+V+P,
    V absent from Sym4 W and Sym12 W,

and the ordinary positive-degree vanishing for the Wp O(-3) term. For example Ext1(V(-4),A(-8)) is the invariant part of A V Sym2 W, and Ext1(V(-4),O(-18)) is the V multiplicity in Sym12 W=1+A+P+D.

The internal target for the full top is

    T O(-5)+Wp O(-7)+O(-12).

In K_A+V(-4), only A O(-8) maps, and only to T O(-5). In K_W+V(-4), only O(-10) maps, again only to T O(-5). In K_U+V(-4), only O(-18) maps, again only to T O(-5). Each Hom is one-dimensional. Every nonzero image is saturated: A(-8)->T(-5) is classical multiplication of a quadratic by the tautological cubic; O(-10)->T(-5) is the tautological degree5 line; the degree13 T covariant from O(-18) has no base divisor, since removing degree12 would require T in Sym1 W.

If the internal image is zero, the full first span has degree -16+6+18=8, impossible. Thus the indicated channel is nonzero in each surviving case.

The K_W case is impossible already on the high-only F. Its internal image in P O(-4)+T O(-5)+Wp O(-7)+O(-12) is a saturated O(-10), with the T component nonzero. Its first span has degree -8+18-8=2, impossible.

In the two other cases, first-polar generation and Euler characters give exactly

    K_A: M=G0^+=V O+(2Wp+T) O(-1),
    K_U: M=G0^+=V O+(Wp+T) O(-1).              (3)

For clarity, the raw external positive contribution to chi_G(M) is

    Sym6+Sym18-2P=A+2V+P+D.

Subtracting A Sym4=A+V+P+D in the first case, or Sym14=A+V+P+D in the second, leaves V. The respective ranks and degrees are (13,-10) and (11,-8); their twist1 characters give the displayed linear coefficients.

The high-only first span has no constant summand:

    K_A: F^+=(Wp+T) O(-1),
    K_U: F^+=T O(-1).                           (4)

Indeed its internal image is the same A(-8) or O(-18), possibly with an extra component into the other P(-4). The nonzero T component already makes that graph image saturated. Rank, degree, and Euler characters give (4); no saturation assertion about an isolated A-to-P map is required.

## 4. The constant V captures the lower positive line

Write M=V O+L with L=(k Wp+T) O(-1), k=1 or2. Project the full top G0=2P O(-2) to L. Its components to k Wp and T are determined by constant multiplicity maps

    alpha:C^2 -> C^k,   b:C^2 -> C.

The universal identities

    P=Wp tensor W,    T=Wp tensor Sym2 W

identify the unique P(-2)->Wp(-1) channel with the Euler quotient, and the unique P(-2)->T(-1) channel with multiplication by the tautological line. The latter is injective, with quotient Wp O(1).

The functional b is nonzero. Otherwise the projected rank is at most2k<=4, so a kernel of rank at least4 would inject into the constant V of rank3. Also alpha is nonzero on ker b; otherwise the whole P(-2) in that direction would inject into V. It follows that the kernel of the full projection is exactly the canonical Euler block

    G0 intersect V O=Wp O(-3)                  (5)

in the P direction ker b. This block is saturated in V O because G0 is saturated in the ambient constant bundle. Its quotient is O(6).

The direction ker b is not the high-only direction F. To see this, project F^+ in (4) to L. Its T component cannot vanish, since then a rank6 T(-1) would map only into rank3 V O. If a Wp(-1) component is present, it cannot vanish under projection either, since Hom_G(Wp(-1),V O)=0. The projection is therefore injective on both inequivalent linear blocks. In particular F projects with rank4. If b vanished on the direction F, that projection would be only an Euler quotient of rank2, a contradiction.

Thus the source P direction in (5) has nonzero lower O(4) row. Its restriction to Wp O(-3) is nonzero and onto: otherwise it would factor through Wp O(-1), whose Hom to O(4) vanishes because Wp is absent from Sym5 W. The degree7 restricted system has no invariant base divisor.

Since V is an actual constant space, derivatives of the block in (5) stay in V. The image of V in Q factors through the saturated positive pair: V lies in M, whose image in Q is exactly that pair twisted by2. The kernel E intersect V is exactly the Wp(-3) in (5). It cannot have larger generic rank, as that would put all of V into saturated E, contradicting H0(E)=0. Therefore V/Wp(-3)=O(6), and its map to the lower O(6) factor is a nonzero scalar, hence an isomorphism. Its image in the positive pair is a saturated graph line.

Constant projection by V consequently embeds the saturated bundle

    E'=Wp O(-1)+P O(-2)+T O(-3)+Wp O(-5)+O(-10)

with saturated derivative image O(-10)+O(16). This projection has removed the lower positive graph, not assumed an arbitrary splitting horizontal.

## 5. A second constant projection removes the high line

The highest Wp O(-1) block of E' maps nontrivially onto O(16) by strict-top. Its degree17 covariant is basepoint-free: any divisor would have degree12, leaving Wp in Sym5 W, which is impossible. Its kernel is O(-18).

The internal target is P O(-4)+T O(-5)+Wp O(-7)+O(-12). The only channels from O(-18) are to P O(-4) and T O(-5). Any nonzero component is basepoint-free: degrees14 and13 could lose only a divisor12, leaving respectively a nonexistent P in Sym2 or T in Sym1. If the internal image were zero, the first span would have positive degree16. Thus the internal image is a saturated O(-18).

The resulting first span has rank4 and degree0 and is the genuine constant P. Its exact intersection with E' is

    N'=Wp O(-1)+O(-16),

and its quotient is the saturated high O(18). Constant projection gives

    E''=R0+Wp O(-5)+O(-10),
    R0=(P O(-2)+T O(-3))/O(-16),              (6)

with only derivative target O(-10). Here the O(-16) can map only into P(-2) and T(-3); the other two possibilities vanish because Wp is absent from Sym11 and the trivial representation is absent from Sym6. Since N' is an actual saturated intersection, the quotient in (6) is locally free. In particular R0 is an actual subbundle of a constant bundle, of rank9 and degree-10. The full E'' has rank12 and degree-30.

## 6. Constants cannot rescue the negative-only residual

Because R0 embeds in a constant bundle and has negative degree, h0(R0)<=8: equality to rank9 would make it a trivial rank9 bundle of degree0. The other two summands in (6) have no global sections. Remove the actual constant space H0(E'') from the ambient bundle. The residual R has

    H0(R)=0,   rank R>=4,   degree R=-30,

and still has only derivative target O(-10). All its splitting degrees are negative. Strict-top forces its largest degree to be at most -10; otherwise the entire highest block has zero map to the sole derivative target. Hence

    degree R<=-10 rank R<=-40,

contradicting degree R=-30. This proves the be source exclusion.

## Boundary

The companion verify.py checks 80 fixed Hom spaces, the bounded rank-three high-P kernel alternatives, the Ext and polar/Euler identities, numerical contradictions, and the exact original source identity against pinned catalog Git blobs. REPRODUCE.md supplies the input download instructions. These arithmetic checks do not replace saturation, actual-connection, exact-intersection, or branch-exhaustion arguments.

This is a single original-source exclusion, not a whole-label exclusion or a current frontier count. All arguments concern universal representations, actual bundle images and saturation, and genuine constant projections. No selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance rank tests, experiments, scans, or large computation are used. This is written mathematics, not Lean certification.
