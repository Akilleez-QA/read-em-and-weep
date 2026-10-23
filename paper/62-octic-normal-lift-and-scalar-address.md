# A canonical polynomial octic lift and an exact scalar address

**Craig Ward · 23 October 2026 · Update through PR1013**

[PR1013](https://github.com/Akilleez-QA/read-em-and-weep/blob/9f3509ff76b9f1fbb5d61288aa0ae036b5c16aca/research/hm/source126-typeII-octic-normal-lift/PROOF.md) constructs a fixed universal polynomial representative of the octic gate and a gauge-independent rule for extracting its scalar from a supplied lift. **No actual lift is supplied, and the actual scalar is not computed.** This is a reproducible specification for the missing calculation, not its result.

## 1. Lift, target factor and projected map are different objects

Let B_a:A O(-1)→D O be multiplication, π its quotient to E, and C=b_T the quotient multiplication family. The signed maximal-minor column κ generates the kernel sheaf of C, including at its ten reduced rank-drop points. Its quotient πκ is nonzero and spans the invariant target line; normalize σ=πκ. For the canonical quartic row ψ, put

    R=κψ,   CR=0,   R²=0,   πR=σψ=g₈.

The squared identity includes the homogeneous degree twist. It does not make R an endomorphism of E: R need not preserve the multiplication subbundle.

The cofactor column has ten reduced order-three zeros, and ψ has six reduced order-five zeros, with disjoint supports. Their product matrix therefore has **sixteen reduced zeros**. The projected generator g₈ instead has length46: its six order-five local ideals are (u,v)³. The target factor σ alone has length34, with local ideals (u²,v²) at those six points. These three lengths describe three different maps, not competing counts. All are nonzero on the square conic away from the distinction between an actual zero scalar and a universal generator.

## 2. Unique normal form removes lift ambiguity

Every homogeneous polynomial lift L whose quotient is in the canonical octic line has a unique decomposition

    L=B U+αR,

where U is a 3×5 matrix of plane-degree-seven polynomials and α is constant. Exactness gives the global factor U, not merely a rational solution. Applying π proves uniqueness of α, and injectivity of B proves uniqueness of U. The preimage has dimension541 inside the 1125-dimensional space of polynomial octic matrices, without imposing equivariance.

The C-annihilated lift of αg₈ is uniquely αR. A monic-chart remainder matrix annihilates every BU term, furnishing a quotient-based extraction algorithm that verifies the entire quotient identity and rejects an off-line candidate. Its synthetic tests do not supply the missing actual L.

## 3. The pinned normalization gives a single coefficient formula

Use a=px²+qxy+ty² and ascending y-exponents for the binary bases. The package authenticates the universal quotient projection P₆, constructs its invariant apolar quotient pairing, and exports all 25 entries of R over Q(√5). In these exact coordinates,

    [p⁰q⁸t⁰] R₀₀ = −1/27,
    α = −27 [p⁰q⁸t⁰] L₀₀.

The first row of B is (p,0,0), so every (BU)₀₀ is divisible by p and has zero pure q⁸ coefficient. This proves the formula is independent of the lift gauge. Its value depends on the stated universal normalizations; an actual lift must first be identified in those coordinates. The actual coefficient on the right has not been obtained or evaluated.

The package has independent full-proof review and 186 checks in both normal and optimized Python, with exact regeneration of both matrix exports. It computes universal polynomial coefficients, not an actual HM parameter point or actual obstruction value. The original repair, actual full-J occurrence, later internal symbols and four-pair/three-label frontier remain unresolved.
