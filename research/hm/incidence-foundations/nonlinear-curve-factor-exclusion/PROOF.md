# Exclusion of nonlinear curve factor images

Work over C. Let dim E=4 and let K⊂Sym²E have dimension five and full support (the sum of its tensor images is E). Let S⊂P(K) be an integral surface generically of rank two. Suppose one irreducible ordered-factor component above S has first-factor image an integral curve C⊂P(E). For the applications in Sections 5 and 7 only, additionally let v:K→E be linear and compatible densely on S, meaning v(lm)∈span(l,m), and assume square avoidance: if 0≠e²∈K, then v(e²)∉Ce.

**Theorem. C is a line. In fact, this structural conclusion does not require v or square avoidance.** Thus the completed line-projected rank-five classification applies to every such surface that has any curve factor projection. This does not assert that a factor projection must be a curve: the case where both factor projections are surfaces remains separate.

## 1. Generic ruling dimension is exactly two

Set M_l={m∈E:lm∈K}. A factor component of dimension two dominating C supplies dim M_l≥2 generically. Suppose C is nonlinear and dim M_l≥3 generically. Choose three independent general representatives l1,l2,l3 and put U=span(l1,l2,l3). The direct sum of the spaces li⊗M_li has dimension at least nine inside U⊗E. The kernel of symmetric multiplication U⊗E→Sym²E is Λ²U and has dimension three. Its image therefore has dimension at least six, contradicting dim K=5.

Consequently dim M_l=2 generically. The complete incidence P(M_l) over a dense open in C is irreducible of dimension two, so the given ordered-factor component is dense in it. When a compatible v is part of the data, compatibility holds densely on this whole family. The product map from ordered factors to nonzero quadrics is finite: a quadratic has at most two ordered factor pairs. This also shows that the closure of any such one-parameter family of complete projective lines of second factors has dimension two in P(K).

## 2. A curve spanning E is impossible, without compatibility

Assume C spans P(E). Choose [l0]∈C general with dim M_l0=2, and let π:E→Ebar=E/Cl0. The image Kbar of K in Sym²Ebar has dimension three because the kernel of Sym²π is l0E and K∩l0E=l0M_l0 has dimension two.

For general l∈C, π is injective on M_l. Otherwise l0∈M_l on a dense subset, so l0 l∈K there. Since C spans E, linearity and closure yield l0E⊂K, contradicting dim M_l0=2.

The projected first-factor curve Cbar⊂P(Ebar) is nonlinear: containment in a projective line would put C in a projective plane through [l0]. For general l, π(M_l) has dimension two. Its products π(l)π(M_l) give a projective line of quadrics, with rank two on a dense open. The resulting ordered incidence has dimension two, even if C→Cbar has degree greater than one: it dominates a curve with line fibers. Finiteness of factorization implies that its product image is a surface. Since P(Kbar)=P², this image is dense in P(Kbar); hence every tensor in Kbar has rank at most two.

Use the bounded-rank plane classification established in /research/hm/normalizer-rank-five/extremal-kernel-planes/PROOF.md, Section 2: a three-dimensional symmetric tensor space of upper rank two is either Sym²W for a two-plane W, or eU for a three-plane U. Here all tensors lie in Sym²Ebar and dim Ebar=3, so the alternatives are Sym²W⊂Sym²Ebar or eEbar.

In the binary alternative both factors of a nonzero product lie in W, forcing Cbar⊂P(W), a line. In the common-factor alternative, for π(l) not proportional to e, the condition π(l)π(M_l)⊂eEbar forces π(M_l)⊂Ce, contradicting its dimension two. Both are impossible. This entire section uses no condition on v.

## 3. A nonlinear planar curve cannot have transverse second factors

It remains that C spans P(U), dim U=3. Put K0=K∩Sym²U. Suppose M_l is not contained in U generically. Its intersection with U is then a line. Write E=U⊕Cw. In Sym²E/Sym²U the image of lM_l is a nonzero multiple of lw. As l ranges over C, these images span the three-dimensional space Uw modulo Sym²U. Thus dim K0≤2.

Choose a nonzero n_l∈M_l∩U. The products l n_l define a curve in P(K0): they cannot be constant because a nonzero quadratic has only finitely many factor lines. Therefore dim K0=2 and these products are dense in its projective pencil. Every member of K0 has rank at most two.

A pencil of ternary quadrics all of rank at most two has only lines and points as irreducible factor images. Here is a direct verification. If the pencil has a rank-two member, write it xy in a basis x,y,z of U, with symmetric matrix having xy entries 1. Write the other member as a symmetric matrix B. The coefficient of t in det(matrix(xy)+tB) forces B_zz=0. Its t² coefficient then forces B_xz B_yz=0. If both entries vanish, both quadrics are binary in x,y. If, for example, B_xz≠0 and B_yz=0, the t³ coefficient det B=0 forces B_yy=0, so the second quadric is divisible by x, as is xy. The other case is symmetric. Thus the pencil is binary or has a common factor. A pencil containing no rank-two member cannot have dimension two: the sum of two independent squares has rank two. In the binary case every factor lies in a fixed projective line; in the common-factor case one factor is fixed and the other ranges in a fixed projective line.

This contradicts the nonlinear factor curve C. Hence M_l⊂U generically.

## 4. Planar rulings are structurally impossible under full support

Now all generic products lie in Sym²U. Let K'⊂K∩Sym²U be the vector span of S. Since S is a surface, dim K'≥3, and K' contains each complete generic ruling lM_l.

If dim K'=5, then K'=K and K is supported on U, contrary to full support.

If dim K'=3, S is dense in P(K'), so every tensor of K' has rank at most two. The bounded-rank plane classification gives K'=Sym²W or K'=eU. In the binary case C lies in P(W), a line. In the common-factor case, for general l not proportional to e, lM_l⊂eU forces M_l⊂Ce, contradicting dim M_l=2.

Suppose dim K'=4. Its annihilator in Sym²U* is a pencil spanned by independent symmetric forms A,B. Since lM_l⊂K' with dim M_l=2, the two linear forms A(l,-) and B(l,-) are dependent for general l∈C. Thus some nonzero member of the pencil has l in its radical.

The pencil parameter is not constant along C: if one fixed nonzero form annihilated all general l, it would annihilate U because C spans U, a contradiction. More explicitly, outside the common radical ker A∩ker B (a proper linear space), dependence determines a unique pencil parameter. It is therefore a nonconstant rational map C→P¹. Consequently det(aA+bB) vanishes identically on the pencil.

Apply the elementary singular-pencil classification proved in Section 3, now to forms on U. A binary pencil has, for its generic rank-two members, a fixed radical line, hence one projective radical point. A common-factor pencil e·span(f,g) has generic radical directions in the fixed projective line ker e⊂P(U). In either case there are only finitely many exceptional rank-one members, since a two-dimensional pencil cannot consist entirely of rank-one forms. Each exceptional member contributes at most a projective radical line. No pencil member is zero because A,B are independent.

Thus the union of all projective radicals of pencil members is contained in a finite union of projective lines and points. The irreducible nonlinear curve C cannot be contained in that union. This excludes dim K'=4.

All dimensions are exhausted. The exclusion of nonlinear curve factor images is therefore independent of compatibility and square avoidance. Compatibility and square avoidance enter only the finite-middle consequences.

## 5. Consequence and exact scope

Together with /research/hm/incidence-foundations/quartic-middle-finiteness/PROOF.md, Section 7, the theorem implies: under the standing global trilinear hypotheses there are only finitely many middle points admitting a densely compatible rank-two surface whose full residual kernel has dimension five and full support and for which at least one ordered factor projection is a curve. Such independent-zero surface components have fixed middle and affine dimension five.

No argument here forces a factor projection to be a curve. Rank-five surfaces with both ordered factor projections of dimension two remain outside this theorem. Moving-middle components with only curve fibers also remain outside the surface theorem.

## 7. Point projections and the precise remaining surface case

For completeness suppose a compatible ordered-factor surface has first image the point [h]. Write M=M_h. If dim M=3, its image is dense in the plane P(hM). If dim M=4, put π:E→E/Ch and T:E→E/Ch, T(m)=v(hm) mod Ch. Away from the square, compatibility is the existence of a unique scalar λ with T(m)=λπ(m). The pencil T−λπ has generic rank three: at least one 3×3 minor has nonzero leading coefficient since π has rank three. Away from finitely many λ its projective kernel is a point, so that portion of the compatible incidence has dimension one. Every surface component must therefore occur at a fixed λ and lie in P(ker(T−λπ)), of dimension at least two. Rank zero is impossible: T=λπ would give T(h)=0 and make h² compatible. Thus the kernel has dimension exactly three when it supplies a surface; the surface is the full plane P(hU), dim U=3.

In either case square avoidance forces h∉U. If h∈U, compatibility on hU and specialization along h(h+tf) and h(h+tg) for independent complementary f,g imply v(h²)∈Ch, a contradiction.

With E=Ch⊕U, the linear map m↦v(hm) on U has the form α(m)h+βm, where α∈U* and β∈C: its U-projection preserves every line, hence is scalar. For an actual residual kernel at middle u, lift h to h−βu and each m∈U to m−α(m)u. The trilinear expansion kills every product between the lifted one-plane and three-plane. This places the middle in the finite C_(1,3) incidence of /research/hm/middle-surface/extremal-surface-geometry/GENERALIZATION.md.

Combining point projections, this theorem, and the completed line-projected analysis: any remaining positive-dimensional family of middle points with full-support dimension-five residual kernels and compatible surface fibers must have BOTH ordered factor projections of dimension two. This is a restriction on that surface-fiber problem, not a resolution of all rank-five kernels or moving families with only curve fibers.
