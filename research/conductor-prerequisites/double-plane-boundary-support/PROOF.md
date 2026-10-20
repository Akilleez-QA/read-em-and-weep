# Double-plane annihilators admit no complete nonconstant support curve

Work over C. This is a universal argument in linear algebra and algebraic geometry. No source operation, physical instance, rank experiment, or computational evaluation is used.

## Statement and conventions

Let E have dimension four, fix a nonzero covector x in E*, put Q=x² and K=ker(Q:Sym²E→C), and let v:K→E be linear. Suppose v has no compatible square: for every nonzero e with x(e)=0, one has v(e²) not in Ce.

There is no complete integral curve T with a nonconstant support map a:T→P(E*) such that, at every t, there exists a five-dimensional subspace

    K_t ⊂ K ∩ Sym²(ker a_t),    v(K_t) ⊂ ker a_t.

Products of covectors are interpreted as polynomials: (aℓ)(e²)=a(e)ℓ(e). For a covector ℓ, the shear is S_ℓ(ef)=(ℓ(e)f+ℓ(f)e)/2, so S_ℓ(e²)=ℓ(e)e. In particular adding or subtracting a shear preserves square avoidance.

## 1. Rational division and its intrinsic quotient

Normalize T. It is now a smooth complete integral curve. Let L=a*O(1), and regard the universal covector as a quotient E⊗O_T→L. Choose a fixed linear extension V:Sym²E→E of v.

Except over the support value [x], Q restricted to ker a_t is nonzero. Therefore K∩Sym²(ker a_t) has dimension five, equals K_t, and a_t V restricted to Sym²(ker a_t) is proportional to Q. Regular proportionality and division by the universal covector, as in Sections 2–3 of https://github.com/Akilleez-QA/read-em-and-weep/blob/4dc50d6f057d1120a1c772316b2e3b961601efab/research/hm/middle-surface/rank-one-boundary-support/PROOF.md, give

    a V = λ x² + a ℓ.                                      (1)

Here λ is a rational section of L and ℓ is a rational function on T with values in E*. Both are regular away from the finite inverse image of [x]. The divided covector ℓ is a section of the trivial E* bundle, not a twisted bundle: scaling a and λ by the same transition unit leaves ℓ unchanged.

If this inverse image is empty, ℓ is globally regular, hence constant. Equation (1) on K then puts (v−S_ℓ)(K) in the intersection I of all supports, of dimension at most two. Section 4 of the cited proof gives a compatible square. Thus it remains to treat the case where at least one point lies over [x].

Fix a decomposition E=Cz⊕H, where x(z)=1 and H=ker x. Extend covectors on H by zero on z. This identifies E*=Cx⊕H*. Write the quadratic polynomial components of the fixed V as

    x V = A x² + x p + P,
    V_H = h x² + x M + N,

where A∈C, p∈H*, P∈Sym²H*, h∈H, M is an H-valued linear polynomial on H, and N is an H-valued quadratic polynomial on H. These are fixed objects, independent of the point of T. In particular P=(x V)|Sym²H.

## 2. Local coefficient identity at an exceptional point

Let R=O_{T,t} at a point over [x], let τ be a uniformizer, and use the affine support chart normalized by a(z)=1. Then

    a=x+b,    b∈H*⊗R,    b=τ^k B,

for some k≥1 and B with nonzero residue B₀∈H*. Nonconstancy ensures b is not the zero rational function, so k is finite. Write ℓ=cx+d, with c∈Frac(R) and d∈H*⊗Frac(R).

Compare the xH and H² coefficients in (1). The λx² term affects neither comparison. With b(M) and b(N) denoting contraction of their H-valued outputs by b, the exact identities are

    d = p + b(M) − c b,                                   (2)
    P + b(N) = b d.                                       (3)

Consequently

    c b² = −P + b p − b(N) + b b(M).                       (4)

There are no extra factors of two in these formulas: x p denotes the polynomial x(e)p(e), consistently with the shear convention above. The terms on the right other than −P have coefficient valuations at least k (and the last term at least 2k).

For a vector of polynomial coefficients, valuation means the minimum valuation of its coefficients. Since B has nonzero residue, B² also has nonzero residue, so val(c b²)=val(c)+2k whenever c≠0.

### Case P=0

Equation (4) gives val(c)+2k≥k, hence val(c)≥−k; if c=0 the conclusion is immediate. Thus cb is regular, and (2) shows d is regular. Therefore ℓ modulo Cx is regular at this point. This conclusion holds at every exceptional point, with no restriction on k.

### Case P≠0

The right side of (4) has valuation zero, so val(c)=−2k. Put c=τ^(-2k)u, where u∈R is a unit. Equation (4) implies

    u B² ≡ −P    modulo τ^k.                              (5)

Reducing modulo τ gives P=−u(0) B₀². In particular P is a nonzero scalar multiple of a square. The line C B₀ is therefore determined by the fixed P and is the same for every exceptional point, including different branches of a singular support image.

We need the stronger consequence that B modulo C B₀ vanishes to order at least k. Choose a constant basis of H* whose first member is B₀ and write

    B=s B₀+D,

where s is a unit of R and D has values in the constant complementary span. Since P is a scalar multiple of B₀², comparison of the B₀ times complementary-basis coefficients in (5) gives

    2 u s D ≡ 0    modulo τ^k.

As 2us is a unit, D∈τ^k(H*⊗R). Hence b modulo C B₀ is divisible by τ^(2k). Since c has pole order exactly 2k, cb modulo C B₀ is regular. Equation (2) now shows that d modulo C B₀ is regular. Equivalently,

    ℓ modulo span(x,B₀) is regular at this point.           (6)

This proves the required pole-direction statement at arbitrary contact order and without choosing a square root of a unit. The normalization accommodates arbitrary ramification and multiple branches.

## 3. Global constancy in the fixed quotient

If P=0, put D=Cx and W=ann(D)=H. If P≠0, choose the common square-root direction B₀ of P and put D=span(x,B₀) and W=ann(D), of dimension two.

The local calculation proves that ℓ modulo D is regular at every point over [x]. It is already regular elsewhere. Hence it is a global regular map from the complete integral curve T to the fixed vector space E*/D, and is constant. Choose a constant lift ℓ₀∈E* of this value. Then

    ℓ−ℓ₀ ∈ D⊗C(T).                                     (7)

Set F=v−S_ℓ₀ on K. Since W⊂H, Sym²W⊂K. Equation (7) makes the shear S_(ℓ−ℓ₀) vanish on Sym²W. Restricting the full ambient polynomial identity (1), not merely its moving-hyperplane restriction, gives

    a F|Sym²W = 0

generically. This regular bundle-section identity extends everywhere. Therefore

    F(Sym²W) ⊂ I := ⋂_t ker a_t.                         (8)

## 4. The common support intersection lies in W

As the curve meets [x], x belongs to the vector span J⊂E* of all its support covectors; thus I=ann(J)⊂H. Nonconstancy gives dim J≥2 and dim I≤2.

When P≠0, also B₀∈J. Indeed, on any exceptional branch, the normalized representatives a=x+b belong to the constant subspace J over R: every constant linear equation defining J vanishes on a at all ordinary points and hence identically. Since x∈J, b lies in J⊗R. Dividing by τ^k and taking the residue shows B₀∈J. Thus in this case I⊂ann(x,B₀)=W.

## 5. A compatible square in either case

If P=0, W=H has dimension three, and (8) gives a linear map F:Sym²H→I with dim I≤2. Its coordinates are at most two homogeneous quadratic polynomials on H. These have a common projective zero in P(H)=P² over C. For completeness, their ideal has height at most two; if their affine zero locus were only the origin, its radical would have height three, a contradiction. Thus some nonzero e∈H satisfies F(e²)=0. It follows that e²∈K and v(e²)=ℓ₀(e)e, a forbidden compatible square.

If P≠0, W has dimension two and (8), together with I⊂W, gives F:Sym²W→W. The map

    e ↦ e∧F(e²)

is a homogeneous binary cubic valued in the one-dimensional vector space det W. It is either identically zero or has a zero in P(W), since C is algebraically closed. Hence some nonzero e∈W has F(e²)∈Ce. Since e²∈K and the shear contributes ℓ₀(e)e, again v(e²)∈Ce. This is the required contradiction.

## Scope

The proof excludes every complete nonconstant support curve for the double-plane annihilator Q=x² under the stated five-plane incidence and square-avoidance assumptions. It includes nonlinear images, singular support images, multiple branches over the exceptional value, and arbitrarily ramified support maps. It does not require a regular choice of the spaces K_t.

Combined with https://github.com/Akilleez-QA/read-em-and-weep/blob/4dc50d6f057d1120a1c772316b2e3b961601efab/research/hm/middle-surface/rank-one-boundary-support/PROOF.md and its distinct-factor ADDENDUM.md, it excludes such curves for every nonzero scalar annihilator quadric Q on a four-dimensional E. This combination concerns the abstract support incidence only; applications to another geometric locus must separately establish that its fibers supply these hypotheses.

## Conditional integration: descent of a boundary curve to a normalized surface

The following is a conditional geometric consequence, not an assertion that all its application-specific premises have been established here.

Assume the following data and independently verified facts:

1. B is the integral projective, generically good middle surface in the full-flag setting of https://github.com/Akilleez-QA/read-em-and-weep/blob/4dc50d6f057d1120a1c772316b2e3b961601efab/research/hm/middle-surface/flag-boundary-resolution/PROOF.md, with the global repeat-injectivity hypothesis used there. The global ambient vector space V has dimension five. Its rational support map has target P(V*); the four-dimensional E in the local theorem above is a local middle space, not this global ambient V. Let Γ⊂B×P(V*) be the reduced support-only graph closure, and let Z⊂B be the closed bad locus.
2. Import the separately established limiting-support and correction-incidence results in this setting: residual rank at least three gives a unique support value; rank two gives at most six values; rank one supplies exactly the local five-plane incidence and square avoidance treated above and in the cited rank-one notes; and rank zero is impossible. At rank one, a positive-dimensional projective support fiber would contain an integral complete curve, so the abstract exclusions prove finiteness there. These facts together show that every support-only graph fiber is finite.
3. Let f:Y→B^ν be the smooth projective full-flag resolution, where B^ν is the normalization of B. In the notation of that full-flag proof, h is the middle hyperplane class and already has the form f*h_B for a Cartier class h_B on B^ν. The class n is the support hyperplane class on Y. Its descent will be proved below rather than assumed.
4. There is an effective divisor A on Y supported over Z, and an established intersection inequality

       A·(n+h) ≥ deg(B) > 0.

Then the support map extends regularly to B^ν. Indeed Γ→B is proper and has finite fibers, hence is quasi-finite and therefore finite. It is birational because it is a graph closure. The normalizations of Γ and B are consequently canonically isomorphic: the normalization of the finite birational Γ→B is the normalization of B. The second projection of Γ thus defines a regular support map B^ν→P(V*).

In particular n=f*n_B for the Cartier support hyperplane class n_B on B^ν: the support maps on Y agree generically and hence everywhere. Together with the already descended middle class h=f*h_B, this gives n+h=f*L_B for L_B=n_B+h_B. Any f-exceptional curve contracts to a point and has zero intersection with f*L_B. Let

    D_B=f_*A

be the effective Weil divisor on B^ν obtained by pushing forward the divisor cycle. The projection formula for the Cartier class L_B gives

    D_B·L_B=A·f*L_B=A·(n+h)≥deg(B)>0.

Thus D_B is nonzero. It is supported over the bad locus, so that locus contains a curve; it cannot consist solely of isolated points. The quantitative inequality descends to an actual effective boundary curve on the normalized middle surface. This conditional integration imports the stated previously established geometric premises; it is not a new realization result, does not establish existence in dimension seven, and makes no universal dimension-six bound claim.
