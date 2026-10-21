# Independent audit of nonsquare Galois pairing of the cubic gates

Reviewed final PROOF.md SHA256: `3fe58cc05417e8471cfe73d8f2faa16409e3ae1d074e29a660073178b4eee088`.

Verdict: PASS for the final PROOF.md and the mathematical argument below, conditional on the pinned geometric and representation inputs of PR615 and PR616. This is an independent mathematical audit, not formal verification. No selected HM coefficient, point value, derivative, matrix, numerical rank, or source-instance evaluation was performed.

## 1. The field-of-definition issue

The cubic construction at issue depends only on the thirty Heisenberg eigenlines, not on a subsequently chosen HM section or coefficient. Choose a universal Schrödinger realization over K=Q(zeta), where zeta is a primitive fifth root, with basis e_i, i in F5, and operators

    g e_i=zeta^i e_i,   s e_i=e_(i+1),   h e_i=zeta^(i^2)e_i.

This is a representation model, not an evaluation of the geometric obstruction. Every noncentral direction operator has order five, has its distinct eigenvalues in K, and has one-dimensional eigenspaces over K. The union Z of the thirty eigenlines is therefore a reduced K-scheme. Its identification with the actual configuration is the pinned input. Transport through that identification does not require the original ambient coordinates themselves to be K-rational.

The blowup of Z, the line bundle 3H-E, its complete section space and morphism, and its scheme-theoretic image are defined over K. Their complex base changes are the specified M,D,V,L. Cohomology and the finite linear maps used here commute with field extension. The normalization map and its quotient, the sheaves of first-order differential operators, their section-evaluation maps, their cohomology maps, and the successive image/kernel/quotient constructions defining b are intrinsic. In particular they are compatible with semilinear automorphisms of this K-model. The argument does not assume a K-form for an unrelated HM bundle, its section data, or the original fixed source.

Both coefficientwise sigma:zeta->zeta^2 and the rational permutation P:e_i->e_(2i) preserve Z. Indeed sigma normalizes the Heisenberg group by g->g^2,s->s, and P normalizes it by g->g^3,s->s^2. Hence their composition acts on the canonical geometry and on the obstruction map. A branch ordering or a trivialization of an obstruction line is not required: those quotient sheaves and the map b were defined before such choices.

## 2. Conjugation identities

For J=P sigma, the exact identities in the universal representation are

    J g J^(-1)=g,
    J s J^(-1)=s^2,
    J h J^(-1)=h^3.

For the last identity, sigma sends h to h^2, while P h P^(-1)=h^4. Thus P h^2 P^(-1)=h^8=h^3. The first identity is P g^2 P^(-1)=g^6=g. These are identities of semilinear operators, not assertions that J belongs to the complex-linear symplectic normalizer. J acts on scalar zeta by zeta^2, which is essential.

The same conjugation identities hold on the naturally associated source and target representations, with the usual covariant convention for the induced group action. Equivalently one may obtain them directly by transporting sections with coefficientwise sigma followed by the inverse-coordinate pullback of P; the resulting map is sigma-semilinear. Scalar changes in a line-bundle linearization cancel in the Hom obstruction spaces.

## 3. Character and shear transport

All character-space calculations are over K. Their zero/nonzero conclusions and dimensions are preserved by extension to C, so no extension of sigma to C is needed.

Choose a nontrivial U-character chi whose kernel is the g-direction, so chi(g)=1 and chi(s)=zeta^k for k nonzero. If v lies in this character space, then

    g Jv = J gv = Jv,
    s Jv = J s^3 v = sigma(zeta^(3k)) Jv = zeta^k Jv.

Thus J preserves this same chi-space; it does not merely move it to a different character requiring an unspecified identification.

If also h v=zeta^t v, the identity J h^2=h J gives

    h Jv = J h^2 v = sigma(zeta^(2t)) Jv = zeta^(4t) Jv.

Therefore J interchanges the shear lines 1 and4, and separately 2 and3. This uses the nonsquare cyclotomic automorphism. Replacing it with ordinary complex conjugation would not justify the same interchange.

## 4. Passage to the gates

The canonical map b is J-equivariant in the semilinear sense. The source and target lines at each t are one-dimensional by PR616. Restricting b J=J b to such a line gives a commuting square with bijective semilinear vertical maps from the t-channel to the 4t-channel. Consequently beta_t is zero if and only if beta_(4t) is zero. This is a statement about zero versus nonzero maps, not about an unchosen numerical scalar value, equality of scalar values, or a complex-linear intertwiner between the two irreducible channels.

It follows that beta_1 and beta_4 vanish together, and beta_2 and beta_3 vanish together. The latter is the new residual-descent restriction. PR616 already proves that at least one normalization gate is nonzero; hence this argument also gives both normalization gates nonzero independently of the two-pentad geometric proof.

With q=2, the number r of nonzero full gates is either2 or4. The formulas of PR616 then give rank b equal to48 or96, dim ker b equal to48 or0, and embedded tangent dimension equal to147 or99. Dimension123 is rigorously excluded. No conclusion that the two remaining descent gates are nonzero follows merely from their being paired.

## 5. Scope

The new input is arithmetic semilinear symmetry of the canonical eigenline construction. It is not part of the complex-linear full-normalizer symmetry analyzed in PR617, so there is no contradiction with that note's independent abstract scalar choices. Abstract complex-linear equivariant maps need not commute with J. The result leaves the one remaining common descent zero/nonzero decision unresolved and makes no higher-order integrability, smoothness, original-source, full-adjoint, or algebraicity assertion.
