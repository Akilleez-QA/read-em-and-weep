# A rank-two Ext bound and an honest-descent restriction

## Proposition
Let X be a complex abelian fourfold and E a simple rank-two vector bundle such that c1(E)=0 in rational cohomology and integral_X c2(E)^2>0. Then

- chi(E) is a positive even integer;
- ext1(E,E)>=8;
- ext2(E,E)=16 chi(E)-2+2 ext1(E,E)>=46.

In particular, the full semiregularity map and the surjectivity condition for HH² evaluation cannot hold: both relevant comparison spaces have dimension 28. This is not a nonexistence result, an actual ambient obstruction, or a failure of the weak image-restricted criterion.

## Proof of parity
Integral cohomology of an abelian variety is torsion-free. Thus det E belongs to Pic0(X). Multiplication by2 on Pic0 is surjective; choose L with L²=(det E)^(-1). The bundle F=E tensor L has determinant O and the same rational Chern character as E.

The perfect alternating wedge pairing F tensor F -> O, combined with Serre duality and a trivialization of the canonical bundle, gives a perfect alternating pairing on H²(X,F). The cohomological interchange sign is (-1)^(2*2)=+1, while interchanging the coefficient vectors contributes -1. Hence h²(F) is even. Self-duality gives h4=h0 and h3=h1, so chi(E)=chi(F)=2h0-2h1+h2 is even.

The rank-two Chern character and Td(X)=1 give

  ch(E)=2-c2(E)+c2(E)^2/12,
  chi(E)=integral_X c2(E)^2/12>0.

Therefore chi(E)>=2.

## Eight independent first-order directions
The Picard twists give four directions in Ext1(E,E): the scalar inclusion splits by one half the trace, and their traces are 2lambda, lambda in H1(O_X).

Translations give another four, via v -> v contraction At(E), for v in H0(T_X). Suppose the image is zero. Naturality of the trace powers of the Atiyah class implies v contraction c2(E)=0, and hence v contraction c2(E)^2=0. A nonzero top-degree cohomology class on an abelian fourfold has no nonzero holomorphic translation annihilator. Indeed it is a nonzero multiple of a volume form in the exterior algebra, and contraction on that line is injective in the vector argument. Thus the translation map is injective.

Their traces vanish because trace At(E)=c1(E)=0 in H1(Omega1_X). Hence the translation and Picard subspaces are disjoint, proving ext1>=8. This sharpening was identified by null in the mathematical coordination discussion.

## Euler characteristic of End(E)
The dual E* has the same Chern character under the hypotheses, so

  ch(End E)=4-4c2(E)+(4/3)c2(E)^2,
  chi(End E)=16chi(E).

Simplicity and Serre duality imply ext0=ext4=1 and ext3=ext1. Therefore

  ext2=16chi(E)-2+2ext1>=32-2+16=46.

The semiregularity target is direct_sum_(q=0)^2 H^{q,q+2}(X), of dimension6+16+6=28. The HKR decomposition of HH²(X) has the same dimension. The two stated dimension exclusions follow.

## Principal-polarization specialization
If theta is principal and c2(E)=d theta² with d>0 rational, then d is an integer. The class theta²/2 is primitive integral: in a symplectic integral basis it is the sum of six different basis monomials with coefficient1. Thus k=2d is integral. Since integral theta4=24, chi(E)=2d²=k²/2 is integral, forcing k even.

Consequently

  ext2=32d²-2+2ext1>=32d²+14.

For d=15 and ext1=87 the identity yields ext2=7372. This is a consistency check against the HM calculation, not an independent certification of its ranks. For the Lange d=8 seed it gives ext2>=2062.

## Honest isogeny descent
Suppose q:X->Y is an isogeny of degree g and E=q*G for an honest rank-two vector bundle G. Pullback is injective on Hom, so G is simple. It is injective on rational cohomology, so c1(G)=0, and integral_X c2(E)^2=g integral_Y c2(G)^2 makes the latter positive. The preceding proposition applies to G as well, independent of its polarization type.

Furthermore chi(E)=g chi(G), with chi(G) positive and even. Hence g divides chi(E)/2. For an HM seed with chi(E)=450, this requires g|225. For the Lange m=2 seed with chi(E)=128, it requires g|64. Neither divisibility condition proves the corresponding descent exists.

Projectively equivariant or twisted descent is outside this assertion, as are higher-rank objects and complexes. Failure of full semiregularity does not imply a nonzero ambient obstruction.

## Sources and scope
- [Stacks Project, Riemann–Roch](https://stacks.math.columbia.edu/tag/02UO).
- [Stacks Project, Serre duality](https://stacks.math.columbia.edu/tag/0FW0).
- [Milne, Abelian Varieties, I.11–12](https://www.jmilne.org/math/CourseNotes/AV.pdf).
- [Markman v2, Lemma11.3 and Question11.4](https://arxiv.org/html/2509.23403v2), for the distinction between full semiregularity and the weak image condition.
- [Translation sharpening in the coordination discussion](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6093720840).

The displayed proposition is a direct argument from these foundations. No novelty claim or proof-assistant verification is made. The earlier Ext2>=38 bound used only Picard directions; it remains true but is superseded here by >=46.
