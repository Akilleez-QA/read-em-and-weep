> Historical mathematical review retained with the source. This is not a new independent review or a formal verification certificate.

# Independent audit: degree-one kernel exclusion

## Verdict

The proof is correct under its stated established inputs. Global generation of E(8), together with H¹(E(8))=0, excludes the previously possible saturated O(1) kernel. The complete negative endomorphism classification, exact component-cohomology dichotomy, and reduced-conic criterion follow without selecting the actual branch or evaluating an ambient detector. No arithmetic, twist, or logical correction is required.

This audit read PROOF.md and all five dependency files explicitly listed there: the global-conic-splitting-exclusion proof and audit, finite-square-component-detector proof, square-detector-factorization proof, and disjoint-zero-extension-detector proof. Their original geometric and bundle-resolution inputs are accepted as established; no HM matrix or selected-source/rank calculation is undertaken.

## 1. The decisive exclusion

A saturated rank-one subsheaf K of a vector bundle on a smooth surface is reflexive: in the exact sequence with torsion-free quotient, the depth lemma gives depth at least two at closed points. Thus on P² it is O(a). The quotient is I_Z(-2-a), and the Chern-class equation is

    16 = a(-2-a) + length(Z),
    length(Z) = a² + 2a + 16 = (a+1)² + 15.

In particular Z is nonempty for every integer a. Twisting by eight gives a globally generated quotient I_Z(6-a). Negative degree has no sections; degree zero cannot generate the ideal of a nonempty finite scheme. For d=6-a>0, choose a section and then a second section avoiding its finitely many curve components. Global generation away from Z makes this possible over C. Their complete intersection contains Z scheme-theoretically, so

    a² + 2a + 16 ≤ (6-a)²,
    14a ≤ 20,
    a ≤ 1.

For a=1, length(Z)=19 and the exact sequence is

    0 → O(9) → E(8) → I_Z(5) → 0.

H¹(E(8))=H²(O(9))=0 implies H¹(I_Z(5))=0. Since h⁰(O(5))=21 and a line-bundle twist does not change the dimension of sections on a finite length-19 scheme, the ideal sequence gives h⁰(I_Z(5))=2.

A basis f,g therefore generates I_Z(5) as a sheaf, not merely a two-dimensional subspace of quintics through Z. The resulting sheaf ideal (f,g) equals I_Z. It has no curve component, so f,g are a regular sequence of homogeneous quintics; their projective complete intersection has length 25. Equality of ideal sheaves forces the same scheme to have length 19, a contradiction.

There is no hidden reducedness or general-position hypothesis. The distinction between two equations vanishing on Z and two equations generating its ideal is essential and is correctly emphasized in the proof. The use of the ideal sheaf, rather than an asserted equality of unsaturated graded ideals, causes no problem: the complete-intersection scheme and its length are already determined by the ideal sheaf.

## 2. Negative endomorphisms and their common kernel

For f:E→E(-k), k>0, the trace and determinant are sections of O(-k) and O(-2k), hence vanish. Twisted Cayley–Hamilton gives f(-k)f=0. A nonzero such map has generic rank one, and its kernel is saturated because the image is torsion-free. If the kernel is O(a), then its image lies in the twisted kernel O(a-k). Thus a nonzero map

    I_Z(-2-a) → O(a-k)

exists. On a smooth surface Hom(I_Z,O)=O, so it corresponds to a nonzero section of O(2a+2-k). The new a≤0 bound and k≥1 imply a=0 and k≤2.

Two saturated nonnegative-degree lines cannot be distinct: their composite maps to each other's quotient vanish by degree, and an inclusion between them with nonzero quotient would produce torsion in a quotient asserted torsion-free. Hence the common kernel K is unique when it exists. Quotient followed by inclusion provides every negative-twist map, and gives exactly

    H⁰(B(-1)) = j H⁰(O(1)), dimension 3;
    H⁰(B(-2)) = j H⁰(O), dimension 1;
    H⁰(B(-k)) = 0 for k≥3.

When K does not exist, all these spaces vanish. This also proves that the nonzero dimensions occur together. The nilpotent line is intrinsically N=K² det(E)⁻¹; identifying it with O(2) uses a line-bundle identification, as the proof notes. All twisted compositions vanish because the quotient map annihilates K. Scalar summands supply no negative sections.

The phrase “entire negative module” is sound when interpreted as the strictly negative graded portion, compatible with polynomial multiplication while the target twist remains negative; it makes no claim about nonnegative endomorphism degrees.

A section of E(-1) would saturate to a line of degree at least one, so H⁰(E(-1))=0. More negative twists also vanish. The rank-two identity E*=E(2) therefore gives

    H²(E(t))* = H⁰(E(-t-1)) = 0 for t≥0.

A nonzero section of E saturates to the unique O, and H⁰(I_Z(-2))=0 then gives h⁰(E)=1. Otherwise h⁰(E)=0. This does not establish stability or semistability of E(1).

## 3. Exact numerical cohomology checks

For B=End₀(E), rank(B)=3, c₁(B)=0, and

    c₂(B)=4c₂(E)-c₁(E)²=64-4=60.

Consequently

    χ(B(t)) = (3/2)(t²+3t+2)-60.

At t=-2 this is -60. The trace pairing identifies B*=B, and surface Serre duality gives h²(B(-2))=h⁰(B(-1)). Therefore the triples are precisely

    (h⁰,h¹,h²)(B(-2)) = (1,64,3) when h⁰(E)=1;
    (h⁰,h¹,h²)(B(-2)) = (0,60,0) when h⁰(E)=0.

The arithmetic is h¹=h⁰+h²-χ. In particular the component target has dimension zero or three, and its actual restriction map has rank at most three. The dimension-three alternative does not prove that the three ambient functionals are independent.

For X=8C, the restriction sequence has left term B(-17), since C has plane degree two. The supplied H¹(B(14))=0 is dual to H¹(B(-17))=0. Together with H⁰(B(-17))=0, it gives the full-section extension isomorphism at 8C. Euler characteristics are

    χ(B(-1))=-60,
    χ(B(-17))=300,
    χ(B(-1)|X)=-360.

Thus (h⁰,h¹) on X is (0,360) or (3,363), as claimed.

For a=0 the ideal-square factorization specializes correctly to

    0 → E → B(-2) → I_Z²(-4) → 0.

Here length(Z)=16. Local freeness of E makes its zero scheme a local complete intersection; I_Z/I_Z² has rank two over O_Z. The exact sequence for O/I_Z² therefore gives length(O/I_Z²)=3·16=48. This remains a quotient carrying the actual extension and ambient restriction data, not a replacement of the Gysin map by an abstract dimension count.

## 4. Reduced-conic extendability and saturation

The restriction sequence for B(-1) to C has kernel B(-3). Its H⁰ vanishes, so global detector sections restrict injectively to C in both branches.

In the nonzero branch, j:O(2)→B has torsion-free cokernel on W. One can check this locally from its entries (-xy,x²,-y²,xy): a regular sequence x,y has no common codimension-one factor. Multiplication by the conic equation is injective on this torsion-free cokernel. Tensoring the sequence with O_C consequently preserves injectivity of j, giving the actual subsheaf

    j_C: O_C(1) ↪ B(-1)|C.

The conic sequence

    0 → O(-1) → O(1) → O_C(1) → 0

has H⁰ and H¹ of its left term equal to zero. Its section restriction is an isomorphism. Hence the globally extendable sections on C are exactly the global sections of the actual image of j_C, and their extension is unique.

This is a necessary-and-sufficient criterion for membership in the image of global restriction, not a claim that every section on C extends. It requires knowledge of the actual restricted nilpotent image. At R=Z∩C, the image has vanishing order twice that of the restricted kernel section; its saturation is O_C(1)(2R). Using that larger line instead can introduce sections that do not extend. Injectivity as a sheaf map is compatible with failure to be a line subbundle at these points.

In the zero branch the globally extendable subspace is simply zero; there is no actual nilpotent line to use. The proof correctly presents its line-membership statement only in the nonzero branch.

## 5. Twist conventions and thresholds

All unqualified twists in the audited proof are plane twists. For the smooth plane conic C≅P¹,

    O_W(1)|C = O_C(1) = O_P¹(2).

In particular:

- j_C has domain O_C(1)=O_P¹(2), whose section dimension is three, not two.
- The disjoint branch E|C=O_C⊕O_C(-2) means O_P¹⊕O_P¹(-4), with splitting gap four.
- The ideal of nC on W is O_W(-2n); its layer on C has P¹ degree -4n.
- Ambient hyperplane twists also pull back with a factor of two: i*O_Y(1)=O_W(2). The component bundle is therefore B(-2), and its surface-dual detector is B(-1).

For full endomorphisms, H⁰(End E(-2n))=0 holds already for n≥2. At n=1 the restriction kernel has dimension one in the K branch and zero otherwise. Surjectivity still uses H¹(End E(2n-3))=0, whose supplied threshold 14 yields n≥9. The better H²(E(t)) bound does not settle H¹(E(7)) in the attempted endpoint t=13 proof.

In the disjoint branch, b=2 and t_n=2n-5 are correct plane-degree quantities. At n≤2 the relevant positive extension group vanishes; at n=6, t_n=7 lies in the established evaluation-surjectivity range k≥6. The imported residue criterion thus still gives 3≤n₀≤6. No stronger general first-nonsplitting bound or selected order follows here. A separately imposed P¹ gap of at least eight would exclude this disjoint branch, but is not an assumption of this proof.

## Scope

 No HM matrices, actual zero schemes, ambient functionals, or selected ranks are evaluated. The earlier a=1 formulas remain valid as conditional algebra but cannot occur for this E under the supplied hypotheses.
