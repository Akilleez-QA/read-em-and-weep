# The actual cubic relation has no triple fiber

## Pinned structural inputs

At commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04, in research/hm/order-four-quadratic-load/:

1. [VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md), sections 1 and 2, identifies the ACTUAL globally flat odd-spinor quotient over L=P(W). Its cubic relation is the equivariant subbundle K3=O_L(-2) of Sym^3 W' tensor O_L(1). Its arrow is the dual complete-cubic evaluation arrow, not an arbitrary generic local cubic. Every nonempty G-orbit on L has at least twelve points.
2. [UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md), sections 1 and 2, constructs the nonzero invariant f in Sym^3 W' tensor Sym^3 W and identifies the above arrow. Its four coefficient sections form a basis of H0(O_L(3)). The same note distinguishes the nonisomorphic representations A=Sym^2 W and V=Sym^2 W'. Here G=SL2(F5), and W' is the positive binary module called U in the later papers.

The first input supplies the actual-grade identification explicitly required in the second input's application boundary. No actual coefficient is selected or evaluated.

## 1. A generically pure-cube cubic is impossible

Twist the actual cubic subbundle by O_L(-1). It becomes a subbundle O_L(-3) of the trivial bundle Sym^3 U tensor O_L. Its projectivization is therefore a G-equivariant morphism

    phi: P(W) -> P(Sym^3 U),   phi^* O(1)=O_L(3).

It is everywhere defined; indeed the cited complete-cubic assertion makes it a closed immersion, although only the displayed degree is necessary below.

Let nu: P(U) -> P(Sym^3 U) be the cubic Veronese map, whose image C is the locus of proportional pure cubes. If the actual f3 over C(L) becomes a cube over an algebraic extension, its generic projective point lies in C. Since C is closed, the entire image of phi lies in C. The Veronese is an isomorphism onto its image, so phi=nu composed with psi for a G-equivariant morphism psi:P(W)->P(U).

Pullback of O(1) gives 3=3 deg(psi). Hence psi has degree one and is a projective isomorphism. An equivariant isomorphism identifies, by transport of vector fields, the G-modules H0(P(W),T_P(W)) and H0(P(U),T_P(U)). These are Sym^2 W and Sym^2 U, using the determinant pairings. Thus A would be isomorphic to V, contradicting the pinned distinction. This argument avoids any assumed equivariance of a selected scalar spinor component: it uses the actual equivariant cubic relation LINE.

Consequently the actual cubic is not generically a pure cube, even geometrically over C(L).

## 2. In fact no fiber is a pure cube

The cubic Veronese curve C is cut out set-theoretically by homogeneous quadrics (the two-by-two minors of the binary cubic catalecticant). Each defining quadric pulls back under phi to a section of O_L(6).

If phi(p) lay in C for any p in L, equivariance and G-invariance of C would put the entire orbit Gp in phi^{-1}(C). That orbit has at least twelve distinct points. Every pulled-back defining quadric would then have at least twelve distinct zeros, whereas a nonzero section of O_P1(6) has at most six. Thus all pulled-back quadrics would be identically zero. This would force phi(L) subset C, contrary to section 1.

Therefore the actual cubic f3 has no triple divisor at any point of the negative line. The next section identifies the remaining multiplicity pattern structurally.

## 3. Exactly one reduced twelve-point orbit of double fibers

Suppose every fiber of phi were a singular cubic. By section 2 no fiber is a triple cubic. At the generic point there is therefore a unique repeated linear factor and a unique residual linear factor, each defined over k=C(L): uniqueness makes each factor invariant under the Galois group, and their projective coefficient points descend. Equivalently, the repeated linear factor is the degree-one gcd of the binary cubic partial derivatives, which is defined over k. This is a universal characterization, not an evaluation of actual derivatives.

These factors define rational maps r,s:L -> P(U) with

    phi = mu composed with (r,s),
    mu([ell],[m])=[ell^2 m].

Uniqueness makes r and s G-equivariant. Any rational map from the smooth complete curve L to P(U) extends uniquely to a morphism; equivariance persists by equality on the dense domain of definition. The displayed factorization likewise persists everywhere, since the target is separated and both sides are morphisms.

The multiplication map mu has mu^*O(1)=O(2,1). Consequently

    3 = 2 deg(r) + deg(s).

The nonnegative integer deg(r) cannot be zero: an equivariant constant map would give a G-fixed point of P(U), hence an invariant line in the irreducible binary representation U. It cannot be one by the tangent-vector-field representation argument of section 1. It would therefore be at least two, contradicting the degree identity. Thus not all cubic fibers are singular.

The universal discriminant hypersurface of binary cubics has degree four and cuts out the singular cubics. Its pullback under phi is consequently a nonzero section of O_L(12). Its zero divisor is G-stable, since singularity is invariant under linear coordinate changes. Every nonzero section of O_P1(12) has a zero divisor of total degree twelve over C. Every nonempty G-orbit has at least twelve points. It follows that this divisor consists of exactly one orbit of twelve distinct points, all with multiplicity one.

At those twelve points the actual cubic has a double linear factor and a distinct simple factor, by section 2. At every other point it has three distinct factors. This determines the multiplicity distribution without selecting a base point, evaluating the actual discriminant, or computing an actual root or coefficient.

## Consequence for the source operator

[PR764](https://github.com/Akilleez-QA/read-em-and-weep/blob/961202467b714be787811f331534659122f761fe/research/hm/noncube-source-exclusion/PROOF.md), commit 961202467b714be787811f331534659122f761fe, establishes that im(K) subset k d forces f3 to be geometrically a pure cube for the regular-pair source operator, with k=C(L). The structural exclusion above contradicts that necessary condition. Hence the actual source operator satisfies im(K) not subset k d. The universal common-direction alternative of PR760 is impossible for the actual source operator.

This is an authored structural proof; its independent review is recorded separately. It is not proof-assistant certified. It uses no selected actual formula substitution, coefficient, point, derivative, root or discriminant evaluation, rank test, scan, model example, or large computation. It makes no claim about the fourth Bockstein or algebraicity.
