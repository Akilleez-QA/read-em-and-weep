# The two quadratic Rao channels and the exterior-channel cubic socle

## Result and scope

This packet adds a representation classification and a commutative-module constraint to the conditional degree-70 frontier. It does not assert existence of a degree-70 curve or exclude all degree-70 curves. Its main exterior-channel lemma applies to arbitrary commutative graded modules and survives any independent exclusion of degree 70.

Use the conventions and hypotheses of ../degree-seventy-smooth-frontier/PROOF.md and its independent audit. Put X=S_1=V*, and write U_2=A_HM*, U_3=A_HM. Suppose the quadratic Rao dimension is ten. There are exactly two possible representation patterns for its nonzero multiplication into cubic Rao dimension at most fifteen:

1. Exterior channel:

       M_2 = U_2 tensor W = exterior^2 X,
       M_3 = (U_3 tensor W) direct-sum Q,
       Q = 0 or U_3.

   The multiplication is, up to a nonzero scalar and equivariant identifications, x tensor m -> x wedge m into exterior^3 X = U_3 tensor W. Its image has dimension ten. Every nonzero linear slice has rank six and kernel dimension four. Moreover

       S_1 (S_1 M_2) = 0.

   Thus the full ten-dimensional cubic image is in the graded socle of the Rao module. This is forced by commutativity, not merely by representation multiplicity.

2. Other channel:

       M_2 = U_2 tensor W',
       M_3 = U_3 tensor Sym^2 W'.

   Multiplication is unique up to a nonzero scalar, is surjective as a total tensor map, and factors on multiplicities through

       W' tensor W' -> Sym^2 W'.

   The T tensor W' summand is killed. The target has dimension fifteen. No exact slice-rank or nonvanishing of higher multiplication is claimed in this second case.

Here W and W' are the two distinct irreducible two-dimensional representations of G=SL_2(F_5), with the historical labels fixed below. In the conditional degree-70 exterior case there is also a new quartic constraint:

       dim I_C(4) is 0 or 5.

If dim M_3=10 in that case, the general hyperplane section has

       h_Gamma(3)=16,
       h_Gamma(4)=25-dim I_C(4), hence 25 or 20.

All assertions are necessary conditions. In particular, an unused U_3 summand in M_3 is allowed and is not silently discarded.

## 1. Conventions and representation inputs

The linear group is N_tilde=H_5 semidirect G; the projective group is its quotient by the order-five scalar center. All representation statements refer to N_tilde. The modules W,W',T=Sym^2 W, and T'=Sym^2 W' are inflated from G. Both W and W' have determinant one and are self-dual; their central G-involution is -1. T and T' are distinct irreducible three-dimensional representations with central involution +1.

The audited HM identities in ../cubic-massey-module-reduction/PROOF.md, ../equivariant-massey-multiplicity/PROOF.md, and ../lower-weight-image-symmetry/PROOF.md give

    X tensor U_2 = U_3 tensor (T direct-sum W'),
    exterior^2 X = U_2 tensor W,
    exterior^3 X = U_3 tensor W.

For the last identity, use unimodularity of the five-dimensional X and exterior^3 X = (exterior^2 X)*; U_2*=U_3 and W*=W. These equalities fix the labels W and W', which cannot be interchanged independently of the HM identities.

The standard binary-icosahedral representation facts used here are: W,W' are exactly the irreducible two-dimensional modules, S=Sym^3 W is irreducible of dimension four, and the quotient A_5 has no irreducible two-dimensional complex representation. These facts are the primary appendix inputs recorded in the cited audited packets, not identifications of an actual Rao map. The primary source is Horrocks–Mumford, Topology 12 (1973), pp. 63–81, its representation appendix and Lemma 3.3:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Only the following small-product consequences are needed:

    T tensor W = W direct-sum S,
    W' tensor W' = 1 direct-sum T',
    W' tensor W is irreducible of dimension four,
    T tensor W' has no constituent of dimension at most three.

The first is the ordinary SL_2 Clebsch–Gordan decomposition restricted to G. The second is the symmetric/exterior square decomposition and determinant one. For the third, the central involution acts trivially, so it is an A_5 representation. It has no trivial summand by Schur's lemma because W and W' are distinct self-dual irreducibles. There are no two-dimensional A_5 irreducibles; a reducible four-dimensional A_5 module with no trivial summand is therefore impossible. For the fourth, central parity excludes dimensions one and three. The only candidate constituents of dimension two are W,W'. Tensor-Hom adjunction gives

    Hom_G(T tensor W', W) = Hom_G(T, W tensor W') = 0,
    Hom_G(T tensor W', W') = Hom_G(T, 1 direct-sum T') = 0.

This proves all small-target claims without needing the complete decomposition of the six-dimensional product T tensor W'.

## 2. Classification under the bounded Rao hypotheses

Import from the degree-70 frontier only the following already audited conditions:

    M_2=U_2 tensor E, with E irreducible of dimension two;
    M_3=U_3 tensor F, with dim F at most three;
    a general slice M_2 -> M_3 has rank at least six.

The last condition is the geometric conclusion that a general hyperplane section has at most four cubic equations. Multiplication is specified by a G-map

    (T direct-sum W') tensor E -> F.

If E=W, Section 1 shows that the only source constituent of dimension at most three is one copy of W. Hence the image multiplicity is W, and F=W or W direct-sum 1. Zero multiplication is impossible by the slice-rank lower bound. The Hom space to the image has dimension one. Exterior multiplication X tensor exterior^2 X -> exterior^3 X is a nonzero equivariant map to exactly that image, so the actual multiplication is its nonzero scalar multiple. This identifies the map itself; it is stronger than identifying its source and target dimensions.

If E=W', the only source constituents of dimension at most three are one copy each of 1 and T'. They cannot both fit in F. An image multiplicity of 1 gives total image dimension five, contradicting slice rank at least six. Thus the image multiplicity is T', F=T', and the only map is the symmetric projection on W' tensor W', up to nonzero scalar. The T tensor W' summand maps to zero. This proves the stated dichotomy.

## 3. Universal exterior-channel lemma for commutative graded modules

Let X be any complex vector space of dimension at least three, and let M be a graded module over Sym X. Suppose that, after identifying a graded piece with exterior^2 X, its next multiplication is the wedge map onto a subspace J identified with exterior^3 X. Then every element of X annihilates J.

Indeed write

    B(a;b,c,d) = a dot (b wedge c wedge d) in the next graded piece.

This is alternating in its last three variables. The module identity for the two commuting linear forms a,b, applied to c wedge d, gives

    B(a;b,c,d)=B(b;a,c,d).

Using this symmetry and the alternating identity repeatedly gives

    B(a;b,c,d)
      = B(b;a,c,d)
      = -B(b;c,a,d)
      = -B(c;b,a,d)
      = B(c;a,b,d)
      = B(a;c,b,d)
      = -B(a;b,c,d).

Characteristic zero implies B=0. Decomposable three-vectors span exterior^3 X, so XJ=0. A nonzero scalar in the original wedge map cancels from the commutativity identity and changes nothing.

This argument does not assume that J exhausts its graded piece. In particular, the optional unused cubic summand Q in the exterior case is not required to be annihilated.

When dim X=5, a nonzero x gives

    ker(x wedge - : exterior^2 X -> exterior^3 X)=x wedge X,

of dimension four. To verify this without evaluating a matrix, choose an abstract vector-space complement X=Cx direct-sum Y. Then exterior^2 X=(x wedge Y) direct-sum exterior^2 Y, and wedge by x vanishes on the first summand and is injective on the second. Its rank is dim exterior^2 Y=6. This is a universal exterior-algebra proof for every nonzero x, not a point or rank-instance computation.

## 4. Conditional quartic consequences for degree 70

Let C be a putative curve satisfying the audited frontier, in the exterior channel. For a general linear form ell with hyperplane section Gamma, the absence of ambient quadrics and cubics identifies

    I_Gamma(3)=ker(ell:M_2 -> M_3).

Section 3 makes its dimension four, giving h_Gamma(3)=20-4=16.

The quartic restriction exact sequence, using I_C(3)=0, gives

    0 -> I_C(4) -> I_Gamma(4)
      -> ker(ell:M_3 -> M_4) -> 0.

The cubic image J has dimension ten and is annihilated by every linear form. Hence this kernel has dimension at least ten. Uniform position gives

    h_Gamma(4) >= h_Gamma(3)+h_Gamma(1)-1=16+4-1=19.

Since there are 35 quartics on the hyperplane P^3,

    dim I_C(4)+10 <= dim I_Gamma(4) <= 35-19=16.

Thus dim I_C(4)<=6. Its Heisenberg central character is nontrivial (the fourth power of that of X), so its dimension is divisible by five. It is therefore zero or five.

If M_3=J has dimension ten, the kernel above has exactly dimension ten, giving the sharper exact equality

    h_Gamma(4)=35-dim I_C(4)-10=25-dim I_C(4).

For the possible fifteen-dimensional M_3, only the stated inequality and quartic dimension alternatives are asserted; multiplication on Q can contribute additional kernel.

## 5. Boundaries and verification

The classification exhausts the M_2-dimension-ten cases under the bounded target and slice hypotheses. It does not address the already separate M_2=0 or 5 alternatives, and does not establish that either classified case is realized by a curve. The second channel is not asserted to have injective slices or to extend to any prescribed higher-degree module. The socle conclusion is specific to the exterior channel and follows from commutativity, which an arbitrary isolated equivariant tensor would not satisfy.

Only existing local proof files were read and this new local proof packet was written. No source tensor, coefficient instance, operation value, selected point, source rank instance, or problem-specific matrix was evaluated. No actual source-instance evaluation is claimed.
