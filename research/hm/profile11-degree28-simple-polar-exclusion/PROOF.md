# A simple invariant polar excludes the last positive-O14 defect-twelve label

## Result and scope

The maximal profile-(1,1) Gauss label

    G3.11.64d33b6d4139,
    A_q=2 O(-8)+O(14),
    B_q=O(-28)+2 O(6),
    original determinant defect=12,

is impossible. The obstruction lies in the degree-twenty-eight constant block forced by its top quadratic bundle. It does not lie in its separate abstract rank-three residual.

The unique V channel in the degree-twenty-eight quotient is divisible by the invariant degree-twelve form exactly once along its twelve-point divisor. This forces a nonzero projective derivative there. The actual top-block Gauss derivative is required to vanish on that same divisor. These conclusions contradict one another.

No selected actual HM/source-instance coefficient, parameter, point, derivative value, matrix or rank is evaluated. The proof uses only universal irreducible multiplicities, invariant divisors, and an arbitrary-point identity for a quotient and its kernel. It does not prove SF>=4, the original research goal, higher-order lifting, or algebraicity.

## 1. Immutable dependencies and the actual constant block

The companion source-reduction and saturated-residual theorem is public in PR801, commit

    4301e3b3027afa1c32e1e7359a5fdf5b9d27edfd,

at

https://github.com/Akilleez-QA/read-em-and-weep/blob/4301e3b3027afa1c32e1e7359a5fdf5b9d27edfd/research/hm/profile11-defect12-constant-residual/PROOF.md

Its independently reviewed proof has SHA256

    0e28eed42faf99a0ebaed4bfcf7e54b20f0e13d642f92f61864e421043e71915.

It proves that the complete source overlist for the stated label reduces to E10, and supplies the following actual objects in the original constant thirty-space H:

    E10=(P+2D) O(-2)+O(-8)+W O(-9),
    F=(P+2D) O(-2),
    F^+=C O,
    C=A+V+P+D,
    0 -> F -> C O -> O(28) -> 0.                       (1)

Here C is a genuine constant fifteen-dimensional subspace, not an abstract bundle complement. The quotient O(28) in (1) embeds saturatedly in Q=(H O)/E. The full derivative of F has image O(14) inside

    (C O/F)(-2)=O(26),

and that inclusion is multiplication by a nonzero invariant form f12 of degree twelve. This follows from Sections2-3 and5 of the cited theorem: J=0, the full top-image saturation defect is twelve, and its saturated projection to the original positive O(26) line is an isomorphism. Thus no internal component remains that could conceal the external zero.

Let D12 be the divisor of f12. Every projective binary-icosahedral orbit has at least twelve points. Since D12 is invariant of degree twelve, it is a single twelve-point orbit with every multiplicity one. The derivative of F therefore vanishes on each fiber over D12:

    beta_F(x)=0 for every x in D12.                     (2)

We use the same binary-icosahedral representations as the companion theorem: W is the defining two-space, Wp the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P are the other even three- and four-spaces. All irreducibles are self-dual.

The original catalog and orbit convention are pinned at db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md and ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md. No further source stratum or selected model is introduced here.

## 2. The unique V channel has exactly one invariant factor

The bounded universal character identities are

    Sym4 W=D,
    Sym12 W=1+A+P+D,
    Sym16 W=V+P+2D,
    Sym28 W=A+V+2P+3D.                                 (3)

In particular V has multiplicity one in both Sym16 W and Sym28 W. Multiplication by the nonzero invariant f12 is an injective G-equivariant map

    Sym16 W -> Sym28 W.

It maps the unique V summand nontrivially to the unique V summand. Therefore those actual polynomial subspaces satisfy

    V28=f12 V16.                                       (4)

This is an equality of universal irreducible subspaces, not a choice of an actual coefficient map.

The V16 subsystem of H0(O(16)) is basepoint-free. To see this, its common zero divisor is invariant. If nonempty, its degree is at least twelve and at most sixteen. Projective orbit sizes are 12,20,30,60, so its degree must be twelve. Its defining polynomial spans a G-stable line; the binary icosahedral group has no nontrivial one-dimensional characters, so that polynomial is invariant. By (3), the invariant line in Sym12 W is unique, and the divisor is therefore D12. Dividing every section by f12 would then give a nonzero equivariant injection

    V -> H0(O(4))=D,

which is impossible for distinct irreducibles. Hence no common zero exists.

Since f12 has simple zeros and V16 has no common zero, (4) has the following uniform consequence: at every x in D12, all sections in V28 vanish, but not all of their first derivatives vanish. This assertion is independent of local trivialization, because the sections themselves vanish at x. It is a universal assertion for all points of the invariant divisor, not an evaluation at a selected point.

For reproducibility, (3) follows from Sym(n+1) W=W tensor Sym(n) W-Sym(n-1) W and the nine fixed McKay tensor identities

    W tensor 1=W,       W tensor W=1+A,
    W tensor A=W+S,     W tensor S=A+D,
    W tensor D=S+T,     W tensor T=D+V+P,
    W tensor V=T,       W tensor P=Wp+T,
    W tensor Wp=P.

This is a bounded representation-ring identity, not a computation on a source instance.

## 3. The quotient curve has a nonzero derivative on D12

Let

    q:C O -> O(28)

be the actual quotient in (1). It is onto at every point. Since H0(F)=0, its map on global sections is an injective equivariant linear system

    C -> H0(O(28))=Sym28 W.                             (5)

In particular, the V summand of C maps isomorphically onto V28, because both copies occur with multiplicity one. By Section2, at every x in D12 the V component of q has zero value but nonzero first derivative as a vector of linear forms on C_V.

Fix an arbitrary x in D12. Trivialize O(28) near x and write q as a local nonzero row of functions. Because q is onto, q(x) is a nonzero functional on C. Its restriction to C_V is zero, while the restriction of its derivative q'(x) to C_V is nonzero. Hence

    q'(x) is not a scalar multiple of q(x).              (6)

Equivalently, the classifying map to P(C*) given by the quotient q has nonzero projective derivative at x. Changing the trivialization adds a multiple of q(x) to the derivative and does not affect (6).

## 4. Kernel and quotient Gauss derivatives give the contradiction

For clarity, the equivalence needed here is an elementary connection identity. A local section s of F satisfies q s=0. Differentiating gives

    q s'=-q' s.

Under C O/F=O(28), the left side is the second fundamental form of F. Therefore beta_F(x)=0 if and only if q'(x) annihilates ker q(x), equivalently if and only if q'(x) is proportional to q(x).

Equation (6) thus implies beta_F(x) is nonzero. This contradicts (2), which required beta_F to vanish at every point of D12. The formal E10 branch is impossible. Since the cited companion theorem exhaustively removed the other source strata, the full label G3.11.64d33b6d4139 is excluded.

## Verification boundary and relation to the abstract residual

The decisive derivative calculation is the universal identity between a quotient and its kernel, applied at an arbitrary point of an invariant divisor. No actual source coefficients or derivative values were selected or evaluated. The nonzero derivative is forced by an irreducible polynomial channel with a simple invariant factor.

The abstract family in PR801's separate UNIVERSAL-RESIDUAL-COMPATIBILITY.md remains valid. It constructs the rank-three residual Z=O(-8)+W O(-9) in a fifteen-dimensional constant quotient. It never constructs the original complementary degree-twenty-eight quotient (1) with its prescribed twelve-point Gauss ramification. The present obstruction lies precisely in that missing constant block, so it does not contradict the residual construction or turn it into an actual HM realization.
