# A finite order-nineteen gate for the last two odd pencil survivors

## Statement and scope

Let A=H1(B(2))_- have dimension 44 and D=H1(B(4))_- have dimension 48. Fix the actual invariant positive equation q0. Over the generic negative quadratic q, consider the actual linear pencil

M(t)=m_q+t m_q0 : A -> D.

All assertions below concern the generic negative parameter, not every selected negative quadratic. Suppose the actual first Bockstein has rank four, equivalently the residual smoothing map has generic rank two. The known negative map has rank 38. Then exactly one of the following holds:

1. For some e with 2 <= e <= 19, the e-th Bockstein has rank two. The intervening higher Bocksteins vanish, both remaining survivors die together, and M(t) has generic rank 44.
2. Every higher Bockstein vanishes. The actual pencil has generic rank 42 and a two-dimensional kernel over the rational function field in q and t.

In particular, testing the canonical higher obstructions through order nineteen suffices. If both survivors lift through the equation modulo t^20, they genuinely survive over the formal fraction field and the rational pencil has kernel dimension two. This does not evaluate any higher obstruction. It does not settle the other even-parity block or claim complete proof repair. The improved bound uses the actual source and target representation multiplicities in addition to pencil linearity and parity. No sharpness for the full actual HM data is claimed.

## 1. Existing results and the distinct new issue

FULL-ADJOINT-PENCIL-INVOLUTION-BLOCKS.md proves the actual 44-to-48 odd ambient presentation. HYPERPLANE-ADJOINT-EXHAUSTION-AND-SIX-TO-TEN.md identifies its negative rank 38 and its first Bockstein with the actual six-to-ten smoothing gate. RESIDUAL-SMOOTHING-NONVANISHING-AND-EVEN-RANK.md proves the residual rank is two or four. Off the negative discriminant, the projected channel adds rank two, so the residual-rank-two case gives first Bockstein rank four.

ODD-FIRST-SCALING-OBSTRUCTION.md and ODD-SECOND-SCALING-OBSTRUCTION.md concern a different finite normal-scaling family and its first two boundaries. They do not provide the finite endpoint proved here for the ambient linear pencil in t. No identification of t with their epsilon or epsilon squared is made.

## 2. Canonical higher obstruction construction

Work first over K=C(q), the function field of the affine negative quadratic space. For r>=1 let K_r consist of leading vectors x0 for which there exist x1,...,x_(r-1) such that

M(t)(x0+t x1+...+t^(r-1) x_(r-1)) = 0 modulo t^r.

Thus K_1=ker(m_q). The canonical successive obstruction d_r has domain K_r and target C_r, the surviving degree-one space of the t-adic Bockstein spectral sequence of the two-term complex [A[[t]] -> D[[t]]]. Concretely its representative is the coefficient of t^r of M(t)x(t), modulo the ambiguity from changing earlier lifts. This quotient, not a chosen complement in D, defines C_r. Its kernel is exactly K_(r+1). Starting with C_1=coker(m_q), each page replaces domain by the kernel and target by the cokernel of d_r.

The first page has dimensions 6 and 10. Rank(d_1)=4 leaves dimensions 2 and 6 on page two. This construction retains all successive correction terms. The fact that M is linear does NOT make d_r zero for r>=2: earlier corrections can create arbitrarily delayed obstructions subject to the bound below.

## 3. Why every generic higher rank is even

The full negative quadratic affine space X=Sym^2 W is center-even. The coefficient q0 is G-invariant. Every finite-jet lifting equation above is G-equivariant, and all source and target jet sheaves have center acting as minus identity. Kernels, images, and quotients inherit that central action. The canonical higher-obstruction sheaves and their generic images therefore remain center-odd.

Any such generic image of rank r can be represented by an equivariant coherent torsion-free sheaf on X; the finite-jet construction supplies one, or it can be obtained by saturation. Its reflexive determinant is an equivariant line bundle on the smooth affine three-space X. Every line bundle on X is trivial. A G-linearization of the trivial line bundle is a character, since the only units of C[X] are constants. Since G=SL2(F5) is perfect, this character is trivial. But the central character of the determinant is (-1)^r. Hence r is even.

This argument uses the family over X, not a fictitious G-action on a fixed general q. It applies separately at every finite Bockstein page. From a two-dimensional domain, a nonzero higher obstruction must therefore have rank two, killing both survivors at once.

## 4. Smith factors and the finite bound

Over the discrete valuation ring K[[t]], the matrix of M has Smith normal form. Its 38 unit factors account for rank(m_q)=38. The first Bockstein rank four accounts for exactly four factors with valuation one. The two remaining columns have either nonzero factors t^e_i times units with e_i>=2, or zero factors.

The rank of d_r is the number of Smith factors of valuation r. By the parity result, the remaining two factors cannot have distinct finite valuations, nor can precisely one be zero. They are either both zero or both have the same finite valuation e>=2.

In the finite case M has full column rank 44. The minimum t-adic valuation among its nonzero 44-by-44 minors equals the sum of its Smith valuations, namely 4+2e. The invariant coefficient m_q0 has rank at most 42, as proved below. Every 44-minor consequently has degree at most 42 in t. Its order of vanishing cannot exceed its degree. Therefore

4+2e <= 42, hence e <=19.

This also proves the finite endpoint: if d_2 through d_19 vanish, finite Smith factors are impossible, so the last two factors are zero. Scalar extension between K(t) and K((t)) preserves rank, giving the claimed rational pencil kernel. No chosen lifts are asserted to equal globally convergent sections; the conclusion is algebraic generic rank.

## 5. Actual representation improvement from twenty to nineteen

The exact ambient Euler character, together with the established cohomology concentration at twists two and four, gives

A = 2W + 2W-prime + 3S4 + 4T6,
D = 3W + W-prime + 4S4 + 4T6.

Here S4 and T6 are the binary irreducibles of dimensions four and six. The verifier independently computes these multiplicities from the existing equivariant monad K-class via chi(B(t))=chi(F tensor F(t+1))-chi(O(t)); only the center-odd constituents are retained. Because q0 is invariant, Schur decomposition bounds its rank by

rank(m_q0) <= 2 min(2,3)+2 min(2,1)+4 min(3,4)+6 min(4,4)=42.

For completeness, the degree bound is universal: in a minor of A+tB, the coefficient of t^k is a sum of determinants selecting k columns from B and the other columns from A. If k>rank(B), each selection has linearly dependent selected B-columns and vanishes. This applies to every row restriction as well. Thus each 44-minor has degree at most rank(m_q0), which is at most 42. This is an upper bound from representations, not an assertion that the actual rank is 42.

## 6. Why sizes and parity alone would only give twenty

Let N20 be the regular nilpotent 20-by-20 Jordan matrix. Its pencil N20+t I20 has nineteen unit Smith factors and one factor t^20: a superdiagonal 19-minor is a unit and its determinant is t^20.

Take the direct sum of this pencil with t I2, tensor the result with the binary two-space W, and enlarge the target by W tensor C^2 with zero components. This is an abstract G-equivariant center-odd 44-to-48 linear pencil. At t=0 its rank is 38; its first Bockstein has rank four; its final rank-two obstruction occurs at order twenty. This is a universal example showing that an order-nineteen bound does not follow from the sizes and parity hypotheses alone. The example has coefficient rank 44 and therefore does not satisfy the additional actual representation bound rank(m_q0)<=42. It is not a model or evaluation of the actual HM coefficients, and no compatibility with their full representation decomposition is claimed.

Reproduction: python verify_odd_pencil_bockstein_bound.py. The verifier checks the exact numerical bounds and the abstract Smith-factor certificate; no actual coefficients, matrices, ranks, or higher boundaries are evaluated.
