# Sectional genera and conductor loss of the degree-thirty Chow hypersurface

## Established input, distinct from the primary degree-fifteen surface

Let S=S(5), let V be the canonical modular ruling bundle, and put P=P_S(V), in the quotient convention. Write ξ for its tautological class, I and F for the pulled-back modular classes, and h=ξ+I. The checked bundle identities are

I²=−5, IF=5, F²=0, det V=I+3F, c2(V)=10,
K_P=−2ξ+I+6F, h³=30.

The source for these identities is MODULAR-RULING-BUNDLE.md at5967472ac1a9afe35628dac672fc88321b429110 and the primary ADHPR dictionary at commit 38c517ed358c08d776b59ab5def5856106dcdeb5.

The fixed-coordinate ruling map φ:P→P4 is a morphism, its reduced image Z is an integral degree-thirty hypersurface, and φ:P→Z is birational. The reduced degree and birational image theorem is now established in SEVENTY-FIVE-SIMPLE-BASEPOINTS.md at commit f23af60ad65fe0677f9c747d84a3165b7e6466ff, read at its immutable source. Its degree-one-hundred kernel-map input is pinned at 2f6995ac73c9b34a08808befb1f4a542abc2d81c. The cube h³=30 alone would not establish these assertions. The polarization is φ*O(1)=O_P(h).

Z is the three-dimensional Chow hypersurface in the fixed-coordinate projective space. None of the conductor numbers below is a conductor number of the primary degree-fifteen surface S15.

## 1. General target surface sections avoid every positive-dimensional fiber

For a proper birational morphism from an integral threefold, the closed subset B of the target over which a fiber has positive dimension has dimension at most one. Otherwise its inverse image would have dimension at least three while being a proper closed subset of the integral threefold. This argument does not classify the exceptional locus.

A general plane Π⊂P4 avoids B, since dim Π+dim B<4. Likewise a general hyperplane H0 meets B in finitely many points, and a general quadric Q avoids those points; hence H0∩Q avoids B. The claim concerns a general pair (H0,Q), equivalently an open set of Q with a general H0 for each Q in that open. It does not assert avoidance for every quadric or hyperplane.

Consequently the restrictions of φ to the pulled-back plane curve and to the pulled-back (quadric,hyperplane) curve are proper and quasi-finite, hence finite. General hyperplane and quadric Bertini, applied successively to their basepoint-free pulled-back systems on smooth P, makes these curves smooth. General sections of the integral target Z are integral; birationality makes the corresponding pullback curves integral and birational to them. Thus these finite maps are the actual normalizations of the target section curves.

This handles the images of the twenty-five known contracted torsion ruled surfaces, namely the HM lines, and any further contracted loci simultaneously. By contrast, the pulled-back surface φ*Q itself may retain contracted curves over the finite set B∩Q. It is not thereby proved to be the finite normalization of Z∩Q.

## 2. Intersection calculation

The projective-bundle relations give

ξ²I=(I+3F)I=10,
ξ²F=(I+3F)F=5,
ξ I²=−5,
ξ IF=5.

It follows that h²I=0 and h²F=15. Since K_P=−2h+3I+6F,

K_P h²=−60+0+90=30.

A general plane Π cuts out a normalization curve C~ of class h². Adjunction gives

2g(C~)−2=(K_P+2h)h²=30+60=90,

g(C~)=46.

The target C=Z∩Π is an integral plane curve of degree thirty, so

p_a(C)=(30−1)(30−2)/2=406.

The exact normalization sequence

0→O_C→ν_*O_C~→Q_C→0

therefore gives

length(Q_C)=406−46=360.

This is the total delta invariant, with no assumption of nodes, transverse double branches, or any particular local singularity type.

## 3. Quadric-hyperplane sectional calculation

A general quadric Q and hyperplane H0 cut a normalization curve D~ of class (2h)h. Adjunction gives

2g(D~)−2=(K_P+3h)(2h²)=2(30+90)=240,

g(D~)=121.

The target D=Z∩Q∩H0 is the complete-intersection curve of degrees (2,30) in H0≅P3. Its arithmetic genus is

p_a(D)=1+(2·30)(2+30−4)/2=841.

Hence its normalization quotient has length

length(ν_*O_D~/O_D)=841−121=720.

Again this is a total conductor loss, not a count of distinct singular points.

## 4. Canonical conductor degrees on the curves

Both target curves are Gorenstein complete intersections. For the normalization of an integral Gorenstein curve, the conductor ideal on the smooth normalization is O(−Δ), and

ω_normalization = ν*ω_target ⊗ O(−Δ).

Thus Δ has degree twice the total delta invariant. In the plane case ν*ω_C has degree 30·27=810, whereas deg ω_C~=90; consequently deg Δ=720. In the (2,30) case the corresponding degrees are 60·28=1680 and 240, yielding deg Δ=1440.

The formal ambient canonical discrepancy is

φ*K_Z−K_P=25h−K_P=27h−3I−6F.

Its intersection with h² is 720, and with 2h² is 1440, agreeing with the curve conductor divisors. This agreement does not identify that entire ambient divisor with a global conductor divisor on P: contracted divisors and the nonfinite normalization map require separate treatment. Only its restrictions to the general normalization curves are used here.

## 5. Nonnormality is forced in codimension one

In particular Z is not normal. If it were normal, its singular locus would have dimension at most one. A general plane would avoid that locus and cut the smooth locus transversely, giving a smooth plane curve of genus406, contrary to its computed normalization genus46. Since a hypersurface is Cohen–Macaulay and hence S2, failure of normality forces failure of R1. Thus the nonnormal locus contains a surface. This conclusion does not specify its components or their local conductor multiplicities.

## Boundary

Using the established birational reduced degree-thirty image theorem, the new exact invariants are (section degree, arithmetic genus, normalization genus, total delta)=(30,406,46,360) and (60,841,121,720). They force substantial nonnormal sectional behavior but do not, by themselves, obstruct the existence of Z or close the proof-repair boundary. No coefficient selection, rank experiment, source-app write, or assumption on a local conductor model enters the argument.
