# Independent audit of the equivariant local realization

Verdict: PASS for PROOF.md Sections1–6 at SHA256 `880f722f146b05f78d32c2084d5de32e5a02d5bdb8c85b29f156c1aeb9cf5583`.

## Matrix and symmetry

Independently expand the exterior products of the relation columns. For ε=−1,

    Σ_i L(m_i)∧L(l_(3i)) = λ L(c1)∧L(c2).

The four terms are −λx1x2 t3∧t4, −λx2x4 t1∧t3, +λx1x3 t2∧t4, and +λx3x4 t1∧t2. The clock product has exactly these four coefficients divided by λ. Thus choosing its pairing coefficient −λ cancels all six upper-triangle entries, establishing LJLᵗ=0 without specialization.

The four m/l pairs and the clock pair have disjoint supports, so det J=λ² and J is invertible. Their B-weights are opposite. The C4 generator simultaneously cycles the m/l pairs and sends c1→c2→−c1; both alternating blocks are invariant. The relation representation has trivial central character. Hence the pairing is invariant for the full stipulated H, not merely B or the order-twenty subgroup.

## Exactness, depth and self-duality

The accepted finite-length candidate input makes L surjective off the closed point. Its transpose, and hence JLᵗ, is a split injection there and an injection everywhere because its domain is free over the domain R. At each nonmaximal prime, the symplectic reduction is locally free of rank10−2·4=2.

With I=im L and K=ker L, the depth-lemma values depth I=1 and depth K=2 follow from finite nonzero P and free modules of depth four. The quotient sequence 0→A*→K→M→0 gives depth M≥2. Any torsion is supported at the closed point and would have finite length, contrary to positive depth. M is therefore torsion-free and S2, hence reflexive over the regular normal ring. The orthogonal-complement identity K=(im JLᵗ)^⊥ gives a perfect alternating form on the punctured quotient. The form and its inverse extend across codimension four between reflexive modules. This proves equivariant alternating self-duality and equivariantly trivial determinant, not merely an untwisted numerical Chern condition.

## Both defects

Dimension shifting gives I*=A*, Ext¹(I,R)=Ext²(I,R)=0 and Ext³(I,R)=D(P). Consequently K*=E*/im Lᵗ, Ext¹(K,R)=0 and Ext²(K,R)=D(P). Dualizing the quotient sequence identifies Ext¹(M,R) with the cokernel of the map induced by LJᵗ. Its image is im L because Jᵗ is invertible; it descends through im Lᵗ because LJᵗLᵗ=0. Thus Ext¹(M,R)=P and Ext²(M,R)=D(P), equivariantly and with the canonical character already included in D. Both lengths are sixteen, so M is nonfree precisely at the closed point.

## Uniqueness and parameter distinction

The two constant invariant alternating blocks are exhaustive: the distinct dual irreducibles O2/O3 occur once, and the irreducible clock pair has its one alternating pairing for ε=−1. Isotropy forces their coefficient ratio b=−λa, so the admissible nondegenerate pairing is unique up to scalar. Such scaling leaves the quotient module unchanged.

An H-equivariant R-linear isomorphism M_λ≅M_μ would induce one on Ext¹ and hence a scalar isomorphism on its irreducible top T. Because R and its action are fixed, the induced map on first-order free generators is that same scalar; the initial linear relation lines must coincide. The two normalized coefficients force λ=μ. Higher-order corrections cannot change those initial relation spaces. This proves pairwise distinct equivariant isomorphism classes, without asserting representability or classification.

## Scope

This is a new universal local realization, so the old statement that the candidate has no known reflexive realization is superseded for ε=−1. It does not produce an actual HM kernel or settle any prescribed global Chern/cohomology/source requirements. The ε=+1 observation excludes only this invariant constant-pairing ansatz, not all realizations. No actual-source evaluation, compiler run or formal proof-assistant check was used in this audit. GLOBAL-CONE.md is a separate extension and is not covered by this verdict.
