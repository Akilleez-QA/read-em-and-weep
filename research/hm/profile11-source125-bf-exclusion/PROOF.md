# The bf source of G3.11.ea6bced3bddf is impossible

## Scope and fixed inputs

This proof excludes exactly source125 tuple (0,1,0,0,0,1,0,1) for G3.11.ea6bced3bddf:

    E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10),
    A_q=O(-10)+O(4)+O(16),
    B_q=O(-18)+O(-6)+O(8),

with original determinant defect zero. The original source and stable-label catalogs are at db51525015bb7c5e825833d550d08dedf6f6ea96, under research/hm/order-four-quadratic-load; their Git blobs are respectively fe0afa410d89340d3082dc814277f89fbb582c19 and 8b5971092f9ef762584912609fd5e9301c4e271d. The actual splitting and strict-top lemmas are the ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md and NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md files at that commit.

We use the actual internal/external derivative-image lemma and quadratic first-polar generation, as in PR796 at d2b43060c83328dd5118aee6b9288fcfa0c873ac, research/hm/profile12-quadratic-block-exclusion/PROOF.md, and PR802 at e484640a6565c278321bf6557860262c1ac1b7df, research/hm/profile11-o16-constant-span-exclusion/PROOF.md. The three high-(P+D) kernels and linear-channel obstruction used below are proved in the ef proof, PR860 at cdf1d9ae5e477ef5f541d92888059ceedb4fd9b4; they are restated where needed. No ef exclusion is assumed as an exclusion of bf.

Conventions: G is binary icosahedral over C; W is the defining two-space, Wp the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W; V and P are the other even irreducibles, of dimensions3 and4. All irreducibles are self-dual. Nonempty invariant effective divisors have degree at least12. E is a saturated subbundle of the constant thirty-space; rank E=17, deg E=-54, and its top ordinary degree is -2. Original defect zero makes the image A_q saturated in Q(-2), where Q=H O/E. Saturated forward transforms are denoted by a plus sign. Every projection below is by a genuine constant subspace, not an equivariant splitting presumed horizontal.

## 1. Two reusable small obstructions

### 1.1 The cubic T obstruction

There cannot be a saturated bundle

    Z=T O(-3)+O(-8)+O(-10)

in a constant bundle whose derivative has saturated image O(-10)+O(4).

Indeed strict-top injects its top T into Sym7 W=Wp+T, and the negative target vanishes by degree. The resulting T O(-3)->O(4) is onto: a degree7 line system has no invariant base divisor. Its kernel is

    V O(-4)+Wp O(-5).

For completeness, the twist3 H1 budget is Wp and the twist4 Euler character is V. The only atom of degree at most -5 fitting the former is Wp O(-5); all other terms have degree -4 and their coefficient is V. Its internal Hom to O(-10)+O(-12) is zero by degree. Thus the cubic F=T O(-3), of rank6 and degree-18, has saturated first increment O(6).

Successive nonzero Gauss increments have rank at most1, because differentiation of each forward span kills the preceding span. Cubic coefficients span after at most three derivatives. If the constant span is reached after one increment, degree forces the increment to have degree18, not6. If reached after two, the next increment has degree12; its derivative from O(6) would be an equivariant map O(6)->O(10), which is zero because Sym4 W=D contains no invariant. If reached after three, the two subsequent increment degrees are at least8 and10, since each preceding line maps nontrivially to the next twisted by -2. Their total, including the first6, is at least24, but total degree18 is necessary to reach a constant bundle. All alternatives are impossible.

### 1.2 A top P with only O(4) available

If a saturated embedded bundle has top block P O(-2), derivative image O(-10)+O(4), and all complementary degrees at most -3, with no internal Hom from V O(-4), it is impossible. Strict-top and the divisor bound make P O(-2)->O(4) onto. Its kernel is V O(-4), from Sym6 W=V+P and P W=Sym7 W=Wp+T. The zero internal image gives saturated first increment O(6). The rank4 quadratic gap requires its degree to be8 or at most3, contradiction.

The quadratic gap follows by taking the constant second span: its rank is r+1 or r+2 for first increment rank1. The former gives b=2r; the latter gives a nonzero map O(b)->O(2r-b-2), hence b<=r-1. This does not require an interior Gauss profile.

## 2. The lower P row is nonzero

Suppose the O(4) derivative component on P O(-2) were zero. Then F=(P+D) O(-2) maps only to saturated O(16); D has no lower component since Sym6 W=V+P. Strict-top injects nine independent sections into O(18), so no invariant base divisor is possible: removing degree12 would leave at most seven sections.

The exact possible high-system kernels are

    (V+P) O(-4)+O(-6),
    Wp O(-3)+V O(-4)+Wp O(-5)+O(-6),
    T O(-3)+O(-6)+O(-10).

This complete list follows from H1(K(2))=A+V+P and chi_G(K(3))=-W, as proved in PR860. Here the internal target is T O(-5)+O(-10)+O(-12). The first two kernels have zero internal Hom. In the third only O(-10) can contribute, through its unique T O(-5) channel and its scalar O(-10) channel. A nonzero such image is saturated: the T component is the tautological degree5 line, or the scalar component is nonzero. Thus J is0 or O(-10), with no hidden divisor.

For J=0, the first span is constant C=A+V+P, of dimension10, and C/F is the saturated high O(18) inside Q. Hence E intersect C=F exactly. Constant projection gives T O(-3)+O(-8)+O(-10) with derivative image O(-10)+O(4), contradicting 1.1.

For J=O(-10), first polars and Euler characters give F^+=A O+(Wp+T) O(-1). Projecting by the actual constant A gives L0=(Wp+T) O(-1). D must map nontrivially to its T summand, since rank5 cannot embed in constant A. P must project nontrivially too, since rank4 cannot embed in A.

The nonzero D-to-T channel is the tautological inclusion with quotient O(4). A nonzero P-to-T component covers this quotient, since otherwise it factors through D O(-2), and Hom_G(P,D)=0; its degree6 line system is onto. If the P-to-Wp component vanishes, F therefore covers all T. If its P-to-T component vanishes, P covers all Wp by the tensor-Wp Euler surjection. If both are nonzero, take the Euler kernel Wp O(-3) in P O(-2). Its map to O(4) is nonzero, since Hom_G(Wp O(-1),O(4))=0, and its degree7 line system is onto. Thus F covers all L0. Every case puts a complete nonzero direct linear summand in the image of F. Local lifts and the actual derivative condition force that summand's first span, a nonzero constant space, into L0, contradicting H0(L0)=0.

The lower P row is therefore nonzero for any prospective bf source. In particular its restriction to the canonical Euler subbundle Wp O(-3) inside P O(-2) is nonzero and onto O(4): otherwise the nonzero P-to-O(4) map factors through Wp O(-1), whose Hom to O(4) is zero. The restriction is a degree7 line system, so it has no base divisor.

## 3. Unique high-D kernel and complete first spans

Let F=D O(-2). It maps only to O(16), and strictly-top it is nonzero. Its high degree18 line system is basepoint-free. The only possible nonempty invariant divisor of degree at most18 has degree12, but this would leave D in Sym6 W=V+P, impossible.

The high-system kernel is uniquely

    K0=Wp O(-5)+O(-6)+O(-10).                    (1)

Here H1(K0(2))=A+V+2P and chi_G(K0(3))=-W-Wp-T, and rank K0=4, degree-26. A direct complete rank4 check gives (1). The only scalar atoms compatible with the H1 budget are O(-6) and O(-10). A rank3 even atom plus a scalar has ordinary degrees (4,14) or (6,8); their H1 characters contain forbidden D or1. A single rank4 atom cannot have total degree-26. Two odd rank2 atoms have total degree divisible by4, also impossible. Four scalar atoms violate the single-A or single-V budget. The remaining form is an odd rank2 atom plus two scalars. Two O(-6) terms exceed A, and two O(-10) terms exceed V; O(-6)+O(-10) forces rank2 degree-5 and its remaining H1 character P forces Wp. These cases also exclude degree-minus-three atoms: with that rank2 degree the two scalar terms would both be O(-10). This exhausts all forms.

The internal target is

    (E/F)(-2)=P O(-4)+T O(-5)+O(-10)+O(-12).

Wp O(-5) has precisely one possible channel, the tautological inclusion into P O(-4)=(Wp W) O(-4). O(-6) has none. O(-10) can map to P O(-4), T O(-5), and O(-10), each by a one-dimensional Hom; it has no O(-12) component.

Every nonzero O(-10) image is a saturated line. Its P component is a degree6 basepoint-free covariant; its T component is the tautological degree5 line; or its scalar component is nonzero. If the Wp image is also present, project by it. The P quotient is Wp O(-3); a nonzero P component induces a nonzero degree7 Wp covariant in that quotient, since Hom_G(O(-10),Wp O(-5))=0. It has no base divisor. The other two components remain as before. Thus the combined image is saturated too, and the complete list is

    J=0, Wp O(-5), O(-10), Wp O(-5)+O(-10).       (2)

The internal/external image lemma applies to these actual saturated images and to the saturated high line. The first-span degrees for the four cases are8,2,0,-6, respectively. The first two contradict embedding in a constant bundle. For the latter two, first-polar generation and Euler characters give precisely

    J=O(-10):                M=F^+=(A+P) O,
    J=Wp O(-5)+O(-10):       M=F^+=A O+T O(-1).   (3)

For instance chi_G(M)=A+V+2P plus chi_G(J(2)); in the second case the two subtractions are P and V+P, leaving A. The twist1 character then leaves linear coefficient T. All scalar-zero alternatives and saturation branches in this interface are covered by (2).

## 4. The constant first span A+P is impossible

Assume the first case in (3), with C=(A+P) O. The actual intersection N=E intersect C is the kernel of C->Q, and the high quotient is exactly O(18). Thus

    N= D O(-2)+O(-8),
    C/N=O(18).

The abstract splitting of N follows from the exact internal image; its extension splits by H1(O(6))=0. Constant projection embeds E'=E/N in (H/C) O with derivative image O(-10)+O(4). The O(-8) summand of N, after quotienting by D, has possible components only in

    P O(-2)+T O(-3)+O(-8);

it has no O(-10) component by degree. There are three exhaustive cases.

If its scalar O(-8) component is nonzero, the quotient is

    E'=P O(-2)+T O(-3)+O(-10).

The P kernel V O(-4) has no internal map to T O(-5)+O(-12). Obstruction1.2 applies.

If the scalar component is zero and its T component is nonzero, set

    R=(P O(-2)+T O(-3))/O(-8).

At twist1, the map H1(O(-7))=T -> H1(T O(-2))=T is an isomorphism: by Serre duality it is the tautological degree5 T system. Hence H0(R(1))=H1(R(1))=0. Rank R=9 and degree R=-18 force all splitting degrees to be -2. Its twist2 Euler character is P+D, so

    E'=(P+D) O(-2)+O(-8)+O(-10).

Its D top block has zero map to both O(-10) and O(4), contradicting strict-top.

Finally suppose both the scalar and T components are zero. The P component is nonzero, and the unique degree6 P line has quotient V O. Explicitly the exact P degree6 system has kernel V O(-4); dualizing and twisting by -4 gives

    0 -> O(-8) -> P O(-2) -> V O ->0.

Thus E'=V O+T O(-3)+O(-8)+O(-10). The V is an actual constant space. Quotienting it leaves the bundle in1.1 with the same derivative image O(-10)+O(4), impossible. This exhausts the constant-first-span case.

## 5. The linear first span captures both positive quotient lines

Assume the second case of (3), M=A O+T O(-1). Project by the actual constant A. The projected D O(-2) is nonzero, because rank5 cannot embed in A. Its only channel is the tautological inclusion D O(-2)->T O(-1), which is saturated with quotient O(4). Its first span is exactly T O(-1): its derivative is nonzero and lands in that line quotient.

Since D O(-2) is quadratic, its second span is a constant space of dimension7. Indeed its first increment is1, so the next increment has rank at most1; T O(-1) itself is not constant. The coefficient representation of this constant space is V+P, from the quotient O(6) and Sym6 W=V+P. Lifting back through the constant A gives a genuine constant space

    C=(A+V+P) O,
    M subset C,
    C/M=O(6).                                    (4)

The exact first-span intersection is

    N=E intersect M=D O(-2)+Wp O(-3)+O(-8),
    M/N=O(18).                                   (5)

All extensions split by the ordinary degrees. The Wp O(-3) in (5) is precisely the canonical Euler subbundle of the source P O(-2): its internal image has only that P component, and its possible lift to D O(-2) vanishes because Wp is absent from D W=S+T.

By Section2, this Wp block has an onto O(4) component under the actual derivative. Its negative O(-10) component is zero by ordinary degree. Its sections and derivatives lie in C because C is constant. The image of M in Q is already the saturated high O(18), whereas the derivative of this Wp block supplies a nonzero lower O(6) component. Consequently the map C/N -> Q has generic rank2. Its image generically lies in the two positive summands O(6)+O(18): modulo M the nonzero derivative supplies the one remaining direction, and all those derivative values belong to the original positive image. Since that positive bundle is saturated, the whole map factors through it.

The sequence 0->M/N->C/N->C/M->0 gives rank C/N=2 and degree24, the same as O(18)+O(6). Its generic isomorphism to that bundle has determinant of degree0 and is therefore everywhere an isomorphism. Thus

    E intersect C=N exactly,
    C/N=O(18)+O(6) inside Q,

and constant projection embeds

    R=E/N subset (H/C) O,
    rank R=9, deg R=-30,

with derivative image only O(-10), saturated.

## 6. The final projected bundle cannot exist

After quotienting E by D O(-2) and the Euler Wp O(-3), the remaining O(-8) in N maps into

    Wp O(-1)+T O(-3)+O(-8)+O(-10).

Its O(-10) component is zero by degree. If its scalar O(-8) component is nonzero, then

    R=Wp O(-1)+T O(-3)+O(-10),

so H0(R)=0. If the scalar component is zero but the T component is nonzero, H0(R) injects into the kernel of

    H1(O(-8))=V+P -> H1(T O(-3))=V+P+D.

This map is injective: its Serre dual is the classical onto multiplication T W=Sym5 W tensor W -> Sym6 W=V+P. Thus again H0(R)=0.

If both scalar and T components vanish, the line maps only to Wp O(-1), nontrivially. Its degree7 covariant is basepoint-free, and its quotient is O(6). Hence R contains a positive-degree direct line O(6), impossible in a constant bundle. These cases are exhaustive.

Therefore every possible actual R has H0(R)=0. All its ordinary splitting degrees are negative. Strict-top applied to its highest block and derivative image O(-10) forces every splitting degree to be at most -10: otherwise the entire highest block has zero Hom to O(-10). But rank R=9 then gives degree R<=-90, contradicting degree R=-30. This eliminates the last first-span case and proves the bf source exclusion.

## Boundary

The attached verify.py checks the fixed high-D kernel and its completeness identities, all 42 stated internal Hom spaces, polar and cubic-T characters, degree contradictions, and exact original source identity against immutable Git blob pins. REPRODUCE.md supplies the input-download instructions. These arithmetic checks do not replace the saturation, constant-connection, exact-intersection, or branch-exhaustion arguments above.

This is a whole-source exclusion, not a whole-label exclusion or a current frontier count. Only the displayed original tuple is removed. Every argument uses universal characters, actual bundle images and saturation, and genuine constant projections. No selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance ranks, experiments, scans, or large computation are used. This is written mathematics, not Lean certification.
