# Focal multiplicities and the Gauss map exclude the marked sextic carrier

## Conclusion

The generic three-cubic curve-base branch cannot have a degree-six marked integral carrier. Combined with the already established degree-six/seven dichotomy, a surviving generic a=0,b=3 branch must have the ACM degree-seven, arithmetic-genus-five carrier.

The proof first forces a hypothetical sextic carrier to be smooth of genus two. It then forces the Gauss map of its swept hypersurface to be constant along every general carrier, with value equal to the varying hyperplane H. A three-dimensional hypersurface cannot have a Gauss image containing an open subset of the four-dimensional dual projective space.

This excludes the sextic branch, not the remaining heptic branch or the full Q4 repair.

## 1. Pinned inputs and notation

The marked-carrier theorem, at 435a20fc680c7ccecc3cbfd762a3d5ae97b76299, supplies an integral D_t⊂H_t=P3 containing all 25 reduced points Z_t=C∩H_t in its smooth locus. The family is defined over a dense open T of dual P4, of dimension four, and D_t spans H_t.

Assume deg D_t=6. SEXTIC-GENUS-DEFICIENCY-BOUND.md, at d1739cf6725a5a3e42ea3a5daf3058a76bfac377, proves p_a(D_t)≤2, including nonreduced residual linkage curves. Only this genus bound from that note is used here.

MARKED-CARRIER-FOCAL-NONDOMINANCE.md, at 1dd24cf0361755b13f796d15e5eb7d855b167a63, proves that the reduced swept image is an invariant integral hypersurface W⊂P4 containing C. Write e=deg W. The same note constructs, on a general normalization f:N→D_t⊂P4, a rank-three saturated normal bundle N_f, with

deg det N_f=5d+2g−2−r,

where d=6, g is the genus of N, and r≥0 is the length of the differential's ramification divisor. It also constructs the regular characteristic map

χ:T_tT⊗O_N→N_f.

At the 25 distinct lifted marked points, χ has fiber rank at most one. Because the whole normalized family dominates W, its generic rank is now exactly two, not three. This follows from generic differential rank three for evaluation into W and the nonzero rank-one relative tangent image.

A general D_t is not contained in Sing(W): otherwise the total swept image would be contained in that proper closed subset of the integral hypersurface. Thus gradient constructions below are generically nonzero on N. W need not be smooth along C, normal, or smooth elsewhere.

## 2. The gradient map on the saturated normal bundle

Let G be an irreducible homogeneous polynomial of degree e defining W. Its gradient defines a bundle map on the smooth curve N,

f*T_P4 → f*O_P4(e).

To see this globally, pull back the Euler sequence

0→O_N→f*O_P4(1)^{⊕5}→f*T_P4→0.

The five partial derivatives G_i give a map from its middle bundle to f*O(e). Its composite with O_N is ΣX_iG_i=eG, which is zero on N. Therefore the map factors through f*T_P4.

The image sheaf is the same before and after this factorization, because the middle bundle surjects onto f*T_P4. Let J be the effective common-zero divisor on N of the five pulled-back partials, regarded as sections of f*O(e−1). At least one is nonzero. Hence the image is precisely f*O(e)(−J). In particular

j:=deg J≤(e−1)d.                                       (1)

The gradient annihilates df(T_N), because G∘f=0. It also annihilates the saturation S of this tangent image: it vanishes generically on S, and its target is torsion-free, so vanishing extends globally. Consequently it factors through N_f, with unchanged image. There is an exact sequence of vector bundles on N,

0→K→N_f→f*O(e)(−J)→0,                                (2)

where K has rank two. This is surjective onto its displayed image by definition; the smoothness of N makes the kernel locally free.

The evaluation of the entire family factors through W. Its differential is annihilated by the gradient, so χ factors through K. It has generic rank two there.

## 3. Twenty-five focal zeros force genus at least two

At each marked point, the map T_tT⊗O_N→K still has rank at most one: K is a subbundle of N_f, so its fiber injection preserves this rank statement. Every 2-by-2 minor therefore vanishes at that point. Generic rank two ensures that at least one of these maximal minors is a nonzero global section of det K. The marked points are distinct, so

25≤deg det K.                                          (3)

Taking degrees in (2),

deg det K=(5−e)d+2g−2−r+j.

Together with (1), this gives the useful general rank-two bound

25≤4d+2g−2−r.                                         (4)

For d=6, (4) reads 25≤22+2g−r. Thus g≥2. On the other hand g≤p_a(D_t)≤2. Therefore g=p_a(D_t)=2. The normalization quotient has length p_a−g=0, so D_t is normal, hence smooth as a complex curve. Its inclusion into P4 is an immersion, giving r=0.

No smoothness of the original carrier was assumed: it has been forced by the focal inequality and the independently proved arithmetic-genus bound.

## 4. The residual gradient series has degree at most one

Define the nonnegative integer

ε=(e−1)d−j.

The five partial derivatives after removing their common divisor J globally generate the line bundle

A=f*O(e−1)(−J)

of degree ε on N. The associated morphism is the extension to N of the Gauss map of W along its smooth points.

With d=6, g=2, and r=0, the exact degree formula becomes

deg det K=26−ε.

By (3), ε≤1. Thus A is globally generated of degree zero or one on the smooth genus-two curve N.

A globally generated line bundle of degree one cannot exist on a positive-genus smooth projective curve. If it has only one independent section, global generation would make that section nowhere zero, forcing degree zero. If it has at least two sections, a nonzero section has a single zero p; global generation provides a second section nonzero at p. Those two sections have no common zero and define a degree-one morphism to P1, making the curve rational. Both possibilities contradict degree one on genus two.

Therefore ε=0. A globally generated degree-zero line bundle is trivial and all its sections are constant multiples of one nowhere-zero section. The five normalized partials are consequently projectively constant. This proves that the Gauss map of W is constant along the general carrier D_t wherever W is smooth.

The common divisor J may include the marked points and may have arbitrary support elsewhere. No exclusion of singularities of W along C has been used.

## 5. Constant Gauss value is exactly H_t, giving the contradiction

Let A_t⊂P4 be this constant tangent hyperplane to W along the dense open D_t∩W_smooth. At a smooth point x of W its tangent hyperplane is Σ_iG_i(x)X_i=0. Euler's identity gives Σ_iG_i(x)x_i=eG(x)=0, so x belongs to that hyperplane. Constancy of the projective gradient therefore implies D_t⊂A_t after taking closure.

But D_t spans its given hyperplane H_t. Both A_t and H_t are hyperplanes in P4, so A_t=H_t.

For every t in a dense open of the four-dimensional hyperplane parameter space, H_t is thus a value of the Gauss map

W_smooth→(P4)*.

The closure of the image of a morphism from the three-dimensional W_smooth has dimension at most three. It cannot contain that dense open subset of the four-dimensional dual space. This is the required contradiction.

## Result and boundaries

The degree-six marked carrier is excluded, including all three arithmetic-genus possibilities 0,1,2 and all nonreduced residual linkage possibilities previously left open. The degree-seven carrier survives this argument: the corresponding rank-two bound has more degree available, so the degree-zero/one Gauss-series conclusion does not follow.

No general-position assumption on actual HM first derivatives, selected coefficients, ranks, hyperplanes, scans, local-model spike, or consumed experiment was used. The gradient is that of the hypothetical swept hypersurface, and only divisor degrees and algebraic differential identities enter. No external write was performed.
