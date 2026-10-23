# A horizontal scalar-line obstruction excludes both two-D sources at index127

## Result and scope

For the original zero-defect label

    G3.11.cce6e3ba4eeb (source_index127),
    A_q=O(-8)+O(2)+O(16), B_q=O(-18)+O(-4)+O(6),

the following two entire source edges are impossible:

    (0,0,0,0,0,2,0,1): E=(P+2D) O(-2)+2 O(-8)+O(-10);
    (0,0,0,0,0,1,1,0): E=(P+2D) O(-2)+O(-8)+W O(-9).

The second statement covers both the scalar-nonzero and Euler-only negative-endpoint branches. In particular, the surviving O(-10) internal derivative channel in the Euler-only kernel is not discarded or assumed zero. The new step uses a different scalar O(-8) subline, whose external derivative is actually zero, and proves that it cannot coexist with the forced constant seven-space.

These are two source-edge exclusions, not a whole-label exclusion. No source113 exclusion or new pair/label count is claimed. The six different edges in PR846 are unchanged. This is a written mathematical proof, not Lean certification. No selected actual HM/source coefficients, parameters, points, derivative values, matrices, source-instance ranks, selected models, scans, or unapproved large computation are used. The optional checks involve only fixed abstract representation identities and original-catalog reads.

## 1. Immutable inputs and actual-sheaf conventions

The original inputs are at commit db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact files and Git blobs are:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3.
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: d7506dae49b4be43230450c4132bd5db91f137ef.
- one-one-endpoint-necessary-pairs.json: fe0afa410d89340d3082dc814277f89fbb582c19.
- rank-three-quotient-frontier-144.json: 8b5971092f9ef762584912609fd5e9301c4e271d.

The complete source_index127 list is

    (0,0,0,0,0,2,0,1), (0,0,0,0,1,1,0,1),
    (0,0,1,0,0,1,0,1), (0,1,0,0,0,1,0,1),
    (0,0,0,0,0,1,1,0), (0,0,0,0,1,0,1,0),
    (0,0,1,0,0,0,1,0), (0,1,0,0,0,0,1,0),
    (0,0,1,1,0,1,0,0), (1,0,1,0,0,2,0,0),
    (1,0,1,0,1,1,0,0), (1,0,2,0,0,1,0,0),
    (1,1,1,0,0,1,0,0).

The decoder is

    E=((c+g+h-1)V+(d+e+g+h)P+(f+g)D) O(-2)
      +(a Wp+b T) O(-3)+(c V+d P) O(-4)
      +e Wp O(-5)+f O(-8)+g W O(-9)+h O(-10).

The two displayed edges are members of this necessary overlist; no realizability is assumed.

We use three published interfaces:

1. PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac, Section3: the actual saturated internal/external derivative-image lemma. If a subbundle F of an actual E has saturated external derivative image U and saturated internal image J from the kernel of F->U into (E/F)(-2), then its full raw derivative image I is saturated and fits 0->J->I->U->0; consequently F^+/F=I(2).

   https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

2. PR802, commit e484640a6565c278321bf6557860262c1ac1b7df, Sections3 and5: the complete P+D degree-eighteen line-system kernels and the three-channel polar obstruction when their internal image is a saturated O(-10). The hypotheses are checked below; no whole-label conclusion of PR802 is imported.

   https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

3. PR828, commit ae077cbe42d65cde27d65ce88923dc35851b6952, Section1: a coherent lattice preserved by a trivial connection equals its constant saturation. The elementary local argument is recalled in Section4.

   https://github.com/Akilleez-QA/read-em-and-weep/blob/ae077cbe42d65cde27d65ce88923dc35851b6952/research/hm/profile11-horizontal-quotient-exclusion/HORIZONTAL-CONSTANT-QUOTIENT-EXCLUSION.md

Work over C with the binary icosahedral group G. W is its defining two-space, Wp the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P its remaining even irreducibles of dimensions3,4. All are self-dual. G is perfect, so equivariant line bundles have their standard linearizations without extra one-dimensional character twists.

The actual E is saturated in H O, rank17 and degree-54, with H0(E(1))=0 and H0(E^-(2))=0. Its derivative quotient A_q is a saturated subbundle of (H O/E)(-2), by the original determinant defect zero. Thus its raw derivative is saturated and E^+/E=A_q(2). Every derivative and constant projection below uses this actual trivial connection, not a connection chosen on an abstract bundle splitting.

## 2. The common high-line reduction

Strict-top injects the quadratic coefficient P+2D into

    H0(O(4)+O(18))=A+V+2P+2D.

Both D multiplicity spaces have dimension two, so the induced multiplicity map is an isomorphism. Its O(2)-row kernel is one D multiplicity line. Together with P, which has no O(2) component, it defines a saturated actual subbundle

    F=(P+D) O(-2)

mapping only to O(16). Its nine independent degree-eighteen sections have no common divisor: any nonempty G-invariant divisor has degree at least12 and would leave at most seven independent sections. Thus F->O(16) is onto everywhere. A complementary D maps nontrivially to O(2).

PR802 Section3 gives precisely the following possible kernels K0 of this onto map:

    (V+P) O(-4)+O(-6);
    Wp O(-3)+V O(-4)+Wp O(-5)+O(-6);
    T O(-3)+O(-6)+O(-10).                         (1)

The actual internal target is respectively

    (E/F)(-2)=D O(-4)+2 O(-10)+O(-12),
    (E/F)(-2)=D O(-4)+O(-10)+W O(-11).            (2)

The components into D O(-4) vanish: V and P are inequivalent to D, Wp is absent from D W=S+T, and D is absent from Sym2 W and Sym6 W. All other components vanish by degrees except the O(-10) in the last kernel mapping by a constant scalar row into the O(-10) summands of (2). Hence J is either zero or a saturated O(-10). A nonzero constant row is an everywhere-injective subbundle, so no torsion correction is suppressed.

In the nonzero case the actual-image lemma and first-polar generation force

    F^+=A O+(Wp+T) O(-1).

These are exactly the interfaces of PR802 Section5: the canonical constant A, the saturated projected linear bundle (Wp+T) O(-1), and only the channels P->Wp, P->T, D->T. Its universal polar contradiction does not depend on where the internal O(-10) landed in E/F. In brief, the P->Wp Euler channel and D->T multiplication channel must both be nonzero. If the P->T channel is zero, a full Wp O(-1) lies in the projected F, forcing its nonzero constant span into a negative pure-linear bundle. If it is nonzero, the induced Wp O(-3)->O(4) is nonzero and onto, since its invariant common divisor would have degree at most7<12. Then the projected F is the full linear bundle, forcing that negative bundle to be horizontal. Both are impossible. Thus J=0.

The actual-image sequences now give

    F^+=C0 O, C0=A+V+P, dim C0=10,
    C0 O/F=O(18).

Indeed rank F^+=10 and degree0, so its saturation in a constant bundle makes it constant. Its image in E^+/E is exactly the saturated O(18) summand. Consequently E intersect C0 O=F and E+C0 O is saturated. Constant projection gives an actual saturated bundle Z in (H/C0) O:

    Z=D O(-2)+2 O(-8)+O(-10),                    (3a)
    Z=D O(-2)+O(-8)+W O(-9),                    (3b)

respectively. Its actual Gauss quotient is exactly O(2)+O(-8), with saturated raw image: projecting the actual raw derivative E^+ by the constant C0 removes precisely the O(18) quotient. This proves the needed reduction independently of any unpublished source exclusion.

## 3. The residual D block and its genuine constant seven-space

Let D0=D O(-2) be the top subbundle of either Z. Its negative quotient component is zero by degree. Its O(2) component is nonzero by the multiplicity construction, hence is the complete quartic evaluation system, with exact kernel S O(-3).

The internal derivative of S O(-3) into (Z/D0)(-2) vanishes by degree: the latter has degrees at most-10 in both (3a),(3b). The external O(2) is saturated. Therefore the actual-image lemma gives the saturated raw first span M=D0^+ and exact sequence

    0 -> D O(-2) -> M -> O(4) ->0.               (4)

First-polar generation shows that M(1) is globally generated, while M lies in a constant bundle; its splitting degrees are0 or-1. Equation(4) gives rank6 and degree-6, so every degree is-1. Twisting (4) by one gives H0(M(1))=Sym5 W=T, hence

    M=T O(-1).

The derivative of M kills D0 and therefore has rank at most one. It is not zero, because a negative saturated subbundle of a constant bundle is not horizontal. The first forward span of a pure-linear embedded bundle is its full constant coefficient span. Thus this actual span is a seven-dimensional constant subspace C1 and

    M subset C1 O,
    C1 O/M=O(6).                                 (5)

The quotient is locally free because M is saturated in the ambient constant bundle. Taking global sections in (5) identifies C1=Sym6 W=V+P. In particular both the constant inclusion and the equivariant O(6) quotient are actual objects for the projected connection.

## 4. A forbidden scalar line with zero external derivative

We prove the following lemma in the setting of Sections2-3. Suppose L=O(-8) is an actual subbundle, independent of D0, such that D0+L is a direct summand of Z and

    beta_Z(L)=0,
    beta_L(L) subset (D0+L)/L tensor O(-2).      (6)

Then such an L cannot exist.

Project L by the constant map from the ambient bundle to its quotient by C1 O. Write N for the image sheaf. It has rank zero or one and may a priori be unsaturated. Equation(6), together with D0 subset C1 O, shows that

    dN subset N tensor Omega^1.                 (7)

To justify this for the actual image sheaf, locally lift any section of N to L and differentiate it. Its derivative lies in (D0+L) tensor Omega^1; constant projection kills D0 and commutes with differentiation. A different lift changes nothing in the projected derivative. No saturation assumption on N is made.

If N has rank one, the nonzero map L->N is injective as a map of torsion-free rank-one sheaves, so N is isomorphic to O(-8). Its generic line is horizontal by (7), and hence its saturation is a constant line in characteristic zero. In that constant line a local lattice has the form t^m O. Preservation would require m t^(m-1)dt to lie in t^m O dt; this forces m=0 at every point. Thus N equals a constant line and has degree0, contradicting degree-8. Therefore N=0, so

    L subset C1 O.

Now the composite L->C1 O/M=O(6) is equivariant and belongs to

    H0(O(14))^G=(Sym14 W)^G=0.                   (8)

For example Sym14 W=A+V+P+D has no trivial constituent. Therefore L subset M. Together with D0 subset M, this gives D0+L subset M. The left side is a saturated rank-six subbundle of the ambient constant bundle: it is a direct summand of the saturated Z. The right side also has rank six. Its quotient by D0+L is thus a torsion subsheaf of the locally free ambient quotient by D0+L and must vanish. Hence D0+L=M, impossible because

    deg(D0+L)=-18,    deg M=-6.                  (9)

This proves the scalar-line obstruction. It depends on the zero external derivative in (6), not merely a vanishing component at one endpoint.

## 5. Exclude the entire h-f-f source

For (3a), the map 2 O(-8)->O(-8) is a constant scalar row. Choose a one-dimensional kernel in its two-dimensional multiplicity space, and let L=O(-8) be the resulting direct summand. This remains possible if the row is zero. There is no map O(-10)->O(-8) equivariantly, since (Sym2 W)^G=0, but the choice of L does not require this additional fact.

The other external component of L is also zero:

    Hom_G(O(-8),O(2))=(Sym10 W)^G=0,
    Sym10 W=A+V+D.                              (10)

Thus beta_Z(L)=0. The internal second fundamental form of L has target

    (Z/L)(-2)=D O(-4)+O(-10)+O(-12).

By degrees only its D O(-4) component can be nonzero. This is exactly (6). Section4 excludes L and hence excludes the whole source (0,0,0,0,0,2,0,1), without making any assertion that the O(-10) channel of the full negative-endpoint kernel vanishes.

## 6. Exclude both branches of the g-f source

For (3b), write L=O(-8). Its negative-endpoint component is a scalar lambda. The W O(-9) component is a scalar multiple of the Euler map W O(-9)->O(-8); these exhaust the possible negative components.

### 6.1 Euler-only branch: lambda=0

The map Z->O(-8) is onto, so the Euler component is nonzero. Equation(10) kills the other external component of L, hence beta_Z(L)=0. Its internal target is

    (Z/L)(-2)=D O(-4)+W O(-11).

Only the D component is possible by degrees, so the scalar-line obstruction of Section4 applies. This excludes the Euler-only branch.

The kernel of the Euler endpoint really does contain an O(-10) summand, and its derivative can have a scalar component to (Z/Z')(-2)=O(-10), where Z'=ker(Z->O(-8)). Nothing above removes that channel. The proof uses L, which is a different O(-8) subbundle, and therefore does not import a scalar-endpoint argument into this branch.

### 6.2 Scalar-nonzero branch: lambda is nonzero

Set Z'=ker(Z->O(-8)). Solving for the scalar L component gives a bundle graph

    Z'=D O(-2)+W O(-9), rank7, degree-28.         (11)

It is saturated because the endpoint map is onto. Let K=Z^-. Since D0 maps onto O(2), the complete kernel has exact sequence

    0 -> S O(-3) -> K -> W O(-9) ->0.

It splits equivariantly: the ordinary extension group vanishes by H1(O(6))=0, and averaging preserves the splitting. Thus every degree of K is at least-9, and Hom(K,O(-10))=0. The derivatives of K lie in Z, and their possible internal component outside Z' is precisely the latter zero Hom space.

The external image of Z' is the full saturated O(2), supplied by D0. Applying the actual-image lemma yields

    G0=(Z')^+=Z'+M,
    G0/Z'=O(4), rank G0=8, degree G0=-24.         (12)

These are exact actual sheaves and a saturated raw image, with no unspecified modification. Equality G0=Z'+M holds because D0 already supplies the entire external image.

The coherent sum S0=Z'+C1 O is preserved by differentiation: derivatives of Z' lie in Z'+M and C1 is constant. Its saturation is constant, and the lattice argument of Section4 forces S0 itself to equal that saturation. Because C1 O/M has rank one and G0=Z'+M, the rank of S0 is eight or nine. Rank eight would force equality with the saturated G0 and would contradict its negative degree. Hence S0 has rank nine, and S0/G0 is a line bundle of degree24. The sum identity provides an onto map

    O(6)=C1 O/M -> S0/G0=O(24).                  (13)

An onto map between line bundles is an isomorphism, impossible for these degrees. This excludes the scalar-nonzero branch and completes the second entire source-edge exclusion.

## Boundary and verification

The proof exhausts all negative-endpoint alternatives for the two stated sources. It does not exclude any other source or a whole stable label, and does not close source2 or the global rank goal. The new root-cause lemma is Section4: a negative scalar line whose derivative is trapped modulo a forced constant subsystem cannot have a nonzero horizontal projected lattice; the invariant-free O(6) quotient then makes it exceed the saturated first polar space.

The exact-version independent review and bounded abstract verifier accompany this proof. The verifier checks representation identities, all stated kernel-to-target Hom channels, the two exact source identities and rank/degree arithmetic. It does not purport to prove the connection, saturation, or preserved-lattice arguments; those are the mathematical arguments above.
