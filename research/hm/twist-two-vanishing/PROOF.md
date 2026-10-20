# The second twisted trace-free HM endomorphism vanishing

## Theorem and dependency

Let F be the normalized Horrocks–Mumford bundle on complex P⁴, and put B=End₀(F). Then

    H⁰(P⁴,B(2))=0,  h¹(P⁴,B(2))=85,
    Hⁱ(P⁴,B(2))=0 for i≥2.

This proof depends on [the twist-one vanishing](../twist-one-vanishing/PROOF.md), H⁰B(1)=0. It is a stacked continuation of [PR #91](https://github.com/Akilleez-QA/read-em-and-weep/pull/91), pinned to [commit ee7c4d4627c2efa07ea167a535cf1582002ef335](https://github.com/Akilleez-QA/read-em-and-weep/commit/ee7c4d4627c2efa07ea167a535cf1582002ef335). That dependency is published for review, not asserted to be merged or independently accepted. All other specialized numerical and symmetry inputs are stated below with primary references.

## 1. Primary inputs and symmetry conventions

Write H=c₁O(1). The normalized bundle has c₁F=−H, c₂F=4H² and F*=F(1). Its section-module resolution sheafifies to

    0→2O(−8)→20O(−6)→35O(−5)
      →15O(−4)⊕4O(−3)→F→0.                    (R)

For provenance of the shifts: Decker, *Monads and cohomology modules of rank 2 vector bundles*, printed pp.14–16, defines the section resolution on p.14, relates its coefficients to the first-cohomology module resolution on p.15, and displays the latter shifts on p.16. Comparison gives (R). [Primary PDF](https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf).

The required cohomology is: H¹F(t) has dimensions 5,10,10,2 in degrees t=0,1,2,3 and is zero otherwise; H²F(t) is zero except at t=−2, where its dimension is 2. Also H⁰F(t)=0 for t<3. These are the HM cohomology calculations in §4, with their bundle normalized by F=F_HM(−3), and the above resolution. Serre duality gives H³F(t)=H¹F(−t−4)* and H⁴F(t)=H⁰F(−t−4)*. [Horrocks–Mumford primary PDF](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf).

Use the classical finite normalizer N=H₅⋊SL₂(F₅)⊂SL₅ acting on P⁴. Its scalar center μ₅ acts trivially on P⁴, on O(a) by ζ^(−a), and on B by the identity. Thus its action on B(2) is ζ³. Every irreducible H₅ representation with a fixed nontrivial central character has dimension 5 (HM §2, the isotypic equivalence (2.2)). Only this numerical representation fact is needed, not a refined label for a five-dimensional summand.

N has no nontrivial characters: [H₅,H₅]=μ₅, the induced SL₂(F₅) action on H₅/μ₅ has no nontrivial invariant character, and SL₂(F₅) is perfect. In particular, comparing linearizations of any fixed line bundle causes no character ambiguity. Finally S₅^N=0: HM Theorem 3.5 decomposes the H₅-invariant quintics as the two nontrivial three-dimensional quotient representations. This is a finite-group assertion, not a continuous SL₂(C) symmetry.

The trace pairing makes B self-dual of rank 3 and determinant trivial, so

    Λ²(B(2))≅B(4),  det(B(2))≅O(6).

Their equivariant versions have no character discrepancy. If α,β are the Chern roots of F, the roots of B are 0,α−β,β−α. Consequently

    ch B=3−15H²+0H³+⋯,
    ch B(2)=3+6H−9H²−26H³+⋯.                  (1)

The twist-one dependency, followed by multiplication by a nonzero polynomial of degree 1−t, gives H⁰B(t)=0 for all t≤1.

## 2. A numerical zero-or-five reduction and the other cohomology groups

Tensor (R) by the locally free F*(2)=F(3). Place the resulting resolution of End(F)(2) in cochain columns p=−3,…,0:

    E⁻³=2F(−5), E⁻²=20F(−3), E⁻¹=35F(−2),
    E⁰=15F(−1)⊕4F.

The spectral sequence E₁^{p,q}=H^q(E^p) converges to H^{p+q}(End(F)(2)). Its only nonzero entries are

    (p,q)=(−3,3): dimension 20;
    (p,q)=(−1,2): dimension 70;
    (p,q)=( 0,1): dimension 20.

Indeed F(−3) and F(−1) are acyclic, H³F(−5)=H¹F(1)* has dimension 10, H²F(−2) has dimension 2, and H¹F has dimension 5. All H⁰ and H⁴ entries vanish by the stated section vanishing and duality. The first term is the unique total-degree-zero position and has no incoming differential. Therefore its E∞ subspace is H⁰End(F)(2), of dimension at most 20. The trace splitting End(F)=O⊕B gives

    15+h⁰B(2)≤20.

Since the H₅ center on H⁰B(2) has nontrivial character ζ³, that space has dimension divisible by 5. Hence h⁰B(2)∈{0,5}. This does not require identifying either possible outgoing spectral-sequence differential or any refined normalizer representation.

All surviving positions have total degree 0 or 1, so HⁱEnd(F)(2)=0 for i≥2. The alternating sum is 20−70−20=−70. Removing the scalar O(2), whose Euler characteristic is 15 and whose higher cohomology vanishes, gives

    χB(2)=−85,  h¹B(2)=85+h⁰B(2),
    HⁱB(2)=0 for i≥2.

Assume for contradiction the five-dimensional alternative. Set T₀=H⁰B(2), and let e:T₀⊗O→B(2) be canonical evaluation, and let r be its generic rank. We now exclude this alternative using its entire section space, without selecting or evaluating any section.

## 3. Evaluation has generic rank three

It is not rank zero. Suppose r=1 or2. Let I be the saturation of im(e) in B(2). It is equivariant, torsion-free of rankr, and its determinant is O(a) for an integer a. Wedges of the global generating sections of im(e) give a nonzero global section of det I, so a≥0. On the complement of codimension at least2, the inclusion I→B(2) induces a nonzero map

    O(a)→Λ^r B(2).

It extends over P⁴ because the target is locally free. Saturation ensures that the determinant map has no poles at any divisor. The linearization on det I has central character ζ^(3r), since the center acts by ζ³ on B(2). Comparing with O(a) gives

    a≡2r (mod5).                                 (2)

Any possible discrepancy between two linearizations on the same line bundle is a character, trivial on μ₅.

For r=1, the map yields H⁰B(2−a)≠0, forcing a≤0 by H⁰B(t)=0 for t≤1. But a≥0 and a≡2 mod5 are incompatible with a≤0.

For r=2, the map yields H⁰B(4−a)≠0, forcing a≤2. This contradicts a≥0 and a≡4 mod5. Hence r=3. This step needs no tensor-product semistability theorem for B.

## 4. There is no divisorial evaluation defect

Write T=coker e, a torsion sheaf. Since e has full generic rank, its maximal minors are sections of O(6), not all zero. Their common divisorial zero part D is an effective N-invariant divisor of degree d≤6. Equivariance of e makes its determinantal ideal, and hence D, invariant.

An invariant divisor defines an N-stable line in S_d. N has no characters, so this line is trivial. The center then forces5|d. In the range1≤d≤6 the only possibility is d=5, but S₅^N=0 since S₅^{H₅}=χ₃⊕χ₃′ has no trivial quotient-group constituent. Therefore D=0.

Over a divisor's DVR, a map from a free rank5 module to a free rank3 module has nonzero cokernel exactly when all maximal minors are nonunits. Thus absence of D means T has support in codimension at least2, not merely that its reduced support lacks an invariant component.

Let K=ker e. We have an exact sequence

    0→K→5O→B(2)→T→0.                            (3)

K is rank2 and reflexive: its quotient in5O is im e, a torsion-free sheaf, and the depth lemma gives S₂ for K. Since T has no divisorial support, c₁K=−6H. Thus E=K(3) is rank2 reflexive with c₁E=0.

## 5. The normalized kernel is semistable

The center acts on K by ζ³, inherited from T₀⊗O, and therefore acts trivially on E=K(3).

If E were slope-unstable for H=O(1), its unique maximal destabilizing subsheaf would be a saturated rank-one subsheaf L with positive first Chern class. Uniqueness of the Harder–Narasimhan subsheaf makes L equivariant. Because E is reflexive and E/L torsion-free, the depth lemma gives reflexivity of L; hence L=O(a), a>0. The inclusion E→T₀⊗O(3) implies a≤3.

But the center is trivial on E and L, while it acts on O(a) by ζ^(−a). Comparing linearizations gives5|a, again because characters are trivial on μ₅. This contradicts0<a≤3. Therefore E is slope-semistable.

## 6. Bogomolov forces vanishing of the codimension-two defect

Let ch₂T=tH². Since T is supported in codimension at least2, its leading codimension-two Chern-character cycle is its effective support cycle with generic lengths, so t≥0. Equation(3) and (1) give

    ch₁K=−6H,   ch₂K=(9+t)H²,
    ch₂E=ch₂(K(3))=tH².

Since c₁E=0, c₂E=−tH². Bogomolov's inequality for the semistable torsion-free rank2 sheaf E says

    (4c₂E−c₁E²)H²≥0.

Hence −4t≥0, so t=0 and c₁E=c₂E=0. Effectiveness also shows that T is now supported in codimension at least3.

Primary verification of the inequality: A. Langer, On boundedness of semistable sheaves, Documenta Mathematica27(2022),1–16, Theorem3.13, printed p.11, applies to smooth projective varieties over characteristic0 and slope-semistable torsion-free sheaves. Take all nef polarizations equal toH:
https://ems.press/content/serial-article-files/26645

## 7. Equality gives an actual trivial bundle, not merely trivial Chern numbers

We use the explicitly reflexive version of the flatness criterion: for an H-semistable reflexive sheaf on a complex projective manifold, vanishing of c₁H^(n−1),c₁²H^(n−2),c₂H^(n−2) implies it is a numerically flat vector bundle. This includes local freeness across codimension3 and higher.

A verified published statement is Wenhao Ou, Foliations whose first Chern class is nef, J. Eur. Math. Soc., DOI10.4171/JEMS/1426, Theorem3.1, PDF p.5. Its hypotheses apply exactly to E above. The theorem cites Bando–Siu, Corollary3, and Nakayama, TheoremIV.4.1:
https://ems.press/content/serial-article-files/34043?nt=1

The same paper's Theorem3.5 gives a holomorphically compatible flat connection on a numerically flat bundle. Since P⁴ is simply connected, parallel transport supplies a global holomorphic flat frame. Thus E≅O² and

    K≅O(−3)².                                   (4)

Equivalently, one can use the filtration by unitary flat bundles: on simply connected P⁴ these factors are trivial, and H¹O=0 splits their successive extensions. No assertion that an arbitrary torsion-free sheaf with zero c₁,c₂ is locally free is being used; reflexivity is essential and was proved above.

## 8. The codimension-three Chern character is negative

From(3),(4),

    [T]=[B(2)]−5[O]+2[O(−3)].

Using(1), the degree-three term is

    ch₃T=−26H³ +2·(−27/6)H³=−35H³.             (5)

A coherent sheaf supported in codimension at least3 has effective codimension-three leading cycle, or zero if its support has larger codimension. Its degree cannot be−35. This contradicts(5), and excludes the assumed five-dimensional space of sections.

Combining with the dimension dichotomy in Section 2 proves H⁰B(2)=0. That section then gives h¹B(2)=85 and HⁱB(2)=0 for i≥2.

## Scope

This is a structural sheaf-theoretic proof, not a formal certificate or novelty claim. It does not evaluate a selected HM matrix, polynomial, cofactor, or multiplication map. It proves no statement about H⁰B(3), H⁰B(4), a quintic pairing scalar, a selected cofactor's invertibility, a source image, an ambient physical obstruction, or a sharper collision bound.
