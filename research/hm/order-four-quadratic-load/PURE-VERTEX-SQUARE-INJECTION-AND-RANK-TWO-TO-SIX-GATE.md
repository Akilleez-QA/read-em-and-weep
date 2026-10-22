# Pure vertex squares inject and reduce the actual residual gate to rank two into rank six

## Theorem

For the actual equivariant residual map on P=P(Sym^2 W),

    m_res: W tensor S6* -> K8,

there is a canonical rank-two subbundle S7* of the source. The actual restriction

    j: S7* -> K8

is injective as a sheaf map. Put Q6=coker(j). It is a coherent sheaf of generic rank six, NOT asserted to be locally free or torsion-free. There is an actual induced map

    m_bar: S5* -> Q6

and a canonical equality of kernel sheaves

    ker(m_res) = ker(m_bar).                         (1)

At the generic point, m_bar has rank zero or two. Consequently the remaining generic injectivity question is an actual two-to-six gate, rather than four-to-eight.

Moreover, if m_res has generic rank two, Q6 must have divisorial torsion: its torsion contains S5*/ker(m_res), whose divisorial degree is d-4>=2, where c1(ker(m_res))=-d. In particular, proving Q6 torsion-free in codimension one would settle residual generic rank four. We do not prove that saturation statement here.

## 1. Canonical root Euler sequence

On the root pencil T=P(W*) the standard rank-two Euler sequence is

    0 -> O_T(5) -> W tensor O_T(6) -> O_T(7) -> 0.

Pull it to the universal finite-flat length-two root scheme and push by nu. Exactness of finite pushforward gives

    0 -> S5 -> W tensor S6 -> S7 -> 0.

All terms are locally free on P, including along the discriminant. Dualizing gives the exact bundle sequence

    0 -> S7* --i--> W tensor S6* -> S5* -> 0.        (2)

For root normalization, use S_n*=nu_*eta*O_T(-n) tensor O_P(1), valid for these n. Sequence (2) is the pushforward of

    0 -> O_T(-7) -> W tensor O_T(-6) -> O_T(-5) -> 0

followed by the common O_P(1) twist. The line in W selected at the root ell is ell itself. Thus the subbundle i has root value w in ell, not an arbitrary two-dimensional residual root value.

The existing actual residual formula uses

    b(ell)w=(ell^4) symmetric-product (ell^3 w).

On the selected line w=ell this is the pure vertex square ell^8 in the Cartan Sym^8 W summand of H0(B_R(3)). Therefore (2) identifies an actual pure-vertex-square subbundle, not merely a bundle with matching Chern classes.

## 2. The actual restriction is nonzero

Let delta_r be the actual relative plane boundary at root r, and q0 the invariant positive conic. The proved residual cross-root formula, for distinct roots r,s, is

    delta_r(q0 [b(s)w-b(r)w]/(s-r)).                 (3)

The same-root term delta_r(q0 b(r)w) vanishes because b(r)w is an actual square section on H_r. Restricting the source to i(S7*) selects w=ell_s in the s-root summand. Hence its cross component is, up to the nonzero root-coordinate normalization factor,

    delta_r(q0 ell_s^8)/(s-r).                      (4)

At distinct roots, values in the two root summands can be prescribed independently; the source identification differs from ambient-boundary coordinates only by invertible complementary-root factors. No statement about double-root fiber rank is used here.

If j=m_res i were the zero bundle map, (4) would vanish for every r!=s. For fixed r, polynomial continuation in s would give delta_r(q0 ell_s^8)=0 for all s. Pure eighth powers span Sym^8 W in characteristic zero. Thus delta5 would annihilate q0 Sym^8 W, contradicting the established nonvanishing on its genuine four-dimensional summand P4. Therefore j is nonzero.

This uses the actual P4 boundary theorem, not a character-theoretic inference that a nonzero abstract intertwiner must occur.

## 3. Parity upgrades nonzero to sheaf injectivity

The center of G=SL2(F5) acts trivially on P and on every G-linearized line bundle on P, since O_P(1) is center-even and G is perfect. The source S7* and target K8 are both center-odd. Were the nonzero j of generic rank one, the double dual of its image determinant would be a center-odd equivariant line bundle, a contradiction.

Thus j has generic rank two. Its kernel, as a subsheaf of the locally free S7*, is torsion-free and has generic rank zero. It is zero. This proves sheaf injectivity, not pointwise fiber injectivity or saturatedness of its image.

Set Q6=coker(j). Its generic rank is eight minus two, namely six. Any torsion, singularities, and exceptional-fiber degeneration are retained in this definition.

## 4. The quotient gate and exact kernel identification

Compare the exact rows

    0 -> S7* -> W tensor S6* -> S5* -> 0,
    0 -> S7* --j--> K8 -> Q6 -> 0,

with the identity on the first term and m_res on the second. They induce m_bar:S5*->Q6. The snake lemma, using that the first vertical map is an isomorphism, gives (1) globally, including the discriminant and finite singular sets.

On the generic point, ordinary rank additivity gives

    rank(m_res)=2+rank(m_bar).

The known even generic rank of m_res is two or four; hence rank(m_bar) is zero or two. On a common locally free dense open, this is literally a map from a rank-two vector bundle into a rank-six vector bundle. Away from the discriminant, it is also equivalent to injectivity of the full smoothing map because the projected rank-two channel is nonzero there.

If m_bar has generic rank zero, it may still be a nonzero torsion-valued sheaf morphism. It must NOT be replaced by the zero map globally. Likewise, Q6 is not silently replaced by its torsion-free quotient: doing that could change the kernel sheaf in (1).

## 5. Chern classes retain the coherent quotient

For n>=1, rank(S_n)=2, c1(S_n)=n-1 and c2(S_n)=n(n-1)/2. Thus

    c(S7*) = 1-6H+21H^2,
    c(S5*) = 1-4H+10H^2,
    c(W tensor S6*) = 1-10H+55H^2.

The last equality also follows by multiplying the first two, independently checking (2). Since c(K8)=1+24H+300H^2, exactness gives the coherent-sheaf Chern class

    rank(Q6)=6,   c1(Q6)=30H,   c2(Q6)=459H^2.       (5)

These are Chern classes in the K-theoretic sense for the coherent Q6, regardless of its torsion. They do not certify local freeness or positivity.

## 6. A rank-two residual alternative forces divisorial torsion

Suppose m_res has generic rank two. Then N=ker(m_res) has rank two. The established finite Chern gates give c1(N)=-d, with even d>=6. Equation (1) realizes N as a subsheaf of S5*, and exactness identifies

    S5*/N = im(m_bar) subset Q6.

This is a torsion sheaf, because m_bar has generic rank zero. Its first Chern class is

    c1(S5*/N)=(-4)-(-d)=d-4.

For a torsion sheaf on a smooth surface this is the effective divisorial support cycle, counted with generic lengths; zero-dimensional contributions have first Chern class zero. Thus Q6 contains a torsion subsheaf with positive divisorial degree d-4>=2. This is a precise necessary failure of saturatedness of j, not a claim that it occurs.

The conclusion is stronger than merely requiring some isolated bad fiber of j. If the cokernel of j has no divisorial torsion, the rank-two residual alternative is impossible and the generic residual rank is four.

## Sources and limitations

- RESIDUAL-SMOOTHING-NONVANISHING-AND-EVEN-RANK.md, Sections 4-7: actual P4 boundary nonvanishing; residual cross-root normalization; generic-rank parity; root-duality identity.
- RANK-TWO-RESIDUAL-KERNEL-FINITE-CHERN-GATES.md: even determinant and d>=6 for a hypothetical rank-two kernel.
- NONZERO-INVARIANT-SMOOTHING-CHANNEL-BY-FLAG-FILTRATION.md: actual residual map and the rank-two projected channel away from the discriminant.

The universal companion script checks only Chern accounting. The actual nonzero-map statement is established by the proof above and its cited actual P4 boundary theorem. No selected coefficients or actual ranks are evaluated, no complete full-adjoint repair is claimed, and no external post is performed here.
