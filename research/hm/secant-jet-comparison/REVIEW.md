# Independent review: secant restriction and the intrinsic cubic jet

## Verdict

**PASS, conditional on the explicitly pinned HM inputs.** The degree-nine exclusion, factoring-line cubic-channel identification, fiber-product compatibility, and normalized splitting are valid. No substantive correction to the theorem is required. This review does not independently certify the underlying actual-map comparison or evaluate any actual HM family or selected source instance.

Reviewed file: `SECANT-RESTRICTION-AND-THE-INTRINSIC-CUBIC-JET.md` in this directory. Review date: 2026-10-22 UTC. Reviewed manuscript SHA256: `abf0109723288cd462c85e82adeba9aa28cba7c0749def26f3e0caac5a8e07c7`.

## Evidence and assumptions

I read the proof independently and fetched these two files read-only at their exact commits:

1. [Secant-kernel theorem, 4e16e69c776bd85506341b5bb785f0d8a396bd3e](https://github.com/Akilleez-QA/read-em-and-weep/blob/4e16e69c776bd85506341b5bb785f0d8a396bd3e/research/hm/order-four-quadratic-load/CANONICAL-LIFTING-KERNEL-IS-A-SECANT-BUNDLE-AND-LEAVES-THREE-QUARTIC-CHANNELS.md). Returned blob SHA: `3ed99ff88205d678eb35767bdcac7112e2824119`.
2. [One-axis jet theorem, c85c756d333281eccefdb77c4899db4f923d768e](https://github.com/Akilleez-QA/read-em-and-weep/blob/c85c756d333281eccefdb77c4899db4f923d768e/research/hm/order-four-quadratic-load/FOURTH-GATE-ONE-AXIS-JET-AND-ONE-SQUARE-FIBER.md). Returned blob SHA: `78fb0141fb97aed1b6d90799ce156bc3625fe828`.

These files contain the cited exact sequence with dimensions (1,4,3), the everywhere-surjective bundle map L, the six-axis geometry, the local ideal and representation data, and dim ker j=1. The first file explicitly depends on an earlier actual-map identification; the second explicitly imports the general-position/conic construction. Those upstream dependencies remain assumptions here.

Necessary assumptions are: characteristic zero; equivariance and transitivity on the six axes; the six distinct smooth five-axis conics; the local ideal (x²,y²); the stated N-representations and O(10) fiber character; and the two pinned global channel/rank computations. The final assertions that C is onto and dim ker C=1 additionally use dim ker j=1. They do not follow from the new degree-nine argument alone.

## 1. Degree-nine exclusion: PASS

Let f be a nonzero degree-nine homogeneous polynomial with multiplicity at least four at all six points. If C_i is not a component of its divisor, restriction to the smooth conic has zeros of order at least four at the five points lying on C_i. Its total degree is 18, whereas the required zeros have total degree at least 20. Thus C_i must be a component, for every i. Distinct irreducible equations c_i are relatively prime in the homogeneous polynomial ring; hence their degree-twelve product divides f, a contradiction.

This argument does not require transverse intersections among the conics and does not require a generic-rank calculation. Smoothness at each marked point ensures the restriction-order lower bound. The argument remains valid for reducible or nonreduced f.

If j(ML)=0, equivariance transports this statement from the chosen axis to all six axes. Since m²I=m⁴, every component of ML vanishes to order at least four there. A local right inverse of the surjective bundle map L implies the same for M. After untwisting, the coefficients of M are global sections of I(9), hence ordinary degree-nine forms satisfying the exclusion. Therefore M=0. This proves T∩ker j=0 without using any square-fiber datum.

## 2. Equivariant bundle symbols and the O(1) character: PASS

The intrinsic fiber exact sequence is

    0 → Hom(ell,ell) → Hom(ell,A) → Hom(ell,A/ell) → 0.

Thus the fiber of A O(1) is A⊗ell*, with a trivial one-dimensional subrepresentation and tangent quotient T_pX. Semisimplicity over C gives its representation type 1⊕rho1. The two-dimensional dihedral representations are self-dual, so tangent and cotangent have the same representation type.

This is the correct way to handle the twist. In particular the normalizer involution can act by -1 on ell, and O(1)|p must not be silently treated as trivial. No preferred equivariant isomorphism between tangent and cotangent is needed. The representation-type statement, not a choice of splitting, is all the proof uses.

Here is a precise filtered-sheaf justification of the symbols. The locally free source B=A O(1) maps under M to I(10). Reduction modulo mI defines an N-equivariant map B_p→(I/mI)⊗O(10)|p. Since mI=m³ and this target is rho2, whereas B_p is 1⊕rho1, this reduction vanishes. Therefore M(B)⊂mI(10), as a statement about the whole sheaf map, not just chosen constant source sections. Reducing again defines a map

    B_p → (mI/m²I)⊗O(10)|p = (m³/m⁴)⊗O(10)|p.

The target is rho1⊕rho2, so only the rho1 component can occur. The source fiber is legitimate because mB maps into m²I. Composing with L reduces to composition with the surjective fiber map L(p); higher-order changes of L contribute only order four. Thus j(T) has only the cubic rho1 component.

The pinned axis action is also consistent explicitly: order-five rotations act by 1 on ell, and a normalizer involution acts by -1. Hence its action on O(10)|p=ell*⊗10 is trivial on both generators of N. This does not imply triviality of O(1)|p.

No equivariant trivialization of O(10) over the whole infinitesimal neighborhood is required. Its *fiber* character suffices on the associated graded pieces. The finite jet representation itself may be treated directly with its natural linearization.

## 3. Canonical projection: PASS

Write V=(I/m⁴)(10), understood as the supported stalk quotient with its actual line-bundle twist. Its cubic submodule U=(m³/m⁴)(10) is canonical, and V/U is rho2. Therefore the rho1-isotypic part V[rho1] lies in U. It has multiplicity one and dimension two. The complementary rho2-isotypic part has dimension four.

For precision, V[rho1] is the image of the central idempotent

    e_rho1 = (2/|N|) sum_{g∈N} chi_rho1(g⁻¹) g.

Consequently this projection is canonical despite the absence of a preferred splitting between the two copies of rho2. Passing to Hom_N(D,-) gives canonical summands E1 and E2 of dimensions one and two. There is no hidden choice of a scalar coordinate on E1, nor a preferred pair of scalar coordinates on E2.

The degree-nine exclusion and dim T=1 now imply j(T)=E1. With ker r=T and r onto, the map (r,pi1 j):Q→R⊕E1 is injective and is an isomorphism by dimensions (or directly by correcting any lift using T).

## 4. Compatibility and canonical splitting: PASS

Since pi2 j kills precisely the required subspace T for descent, it factors uniquely through r, giving C:R→E2. Exactness then yields

    Q ≅ {(a,b)∈R⊕E : C(a)=pi2 b}.

The last map R⊕E→E2 is onto already because pi2:E→E2 is onto; surjectivity of C is not needed for this exact sequence. For any compatible pair, the difference between a chosen lift's jet and b is in E1, and j:T→E1 corrects it uniquely. This proves both existence and uniqueness without choosing an actual HM family or computing C.

The normalization s(a) is the unique q with r(q)=a and pi1 j(q)=0. Equivalently it is the inverse of (r,pi1 j) on R⊕{0}. It is linear, basis-independent, and canonical relative to the fixed equivariant data r and j. Thus Q=s(R)⊕T is genuinely justified, not inferred from abstract semisimplicity of an arbitrary short exact sequence.

Using the separate pinned fact that j is onto, C is onto. Then r restricts to an isomorphism ker j→ker C, and both spaces have dimension one. Also Q/(T+ker j) is canonically identified with E2 via pi2 j. This is the precise meaning of the common two-dimensional quotient.

## Corrections and presentation cautions

No mandatory mathematical correction was found. The following precision points should be retained if the result is rewritten:

- “Canonical” is relative to the fixed actual-map identification, linearizations, and geometric jet construction. It does not compute a normalized actual gate.
- E1 is an intrinsic one-dimensional vector space, not a canonically scaled scalar. The two compatibility conditions form an E2-valued equation, not a canonically ordered pair of numerical equations.
- Do not replace the supported jet module by its residue fiber, and do not trivialize the O(1) fiber character.
- Do not claim that the full finite O(10)-twisted jet module is canonically an untwisted jet module merely from triviality of the fiber character. The filtered/isotypic argument above avoids that unnecessary claim.

## Verification performed and limits

I ran the supplied `verify_secant_jet_channels.py`; it passed. It checks only universal local ideal products, weight arithmetic, numerical inequalities, and dimensions. The independent mathematical review above, not that script, verifies the geometric exclusion, filtered equivariant maps, descent, and canonical splitting.

No GitHub write, actual HM/source-instance evaluation, selected-direction test, numerical rank experiment, or large computation was performed. This is a conditional new structural lemma. It neither decides the actual corrected fourth obstruction nor supplies missing lower lifts, specialized-axis kernel data, higher Smith exponents, source membership, completion of the repair, or algebraicity.
