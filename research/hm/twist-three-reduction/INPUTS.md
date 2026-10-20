# Refined equivariant inputs from the primary sources

The numerical twist-two proof does not supply these representation labels. This note explicitly supplies them and derives the resolution coefficients required by the higher-twist proofs. Throughout F=F_HM(-3), where F_HM is the bundle in the 1973 paper. Thus its argument n corresponds to our twist n+3.

Use the ordinary left action of N=H₅⋊SL₂(F₅)⊂SL(V). Let X=S₁=V*, and let V₁,V₃=V₁* have central characters ζ²,ζ³ respectively. Let W=χ₂ and W′=χ₂′ denote the two historical two-dimensional quotient representations. They are self-dual and determinant one. Write χ₃′=Sym²W′, and χ₄ for the nonspinorial four-dimensional irreducible quotient representation.

The primary section-module resolution sheafifies to

    0→2O(−8)→20O(−6)→35O(−5)
      →15O(−4)⊕4O(−3)→F→0.                       (R)

Its source is Wolfram Decker, Monads and cohomology modules of rank 2 vector bundles, Compositio Math. 76 (1990), pp.14–16:
https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf

The audited cohomology facts are H¹F(*) with dimensions (5,10,10,2) in degrees 0,1,2,3, H²F(*) supported only in degree −2 with dimension2, H⁰F(t)=0 for t<3, and F*=F(1). Serre duality gives H³F(t)=H¹F(−t−4)*. All required H⁴ groups follow from the same duality and section vanishing.

The following refined representations are established in Horrocks–Mumford, A rank 2 vector bundle on P4 with 15,000 symmetries, Topology 12 (1973), §4, equations (4.4),(4.6),(4.12), translated from their bundle F(3):

    H¹F = V₃;  H¹F(1)=V₁⊗W′;
    H¹F(3)=W′; H⁰F(3)=χ₄; H²F(−2)=W.

Primary source:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

The statements H⁰F(3)=χ₄ and H¹F(3)=W′ are precisely the separate H⁰ and H¹ assertions of (4.12), printed p.74; χ₄ is not χ₄#. The H²F(−2)=W assertion comes from (4.2), printed p.72.

All resolutions can be taken N-equivariant: the graded section module is N-equivariant, and at every step invariant complements lift the minimal generator spaces, since a finite group over C is linearly reductive. This preserves the displayed minimal shifts. No choice of equivariant differential values is made.

There is no character ambiguity in F*=F(1): det F and O(−1) are isomorphic underlying line bundles, so their equivariant discrepancy is a character of N. N has no nontrivial characters. Indeed H₅'s central μ₅ is its commutator, SL₂(F₅) acts on H₅/μ₅ without invariant characters, and SL₂(F₅) is perfect. Thus their determinant linearizations agree.

## Recover A and C without dimension guessing

Write A for the two-dimensional coefficient of O(−8) in the equivariant resolution (R), and C for the four-dimensional coefficient of O(−3). Twist (R) by3. Its only nonzero cohomology entries are C⊗H⁰O in total degree0 and A⊗H⁴O(−5) in total degree1. All other line bundles have twists −1,−2,−3 and are acyclic; no differential can connect these entries in the spectral sequence. Since N⊂SL₅, H⁴O(−5) is the trivial representation. Therefore

    C≅H⁰F(3)=χ₄,   A≅H¹F(3)=W′.                 (4)

This identifies the actual coefficients equivariantly, rather than assigning a representation to the numeral ‘2’ or ‘4’ by dimension.


## Exact source map

HM (4.2) identifies H²F(-2)=W; (4.4) identifies H¹F=V₃; (4.6) identifies H¹F(1)=V₁⊗W′; (4.11) identifies H¹F(2)=V⊗W′; and (4.12), printed p.74, identifies separately H⁰F(3)=χ₄ and H¹F(3)=W′. The table following (4.12) and Serre duality supply the numerical support assertions above. Decker pp.14–16 supplies the section-resolution shifts by comparison with the displayed first-cohomology resolution.

D is derived, not imported, in PROOF.md §2. G and P are derived in the twist-four proof from the twist-zero and twist-minus-one line-cohomology complexes. HM Lemma 3.3 and its Appendix supply the symmetric-power and quotient-character identities explicitly written in those proofs. None is a claim about the value of a particular HM differential.
