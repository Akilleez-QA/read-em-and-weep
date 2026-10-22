# Nonzero vertex evaluation in the actual HM hyperplane family

## Theorem

Let F be the normalized Horrocks–Mumford bundle, let R=P(V) be its positive fixed plane, and let L=P(W*) be its negative fixed line. Write H_lambda=P(V directsum lambda), p_lambda=H_lambda intersect L, and E_lambda=F_Hlambda(2). The actual section bundle is

    Y=O_L(-3) tensor W,       Y_lambda=H0(E_lambda).

Then evaluation at the vertex is nonzero and has rank one for EVERY lambda. More precisely:

1. The vertex evaluation is an everywhere surjection

       Y -> O_L(-2),

   with kernel O_L(-4).
2. Under the actual identification Y_lambda=ell_lambda^3 W inside Sym^4 W, its kernel is C ell_lambda^4.
3. The global restriction map

       W=H0(P4,I_R^3 F(5)) -> H0(L,F|L(5))

   is an isomorphism onto the negative summand H0(O_L(1))=W. It has zero component in the positive summand H0(O_L(8)).
4. One has

       H0(P4,I_R^3 I_L F(5))=0.

5. The actual two-by-two W-multiplicity map d_W in the product-ideal Koszul calculation has rank two. This is deduced geometrically, not established by evaluating a selected matrix.
6. For every lambda, the unique vertex-vanishing section has the nonreduced sextic zero curve described below.

## Immutable inputs

The reduced-determinant theorem used here is REDUCED-DETERMINANT-THREE-CONIC-PENCIL.md, in research/hm/order-four-quadratic-load at commit

    35fc96bebf9c771a4de481c753bb527e510cd8c1.

Immutable source: https://github.com/Akilleez-QA/read-em-and-weep/blob/35fc96bebf9c771a4de481c753bb527e510cd8c1/research/hm/order-four-quadratic-load/REDUCED-DETERMINANT-THREE-CONIC-PENCIL.md

The actual restrictions F_H are stable with Chern classes (-1,4), h0(F_H(1))=0, and h0(F_H(2))=2, as required by that theorem. Its Bănică–Manolache analysis supplies the following applicable implication: when the actual determinant surface is reduced, a general member of the two-dimensional section pencil has a reduced zero curve consisting of three disjoint reduced plane conics.

The remaining established inputs are:

- DETERMINANT-CUBIC-FACTORIZATION-DICHOTOMY.md: the actual determinant base cubic is geometrically generically reduced; if its generic member is three distinct lines, its degree-three factor cover is irreducible. Equivalently for the argument below, the family has no A5-equivariantly distinguished generic line factor.
- NEGATIVE-VERTEX-EVALUATION-SCALAR.md: the actual section bundle, the uniform zero/rank-one dichotomy, the identified kernel in the nonzero case, and the restriction and Koszul criteria.
- RANK-ONE-VERTEX-SECTION-CURVE.md: regularity and cohomology of all section zero curves, uniqueness of their containing cubic, and the local and global consequences of rank-one vertex evaluation.

The source theorem now supplies the formerly missing reduced-general-section input. No assumption of generic smoothness or irreducibility of the actual determinant is introduced.

## 1. Pass to the generic section of the generic hyperplane

Let T=L, K=C(T), and M=P_T(Y). Since Y_K has dimension two, the function field of M is the purely transcendental extension K(t). Set k=K(t).

The actual determinant cubic surface S_K is geometrically reduced by the established factorization dichotomy. The reduced-determinant theorem therefore makes the zero curve C of the generic section over k geometrically reduced. Its geometric connected components are three pairwise disjoint reduced plane conics D_1,D_2,D_3, each with its unique spanning plane P_i.

For clarity, the conic and plane assertions also follow from the established section invariants. One has h0(O_C)=3, h1(O_C)=0, and omega_C=O_C(-1). After algebraic closure, reducedness gives three connected components, each of arithmetic genus zero; restricting adjunction gives degree two for each. A reduced connected degree-two curve spans a plane, even if it is two intersecting lines. The planes are distinct because two positive-degree curves in one projective plane must intersect.

The product of their plane equations is a cubic containing C. Since C has exactly one containing cubic, this product is the actual S_K after field extension. Hence the actual generic determinant base cubic c_K is a product of three distinct geometric lines. The planes P_i are the cones over those lines and contain the vertex p.

## 2. Zero evaluation would canonically select a determinant plane

Suppose evaluation were identically zero. The vertex is then a zero of every section, so the k-rational point p belongs to C.

Exactly one of the three disjoint geometric connected conics contains p. Denote it by D_p. Every element of Gal(kbar/k) fixes p and permutes the connected components; uniqueness forces it to preserve D_p as a closed subscheme. Thus D_p descends to k. One can express this descent by the invariant open-and-closed idempotent in H0(C_kbar,O_C_kbar).

Its unique spanning plane P_p is also defined over k: the degree-one forms vanishing on D_p form a one-dimensional kernel, and this kernel commutes with field extension. Intersecting P_p with the positive plane R gives a k-rational line factor of c_K.

## 3. The selected line descends through the section parameter

The line-factor scheme of the square-free cubic c_K is finite over K. Consequently the coefficient ratios of any one of its geometric line equations are algebraic over K. Normalize a nonzero coefficient of the selected factor to one. Section 2 puts all the resulting ratios in k=K(t).

K is relatively algebraically closed in K(t), so these ratios lie in K. Hence the selected factor is K-rational. Equivalently, a point of the finite factor scheme over K(t) has residue field a finite extension of K embedding into K(t); that residue field must equal K.

But the three-line alternative of the actual factorization theorem has an irreducible degree-three factor cover. Its generic factor scheme is the spectrum of a degree-three field extension of K and cannot have a K-rational point. This is a contradiction.

One may also recover the equivariant contradiction directly. The vertex, section family, and determinant are A5-equivariant. The component containing the vertex is characterized uniquely, so its plane selection is equivariant on M. Since it descends to T and M->T is dominant and equivariant, it defines an A5-equivariant rational line-factor map on T. This is precisely the distinguished factor excluded by the degree-six polarization and invariant-conic argument. There is no informal choice of a monodromy branch in either proof.

Therefore evaluation is not identically zero.

## 4. Uniformity and the actual scalar consequences

The actual equivariant vertex evaluation factors through

    O_L(-3) tensor W -> O_L(-2).

Its equivariant Hom space is one-dimensional, generated by the everywhere-surjective tautological evaluation. Nonvanishing therefore implies surjectivity at every parameter, with no exceptional finite set. Its kernel is O_L(-4), and the actual binary identification takes the kernel in each fiber to C ell_lambda^4.

The established incidence projection formula identifies the same scalar, after twisting by O_L(3), with

    H0(I_R^3 F(5))=W -> H0(F|L(5))
                         =H0(O_L(8))_+ directsum H0(O_L(1))_-.

It lands in the negative W summand. Since its scalar is nonzero, this is an isomorphism onto that summand. Its kernel is H0(I_R^3 I_L F(5)), since R and L are disjoint. This proves the stated vanishing.

The actual Koszul criterion identifies the W-multiplicity of this kernel with ker d_W, where d_W:C^2->C^2 is the actual primary multiplication map. The kernel vanishes, so d_W has rank two. This settles the remaining scalar of that actual map without replacing it by a general equivariant map or evaluating coefficients.

## 5. The vertex-vanishing curve is now unconditional

Fix any lambda and let s_lambda span C ell_lambda^4. Its zero curve C_lambda is a pure locally complete-intersection sextic, with

    omega_C_lambda=O_C_lambda(-1),     p_a(C_lambda)=-2.

At the vertex its multiplicity is exactly six. In the odd affine tangent coordinates its tangent-cone ideal is

    (f_2,c_3),

where f_2 is a nonzero quadratic relatively prime to the actual determinant cubic c_3. Its reduced support is a union of lines through the vertex, and C_lambda is necessarily nonreduced. This is not a claim that the nonreduced curve is itself a scheme-theoretic cone.

Its section algebra has dimension three with h1(O_C_lambda)=0 and a two-dimensional nilradical; it is isomorphic to either C[z]/(z^3) or C[x,y]/(x,y)^2. Moreover

    H0(I_C_lambda(2))=0,       h0(I_C_lambda(3))=1,

and its unique containing cubic is the actual determinant cone. These are now unconditional applications of the rank-one vertex-curve theorem for every parameter.

The exceptional nonreduced vertex section is compatible with the reduced general section supplied by the source theorem: they are different members of the pencil.

## Scope

This theorem resolves the actual vertex-evaluation scalar and its listed restriction, Koszul, and section-curve consequences. It does not prove global H0(B_Q(4)) vanishing, resolve all mixed-root square compatibility conditions, or settle any remaining adjoint gate. No inference from a single evaluated HM matrix, a rank experiment, or a selected coefficient specialization is used.
