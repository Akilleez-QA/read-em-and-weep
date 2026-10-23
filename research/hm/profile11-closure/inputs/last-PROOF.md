# Exclusion of the scalar D-source pair 50 by nested images and invariant base divisors

## 1. Statement, dependencies, and scope

Work over C with G=SL2(F5), physical doublet W, and the actual saturated inclusion E into H O, dim H=30. Assume maximal Gauss-rank-three profile (1,1), actual source

    E=D O(-2)+(W'+T) O(-3)+V O(-4)+O(-8),

and actual quotients

    A=O(-8)+O(2)+O(4), B=O(6)+O(-4)+O(-6).

We prove this ordered pair, original record 50, impossible. Put S=E-perp in H* O and L=S^-. Then S has rank13, degree -54, H0(S)=0, and L has rank10, degree -50, with derivative rank at most2. These are imported actual geometric hypotheses, not inferences from a finite enumeration. The proof concerns this single ordered pair only. It does not claim a complete repair or any unproved profile coverage.

The retained inputs contain the actual splitting/spanning and strict-top statements, PR1145's full partial-apolar and constant-splitting argument, PR1147's sextic-net theorem, and PR1151's coefficient-span identity. The finite-jet lemma is pinned at PR1163, commit 2cc35efc270f6105c1aa4f2d0bf99c1bbc4af867. Its needed consequence is S_8=0 for this source: each polynomial source generator has degree at most8, and its derivatives through8 span its constant coefficient image; repeated differentiation of the annihilation pairings identifies S_8 with the constant annihilator of E. Since E spans H, that annihilator is zero. Thus the argument does not assume any full coefficient system prematurely. The frontier note was read as context, but no frontier-count conclusion is imported.

All equivariant line bundles have the standard linearization, since G has no characters. The center acts trivially on B. Nonzero invariant binary forms of degree less than12 are constants; in degree12 the invariant space is one-dimensional, spanned by a nonzero form F12. The former also follows from the minimum A5 orbit size12. The exact character source checks these facts and that Sym6=V+P, Sym8=P+D, and Sym18 contains V with multiplicity one.

## 2. Actual nested image sheaves

Define F_0=S, F_1=L, F_(j+1)=F_j^- and G_j=F_j/F_(j+1), with G_0=B. Each F_j is saturated in the same constant ambient. The actual connection induces injective sheaf maps

    G_j -> G_(j-1)(-2) -> B(-2j).

Their ranks q_j are nonincreasing and at most2 for j>=1. No nonzero negative saturated bundle is horizontal in characteristic zero, so all q_j before termination are positive. Their sum is10. Write h for the last nonzero index, so q_j=2 for j<=10-h and q_j=1 thereafter. Initially 5<=h<=10; the jet bound reduces this to h=5,6,7.

Crucially define I_j to be the actual image of G_j(2j) in B under the composite injection. Then I_j is isomorphic to G_j(2j), is locally free, and

    I_(j+1) is a subsheaf of I_j.

This is nesting of coherent images, not an assertion of saturation. On any equal-rank stretch their generic subspace is the same. Their determinants differ by effective divisors on that stretch, so their degrees cannot increase. The divisors are invariant. In particular a positive determinant deficit cannot disappear before the rank drops.

Let delta_j denote the deficit from the highest determinant degree of B at rank q_j. Since the ordinary degrees of B are 6,-4,-6, the top degrees are6 for rank1 and2 for rank2. Degree addition gives

    sum delta_j=capacity(h)-deg L,
    capacity(5)=-50, capacity(6)=-42, capacity(7)=-38.

An equivariant determinant map from a line of degree 2-delta into wedge2 B, whose line degrees are2,0,-10, can be nonzero only if one of delta, delta-2, delta-12 is an invariant degree. Similarly rank1 has possible invariant degrees delta,delta-10,delta-12. Within the present budget12 the allowed deficits are therefore

    rank2: 0,2,12; rank1: 0,10,12.

Deficit0 at rank2 identifies the exact image with the constant top plane O6+O(-4); deficit2 identifies it with O6+O(-6). Indeed only the relevant constant Pluecker component survives, and the determinant then has no zero. Deficit0 at rank1 identifies the exact image with O6; deficit10 identifies it with O(-4). These statements use the actual composite image. A deficit12 image need not be saturated or a constant-plane image and is never assumed so.

## 3. Heights five and six

For h=5 all five quotients have rank2 and all deficits vanish. Hence F5=G5 is O(-4)+O(-14). But strict-top applied five times to S, whose top is at most -1, gives top(F5)<=-6. This contradiction excludes h=5.

For h=6 the total deficit is8. There are four rank2 and two rank1 quotients. The allowed deficits force all four rank2 deficits to be2 and both rank1 deficits to be0. Thus the terminal saturated line F6 is O(-6). Its first six actual derivatives lie in S. On an affine chart its frame is a vector polynomial of degree at most6, and Taylor inversion expresses every coefficient vector as a regular combination of these derivatives. Consequently S contains a nonzero constant coefficient vector on that chart, hence globally by saturation. This contradicts H0(S)=0. Completeness of the degree-six coefficient system is not needed.

## 4. Height seven: two locations for the unique defect

Now the total deficit is12, with three rank2 and four rank1 quotients. The only raw possibilities are a single12, or one rank2 deficit2 together with one rank1 deficit10. In the latter case the rank2 stretch has one exact constant plane O6+O(-6) and two exact constant planes O6+O(-4). Nesting of same-rank generic images forbids this. Thus there is exactly one deficit12.

Within either equal-rank stretch, the determinant degree is nonincreasing by Section2. If the unique deficit12 were followed by a zero deficit of the same rank, its degree would increase, impossible. Thus the only positions are j=3, the last rank2 image, or j=7, the last rank1 image. In the first case all rank1 images are exactly O6 and F7=O(-8). In the second case I1,I2,I3 are the top plane, I4,I5,I6 are O6, and F7=O(-20). This classification includes torsion in the composite images; it does not replace them by their saturations.

## 5. Partial apolarity and a common-factor obstruction

We record the precise mechanism used twice below. Let C=O(-n) be an actual saturated line in a constant H* O, with coefficient quotient q:Sym^n W -> R subset H*. Let a saturated F subset H O span H and annihilate C and its derivatives through k. Dualizing q embeds R* into (Sym^n W)*. The projection of F to R*, followed by this injection, annihilates the universal osculating fiber l^(n-k) Sym^k W. Under the fixed invariant apolarity its annihilator is

    l^(k+1) Sym^(n-k-1) W,

so the actual morphism factors through Sym^(n-k-1) W O(-k-1). This holds for partial q and does not require independence of those derivatives. Generic containment extends globally as vanishing of a bundle morphism.

If this factor map has fixed active coefficient subspace U in Sym^(n-k-1), then its fibers in the full polynomial space are l^(k+1) U. Since F spans H and the constant projection H -> R* is onto, the exact identity is

    R*=span_l l^(k+1) U,

not merely containment. If this subspace consists of forms with a common nonconstant homogeneous factor f, then C cannot be saturated. Indeed for every functional a on R, the scalar coordinate a(q(l^n)) is the evaluation of q*(a) on l^n. Under determinant self-duality this is, up to the fixed nonzero normalization, apolar evaluation of the corresponding polynomial at l. Thus every coordinate vanishes wherever f does (equivalently at the determinant-identified point). The fiber map C -> H* O is zero there, contradicting that a saturated line subbundle has injective fibers. This evaluation argument is invariant under the fixed dual convention; no basis or selected parameter is computed.

## 6. The final-step defect is impossible

If the unique deficit12 occurs at j7, take C=F7=O(-20). Its derivatives through7 lie in S. Section5 factors the projection of E through Sym12 W O(-8). By degree all source blocks except O(-8) map to zero. The latter maps into the unique invariant line C F12. Its scalar must be nonzero: otherwise R would be a nonzero constant subspace of S. Exact coefficient-span equality gives

    R*=span_l l^8 F12=F12 Sym8 W.

Every form has the common factor F12. Section5 contradicts saturation of C. This closes the j7 branch.

## 7. The rank-drop defect gives a genuine constant splitting

Suppose the defect occurs at j3. The terminal line is C=F7=O(-8). Its first seven derivatives lie in S, and the intermediate leading classes are nonzero: the composite injections G7 -> G_(7-k)(-2k) are injective, so the leading class of the kth derivative cannot vanish generically. By induction these derivatives give eight generically independent directions. Consequently the coefficient image of Sym8 W has dimension at least8. Since Sym8=P+D, any proper equivariant quotient has dimension at most5. The coefficient map is therefore injective, with constant image U9.

The universal seventh osculating bundle Sym7 W O(-1) lies in S inside U9 O. Its annihilator is the complete degree-eight line J0=O(-8) in U9* O. Only the O(-8) source block of E maps to it, by a nonzero scalar. Choose an equivariant bundle split E=F+J with J=O(-8) and

    F=D O(-2)+(W'+T) O(-3)+V O(-4).

The actual embedded F lies in the constant N=ker(H -> U9*) of dimension21. The actual coefficient map of J onto U9* is an isomorphism, so its coefficient image C9 in H is a constant complement to N. Hence H=N direct-sum C9 and E=F direct-sum J as embedded bundles. This is the actual constant-splitting argument, not a horizontal Birkhoff assumption. F is saturated, spans N, has rank16 and degree -46.

Derivatives are block diagonal. The complete line J has S_J=Sym7 W O(-1), L_J=Sym6 W O(-2), B_J=O6, and derivative rank of L_J equal1. Thus the actual residual data are

    rank S_F=5, degree S_F=-46,
    rank L_F=3, degree L_F=-36,
    B_F=O(-4)+O(-6), rank beta_(L_F)<=1.

Cancellation is justified by the actual constant direct sum and uniqueness of bundle splitting. No property of the j3 torsion image is needed beyond what forced the complete terminal line.

## 8. Saturate the residual common line, not each image

The negative residual endpoint has a three-step rank-one quotient chain: M0=S_F, M1=L_F, M2=M1^-, M3=M2^-, M4=0, with successive quotient lines T_j=M_j/M_(j+1), j=1,2,3. Their untwisted actual images in B_F are nested rank-one sheaves with the same generic line. Let J'=O(e) be its saturation in B_F. This is an equivariant line subbundle; its center parity is even and e<=-4.

Each T_j injects into J'(-2j), so degree L_F<=3e-12. Since degree L_F=-36, e>=-8. Thus e=-8,-6,-4. For e=-8 both components of a map to B_F would be invariant forms of degrees4 and2, which do not exist. For e=-6 only the bottom constant component exists; for e=-4 only the top constant component exists. This exhausts all generic rational lines, including possible mixed ones.

Write the actual image T_j(2j)=J'(-D_j) for effective invariant divisors D_j. Nesting gives D1<=D2<=D3. Degree addition gives

    sum degree D_j=3e+24.

For e=-6 this sum is6, impossible since every nonempty invariant divisor has degree at least12. For e=-4 it is12, so nesting forces D1=D2=0 and degree D3=12. Therefore the terminal actual saturated line is

    M3=O(-22).

Its derivatives through3 lie in S_F. This distinguishes its saturation in the original constant ambient from the torsion-bearing composite image in B_F.

## 9. The residual invariant factor is impossible

Apply Section5 to M3, F, n=22 and k=3. Projection factors through Sym18 W O(-4). The higher source blocks have no maps to it by degree; the V O(-4) block maps by a scalar into the unique V summand of Sym18. The scalar is nonzero, else a nonzero constant subspace lies in S_F. The unique V in Sym18 is precisely F12 times the V in Sym6: polynomial multiplication by the nonzero invariant F12 is injective, and multiplicity one identifies its image.

The sextic net theorem gives V Sym4 W=Sym10 W. For completeness, the V sextic net is basepoint-free since a common divisor would be invariant of degree at most6, whereas invariant divisors have minimum12. Its rank-two evaluation kernel has negative splitting O(-a)+O(-b), a+b=6, a,b>=1; hence a,b<=5. Twisting by4 kills H1 and proves the stated surjectivity. Therefore exact coefficient-span equality yields

    R*=span_l l^4 F12 V=F12 Sym10 W.

This has a nonconstant common factor, contradicting saturation of M3. The j3 branch is impossible. All possible heights and defect locations have now been excluded, proving the stated pair50 exclusion.

## 10. Evidence boundary

The verifier authenticates retained bytes and checks universal character multiplicities, capacity arithmetic, every finite deficit allocation and its equal-rank persistence filters, the residual saturated-line degree possibilities, source block Hom-degree vanishings, and exact formal pure-power/evaluation identities. It uses no selected actual HM coefficients, points, source parameters, instance matrices, numerical rank tests, or stopped experiment. These tests support the written proof; they are not proof-assistant verification. All eight retained source files have immutable public pins, freshly checked against their Git blob identities before freezing this packet.
