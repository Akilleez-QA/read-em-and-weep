# Symmetry and paired characters of the middle obstruction

## Pinned inputs and scope

Work over C with S=Sym(T), dim T=5. Fix any nonzero w in W. Use the actual graded module H, its symmetric perfect S-balanced pairing b_H of total degree five, L=Sw, A=H/L, and B=L^perp inside H. Thus B is a specified submodule, not merely an abstract module with the same Hilbert function. The pairing identifies B with D_5(A), and B is contained in L.

These facts and the quotient G=L/B are pinned in [PR514, commit d915ed6a7f0c679343447106707692eb7bdee6f7](https://github.com/Akilleez-QA/read-em-and-weep/blob/d915ed6a7f0c679343447106707692eb7bdee6f7/research/hm/cyclic-submodule-duality/PROOF.md). The original H has pure resolution shifts 0,2,4,6,8,10, by [PR499, commit 1112189481554b0353c64178e3adc0dede2c3fbe](https://github.com/Akilleez-QA/read-em-and-weep/blob/1112189481554b0353c64178e3adc0dede2c3fbe/research/hm/middle-euler-ghost-exclusion/PROOF.md).

[PR516, commit 89b66cbede7513c4f196fdbda0ee3bb77c53d2e0](https://github.com/Akilleez-QA/read-em-and-weep/blob/89b66cbede7513c4f196fdbda0ee3bb77c53d2e0/research/hm/gorenstein-resolution/PROOF.md) defines

Q_w = delta^(-1) Tor_2(B -> L)_5 : Tor_2(B)_5 -> Tor_3(A)_5,

where delta:Tor_3(A)_5 -> Tor_2(L)_5 is the connecting isomorphism for 0 -> L -> H -> A -> 0. Both spaces have dimension 26. Their kernel/cokernel dimensions are the common middle ghost number b=beta_(3,5)(G)=beta_(2,5)(G).

For the character conclusions we use the same equivariant duality as PR516: the Heisenberg group Gamma fixes W, preserves b_H, and lies in SL(T). Both middle spaces have character Reg+1 for Gamma/Z(Gamma)=(Z/5)^2. The Gamma-invariance of b_H comes from the equivariant trace pairing on End_0(F) and equivariant Serre duality; Gamma is contained in SL(T), so there is no ambient determinant-character correction. See the linearization check in [PR464 review, item 4, commit a091db646c2ad9ba73d0893f4d92ff54891aaf0c](https://github.com/Akilleez-QA/read-em-and-weep/blob/a091db646c2ad9ba73d0893f4d92ff54891aaf0c/research/hm/exact-sextic-saturation/REVIEW.md). The symmetry theorem itself needs no group action. All claims are structural and uniform; no selected actual instance is evaluated.

## 1. The chain-level sign

Write K_i(M)=M tensor Lambda^i T for the Koszul complex, with differential

d(m tensor x_1 wedge ... wedge x_i)
 = sum_r (-1)^(r-1) x_r m tensor x_1 wedge ... omit x_r ... wedge x_i.

The internal-degree-five complex has K_i(M)_5=M_(5-i) tensor Lambda^i T. The pairing b_H gives perfect pairings

< , > : K_i(H)_5 times K_(5-i)(H)_5 -> det(T)

by <h tensor alpha,k tensor beta>=b_H(h,k) alpha wedge beta. Its transposition sign is (-1)^(i(5-i)). In particular swapping degrees two and three has sign +1.

For z in K_i(H)_5 and t in K_j(H)_5 with i+j=6, balance gives

<dz,t> + (-1)^i <z,dt> = 0.                         (1)

Indeed write the differential as sum_a x_a tensor contraction_a. Move x_a between coefficient factors using S-balance, then use

contraction_a(alpha wedge beta)
 = contraction_a(alpha) wedge beta + (-1)^i alpha wedge contraction_a(beta).

Here alpha wedge beta is zero in Lambda^6 T, so its contraction is zero. This derives (1) with the stated sign, rather than assuming a self-duality sign for a minimal resolution. For i=j=3, (1) says

<dz,t>=<z,dt>.                                      (2)

## 2. The actual obstruction is symmetric

Set V=Tor_2(B)_5. Because the pairing on H is perfect and B=L^perp, it induces perfect pairings between K_i(A)_5 and K_(5-i)(B)_5. The adjoint differential identity (1) identifies these finite complexes as dual complexes with the usual signs. It consequently induces a perfect pairing

Tor_3(A)_5 times V -> det(T).

Thus Q_w defines a det(T)-valued bilinear form q_w on V, with convention

q_w(v,v')=<Q_w(v),v'>.

We prove that this form is symmetric.

Let b,c in K_2(B)_5 represent v,v'. The complex K(H)_5 is acyclic: all Tor_i(H)_5 vanish by the even pure shifts. Hence choose z,t in K_3(H)_5 with dz=b and dt=c. The image of z in K_3(A)_5 is a cycle, and the connecting convention delta([z mod L])=[dz] shows that it represents Q_w(v). Therefore

q_w(v,v')=<z,c>.

This expression is independent of all choices. If z changes by a cycle in K_3(H)_5, that cycle is d eta by acyclicity, and <d eta,c>=0 by (1) and dc=0. If b changes by d beta with beta in K_3(B)_5, use z+beta; the extra pairing <beta,c> is zero since B is isotropic. If c changes by d gamma with gamma in K_3(B)_5, equation (2) gives <z,d gamma>=<b,gamma>=0, again by isotropy. Here isotropy follows from B contained in L and B=L^perp. (In this particular degree K_3(B)_5 is actually zero; the argument does not need that extra simplification.)

Using (2) and the degree-two/degree-three swap sign now gives

q_w(v,v')=<z,dt>=<dz,t>=<b,t>=<t,b>=q_w(v',v).

This proves symmetry. Reversing the convention for the connecting map negates the whole form and does not change the assertion. The assertion concerns the pairing-induced identification of B with D_5(A); arbitrary unrelated coordinates on source and target need not display a symmetric matrix.

In particular Q_w is not forced to be alternating by its middle position. No assertion that b or rank(Q_w) is even follows from symmetry alone.

## 3. Inverse-character degeneracy is paired

Trivialize det(T); Gamma preserves this trivialization because Gamma is contained in SL(T). The induced q_w is Gamma-invariant. Decompose

V=V_1 direct_sum (direct_sum over chi != 1 of V_chi),

dim V_1=2 and dim V_chi=1 for every nontrivial character chi of Gamma/Z(Gamma). Invariance implies q_w(V_chi,V_psi)=0 unless chi psi=1. The quotient group has odd order, so its 24 nontrivial characters form precisely 12 unordered distinct pairs {chi,chi^(-1)}.

Choose bases on each pair. By symmetry the restriction to that pair has matrix

[ 0  a_chi ]
[ a_chi  0 ].

Thus each inverse pair contributes either zero or two to rank and either two or zero to the radical dimension. Equivalently the chi and chi^(-1) scalar blocks of Q_w have equal rank and equal corank. This equality does not follow merely from equivariance of a map between two copies of Reg+1.

If m is the number of inverse pairs on which a_chi=0, and b_1 is the radical dimension of the symmetric form on the two-dimensional trivial-character space, then

b=2m+b_1, with 0<=m<=12 and b_1 in {0,1,2}.

The nontrivial-character part of each middle ghost is therefore an inverse-pair-stable sum of characters. Odd total b is possible only if the trivial block has radical dimension one. We do not prove that this case occurs or is excluded.

## 4. Determinant reduction and exact remaining dependency

In the paired bases above, let C be the symmetric two-by-two trivial-character block. The block decomposition proves the identity

det(q_w)=det(C) product_{12 inverse pairs} a_chi^2.

Each two-by-two block has determinant -a_chi^2, and the 12 signs multiply to +1. A basis change multiplies this formula by the expected square of a nonzero basis determinant; the vanishing criterion is intrinsic.

Consequently the middle ghost vanishes exactly when det(C) is nonzero and all twelve pair scalars are nonzero. The earlier 24 nontrivial scalar invertibility questions reduce to twelve paired questions, and every nontrivial-character failure contributes at least two middle ghosts. Neither symmetry nor this factorization proves any scalar nonzero or determines the rank of C. In particular the total numerical range 0<=b<=26 is not sharpened without more information.

These are original-module Koszul and representation-theoretic conclusions conditional on the pinned inputs. They make no claim concerning first-order source liftability, higher-order lifting, or algebraicity. No actual HM matrix, numerical rank, coefficient search, or large computation was used. This is an authored proof awaiting independent mathematical review, not a formal proof-assistant check.
