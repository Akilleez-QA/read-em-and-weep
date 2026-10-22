# Independent review: exterior septics, channel separation, and reduced detection

## Verdict

**PASS.** Under the pinned canonical endpoint interface, the proof establishes the following statements for every nonzero channel q:

- Its zero scheme Z_q is reduced, and its nonzero length is 6, 10, or 15.
- The C5 and C3 kernel channels are distinct. The C2 channel, if present, is distinct from both.
- The family-detection scheme Δ is reduced and has length exactly 16 or 31.
- There are exactly two exceptional projective channels, or exactly three if the C2 orbit occurs.

No mathematical gap was found. The nonzero-channel convention is explicit in the revised statement; it correctly excludes q=0, whose zero scheme is the whole plane. The intermediate list 6, 10, 15, 16 in Section 3 is correctly sharpened by Section 6 rather than asserted as the final list.

## 1. Dependency and scope audit

The review compared the argument with the supplied proofs for PR663, PR664, PR666, and PR667, and checked that the new argument uses the following precise inputs:

1. The canonical surjection D⊗O → A⊗O(1), its rank-two kernel K, and the two-dimensional space Q of equivariant channels.
2. PR663: each pure parity section is nowhere zero; the family-evaluation map has rank at least one everywhere and exact rank one at the C5 and C3 axes.
3. PR664: the finite support of Δ is either the sixteen C5/C3 axes or all thirty-one C5/C3/C2 axes. The stabilizers of those orbits are respectively D10, D6, and V4.
4. PR666: for nonzero q, the only surviving nonreduced Z_q is the union of the six local schemes defined by m_p² at the C5 axes, of total length 18. All other surviving cases are reduced, with lengths 6, 10, 15, or 16. The C2 channel, if present, already differs from both other channels.
5. PR667, Sections 2–4 only: every fixed channel with nonzero symmetric component has generic rank two on the square conic.

The fifth input is genuinely universal. In PR667 the symmetric map has an everywhere embedded image F≅W⊗O(−7), established by the Wronskian root-multiplicity bound. Generic rank one for a mixed channel would make the nonzero map O(−6) → P⊗O factor through F, whereas Hom(O(−6),F)=0. This proof does not use the actual-normal-variation hypothesis introduced for later conclusions in that document.

The review does not identify the actual HM family with an exceptional channel and does not use a selected endpoint, source-instance evaluation, parameter scan, or large computation. The pinned canonical interface remains an explicit hypothesis; no new verification of actual coefficients is claimed.

## 2. Six conics and the fourth-order septic exclusion

The general-position argument is correct. The C5 stabilizer fixes its own axis and acts as a five-cycle on the other five axes, so the action on the six-point orbit is two-transitive. Consequently the number k of orbit points on a pair-joining line is constant. Counting unordered pairs gives k=2, 3, or 6; the equality r(k−1)=5 rules out k=3, and irreducibility rules out k=6. Thus no three C5 axes are collinear.

For any five of the points, products of pair-joining lines give independent conic interpolation conditions. There is therefore a unique conic through those five. It is smooth and irreducible, since two lines can contain at most four of them. A conic through all six would be G-stable and hence invariant, because A5 has no nontrivial characters. Uniqueness of the invariant quadratic form would identify it with the square conic, which is disjoint from the six axes. Hence the six omitted-point conics are distinct and each misses the omitted point.

If a septic has multiplicity at least four at all six axes, then each of these smooth conics meets it with multiplicity at least 5·4=20. Since 20>2·7, Bézout forces each conic to be a component. Six distinct irreducible quadratic factors cannot divide a nonzero degree-seven polynomial. This proves the required vanishing of the fourth-power fat-point septic space scheme-theoretically, without an unjustified independence-of-conditions argument.

## 3. Exterior degree and exclusion of the fat zero scheme

The determinant calculation is correct: the kernel sequence gives det K≅O(−3), up to a constant line. For the fixed map K → P⊗O(2), the exterior square is consequently a vector of sections of O(7).

At a zero scheme locally defined by m_p², all entries of a local matrix lie in m_p². Every 2×2 minor therefore lies in m_p⁴. These local multiplicities belong to the global exterior septic sections and are unchanged by local trivializations. Section 2 then makes the exterior square identically zero.

A channel with this nonempty zero scheme cannot be either pure parity channel, by PR663. In particular its symmetric component is nonzero, so the universal generic-rank-two result on the square conic applies and contradicts the zero exterior square. This removes the sole nonreduced case left by PR666. It is important that the argument uses exterior septics, not only the quintic generators of the fixed-channel zero ideal.

## 4. Reducedness of Δ

The local transfer criterion supplies a necessary argument that does not follow from fixed-channel reducedness alone.

For a reduced isolated zero of an invariant section t, its component functions generate the maximal ideal, so dt_p:T_pX → F_p is injective. If the tangent representation has no invariant vector, its image cannot meet the invariant line ℓ spanned by a nonzero invariant section s(p). Thus projection gives an injective map T_pX → F_p/ℓ.

Locally s is a direct-summand basis vector. The rank-at-most-one ideal of (s,t) is exactly the ideal generated by the remaining components of t, namely the zero ideal of its quotient section in F/O·s. Its derivative is the projection of dt_p because t(p)=0. Injectivity implies that those components span m_p/m_p²; Nakayama gives the entire maximal ideal. The determinantal scheme is therefore reduced at p.

All equivariance hypotheses hold here: Q consists of equivariant maps and has trivial G-action, so both chosen sections are invariant. At C3 and C5 axes, the rotation subgroup already has two nontrivial tangent characters. At a C2 axis, A restricts to the three distinct nontrivial characters of V4; dividing the two quotient characters by the axis character leaves two nontrivial characters. Thus the criterion applies at every point in the known finite support. It proves reducedness of Δ and the exact length alternative 16 or 31, rather than merely a support statement.

## 5. Mirror-line separation of the known channels

The added Section 6 is also valid. Each involution has eigenvalues (1,−1,−1) on A. Its negative eigenspace defines a mirror line, and the invariant nondegenerate quadratic form identifies that plane as the orthogonal complement of its positive C2 axis. Distinct involutions have distinct positive axes and hence distinct mirror lines.

There are 6·5=30 incidences between C5 axes and involutions in their D10 stabilizers. Conjugacy of the fifteen involutions makes each incident with exactly two C5 axes. Likewise 10·3=30 incidences for the D6 stabilizers give exactly two C3 axes per involution. None is the positive C2 axis, so all four distinct points lie on the negative-eigenspace line.

If the C5 and C3 kernel channels coincided, every exterior septic for that channel would vanish to order at least two at all sixteen axes. On each mirror line its four specified points would contribute at least eight to the intersection multiplicity. Since 8>7, all fifteen distinct lines would divide every nonzero exterior septic, which is impossible. The exterior square would again vanish identically, contradicting the same universal generic-rank-two theorem. This separation argument requires only zero values of the fixed map, not prior reducedness of Z_q.

Together with PR666's separation of the C2 channel, this proves that the final possible nonzero fixed-channel lengths are 6, 10, and 15. The first two occur at the two compulsory, distinct kernel channels; the last occurs exactly when the C2 orbit is exceptional. Every other projective channel has empty zero scheme.

## 6. Limits preserved

The proof leaves C2 occurrence unresolved. It also leaves actual-channel identification, actual coefficient normalization, the next ambient division, the fourth Bockstein, prescribed-source membership, higher lifting, and the original repair unresolved. None of the new reducedness or channel-separation conclusions is used to claim those stronger results.

## Source references

- [PR663: secant-detection exceptions](https://github.com/Akilleez-QA/read-em-and-weep/pull/663), pinned in the proof at ad3ab59f6fbbbb3e5bde1da58b3b92a1f49c6889.
- [PR664: exceptional channel loci](https://github.com/Akilleez-QA/read-em-and-weep/pull/664), pinned at 90d9aa88b3cea99e8dd1acea0acda9095021185e.
- [PR666: maximal fixed-channel exclusion](https://github.com/Akilleez-QA/read-em-and-weep/pull/666), pinned at 0fc85f297a62c7be473a8da9ad992bb84706f8f2.
- [PR667: square-conic rank stratification](https://github.com/Akilleez-QA/read-em-and-weep/pull/667), pinned at 7d53ea234b99b75e89a29c4caba7ec564e134410; only Sections 2–4 are needed here.
