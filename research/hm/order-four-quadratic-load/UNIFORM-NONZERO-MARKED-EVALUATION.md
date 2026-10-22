# Generic nonzero evaluation at all fifty marked points

## Statement

Let S be an irreducible nonempty H5-invariant open set of quadrics Q in P4. Assume every Q is smooth and transverse to the fixed twenty-five lines C_i, and lies on the checked primary-injective open, so H0(V(2))=0 for V=F|Q. Fix k∈{2,3,4}. Suppose h0(B_Q(k)) is generically a positive constant r, where B=End_0(F). Shrink S to its constant-dimension, cohomology-and-base-change locus and intersect its finitely many translates. The actual kernels then form a vector bundle K on S with fiber H0(B_Q(k)).

The actual Heisenberg action on F, up to scalar, is an input. It induces an action on B and its section family; scalar ambiguity disappears under conjugation. Preservation of the line configuration alone would not justify this action.

Let P=P_S(K), the irreducible projective family of nonzero sections up to scalar. For a general pair (Q,[ψ]) in P, the value of ψ under the actual fifty-point quotient map is nonzero at every point of Z_Q=C intersect Q. Equivalently, its eigenquotient divisor avoids all fifty evaluation base points, so every basepoint multiplicity m_z is zero.

No independence of the fifty evaluations is asserted or needed.

## 1. The actual evaluation map is injective on sections

Restrict the exterior-symmetric resolution and twist by k−5:

0→D O_Q(k−10)→Λ²U O_Q(k−5)→U V(k−2)→B_Q(k)→T_k→0,

where D=det U and T_k=ell²(k−5)|Z_Q is an invertible sheaf on the reduced fifty-point scheme. Denote by R1 and R0 the two successive images preceding B_Q(k).

Since Q is arithmetically Cohen–Macaulay, H1(R1)=0 follows from H1 of the middle line bundles and H2 of the left line bundle vanishing. Also H0(V(k−2))=0: it follows from H0(V(2))=0 by multiplication by a nonzero section of O_Q(4−k). Thus H0(R0)=0, and

H0(B_Q(k)) → H0(T_k)

is injective. This argument does not discard any H3 term and is unaffected by the corrected twist-two projected target85.

In a local frame, the quotient B_Q(k)→T_k is the value of the symmetric-square representative of ψ on the rank-one evaluation quotient ell. The eigenquotient equation is that same quadratic expression on the quotient line. Therefore its value is zero exactly when the distinguished evaluation base point belongs to the eigenquotient divisor. This is intrinsic and independent of the frame or scalar representative of ψ.

## 2. Each marked double cover remains irreducible

For a fixed line C_i, consider

Z_i={(Q,p): Q∈S, p∈C_i, q(p)=0} → S.

Before restricting the quadric parameter space, this incidence is a projective P13-bundle over C_i=P1: evaluation of all fifteen quadratic coefficients at p is a nonzero linear functional. Consequently it is irreducible. Its restriction to S is a nonempty open subset, still irreducible. Transversality makes Z_i→S finite étale of degree two.

Pulling back to P gives W_i=Z_i×_S P. This is the projective bundle P_(Z_i)(K|Z_i), hence irreducible, and W_i→P is finite étale of degree two. In particular this argument does not require choosing or globally labeling the two roots on a line.

## 3. Equivariance prevents an identically zero evaluation component

On W_i, the universal section and the quotient to T_k define a morphism between invertible sheaves. Let E_i be its zero locus. It is closed in W_i.

If E_i were all of W_i for one index i, every section on every Q in the family would evaluate to zero at both marked points of C_i. The actual H5-equivariance and transitivity on the twenty-five C-lines would imply the same assertion for every index. Each nonzero ψ would then map to zero in H0(T_k), contrary to the injection of Section 1. Therefore E_i is a proper closed subset of the irreducible W_i for every i.

Because W_i→P is finite and both spaces have the same dimension, the image of E_i is closed and has strictly smaller dimension than P. The union of these twenty-five images is still proper closed. Outside that union all fifty evaluations are nonzero. This proves the statement, and supplies a nonempty open subset of P rather than merely a claim about its generic point.

## 4. Consequences for primitive eigenquotients

For a primitive ψ, its eigenquotient divisor T is integral by the checked irreducible-characteristic-polynomial argument. It has class 2L+(k−5)H on X=P_Q(V(3)). Since it avoids all base points, the four evaluation sections restrict to a basepoint-free system on T itself. Its cube is

L³·T=30k−50.

For k≥2 this is positive. The induced morphism T→P(U*)=P3 therefore dominates and has generic degree30k−50. No finiteness over all of P3 is asserted.

Two successive general evaluation hyperplanes cut an integral Gorenstein curve, by the checked Bertini/CM argument. With all m_z=0, adjunction gives

2p_a−2=10k²+40k−130.

Thus k=2 would give p_a=−4, a contradiction. Since primitive twist one has already been excluded and every nonzero twist-two section is primitive after the lower-twist vanishings, generic twist-two nonvanishing is impossible. This supplies a generic twist-two exclusion without the earlier low-orbit or thirty-block arguments.

For primitive k=3 the general evaluation curve has genus41 and the morphism has degree40. For primitive k=4 the corresponding numbers are genus96 and degree70.

The word primitive is essential in the last paragraph: at k=4 the complete section family could have scalar-divisible sections, and integrality of their total eigenquotient divisor must not be presumed. The uniform fifty-value assertion itself holds regardless of primitivity. Whenever the generic section is primitive, the stated degree and genus conclusions apply directly; more generally they apply on any nonempty open primitive locus intersecting the established nonzero-evaluation open. At k=3, after generic vanishing of twists≤2, every nonzero section is primitive.

## Scope

The conclusion is about a general pair (Q,[ψ]) and hence a general section over a general Q. It does not claim every section on a fixed Q has all fifty values nonzero. The proof requires the actual equivariant HM bundle, the actual fifty-point resolution, and the transitivity on the twenty-five lines, but no classification of thirty exceptional blocks, no independently chosen point values, and no selected coefficient or rank experiment.

Pinned inputs: actual exterior-symmetric resolution in PR538 at d5d9bd997145b0ecf7d7bd659a19fb7845afb75f; nef twist-one exclusion at 0c497348c3935ddf4648043f988e1b172c158382; evaluation-basepoint intersection and adjunction formulas at 3c4ab4b2cdfb9e54012f92f798a8da34768413d0 and 4ea187ccf0a296b399aced6c722e1f9e9bac3763. The actual normalizer action on normalized HM and the twenty-five translated evaluation lines are stated in ADHPR, Section3, printed page9, https://arxiv.org/pdf/alg-geom/9606013 , read at the source. No equality of inequivalent ambient linear representations is inferred.
