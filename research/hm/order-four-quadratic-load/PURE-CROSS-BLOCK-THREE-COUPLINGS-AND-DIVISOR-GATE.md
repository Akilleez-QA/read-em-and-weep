# Three pure cross-block couplings, the diagonal jet, and divisorial failure of saturation

## Scope

Let T=P(W*) and let F4=ker[C_lin->O_T(2)]. We use the actual pure-vertex restriction j:S7*->K8 proved injective in PURE-VERTEX-SQUARE-INJECTION-AND-RANK-TWO-TO-SIX-GATE.md. This note identifies its cross-block section and a three-dimensional universal coupling space. It does not select the actual couplings, assert an actual fiber rank, or prove saturation.

## 1. The raw section and the justified diagonal factor

On T_r x T_s let D be the diagonal and define the actual raw pure cross block

    R(r,s)=delta_r(q0 ell_s^8).

Here ell_s^8 means the pure eighth-power vector in the Cartan Sym^8 W summand of Sym^2 D5, where D5=Sym^4 W. The target of delta_r is C_lin(2)_r; the invariant projected channel annihilates this Cartan summand, so R lies in

    H0(T x T, pr1*F4(2) tensor pr2*O(8))^G.          (1)

At s=r, both ell_r^8 and its first s-derivative 8 ell_r^7 v are actual square products at H_r. Their q0 multiples extend on that same hyperplane. Thus delta_r annihilates both. Consequently R is scheme-theoretically divisible by D^2, giving a canonical invariant section

    T2=R/D^2 in H0(T x T, pr1*F4 tensor pr2*O(6))^G. (2)

D is defined by the invariant alternating determinant [ell_r,ell_s], so this division is equivariant and independent of affine root frames.

There is NO automatic third-order vanishing. The second derivative is a pure Cartan vector, not generally an actual square vector. For example, with ell=x and v=y, the actual square (x^3 y) symmetric-product (x^3 y) has second transvectant -18 x^4. It therefore has a nonzero low Sym^4 W component, whereas the pure Cartan vector x^6 y^2 has zero second transvectant. The actual boundary annihilates the former square, not each of its irreducible components separately. This distinction is essential.

Equivalently, the diagonal value of (2) is a nonzero normalization multiple of the low-Sym^4 Veronese boundary delta_r(q0 iota4(ell_r^4)). That boundary is not proved zero. The exact numerical multiple depends on the normalization of iota4; only its nonvanishing as a universal scalar is used.

## 2. Exactly three abstract couplings

The seven established F4 types all have nonnegative summand degrees and the same global character

    H0(F4)=1+2A+V+2P4+2D5.

Since Sym^6 W=V+P4, equation (2) belongs to the intertwiner space

    Hom_G(Sym^6 W,H0(F4)),

of dimension THREE. This is one V coupling and two P4 couplings, after choosing a basis of the multiplicity-two P4 space. The actual section is nonzero, by the actual P4 boundary nonvanishing used to prove j nonzero. No assertion that any particular one of these three couplings is nonzero follows merely from its availability.

## 3. One diagonal scalar and a conditional higher-order statement

Restricting (2) to D gives a section of F4(6), not F4(4). The diagonal restriction exact sequence is

    0 -> F4(-1) external-tensor O(5)
      -> F4 external-tensor O(6) -> F4(6)|D -> 0.

All summand degrees of F4(-1) are at least -1, so its H1 vanishes. Taking invariant global sections remains exact in characteristic zero. The universal character calculation gives

    dim H0(F4 external-tensor O(6))^G = 3,
    dim H0(F4(-1) external-tensor O(5))^G = 2,
    dim H0(F4(6))^G = 1.

Thus the order-two diagonal leading jet is controlled by a single scalar quotient of the three-dimensional coupling space. It is not forced to vanish.

There is a useful CONDITIONAL refinement. If that scalar is zero, then R is divisible by D^3. Its divided section T3 lies in F4(-1) external-tensor O(5), whose restriction to D lies in F4(4). For all seven types,

    H0(F4(4))^G=0.

Therefore T3 vanishes on D and R is then divisible by D^4. Hence exact diagonal order three cannot occur. The alternatives are order two or order at least four; we do not choose between them. In particular no unconditional vanishing of j along the discriminant is asserted.

## 4. Off-diagonal zeros are exactly the divisorial torsion gate

Over distinct roots r!=s, source S7* splits into two root lines and K8 into the two four-dimensional root fibers. In these frames the pure map j has zero same-root blocks and cross blocks

    [ 0, R(r,s)/(s-r) ; R(s,r)/(r-s), 0 ],           (3)

up to the invertible complementary-root normalization factors. Same-root vanishing follows from the first derivative 8 ell^7 v being an actual square product. These factors are units off D and cannot affect rank there.

The two columns of (3) have disjoint root target summands. Hence j has rank below two at an off-diagonal point exactly when T2(r,s)=0 or T2(s,r)=0. This is a statement about this actual section, not a generic choice of three couplings.

More precisely, let E_div be the divisorial common-zero cycle of T2 away from D, and let tau exchange the roots. At a codimension-one point, each column contributes its minimum coordinate valuation to the maximal-minor ideal. Therefore the divisorial degeneracy cycle of nu*j away from D is

    E_div + tau(E_div).                              (4)

Equivalently, the divisorial torsion cycle of coker(j) off the discriminant is the norm/pushforward cycle nu_*E_div. This treats symmetric components with their correct multiplicities: a tau-invariant component is counted twice in (4). Isolated common zeros do not contribute divisorial torsion.

The diagonal/discriminant is excluded from this calculation. Its contribution requires the actual diagonal jet, and must not be reconstructed by treating a double root as two independent reduced roots.

## 5. Elementary constraints on a possible common-zero divisor

The cycle E_div is G-stable. In the known splitting types every nonzero component of T2 has bidegree (d_i,6), with 0<=d_i<=18. Thus its common divisor, if present, has bidegree (p,q) with 0<=p<=18 and 0<=q<=6.

There is no purely horizontal component (a whole T_r fiber at a fixed s). Such components would give a G-stable effective divisor of degree at most six on the second P1, but every nonempty A5 orbit there has size at least twelve. Vertical components are not ruled out by this argument: their first degree may be twelve. Mixed invariant curves are also not excluded.

These are necessary constraints, not an existence claim. The problem of determining the actual common-zero divisor remains a geometric question about the actual three couplings.

## Reproducibility and limits

verify_pure_cross_block_couplings.py checks all seven types, the dimensions 3,2,1, the vanishing H0(F4(4))^G, and the nonzero low transvectant of the second-derivative square. These are universal character and polynomial calculations, not evaluations of actual HM coefficients or a selected residual matrix.

Dependencies: the actual residual cross-root formula and projected Cartan annihilation; the actual pure-vertex injection; and the established seven F4 types. No complete repair, selected coupling value, or generic-rank improvement is inferred from this factorization alone.
