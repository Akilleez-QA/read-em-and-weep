# Three exact constant-gauge templates for the degree-twenty-eight residual

## Result and scope

Consider the actual saturated full-span residual inclusion

    R=O(-8)+W O(-9) subset Hbar O,
    Hbar=A+V+P+D,

with actual saturated Gauss quotient 2 O(-8), forced by the remaining source E10 of G3.11.8ae96830fd21. There are exactly three equivariant constant-gauge classes of such residual inclusions. All three admit universal constructions with the stated saturation and actual Gauss quotient. This is a residual classification, not an actual HM realization theorem or a full-label exclusion.

Let X=O(-8) be the canonical top line, let L=R^- be the actual backward kernel, and let Y=L^+ be its actual first transform. The three classes are distinguished by

    (dim span L, dim span X) = (11,4), (11,9), (6,9).   (1)

Their equivariant constant endomorphism algebras are, respectively,

    C times C, C, C times C.                          (2)

Here constant endomorphisms mean endomorphisms of Hbar preserving the actual R; no endomorphism of a larger module is asserted.

## 1. Exact inputs and notation

The repository is Akilleez-QA/read-em-and-weep. The relevant original actual data and full-span statement are at commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md.

PR817, commit a0b7cbd7a53c1603f284cf0e1a29fff106d02cb3, research/hm/profile11-o26-basepoint-free-top/PROOF.md, Sections 5–7, proves the actual saturated constant projection and quotient used here. Its constant fifteen-space C satisfies E intersect C O=F and C O/F=O(28), precisely the saturated positive summand in E^+/E. Thus E+C O is saturated and R=E/F is genuinely saturated in (H/C) O. Projection of the original connection gives R^+/R=2 O(-6) and the onto derivative map R->2 O(-8). E spans H, so R spans Hbar=H/C. The actual character of H is 2A+2V+2P+2D.

PR856, commit cee45480686c39a321feaa77d4b669682cc71efe, research/hm/profile11-degree28-constant-separation/PROOF.md, further proves that this residual is genuinely separated from the degree-twenty-eight constant block by a constant ambient shear. Thus the classification below describes the actual complementary inclusion in that decomposition, not only a projected abstract bundle. The residual proof below requires only the already saturated projection and does not reprove the separation.

For the identification with the only remaining source of the displayed label, additionally use PR813, commit 3f99ecf539a3a3da61743df0dff409e54270c865, research/hm/profile11-o26-divisor-reduction/PROOF.md, and PR822, commit b6bcb1fc5ba0ce245bd14ce104afb0a0a4222bbc, research/hm/profile11-o26-e18-polar-exclusion/PROOF.md. These remove the other divisor and source alternatives. The present proof itself uses only the actual residual inclusion and quotient stated above.

Work over C with the binary icosahedral group G. Write W for its defining symplectic two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W; V,P,Wp have dimensions 3,4,2, and P=W tensor Wp. All irreducibles are self-dual. Effective invariant divisors on P(W) have orbit sizes 12,20,30,60. The notation

    U_j^d subset Sym^d W O,
    (U_j^d)_ell=ell^(d-j) Sym^j W,
    U_j^d=Sym^j W O(j-d)

denotes the complete osculating bundles, with the invariant apolar convention for the constant coefficient space. The displayed fiber formula is universal in the arbitrary line ell; no point is selected.

## 2. The intrinsic residual line and tail

The top X=O(-8) is intrinsic: it is the entire maximal-slope subbundle of R. Initially choose any equivariant complementary W O(-9). In the onto actual Gauss map R->2 O(-8), the X component is a constant column a and the tail component is a constant column b times the unique Euler quotient W O(-9)->O(-8). Surjectivity means that a,b are independent. Therefore

    L=R^-=O(-10),  R/L=2 O(-8).                       (3)

The internal derivative L->(R/L)(-2)=2 O(-10) is nonzero, since otherwise L would be a negative horizontal line in a constant bundle. It is a nonzero constant column, so its image is saturated. As R is saturated in Hbar O, the actual first transform L^+ has rank two and degree -18.

The universal first-polar map of the degree-ten line, W O(-9)->Hbar O, has image the value-and-first-derivative sheaf. The saturation just proved and the equal rank and degree identify it with Y=L^+. The projection of Y to the chosen abstract tail is an equivariant scalar endomorphism of W O(-9), and cannot vanish because Y has rank two whereas X has rank one. Hence

    R=X direct-sum Y, Y=L^+=W O(-9)                   (4)

as actual subbundles. The initially possible Euler graph Y->X has now been fixed by the canonical choice Y=L^+. No subsequent classification step varies it by an arbitrary bundle automorphism.

The constant span of L equals the constant span of its first polar Y: a constant functional kills one if and only if it kills the other. The coefficient map of L factors through

    Sym10 W=A+V+D,

whereas that of X factors through

    Sym8 W=P+D.                                      (5)

Because R spans Hbar, the A and V coefficients of L are nonzero and the P coefficient of X is nonzero. Each constituent in (5) has multiplicity one. Thus the span of L is either A+V or A+V+D. If it is A+V, the D coefficient of X must be nonzero. If it is A+V+D, the D coefficient of X can be zero or nonzero. This gives exactly the three cases in (1).

The vanishing of the P component of Y follows from its actual first-polar origin and (5). It is not a claim that Hom_G(W O(-9),P O) vanishes; that abstract Hom space is nonzero.

## 3. Constant-gauge normalization, not a source-bundle substitution

All four irreducibles of Hbar have multiplicity one, so every equivariant constant automorphism is an independent nonzero scalar on A,V,P,D. The maps from the degree-ten line to its A,V,D constituents and from the degree-eight line to P,D are unique up to scalars by (5).

If the D coefficient of L vanishes, full span makes both coefficients of X nonzero. Independent constant scalings of A,V and of P,D normalize the two lines to the projections of the complete degree-ten line onto A+V and the complete degree-eight line onto P+D, respectively.

If the D coefficient of L is nonzero, normalize its three coefficients by independent A,V,D scalings. It then becomes the complete degree-ten line in A+V+D. The P coefficient of X is nonzero and can also be normalized. The remaining relative D coefficient of X is either zero or nonzero. Common scaling of A+V+D preserves the degree-ten line as a subbundle, while independent P scaling permits every nonzero relative D coefficient to be normalized to the same value.

These are statements about orbits under constant automorphisms of the ambient representation. Scalars multiplying a line's parametrizing map do not change the line subbundle. No independently chosen nonconstant source automorphism has been used to change X or the canonical Y.

In the following list, repeated irreducibles are the same constant summand of Hbar, not extra copies. Projection onto a named irreducible is its unique equivariant projection, up to the harmless constant normalization just explained.

    Type I:
      X = projection_P(U_0^8),
      Y = U_1^10 in (A+V+D) O.

    Type II:
      X = U_0^8 in (P+D) O,
      Y = U_1^10 in (A+V+D) O.
      The two indicated constant spaces share their D summand.

    Type III:
      X = U_0^8 in (P+D) O,
      Y = projection_(A+V)(U_1^10).                  (6)

The intrinsic pair of dimensions (1) proves that distinct rows cannot be equivariantly constant-gauge equivalent. It remains to check these are actual saturated residual constructions with the prescribed derivative, rather than merely coefficient templates.

## 4. Two universal projected-jet facts

For an h-dimensional independent degree-d section system on P1, the characteristic-zero Wronskian is nonzero and has degree h(d-h+1). At a point with vanishing sequence a_0<...<a_(h-1), its weight is sum_i(a_i-i). If the system is basepoint-free and fails to generate jets through order j, then a_j>=j+1, so its Wronskian weight is at least h-j. The failure locus is invariant for an invariant system.

Apply this first to the P summand of Sym8 W, with h=4,d=8. It is basepoint-free: a nonempty common divisor would be invariant of degree at most eight. The Wronskian has degree 20. Failure to generate first jets has weight at least three, so an entire invariant orbit would contribute at least 36. Therefore

    projection_P:U_1^8 -> P O

is fiberwise injective everywhere. Its line subbundle projection_P(U_0^8) is also saturated. The coefficient space is all P, so this line spans P.

Next use the A+V summand of Sym10 W, with h=6,d=10. It too is basepoint-free. Its Wronskian has degree 30. Failure to generate second jets has weight at least four, so one invariant orbit would contribute at least 48. Therefore

    projection_(A+V):U_2^10 -> (A+V) O

is fiberwise injective everywhere, and the same holds for U_1^10 and U_0^10. The projected first-polar bundle has the projected second-polar bundle as its actual saturated forward transform. These statements concern arbitrary points simultaneously and require no orbit representative or evaluated derivative.

## 5. Every row has the exact residual Gauss quotient

In Type I, X and Y lie in disjoint constant spaces P and A+V+D. Section 4 makes X and its first transform saturated. The complete degree-ten osculations Y=U_1^10 and Y^+=U_2^10 are saturated as well. Their sums are therefore saturated.

In Type III, the two constant spaces P+D and A+V are disjoint. The complete degree-eight osculations and the projected degree-ten osculations in Section 4 are saturated, so the same conclusion holds.

In Type II there is a shared D, which must not be ignored. Nevertheless the projection of X^+=U_1^8 to P is fiberwise injective by Section 4, while Y^+=U_2^10 has zero P component. Their fibers therefore intersect trivially at every point. The induced inclusion

    U_1^8 direct-sum U_2^10 -> Hbar O

is fiberwise injective, hence has locally free quotient. In particular X+Y and X^++Y^+ are genuinely saturated, not just generically disjoint image sheaves.

In every row the raw first derivatives generate exactly

    R^+=X^+ direct-sum Y^+,
    R^+/R=(X^+/X) direct-sum (Y^+/Y)
          =O(-6)+O(-6).                              (7)

For the projected bundles the quotient identities are transported by the proved fiberwise isomorphisms with the corresponding complete osculating domains. The standard derivative on each osculating step is onto. Thus the actual derivative of R onto (7)(-2) is onto, and its saturated Gauss quotient is exactly 2 O(-8). Its kernel is the degree-ten line L within Y, and L^+=Y as required. The coefficient spans of X,Y sum to all Hbar in each row.

This proves the existence of all three residual constant-gauge classes as universal abstract inclusions and also proves completeness for the actual residual hypotheses. These constructions do not select, evaluate, or identify any actual HM instance. They show why the residual hypotheses alone cannot exclude the remaining label.

## 6. Exact equivariant constant endomorphism algebras

Let t be a G-equivariant endomorphism of Hbar with t(R) contained in R. It is diagonal on A,V,P,D. Its induced bundle map preserves the canonical top X. Because t is constant it commutes with the derivative, hence preserves L=R^- and Y=L^+. Restriction to either line X or L is a scalar, so t has a common scalar on all constant coefficients spanning that line.

Conversely, these scalar equalities visibly suffice to preserve both X and Y, hence R. Therefore:

- Type I requires t_A=t_V=t_D, with t_P independent; the algebra is C times C.
- Type II requires t_A=t_V=t_D and t_P=t_D; the algebra is C.
- Type III requires t_A=t_V and t_P=t_D; the algebra is C times C.

The corresponding automorphism groups are the units of these algebras. This is a statement about the actual constant inclusion. No inference of a full-module endomorphism, projector lift, or actual HM realization is made.

## Verification boundary

The small verifier uses only the nine fixed McKay rules to check (5), the stated irreducible dimensions, the Euler channels, and the Wronskian integer inequalities. It does not enumerate source types or evaluate an actual coefficient, point, derivative, matrix or rank. No all-twist envelope or large computation is used. Saturation, intrinsicness and actual quotient identities are proved in the text.
