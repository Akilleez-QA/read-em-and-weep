# Independent review of the source125 cc exclusion

## Verdict and frozen files

**PASS.** I found no unresolved mathematical gap in the complete exclusion at the exact bytes below. I independently read the proposed proof, inspected and executed its verifier, and checked the geometric arguments rather than treating the arithmetic output as their certification.

Audited SHA256 values:

- `PROOF.md`: `31758f74dace16b0a58426d9840c7b0dfcb4631e6e29e384508c12aa732c0347`
- `verify.py`: `353500d8b6a3d1e1090ad4b1ae9d632859950c6586b3ad6d5101c9afcf7a4acf`
- `REPRODUCE.md`: `8e817e1f55510cd4d24c14981ba54e9fc0e8f7e4c05114477a20861c5c62a3d2`

The scope is exactly original source index125, tuple `(0,0,2,0,0,0,0,1)`, for `G3.11.ea6bced3bddf`. This review does not certify a whole-label exclusion, any current frontier total, an actual source realization, or a Lean formalization.

I read the local bf and cf proof texts and compared them byte-for-byte with the cited dependency copies. I also inspected the actual-splitting and strict-top texts and the relevant saturated-image, quadratic-span and first-polar arguments in the freshly retrieved immutable PR796/PR802 copies. The dependencies are used as universal geometric lemmas, not by transferring another source's exclusion. The actual source splitting, saturation in a constant ambient bundle, characteristic-zero setting, and original determinant-defect-zero identification remain hypotheses supplied by those dependencies and the pinned catalogs.

## 1. Saturated-pair kernel exhaustion

The proposed saturated external quotient of the rank10, degree-20 top is `O(4)+O(16)`. Its kernel consequently has rank8 and degree-40. Strict-top gives `H0(K(2))=0`; the exact sequence then gives

- `H1(K(2))=A+2P+D`, of dimension16;
- `chi_G(K(3))=-W-Wp-S`.

Equivariant splitting is legitimate in characteristic zero. Every kernel atom has ordinary degree at most-3. For an atom `R O(-j)` with `j>=4`, its genuine, noncancelling contribution to `H1(K(2))` has dimension `(j-3) dim R`; thus `j<=19`. Central parity, rank, degree and nonzero Hom into the actual top give necessary filters, not unsupported realizability assertions. I checked that the fixed character calculation applies these filters to every irreducible and every degree3 through19. The eleven listed survivors and their two character columns agree with the calculation.

Only `W(-7)` contributes negatively to W, and no surviving atom contributes positively to W. Its multiplicity is therefore exactly one. It consumes all A and D, leaving only `Wp(-3)`, `T(-3)`, `P(-4)`, `Wp(-5)`. The T character forces the `T(-3)` multiplicity to vanish. The remaining equations are exactly `z+w=2` and `x-w=-1`. Nonnegativity gives precisely the two displayed kernels. Their rank and degree are respectively8 and-40; no additional rank/degree solution is being discarded.

Both kernels have zero Hom into `2V(-6)+O(-12)`. The sole degree-compatible exception would be `W(-7)->V(-6)`, but `V W=T` contains no W. Hence the actual derivative on the external kernel has zero internal image. The actual raw derivative image is therefore the saturated external pair itself. The first span has degree4, impossible for a subsheaf of a constant bundle. In particular this conclusion does not confuse a generic external quotient with a saturated one: saturation is the explicit assumption of this section, and the actual-image lemma applies.

## 2. The invariant divisor and the raw first span

Multiplication by the nonzero invariant of degree12 injects the unique V in `Sym6` into the unique V in `Sym18`, so these spaces are identified up to scale. Strict-top is injective on the two-copy V multiplicity space, hence the two independent V rows can genuinely be diagonalized into a lower-only and a high-only source summand. The degree6 V system is basepoint-free because any invariant common divisor would have degree at least12.

For a nonzero degree18 P row, its common divisor is invariant. Since G is perfect, the equation of such a divisor has trivial character; the invariant calculation through degree18 permits only the degree12 divisor of f. Dividing by it leaves the unique degree6 P system. Thus a high P row outside `f Sym6` would be basepoint-free. The two V rows give rank2 away from f, and the lower V together with that P row give rank2 on f. That would produce the forbidden saturated pair. The high P row must therefore be divisible by f, including the possibility that it is zero.

The raw external image is exactly `O(4)+O(4)`, not `O(4)+O(16)`: the lower and divided-high V rows individually surject onto the two abstract factors. Strict-top ensures the P coefficient vector in this pair is nonzero. Constant changes of basis in this *abstract equal-degree pair* and in the V multiplicity space reduce the map to the complete `Sym6` system plus the V subsystem. These changes are used to compute an abstract kernel, not as horizontal changes of the unequal-degree saturated positive pair.

The complete degree6 evaluation system has kernel `T(-3)`. The V subsystem has kernel `Wp(-5)`. One can independently recover the latter from rank2, degree-10, `H0(K(2))=0`, and `H1(K(2))=P`: a rank2 irreducible atom must be at degree-5 and only Wp has tensor product P with W; the scalar alternative `O(-4)+O(-6)` gives `1+A`, not P. Thus the combined raw external kernel is exactly the asserted one.

Its internal Hom to `2V(-6)+O(-12)` vanishes by degree. Therefore the actual raw first increment is `2O(6)` and the raw first span has rank12 and degree-8. This is an image-sheaf assertion before saturation. A nonzero saturation correction is a G-invariant finite-length quotient; its determinant divisor has positive degree at least12. The resulting saturated bundle would have degree at least4, impossible in a constant bundle. Therefore the correction is zero.

This is the decisive raw-versus-saturated check: the high factor is not replaced by `O(18)`. The full top's raw span really is already saturated, even though its raw external image is not saturated in the original positive pair.

The first-polar principle is now applicable in exactly its stated form. The saturated first span is a quotient of the first-polar source with degree-1 generators and is also a subbundle of a constant bundle; its only splitting degrees are0 and-1. The two Euler characters identify its coefficient representations as

`M=P O+(Wp+T) O(-1)`.

Its degree-zero part is the image of `H0(M)` in the original ambient H and therefore is a genuine constant P subspace, not a presumed horizontal splitting.

## 3. Actual constant projection and the constant thirteen-space

Write the actual constant P as C0 and the quotient of M by C0 as L. Since M is saturated, L is saturated in the actual constant quotient `(H/C0) O`. A generic rank4 kernel of `F->L` would put all of C0 generically inside F. Saturation of F in H then forces C0 to be contained in F as a sheaf, contradicting `H0(E)=0`. Thus the image rank is at least7.

The only V channel into L is the one-dimensional channel to T. Therefore the two-copy V source is controlled by one multiplicity functional. It cannot vanish, since otherwise the image rank is at most4. Its kernel gives a genuine direct `V_0(-2)` summand, so the image rank is at most7. Consequently it is exactly7.

Both P channels must be nonzero. Without the Wp channel the image lies in rank6 T. Without the T channel it has rank at most `3+2=5`. The surviving V channel and the two P channels are all multiplicity-one. They form a three-edge tree on the two source factors and two target factors; independent nonzero rescalings of these factors normalize all three simultaneously. Thus there is no unexamined scalar modulus obstructing identification with the usual multiplication map

`Sym6 W O(-2) -> Sym7 W O(-1)`.

All three channels of this standard map are nonzero: a zero V or P-to-Wp channel gives rank at most4 or6, and a zero P-to-T channel gives rank at most5, whereas multiplication by a nonzero tautological linear form is everywhere injective of rank7. Hence the normalized map has everywhere rank7, saturated image S0, and line quotient `O(6)`. This also upgrades the generic kernel statement to the exact saturated kernel `V_0(-2)`.

Constant projection commutes with forming the *raw* first derivative span: local sections of the image lift to sections of F, and differentiation of such lifts differs only by terms already in the projected image. Since the raw first span of F was proved to be M, the raw first span of S0 is exactly L. Both S0 and L are saturated in the actual quotient ambient bundle. No connection on an abstract complement of M is used.

The derivative of L kills S0 modulo L, so its next increment has rank at most one. It is nonzero, since the negative-degree L cannot be horizontal in a constant bundle. S0 is still a quadratic bundle in that ambient space: its embedding is the original quadratic inclusion followed by a constant projection and the genuine direct quotient of its source. Quadratic coefficients are spanned after at most two derivatives, so its second span is constant. Its rank is therefore exactly9, its quotient by L has degree8, and its constant representation is `Sym8=P+D` from the Euler character.

Taking the inverse image of this actual constant nine-space under the constant map H to H/C0 produces an actual constant thirteen-space C containing F. This conclusion does not require a horizontal splitting of the degree-1 part of M, nor does it presume saturation of any projected copy of the entire E.

## 4. The coherent tail image and the final contradiction

For the two `V(-4)` tails, the negative external row vanishes by ordinary degree; the lower positive row vanishes because `Sym8=P+D` contains no V. The high row has one-dimensional coefficient Hom because `Sym20` contains one V. A linear map from the two-copy tail multiplicity space into this one-dimensional channel therefore has a nonzero kernel, giving a genuine direct summand `J=V(-4)` with zero external derivative.

For this J, the internal derivative modulo J can land only in the top V summands. The top target after twisting by-2 is `(2V+P)(-4)`, so Schur's lemma removes P; the other tail and scalar targets are too negative. Hence, for local sections, the ambient connection satisfies `nabla(J) subset (J+F) tensor Omega1`. Since F lies in C and projection by C is constant, the coherent image I of J in `(H/C) O` is preserved by the regular connection.

The fact that I is initially only a coherent image does not create a gap. Its saturation N has zero second fundamental form, since I agrees with N generically; hence N is an actual constant subbundle. Connection preservation then eliminates the finite-length quotient N/I. Equivalently, in a local discrete valuation ring, write `det I = t^d u det N` with u a unit. The induced determinant connection preserves `det I`. If `d>0`, differentiating `t^d u` has valuation `d-1` in characteristic zero, a contradiction. Thus d=0 everywhere and I=N is itself constant. This determinant argument also covers arbitrary elementary-divisor arrangements and does not assume a horizontal diagonalization of the lattice.

The image I is center-even because it is a quotient of the center-even J. If its rank is1 or2, its constant representation is therefore trivial, and the map from J is excluded by `Hom_G(V(-4),O)=0`. If its rank is3, the image-sheaf map `J->I` is an everywhere surjective map of equal-rank vector bundles and therefore an isomorphism, contradicting degrees-12 and0. A rank-zero image is zero because it is a subsheaf of a vector bundle. These possibilities exhaust the rank bound, so J is contained in C.

Finally F and J are actual disjoint direct summands of E. Their direct sum is saturated in E and hence in H, has rank13 and degree-32, and lies in the rank13 constant C. The quotient `C/(F+J)` is torsion but injects into the torsion-free `H/(F+J)`, so it is zero. Thus `F+J=C`, contradicting its negative degree. This uses actual ambient saturation, not merely equality of generic ranks.

## 5. Verifier, reproduction, and remaining boundaries

I inspected and independently ran `python3 verify.py` against the frozen files. It completed successfully with:

    PASS: 30 fixed Hom checks; 11 complete kernel atoms, two kernels, raw-divisor/polar/tail identities, original cc source pins.
    No actual source/model evaluation, selected points, matrices, ranks, scans, or frontier counts were performed.

The code authenticates both immutable catalog inputs by their Git blob hashes before checking the original tuple, quotient pair and stable label. Its finite atom filter has the proof's independently justified complete bound, and the subsequent multiplicity solution is the stated elementary two-kernel argument. The reproduction instructions specify the same inputs and execution route.

The character arithmetic does not itself verify saturation, horizontal-image arguments, or actual constant projections; those were checked separately above. I found no missing branch or additional hypothesis needed beyond the written setup and cited universal inputs. The distinctions explicitly audited include raw versus saturated images, the degree of a saturation defect, ordinary bundle splitting versus ambient horizontality, generic versus everywhere rank, and coherent image versus saturated image. None remains an unresolved gap.

No selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance ranks, selected models, scans, or large computation were used. No external writes or publication were performed. This approval applies to the three exact frozen files above; a substantive change requires renewed review.
