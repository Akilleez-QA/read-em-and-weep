# Full-flag resolution of the canonical-complement boundary

## Result

Work over C. Let B be an integral projective surface in P(V), dim V=5, whose general middle point is good in the sense of `/research/hm/middle-surface/rank-five-middle-families/PROOF.md`. On its good open locus there are canonical subspaces

    U_u = Cu,    C_u ⊂ H_u ⊂ V,
    dim C_u=3,   dim H_u=4,   H_u=U_u ⊕ C_u.

Close the graph of the **pair** (C_u,H_u), rather than just C_u, and take a projective resolution Y. Write π:Y→B and use the same letters for the pulled-back tautological bundles. Set

    R=V/C,    N=V/H,    F=R⊗U*,
    h=c1(U*),    n=c1(N).

Then there is a nonzero effective Cartier divisor A on Y, supported over the bad middle locus, and a canonical exact sequence

    0 → U(A) → R → N → 0.                              (1)

The middle-induced section of F has zero scheme **exactly A**, including all scheme multiplicities. There is no residual isolated zero scheme. In CH_0(Y),

    c2(F) = A·(n+h),                                    (2)

and numerically

    ∫_Y A·(n+h) ≥ degree(B) > 0.                        (3)

Every irreducible component of A contributes a nonnegative amount to the left side of (3). At least one contributes positively. In particular, if the bad middle locus is finite, at least one bad point has a positive-dimensional family of limiting support hyperplanes H_u. A finite bad locus with only finitely many limiting support hyperplanes at each point is impossible.

In the residual-kernel setting of the source proof, rank-three, rank-four, and rank-five middle points have a unique limiting support hyperplane. Consequently the boundary must either contain a curve, or contain a point with rank Q≤2 and positive-dimensional variation of limiting support hyperplanes.

These statements allow B to be singular, residual rank to drop, the ternary metric to have arbitrary corank, and exceptional divisors to occur. They do not identify A with a discriminant divisor in this generality. They do not exclude all boundary configurations or prove existence of a rank-five family.

## 1. The full-flag graph and its tautological geometry

Let B° be the good open locus. The prior canonical-complement theorem supplies a regular map

    B° → Flag(3,4;V),    u ↦ (C_u,H_u).

Here H_u is the inverse image in V of the three-dimensional residual support. The canonical complement is regular on every good point, and H_u is regular there as well. Let G^fl be the reduced closure of this graph inside B×Flag(3,4;V). It is integral and projective. Its projection to B is an isomorphism over B° and is therefore birational, even when B is singular.

The flag variety carries subbundles C⊂H⊂V of ranks three and four. Their pullbacks to G^fl remain subbundles: their successive quotients are locally free and the relevant exact sequences are locally split. The middle line U is pulled back from B⊂P(V).

The incidence U⊂H holds over the graph of B° and extends over its closure. Equivalently, the bundle homomorphism U→V/H vanishes on a dense open of an integral scheme and hence vanishes identically. Thus, everywhere on G^fl,

    U → H/C → V/C,
    0 → H/C → V/C → V/H → 0.                            (4)

Crucially, Z_line:=H/C is a line **subbundle** of the rank-two bundle V/C, not merely a saturated rank-one subsheaf with a possibly non-locally-free quotient.

Choose any projective resolution ρ:Y→G^fl. Such a resolution exists in characteristic zero, and Y is a smooth integral projective surface. No assumption that B° is smooth is needed; the resolution need not be an isomorphism over its singular points. All incidences and locally free exact sequences pull back to Y. The composite π:Y→B is still birational.

## 2. Exact scheme-theoretic divisor of the middle section

On Y the map U→Z_line is a section t of the line bundle Z_line⊗U*. It is nowhere zero above B°, since there U⊕C=H. In particular t is generically nonzero. On an integral scheme a generically nonzero section of a line bundle has a locally nonzero, non-zero-divisor equation. Its zero scheme is therefore an effective Cartier divisor, provisionally allowed to be empty. Denote it by A.

The section gives the canonical identification

    Z_line⊗U* ≅ O_Y(A),    Z_line ≅ U(A),                (5)

where t corresponds to the canonical divisor section. Substitute (5) in (4) to obtain (1), and twist by U* to obtain

    0 → O_Y(A) → F → N⊗U* → 0.                         (6)

To check the full zero scheme, trivialize and split (6) locally. The middle section s of F is then (a,0), with a a local equation of A. Its zero ideal is exactly (a). No extra ideal supported at isolated points appears. Since Y is smooth, A has no embedded point components and is purely one-dimensional when nonempty. Its coefficients are its actual orders of vanishing, not reduced-support coefficients.

The same factorization already makes the zero scheme an effective Cartier divisor on the integral graph G^fl. We make the stronger assertion about absence of embedded points only after passing to the smooth resolution: an arbitrary integral singular graph need not have the depth properties needed for that assertion.

At every good point of B the pair (C,H) has a regular extension on a neighborhood. Its graph is closed there, so G^fl has the prescribed graph over that neighborhood, and t is nowhere zero throughout its inverse image. Thus

    supp(A) ⊂ π^{-1}(B\B°).                             (7)

In the rank-five application, the earlier boundary theorem identifies B\B° with the possible lower-rank or degenerate-ternary-metric locus: full four-dimensional residual support cannot intervene at rank five. Nothing in (4)–(7) requires rank or metric bundles themselves to extend across this locus.

## 3. Universal Chern identity, positivity, and nonempty boundary

Whitney's formula applied to (6) yields the identity (2) in the Chow group of zero-cycles, not merely an equality of degrees. The line quotient in (6) has first Chern class n+h, so there is no additional codimension-two correction term.

Independently, the rank-two twisting formula gives

    c2(F) = c2(R)+h c1(R)+h².                           (8)

R is a quotient of the trivial bundle V and is globally generated. Therefore det R is globally generated and nef; also ∫c2(R)≥0, for example by taking a general section of R and representing its top Chern class by its empty or zero-dimensional zero scheme. The middle class h is globally generated and nef. Consequently ∫h c1(R)≥0. Finally,

    ∫_Y h² = degree(B),

by birationality and the projection formula, without any smoothness assumption on B. Equations (2) and (8) prove (3). In particular A cannot be empty.

More generally, the same argument for a smooth projective surface with middle map generically finite of degree d onto B gives lower bound d·degree(B). The graph construction itself has d=1 in the setting of this note.

## 4. Componentwise positivity and the limiting-hyperplane obstruction

Both N=V/H and U* are globally generated line bundles: they come from the hyperplane and middle maps, respectively. Hence n+h is nef. Writing

    A = Σ_i m_i D_i,    m_i>0,

one has

    D_i·(n+h) ≥ 0,
    Σ_i m_i D_i·(n+h) ≥ degree(B)>0.                    (9)

For an integral curve D_i, pass to its normalization. The degree of h there is positive exactly when its middle map to P(V) is nonconstant; the degree of n is positive exactly when its support-hyperplane map to P(V*) is nonconstant. This follows because these line bundles pull back O(1). Thus some boundary curve has nonconstant middle map or nonconstant support-hyperplane map.

Equivalently, under the morphism

    (middle,H):Y→P(V)×P(V*),

the effective cycle A has nonzero effective one-cycle pushforward. Its degree for O(1,1), with pushforward multiplicities, is the left side of (9).

If B\B° is finite, each D_i maps to a single bad middle point, and D_i·h=0. Then (9) forces D_i·n>0 for at least one i. The image of that curve in the flag graph gives infinitely many, indeed a curve of, limiting H values at its bad point. These are actual graph limits from B°, since G^fl is the closure of that graph. Exceptional curves added solely by resolving singularities cannot create new H values: the H map factors through G^fl.

Therefore finitely many bad points, each with a unique limiting H, are impossible; even finitely many H limits at each is insufficient. This does not exclude a finite bad locus with varying H limits, nor a boundary curve in B. It is a necessary geometric obstruction, not a claim that every bad point has varying limits.

### 4A. Rank-four and rank-five points cannot carry support ambiguity

We now use the additional residual-kernel structure in the source proof. The repeated-input injectivity hypothesis makes the residual construction a regular bundle map Q on the middle space. Its domain at u is Sym² E_u, where E_u=V/U_u has dimension four. Thus

    dim ker Q_u = 10 - rank Q_u.

On B° its kernel K_u has dimension five and is contained in Sym² E0_u for the three-dimensional support E0_u=H_u/U_u.

Fix any middle point b. Every limiting support E_A in E_b, obtained from the graph closure, carries at least one limiting five-plane K_A with

    K_A ⊂ ker Q_b ∩ Sym² E_A.                            (17)

To justify this without assuming the kernel bundle extends, close the joint graph of the five-plane K_u and the support E0_u in the corresponding relative Grassmannians. Its projection to the support graph is proper and surjective. The equations Q(K)=0 and K⊂Sym² E0 are closed incidence conditions, so every lift over a limiting support satisfies (17). The five-plane stays five-dimensional because its parameter space is a Grassmannian, even when the actual kernel jumps in dimension.

Suppose rank Q_b=4 and two distinct limiting supports E_A,E_B exist. The common ambient kernel has dimension six, so

    dim(K_A∩K_B) ≥ 5+5-6 = 4.                           (18)

But two distinct three-planes in E_b of dimension four intersect in dimension two, and

    Sym² E_A ∩ Sym² E_B = Sym²(E_A∩E_B),

whose dimension is three. The equality follows immediately by extending a basis of E_A∩E_B to bases of E_A, E_B, and E_b, and comparing the symmetric monomials. This contradicts (17)–(18). Hence the limiting support, and therefore H, is unique at every rank-four point.

At rank five the same argument is stronger: the two limiting five-planes would both equal ker Q_b, contradicting their possible intersection dimension at most three. This also recovers uniqueness of H at rank-five degenerate-metric points.

### 4B. A regular correction through jumping kernels excludes rank-three ambiguity

The correction used in the source proof has a regular ambient extension locally even where the residual kernel jumps. Here is the precise reason. Choose a regular local splitting s:E→V of V→E=V/U and a frame u of U. The repeated-input map A_u:E→J is injective at every point by hypothesis. It therefore has constant rank four and admits a regular local left inverse L:J→E. Indeed an invertible rank-four minor supplies such a left inverse on a neighborhood; equivalently its image is a subbundle and the bundle sequence splits locally.

The middle numerator

    β_u:Sym² E→J,    ab↦f(s(a),u,s(b)),

is regular in this local trivialization. Define the ambient extension v_tilde=Lβ_u on all Sym² E. On the actual residual kernel K_u=ker Q_u, β_u takes values in im A_u, and hence v_tilde|K_u is precisely the correction v_u characterized by A_u(v_u(q))=β_u(q). Its restriction to K_u is independent of the choice of left inverse. We do not claim the extension away from K_u is canonical; its regularity is all that is needed.

On the dense good locus, the previously proved support property says v_u(K_u)⊂E0_u. The condition v_tilde(K)⊂E0 is a closed bundle incidence on the joint kernel/support graph from Section 4A. It follows that every limiting pair satisfies

    v_b(K_A)⊂E_A.                                      (20)

This argument does not require the jumping kernel itself to be a vector bundle. It uses a regular ambient extension and the Grassmannian limits of its five-dimensional good-locus subspaces.

Now suppose rank Q_b=3 and two distinct limiting supports E_A,E_B exist. The ambient kernel has dimension seven, so dim(K_A∩K_B)≥3. Set W=E_A∩E_B, a two-dimensional vector space. Since their intersection is contained in Sym² W, also of dimension three, necessarily

    K_A∩K_B=Sym² W ⊂ K_b.

Equation (20) then gives v_b(Sym² W)⊂W. For any linear map w:Sym² W→W, the expression

    e ↦ e∧w(e²)

is a homogeneous cubic with values in the one-dimensional space det W. Over C it either vanishes identically or has a zero on P(W)≅P¹. Thus some nonzero e∈W satisfies w(e²)∈Ce. Applying this to w=v_b|Sym²W produces a square e²∈K_b with v_b(e²)∈Ce.

That is a compatible square, forbidden by the repeated-input square-avoidance lemma at every middle point, including b. The lemma uses the independence of A_e(u) and A_u(e) for independent e,u and does not assume rank Q is constant. Hence rank-three points also have a unique limiting support hyperplane.

Combining Sections 4, 4A, and 4B gives the necessary alternative

    the bad locus contains a curve;
    or some bad point has rank Q≤2 and varying limiting H.  (19)

In particular, if the entire bad locus is finite and rank Q≥3 everywhere on B, the assumed good-general middle surface cannot exist. At rank Q=2 the ambient kernel has dimension eight and the lower bound for K_A∩K_B is only two. The argument no longer forces all Sym² W into the intersection, so the binary-cubic contradiction does not apply. No exclusion at rank two or below is claimed here.

## 5. A new modification: the flag graph is a blowup of the zero ideal

Let G be the integral complement-graph closure in B×Gr(3,V), before resolving it. On G, U and C are already bundles, and R=V/C is locally free of rank two. Let I_s be the zero ideal of the middle section of F=R⊗U*; equivalently it is the image of F*→O_G. It is a coherent, generically nonzero ideal.

Over the locus where s is nonzero, there is a unique line in R spanned by the image of U. Its inverse image in V is the unique four-plane containing C and U. Thus its rational map to the relative projective line bundle P_G(R) is exactly the rational support-hyperplane extension furnished by the good flag map.

Locally choose frames and write s=(f,g). The closure of the graph of the line [f:g] is

    Proj O_G[ft,gt] = Bl_(f,g)(G),                       (10)

where the algebra is the Rees subalgebra of O_G[t]. Indeed, it is a closed subscheme of G×P¹, is integral, and agrees with the graph on its dense domain of definition. Hence it is its reduced scheme-theoretic closure. Frame changes glue these descriptions. Twisting by U* does not affect the line projectivization or the zero ideal. Consequently

    G^fl ≅ Bl_{I_s}(G)                                 (11)

over G. This identification is with the full graph closure, not with an arbitrary incidence component. In particular, merely imposing that C,U⊂H without taking the graph closure could introduce extraneous components and is not the construction used here.

Formula (11) is the geometric content beyond a renaming of the old excess formula. It supplies a canonical projective modification that principalizes the entire middle-section ideal, simultaneously extends the support-hyperplane map, and makes its complementary quotient a globally generated line bundle. It works at residual-rank drops and at all metric degeneracies without needing a local metric normal form.

## 6. Comparison with any old smooth complement-graph resolution

Let X→G be any smooth projective complement-graph resolution. On X write F_X=(V/C)⊗U*, and decompose the zero scheme of its middle section into its maximal divisorial part A_X and residual finite scheme Z:

    I_s = O_X(-A_X) I_Z.

As in the preceding metric-boundary proof, Z is empty or a zero-dimensional local complete intersection and

    c2(F_X) = [Z]+A_X·(c1(F_X)-A_X).                    (12)

Take the closure of the full-flag graph over X and resolve it, obtaining p:Y_X→X. This is also a smooth full-flag model over B and maps to G^fl. By (10) it factors through the blowup of I_s, equivalently of I_Z since tensoring an ideal by an invertible ideal does not change its blowup. Write

    I_Z O_{Y_X}=O_{Y_X}(-E).

E is an effective divisor supported over Z and is zero when Z is empty. If A_{Y_X} is the actual middle-section divisor on this model, equality of pulled-back zero ideals gives

    A_{Y_X}=p* A_X+E.                                  (13)

In particular A_{Y_X} is not, in general, merely the pullback or strict transform of A_X. Old isolated zeros acquire exceptional divisorial multiplicity.

The full-flag exact sequence on Y_X gives

    c1(p*F_X)-A_{Y_X}=n_{Y_X}+h_{Y_X},
    c2(p*F_X)=A_{Y_X}·(c1(p*F_X)-A_{Y_X}).              (14)

Push forward to X. Chern classes commute with pullback, and p_*[Y_X]=[X], so the pushforward of (14) is exactly c2(F_X). Since p_*E=0 as a divisor cycle and the cross terms vanish by the projection formula, expanding (13) yields

    p_* c2(p*F_X)
      = A_X·(c1(F_X)-A_X) - p_*(E²).

Comparison with (12) proves

    p_*(E²) = -[Z] in CH_0(X).                          (15)

Thus the old residual zero-cycle is precisely recovered by the exceptional self-intersection correction. Its local multiplicities are the lengths of the original local complete intersection, not a count of distinct points. If a specified resolution Y of G^fl does not map to X, take a common smooth resolution before using (13)–(15).

There is also an intrinsic pushforward statement to the possibly singular graph G itself. Let F_G=(V/C)⊗U*. For q:Y→G, the operational Chern class projection formula gives

    q_*(A·(n+h)∩[Y]) = c2(F_G)∩[G] in CH_0(G).         (16)

Analogous pushforward to B is valid as a zero-cycle. We do not assert invariance of a naively chosen divisor A across different complement models. Once a smooth full-flag model is fixed, further birational pullback does pull its Cartier zero divisor back exactly, because its entire zero ideal is already invertible.

## 7. Relation to the simple and multiple corank-one metric formulas

On a neighborhood where the preceding metric-boundary proof applies, the metric has rank exactly two on its Cartier discriminant D, square avoidance holds, and the support hyperplane extends. There the canonical complement already extends as a subbundle, the section ideal is precisely I_D, and the full flag graph adds no modification. The divisor A equals D on that neighborhood, with its full discriminant multiplicity. For a reduced simple degeneration its coefficient is one.

Outside those hypotheses, A may include divisors lying over rank drops, higher-corank metric points, indeterminacy of H, and exceptional divisors originating in residual isolated zeros. No equality with a metric discriminant is claimed there. Nevertheless (1)–(3) and the componentwise positivity (9) remain valid on the full-flag resolution.

In the old expression (12), individual contributions from A_X·(c1(F_X)-A_X) can be negative. The improvement is not that those old summands were secretly nonnegative: changing to the full-flag model changes the divisorial section data as in (13). On the new model the quotient is the actual globally generated support-hyperplane line N, making every component's contribution to A·(n+h) nonnegative. This yields the limiting-hyperplane obstruction of Section 4, which does not follow from the old formula without this new geometric construction.

## Scope of the argument

Only universal algebraic geometry and the established canonical good-locus flag are used.  The result settles the general divisorial-versus-isolated defect bookkeeping after a specified projective flag modification. It leaves open the existence or nonexistence of families with the required boundary geometry.
