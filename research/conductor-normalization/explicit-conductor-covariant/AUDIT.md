# Preserved mathematical audit of the geometric core

The application review is separated; publication edits are checked independently.

# Independent audit: explicit conductor covariant and module constraints

## Verdict and inputs

The generator theorem, displayed coefficients, four syzygies, Hilbert–Burch identification, primary-factorization signs, and the block-pairing identities in PROOF.md are correct. The original module-application review is preserved separately in MODULE-APPLICATION-AUDIT.md, unit09.

For the geometric claims this audit uses the reduced conductor ideal and its resolution from ../discriminant-normalization-conductor/PROOF.md. The separate module application has additional hypotheses recorded in unit09. All calculations below are universal polynomial identities, representation arguments, exact-sequence arguments, or formal module consequences. No actual HM multiplication, selected quartic, retained source, or map rank is evaluated.

## 1. Invariant normalization and a direct full-gradient check on W

For the binomial quartic coordinates set

    i=ae−4bd+3c²,
    k=ace+2bcd−ad²−b²e−c³,
    I=3i, J=54k.

Then 4I³−J²=108(i³−27k²), a nonzero scalar multiple of the quartic discriminant. For q=u x²+2vxy+w y², the coefficient substitution for q² is

    a=u², b=uv, c=(uw+2v²)/3, d=vw, e=w².

Write δ=uw−v² and D=−2δ. Universal substitution gives

    i(q²)=4δ²/3, k(q²)=8δ³/27,
    I(q²)=D², J(q²)=−2D³.

There is a stronger useful identity for the full ambient gradients, not merely their pullbacks to the tangent directions of W:

    ∇k(q²)=(δ/3)∇i(q²),
    ∇J(q²)=−3D∇I(q²).

Indeed

    ∇i=(e,−4d,6c,−4b,a),
    ∇k=(ce−d²,2cd−2be,ae+2bd−3c²,2bc−2ad,ac−b²).

Substitution into the second row gives δ/3 times the first row component by component. For example, the first component is δw²/3, and the middle component is (2δ/3)(uw+2v²)=(δ/3)6c. The other three components give the same factor. Scaling by 54 and 3 yields the normalized identity.

Consequently every coefficient of j=2I dJ−3J dI vanishes on all of W directly:

    j(q²)=2D²(−3D dI)−3(−2D³)dI=0.

This independently verifies PROOF.md's valid dense-open discriminant-singularity argument. Differentiating only the two scalar identities I(q²)=D² and J(q²)=−2D³ would prove tangential vanishing and would not by itself prove that all five ambient coefficients vanish. The full-gradient computation avoids that potential shortcut.

On N=V(I,J), vanishing of j is immediate. Since N and W have their reduced structures, all five coefficients therefore belong to the reduced union ideal K.

## 2. Nonzero irreducible generator space and actual ideal equality

The polynomial 1-form j is invariant under the induced SL₂ action because I and J are invariant. Contraction with a constant tangent vector gives an equivariant coefficient map from the five-dimensional quartic representation to S₄. Its source is irreducible. The common scalar factor is

    j=162(2i dk−3k di).

The a-coefficient after dividing by 162 is

    2i(ce−d²)−3ke.

The coefficient of b²e² in this expression is exactly 3: it comes from −3ke, and the first term contributes none. Thus the coefficient map is nonzero as a formal polynomial map, so it is injective and has five-dimensional image. The previously proved K₄ is also an irreducible five-dimensional representation. Inclusion therefore gives equality of these spaces.

Finally the imported Hilbert–Burch resolution establishes that K is generated in degree four. Hence equality in degree four proves equality of ideals, including the cone vertex, rather than just equality of their zero sets. No saturation or embedded-component step is missing here.

For g(v,w)=(I(v+w)−I(v)−I(w))/2, one has I(v)=g(v,v), so dIᵥ=2g(v,−). The quadratic form is nondegenerate, and g⁻¹(dI)=2v. The vector-covariant expression in PROOF.md follows with its stated factor 6.

## 3. Coefficient factorization and signs

The factorization is literally

    j_r=I(2∂ᵣJ)+J(−3∂ᵣI).

The displayed quadratic vector A=2∇J and linear vector B=−3∇I are correct. In particular

    B=(−9e,36d,−54c,36b,−9a)

is a basis of S₁. Its spanning property therefore needs no further module or representation hypothesis.

For the regular pair (I,J), a homogeneous relation IA+JB=0 in total degree four would be a multiple of (J,−I) with multiplier of degree −1. It is therefore zero. This proves uniqueness in exactly the required degrees.

With P(x)=(Ix,−Jx), the factor map

    F(u,v)_r=2(∂ᵣJ)u+3(∂ᵣI)v

satisfies FP(x)=j_r x, with the indicated plus sign in the second term of F. A change of quartic-generator basis acts by an invertible target transformation on α. It is generally a target change, rather than conjugation of an endomorphism; its kernel and rank are unaffected.

## 4. Complete syzygies and maximal minors

The infinitesimal substitutions x∂ᵧ, y∂ₓ, and x∂ₓ−y∂ᵧ produce the coefficient vectors

    E₊=(4b,3c,2d,e,0),
    E₋=(0,a,2b,3c,4d),
    H=(4a,2b,0,−2d,−4e).

They annihilate I and J, and hence their contractions with j vanish. The Euler field E₀=(a,b,c,d,e) also annihilates j because

    j(E₀)=2I·3J−3J·2I=0.

These are exactly the four columns of the displayed matrix L. Their linear independence as elements of S₁⁵ can be checked without any specialization. In a constant linear relation among the columns, the coefficient of b in the a-row kills the E₊ coefficient, and the coefficient of a in the b-row kills the E₋ coefficient. The c-row then kills the E₀ coefficient, and the a-row kills the H coefficient.

The known free syzygy module is S(−5)⁴, so its degree-five part has dimension four and generates the whole module. The four independent syzygies are therefore its basis. In particular they are independent over S as well; this latter conclusion uses the imported free resolution and does not follow from constant independence alone. The displayed L is consequently a complete Hilbert–Burch matrix. Its signed maximal minors equal the fixed ordered j-vector up to a common nonzero scalar and the chosen sign convention.

Equivariantly, E₀ is the V₀ summand and the three Lie columns form V₂. The exact degree-five presentation is

    0→V₀⊕V₂→S₁⊗K₄→K₅→0.

Since V₄⊗V₄=V₈⊕V₆⊕V₄⊕V₂⊕V₀, it follows that

    K₅≅V₈⊕V₆⊕V₄,  dim K₅=21.

This is a representation statement about the polynomial conductor ideal. No SL₂ representation on the cohomology module is needed or asserted.

