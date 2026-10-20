# A canonical complement and unavoidable boundary for rank-five ternary surface families

## Result and scope

Work over C. Let dim V=5, let f be outer symmetric and cyclic-zero, and assume every repeated-input map A_u:V/Cu -> J, [z] -> f(u,u,z), is injective. This is the convention used throughout; f(u,z,u)=-2f(u,u,z). No equivariance assumption is made.

Call a middle line [u] **good** if:

- rank Q_u=5;
- K_u=ker Q_u is supported on a three-dimensional subspace E0_u of E_u=V/Cu;
- K_u is the kernel of a nondegenerate bilinear form h_u on E0_u, regarded as a functional on Sym² E0_u;
- its projective independent-zero fiber has dimension at least two.

The following restrictions are new:

1. At a good point the graph correction necessarily takes values in E0_u. There is a canonical, algebraically varying three-plane C_u in V, with

       H_u = Cu direct-sum C_u,
       H_u = inverse image of E0_u in V.

   It is obtained by eliminating the contraction component of the correction. It is independent of all splittings, middle-vector scales, and scales of h_u.

2. There is no complete algebraic surface consisting entirely of good middle points. More precisely, any projective variety mapping finitely onto a surface in P(V) cannot carry such an everywhere-transverse canonical complement.

3. If B is an integral projective middle surface whose general point is good, then B necessarily contains a point where either rank Q_u<=4, or rank Q_u=5 and the defining ternary form h_u is degenerate. Full four-dimensional residual support cannot provide an alternative boundary at rank five.

4. Let Gamma be a smooth projective resolution of the closure of the canonical-complement graph over B. Let h be the pullback of the hyperplane class on B and let R be the rank-two quotient V/C on Gamma. The canonical section of R tensor O(h), induced by the middle line, has a nonempty zero locus, supported over the exceptional boundary in (3), and

       integral_Gamma c2(R tensor O(h))
         = integral_Gamma [h² + h c1(R) + c2(R)]
         >= degree(B) > 0.

   If this zero locus is zero-dimensional, its scheme length is this integer, hence at least degree(B). No zero-dimensionality is asserted in general.

5. On any nonconstant complete good curve, the degree of the support-hyperplane map [u] -> H_u exceeds the degree of the middle-line map by a positive multiple of three. In particular the difference is at least three, and such a curve cannot have constant H_u.

These results do not exclude a surface with the required lower-rank or degenerate-form boundary. They give a bounded, intrinsic obstruction to a seven-dimensional affine independent-zero component generically of this type: its middle surface must have that boundary, and its complement graph carries the positive defect class above. They do not repackage the isolated K3 model or claim existence of a positive-dimensional family.

## 1. A surface forces the correction into the ternary support

Fix u and a splitting s:E_u -> V. For q in K_u define v(q) by

       f(s(a),u,s(b)) = A_u(v(ab)),       q=ab,

extended linearly. A rank-two q is compatible exactly when v(q) lies in im q. The repeated-input hypothesis implies that no square e² in K_u is compatible: the independent vectors A_e(u), A_u(e) cannot be proportional. This is the elementary pencil consequence proved in the existing structural proofs.

Suppose that v modulo E0_u is nonzero. Since E_u/E0_u is one-dimensional, its kernel K' inside K_u has dimension four. Every compatible q lies in K'. The restricted correction v|K' still has no compatible square.

The purely linear supported-ternary theorem in /research/hm/normalizer-rank-five/rank-six-cubic-web/REDUCIBLE.md applies to every four-dimensional K' inside Sym² E0_u and every linear correction having no compatible square. It does not require K' to be the entire residual kernel of an operation. It states that its compatible rank-two locus has dimension at most one. This contradicts a surface fiber, since ordered-factor reconstruction is finite. Hence

       v(K_u) subset E0_u.                                      (1)

Changing s to s+d u changes the correction by

       v'(q)=v(q)+2q(d).                                        (2)

Here q(d) denotes symmetric contraction, so (ab)(d)=(d(a)b+d(b)a)/2. Thus (1) is splitting independent.

## 2. The intrinsic contraction projection

Write E0=E0_u, choose a representative nondegenerate form h, and put

       K=ker(h:Sym² E0 -> C).

Use h to identify K with the traceless h-self-adjoint endomorphisms of E0: q corresponds to q composed with h:E0 -> E0*. The trace pairing on this five-dimensional space is nondegenerate. It therefore admits a trace-orthonormal basis T_1,...,T_5 over C; let q_i be the corresponding tensors.

For v:K -> E0 define a covector

       tau_h(v)=h(sum_i T_i(v(q_i)), -).                       (3)

This expression is independent of the trace-orthonormal basis, because it contracts against the inverse trace pairing. The sum of endomorphisms sum_i T_i² commutes with every h-isometry, hence is scalar: commuting with all orthogonal sign changes and permutations in an orthonormal basis already proves this assertion. Its trace is five, so

       sum_i T_i² = (5/3) Id_E0.

For sigma(d):q -> 2q(d), it follows that

       tau_h(sigma(d))=(10/3)d.                              (4)

Indeed q_i(d)=T_i(h^{-1}d), and (4) follows by substitution into (3).

The construction also does not depend on scaling h. If h is replaced by c h, one may replace q_i by q_i/c; their associated endomorphisms T_i are unchanged. In (3), the factor c in h cancels the factor 1/c in v(q_i). Thus tau_(c h)=tau_h.

This is an abstract contraction identity. It evaluates neither the source operation nor any source rank instance.

## 3. Canonical normalized complement

Restrict the splitting s to E0 and define

       s_can(a)=s(a) - (3/10)tau_h(v)(a) u,
       C_u=im(s_can).                                        (5)

Under a shear s'=s+d u, equations (2) and (4) show that the added d u cancels exactly in (5). Thus C_u is independent of s. If u is replaced by t u, then A_u scales by t², the middle-linear numerator scales by t, and v scales by t^{-1}; the correction term in (5) is unchanged. Scaling h changes nothing by Section 2.

Projection V -> E_u identifies C_u with E0. Therefore

       H_u = Cu direct-sum C_u.                              (6)

Equivalently, C_u is the unique complement inside H_u for which the correction has tau_h(v)=0. Uniqueness follows directly from (4).

All operations are regular on the nondegenerate, constant-rank stratum: kernels and support spaces are subbundles there, the inverse trace pairing is regular, and the formulas are invariant under changes of local frames. Consequently [u] -> C_u is an algebraic morphism on the good stratum. No global choice of u, h, or s is required.

## 4. Why an everywhere-transverse complete surface is impossible

Here is a general geometric lemma independent of f.

Let T be a smooth projective surface with a morphism a:T -> P(V) generically finite onto a surface, and a morphism c:T -> Gr(3,V). Let U=a*O(-1), let C be the rank-three tautological bundle from c, and put R=(V tensor O_T)/C. If U and C are disjoint at every point, then U -> R is nowhere zero. It gives a nowhere-zero section of

       R tensor U*.

The latter rank-two bundle must have zero top Chern class. Write h=c1(U*). But

       c2(R tensor U*)=c2(R)+h c1(R)+h².                      (7)

The quotient R of a trivial bundle is globally generated. Its determinant is nef, and its second Chern number is nonnegative: a general section has a zero-dimensional or empty zero scheme, whose length represents c2(R). The class h is nef, and h² is the positive degree of the generically finite map times the degree of its image. Every term on the right of (7) has nonnegative degree, and the last is strictly positive. This is a contradiction.

The same conclusion applies to an integral singular projective surface by pulling the tautological bundles to a projective resolution. The middle hyperplane class becomes nef and big, which is sufficient for the same numerical argument.

Applying the lemma to (6) excludes a complete surface of good middle points. This is stronger than the elementary fixed-hyperplane observation and does not require H_u to be constant.

## 5. Exact location of the necessary boundary

Let B subset P(V) be integral projective of dimension two, with good general point. The locus rank Q_u<=5 is closed, so it contains all of B.

At every rank-five point, K_u varies regularly with dimension five. The condition that its support have dimension at most three is closed in the Grassmannian of five-planes in Sym² E_u. One way to see this is to take the proper image of the incidence of a three-plane E0 and a five-plane contained in Sym² E0. Consequently, throughout the rank-five part of B, support dimension is at most three. It cannot be at most two since dim Sym²(C²)=3<5. It is therefore exactly three, and its hyperplane in Sym² E0 defines a unique projective ternary form h_u. Nondegeneracy is an open condition.

It remains to check that surface fibers do not disappear at these boundary points. The full zero scheme in P(V)^3 is projective over its middle factor; fiber dimension is upper semicontinuous. Every dependent nonzero zero triple has all three lines equal. Indeed if outer vectors x,z are independent and u=a x+b z, then zero means a A_x(z)+b A_z(x)=0, impossible by their independence. If x,z are proportional, cyclic-zero reduces the equation to A_x(u)=0, forcing u proportional to x. Thus the dependent locus in every middle fiber is just one point.

A general good fiber has dimension at least two, so every full fiber over B has dimension at least two, and removing its one dependent point leaves dimension at least two. Hence every rank-five point with nondegenerate h_u on B is good, with canonical complement (5).

If B had no lower-rank or degenerate-form boundary, Section 4 would be contradicted. This proves the precise alternative in the statement.

## 6. The quantitative boundary class

Take the closure of the graph of the canonical-complement map over the good open B^o:

       G subset B x Gr(3,V).

Its projection to B is proper and birational. Resolve G to a smooth projective surface Gamma. On Gamma both the middle line U and the limiting complement C are tautological subbundles of the trivial V-bundle. The section

       s:O -> R tensor U*,       R=V/C,

vanishes exactly where the limiting three-plane C contains the middle line U. It is nonzero over B^o by (6). In fact it is nonzero over every good point of B: there the canonical complement map extends regularly, so its graph has a single limiting value. Therefore its entire zero locus lies over the boundary identified in Section 5.

If the zero locus were empty, its top Chern class would vanish, contradicting (7). Moreover h²=degree(B), since Gamma -> B is birational. Formula (7) gives exactly

       integral_Gamma c2(R tensor U*) >= degree(B)>0.        (8)

When the zero locus is zero-dimensional, the section is regular on the smooth surface, and its length equals (8). If it contains curves, (8) remains a positive top-Chern number, but is not asserted to be the naive length or degree of the reduced zero locus. This distinction prevents an unjustified multiplicity claim at the boundary.

## 7. A degree restriction for complete good curves

Let T be a complete integral curve of good points and pass to its normalization. Write h=deg U*, n=deg(V/H), and a=deg det(C*). Since C* is globally generated, a>=0. From H=U direct-sum C and det H=(V/H)^{-1} one obtains

       n=h+a>=h.                                          (9)

If the middle map is nonconstant, h>0, so the hyperplane map H cannot be constant. More generally (9) holds for any complete parameter curve in the good stratum, with the degrees pulled back along its maps. It gives no contradiction for varying H, and does not claim that all complete good curves are impossible.

## 8. Consequence for the remaining independent-zero frontier

Under the established middle rank-drop support bound at most two, a seven-dimensional affine independent-zero component generically of the good tracefree-ternary rank-five type has a projective middle image of dimension two, provided its generic projective fiber has dimension two. Its middle closure B is subject to Sections 5 and 6. In particular its canonical complement cannot extend everywhere transversely; it must meet rank<=4 or degenerate h, with nonzero boundary defect (8).

For completeness, at a good point the compatible rank-two locus has dimension at most two. The rank-two locus of the nondegenerate tracefree ternary hyperplane is the dense open of an irreducible cubic threefold, as proved in /research/hm/universal-polar/rank-five-surface-countermodel/PROOF.md, Section 1.1. If compatibility filled that threefold, restricting to a general four-dimensional subspace of K would give a compatible surface with no compatible square, contradicting the supported-ternary theorem used in Section 1. Thus compatibility is a proper closed subset of the rank-two open and has dimension at most two. The good-point assumption therefore means dimension exactly two. With a middle image of dimension at most two, this also bounds such affine components by seven and proves that dimension seven forces a middle surface.

The argument neither rules out the required boundary nor establishes a universal affine bound six. Its new content is the canonical splitting and the forced, quantitatively nontrivial boundary geometry.  

## 9. Sharpening the complete-curve bound

For a nonconstant complete good curve, the integer a in Section 7 is in fact a positive multiple of three. Hence

       degree(H-map) >= degree(middle-map)+3.                (10)

First, the conformal form defines a nowhere-degenerate pairing C tensor C -> M for a line bundle M on the normalized curve. Thus C is isomorphic to C* tensor M. Taking determinant degrees gives

       -2a=3 degree(M),

so 3 divides a.

If a=0, the Plücker line of the map to Gr(3,V) has degree zero, so that map is constant. Thus C is one fixed three-plane. The class [h] is now a morphism from the complete curve to the complement of the determinant hypersurface in P(Sym² C*). This complement is affine (the standard affine principal open of a positive-degree homogeneous polynomial). Every morphism from a complete integral curve to an affine variety is constant. Therefore [h] and K=ker h are constant as well.

Use the fixed complement C to define the correction. Under a change of local middle frame u' = t u, one has v' = t^{-1}v. Consequently the local tensors v tensor u glue to a section of

       Hom(K,C) tensor U,

where U is the middle tautological line. Because the middle map is nonconstant, degree U<0, so this bundle has no nonzero global section. Hence v=0. A nondegenerate ternary form over C has a nonzero isotropic vector e, giving e² in K and v(e²)=0 in Ce, contrary to square avoidance. Thus a cannot be zero. Together with a>=0 and 3|a, this proves a>=3 and (10).

The inverse scaling in this argument is essential: v tensor u is a section with the negative tautological line U, not U*. There is still no contradiction for curves with a>=3, and no assertion that such curves exist.
