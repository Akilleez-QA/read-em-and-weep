# Independent review of the internal cubic gate

## Verdict and scope

No mathematical blocker found in the stated conditional theorem. Under the actual full-J Type II hypotheses, the internal third is a global cubic morphism in a canonical two-dimensional linear space, and its generic nonvanishing is equivalent to that of the original fourth Bockstein on the surviving D kernel. Neither nonvanishing nor occurrence is established, and the specialized extra A kernels are not computed.

## Substantive checks

1. **Global normalization.** The raw internal second residual is a global quadratic D-valued polynomial whose projection to E is zero by PR979. The first multiplication map is an injective subbundle map, so its inverse on the image gives a unique global linear A-valued polynomial. Subtracting that kernel correction retains the first lifting equation and makes the second residual genuinely zero in H1(S), permitting a second S-valued correction through the fixed Q inverse. This avoids rational division by a selected coefficient.
2. **Independence.** Two normalized first corrections differ by a kernel-valued linear polynomial. Their vanishing residuals force its A component to vanish by injectivity of multiplication. Its D component changes the third residual by the internal second applied to that D-valued polynomial, hence zero modulo the first image. Changing the second correction adds only the first image. These statements suffice for global well-definedness and equivariance of r.
3. **Higher naturality.** On the rank-four open, the quotient first symbol is onto. A quotient first-kernel class can therefore be lifted to every prescribed finite order after cancelling Q-contractible pairs. Applying a radical chain map with nonzero scalar degree-zero action gives the internal third naturality relation on this open. Extending a morphism into a vector bundle proves r kappa(-2)=0 globally. This does not require kernel formation to commute with specialization at the ten exceptional quotient directions.
4. **Nonzero restriction.** The proposed cubic map Delta times pi rho is equivariant. At a general square, the nonzero sextic Wronskian gives vanishing sequence (0,1,2), so the unique tangent section v has exactly double contact. Thus h=v/l^2 is not divisible by l. In universal coordinates l=x, rho(x^2)h modulo x^2 Sym2 W is 8 h4 x y^3 and is nonzero. Hence pi rho kappa is not identically zero. Multiplication by the nonzero discriminant cannot kill this map on the integral parameter surface, despite its vanishing at every square. The restriction therefore has rank one, leaving precisely two dimensions from the raw three-dimensional Hom space.
5. **Rank-one exclusion.** Saturation of a generic rank-one image is reflexive by the depth lemma, hence O(k). G-stability gives its linearization, with no character ambiguity for A5. The possible interval is -3 through 1; only k=-1 and k=1 support a source D channel. The former is excluded by H0(E(1))^G=0 and the latter by H0(E(-1))=0. Every nonzero equivariant cubic map is therefore generically onto E.
6. **Original fourth comparison.** The normalized S corrections are legitimate first and second corrections in M. A third M correction projects to a quotient Q-cycle whose connecting image is minus the internal cubic residual. Projection of its fourth residual is consequently -bbar_T delta^-1 r, with the correct original second-image quotient. Original first and third vanish; no additional earlier page image has been omitted. This assertion is needed only on the common dense open where the surviving original kernel is D.
7. **Higher terms.** After the stated normalization, s1 and s2 vanish on D in a compatible reduced block model. In the complete quartic coefficient of -q delta^-1 s, every term other than -q1 delta0^-1 s3 contains s1 or s2. Thus there is no missing term from q2, q3, delta1, or delta2. The direct correction proof independently establishes the same sign and target.
8. **Equivalence, not selection.** The induced quotient-first map on E has rank one generically. A nonzero r is generically onto E, so its composition is nonzero. Conversely zero composition forces r to have rank at most one and hence to be zero. This proves the equivalence without choosing either outcome.

## Frozen bytes and execution

Independently read the checker and ran both normal and optimized Python. Both passed **48** checks and produced byte-identical output to `RESULT.json`. The checker authenticates all three input copies by SHA256 and Git blob, computes exact A5 characters, checks the universal square residue, and verifies synthetic correction equations and the full noncommutative quartic expansion. No actual HM instance was evaluated.

- PROOF.md: `064b115e5b583ecb98c5d6fae5ca84fc54424c775fbad7d7578fa816f25b4acb`
- verify.py: `365e1adbb38fbf35f727135d70330539c2a5f32dc41f7437531b1191ed10e38f`
- INPUTS.json: `87e8c28e35d41b4d024f8a0493f972ba063480ee3650f305c75ae4a580e218a6`
- RESULT.json: `2338361d415828203ac7a381057a149fe8d8953ad5103bed55fce4ae6e72f27b`

The review is conditional on the pinned mathematical dependencies. Exact finite tests are supporting evidence, not proof-assistant certification of the whole geometry or a completed original proof repair.
