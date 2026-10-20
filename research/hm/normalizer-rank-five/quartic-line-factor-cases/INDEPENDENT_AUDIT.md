# Independent audit: bounded line-projection classification

PASS, with the rank-jump clarification incorporated into the quartic proof before its contact argument. Reviewed on 2026-10-19 against `PROOF.md` here and `PROOF.md`, including the latter's no-rectangle addendum. This audit concerns the abstract tensor arguments only; no source operation, physical value, external write, or numerical rank computation was used.

## Scope

The hypotheses are essential: E has dimension four, K has dimension five and full support, an irreducible compatible rank-two surface has an ordered-factor component projecting onto a line P(X), and the correction has no compatible square. These results do not show that every compatible rank-two surface has line projection. Nor do they show that every resulting abstract pair is realized by the global trilinear problem.

Within that scope, the surviving alternatives are a complementary-product quadric, the existing squarefree cubic-scroll type III, and the two new squarefree quartic normal forms. In particular, forcing every surviving case into the previous cubic family or a rank-one rectangular incidence would be incorrect.

## Reduction checks

1. The image sheaf I of the multiplication pencil is locally free on P1, globally generated as a quotient of O4, and a subsheaf of O(1)^5. Its splitting degrees are therefore zero or one. The kernel W is a subbundle of O4, has nonpositive splitting degrees, and satisfies -deg W=deg I.

2. A dominating ordered-factor surface requires generic kernel dimension at least two. Generic pencil rank zero contradicts dim XE=7. For rank one and I=O, a constant three-plane gives dim XW0 at least six unless X lies in W0; in that exception K=XW0 is ternary. For I=O(1), the two independent coefficient functionals give a fixed common kernel W0 and an invertible linear moving factor modulo W0. If X differs from W0, at least two independent product coefficients survive modulo W0-products in addition to the four-dimensional XW0. If X=W0, the three independent mixed coefficients supplement Sym²X. Each alternative exceeds dimension five. Thus generic kernel rank is exactly two and -deg W is 0, 1, or 2.

3. For degree one the coefficient vectors z,p,r are independent by the subbundle condition. For degree two all four generator coefficient vectors span E: otherwise a constant three-space H containing them would give I=(H O/W) direct-sum O, with a degree-two line summand, contradicting the splitting bound. The unsymmetrized coefficient space R then has dimension d+4. Multiplication X tensor E to Sym²E has the one-dimensional kernel wedge²X. Consequently degree two spans exactly five dimensions and hence all of K. This supplies the spanning hypothesis required by the quartic classification.

4. In degree one, any coefficient dependence forces X into span(z,p,r). The image span has dimension exactly four and is ternary. The independently established abstract ternary theorem in `../rank-six-cubic-web/REDUCIBLE.md` applies to this subweb and to the restriction of v; it does not require equality with the full K. Thus the lower-span case is excluded. Independent coefficients give precisely the already classified full-support cubic family.

5. In degree zero, intersecting distinct factor planes give two support limits at their shared square, while equal planes give the binary cubic obstruction. Hence the surviving factor planes are complementary. The subsequent finite C_(2,2) conclusion belongs to the previously established global trilinear incidence argument; the new local reduction supplies its complementary-product hypothesis.

## Quartic checks

The preliminary surjectivity argument is necessary and now correctly placed. Since K is contained in XE and has codimension two there, the relevant pencil is O4 to O(1)^2. Degree W=-2 forces its torsion cokernel to have length zero. Actual kernel fibers therefore equal W_l everywhere. In particular an isolated square in K cannot escape the contact argument through a pencil rank jump.

At a square e², variation inside the fixed fiber gives support limit W0. Projection of l(t) onto W_t along a fixed complementary plane gives a second support limit span(e,u0), where u0 is nonzero and outside W0. Their intersection is Ce. This proves the contact lemma without extending a rank-two image bundle across rank one. The alternative in which every l lies in W_l is excluded for O direct-sum O(-2) by the impossibility of a nowhere-zero O(-1) subbundle, and for O(-1)^2 by six independent coefficients. All of K is consequently squarefree.

Squarefreeness forces K intersect Sym²X to be a nonsquare one-dimensional line, normalized to Cxy. Removing diagonal complement terms in the two defining equations leaves the two nonzero functionals B,C. Their independent and proportional cases exhaust the classification; the explicit cube-root rescaling in the proportional case is valid over C. The displayed kernel columns are independent at every point and give the claimed distinct splitting types.

The compatibility calculation is complete: after quotienting by L=O(-1), preservation of every ruling line forces a scalar section b of L*, and the remaining term is a section a of W*. Matching the unique repeated coefficient gives exactly the stated two constraints in each case. The four remaining parameters are precisely restrictions of contractions q↦d(l)m+d(m)l. Direct coefficient substitution verifies the signs and factors of two.

Both images really have degree four: their parameter ruled surfaces have hyperplane line bundle associated with O(1) direct-sum O(3), respectively O(2) direct-sum O(2). Its self-intersection is four. Multiplication is finite, since a nonzero rank-two tensor has just two ordered factorizations up to scale, and generically birational, since only one factor lies in X. Thus the image degree is four. This does not assert that the images are smooth or embedded scrolls in P4.

Finally neither quartic K contains a two-by-two product rectangle. Projection to Sym²(E/X) forces one of its two factor planes to equal X, and the other would then be a constant two-plane in every W_l, contradicting degree -2. This supports keeping the quartic alternatives separate from earlier rank-one rectangle arguments. The immediate corrected residual statement is only the separately justified rank-at-most-two consequence on XE; a stronger global exclusion needs a new argument.
