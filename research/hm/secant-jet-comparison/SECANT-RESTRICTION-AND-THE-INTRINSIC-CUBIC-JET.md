# Secant restriction and the intrinsic cubic jet

## Pinned inputs and scope

Work over C with G=SL2(F5), X=P(A), A=Sym²W, D=D5, and F=I_Sigma(10). All relevant representations factor through A5. No actual HM/source evaluation is made here.

Use the secant-kernel theorem at 4e16e69c776bd85506341b5bb785f0d8a396bd3e for the actual-map identification and exact sequence

    0 → K → D O_X --L→ A O_X(1) → 0,
    0 → T → Q --r→ R → 0,
    Q=Hom_G(D,H0(F)), R=Hom_G(K,F), dim(T,Q,R)=(1,4,3),
    T={M L : M in Hom_G(A,H0(I_Sigma(9)))}.

The first sequence is everywhere exact; in particular L has local right inverses at the six axes. The local second-symbol ideal there is (x²,y²). Use FOURTH-GATE-ONE-AXIS-JET-AND-ONE-SQUARE-FIBER.md at c85c756 for: six axes in general position; distinct smooth conics C_i through the five axes other than p_i; the jet map

    j:Q → E=Hom_N(D,(I_Sigma/m_p² I_Sigma)(10)), dim E=3,

where N=Stab_A5(p) is dihedral of order10. The quotient here is a stalk-supported module, not a further residue fiber. Write rho1 for the cotangent representation at p and rho2 for the other two-dimensional N-irreducible. The same input establishes

    D|N=1+rho1+rho2,
    I_Sigma/m_p³=rho2,
    m_p³/m_p⁴=Sym³(rho1)=rho1+rho2,
    m_p² I_Sigma=m_p⁴.

The O(10) fiber twist is trivial on N. These local modules and the actual-map identification are pinned dependencies, not independently rederived HM statements. No square datum is used below.

## Theorem

There is a canonical one-dimensional target E1 inside E, namely its unique rho1-valued cubic-symbol channel. Let pi1:E→E1 be the canonical isotypic projection. Then

    (r, pi1 j): Q → R ⊕ E1

is an isomorphism. The factoring line T maps isomorphically to E1, while its two rho2-valued jet channels vanish. In particular a single intrinsic cubic jet channel, rather than the entire three-dimensional first ideal-sheaf jet or any square evaluation, supplements secant restriction.

## 1. An elementary degree-nine exclusion

No nonzero plane polynomial of degree nine vanishes to order at least four at all six axes. Indeed, on every smooth C_i its intersection multiplicity is at least 5·4=20, exceeding 2·9=18. Bezout therefore forces C_i to divide the polynomial. The six conics are distinct and irreducible, so their product of degree12 divides it, impossible in degree nine.

Suppose ML is in ker j. Equivariance propagates the zero entire-family jet to all six axes. In a local trivialization j(ML)=0 means all components of ML lie in m²I_Sigma=m⁴. A local right inverse S of L gives M=(ML)S, so every coefficient of M lies in m⁴ at every axis. These coefficients are global degree-nine sections, hence zero by the preceding paragraph. Thus M=0 and

    T ∩ ker j = 0.

This proves combined secant/whole-jet injectivity already. The next step identifies exactly which jet component is needed.

## 2. Factoring families have only the cubic rho1 symbol

Let ell=O_X(-1)|p be the axis line in A. Since N is finite, the inclusion ell⊂A splits N-equivariantly. Consequently

    (A O_X(1))|p = A⊗ell* = 1 ⊕ T_pX = 1 ⊕ rho1.

The final identification uses the self-duality of a dihedral two-dimensional irreducible: T_pX and its cotangent rho1 are isomorphic. This argument includes the possibly nontrivial reflection character of ell; it does not treat O(1)|p as trivial.

Because m I_Sigma=m³, the leading ideal-fiber map of M is an N-map

    1+rho1 → (I_Sigma/m I_Sigma)(10)=rho2.

There is no such nonzero map. Therefore M takes values in mI_Sigma=m³ locally. Its next symbol is now an unambiguous N-map

    (A O_X(1))|p=1+rho1 → (m³/m⁴)(10)=rho1+rho2.

Only the rho1-to-rho1 part can be nonzero. Composing with L does not change this assertion: modulo m⁴ the product ML is its cubic symbol composed with the constant fiber L(p), since positive-order variations of L multiply m³ into m⁴. L(p) is onto, so a nonzero cubic symbol remains nonzero upon this composition.

Thus j(T) lies entirely in the unique rho1 isotypic component of I_Sigma/m⁴. That component is contained in the canonical submodule m³/m⁴: the quotient I_Sigma/m³ is rho2, so it has no rho1 part. The whole module has decomposition rho1+2rho2. Central character idempotents in C[N] give canonical projections onto the two isotypic parts, irrespective of the lack of a preferred splitting between the two rho2 copies. Define

    V1=(I_Sigma/m⁴)(10)[rho1],
    V2=(I_Sigma/m⁴)(10)[rho2],
    E1=Hom_N(D,V1), E2=Hom_N(D,V2).

Their dimensions are one and two, and E=E1⊕E2 canonically. The degree-nine exclusion shows j|T is injective; hence j(T)=E1 and pi1 j|T is an isomorphism. Since r is onto with kernel T, (r,pi1 j) is an isomorphism, proving the theorem.

## 3. Exact compatibility of the two three-channel descriptions

There is a unique canonical linear map C:R→E2 satisfying

    pi2 j = C r.

It exists because pi2 j kills T=ker r; no choice of a lift in Q is involved. For any proposed secant value a in R and full jet b in E, they come from a common family if and only if

    pi2 b = C(a).

Necessity is the displayed factorization. For sufficiency choose a lift q of a. The difference b-j(q) lies in E1, which j(T) fills uniquely, so a unique element of T corrects the lift. Thus

    image(r,j) = R ×_{E2} E,
    0 → Q --(r,j)→ R⊕E --[(a,b)↦pi2 b-C(a)]→ E2 → 0.

The two independent compatibility equations are intrinsic, though this theorem does not compute C on actual fourth-gate data. Since dim ker j=1 from the pinned jet theorem, j is onto; therefore C is onto and ker C has dimension one. The secant image of the jet-invisible line is exactly ker C. This distinguishes the two invisible lines and identifies their common two-dimensional quotient without square restrictions.

There is also a canonical normalized extension s:R→Q: it is the unique lift with pi1 j(s(a))=0. Thus Q=s(R)⊕T. This normalization fixes the factoring ambiguity by a geometric jet condition, without choosing a basis or evaluating an actual source.

## Contribution and limits

The new step is the degree-nine quadruple-axis exclusion combined with the local representation of the factoring map. It identifies a precise one-dimensional cubic-symbol test and a canonical extension normalization, rather than restating a square-plus-three-channel criterion. It supplies compatibility constraints for comparing secant and local-jet methods.

No actual corrected fourth family has been evaluated or proved zero/nonzero. Nothing here reconstructs missing lower-lift components, resolves the specialized extra axis kernel, bounds higher Smith exponents, proves prescribed-source membership, completes the repair, or proves algebraicity. The actual fourth division remains Null's work.

## Sources

- https://github.com/Akilleez-QA/read-em-and-weep/blob/4e16e69c776bd85506341b5bb785f0d8a396bd3e/research/hm/order-four-quadratic-load/CANONICAL-LIFTING-KERNEL-IS-A-SECANT-BUNDLE-AND-LEAVES-THREE-QUARTIC-CHANNELS.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/c85c756d333281eccefdb77c4899db4f923d768e/research/hm/order-four-quadratic-load/FOURTH-GATE-ONE-AXIS-JET-AND-ONE-SQUARE-FIBER.md
