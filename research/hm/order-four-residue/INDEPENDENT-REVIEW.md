# Independent mathematical review: order-four residue and sextic saturation

Reviewed on 2026-10-20.

Frozen proof: `PROOF.md`, SHA-256
`556ebcc8139e03b804ac9991044aac8eed5af883170d1799db78d6fb12209b3e`.

## Verdict and precise scope

PASS for the stated mathematical deductions, conditional on the explicitly cited geometric and cohomological predecessors. This is independent mathematical text review, not formal verification.

The actual upstairs collision-coefficient identity in equation (1) uses the descended forms of PR437, namely its fixed collision pair `u=t_2`, `v=t_3`, with the normalizations and coefficient identification imported there. The revised first paragraph of Section 1 now explicitly distinguishes this requirement from the arbitrary-pair scope of Sections 2–4. The latter cohomological quotients and residue constructions make sense for arbitrary nonzero globally coprime forms of degrees two and three, without identifying an arbitrary replacement pair with the fixed upstairs collision ideal.

The scope clarification was the only change from the initially reviewed bytes, whose SHA-256 was `f814b3f73670de2d2d3d46fb49421c3bf9d797c26f7c1f43f180419553c9b69c`. I checked the new paragraph and verified that replacing it by the original paragraph reconstructs exactly that prior hash. No mathematical correction remains for the claims reviewed below.

## 1. All three order-four cokernels

PR437's filtration at order four is indeed

    B(-3)K_3 + B(-4)K_2 + B(-5)K_1,
    K_3=(v,u^2), K_2=K_1=(u,v).

The first two generator twists are both `(-6,-7)`, but their syzygy twists differ: they are `-10` and `-9`, respectively. The third has generator twists `(-7,-8)` and syzygy twist `-10`. These agree with the three displayed resolutions. For the first ideal, global coprimality of `u,v` also implies coprimality of `u^2,v`; the usual two-generator complete-intersection resolution applies. Local freeness of `B` preserves exactness.

Trace self-duality of `B` and Serre duality on `P^4` send generator `H^2` at twists `-6,-7,-8` to the duals of `H^2B(1), H^2B(2), H^2B(3)`. The cited vanishings kill every generator contribution. Thus the long exact sequence identifies each quotient's `H^2` with the kernel of the corresponding `H^3` syzygy map. No vanishing of the syzygy's own `H^2` is being assumed or needed.

Dualizing these kernel sequences gives exactly:

- target `H^1B(5)`, with image `u^2H^1B(1)+vH^1B(2)`;
- target `H^1B(4)`, with image `vH^1B(1)+uH^1B(2)`;
- target `H^1B(5)`, with image `vH^1B(2)+uH^1B(3)`.

Consequently all three cokernels in equation (1) are necessary. Their assembly uses the exact finite pushforward and characteristic-zero character projection already supplied by PR437. The map from `P_5^(2,1)` onto `Q_5` follows from the containment of denominator spaces, because multiplication by `u` takes `H^1B(1)` into `H^1B(3)`. Equality of these quotients is not implied.

## 2. Residue sequences at twists minus one and minus four

I checked the cohomology chase directly, not only its dimension consequences. Write `R_1` and `R_0` for the two successive image sheaves in the evaluation resolution. At each of `t=-1,-3,-4`, its first image sequence gives

    H^1R_1(t)=H^2R_1(t)=0,
    H^3R_1(t)=D tensor H^4O(t-5).

Besides vanishing intermediate line-bundle cohomology, the latter identification uses `H^4O(t)=0`. This is valid even at the endpoint `t=-4`; there is no omitted top-cohomology term.

The primary vanishings of `H^2E(t)` and `H^3E(t)` then give

    H^1R_0(t)=V tensor H^1E(t),
    H^2R_0(t)=D tensor H^4O(t-5).

Finally `H^0(ell^2(t))=0` and `H^2B(5+t)=0` give the full exact sequence (3), including injectivity of its first arrow and surjectivity of its last arrow. The primary bundle twists are correctly `F(2), F(0), F(-1)`.

The first map is the natural cup map from the evaluation resolution. The transpose of the final boundary is restriction by PR457's dual-resolution construction; it is not inferred merely from a matching dimension. Retaining the single determinant line gives all three dual residue models in (4).

In particular, surjectivity of the boundary proves injectivity of restrictions in degrees one, three and four. The primary dimensions are `40,20,0`. The line-section dimensions are `50,100,125`, and the polynomial dimensions are `5,35,70`. The asserted dimensions `h^1B(4)=85`, `h^1B(2)=85`, and `h^1B(1)=55` follow.

Naturality supplies the induced simultaneous residue map and its transpose. The same linear section must multiply both `u` and `v`; two separately chosen sections would describe a different kernel. The exact sequence (6) retains the entire remaining primary quotient, so the residue calculation is not promoted to a computation of `Q_4`.

## 3. The sextic map and its exact kernel

The degrees in `vf-ug` are six. Changing the representative of a linear residue class by `res(h)`, with `h` a global linear form, changes `(f,g)` by `(hu,hv)` and leaves the sextic unchanged. Thus the map is well-defined.

If the sextic vanishes, global coprimality gives `f=hu`, `g=hv` with a common `h` of degree one. The syzygy freedom is the full space `S_1`, not merely constants. On any line where at least one of `u,v` is nonzero, the polynomial domain of that line forces `lambda=h`. Consequently the kernel is represented exactly by sections supported on the common-contained lines.

Those supported sections really inject into the quotient by `res(S_1)`. If a global `h` has such support, then `hu` vanishes on every component of `C`. Injectivity of cubic restriction implies `hu=0` as a polynomial, hence `h=0` because `u` is nonzero. Each common-contained line contributes two independent sections of its `O(1)`, establishing the exact `2k` kernel and the lower bound for both the residual and full cokernels.

Under the stronger avoidance assumption `C intersect V(u,v)=empty`, the restrictions of both forms to each line are nonzero and coprime. The equation `v_l f_l=u_l g_l` then gives a common quotient of degree one. Disjointness of the lines makes these quotients a section of `O_C(1)`. The global representation ambiguity is precisely the already-removed `S_1` syzygy. This proves surjectivity onto the entire sextic intersection in (10).

The distinction between avoidance and merely having no common-contained line is essential and is correctly maintained: the latter proves injectivity of the sextic map, not its surjectivity.

## 4. Sextic saturation and at least five new classes

Twisting PR458's Eagon–Northcott resolution by one gives exactly

    0 -> D tensor B(-4) -> Lambda^3V tensor F(-1)
      -> Lambda^2V tensor O(1) -> I_C(6) -> 0.

The bundle identifications used here are `E^*=F(-2)` and `Sym^2E^*=B(-5)`. For the image sheaf `K`, the cited primary vanishings and

    H^1B(-4)=H^3B(-1)^*=0

give `H^0K=0` and `H^1K=D tensor H^2B(-4)`. The second image sequence therefore produces precisely (12).

The preceding quintic theorem identifies `Lambda^2V` with all of `H^0I_C(5)`. Twisting its minors map makes the first arrow of (12) actual polynomial multiplication. Its injectivity excludes linear syzygies among those six quintics and gives a thirty-dimensional image. This does not assert that all saturated sextics are polynomial multiples of the quintics.

Restriction of degree-six polynomials to the twenty-five disjoint lines has target dimension `25 times 7=175`, while `dim S_6=210`. Its kernel therefore has dimension at least thirty-five, regardless of whether restriction is surjective. Combining this lower bound with (12) proves at least five independent classes modulo linear quintic multiples. Serre duality gives `h^2B(-4)=h^2B(-1)` as claimed.

Injectivity of degree-four restriction also excludes every nonzero ideal section in lower degree: multiplying such a section by a suitable nonzero polynomial would contradict degree-four injectivity. Thus the new sextic classes cannot be attributed to previously omitted lower-degree generators. The proof correctly does not assert the exact sextic dimension or evaluate the pair-dependent sextic intersection.

## Evidence and limitations

I inspected the frozen proof and the available local texts for PR437's exact filtration, PR167's primary resolution and positive-twist vanishings, PR451's transpose-syzygy endpoint, PR455's twist-one and `H^3B(-1)` vanishings, PR457's evaluation resolution and boundary duality, and PR458's quintic saturation argument. These establish the immediate dependency statements used above. This review does not constitute a fresh proof of every predecessor or an independent authentication of every local predecessor against its remote commit.

No selected HM/source-instance evaluation, multiplication-matrix rank computation, parameter search, generator/checker, large computation, or public write was performed. Standard symbolic cohomology chases and elementary dimension identities are the only calculations used. The fixed-pair quotient values, primary intersections, actual-source membership, pure conditions, higher lifting and algebraicity remain unresolved exactly as stated in the proof.
