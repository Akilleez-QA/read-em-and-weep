# Historical review receipt

This receipt reviews the original full manuscript, including conditional applications not claimed in this universal unit. It does not certify these normalized publication bytes.

# Independent audit: isotropic four-dimensional kernel exclusion

## Verdict and frozen inputs

PASS. The proof establishes its stated complex-algebraic theorem: a four-dimensional linear subspace K of sl(U), dim U=3, with no nonzero rank-one element cannot have tr(A²) identically zero. The stronger intermediate statement that a projective integral surface cannot consist entirely of regular nilpotent classes is also proved.

This audit is bound to these SHA256 hashes:

- the isotropic four kernel exclusion manuscript: `bb94740ee18d4f0895c39786e2d8bb9358eb39243b500ba3cc72bca7fe1cddb0`.
- the constant rank kernel nets manuscript: `8a383ae4203d34a3893334883b9bff791c7c447978cf20fd8ef77d9b3082ad5c`.
- the general three plane kernel manuscript: `76a978a5cd8a2ef4e8d4f497843b38c3cf7c023976078fcbb91ea2511339fca6`.
- the full cubic locus dimension manuscript: `f8a854b2a9f5c8924c5f81e465791a13ff7d8f6f808827cf8a4953baedf5290b`.

Paths are relative to the common parent directory of this audit's directory. The first file is the principal audited proof. For the others, this audit checks the classification and polynomial argument needed for the combined four-dimensional conclusion, and the constant-rank P³ lemma. It does not re-audit all upstream geometric or Massey-operation imports.

## 1. Universal map and positive twists

The tautological inclusion O(-1)→End(U)⊗O gives U⊗O→U⊗O(1), not the oppositely twisted map. For N:E→E⊗M with N³=0 and regular nilpotent fibers, put F1=ker N and F2=ker N². Then

- N(F2)⊂F1⊗M;
- N(E)⊂F2⊗M;
- the induced maps F2/F1→F1⊗M and E/F2→(F2/F1)⊗M are nonzero in every fiber.

Consequently they are line-bundle isomorphisms. For L=F1 the successive quotients are exactly L, L⊗M, L⊗M². This confirms the twist signs independently; there is no splitting assumption.

## 2. Constant rank, kernels, and base change

On the smooth reduced surface, rank-two N and rank-one N² are locally equivalent to split constant-rank matrices. Higher minors vanish as functions because they vanish at every closed point of a reduced complex variety. An invertible maximal minor then eliminates all remaining matrix entries. Kernels, images, and cokernels are locally free and the split presentations commute with arbitrary base change, in particular with fibers.

The inclusion F1⊂F2 is a subbundle inclusion: on fibers it is the usual one-dimensional kernel inside the two-dimensional kernel of the square. Equivalently, E/F1→E/F2 is a surjection of vector bundles with kernel F2/F1. Thus its quotient is locally free and the graded-piece reasoning is valid.

The proof does not attempt to infer these properties from constant geometric rank on an arbitrary nonreduced base, where that inference alone would be invalid. Reduction and smooth resolution explicitly remove this issue. After pulling the map to the resolution, the ranks remain two and one because each fiber is the corresponding original matrix after field extension. No assertion about pulling back a nonsplit coherent kernel is needed: the kernels can be formed anew upstairs.

## 3. Chern arithmetic

Whitney multiplication yields

c1(E)=3l+3H,
c2(E)=3l²+6lH+2H².

Since E is trivial, rational Chow classes give l=−H and then c2(E)=−H²=0. Taking degrees is legitimate on a smooth projective surface. Possible torsion in Picard groups does not affect rational classes or the numerical contradiction. The argument uses only the first two Chern classes; no nonexistent surface degree-three relation is invoked.

## 4. Reduced cubic component, nilpotence, and resolution

For nonzero homogeneous cubic h on K of dimension four, every irreducible component of its projective support is a projective surface. Giving a component its reduced structure produces an integral surface, whether h is reducible or has repeated factors. A nonzero projective representative on this surface has trace, trace-square, and determinant zero. Its characteristic polynomial is t³, so it is nilpotent. Rank-one exclusion makes its rank two, hence its Jordan type is the unique size-three block and its square has rank one.

The universal cube vanishes on the reduced surface, either by Cayley–Hamilton or by reducedness and vanishing at closed points. A smooth projective resolution exists for this integral complex projective surface, including if it is not normal. The map remains regular nilpotent on every fiber upstairs.

For the birational resolution π:X→S, π_*[X]=[S]. The projection formula gives

deg_X(π*c1(O_S(1)))² = deg_S c1(O_S(1))² = deg S > 0.

Ample pullback is not required and is not claimed. Exceptional curves cause no error in this equality. It directly contradicts Section 3's vanishing.

When h is identically zero, the proof restricts to a projective plane in P(K). Every point on that plane is again regular nilpotent and the same surface argument applies. Thus the principal theorem is logically independent of the imported constant-rank P³ lemma.

## 5. Cross-check of the combined four-dimensional existence claim

The additional frozen inputs justify the following combined statement:

For every complex four-dimensional rank-one-free K⊂sl(U), the projective set {det A=0, tr(A²)≠0} is nonempty.

The dependency chain is sound:

1. The principal proof gives q≠0.
2. If h were zero, the incidence is immediately nonempty since q≠0. Independently, the P³ constant-rank lemma excludes h≡0: its line-bundle kernel/cokernel give a−b=−3 and a²−b²=−3, hence (a,b)=(−1,2), whereas the degree-three equation requires a³−b³=−3 rather than −9.
3. For h≠0, absence is exactly V(h)⊂V(q), hence q belongs to the radical of (h). In a polynomial UFD this means every distinct irreducible factor of h divides q. The direction of divisibility is correct.
4. If rank q≥3, q is irreducible over C. A cubic cannot have only this quadratic as its irreducible factor. Hence absence is impossible.
5. If rank q is one or two, all its irreducible factors are linear. Absence would give a linear factor ℓ of h and a three-dimensional subspace ker ℓ with identically zero determinant and no nonzero rank-one element.
6. The constant-rank-net classification is valid: on P² the kernel is O(-1), its three basepoint-free linear entries identify the parameter space with U, and M(x)x=0 gives M(x)=B C(x). Constant rank forces B invertible; trace zero forces B symmetric. Writing B=P P^T proves conjugacy to the full skew-symmetric space. Its trace-square form is −2(x1²+x2²+x3²), of rank three. Thus q restricted to ker ℓ would have rank three, contradicting rank q≤2 on K.

This checks the universal classification needed in step 6, rather than treating it as an unexamined citation. The spectral criterion in the general-kernel proof then converts nonempty incidence into independent ordered zero frames for every *actual structural kernel that has dimension four*, subject to that proof's structural identification and nonvanishing imports.

Moreover, for such a fixed K the incidence is a nonempty open subset of a projective cubic hypersurface in P³, so it has dimension two, and the imported orientation-cover/torus description gives fixed-plane independent-frame dimension five. This dimension consequence does not assert smoothness, reducedness, irreducibility, or global triviality.

## 6. Audit of the appended exact top-dimensional criterion

PASS for Sections 6–7 of the final principal-proof freeze. A nonempty open in a projective cubic hypersurface in P³ is pure two-dimensional in the explicitly stated sense of irreducible-component dimensions. A finite étale cover followed by a locally trivial three-dimensional torus bundle therefore gives a pure five-dimensional frame fiber. These statements do not mistake topological purity for reducedness or smoothness.

The determinant-zero condition on the rank-three kernel stratum is a section-vanishing condition on a vector bundle. Thus B=G4 ∪ {W in G3 : h_W identically zero} is constructible and has a finite locally closed stratification. Every closed geometric fiber of the span map above B is nonempty and five-dimensional, by the two audited universal results. The same dimension holds at generic geometric points: either the arguments apply after an algebraically closed characteristic-zero field extension, or constructibility of fiber dimensions would otherwise give a conflicting nonempty locally closed locus with closed points over C.

For a finite-type surjective map with all geometric fibers five-dimensional, dimension of the source is dimension of the target plus five. Applying this to the finite stratification of B proves dim(Z^(3)|B)=dim B+5 when B is nonempty. The proof's dominant-component explanation is correct: over an integral target, finitely many nondominant component images can be avoided on an open subset; some dominant component must account for the dimension-five generic full fiber. Neither properness nor flatness is needed.

The imported k≤2 bounds are at most nine. For k=3 and h nonzero, the projective cubic has dimension one, the incidence has dimension at most one, and the frame fiber has dimension at most four. The base has dimension at most five, hence this remaining part also has dimension at most nine. No independent part outside B can contribute dimension ten.

Consequently dim B=5 is equivalent to existence of a ten-dimensional irreducible component of Z whose generic triple is independent. Forward: a ten-dimensional constructible piece in the independent open contains an irreducible locally closed piece of dimension ten; its closure is a component because dim Z=10, and it still meets that open. Reverse: the independent open of such a component has dimension ten, and its portion over B must have dimension ten because the complement has dimension at most nine. The dimension formula and dim B≤5 force dim B=5. Empty B makes the existence assertion false without needing an empty-set dimension convention.

This exact equivalence remains conditional on the imported structural full-dimension theorem and bounds. It determines no actual value of dim B.

## 7. Precise limits

- No actual structural kernel is computed or shown to have dimension four.
- No nonemptiness, dimension, generic behavior, or smoothness of the locus of such three-planes in the Grassmannian is established.
- The principal isotropic-exclusion proof alone does not exclude quadratic ranks one or two; the combined argument proves incidence nonemptiness without classifying which quadratic ranks actually occur.
- The argument does not establish additional ten-dimensional components of the full zero scheme, their number, or their multiplicities.
- Actual operation-specific nonvanishing and spectral identifications remain imported where explicitly used.
- All checks are universal algebraic reasoning over C. No actual HM/source/model evaluations, selected input values, external writes, or local Codex tasks were performed. The only output written for this audit is this local audit document.
