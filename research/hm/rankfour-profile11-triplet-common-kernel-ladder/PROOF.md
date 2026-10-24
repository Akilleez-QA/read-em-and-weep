# The defect-twelve common-kernel ladder has two forced images and an honest rank-seven endpoint

## Statement and retained boundary

Retain all actual-geometric hypotheses and conclusions of PR1216, including the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive branch A_q=A(4)+O(-8), im beta_K=A(2). Retain the original t=0 and the new local defect delta in {0,12} of F=p(K^-).

Assume in this proof that delta=12. PR1215 then gives the actual embedded coherent image

    im beta_F=O(10)+O(2)(-D12),                       (1)

where D12 is the unique reduced twelve-point orbit and the O(2) is the actual lower normal subline. Let T_j be the original actual degree-eighteen jets and B_j=ann(T_j), as proved through order nine in PR1216. Put

    F3=F,  F4=F intersect B4,
    F5=F intersect B5,  F6=F intersect B6.

Then all these intersections are actual saturated subbundles in the same constant ambient V18* O, and

    rank F4=9, deg F4=-74,
    rank F5=8, deg F5=-82,
    rank F6=7, deg F6=-88,
    B_j/Fj=O(4),  j=3,4,5,6.                       (2)

For j=4,5,6 their derivatives have generic rank two. Their saturated actual normal targets are

    E_j=(B_(j-1)/Fj)(-2)=O(16-2j)+O(2).             (3)

The first two coherent images are forced as actual subsheaves:

    I4=im beta_(F4)=O(8)+O(2)(-D12),
    I5=im beta_(F5)=O(6)+O(2)(-D12).                (4)

At rank seven the exact necessary alternatives are

    I6=O(4)+O(2)(-D12),                             (5a)
    or
    I6=O(4)(-D12)+O(2)(-D12)=E6(-D12).             (5b)

Thus the same simple lower-normal defect propagates through ranks nine and eight. At rank seven it either remains cyclic in that direction or appears in both normal directions, with local elementary divisors (1,1) on D12. The corresponding defect lengths of I_j in E_j are 12,12, and respectively 12 or24; these are not redefinitions of the original delta.

Every Fj in (2) spans all fifteen constant dimensions. No alternative in (5), no value of delta or the separate e9 from PR1216, and no retained F18 or dual-extension type is excluded or asserted to occur here. No original higher jets beyond the already proved order nine, algebraicity or whole-branch/profile exclusion are inferred. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank or normalization is selected or evaluated.

## 1. Complete immutable inputs and actual adjacent quotients

INPUTS.json records two complete freshly fetched immutable sources with exact commits, paths, Git blobs, UTF8 lengths and SHA256 hashes:

* PR1216 at 66a6bfe8dd424da58f3d775be1818d1f4f71eff1, research/hm/rankfour-profile11-triplet-nine-jets/PROOF.md.
* PR1215 at 8ca4ccd046248752714a84dfb05aae42a6433f55, research/hm/rankfour-profile11-triplet-twelve-orientation/PROOF.md.

All transitive actual-geometric hypotheses remain assumptions. We work over C on the physical binary-icosahedral line, with G=SL2(F5) and the fixed determinant convention. There are no nontrivial scalar characters. The projective orbit sizes are 12,20,30,60; thus the only invariant effective divisor of positive degree below fourteen has degree twelve and equals D12. There is no invariant section of O(14), since fourteen is not a nonnegative combination of the orbit sizes. The center-even irreducible dimensions are 1,3,3,4,5.

The actual original jet annihilators satisfy

    B_j=B_(j-1)^-,
    rank B_j=14-j, deg B_j=-(j+1)(18-j),
    phi_j:=beta_(B_j):B_j -> O(16-2j)
    is coherently onto,  3<=j<=8.                    (6)

For the present ladder only j=3,4,5 is needed to construct the next common kernel. All these bundles and all their subbundles have negative top degree, since B_j subset B3 subset Sym14 W(-4).

The initial F3 has rank ten and degree -64, lies in B3 with quotient O(4), and its coherent image is (1). The O(10) projection of beta_(F3) is the restriction phi_3|F3, by naturality of the derivative in the constant ambient.

## 2. The coherent two-column capacity for the ranks used here

Let Q be a negative-top actual saturated bundle of rank n in a constant ambient, whose derivative has generic rank two and actual coherent image with ordinary degrees a>=b. Then for some 1<=k<=floor(n/2),

    deg Q <= (n-k)a+kb
       -(n-k)(n-k-1)-k(k-1).                       (7)

Indeed form the actual backward kernels Q_(i+1)=Qi^-. Every nonzero stage has negative top, so it cannot be horizontal and no nonzero residue survives. The actual quotients Ri admit coherent injections Ri->R_(i-1)(-2), hence Ri->im beta_Q(-2i). Their positive ranks are two repeated k times, followed by one repeated n-2k times. A rank-two quotient has degree at most a+b-4i; a rank-one quotient has degree at most a-2i. Summing yields (7).

No coherent image is replaced by its saturation, and no quotient is assigned a connection. This is the same direct actual-flag argument at each indicated rank, not a theorem transported from a different ambient rank.

We also use its rank-one version: if the coherent derivative image is O(c), the n actual line quotients give

    deg Q<=n c-n(n-1).                              (8)

Both inequalities keep all torsion deficits in the individual coherent injections.

## 3. One actual common-kernel step and its two normal projections

Suppose, for one j in {4,5,6}, that F_(j-1) subset B_(j-1) has quotient O(4), and its coherent derivative image is already

    O(18-2j)+O(2)(-D12).                            (9)

The first projection is the restriction of phi_(j-1). It is onto. Define

    Fj=F_(j-1) intersect B_j
      =ker(phi_(j-1)|F_(j-1)).                       (10)

There are actual exact sequences

    0 -> Fj -> F_(j-1) -> O(18-2j) -> 0,
    0 -> Fj -> B_j -> O(4) -> 0.                    (11)

The first quotient is locally free and F_(j-1) is saturated, so Fj is saturated in the constant ambient. Surjectivity onto B_(j-1)/B_j gives the actual sum and intersection

    F_(j-1)+B_j=B_(j-1),
    F_(j-1) intersect B_j=Fj.                        (12)

Consequently the two actual quotient subbundles give a direct sum

    B_(j-1)/Fj
       =(F_(j-1)/Fj) direct-sum (B_j/Fj)
       =O(18-2j)+O(4).                              (13)

After twisting, this is exactly E_j in (3). The splitting comes from the actual sum/intersection (12), not from a vanishing Ext group. In particular no Ext vanishing is asserted at j=6, where the abstract extension of O(4) by O(2) could be nontrivial without this geometric splitting. Neither quotient summand is declared horizontal.

Derivatives of Fj lie in B_(j-1), because Fj subset B_j=B_(j-1)^-. Thus beta_(Fj) factors regularly through E_j. Its projection to the O(2) summand is the restriction of beta_(F_(j-1)) projected to B_(j-1)/F_(j-1). Since Fj is exactly the kernel of the first projection in (9), the remaining coherent projection is everywhere onto

    O(2)(-D12)=O(-10).                              (14)

This is the same actual divisor and normal line as before, not a newly chosen defect. Therefore

    I_j:=im beta_(Fj) subset O(16-2j)+O(-10),        (15)

and its projection onto the displayed O(-10) is onto.

Using (11), the three possible steps give respectively

    (rank Fj,deg Fj)=(9,-74),(8,-82),(7,-88).        (16)

Their derivatives cannot have rank one. If one did, its nonzero projection onto O(-10) would identify its coherent image with O(-10), as a map from a line bundle onto its image. The upper bounds (8) would be respectively

    -162, -136, -112,

strictly below the degrees in (16). Thus rank beta_(Fj)=2. Its saturation is the entire actual E_j, because it has full generic rank in that rank-two subbundle. This proves the normal-target assertions without prematurely saturating the coherent image in (15).

## 4. The rank-nine coherent image is forced

Apply Section 3 first with j=4, using (1). It constructs F4 of rank nine and degree -74, with coherent image I4 subset O(8)+O(-10), onto the second line. Let a>=b be its ordinary degrees. Necessarily

    b<=-10:                                         (17)

if both degrees exceeded -10, no ordinary map to the second line could be nonzero.

Suppose a<=-2. Substitution into (7), with 1<=k<=4, gives

    deg F4<=-90+10k-2k^2<=-78,

contradicting -74. Hence a>-2. Since b<=-10, the degrees are unequal. The canonical top line is equivariant and has the physical scalar linearization O(a). Its component to O(-10) is zero by degree, so its component to O(8) is nonzero. The degree 8-a is nonnegative and less than ten, hence an invariant section must have degree zero. Therefore a=8 and the actual top line maps isomorphically to the full O(8) in (15).

I4 thus contains that full normal summand. Since its projection to O(-10) is onto, it is the entire preimage of that quotient line:

    I4=O(8)+O(-10)
      =O(8)+O(2)(-D12) subset E4.                  (18)

This establishes (9) for the next step, not just an abstract splitting type.

## 5. The rank-eight coherent image is forced

Apply Section 3 with j=5 using (18). It constructs F5 of rank eight and degree -82, with I5 subset O(6)+O(-10), onto O(-10). Again its ordinary lower degree satisfies b<=-10.

If a<=-6, the actual capacity (7), now for 1<=k<=4, gives

    deg F5<=-104+12k-2k^2<=-86,

contradicting -82. Hence a>-6, so the degrees are unequal and the top line is a physical scalar O(a). Its only possible nonzero component is to O(6), with invariant degree 6-a between zero and eleven. This forces a=6. The same full-summand and quotient argument gives

    I5=O(6)+O(-10)
      =O(6)+O(2)(-D12) subset E5.                  (19)

Again this is an actual embedded coherent image, preserving the lower defect orientation.

## 6. The rank-seven endpoint really has two alternatives

Apply Section 3 with j=6 using (19). It constructs F6 of rank seven and degree -88. Its coherent image satisfies

    I6 subset O(4)+O(-10),
    I6 -> O(-10) is onto,
    rank I6=2.                                      (20)

Let a>=b be its ordinary degrees. As before b<=-10. If a<=-10, capacity (7) gives, for 1<=k<=3,

    -88=deg F6<=-112+14k-2k^2<=-88.

Equality is necessary throughout. The last equality occurs only at k=3, and the positive coefficients of both a and b force a=b=-10. Equivariance would then give I6=R O(-10), with R a two-dimensional center-even representation. The retained irreducible dimensions force R=1+1. But its component to O(4) in (20) would be an invariant section of O(14), and this space is zero. Its map into (20) would have generic rank at most one, a contradiction.

Thus a>-10 and the degrees are unequal. The top scalar line has zero component to O(-10) and a nonzero component to O(4). Its invariant degree 4-a is nonnegative and strictly less than fourteen. The orbit-size restriction forces

    4-a=0 or12,
    a=4 or-8.                                       (21)

In either case the top line has no lower component. The lower summand alone must map onto O(-10); a surjection between line bundles is an isomorphism, so b=-10.

For a=4, the top maps isomorphically onto the full O(4). Equation (20) therefore yields precisely (5a).

For a=-8, the top maps into O(4) with zero divisor D12. The lower O(-10) cannot have an O(4) component, since its degree-fourteen invariant Hom space is zero. Its O(-10) component is an isomorphism by surjectivity. Thus the actual coherent subsheaf is diagonal with both normal directions vanishing on the same D12:

    I6=O(4)(-D12)+O(2)(-D12),

which is (5b). This second case has torsion length twenty-four and elementary divisors (1,1), not a cyclic length-two defect.

No torsion-Hom argument from an earlier rank excludes (5b): the relevant upper target has become O(4), and Hom_G(O(4),O(4)|D12) contains the nonzero invariant restriction of the identity. The proof deliberately retains this endpoint.

## 7. Full constant span and the remaining incidence problem

The recursive intersections in (10) equal F intersect B_j because the B_j are nested. Moreover (12), inductively together with F+B3=B3, gives F+B_j=B3 for j=3,4,5,6. The quotients in (11) are the actual O(4) quotients inherited from B3/F.

Dualizing 0->Fj->B_j->O(4)->0 inside the constant pairing gives

    0 -> T_j -> ann(Fj) -> O(-4) -> 0.              (22)

Since T_j=Sym^j W(j-18) has negative ordinary degree for these j, both end terms have no global sections. Therefore H0(ann(Fj))=0. No constant functional annihilates all fibers of Fj, so its full constant span is V18*, of dimension fifteen.

This full-span conclusion concerns each entire Fj. It is not transferred to a scalar tail or a proper jet subbundle in a later hypothetical backward flag. Such a transfer would need its own proof.

The original delta=12 has now forced two more actual coherent images, with exact transversality and a controlled rank-seven endpoint. The upper-normal degree has fallen to four precisely where the earlier invariant Hom obstruction stops vanishing. Resolving either alternative in (5), or relating it to the separate e9 endpoint, is a further problem and is not asserted here.
