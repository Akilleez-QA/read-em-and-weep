# Hodge index excludes the moving sextic branch away from the rank-zero curve

## Scope

This proves a new exclusion for the residual beta family: its parameter image must be contained in Γ=κ(C). It applies even when the fixed degeneracy surface is nonnormal, and uses no conductor or discrepancy assumption. Together with the separately checked smooth-modular Γ exclusion, it rules out the residual generic beta sextic branch. Combined with the existing alpha/line exclusion, this closes the a=0,b=4 branch only, not the full Q4 problem.

## Inputs

Over C, let E have rank two, det E=O_P4(5), and U=H0(E) have dimension four. The full evaluation minors generate I_C, where C is the disjoint union of 25 lines. For B⊂U of dimension three, X_B is the degree-fifteen locally Cohen–Macaulay rank-at-most-one degeneracy surface. The rank-one full evaluation on C defines κ:C→P(U*), and Γ=κ(C).

The established residual-surface exclusion says that a fixed X_B supporting a positive-dimensional family of the integral beta sextics is reduced integral of degree fifteen. For B outside Γ, the B evaluation has rank one everywhere on X_B. Thus X=X_B is a local complete intersection, ω_X≅O_X(C), and X is smooth along every line of C. These statements and their local proofs are in BETA-QUOTIENT-POSITIVITY.md and BETA-IMAGE-DIMENSION-DROP.md; the degree-ten residual alternatives have now been removed in BETA-RESIDUAL-SURFACE-EXCLUSION.md.

Assume a positive-dimensional algebraic family of distinct integral curves D_t⊂X, each of degree six and contained in a hyperplane H_t, with D_t containing Z_t=C∩H_t. Work on the open where H_t contains none of the lines of C and Z_t is reduced. The beta family has these properties.

## 1. The 25 lines remain minus-one curves on a resolution

Each L_i⊂C is contained in the smooth locus of X and is Cartier on X. Its intersections with the other component lines are zero. Adjunction in a smooth neighborhood gives

−2=(K_X+L_i)·L_i=(C+L_i)·L_i=2L_i²,

so L_i²=−1. Also H·L_i=1, with H the hyperplane class.

Take a smooth projective resolution of the normalization π:Y→X, chosen to be an isomorphism over the smooth locus of X. Such a choice exists in characteristic zero. The lifted 25 lines, still denoted L_i, are therefore disjoint minus-one curves. Write C=ΣL_i and H=π*O_X(1) on Y. Projection formula and the unchanged neighborhood of C give

H²=15, H·C=25, C²=−25.

None of these equalities assumes that X is normal away from C.

## 2. Strict transforms of the moving sextics

A general member D_t is not contained in Sing(X). That fixed closed locus has dimension at most one, and hence finitely many curve components, whereas the D_t are distinct in a positive-dimensional family. Thus its strict transform D~_t on Y is integral and maps birationally onto D_t. The strict transforms are again distinct. After replacing the parameter by an irreducible positive-dimensional subfamily and shrinking, they form a flat algebraic family: take the closure of the inverse-image family over the isomorphism locus and apply generic flatness, discarding the locus where an unwanted vertical component appears.

Two distinct general members of this family are algebraically, hence numerically, equivalent. On the smooth surface Y the intersection of two distinct effective integral curves is nonnegative. Consequently, for a general D~=D~_t,

n=(D~)²≥0.

Moreover H·D~=6 by birationality and the projection formula. Scheme-theoretically D_t∩C=Z_t: since D_t⊂H_t and Z_t⊂D_t, the sum of the two ideals with I_C is exactly I_{Z_t}. The morphism π is an isomorphism near C, so

D~·L_i=1 for every i, and D~·C=25.

No smoothness or Gorenstein assumption on D_t is used. In fact the reduced length-one local intersections suffice for these intersection numbers.

## 3. The Hodge-index contradiction

On Y set

L=H+C,   M=D~+C.

Their intersections are

L²=15+50−25=40,
M²=n+50−25=n+25,
L·M=6+25+25−25=31.

The Hodge index theorem on the smooth projective surface Y implies (L·M)²≥L²M² because L²>0. One does not need to assume that L is ample; the intersection-form signature gives this inequality for every class of positive square. Therefore

961≥40(n+25),
40n≤−39,

contradicting n≥0. This excludes the proposed moving sextic family on every such X_B with B outside Γ, including singular and nonnormal X_B.

Equivalently, the same calculation for a moving degree-m curve meeting each of the 25 lines once gives

(m+25)²≥25(15+25)=1000.

Thus any such moving curve has degree at least seven.

## 4. Consequence for the beta parameter map

The beta assignment f from a dense open of dual P4 to P(U*) has target dimension three, so every nonempty fiber has dimension at least one. Its sextics are distinct because each nonplanar D_H spans its unique H. Hence a general B in its image outside Γ would provide the forbidden fixed-surface family, on the open where the established integral-degree-fifteen reduction applies. In particular the closure of the beta image is contained in Γ.

The beta image cannot be a point. If B were constant, all general H would yield degree-six D_H⊂X_B∩H for the fixed integral degree-fifteen X_B. Bertini makes a general hyperplane section of X_B integral of degree fifteen, which cannot contain an integral degree-six curve. Thus the image is positive-dimensional. Since Γ is the established irreducible rational sextic curve, the beta image is dense in Γ.

## 5. Combination with the separately checked Γ result

GAMMA-SCROLL-SEXTIC-EXCLUSION.md identifies X_{κ(p)}, for p away from the twelve modular parameters, with the degree-fifteen incidence-scroll image and proves it has no integral sextic. Its dictionary uses the first-order evaluation description to identify the precise net of quintics; this is not an analogy between parameter curves. The primary source is Aure–Decker–Hulek–Popescu–Ranestad, “Syzygies of Abelian and Bielliptic Surfaces in P4,” Section 4, https://arxiv.org/pdf/alg-geom/9606013 .

A dense beta image in Γ meets that open set, contradicting the existence of its integral sextic. The finite twelve cusp parameters cannot contain a positive-dimensional image. Therefore the generic beta sextic branch is impossible.

With the independently established alpha-plane and line alternatives already excluded, the residual a=0,b=4 case is excluded. This does not settle the other surviving (a,b) alternatives or claim a complete proof repair.

## Reproducibility and boundary

All arithmetic is displayed: the decisive discrepancy is 31²−40·25=−39. The new part is the lifted moving-curve Hodge argument; the final combination explicitly depends on the separate Γ dictionary/exclusion. There is no selected HM coefficient evaluation, matrix-rank computation, scan, local-model restart, or one-shot experiment. No external writes were made.

Public proof pins in Akilleez-QA/read-em-and-weep: quotient geometry 098a2769986103880e9c8aec437c7ea06b9388b1; integral surface reduction 3714d276821366f9b1230abb6cc60b81861bb878; Gamma exclusion 38c517ed358c08d776b59ab5def5856106dcdeb5; alpha exclusion in PR557 at 212f18bb3afb52171068d1aaf8a0dbfbf9954d2b. A public statement of the exact positive-square form of Hodge index used here is Patrick Brosnan, Algebraic Surfaces, Theorem3.15: https://terpconnect.umd.edu/~pbrosnan/notes/Surfaces/shit.html .
