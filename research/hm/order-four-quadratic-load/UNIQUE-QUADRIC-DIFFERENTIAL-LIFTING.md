# Differential lifting excludes the remaining a=1, b=4 branch

## New lifting lemma, allowing reducible curves

Let C⊂P4 over C be a reduced curve, and let T be a dense open subset of the dual P4. Assume that H∩C=Z_H is a reduced finite set for H∈T. Suppose:

1. For each H∈T there is a unique quadric Q_H⊂H containing Z_H, up to its scalar equation, and Q_H is geometrically integral.
2. Every cubic on H vanishing on Z_H is a linear multiple of the equation of Q_H.

Then C is contained in an ambient quadric hypersurface in P4.

The lemma does not assume that C is integral, connected, or in uniform position. It uses variation of the actual unique quadric, not a selected coefficient evaluation or numerical rank calculation.

## 1. Write the unique family in an affine hyperplane chart

Choose homogeneous ambient coordinates [X0:X1:X2:X3:X4], and parametrize an affine chart of hyperplanes by

    H_t: X4=t0 X0+t1 X1+t2 X2+t3 X3,
    t=(t0,t1,t2,t3).

Write x=[X0:X1:X2:X3] as homogeneous coordinates on H_t. Since the quadric equation is unique, the kernels of the restriction maps to Z_H form a line bundle after shrinking T. Choose a rational nonzero generator and shrink once more to write the equation as q(t,x), homogeneous quadratic in x, with coefficients regular in t. This yields an algebraic family whose fibers are the integral quadrics Q_t.

For the HM application, this algebraicity can be seen directly without any cohomology/base-change assertion: the 25 line-intersection points are rational functions of t on a suitable open; the linear equations imposing vanishing of a symbolic quadratic have a one-dimensional kernel of constant dimension; a nonzero kernel coordinate can be normalized to one. This describes rational dependence, not an evaluation of coefficients.

## 2. Differentiate at the marked points

Fix t and p∈Z_t. We claim that

    (∂q/∂t0,...,∂q/∂t3)(t,p)

is proportional to the vector (x0(p),...,x3(p)).

Indeed consider a tangent direction v=(v0,...,v3) satisfying Σv_i x_i(p)=0. Varying H_t in this direction keeps the ambient point p fixed to first order: the moving hyperplane equation still vanishes at p to first order. Because the intersection of H_t with the smooth curve C is transverse at p, the local marked intersection point of C with the moving hyperplane has derivative zero in this direction. Differentiating q(t,p(t))=0 consequently gives Σv_i(∂q/∂t_i)(t,p)=0. The annihilator of the three-dimensional subspace {v:Σv_i x_i(p)=0} is exactly the span of x(p), proving the claim. This argument applies separately to every branch/component of C. For C a disjoint union of lines it follows directly from the explicit line/hyperplane intersection map.

It follows that, for every pair i,j, the homogeneous cubic

    F_ij(t,x)=x_i ∂q/∂t_j − x_j ∂q/∂t_i

vanishes on every point of Z_t. Hypothesis 2 gives F_ij(t,x)∈q(t,x)·H0(O_P3(1)). In particular, for every x∈Q_t,

    x_i ∂q/∂t_j = x_j ∂q/∂t_i.

Thus the same proportionality now holds at every point of the quadric, not merely at the marked points. No assertion that the derivatives themselves vanish is made; their common proportionality is precisely what is needed.

## 3. The swept-out locus has dimension three

Let

    D={(t,x)∈T×P3:q(t,x)=0}.

Its general fiber is an integral surface, so after restricting the base it has a unique dominating irreducible component, of dimension six; work on that component. Define its ambient evaluation map

    π:D→P4,    (t,x)↦[x0:x1:x2:x3:Σt_i x_i].

The whole space T×P3 identifies with the incidence variety over this hyperplane chart. At a general smooth point of D, tangent vectors fixing the ambient point π(t,x) are exactly the vectors with δx=0 (projectively) and Σδt_i x_i=0. This is a three-dimensional space. Section 2 shows that all these vectors lie in T_(t,x)D, because the derivative of q is Σ(∂q/∂t_i)δt_i, which vanishes whenever Σx_iδt_i=0.

Therefore the differential of π|D has rank at most 6−3=3 at its general point. In characteristic zero, generic differential rank equals the dimension of the image. Hence the reduced image closure S=closure π(D) has dimension at most three.

Its dimension is at least three. If it were two, every integral two-dimensional quadric Q_t would equal the integral surface S as a closed set. Then S would be contained in every H_t for t in a dense open of dual P4, impossible. Smaller dimension cannot contain a quadric surface. Thus dim S=3.

The closure S is integral because D is irreducible. It is consequently an integral hypersurface of P4.

## 4. Its degree is two, and it contains C

A general hyperplane section S∩H is integral by Bertini irreducibility and generic reducedness. Such a general H belongs to T, and Q_H⊂S∩H. Both are integral surfaces of dimension two. Therefore they are the same reduced surface. The hyperplane section is generically reduced, so its degree equals deg Q_H=2. Since a hyperplane section has the same degree as S, deg S=2.

Every component of C is contained in S: its intersections with the varying general hyperplanes lie on Q_H⊂S and range over a dense subset of that component. Taking closures proves C⊂S. This completes the lemma.

## 5. Application to the HM residual lane

In the generic a=1,b=4 case, the actual HM section Z_H lies on its unique irreducible quadric. The four-dimensional space q_H·H0(O_H(1)) is contained in H0(I_Z(3)); equality follows from b=4. All hypotheses of the lemma apply to the reduced union C of 25 skew lines.

Therefore a nonzero ambient quadric vanishes on C. Multiplying it by any nonzero quadric gives a nonzero quartic vanishing on C, contradicting the established H0(I_C(4))=0. Hence generic a=1,b=4 is impossible.

Combined with the a=1,b=5 exclusion and the previously excluded a=1,b=6 endpoint, this eliminates the entire unique-quadric branch: a=0 generically. Combining with the existing a=0,b=4/5 exclusions leaves precisely a=0,b≤3 as the current residual numerical frontier. It does not prove cubic trace transversality or full Q4.

## Dependencies and verification boundary

The new lemma is proved in full above. Its only general geometric inputs are generic smoothness/differential rank in characteristic zero and Bertini for a general hyperplane section of an integral projective variety of dimension at least two. It never invokes an integral-curve lifting theorem on reducible C.

HM-specific inputs: uniqueness and irreducibility of the generic quadric, b=4, reduced transverse section of the 25 skew lines, and H0(I_C(4))=0. The preceding a=1,b=5 deduction is published in Akilleez-QA/read-em-and-weep at d0edac7da9a616efcdd99b449c1c7f91682e2529. The established a=1,b=6 endpoint is at 8e209e366d157281706bc0f83bf526c5ac46ec60, EXCLUDE-UNIQUE-QUADRIC-ENDPOINT.md.

This is a new symbolic proof, not a formal proof-assistant certificate. No source-instance coefficient, matrix, minor, numerical rank, parameter scan, local-model spike, or external write was performed.
