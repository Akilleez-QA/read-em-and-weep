# Conditional transition and source-leaf bridge

## Result and scope

The quotient-resolution identities imply the frozen transition cocycle and genuine inverse, even when the inclusion images differ. They do NOT imply determinant one. Reciprocal line factors preserve the determinant. The raw engine's method named inverse is an adjugate, so its interpretation as the Source.gi inverse still requires the determinant-one normalization of the actual pinned primitive frames.

This is a conditional formal proof and static source audit. No production imports, actual model products, polynomial cross multiplication, physical source/owner/jet evaluation, or external writes were performed. The executable checker uses static text/AST/JSON metadata, free-word algebra and tiny invented matrices only; bundled production sources are inert text. No physical execution permission follows.

## 1. Quotient identification, with the necessary hypotheses visible

Work over a commutative field of characteristic zero (or a commutative localization with 2 invertible). All carrier matrices on an overlap refer to the SAME ambient complex, after any necessary ambient-frame transport. For each i assume

    Id_V = gamma H0_i + I_i P_i + H1_i delta,
    P_i I_i = Id_2,  P_i gamma = 0,  delta I_i = 0.

Assume also delta gamma=0 when identifying the cohomology quotient H=ker(delta)/im(gamma). These are consequences of the sufficient contraction systems in the earlier primitive bridge, conditional on its premises; the present proof does not independently validate actual primitive entries.

For z in ker(delta), z−I_iP_i z=gamma H0_i z. Thus [I_i] and the map induced by P_i are mutual inverses between the rank-two coefficient module and H. P_i descends because P_i gamma=0; I_i lands in ker(delta) because delta I_i=0. Different literal images of I_i need only be representatives of the same quotient.

Put T_ij=P_i I_j. Then

    T_ij T_jk
      = P_i (Id−gamma H0_j−H1_j delta) I_k
      = P_i I_k = T_ik.

Each error term vanishes separately: the first by P_i gamma=0, the second by delta I_k=0. No condition P_i H1_j=0 for different carriers is assumed or needed. T_ii=Id, hence T_ij T_ji=T_ji T_ij=Id. In particular invertibility is derived, not guessed from the diagonal PI identities. Also

    I_j−I_i T_ij = gamma H0_i I_j,

so literal equality of inclusion images is neither necessary nor generally true. The cocycle derivation itself does not use delta gamma=0; that extra hypothesis is needed only for the stated quotient interpretation.

## 2. Exact line factors and transpose order

For an owner i with carrier c_i, set n_i=nu(i), D_i=diag(n_i,n_i^-1), assuming n_i is invertible in the relevant coefficient field/localization. Frozen PhysicalModel.Dframe(i,True)=D_i^-1. Its g method returns

    g_ij = D_j (P_ci I_cj)^t D_i^-1
         = (D_i^-1 T_ij D_j)^t.

This equals the pinned JavaScript formula exactly: its left row factors are (nu_i^-1,nu_i), its right column factors (nu_j,nu_j^-1), followed by transpose. Thus column transitions G_ij=g_ij^t satisfy

    G_ij G_jk=G_ik,   g_jk g_ij=g_ik,
    g_ii=Id,         g_ji=g_ij^-1.

The physical inclusion/projection leaves are I_i D_i and D_i^-1 P_i, so their cross contraction is G_ij, while their diagonal product and reversed diagonal product give the intended quotient inclusion/projection identities. The engine explicitly notes that omitted COMMON physical nu factors cancel in j and IP; that observation does not by itself identify every omitted physical leaf individually. Geometric use still needs the stated physical-frame identification.

Because det D_i=1,

    d_ij := det g_ij = det T_ij,
    d_ii=1, d_ij d_jk=d_ik, d_ji=d_ij^-1.

These identities give a multiplicative determinant cocycle, not d_ij=1. On a connected common chart family it suffices to establish d_ri=1 for one reference carrier r and every i: the other determinant identities follow. This is a logical reduction of proof obligations, not authorization to compute even those reduced actual products.

## 3. Exact normalization premise and countermodels

The missing scalar premise is: the determinants of the ordered quotient bases [I_i(:,1)] wedge [I_i(:,2)] agree on overlaps, in the specified determinant-line trivialization. Equivalently det(P_iI_j)=1 for every pair. Triviality of the determinant bundle alone only asserts existence of a compatible volume normalization; it does not certify that these particular stored frames use it.

A full-contraction countermodel has V=K^4, gamma=e1, delta=e4^t, H0=e1^t, H1=e4, I_i=(e2,e3), P_i=(e2^t;e3^t). At j replace I_i by I_i diag(2,1), P_i by diag(1/2,1)P_i and leave the other maps fixed. Every displayed resolution, annihilation, and inverse identity still holds; det(P_i I_j)=2. Thus no contraction-only derivation can close the normalization gap. By contrast, PI=Id alone is even weaker: in V=K^4 take I_i=(e1,e2), P_i=(e1^t;e2^t), I_j=(e3,e4), P_j=(e3^t;e4^t). Both PI identities hold but P_i I_j=0. The checker executes only these invented examples and a third example with different inclusion images and a valid quotient cocycle.

The immutable historical receipt bundled here claims all 36 ordered pairs of the six stored carriers, including the auxiliary carrier. The producer, manifest, dependency pins, and exact model bytes have been bound by static inspection and hashes. See REVIEW.md for the precise denominator normalization and evidence limits. The receipt is an attributable historical claim, not an independently attested execution or a newly checked model identity. Acceptance of its mathematical claim is an additional evidence premise; this package does not replace that premise by a PASS string or a hash.

## 4. Inverse, trace-free projection, k and F

For any 2x2 g, adj(g)g=g adj(g)=det(g) Id. The frozen raw Mat.inverse returns precisely adj(g), with NO division by det(g); compiler.Circuit.inverse emits a matrix_inverse node whose metadata explicitly says source determinant one is required. Source.gi calls that inverse on the g leaf. Therefore, under Section 1 alone, the correct inverse exists and equals g_ji, but the implemented gi equals d_ij g_ji. The implementation agrees with the geometric inverse exactly when d_ij=1. Even a constant determinant other than one is insufficient for this implementation.

Mat.tf and the compiler tf implement A−tr(A)Id/2; their trace is zero for every 2x2 matrix. This particular operator requires no determinant-one hypothesis. Its being trace-free does not repair an incorrect adjugate input upstream.

Let D_a,D_b be derivations, and mu(B,A)=(D_a B D_b A−D_b B D_a A)/2. Under det(g)=1 and the exact derivative/arithmetic denotation premises,

    K(g)=mu(g^-1,g),
    Source.k = −K(g)/2,
    C_ijk = g_ik^-1 mu(g_jk,g_ij),
    Source.F = b_ijk−tr(C_ijk)/2,
    b_ijk=(15/4) q_ij,a q_jk,b.

The −1/4 in Source.k is exactly −1/2 times mu's 1/2, matching the pinned JavaScript K and Z=scalar Id−K/2. Source.F's compiler scalar shape is 1x1. This bridge identifies the leaf formulas, not the separate transgression theorem δs=F.

For clarity, put P_r=g_ij^-1 D_r g_ij and Q_r=g_ij^-1 g_jk^-1 D_r g_jk g_ij. Differentiate the cocycle and inverse identities. Then

    C=(Q_a P_b−Q_b P_a)/2,
    K(g_ij)=−[P_a,P_b]/2,
    δK=( [Q_a,P_b]−[Q_b,P_a] )/2,

where δK=K_ij+g_ij^-1 K_jk g_ij−K_ik. Jacobi's determinant derivative formula gives tr P_r=D_r(det g_ij)/det g_ij=0, and likewise tr Q_r=0. For traceless 2x2 X,Y, XY+YX=tr(XY)Id, hence

    δK=2C−tr(C)Id,     δk=−C+tr(C)Id/2.

Consequently δs=F would imply δ(sId+k)=bId−C, as in the pinned first-order source. The traceless logarithmic-derivative step needs locally constant determinant; determinant ONE is the stronger requirement actually needed by the denominator-free implementation. K itself is traceless for any invertible GL2 transition, because it is a commutator; this alone does not prove the δK identity without the trace hypotheses.

## 5. Remaining root-line and geometric premises

The code constructs nu=product_r(y_r/x_r)^m_r for legal bits m_r. Algebraically its use requires the relevant ratios to be invertible in the localized function field and the derivations to be those already established in the curve bridge. The geometric claim further requires the pinned root line N, its frames e0=1 and e1=y/x, its old square-line identification e0^2=ell0 and e1^2=(1−x^-2)ell1, and correct transport at infinity. A rational expression y/x need not be a regular invertible FUNCTION on every chart where it is used as a LINE frame; the correct assertion is about a nonvanishing local section with the appropriate trivialization. This bridge does not infer chart regularity from the rational formula or mask name.

The reciprocal D_i factors have determinant one identically and cannot normalize a nonunit determinant cocycle. Common physical root-line factors and the cohomology-frame identification must be justified geometrically, with their ambient transports. An arbitrary further GL2 re-normalization could change determinant, but would change the pinned source and cannot silently be introduced.

The JS choice nu[0]=1 is a pointwise constant frame normalization with retained nonzero derivative slots, not the identity function. Equating its jet representation to the unnormalized physical nu requires that normalization/derivative dictionary and the invariant-y stripping convention from the first-order source. No such jets are evaluated here. Neither determinant normalization nor these root-line conventions can be replaced by numeric tests or by source hashes alone.
