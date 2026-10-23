# The cf source of G3.11.ea6bced3bddf is impossible

## 0. Scope and dependencies

The single original source under consideration is tuple (0,0,1,0,0,1,0,1) at source index125 for label G3.11.ea6bced3bddf:

    E=(V+P+D) O(-2)+V O(-4)+O(-8)+O(-10),
    A_q=O(-10)+O(4)+O(16),
    B_q=O(-18)+O(-6)+O(8),

with original determinant defect zero. The original catalogs and fixed conventions are those of the bf proof in PR875 at 01f835fda6e771351555f0af1fa11647c27eb01e, research/hm/profile11-source125-bf-exclusion/PROOF.md. Their immutable source commit is db51525015bb7c5e825833d550d08dedf6f6ea96. Source and stable-label catalog Git blobs are fe0afa410d89340d3082dc814277f89fbb582c19 and 8b5971092f9ef762584912609fd5e9301c4e271d.

We use the actual internal/external derivative-image lemma, first-polar generation of quadratic bundles, strict-top kernel lemma, and representation conventions stated there. We invoke the universal high-D and high-(P+D) kernel classifications from PR875 and PR860 at cdf1d9ae5e477ef5f541d92888059ceedb4fd9b4, not either source exclusion as a new exclusion. Every projection is by a genuine constant subspace. Original defect zero makes the displayed derivative image saturated in Q(-2), where Q=H O/E and H has dimension30.

## 1. Two small actual-connection obstructions

### 1.1 The V-top obstruction

A saturated bundle

    Z=V O(-2)+V O(-4)+O(-8)+O(-10)

cannot have saturated derivative image O(-10)+O(4). Strict-top forces the top V to map nontrivially onto O(4). Its degree6 system has no invariant base divisor; its kernel is Wp O(-5). This follows from the exact degree6 V covariant: the kernel has rank2, degree-10, twist2 H1 equal to P, and hence is Wp O(-5). Its internal Hom to V O(-6)+O(-10)+O(-12) is zero. Thus the first span of V O(-2) is a genuine constant P, with quotient O(6). Its exact intersection with Z is the V top, because that quotient is saturated. Constant projection leaves V O(-4)+O(-8)+O(-10) with derivative image O(-10). Its highest degree is -4, which cannot map to O(-10), contradicting strict-top.

The same last contradiction applies whenever those three tails remain after a genuine constant projection.

### 1.2 The complete quadratic Sym6 obstruction

A saturated bundle

    Z=(V+P) O(-2)+V O(-4)+O(-10)

cannot have saturated derivative image O(-10)+O(4).

The top F=(V+P) O(-2) maps onto O(4) by the complete degree6 system: strict-top makes its map on top coefficient space injective, and Sym6 W=V+P. Its kernel is T O(-3), with zero internal Hom to V O(-6)+O(-12). Hence its first span is M=(Wp+T) O(-1), and M/F is the saturated low line O(6). Its second span is a genuine constant C of dimension9: the quadratic rank7 block has first increment1; M is not constant; and all its quadratic coefficients occur after the second derivative. In particular C/M is a line. Also Z intersect M=F exactly.

Put L=V O(-4), the complementary source tail. Its external derivative is zero: the negative target is too low, and V is absent from Sym8 W=P+D. Its internal derivative modulo L can land only in the top V O(-2). Therefore, after projection by the actual constant C, the coherent image of L in (H/C) O is preserved by the constant connection.

A coherent subsheaf of a constant bundle preserved by its regular connection is itself a constant subbundle. Indeed its saturation is horizontal, and at each local discrete valuation ring any nonzero elementary-divisor exponent would decrease upon differentiation, contradicting preservation of the lattice; the resulting subbundle has zero Gauss map and is constant. This argument uses characteristic zero.

If that projected image has rank1 or2, its even G-representation is a sum of trivial representations, since the only nontrivial even irreducibles of dimension at most3 are A and V, both dimension3. But Hom_G(V O(-4),O)=0 because V is absent from Sym4 W=D. If the image has rank3, the surjection from L onto that constant rank3 image is an isomorphism, impossible since deg L=-12. Thus the projected image is zero, and L lies in C.

This is impossible because the disjoint summands F and L would have total rank10 inside the rank9 constant space C. This proves the obstruction.

## 2. The lower P derivative row is nonzero

Suppose P O(-2) had zero component to O(4). Then F=(P+D) O(-2) maps only to O(16). Strict-top injects its nine-dimensional coefficient space into Sym18 W, so its degree18 system has no invariant base divisor: after any nonempty divisor at least12, no more than seven sections remain.

The complete high-(P+D) kernel list is

    K1=(V+P) O(-4)+O(-6),
    K2=Wp O(-3)+V O(-4)+Wp O(-5)+O(-6),
    K3=T O(-3)+O(-6)+O(-10).

The internal target is V O(-4)+V O(-6)+O(-10)+O(-12). For K1 and K2 the only possible internal map is the scalar V O(-4) to V O(-4). For K3 only O(-10) contributes, through V O(-4) and the scalar O(-10). The nonzero V component is a degree6 covariant with no invariant base divisor; thus it is a saturated line. A scalar component is also saturated. Therefore the exhaustive internal-image possibilities are

    J=0, V O(-4), or O(-10).

If J=0, F has genuine constant first span A+V+P, with exact intersection F and saturated high quotient O(18). Constant projection gives the bundle in1.1 with derivative image O(-10)+O(4), impossible.

If J=O(-10), the first span is A O+(Wp+T) O(-1). The linear-channel obstruction from PR875 Section2 applies without change: after projecting the genuine constant A, the D and P images cover either a whole Wp or T linear summand, or the whole linear bundle. The actual derivative condition then forces a nonzero constant span inside that purely linear bundle, impossible. That argument uses only F and its actual first span, not the complementary source blocks.

It remains to consider J=V O(-4). This occurs only with K1 or K2. Let G0=(V+P+D) O(-2) be the full quadratic top. First suppose its V row to O(4) vanishes too. Then its high external kernel is an extension of V O(-2) by K1 or K2. Both ends have zero Hom to the remaining internal target V O(-6)+O(-10)+O(-12), so G0 has saturated first increment O(18). The quadratic rank12 gap permits only increment degree24 or at most11, not18. Thus the V row is nonzero. Its degree6 system is basepoint-free, with kernel Wp O(-5); together with the onto high row on F, it makes the external image of G0 the whole saturated positive pair O(4)+O(16).

The external kernel of G0 is an extension of Wp O(-5) by K1 or K2. Its internal target, after removing the entire top, is V O(-6)+O(-10)+O(-12). Both K1 and K2, and Wp O(-5), have zero Hom to this target. The kernel extension therefore has zero Hom as well. Thus G0 has zero internal derivative image and saturated external image O(4)+O(16). Its first span has rank14 and degree

    -24+6+18=0.

As a saturated degree-zero subbundle of a constant bundle it is genuinely constant. It meets E exactly in G0 and captures the positive pair. Constant projection leaves V O(-4)+O(-8)+O(-10) with only derivative target O(-10), impossible by strict-top. This exhausts the lower-P-zero assumption.

In particular the canonical Euler Wp O(-3) inside the source P O(-2) has nonzero, onto derivative component to O(4). Otherwise the P map would factor through Wp O(-1), whose Hom to O(4) is zero. Its restricted degree7 system has no invariant base divisor.

## 3. Complete high-D first spans

For F=D O(-2), the high O(16) row is nonzero and basepoint-free, and its kernel is

    K0=Wp O(-5)+O(-6)+O(-10),

as in PR875 Section3. Its internal target in the present source is

    (V+P) O(-4)+V O(-6)+O(-10)+O(-12).

Wp O(-5) maps only to P O(-4), by the tautological Euler inclusion. O(-6) has no channel. O(-10) maps only to V O(-4), P O(-4), or O(-10). Every nonzero line image is saturated: both V and P degree6 covariants have no base divisor, as does a nonzero scalar component. If the Wp image also occurs, quotient by it. The projected P component goes to Wp O(-3) by a nonzero degree7 covariant: it cannot vanish because Hom_G(O(-10),Wp O(-5))=0. The V and scalar components remain saturated as before. Thus the combined image is saturated too.

The exhaustive internal-image list is consequently

    0, Wp O(-5), O(-10), Wp O(-5)+O(-10).

The first-span degrees are8,2,0,-6; the first two are impossible in a constant bundle. First-polar generation and the exact Euler characters give the two surviving actual first spans

    M=(A+P) O,
    M=A O+T O(-1).

## 4. The constant first span is impossible

Suppose M=(A+P) O. Its exact intersection with E is N=D O(-2)+O(-8), and M/N is the saturated high O(18). Constant projection embeds E'=E/N with derivative image O(-10)+O(4). After removing D, the O(-8) in N has possible components only into

    (V+P) O(-2)+O(-8).

There is no component into V O(-4), because V is absent from Sym4 W, nor into O(-10) by degree.

If its scalar O(-8) component is nonzero, then E'=(V+P) O(-2)+V O(-4)+O(-10), excluded by1.2.

Suppose the scalar component is zero and both V and P components are nonzero. The quotient

    R=((V+P) O(-2))/O(-8)

is locally free. At twist0 the map H1(O(-8))=V+P -> H1((V+P) O(-2))=V+P is an isomorphism: the two inequivalent components are the duals of the nonzero degree6 covariants. Thus H0(R)=H1(R)=0. Rank R=6 and degree R=-6 force R=T O(-1), with coefficient T obtained from the twist1 Euler character. Then E'=T O(-1)+V O(-4)+O(-8)+O(-10). Its top T maps onto O(4) by the complete degree5 system, with kernel D O(-2) and zero internal Hom. Hence its first span is a genuine constant V+P, capturing O(6). Constant projection gives the tails in1.1 with only negative derivative target, impossible.

If the scalar and P components vanish, the nonzero V degree6 line is basepoint-free. The quotient V O(-2)/O(-8) has rank2 and degree2 and is a direct summand of E'. Its positive total degree contradicts embedding in a constant bundle.

Finally, if the scalar and V components vanish, the P component is nonzero. The universal dual degree6 P sequence gives P O(-2)/O(-8)=V O. Project this actual constant V out of E'. The remainder is exactly the bundle in1.1, impossible. All cases are exhausted.

## 5. The linear first span is impossible

Suppose M=A O+T O(-1). As in PR875 Section5, projecting the actual constant A shows that D O(-2) maps by the tautological inclusion into T O(-1), with first span T O(-1) and second constant span V+P. Hence M lies in the genuine constant space

    C=(A+V+P) O,   C/M=O(6).

Its exact intersection with E is

    N=E intersect M=D O(-2)+Wp O(-3)+O(-8),
    M/N=O(18).

The Wp block is the canonical Euler subbundle of the source P: its only possible internal image is that P component, and no lift to D exists because Wp is absent from D W. By Section2 its derivative has a nonzero onto O(4) component; its negative component is zero by ordinary degree. Its sections and derivatives lie in C. Consequently C/N maps generically isomorphically to the saturated positive pair O(18)+O(6) in Q. Its rank2 and degree24 equal those of that pair, so the determinant is a nonzero degree-zero section and the map is an isomorphism. Thus E intersect C=N exactly, and

    R=E/N subset (H/C) O

is saturated, rank9, degree-30, with derivative image only O(-10).

After removing D and the canonical Euler Wp, its presentation is

    0 -> O(-8) -> V O(-2)+Wp O(-1)+V O(-4)+O(-8)+O(-10) -> R ->0.

The line has possible components only in V O(-2), Wp O(-1), and scalar O(-8). If its scalar component is nonzero, the quotient has no global sections. Strict-top then forces all its ordinary splitting degrees to be at most -10, giving degree at most -90, contrary to -30.

If the scalar component vanishes but the V component is nonzero, form

    R0=(V O(-2)+Wp O(-1))/O(-8).

It is locally free because the V component is a degree6 basepoint-free covariant, has rank4 and degree0, and is a direct summand of R. Since R is a subbundle of a constant bundle, R0 is a genuine constant four-space. Project it out. The remainder V O(-4)+O(-8)+O(-10) retains only derivative target O(-10), again impossible by strict-top.

If both scalar and V components vanish, the line maps only to Wp O(-1). Its degree7 covariant is basepoint-free, and its quotient is the positive line O(6), a direct summand of R. This contradicts embedding in a constant bundle. The linear-first-span case is exhausted, proving the whole-source cf exclusion.

## Boundary

The companion verify.py checks 105 fixed internal Hom spaces, the polar and trapped-tail character identities, numerical contradictions, and this exact original source identity against immutable catalog Git blobs. REPRODUCE.md gives the download instructions. These checks do not replace the connection-preserved coherent-image lemma, saturation, exact-intersection, or branch-exhaustion arguments.

This excludes only the stated original cf tuple, not the entire label and not a current frontier count. It uses universal representations, actual saturated derivative images, and genuine constant projections. There are no selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance rank tests, experiments, scans, or large computation. This is a written proof, not Lean certification.
