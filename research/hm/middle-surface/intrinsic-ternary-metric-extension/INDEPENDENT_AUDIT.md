# Independent audit: intrinsic ternary metric extension

## Verdict

The proposed intrinsic extension is valid under the hypotheses below. It removes metric-graph ambiguity once the middle line and support hyperplane are regular. It does not establish regularity of the support hyperplane, nor regularity of the normalized complement at metric rank one.

## Precise hypotheses

Work over C. Let B be a reduced integral scheme of finite type, with regular subbundles U⊂H⊂V⊗O_B of ranks 1 and 4, where dim V=5. Let f:V³→J be one fixed outer-symmetric, cyclic-zero trilinear map, and assume every repeated-input map A_u:V/Cu→J is injective. Put E=H/U, rank three. On a dense open subset suppose a rank-five hyperplane K⊂Sym²E is given and the actual middle numerator on U⊗K has image in the repeated-input subbundle A_U(E). This last hypothesis follows from the established support-valued correction on the good ternary locus; it is stronger than merely saying the correction exists with values in V/U.

Normality, dimension two, properness, and generic nondegeneracy are not needed for the extension lemma itself. Generic nondegeneracy is needed only to identify the extension with the particular good metric under discussion.

## Construction and rank bound

Repeated injectivity makes A_U(E) the image of a constant-rank monomorphism U²⊗E→J⊗O_B. Thus it is a rank-three subbundle, and the quotient is locally free. Local splittings s:E→H give

    Φ:U⊗Sym²E→(J⊗O_B)/A_U(E),
    u⊗ab↦f(s(a),u,s(b)) modulo A_U(E).

If s changes by d:E→U, the numerator changes by d(a)A_u(b)+d(b)A_u(a); its quadratic-in-d term is zero since f(u,u,u)=0. Therefore Φ is intrinsic. On the dense open, Φ kills U⊗K and has rank at most one. Its 2×2 minors vanish on all B because B is reduced and integral.

## Why a zero fiber is impossible

If Φ_b=0, fix a middle generator u and splitting at b. The entire numerator factors uniquely through A_u:E_b→J. This gives v:Sym²E_b→E_b. If v(e²)∈Ce for nonzero e, cyclic symmetry implies A_e(u) is proportional to A_u(e), for independent lifts e,u. Both vectors are nonzero by repeated injectivity. Writing A_e(u)=c A_u(e), with c≠0, gives

    A_(u+t e)(e)=A_u(e)−t A_e(u).

At t=1/c this is zero although e is independent of u+t e, contradicting injectivity. Thus v is square-avoiding.

On P(E_b)=P² let Q=(E_b⊗O)/O(−1). The diagonal map v defines a section of Q(2); its vanishing is exactly v(e²)∈Ce. Since

    c(Q(2))=(1+2h)³/(1+h),
    c₂(Q(2))=7h²≠0,

this section cannot be nowhere zero. This contradiction excludes Φ_b=0. The argument applies at every geometric closed point; over a finite-type C scheme that suffices to exclude any rank-zero locus.

## Consequences and limits

The map Φ has constant rank one. Elementary local constant-rank matrix reduction gives a line subbundle I=im Φ of the quotient, a rank-five kernel U⊗K, and a surjection

    h:Sym²E→M, where M=I⊗U*.

This is the unique extension of the dense projective metric. Its kernel is locally free and commutes with base change. Pulling the regular metric to any metric graph gives the same metric, so the reduced graph closure of the dense metric map is its ordinary graph; there are no exceptional metric fibers over fixed U,H.

The construction also gives local actual supported corrections K→U⊗E everywhere, with the usual shear transition. It allows larger actual residual kernels and residual-rank drops. It does not imply that h is nondegenerate, nor that the canonical complement extends at rank-one metric points. An independently proved support-extension theorem is still required before applying this conclusion globally on a middle normalization.

The finalized proof at /research/hm/middle-surface/rank-one-metric-radical-constraint/INTRINSIC_METRIC_EXTENSION.md was subsequently read in full and agrees with this independently checked argument. Its statements and limits pass audit.
