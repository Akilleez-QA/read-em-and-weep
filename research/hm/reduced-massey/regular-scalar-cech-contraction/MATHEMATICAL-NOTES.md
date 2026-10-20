# Verification details and exact mathematical limits

These arguments supplement [the proof](PROOF.md). They retain the signed, domain and effectivity qualifications of the statements, without adding a selected-instance conclusion.

## 1. Negative-support regularity and insertion signs

For a homogeneous Laurent monomial, membership in the localized degree-k component is exactly the containment of its negative support in the intersection index set. At k=0,-1,-2, not all five exponents can be negative, so the prescribed j exists. If its inserted coefficient is nonzero, its negative support is contained in {j} union I. Since the exponent at j is nonnegative, this implies containment in I. Thus deleting j in the output introduces no forbidden denominator.

Interpret missing coefficients as zero. Alternating insertion at the first position produces the usual sign of moving j into the increasing tuple; a repeated index is zero. These conventions are necessary and are explicitly present in the proof. Only finitely many input components and finitely many monomials per component occur, so the output remains finite. The operator is C-linear, not asserted to be S-linear.

## 2. Contraction and side conditions

At fixed monomial, expanding δ on (j,i_0,...,i_q) gives f_I and the alternating omitted-index terms with sign (-1)^(r+1). Expanding δh gives those same terms with sign (-1)^r. They cancel. This proves δh+hδ=id in positive degrees, including repeated-index cases. At top Čech degree the same alternating identity holds with the nonexistent higher component zero, since a tuple of six indices from five vertices has a repetition.

In degree zero, hδf has coefficient f_i-f_j. If negative support is nonempty then f_j=0, because j is outside that support. If negative support is empty, only the monomial 1 at weight zero remains. Its chosen j is 0 and its subtraction is precisely ιπ. At negative weights this case does not occur. Thus the stated degree-zero exception is exact.

The same monomial has the same j after insertion, so two successive insertions repeat j and give h²=0. At degree one, the constant-monomial coefficient of hf on U_0 is the repeated component f_(0,0), hence πh=0. The other side conditions follow directly. In particular this is a genuine normalized deformation retraction, rather than merely a solver on two-cocycles.

## 3. Primitive uniqueness and corrections

For a closed two-cochain z, the positive-degree identity gives δhz=z and h²z=0. For any primitive s with hs=0, applying the degree-one identity gives s=hδs=hz. This proves uniqueness with the stated normalization. Two arbitrary primitives differ by a closed one-cochain v, and v=δhv; the ambiguity is explicitly regular scalar exact.

For another regular contraction h′, w=(h-h′)z is closed. Applying the original contraction to w gives δhw=w, without needing agreement of the two degree-zero projections or requiring h′ to have the same side conditions.

Multiplication by a homogeneous polynomial is a chain map on the localized complexes. Therefore w_f=h_target(fz)-f h_source(z) is closed, and r_f=h_target(w_f) satisfies δr_f=w_f. All terms are regular and finite. The displayed linear-form formula is its particular case. These statements require both source and target weights to be in the range where the asserted contractions have been defined. They prove coherence only at the stated boundary level for closed two-cochains. No strict multiplicativity or higher coherence follows.

## 4. Trace and ordered products

For closed algebraic ordered Čech one-cochains p,q in the appropriate endomorphism twists, δ(p cup q)=0 by the DGA Leibniz rule. Trace commutes with restrictions and δ, giving a valid scalar two-cocycle.

There is no cochain-level graded trace-cyclicity identity obtained merely by swapping those ordered factors: p and q then occupy different overlaps. The proof avoids this substitution and does not infer antisymmetry of scalar inputs. Bilinearity and antisymmetry are preserved by h only when they were already identities of the scalar inputs. Likewise, the rank-two identities for differential forms cannot simply be transplanted into this ordered Čech product.

## 5. DGA zigzag and quasi-isomorphisms

The proof uses the full twist-graded endomorphism algebra and excludes finite twist truncation. In particular, a bare finite selection of twists is not automatically a DGA. The final formulation is multiplication-closed and requires no such qualification.

On Čech degree p and Dolbeault degree q, the differential δ+(-1)^p bar-partial and product sign (-1)^(qr) are compatible with the total grading. Analytification, inclusion of holomorphic sections in Dolbeault degree zero, and restriction of global forms into Čech degree zero preserve these differentials and products. The arrows therefore are DGA morphisms, not just maps of complexes.

For each twist, algebraic standard-cover intersections are affine. Analytic intersections are affine-space factors times copies of C*, hence Stein. Their coherent acyclicity gives the respective Čech cohomology computations. Proper GAGA identifies the resulting algebraic and analytic groups by the stated map. The local Dolbeault resolution and Stein acyclicity give the second quasi-isomorphism. Fineness of smooth bundle-valued form sheaves gives exactness of their augmented Čech complexes and the third quasi-isomorphism. Both Čech and Dolbeault directions are bounded here, so the indicated spectral-sequence comparisons cause no convergence problem. The infinite twist direct sum causes no coherence claim about an infinite-rank sheaf: these arguments are weightwise, and direct sums of complexes of C-vector spaces preserve quasi-isomorphisms.

## 6. Massey consequence and exact limitations

A DGA morphism takes defining systems to defining systems, and a quasi-isomorphism identifies the triple Massey sets and their usual indeterminacy. One can see equality here without constructing an inverse DGA map: once the two ordered pair classes vanish, a defining system exists in the source; its image supplies a value in the target. The cohomology isomorphism identifies the indeterminacy subspaces, and each nonempty triple product is the corresponding coset. The zigzag consequently identifies singleton products when that indeterminacy is zero.

This argument presumes that the inputs correspond under the zigzag, that the necessary pair products vanish, and that the zero-indeterminacy hypotheses and smooth formula have been established in the contextual problem. The scalar proof itself does not establish those input-specific claims. Scalar H² vanishing alone would not establish vanishing of the End-valued pair products.

An algebraic defining system, when its pair classes vanish, consists of actual finite regular localized sections by the definition of the algebraic complex. Existence gives neither an algorithm for choosing that defining system from the smooth formula nor a constructive inverse to analytification. The proof makes no algebraic construction of L_X, no elimination of algebraic End-valued primitives, no strict ordered-Čech rank-two identity, and no actual vanishing/nonvanishing conclusion for a Massey operation.
