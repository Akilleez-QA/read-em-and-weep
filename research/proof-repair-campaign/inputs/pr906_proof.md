# The bb and bc sources of G3.11.ea6bced3bddf are impossible

## 0. Scope, actual bundles, and fixed dependencies

This excludes exactly two original source tuples at index125, stable label G3.11.ea6bced3bddf:

    bb=(0,2,0,0,0,0,0,1): E=P(-2)+2T(-3)+O(-10),
    bc=(0,1,1,0,0,0,0,1): E=(V+P)(-2)+T(-3)+V(-4)+O(-10).

Both have rank17, degree-54, and endpoints

    A_q=O(-10)+O(4)+O(16),
    B_q=O(-18)+O(-6)+O(8),

with original determinant defect zero. The pinned catalog commit is db51525015bb7c5e825833d550d08dedf6f6ea96. Under research/hm/order-four-quadratic-load/, the source and label catalogs are one-one-endpoint-necessary-pairs.json and rank-three-quotient-frontier-144.json, with Git blobs fe0afa410d89340d3082dc814277f89fbb582c19 and 8b5971092f9ef762584912609fd5e9301c4e271d.

Use the actual-bundle conventions and lemmas of the published cf proof, PR882 at ef8ed8d457494608472a2c07de776e9162b2c20f, research/hm/profile11-source125-cf-exclusion/PROOF.md. In particular E is saturated in H O, dim H=30, H0(E(1))=0, and the displayed A_q is the actual saturated derivative image in Q(-2), Q=H O/E. We use strict-top, the actual internal/external image lemma, the connection-preserved coherent-image lemma, and the quadratic rank-r rank-one increment gap: its saturated first increment O(b) satisfies b=2r or b<=r-1. The cf complete-Sym6 obstruction is restated in Section7 below.

G is binary icosahedral. W is the defining two-space; Wp is the other two-space; A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W; V and P are the remaining even irreducibles of dimensions3 and4. All are self-dual. Every nonempty invariant divisor has degree at least12; below20 the only positive possibility is12. All constant spaces below are genuine subspaces of the ambient H, obtained from global sections. No abstract splitting is assumed horizontal.

Write E=F+O(-10), where F is the rank16 degree-44 positive-degree source part displayed above.

## 1. A forced actual constant A captures the high line

Let Epos be the inverse image in H O of the saturated positive pair O6+O18 in Q. Thus

    0 -> E -> Epos -> O6+O18 ->0.

It has rank19 and degree-30. For both bb and bc,

    chi_G(E)=-2V-4P-3D,
    Sym6=V+P,
    Sym18=A+V+2P+D,

so

    chi_G(Epos)=A-P-2D.                         (1)

The A multiplicity in H0(Epos) is therefore positive. Choose an irreducible A subspace of these sections. Since Epos lies in H O, it is an actual constant A O in H O. Its image in Q lies in O6+O18. The low component vanishes because A is absent from Sym6. The high component is nonzero, since otherwise A O would lie in E, contrary to H0(E)=0.

The degree18 A system is basepoint-free. A nonempty invariant base divisor could only have degree12, but removing it would require A in Sym6. Consequently this constant A maps onto the saturated high O18.

Let K=E intersect A O. Then K is a saturated rank2 degree-18 subbundle of A O. Its exact splitting is

    K=W(-9).                                   (2)

Here are all rank-two possibilities, not merely a K-class inference. Its H1 is Sym18-A=V+2P+D and H0 is zero. A rank-two irreducible must be W(-9) or Wp(-9). The latter has H1=1+A+V+P+D and is excluded. Two scalar lines have even positive degrees summing18, hence pairs (2,16),(4,14),(6,12),(8,10). The first three violate the H1 budget; the last has the correct budget but O(-8) cannot inject into A O because A is absent from Sym8=P+D. This proves (2).

Constant projection by A is now legitimate without any saturation correction: its image in Q is the whole saturated O18. It embeds

    E'=E/K subset (H/A) O

as a saturated bundle with actual derivative image O(-10)+O4. Since Hom(W(-9),O(-10))=0 by ordinary degree, K lies in the original F summand. Hence

    E'=R+O(-10),  R=F/K,  rank R=14, deg R=-26.  (3)

This is an actual quotient splitting, not a character replacement. We do not assert that the source splitting in (3) is horizontal. The external derivative of R has zero O(-10) component: precomposition with F onto R reduces this to the ordinary degree vanishing Hom(F,O(-10))=0.

## 2. Determine the genuine constants of R

Let C0=H0(R), viewed as its actual constant subspace in (H/A) O. Since R is a subbundle of a constant bundle, all its ordinary degrees are nonpositive, and its global sections are exactly its degree-zero direct summand. Project C0. We obtain

    E''=Z+O(-10),  Z=R/C0,
    H0(Z)=0,  deg Z=-26,                        (4)

still with saturated derivative image O(-10)+O4. At this point rank Z is not yet assumed.

The exact sequence 0->W(-9)->F->R->0 gives

    C0 subset H1(W(-9))=V+2P+D,                 (5)
    H0(R(1)) subset H1(W(-8))=Wp+2T.            (6)

For both sources H0(F(1))=0 and H1(F(1))=2T. Thus the mandatory Wp in the right side of (6) lies in H0(R(1)). Also

    H0(Z(1))=H0(R(1))-C0 tensor W               (7)

as representations, by the exact sequence of global sections after twisting the constant quotient by1.

The Wp multiplicity in H0(Z(1)) is zero. Indeed, since H0(Z)=0, any such copy is a genuine degree-1 direct summand Wp(-1) of Z. Its external derivative to O4 vanishes because Wp is absent from Sym5, and its derivative to O(-10) vanishes by degree. Its internal derivative to the other source summands twisted by-2 is also zero: every other degree is at most-1, whereas the source has degree-1. Thus its actual derivative is zero modulo E'', and its nonzero constant first span P would lie in E''. This contradicts H0(E'')=0.

Therefore C0 tensor W must account for the mandatory Wp in (6). Using

    V tensor W=T,
    P tensor W=Wp+T,
    D tensor W=S+T,

together with (5)-(6), the only possibilities are

    C0=P or C0=V+P.                             (8)

There is no D, since that would supply an S in (6); there is at most one P, since (6) contains only one Wp; and (5) contains at most one V.

The second possibility is impossible already at twist2. We have

    H1(W(-7))=D+V+P.

For bb, H0(F(2))=P and H1(F(2))=0. For bc, H0(F(2))=V+P and H1(F(2))=V. In both cases the cohomology exact sequence shows that H0(R(2)) has D multiplicity exactly one. But

    (V+P) tensor Sym2 = V+2P+2D

has D multiplicity two and cannot inject into H0(R(2)). Hence

    C0=P,  rank Z=10.                           (9)

## 3. There is no surviving linear top

Equations (6)-(9) show that H0(Z(1)) is either zero or one copy of T. Suppose T occurs. It is the whole degree-1 top T(-1) of Z. Strict-top makes its O4 map nonzero; it is the complete degree5 system, hence onto, with kernel D(-2).

The remaining summands of Z have degrees at most-2. The internal target after removing T(-1) therefore has degrees at most-4, together with the scalar O(-12). There is no ordinary Hom from D(-2) to these targets. Thus the first span of T(-1) is the actual constant V+P, with exact intersection T(-1) and saturated quotient O6.

Project this constant span, removing the low positive derivative line. The residual is section-free, rank5 and degree-30: Z loses rank6 and degree-6, and the original scalar O(-10) remains. Its only derivative target is O(-10). Strict-top forces every splitting degree to be at most-10, which would give total degree at most-50, a contradiction.

Consequently

    H0(Z(1))=0,                                (10)

so every ordinary degree of Z is at most-2.

## 4. The bb source reduces to a forbidden quadratic P top

For bb the twist2 exact sequence gives

    H0(R(2))=V+2P+D,  H1(R(2))=0.

Subtracting the actual constant P tensor Sym2=V+P+D yields

    H0(Z(2))=P,  H1(Z(2))=0.

Thus Z has exactly the quadratic top P(-2). Since rank Z=10 and deg Z=-26, its remaining rank6 part has degree-18 and all degrees at most-3. It must be pure degree-3. The twist3 Euler character is

    chi_G(R(3))=Wp+S+4T,
    P tensor Sym3=S+2T,
    chi_G(Z(3))=Wp+2T.

The quadratic P contributes Wp+T, leaving cubic coefficient T. Therefore the actual quotient splitting is

    Z=P(-2)+T(-3).                              (11)

Section6 excludes (11) together with the untouched scalar O(-10).

## 5. The two bc quartic-component cases

Let u be the component of the actual K=W(-9) inclusion into the original V(-4) source tail.

If u is nonzero, the twist2 cohomology map

    H1(W(-7))=D+V+P -> H1(V(-2))=V

is onto. This is not inferred just from its allowed character: by Serre duality its dual is the coefficient inclusion V -> W tensor Sym5 associated to the nonzero bundle map u. It is nonzero and injective by irreducibility.

The exact sequence therefore gives H0(R(2))=V+2P+D and H1(R(2))=0, exactly as for bb. Sections3-4 again force the actual splitting (11), and Section6 excludes it.

If u is zero, K lies entirely in F0=(V+P)(-2)+T(-3), so

    R=(F0/K)+V(-4).

The actual constants P have zero projection to V(-4) by degree. Hence

    Z=Z0+V(-4),  Z0=(F0/K)/P.

Here rank Z0=7, degree Z0=-14, and every degree is at most-2 by (10). Thus Z0 is pure degree-2. In this case H0(R(2))=2V+2P+D; subtracting P tensor Sym2 and noting H0(V(-2))=0 identifies its coefficient as V+P. We obtain

    Z=(V+P)(-2)+V(-4).                          (12)

Together with O(-10), this is exactly the published complete-Sym6 obstruction, restated in Section7. This exhausts bc.

## 6. The residual P-cubic obstruction

A saturated source P(-2)+T(-3)+O(-10) cannot have saturated derivative image O(-10)+O4. Strict-top forces the top P onto O4 by its nonzero degree6 system. Its kernel is V(-4). The internal target is T(-5)+O(-12), and all Homs from V(-4) vanish by ordinary degree. Thus its saturated rank-one first increment is O6. The quadratic rank4 gap permits b=8 or b<=3, not b=6. Contradiction.

## 7. Published complete-Sym6 obstruction used in (12)

For clarity, the cf Section1.2 argument uses only a saturated source (V+P)(-2)+V(-4)+O(-10) with saturated derivative image O(-10)+O4. Strict-top forces the complete degree6 top system. Its kernel T(-3) has no internal channel to V(-6)+O(-12), so its first span is (Wp+T)(-1), with saturated low quotient O6. Its second span is the actual constant C=Sym8=P+D of rank9.

The quartic tail V(-4) has zero external derivative: V is absent from Sym8, and the negative target is too low. Its internal derivative modulo itself can hit only the top V. Projection modulo C therefore gives a connection-preserved coherent image of V(-4). Such an image is already a constant subbundle. Ranks1 or2 would be trivial representations and are impossible because V is absent from Sym4; rank3 would be a surjective equal-rank map from degree-12 to degree0 and is impossible. Thus the tail lies in C, contradicting rank10 for the disjoint top-plus-tail subbundle inside rank9 C.

This is the published actual-connection lemma, not a claim that an arbitrary source splitting is horizontal.

## Boundary

This proves exactly the two displayed original bb and bc exclusions. It does not by itself assert a whole-label exclusion or update a frontier count. Other original source cuts require their own pinned coverage check. The companion verifier checks only fixed universal characters, Homs, rank/degree deductions, the rank-two kernel alternatives and these two exact catalog entries. These checks do not replace actual saturation, genuine constant projections, exact cohomology sequences or the written connection proof.

No selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance rank tests, experiments, scans or large computation are used. This is written mathematics, not formal proof certification.
