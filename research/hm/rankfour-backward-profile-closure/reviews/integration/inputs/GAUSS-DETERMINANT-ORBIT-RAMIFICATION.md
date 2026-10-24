# Icosahedral orbit ramification and sharper rank-two exclusions

## Result and scope

For the actual G action on T=P^1, every effective zero divisor of a determinant derivative in a saturated Gauss filtration has degree in

    <12,20,30> = {12a+20b+30c : a,b,c nonnegative integers}.

Consequently the half-degree epsilon_i=delta_i/2 in the rank-two plateau identity belongs to <6,10,15>, not merely to the nonnegative integers.

Together with a stronger endpoint-span argument, this reduces the still-possible rank-two plateau profiles to

    (k,l) = (1,1), (1,2), or (2,1).                (1)

This does not exclude actual generic SF rank two. It does not increase the already proved positive-square rank lower bound 26 or settle the generic four-or-five count. No horizontal decomposition, actual coefficient evaluation, actual matrix/rank test, or local-model experiment is used.

The frozen rank-one and initial rank-two plateau files remain unchanged. This note adds new necessary conditions and exclusions.

## 1. Orbit sizes and stabilizers

The projective action factors through A5 of order 60; the center of the binary icosahedral group acts trivially on T. A finite stabilizer of a point of P^1 in characteristic zero is cyclic: its action on the tangent line is faithful, since a finite-order projective transformation fixing a point with derivative one is the identity. The only possible nontrivial cyclic subgroup orders in A5 are 2,3,5.

Thus orbit sizes are 60,30,20,12. More precisely there is one exceptional orbit of each of the last three sizes. The 15 involutions fix 30 points in total, each with stabilizer order two. The 20 elements of order three have 40 fixed-point incidences, two per point, giving 20 points. The 24 elements of order five have 48 incidences, four per point, giving 12 points. Stabilizers cannot mix these orders because they are cyclic and A5 has no cyclic subgroup of order 6,10, or 15.

Every effective invariant divisor is therefore a nonnegative combination of the exceptional orbit divisors and ordinary orbits of degree 60. Since 60 is already in <12,20,30>, its degree belongs to that semigroup.

All Gauss transforms and derivative maps are G-equivariant. Taking the determinant of a generically invertible derivative between equal-rank blocks gives a nonzero equivariant morphism of line bundles. Its effective zero divisor is G-invariant. This proves the stated degree restriction, including zeros at special and ramified parameters.

## 2. Exact orbit refinement of the frozen plateau bound

Keep the notation of RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md:

    m=k+l,     p=17-2k,     q=13-2l,
    C=20k+10l-kl(k+l-3).

The exact defect identity is

    C = l alpha + k beta + sum_(j=1)^(m-1) w_j epsilon_j,

where alpha,beta are nonnegative integers,

    w_j = l j              if j<k,
          k(m-j)           if j>=k,

and now

    epsilon_j in <6,10,15>.                        (2)

A particular block is forced unramified by these numerical conditions precisely when

    C-6w_j is not in <k,l>.                        (3)

Here "precisely" refers only to feasibility of this integer defect identity, not to existence of any actual geometric profile. To prove it, if epsilon_j>0 then epsilon_j>=6, and all remaining terms, including w_j(epsilon_j-6), lie in <k,l>. Conversely, a nonnegative representation of C-6w_j by k,l satisfies the numerical identity with epsilon_j=6, all other epsilon zero, and appropriate alpha,beta. No map is constructed in this converse.

Among the profiles allowed by the frozen inequality, those forced entirely unramified are exactly

    (3,6), (4,5), (5,4), (7,3).                   (4)

The last case illustrates why the semigroup test is stronger than the size test: C=23 and the smallest ramification cost is 18, but the remainder 5 is not in <3,7>.

Whenever delta_j=0, the rank-two derivative has nowhere-zero determinant and is an isomorphism

    L_j -> L_(j+1) tensor Omega.

If every plateau divisor vanishes, it follows equivariantly that

    L_i is isomorphic to L_1(2i-2).

These are bundle isomorphisms induced by derivatives on the graded pieces. They do not assert a splitting of the original filtered bundle or a horizontal direct sum of two curves.

## 3. Every interior plateau stage has both nondegeneracy properties

Write the saturated plateau as

    F_0 subset F_1 subset ... subset F_m,
    rank F_i=p+2i,     F_k=E.

For every 1<=i<m, beta_(F_i) has generic rank two. Moreover,

    ker beta_(F_i) = F_(i-1),     F_i^+ = F_(i+1).  (5)

For the kernel equality, the inclusion follows from differentiation. Its generic rank equals rank F_i minus two, exactly rank F_(i-1). Both sides are saturated in the ambient bundle, so equality of generic fibers proves equality of sheaves. For the forward equality, the saturated derivative image is contained in F_(i+1), has its rank, and both subbundles are saturated in the ambient bundle.

It follows that every F_i with i<m contains no nonzero constant subbundle. For i<=k this follows from F_i subset E and H0(E)=0. For i>k any constant subbundle is contained in ker beta_(F_i)=F_(i-1); applying (5) repeatedly brings it into E, a contradiction.

Dually, every F_i with i>0 spans the whole constant ambient space. This is immediate for i>=k. For i<k, a proper constant subbundle containing F_i would contain its forward transform F_(i+1) by (5), and hence eventually E, again a contradiction.

These facts strengthen the endpoint information; they do not claim that the two endpoints themselves have both properties.

## 4. Stronger endpoint span and degree bounds

The lower endpoint F_0 has rank p and generic SF rank one. Let U be its smallest constant span, of dimension n. The forward Gauss transforms of F_0 lie in the corresponding F_j, by induction from dF_j subset F_(j+1) tensor Omega and saturation.

Inside U, the rank-one forward transforms grow by one until reaching U. They cannot reach that constant subbundle in at most m-1 steps, because the relevant interior F_j contains no nonzero constant subbundle. Thus

    n-p >= m.

F_0 has no nonzero constant subbundle, so the proved complete rank-one flag theorem applies inside U and gives

    a:=deg F_0 <= -p(n-p) <= -pm.                  (6)

For the upper endpoint, apply the same argument to A=F_m^perp in the dual constant bundle. It has rank q, generic SF rank one, and no nonzero constant section because F_m spans the ambient space. Its j-th forward transform lies in F_(m-j)^perp. For j<=m-1 the latter has no constant section, because F_(m-j) has full span by Section 3. Hence the constant span of A has dimension at least q+m, and

    b:=deg F_m = deg A <= -qm.                     (7)

No decomposition of either constant span, or of the ambient G-module, is used.

Combine (6)-(7) with the exact plateau identity. Since deg E=-54,

    54 >= lp+kq+2kl = 17l+13k-2kl.                (8)

In the established ranges 1<=k<=8, 1<=l<=6, this leaves only

    (1,1), (1,2), (2,1), (2,2), (3,1).            (9)

In particular all four orbit-forced unramified profiles in (4) are excluded by this stronger geometric bound.

## 5. The strengthened effective-defect identity

All stage determinant degrees are even, as proved in the frozen plateau note. Since p,q are odd, let eta=0 if m is even and eta=1 if m is odd. Write

    a=-pm-eta-2alpha,
    b=-qm-eta-2beta,

with alpha,beta nonnegative integers. The plateau identity becomes

    C_strong = l alpha + k beta + sum_j w_j epsilon_j,

where the w_j are as in Section 2, epsilon_j belongs to <6,10,15>, and

    C_strong = (m/2) [54-(17l+13k-2kl)-eta].        (10)

For the five profiles in (9), its values are respectively 26,15,21,4,8.

The following useful rank-one endpoint test will be applied twice. For a rank-r subbundle of degree -D with generic SF rank one, no common constant subbundle, and constant span dimension n=r+s, the complete-flag identity says

    n(D-rs)
      = s sum_(j<r) j delta_j
        +r sum_(j>=r)(n-j) delta_j.                (11)

All these rank-one derivative divisors are also G-invariant. Therefore the right side, when nonzero, is at least 12 min(r,s). More precisely it belongs to

    <12r,20r,30r,12s,20s,30s>.                    (12)

This is a necessary numerical condition only. It does not assert geometric realization of each semigroup element.

## 6. Exclude (k,l)=(2,2)

Here m=4, p=13, q=9, and C_strong=4. Every ramification contribution is at least 12, so all epsilon_j vanish. Equation (10) gives alpha+beta=2.

Let c_1=deg L_1. Unramified rank-two blocks have c_i=c_1+4(i-1). The prefix degree equation for E is

    -54=(-52-2alpha)+2c_1+4,

so c_1=alpha-3. Since c_1 is even, alpha=1 and beta=1. Thus

    a=-54,     b=-38.

The constant span of F_0 has dimension at least p+m=17. The rank-one bound D>=p(n-p), with D=54 and p=13, forces that dimension to be exactly 17. In (11), r=13, s=4, and the required ramification weight is

    17(54-13*4)=34.

A nonzero weight would be at least 12*4=48, while zero weight would be zero. This contradiction excludes (2,2).

## 7. Exclude (k,l)=(3,1)

Here m=4, p=q=11, a=-44-2alpha, b=-44-2beta, and (10) is

    alpha+3beta+epsilon_1+2epsilon_2+3epsilon_3=8.

Thus epsilon_2=epsilon_3=0, and epsilon_1 is either 0 or 6.

### 7.1. Force the upper endpoint to be unramified

The upper annihilator A=F_4^perp has rank 11 and degree -(44+2beta), with beta in {0,1,2}. Its constant span has dimension at least 15 by Section 4; the rank-one bound and 44+2beta<=48 force that dimension to be exactly 15.

If beta=1, (11) would require weight 15(46-44)=30, below the least positive weight 48. If beta=2, the required weight is 60. It is not in

    <48,80,120,132,220,330>:

below 80 the only positive available value is 48. Thus beta=0.

If epsilon_1=6, the defect identity gives alpha=2. The lower endpoint would then also have rank 11, span dimension 15, and degree -48; the same required weight 60 is impossible. Hence

    alpha=8, beta=0, and all plateau epsilon_j=0.

In particular A has rank 11, degree -44, and span dimension 15. Equality in the complete rank-one degree bound forces every divisor in its full rank-one flag to vanish. Its first forward transform A^+ has rank 12 and degree

    -12(15-12)=-36.                               (13)

### 7.2. Project E without assuming a horizontal splitting

Let W be the 15-dimensional constant span of A inside H*. Then A^+ is a saturated rank-12 subbundle of W tensor O_T. The dual derivative inclusion gives

    A^+ subset E^perp.

The intersection E^perp with W tensor O_T has rank exactly 12. If it had rank 13, all of E^perp would lie in W tensor O_T, so E would contain the nonzero constant subbundle W^perp tensor O_T, contradicting H0(E)=0. Since the intersection and A^+ are saturated in W tensor O_T and have the same generic fiber, they are equal.

Consider the restriction projection H tensor O_T -> W* tensor O_T and its image I on E. The saturation of I is the annihilator of A^+ in W* tensor O_T, namely

    P=(W tensor O_T/A^+)*.

This bundle has rank 3 and degree -36 by (13). The actual image I is a rank-3 subsheaf of P with torsion quotient, so

    deg I <= -36.

Its kernel K in E has rank 14, and exactness gives

    deg K = -54-deg I >= -18.

But K subset E implies H0(K(1))=0; splitting on P^1 then forces every summand of K to have degree at most -2, and hence deg K<=-28. This is a contradiction.

The inequality direction explicitly allows torsion in P/I. No equality of the actual image with its saturation, and no horizontal splitting, was assumed.

## 8. Remaining scope

Sections 6-7 remove the last two profiles in (9), leaving exactly the necessary list (1). No realization is asserted for any remaining profile. Additional geometry is still needed to exclude them or to determine the actual SF rank.

## Reproduction

Run `python verify_gauss_determinant_orbit_ramification.py`.

The verifier checks exact orbit counts, universal degree identities, bounded hypothetical integer profiles, and the small semigroup contradictions in Sections 6-7. These are universal representation/degree consequences, not actual map or rank evaluations.

Dependencies are the frozen RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md, RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md, and TWIST-ONE-ACTUAL-SECTION-KERNEL-VANISHING.md. The geometric saturation, actual bundle identifications, and cohomology inputs remain those proved there.
