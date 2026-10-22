# Separating the two invisible quartic lines

## Scope and pinned inputs

Work over C with G=SL2(F5), A=Sym^2 W, and X=P(A). Write D=D5 and F=I_Sigma(10). The discriminant conic Delta is the Veronese P(W), with invariant equation delta. Sigma is disjoint from Delta.

Use PR543 at 4e16e69c776bd85506341b5bb785f0d8a396bd3e, specifically CANONICAL-LIFTING-KERNEL-IS-A-SECANT-BUNDLE-AND-LEAVES-THREE-QUARTIC-CHANNELS.md, for the fixed nonzero equivariant identification J:D→Sym^4 W and the everywhere-surjective canonical lifting family

    0 → K → D O_X --L_can→ A O_X(1) → 0.

The same input proves that Q=Hom_G(D,H0(F)) has dimension four and restriction r:Q→Hom_G(K,F) is onto a three-dimensional space, with one-dimensional kernel

    T = { M ∘ L_can : M in Hom_G(A,H0(I_Sigma(9))) }.

This note uses, but does not reprove, the independently reviewed actual-map identification in that input. The identification remains an explicit dependency, not a formal certificate. PR658 at 95004606fb8b2ec51ecd97e2fde0d6d0ff328407 supplies a different one-dimensional space N in Q: the kernel of square restriction together with all six actual ideal-sheaf fibers. In particular every family in N vanishes on Delta.

No actual fourth coefficient, actual selected point, source vector, derivative, or matrix is evaluated below. All tests described are sufficient abstract criteria, not performed tests.

## Theorem

Every nonzero family in T has a nonzero full D-family fiber at every square point of Delta. Consequently:

1. T and N are distinct, and r is injective on N.
2. Restriction to K together with the full D-family fiber at any one square point is injective on Q.
3. At any square with C5 stabilizer, this latter full-fiber datum has only one character-allowed scalar component. Thus the three-dimensional K-restriction and that one scalar together give an isomorphism from Q to their four-dimensional target. The test is not an assertion that the actual scalar or restricted gate vanishes.

## 1. The factoring covector cannot vanish identically on the square conic

The second-symbol resolution is

    0 → A O_X(-8) → P4 O_X(-6) → I_Sigma → 0.

Twisting by seven and using H0(O(-1))=H1(O(-1))=0 yields

    H0(I_Sigma(7)) = P4 ⊗ A = V + P4 + D.

There is therefore no A summand. Since Sigma is disjoint from Delta, multiplication by delta gives the restriction sequence

    0 → I_Sigma(7) --delta→ I_Sigma(9) → O_Delta(9) → 0.

Let M be nonzero in the one-dimensional Hom_G(A,H0(I_Sigma(9))). If its restriction to Delta were zero, it would factor equivariantly through H0(I_Sigma(7)), contradicting the preceding decomposition. Its restriction is thus a nonzero equivariant map

    A → H0(P(W),O(18)) = Sym^18 W.

As A is irreducible, this map is injective.

## 2. Its three sections have no common zero

Let B be the common-zero divisor of this three-dimensional binary degree-eighteen series. The divisor is invariant under the projective A5 action. Every point orbit on P(W) has size 12, 20, 30, or 60: a stabilizer of a point in a finite subgroup of PGL2 is cyclic, and the possible nontrivial cyclic subgroup orders in A5 are 2, 3, and 5. (The order-five fixed points form the unique twelve-point orbit.) Thus a nonempty invariant effective divisor of degree at most eighteen must be exactly the reduced twelve-point orbit, with multiplicity one.

Its defining binary form f12 is G-invariant up to a character. G is perfect, so that character is trivial. Dividing the three degree-eighteen sections by f12 would therefore give a nonzero equivariant map

    A → Sym^6 W.

But Sym^6 W=V+P4 contains no A. This contradiction proves B is empty. Accordingly the restricted bundle map

    M|Delta : A O_Delta(1) → O_Delta(10)

is a nonzero functional on every fiber, hence is surjective on every fiber. The twists in this display are plane twists; their pullbacks to P(W) have degrees two and twenty respectively. The coefficient sections have degree eighteen, as above.

Since L_can is fiberwise onto A O_X(1), the composition M L_can has a nonzero fiber D→O_Delta(10)|p at every p in Delta. This proves the first assertion of the theorem without assigning any value to M or L_can at any actual point.

## 3. Separation and the minimal supplementary square datum

For any square p define e_p:Q→Hom(D,F|p), using that F is a line bundle near Delta. The kernel of r is T, and e_p is nonzero on T by Section2. Since T is one-dimensional, the map (r,e_p) is injective.

Every element of N has zero restriction to Delta. Hence T∩N=0, proving that r detects the entire PR658 invisible line. The two reductions thus have complementary, not coincident, one-dimensional ambiguities.

For the sharper scalar formulation, let p=[ell^2] have projective C5 stabilizer. In a universal eigenbasis ell,m of W, a lift of its generator has eigenvalues eta,eta^(-1), where eta is a primitive tenth root. The five monomials of Sym^4 W have weights eta^4,eta^2,1,eta^(-2),eta^(-4). The target O_X(10)|[ell^2] has weight eta^(-20)=1. Thus the only allowed source character is the one-dimensional line represented by ell^2 m^2, transported to D by the fixed J. All other character components of e_p vanish for every equivariant family.

This specifies a canonical one-dimensional character component, not a normalization or an evaluated source vector. Since e_p is nonzero on T, its target character line is attained. Surjectivity of r and the ability to adjust its lifts by T show that

    Q → Hom_G(K,F) ⊕ Hom_{Stab(p)}(D,F|p)

is an isomorphism: its dimensions are 4→3+1 and its kernel is zero. The choice of a basis to call the last component a numerical scalar is unnecessary for the vanishing criterion.

## Contribution and limits

Vanishing on the canonical secant kernel leaves a factoring line that is visible at every square, whereas the line left by the previous square-plus-six-fiber method is already visible on the secant kernel. It is therefore unnecessary to compute the complete two-channel square restriction after the K-restricted quartic has vanished: one character-allowed square datum suffices. Conversely square vanishing excludes the entire factoring ambiguity immediately.

This is a structural separation of universal equivariant spaces, not a proof of actual fourth vanishing or nonvanishing. It says nothing about the extra specialized A-kernel line at an axis, higher Smith exponents, full repair, prescribed-source membership, or algebraicity. Null retains the actual corrected fourth calculation.

Dependencies:
- https://github.com/Akilleez-QA/read-em-and-weep/blob/4e16e69c776bd85506341b5bb785f0d8a396bd3e/research/hm/order-four-quadratic-load/CANONICAL-LIFTING-KERNEL-IS-A-SECANT-BUNDLE-AND-LEAVES-THREE-QUARTIC-CHANNELS.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/95004606fb8b2ec51ecd97e2fde0d6d0ff328407/research/hm/fourth-gate-geometric-constraints/FOURTH-GATE-SIX-AXIS-INVISIBLE-CHANNEL.md
