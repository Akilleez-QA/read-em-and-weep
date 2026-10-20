> Historical mathematical review of the source manuscript. This is not a new independent review or a formal verification certificate. Original source-byte hashes refer to the archived manuscript; public-byte hashes are in SOURCE-BINDINGS.json.

# Independent audit of the fixed-quotient tangent countermodel

## Verdict

The construction in `PROOF.md` is valid as a counterexample to a universal bound of one on the dimension of the **determinantal first-variation kernel** at a good rank-five point. Its incidence avoidance, exact intersection with the middle image, and target dimensions all check out. No mathematical correction to those arguments is necessary.

The conclusion concerns the tangent space of the determinantal scheme. It does not establish a two-dimensional tangent space to its reduced support, a reduced middle surface, or preservation of the ternary-support and nondegenerate-metric conditions in those directions. The proof explicitly respects these limitations. It also does not inherit the generic-rank or isolated-support conclusions of the earlier countermodel: that earlier construction used a different family of quotient kernels and an additional avoidance argument.

 

## 1. Universal space, repeated inputs, and the initial graph

The exterior multiplication map V tensor wedge-square V -> wedge-cube V is surjective, so dim W = 5*10-10 = 40. For nonzero a, the decomposition Sym-square V = C a-square + aU + Sym-square U shows ker B_a = C a-square and dim F_a = 4+10 = 14.

The projective rank-one locus in W consists exactly of a tensor a tensor (a wedge b): a wedge beta = 0 forces beta = a wedge b. It is the image of the projective flag variety of a line in a two-plane. The line and two-plane are recoverable, and its dimension is 4+3 = 7. In particular X is projective and closed, including every possible repeated-input direction.

The dependency's construction of v is sound. Square compatibility imposes two conditions over a projective curve, leaving a proper closed bad set in the 15-dimensional parameter space. Rank-two compatibility is a rank-14 vector-bundle incidence over a smooth irreducible threefold. Its stated differential witness proves dominance, rather than merely presuming dominance from dimensions. A nonempty open of the parameter space has nonempty fibers of dimension two. The two parameter opens therefore intersect.

For the graph L, the tensor block has rows -v(q) and 2M(q). Its second-factor support is exactly u wedge (im q + C v(q)). It has dimension at least two for every nonzero q in K, including rank-one q by square avoidance. Consequently L has dimension five and its projectivization avoids X. The factor two in the dependency is consistent with B_u(uv)=A_u(v), so no correction factor is missing from the graph equation.

## 2. Ten independent universal first variations

Use the fixed representatives e,z in E=E0+Cz. Projection of V tensor wedge-square V onto E tensor wedge-square E kills F_u and every correction f0(u,xi,v(q)). Hence a relation modulo F_u among the ten variations implies

    B_e(q_e) + B_z(q_z) = 0.

Here B_e(q_e) is in E0 tensor wedge-square E0, whereas B_z(q_z) is in E0 tensor (z wedge E0). These are genuinely disjoint ambient tensor summands; it is not necessary that either summand separately describe a full graded piece of W(E).

B_z is injective on Sym-square E0. The kernel of B_e on Sym-square E0 is C e-square, and h(e,e) nonzero ensures this line has zero intersection with K. Thus both q_e and q_z vanish. This proves the asserted injection D tensor K -> W/F_u and dim S = 10.

## 3. The lifting incidence, including zero projections

Let R=F_u/L, of dimension nine. The preimage of S in W has dimension 14+10 = 24, and its quotient by L has dimension 19. Splittings of its surjection onto S form an affine torsor under Hom(S,R), of dimension 90. Taking the inverse image in W of a splitting image gives a 15-dimensional N with

    N intersection F_u = L, and pi(N)=S.

These equalities hold for every splitting, before any generic choice.

There are precisely three relevant strata of X:

1. Points with zero projection to W/F_u lie in P(F_u). None can lie in P(N), because its intersection with P(F_u) is P(L), which avoids X.
2. Points whose nonzero projection is outside P(S) cannot belong to P(N).
3. For a point with nonzero projected representative s in S, membership is equivalent to sigma(s)=w modulo L. Relative to a fixed splitting this is a prescribed value of a map in Hom(S,R) at s. Evaluation is surjective onto the nine-dimensional R. The fiber is therefore an affine space of dimension 81, with exactly nine independent equations.

This condition is invariant under rescaling w and s. On projective affine charts it is algebraic, so the incidence over the eligible locally closed subset of X is a legitimate finite-type incidence, with fibers of dimension 81. Its dimension is at most 7+81=88. The closure of its image in the 90-dimensional affine splitting space still has dimension at most 88. Its complement is nonempty open and consists of splittings avoiding all of X. No properness of the eligible stratum is required or silently used.

## 4. Extension to the final quotient

After fixing such N, dim W/N=25. The image H of F_u has dimension nine, since N intersection F_u=L. A general five-dimensional subspace M' of W/N is disjoint from H; the relevant open is nonempty since 5+9 <= 25.

Projection from N is a morphism on all of X because P(N) avoids X. Its image Y in P(W/N) is projective, closed, and of dimension at most seven. Five-dimensional subspaces containing a fixed line form Gr(4,24), of dimension 80. The bad incidence in Y times Gr(5,25) therefore has dimension at most 87, compared with dim Gr(5,25)=100, and its projection is closed. Thus the repeated-input-avoidance open is also nonempty.

Irreducibility of Gr(5,25) permits the simultaneous choices. For the inverse image M of M',

    dim M=20, M intersection F_u=L, P(M) intersection X is empty.

This proves exact intersection, not just containment of L. It also proves simultaneous global repeated-input injectivity for the single quotient f=p composed with f0.

## 5. Residual ranks, fiber, and dimensions in J

The dimensions are:

- J=W/M: 20.
- A_a(V/Ca): 4 for every nonzero a.
- J/A_a(V/Ca): 16.
- Sym-square(V/Cu): 10.
- p(F_u)=I_u: 14-5=9.
- Q_u: rank 9-4=5, kernel dimension five.
- J/I_u: 11.
- Full middle map Phi_u: source dimension 15, rank nine, kernel dimension six.

The graph projects to K under F_u/A0_u(V) identified with Sym-square(V/Cu). Hence ker Q_u is exactly K, and B_u(q)=A_u(v(q)) on K. This establishes the dependency hypotheses actually needed for the fiber reconstruction, independently of any ranks at other middle points.

Rank-two q in K admits precisely two ordered projective factor pairs. The equation for their lifts is A_u(v(q)+beta a+alpha b)=0. Injection of A_u yields exactly the compatibility v(q) in im q, with unique lift directions for each ordered factor pair. Thus the independent-zero fiber is the finite degree-two cover of the compatible rank-two surface and has dimension exactly two. No new quotient-kernel directions contribute to this fiber because M intersection F_u remains exactly L.

## 6. Determinantal tangent calculation and its exact meaning

The full kernel is

    C u-square + {q-u v(q): q in K}.

For a rank-nine linear map, the tangent condition for its rank-at-most-nine determinantal scheme is that its variation map the kernel into the image. On u-square the variation is -2A_u(xi), already in I_u. On the graph vector it is p(d(xi,q)). Since pi(d(xi,q)) is in S=pi(N), d(xi,q) lies in N+F_u, so its image in J lies in I_u. Every xi in D therefore meets the tangent condition.

For clarity, equivalence with the residual determinantal scheme is stronger than mere equality of rank sets and can be checked locally: choose a local representative a of the middle line and a fixed complementary four-space. The columns from a times that complement map isomorphically onto the rank-four repeated-input image. Locally split off this image in J and eliminate those columns. The remaining block is Q_a, while the a-square column is zero. Consequently the rank-at-most-nine minors of Phi and the rank-at-most-five minors of Q define the same local scheme. Thus the full-map tangent computation really computes the claimed residual determinantal tangent condition.

The cyclic-sign statement also holds: cyclic zero gives

    -f(u,xi,v)=f(u,v,xi)+f(xi,u,v),

and the last summand lies in I_u. There is no sign discrepancy in the obstruction modulo I_u.

## 7. Scope guardrails

No argument here proves that D lies in the tangent space of the reduced rank-at-most-five support. For a nonreduced determinantal scheme, its tangent space may be strictly larger. Likewise the displayed first-order equations do not impose the deformation equations retaining ternary support, nondegeneracy, or the two-dimensional compatible fiber. The precise verified conclusion is a two-dimensional subspace in the determinantal first-variation kernel at the specified good point.

The earlier proof's avoidance of all F_a for a different from u does not transfer to this more constrained quotient family. Neither generic residual rank ten nor an upper bound on global rank-drop-support dimension is established here. The current proof correctly makes neither claim. Any application requiring either must supply a new argument.

Subject to these explicitly stated boundaries, the proof is complete.
