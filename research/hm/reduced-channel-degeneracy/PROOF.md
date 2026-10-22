# Septic exterior minors exclude fat axes and make the family-detection locus reduced

## Statement and pinned inputs

Work over C. Let G=A5, A its rotation representation, X=P(A), and C⊂X its invariant square conic. Use the canonical endpoint interface of PR661–664: D is the five-dimensional module, P the lower four-dimensional endpoint module, and

0 → K → D⊗O_X → A⊗O_X(1) → 0,
Q=Q_+⊕Q_−,  dim Q_+=dim Q_−=1,
F=K*⊗P⊗O_X(2),  E:Q⊗O_X→F.

Each q∈Q gives the section t_q=q|K of F. For nonzero q, write Z_q for its zero scheme and Δ for the rank-at-most-one scheme of E. These are DIFFERENT constructions: the rank of the fixed map K→P(2) is also different from the rank of E.

Pinned dependencies:

- PR661, 1325647fd916bf2daa71b11efeae6d52cfefa2cd: canonical kernel and two parity channels.
- PR663, ad3ab59f6fbbbb3e5bde1da58b3b92a1f49c6889: neither parity section vanishes anywhere; E has rank at least one everywhere; the six C5 axes and ten C3 axes have rank exactly one.
- PR664, 90d9aa88b3cea99e8dd1acea0acda9095021185e: Supp(Δ) is either those sixteen axes or all thirty-one C5/C3/C2 axes.
- PR666, 0fc85f297a62c7be473a8da9ad992bb84706f8f2: every nonempty Z_q has length 6,10,15,16 or18. The sole possible nonreduced case is the six first infinitesimal C5 neighborhoods, with local ideal m_p². All other cases are reduced. The C2 channel, if present, is distinct from both C3 and C5 channels.
- PR667, 7d53ea234b99b75e89a29c4caba7ec564e134410, Sections 2–4 only: whenever q has nonzero symmetric component, its FIXED map K→P(2) has generic rank two already on C. This is the universal statement proved from the embedded symmetric osculating bundle; no actual-normal-variation hypothesis from later sections is needed here.

**Theorem.** The length18 and length16 cases are impossible. For every nonzero q∈Q, Z_q is reduced, with nonzero length among 6,10,15. The C3 and C5 kernel channels are distinct; if the C2 orbit occurs, its channel is distinct from both. Moreover Δ itself is reduced. Thus Δ is exactly the reduced union of the sixteen C5/C3 axes or the reduced union of all thirty-one axes.

This is a structural argument. It evaluates no selected actual HM endpoint or source instance, and uses no parameter scan or numerical computation.

## 1. The six C5 axes are in plane general position

Let Σ be the six C5 axes. Its stabilizer at an axis is D10=N_G(C5). A generator of C5 cannot fix a different axis in Σ: otherwise it belongs to the normalizer of that axis's C5 subgroup, whose unique order-five subgroup would then be the original C5. Thus C5 acts as a five-cycle on the other five axes. The G-action on Σ is consequently two-transitive.

All lines joining pairs of Σ therefore meet Σ in the same number k of points. Counting pairs gives b·k(k−1)/2=15, where b is the number of such lines. For 2≤k≤6 the only possibilities are k=2,3,6. If k=3, counting the five other points on lines through one point gives r(k−1)=5, impossible. If k=6, their unique common line is G-invariant, contradicting irreducibility of A. Hence k=2: no three axes are collinear.

Five points with no three collinear impose independent conditions on conics. For example, for each one of the five points, the product of the two lines pairing the other four points vanishes at those four but not at the chosen point. Thus each five-point subset of Σ lies on a unique conic. That conic is irreducible and smooth: a union of two lines, including a repeated line, could contain at most four points when no three are collinear.

The six axes cannot all lie on a conic. If they did, uniqueness through five would make its equation a G-stable line in Sym²A*. Since A5 has no nontrivial characters, this equation would be invariant. The invariant quadratic forms form a one-dimensional space by irreducibility and self-duality of A; its conic is C. But Σ is disjoint from C. This is a contradiction.

For each p∈Σ let C_p be the conic through Σ\{p}. These are six distinct smooth irreducible conics, and C_p does not contain p.

## 2. A septic cannot vanish to fourth order at all six axes

We prove

H⁰(X, (∩_{p∈Σ} m_p⁴)(7))=0.                    (1)

Suppose a nonzero septic f has multiplicity at least four at all six axes. Fix p. If C_p is not a component of f, Bézout gives intersection number 2·7=14. At each of the five points of Σ\{p}, the local intersection multiplicity is at least four: restricting an element of m_x⁴ to the smooth conic gives vanishing order at least four. This would give total intersection at least20, a contradiction. Thus every C_p divides f. They are distinct irreducible conics, so their product of degree12 divides the degree7 polynomial f, impossible. This proves (1).

This argument uses the multiplicities of exterior minors, not just the quintic generators of the zero ideal. The latter alone would not exclude the classical six-double-point quintic configuration.

## 3. Exterior minors rule out the last nonreduced fixed-channel scheme

The kernel sequence gives det K≅O_X(−3), up to a constant one-dimensional factor harmless for degrees. Therefore

Λ²(t_q):det K → Λ²P⊗O_X(4)

is a vector of global sections of O_X(7). Its scalar components are the 2×2 minors of a local matrix for the fixed map K→P(2), glued as septics.

Suppose Z_q is the remaining length18 possibility. At every p∈Σ, its defining ideal is m_p². The entries of t_q in local bundle frames generate that ideal, so each entry belongs to m_p². Every 2×2 minor consequently belongs to m_p⁴. By (1), all global exterior minors vanish identically. The fixed map therefore has rank at most one everywhere.

But q cannot be a parity channel, because neither parity section ever vanishes. In particular its symmetric component is nonzero. The universal generic-rank-two theorem of PR667 applies to its restriction to C, contradicting the identically vanishing exterior square. The length18 case is excluded.

PR666 now gives that every Z_q is reduced and its nonzero length is 6,10,15 or16. In particular length(Z_q)≤16. These are necessary possibilities, not an assertion that all four occur.

## 4. A stabilizer criterion transfers reducedness to the detection scheme

We give the local argument explicitly; reduced fixed-channel zeros do not imply reduced detection loci without an additional hypothesis.

Let a finite group H fix p on a smooth surface, let F be an H-equivariant bundle, and let s,t be H-invariant sections with s(p)≠0 and t(p)=0. Assume the zero scheme of t is reduced and supported at p locally. Then its local entries generate m_p. Equivalently the intrinsic derivative

dt_p:T_pX→F_p

is injective. This derivative is canonical because t(p)=0, and is H-equivariant.

Suppose also T_pX has no trivial H-subrepresentation. The line ℓ=Cs(p) is a trivial H-module. Since dt_p is injective, its image has no trivial subrepresentation either, and

dt_p(T_pX)∩ℓ=0.                                (2)

Near p the nonzero section s generates a line subbundle. The rank-drop ideal of the two-column map (s,t) is exactly the zero ideal of the image of t in F/O·s: locally put s into its first basis vector, and the 2×2 minors are precisely the remaining entries of t. The derivative of that quotient section at p is dt_p followed by projection F_p→F_p/ℓ; the terms differentiating the quotient trivialization vanish because t(p)=0. By (2) this derivative is injective. Thus the entries of the quotient section span m_p/m_p². Nakayama's lemma gives that their ideal is m_p itself. Hence the rank-drop scheme is reduced at p.

## 5. Apply the criterion at every exceptional axis

Every p∈Supp(Δ) has exact rank one. Choose a nonzero kernel-channel q and a complementary r∈Q. Put t=t_q and s=t_r. Both sections are invariant under the stabilizer H, since Q consists of equivariant families, and H acts trivially on the parameter space Q. We have t(p)=0 and s(p)≠0. By Section 3 the zero scheme Z_q is reduced at p.

It remains to check that T_pX has no trivial stabilizer constituent.

At a C3 or C5 axis, H is the respective dihedral normalizer. The cyclic subgroup fixes the axis line L⊂A and acts on A/L with two nontrivial inverse characters. Thus T_pX=L*⊗(A/L) has no invariants already under that cyclic subgroup. (The full tangent representation is in fact irreducible under H.)

At a C2 axis, H=V4. The rotation representation restricted to V4 is the direct sum of its three distinct nontrivial characters. One is the axis line L; dividing the other two characters by that of L gives the remaining two nontrivial characters. Thus T_pX again has no trivial H-constituent.

Section 4 applies at every point of Supp(Δ). Since that support is finite, it follows that Δ is reduced everywhere. Its length is therefore exactly16 or31 according to whether the C2 orbit occurs.

The kernel line of E over each reduced point is well-defined, and is constant on each orbit. Each nonempty Z_q is precisely the reduced fiber of this orbitwise kernel assignment: it consists of the points whose kernel equals Cq. The C2 fiber, if present, consists of exactly its fifteen axes. The next section excludes coincidence of the C3 and C5 fibers.

## 6. Fifteen mirror lines separate the C3 and C5 channels

For an involution g∈A5, its action on A has eigenvalues (1,−1,−1). Denote by M_g⊂X the projective line of its negative eigenspace. The positive eigenline is its C2 axis. Different involutions give different M_g: with respect to the invariant nondegenerate quadratic form, M_g is the orthogonal complement of that positive axis, and distinct involutions have distinct axes. Thus there are fifteen distinct mirror lines.

Each M_g contains exactly two C5 axes and two C3 axes. Here is a coordinate-free incidence count. The stabilizer of each C5 axis is D10 and contains five involutions. Counting pairs (C5 axis, involution fixing it) gives 6·5=30. The fifteen involutions form one conjugacy class, so each fixes exactly two of these axes. Similarly the C3 stabilizer D6 contains three involutions; 10·3=30 gives exactly two fixed C3 axes per involution. A fixed C3 or C5 axis cannot be g's positive C2 eigenline, since the three axis orbits are disjoint. Hence all four fixed points lie on M_g. Equivalently, the relevant involution lies outside the cyclic rotation subgroup and acts by −1 on the axis line. These are four distinct points.

Suppose the C3 and C5 kernel channels coincide, represented by a nonzero q. Then t_q vanishes at all sixteen axes. Every entry of its local matrix lies in m_p at each such point, so every exterior minor lies in m_p². Let f be any scalar septic component of Λ²(t_q). On each M_g, its four specified double points give intersection multiplicity at least8. Since a line meets a septic not containing it with total multiplicity7, M_g must be a component of f unless f=0. All fifteen distinct lines must then divide f, impossible for degree7. Thus Λ²(t_q)=0 identically.

Again q is mixed, and PR667's universal generic-rank-two statement contradicts this. Therefore the C3 and C5 kernel lines are distinct. Combined with Section 3 and PR666's separation of the C2 channel, the final possible nonzero fixed-channel lengths are exactly the necessary list

                              6,10,15.

The six C5 axes and ten C3 axes realize their respective reduced zero schemes in distinct channels. If the C2 orbit occurs, its third distinct channel realizes the fifteen reduced C2 axes. All remaining projective channels have empty zero scheme. Thus the number of exceptional channels is exactly two or three, according to the same unresolved C2 alternative governing Δ's length16 or31.

## Contribution and limits

The new conclusions are universal fixed-channel reducedness and bound15, separation of the C3 and C5 channels, and scheme-theoretic reducedness of the family-detection locus with exact alternative lengths16 or31. Exterior septics and conic Bézout exclude fat axes; mirror-line Bézout separates the known channels; the absence of trivial tangent stabilizer constituents transfers reducedness to Δ.

This does not decide C2 occurrence. It does not identify the actual HM family with an axis kernel, normalize an actual coefficient, evaluate the next ambient division, determine the fourth Bockstein, establish prescribed-source membership or higher lifting, or repair the original theorem.

Sources:

- https://github.com/Akilleez-QA/read-em-and-weep/pull/1
- https://github.com/Akilleez-QA/read-em-and-weep/pull/661
- https://github.com/Akilleez-QA/read-em-and-weep/pull/663
- https://github.com/Akilleez-QA/read-em-and-weep/pull/664
- https://github.com/Akilleez-QA/read-em-and-weep/pull/666
- https://github.com/Akilleez-QA/read-em-and-weep/pull/667
