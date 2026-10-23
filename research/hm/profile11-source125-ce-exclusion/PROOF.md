# The ce source of G3.11.ea6bced3bddf is impossible

## Scope

This proof excludes exactly the original ce source stated below. It does not exclude the whole label. The source is index125 tuple (0,0,1,0,1,0,0,1), label G3.11.ea6bced3bddf:

    E=(V+2P) O(-2)+V O(-4)+Wp O(-5)+O(-10),
    A_q=O(-10)+O(4)+O(16), B_q=O(-18)+O(-6)+O(8), defect=0.

The original catalog commit is db51525015bb7c5e825833d550d08dedf6f6ea96. Source and label Git blobs are fe0afa410d89340d3082dc814277f89fbb582c19 and 8b5971092f9ef762584912609fd5e9301c4e271d. Conventions, saturated actual derivative images, first-polar generation, strict-top, and genuine constant projections are those of the reviewed cf proof, PR882, commit ef8ed8d457494608472a2c07de776e9162b2c20f. The fixed high-P kernel classification below is the universal calculation in Section2 of the be proof, PR887 at commit 3ab2f311ed2e87828d42c7c0ce0124bcd6e35771, research/hm/profile11-source125-be-exclusion/PROOF.md; a short completeness summary is included here. No be source exclusion is assumed to exclude ce.

We write W for the defining binary-icosahedral two-space, Wp for the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P for the remaining even representations of dimensions3,4. Every nonempty invariant effective divisor has degree at least12. The source has rank17, degree-54. The full quadratic top G0=(V+2P)O(-2) has rank11, degree-22. All projections below are by actual constant subspaces.

## 1. The lower row on 2P is nonzero

Suppose its O(4) row vanished. The high system on F2=2P O(-2) is onto: strict-top gives eight independent sections of O(18), whereas removing any invariant divisor leaves at most seven. Its complete kernel list is

    K1=Wp O(-3)+V O(-4)+W O(-7),
    K2=Wp O(-3)+V O(-4)+O(-6)+O(-8).

For completeness, rank K=7, degree K=-32, H1(K(2))=A+V+D, and chi(K(3))=Wp-W-S. Degree, rank and parity bound all summands with nonzero H1 to

    A(-4), V(-4), D(-4), S(-5), O(-6), W(-7), Wp(-7), O(-8), O(-14).

The remaining possible degree-minus-three coefficients are W,Wp,S,T. The H1 budget allows, before adding degree-minus-three atoms, only the following rank-at-most-seven assemblies:

    A(-4)+V(-4)+O(-8),
    V(-4)+S(-5),
    A(-4)+Wp(-7),
    V(-4)+W(-7),
    V(-4)+O(-6)+O(-8),
    O(-6)+Wp(-7),
    O(-14).

The first two have twist3 character -S and fail. The third requires degree-minus-three coefficient Wp+T-W-S, the sixth Wp+T-S, and the seventh Wp+T-W, all impossible characters. The fourth and fifth each require precisely Wp(-3), giving K1,K2.

The internal target is V(-4)+V(-6)+Wp(-7)+O(-12). For either kernel the only channel is the scalar V(-4) to V(-4). Thus the internal image is either zero or that full saturated V(-4). Zero gives first-span degree -16+18=2, impossible. The nonzero case gives rank12, degree-4. Its Euler character is A+D, so first-polar generation would make its constant coefficient A+D and its linear coefficient

    Sym19 W-(A+D)W = Wp-S+T.

This is not an actual representation. Both cases are impossible.

Thus the lower P functional is nonzero. Let P_h be its kernel direction and P_l a complementary direction. Then F=P_h O(-2) is high-only, and P_l maps onto O(4).

## 2. The high-only P cannot be basepoint-free

An onto P(-2)->O(16) has exactly the following necessary kernels:

    K_A=A(-8), K_W=W(-7)+O(-10), K_U=Wp(-3)+O(-18).

The bounded proof uses rank3, degree-24, H1(K(2))=A+V+P+D and chi(K(3))=-W-S-T. Rank-three even atoms leave only A(-8); rank-two odd plus a line leaves W(-7)+O(-10) and Wp(-3)+O(-18), after O(-6) is excluded by Hom(O(-6),P(-2))=0. Three scalar lines similarly require O(-6) and are excluded. No realization claim for all three types is used.

Suppose F were onto O(16). The full top then maps onto the saturated positive pair. Its external kernel fits

    0 -> K -> Kfull -> Klow ->0,

where Klow is the kernel of (V+P_l)(-2)->O(4). If the V lower row vanishes, Klow=V(-2)+V(-4). If it is nonzero, the system is complete Sym6 and Klow=T(-3). Every one of these kernels, including all three possible K, has zero Hom to the remaining internal target

    V(-6)+Wp(-7)+O(-12).

Hom vanishing on both ends of the extension implies Hom vanishing on Kfull; no Ext splitting is required. Thus the full top has no internal derivative image. Its saturated first span has degree

    -22+6+18=2,

impossible in a constant bundle. The high-only P therefore has a nonempty invariant base divisor. It is necessarily the degree12 divisor; its raw high image is O(4), with kernel V(-4).

## 3. The high-only P first span in the divisor branch

For F=P_h(-2), the internal target is (V+P_l)(-4)+V(-6)+Wp(-7)+O(-12). Its V(-4) kernel has only the scalar channel to the top V(-4). If this is zero, its total raw derivative has rank1 and image O(4). The saturation has image O(4+delta), where delta is zero or an invariant divisor degree at least12. The quadratic rank4 rank-one gap requires 6+delta=8 or 6+delta<=3, impossible.

Hence the internal image is the full V(-4). The raw full derivative has rank4, degree-8. Its saturation can only add an invariant divisor of degree delta=0 or delta>=12. The corresponding first-span degree is -8+delta, so delta must be zero. First polars and characters give

    M_F=F^+=(Wp+T)(-1),
    E intersect M_F=(V+P_h)(-2)=:N,
    M_F/N=O(6),

and this last line maps to the original high O(18) through the invariant degree12 divisor. The intersection splitting follows because V(-2) has no component in P_h(-2), and the only internal channel above was the source top V itself.

## 4. The V lower row cannot be nonzero

Assume it is nonzero. The external derivative of N=(V+P_h)(-2) is abstractly O(4)+O(4): the lower V degree6 system is onto, the high P_h degree6 system is onto, and the second line is included in O(16) through the divisor12. Its kernel is

    Wp(-5)+V(-4).

In the complementary internal target P_l(-4)+V(-6)+Wp(-7)+O(-12), its only channel is the tautological Wp(-5)->P_l(-4). Hence the internal image is zero or that full saturated Euler subbundle. In the two cases the raw first spans have degrees -2 and -8. Any nonzero saturation divisor would have degree at least12 and make the span positive, so these raw spans are saturated.

First-polar characters give respectively

    M0=(V+P)O+Wp(-1),
    M1=V O+(Wp+T)(-1).

The first case is impossible. Project by its actual constant V+P. If N has nonzero image in Wp(-1), its P component covers that whole linear bundle. Local lifts and the actual derivative force its nonzero constant first span inside Wp(-1), impossible. If its image is zero, N is a full-rank saturated subbundle of the rank7 constant V+P, impossible since degree N=-14.

Consider M1. Project by its actual constant V, and write L=(Wp+T)(-1). The source V(-2) maps only to T(-1), nontrivially: Hom(V(-2),V O)=0 because V is absent from V A=P+D. Both P_h components must be nonzero. If its Wp component vanished, V+P_h would cover the whole T(-1) by the complete Sym6 contraction, contradicting the linear-span obstruction. If its T component vanished, P_h would cover the whole Wp(-1), with the same contradiction.

With all three components nonzero, rescaling the irreducible source and target factors identifies N->L with the standard saturated inclusion

    Sym6 W O(-2) -> Sym7 W O(-1),

whose quotient is O(6). The exact intersection of M1 with E is

    N1=N+Wp(-3),

where the extra Wp is the canonical Euler subbundle of P_l(-2). This follows from the unique internal channel and ordinary extension vanishing. The composition of that extra block with L/N=O(6) is zero, since Wp is absent from Sym9 W. It follows that

    E intersect V O=Wp(-3),   V/(E intersect V)=O(6).

More explicitly N maps isomorphically onto its image in L, so the preimage of that image in M1 is the direct sum of N and the actual constant V. The extra Wp therefore yields the stated rank2 intersection. The intersection cannot have rank3, as saturated E would then contain V O. Its projection to the P_l source direction is the canonical Euler map and is nonzero. It has no lift to the top V(-2), because Wp is absent from V W=T; a possible lift to P_h(-2) has zero lower row by definition.

The derivative of this intersection block has nonzero lower row: otherwise the nonzero degree6 P_l system would factor through Wp(-1), whose Hom to O(4) is zero. Its degree7 restriction is onto. Since V is constant and lies in M1, its image in Q lies in the saturated positive pair. The quotient O(6) has nonzero scalar lower component and hence is a saturated graph line. Constant projection therefore produces a saturated source

    E'=Wp(-1)+(V+P)(-2)+V(-4)+Wp(-5)+O(-10)

with derivative image O(-10)+O(16). Here quotienting 2P(-2) by the Euler block gives P(-2)+Wp(-1); possible diagonal lifts do not affect the splitting.

The highest Wp(-1) must map onto O(16). Its degree17 covariant has no base divisor, since removing degree12 would require Wp in Sym5 W. Its constant first span is P=Wp W. The kernel of its external derivative is O(-18); its only internal channels are into the two top rows V(-4),P(-4). Both degree14 line systems are basepoint-free: removing divisor12 would require V or P in Sym2 W. A zero internal image gives positive first-span degree16. Thus the internal image is a saturated O(-18), and the first span is the actual constant P, with exact intersection

    Wp(-1)+O(-16),

and saturated high quotient O(18).

Project this constant P out. The remaining O(-16) maps only into (V+P)(-2): it has no component in V(-4), Wp(-5), or O(-10), because V is absent from Sym12, Wp from Sym11, and 1 from Sym6. The final projected source therefore contains the locally free direct summand

    ((V+P)(-2))/O(-16),

of rank6 and degree -14+16=2. A positive-degree bundle cannot embed in a constant bundle. This excludes the entire divisor12 branch with nonzero V lower row.

## 5. The remaining zero-V-lower-row branch is impossible

We are left with zero lower row on the top V. Write N=(V+P_h)(-2). Strict-top makes its high system the complete degree6 system multiplied by the invariant degree12 form: both V and P_h components are nonzero, and their degree18 systems have this factor. The V component factors because V occurs only once in Sym18, and multiplication of its nonzero degree6 covariant by the invariant form already gives that occurrence.

Let q be the restriction of the complementary P_l high row to its lower-row kernel V(-4). This is either zero or the unique degree20 V covariant.

### 5.1 The nonzero restricted high row

Suppose q is nonzero. It is basepoint-free. The only possible nonempty invariant base-divisor degrees at most20 are12 and20; removing them would require V in Sym8 or Sym0, neither of which occurs. Consequently the full top G0 maps onto O(4)+O(16), including at the zero divisor of the high-only P row: the lower P_l row is onto, and q supplies a nonzero high component within its kernel at every point.

Let Kfull be the full positive kernel. Then

    rank Kfull=9, degree Kfull=-42,
    H1(Kfull(2))=A+V+P+D,
    chi_G(Kfull(3))=-W-S.

Its complete necessary kernel list is

    W(-7)+V(-4)+P(-4),
    W(-7)+V(-4)+Wp(-5)+Wp(-3),
    W(-7)+O(-10)+T(-3),
    A(-8)+T(-3),
    O(-18)+(Wp+T)(-3).                         (5)

Here is a short completeness proof. Every degree is at most-3 by strict-top. For an atom of rank r and ordinary degree -j, the rank and degree bound gives r*j+3*(9-r)<=42. This bound, central parity and the H1 budget restrict all nonzero-H1 atoms to

    A,V,P,D at degree-4;
    Wp,S,T at degree-5;
    1,V,P,D at degree-6;
    W,Wp at degree-7;
    1,A,V at degree-8;
    W,Wp at degree-9;
    1 at degrees-10,-12,-14,-18.

The zero-H1 atoms are W,Wp,S,T at degree-3. Among the displayed nonzero-H1 atoms, only O(-6), W(-7), A(-8), and O(-18) contribute a negative W to chi at twist3. Each consumes the unique A in the H1 budget, so exactly one of these must occur. O(-6) cannot inject into G0, since neither V nor P occurs in Sym4. A(-8) or O(-18) consumes the whole H1 budget, and the twist3 character forces T(-3) or (Wp+T)(-3), respectively. W(-7) consumes A+D; the remaining V+P budget can only be V(-4)+P(-4), V(-4)+Wp(-5), or O(-10). The required degree-minus-three corrections are respectively zero, Wp, and T. This proves (5).

Every atom in every kernel in (5) has zero Hom to the remaining internal target

    V(-6)+Wp(-7)+O(-12).

Thus the full top has zero internal derivative image and saturated first increment O(6)+O(18). Its first-span degree is again -22+24=2, impossible.

### 5.2 The zero restricted high row

Suppose q is zero. The complementary P_l high row then factors through its lower quotient O(4). The factor O(4)->O(16) is a scalar multiple of the unique degree12 invariant form. Hence the whole full-top high row has this divisor, and the abstract raw positive image is O(4)+O(4). The first raw O(4) is the actual lower target, and the second is included in the high target through the invariant form.

The kernel is T(-3)+V(-4): first take the complete high degree6 system on N, with kernel T(-3), then the lower quotient of P_l, with kernel V(-4); the resulting extension splits by ordinary positive-degree H1 vanishing. Both summands have zero Hom to V(-6)+Wp(-7)+O(-12), so the full internal image is zero.

The raw first span has rank13 and degree-10. Any nonzero saturation divisor has invariant length at least12, making its degree positive. Thus it is saturated. First-polar characters give precisely

    M=G0^+=V O+(2Wp+T)(-1).                    (6)

Project by its actual constant V and write L=(2Wp+T)(-1). The component of 2P(-2) in the unique T(-1) factor is determined by a linear functional on the two-dimensional P multiplicity space. Choose any nonzero P direction in its kernel. Its projection to 2Wp(-1) cannot vanish as well, since then that rank4 source copy would inject into the rank3 constant V.

The unique nonzero P(-2)->Wp(-1) channel is the Euler surjection, since P=Wp tensor W. Thus this source direction covers an entire Wp(-1) multiplicity summand of L. Every local section of that summand has a local lift in G0; its derivative therefore lies in L, because the full first span is M and the projection is by a genuine constant space. The nonzero constant first span of this linear summand would consequently lie in the pure linear bundle L. This contradicts H0(L)=0.

Both q branches are impossible. Together with Sections1-4 this proves the entire original ce source exclusion.

## Boundary

The companion verify.py checks fixed universal characters, 121 Hom spaces, the bounded kernel support and negative-W classification, degree contradictions, and the exact original source identity against pinned Git blobs. These checks do not replace the actual-connection, saturation, exact-intersection or branch-exhaustion arguments above.

This excludes one original source, not the whole label or a current frontier count. No selected actual HM/source coefficient, parameter, point, derivative evaluation, matrix, instance rank test, experiment, source scan, or large computation is used. This is a written structural proof, not Lean certification.
